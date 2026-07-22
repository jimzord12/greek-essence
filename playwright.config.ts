import { defineConfig } from "@playwright/test"

export default defineConfig({
  testDir: "./tests/e2e",
  outputDir: ".artifacts/bootstrap/playwright/test-results",
  timeout: 30_000,
  retries: 0,
  reporter: [
    ["list"],
    [
      "html",
      { outputFolder: ".artifacts/bootstrap/playwright/report", open: "never" },
    ],
  ],
  use: {
    baseURL: "http://127.0.0.1:3100",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
  webServer: {
    command: "pnpm dev --port 3100",
    url: "http://127.0.0.1:3100",
    timeout: 120_000,
    reuseExistingServer: !process.env.CI,
  },
  projects: [
    {
      name: "chromium-compact",
      use: { browserName: "chromium", viewport: { width: 390, height: 844 } },
    },
    {
      name: "chromium-medium",
      use: { browserName: "chromium", viewport: { width: 834, height: 1112 } },
    },
    {
      name: "chromium-wide",
      use: { browserName: "chromium", viewport: { width: 1440, height: 1024 } },
    },
  ],
})
