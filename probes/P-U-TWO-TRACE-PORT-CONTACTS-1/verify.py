#!/usr/bin/env python3
"""Exact public wrapper; no scientific execution before the published pin."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError('Optimized Python is outside the frozen contract')
    manifest = (HERE / 'INPUTS.sha256').read_bytes()
    seen = set()
    for line in manifest.decode('utf-8').splitlines():
        expected, name = line.split('  ', 1)
        path = Path(name)
        if path.is_absolute() or '..' in path.parts or name in seen:
            raise RuntimeError('Invalid frozen input path')
        seen.add(name)
        if hashlib.sha256((HERE / path).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f'Frozen input mismatch: {name}')
    if not {'primary.py', 'independent.py', 'PREREG.md', 'PROOF.md'} <= seen:
        raise RuntimeError('Missing required frozen input')
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0',
               PYTHONIOENCODING='utf-8', LC_ALL='C', LANG='C', TZ='UTC')
    reports = {}
    for role, filename in [('primary', 'primary.py'), ('independent', 'independent.py')]:
        result = subprocess.run([sys.executable, '-B', str(HERE / filename)],
                                cwd=HERE, env=env, capture_output=True, timeout=270)
        if result.returncode or result.stderr:
            sys.stdout.buffer.write(result.stdout)
            sys.stderr.buffer.write(result.stderr)
            raise RuntimeError(f'{role} failed, exit {result.returncode}')
        if b'\r' in result.stdout or not result.stdout.endswith(b'\n'):
            raise RuntimeError(f'{role} must emit UTF-8/LF JSON')
        reports[role] = json.loads(result.stdout.decode('utf-8'))
        if reports[role].get('status') != 'PASS':
            raise RuntimeError(f'{role} did not pass')
    first, second = reports['primary'], reports['independent']
    for field in ('input_pairs', 'history_rows', 'contact_rows',
                  'history_sha256', 'contact_sha256'):
        if first[field] != second[field]:
            raise RuntimeError(f'Independent full-state disagreement: {field}')
    for field, required in [('input_pairs', 25), ('history_rows', 250), ('contact_rows', 50)]:
        if first[field] != required:
            raise RuntimeError(f'Incomplete frozen coverage: {field}')
    if first['selectors_sha256'] != second['selector_sha256']:
        raise RuntimeError('Independent actual-selector disagreement')
    if first['control_sha256'] != second['control_history_sha256']:
        raise RuntimeError('Independent no-exchange control disagreement')
    payload = {'status': 'PASS', 'reports': reports,
               'frozen_inputs_sha256': hashlib.sha256(manifest).hexdigest()}
    sys.stdout.buffer.write((json.dumps(payload, sort_keys=True,
                                       separators=(',', ':')) + '\n').encode('utf-8'))


if __name__ == '__main__':
    main()
