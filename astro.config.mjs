// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// Determine the site URL based on deployment environment
const getSiteUrl = () => {
  // GitHub Pages deployment
  if (process.env.GITHUB_ACTIONS) {
    return 'https://ykperdgn.github.io/mindpulse-daily';
  }
  // Vercel deployment (fallback)
  return 'https://mindpulse-daily.vercel.app';
};

// https://astro.build/config
export default defineConfig({
  site: getSiteUrl(),
  base: process.env.GITHUB_ACTIONS ? '/mindpulse-daily' : '/',
  vite: {
    plugins: [tailwindcss()]
  }
});