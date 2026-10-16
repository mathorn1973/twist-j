#!/usr/bin/env python3
"""Read-only audit of CLOSED OFFLINE evidence; no solver, network or subprocess.

Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
PUBLIC NON-CANONICAL. Exact saved aggregation is not propagation replication.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import struct
import sys

Q = Fraction
PIN = 'bca348445715c03f4cdc3af6079207024dd40332'
SCOPE = 'FULL_WORD_SIX_CASES_K3_CONDITIONAL'
FIELDS = ('guard', 'tail', 'continuum', 'jumps', 'total',
          'sampled_time_node_L2', 'sampled_projection_node_L2',
          'sampled_arithmetic_node_L2', 'maximum_node_bound', 'maximum_norm_error',
          'endpoint_norm_squared_lo', 'endpoint_norm_squared_hi')
LABELS = ((4, 3), (4, 4), (1, 1))
PAIRS = ((0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5))
TAIL = Q(680046581, 794280046581)
MASS = 1 - TAIL
GOAL = Q(1, 1000)
DIM, LANES, COLUMNS, SEGMENTS, STEPS = 6435, 8, 120, 80, 384
VECTOR_BYTES = DIM * 16
END_BYTES = LANES * VECTOR_BYTES
ROW_BYTES = 12 * 8
COMP_BYTES = LANES * ROW_BYTES
PAYLOAD_BYTES = END_BYTES + COMP_BYTES
PIN_HASHES = {
    'DERIVATION.md': '5f008ce30874a86aee371e9a8670316be34434db8287ec9848006b1cfc4efc0d',
    'EXACT-DESIGN.md': '58c3660187381bb1996741db8f7aefc0ed1dcd6cb681b73d93258fec5023292d',
    'PREREG.md': 'c91e7ded1353458d3023f07150be7495293822bae6b3c924b29ba4879288b25c',
    'README.md': '916e038bb7d89a156e414f24cc2f35db970348141b202db235767b2a41d17532',
    'dp5_tableau.hpp': '8121796d1a2b1991b1e4d6ce0b340fbbd9e535500a9f22547d257919484de0b5',
    'full.cpp': '955d68d13de28a275fe2f1844238d5cdaf248d04e3332560a715a43009a5c3ea',
    'full_run.py': 'd39d81c25ae5f83f7d84e626788055c6e566050cbb1d7a5f2cb7d170e28769d5',
    'higher_order.hpp': '72e771a0f6eb58a47c2126b2edc01fa735f51d5d85211d40f62c2af4d8254299',
    'input.json': 'ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53',
    'kernel.cpp': '9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2',
    'prepare_input.py': 'cce5d0d03e134f24a618ae0e20db0b69f240d6f0cfdfd2fe96ce28dc9c840e9a',
    'validated_model.cpp': '49da6c238f8e938a79eb38aeeb16b4ed3b6cf676d076b0b2d483ab1e4eb9763a',
    'validated_model.hpp': 'adfc94f482f34bf243dc86dc77c68aa5bcd3e97e8e96943fa624f320ddf04b1b',
    'verify.py': '8a5797045d8fea0bdd5fa918125d339d3b59d3dacb25fb83ab3fd845ccec88a7',
    'SOURCE_SHA256SUMS': 'fa029eef8f387251a1a935f36605fdc84b24f311b3c32396881306b3a63015b1',
}


class AuditError(Exception):
    """A failed saved-evidence obligation, never an automatic solver retry."""


def demand(condition, message):
    if not condition:
        raise AuditError(message)


def unique_object(items):
    out = {}
    for key, value in items:
        demand(key not in out, 'duplicate JSON key: ' + key)
        out[key] = value
    return out


def nonfinite_token(token):
    raise AuditError('nonfinite JSON token: ' + token)


def parse_json(raw):
    result = json.loads(raw, object_pairs_hook=unique_object,
                        parse_constant=nonfinite_token)
    def walk(value):
        if isinstance(value, float):
            demand(math.isfinite(value), 'nonfinite parsed number')
        elif isinstance(value, list):
            for member in value:
                walk(member)
        elif isinstance(value, dict):
            for member in value.values():
                walk(member)
    walk(result)
    return result


def read_json(path):
    return parse_json(path.read_bytes())


def contract_equal(actual, expected):
    """JSON booleans cannot impersonate integer counters or case labels."""
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(contract_equal(a,b) for a,b in zip(actual,expected))
    if isinstance(expected, dict):
        return actual.keys() == expected.keys() and all(contract_equal(actual[k],v) for k,v in expected.items())
    return actual == expected


def require_contract(record, fixed, message):
    demand(all(contract_equal(record[key], value) for key,value in fixed.items()), message)


def check_inventory_flag(summary, inventory):
    demand(type(inventory['complete']) is bool and
           contract_equal(summary['artifact_inventory_complete'], inventory['complete']),
           'summary/inventory completeness flag differs')


def check_final_receipt(receipt):
    demand(contract_equal(receipt['exit_code'], 0) and receipt['error'] is None and receipt['cleanup_error'] is None,
           'child receipt not clean')


def check_column_values(column, row, index):
    demand(contract_equal(column['thermal_index'], index), 'column thermal identity')
    for k,field in enumerate(FIELDS[:10]):
        demand(type(column[field]) in (int,float), 'JSON component must be numeric, not boolean')
        rational(column[field])
        demand(struct.pack('<d', column[field]) == struct.pack('<d', row[k]), 'JSON/raw component bytes differ')


def rational(value):
    demand(type(value) in (int, float, Fraction), 'numeric value required')
    if isinstance(value, float):
        demand(math.isfinite(value), 'finite binary64 required')
    return Q(value)


def bounds(value):
    demand(isinstance(value, list) and len(value) == 2, 'interval pair required')
    a, b = map(rational, value)
    demand(a <= b, 'inverted interval')
    return a, b


def up_add(a, b):
    """Least binary64 >= exact sum, independent of current hardware rounding."""
    target = rational(a) + rational(b)
    try:
        result = float(target)
    except OverflowError as exc:
        raise AuditError('upward sum overflow') from exc
    demand(math.isfinite(result), 'upward sum overflow')
    if Q(result) < target:
        result = math.nextafter(result, math.inf)
    demand(math.isfinite(result), 'upward sum overflow')
    return result


def check_row(row):
    demand(len(row) == 12 and all(math.isfinite(v) and v >= 0 for v in row),
           'component finite nonnegative domain')
    demand(row[10] <= row[11], 'component norm interval inverted')
    expected = up_add(up_add(row[0], row[1]), up_add(row[2], row[3]))
    demand(struct.pack('<d', row[4]) == struct.pack('<d', expected),
           'component total is not the prescribed upward sum')


def rows_from_bytes(raw, count=None):
    demand(len(raw) % ROW_BYTES == 0, 'component row truncation')
    rows = list(struct.iter_unpack('<12d', raw))
    demand(count is None or len(rows) == count, 'component row count')
    for row in rows:
        check_row(row)
    return rows


def exact_squared_norm(raw):
    """Exact sum of binary64 squares using exponent buckets, no float squares.

    A normal value is m*2**(E-1075); a subnormal is m*2**(-1074).
    All squared terms have common denominator 2**2148. Bucket accumulation
    avoids repeated Fraction normalization and retains underflowed squares.
    """
    demand(len(raw) % 16 == 0, 'complex-vector byte alignment')
    buckets = Counter()
    for (bits,) in struct.iter_unpack('<Q', raw):
        exponent = (bits >> 52) & 2047
        mantissa = bits & ((1 << 52) - 1)
        demand(exponent != 2047, 'nonfinite endpoint component')
        if exponent:
            mantissa += 1 << 52
        if mantissa:
            buckets[max(0, exponent - 1)] += mantissa * mantissa
    numerator = sum(value << (2 * shift) for shift, value in buckets.items())
    return Q(numerator, 1 << 2148)


def check_vector_norm(raw, interval):
    lo, hi = bounds(list(interval))
    value = exact_squared_norm(raw)
    demand(lo <= value <= hi, 'saved norm interval misses exact endpoint norm')
    return value


def affine_sqrt_enclosed(upper, coefficient, constant, radicand):
    u, c, k, r = map(rational, (upper, coefficient, constant, radicand))
    demand(min(c, k, r) >= 0, 'negative sqrt-affine datum')
    difference = u - k
    return difference >= 0 and difference * difference >= c * c * r


def square_range(lo, hi):
    demand(lo <= hi, 'square interval inverted')
    return (Q(0) if lo <= 0 <= hi else min(lo * lo, hi * hi),
            max(lo * lo, hi * hi))


def audit_pair(pair, expected, errors, norms):
    demand(contract_equal(pair['cases'], list(expected)), 'pair identity/order')
    n, t, a, total = [rational(pair[key]) for key in
                      ('numerical_radius', 'thermal_radius', 'arithmetic_radius', 'total_radius')]
    demand(min(n, t, a, total) >= 0, 'negative pair radius')
    c, d = expected
    demand(affine_sqrt_enclosed(2*n, errors[c], norms[c]*errors[d], MASS) or
           affine_sqrt_enclosed(2*n, errors[d], norms[d]*errors[c], MASS),
           'pair Gram error radius understated')
    demand(t >= TAIL/2, 'omitted thermal contribution understated')
    s, lin = pair['sine_retained_interval'], pair['linear_full_interval']
    demand(len(s) == len(lin) == 2, 'complex coherence rectangle shape')
    squares = [square_range(sa-lb, sb-la)
               for (sa, sb), (la, lb) in zip(map(bounds, s), map(bounds, lin))]
    min2, max2 = map(sum, zip(*squares))
    clo, chi = bounds(pair['witness_center_interval'])
    demand(clo >= 0 and (2*clo)**2 <= min2 and (2*chi)**2 >= max2,
           'coherence rectangle magnitude not enclosed')
    demand(a >= (chi-clo)/2 and total >= n+t+a, 'arithmetic halfwidth/total understated')
    lo, hi = bounds(pair['certified_trace_distance_interval'])
    demand(0 <= lo <= max(Q(0), clo-n-t) and
           min(Q(1), chi+n+t) <= hi <= 1, 'final distance interval not outward')
    decision = 'EXCEEDS_TARGET' if lo > GOAL else 'WITHIN_TARGET' if hi <= GOAL else 'UNRESOLVED'
    return {'cases': list(expected), 'numerical_radius_exact': str(n),
            'thermal_radius_exact': str(t), 'arithmetic_radius_exact': str(a),
            'total_radius_exact': str(total), 'distance_interval_exact': [str(lo), str(hi)],
            'precision_goal_pass': total <= GOAL, 'discrepancy': decision}


def compositions(total, width):
    if width == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, width-1):
                yield (first,) + rest


def occupation_basis():
    return [row for grade in range(9) for row in compositions(grade, 7)]


def occupied(case, segment):
    return any((label + segment//16) % 5 == 0 for label in LABELS[case % 3])


def hash_file(path):
    h = hashlib.sha256()
    count = 0
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            count += len(block)
            h.update(block)
    return {'bytes': count, 'sha256': h.hexdigest()}


def safe_member(root, name):
    demand(isinstance(name, str) and '\\' not in name and ':' not in name,
           'unsafe inventory name')
    relative = PurePosixPath(name)
    demand(not relative.is_absolute() and relative.parts and
           all(part not in ('', '.', '..') for part in relative.parts) and
           relative.as_posix() == name, 'unsafe inventory path')
    path = root.joinpath(*relative.parts)
    demand(not path.is_symlink(), 'symlink evidence member')
    demand(path.resolve().is_relative_to(root.resolve()), 'evidence path escaped root')
    return path


def inventory_audit(state, inventory):
    recorded = inventory['files']
    demand(isinstance(recorded, dict), 'inventory file mapping')
    actual = {}
    for path in sorted(state.rglob('*')):
        demand(not path.is_symlink(), 'symlink in offline evidence tree')
        demand(path.resolve().is_relative_to(state.resolve()), 'offline evidence entry escaped root')
        if path.is_file():
            actual[path.relative_to(state).as_posix()] = hash_file(path)
        else:
            demand(path.is_dir(), 'nonregular evidence entry')
    for name, receipt in recorded.items():
        safe_member(state, name)
        demand(name in actual and contract_equal(actual[name], receipt), 'copied inventory/hash mismatch: '+name)
    demand(type(inventory['complete']) is bool, 'inventory completeness must be JSON boolean')
    complete = inventory.get('complete') is True
    if complete:
        demand(set(actual) == set(recorded) and not inventory.get('errors'), 'complete inventory differs from tree')
    return actual, complete


def prefix_numbers(names):
    numbers = []
    for name in names:
        demand(name.startswith('checkpoint-') and name.endswith('.json'), 'checkpoint marker name')
        word = name[11:-5]
        demand(word.isdigit() and str(int(word)) == word, 'noncanonical checkpoint number')
        numbers.append(int(word))
    numbers.sort()
    demand(not numbers or numbers == list(range(numbers[-1]+1)), 'checkpoint prefix hole or duplicate')
    demand(not numbers or numbers[-1] <= SEGMENTS, 'checkpoint outside word')
    return numbers


def check_initial(raw, batch, dimension=DIM, lanes=LANES):
    demand(len(raw) == dimension*lanes*16, 'initial payload size')
    expected = bytearray(len(raw))
    for lane in range(lanes):
        row = batch*lanes+lane
        demand(row < dimension, 'initial basis index outside dimension')
        struct.pack_into('<d', expected, 16*(lane*dimension+row), 1.0)
    demand(raw == expected, 'initial basis state differs')


def check_carry(previous, current, inactive, previous_hash, current_hash):
    demand(len(previous) == len(current), 'carry lane count')
    demand(all(new[k] >= old[k] for old, new in zip(previous, current) for k in range(10)),
           'cumulative checkpoint component decreased')
    if inactive:
        demand(previous_hash == current_hash, 'inactive state/certificate payload changed')


def checkpoint_audit(state, actual, require_complete, all_norms):
    known = set()
    snapshots = inactive = norms_checked = complete_tasks = 0
    terminal_rows = {}
    task_places = Counter()
    tasks = []
    checkpoint_totals = {}
    for case in range(6):
        for batch in range(15):
            folder = state/'checkpoints'/f'case-{case}'/f'batch-{batch}'
            numbers = prefix_numbers([p.name for p in folder.glob('checkpoint-*.json')])
            previous_rows = previous_hash = place = None
            for boundary in numbers:
                stem = f'checkpoint-{boundary}'
                marker = folder/(stem+'.json')
                rec = read_json(marker)
                active_count = sum(occupied(case, s) for s in range(boundary))
                fixed = {'schema': 'FULL_SEGMENT_CHECKPOINT_V1', 'scope': SCOPE,
                         'case': case, 'batch': batch, 'segment_boundary': boundary,
                         'physical_time_seconds_rational': [boundary, 160000],
                         'thermal_column_start': batch*LANES, 'thermal_columns': LANES,
                         'dimension': DIM, 'cumulative_cells': active_count*STEPS,
                         'active_segments_completed': active_count, 'payload': stem+'.bin',
                         'payload_bytes': PAYLOAD_BYTES, 'endpoint_bytes': END_BYTES,
                         'component_bytes': COMP_BYTES, 'component_offset': END_BYTES,
                         'component_fields': list(FIELDS)}
                require_contract(rec, fixed, 'checkpoint metadata mismatch')
                demand(type(rec['cpu']) is int and type(rec['place']) is int and
                       0 <= rec['cpu'] < 80 and rec['cpu'] == rec['place'], 'checkpoint CPU/place')
                here = rec['cpu']
                demand(place is None or place == here, 'checkpoint task migration')
                place = here
                payload = folder/(stem+'.bin')
                name = payload.relative_to(state).as_posix()
                demand(name in actual and actual[name]['bytes'] == PAYLOAD_BYTES,
                       'committed payload missing or truncated')
                known.update((name, marker.relative_to(state).as_posix()))
                with payload.open('rb') as stream:
                    stream.seek(END_BYTES)
                    rows = rows_from_bytes(stream.read(), LANES)
                checkpoint_totals[(case, batch, boundary)] = max(row[4] for row in rows)
                if boundary == 0:
                    demand(all(all(v == 0 for v in row[:10]) and row[10:] == (1, 1) for row in rows),
                           'initial certificate/norm mismatch')
                    with payload.open('rb') as stream:
                        check_initial(stream.read(END_BYTES), batch)
                if previous_rows is not None:
                    off = not occupied(case, boundary-1)
                    check_carry(previous_rows, rows, off, previous_hash, actual[name]['sha256'])
                    inactive += int(off)
                if all_norms or boundary == SEGMENTS:
                    with payload.open('rb') as stream:
                        for lane in range(LANES):
                            check_vector_norm(stream.read(VECTOR_BYTES), rows[lane][10:])
                            norms_checked += 1
                if boundary == SEGMENTS:
                    terminal_rows[(case, batch)] = rows
                snapshots += 1
                previous_rows, previous_hash = rows, actual[name]['sha256']
            full = len(numbers) == SEGMENTS+1
            complete_tasks += int(full)
            if full:
                task_places[place] += 1
            tasks.append({'case': case, 'batch': batch, 'snapshots': len(numbers),
                          'last_boundary': numbers[-1] if numbers else None})
    uncommitted = sorted(name for name in actual if name.startswith('checkpoints/') and name not in known)
    if require_complete:
        demand((snapshots, complete_tasks, inactive) == (7290, 90, 5280) and not uncommitted,
               'complete checkpoint inventory not met')
    return {'snapshots': snapshots, 'complete_tasks': complete_tasks,
            'inactive_payload_identities': inactive, 'exact_norm_columns_checked': norms_checked,
            'all_snapshot_norms_requested': all_norms, 'uncommitted_files': uncommitted,
            'tasks': tasks}, terminal_rows, task_places, checkpoint_totals


def metadata_audit(state, allow_missing=False):
    paths = {name: state/name for name in ('metadata.json','layout.txt','basis.json')}
    demand(allow_missing or all(path.exists() for path in paths.values()), 'complete model metadata missing')
    expected = occupation_basis()
    weights = [Q(20, 21)**7 * Q(1, 21)**sum(row) for row in expected[:COLUMNS]]
    demand(len(expected) == DIM and sum(weights) == MASS, 'independent thermal basis/count')
    fixed = {'scope': SCOPE, 'cutoff': 8, 'guard': 10, 'steps_per_segment': STEPS,
             'integrator': 'DP5_TWO_HALF_STEPS', 'dense_curve': 'QUINTIC_THREE_POINT_HERMITE',
             'substeps_per_cell': 2, 'rhs_per_cell': 13, 'original_segments': SEGMENTS,
             'segment_seconds_rational': [1, 160000], 'final_time_seconds_rational': [1, 2000],
             'cases': 6, 'thermal_columns': COLUMNS, 'thermal_cutoff': 3, 'dimension': DIM,
             'guard_dimension': 19448, 'tasks': 90, 'required_snapshots': 7290,
             'required_cells': 737280, 'required_active_task_segments': 1920,
             'required_inactive_task_segments': 5280, 'initial_state_in_moving_frame': True,
             'reset_between_checkpoints': False, 'fsal_between_cells': False,
             'normalization_applied': False, 'phase_fit_applied': False,
             'task_case_order': [1, 2, 4, 5, 0, 3], 'component_fields': list(FIELDS),
             'case_active_cells': [12288, 6144, 6144, 12288, 6144, 6144]}
    if paths['metadata.json'].exists():
        meta = read_json(paths['metadata.json'])
        require_contract(meta, fixed, 'fixed metadata mismatch')
        demand(len(meta['thermal_weights']) == COLUMNS, 'thermal weight count')
        for w, enc in zip(weights, meta['thermal_weights']):
            lo, hi = bounds(enc)
            demand(0 <= lo <= w <= hi, 'thermal weight enclosure')
        lo, hi = bounds(meta['thermal_tail'])
        demand(0 <= lo <= TAIL <= hi <= 1, 'thermal tail enclosure')
    # Parse the contract instead of trusting an arbitrary preformatted string.
    required = {'steps': '384', 'integrator': 'DP5_TWO_HALF_STEPS',
                'dense_curve': 'QUINTIC_THREE_POINT_HERMITE', 'substeps_per_cell': '2',
                'rhs_per_cell': '13', 'segment_boundaries': '81', 'cases': '6',
                'columns': '120', 'batch_columns': '8', 'dimension': '6435', 'components': '12',
                'checkpoint_payload': 'lane,basis,re_im;then_lane,field',
                'checkpoint_endpoint_bytes': '823680', 'checkpoint_component_bytes': '768',
                'checkpoint_bytes': '824448', 'final_endpoints': 'case,column,basis,re_im',
                'final_components': 'case,column,field', 'encoding': 'little_endian_IEEE_binary64',
                'commit': 'checkpoint-N.json_after_payload_rename'}
    if paths['layout.txt'].exists():
        layout_lines = paths['layout.txt'].read_text('ascii').splitlines()
        demand(layout_lines and layout_lines[0] == 'FULL_WORD_SEGMENT_CHECKPOINTS_V1', 'layout schema')
        layout = unique_object([line.split('=', 1) for line in layout_lines[1:]])
        demand(layout == required, 'binary layout differs')
    if paths['basis.json'].exists():
        basis = read_json(paths['basis.json'])
        require_contract(basis, {'scope': SCOPE, 'cutoff': 8, 'guard': 10, 'thermal_cutoff': 3}, 'basis header')
        require_contract(basis, {'occupations': [list(row) for row in expected]}, 'occupation order/content mismatch')
    return weights


def final_audit(state, record, weights, terminal_rows, task_places):
    fixed = {'status': 'COMPLETED', 'scope': SCOPE,
             'error_account_scope': 'normwise_ball_full_space_defect',
             'full_trajectory_certificate': True, 'final_coherences_computed': True,
             'cutoff': 8, 'guard': 10, 'dimension': DIM, 'guard_dimension': 19448,
             'steps_per_segment': STEPS, 'integrator': 'DP5_TWO_HALF_STEPS',
             'dense_curve': 'QUINTIC_THREE_POINT_HERMITE', 'thermal_columns': COLUMNS,
             'thermal_cutoff': 3, 'cases': 6, 'threads': 80, 'simd_lanes': LANES,
             'final_time_seconds_rational': [1, 2000], 'completed_tasks': 90,
             'committed_snapshots': 7290, 'trajectory_initializations': 90,
             'state_and_certificate_carry_checks': 7200, 'polynomial_start_checks': 737280,
             'certificate_monotonicity_checks': 737280, 'inactive_identity_checks': 5280,
             'active_task_segments': 1920, 'worker_arithmetic_fixtures': 80, 'migrations': 0,
             'reset_between_checkpoints': False, 'normalization_applied': False, 'phase_fit_applied': False}
    require_contract(record, fixed, 'full result metadata')
    fixtures = record['fixtures']
    demand(all(fixtures[key] is True for key in ('directed_arithmetic', 'zero_displacement_enclosure',
           'adjoint_enclosure', 'ball_interval_fixture_enclosure')), 'runtime fixture declaration')
    demand(0 <= rational(fixtures['dense_displacement_error']) <= rational(1e-11) and
           0 <= rational(fixtures['collective_displacement_error']) <= rational(1e-11) and
           0 <= rational(fixtures['ball_reference_radius_ratio']) <= 1, 'runtime fixture diagnostic')
    for field in ('preparation_seconds', 'model_preparation_seconds', 'kernel_seconds', 'end_to_end_seconds'):
        demand(rational(record[field]) > 0, 'positive recorded timing')
    demand(record['end_to_end_seconds'] >= record['kernel_seconds'] and
           record['preparation_seconds'] >= record['model_preparation_seconds'], 'recorded timing order')
    check_workers(record['thread_map'], task_places)
    for key, target in (('thermal_tail', TAIL), ('retained_thermal_weight', MASS)):
        lo, hi = bounds(record[key])
        demand(0 <= lo <= target <= hi <= 1, 'recorded thermal mass enclosure')
    raw = (state/'components.bin').read_bytes()
    demand(len(raw) == 6*COLUMNS*ROW_BYTES and
           (state/'endpoints.bin').stat().st_size == 6*COLUMNS*VECTOR_BYTES, 'final byte sizes')
    rows = rows_from_bytes(raw, 6*COLUMNS)
    with (state/'endpoints.bin').open('rb') as endpoints:
        for case in range(6):
            for batch in range(15):
                path = state/'checkpoints'/f'case-{case}'/f'batch-{batch}'/'checkpoint-80.bin'
                saved = path.read_bytes()
                demand(endpoints.read(END_BYTES) == saved[:END_BYTES], 'final endpoint differs from terminal snapshot')
                off = (case*COLUMNS+batch*LANES)*ROW_BYTES
                demand(raw[off:off+COMP_BYTES] == saved[END_BYTES:], 'final components differ from terminal snapshot')
                demand(rows[case*COLUMNS+batch*LANES:case*COLUMNS+(batch+1)*LANES] == terminal_rows[(case,batch)],
                       'terminal component decoding mismatch')
    demand(len(record['branches']) == 6, 'branch count')
    errors, norms = [], []
    component_indices = {'guard_component': 0, 'tail_component': 1, 'continuum_component': 2,
                         'jump_component': 3, 'sampled_time_node_L2': 5,
                         'sampled_projection_node_L2': 6, 'sampled_arithmetic_node_L2': 7}
    for case, branch in enumerate(record['branches']):
        require_contract(branch, {'case': case, 'labels': list(LABELS[case % 3]),
             'node_split_scope': 'diagnostic_quadrature_only_continuum_allowance_is_combined'},
             'branch identity/diagnostic scope')
        bounds(branch['linear_phase'])
        demand(len(branch['linear_alpha']) == 7, 'linear alpha mode count')
        for alpha in branch['linear_alpha']:
            demand(len(alpha) == 2, 'linear alpha complex shape')
            for interval in alpha:
                bounds(interval)
        current = rows[case*COLUMNS:(case+1)*COLUMNS]
        demand(len(branch['columns']) == COLUMNS, 'branch column count')
        for index, (column, row) in enumerate(zip(branch['columns'], current)):
            check_column_values(column, row, index)
        e, a = rational(branch['error_bound']), rational(branch['weighted_endpoint_norm'])
        demand(min(e, a) >= 0, 'negative weighted bound')
        demand(e*e >= sum(w*rational(row[4])**2 for w, row in zip(weights, current)),
               'weighted error RMS understated')
        demand(a*a >= sum(w*rational(row[11]) for w, row in zip(weights, current)),
               'weighted stored norm understated')
        for field, index in component_indices.items():
            upper = rational(branch[field])
            demand(upper >= 0 and upper*upper >= sum(w*rational(row[index])**2 for w,row in zip(weights,current)),
                   'weighted component RMS understated: '+field)
        errors.append(e)
        norms.append(a)
    demand(len(record['pair_coherences']) == len(PAIRS), 'pair count')
    pairs = [audit_pair(pair, identity, errors, norms)
             for pair, identity in zip(record['pair_coherences'], PAIRS)]
    return {'pairs': pairs, 'precision_goal_pass': all(p['precision_goal_pass'] for p in pairs),
            'nonlinear_discrepancy_resolved_for_both_signs':
                all(any(p['discrepancy'] == 'EXCEEDS_TARGET' for p in pairs[3*s:3*s+3]) for s in range(2))}


def check_workers(workers, task_places):
    demand(all(all(type(w[key]) is int for key in ('thread','cpu','place','completed_tasks')) for w in workers),
           'worker counters must be JSON integers')
    demand(len(workers) == 80 and sorted(w['thread'] for w in workers) == list(range(80)) and
           sorted(w['cpu'] for w in workers) == sorted(w['place'] for w in workers) == list(range(80)),
           'worker inventory/coverage')
    demand(all(w['cpu'] == w['place'] and w['completed_tasks'] == task_places[w['cpu']] > 0
               for w in workers) and sum(w['completed_tasks'] for w in workers) == 90,
           'worker counts disagree with committed task placement')


LIFECYCLE = ('model_preparation_started', 'model_preparation_completed', 'fixtures_completed',
             'worker_coverage_validated', 'full_word_scan_completed', 'full_time_restoration_completed')


def log_records(raw):
    """Only LF-terminated records are committed log evidence after interruption."""
    lines = raw.splitlines(keepends=True)
    truncated = bool(lines and not lines[-1].endswith(b'\n'))
    if truncated:
        lines.pop()
    return [parse_json(line) for line in lines], truncated


def check_lifecycle(phases, complete):
    names = [row['phase'] for row in phases]
    demand(names == list(LIFECYCLE[:len(names)]), 'lifecycle inventory/order')
    demand(not complete or names == list(LIFECYCLE), 'complete lifecycle missing phases')
    times = [rational(row['elapsed_seconds']) for row in phases]
    demand(times == sorted(times) and (not times or min(times) >= 0), 'lifecycle timing order')
    return names


def check_progress(records, checkpoint_totals, complete):
    task_rows = {}
    counts = Counter()
    snapshot_counts, completed_counts = set(), set()
    for row in records:
        case, batch = row['case'], row['batch']
        demand(type(case) is int and type(batch) is int and 0 <= case < 6 and 0 <= batch < 15,
               'progress task identity')
        key = case, batch
        demand((case,batch,0) in checkpoint_totals, 'progress task has no committed initial state')
        track = task_rows.setdefault(key, {'cells': 0, 'boundary': 0, 'done': False, 'time': Q(0)})
        now = rational(row['elapsed_seconds'])
        demand(now >= track['time'] and not track['done'], 'progress after completion/time reversal')
        track['time'] = now
        kind = row['kind']
        demand(kind in ('cells', 'checkpoint', 'task_completed'), 'unknown progress kind')
        demand(type(row['cells']) is int and row['cells'] >= 0, 'progress cells must be JSON integer')
        counts[kind] += 1
        if kind == 'cells':
            segment, within = row['original_segment'], row['cell_in_segment']
            demand(type(segment) is int and 0 <= segment < SEGMENTS and segment == track['boundary'] and
                   type(within) is int and 1 <= within <= STEPS and within % 32 == 0 and
                   occupied(case, segment), 'cell progress geometry')
            expected_cells = STEPS*sum(occupied(case,s) for s in range(segment))+within
            demand(type(row['total_cells']) is int and row['cells'] == expected_cells == track['cells']+32 and
                   row['total_cells'] == STEPS*sum(occupied(case,s) for s in range(SEGMENTS)) and
                   rational(row['error_bound_max']) >= 0, 'cell progress sequence/count')
            track['cells'] = expected_cells
        elif kind == 'checkpoint':
            count = row['committed_snapshots']
            demand(type(count) is int and 2 <= count <= len(checkpoint_totals) and count not in snapshot_counts,
                   'progress snapshot counter type/range/duplicate')
            snapshot_counts.add(count)
            boundary = row['segment_boundary']
            demand(type(boundary) is int and boundary == track['boundary']+1 and boundary <= SEGMENTS,
                   'checkpoint progress sequence')
            expected_cells = STEPS*sum(occupied(case,s) for s in range(boundary))
            demand(row['cells'] == expected_cells == track['cells'], 'checkpoint/progress cells disagree')
            demand((case,batch,boundary) in checkpoint_totals and
                   rational(row['error_bound_max']) == rational(checkpoint_totals[(case,batch,boundary)]),
                   'logged checkpoint has no matching committed payload/error total')
            track['boundary'] = boundary
        else:
            count = row['completed_tasks']
            demand(type(count) is int and 1 <= count <= 90 and count not in completed_counts,
                   'progress completion counter type/range/duplicate')
            completed_counts.add(count)
            demand(track['boundary'] == SEGMENTS and row['cells'] == track['cells'] and
                   (case,batch,SEGMENTS) in checkpoint_totals, 'premature task completion')
            track['done'] = True
    # A payload is committed before its log row. At interruption one newest
    # payload per task may lack a row; earlier unlogged boundaries are invalid.
    for case,batch in {(c,b) for c,b,_ in checkpoint_totals}:
        last = max(n for c,b,n in checkpoint_totals if (c,b) == (case,batch))
        logged = task_rows.get((case,batch), {}).get('boundary', 0)
        demand(logged <= last <= logged+1, 'committed prefix not linked to available progress')
    if complete:
        demand(counts == {'cells': 23040, 'checkpoint': 7200, 'task_completed': 90} and
               len(task_rows) == 90 and all(row['done'] for row in task_rows.values()), 'complete progress inventory')
    return dict(sorted(counts.items()))


def logs_audit(state, checkpoint_totals, complete):
    lifecycle_path, progress_path = state/'lifecycle.jsonl', state/'progress.jsonl'
    demand(lifecycle_path.exists() or not checkpoint_totals, 'checkpoints without lifecycle log')
    demand(progress_path.exists() or not checkpoint_totals, 'checkpoints without progress log')
    phases, life_truncated = log_records(lifecycle_path.read_bytes()) if lifecycle_path.exists() else ([],False)
    rows, progress_truncated = log_records(progress_path.read_bytes()) if progress_path.exists() else ([],False)
    names = check_lifecycle(phases, complete)
    demand(not checkpoint_totals or len(names) >= 4, 'checkpoint precedes worker coverage phase')
    counts = check_progress(rows, checkpoint_totals, complete)
    demand('full_word_scan_completed' not in names or counts.get('task_completed') == 90,
           'scan-completed phase without complete task logs')
    demand(not complete or not (life_truncated or progress_truncated), 'complete outcome has truncated log line')
    return {'available': lifecycle_path.exists() and progress_path.exists(),
            'lifecycle_available': lifecycle_path.exists(), 'progress_available': progress_path.exists(),
            'all_records_complete': not (life_truncated or progress_truncated),
            'truncated_lifecycle_tail': life_truncated, 'truncated_progress_tail': progress_truncated,
            'counts': counts, 'lifecycle_phases': names,
            'scope': 'available_prefix_records_linked_to_committed_payloads'}


def declared_custody(campaign, binary=None, source=None):
    rec = read_json(campaign/'final-custody.json')
    demand(rec['status'] == 'PASS', 'final custody declaration failed')
    recorded = rec['pins']
    demand(set(recorded) == set(PIN_HASHES) | {'binary'} and
           all(recorded[name] == expected for name, expected in PIN_HASHES.items()),
           'source manifest declarations differ from reviewed pin')
    executable_hash = recorded['binary']
    demand(isinstance(executable_hash, str) and len(executable_hash) == 64 and
           all(c in '0123456789abcdef' for c in executable_hash), 'invalid executable hash declaration')
    demand(contract_equal(hash_file(campaign/'exact_input.txt'), rec['input']), 'serialized input custody differs')
    if binary is not None:
        demand(binary.is_file() and not binary.is_symlink() and
               hash_file(binary)['sha256'] == executable_hash, 'copied binary hash differs')
    if source is not None:
        for name, expected in PIN_HASHES.items():
            path = safe_member(source, name)
            demand(path.is_file() and hash_file(path)['sha256'] == expected, 'copied source hash differs: '+name)
    return {'source_pin_declarations_match': True, 'copied_source_rehashed': source is not None,
            'copied_binary_rehashed': binary is not None,
            'original_execution_independently_authenticated': False}


def audit_campaign(campaign, allow_incomplete=False, all_norms=False, binary=None, source=None):
    demand(campaign.is_absolute() and campaign.is_dir() and not campaign.is_symlink(),
           'absolute closed offline campaign directory required')
    # This final receipt is produced only after child closure by the pinned runner.
    # The auditor cannot authenticate who wrote it, and does not contact /proc.
    summary = read_json(campaign/'summary.json')
    complete_status = summary['status'] in ('COMPLETE_PRECISION_GOAL_MET', 'COMPLETE_PRECISION_UNRESOLVED')
    demand(summary['scope'] == SCOPE and isinstance(summary['ended_utc'], str) and summary['ended_utc'],
           'closed summary scope/end missing')
    demand(summary['first_outcome_preserved'] is True and summary['retry_or_resume_performed'] is False and
           contract_equal(summary['total_seconds'], 86400) and contract_equal(summary['required_children'], 1),
           'single-attempt resource declaration differs')
    demand(type(summary['attempted_launches']) is int and type(summary['launched_children']) is int and
           0 <= summary['launched_children'] <= summary['attempted_launches'] <= 1,
           'attempt/launch count outside contract')
    demand(complete_status or (allow_incomplete and summary['status'] == 'NOT_CERTIFIED'),
           'incomplete outcome requires --allow-incomplete')
    state = campaign/'full-state'
    demand(not state.is_symlink() and (state.is_dir() or (not complete_status and not state.exists())),
           'offline full-state directory missing or unsafe')
    inventory = read_json(campaign/'artifact-inventory.json')
    check_inventory_flag(summary, inventory)
    actual, inventory_complete = inventory_audit(state, inventory)
    demand(not complete_status or inventory_complete, 'complete outcome lacks complete inventory')
    cp, terminal, placements, checkpoint_totals = checkpoint_audit(state, actual, complete_status, all_norms)
    report = {'schema': 'INDEPENDENT_SAVED_AUDIT_V1', 'reviewed_source_pin': PIN,
              'original_outcome': summary['status'], 'scope': SCOPE,
              'inventory_complete': inventory_complete, 'state_artifacts_rehashed': len(actual),
              'full_state_directory_available': state.is_dir(),
              'checkpoint_audit': cp, 'full_propagation_independently_reexecuted': False,
              'intermediate_quintics_or_node_bounds_independently_recomputed': False,
              'restored_coherence_intervals_independently_recomputed': False,
              'precision_goal_pass': None, 'nonlinear_discrepancy_resolved_for_both_signs': None}
    if not complete_status:
        metadata_files = [state/name for name in ('metadata.json','layout.txt','basis.json')]
        metadata_available = all(path.exists() for path in metadata_files)
        metadata_audit(state, allow_missing=True)
        report['metadata_validated'] = metadata_available
        report['metadata_state'] = 'VALIDATED' if metadata_available else 'INCOMPLETE_OR_PRELAUNCH_MISSING'
        report['progress_audit'] = logs_audit(state, checkpoint_totals, False)
        report['full_account_validated'] = False
        report['source_custody_declaration_available'] = (campaign/'final-custody.json').exists()
        if report['source_custody_declaration_available'] and summary.get('custody_verified') is True:
            report['custody'] = declared_custody(campaign, binary, source)
        prefix_checks_complete = (cp['snapshots'] > 0 and inventory_complete and metadata_available and
                                 report['progress_audit']['available'] and
                                 report['progress_audit']['all_records_complete'] and
                                 'custody' in report)
        report['status'] = 'SAVED_COMMITTED_PREFIX_AUDIT_PASS' if prefix_checks_complete else 'PARTIAL_EVIDENCE_ONLY'
        return report
    demand(summary['attempted_launches'] == summary['launched_children'] == 1 and
           summary['custody_verified'] is True and summary['full_trajectory_certificate'] is True and
           summary['artifact_inventory_complete'] is True and not summary.get('failure') and
           not summary.get('failure_history'), 'complete summary integrity declaration')
    report['custody'] = declared_custody(campaign, binary, source)
    receipt = read_json(campaign/'full-receipt.json')
    check_final_receipt(receipt)
    demand((campaign/'full.stderr').read_bytes() == b'', 'nonempty recorded child stderr')
    for name in ('full.stdout', 'full.stderr'):
        demand(contract_equal(hash_file(campaign/name), summary['streams'][name]), 'summary stream custody differs')
    demand((campaign/'full.stdout').read_bytes() == (state/'result.json').read_bytes(),
           'child stdout differs from final JSON')
    top = {name for name in actual if '/' not in name}
    demand(top == {'layout.txt', 'basis.json', 'metadata.json', 'lifecycle.jsonl', 'progress.jsonl',
                   'endpoints.bin', 'components.bin', 'result.json'}, 'unexpected/missing final state root artifact')
    weights = metadata_audit(state)
    record = read_json(state/'result.json')
    account = final_audit(state, record, weights, terminal, placements)
    report['progress_audit'] = logs_audit(state, checkpoint_totals, True)
    demand(summary['precision_goal_pass'] is account['precision_goal_pass'] and
           summary['nonlinear_discrepancy_resolved_for_both_signs'] is
               account['nonlinear_discrepancy_resolved_for_both_signs'], 'summary decision disagrees with exact saved account')
    demand((summary['status'] == 'COMPLETE_PRECISION_GOAL_MET') is account['precision_goal_pass'],
           'precision label disagrees with exact saved radius')
    report.update(account)
    report['status'] = 'SAVED_FULL_ACCOUNT_AUDIT_PASS'
    report['full_account_validated'] = True
    report['full_account_validation_scope'] = 'saved_consistency_and_exact_aggregation_only'
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--campaign', type=Path, required=True)
    parser.add_argument('--allow-incomplete', action='store_true')
    parser.add_argument('--all-snapshot-norms', action='store_true')
    parser.add_argument('--binary', type=Path, help='optional copied binary: hash only, never execute')
    parser.add_argument('--source', type=Path, help='optional offline source copy: hash only, never import')
    args = parser.parse_args(argv)
    try:
        result = audit_campaign(args.campaign, args.allow_incomplete, args.all_snapshot_norms,
                                args.binary, args.source)
    except (AuditError, OSError, ValueError, TypeError, KeyError, IndexError, OverflowError) as exc:
        result = {'status': 'SAVED_AUDIT_REJECTED', 'reason': str(exc),
                  'reviewed_source_pin': PIN, 'full_account_validated': False}
    sys.stdout.write(json.dumps(result, sort_keys=True, ensure_ascii=True, allow_nan=False)+'\n')
    return 0 if result['status'] in ('SAVED_FULL_ACCOUNT_AUDIT_PASS', 'SAVED_COMMITTED_PREFIX_AUDIT_PASS') else 2


if __name__ == '__main__':
    raise SystemExit(main())
