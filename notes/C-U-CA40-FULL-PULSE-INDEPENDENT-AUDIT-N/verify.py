#!/usr/bin/env python3
"""Synthetic fixtures only. No campaign input, solver, network or subprocess.

Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
PUBLIC NON-CANONICAL. First execution requires the immutable public audit pin.
"""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import sys


def main():
    path = Path(__file__).with_name('audit_saved.py')
    spec = importlib.util.spec_from_file_location('independent_saved_audit', path)
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    positive, negative = [], []

    def expect(name, condition):
        if not condition:
            raise AssertionError(name)
        positive.append(name)

    def reject(name, call):
        try:
            call()
        except (audit.AuditError, ValueError):
            negative.append(name)
        else:
            raise AssertionError('negative fixture escaped: '+name)

    class MemoryPath:
        """Small synthetic saved members; never accesses campaign files."""
        def __init__(self, members, name=''):
            self.members, self.name = members, name
        def __truediv__(self, name):
            return MemoryPath(self.members, name)
        def exists(self):
            return self.name in self.members
        def read_bytes(self):
            return self.members[self.name]
        def read_text(self, encoding):
            return self.read_bytes().decode(encoding)

    # A dyadic endpoint can contain a squared subnormal too small for binary64.
    vector = struct.pack('<4d', 3.0, 4.0, 0.0, -0.0)
    expect('complex_norm_3_4_exact', audit.exact_squared_norm(vector) == 25)
    tiny = math.ldexp(1.0, -1074)
    expect('subnormal_square_retained_exactly',
           audit.exact_squared_norm(struct.pack('<2d', tiny, 0.0)) == Q(1, 1 << 2148))
    expect('terminal_norm_enclosure', audit.check_vector_norm(vector, [25.0, 25.0]) == 25)
    reject('understated_endpoint_norm', lambda: audit.check_vector_norm(vector, [0.0, 24.0]))
    reject('nan_endpoint', lambda: audit.exact_squared_norm(struct.pack('<2d', math.nan, 0.0)))
    reject('infinite_endpoint', lambda: audit.exact_squared_norm(struct.pack('<2d', 0.0, math.inf)))
    reject('truncated_complex_vector', lambda: audit.exact_squared_norm(b'12345678'))
    expect('directed_sum_half_ulp', audit.up_add(1.0, 2**-53) == math.nextafter(1.0, math.inf))
    expect('directed_sum_subnormal', audit.up_add(tiny, tiny) == 2*tiny)

    row = (0.125, 0.25, 0.0, 0.0, 0.375, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
    expect('saved_component_row', audit.rows_from_bytes(struct.pack('<12d', *row), 1) == [row])
    short_total = list(row)
    short_total[4] = 0.125
    reject('omitted_error_component', lambda: audit.check_row(short_total))
    reject('truncated_component_row', lambda: audit.rows_from_bytes(b'0'*95))
    decreasing = list(row)
    decreasing[0], decreasing[4] = 0.0, 0.25
    reject('cumulative_bound_reset', lambda: audit.check_carry([row], [decreasing], False, 'a', 'b'))
    reject('inactive_payload_state_change', lambda: audit.check_carry([row], [row], True, 'a', 'b'))
    audit.check_carry([row], [row], True, 'same', 'same')
    expect('inactive_payload_identity', True)

    initial = bytearray(2*4*16)
    struct.pack_into('<d', initial, 0, 1.0)
    struct.pack_into('<d', initial, 16*(4+1), 1.0)
    audit.check_initial(initial, 0, dimension=4, lanes=2)
    expect('full_initial_basis_not_norm_only', True)
    wrong = bytearray(initial)
    struct.pack_into('<d', wrong, 0, 0.0)
    struct.pack_into('<d', wrong, 16*2, 1.0)
    reject('unit_norm_wrong_initial_basis', lambda: audit.check_initial(wrong, 0, dimension=4, lanes=2))
    expect('committed_prefix_sequence', audit.prefix_numbers(['checkpoint-2.json', 'checkpoint-0.json', 'checkpoint-1.json']) == [0,1,2])
    reject('checkpoint_hole', lambda: audit.prefix_numbers(['checkpoint-0.json', 'checkpoint-2.json']))
    reject('checkpoint_duplicate_alias', lambda: audit.prefix_numbers(['checkpoint-00.json']))
    reject('checkpoint_outside_word', lambda: audit.prefix_numbers([f'checkpoint-{n}.json' for n in range(82)]))
    reject('duplicate_json_key', lambda: audit.parse_json('{"radius":1,"radius":0}'))
    reject('nan_json', lambda: audit.parse_json('{"radius":NaN}'))
    reject('overflow_json', lambda: audit.parse_json('{"radius":1e999}'))
    reject('boolean_numeric_interval', lambda: audit.bounds([False, True]))
    expect('boolean_cannot_impersonate_case_zero', not audit.contract_equal(False, 0))
    expect('boolean_cannot_impersonate_nested_label', not audit.contract_equal([True,4], [1,4]))
    for name,actual,expected in (
        ('boolean_basis_occupation', [[False,True]], [[0,1]]),
        ('boolean_branch_case', False, 0),
        ('boolean_branch_label', [True,1], [1,1]),
        ('boolean_required_children', True, 1),
        ('boolean_hash_byte_count', {'bytes':False,'sha256':'x'}, {'bytes':0,'sha256':'x'})):
        reject(name, lambda actual=actual,expected=expected:
               audit.require_contract({'value':actual}, {'value':expected}, 'frozen schema'))
    reject('boolean_receipt_exit_code', lambda: audit.check_final_receipt(
        {'exit_code':False,'error':None,'cleanup_error':None}))
    reject('summary_inventory_flag_disagreement', lambda: audit.check_inventory_flag(
        {'artifact_inventory_complete':False}, {'complete':True}))
    reject('boolean_like_integer_inventory_flag', lambda: audit.check_inventory_flag(
        {'artifact_inventory_complete':False}, {'complete':0}))
    workers = [{'thread':i,'cpu':i,'place':i,'completed_tasks':2 if i < 10 else 1} for i in range(80)]
    placements = {i:worker['completed_tasks'] for i,worker in enumerate(workers)}
    audit.check_workers(workers, placements)
    expect('worker_exact_integer_schema', True)
    for field in ('thread','cpu','place','completed_tasks'):
        broken = copy.deepcopy(workers)
        broken[79 if field == 'completed_tasks' else 0][field] = (field == 'completed_tasks')
        reject('boolean_worker_'+field, lambda broken=broken: audit.check_workers(broken,placements))
    column = dict(zip(audit.FIELDS[:10], row[:10]),thermal_index=0)
    audit.check_column_values(column,row,0)
    expect('column_saved_bytes_exact', True)
    wrong_column = dict(column,thermal_index=False)
    reject('boolean_thermal_index', lambda: audit.check_column_values(wrong_column,row,0))
    wrong_column_value = dict(column,continuum=False)
    reject('boolean_raw_column_value', lambda: audit.check_column_values(wrong_column_value,row,0))
    phases = [{'phase':name,'elapsed_seconds':n} for n,name in enumerate(audit.LIFECYCLE[:4])]
    expect('available_lifecycle_prefix', len(audit.check_lifecycle(phases,False)) == 4)
    wrong_phases = copy.deepcopy(phases)
    wrong_phases[1], wrong_phases[2] = wrong_phases[2], wrong_phases[1]
    reject('misordered_lifecycle_prefix', lambda: audit.check_lifecycle(wrong_phases,False))
    reject('corrupt_committed_log_json', lambda: audit.log_records(b'{"kind":broken}\n'))
    records, truncated = audit.log_records(b'{"kind":"checkpoint"}\n{"kind":')
    expect('truncated_log_tail_is_partial', len(records) == 1 and truncated)
    checkpoint_log = {'kind':'checkpoint','case':0,'batch':0,'segment_boundary':1,
                      'committed_snapshots':2,'cells':0,'error_bound_max':0.0,'elapsed_seconds':0.1}
    totals = {(0,0,0):0.0,(0,0,1):0.0}
    expect('prefix_log_linked_to_payload', audit.check_progress([checkpoint_log],totals,False) == {'checkpoint':1})
    misordered_log = dict(checkpoint_log,segment_boundary=2)
    reject('misordered_checkpoint_log', lambda: audit.check_progress([misordered_log],totals,False))
    reject('logged_checkpoint_without_payload', lambda: audit.check_progress([checkpoint_log],{(0,0,0):0.0},False))
    wrong_error_log = dict(checkpoint_log,error_bound_max=0.5)
    reject('logged_checkpoint_total_differs_from_payload', lambda: audit.check_progress([wrong_error_log],totals,False))
    reject('unlinked_committed_prefix', lambda: audit.check_progress([],totals|{(0,0,2):0.0},False))
    bool_cells = dict(checkpoint_log,cells=False)
    reject('boolean_log_cells', lambda: audit.check_progress([bool_cells],totals,False))
    life_bytes = b''.join((json.dumps(row)+'\n').encode('ascii') for row in phases)
    incomplete_logs = audit.logs_audit(MemoryPath({'lifecycle.jsonl':life_bytes}),{},False)
    expect('missing_progress_never_available', not incomplete_logs['available'])
    reject('corrupt_available_progress_without_lifecycle', lambda: audit.logs_audit(
        MemoryPath({'progress.jsonl':b'{broken}\n'}),{},False))
    reject('corrupt_available_metadata_in_partial_set', lambda: audit.metadata_audit(
        MemoryPath({'metadata.json':b'{broken}'}),allow_missing=True))
    reject('corrupt_available_basis_in_partial_set', lambda: audit.metadata_audit(
        MemoryPath({'basis.json':b'{broken}'}),allow_missing=True))
    reject('reversed_interval', lambda: audit.bounds([1.0, 0.0]))
    root = Path(__file__).resolve().parent
    reject('inventory_path_traversal', lambda: audit.safe_member(root, '../hidden.bin'))
    reject('inventory_windows_path_traversal', lambda: audit.safe_member(root, '..\\hidden.bin'))
    reject('inventory_absolute_path', lambda: audit.safe_member(root, '/hidden.bin'))

    basis = audit.occupation_basis()
    expect('independent_basis_dimension', len(basis) == 6435)
    expect('thermal_column_36', basis[36] == (0,0,0,0,0,0,3))
    weights = [Q(20,21)**7 * Q(1,21)**sum(n) for n in basis[:120]]
    expect('unequal_thermal_mass', len(set(weights)) == 4 and sum(weights) == audit.MASS)
    expect('active_segment_inventory', [sum(audit.occupied(c,s) for s in range(80)) for c in range(6)] == [32,16,16,32,16,16])
    expect('sqrt_affine_equality', audit.affine_sqrt_enclosed(Q(3), Q(1), Q(2), Q(1)))
    expect('sqrt_affine_negative_difference_rejected', not audit.affine_sqrt_enclosed(Q(1),Q(1),Q(2),Q(1)))

    errors, norms = [Q(0)]*6, [Q(1)]*6
    pair = {'cases':[0,1], 'numerical_radius':0.0, 'thermal_radius':2**-11,
            'arithmetic_radius':0.0, 'total_radius':2**-11,
            'sine_retained_interval':[[0.004,0.004],[0.0,0.0]],
            'linear_full_interval':[[0.0,0.0],[0.0,0.0]],
            'witness_center_interval':[0.002,0.002],
            'certified_trace_distance_interval':[0.0015,0.0025]}
    outcome = audit.audit_pair(pair, (0,1), errors, norms)
    expect('precision_pass_with_resolved_discrepancy', outcome['precision_goal_pass'] and outcome['discrepancy'] == 'EXCEEDS_TARGET')
    wide = copy.deepcopy(pair)
    wide.update(numerical_radius=2**-6, total_radius=2**-5,
                sine_retained_interval=[[0.5,0.5],[0.0,0.0]],
                witness_center_interval=[0.25,0.25], certified_trace_distance_interval=[0.23,0.27])
    outcome = audit.audit_pair(wide, (0,1), errors, norms)
    expect('wide_valid_interval_resolves_discrepancy', not outcome['precision_goal_pass'] and outcome['discrepancy'] == 'EXCEEDS_TARGET')
    under_tail = copy.deepcopy(pair)
    under_tail['thermal_radius'] = 0.0
    reject('thermal_tail_silently_omitted', lambda: audit.audit_pair(under_tail,(0,1),errors,norms))
    unsafe_gram = copy.deepcopy(pair)
    reject('nonunit_gram_unsafe_sum', lambda: audit.audit_pair(unsafe_gram,(0,1),[Q(1,5)]*6,[Q(2)]*6))
    narrow = copy.deepcopy(pair)
    narrow['certified_trace_distance_interval'] = [0.002,0.002]
    reject('distance_interval_missing_numerical_thermal_expansion', lambda: audit.audit_pair(narrow,(0,1),errors,norms))
    no_arithmetic = copy.deepcopy(pair)
    no_arithmetic['witness_center_interval'] = [0.0019,0.0021]
    reject('center_arithmetic_width_omitted', lambda: audit.audit_pair(no_arithmetic,(0,1),errors,norms))
    low_total = copy.deepcopy(pair)
    low_total['total_radius'] = 0.0
    reject('understated_total_pair_radius', lambda: audit.audit_pair(low_total,(0,1),errors,norms))
    false_center = copy.deepcopy(pair)
    false_center['witness_center_interval'] = [0.003,0.003]
    reject('rectangle_magnitude_wrong_center', lambda: audit.audit_pair(false_center,(0,1),errors,norms))
    wrong_pair = copy.deepcopy(pair)
    wrong_pair['cases'] = [0,3]
    reject('cross_angle_pair', lambda: audit.audit_pair(wrong_pair,(0,1),errors,norms))
    bool_pair = copy.deepcopy(pair)
    bool_pair['cases'] = [False,True]
    reject('boolean_cases_impersonate_pair_indices', lambda: audit.audit_pair(bool_pair,(0,1),errors,norms))

    # Exact threshold equality cannot use rounded decimal displays of 1/1000.
    equal = copy.deepcopy(pair)
    equal.update(numerical_radius=Q(0), thermal_radius=audit.TAIL/2,
                 total_radius=audit.GOAL, sine_retained_interval=[[Q(0),Q(0)],[Q(0),Q(0)]],
                 linear_full_interval=[[Q(0),Q(0)],[Q(0),Q(0)]], witness_center_interval=[Q(0),Q(0)],
                 certified_trace_distance_interval=[Q(0),audit.GOAL])
    outcome = audit.audit_pair(equal,(0,1),errors,norms)
    expect('exact_threshold_equality_within', outcome['precision_goal_pass'] and outcome['discrepancy'] == 'WITHIN_TARGET')
    overlap = copy.deepcopy(pair)
    overlap['certified_trace_distance_interval'] = [0.0005,0.004]
    expect('interval_overlap_unresolved', audit.audit_pair(overlap,(0,1),errors,norms)['discrepancy'] == 'UNRESOLVED')

    report = {'status':'SYNTHETIC_AUDIT_FIXTURES_PASS', 'positive_fixtures':sorted(positive),
              'negative_fixtures_exposed':sorted(negative), 'candidate_source_imported':False,
              'campaign_data_read':False, 'solver_executed':False,
              'audit_source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    sys.stdout.write(json.dumps(report, sort_keys=True, separators=(',',':'))+'\n')


if __name__ == '__main__':
    main()
