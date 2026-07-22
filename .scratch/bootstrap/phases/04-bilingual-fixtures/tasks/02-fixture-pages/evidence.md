# B04-02 evidence

## Environment

- `node --version` → exit 0, `v24.18.0`
- `pnpm --version` → exit 0, `10.33.0`
- `playwright-cli --version` → exit 0, `0.1.14`

## Required checks

1. `pnpm lint`
   - Exit 0.
   - Result: no errors; pre-existing warning in `commitlint.config.mjs` for anonymous default export.

2. `pnpm typecheck`
   - First execution: exit 2. Next.js generated route types had not yet included the newly created nested route (`PageProps<"/[locale]/quality-lab">`).
   - `pnpm build` regenerated the route types successfully (see below).
   - Affected re-check: `pnpm typecheck` → exit 0.

3. `pnpm build`
   - Exit 0.
   - Result: static routes generated for `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab`.

4. `pnpm start --port 3101`
   - Started a production server for browser verification; ready output confirmed `http://localhost:3101`.
   - Stopped after verification.

5. `playwright-cli -s=b0402 close && playwright-cli -s=b0402 open http://localhost:3101/en && playwright-cli -s=b0402 run-code "async (page) => { const pages=['/en','/el','/en/quality-lab','/el/quality-lab']; const widths=[320,390,834,1440]; const failures=[]; const consoleErrors=[]; page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); }); await page.emulateMedia({reducedMotion:'reduce'}); for (const width of widths) { await page.setViewportSize({width,height:900}); for (const path of pages) { const response=await page.goto('http://localhost:3101'+path); await page.getByRole('heading',{level:1}).waitFor(); if (!response || !response.ok()) failures.push(width+path+': non-OK document response'); if (await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) failures.push(width+path+': horizontal overflow'); }} await page.goto('http://localhost:3101/en/quality-lab'); const button=page.getByRole('button'); await button.focus(); if (await page.evaluate(() => document.activeElement?.tagName) !== 'BUTTON') failures.push('keyboard focus missing'); await button.press('Space'); if (await button.getAttribute('aria-pressed') !== 'true') failures.push('keyboard toggle failed'); await page.evaluate(() => { document.documentElement.style.fontSize='200%'; }); if (await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) failures.push('200% text zoom overflow'); if (consoleErrors.length) failures.push('console errors: '+consoleErrors.join(' | ')); if (failures.length) throw new Error(failures.join('; ')); console.log('B04-02 browser smoke passed: 16 route/viewport checks, keyboard toggle, reduced motion, and 200% text zoom.'); }" && playwright-cli -s=b0402 console error`
   - Exit 0.
   - Result: production browser smoke passed all four localized routes at 320, 390, 834, and 1440 px; all document responses were OK; no horizontal overflow; keyboard focus and Space activation set `aria-pressed="true"`; reduced-motion media was emulated; root text size was set to 200% with no overflow; console error count was zero.

## Artifact policy

- `git check-ignore -v .artifacts/bootstrap` → exit 0: `.gitignore:40:.artifacts/bootstrap/`.
- Playwright CLI transient `.playwright-cli/` snapshots were deleted after verification because that directory is not ignored. No generated browser artifacts are retained.

## Review cycle 01 correction checks

1. `pnpm exec prettier --write "app/[locale]/layout.tsx" "app/[locale]/page.tsx" "app/[locale]/quality-lab/page.tsx"`
   - Exit 0. Only `app/[locale]/quality-lab/page.tsx` changed formatting.

2. `rm -rf .playwright-cli && pnpm exec prettier --write components/fixture-toggle.tsx && pnpm format:check && pnpm build`
   - Exit 0.
   - Result: affected toggle file was formatted; `pnpm format:check` passed; static `/en`, `/el`, `/en/quality-lab`, and `/el/quality-lab` rebuilt successfully. An earlier `pnpm format:check` exit 1 was caused solely by unignored transient `.playwright-cli/*.yml` snapshots; they were deleted before the passing re-check.

3. `pnpm start --port 3101`
   - Production server started and reported ready at `http://localhost:3101`; stopped after smoke verification.

4. `playwright-cli -s=b0402-r01 open http://localhost:3101/en && playwright-cli -s=b0402-r01 run-code "async (page) => { const pages=['/en','/el','/en/quality-lab','/el/quality-lab']; const widths=[320,390,834,1440]; const failures=[]; const consoleErrors=[]; page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); }); await page.emulateMedia({reducedMotion:'reduce'}); for (const width of widths) { await page.setViewportSize({width,height:900}); for (const path of pages) { const response=await page.goto('http://localhost:3101'+path); await page.getByRole('heading',{level:1}).waitFor(); const expectedLocale=path.split('/')[1]; if (!response || !response.ok()) failures.push(width+path+': non-OK document response'); if (await page.locator('h1').count() !== 1) failures.push(width+path+': H1 count'); if (await page.locator('html').getAttribute('lang') !== expectedLocale) failures.push(width+path+': locale mismatch'); if (await page.evaluate(() => document.styleSheets.length === 0)) failures.push(width+path+': stylesheet absent'); if (await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) failures.push(width+path+': base horizontal overflow'); const targets=await page.locator('a,button').all(); for (const target of targets) { await target.focus(); const box=await target.boundingBox(); if (!box || box.width < 44 || box.height < 44) failures.push(width+path+': target below 44px'); } await page.evaluate(() => { document.documentElement.style.fontSize='200%'; }); if (await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) failures.push(width+path+': 200% text zoom overflow'); }} await page.goto('http://localhost:3101/en/quality-lab'); const button=page.getByRole('button'); await button.focus(); await page.waitForTimeout(200); const focus=await button.evaluate((element) => { const style=getComputedStyle(element); return {width:style.outlineWidth,offset:style.outlineOffset,color:style.outlineColor}; }); if (focus.width !== '2px' || focus.offset !== '2px' || focus.color !== 'lab(44.4134 -33.1436 -4.22149)') failures.push('focus treatment mismatch: '+JSON.stringify(focus)); await button.press('Space'); if (await button.getAttribute('aria-pressed') !== 'true') failures.push('keyboard Space toggle failed'); if (consoleErrors.length) failures.push('console errors: '+consoleErrors.join(' | ')); if (failures.length) throw new Error(failures.join('; ')); }" && playwright-cli -s=b0402-r01 console error`
   - Exit 0.
   - Result: all 16 route/viewport document responses were OK; each page had one H1 and matching `lang`; the stylesheet loaded; every inspected link/button target was at least 44×44 CSS px; reduced motion was emulated; 200% root-text reflow had no horizontal overflow; focused toggle computed `2px` outline width, `2px` offset, and teal `lab(44.4134 -33.1436 -4.22149)`; Space set `aria-pressed="true"`; console error count was zero.

## Assumptions and deviations

- None. The 200% zoom smoke emulates text zoom by setting the root font size to `200%`; it verifies text reflow without relying on browser UI zoom controls.

## Root closure verification

- `git diff --check` → exit 0.
- `pnpm check` → exit 1 after `format:check`, `lint`, and `typecheck` passed; the later `test:unit` step could not start because Vitest is not installed until B05-01. Unit testing is outside verification row B04-02, so this future-phase aggregate failure does not replace or invalidate the passing B04-02 browser, format, build, lint, and type checks above.
- Independent re-review 02 approved both cycle-01 High corrections with zero remaining Blocking, High, or Non-blocking findings.
