"""Exercise the CLI with tiny synthetic media; no personal footage or model runs."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "explainer-video-producer/scripts/verify_media.py"


class VerifyMediaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            raise unittest.SkipTest("FFmpeg and FFprobe are required")
        cls.temporary = tempfile.TemporaryDirectory(prefix="explainer-media-test-")
        cls.root = Path(cls.temporary.name)
        cls.valid = cls.root / "sample 'quoted' name.mp4"
        cls.silent = cls.root / "silent.mp4"
        for path, with_audio in ((cls.valid, True), (cls.silent, False)):
            command = ["ffmpeg", "-v", "error", "-nostdin", "-f", "lavfi", "-i",
                       "color=c=blue:size=96x64:rate=10:duration=1"]
            if with_audio:
                command += ["-f", "lavfi", "-i", "sine=frequency=440:sample_rate=16000:duration=1",
                            "-c:a", "aac"]
            command += ["-c:v", "mpeg4", "-q:v", "5", "-t", "1", "-movflags", "+faststart", str(path)]
            subprocess.run(command, check=True, capture_output=True, timeout=30)
        cls.truncated = cls.root / "truncated.mp4"
        data = cls.valid.read_bytes()
        cls.truncated.write_bytes(data[:len(data) // 2])
        cls.digest = hashlib.sha256(data).hexdigest()

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def run_check(self, path=None, *options):
        result = subprocess.run([sys.executable, str(SCRIPT), str(path or self.valid),
                                 "--timeout", "30", *options], capture_output=True, text=True, timeout=40)
        return result, json.loads(result.stdout) if result.stdout else None

    def test_valid_and_report(self):
        output = self.root / "report.json"
        result, report = self.run_check(None, "--expected-duration", "1", "--width", "96",
                                        "--height", "64", "--fps", "10", "--expected-frames", "10",
                                        "--expected-sha256", self.digest, "--output", str(output))
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertEqual(report["status"], "technical_only_content_review_pending")
        self.assertEqual(report["scope"], "technical_only_content_review_pending")
        self.assertEqual(report["input"]["sha256"], self.digest)
        self.assertTrue(report["checks"]["source_unchanged"])
        self.assertEqual(report["checks"]["decode"], {"performed": True, "passed": True, "frames": 10})
        self.assertAlmostEqual(report["checks"]["duration"]["tolerance_seconds"], 0.1)
        self.assertEqual(json.loads(output.read_text()), report)

    def test_one_frame_tolerance(self):
        result, report = self.run_check(None, "--expected-duration", "1.09")
        self.assertEqual(result.returncode, 0, report)
        result, report = self.run_check(None, "--expected-duration", "1.11")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["checks"]["duration"]["passed"])

    def test_wrong_expectations(self):
        for options in (("--expected-duration", "2"), ("--width", "100"),
                        ("--height", "80"), ("--fps", "20"), ("--expected-frames", "20"),
                        ("--expected-sha256", "0" * 64)):
            with self.subTest(options=options):
                result, report = self.run_check(None, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(report["status"], "failed")
                self.assertTrue(report["issues"])

    def test_missing_audio(self):
        result, report = self.run_check(self.silent)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("audio stream", " ".join(report["issues"]))

    def test_truncated_and_missing_file(self):
        for path in (self.truncated, self.root / "missing.mp4"):
            with self.subTest(path=path):
                result, report = self.run_check(path)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(report["status"], "failed")
                self.assertTrue(report["issues"])

    def test_invalid_values_are_not_defaults(self):
        for option, values in (("--expected-duration", ("nan", "inf", "0", "-1")),
                               ("--fps", ("nan", "inf", "0", "-1")),
                               ("--width", ("0", "-1", "1.5"))):
            for value in values:
                with self.subTest(option=option, value=value):
                    result, _ = self.run_check(None, option, value)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("error:", result.stderr)

    def test_report_cannot_overwrite_media_or_hardlink(self):
        alias = self.root / "alias.mp4"
        alias.hardlink_to(self.valid)
        for output in (self.valid, alias):
            result, _ = self.run_check(None, "--output", str(output))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must not overwrite", result.stderr)
            self.assertEqual(hashlib.sha256(self.valid.read_bytes()).hexdigest(), self.digest)


if __name__ == "__main__":
    unittest.main()
