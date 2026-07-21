
# Part XV — shadcn/ui + Base UI

## 38. Customization Strategy

shadcn/ui is source-owned component code, not a visual system to accept unchanged.

Base UI provides behavior and accessible primitives. Greek Essence owns visual styling.

### 38.1 Primitive layer

`components/ui/` contains:

- button;
- input;
- textarea;
- select/combobox;
- checkbox;
- radio group;
- dialog;
- popover;
- accordion;
- tooltip;
- navigation menu where used;
- progress;
- separator;
- status/badge primitives where justified.

These components:

- consume semantic tokens;
- expose controlled variants;
- contain no Greek Essence business content;
- remain easy to compare against upstream updates;
- preserve Base UI semantics and keyboard behavior.

### 38.2 Composition layer

`components/layout`, `components/sections`, and `components/forms` contain Greek Essence-specific compositions.

Examples:

- `GlobalHeader`
- `DestinationCard`
- `JourneyCard`
- `Hero`
- `TripRequestStepper`
- `TripRequestFieldGroup`
- `TrustCredential`
- `PrimaryCtaBlock`

### 38.3 Upgradeability rules

- Do not casually rewrite primitive internals.
- Prefer wrappers and variants.
- Keep upstream component attribution/history where generated.
- Review upstream changes before regeneration.
- Run visual regression and keyboard tests after upgrades.
- Do not allow generated defaults to reintroduce gray SaaS styling, excessive radii, or mismatched focus rings.
- Base UI component behavior remains authoritative unless the Prototype explicitly requires different behavior.

### 38.4 Variant ownership

Use `cva` or an equivalent small variant helper where it improves consistency.

Variants should represent meaningful visual contracts:

- button intent and size;
- card type;
- hero type;
- surface tone;
- status intent;
- form control state.

Avoid “style prop” APIs that permit arbitrary token combinations from page code.

---


