## 9. Navigation and Language Switching

The logo returns to locale Home. The header renders crawlable primary links in the Prototype’s specified order. Wide submenus open only through explicit activation, expose expanded state, work by keyboard, and close on Escape, navigation, or click/tap outside. Compact menu opening returns focus reliably to its trigger when closed and does not leave background controls reachable.

Language switching uses `next-intl` routing plus the content stable ID:

- detail page → equivalent localized detail route;
- index/static page → same equivalent route;
- missing translation → explained C-30 recovery state;
- Plan My Trip → switch labels/options, retain local draft values, and announce saved draft state;
- values such as names, dates, notes, and contact details are not translated;
- stored option IDs re-render as labels in the selected locale.

There is no global application state library. Server routes/data own page state; small client components own their own state; form state remains inside the form feature.

---

