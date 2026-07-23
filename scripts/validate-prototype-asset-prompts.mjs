import fs from "node:fs"
import path from "node:path"
import { fileURLToPath } from "node:url"

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const packPath = path.join(
  root,
  "content",
  "planning",
  "prototype-asset-prompts.json"
)
const expectedTestIds = [
  "home-aegean-human-arrival-01",
  "destination-athens-primary-01",
  "paros-antiparos-editorial-culture-food-01",
  "experience-family-01",
]
const authoritativeAssets = [
  ["home-aegean-human-arrival-01", "16:9", ["3:2", "4:5"], 2560, 1440],
  ["destination-athens-primary-01", "4:3", [], 2400, 1800],
  [
    "destination-paros-antiparos-primary-01",
    "4:3",
    ["16:9", "3:2", "4:5", "3:4"],
    2400,
    1800,
  ],
  ["destination-mykonos-primary-01", "4:3", [], 2400, 1800],
  ["destination-santorini-primary-01", "4:3", [], 2400, 1800],
  [
    "paros-antiparos-editorial-culture-food-01",
    "4:5",
    ["3:4", "3:2"],
    1800,
    2250,
  ],
  [
    "paros-antiparos-editorial-hospitality-01",
    "4:5",
    ["3:4", "3:2"],
    1800,
    2250,
  ],
  [
    "paros-antiparos-editorial-local-moment-01",
    "3:2",
    ["4:5", "3:4"],
    2400,
    1600,
  ],
  ["experience-tailor-made-01", "3:2", [], 2100, 1400],
  ["experience-island-hopping-01", "3:2", [], 2100, 1400],
  ["experience-local-experiences-01", "3:2", [], 2100, 1400],
  ["experience-multi-destination-01", "3:2", [], 2100, 1400],
  ["experience-vip-planning-01", "3:2", [], 2100, 1400],
  ["experience-family-01", "3:2", ["16:9", "4:5", "3:4"], 2100, 1400],
  ["journey-cyclades-romance-01", "3:2", ["16:9", "4:5", "3:4"], 2400, 1600],
  ["journey-athens-islands-01", "3:2", [], 2400, 1600],
  ["journey-culture-gastronomy-01", "3:2", [], 2400, 1600],
  ["person-founder-profile-01", "4:5", ["1:1"], 1600, 2000],
]
const expectedRights = [
  "generation_source_and_creator_record",
  "web_and_prototype_use",
  "localized_public_demo_use",
  "resizing_and_derivative_crops",
]
const negativeConstraintKeys = [
  "booking",
  "offerTerms",
  "partnershipOrIdentity",
  "transportOrRoute",
  "reviewsOrAwards",
  "embeddedText",
  "stockLuxuryOrProcessing",
  "locationRepresentation",
  "assetSpecific",
]
const exactKeys = (value, expected, label) => {
  if (!value || typeof value !== "object" || Array.isArray(value))
    throw new Error(`${label} must be an object`)
  const actual = Object.keys(value).sort()
  const wanted = [...expected].sort()
  if (JSON.stringify(actual) !== JSON.stringify(wanted))
    throw new Error(
      `${label} fields must be exactly [${wanted.join(", ")}], received [${actual.join(", ")}]`
    )
}
const nonEmpty = (value, label) => {
  if (typeof value !== "string" || value.trim() === "")
    throw new Error(`${label} must be a non-empty string`)
}
const exactArray = (actual, expected, label) => {
  if (
    !Array.isArray(actual) ||
    JSON.stringify(actual) !== JSON.stringify(expected)
  )
    throw new Error(
      `${label} must be exactly [${expected.join(", ")}] in order`
    )
}
const ratioForDimensions = (width, height) => {
  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b))
  const divisor = gcd(width, height)
  return `${width / divisor}:${height / divisor}`
}

let pack
try {
  pack = JSON.parse(fs.readFileSync(packPath, "utf8"))
} catch (error) {
  throw new Error(`Invalid JSON at ${packPath}: ${error.message}`)
}
exactKeys(
  pack,
  ["schemaVersion", "purpose", "source", "testSetIds", "assets"],
  "pack"
)
if (pack.schemaVersion !== 1) throw new Error("schemaVersion must be 1")
nonEmpty(pack.purpose, "purpose")
nonEmpty(pack.source, "source")
exactArray(pack.testSetIds, expectedTestIds, "testSetIds")
if (
  !Array.isArray(pack.assets) ||
  pack.assets.length !== authoritativeAssets.length
)
  throw new Error("assets must contain exactly 18 records")
exactArray(
  pack.assets.map(({ id }) => id),
  authoritativeAssets.map(([id]) => id),
  "ordered asset IDs"
)

const assetKeys = [
  "sequence",
  "id",
  "family",
  "testSet",
  "status",
  "routeUse",
  "subject",
  "location",
  "visualDirection",
  "composition",
  "delivery",
  "responsiveCropIntent",
  "textOverlay",
  "accessibilityIntent",
  "accuracyConstraints",
  "negativeConstraints",
  "continuityInstructions",
  "review",
  "prompt",
]
for (const [index, asset] of pack.assets.entries()) {
  const label = `assets[${index}]`
  const [
    expectedId,
    expectedMasterRatio,
    expectedCrops,
    expectedWidth,
    expectedHeight,
  ] = authoritativeAssets[index]
  const expectedRequiredCrops =
    expectedId === "person-founder-profile-01" ? [] : expectedCrops
  exactKeys(asset, assetKeys, label)
  if (asset.sequence !== index + 1)
    throw new Error(`${label}.sequence must match authoritative array order`)
  if (asset.id !== expectedId)
    throw new Error(`${label}.id must be ${expectedId}`)
  for (const field of [
    "family",
    "routeUse",
    "subject",
    "location",
    "visualDirection",
    "responsiveCropIntent",
    "accessibilityIntent",
    "continuityInstructions",
  ])
    nonEmpty(asset[field], `${label}.${field}`)

  const designated = expectedTestIds.includes(asset.id)
  const expectedStatus = designated
    ? "test_set_pending_operator_visual_direction_feedback"
    : "draft_pending_test_feedback"
  if (asset.testSet !== designated || asset.status !== expectedStatus)
    throw new Error(
      `${label} must retain its designated test membership and status`
    )

  exactKeys(
    asset.composition,
    ["direction", "textSafeArea", "focalPoint"],
    `${label}.composition`
  )
  Object.entries(asset.composition).forEach(([key, value]) =>
    nonEmpty(value, `${label}.composition.${key}`)
  )
  exactKeys(
    asset.delivery,
    [
      "masterAspectRatio",
      "allowedDerivativeCropRatios",
      "requiredDerivativeCropRatios",
      "targetDimensions",
    ],
    `${label}.delivery`
  )
  if (asset.delivery.masterAspectRatio !== expectedMasterRatio)
    throw new Error(
      `${label}.delivery.masterAspectRatio must be ${expectedMasterRatio}`
    )
  exactArray(
    asset.delivery.allowedDerivativeCropRatios,
    expectedCrops,
    `${label}.delivery.allowedDerivativeCropRatios`
  )
  exactArray(
    asset.delivery.requiredDerivativeCropRatios,
    expectedRequiredCrops,
    `${label}.delivery.requiredDerivativeCropRatios`
  )
  if (
    asset.delivery.requiredDerivativeCropRatios.some(
      (ratio) => !asset.delivery.allowedDerivativeCropRatios.includes(ratio)
    )
  )
    throw new Error(
      `${label}.delivery required derivative crops must be allowed`
    )
  const allRatios = [
    asset.delivery.masterAspectRatio,
    ...asset.delivery.allowedDerivativeCropRatios,
  ]
  if (
    allRatios.some((ratio) => !/^\d+:\d+$/.test(ratio)) ||
    new Set(allRatios).size !== allRatios.length
  )
    throw new Error(
      `${label}.delivery ratios must be valid and contain no duplicates`
    )
  exactKeys(
    asset.delivery.targetDimensions,
    ["width", "height", "unit", "minimum"],
    `${label}.delivery.targetDimensions`
  )
  const dimensions = asset.delivery.targetDimensions
  if (
    dimensions.width !== expectedWidth ||
    dimensions.height !== expectedHeight ||
    dimensions.unit !== "px" ||
    dimensions.minimum !== true
  )
    throw new Error(
      `${label}.delivery.targetDimensions do not match the authoritative master dimensions`
    )
  if (
    ratioForDimensions(dimensions.width, dimensions.height) !==
    asset.delivery.masterAspectRatio
  )
    throw new Error(
      `${label}.delivery master ratio must match target dimensions`
    )

  exactKeys(
    asset.textOverlay,
    ["embeddedTextAllowed", "english", "greek"],
    `${label}.textOverlay`
  )
  if (
    asset.textOverlay.embeddedTextAllowed !== false ||
    asset.textOverlay.english !==
      "prohibited_in_pixels_use_localized_DOM_text_only" ||
    asset.textOverlay.greek !==
      "prohibited_in_pixels_use_localized_DOM_text_only"
  )
    throw new Error(
      `${label}.textOverlay must prohibit embedded English and Greek text`
    )
  exactKeys(
    asset.accuracyConstraints,
    ["geographic", "brand"],
    `${label}.accuracyConstraints`
  )
  Object.entries(asset.accuracyConstraints).forEach(([key, value]) =>
    nonEmpty(value, `${label}.accuracyConstraints.${key}`)
  )
  exactKeys(
    asset.negativeConstraints,
    negativeConstraintKeys,
    `${label}.negativeConstraints`
  )
  Object.entries(asset.negativeConstraints).forEach(([key, value]) =>
    nonEmpty(value, `${label}.negativeConstraints.${key}`)
  )

  exactKeys(
    asset.review,
    [
      "sceneStatus",
      "peopleContentStatus",
      "releasesRequired",
      "journeyContentStatus",
      "licensingStatus",
      "requiredRights",
      "provenanceStatus",
      "exactLocationOrPropertyStatus",
      "approvalStatus",
    ],
    `${label}.review`
  )
  if (asset.review.sceneStatus !== "inferred_provisional")
    throw new Error(`${label}.review.sceneStatus is invalid`)
  if (
    !["inferred_provisional", "not_required"].includes(
      asset.review.peopleContentStatus
    )
  )
    throw new Error(`${label}.review.peopleContentStatus is invalid`)
  if (
    asset.review.releasesRequired !==
    (asset.review.peopleContentStatus === "inferred_provisional")
  )
    throw new Error(
      `${label}.review.releasesRequired must reflect people content status`
    )
  if (
    ![null, "inferred_provisional"].includes(asset.review.journeyContentStatus)
  )
    throw new Error(`${label}.review.journeyContentStatus is invalid`)
  if (asset.review.licensingStatus !== "unlicensed_planning_only")
    throw new Error(`${label}.review.licensingStatus is invalid`)
  exactArray(
    asset.review.requiredRights,
    expectedRights,
    `${label}.review.requiredRights`
  )
  if (
    asset.review.provenanceStatus !==
      "planned_from_authorized_source_output_not_generated" ||
    asset.review.exactLocationOrPropertyStatus !== "unverified_provisional" ||
    asset.review.approvalStatus !== asset.status
  )
    throw new Error(`${label}.review statuses are invalid or inconsistent`)

  nonEmpty(asset.prompt, `${label}.prompt`)
  if (!asset.prompt.startsWith("Create a high-quality image"))
    throw new Error(`${label}.prompt must begin “Create a high-quality image…”`)
  const cropList = (ratios) => (ratios.length ? ratios.join(", ") : "none")
  const requiredPromptValues = [
    asset.id,
    `Route/use: ${asset.routeUse}`,
    `Subject: ${asset.subject}`,
    `Location: ${asset.location}`,
    `Visual direction: ${asset.visualDirection}`,
    `Composition direction: ${asset.composition.direction}`,
    `Text-safe area: ${asset.composition.textSafeArea}`,
    `Focal point: ${asset.composition.focalPoint}`,
    `${dimensions.width} × ${dimensions.height} ${dimensions.unit} master at ${asset.delivery.masterAspectRatio}`,
    `allowed derivative crop ratios: ${cropList(asset.delivery.allowedDerivativeCropRatios)}`,
    `required derivative crop ratios: ${cropList(asset.delivery.requiredDerivativeCropRatios)}`,
    `Responsive intent: ${asset.responsiveCropIntent}`,
    `Accessibility intent: ${asset.accessibilityIntent}`,
    `embeddedTextAllowed=${asset.textOverlay.embeddedTextAllowed}`,
    `English=${asset.textOverlay.english}`,
    `Greek=${asset.textOverlay.greek}`,
    `Geographic accuracy: ${asset.accuracyConstraints.geographic}`,
    `Brand accuracy: ${asset.accuracyConstraints.brand}`,
    `Continuity: ${asset.continuityInstructions}`,
    `sceneStatus=${asset.review.sceneStatus}`,
    `peopleContentStatus=${asset.review.peopleContentStatus}`,
    `releasesRequired=${asset.review.releasesRequired}`,
    `journeyContentStatus=${asset.review.journeyContentStatus === null ? "null" : asset.review.journeyContentStatus}`,
    `licensingStatus=${asset.review.licensingStatus}`,
    `requiredRights=${asset.review.requiredRights.join(", ")}`,
    `provenanceStatus=${asset.review.provenanceStatus}`,
    `exactLocationOrPropertyStatus=${asset.review.exactLocationOrPropertyStatus}`,
    `approvalStatus=${asset.review.approvalStatus}`,
    ...Object.entries(asset.negativeConstraints).map(
      ([key, value]) => `${key}: ${value}`
    ),
  ]
  const missing = requiredPromptValues.filter(
    (value) => !asset.prompt.includes(value)
  )
  if (missing.length)
    throw new Error(
      `${label}.prompt is missing exact structured values: ${missing.join(" | ")}`
    )
}
if (pack.assets.filter(({ testSet }) => testSet).length !== 4)
  throw new Error(
    "assets must contain exactly the four designated test-set records"
  )
console.log(
  `Validated ${pack.assets.length} authoritative ordered prototype asset prompts (${expectedTestIds.length} test-set, ${pack.assets.length - expectedTestIds.length} draft pending feedback).`
)
