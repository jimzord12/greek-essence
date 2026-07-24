import { describe, expect, it } from "vitest"

import { assertHomeLcpCeiling } from "../../../scripts/assert-unlighthouse-lcp.mjs"

const reports = (en: number, el: number) => [
  { route: "/en", lcp: en },
  { route: "/el", lcp: el },
]

describe("strict Home LCP ceiling", () => {
  it("accepts values below 2500ms", () => {
    expect(() => assertHomeLcpCeiling(reports(2499.999, 2400))).not.toThrow()
  })

  it("accepts values exactly at 2500ms", () => {
    expect(() => assertHomeLcpCeiling(reports(2500, 2500))).not.toThrow()
  })

  it("rejects either locale above 2500ms", () => {
    expect(() => assertHomeLcpCeiling(reports(2500.001, 2400))).toThrow("/en")
    expect(() => assertHomeLcpCeiling(reports(2400, 2500.001))).toThrow("/el")
  })

  it("fails closed when either required locale report is absent", () => {
    expect(() => assertHomeLcpCeiling([{ route: "/en", lcp: 2000 }])).toThrow(
      "/el"
    )
  })
})
