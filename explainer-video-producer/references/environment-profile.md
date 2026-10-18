# Environment profile

This optional adapter points to existing tools and approved creator settings. It is private configuration, not a second skill and not a source of extra permissions.

## Discovery

Use a profile explicitly supplied with the job first. Otherwise check `EXPLAINER_VIDEO_PROFILE`, then `${XDG_CONFIG_HOME:-~/.config}/explainer-video-producer/profile.json`. Resolve `~` as the current user's home directory. If no profile exists, discover available capabilities and ask only for the missing choices needed by the requested stage. Planning and scripting can proceed without a GPU or avatar.

The profile can contain:

| Field | Purpose |
| --- | --- |
| `status` | `configured` or `unconfigured`; still verify live availability |
| `creator` | Display identity, when relevant to the job |
| `operator_guide` | Private guide for the existing capture/voice/avatar/render routes |
| `voice` | Method, recipe reference, approved settings, authorized source/transcript references and approval evidence |
| `avatar` | Selected engine, frozen profile, authorized source and approval evidence |
| `capture` | Configured recorder route and supported surfaces |
| `compositor` | Existing editor/render stack and its local documentation |
| `storage` | Suitable durable production directory |
| `distribution` | Canonical site/author identity, exact permitted creator accounts, configured publishing route and current policy references |
| `media_metadata` | Verified creator name, role, website and export-tag policy; kept separate from platform disclosure preferences |

References may be local file paths or protected configuration identifiers. Keep credentials in their established secret store; do not put raw tokens, keys, cookies or credential exports here. Keep this profile outside the public repository and outside public generated artifacts. Do not invent source assets or mark a profile approved because an example contains the word `approved`.

Start from [profile.example.json](../assets/profile.example.json) only if configuring a new environment. A null capability is genuinely unconfigured, not a fallback engine selection.

## Applying the profile

Inspect the relevant local recipe and current evidence. The user's latest request and accepted settings govern the job. Source paths, service addresses, resource ownership and model availability can drift; verify them before dependent operations.

A local reference to a course workflow supplies its applicable technical route, not unrelated tracker, runtime, messaging or delivery mandates. Preserve this skill's beat-driven pacing and the current brief. If a generic voice guide conflicts with a newer accepted transcript-conditioned recipe, use the documented accepted recipe.

Public installs include the workflow and local media checker. They do not install a recorder, GPU server, voice model, InfiniteTalk, publishing accounts, account credentials or a creator's face. Verify those separately. Skill-file synchronization across machines establishes file parity, not working services on each machine. A saved distribution profile identifies the route; the current request or a verified standing policy supplies the publishing scope.
