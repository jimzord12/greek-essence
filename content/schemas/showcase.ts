import { z } from "zod"

const routeIdSchema = z.enum(["home", "paros", "plan-my-trip", "confirmation"])
const ctaSchema = z.object({
  label: z.string().trim().min(1),
  routeId: routeIdSchema,
  destinationContext: z.literal("paros-antiparos").nullable(),
})
const editorialSchema = z.object({
  eyebrow: z.string().trim().min(1).nullable(),
  heading: z.string().trim().min(1),
  body: z.array(z.string().trim().min(1)).min(1),
  mediaId: z.string().trim().min(1).nullable(),
})
const cardSchema = z.object({
  id: z.string().trim().min(1),
  title: z.string().trim().min(1),
  summary: z.string().trim().min(1),
  cta: ctaSchema.nullable(),
})

export const showcaseContentSchema = z.object({
  home: z.object({
    metadata: z.object({
      title: z.string().trim().min(1),
      description: z.string().trim().min(1),
    }),
    hero: z.object({
      eyebrow: z.string().trim().min(1).nullable(),
      title: z.string().trim().min(1),
      summary: z.string().trim().min(1),
      mediaId: z.string().trim().min(1).nullable(),
      primaryCta: ctaSchema,
      secondaryCta: ctaSchema.nullable(),
    }),
    promise: editorialSchema,
    parosFeature: cardSchema.extend({ mediaId: z.string().trim().min(1) }),
    howItWorks: z.object({
      heading: z.string().trim().min(1),
      steps: z.tuple([
        z.object({
          title: z.string().trim().min(1),
          summary: z.string().trim().min(1),
        }),
        z.object({
          title: z.string().trim().min(1),
          summary: z.string().trim().min(1),
        }),
        z.object({
          title: z.string().trim().min(1),
          summary: z.string().trim().min(1),
        }),
      ]),
    }),
    trustStory: editorialSchema,
    finalCta: ctaSchema,
  }),
})

export type ShowcaseContent = z.infer<typeof showcaseContentSchema>
