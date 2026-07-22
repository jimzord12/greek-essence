"use client"

import { useState } from "react"

import { Button } from "@/components/ui/button"

type FixtureToggleProps = {
  label: string
  selectedLabel: string
  statusLabel: string
}

export function FixtureToggle({
  label,
  selectedLabel,
  statusLabel,
}: FixtureToggleProps) {
  const [selected, setSelected] = useState(false)

  return (
    <div className="space-y-3">
      <Button
        aria-pressed={selected}
        className="min-h-11 px-4 focus:outline-2 focus:outline-offset-2 focus:outline-teal-700 motion-reduce:transition-none motion-reduce:duration-0"
        onClick={() => setSelected((value) => !value)}
        type="button"
        variant={selected ? "secondary" : "outline"}
      >
        {selected ? selectedLabel : label}
      </Button>
      <p aria-live="polite" className="text-sm text-muted-foreground">
        {statusLabel}: {selected ? selectedLabel : label}
      </p>
    </div>
  )
}
