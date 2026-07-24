import greekContent from "@/content/el/showcase.json"
import englishContent from "@/content/en/showcase.json"
import {
  showcaseContentSchema,
  type ShowcaseContent,
} from "@/content/schemas/showcase"
import mediaManifest from "@/content/shared/media.json"
import type { Locale } from "@/i18n/routing"

export type MediaManifest = {
  assetRoot: string
  setStatus: string
  defaults: {
    source: string
    sourceApprovalStatus: string
    rightsStatus: string
    approvalStatus: string
    provisional: boolean
    focalPoint: { xPercent: number; yPercent: number } | null
    alt: Record<Locale, string | null>
  }
  assets: Array<{
    id: string
    files: Array<{ path: string; width: number; height: number; role: string }>
  }>
}

const manifest = mediaManifest as unknown as MediaManifest

function shape(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(shape)
  if (value && typeof value === "object") {
    return Object.fromEntries(
      Object.keys(value as Record<string, unknown>)
        .sort()
        .map((key) => [key, shape((value as Record<string, unknown>)[key])])
    )
  }
  return typeof value
}

function referencedMedia(content: ShowcaseContent): string[] {
  return [
    content.home.hero.mediaId,
    content.home.promise.mediaId,
    content.home.parosFeature.mediaId,
    content.home.trustStory.mediaId,
  ].filter((id): id is string => id !== null)
}

export function validateShowcaseContentPair(
  englishInput: unknown,
  greekInput: unknown,
  knownMediaIds: Iterable<string>
): { en: ShowcaseContent; el: ShowcaseContent } {
  if (
    JSON.stringify(shape(englishInput)) !== JSON.stringify(shape(greekInput))
  ) {
    throw new Error("Showcase locale structure differs")
  }
  const en = showcaseContentSchema.parse(englishInput)
  const el = showcaseContentSchema.parse(greekInput)
  const mediaIds = new Set(knownMediaIds)
  for (const content of [en, el]) {
    for (const id of referencedMedia(content)) {
      if (!mediaIds.has(id)) throw new Error(`Unknown showcase media id: ${id}`)
    }
  }
  return { en, el }
}

const validated = validateShowcaseContentPair(
  englishContent,
  greekContent,
  manifest.assets.map((asset) => asset.id)
)
const contentByLocale: Record<Locale, ShowcaseContent> = validated

export function getShowcaseContent(locale: Locale): ShowcaseContent {
  return contentByLocale[locale]
}

export type MediaResolution =
  | {
      kind: "approved"
      media: {
        id: string
        src: string
        width: number
        height: number
        alt: string
        focalPoint: { xPercent: number; yPercent: number }
      }
    }
  | { kind: "fallback"; id: string; reason: "pending-approval" }

const approvedSources = new Set(["operator-generated", "licensed", "owned"])
const approvedRoles = /^(master|crop-(?:16x9|4x5|3x2|3x4|4x3))$/

export function resolveMediaFromManifest(
  sourceManifest: MediaManifest,
  id: string,
  locale: Locale,
  fileExists: (path: string) => boolean = () => true
): MediaResolution {
  const asset = sourceManifest.assets.find((candidate) => candidate.id === id)
  if (!asset) throw new Error(`Unknown media id: ${id}`)

  const defaults = sourceManifest.defaults
  const alt = defaults.alt[locale]
  const focalPoint = defaults.focalPoint
  const claimsApproved = defaults.approvalStatus === "approved"
  if (!claimsApproved)
    return { kind: "fallback", id, reason: "pending-approval" }

  const file = asset.files[0]
  const completeApproval =
    sourceManifest.setStatus === "approved" &&
    defaults.sourceApprovalStatus === "approved" &&
    approvedSources.has(defaults.source) &&
    defaults.rightsStatus === "approved" &&
    defaults.provisional === false &&
    typeof alt === "string" &&
    alt.trim() !== "" &&
    focalPoint !== null &&
    file !== undefined &&
    file.width > 0 &&
    file.height > 0 &&
    approvedRoles.test(file.role) &&
    fileExists(`${sourceManifest.assetRoot}/${file.path}`) &&
    focalPoint.xPercent >= 0 &&
    focalPoint.xPercent <= 100 &&
    focalPoint.yPercent >= 0 &&
    focalPoint.yPercent <= 100

  if (!completeApproval) throw new Error(`Approved media is incomplete: ${id}`)
  return {
    kind: "approved",
    media: {
      id,
      src: `/${sourceManifest.assetRoot}/${file.path}`,
      width: file.width,
      height: file.height,
      alt,
      focalPoint,
    },
  }
}

export function resolveMedia(id: string, locale: Locale): MediaResolution {
  return resolveMediaFromManifest(manifest, id, locale)
}
