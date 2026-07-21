
# Part X — Core Controls

## 23. Buttons and CTA Hierarchy

### 23.1 Anatomy

- container;
- label;
- optional start/end icon;
- focus ring;
- loading indicator;
- optional count/status only when necessary.

### 23.2 Sizes

| Size | Height | Horizontal padding | Typography | Icon |
|---|---:|---:|---|---:|
| Small | 36 px | 14 px | label-sm/md | 16 px |
| Medium | 44 px | 18 px | label-md | 18–20 px |
| Large | 52 px | 24 px | label-lg | 20 px |
| Hero | 56 px | 28 px | label-lg | 20 px |

Touch targets should normally meet or exceed 44 × 44 px.

### 23.3 Variants

#### Primary

- background: `primary`;
- foreground: `primary-foreground`;
- radius: `radius-md`;
- shadow: `shadow-xs`;
- hover: `primary-hover`, optional 1 px lift;
- active: `primary-active`, no lift;
- focus: teal ring;
- disabled: disabled tokens.

Used for `Plan My Trip`, final submit, and one dominant action per section.

#### Secondary

- transparent or surface background;
- primary text;
- soft primary/neutral border;
- hover uses primary subtle tint;
- no strong shadow.

Used for consultation or meaningful secondary exploration.

#### Tertiary/ghost

- transparent;
- foreground or primary text;
- hover uses muted surface;
- underline may be appropriate.

#### Destructive

Reserved for actual destructive actions such as clearing a saved form. It must not visually dominate normal flow.

### 23.4 Link styles

- Inline prose links are underlined with controlled offset and thickness.
- Navigation links use active state plus non-color cue.
- Card links may use whole-card treatment if nested actions are avoided.
- External contact links clearly name their channel.
- Avoid “click here.”

---


