#!/bin/bash

PASS=0
FAIL=0

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

assert_version() {
  local commit_msg="$1"
  local current_version="$2"
  local stage="$3"
  local expected="$4"

  result=$(bash "$SCRIPT_DIR/../scripts/calculate-version.sh" "$commit_msg" "$current_version" "$stage")

  if [ "$result" = "$expected" ]; then
    echo "✓ $commit_msg | $current_version | $stage → $result"
    PASS=$((PASS + 1))
  else
    echo "✗ $commit_msg | $current_version | $stage → got $result, expected $expected"
    FAIL=$((FAIL + 1))
  fi
}

echo "Running versioning tests..."
echo ""

assert_version "docs: initial commit" "0.0.1" "dev" "0.0.1-dev.1"
assert_version "fix: bug fix" "0.0.1-dev.1" "dev" "0.0.1-dev.2"
assert_version "feat: add feature" "0.0.1-dev.5" "dev" "0.1.0-dev.1"
assert_version "fix!: breaking change" "0.1.0-dev.3" "dev" "1.0.0-dev.1"
assert_version "feat: new feature" "0.0.1" "alpha" "0.1.0-alpha.1"
assert_version "docs: update docs" "0.1.0-alpha.1" "alpha" "0.1.0-alpha.2"
assert_version "feat!: major alpha" "0.1.0-alpha.3" "alpha" "1.0.0-alpha.1"
assert_version "fix: bug" "0.1.0-alpha.3" "beta" "0.1.0-beta.1"
assert_version "feat: minor beta" "0.1.0-beta.1" "beta" "0.2.0-beta.1"
assert_version "fix!: major beta" "0.2.0-beta.1" "beta" "1.0.0-beta.1"
assert_version "fix: critical" "0.1.0-beta.2" "rc" "0.1.0-rc.1"
assert_version "chore: cleanup" "0.1.0-rc.1" "rc" "0.1.0-rc.2"
assert_version "feat: minor rc" "0.1.0-rc.2" "rc" "0.2.0-rc.1"
assert_version "fix!: major rc" "0.2.0-rc.1" "rc" "1.0.0-rc.1"
assert_version "fix: final bug" "0.1.0-rc.2" "" "0.1.0"
assert_version "docs: patch stable" "0.1.0" "" "0.1.0"
assert_version "feat: minor stable" "0.1.0" "" "0.2.0"
assert_version "fix!: major stable" "0.2.0" "" "1.0.0"
assert_version "feat: after release" "0.1.0" "dev" "0.2.0-dev.1"
assert_version "feat: after release" "1.0.0" "alpha" "1.1.0-alpha.1"
assert_version "docs: after release" "1.0.0" "beta" "1.0.0-beta.1"
assert_version "fix: after release" "1.0.0" "rc" "1.0.0-rc.1"
assert_version "chore: dev to stable" "0.0.1-dev.5" "" "0.0.1"
assert_version "chore: alpha to stable" "0.1.0-alpha.2" "" "0.1.0"
assert_version "chore: beta to stable" "0.1.0-beta.1" "" "0.1.0"

echo ""
echo "Results: $PASS passed, $FAIL failed"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi