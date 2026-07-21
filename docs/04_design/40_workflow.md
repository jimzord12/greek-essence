
# Part XVII — Design QA

## 40. Workflow

### 40.1 Design review stages

1. **Foundation review**  
   Fonts, colors, typography, spacing, grid, radii, borders, shadows.

2. **Primitive review**  
   Buttons, fields, choices, menu, accordion, dialog, status.

3. **Composition review**  
   C-01 through C-30 representative states.

4. **Page review**  
   Home, one destination detail, one journey detail, About, FAQ, Contact, Plan My Trip.

5. **Bilingual review**  
   English/Greek navigation, headings, cards, form fields, errors, confirmation.

6. **Responsive review**  
   320, 390, 834, 1440, intermediate widths, 200% zoom.

7. **Accessibility review**  
   contrast, focus, keyboard, forced colors, reduced motion, target sizes.

8. **Performance/art review**  
   final representative imagery, font payload, LCP, CLS.

### 40.2 Visual regression

At minimum, capture:

- Home compact/wide;
- solid and overlay header;
- open compact menu;
- one destination detail compact/wide;
- one journey detail;
- FAQ expanded state;
- Contact validation error;
- each Plan My Trip step compact/wide;
- form error summary;
- saved draft state;
- submission failure;
- confirmation;
- English and Greek variants;
- reduced-motion state where visually different;
- unavailable translation/content state.

Use deterministic data and stable representative images.

### 40.3 Visual QA checklist

- no raw colors or unapproved spacing;
- typography roles used correctly;
- one H1;
- line lengths controlled;
- Greek text does not truncate;
- focus visible;
- primary CTA unique and dominant;
- cards do not resemble commerce listings;
- no accidental dark-theme styles;
- imagery has correct focal crop;
- text-over-image contrast passes;
- no unapproved trust marks;
- borders and shadows remain restrained;
- decorative motif is not overused;
- no horizontal page overflow;
- no layout shift from fonts/media;
- status is not color-only;
- form states preserve hierarchy;
- mobile targets remain usable.

---


