#!/bin/bash

PASS=0
FAIL=0
RESULTS_FILE="test-results.csv"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Clean results file
echo "status,commit,current,stage,expected,got" > "$RESULTS_FILE"

assert_version() {
  local commit_msg="$1"
  local current_version="$2"
  local stage="$3"
  local expected="$4"
  
  result=$(bash "$SCRIPT_DIR/../scripts/calculate-version.sh" "$commit_msg" "$current_version" "$stage")
  
  if [ "$result" = "$expected" ]; then
    echo "✓ $commit_msg | $current_version | $stage → $result"
    echo "pass,$commit_msg,$current_version,$stage,$expected,$result" >> "$RESULTS_FILE"
    PASS=$((PASS + 1))
  else
    echo "✗ $commit_msg | $current_version | $stage → got $result, expected $expected"
    echo "fail,$commit_msg,$current_version,$stage,$expected,$result" >> "$RESULTS_FILE"
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
assert_version "fix: bug" "0.1.0-alpha.3" "beta" "0.1.0-beta.1"
assert_version "fix: critical" "0.1.0-beta.2" "rc" "0.1.0-rc.1"
assert_version "chore: cleanup" "0.1.0-rc.1" "rc" "0.1.0-rc.2"
assert_version "fix: final bug" "0.1.0-rc.2" "" "0.1.0"
assert_version "feat: after release" "0.1.0" "dev" "0.2.0-dev.1"

echo ""
echo "Results: $PASS passed, $FAIL failed"

echo "pass=$PASS" >> "$GITHUB_OUTPUT"
echo "fail=$FAIL" >> "$GITHUB_OUTPUT"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi