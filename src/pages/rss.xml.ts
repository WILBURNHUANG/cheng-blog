import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET() {
  const posts = (await getCollection('posts', ({data}) => !data.draft))
    .sort((a,b)=>b.data.date.getTime()-a.data.date.getTime());

  return rss({
    title: "Tech & Trek — Cheng",
    description: "AI, Space Tech, Outdoor, Thoughts, Startups, Money",
    site: import.meta.env.SITE,
    items: posts.map((p)=>({
      title: p.data.title,
      description: p.data.description,
      link: `/posts/${p.slug}`,
      pubDate: p.data.date
    }))
  });
}
