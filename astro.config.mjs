// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import image from '@astrojs/image';

// https://astro.build/config
export default defineConfig({
	
  site: "https://YOURDOMAIN.com",
  integrations: [tailwind(), mdx(), sitemap(), image()],
  vite: {
    plugins: [tailwindcss()]
  },

  integrations: [mdx(), sitemap(), image()]
});

