import { expect, test, type Page } from "@playwright/test"

const criticalResourceTypes = new Set([
  "document",
  "script",
  "stylesheet",
  "fetch",
  "xhr",
])

async function localeLinkIndex(page: Page, locale: string) {
  return page.getByRole("link").evaluateAll((links, targetLocale) => {
    return links.findIndex((link) => {
      const href = link.getAttribute("href")
      return (
        href !== null &&
        new URL(href, window.location.href).pathname === `/${targetLocale}`
      )
    })
  }, locale)
}

test.describe("localized prototype shell", () => {
  let consoleErrors: string[]
  let criticalRequestFailures: string[]
  let expectsNotFound: boolean

  test.beforeEach(({ page }) => {
    consoleErrors = []
    criticalRequestFailures = []
    expectsNotFound = false

    page.on("console", (message) => {
      if (!expectsNotFound && message.type() === "error") {
        consoleErrors.push(message.text())
      }
    })

    page.on("requestfailed", (request) => {
      if (criticalResourceTypes.has(request.resourceType())) {
        criticalRequestFailures.push(`${request.method()} ${request.url()}`)
      }
    })

    page.on("response", (response) => {
      if (
        !expectsNotFound &&
        criticalResourceTypes.has(response.request().resourceType()) &&
        response.status() >= 400
      ) {
        criticalRequestFailures.push(`${response.status()} ${response.url()}`)
      }
    })
  })

  test.afterEach(() => {
    expect(consoleErrors).toEqual([])
    expect(criticalRequestFailures).toEqual([])
  })

  test("renders localized pages with canonical metadata", async ({ page }) => {
    await page.goto("/en")
    await expect(page.locator("html")).toHaveAttribute("lang", /^en/)
    await expect(page).toHaveTitle(/.+/)
    await expect(page.locator('meta[name="description"]')).toHaveAttribute(
      "content",
      /.+/
    )
    await expect(page.locator('link[rel="canonical"]')).toHaveAttribute(
      "href",
      /.+/
    )

    await page.goto("/el")
    await expect(page.locator("html")).toHaveAttribute("lang", /^el/)
    await expect(page).toHaveTitle(/.+/)
    await expect(page.locator('meta[name="description"]')).toHaveAttribute(
      "content",
      /.+/
    )
    await expect(page.locator('link[rel="canonical"]')).toHaveAttribute(
      "href",
      /.+/
    )
  })

  test("switches locale using an accessible link", async ({ page }) => {
    await page.goto("/en")
    const index = await localeLinkIndex(page, "el")
    expect(index).toBeGreaterThanOrEqual(0)

    await page.getByRole("link").nth(index).click()
    await expect(page).toHaveURL(/\/el$/)
  })

  test("redirects the root route and rejects an invalid locale", async ({
    page,
  }) => {
    await page.goto("/")
    await expect(page).toHaveURL(/\/(en|el)$/)

    expectsNotFound = true
    const invalidLocaleResponse = await page.goto("/invalid")
    expect(invalidLocaleResponse?.status()).toBe(404)
  })

  test("provides keyboard focus for interactive navigation", async ({
    page,
  }) => {
    await page.goto("/en")
    await page.keyboard.press("Tab")
    await expect(page.locator(":focus")).toBeVisible()
  })
})
