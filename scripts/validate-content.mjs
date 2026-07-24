import { existsSync, readFileSync } from "node:fs"
import { resolve } from "node:path"

import { showcaseContentSchema } from "../content/schemas/showcase.ts"

const root = process.cwd()
const locales = ["en", "el"]
const contents = Object.fromEntries(
  locales.map((locale) => [
    locale,
    showcaseContentSchema.parse(
      JSON.parse(
        readFileSync(resolve(root, `content/${locale}/showcase.json`), "utf8")
      )
    ),
  ])
)
const manifest = JSON.parse(
  readFileSync(resolve(root, "content/shared/media.json"), "utf8")
)
const mediaIds = new Set(manifest.assets.map((asset) => asset.id))

function shape(value) {
  if (Array.isArray(value)) return value.map(shape)
  if (value && typeof value === "object")
    return Object.fromEntries(
      Object.keys(value)
        .sort()
        .map((key) => [key, shape(value[key])])
    )
  return typeof value
}
if (JSON.stringify(shape(contents.en)) !== JSON.stringify(shape(contents.el)))
  throw new Error("Showcase locale structure differs")

for (const [locale, content] of Object.entries(contents)) {
  if (locale === "el" && !/[Α-Ωα-ω]/.test(JSON.stringify(content)))
    throw new Error("Greek showcase content lacks Greek prose")
  const referenced = [
    content.home.hero.mediaId,
    content.home.promise.mediaId,
    content.home.parosFeature.mediaId,
    content.home.trustStory.mediaId,
  ].filter(Boolean)
  for (const id of referenced)
    if (!mediaIds.has(id)) throw new Error(`Unknown showcase media id: ${id}`)
}

if (manifest.defaults.approvalStatus === "approved") {
  const {
    alt,
    focalPoint,
    rightsStatus,
    source,
    sourceApprovalStatus,
    provisional,
  } = manifest.defaults
  const approvedSources = new Set(["operator-generated", "licensed", "owned"])
  const approvedRoles = /^(master|crop-(?:16x9|4x5|3x2|3x4|4x3))$/
  if (
    manifest.setStatus !== "approved" ||
    sourceApprovalStatus !== "approved" ||
    !approvedSources.has(source) ||
    rightsStatus !== "approved" ||
    provisional !== false ||
    !alt.en?.trim() ||
    !alt.el?.trim() ||
    !focalPoint ||
    focalPoint.xPercent < 0 ||
    focalPoint.xPercent > 100 ||
    focalPoint.yPercent < 0 ||
    focalPoint.yPercent > 100
  )
    throw new Error("Approved media source, rights, or defaults are incomplete")
  for (const asset of manifest.assets)
    for (const file of asset.files) {
      if (
        !(file.width > 0 && file.height > 0) ||
        !approvedRoles.test(file.role) ||
        !existsSync(resolve(root, manifest.assetRoot, file.path))
      )
        throw new Error(`Approved media file is invalid: ${asset.id}`)
    }
}
console.log(
  "Showcase content validation passed for en/el with media approval checks"
)
