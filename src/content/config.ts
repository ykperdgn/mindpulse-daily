import { defineCollection, z } from "astro:content";

const postSchema = z.object({
  title: z.string(),
  description: z.string(),
  date: z.string(),
  language: z.enum(['en', 'tr']),
  category: z.enum(['psychology', 'astrology', 'space', 'history', 'science', 'lifestyle', 'mystery']).optional(),
  image: z.string().optional(),
});

export const collections = {
  posts: defineCollection({ schema: postSchema }),
};
