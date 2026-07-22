import { expect, type Page, type Response } from "@playwright/test"

const criticalResourceTypes = new Set([
  "document",
  "script",
  "stylesheet",
  "fetch",
  "xhr",
])

const expectedInvalidLocaleDocumentUrl = "http://127.0.0.1:3100/invalid"
const expectedInvalidLocale404ConsoleMessage =
  "Failed to load resource: the server responded with a status of 404 (Not Found)"

export type BrowserGuards = {
  consoleErrors: string[]
  criticalRequestFailures: string[]
  pageErrors: string[]
}

function isExpectedInvalidLocaleDocument404(response: Response) {
  return (
    response.url() === expectedInvalidLocaleDocumentUrl &&
    response.request().resourceType() === "document" &&
    response.status() === 404
  )
}

export function installBrowserGuards(page: Page): BrowserGuards {
  const guards: BrowserGuards = {
    consoleErrors: [],
    criticalRequestFailures: [],
    pageErrors: [],
  }
  let expectedInvalidLocale404Observed = false
  let expectedInvalidLocale404ConsoleConsumed = false

  page.on("console", (message) => {
    const isExpectedInvalidLocale404Console =
      !expectedInvalidLocale404ConsoleConsumed &&
      expectedInvalidLocale404Observed &&
      message.type() === "error" &&
      message.text() === expectedInvalidLocale404ConsoleMessage &&
      message.location().url === expectedInvalidLocaleDocumentUrl

    if (isExpectedInvalidLocale404Console) {
      expectedInvalidLocale404ConsoleConsumed = true
      return
    }

    if (message.type() === "error") {
      guards.consoleErrors.push(message.text())
    }
  })

  page.on("requestfailed", (request) => {
    if (criticalResourceTypes.has(request.resourceType())) {
      guards.criticalRequestFailures.push(
        `${request.method()} ${request.url()} (${request.failure()?.errorText ?? "unknown"})`
      )
    }
  })

  page.on("response", (response) => {
    if (isExpectedInvalidLocaleDocument404(response)) {
      expectedInvalidLocale404Observed = true
      return
    }

    if (
      criticalResourceTypes.has(response.request().resourceType()) &&
      response.status() >= 400
    ) {
      guards.criticalRequestFailures.push(
        `${response.status()} ${response.url()}`
      )
    }
  })

  page.on("pageerror", (error) => {
    guards.pageErrors.push(`${error.name}: ${error.message}`)
  })

  return guards
}

export function assertNoBrowserFailures(guards: BrowserGuards) {
  expect(guards.consoleErrors).toEqual([])
  expect(guards.criticalRequestFailures).toEqual([])
  expect(guards.pageErrors).toEqual([])
}
