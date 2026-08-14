#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 AME46_ORIGINAL.m" >&2
  exit 2
fi

package_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python_bin=${PYTHON:-python3}
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
unset PYTHONOPTIMIZE

if ! "$python_bin" -c 'import sys; raise SystemExit(0 if sys.flags.optimize == 0 else 2)'; then
  echo "refusing optimized Python: exact verifier requires active assertions" >&2
  exit 2
fi

"$python_bin" "$package_dir/independent_sympy.py" "$1"
