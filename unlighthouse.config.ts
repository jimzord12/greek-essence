const unlighthouseConfig = {
  site: "http://127.0.0.1:3101/en",
  outputPath: ".artifacts/bootstrap/unlighthouse",
  scanner: {
    device: "mobile",
    samples: 3,
    include: ["/en", "/el", "/en/quality-lab", "/el/quality-lab"],
    sitemap: false,
    robotsTxt: false,
    dynamicSampling: false,
  },
  lighthouseOptions: {
    skipAudits: ["is-crawlable"],
    // Lighthouse's Lantern simulator currently inflates text LCP from ~150 ms
    // observed to ~4.9 s on Windows/Chrome 150, including on the unchanged
    // quality-lab route. DevTools throttling preserves the mobile profile while
    // measuring the actual throttled browser timeline.
    throttlingMethod: "devtools",
  },
  ci: {
    budget: {
      performance: 90,
      accessibility: 100,
      bestPractices: 95,
      seo: 95,
    },
  },
}

export default unlighthouseConfig
