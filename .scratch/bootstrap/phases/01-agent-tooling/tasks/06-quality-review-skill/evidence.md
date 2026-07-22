# B01-06 evidence

## Decisive verification

- Command: `python -c "from pathlib import Path; import re; root=Path('.'); skill=root/'.agents/skills/greek-essence-quality-review'; required=['visual-review-checklist.md','responsive-review-checklist.md','accessibility-review-checklist.md','seo-localization-review-checklist.md','form-quality-security-review-checklist.md']; files=[skill/'SKILL.md']+[skill/'references'/n for n in required]; assert list(skill.glob('SKILL.md'))==[skill/'SKILL.md']; assert sorted(p.name for p in (skill/'references').glob('*.md'))==sorted(required); text=files[0].read_text(encoding='utf-8'); assert re.search(r'^name: greek-essence-quality-review$', text, re.M); assert re.search(r'^description: .+', text, re.M); headings=['1. Blocking defects','2. High-impact quality issues','3. Accessibility issues','4. Responsive issues','5. English/Greek issues','6. Performance or implementation risks','7. Suggested permanent tests','8. Evidence: route, locale, viewport, screenshot or trace, and reproduction steps']; positions=[text.index(h) for h in headings]; assert positions==sorted(positions); assert all('Playwright CLI' in p.read_text(encoding='utf-8') for p in files); links=[]; [links.extend(re.findall(r'\[[^]]+\]\(([^)]+)\)', p.read_text(encoding='utf-8'))) for p in files]; assert links and all((p.parent/link).resolve().is_file() for p in files for link in re.findall(r'\[[^]]+\]\(([^)]+)\)', p.read_text(encoding='utf-8'))); assert '../../../docs/01_prd/index.md' in text and '../../../docs/02_prototype_specification/index.md' in text and '../../../docs/03_technical_design/index.md' in text; print('B01-06 structural review: PASS; SKILL.md=1; references=5; ordered_output=8; modular_links='+str(len(links)))"`
- Exit code: `0`
- Result: `B01-06 structural review: PASS; SKILL.md=1; references=5; ordered_output=8; modular_links=37`
- Artifact paths: none generated; structural assertions ran against `.agents/skills/greek-essence-quality-review/SKILL.md` and `.agents/skills/greek-essence-quality-review/references/`.

## Notes

Live rendered validation is assigned to B06-03 by this task's acceptance criteria and was not run.
