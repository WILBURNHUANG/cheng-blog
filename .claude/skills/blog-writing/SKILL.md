---
name: blog-writing
description: Write engaging blog posts on any topic. Use when user asks to write a blog post, create an article, or mentions "/blog-write [topic]". Takes a topic as argument, performs preliminary research, asks follow-up questions to gather context and materials, then writes an accessible yet informative blog post with relevant images.
---

# Blog Writing Skill

Write engaging, accessible blog posts with technical depth and visual appeal.

## Usage

```
/blog-write [topic]
```

Example: `/blog-write quantum computing basics`

## Workflow Overview

This skill follows a **3-phase workflow**:

1. **Research Phase** - Gather background information on the topic
2. **Discovery Phase** - Ask follow-up questions and request materials from user
3. **Writing Phase** - Create the blog post with images

---

## Phase 1: Research

### 1.1 Initial Topic Research

Perform web searches to understand:
- What is the topic about (basic definition/overview)
- Current state/latest developments (2025-2026)
- Key concepts, terminology, and frameworks
- Common misconceptions or debates
- Who the main players/companies/researchers are

**Search queries to use:**
```
[topic] explained 2026
[topic] latest developments
[topic] for beginners guide
[topic] key concepts overview
[topic] industry trends
```

### 1.2 Identify Knowledge Gaps

After research, identify:
- Areas that need more depth
- Angles that could make the post unique
- Technical details that would benefit from user expertise
- Potential visuals or diagrams that would help explain concepts

---

## Phase 2: Discovery

### 2.1 Ask Follow-Up Questions

Use the AskUserQuestion tool to gather context. Questions should cover:

**Content Direction:**
- What angle or perspective should the post take?
- Who is the target audience (beginners, practitioners, decision-makers)?
- What's the main takeaway you want readers to have?
- Are there specific subtopics to include or avoid?

**User's Expertise:**
- Do you have personal experience or insights to include?
- Any specific examples, case studies, or anecdotes to reference?
- What's your unique take on this topic?

**Depth & Scope:**
- How technical should it get (high-level overview vs deep dive)?
- Approximate length preference (short ~800 words, medium ~1500, long ~2500+)?

### 2.2 Request Materials

Ask if the user can provide supporting materials:

**Helpful materials include:**
- YouTube videos explaining concepts (provide URLs)
- Articles or papers for reference (provide URLs)
- Images, diagrams, or screenshots to include
- Data, statistics, or reports to cite
- Personal notes or outlines

**How to ask:**
```
Do you have any materials to help with this post?
- YouTube videos explaining [specific concept]
- Articles or blog posts for reference
- Images or diagrams to include
- Data or statistics to cite
```

### 2.3 Process Provided Materials

For YouTube videos:
- Use WebFetch to get video information and transcript highlights
- Extract key points, quotes, and explanations

For articles:
- Use WebFetch to read and summarize key sections
- Identify quotable insights and data points

For images:
- Note file paths for inclusion in the post
- Ensure images are placed in `/public/images/`

---

## Phase 3: Writing

### 3.1 Article Structure

Create MDX file at: `src/content/posts/[YYYY-MM-DD]-[slug].mdx`

See [references/article-template.md](references/article-template.md) for the full template.

**General structure:**
```markdown
---
title: "Engaging Title That Summarizes the Value"
description: "1-2 sentence hook for SEO and social sharing"
date: YYYY-MM-DD
category: "[Category]"
tags: ["tag1", "tag2", "tag3"]
hero: "/images/[hero-image].jpg"
draft: false
---

[Hook paragraph - grab attention, state the problem or opportunity]

![Descriptive alt text](/images/image1.png "Caption")

## Section 1: The Foundation
[Build understanding from basics]

## Section 2: Going Deeper
[Add technical depth without losing readers]

![Another visual](/images/image2.png "Caption")

## Section 3: Practical Applications
[Real-world examples and use cases]

## Section 4: What This Means for You
[Actionable takeaways]

---

## TL;DR
[3-5 bullet points summarizing key points]

## Sources
[List of references with links]
```

### 3.2 Writing Style Guidelines

**Tone:**
- Conversational but authoritative
- Explain like you're talking to a smart friend who's new to the topic
- Use "you" and "we" to create connection
- Avoid jargon; define technical terms when first used

**Technical Balance:**
- Include enough technical detail to be useful
- Break down complex concepts with analogies
- Use examples and real-world scenarios
- Don't assume prior knowledge unless specified

**Formatting:**
- Short paragraphs (3-4 sentences max)
- Use headers to create scannable structure
- Bold **key terms** and **important numbers**
- Use bullet lists for multiple items
- Include tables for comparisons or data

### 3.3 Image Requirements

**Every post MUST include images.** Plain text walls hurt readability.

**Image types to include:**
- Hero image (required) - set in frontmatter
- Concept diagrams (at least 1)
- Screenshots or examples (if applicable)
- Data visualizations (charts, graphs) for data-heavy posts

**Image sources:**
1. User-provided images (preferred)
2. Generate diagrams describing what should be shown
3. Reference Unsplash/Pexels for stock photos (provide search terms)

**Image placement:**
- Place images after introducing a concept, not before
- Space images evenly (roughly every 2-3 sections)
- Always include alt text and caption

**Image syntax:**
```markdown
![Alt text describing the image](/images/filename.png "Optional caption")
```

### 3.4 Categories to Use

Based on the blog's existing structure:
- "AI" - artificial intelligence, machine learning, LLMs
- "Space Tech" - GNSS, satellites, positioning, navigation
- "Tech" - general technology, software, hardware
- "Finance" - fintech, trading, markets
- "Productivity" - tools, workflows, optimization
- "Tutorial" - how-to guides, step-by-step instructions

### 3.5 SEO & Discoverability

- Title: Include primary keyword, under 60 characters
- Description: Hook with value proposition, under 160 characters
- Tags: 3-7 relevant tags, mix of broad and specific

---

## Quality Checklist

Before finalizing, verify:

- [ ] Hook paragraph grabs attention
- [ ] Technical concepts are explained clearly
- [ ] At least 2-3 images included (hero + inline)
- [ ] Headers create logical flow
- [ ] Bold used for key terms and numbers
- [ ] TL;DR section summarizes key points
- [ ] Sources cited where applicable
- [ ] No walls of text (paragraphs under 4 sentences)
- [ ] Reads conversationally, not like a textbook

---

## Commit (if requested)

Use commit message format:
```
feat: add blog post on [topic]
```
