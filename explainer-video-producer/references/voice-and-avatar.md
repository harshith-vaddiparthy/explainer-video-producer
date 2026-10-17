# Approved voice and avatar production

Read for voice cloning, lip synchronization or a presenter overlay. Use the creator's authorized recordings and current approved profile. The public package contains no personal face or voice assets, model weights, credentials or GPU service.

## Voice before lips

Establish the selected voice, reference audio and transcript, generation method and relevant settings from current evidence. A newer accepted recipe takes precedence over an older generic helper. Keep source file hashes and a dated approval reference in the private job.

For a new or materially changed voice, generate a representative passage with normal sentence endings and relevant terminology. Let the creator assess the sound. Reuse an approval already supplied for the unchanged recipe. For existing accepted audio, retain the media rather than regenerating it to reconfirm the same preference.

Generate narration at the agreed natural pace. Check names, numbers, acronyms, pronunciation and missing or invented words. Automatic transcription helps locate defects; it does not replace listening. Repair the affected passage, preserve accepted passages and record the splice.

Estimate timing while scripting; commit timing from the accepted audio. Keep intentional pauses tied to a visual or teaching purpose. Preserve an unmodified narration master for the lip driver, with sample rate, exact sample count and hash. A separate delivery mix may adjust level or true peak; record that processing and verify that it introduced no time shift or speed change.

## Approve a moving avatar profile

Use the selected avatar engine and approved generation quality. A small overlay does not justify reducing model input/output resolution: generate at the accepted quality and scale the finished picture for layout.

For a new profile, compare a moving sample with its source and listen to the complete spoken passage. Include open and closed mouth shapes, pauses and normal head movement. Look for identity drift, doubled teeth or lips, soft or swollen mouth geometry, glasses/face distortions and implausible motion. Pixel similarity outside a mask cannot prove a natural face.

Record the model and workflow versions, checkpoint identifiers or hashes, source geometry, sampler, steps, guidance, seed and other consequential settings. Preserve the accepted profile during the full render. A faster model, lower resolution, mouth mask or beautifier is a profile change, not an incidental optimization.

### InfiniteTalk reference

The motivating production used an approved 720×1280, 25 fps InfiniteTalk profile. Its private recipe also froze the workflow, model files and sampler settings. That result is evidence for preserving a creator-approved profile, not a guarantee that those dimensions or settings fit another creator or installation. Locate the actual configured workflow before running it; this skill does not ship or install InfiniteTalk.

## Plan joins before a long render

Chunked synthesis can reset head pose, hands and framing even when the same settings are used. Review several representative joins early, at the final card size and with sound, before committing to a long batch. A good first sentence proves neither later source positions nor seamless joins.

Use continuous source mapping where supported. Choose boundaries at appropriate pauses and compatible poses; check source length and end-of-file behavior. Render fresh lip motion for each distinct audio interval. If an engine needs context overlap, record the overlap, the exact selected output range and how it maps to the narration.

For a visible reset, first evaluate a nearby clean cut or a planned explanatory cutaway with continuous narration. If the whole-time presenter is required, retain the face and explain the unresolved tradeoff rather than silently hiding it. Avoid face-morph transitions or blended double faces to conceal a bad boundary. Repair only affected material within the approved scope.

## Reliable long jobs

Use the current environment's resource claims and one owner for each shared renderer. Before launch or resume, inspect active workers and existing outputs. A process name or remembered address alone does not establish ownership.

Freeze the plan, accepted master and generation profile before submission. Save request IDs and uncertain-submission state durably. If a response is lost, reconcile the queue/history before submitting again. Use timeouts appropriate to measured full-quality jobs; an elapsed timer alone does not prove that an active job failed.

For every segment, retain:

- Source media hash and selected source time/frame range.
- Exact narration master sample range and any documented conditioning derivative.
- Workflow/profile identity and remote job ID.
- Generated output, selected frame range, final frame count and hashes.
- Completion, decode, transfer and sampled review results.

Use cumulative boundaries, for example `round(time_seconds × fps)`, so the joined track has the intended total frame count. Treat audio sample mapping and video frame mapping separately. Explicitly account for tiny codec rounding at an edge; never use it to hide a substantive shortfall.

Copy accepted outputs to durable storage and verify the copy before declaring a checkpoint complete. Completion of the track requires every expected segment, correct order and total duration, full decode and source/audio bindings. Release the owned resource after finishing without stopping unrelated services.

Technical alignment establishes where the driver belongs; it does not prove perceptually accurate lips. Review the final encoded overlay with the final mix, including starts, ends, joins and more than one voiced interval.
