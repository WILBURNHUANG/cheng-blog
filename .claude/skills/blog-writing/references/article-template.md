# Blog Article Template

## MDX Frontmatter

```yaml
---
title: "Engaging Title - Include Main Keyword"
description: "1-2 sentence summary that hooks readers and includes key terms for SEO."
date: YYYY-MM-DD
category: "Category"
tags: ["Primary Tag", "Secondary Tag", "Related Tag"]
hero: "/images/hero-image.jpg"
draft: false
---
```

### Category Options
- "AI" - artificial intelligence, machine learning, LLMs, agents
- "Space Tech" - GNSS, satellites, positioning, navigation
- "Tech" - general technology, software, hardware
- "Finance" - fintech, trading, markets
- "Productivity" - tools, workflows, optimization
- "Tutorial" - how-to guides, step-by-step instructions
- "News Digest" - reserved for daily news posts

---

## Article Structure

```markdown
[Opening Hook - 2-3 sentences that grab attention]

[Problem/opportunity statement - why should reader care?]

![Relevant visual](/images/topic-overview.png "Caption explaining the image")

[Transition to what the article will cover]

## What Is [Topic]?

[Clear, jargon-free explanation of the core concept]

[Analogy or real-world comparison to make it relatable]

[Why it matters - connect to reader's world]

## How It Works

[Break down the mechanics/process]

![Diagram or visualization](/images/how-it-works.png "Process diagram")

[Technical details explained accessibly]

**Key components:**
- **Component 1**: Brief explanation
- **Component 2**: Brief explanation
- **Component 3**: Brief explanation

## Real-World Applications

### Example 1: [Use Case Name]

[Describe how this applies in practice]

[Specific numbers, outcomes, or case study details]

### Example 2: [Use Case Name]

[Another practical application]

## The Challenges / What to Watch Out For

[Balanced view - acknowledge limitations or concerns]

[What the industry/community is doing about it]

## What This Means for You

[Practical takeaways for the reader]

**If you're [audience type 1]:**
- Action or consideration

**If you're [audience type 2]:**
- Action or consideration

---

## TL;DR

- **Key point 1**: One sentence summary
- **Key point 2**: One sentence summary
- **Key point 3**: One sentence summary

---

## Sources

- **[Source Name]** — *[Publication/Report Title]*. [Brief note on what it covers]
- [Link to source if available]
```

---

## Writing Style Examples

### Good Opening Hooks

**Problem-focused:**
> "Every day, 2 million developers hit the same wall: their code works locally but breaks in production. Here's what's actually happening—and how to fix it."

**Surprising stat:**
> "By 2033, there will be 9 billion GNSS devices on Earth—more than one per person. Yet most people have no idea how fragile this invisible infrastructure really is."

**Conversational:**
> "If you've ever wondered why your GPS gets confused in downtown Manhattan, you're about to understand a lot more than you expected."

**Direct value:**
> "This post will save you 10+ hours of debugging. I learned these patterns the hard way so you don't have to."

### Good Technical Explanations

**Before (too technical):**
> "The transformer architecture uses multi-head self-attention mechanisms to compute weighted representations of input sequences through learned query, key, and value projections."

**After (accessible):**
> "Think of a transformer like a reader with perfect memory. When it reads a sentence, it can look at every word and ask: 'How much does this word relate to every other word?' That's self-attention—and it's why ChatGPT can track what 'it' refers to across a long paragraph."

### Using Bold Effectively

**Key metrics:**
> "The market grew from **$13B in 2023** to an expected **$20B by 2030**—a **53% increase** in just seven years."

**Important terms (first use):**
> "This is where **RTK (Real-Time Kinematics)** comes in—a technique that uses a nearby base station to correct GPS errors in real-time."

**Actionable items:**
> "The three things to remember: **start small**, **measure everything**, and **iterate weekly**."

---

## Image Guidelines

### Hero Image
- Should visually represent the topic
- High quality, 1200x630px or larger
- Place in `/public/images/`
- Reference in frontmatter: `hero: "/images/filename.jpg"`

### Inline Images
- Use after explaining a concept, not before
- Always include alt text (accessibility)
- Optional caption in quotes

```markdown
![Alt text describing what's shown](/images/filename.png "Caption visible to readers")
```

### Image Types to Include

| Post Type | Suggested Images |
|-----------|------------------|
| Explainer | Concept diagram, process flow |
| Tutorial | Screenshots, step-by-step visuals |
| Analysis | Charts, data visualizations |
| Opinion | Hero image, maybe 1 supporting visual |
| Case Study | Before/after, results charts |

---

## Common Tags by Topic

| Topic Area | Suggested Tags |
|------------|----------------|
| AI/ML | "AI", "Machine Learning", "LLMs", "Agents" |
| Development | "Programming", "DevOps", "Tools" |
| GNSS/Navigation | "GNSS", "GPS", "Positioning", "Navigation" |
| Business | "Strategy", "Startups", "Markets" |
| Productivity | "Automation", "Workflows", "Tools" |
| Hardware | "Semiconductors", "Chips", "Hardware" |
| Space | "Satellites", "LEO", "Space Tech" |
