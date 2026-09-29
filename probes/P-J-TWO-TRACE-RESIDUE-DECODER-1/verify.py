#!/usr/bin/env python3
"""Pinned L1 audit; no physical or Canon promotion is performed here."""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
# Filled by the owner before the first public pin, never after execution.
INPUT_HASHES = {'PREREG.md': '2639f6d00d855ce36e73c1f74738275816b45d010577d81db6336434cf31e569', 'PROOF.md': '491f568d1c03c20578af7858cccae40a97f0ff5b83af272e2ec49295a96a3fc0', 'REVIEW.md': '3a7e9ddc2b947f9d30667b7c395140505b50d40412d23f0411776dc065ad37ac', 'decoder.py': '45b0b37ec2ef1cd99e92260b7666653dbcbb1ffc99142766b2c267bab97a0ebc', 'primary.py': 'dc97abd593cc78b7116006d012b31096109b000114a34a9e7ab92bce01fa7cdd', 'break.py': '57a3c7e03d683bbc5fae074ef5611fd21bce1a5a3922e69eaa8b32b1831ef112'}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def main():
    assert set(INPUT_HASHES) == {
        'PREREG.md', 'PROOF.md', 'REVIEW.md',
        'decoder.py', 'primary.py', 'break.py',
    }
    for name, expected in sorted(INPUT_HASHES.items()):
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name

    # These imports happen only after the complete input-custody check.
    import primary
    from decoder import decode, norm, reading, trace_pair, uv

    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        primary.main()
    primary_output = stream.getvalue()
    census_lines = [line for line in primary_output.splitlines()
                    if line.startswith('CENSUS ')]
    assert len(census_lines) == 1
    primary_summary = json.loads(census_lines[0][len('CENSUS '):])

    spec = importlib.util.spec_from_file_location('independent_breaker', ROOT / 'break.py')
    assert spec is not None and spec.loader is not None
    breaker = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = breaker
    spec.loader.exec_module(breaker)
    independent = breaker.run_audit()
    assert set(independent) == {'summary', 'scanned', 'roundtrips', 'collision_differences'}
    assert independent['scanned'] == 19**4
    assert independent['roundtrips'] == 5 * 3150
    assert canonical(primary_summary) == canonical(independent['summary'])
    expected_counts = {
        'bound': 941, 'strip_count': 3150, 'strip_below': 3110,
        'trace_pair_count': 145, 'mod5_key_count': 2603,
        'mod25_key_count': 3150, 'mod5_capacity_shortfall': 522,
    }
    for key, expected in expected_counts.items():
        assert primary_summary[key] == expected, key
    assert primary_summary['mod5_first_collision']['norm'] == 55

    # This witness is independent of which lexicographic collision is first.
    left, right = (0, 1, 1, -2), (0, 1, 1, 3)
    assert uv(left) == uv(right) == (7, 1)
    assert trace_pair(left) == trace_pair(right) == (15, 20)
    assert norm(left) == norm(right) == 55
    assert tuple(b-a for a, b in zip(left, right)) == (0, 0, 0, 5)
    assert reading(left, 5) == reading(right, 5)
    assert reading(left) != reading(right)
    assert decode(*reading(left)).coefficients == left
    assert decode(*reading(right)).coefficients == right
    native5 = min(3125, primary_summary['mod5_key_count'])
    native25 = min(3125, primary_summary['mod25_key_count'])
    assert (native5, native25) == (2603, 3125)

    print('P-J-TWO-TRACE-RESIDUE-DECODER-1; exact L1 formal audit')
    print('PASS immutable_input_hashes=6')
    print(primary_output, end='')
    print('INDEPENDENT ' + canonical(independent))
    print('PASS independently_authored_census_byte_identity=1')
    print('PASS norm55_explicit_witness=1')
    print(f'PASS native_label_capacity_mod5={native5} native_label_capacity_mod25={native25}')
    print('SCOPE D_m only; no separately supplied sheet index; pure J step')
    print('RESULT PASS; mathematical evidence only, no Canon or physical-owner promotion')


if __name__ == '__main__':
    main()
