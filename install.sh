#!/usr/bin/env bash
# ============================================================
#  DoneScene Skills Installer (macOS / Linux)
# ============================================================
#  Usage:  chmod +x install.sh && ./install.sh
# ============================================================

set -euo pipefail

echo ""
echo "========================================"
echo "  DoneScene Skills Installer"
echo "========================================"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SOURCE="$SCRIPT_DIR/skills"
TARGET_ROOT="$HOME/.gemini/antigravity/skills"

if [ ! -d "$SKILLS_SOURCE" ]; then
    echo "[ERROR] Could not find the 'skills' folder next to this script."
    echo "        Expected: $SKILLS_SOURCE"
    exit 1
fi

# Create target if needed
mkdir -p "$TARGET_ROOT"

installed=0
skipped=0

for skill_dir in "$SKILLS_SOURCE"/ds-*/; do
    skill_name="$(basename "$skill_dir")"
    dest="$TARGET_ROOT/$skill_name"

    if [ -d "$dest" ]; then
        echo "  [SKIP]    $skill_name (already exists)"
        skipped=$((skipped + 1))
    else
        cp -r "$skill_dir" "$dest"
        echo "  [OK]      $skill_name"
        installed=$((installed + 1))
    fi
done

echo ""
echo "========================================"
echo "  Done!  Installed: $installed  |  Skipped: $skipped"
echo "========================================"
echo ""
echo "Restart Antigravity, then type  /ds  to see all commands."
echo ""
