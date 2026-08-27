#!/usr/bin/env bash
set -euo pipefail

# Descarga únicamente los repositorios aprobados del manifiesto como clones superficiales.
# No procesa las entradas pendientes de revisión de seguridad.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DESTINATION="${1:-"$ROOT/worktrees"}"
mkdir -p "$DESTINATION"

tail -n +2 "$ROOT/sources/repositorios.csv" | while IFS=, read -r repository url visibility pushed area status module_path commit exclusion; do
  if [[ "$status" != "submodulo_verificado" ]]; then
    printf 'Omitido por revisión de seguridad: %s\n' "$repository"
    continue
  fi
  target="$DESTINATION/${repository#*/}"
  if [[ -d "$target/.git" ]]; then
    printf 'Ya existe: %s\n' "$target"
  else
    git clone --depth=1 "$url" "$target"
  fi
done
