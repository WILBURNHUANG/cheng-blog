---
name: pnt-pulse-newsletter
description: >-
  Publish the monthly "PNT Pulse" PNT Industry Observation newsletter as an MDX blog post in the
  Newsletter column of cheng-blog. Use when the user asks to "do this month's PNT Pulse", "write the
  monthly PNT newsletter", "GNSS/PNT market newsletter", "monthly market digest", or names a single
  highlight to refresh. Pairs the bundled EUSPA market knowledge base with live web-news search and
  writes in Cheng's concise, friendly, first-person voice, then publishes to the blog with a hero
  thumbnail and in-body images.
---

# PNT Pulse — Monthly Newsletter (blog-publishing skill)

This skill produces the monthly **PNT Pulse** newsletter and publishes it as an MDX post in the
**Newsletter** column of cheng-blog. It is the blog-integrated wrapper around the general
`gnss-market-newsletter` skill: use that skill's knowledge base for the *content*, and the
conventions below for the *publishing*.

## Knowledge base (read what you need)
The market fundamentals, highlight anchors, key players, and the news-source search playbook live in
the bundled `gnss-market-newsletter` skill. Read these first — do not re-derive market numbers:
- `gnss-market-newsletter/references/market-fundamentals.md` — **read first** (sizing, 15 segments, PNT/EO concepts, Galileo/EGNOS, value chains, drivers).
- `gnss-market-newsletter/references/highlight-automotive.md`, `highlight-space-defense.md`, `highlight-cross-segment.md`.
- `gnss-market-newsletter/references/key-players.md`, `news-sources.md`.
- `gnss-market-newsletter/assets/newsletter-template.md` — section structure.

## Voice (non-negotiable)
Concise, friendly, slightly funny, first-person ("I'm watching…"), short paragraphs, real technical
detail, minimal fluff — explaining the month to a sharp friend over coffee. Every item delivers a
"so what," not just "X announced Y." Match the existing first issue,
`src/content/posts/2026-06-06-pnt-pulse-june-2026.mdx`, as the reference for tone and structure.

## Hard rules (always apply)
- **Never mention "Tesla"** anywhere in the newsletter — not in the body, the title, or the frontmatter `description`. Cover robotaxi / autonomy trends through the general end-to-end "large driving models" shift and other operators instead. (A source URL that happens to contain the word in its slug is fine; just no visible mention.)
- **The intro paragraph must not name EUSPA** or any specific report. Keep the opening framing general and reader-focused (what PNT Pulse is, the method, the running order). EUSPA remains the factual backbone — still cite it in the body `> **Anchor:**` blockquotes and the closing note, just not in the intro.
- **Don't call any issue "the first issue"** or number the issues; refer to them by month.
- **Citations go at the end, not inline.** In the body, mark each source with a superscript number (`<sup>1</sup>`, or `<sup>1,2</sup>` for multiple) right after the sentence punctuation — never an inline `[label](url)` link. Collect all sources in a numbered `## References` section just before the closing italic footer, each as `1. [Publisher — short title](url)`. The footer should say sources are numbered in the References above.

## Standard intro (reuse, lightly varied each month)
Open with a short paragraph that says what PNT Pulse is (a monthly read on where PNT is actually heading), the three-step method (gather the month's most consequential GNSS/PNT/EO news → place each story against the wider market and value chain → draw out the "so what"), and the fixed running order (automotive & AI navigation → space LEO-PNT & defense PNT → rotating roundup of every other sector). Do not mention EUSPA here.

## Workflow

### 1. Set the window
Confirm the issue month and news window (default: last ~30 days; ~45 for the first issue or a quiet
month). Use today's real date so searches use the right year/month.

### 2. Load anchors, then gather news (search-driven)
Read `market-fundamentals.md` and skim the relevant highlight references. Then run **2–4 separate,
targeted searches per highlight** (never one combined query) per `news-sources.md`. Aim for ~8–16
searches total. Fetch promising sources to confirm specifics and **numbers** before citing — vendor
forecasts and contract values are routinely misreported (e.g. an early result claimed Xona's AFRL
award was "$4.6 billion"; it is **$4.65M**). Verify suspicious figures with a second search.

### 3. Map before you write
For each candidate item answer internally: which highlight/segment? which value-chain stage? which
key player(s)? which market driver? any Galileo/EGNOS/Copernicus (EU) angle? Drop items that don't
map to anything meaningful — that mapping is what makes it insight.

### 4. Read recent issues to avoid repetition
List existing newsletter posts (`src/content/posts/*-pnt-pulse-*.mdx`) and skim the last 1–2 so you
don't recycle the same stories. Rotate Highlight 3's sectors across issues.

### 5. Create images
Each issue reuses the standing hero thumbnail and adds images as needed.
- **Hero / thumbnail:** reuse `/images/pnt-pulse/hero.svg` (the standing PNT Pulse brand thumbnail).
  Only design a new one if the user wants a fresh look. Heroes are **1200×630 SVG**, dark palette:
  bg `#050A19`, surface `#0A1530`, accent `#5CE1FF`, muted `#9DB4D8`, text `#F1F5FF`, indigo `#818CF8`.
- **In-body diagrams:** create new SVGs under `public/images/pnt-pulse/` (e.g. a concept diagram for
  the month's biggest theme). Reference EUSPA market charts already in `public/images/`
  (`GNSS_Revenue.png`, `GNSS_Segment.png`, `GNSS_Value_Chain.png`, `GNSS_Demand.png`) for anchors.
- Embed in-body images with plain `<img src="/images/..." style="width:100%;border-radius:12px;margin:1.5rem 0;" />`
  plus a centered `#9DB4D8` caption paragraph. Do **not** `import` `astro:assets`.

### 6. Write the MDX post
File: `src/content/posts/{YYYY-MM-DD}-pnt-pulse-{month}-{year}.mdx` (e.g. `2026-06-06-pnt-pulse-june-2026.mdx`).

Frontmatter (exact shape — `category` MUST be `"Newsletter"` so it lands in the PNT Pulse column):
```yaml
---
title: "PNT Pulse — {Month Year}: {short hook}"
description: "{1–2 sentence skimmable summary with the month's biggest story.}"
date: {YYYY-MM-DD}
category: "Newsletter"
tags: ["PNT Pulse", "Newsletter", "GNSS", "PNT", ...topical tags]
hero: "/images/pnt-pulse/hero.svg"
draft: false
---
```

Body structure (from the template, in Cheng's voice):
- One-paragraph intro + a **60-second version** bold lead with one memorable number.
- `## 🚗 Automotive, AI & End-to-End Navigation` — 2–4 items; weave autonomy-stack framing. Include a short "Who else is moving" roundup (2-4 sentences) covering the past month's developments from the major AV / robotaxi players beyond any single brand — e.g. Waymo, Zoox, Waabi, Pony.ai, WeRide, Baidu Apollo Go, and relevant OEMs — kept brief, ending on the PNT "so what" (multi-constellation reach + integrity as fleets expand geographically). Never name Tesla.
- `## 🛰️ Space (LEO-PNT) & Defense PNT` — 2–4 items; flag the "LEO flipped to PNT source" narrative; label third-party market sizes.
- `## 🌍 Across the Rest of the Map` — rotating roundup, one tight paragraph per sector that had news.
- `## 📈 Number of the month` and `## 🔭 What I'm watching next month`.
- Use `> **Anchor:**` blockquotes to tie sections back to EUSPA facts.
- Link sources **inline** (markdown links). Bold key figures.

### 7. Quality pass
- EUSPA figures labelled as EUSPA; analyst forecasts labelled third-party with the "estimates vary" caveat; no single vendor forecast as settled fact.
- Paraphrase; short quotes only (<15 words), one per source, attributed.
- Balance the three highlights unless the month genuinely warrants otherwise.
- Confirm `category: "Newsletter"`, the hero path resolves, and any `<img>` paths exist in `public/images/`.

### 8. Build & deliver
Run `npm run build` (or `npx astro check`) to confirm the post compiles, then present the MDX file
and any new images. The post appears at `/newsletter` (nav label "PNT Pulse") and `/posts/{slug}`.

## When the user asks for less
- "Just refresh Highlight 2" → run only that highlight's searches + section.
- "Email/short version" → 60-second summary + one item per highlight.
- Single-sector deep dive → use the relevant `highlight-*` reference and go deeper.
