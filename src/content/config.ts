import { defineCollection, z } from "astro:content";

const postSchema = z.object({
  title: z.string(),
  description: z.string(),
  date: z.string(),
  language: z.enum(['en', 'tr']),
});

export const collections = {
  posts: defineCollection({ schema: postSchema }),
};
