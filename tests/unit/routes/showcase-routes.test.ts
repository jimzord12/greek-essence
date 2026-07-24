import { describe, expect, it } from "vitest"

import { getLocalizedHref } from "@/lib/routes"

describe("showcase route identities", () => {
  it.each([
    ["home", "en", "/en"],
    ["home", "el", "/el"],
    ["paros", "en", "/en/destinations/paros-antiparos"],
    ["paros", "el", "/el/destinations/paros-antiparos"],
    ["plan-my-trip", "en", "/en/plan-my-trip"],
    ["plan-my-trip", "el", "/el/plan-my-trip"],
    ["confirmation", "en", "/en/plan-my-trip/confirmation"],
    ["confirmation", "el", "/el/plan-my-trip/confirmation"],
  ] as const)("maps %s independently for %s", (route, locale, href) => {
    expect(getLocalizedHref(route, locale)).toBe(href)
  })
})
