#!/usr/bin/env bash
# Symlink this repo's setup into ~/.claude, backing up anything already there.
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"
claude="$HOME/.claude"
mkdir -p "$claude/skills"

link() {
  local src="$1" dest="$2"
  if [ -L "$dest" ] && [ "$(readlink "$dest")" = "$src" ]; then
    echo "ok       $dest"
    return
  fi
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    mv "$dest" "$dest.bak"
    echo "backup   $dest -> $dest.bak"
  fi
  ln -s "$src" "$dest"
  echo "linked   $dest -> $src"
}

link "$repo/CLAUDE.md" "$claude/CLAUDE.md"
link "$repo/skills/design" "$claude/skills/design"
