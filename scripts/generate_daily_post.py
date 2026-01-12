#!/usr/bin/env python3
"""
Daily Tech & GNSS News Blog Post Generator

This script uses the Anthropic Claude API to generate a daily news digest
blog post combining tech news and GNSS industry news.

Environment variables required:
- ANTHROPIC_API_KEY: Your Anthropic API key

Usage:
    python generate_daily_post.py

    # Or with custom output directory
    python generate_daily_post.py --output-dir /path/to/posts
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


SYSTEM_PROMPT = """You are a professional tech and GNSS industry analyst who writes daily news digest blog posts.

Your task is to generate a daily news digest blog post in MDX format with two main sections:
1. Tech News - covering AI, semiconductors, big tech, startups, and regulations
2. GNSS News - covering RTK, PPP, multi-constellation, autonomous vehicles, agriculture, and surveying

Writing Guidelines:
- Write in analytical blog style, not news wire format
- Lead each section with the most impactful story
- Include business context: why this matters, who's affected
- Keep each news item to 2-3 paragraphs max
- Use H3 subheadings for individual stories within each section
- Maintain professional but accessible tone
- Focus on business-impacting stories

You have web search capability to find today's news."""

USER_PROMPT_TEMPLATE = """Please generate today's daily tech and GNSS news digest blog post.

Today's date is: {date}
Formatted date for title: {formatted_date}

Search for and include:

**Tech News Sources** (Bloomberg Technology focus):
- AI developments and major announcements
- Semiconductor industry news
- Big tech earnings and strategic moves
- Startup funding and acquisitions
- Regulatory developments

**GNSS News Sources** (Inside GNSS, GPS World focus):
- RTK and PPP developments
- Multi-constellation updates
- Autonomous vehicle positioning
- Agriculture and surveying applications
- New products and partnerships
- Spectrum policy updates

Output the complete MDX file with this exact structure:

```mdx
---
title: "Daily Tech & GNSS News Digest - {formatted_date}"
description: "Today's top business-impacting stories from tech and GNSS industries: [brief 1-line summary]"
date: {date}
category: "News Digest"
tags: ["Tech News", "GNSS", "Daily Digest", ...add relevant topic tags]
hero: "/images/daily-digest.svg"
draft: false
---

[Opening paragraph: 2-3 sentences summarizing the day's most significant developments]

## Tech News

### [Most Important Story Headline]

[2-3 paragraphs with business analysis]

### [Second Story Headline]

[2-3 paragraphs]

### [Third Story Headline]

[1-2 paragraphs]

---

## GNSS News

### [Most Important GNSS Story Headline]

[2-3 paragraphs with industry analysis]

### [Second GNSS Story Headline]

[2-3 paragraphs]

---

## Key Takeaways

- [Most actionable insight from tech news]
- [Most actionable insight from GNSS news]
- [Cross-sector implications or trends]
```

Generate the complete blog post now, searching for today's actual news stories."""


def generate_daily_post(output_dir: Path) -> str:
    """Generate daily blog post using Claude API with web search."""

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    client = anthropic.Anthropic(api_key=api_key)

    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    formatted_date = today.strftime("%B %d, %Y")

    user_prompt = USER_PROMPT_TEMPLATE.format(
        date=date_str,
        formatted_date=formatted_date
    )

    print(f"Generating daily post for {formatted_date}...")

    # Use Claude with web search tool
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 10
        }],
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    # Extract the text content from response
    content = ""
    for block in response.content:
        if hasattr(block, 'text'):
            content += block.text

    # Extract just the MDX content (between ```mdx and ```)
    if "```mdx" in content:
        start = content.find("```mdx") + 6
        end = content.find("```", start)
        if end > start:
            content = content[start:end].strip()
    elif "---" in content:
        # Content might already be raw MDX
        pass

    # Write to file
    filename = f"{date_str}-daily-tech-gnss-news.mdx"
    output_path = output_dir / filename

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully generated: {output_path}")
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate daily tech & GNSS news blog post"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent / "src" / "content" / "posts",
        help="Directory to save the generated post"
    )

    args = parser.parse_args()

    # Ensure output directory exists
    args.output_dir.mkdir(parents=True, exist_ok=True)

    try:
        output_path = generate_daily_post(args.output_dir)
        print(f"\nBlog post generated successfully!")
        print(f"Output: {output_path}")
    except Exception as e:
        print(f"Error generating post: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
