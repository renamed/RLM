#!/bin/bash

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PASS=0
FAIL=0

# Helper function
assert_version() {
  local commit_msg="$1"
  local current_version="$2"
  local stage="$3"
  local expected="$4"
  
  # Simulate the logic
  BASE_VERSION=$(echo $current_version | cut -d '-' -f 1)
  MAJOR=$(echo $BASE_VERSION | cut -d '.' -f 1)
  MINOR=$(echo $BASE_VERSION | cut -d '.' -f 2)
  
  if [[ "$current_version" == *"-dev."* ]]; then
    PRE_NUM=$(echo $current_version | sed 's/.*-dev\.//')
  elif [[ "$current_version" == *"-alpha."* ]]; then
    PRE_NUM=$(echo $current_version | sed 's/.*-alpha\.//')
  elif [[ "$current_version" == *"-beta."* ]]; then
    PRE_NUM=$(echo $current_version | sed 's/.*-beta\.//')
  elif [[ "$current_version" == *"-rc."* ]]; then
    PRE_NUM=$(echo $current_version | sed 's/.*-rc\.//')
  else
    PRE_NUM=0
  fi
  
  MAJOR_TRIGGERS=("feat!:" "fix!:")
  MINOR_TRIGGERS=("feat:")
  
  IS_MAJOR=false
  IS_MINOR=false
  
  for trigger in "${MAJOR_TRIGGERS[@]}"; do
    if [[ "$commit_msg" == "$trigger"* ]]; then IS_MAJOR=true; break; fi
  done
  
  if [ "$IS_MAJOR" = false ]; then
    for trigger in "${MINOR_TRIGGERS[@]}"; do
      if [[ "$commit_msg" == "$trigger"* ]]; then IS_MINOR=true; break; fi
    done
  fi
  
  if [ "$IS_MAJOR" = true ]; then
    NEW_MAJOR=$((MAJOR + 1))
    BASE_VERSION="${NEW_MAJOR}.0.0"
    NEW_PRE=1
  elif [ "$IS_MINOR" = true ]; then
    NEW_MINOR=$((MINOR + 1))
    BASE_VERSION="${MAJOR}.${NEW_MINOR}.0"
    NEW_PRE=1
  else
    NEW_PRE=$((PRE_NUM + 1))
  fi
  
  if [ -n "$stage" ]; then
    NEW_VERSION="${BASE_VERSION}-${stage}.${NEW_PRE}"
  else
    NEW_VERSION="${BASE_VERSION}"
  fi
  
  if [ "$NEW_VERSION" = "$expected" ]; then
    echo -e "${GREEN}✓${NC} $commit_msg | $current_version | $stage → $NEW_VERSION"
    PASS=$((PASS + 1))
  else
    echo -e "${RED}✗${NC} $commit_msg | $current_version | $stage → got $NEW_VERSION, expected $expected"
    FAIL=$((FAIL + 1))
  fi
}

echo "Running versioning tests..."
echo ""

# Dev stage tests
assert_version "docs: initial commit" "0.0.1" "dev" "0.0.1-dev.1"
assert_version "fix: bug fix" "0.0.1-dev.1" "dev" "0.0.1-dev.2"
assert_version "feat: add feature" "0.0.1-dev.5" "dev" "0.1.0-dev.1"
assert_version "fix!: breaking change" "0.1.0-dev.3" "dev" "1.0.0-dev.1"

# Alpha stage tests
assert_version "feat: new feature" "0.0.1" "alpha" "0.1.0-alpha.1"
assert_version "docs: update docs" "0.1.0-alpha.1" "alpha" "0.1.0-alpha.2"

# Beta stage tests
assert_version "fix: bug" "0.1.0-alpha.3" "beta" "0.1.0-beta.1"

# RC stage tests
assert_version "fix: critical" "0.1.0-beta.2" "rc" "0.1.0-rc.1"
assert_version "chore: cleanup" "0.1.0-rc.1" "rc" "0.1.0-rc.2"

# Stable (no stage)
assert_version "fix: final bug" "0.1.0-rc.2" "" "0.1.0"
assert_version "feat: after release" "0.1.0" "dev" "0.2.0-dev.1"

echo ""
echo "Results: ${GREEN}$PASS passed${NC}, ${RED}$FAIL failed${NC}"