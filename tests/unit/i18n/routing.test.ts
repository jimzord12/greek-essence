import { describe, expect, it } from "vitest"

import { routing } from "@/i18n/routing"

describe("routing", () => {
  it("supports the explicit English and Greek locale routes", () => {
    expect(routing.locales).toEqual(["en", "el"])
    expect(routing.defaultLocale).toBe("en")
    expect(routing.localePrefix).toBe("always")
  })
})
