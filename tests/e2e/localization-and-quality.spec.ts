import { expect, test, type Page } from "@playwright/test"

import {
  assertNoBrowserFailures,
  installBrowserGuards,
  type BrowserGuards,
} from "./browser-guards"

const localizedRoutes = [
  {
    route: "/en",
    locale: "en",
    canonical: "/en",
    alternates: { en: "/en", el: "/el", "x-default": "/en" },
  },
  {
    route: "/el",
    locale: "el",
    canonical: "/el",
    alternates: { en: "/en", el: "/el", "x-default": "/en" },
  },
  {
    route: "/en/quality-lab",
    locale: "en",
    canonical: "/en/quality-lab",
    alternates: {
      en: "/en/quality-lab",
      el: "/el/quality-lab",
      "x-default": "/en/quality-lab",
    },
  },
  {
    route: "/el/quality-lab",
    locale: "el",
    canonical: "/el/quality-lab",
    alternates: {
      en: "/en/quality-lab",
      el: "/el/quality-lab",
      "x-default": "/en/quality-lab",
    },
  },
] as const

const toggleJourneys = [
  {
    route: "/en/quality-lab",
    initial: "Not selected",
    selected: "Selected",
    status: "Current state",
    activation: "click",
  },
  {
    route: "/el/quality-lab",
    initial: "Δεν έχει επιλεγεί",
    selected: "Επιλεγμένο",
    status: "Τρέχουσα κατάσταση",
    activation: "keyboard",
  },
] as const

async function expectPathname(
  locator: ReturnType<Page["locator"]>,
  path: string
) {
  const href = await locator.getAttribute("href")
  expect(href).not.toBeNull()
  expect(new URL(href!, "http://127.0.0.1:3100").pathname).toBe(path)
}

async function tabTo(page: Page, locator: ReturnType<Page["getByRole"]>) {
  for (let attempt = 0; attempt < 12; attempt += 1) {
    await page.keyboard.press("Tab")
    if (
      await locator.evaluate((element) => element === document.activeElement)
    ) {
      return
    }
  }

  throw new Error("Keyboard focus did not reach the expected control")
}

async function expectLocalizedMetadata(
  page: Page,
  route: (typeof localizedRoutes)[number]
) {
  await expect(page.locator("html")).toHaveAttribute("lang", route.locale)
  await expect(page).toHaveTitle(/.+/)
  await expect(page.locator('meta[name="description"]')).toHaveAttribute(
    "content",
    /.+/
  )
  await expectPathname(page.locator('link[rel="canonical"]'), route.canonical)

  const alternateLinks = await page
    .locator('link[rel="alternate"][hreflang]')
    .evaluateAll((links) =>
      links.map((link) => ({
        hreflang: link.getAttribute("hreflang"),
        pathname: new URL(link.getAttribute("href")!, "http://127.0.0.1:3100")
          .pathname,
      }))
    )

  expect(alternateLinks).toEqual(
    Object.entries(route.alternates).map(([hreflang, pathname]) => ({
      hreflang,
      pathname,
    }))
  )
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute(
    "content",
    "noindex, nofollow"
  )
}

test.describe("localized prototype shell", () => {
  let browserGuards: BrowserGuards

  test.beforeEach(({ page }) => {
    browserGuards = installBrowserGuards(page)
  })

  test.afterEach(() => {
    assertNoBrowserFailures(browserGuards)
  })

  test("renders exact localized metadata semantics", async ({ page }) => {
    for (const route of localizedRoutes) {
      await page.goto(route.route)
      await expectLocalizedMetadata(page, route)
    }
  })

  test("switches locale using an accessible link", async ({ page }) => {
    await page.goto("/en")
    await page.getByRole("link", { name: "Greek", exact: true }).click()
    await expect(page).toHaveURL(/\/el$/)
  })

  test("redirects the root route and rejects an invalid locale", async ({
    page,
  }) => {
    await page.goto("/")
    await expect(page).toHaveURL(/\/(en|el)$/)

    const invalidLocaleResponse = await page.goto("/invalid")
    expect(invalidLocaleResponse?.status()).toBe(404)
  })

  test("exercises localized quality-lab toggle interaction", async ({
    page,
  }) => {
    for (const journey of toggleJourneys) {
      await page.goto(journey.route)
      const toggle = page.getByRole("button", {
        name: journey.initial,
        exact: true,
      })

      await expect(toggle).toHaveAttribute("aria-pressed", "false")

      if (journey.activation === "keyboard") {
        await tabTo(page, toggle)
        await page.keyboard.press("Space")
      } else {
        await toggle.click()
      }

      await expect(
        page.getByRole("button", { name: journey.selected, exact: true })
      ).toHaveAttribute("aria-pressed", "true")
      await expect(page.locator('[aria-live="polite"]')).toHaveText(
        `${journey.status}: ${journey.selected}`
      )
    }
  })

  test("provides keyboard focus for interactive navigation", async ({
    page,
  }) => {
    await page.goto("/en")
    await page.keyboard.press("Tab")
    await expect(page.locator(":focus")).toBeVisible()
  })
})
