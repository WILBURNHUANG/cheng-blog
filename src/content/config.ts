import { z, defineCollection } from "astro:content";

const posts = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    description: z.string(),
    // ⬇️ use date types (matches how Astro parses unquoted dates)
    date: z.date(),
    updated: z.date().optional(),
    category: z.enum(["AI","Space Tech","Outdoor Sports","Thoughts","Startups","Money"]),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    hero: z.string().optional(),
    canonical: z.string().url().optional(),
  }),
});

export const collections = { posts };
