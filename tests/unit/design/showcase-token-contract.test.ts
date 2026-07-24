import { readFileSync } from "node:fs"
import { resolve } from "node:path"

import { describe, expect, it } from "vitest"

const css = readFileSync(resolve("app/globals.css"), "utf8")
const button = readFileSync(resolve("components/ui/button.tsx"), "utf8")

const normalizedCss = css
  .replace(/\s+/g, " ")
  .replace(/\(\s+/g, "(")
  .replace(/\s+\)/g, ")")

const semanticColors: Record<string, string> = {
  "--color-background": "var(--ge-ivory-100)",
  "--color-foreground": "var(--ge-slate-950)",
  "--color-surface": "var(--ge-ivory-50)",
  "--color-surface-subtle": "var(--ge-limestone-100)",
  "--color-card": "var(--ge-ivory-50)",
  "--color-card-foreground": "var(--ge-slate-950)",
  "--color-popover": "var(--ge-white)",
  "--color-popover-foreground": "var(--ge-slate-950)",
  "--color-primary": "var(--ge-blue-800)",
  "--color-primary-hover": "var(--ge-blue-900)",
  "--color-primary-active": "var(--ge-blue-950)",
  "--color-primary-foreground": "var(--ge-white)",
  "--color-primary-subtle": "var(--ge-blue-100)",
  "--color-accent": "var(--ge-teal-700)",
  "--color-accent-hover": "var(--ge-teal-800)",
  "--color-accent-subtle": "var(--ge-teal-100)",
  "--color-accent-foreground": "var(--ge-slate-950)",
  "--color-muted": "var(--ge-limestone-100)",
  "--color-muted-foreground": "var(--ge-slate-600)",
  "--color-border": "var(--ge-limestone-200)",
  "--color-border-strong": "var(--ge-sand-200)",
  "--color-input": "var(--ge-limestone-200)",
  "--color-ring": "var(--ge-teal-700)",
  "--color-link": "var(--ge-blue-800)",
  "--color-link-hover": "var(--ge-blue-950)",
  "--color-disabled-bg": "var(--ge-limestone-100)",
  "--color-disabled-fg": "var(--ge-slate-500)",
  "--color-success": "var(--ge-success-700)",
  "--color-success-subtle": "var(--ge-success-100)",
  "--color-warning": "var(--ge-warning-800)",
  "--color-warning-subtle": "var(--ge-warning-100)",
  "--color-destructive": "var(--ge-error-700)",
  "--color-destructive-subtle": "var(--ge-error-100)",
  "--color-info": "var(--ge-info-700)",
  "--color-info-subtle": "var(--ge-info-100)",
  "--color-overlay": "rgb(0 0 0 / 0.6)",
  "--color-hero-foreground": "var(--ge-white)",
  "--color-hero-scrim":
    "linear-gradient(180deg, rgb(0 0 0 / 0.08), rgb(0 0 0 / 0.68))",
}

describe("Greek Essence CSS-first token contract", () => {
  it("maps every documented semantic color token to its exact authoritative value", () => {
    for (const [name, value] of Object.entries(semanticColors)) {
      expect(normalizedCss).toContain(`${name}: ${value};`)
    }
  })

  it("defines the remaining reusable documented inventory with exact values", () => {
    const required = [
      "--ge-ivory-50: #fffcf6",
      "--ge-ivory-100: #faf6ed",
      "--ge-limestone-100: #f1ede3",
      "--ge-limestone-200: #e6dfd2",
      "--ge-sand-200: #d8c8ad",
      "--ge-sand-500: #9b7c55",
      "--ge-blue-950: #0b2433",
      "--ge-blue-900: #103348",
      "--ge-blue-800: #17475f",
      "--ge-blue-700: #215b72",
      "--ge-blue-100: #dceaf0",
      "--ge-teal-800: #275f63",
      "--ge-teal-700: #34767a",
      "--ge-teal-100: #dcebe8",
      "--ge-olive-700: #5d684b",
      "--ge-olive-100: #e7e9de",
      "--ge-slate-950: #172126",
      "--ge-slate-800: #2d393e",
      "--ge-slate-600: #59666b",
      "--ge-slate-500: #707c80",
      "--ge-slate-300: #bfc7c8",
      "--ge-white: #ffffff",
      "--ge-black: #000000",
      "--ge-success-700: #2f6b4f",
      "--ge-success-100: #e1efe7",
      "--ge-warning-800: #7a5725",
      "--ge-warning-100: #f4e8cf",
      "--ge-error-700: #a13b39",
      "--ge-error-100: #f7e3e1",
      "--ge-info-700: #2e607a",
      "--ge-info-100: #e0edf3",
      "--space-0: 0",
      "--space-5: 1.25rem",
      "--space-10: 2.5rem",
      "--space-20: 5rem",
      "--space-32: 8rem",
      "--space-40: 10rem",
      "--container-prose: 45rem",
      "--container-narrow: 55rem",
      "--container-content: 70rem",
      "--container-wide: 80rem",
      "--container-hero: 90rem",
      "--page-gutter: clamp(1.25rem, 3.5vw, 5rem)",
      "--radius-xs: 0.25rem",
      "--radius-sm: 0.5rem",
      "--radius-md: 0.625rem",
      "--radius-lg: 0.75rem",
      "--radius-xl: 1rem",
      "--radius-2xl: 1.25rem",
      "--radius-3xl: 1.5rem",
      "--radius-full: 9999px",
      "--shadow-none: none",
      "--shadow-xs: 0 1px 2px rgb(11 36 51 / 0.05)",
      "--shadow-sm: 0 6px 18px rgb(11 36 51 / 0.08)",
      "--shadow-md: 0 12px 32px rgb(11 36 51 / 0.12)",
      "--shadow-lg: 0 24px 64px rgb(11 36 51 / 0.18)",
      "--ease-standard: cubic-bezier(0.2, 0, 0, 1)",
      "--ease-emphasized: cubic-bezier(0.2, 0.8, 0.2, 1)",
      "--ease-exit: cubic-bezier(0.4, 0, 1, 1)",
      "--focus-width: 2px",
      "--focus-offset: 2px",
      "--state-hover: var(--ge-blue-900)",
      "--state-selected: var(--ge-teal-100)",
      "--state-disabled: var(--ge-limestone-100)",
      "--state-loading: var(--ge-info-100)",
      "--state-error: var(--ge-error-100)",
      "--state-success: var(--ge-success-100)",
      "--state-unavailable: var(--ge-limestone-100)",
      "--text-display-1:",
      "--text-display-2:",
      "--text-heading-1:",
      "--text-heading-2:",
      "--text-heading-3:",
      "--text-heading-4:",
      "--text-title-lg:",
      "--text-title-md:",
      "--text-body-lg:",
      "--text-body-md:",
      "--text-body-sm:",
      "--text-label-lg:",
      "--text-label-md:",
      "--text-label-sm:",
      "--text-caption:",
      "--text-eyebrow:",
      "--text-quote:",
    ]
    for (const token of required) expect(css, token).toContain(token)
  })

  it("is light-only with no parallel dark branch", () => {
    expect(css).not.toMatch(/\.dark\b|prefers-color-scheme:\s*dark/)
    expect(button).not.toContain("dark:")
  })
})
