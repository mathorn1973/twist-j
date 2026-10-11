#!/usr/bin/env python3
"""Fixed short equal-time local-window grid comparison; Apache-2.0, NON-CANONICAL.

No scientific execution or import is performed on importing this driver.
No option enables a full trajectory or changes the frozen resource limits.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import signal
import statistics
import struct
import subprocess
import sys
import time

SOURCES = {'README.md', 'PREREG.md', 'DERIVATION.md', 'EXACT-DESIGN.md',
           'input.json', 'prepare_input.py', 'validated_model.hpp',
           'validated_model.cpp', 'kernel.cpp', 'benchmark.cpp',
           'compare.cpp', 'grid_run.py', 'verify.py'}
ORDER = (512, 256, 256, 512, 512, 256)
PAIRS = {2: (1, 2), 4: (4, 3), 6: (5, 6)}
FIELDS = ('guard', 'tail', 'continuum', 'jumps', 'total',
          'sampled_time_node_L2', 'sampled_projection_node_L2',
          'sampled_arithmetic_node_L2', 'maximum_node_bound', 'maximum_norm_error',
          'endpoint_norm_squared_lo', 'endpoint_norm_squared_hi')
CHILD_SECONDS = 300
TOTAL_SECONDS = 1800
COMPARE_SECONDS = 90
ERROR_GROWTH_TARGET = 2


def utc():
    return datetime.now(timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def artifact(path):
    return {'bytes': path.stat().st_size, 'sha256': digest(path)}


def save(path, value):
    with path.open('x', encoding='ascii', newline='\n') as stream:
        json.dump(value, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write('\n')


def load(path):
    return json.loads(path.read_bytes())


def finite(value):
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, dict):
        return all(finite(x) for x in value.values())
    if isinstance(value, list):
        return all(finite(x) for x in value)
    return True


def pins(source, binaries):
    found = {}
    for line in (source/'SOURCE_SHA256SUMS').read_text('ascii').splitlines():
        expected, name = line.split('  ')
        require(name in SOURCES and name not in found, 'manifest inventory')
        require(digest(source/name) == expected, 'changed source: '+name)
        found[name] = expected
    require(set(found) == SOURCES, 'incomplete source manifest')
    found['SOURCE_SHA256SUMS'] = digest(source/'SOURCE_SHA256SUMS')
    for variant, path in binaries.items():
        found['binary_'+variant] = digest(path)
    return found


def topology():
    require(sys.platform == 'linux', 'Linux required')
    cpus = sorted(os.sched_getaffinity(0))
    require(cpus == list(range(80)), '80 prescribed logical CPUs required')
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
    return rows, cpus


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
    try:
        if proc.poll() is not None:
            return None
        try:
            os.killpg(proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            proc.wait(timeout=5)
        return None
    except BaseException as exc:
        return repr(exc)


def capture(out, name, command, env, limit, overall_deadline):
    started, started_utc = time.perf_counter(), utc()
    deadline = min(started+limit, overall_deadline)
    stdout, stderr = out/(name+'.stdout'), out/(name+'.stderr')
    proc, error, cleanup_error = None, None, None
    with stdout.open('xb') as sout, stderr.open('xb') as serr:
        try:
            require(time.perf_counter() < deadline, 'deadline before launch')
            proc = subprocess.Popen(command, stdout=sout, stderr=serr, env=env,
                                    start_new_session=True)
            save(out/(name+'-launch.json'), {'pid': proc.pid, 'command': command,
                 'utc': started_utc, 'time_limit_seconds': deadline-started})
            proc.wait(timeout=max(0, deadline-time.perf_counter()))
        except BaseException as exc:
            error = repr(exc)
            if proc is not None:
                cleanup_error = stop_group(proc)
    receipt = {'started_utc': started_utc, 'ended_utc': utc(),
               'wall_seconds': time.perf_counter()-started,
               'exit_code': proc.returncode if proc else None,
               'error': error, 'cleanup_error': cleanup_error,
               'stdout': artifact(stdout), 'stderr': artifact(stderr)}
    save(out/(name+'-receipt.json'), receipt)
    return receipt


def compare_bytes(first, second):
    offset = 0
    with first.open('rb') as a, second.open('rb') as b:
        while True:
            left, right = a.read(1024*1024), b.read(1024*1024)
            if left != right:
                n = next((i for i, pair in enumerate(zip(left, right)) if pair[0] != pair[1]),
                         min(len(left), len(right)))
                return {'equal': False, 'first_differing_byte': offset+n}
            if not left:
                return {'equal': True, 'compared_bytes': offset}
            offset += len(left)


def component_rows(state):
    raw = (state/'components.bin').read_bytes()
    require(len(raw) == 276480, 'component byte count')
    rows = list(struct.iter_unpack('<12d', raw))
    require(len(rows) == 2880 and all(all(math.isfinite(v) and v >= 0 for v in row)
            and row[10] <= row[11] for row in rows), 'finite nonnegative component domain')
    return rows


def error_summary(fine, coarse):
    """Exact decision on dyadic upper bounds; ratios are descriptive only."""
    groups, total_failed = [], 0
    for window in range(4):
        for case in range(6):
            start = (window*6+case)*120
            f, c = fine[start:start+120], coarse[start:start+120]
            failed = [j for j in range(120) if Fraction(c[j][4]) >
                      ERROR_GROWTH_TARGET*Fraction(f[j][4])]
            total_failed += len(failed)
            fields = {}
            for k, name in enumerate(FIELDS):
                ratios = [b[k]/a[k] for a, b in zip(f, c) if a[k] > 0]
                finite_ratios = [r for r in ratios if math.isfinite(r)]
                fields[name] = {'fine_min': min(a[k] for a in f),
                                'fine_max': max(a[k] for a in f),
                                'coarse_min': min(a[k] for a in c),
                                'coarse_max': max(a[k] for a in c),
                                'ratio_min': min(finite_ratios) if finite_ratios else None,
                                'ratio_max': max(finite_ratios) if finite_ratios else None,
                                'ratio_float_overflow': len(ratios)-len(finite_ratios),
                                'zero_fine_positive_coarse': sum(a[k] == 0 and b[k] > 0
                                                               for a, b in zip(f, c))}
            groups.append({'window': window, 'case': case,
                           'error_growth_screen_pass': not failed,
                           'failed_thermal_columns': failed, 'components': fields})
    return {'scope': 'ratio_of_local_certificate_upper_bounds_not_actual_errors',
            'threshold': ERROR_GROWTH_TARGET, 'passed': total_failed == 0,
            'failed_columns': total_failed, 'required_columns': 2880, 'groups': groups}


def check_capture(receipt, name):
    require(receipt['error'] is None and receipt['cleanup_error'] is None and
            receipt['exit_code'] == 0 and receipt['stderr']['bytes'] == 0,
            'child failed: '+name+' '+str(receipt['error']))


def window_selection(steps):
    result = []
    for window in range(4):
        for case in range(6):
            labels = ((4, 3), (4, 4), (1, 1))[case % 3]
            occupied = [seg for seg in range(80) if any((label+seg//16) % 5 == 0 for label in labels)]
            count = len(occupied)
            ordinal = (0, (count-1)//3, 2*(count-1)//3, count-1)[window]
            segment = occupied[ordinal]
            q = (0, 128, 128, 254)[window]*(steps//256)
            result.append({'window': window, 'case': case, 'labels': list(labels),
                           'occupied_segment_ordinal': ordinal, 'absolute_segment': segment,
                           'start_subcell': q, 'first_occupied_cell': ordinal*steps+q,
                           'cells': steps//128,
                           'start_original_segment_units': [segment*steps+q, steps],
                           'duration_original_segment_units': [1, 128],
                           'available_full_trajectory_cells': count*steps})
    return result


def validate(record, state, steps, cpus):
    require(finite(record) and record['status'] == 'COMPLETED', 'finite completed output')
    fixed = {'scope': 'LOCAL_WINDOW_GRID_COMPARISON_ONLY',
             'reset_state_in_moving_frame': True, 'full_analytic_linear_history_retained': True,
             'full_trajectory_certificate': False, 'final_coherences_computed': False,
             'cutoff': 8, 'guard': 10, 'steps_per_segment': steps, 'windows': 4,
             'local_cells_per_task': steps//128, 'tasks': 360,
             'total_certified_cells': 360*(steps//128), 'cases': 6, 'thermal_columns': 120,
             'thermal_cutoff': 3, 'simd_lanes': 8, 'threads': 80, 'dimension': 6435,
             'guard_dimension': 19448, 'migrations': 0, 'endpoint_bytes': 296524800,
             'component_bytes': 276480, 'mpfr_version': '4.2.2'}
    require(all(record[k] == v for k, v in fixed.items()), 'fixed configuration')
    require(record['component_fields'] == list(FIELDS), 'component order')
    require(record['window_selection'] == window_selection(steps), 'window selection')
    require(all(record[k] > 0 for k in ('preparation_seconds', 'kernel_seconds',
                'model_preparation_seconds', 'end_to_end_seconds')), 'positive timings')
    require(record['end_to_end_seconds'] >= record['preparation_seconds']+
            record['kernel_seconds'], 'timing decomposition')
    fixture = record['fixtures']
    require(all(fixture[k] is True for k in ('directed_arithmetic',
            'zero_displacement_enclosure', 'adjoint_enclosure',
            'ball_interval_fixture_enclosure')), 'runtime enclosure fixtures')
    require(0 <= fixture['ball_reference_radius_ratio'] <= 1 and
            all(0 <= fixture[k] <= 1e-11 for k in
                ('dense_displacement_error', 'collective_displacement_error')),
            'runtime comparison fixtures')
    mapping = record['thread_map']
    require(len(mapping) == 80 and {r['cpu'] for r in mapping} == set(cpus) and
            {r['thread'] for r in mapping} == set(range(80)) and
            {r['place'] for r in mapping} == set(range(80)), 'thread map coverage')
    require(all(r['cpu'] == cpus[r['place']] for r in mapping), 'CPU/place association')
    component_rows(state)
    basis = load(state/'basis.json')
    require((basis['scope'], basis['cutoff'], basis['guard'], basis['thermal_cutoff']) ==
            ('LOCAL_WINDOW_GRID_COMPARISON_ONLY', 8, 10, 3), 'basis metadata')
    occupations = basis['occupations']
    require(len(occupations) == 6435 and len({tuple(n) for n in occupations}) == 6435,
            'basis inventory')
    require(all(len(n) == 7 and all(type(x) is int and x >= 0 for x in n)
                and sum(n) <= 8 for n in occupations), 'basis carrier')
    require([sum(n) for n in occupations] == sorted(sum(n) for n in occupations), 'basis grading')
    require(sum(sum(n) <= 3 for n in occupations) == 120, 'thermal basis count')
    require(len(record['thermal_weights']) == 120, 'thermal weight inventory')
    for n, (lo, hi) in zip(occupations[:120], record['thermal_weights']):
        exact_weight = Fraction(20, 21)**7*Fraction(1, 21)**sum(n)
        require(0 <= Fraction(lo) <= exact_weight <= Fraction(hi), 'unnormalized thermal weight')
    metadata = load(state/'metadata.json')
    metadata_keys = {'scope', 'reset_state_in_moving_frame', 'full_analytic_linear_history_retained',
                     'full_trajectory_certificate', 'final_coherences_computed', 'cutoff', 'guard',
                     'steps_per_segment', 'windows', 'cases', 'thermal_columns', 'thermal_cutoff',
                     'dimension', 'guard_dimension', 'local_cells_per_task', 'endpoint_bytes',
                     'component_bytes', 'component_fields', 'window_selection', 'thermal_weights'}
    require(set(metadata) == metadata_keys and all(metadata[k] == record[k] for k in metadata),
            'immutable metadata/stdout agreement')
    layout = ('GRID_LOCAL_WINDOWS_V1\nsteps='+str(steps)+
              '\nwindows=4\ncases=6\ncolumns=120\ndimension=6435\ncomponents=12\n'
              'endpoints=window,case,column,basis,re_im\ncomponents=window,case,column,field\n'
              'encoding=little_endian_IEEE_binary64\n')
    require((state/'layout.txt').read_bytes() == layout.encode('ascii'), 'binary layout')
    endpoint = state/'endpoints.bin'
    require(endpoint.stat().st_size == 296524800, 'endpoint byte count')
    with endpoint.open('rb') as stream:
        while block := stream.read(1024*1024):
            require(all(math.isfinite(v[0]) for v in struct.iter_unpack('<d', block)),
                    'finite endpoint bytes')
    progress = [json.loads(row) for row in (state/'progress.jsonl').read_text('ascii').splitlines()]
    require(finite(progress) and len(progress) == 360 and
            {r['completed'] for r in progress} == set(range(1, 361)) and
            {(r['window'], r['case'], r['batch']) for r in progress} ==
            {(w, c, b) for w in range(4) for c in range(6) for b in range(15)} and
            all(r['cells'] == steps//128 and 0 <= r['elapsed_seconds'] <= record['kernel_seconds']
                for r in progress), 'completed local-window task inventory')
    lifecycle = [json.loads(row) for row in (state/'lifecycle.jsonl').read_text('ascii').splitlines()]
    require([r['phase'] for r in lifecycle] == ['model_preparation_started',
            'model_preparation_completed', 'fixtures_completed', 'local_window_scan_completed'],
            'lifecycle inventory')
    times = [r['elapsed_seconds'] for r in lifecycle]
    require(finite(times) and times[0] == 0 and times == sorted(times), 'lifecycle times')
    return {name: artifact(state/name) for name in ('basis.json', 'metadata.json', 'layout.txt',
            'endpoints.bin', 'components.bin', 'progress.jsonl', 'lifecycle.jsonl')}


def validate_comparison(result, fine, coarse):
    require(finite(result), 'finite comparison output')
    fixed = {'status': 'COMPLETED', 'scope': 'LOCAL_WINDOW_ENDPOINT_CONSISTENCY_ONLY',
             'full_trajectory_certificate': False, 'propagation_executed': False,
             'normalization_applied': False, 'phase_fit_applied': False,
             'fine_steps': 512, 'coarse_steps': 256, 'windows': 4, 'cases': 6,
             'thermal_columns': 120, 'dimension': 6435, 'records': 2880}
    require(all(result[k] == v for k, v in fixed.items()), 'comparison scope/inventory')
    require(len(result['decisions']) == 2880 and result['comparison_seconds'] > 0,
            'comparison decisions/time')
    counts = {name: 0 for name in ('COMPATIBLE', 'INCONSISTENT', 'UNRESOLVED')}
    for index, row in enumerate(result['decisions']):
        require((row['window'], row['case'], row['column']) ==
                (index//720, (index//120) % 6, index % 120), 'comparison row identity')
        require(struct.pack('<d', row['eps_fine']) == struct.pack('<d', fine[index][4]) and
                struct.pack('<d', row['eps_coarse']) == struct.pack('<d', coarse[index][4]),
                'comparison/raw component agreement')
        lo, hi, radius = row['d_lo'], row['d_hi'], row['R']
        require(0 <= lo <= hi and Fraction(radius) >=
                Fraction(fine[index][4])+Fraction(coarse[index][4]), 'directed comparison domain')
        status = 'COMPATIBLE' if hi <= radius else 'INCONSISTENT' if lo > radius else 'UNRESOLVED'
        require(row['status'] == status, 'three-way decision')
        counts[status] += 1
    require(all(result[k] == v for k, v in counts.items()), 'comparison count agreement')
    require(result['max_d_hi'] == max(r['d_hi'] for r in result['decisions']) and
            result['max_R'] == max(r['R'] for r in result['decisions']), 'comparison maxima')
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--comparator', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source, out = Path(__file__).resolve().parent, args.output.resolve()
    binaries = {'benchmark': args.binary.resolve(), 'comparator': args.comparator.resolve()}
    out.mkdir(parents=True, exist_ok=False)
    signal.signal(signal.SIGTERM, interrupted)
    signal.signal(signal.SIGINT, interrupted)
    started, started_utc = time.perf_counter(), utc()
    deadline = started+TOTAL_SECONDS
    initial, input_pin, failure = None, None, None
    records, repeats, comparisons, states, inventories = [], [], [], {}, {}
    first_by_grid, medians, speedup = {}, {}, None
    status = 'INCOMPLETE'
    try:
        initial = pins(source, binaries)
        save(out/'source-pins.json', initial)
        from prepare_input import serialize
        rows, cpus = topology()
        env, overrides = child_env(cpus)
        save(out/'metadata.json', {'started_utc': started_utc, 'python': platform.python_version(),
             'topology': rows, 'environment': overrides, 'order': ORDER,
             'child_seconds': CHILD_SECONDS, 'comparison_seconds': COMPARE_SECONDS,
             'total_seconds': TOTAL_SECONDS, 'error_growth_screen': ERROR_GROWTH_TARGET,
             'loadavg': os.getloadavg()})
        save(out/'input-pin.json', serialize(source/'input.json', out/'exact_input.txt'))
        input_pin = artifact(out/'exact_input.txt')
        for index, steps in enumerate(ORDER, 1):
            require(pins(source, binaries) == initial and
                    artifact(out/'exact_input.txt') == input_pin, 'pre-child custody')
            name = f'{index:02d}-N{steps}'
            state = out/(name+'-state')
            command = [str(binaries['benchmark']), '--input', str(out/'exact_input.txt'),
                       '--output', str(state), '--steps', str(steps)]
            receipt = capture(out, name, command, env, CHILD_SECONDS, deadline)
            require(pins(source, binaries) == initial and
                    artifact(out/'exact_input.txt') == input_pin, 'post-child custody')
            check_capture(receipt, name)
            record = load(out/(name+'.stdout'))
            inventory = validate(record, state, steps, cpus)
            save(out/(name+'-validated.json'), {'status': 'VALID_LOCAL_WINDOWS',
                 'artifacts': inventory, 'custody_unchanged': True})
            records.append({'ordinal': index, 'steps': steps,
                            'preparation_seconds': record['preparation_seconds'],
                            'kernel_seconds': record['kernel_seconds'],
                            'end_to_end_seconds': record['end_to_end_seconds'],
                            'child_wall_seconds': receipt['wall_seconds']})
            states[index], inventories[index] = state, inventory
            if steps in first_by_grid:
                reference = states[first_by_grid[steps]]
                comparison = {name: compare_bytes(reference/name, state/name)
                              for name in ('basis.json', 'metadata.json', 'layout.txt',
                                           'endpoints.bin', 'components.bin')}
                comparison.update(ordinal=index, steps=steps, reference=first_by_grid[steps])
                repeats.append(comparison)
                save(out/(name+'-repeat.json'), comparison)
                if not all(comparison[k]['equal'] for k in
                           ('basis.json', 'metadata.json', 'layout.txt', 'endpoints.bin', 'components.bin')):
                    status = 'REPEATABILITY_FAILED'
                    raise RuntimeError('same-grid byte mismatch: '+name)
            else:
                first_by_grid[steps] = index
            if index in PAIRS:
                fine_id, coarse_id = PAIRS[index]
                fine, coarse = states[fine_id], states[coarse_id]
                require(compare_bytes(fine/'basis.json', coarse/'basis.json')['equal'],
                        'common fine/coarse basis')
                pair_name = f'compare-{fine_id:02d}-{coarse_id:02d}'
                result_path = out/(pair_name+'.json')
                for idx in (fine_id, coarse_id):
                    require(all(artifact(states[idx]/k) == v for k, v in inventories[idx].items()),
                            'pre-comparison artifact custody')
                command = [str(binaries['comparator']), '--fine', str(fine), '--coarse', str(coarse),
                           '--output', str(result_path)]
                require(pins(source, binaries) == initial and
                        artifact(out/'exact_input.txt') == input_pin, 'pre-comparison source custody')
                receipt = capture(out, pair_name, command, env, COMPARE_SECONDS, deadline)
                require(pins(source, binaries) == initial and
                        artifact(out/'exact_input.txt') == input_pin, 'post-comparison source custody')
                for idx in (fine_id, coarse_id):
                    require(all(artifact(states[idx]/k) == v for k, v in inventories[idx].items()),
                            'post-comparison artifact custody')
                check_capture(receipt, pair_name)
                fine_rows, coarse_rows = component_rows(fine), component_rows(coarse)
                comparison = load(result_path)
                counts = validate_comparison(comparison, fine_rows, coarse_rows)
                comparator_stdout = load(out/(pair_name+'.stdout'))
                require(comparator_stdout == dict(status='COMPLETED', records=2880, **counts),
                        'comparator stdout/JSON agreement')
                screen = error_summary(fine_rows, coarse_rows)
                save(out/(pair_name+'-screen.json'), screen)
                summary = {'fine_ordinal': fine_id, 'coarse_ordinal': coarse_id,
                           'compatibility_counts': counts, 'error_growth_screen_pass': screen['passed'],
                           'error_growth_failed_columns': screen['failed_columns'],
                           'comparison_artifact': artifact(result_path), 'wall_seconds': receipt['wall_seconds']}
                comparisons.append(summary)
                if counts['INCONSISTENT']:
                    status = 'INCONSISTENT_CERTIFICATES'
                    raise RuntimeError('directed endpoint/certificate contradiction')
        require(time.perf_counter() <= deadline, 'total budget exhausted')
        for steps in (512, 256):
            medians[str(steps)] = {field: statistics.median(r[field] for r in records if r['steps'] == steps)
                                  for field in ('preparation_seconds', 'kernel_seconds',
                                                'end_to_end_seconds', 'child_wall_seconds')}
        speedup = {field: medians['512'][field]/medians['256'][field] for field in medians['512']}
        status = ('COMPLETE_LOCAL_COMPARISON_UNRESOLVED' if any(
                  c['compatibility_counts']['UNRESOLVED'] for c in comparisons) else
                  'COMPLETE_LOCAL_COMPARISON_COMPATIBLE')
    except BaseException as exc:
        failure = repr(exc)
    finally:
        if initial is not None:
            try:
                require(pins(source, binaries) == initial, 'final source custody')
                if input_pin is not None:
                    require(artifact(out/'exact_input.txt') == input_pin, 'final input custody')
            except BaseException as exc:
                status, failure = 'CUSTODY_FAILURE', repr(exc)
        result = {'status': status, 'scope': 'LOCAL_WINDOW_GRID_COMPARISON_ONLY',
                  'full_trajectory_certificate': False, 'long_run_authorized_or_started': False,
                  'started_utc': started_utc, 'ended_utc': utc(),
                  'wall_seconds': time.perf_counter()-started, 'failure': failure,
                  'completed_children': len(records), 'required_children': 6, 'order': ORDER,
                  'records': records, 'repeat_comparisons': repeats, 'grid_comparisons': comparisons,
                  'median_seconds': medians, 'median_speedup': speedup,
                  'error_growth_screen_pass': (all(c['error_growth_screen_pass'] for c in comparisons)
                                               if len(comparisons) == 3 else None)}
        save(out/'summary.json', result)
        print(json.dumps({'status': status, 'completed_children': len(records),
                          'failure': failure}, sort_keys=True), flush=True)
    return 0 if status.startswith('COMPLETE_LOCAL_COMPARISON_') else 2


if __name__ == '__main__':
    raise SystemExit(main())
