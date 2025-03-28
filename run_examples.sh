#!/bin/bash

EXAMPLES_DIR="./examples/api"
FILES=($(find "$EXAMPLES_DIR" -maxdepth 1 -name "*.py" | sort))

# ANSI colors
YELLOW='\033[1;33m'
GREEN='\033[1;32m'
BLUE='\033[1;34m'
RESET='\033[0m'
DIVIDER="------------------------------------------------------------"

print_header() {
  echo -e "${BLUE}${DIVIDER}"
  echo -e "$1"
  echo -e "${DIVIDER}${RESET}"
}

run_script() {
  echo -e "${YELLOW}Running: $1${RESET}"
  echo -e "${GREEN}"
  python "$1"
  echo -e "${RESET}"
}

# If a number is passed
if [ "$1" ]; then
  COUNT=$1
  print_header "🟢 Running $COUNT example script(s) from: $EXAMPLES_DIR"
  for ((i = 0; i < COUNT && i < ${#FILES[@]}; i++)); do
    run_script "${FILES[$i]}"
    echo -e "${BLUE}${DIVIDER}${RESET}"
  done
else
  print_header "📄 Available Python scripts in: $EXAMPLES_DIR"
  for file in "${FILES[@]}"; do
    echo -e "${GREEN}- $file${RESET}"
  done
  echo -e "\nTo run N scripts: ${YELLOW}$0 N${RESET}"
fi
