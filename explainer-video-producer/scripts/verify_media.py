#!/usr/bin/env python3
"""Check local narrated media; technical checks do not establish content approval."""

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be positive and finite")
    return number


def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def sha_argument(value):
    if not re.fullmatch(r"[a-fA-F0-9]{64}", value):
        raise argparse.ArgumentTypeError("must be a 64-character SHA-256 digest")
    return value.lower()


def number(value):
    try:
        result = float(Fraction(str(value)))
        return result if math.isfinite(result) else None
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(command, timeout):
    result = subprocess.run(command, stdin=subprocess.DEVNULL, capture_output=True,
                            text=True, timeout=timeout)
    # Both tools run at error verbosity: reported errors fail even with exit 0.
    if result.returncode or result.stderr.strip():
        raise RuntimeError(result.stderr.strip()[-1500:] or
                           f"Media command exited {result.returncode}")
    return result.stdout


def inspect(args):
    path = args.media.expanduser().resolve()
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "failed",
        "scope": "technical_only_content_review_pending",
        "input": {"path": str(path)},
        "checks": {"decode": {"performed": False, "passed": None}},
        "pending": ["av_alignment_review", "voice_content_review", "visual_review",
                    "owner_approval", "delivery_verification"],
        "issues": [],
    }
    try:
        if not path.is_file():
            raise ValueError("Input must be an existing regular local file")
        ffprobe, ffmpeg = shutil.which("ffprobe"), shutil.which("ffmpeg")
        if not ffprobe or not ffmpeg:
            raise RuntimeError("FFprobe and FFmpeg must be installed on PATH")
        initial_hash = sha256(path)
        report["input"].update(sha256=initial_hash, bytes=path.stat().st_size)
        if args.expected_sha256 is not None:
            matches = initial_hash == args.expected_sha256
            report["checks"]["expected_sha256"] = {"expected": args.expected_sha256,
                                                    "passed": matches}
            if not matches:
                report["issues"].append("Input SHA-256 differs from the expected digest")
        # Restrict nested references too; a local playlist must not fetch a URL.
        probe = json.loads(run([ffprobe, "-v", "error", "-protocol_whitelist", "file,pipe",
                                "-show_streams", "-show_format", "-of", "json", str(path)],
                               args.timeout))
        streams = probe.get("streams", [])
        videos = [s for s in streams if s.get("codec_type") == "video"
                  and not s.get("disposition", {}).get("attached_pic")]
        audios = [s for s in streams if s.get("codec_type") == "audio"]
        if not videos or not audios:
            raise ValueError("Narrated media requires a video stream and an audio stream")
        video = videos[0]
        fps = number(video.get("avg_frame_rate"))
        duration = number(probe.get("format", {}).get("duration"))
        if fps is None or fps <= 0 or duration is None or duration <= 0:
            raise ValueError("Media must have a positive measured duration and frame rate")
        report["media"] = {
            "duration_seconds": duration,
            "width": video.get("width"), "height": video.get("height"), "fps": fps,
            "video": {k: video.get(k) for k in ("index", "start_time", "duration", "nb_frames")},
            "audio": [{k: s.get(k) for k in ("index", "start_time", "duration", "sample_rate", "channels")}
                      for s in audios],
        }
        for key in ("width", "height", "fps"):
            expected = getattr(args, key)
            if expected is not None:
                actual = report["media"][key]
                passed = actual is not None and math.isclose(actual, expected, rel_tol=1e-6, abs_tol=1e-6)
                report["checks"][key] = {"actual": actual, "expected": expected, "passed": passed}
                if not passed:
                    report["issues"].append(f"{key} differs from the requested value")
        if args.expected_duration is not None:
            tolerance = 1 / fps
            durations = {"container": duration, "video": number(video.get("duration")),
                         **{f"audio_{s['index']}": number(s.get("duration")) for s in audios}}
            passed = all(value is not None and value > 0 and
                         abs(value - args.expected_duration) <= tolerance + 1e-9
                         for value in durations.values())
            report["checks"]["duration"] = {
                "expected_seconds": args.expected_duration, "actual_seconds": durations,
                "tolerance_seconds": tolerance, "tolerance_rule": "one measured video frame",
                "passed": passed,
            }
            if not passed:
                report["issues"].append("Container or stream duration is unavailable or outside one video frame of the requested duration")
        report["checks"]["decode"]["performed"] = True
        decoded = run([ffmpeg, "-v", "error", "-xerror", "-nostdin", "-nostats",
                       "-threads", "2", "-protocol_whitelist", "file,pipe", "-i", str(path),
                       "-map", f"0:{video['index']}", "-map", "0:a", "-progress", "pipe:1",
                       "-f", "null", "-"], args.timeout)
        counts = [int(line.partition("=")[2]) for line in decoded.splitlines()
                  if line.startswith("frame=")]
        if not counts or counts[-1] <= 0:
            raise ValueError("Full decode produced no video frames")
        report["checks"]["decode"].update(passed=True, frames=counts[-1])
        if args.expected_frames is not None:
            passed = counts[-1] == args.expected_frames
            report["checks"]["frames"] = {"actual": counts[-1], "expected": args.expected_frames,
                                            "passed": passed}
            if not passed:
                report["issues"].append("Decoded frame count differs from the requested value")
        unchanged = initial_hash == sha256(path)
        report["checks"]["source_unchanged"] = unchanged
        if not unchanged:
            report["issues"].append("Input changed during verification")
        if not report["issues"]:
            report["status"] = "technical_only_content_review_pending"
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        report["issues"].append(str(error))
        if report["checks"]["decode"]["performed"] and report["checks"]["decode"]["passed"] is None:
            report["checks"]["decode"]["passed"] = False
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path, help="existing local narrated media file")
    parser.add_argument("--expected-duration", type=positive, help="seconds; every stream must match within one measured video frame")
    parser.add_argument("--width", type=positive_int)
    parser.add_argument("--height", type=positive_int)
    parser.add_argument("--fps", type=positive)
    parser.add_argument("--expected-frames", type=positive_int)
    parser.add_argument("--expected-sha256", type=sha_argument)
    parser.add_argument("--timeout", type=positive, default=1800, help="per-command timeout in seconds")
    parser.add_argument("--output", type=Path, help="optional JSON report; stdout always receives JSON")
    args = parser.parse_args()
    if args.output:
        args.output = args.output.expanduser()
        source = args.media.expanduser()
        aliases = args.output.resolve() == source.resolve()
        if args.output.exists() and source.exists():
            aliases = aliases or args.output.samefile(source)
        if aliases:
            parser.error("Report output must not overwrite input media")
    report = inspect(args)
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
        except OSError as error:
            report["status"] = "failed"
            report["issues"].append(f"Cannot save report: {error}")
    print(json.dumps(report, indent=2, allow_nan=False))
    return 2 if report["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
