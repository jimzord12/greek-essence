import { readFileSync } from "node:fs"
import { resolve } from "node:path"
import { fileURLToPath } from "node:url"

export const HOME_LCP_CEILING_MS = 2500

export function assertHomeLcpCeiling(reports) {
  for (const route of ["/en", "/el"]) {
    const report = reports.find((candidate) => candidate.route === route)
    if (!report || !Number.isFinite(report.lcp)) {
      throw new Error(`Missing valid Unlighthouse LCP report for ${route}`)
    }
    if (report.lcp > HOME_LCP_CEILING_MS) {
      throw new Error(
        `${route} LCP ${report.lcp}ms exceeds ${HOME_LCP_CEILING_MS}ms`
      )
    }
  }
}

export function readHomeLcpReports(
  outputPath = ".artifacts/bootstrap/unlighthouse"
) {
  return ["en", "el"].map((locale) => {
    const report = JSON.parse(
      readFileSync(
        resolve(outputPath, "reports", locale, "lighthouse.json"),
        "utf8"
      )
    )
    return {
      route: `/${locale}`,
      lcp: report.audits?.["largest-contentful-paint"]?.numericValue,
    }
  })
}

if (
  process.argv[1] &&
  resolve(process.argv[1]) === fileURLToPath(import.meta.url)
) {
  const reports = readHomeLcpReports(process.argv[2])
  assertHomeLcpCeiling(reports)
  for (const report of reports)
    console.log(`${report.route} LCP: ${report.lcp}ms`)
}
