#!/usr/bin/env bash
set -euo pipefail

repo_root=$(git rev-parse --show-toplevel)
work=$(mktemp -d)
cleanup() {
  rm -rf "$work"
  if [ -e "$work" ]; then
    printf 'cleanup_result=failed path=%s\n' "$work"
    return 1
  fi
  printf 'cleanup_result=removed path=%s\n' "$work"
}
trap cleanup EXIT

printf 'repo_root=%s\n' "$repo_root"
printf 'temporary_workdir=%s\n' "$work"

printf '\n== Wrapper help ==\n'
DISABLE_TELEMETRY=1 npx modern-web-guidance@latest --help

printf '\n== Wrapper package and install delegation ==\n'
(
  cd "$work"
  npm pack --silent modern-web-guidance@0.0.177 >/dev/null
  archive=$(printf '%s\n' modern-web-guidance-*.tgz)
  mkdir wrapper
  tar -xzf "$archive" -C wrapper --strip-components=1
  node -e "const p=require('./wrapper/package.json'); console.log(JSON.stringify({version:p.version,repository:p.repository,license:p.license,bin:p.bin},null,2))"
  grep -n -F 'const installArgs = `-y skills add GoogleChrome/modern-web-guidance ${values.choose ? "" : "--skill modern-web-guidance"}`.split(" ").filter(Boolean);' wrapper/skills/modern-web-guidance/modern-web.mjs
)

printf '\n== Official repository release and complete core layout ==\n'
git clone --quiet https://github.com/GoogleChrome/modern-web-guidance.git "$work/upstream"
git -C "$work/upstream" checkout --quiet --detach 79aae1e0bed948e48fd78b58538c5ee1e6463da9
git -C "$work/upstream" show -s --format='commit=%H%nsubject=%s' HEAD
mkdir "$work/upstream-export"
git -C "$work/upstream" archive HEAD | tar -x -C "$work/upstream-export"
printf 'core_file_count='
find "$work/upstream-export/skills/modern-web-guidance" -type f | wc -l
printf 'guide_categories=\n'
find "$work/upstream-export/skills/modern-web-guidance/guides" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort
for path in \
  skills/chrome-extensions \
  skills/modern-web-guidance/guides/security/passkeys.md \
  skills/modern-web-guidance/guides/webmcp \
  THIRD_PARTY_NOTICES; do
  if [ -e "$work/upstream-export/$path" ]; then
    printf 'upstream_present=%s\n' "$path"
  else
    printf 'upstream_absent=%s\n' "$path"
  fi
done

printf '\n== Underlying official installer output ==\n'
mkdir "$work/installer-output"
(
  cd "$work/installer-output"
  DISABLE_TELEMETRY=1 npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy
)
printf 'generated_core_files_by_target=\n'
for target in .agents .claude .hermes .trae; do
  target_path="$work/installer-output/$target/skills/modern-web-guidance"
  test -d "$target_path"
  printf '%s=' "$target"
  find "$target_path" -type f | wc -l
  test "$(find "$target_path" -type f | wc -l | tr -d '[:space:]')" = 139
done
printf 'generated_targets=\n'
find "$work/installer-output" -type f -path '*/skills/modern-web-guidance/*' -printf '%P\n' | sort

printf '\n== Selected local runtime-search layout and source comparisons ==\n'
local_skill="$repo_root/.agents/skills/modern-web-guidance"
test "$(find "$local_skill" -maxdepth 1 -type f | wc -l | tr -d '[:space:]')" = 3
test -f "$local_skill/SKILL.md"
test -f "$local_skill/LICENSE"
test -f "$local_skill/THIRD_PARTY_NOTICES"
test ! -e "$repo_root/.agents/skills/chrome-extensions"
test ! -e "$local_skill/guides/security/passkeys.md"
test ! -e "$local_skill/guides/webmcp"
printf 'local_selected_files=\n'
find "$local_skill" -maxdepth 1 -type f -printf '%f\n' | sort
cmp "$local_skill/SKILL.md" "$work/wrapper/skills/modern-web-guidance/SKILL.md"
cmp "$local_skill/LICENSE" "$work/wrapper/LICENSE"
cmp "$local_skill/THIRD_PARTY_NOTICES" "$work/wrapper/THIRD_PARTY_NOTICES"
diff -u <(tr -d '\r' < "$local_skill/SKILL.md") <(tr -d '\r' < "$work/upstream-export/skills/modern-web-guidance/SKILL.md")
diff -u <(tr -d '\r' < "$local_skill/LICENSE") <(tr -d '\r' < "$work/upstream-export/LICENSE")
printf 'selected_files_match_wrapper_bytes=yes\n'
printf 'skill_and_license_match_upstream_after_crlf_normalization=yes\n'
printf 'third_party_notice_source=wrapper_package_only\n'

printf '\n== Corrected record assertions ==\n'
readme="$repo_root/.agents/README.md"
for text in \
  '79aae1e0bed948e48fd78b58538c5ee1e6463da9' \
  'Release v0.0.177' \
  '139 files' \
  'npx -y skills add GoogleChrome/modern-web-guidance --skill modern-web-guidance --yes --copy' \
  'Selected three-file local runtime-search design' \
  'No local guide/reference is required' \
  'Separately excluded optional disciplines'; do
  grep -F "$text" "$readme" >/dev/null
done
printf 'README_corrected_provenance_and_selection_fields=yes\n'

printf '\n== Cleanup ==\n'
printf 'cleanup_scheduled_for=%s\n' "$work"
