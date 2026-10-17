# Explainer Video Producer

An agent skill by [Harshith Vaddiparthy](https://harshith.com) for producing educational videos with a clear explanation, genuine software demonstrations, deliberate pacing and an optional approved presenter avatar.

The video opens with its subject, practical relevance and intended outcome. Each section builds the understanding needed for the next. Screen recordings prove actions and results; diagrams explain relationships; the presenter helps orient and connect the story. **There is no fixed screen-to-diagram ratio.**

## Install

```bash
npx skills add https://github.com/harshith-vaddiparthy/explainer-video-producer --skill explainer-video-producer
```

Or copy the `explainer-video-producer/` directory into your agent's supported skill directory.

## Use

```text
Use $explainer-video-producer to make an approximately six-minute explainer
about AI harnesses for someone who has used chatbots but never an agent.
Introduce what a harness does and why it matters, then show a real workflow
and explain the result. Use my configured voice and avatar. Choose visuals
and timing for comprehension; don't force a screen/diagram percentage.
```

It also supports a script or storyboard on its own, revisions to an existing film, reference-video analysis, and resuming interrupted production. The current request determines the scope.

## Included

- A compact [production workflow](explainer-video-producer/SKILL.md).
- [Script and pacing guidance](explainer-video-producer/references/pacing-and-script.md) with an opening, transitions, prerequisite order and section payoffs.
- Genuine recording, cursor timing and composition guidance.
- Approved voice/avatar continuity, recoverable long renders and join review.
- A private environment profile adapter and reusable brief/beat sheet.
- A local FFmpeg/FFprobe media checker, with tests. Its pass means technical checks passed, not that teaching or lip sync was approved.

This is an agent workflow, not a bundled video generation service. Recording and production require an available recorder/editor and a configured voice route. Avatar work additionally requires authorized reference media and a working avatar engine. The skill can use an existing InfiniteTalk setup but does not install models or provide GPU compute, personal assets or credentials. The media checker requires Python 3 and FFmpeg/FFprobe.

Configuration stays outside the repository. See [environment-profile.md](explainer-video-producer/references/environment-profile.md). Existing creator approvals are retained; a new profile is evaluated with a moving sample before a long render.

## Development checks

```bash
python3 -m unittest discover -s tests -v
python3 explainer-video-producer/scripts/verify_media.py --help
```

The workflow was extracted from a completed six-minute screen-plus-avatar production. The new pacing guidance removes the earlier visual allocation rule. Its writing behavior is tested with independent planning scenarios; that is not a claim that another full film has already been rendered with this release.

## Attribution and license

Script planning adapts ideas from [`youtube-scriptwriting` in cdeistopened/skill-stack](https://github.com/cdeistopened/skill-stack/tree/d607d66198b250b12c8e05c6d265ddb73d871aa5/.claude/skills/youtube-scriptwriting), with original teaching-focused wording. The upstream source supplies writing guidance, not this project's screen capture, voice or avatar infrastructure. See the [retained MIT notice and pinned source](explainer-video-producer/THIRD_PARTY_NOTICES.md).

This project is released under the [MIT License](LICENSE). Creator media and model licenses are separate from the skill's license.
