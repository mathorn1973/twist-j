#!/usr/bin/env python3
"""One bounded fixed full-word attempt; Apache-2.0, PUBLIC NON-CANONICAL.

Importing this driver performs no scientific execution. Only main imports the
adjacent pinned decimal serializer, after source custody has been checked.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import shutil
import signal
import struct
import subprocess
import sys
import time

SOURCES = {'README.md', 'PREREG.md', 'DERIVATION.md', 'EXACT-DESIGN.md',
           'verify.py', 'input.json', 'prepare_input.py', 'validated_model.hpp',
           'validated_model.cpp', 'kernel.cpp', 'higher_order.hpp',
           'dp5_tableau.hpp', 'full.cpp', 'full_run.py'}
SCOPE = 'FULL_WORD_SIX_CASES_K3_CONDITIONAL'
TOTAL_SECONDS, RESERVE_SECONDS, CLEANUP_SECONDS = 86400, 300, 30
FIELDS = ('guard', 'tail', 'continuum', 'jumps', 'total',
          'sampled_time_node_L2', 'sampled_projection_node_L2',
          'sampled_arithmetic_node_L2', 'maximum_node_bound', 'maximum_norm_error',
          'endpoint_norm_squared_lo', 'endpoint_norm_squared_hi')
LABELS = ((4, 3), (4, 4), (1, 1))
PAIRS = ((0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5))
TAIL = Q(680046581, 794280046581)
RETAINED = 1-TAIL
THRESHOLD = Q(1, 1000)
ENDPOINT_BYTES, COMPONENT_BYTES, PAYLOAD_BYTES = 823680, 768, 824448
LAYOUT = ('FULL_WORD_SEGMENT_CHECKPOINTS_V1\nsteps=384\nintegrator=DP5_TWO_HALF_STEPS\n'
    'dense_curve=QUINTIC_THREE_POINT_HERMITE\nsubsteps_per_cell=2\nrhs_per_cell=13\n'
    'segment_boundaries=81\ncases=6\ncolumns=120\nbatch_columns=8\ndimension=6435\ncomponents=12\n'
    'checkpoint_payload=lane,basis,re_im;then_lane,field\ncheckpoint_endpoint_bytes=823680\n'
    'checkpoint_component_bytes=768\ncheckpoint_bytes=824448\n'
    'final_endpoints=case,column,basis,re_im\nfinal_components=case,column,field\n'
    'encoding=little_endian_IEEE_binary64\ncommit=checkpoint-N.json_after_payload_rename\n')


def utc():
    return datetime.now(timezone.utc).isoformat()


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def budget(deadline):
    require(time.perf_counter() < deadline, 'numerical campaign deadline exhausted')


def digest(path, deadline=None):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while True:
            if deadline is not None:
                budget(deadline)
            block = stream.read(4*1024*1024)
            if not block:
                return h.hexdigest()
            h.update(block)


def artifact(path, deadline=None):
    return {'bytes': path.stat().st_size, 'sha256': digest(path, deadline)}


def save(path, value):
    with path.open('x', encoding='ascii', newline='\n') as stream:
        json.dump(value, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write('\n')


def finite(value):
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, dict):
        return all(finite(v) for v in value.values())
    if isinstance(value, list):
        return all(finite(v) for v in value)
    return True


def load(path):
    value = json.loads(path.read_bytes())
    require(finite(value), 'nonfinite JSON: '+path.name)
    return value


def pins(source, binary, deadline=None):
    found = {}
    for line in (source/'SOURCE_SHA256SUMS').read_text('ascii').splitlines():
        expected, name = line.split('  ')
        require(name in SOURCES and name not in found, 'manifest inventory')
        require(digest(source/name, deadline) == expected, 'source changed: '+name)
        found[name] = expected
    require(set(found) == SOURCES, 'incomplete source manifest')
    found['SOURCE_SHA256SUMS'] = digest(source/'SOURCE_SHA256SUMS', deadline)
    found['binary'] = digest(binary, deadline)
    return found


def topology():
    require(sys.platform == 'linux', 'Linux required')
    cpus = sorted(os.sched_getaffinity(0))
    require(cpus == list(range(80)), 'exact CPU affinity 0..79 required')
    rows = []
    for cpu in cpus:
        root = Path('/sys/devices/system/cpu')/('cpu'+str(cpu))/'topology'
        rows.append({'cpu': cpu, 'package': int((root/'physical_package_id').read_text()),
                     'core': int((root/'core_id').read_text())})
    cores = {(r['package'], r['core']) for r in rows}
    require(len(cores) == 40 and len({r['package'] for r in rows}) == 2,
            'two packages and forty physical cores required')
    require(all(sum((r['package'], r['core']) == core for r in rows) == 2
                for core in cores), 'both SMT siblings required')
    flags = [set(line.split(':', 1)[1].split()) for line in
             Path('/proc/cpuinfo').read_text().splitlines() if line.startswith('flags')]
    require(flags and all({'avx512f', 'avx512dq', 'avx512vl'} <= f for f in flags),
            'AVX512F/DQ/VL required')
    return rows, cpus


def resources(out):
    available = {}
    for line in Path('/proc/meminfo').read_text().splitlines():
        key, value = line.split(':', 1)
        if key == 'MemAvailable':
            number, unit = value.split()
            require(unit == 'kB', 'memory unit')
            available['mem_available_bytes'] = int(number)*1024
    available['disk_free_bytes'] = shutil.disk_usage(out).free
    require(available.get('mem_available_bytes', 0) >= 64*1024**3, '64 GiB MemAvailable required')
    require(available['disk_free_bytes'] >= 16*1024**3, '16 GiB free output storage required')
    return available


def child_env(cpus):
    overrides = {'OMP_NUM_THREADS': '80', 'OMP_DYNAMIC': 'FALSE',
                 'OMP_MAX_ACTIVE_LEVELS': '1', 'OMP_NESTED': 'FALSE',
                 'OMP_PROC_BIND': 'TRUE', 'OMP_PLACES': ','.join('{'+str(c)+'}' for c in cpus),
                 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
                 'LC_ALL': 'C', 'LANG': 'C', 'PYTHONHASHSEED': '0',
                 'PYTHONDONTWRITEBYTECODE': '1'}
    env = os.environ.copy()
    env.update(overrides)
    return env, overrides


def interrupted(signum, frame):
    raise RuntimeError('Interrupted by signal '+str(signum))


def stop_group(proc):
    until = time.perf_counter()+CLEANUP_SECONDS
    old = {sig: signal.signal(sig, signal.SIG_IGN) for sig in (signal.SIGTERM, signal.SIGINT)}
    try:
        if proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                proc.wait(timeout=min(5, max(0, until-time.perf_counter())))
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                proc.wait(timeout=max(0, until-time.perf_counter()))
        return None
    except BaseException as exc:
        return repr(exc)
    finally:
        for sig, handler in old.items():
            signal.signal(sig, handler)


def capture(out, command, env, child_deadline):
    started, start_utc = time.perf_counter(), utc()
    proc = None
    error = cleanup_error = None
    with (out/'full.stdout').open('xb') as sout, (out/'full.stderr').open('xb') as serr:
        try:
            budget(child_deadline)
            proc = subprocess.Popen(command, stdout=sout, stderr=serr, env=env,
                                    start_new_session=True)
            save(out/'full-launch.json', {'pid': proc.pid, 'command': command,
                 'started_utc': start_utc, 'remaining_child_seconds': child_deadline-started})
            proc.wait(timeout=max(0, child_deadline-time.perf_counter()))
        except BaseException as exc:
            error = repr(exc)
            if proc is not None:
                cleanup_error = stop_group(proc)
    receipt = {'started_utc': start_utc, 'ended_utc': utc(),
               'wall_seconds': time.perf_counter()-started,
               'pid': proc.pid if proc else None,
               'exit_code': proc.returncode if proc else None,
               'error': error, 'cleanup_error': cleanup_error}
    save(out/'full-receipt.json', receipt)
    return receipt


def sum_up(a, b):
    exact = Q(a)+Q(b)
    value = float(exact)
    require(math.isfinite(value), 'finite directed sum')
    if Q(value) < exact:
        value = math.nextafter(value, math.inf)
    require(math.isfinite(value), 'finite directed sum result')
    return value


def component_rows(raw):
    require(len(raw) % 96 == 0, 'component alignment')
    rows = list(struct.iter_unpack('<12d', raw))
    for row in rows:
        require(all(math.isfinite(v) and v >= 0 for v in row) and row[10] <= row[11],
                'component finite nonnegative domain')
        require(row[4] == sum_up(sum_up(row[0], row[1]), sum_up(row[2], row[3])),
                'exact upward cumulative component sum')
    return rows


def active(case, segment):
    return any((label+segment//16) % 5 == 0 for label in LABELS[case % 3])


def inventory(state, deadline):
    records, errors = {}, []
    complete = True
    if state.exists():
        for path in sorted(state.rglob('*')):
            try:
                require(not path.is_symlink(), 'symlink in output')
                if path.is_dir():
                    continue
                records[path.relative_to(state).as_posix()] = artifact(path, deadline)
            except BaseException as exc:
                complete = False
                errors.append({'file': path.relative_to(state).as_posix(), 'error': repr(exc)})
                if time.perf_counter() >= deadline:
                    break
    return {'complete': complete, 'files': records, 'errors': errors}


def audit_checkpoints(state, inv, deadline, need_complete):
    """Audit committed prefixes; orphan binaries and temporary files remain evidence."""
    result = {'status': 'VALID_COMMITTED_PREFIXES', 'committed_snapshots': 0,
              'complete_tasks': 0, 'inactive_payload_identities': 0,
              'component_monotonicity_comparisons': 0, 'tasks': []}
    recognized = set()
    for case in range(6):
        for batch in range(15):
            budget(deadline)
            folder = state/'checkpoints'/('case-'+str(case))/('batch-'+str(batch))
            numbers = sorted(int(p.stem.split('-')[1]) for p in folder.glob('checkpoint-*.json'))
            require(not numbers or numbers == list(range(numbers[-1]+1)), 'checkpoint prefix hole')
            require(not numbers or numbers[-1] <= 80, 'checkpoint outside full word')
            previous = previous_hash = placement = None
            active_count = 0
            for boundary in numbers:
                budget(deadline)
                if boundary:
                    active_count += int(active(case, boundary-1))
                marker = folder/('checkpoint-'+str(boundary)+'.json')
                rec = load(marker)
                expected = {'schema': 'FULL_SEGMENT_CHECKPOINT_V1', 'scope': SCOPE,
                    'case': case, 'batch': batch, 'segment_boundary': boundary,
                    'physical_time_seconds_rational': [boundary, 160000],
                    'thermal_column_start': batch*8, 'thermal_columns': 8, 'dimension': 6435,
                    'cumulative_cells': active_count*384, 'active_segments_completed': active_count,
                    'payload': 'checkpoint-'+str(boundary)+'.bin', 'payload_bytes': PAYLOAD_BYTES,
                    'endpoint_bytes': ENDPOINT_BYTES, 'component_bytes': COMPONENT_BYTES,
                    'component_offset': ENDPOINT_BYTES, 'component_fields': list(FIELDS)}
                require(all(rec[k] == value for k, value in expected.items()), 'checkpoint metadata contract')
                require(type(rec['cpu']) is int and type(rec['place']) is int and
                        0 <= rec['cpu'] < 80 and 0 <= rec['place'] < 80, 'checkpoint placement')
                if placement is None:
                    placement = (rec['cpu'], rec['place'])
                require(placement == (rec['cpu'], rec['place']), 'task checkpoint migration')
                payload = folder/rec['payload']
                key = payload.relative_to(state).as_posix()
                require(key in inv['files'] and inv['files'][key]['bytes'] == PAYLOAD_BYTES,
                        'committed payload missing or truncated')
                recognized.update((key, marker.relative_to(state).as_posix()))
                with payload.open('rb') as stream:
                    stream.seek(ENDPOINT_BYTES)
                    rows = component_rows(stream.read())
                require(len(rows) == 8, 'checkpoint lane count')
                if boundary == 0:
                    require(all(all(v == 0 for v in row[:10]) and row[10:] == (1, 1) for row in rows),
                            'initial certificate and norm')
                    # Exact initial basis payload, not a norm-only initial-state claim.
                    initial = bytearray(ENDPOINT_BYTES)
                    for lane in range(8):
                        struct.pack_into('<d', initial, (lane*6435+batch*8+lane)*16, 1)
                    with payload.open('rb') as stream:
                        require(stream.read(ENDPOINT_BYTES) == initial, 'initial basis state payload')
                if previous is not None:
                    require(all(rows[lane][k] >= previous[lane][k] for lane in range(8) for k in range(10)),
                            'checkpoint cumulative component decreased')
                    result['component_monotonicity_comparisons'] += 80
                    if not active(case, boundary-1):
                        require(inv['files'][key]['sha256'] == previous_hash,
                                'inactive segment changed state or certificate bytes')
                        result['inactive_payload_identities'] += 1
                previous, previous_hash = rows, inv['files'][key]['sha256']
                result['committed_snapshots'] += 1
            complete = len(numbers) == 81
            result['complete_tasks'] += int(complete)
            result['tasks'].append({'case': case, 'batch': batch, 'committed_snapshots': len(numbers),
                                    'last_boundary': numbers[-1] if numbers else None,
                                    'cumulative_cells': active_count*384, 'complete': complete})
    result['uncommitted_files'] = sorted(k for k in inv['files']
                                         if k.startswith('checkpoints/') and k not in recognized)
    if need_complete:
        require(result['committed_snapshots'] == 7290 and result['complete_tasks'] == 90 and
                result['inactive_payload_identities'] == 5280 and not result['uncommitted_files'],
                'complete checkpoint inventory')
    return result


def interval(value):
    require(len(value) == 2 and value[0] <= value[1], 'ordered interval')
    return Q(value[0]), Q(value[1])


def above_sqrt_affine(bound, coefficient, constant, radicand):
    difference = bound-constant
    return difference >= 0 and difference*difference >= coefficient*coefficient*radicand


def square_interval(lo, hi):
    return (Q(0) if lo <= 0 <= hi else min(lo*lo, hi*hi), max(lo*lo, hi*hi))


def validate_final(state, record, cpus, deadline):
    fixed = {'status': 'COMPLETED', 'scope': SCOPE,
             'error_account_scope': 'normwise_ball_full_space_defect',
             'full_trajectory_certificate': True, 'final_coherences_computed': True,
             'cutoff': 8, 'guard': 10, 'dimension': 6435, 'guard_dimension': 19448,
             'steps_per_segment': 384, 'integrator': 'DP5_TWO_HALF_STEPS',
             'dense_curve': 'QUINTIC_THREE_POINT_HERMITE', 'thermal_columns': 120,
             'thermal_cutoff': 3, 'cases': 6, 'threads': 80, 'simd_lanes': 8,
             'final_time_seconds_rational': [1, 2000], 'completed_tasks': 90,
             'committed_snapshots': 7290, 'trajectory_initializations': 90,
             'state_and_certificate_carry_checks': 7200, 'polynomial_start_checks': 737280,
             'certificate_monotonicity_checks': 737280, 'inactive_identity_checks': 5280,
             'active_task_segments': 1920, 'worker_arithmetic_fixtures': 80, 'migrations': 0,
             'reset_between_checkpoints': False, 'normalization_applied': False, 'phase_fit_applied': False}
    require(finite(record) and all(record[k] == v for k, v in fixed.items()), 'full result contract')
    require(all(record[k] > 0 for k in ('preparation_seconds', 'model_preparation_seconds',
                                      'kernel_seconds', 'end_to_end_seconds')), 'positive timings')
    require(record['end_to_end_seconds'] >= record['kernel_seconds'] and
            record['preparation_seconds'] >= record['model_preparation_seconds'], 'timing order')
    fixtures = record['fixtures']
    require(all(fixtures[k] is True for k in ('directed_arithmetic', 'zero_displacement_enclosure',
            'adjoint_enclosure', 'ball_interval_fixture_enclosure')) and
            0 <= fixtures['dense_displacement_error'] <= 1e-11 and
            0 <= fixtures['collective_displacement_error'] <= 1e-11 and
            0 <= fixtures['ball_reference_radius_ratio'] <= 1, 'runtime fixture outcome')
    workers = record['thread_map']
    require(len(workers) == 80 and sorted(w['thread'] for w in workers) == list(range(80)) and
            sorted(w['cpu'] for w in workers) == cpus and sorted(w['place'] for w in workers) == cpus and
            all(w['completed_tasks'] > 0 and w['cpu'] == w['place'] for w in workers) and
            sum(w['completed_tasks'] for w in workers) == 90,
            'worker coverage and task inventory')
    require((state/'layout.txt').read_bytes() == LAYOUT.encode('ascii'), 'binary layout contract')
    meta = load(state/'metadata.json')
    metadata_fixed = {'scope': SCOPE, 'cutoff': 8, 'guard': 10, 'steps_per_segment': 384,
         'integrator': 'DP5_TWO_HALF_STEPS', 'dense_curve': 'QUINTIC_THREE_POINT_HERMITE',
         'substeps_per_cell': 2, 'rhs_per_cell': 13, 'original_segments': 80,
         'segment_seconds_rational': [1, 160000], 'final_time_seconds_rational': [1, 2000],
         'cases': 6, 'thermal_columns': 120, 'thermal_cutoff': 3, 'dimension': 6435,
         'guard_dimension': 19448, 'tasks': 90, 'required_snapshots': 7290, 'required_cells': 737280,
         'required_active_task_segments': 1920, 'required_inactive_task_segments': 5280,
         'initial_state_in_moving_frame': True, 'reset_between_checkpoints': False,
         'fsal_between_cells': False, 'normalization_applied': False, 'phase_fit_applied': False,
         'task_case_order': [1, 2, 4, 5, 0, 3], 'component_fields': list(FIELDS),
         'case_active_cells': [12288, 6144, 6144, 12288, 6144, 6144]}
    require(all(meta[k] == v for k, v in metadata_fixed.items()), 'metadata contract')
    basis = load(state/'basis.json')
    require(all(basis[k] == v for k, v in {'scope': SCOPE, 'cutoff': 8, 'guard': 10, 'thermal_cutoff': 3}.items()),
            'basis metadata')
    occupations = basis['occupations']
    require(len(occupations) == 6435 and len({tuple(n) for n in occupations}) == 6435 and
            all(len(n) == 7 and all(type(k) is int and k >= 0 for k in n) and sum(n) <= 8 for n in occupations),
            'full finite occupation basis')
    require([sum(n) for n in occupations] == sorted(sum(n) for n in occupations) and
            [sum(sum(n) == grade for n in occupations[:120]) for grade in range(4)] == [1, 7, 28, 84],
            'thermal initial basis ordering')
    weights = [Q(20, 21)**7*Q(1, 21)**sum(n) for n in occupations[:120]]
    require(sum(weights) == RETAINED and len(meta['thermal_weights']) == 120, 'thermal retained mass')
    for weight, bounds in zip(weights, meta['thermal_weights']):
        lo, hi = interval(bounds)
        require(0 <= lo <= weight <= hi, 'prepared thermal enclosure')
    for data, target in ((meta['thermal_tail'], TAIL), (record['thermal_tail'], TAIL),
                         (record['retained_thermal_weight'], RETAINED)):
        lo, hi = interval(data)
        require(0 <= lo <= target <= hi <= 1, 'thermal mass enclosure')
    require(interval(record['legacy_eta_mismatch'])[0] >= 0, 'legacy mismatch diagnostic')
    raw = (state/'components.bin').read_bytes()
    require(len(raw) == 69120 and (state/'endpoints.bin').stat().st_size == 74131200, 'final artifact sizes')
    rows = component_rows(raw)
    with (state/'endpoints.bin').open('rb') as endpoint:
        for case in range(6):
            for batch in range(15):
                budget(deadline)
                path = state/'checkpoints'/('case-'+str(case))/('batch-'+str(batch))/'checkpoint-80.bin'
                payload = path.read_bytes()
                require(endpoint.read(ENDPOINT_BYTES) == payload[:ENDPOINT_BYTES], 'final endpoint/snapshot byte agreement')
                offset = (case*120+batch*8)*96
                require(raw[offset:offset+COMPONENT_BYTES] == payload[ENDPOINT_BYTES:], 'final component/snapshot byte agreement')
    require(len(record['branches']) == 6, 'branch inventory')
    errors, norms = [], []
    component_names = ('guard_component', 'tail_component', 'continuum_component', 'jump_component',
                       'sampled_time_node_L2', 'sampled_projection_node_L2', 'sampled_arithmetic_node_L2')
    for case, branch in enumerate(record['branches']):
        budget(deadline)
        require(branch['case'] == case and branch['labels'] == list(LABELS[case % 3]) and
                branch['node_split_scope'] == 'diagnostic_quadrature_only_continuum_allowance_is_combined',
                'branch identity and diagnostic scope')
        interval(branch['linear_phase'])
        require(len(branch['linear_alpha']) == 7, 'linear mode inventory')
        for alpha in branch['linear_alpha']:
            for bounds in alpha:
                interval(bounds)
        require(len(branch['columns']) == 120, 'branch column inventory')
        for n, col in enumerate(branch['columns']):
            require(col['thermal_index'] == n and all(struct.pack('<d', col[name]) ==
                    struct.pack('<d', rows[case*120+n][k]) for k, name in enumerate(FIELDS[:10])),
                    'JSON/raw column byte agreement')
        e, a = Q(branch['error_bound']), Q(branch['weighted_endpoint_norm'])
        require(e >= 0 and a >= 0 and e*e >= sum(weights[n]*Q(rows[case*120+n][4])**2 for n in range(120)),
                'weighted error RMS upper enclosure')
        # Component norm upper endpoints enclose exact dyadic endpoint norms.
        require(a*a >= sum(weights[n]*Q(rows[case*120+n][11]) for n in range(120)),
                'weighted stored endpoint norm enclosure')
        errors.append(e)
        norms.append(a)
        for name, field in zip(component_names, (0, 1, 2, 3, 5, 6, 7)):
            upper = Q(branch[name])
            require(upper >= 0 and upper*upper >= sum(weights[n]*Q(rows[case*120+n][field])**2 for n in range(120)),
                    'weighted component RMS enclosure')
    require(len(record['pair_coherences']) == 6, 'final pair inventory')
    decisions = []
    for pair, expected in zip(record['pair_coherences'], PAIRS):
        require(pair['cases'] == list(expected), 'within-sign pair identity')
        c, d = expected
        numerical, thermal, arithmetic, total = (Q(pair[k]) for k in
                  ('numerical_radius', 'thermal_radius', 'arithmetic_radius', 'total_radius'))
        require(min(numerical, thermal, arithmetic, total) >= 0, 'nonnegative pair radii')
        require(above_sqrt_affine(2*numerical, errors[c], norms[c]*errors[d], RETAINED) or
                above_sqrt_affine(2*numerical, errors[d], norms[d]*errors[c], RETAINED),
                'nonunit Gram minimum enclosure')
        require(thermal >= TAIL/2, 'single omitted thermal contribution')
        centerlo, centerhi = interval(pair['witness_center_interval'])
        sqlo = sqhi = Q(0)
        require(len(pair['sine_retained_interval']) == len(pair['linear_full_interval']) == 2,
                'complex coherence interval shape')
        for a, b in zip(pair['sine_retained_interval'], pair['linear_full_interval']):
            alo, ahi = interval(a)
            blo, bhi = interval(b)
            lo, hi = square_interval(alo-bhi, ahi-blo)
            sqlo += lo
            sqhi += hi
        require(centerlo >= 0 and (2*centerlo)**2 <= sqlo and (2*centerhi)**2 >= sqhi,
                'complex rectangle magnitude enclosure')
        require(arithmetic >= (centerhi-centerlo)/2 and total >= numerical+thermal+arithmetic,
                'total radius includes arithmetic halfwidth once')
        lo, hi = interval(pair['certified_trace_distance_interval'])
        require(0 <= lo <= max(Q(0), centerlo-numerical-thermal) and
                min(Q(1), centerhi+numerical+thermal) <= hi <= 1, 'final clipped interval enclosure')
        decisions.append({'cases': list(expected), 'precision_goal_pass': total <= THRESHOLD,
             'total_radius_exact': str(total), 'distance_interval_exact': [str(lo), str(hi)],
             'discrepancy': 'EXCEEDS_TARGET' if lo > THRESHOLD else 'WITHIN_TARGET' if hi <= THRESHOLD else 'UNRESOLVED'})
    return {'status': 'VALID_FULL_FIXED_MODEL_ACCOUNT', 'scope': SCOPE,
            'threshold_exact': str(THRESHOLD), 'pairs': decisions,
            'precision_goal_pass': all(p['precision_goal_pass'] for p in decisions),
            'nonlinear_discrepancy_resolved_for_both_signs': all(any(p['discrepancy'] == 'EXCEEDS_TARGET'
                for p in decisions[3*sign:3*sign+3]) for sign in range(2)),
            'runtime_node_enclosures_independently_recomputed': False,
            'arithmetic_check_scope': 'exact_saved_aggregation_and_checkpoint_custody'}


def validate_logs(state, deadline):
    phases = [load_line for load_line in (json.loads(line) for line in
              (state/'lifecycle.jsonl').read_text('ascii').splitlines())]
    required = ['model_preparation_started', 'model_preparation_completed', 'fixtures_completed',
                'worker_coverage_validated', 'full_word_scan_completed', 'full_time_restoration_completed']
    require(finite(phases) and [r['phase'] for r in phases] == required and
            all(0 <= a['elapsed_seconds'] <= b['elapsed_seconds'] for a, b in zip(phases, phases[1:])),
            'lifecycle phases/timing')
    counts = {'cells': 0, 'checkpoint': 0, 'task_completed': 0}
    last_cells, last_boundary, completed = {}, {}, set()
    with (state/'progress.jsonl').open(encoding='ascii') as stream:
        for line in stream:
            budget(deadline)
            row = json.loads(line)
            require(finite(row), 'finite progress')
            case, batch = row['case'], row['batch']
            require(type(case) is int and 0 <= case < 6 and type(batch) is int and 0 <= batch < 15,
                    'progress task identity')
            key = case, batch
            kind = row['kind']
            require(kind in counts and row['elapsed_seconds'] >= 0, 'progress kind/time')
            counts[kind] += 1
            cells = row['cells']
            if kind == 'cells':
                require(cells == last_cells.get(key, 0)+32 and active(case, row['original_segment']) and
                        1 <= row['cell_in_segment'] <= 384 and row['cell_in_segment'] % 32 == 0 and
                        row['total_cells'] == (12288 if case % 3 == 0 else 6144) and row['error_bound_max'] >= 0,
                        'cell progress chronology')
                expected = 384*sum(active(case, s) for s in range(row['original_segment']))+row['cell_in_segment']
                require(cells == expected, 'progress absolute cell inventory')
                last_cells[key] = cells
            elif kind == 'checkpoint':
                boundary = row['segment_boundary']
                require(boundary == last_boundary.get(key, 0)+1 and 1 <= boundary <= 80 and
                        cells == 384*sum(active(case, s) for s in range(boundary)), 'checkpoint progress chronology')
                last_boundary[key] = boundary
            else:
                require(key not in completed and last_boundary.get(key) == 80 and
                        cells == (12288 if case % 3 == 0 else 6144), 'completed progress task')
                completed.add(key)
    require(counts == {'cells': 23040, 'checkpoint': 7200, 'task_completed': 90} and len(completed) == 90,
            'complete progress inventory')
    return {'status': 'PASS', 'counts': counts, 'lifecycle_phases': required}


def main():
    started, started_utc = time.perf_counter(), utc()
    deadline = started+TOTAL_SECONDS
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    require(args.binary.is_absolute() and args.output.is_absolute(), 'absolute CLI paths required')
    source, binary, out = Path(__file__).resolve().parent, args.binary.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    state = out/'full-state'
    signal.signal(signal.SIGTERM, interrupted)
    signal.signal(signal.SIGINT, interrupted)
    initial = input_pin = receipt = account = checkpoint_audit = final_pins = None
    inv = {'complete': False, 'files': {}, 'errors': []}
    failure, status, launched, attempted = None, 'NOT_CERTIFIED', False, False
    failures, custody_verified = [], False
    try:
        initial = pins(source, binary, deadline)
        save(out/'source-pins.json', initial)
        cpu_rows, cpus = topology()
        env, overrides = child_env(cpus)
        resource_record = resources(out)
        save(out/'metadata.json', {'started_utc': started_utc, 'python': platform.python_version(),
             'scope': SCOPE, 'topology': cpu_rows, 'environment': overrides,
             'resources': resource_record, 'loadavg': os.getloadavg(),
             'total_seconds': TOTAL_SECONDS, 'postprocessing_reserve_seconds': RESERVE_SECONDS,
             'cleanup_seconds': CLEANUP_SECONDS, 'required_children': 1})
        spec = importlib.util.spec_from_file_location('pinned_decimal_serializer', source/'prepare_input.py')
        serializer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(serializer)
        save(out/'input-pin.json', serializer.serialize(source/'input.json', out/'exact_input.txt'))
        input_pin = artifact(out/'exact_input.txt', deadline)
        require(pins(source, binary, deadline) == initial, 'prelaunch source custody')
        require(artifact(out/'exact_input.txt', deadline) == input_pin, 'prelaunch input custody')
        save(out/'launch-resources.json', resources(out))
        child_deadline = deadline-RESERVE_SECONDS
        budget(child_deadline)
        attempted = True
        receipt = capture(out, [str(binary), '--input', str(out/'exact_input.txt'), '--output', str(state)],
                          env, child_deadline)
        launched = receipt['pid'] is not None
        require(pins(source, binary, deadline) == initial, 'post-child source custody')
        require(artifact(out/'exact_input.txt', deadline) == input_pin, 'post-child input custody')
        # Inventory is performed before deciding whether the child succeeded.
        inv = inventory(state, deadline)
        save(out/'artifact-inventory.json', inv)
        require(inv['complete'], 'artifact inventory incomplete')
        good_child = receipt['exit_code'] == 0 and receipt['error'] is None and receipt['cleanup_error'] is None
        checkpoint_audit = audit_checkpoints(state, inv, deadline, good_child)
        save(out/'checkpoint-audit.json', checkpoint_audit)
        require(good_child, 'child did not complete cleanly')
        require((out/'full.stderr').stat().st_size == 0, 'child stderr is nonempty')
        require((state/'result.json').read_bytes() == (out/'full.stdout').read_bytes(), 'stdout/result byte agreement')
        record = load(state/'result.json')
        account = validate_final(state, record, cpus, deadline)
        save(out/'log-audit.json', validate_logs(state, deadline))
        save(out/'pair-account.json', account)
        budget(deadline)
        status = 'COMPLETE_PRECISION_GOAL_MET' if account['precision_goal_pass'] else 'COMPLETE_PRECISION_UNRESOLVED'
    except BaseException as exc:
        failure = repr(exc)
        failures.append(failure)
    finally:
        # Failed-child artifacts are never removed. A late interruption may make
        # inventory incomplete; that fact is explicit and cannot earn a result.
        if not (out/'artifact-inventory.json').exists():
            try:
                inv = inventory(state, deadline)
                save(out/'artifact-inventory.json', inv)
            except BaseException as exc:
                inv['complete'] = False
                inv['errors'].append({'file': None, 'error': repr(exc)})
        try:
            if initial is not None:
                final_pins = pins(source, binary, deadline)
                require(final_pins == initial, 'final source custody')
                if input_pin is not None:
                    require(artifact(out/'exact_input.txt', deadline) == input_pin, 'final input custody')
                save(out/'final-custody.json', {'status': 'PASS', 'pins': final_pins, 'input': input_pin})
                custody_verified = True
            budget(deadline)
        except BaseException as exc:
            status, failure = 'NOT_CERTIFIED', repr(exc)
            failures.append(failure)
        if failure is not None:
            status = 'NOT_CERTIFIED'
        streams = {}
        for name in ('full.stdout', 'full.stderr'):
            if (out/name).exists():
                try:
                    streams[name] = artifact(out/name, deadline)
                except BaseException as exc:
                    streams[name] = {'bytes': (out/name).stat().st_size, 'hash_complete': False, 'error': repr(exc)}
                    status, failure = 'NOT_CERTIFIED', repr(exc)
                    failures.append(failure)
        try:
            budget(deadline)
        except BaseException as exc:
            status, failure = 'NOT_CERTIFIED', repr(exc)
            failures.append(failure)
        # This minimal receipt is allowed after the scientific deadline. It
        # contains no new calculation, certificate acceptance or propagation.
        summary = {'status': status, 'scope': SCOPE, 'started_utc': started_utc, 'ended_utc': utc(),
             'wall_seconds': time.perf_counter()-started, 'total_seconds': TOTAL_SECONDS,
             'failure': failure, 'failure_history': failures, 'attempted_launches': int(attempted),
             'launched_children': int(launched), 'required_children': 1,
             'child_receipt': receipt, 'streams': streams,
             'full_trajectory_certificate': status.startswith('COMPLETE_'),
             'committed_checkpoint_audit': checkpoint_audit,
             'artifact_inventory_complete': inv['complete'], 'hashed_artifacts': len(inv['files']),
             'custody_verified': custody_verified,
             'precision_goal_pass': account['precision_goal_pass'] if status.startswith('COMPLETE_') else None,
             'nonlinear_discrepancy_resolved_for_both_signs': account['nonlinear_discrepancy_resolved_for_both_signs']
                 if status.startswith('COMPLETE_') else None,
             'first_outcome_preserved': True, 'retry_or_resume_performed': False}
        save(out/'summary.json', summary)
        print(json.dumps({'status': status, 'launched_children': int(launched), 'failure': failure}, sort_keys=True), flush=True)
    return 0 if status.startswith('COMPLETE_') else 2


if __name__ == '__main__':
    raise SystemExit(main())
