// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import image from '@astrojs/image';

// https://astro.build/config
export default defineConfig({
  site: "https://techntrek.is-a.dev",
  integrations: [mdx(), sitemap(), image()],
  vite: {
    plugins: [tailwindcss()]
  },
});
