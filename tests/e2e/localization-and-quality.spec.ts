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

async function expectNoHorizontalOverflow(page: Page, width: number) {
  expect(
    await page.evaluate(() => ({
      body: {
        clientWidth: document.body.clientWidth,
        scrollWidth: document.body.scrollWidth,
      },
      document: {
        clientWidth: document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
      },
      overwideElements: [...document.querySelectorAll<HTMLElement>("body *")]
        .filter(
          (element) =>
            element.scrollWidth > element.clientWidth + 1 ||
            element.getBoundingClientRect().right >
              document.documentElement.clientWidth + 1
        )
        .map(
          (element) =>
            `${element.tagName}.${element.className}:scroll=${element.scrollWidth},client=${element.clientWidth},right=${Math.round(element.getBoundingClientRect().right)}`
        ),
    }))
  ).toEqual({
    body: { clientWidth: width, scrollWidth: width },
    document: { clientWidth: width, scrollWidth: width },
    overwideElements: [],
  })
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

  test("renders the complete bilingual Home and switches equivalent locale", async ({
    page,
  }) => {
    await page.goto("/en")
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: "Greece, experienced with intention",
      })
    ).toBeVisible()
    await expect(page.locator("main > section")).toHaveCount(6)
    const menuButton = page.getByRole("button", { name: "Menu", exact: true })
    if (await menuButton.isVisible()) await menuButton.click()
    await page.getByRole("link", { name: "Ελληνικά", exact: true }).click()
    await expect(page).toHaveURL(/\/el$/)
    await expect(
      page.getByRole("heading", {
        level: 1,
        name: "Η Ελλάδα, όπως αξίζει να τη ζήσετε",
      })
    ).toBeVisible()
    await expect(page.locator("main > section")).toHaveCount(6)
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

  test("provides security headers on both Home locales", async ({
    request,
  }) => {
    for (const route of ["/en", "/el"]) {
      const response = await request.get(route)
      expect(response.headers()["content-security-policy"]).toBeTruthy()
      expect(response.headers()["x-content-type-options"]).toBe("nosniff")
      expect(response.headers()["referrer-policy"]).toBe(
        "strict-origin-when-cross-origin"
      )
      expect(response.headers()["permissions-policy"]).toBe(
        "camera=(), microphone=(), geolocation=()"
      )
      expect(response.headers()["x-frame-options"]).toBe("DENY")
    }
  })

  test("closes the compact menu by Escape, outside activation, and navigation with focus return", async ({
    page,
  }) => {
    test.skip((await page.viewportSize())!.width >= 768, "compact interaction")
    await page.goto("/en")
    const trigger = page.getByRole("button", { name: "Menu", exact: true })
    await trigger.click()
    await page.keyboard.press("Escape")
    await expect(trigger).toHaveAttribute("aria-expanded", "false")
    await expect(trigger).toBeFocused()
    await trigger.click()
    await page.locator("main").click({ position: { x: 10, y: 10 } })
    await expect(trigger).toHaveAttribute("aria-expanded", "false")
    await trigger.click()
    await page.getByRole("link", { name: "Ελληνικά", exact: true }).click()
    await expect(page).toHaveURL(/\/el$/)
  })

  test("preserves focus, current state, reduced motion, responsive layout, and 200% zoom", async ({
    page,
  }) => {
    await page.emulateMedia({ reducedMotion: "reduce" })
    await page.goto("/el")
    const compactMenu = page.getByRole("button", { name: "Μενού", exact: true })
    if (await compactMenu.isVisible()) await compactMenu.click()
    await expect(
      page.getByRole("link", { name: "Αρχική", exact: true })
    ).toHaveAttribute("aria-current", "page")
    if (await compactMenu.isVisible()) await page.keyboard.press("Escape")
    await page.keyboard.press("Tab")
    await expect(page.locator(":focus")).toBeVisible()
    await page.setViewportSize({ width: 195, height: 844 })
    await expectNoHorizontalOverflow(page, 195)
    expect(
      await page
        .locator(".button")
        .first()
        .evaluate((element) => getComputedStyle(element).transitionDuration)
    ).toBe("0s")
    await page.goto("/en")
    await expectNoHorizontalOverflow(page, 195)
  })

  test("provides keyboard focus for interactive navigation", async ({
    page,
  }) => {
    await page.goto("/en")
    await page.keyboard.press("Tab")
    await expect(page.locator(":focus")).toBeVisible()
  })
})
