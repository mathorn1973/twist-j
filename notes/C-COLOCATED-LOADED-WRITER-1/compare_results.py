#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Compare common fields of frozen independent first-run records; no rerun."""
import hashlib
import json
from pathlib import Path

p = Path(__file__).resolve().parent
a = json.loads((p / 'EXPECTED.txt').read_text())
b = json.loads((p / 'BREAK_EXPECTED.txt').read_text())
checks = 0


def same(x, y, name):
    global checks
    checks += 1
    if x != y:
        raise AssertionError((name, x, y))


same(a['status'], b['outcome'], 'outcome')
same(a['general']['inputs'], b['general_loaded']['inputs'], 'general inputs')
same(5*a['general']['admitted'], b['general_loaded']['counts']['admitted'], 'general admissions')
br = {}
for row in b['two_contact']['rows']:
    name = row['input']
    key = 'Jrho0' if name == 'J' else name.replace('J*rho^', 'Jrho')
    br[key] = row
same(len(a['two_contact']), len(br), 'two-contact count')
mapping = {'admitted': 'admitted', 'changed': 'state_changes',
           'diagonal_admitted': 'accepted_diagonal', 'field_changes': 'field_changes',
           'attempts': 'attempts'}
for ar in a['two_contact']:
    row = br[ar['input']]
    same(ar['account'], row['account'], 'two account')
    same(ar['record_q'], row['record_q'], 'record Q')
    same(ar['record'], row['endpoint']['slots'][3], 'record coordinate')
    for k, kk in mapping.items():
        same(ar[k], row['forward'][kk], 'two '+k)
bp = b['root_pair']
same(a['phase']['account'], bp['account'], 'phase account')
same(a['phase']['inputs'], bp['inputs'], 'phase inputs')
same(a['phase']['forward_contacts'], bp['forward_word_length'], 'forward length')
same(a['phase']['inverse_contacts'], bp['inverse_word_length'], 'inverse length')
rows = [row['input'] + row['output'] for row in bp['phase_table']]
digest = hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
same(a['phase']['matrix_sha256'], digest, 'all 125 phase outputs')
for k, v in a['phase']['forward_totals'].items():
    same(v, bp['counts']['forward'][mapping[k]], 'phase '+k)
writers = [row['input'][:2] + row['output'] + [row['forward']['field_changes']]
           for row in bp['positive_writer']['rows']]
same(a['phase']['writer_inputs'], len(writers), 'writer count')
for ar, row in zip(a['phase']['writer_rows'], writers):
    same(ar, row, 'writer endpoint and field changes')
print(f'PASS: {checks} common result comparisons; all 125 phase outputs agree.')
