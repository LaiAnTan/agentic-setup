#!/usr/bin/env bash
# Symlink this repo's rules and skills into each coding agent's global config,
# backing up anything already there. Claude Code is always set up; other agents
# only if their config folder already exists.
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"

link() {
  local src="$1" dest="$2"
  mkdir -p "$(dirname "$dest")"
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

# agent config dir | global rules file name
agents=(
  "$HOME/.claude|CLAUDE.md"
  "$HOME/.codex|AGENTS.md"
  "$HOME/.gemini|GEMINI.md"
)

for entry in "${agents[@]}"; do
  dir="${entry%%|*}"
  rules="${entry##*|}"
  if [ "$dir" != "$HOME/.claude" ] && [ ! -d "$dir" ]; then
    echo "skip     $dir (not installed)"
    continue
  fi
  link "$repo/CLAUDE.md" "$dir/$rules"
  for skill in "$repo"/skills/*/; do
    name="$(basename "$skill")"
    link "$repo/skills/$name" "$dir/skills/$name"
  done
done
