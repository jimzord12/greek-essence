import AxeBuilder from "@axe-core/playwright"
import { expect, test } from "@playwright/test"

import {
  assertNoBrowserFailures,
  installBrowserGuards,
  type BrowserGuards,
} from "./browser-guards"

const routes = ["/en", "/el", "/en/quality-lab", "/el/quality-lab"]
const wcag22Tags = [
  "wcag2a",
  "wcag2aa",
  "wcag21a",
  "wcag21aa",
  "wcag22a",
  "wcag22aa",
]

test.describe("WCAG A/AA accessibility", () => {
  let browserGuards: BrowserGuards

  test.beforeEach(({ page }) => {
    browserGuards = installBrowserGuards(page)
  })

  test.afterEach(() => {
    assertNoBrowserFailures(browserGuards)
  })

  for (const route of routes) {
    test(`${route} has no axe violations`, async ({ page }, testInfo) => {
      await page.goto(route)

      const results = await new AxeBuilder({ page })
        .withTags(wcag22Tags)
        .analyze()

      if (results.violations.length > 0) {
        await testInfo.attach("axe-results", {
          body: JSON.stringify(results, null, 2),
          contentType: "application/json",
        })
      }

      expect(results.violations).toEqual([])
    })
  }
})
