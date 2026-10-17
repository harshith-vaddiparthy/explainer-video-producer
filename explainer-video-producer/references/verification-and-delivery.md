# Verification and delivery

Check the selected final encode. A good script, accepted voice sample, renderer exit code or source-frame preview is not a finished-video review.

## Technical pass

Run the included local checker using the expectations from the current brief:

```bash
python3 scripts/verify_media.py ./final.mp4 --output ./verification.json
```

Supply `--expected-duration`, `--width`, `--height`, `--fps` and `--expected-frames` when the brief specifies them; run `--help` for details. An exact duration is checked against container and stream durations within one measured video frame. Approximate briefs need a reasoned pacing assessment rather than a fabricated exact-duration requirement. Require a full decode, both video and narration audio, valid timing, and no unintended stream or frame loss. Save the checker result and final file hash in the job.

Where the environment supports them, inspect loudness, true peak, start/end truncation and audio lag against the accepted master. State which checks actually ran. A normalized delivery mix need not be byte-identical to the raw lip driver; its timing must stay aligned.

## Teaching and pace

Review the whole narration/script and the actual video at its important transitions. Ask:

- Does the opening say what this is about, who it helps and what the viewer will gain?
- Does every new concept have enough context before the viewer needs it?
- Does each section answer a useful question, then establish the next one?
- Can the viewer see the named control, action, intermediate state and result when the narration refers to them?
- Are unfamiliar terms, diagrams and outputs visible long enough to understand?
- Does a long section develop the idea, rather than repeat it or disguise waiting?
- Does the closing resolve the promise and leave a useful takeaway or justified next action?

Judge pace by comprehension and progress. The relative amount of screen footage, diagrams or presenter time is not a pass/fail metric.

## Picture, privacy and avatar review

Inspect encoded frames at the beginning and end, each chapter/scene transition, important action, reading hold, and avatar segment boundary. Include short sequences around high-risk joins, not just one still. Review the actual overlay size, text legibility, cursor targets, pop-ups, unrelated histories, sensitive data and any subtitles the brief requests or excludes.

Watch motion with audio when the available player permits it. Inspect face identity and mouth/teeth behavior, pose continuity, audible word-to-mouth timing and silence behavior. Matching timestamps or driver hashes do not certify perceptual lip sync. If only sampled frame sequences were possible, record that limitation and leave perceptual playback approval to the user.

For large jobs, build bounded contact sheets and short excerpts tied to the exact final hash. Keep review notes outside chat context. If an image limit is reached, resume with a compact handoff and selected evidence in a fresh review context; preserve the existing render and job owner.

Record the review scope, actual timestamps/frames examined, findings, repairs and unresolved issues. A visible pose reset is an editing defect or tradeoff to report, not proof of a corrupt file. Do not call a visibly cut avatar seamless.

## Completion states

Keep these separate:

| State | Evidence |
| --- | --- |
| Script ready | Coherent progression, factual grounding, recordable beats and pacing review |
| Media rendered | A real output file with selected inputs and render provenance |
| Technical checks passed | Selected file passes decode, streams and brief-specific timing checks |
| Ready for user review | Technical pass plus recorded content/visual review and disclosed limitations |
| User accepted | Actual approval covering this final version and relevant scope |
| Published | Separately authorized destination and readback of the correct uploaded version |

For an authorized full production request, keep working through a ready-for-review movie. An intermediate chapter, silent background cut or successful upload response is not that result. A selected original-quality sample is approval of that profile, not a claim that the user watched the entire final film.

Deliver a playable video preview when supported and a usable download link. If the native panel only queues the request, do not claim it opened or played; provide the supported inline preview and describe any actual limitation. State the runtime, material remaining defects and verification scope concisely. Keep raw scripts, approval records, personal reference media, credentials and job logs private unless sharing them is part of the request.

When publication is requested, prepare the exact destination and content, execute within the user's authorization, and verify the remote version. Do not silently add a public upload as a workaround for a local preview problem.
