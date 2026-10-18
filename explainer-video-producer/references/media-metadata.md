# File metadata, attribution and platform labels

Use for creator tags, unnecessary export metadata, or a platform's “Made with AI” label. Diagnose the actual layer before changing anything.

## Three separate layers

| Layer | Examples | What a change affects |
| --- | --- | --- |
| Embedded file metadata | Title, artist/author, description, copyright, language, encoder | The exported file and tools that read those fields |
| Platform publishing settings | An AI-media disclosure flag, audience, caption or visibility | The native post, subject to that platform's rules and edit capabilities |
| Search-facing content | Page title, visible author bio, transcript, canonical URL, Article/Person/VideoObject data | The information available for crawling and attribution |

An encoder such as FFmpeg, Lavf or libx264 is not an AI-generator label. X's `made_with_ai` parameter is a post-level publishing field, separate from its media attachment. A badge can therefore appear even when no AI tag is present in the inspected file metadata.

Inspect the actual submitted settings and provider response as well as the media. Do not diagnose a platform label from its wording alone. A failed automated fetch or incomplete tag inspection should remain a stated limit.

## Creator metadata

Use a small allowlist drawn from the current brief or verified creator profile:

- A specific title matching the content.
- The creator's actual name in the format's author/artist field.
- A concise, accurate description.
- A verified website/source URL and professional role, when useful.
- Copyright ownership only when established.
- Correct language information for the relevant track.

Use platform-standard supported fields. For example, an MP4 can carry title, artist, description and a concise comment containing the creator's role and website. A PNG can use named textual attribution fields. Arbitrary keyword lists, repeated job titles and invented credentials are not an SEO strategy. Never insert a false camera identity, fake creation history, “human-made” claim or unsupported qualification.

Keep a private provenance record even when producing a minimal public export. Preserve essential codec/container information and useful accessibility, language, subtitle and chapter data. Remove incidental software/path tags selectively; do not erase functional information merely to make the metadata inventory empty.

## Make a safe new export

Inspect first, for example:

```bash
ffprobe -v error -show_entries format_tags:stream_tags -of json input.mp4
```

Preserve the original and write a distinct output. For MP4/MOV, prefer stream-copy remuxing when only descriptive metadata changes; re-encoding the creator's face or voice is unnecessary. FFmpeg's `-map_metadata -1` controls global input metadata, while per-stream metadata needs separate handling. The muxer can add its own encoder tag; inspect the output instead of assuming an empty `encoder` argument removed it. Preserve or restore legitimate track language and other functional tags deliberately.

Verify the resulting fields, file validity, stream count, codecs, duration and timing. For a metadata-only copy, compare compressed packet payloads and timing per stream; for an image, compare decoded pixels. Save input/output hashes and the actual removed/added fields. A tag-cleaning operation does not establish that pixel/audio watermarks, vendor detection or all unknown provenance mechanisms are gone.

## Optional and required disclosure

Respect the creator's choice for genuinely optional publishing flags. Do not automatically enable an AI flag merely because an AI tool helped with writing, coding, editing or file export. If applicable platform policy requires a disclosure for the actual content, retain it. An API parameter being optional does not itself prove that every use of the platform makes disclosure optional.

Keep each provider's rules separate. Changing an optional X preference is not an instruction to disable a required TikTok disclosure. Use accurate wording and recorded evidence without misrepresenting how a real person's image or voice was used.

For an existing post, inspect its actual editing capabilities and time limits. Rewriting a local file cannot retroactively change a native post flag. If the available route cannot edit the field, report that directly. Do not delete and repost an existing release merely to remove a label unless the user authorizes that consequential change; it can change the URL and lose engagement, and it may not prevent a platform from applying its own label.

## SEO/GEO boundary

Accurate embedded tags help file attribution and organization. Keep the main discovery work in the accessible article, useful title/description, complete transcript, stable author identity and truthful structured data described in [blog-seo-geo.md](blog-seo-geo.md). Neither creator tags nor removing an encoder string guarantees indexing, rankings or AI citations.

Current provider behavior must be rechecked when needed. Reference: [X Create Post fields](https://docs.x.com/x-api/posts/create-post).
