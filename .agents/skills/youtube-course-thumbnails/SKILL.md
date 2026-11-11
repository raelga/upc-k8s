---
name: youtube-course-thumbnails
description: Create consistent YouTube thumbnails for the UPC School Platform Engineering with Kubernetes course, using the established Session 1 and 2 designs as brand references.
metadata:
  short-description: Create consistent course thumbnails
---

# UPC School course thumbnails

Create a new thumbnail for each course video while keeping the visual identity established by the Session 1 and Session 2 examples. Use this skill for thumbnail concepts, creation, and revisions for this course.

## Reference designs

Before designing, inspect the original images in the repository's [2026 assets folder](../../../2026/assets/) and use them as the actual visual template, not merely as inspiration. Resolve all links below relative to this `SKILL.md`:

- [Session 1 / Fundamentals](../../../2026/assets/thumbnails/youtube-session01-thumbnail.png)
- [Session 2 / Cloud, Infrastructure as Code](../../../2026/assets/thumbnails/youtube-session02-thumbnail.png)
- [Course banner](../../../2026/assets/branding/course-banner.png) — supporting brand reference
- [Session 3 / AWS](../../../2026/assets/thumbnails/youtube-session03-thumbnail.png) — example of the approved orange AWS panel, not a replacement for the original templates

Inspect the Session 1 and 2 originals directly before designing. Do not reconstruct the template from memory or from an unapproved later thumbnail.

Treat elements shared by both thumbnails as the brand system. Preserve the navy left panel with the PE monogram, turquoise blocks, cream central panel, typography, layout, spacing, UPC School identity, and course-year treatment. Sample the actual images for their appearance and placement. Treat session number, topic label, headline, subtitle, and the topic-specific right panel as variable content. If the references differ, prefer the shared treatment; adapt a treatment only when it clearly belongs to one topic. Adapt the right panel to the session's cloud provider: use orange for AWS, blue for Azure, and green for GCP. Use a topic-appropriate illustration while preserving the panel's placement and the rest of the original template. For sessions without one of these providers, choose a fitting color and illustration consistent with the course identity.

For revisions to an approved design, change only the requested part and preserve everything else, unless the user explicitly asks for broader changes.

## Make each thumbnail

1. Inspect the video, its title, and available slides or course material. Identify the specific idea the session teaches; do not infer details that are not present in the source.
2. Write a short, accurate headline in the video's language. Keep the wording concise enough to read at small size. Add a supporting phrase only when it clarifies the topic. Give the session's main idea priority over a laboratory example such as WordPress.
3. Follow the references' visual hierarchy and sampled brand tokens. Keep the UPC School identity and course-year treatment consistent. Use topic imagery that explains the session and does not compete with the headline.
4. Keep important text and logos comfortably inside the canvas; avoid placing them near edges or over busy imagery.
5. Export a high-quality 16:9 PNG or JPEG at 3840 × 2160 px. YouTube recommends this resolution and aspect ratio for video thumbnails; use a smaller 16:9 size only when the requested destination or design tool requires it. Keep the file below the applicable upload limit. See [YouTube thumbnail size and resolution guidance](https://support.google.com/youtube/answer/72431).
6. Review the export at actual size and as a small preview (about 320 × 180 px). Check that the headline is legible, contrast is strong, the subject is clear, all text is correct, and the logo and text are not clipped. Correct any issue before delivering.

Use precise technical wording grounded in the session material. Distinguish work actually completed from future steps or ideas. Avoid unnecessary terminology such as “fleet”, and do not repeat the same concept in both the headline and the diagram.

For Session 3, the agreed wording was “DE EC2 A AUTO SCALING” with “STATELESS · RDS · S3 · AMIs” as the supporting line. This is an example for that session, not a fixed title or subtitle for future sessions.

## Deliverable

Use a predictable filename such as `youtube-session03-thumbnail.png`. Return the finished image and briefly note the headline and any meaningful departure from the reference system. Do not upload or replace a YouTube thumbnail unless the user explicitly asks for that action.
