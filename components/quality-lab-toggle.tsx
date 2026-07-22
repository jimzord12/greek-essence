"use client"

import dynamic from "next/dynamic"

import type { FixtureToggleProps } from "./fixture-toggle"

const FixtureToggle = dynamic(
  () => import("./fixture-toggle").then((module) => module.FixtureToggle),
  { ssr: false }
)

export function QualityLabToggle(props: FixtureToggleProps) {
  return <FixtureToggle {...props} />
}
