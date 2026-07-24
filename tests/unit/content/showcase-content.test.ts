import { describe, expect, it } from "vitest"

import greekFixture from "@/content/el/showcase.json"
import englishFixture from "@/content/en/showcase.json"
import {
  getShowcaseContent,
  resolveMedia,
  resolveMediaFromManifest,
  validateShowcaseContentPair,
  type MediaManifest,
} from "@/lib/content"

const clone = <T>(value: T): T => structuredClone(value)
const approvedManifest = (): MediaManifest => ({
  assetRoot: "assets/imgs",
  setStatus: "approved",
  defaults: {
    source: "operator-generated",
    sourceApprovalStatus: "approved",
    rightsStatus: "approved",
    approvalStatus: "approved",
    provisional: false,
    focalPoint: { xPercent: 25, yPercent: 60 },
    alt: { en: "Aegean arrival", el: "Άφιξη στο Αιγαίο" },
  },
  assets: [
    {
      id: "hero",
      files: [{ path: "hero.jpg", width: 1200, height: 800, role: "master" }],
    },
  ],
})

describe("showcase content boundary", () => {
  it("loads structurally equivalent English and Greek Home content", () => {
    const english = getShowcaseContent("en")
    const greek = getShowcaseContent("el")
    expect(Object.keys(greek.home)).toEqual(Object.keys(english.home))
    expect(english.home.howItWorks.steps).toHaveLength(3)
    expect(greek.home.howItWorks.steps).toHaveLength(3)
    expect(greek.home.hero.title).toMatch(/[Α-Ωα-ω]/)
  })

  it("rejects an empty editorial field", () => {
    const invalid = clone(englishFixture)
    invalid.home.hero.title = "   "
    expect(() =>
      validateShowcaseContentPair(invalid, greekFixture, [])
    ).toThrow()
  })

  it("rejects an unknown route ID", () => {
    const invalid: unknown = {
      ...clone(englishFixture),
      home: {
        ...clone(englishFixture.home),
        hero: {
          ...clone(englishFixture.home.hero),
          primaryCta: {
            ...clone(englishFixture.home.hero.primaryCta),
            routeId: "unknown",
          },
        },
      },
    }
    expect(() =>
      validateShowcaseContentPair(invalid, greekFixture, [])
    ).toThrow()
  })

  it("rejects an unknown media ID", () => {
    const invalid = clone(englishFixture)
    invalid.home.hero.mediaId = "unknown-media"
    expect(() =>
      validateShowcaseContentPair(invalid, greekFixture, [])
    ).toThrow("Unknown showcase media id")
  })

  it("rejects English/Greek structural drift", () => {
    const promiseWithoutBody: Record<string, unknown> = clone(
      greekFixture.home.promise
    )
    Reflect.deleteProperty(promiseWithoutBody, "body")
    const invalidGreek: unknown = {
      ...clone(greekFixture),
      home: { ...clone(greekFixture.home), promise: promiseWithoutBody },
    }
    expect(() =>
      validateShowcaseContentPair(englishFixture, invalidGreek, [])
    ).toThrow("Showcase locale structure differs")
  })

  it("keeps both live Home media records behind the pending approval fallback", () => {
    expect(resolveMedia("home-aegean-human-arrival-01", "en")).toEqual({
      kind: "fallback",
      id: "home-aegean-human-arrival-01",
      reason: "pending-approval",
    })
    expect(
      resolveMedia("destination-paros-antiparos-primary-01", "el")
    ).toEqual({
      kind: "fallback",
      id: "destination-paros-antiparos-primary-01",
      reason: "pending-approval",
    })
  })

  it("resolves a controlled fully approved record with localized geometry", () => {
    expect(
      resolveMediaFromManifest(approvedManifest(), "hero", "el", () => true)
    ).toEqual({
      kind: "approved",
      media: {
        id: "hero",
        src: "/assets/imgs/hero.jpg",
        width: 1200,
        height: 800,
        alt: "Άφιξη στο Αιγαίο",
        focalPoint: { xPercent: 25, yPercent: 60 },
      },
    })
  })

  it.each([
    [
      "pending source approval",
      (manifest: MediaManifest) => {
        manifest.defaults.sourceApprovalStatus = "pending"
      },
    ],
    [
      "arbitrary source",
      (manifest: MediaManifest) => {
        manifest.defaults.source = "arbitrary"
      },
    ],
    [
      "provisional manifest",
      (manifest: MediaManifest) => {
        manifest.defaults.provisional = true
      },
    ],
    [
      "incomplete crop role",
      (manifest: MediaManifest) => {
        manifest.assets[0]!.files[0]!.role = ""
      },
    ],
  ])("fails closed for approved media with %s", (_name, mutate) => {
    const manifest = approvedManifest()
    mutate(manifest)
    expect(() =>
      resolveMediaFromManifest(manifest, "hero", "en", () => true)
    ).toThrow("Approved media is incomplete")
  })
})
