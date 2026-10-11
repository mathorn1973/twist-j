#!/usr/bin/env python3
"""Normwise-ball error-account ladder. Apache-2.0; NON-CANONICAL.

No candidate model is executed on import. Runtime output is retained even
when a child fails, a precision target is missed or the budget expires.
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
import subprocess
import sys
import time

SOURCES = {'README.md', 'PREREG.md', 'DERIVATION.md', 'EXACT-DESIGN.md',
           'input.json', 'prepare_input.py', 'validated_model.hpp',
           'validated_model.cpp', 'kernel.cpp', 'verify.py', 'numerical_run.py'}
CONFIGS = ((8, 10, 512), (10, 12, 512), (10, 12, 1024), (12, 14, 1024))
BUDGET_SECONDS = 14400
PRECISION_TARGET = 1e-3
DISCREPANCY_TARGET = 1e-3

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

def pins(source, binary):
    found = {}
    for line in (source/'SOURCE_SHA256SUMS').read_text('ascii').splitlines():
        expected, name = line.split('  ')
        require(name in SOURCES and name not in found, 'manifest inventory')
        require(digest(source/name) == expected, 'changed source: '+name)
        found[name] = expected
    require(set(found) == SOURCES, 'incomplete source manifest')
    found['SOURCE_SHA256SUMS'] = digest(source/'SOURCE_SHA256SUMS')
    found['binary'] = digest(binary)
    return found

def topology():
    require(sys.platform == 'linux', 'Linux required')
    allowed = sorted(os.sched_getaffinity(0))
    require(allowed == list(range(80)), '80 prescribed logical CPUs required')
    rows = []
    for cpu in allowed:
        root = Path('/sys/devices/system/cpu')/('cpu'+str(cpu))/'topology'
        rows.append({'cpu': cpu, 'package': int((root/'physical_package_id').read_text()),
                     'core': int((root/'core_id').read_text())})
    cores = {(r['package'], r['core']) for r in rows}
    require(len(cores) == 40 and len({r['package'] for r in rows}) == 2,
            'two packages and forty physical cores required')
    require(all(sum((r['package'], r['core']) == core for r in rows) == 2
                for core in cores), 'both SMT siblings required')
    return rows, allowed

def child_env(cpus):
    overrides = {'OMP_NUM_THREADS': '80', 'OMP_DYNAMIC': 'FALSE',
                 'OMP_PROC_BIND': 'TRUE', 'OMP_PLACES': ','.join('{'+str(c)+'}' for c in cpus),
                 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
                 'LC_ALL': 'C', 'LANG': 'C', 'PYTHONHASHSEED': '0'}
    env = os.environ.copy()
    env.update(overrides)
    return env, overrides

def interrupted(signum, frame):
    raise RuntimeError('Interrupted by signal '+str(signum))

def stop_group(proc):
    if proc.poll() is not None:
        return
    os.killpg(proc.pid, signal.SIGTERM)
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.wait()

def validate_record(record, state_dir, config, cpus):
    import numpy as np
    L, G, N = config
    require(record['status'] == 'COMPLETED' and finite(record), 'finite completed output')
    require((record['cutoff'], record['guard'], record['steps_per_segment']) == config,
            'configuration mismatch')
    require(record['scope'] == 'normwise_ball_full_space_defect', 'certificate scope')
    require(record['dimension'] == math.comb(L+7, 7) and
            record['guard_dimension'] == math.comb(G+7, 7), 'dimension mismatch')
    require(record['thermal_columns'] == 120 and record['cases'] == 6 and
            record['threads'] == 80, 'carrier/thread inventory')
    require(record['mpfr_version'] == '4.2.2', 'frozen MPFR version')
    fixtures = record['fixtures']
    require(all(fixtures[k] is True for k in ('directed_arithmetic',
            'zero_displacement_enclosure', 'adjoint_enclosure',
            'ball_interval_fixture_enclosure')), 'runtime enclosure fixtures')
    require(0 <= fixtures['ball_reference_radius_ratio'] <= 1 and
            all(0 <= fixtures[k] <= 1e-11 for k in
                ('dense_displacement_error', 'collective_displacement_error')),
            'runtime comparison fixtures')
    mapping = record['thread_map']
    require(len(mapping) == 80 and {r['cpu'] for r in mapping} == set(cpus) and
            {r['thread'] for r in mapping} == set(range(80)) and
            {r['place'] for r in mapping} == set(range(80)), 'thread map coverage')
    require(all(r['cpu'] == cpus[r['place']] for r in mapping), 'CPU/place association')
    require(len(record['branches']) == 6 and len(record['pair_coherences']) == 6,
            'complete branch/pair inventory')
    require([p['cases'] for p in record['pair_coherences']] ==
            [[0,1],[0,2],[1,2],[3,4],[3,5],[4,5]], 'pair ordering')
    for case, branch in enumerate(record['branches']):
        require(branch['case'] == case and len(branch['columns']) == 120, 'column inventory')
        require(branch['node_split_scope'] ==
                'diagnostic_quadrature_only_continuum_allowance_is_combined',
                'node diagnostics scope')
        require(all(branch[k] >= 0 for k in ('sampled_time_node_L2',
                'sampled_projection_node_L2', 'sampled_arithmetic_node_L2')),
                'nonnegative branch node diagnostics')
        for n, column in enumerate(branch['columns']):
            require(column['thermal_index'] == n, 'thermal column order')
            require(all(column[k] >= 0 for k in ('guard','tail','continuum','jumps','total')),
                    'nonnegative error components')
            require(all(column[k] >= 0 for k in ('sampled_time_node_L2',
                    'sampled_projection_node_L2', 'sampled_arithmetic_node_L2')),
                    'nonnegative node diagnostics')
    for pair in record['pair_coherences']:
        require(pair['total_radius'] >= pair['thermal_radius'] >= 0 and
                pair['numerical_radius'] >= 0 and pair['arithmetic_radius'] >= 0,
                'radius inventory')
        lo, hi = pair['certified_trace_distance_interval']
        require(0 <= lo <= hi <= 1, 'trace-distance interval')
    basis = load(state_dir/'basis.json')
    require((basis['cutoff'], basis['guard'], basis['thermal_cutoff']) == (L, G, 3),
            'basis metadata')
    occupations = basis['occupations']
    require(len(occupations) == record['dimension'] and
            len({tuple(n) for n in occupations}) == len(occupations), 'basis inventory')
    require(all(len(n) == 7 and all(type(x) is int and x >= 0 for x in n)
                and sum(n) <= L for n in occupations), 'basis carrier')
    require([sum(n) for n in occupations] == sorted(sum(n) for n in occupations),
            'basis grading')
    require(sum(sum(n) <= 3 for n in occupations) == 120, 'thermal basis count')
    endpoint = state_dir/'endpoints.bin'
    require(endpoint.stat().st_size == 6*120*record['dimension']*16, 'endpoint byte count')
    values = np.memmap(endpoint, mode='r', dtype='<c16', shape=(6,120,record['dimension']))
    require(bool(np.isfinite(values).all()), 'finite endpoint data')
    del values
    lifecycle = [json.loads(row) for row in
                 (state_dir/'lifecycle.jsonl').read_text('ascii').splitlines()]
    require([row['phase'] for row in lifecycle] ==
            ['model_preparation_started', 'model_preparation_completed', 'fixtures_completed'],
            'lifecycle inventory')
    times = [row['elapsed_seconds'] for row in lifecycle]
    require(finite(times) and times[0] == 0 and times == sorted(times),
            'lifecycle timing')
    return {name: artifact(state_dir/name) for name in
            ('basis.json','endpoints.bin','progress.jsonl','lifecycle.jsonl')}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    binary, out = args.binary.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    signal.signal(signal.SIGTERM, interrupted)
    signal.signal(signal.SIGINT, interrupted)
    started, started_utc = time.perf_counter(), utc()
    initial = pins(source, binary)
    from prepare_input import serialize
    save(out/'source-pins.json', initial)
    rows, cpus = topology()
    env, overrides = child_env(cpus)
    import numpy as np
    save(out/'metadata.json', {'started_utc': started_utc, 'python': platform.python_version(),
         'numpy': np.__version__, 'topology': rows, 'environment': overrides,
         'configurations': CONFIGS, 'budget_seconds': BUDGET_SECONDS})
    input_receipt = serialize(source/'input.json', out/'exact_input.txt')
    save(out/'input-pin.json', input_receipt)
    input_hash = artifact(out/'exact_input.txt')
    results, failure, status = [], None, 'LADDER_EXHAUSTED'
    try:
        for config in CONFIGS:
            require(pins(source,binary) == initial, 'source/binary mutation before child')
            require(artifact(out/'exact_input.txt') == input_hash, 'input mutation before child')
            remaining = BUDGET_SECONDS-(time.perf_counter()-started)
            if remaining <= 0:
                status = 'BUDGET_EXHAUSTED'
                break
            L, G, N = config
            directory = out/('L%d-G%d-N%d' % config)
            directory.mkdir(exist_ok=False)
            command = [str(binary),'--input',str(out/'exact_input.txt'),
                       '--output',str(directory/'states'),'--cutoff',str(L),
                       '--guard',str(G),'--steps',str(N)]
            record = {'config': config, 'command': command, 'started_utc': utc(),
                      'limit_seconds': remaining, 'status': 'STARTED'}
            save(directory/'launch.json', record)
            t0, proc = time.perf_counter(), None
            try:
                with (directory/'stdout.txt').open('xb') as stdout, (directory/'stderr.txt').open('xb') as stderr:
                    proc = subprocess.Popen(command, cwd=source, env=env, stdout=stdout,
                                            stderr=stderr, start_new_session=True)
                    try:
                        proc.wait(timeout=remaining)
                    except BaseException:
                        stop_group(proc)
                        raise
                record.update(exit_code=proc.returncode, status='RETURNED')
            except subprocess.TimeoutExpired:
                record.update(exit_code=proc.returncode, status='TIMEOUT')
                status = 'BUDGET_EXHAUSTED'
            except BaseException as exc:
                record.update(exit_code=proc.returncode if proc else None,
                              status='INTERRUPTED_OR_FAILED', error=repr(exc))
                raise
            finally:
                record.update(ended_utc=utc(), wall_seconds=time.perf_counter()-t0)
                for name in ('stdout.txt','stderr.txt'):
                    if (directory/name).exists(): record[name] = artifact(directory/name)
                custody_error = None
                try:
                    require(pins(source,binary) == initial, 'source/binary mutation after child')
                    require(artifact(out/'exact_input.txt') == input_hash, 'input mutation after child')
                    record['post_child_custody'] = 'PASS'
                except Exception as exc:
                    custody_error = str(exc)
                    record['post_child_custody'] = custody_error
                save(directory/'receipt.json', record)
                if custody_error:
                    raise RuntimeError(custody_error)
            if status == 'BUDGET_EXHAUSTED':
                break
            require(proc.returncode == 0, 'kernel returned nonzero')
            require((directory/'stderr.txt').stat().st_size == 0, 'kernel stderr not empty')
            result = load(directory/'stdout.txt')
            receipts = validate_record(result, directory/'states', config, cpus)
            require(pins(source,binary) == initial, 'source/binary mutation after child')
            require(artifact(out/'exact_input.txt') == input_hash, 'input mutation after child')
            save(directory/'artifacts.json', receipts)
            precision = all(Fraction(p['total_radius'])*1000 <= 1 for p in result['pair_coherences'])
            angle_decisions = [any(Fraction(p['certified_trace_distance_interval'][0])*1000 > 1
                               for p in result['pair_coherences'][3*s:3*s+3]) for s in range(2)]
            results.append({'configuration':config, 'result':result, 'artifacts':receipts,
                            'precision_goal_met':precision,
                            'nonlinear_discrepancy_certified_by_angle':angle_decisions})
            save(directory/'decision.json', {'precision_goal_met':precision,
                 'nonlinear_discrepancy_certified_by_angle':angle_decisions})
            if precision:
                status = 'PRECISION_GOAL_MET'
                break
    except Exception as exc:
        status, failure = 'NOT_CERTIFIED', str(exc)
    final = {'status':status, 'failure':failure, 'started_utc':started_utc, 'ended_utc':utc(),
             'wall_seconds':time.perf_counter()-started, 'budget_seconds':BUDGET_SECONDS,
             'precision_target':PRECISION_TARGET, 'discrepancy_target':DISCREPANCY_TARGET,
             'threshold_comparison':'exact Fraction(binary64 bound) versus 1/1000',
             'configurations_prescribed':CONFIGS, 'completed':len(results), 'runs':results,
             'source_pins':initial, 'input':input_receipt,
             'certificate_scope':'conditional seven-mode exact-decimal coherent model and selected panel',
             'online_certificate':True, 'full_intermediate_polynomials_retained':False,
             'physical_experiment':False, 'canonical_promotion':False}
    save(out/'result.json', final)
    print(json.dumps({'status':status,'completed':len(results),'wall_seconds':final['wall_seconds'],
                      'failure':failure}, sort_keys=True, allow_nan=False))
    return 0 if status in ('PRECISION_GOAL_MET','LADDER_EXHAUSTED','BUDGET_EXHAUSTED') else 2

if __name__ == '__main__':
    sys.exit(main())
