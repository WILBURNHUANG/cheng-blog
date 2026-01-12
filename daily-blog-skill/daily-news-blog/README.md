# Daily News Blog Generator

Automated daily blog post generator for technology and GNSS industry news.

## Overview

This project generates daily news digest blog posts combining top business-impacting stories from:
- **Tech News**: Bloomberg Technology (AI, semiconductors, big tech, startups, regulations)
- **GNSS News**: Inside GNSS and GPS World (RTK, PPP, autonomous vehicles, agriculture, surveying)

## Project Structure

```
daily-news-blog/
├── .claude/
│   └── skills/
│       └── daily-blog-post/    # Blog generation skill
├── posts/                       # Generated blog posts (MDX format)
├── images/
│   └── daily-digest.jpg        # Hero image for posts
└── README.md
```

## Usage

To generate a daily blog post, simply say:

```
Daily blog post
```

This will:
1. Search Bloomberg Technology for today's top tech news
2. Search Inside GNSS and GPS World for GNSS industry news
3. Filter for stories with business impact
4. Generate a formatted MDX blog post
5. Save to `posts/YYYY-MM-DD-daily-tech-gnss-news.mdx`

## Output Format

Each blog post is an MDX file with:

- **YAML Frontmatter**: Title, description, date, category, tags, hero image
- **Opening Paragraph**: Summary of the day's key developments
- **Tech News Section**: 3-4 stories with business analysis
- **GNSS News Section**: 2-3 industry stories
- **Key Takeaways**: Actionable insights from both sectors

### File Naming Convention

Posts are saved as: `YYYY-MM-DD-daily-tech-gnss-news.mdx`

Example: `2026-01-12-daily-tech-gnss-news.mdx`

## News Sources

### Technology
- **Bloomberg Technology** - Focus on AI, semiconductors, big tech earnings, startup funding, regulatory moves
- Prioritize stories with clear business implications

### GNSS Industry
- **Inside GNSS** (insidegnss.com) - RTK, PPP, multi-constellation, precision positioning
- **GPS World** (gpsworld.com) - Products, partnerships, spectrum policy, accuracy improvements
- Focus on autonomous vehicles, agriculture, surveying, defense applications

## Writing Style

- Analytical blog style (not news wire format)
- Lead each section with most impactful story
- Include business context: why it matters, who's affected
- 2-3 paragraphs per major story
- Professional but accessible tone

## Skill Configuration

The blog generation workflow is defined in `.claude/skills/daily-blog-post/SKILL.md`

Template structure: `.claude/skills/daily-blog-post/references/output-template.md`
