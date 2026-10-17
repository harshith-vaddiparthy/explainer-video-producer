# Companion article, metadata and discovery

Read when the job includes an owned-site article, public transcript, video metadata or SEO/GEO. Aim to make the work easy to understand, retrieve and attribute. Crawl access, indexing, ranking and citation by an AI system are different outcomes; none is guaranteed by schema or frequent reposting.

## Establish the canonical source

Inspect the actual site's content model, publication/deployment route, current published version and related articles. Use the existing canonical host and author identity. Check for a substantial existing article with the same purpose before creating a duplicate.

Update an existing article when the new video serves the same intent. Create a new article when it teaches a distinct task or adds substantial original evidence, and link the related guide as the next step. Keep publication dates truthful and update modification dates only for real changes.

Use the existing public video ID and URL. Verify the title, creator, runtime, public status and available upload-date precision from actual publication evidence. A scheduler's requested time is not necessarily the platform's native publication timestamp. An existing post should not be deleted or duplicated to work around a metadata-edit limitation.

## Write an article worth reading without the video

Build the article around the question the video answers:

- A direct explanation near the top, with the intended reader and practical relevance.
- The key concepts and prerequisite order, using descriptive headings.
- The real worked example, including inputs, important decisions, observable outputs and verification.
- What the demonstration establishes and what it does not establish.
- A useful conclusion, source links and an appropriate next step.

Use exact numbers and claims only when the source supports them. Label fictional data, authored illustrations and AI-generated presenter/voice where relevant. Do not turn private business motivations into public announcements or add unsupported credentials, clients, funding, outcomes or endorsements.

Place the video prominently enough to be useful, with a descriptive accessible iframe/player title and responsive dimensions. Retain an ordinary link to the original video. Check the actual rendered placement and player availability where the permitted tools allow it; markup alone does not prove playback or native embeddability.

## Transcript and captions

Use the accepted spoken media and its timestamped transcript, not a discarded draft. Correct transcription errors without silently changing the meaning. Keep a clean reading transcript and a timed SRT/VTT when available. Label edited summaries separately from the transcript.

Expose the useful transcript as ordinary accessible page text, with descriptive chapter headings and meaningful timestamps. A transcript hidden behind registration, an image, or a client-only interaction is not equivalent to immediately available article text. Preserve unrelated access restrictions; enable public access explicitly for the intended article rather than silently ungating a whole archive.

Offer useful text/caption downloads with clear topic-and-language filenames, such as `agent-harness-explained.en.vtt`. Keep production paths, prompts, job IDs, keys and raw coordination logs out of these exports. Chapter and caption times must stay within the actual video duration and refer to the correct version.

Upload corrected captions or update existing video metadata only through an available authorized route. If the scheduler cannot edit a published description or upload a subtitle track, record that limitation. Publishing a transcript on the site does not mean a subtitle track was installed on YouTube.

## Page and video metadata

Use natural, specific titles and descriptions that match the demonstrated idea. Optimize for a clear reader question, not a keyword/entity quota. Give each clip its own title and explanation; avoid merely numbering otherwise identical metadata.

Check:

- One correct canonical URL, descriptive HTML title and meta description.
- Visible byline linked to the creator's established author/about page.
- Stable `Person` identity and relevant verified `sameAs` profile links. Reuse an existing entity ID rather than fragmenting it across host variants.
- Accurate `Article` or `BlogPosting` properties: headline, description, author, main page, publication and modification dates, image and truthful access status.
- Matching Open Graph/social preview metadata and an accessible representative image with useful alt text.
- A `VideoObject` only when its required facts and representative crawlable thumbnail are known. Use the actual name, description, upload date at verified precision, duration, thumbnail URL and embed URL. Link it to the article/page consistently.

`contentUrl` means the actual publicly accessible video bytes URL. A watch page, local filesystem path, private storage address or embed page is not a media content URL. Use `embedUrl` for the player and omit unknown optional values. Never invent views, ratings, precise timestamps or unavailable thumbnails to fill a schema template.

Use chapter `Clip` data only when the named ranges really exist and timestamps work. Timestamp syntax or structured data can establish eligibility, not guaranteed rich results. Do not claim a video-rich-result entitlement when the page is primarily an article with a supplementary video.

## Crawl and retrieval checks

Verify the deployed page, not just source files:

1. The canonical URL returns the intended successful response; redirects, real 404s and MIME types behave correctly.
2. The primary article and transcript are available in the public HTML/rendered output without an unintended login gate or `noindex`.
3. Canonical, robots directives and structured data agree with the visible content and access policy.
4. Relevant sitemap/feed entries and contextual internal links include the canonical article. Update a maintained video sitemap when the site actually supports one and its fields can be verified.
5. The thumbnail and public transcript assets load with appropriate content types. A signed/private URL is not a durable public asset.
6. Intended search/AI retrieval crawlers can reach the page under the creator's policy. Distinguish retrieval and model-training crawlers rather than changing every bot permission automatically.

An `llms.txt` file can be an optional maintained navigation aid; it is not a substitute for readable HTML, an authoritative sitemap, accurate content or verified crawl access. No special “AI schema” or keyword stuffing is required for Google AI features beyond applicable search requirements.

If authorized search-console inspection is available, record the actual submission/inspection result and timestamp. Report “published and crawlable,” “submitted,” “indexed,” and “observed in an AI answer” only when each has its own evidence. Preserve the environment's service-specific access rules instead of switching to an unapproved API or browser route.

## Syndication

Publish and verify the owned-site article first. A DEV syndication can use its canonical URL and an embedded existing YouTube video, with platform-appropriate formatting. Keep the original article's core content when asserting that canonical relationship. A substantially different article should link to its sources without pretending to be an identical canonical copy.

Add a stable author attribution and relevant source links. Use only verified profile identities; distributing more copies does not itself prove expertise or fundraising readiness.

## Primary references

Recheck current requirements when implementing:

- [Google video SEO](https://developers.google.com/search/docs/appearance/video)
- [Google VideoObject guidance](https://developers.google.com/search/docs/appearance/structured-data/video)
- [Google Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Google AI features and website guidance](https://developers.google.com/search/docs/appearance/ai-features)
- [Google canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Schema.org VideoObject](https://schema.org/VideoObject)
