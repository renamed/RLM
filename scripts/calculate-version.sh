#!/bin/bash
# Usage: bash scripts/calculate-version.sh <commit_msg> <current_version> <stage>

COMMIT_MSG="$1"
CURRENT_VERSION="$2"
STAGE="$3"

BASE_VERSION=$(echo $CURRENT_VERSION | cut -d '-' -f 1)
MAJOR=$(echo $BASE_VERSION | cut -d '.' -f 1)
MINOR=$(echo $BASE_VERSION | cut -d '.' -f 2)

if [[ "$CURRENT_VERSION" == *"-dev."* ]]; then
  CURRENT_STAGE="dev"
  PRE_NUM=$(echo $CURRENT_VERSION | sed 's/.*-dev\.//')
elif [[ "$CURRENT_VERSION" == *"-alpha."* ]]; then
  CURRENT_STAGE="alpha"
  PRE_NUM=$(echo $CURRENT_VERSION | sed 's/.*-alpha\.//')
elif [[ "$CURRENT_VERSION" == *"-beta."* ]]; then
  CURRENT_STAGE="beta"
  PRE_NUM=$(echo $CURRENT_VERSION | sed 's/.*-beta\.//')
elif [[ "$CURRENT_VERSION" == *"-rc."* ]]; then
  CURRENT_STAGE="rc"
  PRE_NUM=$(echo $CURRENT_VERSION | sed 's/.*-rc\.//')
else
  CURRENT_STAGE=""
  PRE_NUM=0
fi

if [ "$STAGE" != "$CURRENT_STAGE" ]; then
  PRE_NUM=0
fi

MAJOR_TRIGGERS=("feat!:" "fix!:")
MINOR_TRIGGERS=("feat:")

IS_MAJOR=false
IS_MINOR=false

for trigger in "${MAJOR_TRIGGERS[@]}"; do
  if [[ "$COMMIT_MSG" == "$trigger"* ]]; then IS_MAJOR=true; break; fi
done

if [ "$IS_MAJOR" = false ]; then
  for trigger in "${MINOR_TRIGGERS[@]}"; do
    if [[ "$COMMIT_MSG" == "$trigger"* ]]; then IS_MINOR=true; break; fi
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

if [ -n "$STAGE" ]; then
  echo "${BASE_VERSION}-${STAGE}.${NEW_PRE}"
else
  echo "${BASE_VERSION}"
fi