import { fireEvent, render, screen } from "@testing-library/react"
import { describe, expect, it } from "vitest"

import { FixtureToggle } from "@/components/fixture-toggle"

describe("FixtureToggle", () => {
  it("announces the selected state after interaction", () => {
    render(
      <FixtureToggle
        label="Not selected"
        selectedLabel="Selected"
        statusLabel="Current state"
      />
    )

    const toggle = screen.getByRole("button", { name: "Not selected" })
    expect(toggle.getAttribute("aria-pressed")).toBe("false")
    expect(screen.getByText("Current state: Not selected")).not.toBeNull()

    fireEvent.click(toggle)

    expect(
      screen
        .getByRole("button", { name: "Selected" })
        .getAttribute("aria-pressed")
    ).toBe("true")
    expect(screen.getByText("Current state: Selected")).not.toBeNull()
  })
})
