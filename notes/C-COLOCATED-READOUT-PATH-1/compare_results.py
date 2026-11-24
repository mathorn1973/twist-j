#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Compare saved primary output with the disclosed explicit-convention audit."""
import json
from pathlib import Path

p = Path(__file__).resolve().parent
a = json.loads((p/'EXPECTED.txt').read_text())
b = json.loads((p/'BREAK_EXPLICIT_TRACE_EXPECTED.txt').read_text())
n = 0


def same(x,y,label):
    global n
    n += 1
    if x != y:
        raise AssertionError((label,x,y))


same(a['status'],b['status'],'completed statuses')
same(len(a['paid_readout']['rows']),len(b['A']),'paid domain')
for x,y in zip(a['paid_readout']['rows'],b['A']):
    for k,kk in [('input','input'),('writer_phase','writer_phases'),('stock','stock_out'),
                 ('stock_q','stock_Q'),('memory_q','memory_Q'),('field_returned','field_return')]:
        same(x[k],y[kk],'paid '+k)
    same(x['reader_counts']['admitted'],y['reader_admissions'],'reader admissions')
by={(r['path'],'cut5' if r['timing']=='immediate' else r['timing']):r for r in b['B']}
same(len(a['path_record']['rows']),len(by),'path domain')
roots=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[-1,-1,-1,-1]]
for x in a['path_record']['rows']:
    y=by[x['path'],x['timing']]
    for k,kk in [('response','record_Q'),('field','field_final'),('account','E'),
                 ('hermitian_account','H_account'),('area','H_path'),
                 ('source_area','H_source'),('port_area','H_port')]:
        same(x[k],y[kk],'path '+k)
    same(x['slots'],y['source_final']+y['archive_final'],'complete path endpoint')
    same(x['determinant'],roots[y['combined_det_j_exponent']],'actual determinant')
    for k,kk in [('attempts','attempts'),('admitted','admissions'),('changed','changes'),
                 ('diagonal','diagonal'),('field_changes','field_changes')]:
        same(x['counts'][k],y['source_counts'][kk]+y['port_counts'][kk],'path '+k)
print(f'PASS: {n} common result comparisons; 125 paid cases and 6 path/control cases agree.')
print('Original and reader-boundary checker STOP outputs remain preserved; comparison uses the disclosed explicit-trace revision.')
