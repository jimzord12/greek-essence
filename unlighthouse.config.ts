export default {
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
