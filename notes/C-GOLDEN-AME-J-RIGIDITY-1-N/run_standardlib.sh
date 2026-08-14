#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 AME46_ORIGINAL.m block944.m" >&2
  exit 2
fi

package_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python_bin=${PYTHON:-python3}
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
unset PYTHONOPTIMIZE

if ! "$python_bin" -c 'import sys; raise SystemExit(0 if sys.flags.optimize == 0 else 2)'; then
  echo "refusing optimized Python: exact verifiers require active assertions" >&2
  exit 2
fi

"$python_bin" "$package_dir/verify_frozen_order_cert.py" \
  --source "$1" --block944 "$2"
"$python_bin" "$package_dir/independent_stdlib_verify.py" "$1"
"$python_bin" "$package_dir/verify_g3_controls.py" \
  --source "$1" --block944 "$2" --builder "$package_dir/golden_symbolic.py"
"$python_bin" "$package_dir/verify_result_json.py" \
  --source "$1" --block944 "$2"
