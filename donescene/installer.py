#!/usr/bin/env python3
"""
DoneScene Skills Installer

Copies all ds-* skill folders into ~/.gemini/antigravity/skills/
so that Antigravity recognises them as /ds-* slash commands.
"""

import os
import sys
import shutil
from pathlib import Path


def get_skills_source() -> Path:
    """Return the path to the bundled skills directory."""
    return Path(__file__).parent / "skills"


def get_target_dir() -> Path:
    """Return the Antigravity skills directory for the current user."""
    home = Path.home()
    return home / ".gemini" / "antigravity" / "skills"


def install_skills(force: bool = False) -> None:
    """Copy every ds-* folder from the package into the user's skills dir."""
    source = get_skills_source()
    target = get_target_dir()

    if not source.exists():
        print(f"[ERROR] Bundled skills not found at {source}")
        sys.exit(1)

    target.mkdir(parents=True, exist_ok=True)

    installed = 0
    skipped = 0
    updated = 0

    for skill_dir in sorted(source.iterdir()):
        if not skill_dir.is_dir() or not skill_dir.name.startswith("ds-"):
            continue

        dest = target / skill_dir.name

        if dest.exists():
            if force:
                shutil.rmtree(dest)
                shutil.copytree(skill_dir, dest)
                print(f"  [UPDATE]  {skill_dir.name}")
                updated += 1
            else:
                print(f"  [SKIP]    {skill_dir.name}  (already exists, use --force to overwrite)")
                skipped += 1
        else:
            shutil.copytree(skill_dir, dest)
            print(f"  [OK]      {skill_dir.name}")
            installed += 1

    print()
    print("=" * 48)
    print(f"  Installed: {installed}  |  Updated: {updated}  |  Skipped: {skipped}")
    print("=" * 48)
    print()
    print("  Restart Antigravity, then type /ds to see all commands.")
    print()


def uninstall_skills() -> None:
    """Remove all ds-* folders from the user's skills directory."""
    target = get_target_dir()
    removed = 0

    for item in sorted(target.iterdir()):
        if item.is_dir() and item.name.startswith("ds-"):
            shutil.rmtree(item)
            print(f"  [REMOVED] {item.name}")
            removed += 1

    print(f"\n  Removed {removed} skill(s).\n")


def main() -> None:
    """CLI entry point."""
    print()
    print("=" * 48)
    print("  DoneScene Skills Installer  v1.0.0")
    print("=" * 48)
    print()

    args = sys.argv[1:]

    if "--uninstall" in args:
        uninstall_skills()
    elif "--force" in args:
        install_skills(force=True)
    elif "--help" in args or "-h" in args:
        print("Usage:")
        print("  donescene            Install skills (skip existing)")
        print("  donescene --force    Install and overwrite existing skills")
        print("  donescene --uninstall  Remove all ds-* skills")
        print()
    else:
        install_skills(force=False)


if __name__ == "__main__":
    main()
