import { describe, expect, it } from "vitest"

import greekMessages from "@/messages/el.json"
import englishMessages from "@/messages/en.json"

function collectKeyPaths(value: unknown, path = ""): string[] {
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    return []
  }

  return Object.entries(value)
    .sort(([left], [right]) => left.localeCompare(right))
    .flatMap(([key, nestedValue]) => {
      const keyPath = path === "" ? key : `${path}.${key}`

      return [keyPath, ...collectKeyPaths(nestedValue, keyPath)]
    })
}

describe("fixture messages", () => {
  it("keeps English and Greek message keys in parity", () => {
    expect(collectKeyPaths(greekMessages)).toEqual(
      collectKeyPaths(englishMessages)
    )
  })
})
