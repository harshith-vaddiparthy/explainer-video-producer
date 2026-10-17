# Pacing and Script

Use this reference when planning or revising the explanation, narration, or visual
sequence. The finished lesson should make a useful promise, explain why it
matters, demonstrate the necessary work, and leave the viewer able to interpret
the result.

## Start with the viewer's question

Before writing narration, record:

- The topic and the specific audience, including what they already know.
- The task they should be able to perform or the concept they should understand.
- Why that outcome matters in an ordinary working situation.
- The real example, starting state, and visible result that can prove the lesson.
- The requested scope and whether runtime is approximate or exact.

Turn these into a plain opening promise. Name the topic and its practical value
early enough that the first demonstration has context. Show a brief preview of
the outcome when it helps the viewer understand the destination.

An opening does not need dramatic stakes. A concrete problem and useful result
are enough. Ground claims in inspected sources or observed behavior; label sample
data and hypothetical examples. Personal anecdotes, measurements, and product
capabilities require evidence.

Planning is ready when the viewer's question, promised outcome, and demonstration
all describe the same lesson.

## Build a progression that can be followed

Outline the explanation before polishing sentences. Put prerequisite concepts
and actions before the steps that depend on them. Distinguish the instructions
needed to reproduce a result from optional background or independent tips.

Use these teaching functions where they help:

| Function | What the viewer needs |
| --- | --- |
| Orient | Where we are, what we are trying to do, and why this part matters. |
| Explain | The smallest mental model needed to understand the next action. |
| Demonstrate | A visible action or worked example that makes the explanation concrete. |
| Interpret | What changed, what the result means, and how to tell whether it worked. |
| Recap | The useful conclusion and any next action that follows from it. |

These are functions, not mandatory separate scenes or a fixed sequence repeated
in every section. A short sentence can orient and explain together. A diagram
can interpret a result after a demonstration. Revisit a concept when a new case
needs it, rather than repeating the entire introduction.

Connect steps through their actual purpose: “Now that we have selected the open
requests, we can check what will be included in the export.” A transition should
resolve the previous action and make the next one understandable.

Keep the number of beats proportional to the topic. A beat is one meaningful
unit of explanation or action, not a fixed duration or a required scene count.

## Write narration and visuals together

For each beat, record the learner's question, spoken passage, visual purpose,
screen state or diagram, cursor action if relevant, and observable result.
Add measured timing once the approved voice track exists.

Choose the visual that answers the question:

- Use a real screen recording when the viewer needs to see where an action
  happens, how the interface responds, or what output was produced.
- Use a supplementary diagram when a relationship, sequence, or hidden mechanism
  is difficult to understand from the interface alone.
- Use the approved avatar when its presence helps introduce, bridge, or conclude
  the explanation. Keep important controls and evidence readable around it.
- Keep the current view when it still serves the explanation. Change views when
  the learning task changes or a clearer view is needed.

Choose media by teaching purpose. Do not impose screen, diagram, or avatar
percentages, novelty scores, or recurring visual-change and rehook timers.

Make speech, screen, pointer, and annotations agree. Identify the relevant
control before clicking it; let the visible cursor guide attention; then show
and explain the resulting state. Read the actual interface labels into the
script where they help someone follow along.

If the recording differs from the plan, resolve the mismatch in the script or
recording. A narration claim that an action succeeded needs the corresponding
visible result or other appropriate evidence. Supplementary graphics should
explain the demonstration without passing an invented interface off as footage.

## Measure the pace

Use a word-count estimate only during drafting. Once narration is approved,
measure the actual audio and align beats to its spoken phrases and pauses.
Check those timings against real clicks, typing, loading, and reading time.

A viewer may need more time to inspect a result than the narrator needs to name
it. Hold the relevant view long enough to read it, simplify the displayed
material, or add a useful interpretation. Give intricate operations room;
move quickly through familiar actions that do not need further explanation.

If speech outruns the demonstration, shorten or split the passage, add a natural
pause, or revise the action sequence. If the video drags, remove repetition and
unnecessary setup. Use cuts only where the remaining sequence stays truthful and
understandable. Extra explanation should answer a real question, not fill time.

Treat an explicitly exact runtime as a delivery constraint: record the target,
fit the substantive content to it, and verify the final rendered duration.
Otherwise use the requested length as an approximate planning guide. An example
that previously ran six minutes does not set the duration for future topics.

When narration changes after approval, regenerate the affected voice passage
through the approved route and recheck dependent screen, diagram, and avatar
timings. The written script's estimate is not the final runtime evidence.

## Example: give an app action a reason

This example uses a hypothetical support-request table. Replace its labels and
behavior with the inspected application before producing a real lesson.

**Cold jump into the app:**

> “Click Filter. Choose Open. Now click Export and download the CSV.”

The clicks are named, but the viewer has no reason to perform them and no check
that the export contains the intended records.

**Useful opening:**

> “We need a list of unresolved support requests for the weekly handoff. This
> table also contains closed requests, so we will first select the open ones,
> export that view, and check the downloaded file.”

**Useful transition after filtering:**

> “The table now shows the open requests. Before exporting, check the status
> column so we know the view matches our handoff. Next, we will confirm that the
> downloaded file contains the same records.”

The explanation establishes purpose, follows the task's dependencies, and makes
verification part of the result. It does not assume that exporting a filtered
view behaves correctly before the application and output have been inspected.

## Example beat sheet

These rows illustrate choices, not a required number of beats. Timing is filled
from the approved audio and the actual recording.

| Learner question | Spoken intent | Visual and reason | Action and result |
| --- | --- | --- | --- |
| What are we making? | Explain the weekly handoff and show the intended output. | Brief real output preview: establishes a concrete destination. | Show a verified sample and return to the starting table. |
| Which records belong? | Define the open-request condition. | Small diagram of all requests, selection, and export: makes inclusion clear if the distinction needs explanation. | Reveal the selected subset; return to the app for the action. |
| How do I select them? | Name the actual filter control and chosen condition. | Real screen recording: the location and interface response matter. | Visible cursor selects the condition; show and inspect the resulting rows. |
| Did the export work? | Compare the output with the intended selection. | Real downloaded file beside the relevant source evidence: supports the conclusion. | Check relevant records and fields; state what was verified. |
| What should I remember? | Summarize selection, export, and verification. | Keep the result visible or use the approved avatar if it helps the closing explanation. | Give a concise takeaway and a relevant next step, if needed. |

## Review before production and after rendering

- Does the opening identify the topic, useful outcome, and reason to care?
- Can a viewer follow the prerequisite order without an unexplained jump?
- Does each section answer a question or show a meaningful result?
- Do spoken instructions match the actual labels, pointer target, and app state?
- Can the viewer read the evidence while hearing its interpretation?
- Are factual claims, examples, and conclusions supported and clearly framed?
- Does the conclusion fulfill the opening promise before offering any next step?
- Has the final audio and render been checked against the requested duration?

Listen to the complete narration, then watch the assembled video. A script can
read well while its recording moves too quickly or displays a different state.
Resolve those mismatches before calling the lesson complete.

## Source

This guide uses original wording and adapts selected planning and editing ideas
from [YouTube Script Writing in Skill Stack at revision d607d66198b250b12c8e05c6d265ddb73d871aa5](https://github.com/cdeistopened/skill-stack/blob/d607d66198b250b12c8e05c6d265ddb73d871aa5/.claude/skills/youtube-scriptwriting/SKILL.md).
See the bundled [third-party notices](../THIRD_PARTY_NOTICES.md) for the upstream
license and attribution. The production and verification guidance here is part
of this skill; the upstream writing reference does not supply that pipeline.
