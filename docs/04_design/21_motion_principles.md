
# Part IX — Motion and Interaction States

## 21. Motion Principles

Motion supports orientation, feedback, and hierarchy. It does not create spectacle.

### 21.1 Motion tokens

| Use case | Duration | Easing | Reduced motion | Forbidden behavior |
|---|---:|---|---|---|
| Hover color | 120 ms | `ease-out` | instant | delayed hover |
| Button press | 90 ms | `ease-out` | instant | bounce |
| Focus appearance | 0–100 ms | linear/ease-out | unchanged | animated ring loops |
| Menu open/close | 160–200 ms | standard deceleration | near-instant fade | slide across full viewport slowly |
| Accordion | 180–220 ms | ease-in-out | instant reveal | forcing one-at-a-time closure |
| Popover/dialog | 160–220 ms | ease-out | fade/instant | scale from tiny size |
| Card hover | 140–180 ms | ease-out | color/border only | large lift |
| Image reveal | 220–320 ms | ease-out | no transform | blur-heavy reveal |
| Header transition | 160–200 ms | ease-out | instant state | excessive shrink |
| Form step transition | 160–220 ms | ease-out | instant/crossfade | horizontal wizard swipe |
| Status feedback | 140–180 ms | ease-out | immediate | celebration/confetti |
| Gallery navigation | 180–240 ms | ease-in-out | instant | autoplay |

### 21.2 Easing tokens

```css
--ease-standard: cubic-bezier(0.2, 0, 0, 1);
--ease-emphasized: cubic-bezier(0.2, 0.8, 0.2, 1);
--ease-exit: cubic-bezier(0.4, 0, 1, 1);
```

### 21.3 Reduced motion

Under `prefers-reduced-motion: reduce`:

- remove non-essential transforms;
- remove parallax;
- stop auto movement;
- use instant state changes or brief opacity fades;
- preserve focus and interaction feedback;
- do not disable necessary progress/status communication.

---


