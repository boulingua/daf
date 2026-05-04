#!/usr/bin/env bash
# organise_downloads.sh — move exam PDFs produced by `quarto render`
# out of the course `units/` folders and into the canonical
# `docs/downloads/<stufe>/unit<NN>_<slug>_exam.pdf` path that the
# {{< downloads >}} shortcode links to.
#
# `quarto render` produces `unit<NN>_<slug>_exam.pdf` in
# `docs/kurs_<stufe>/units/` (because the `_exam.qmd` wrapper lives
# there). This script walks every such file and rehomes it.
#
# Safe to run when no exam PDFs exist (e.g. during scaffold phase);
# it simply reports and exits 0.

set -euo pipefail

ROOT="${1:-docs}"

if [ ! -d "$ROOT" ]; then
  echo "organise_downloads: $ROOT does not exist — nothing to do."
  exit 0
fi

moved=0
skipped=0

while IFS= read -r src; do
  # src looks like: docs/kurs_b1/units/unit03_gesundheitssystem-dach_exam.pdf
  filename="$(basename "$src")"           # unit03_gesundheitssystem-dach_exam.pdf
  # parent dir: docs/kurs_b1/units
  parent="$(dirname "$src")"
  # grandparent: docs/kurs_b1
  grandparent="$(dirname "$parent")"
  kursdir="$(basename "$grandparent")"    # kurs_b1
  # Extract CEFR level from course dir name (kurs_<stufe>)
  cefr="${kursdir#kurs_}"                 # b1

  dest_dir="$ROOT/downloads/$cefr"
  mkdir -p "$dest_dir"
  dest="$dest_dir/$filename"

  mv "$src" "$dest"
  echo "  moved  $src -> $dest"
  moved=$((moved + 1))
done < <(find "$ROOT" -type f -name "unit*_exam.pdf" -not -path "$ROOT/downloads/*" 2>/dev/null)

echo "organise_downloads: $moved exam PDF(s) moved, $skipped skipped."
