---
name: daily-blog-post
description: Generate a daily tech and GNSS news blog post in MDX format. Triggers on "Daily blog post" or similar requests for daily news digest. Gathers today's business-impacting news from Bloomberg Technology, Inside GNSS, and GPS World, then outputs a professionally formatted markdown file with Tech and GNSS sections.
---

# Daily Blog Post Generator

Generate a daily news digest blog post with two sections: general Tech news and GNSS industry news.

## Workflow

1. **Search for today's tech news** from Bloomberg Technology
2. **Search for today's GNSS news** from Inside GNSS and GPS World
3. **Filter for business impact** — prioritize news affecting markets, industry trends, partnerships, product launches, regulations
4. **Write the blog post** following the output template in `references/output-template.md`
5. **Save as MDX file** with today's date in filename: `YYYY-MM-DD-daily-tech-gnss-news.mdx`

## Source Guidelines

### Tech News (Bloomberg Technology)
- Search: `Bloomberg Technology news today` or `Bloomberg tech [current date]`
- Focus: AI, semiconductors, big tech earnings, startup funding, regulatory moves
- Prioritize stories with clear business implications

### GNSS News (Inside GNSS + GPS World)
- Search: `site:insidegnss.com [current date]` and `site:gpsworld.com [current date]`
- Focus: RTK, PPP, multi-constellation, autonomous vehicles, agriculture, surveying, defense
- Prioritize: new products, partnerships, spectrum policy, accuracy improvements

## Writing Guidelines

- Write in analytical blog style, not news wire format
- Lead each section with the most impactful story
- Include business context: why this matters, who's affected
- Keep each news item to 2-3 paragraphs max
- Use subheadings within each section for individual stories
- Maintain professional but accessible tone

## Output Format

Follow the exact template structure in `references/output-template.md`:
- YAML frontmatter with title, description, date, category, tags
- Two main sections: `## Tech News` and `## GNSS News`
- Each story as H3 subheading within its section
