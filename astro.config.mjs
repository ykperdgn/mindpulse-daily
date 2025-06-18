// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://mindpulse-daily.vercel.app', // Vercel deployment URL
  vite: {
    plugins: [tailwindcss()]
  }
});