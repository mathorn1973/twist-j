#!/usr/bin/env python3
"""Fixed short prefix comparison; Apache-2.0, NON-CANONICAL.

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

SOURCES = {'README.md', 'PREREG.md', 'EXACT-DESIGN.md', 'OPTIMIZATION.md',
           'input.json', 'prepare_input.py', 'validated_model.hpp',
           'validated_model.cpp', 'baseline_kernel.cpp', 'kernel.cpp',
           'benchmark.cpp', 'benchmark_run.py', 'verify.py'}
ORDER = ('baseline', 'optimized', 'optimized', 'baseline', 'baseline', 'optimized')
FIELDS = ('guard', 'tail', 'continuum', 'jumps', 'total',
          'sampled_time_node_L2', 'sampled_projection_node_L2',
          'sampled_arithmetic_node_L2', 'maximum_node_bound', 'maximum_norm_error',
          'endpoint_norm_squared_lo', 'endpoint_norm_squared_hi')
CHILD_SECONDS = 300
TOTAL_SECONDS = 1800
SPEEDUP_TARGET = 2.0


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


def validate(record, state, variant, cpus):
    require(finite(record) and record['status'] == 'COMPLETED', 'finite completed output')
    require(record['scope'] == 'PREFIX_PERFORMANCE_ONLY' and record['variant'] == variant,
            'scope or variant')
    require(record['full_trajectory_certificate'] is False and
            record['final_coherences_computed'] is False, 'partial prefix scope')
    fixed = {'cutoff': 8, 'guard': 10, 'steps_per_segment': 512,
             'prefix_occupied_cells_per_task': 4, 'tasks': 90, 'cases': 6,
             'thermal_columns': 120, 'thermal_cutoff': 3, 'simd_lanes': 8,
             'threads': 80, 'dimension': 6435, 'guard_dimension': 19448, 'migrations': 0,
             'endpoint_bytes': 74131200, 'component_bytes': 69120, 'mpfr_version': '4.2.2'}
    require(all(record[k] == v for k, v in fixed.items()), 'fixed configuration')
    require(record['component_fields'] == list(FIELDS), 'component order')
    require(all(record[k] > 0 for k in ('preparation_seconds', 'kernel_seconds',
                'model_preparation_seconds', 'end_to_end_seconds')), 'positive timings')
    require(record['end_to_end_seconds'] >= record['preparation_seconds'] +
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
    require(len(record['branches']) == 6, 'branch inventory')
    raw_components = bytearray()
    for case, branch in enumerate(record['branches']):
        require(branch['case'] == case and len(branch['columns']) == 120, 'column inventory')
        require(branch['labels'] == [[4, 3], [4, 4], [1, 1]][case % 3], 'branch labels')
        require(branch['available_full_trajectory_cells'] ==
                (16384 if case % 3 == 0 else 8192), 'full trajectory cell inventory')
        for column, values in enumerate(branch['columns']):
            require(values['thermal_index'] == column, 'column ordering')
            require(all(values[k] >= 0 for k in FIELDS), 'nonnegative partial components')
            require(values['endpoint_norm_squared_lo'] <= values['endpoint_norm_squared_hi'],
                    'endpoint norm enclosure ordering')
            raw_components.extend(struct.pack('<12d', *(values[k] for k in FIELDS)))
    require((state/'components.bin').read_bytes() == raw_components,
            'JSON/raw IEEE component disagreement')
    basis = load(state/'basis.json')
    require((basis['scope'], basis['cutoff'], basis['guard'], basis['thermal_cutoff']) ==
            ('PREFIX_PERFORMANCE_ONLY', 8, 10, 3), 'basis metadata')
    occupations = basis['occupations']
    require(len(occupations) == 6435 and len({tuple(n) for n in occupations}) == 6435,
            'basis inventory')
    require(all(len(n) == 7 and all(type(x) is int and x >= 0 for x in n)
                and sum(n) <= 8 for n in occupations), 'basis carrier')
    require([sum(n) for n in occupations] == sorted(sum(n) for n in occupations),
            'basis grading')
    require(sum(sum(n) <= 3 for n in occupations) == 120, 'thermal basis count')
    endpoint = state/'endpoints.bin'
    require(endpoint.stat().st_size == 74131200 and len(raw_components) == 69120,
            'binary byte counts')
    with endpoint.open('rb') as stream:
        while block := stream.read(1024*1024):
            require(all(math.isfinite(v[0]) for v in struct.iter_unpack('<d', block)),
                    'finite endpoint bytes')
    progress = [json.loads(row) for row in (state/'progress.jsonl').read_text('ascii').splitlines()]
    require(len(progress) == 90 and {r['completed'] for r in progress} == set(range(1, 91))
            and {(r['case'], r['batch']) for r in progress} ==
            {(c, b) for c in range(6) for b in range(15)}
            and all(r['cells'] == 4 and 0 <= r['elapsed_seconds'] <= record['kernel_seconds']
                    for r in progress), 'completed prefix inventory')
    lifecycle = [json.loads(row) for row in (state/'lifecycle.jsonl').read_text('ascii').splitlines()]
    require([r['phase'] for r in lifecycle] == ['model_preparation_started',
            'model_preparation_completed', 'fixtures_completed', 'prefix_scan_completed'],
            'lifecycle inventory')
    times = [r['elapsed_seconds'] for r in lifecycle]
    require(finite(times) and times[0] == 0 and times == sorted(times), 'lifecycle times')
    return {name: artifact(state/name) for name in
            ('basis.json', 'endpoints.bin', 'components.bin', 'progress.jsonl', 'lifecycle.jsonl')}


def compare_bytes(first, second):
    """Compare actual bytes, not just digests; preserve first differing offset."""
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--optimized', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source, out = Path(__file__).resolve().parent, args.output.resolve()
    binaries = {'baseline': args.baseline.resolve(), 'optimized': args.optimized.resolve()}
    out.mkdir(parents=True, exist_ok=False)
    signal.signal(signal.SIGTERM, interrupted)
    signal.signal(signal.SIGINT, interrupted)
    started, started_utc = time.perf_counter(), utc()
    records, comparisons, failure = [], [], None
    status, initial, input_pin = 'INCOMPLETE', None, None
    medians, speedup = {}, None
    try:
        initial = pins(source, binaries)
        save(out/'source-pins.json', initial)
        from prepare_input import serialize
        rows, cpus = topology()
        env, overrides = child_env(cpus)
        save(out/'metadata.json', {'started_utc': started_utc, 'python': platform.python_version(),
             'topology': rows, 'environment': overrides, 'order': ORDER,
             'child_seconds': CHILD_SECONDS, 'total_seconds': TOTAL_SECONDS,
             'speedup_target': SPEEDUP_TARGET, 'loadavg': os.getloadavg()})
        save(out/'input-pin.json', serialize(source/'input.json', out/'exact_input.txt'))
        input_pin = artifact(out/'exact_input.txt')
        for index, variant in enumerate(ORDER, 1):
            require(pins(source, binaries) == initial, 'pre-child source custody')
            require(artifact(out/'exact_input.txt') == input_pin, 'pre-child input custody')
            remaining = TOTAL_SECONDS-(time.perf_counter()-started)
            require(remaining > 0, 'total resource budget exhausted')
            limit = min(CHILD_SECONDS, remaining)
            prefix = f'{index:02d}-{variant}'
            state = out/(prefix+'-state')
            stdout, stderr = out/(prefix+'.stdout'), out/(prefix+'.stderr')
            command = [str(binaries[variant]), '--input', str(out/'exact_input.txt'),
                       '--output', str(state)]
            child_start, child_utc, proc, error = time.perf_counter(), utc(), None, None
            deadline = min(started+TOTAL_SECONDS, child_start+CHILD_SECONDS)
            cleanup_error = None
            with stdout.open('xb') as sout, stderr.open('xb') as serr:
                try:
                    require(time.perf_counter() < deadline, 'deadline before launch')
                    proc = subprocess.Popen(command, stdout=sout, stderr=serr, env=env,
                                            start_new_session=True)
                    save(out/(prefix+'-launch.json'), {'pid': proc.pid, 'command': command,
                         'utc': child_utc, 'time_limit_seconds': limit})
                    proc.wait(timeout=max(0, deadline-time.perf_counter()))
                except BaseException as exc:
                    error = repr(exc)
                    if proc is not None:
                        cleanup_error = stop_group(proc)
            receipt = {'variant': variant, 'ordinal': index, 'started_utc': child_utc,
                       'ended_utc': utc(), 'wall_seconds': time.perf_counter()-child_start,
                       'exit_code': proc.returncode if proc else None, 'error': error,
                       'cleanup_error': cleanup_error,
                       'stdout': artifact(stdout), 'stderr': artifact(stderr)}
            # This receipt is saved even if custody validation subsequently fails.
            save(out/(prefix+'-receipt.json'), receipt)
            require(pins(source, binaries) == initial and artifact(out/'exact_input.txt') == input_pin,
                    'post-child custody')
            require(error is None and receipt['exit_code'] == 0 and stderr.stat().st_size == 0,
                    'child failed: '+prefix+' '+str(error))
            record = load(stdout)
            inventory = validate(record, state, variant, cpus)
            save(out/(prefix+'-validated.json'), {'status': 'VALID_PREFIX', 'artifacts': inventory,
                                                'custody_unchanged': True})
            records.append({'ordinal': index, 'variant': variant,
                            'preparation_seconds': record['preparation_seconds'],
                            'kernel_seconds': record['kernel_seconds'],
                            'end_to_end_seconds': record['end_to_end_seconds'],
                            'child_wall_seconds': receipt['wall_seconds']})
            if index > 1:
                first = out/'01-baseline-state'
                comparison = {name: compare_bytes(first/name, state/name)
                              for name in ('basis.json', 'endpoints.bin', 'components.bin')}
                comparison.update(ordinal=index, variant=variant)
                comparisons.append(comparison)
                save(out/(prefix+'-comparison.json'), comparison)
                if not all(comparison[name]['equal'] for name in
                           ('basis.json', 'endpoints.bin', 'components.bin')):
                    status = 'REGRESSION_FAILED'
                    raise RuntimeError('strict byte comparison failed: '+prefix)
        require(time.perf_counter()-started <= TOTAL_SECONDS, 'total resource budget exhausted')
        for variant in ('baseline', 'optimized'):
            medians[variant] = {field: statistics.median(r[field] for r in records if r['variant'] == variant)
                               for field in ('preparation_seconds', 'kernel_seconds',
                                             'end_to_end_seconds', 'child_wall_seconds')}
        speedup = {field: medians['baseline'][field]/medians['optimized'][field]
                   for field in medians['baseline']}
        bitwise = all(c[name]['equal'] for c in comparisons
                      for name in ('basis.json', 'endpoints.bin', 'components.bin'))
        target_met = (Fraction(medians['baseline']['kernel_seconds']) >=
                      2*Fraction(medians['optimized']['kernel_seconds']))
        status = ('REGRESSION_FAILED' if not bitwise else
                  'PREFIX_SPEEDUP_TARGET_MET' if target_met else
                  'PREFIX_SPEEDUP_TARGET_MISSED')
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
        result = {'status': status, 'scope': 'PREFIX_PERFORMANCE_ONLY',
                  'full_trajectory_certificate': False, 'long_run_authorized_or_started': False,
                  'started_utc': started_utc, 'ended_utc': utc(),
                  'wall_seconds': time.perf_counter()-started, 'failure': failure,
                  'completed_children': len(records), 'required_children': 6,
                  'order': ORDER, 'records': records, 'comparisons': comparisons,
                  'median_seconds': medians, 'median_speedup': speedup,
                  'propagation_window_speedup_target': SPEEDUP_TARGET}
        save(out/'summary.json', result)
        print(json.dumps({'status': status, 'completed_children': len(records),
                          'failure': failure}, sort_keys=True), flush=True)
    return 0 if status in ('PREFIX_SPEEDUP_TARGET_MET', 'PREFIX_SPEEDUP_TARGET_MISSED') else 2


if __name__ == '__main__':
    raise SystemExit(main())
