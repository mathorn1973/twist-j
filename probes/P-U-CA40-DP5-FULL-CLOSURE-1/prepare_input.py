#!/usr/bin/env python3
"""Preserve original decimal tokens for directed MPFR model preparation.

Apache-2.0; PUBLIC NON-CANONICAL. No scientific execution on import.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path

INPUT_SHA256 = 'ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53'

def serialize(source, output):
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != INPUT_SHA256:
        raise ValueError('Unchanged original input bytes required')
    obj = json.loads(data, parse_float=Decimal, parse_int=Decimal)
    cfg, modes = obj['config'], obj['modes']
    pulses = obj['pulses']
    rows = ['EXACT-CA40-1']
    rows.append(' '.join(str(cfg[k]) for k in (
        'axial_hz', 'beatnote_offset_hz', 'wavelength_m', 'hbar_Js',
        'mass_kg', 'loop_seconds', 'nbar')))
    rows.append(' '.join(map(str, modes['omega_rad_s'])))
    rows.append(' '.join(map(str, modes['positions_m'])))
    rows.extend(' '.join(map(str, row)) for row in modes['vectors_by_mode'])
    rows.extend(' '.join(str(x) for pair in row for x in pair)
                for row in modes['eta_by_mode_ion'])
    if len(pulses) != 2 or [p['sign'] for p in pulses] != [1, -1]:
        raise ValueError('Frozen signed envelope order')
    rows.extend(' '.join(map(str, p['amplitudes_rad_s'])) for p in pulses)
    payload = ('\n'.join(rows)+'\n').encode('ascii')
    with output.open('xb') as stream:
        stream.write(payload)
    return {'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest(),
            'semantics': 'original JSON decimal tokens as exact rational inputs'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(serialize(args.input, args.output), sort_keys=True))
