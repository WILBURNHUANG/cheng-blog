# Discovery Phase Questions

Use these question templates during Phase 2 to gather context from the user.

## Question Categories

### 1. Audience & Angle

**Question:** Who is the target audience for this post?
- Beginners (new to the topic)
- Practitioners (working in the field)
- Decision-makers (evaluating options)
- General curious readers

**Question:** What angle should the post take?
- Educational explainer (what is X and how does it work)
- Practical guide (how to do X)
- Analysis/opinion (what I think about X)
- Industry overview (state of X in 2026)

### 2. Depth & Scope

**Question:** How technical should this post be?
- High-level overview (concepts only)
- Moderate (some technical details, explained simply)
- Deep dive (technical details for practitioners)

**Question:** What's the ideal length?
- Short (~800 words) - quick read, single concept
- Medium (~1,500 words) - thorough coverage
- Long (~2,500+ words) - comprehensive guide

**Question:** Are there specific subtopics to include or avoid?
- Include: [list]
- Avoid: [list]

### 3. User's Unique Value

**Question:** Do you have personal experience or insights to share?
- War stories / lessons learned
- Unique perspective from your work
- Contrarian views vs conventional wisdom

**Question:** What's the main takeaway you want readers to have?
- [Single sentence describing the key insight]

### 4. Materials Request

**Question:** Can you provide any supporting materials?

**Helpful materials:**
- YouTube videos explaining concepts (URLs)
- Articles or papers for reference (URLs)
- Images, diagrams, or screenshots to include
- Data, statistics, or reports to cite
- Personal notes or rough outlines

---

## AskUserQuestion Tool Usage

Use the AskUserQuestion tool with structured options. Example:

```json
{
  "questions": [
    {
      "question": "Who is the target audience for this post?",
      "header": "Audience",
      "options": [
        {"label": "Beginners", "description": "New to the topic, need concepts explained from scratch"},
        {"label": "Practitioners", "description": "Already working in the field, want practical depth"},
        {"label": "Decision-makers", "description": "Evaluating options, need business context"},
        {"label": "General readers", "description": "Curious but not necessarily technical"}
      ],
      "multiSelect": false
    },
    {
      "question": "How technical should the post be?",
      "header": "Depth",
      "options": [
        {"label": "High-level overview", "description": "Concepts and big picture only"},
        {"label": "Moderate depth", "description": "Some technical details, explained accessibly"},
        {"label": "Deep dive", "description": "Detailed technical content for practitioners"}
      ],
      "multiSelect": false
    }
  ]
}
```

---

## Materials Processing

### For YouTube Videos

1. Use WebFetch to retrieve video page
2. Extract: title, channel, key talking points from description
3. If transcript available, identify quotable sections
4. Note timestamps for specific claims or explanations

### For Articles/Papers

1. Use WebFetch to read the content
2. Extract: main thesis, key data points, quotable insights
3. Note the publication date and author credibility
4. Identify sections most relevant to the blog post

### For User-Provided Images

1. Note the file path
2. Ask user to place in `/public/images/` if not already
3. Write descriptive alt text
4. Determine placement in article (after which section)

---

## Sample Discovery Flow

**After initial research, ask:**

1. **Audience + Angle** (first question set)
   - "Based on my research, this topic could be approached as [A] or [B]. Which fits your goal?"

2. **Depth + Unique Value** (second question set)
   - "Do you have personal experience with [topic] you'd like to include?"
   - "Any specific examples or case studies to reference?"

3. **Materials Request** (open-ended)
   - "Do you have any YouTube videos, articles, or images that would help? Just share the links."

4. **Confirm Direction** (before writing)
   - "Here's my plan: [brief outline]. Does this match what you're looking for?"
