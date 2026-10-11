#!/usr/bin/env python3
"""One frozen floating campaign. No scientific work executes on import.

PUBLIC NON-CANONICAL; Apache-2.0, A. M. Thorn. Not interval arithmetic.
"""
import argparse
import cmath
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

from linear_model import (advance, artifact, digest, environment, finite_tree,
                          load_json_bytes, prepare_model, require, topology,
                          utc, write_json, zero_state)

SOURCES = {'README.md','PREREG.md','DERIVATION.md','EXACT-DESIGN.md','input.json',
           'linear_model.py','verify.py','kernel.cpp','numerical_run.py'}
PANEL = ((4,3),(4,4),(1,1))
CONFIGS = ((4,128),(6,128),(6,256),(6,512))
BUDGET_SECONDS = 1800


def interrupted(signum, frame):
    raise RuntimeError('Campaign interrupted by signal '+str(signum))


def pins(source, binary):
    rows = (source/'SOURCE_SHA256SUMS').read_text(encoding='ascii').splitlines()
    found = {}
    for row in rows:
        expected, name = row.split('  ')
        require(name in SOURCES and name not in found, 'source manifest inventory')
        require(digest(source/name) == expected, 'source hash: '+name)
        found[name] = expected
    require(set(found) == SOURCES, 'incomplete source inventory')
    found['SOURCE_SHA256SUMS'] = digest(source/'SOURCE_SHA256SUMS')
    found['binary'] = digest(binary)
    return found


def serialize(path, model):
    rows = [[model[k] for k in ('mu','k','tau','nbar')], model['omega'], model['position']]
    for matrix in (model['kappa'], [[z.real for z in row] for row in model['eta']],
                   [[z.imag for z in row] for row in model['eta']]):
        rows.extend(matrix)
    rows.extend([[p['theta_rad']]+p['amplitudes_rad_s'] for p in model['pulses']])
    with path.open('x', encoding='ascii', newline='\n') as f:
        f.write('\n'.join(' '.join(format(x,'.17g') for x in row) for row in rows)+'\n')


def linear_endpoints(model):
    out=[]
    for sign_index in range(2):
        for a,b in PANEL:
            state=zero_state()
            for segment in range(80):
                state=advance(model,state,sign_index*25+5*a+b,segment,model['dt'])
            out.append(dict(labels=[a,b], sign=model['pulses'][sign_index]['sign'],
                            alpha=[[z.real,z.imag] for z in state['l']],
                            phase=state['pl'], unary=state['unary']))
    return out


def check_map(mapping, places):
    require(type(mapping) is list and len(mapping)==80, 'thread map size')
    require({r['thread'] for r in mapping}==set(range(80)), 'thread coverage')
    require({r['cpu'] for r in mapping}==set(places), 'CPU coverage')
    require({r['place'] for r in mapping}==set(range(80)), 'place coverage')
    require(all(r['cpu']==places[r['place']] for r in mapping), 'CPU/place association')


def endpoints(directory, cutoff):
    import numpy as np
    basis_record=load_json_bytes((directory/'basis.json').read_bytes())
    require(basis_record['cutoff']==cutoff and basis_record['thermal_cutoff']==3,'basis cutoffs')
    basis=basis_record['occupations']
    require(type(basis) is list and len(basis)==math.comb(cutoff+7,7), 'basis dimension')
    require(len({tuple(n) for n in basis})==len(basis), 'duplicate basis state')
    require(all(len(n)==7 and all(type(x) is int and x>=0 for x in n)
                and sum(n)<=cutoff for n in basis), 'basis carrier')
    require([sum(n) for n in basis]==sorted(sum(n) for n in basis), 'basis grading')
    require(sum(sum(n)<=3 for n in basis)==120, 'initial thermal carrier')
    path=directory/'endpoints.bin'
    require(path.stat().st_size==6*120*len(basis)*16, 'endpoint bytes')
    v=np.memmap(path,dtype='<c16',mode='r',shape=(6,120,len(basis)))
    require(bool(np.isfinite(v).all()), 'nonfinite endpoint')
    return basis,v


def compare_states(old_dir, old_L, new_dir, new_L):
    import numpy as np
    old_basis,a=endpoints(old_dir,old_L)
    new_basis,b=endpoints(new_dir,new_L)
    require(old_basis==new_basis[:len(old_basis)], 'basis prefix embedding')
    weights=np.array([(20/21)**7*(1/21)**sum(n) for n in old_basis[:120]])
    retained_mass=float(weights.sum())
    distance=[]
    for case in range(6):
        q=np.sum(np.abs(b[case,:,:len(old_basis)]-a[case])**2,axis=1)
        if new_L>old_L:
            q+=np.sum(np.abs(b[case,:,len(old_basis):])**2,axis=1)
        distance.append(float(np.sqrt(np.dot(weights,q))))
    return dict(weighted_endpoint_vector_distance=distance,
                maximum=max(distance),retained_thermal_mass=retained_mass,
                interpretation='Unnormalized thermal purification vector difference; convergence diagnostic only.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--binary',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    source=Path(__file__).resolve().parent
    binary=args.binary.resolve()
    out=args.output.resolve()
    out.mkdir(parents=True,exist_ok=False)
    signal.signal(signal.SIGTERM,interrupted)
    signal.signal(signal.SIGINT,interrupted)
    started=time.perf_counter()
    initial_pins=pins(source,binary)
    write_json(out/'source-pins.json',initial_pins)
    rows,places=topology()
    env,overrides=environment(places)
    import numpy as np
    write_json(out/'metadata.json',dict(started_utc=utc(),numpy=np.__version__,
               topology=rows,environment=overrides,configurations=CONFIGS,
               budget_seconds=BUDGET_SECONDS))
    model=prepare_model(load_json_bytes((source/'input.json').read_bytes()))
    serialize(out/'input.txt',model)
    input_pin=artifact(out/'input.txt')
    write_json(out/'input-pin.json',input_pin)
    oracle=linear_endpoints(model)
    write_json(out/'linear-oracle.json',oracle)
    results=[]
    status='COMPLETE'
    failure=None
    try:
        for cutoff,steps in CONFIGS:
            require(pins(source,binary)==initial_pins,'source/binary mutation before child')
            require(artifact(out/'input.txt')==input_pin,'generated input mutation before child')
            remaining=BUDGET_SECONDS-(time.perf_counter()-started)
            require(remaining>0, 'CAMPAIGN_BUDGET_EXHAUSTED')
            label=f'L{cutoff}-N{steps}'
            run=out/label
            run.mkdir()
            cmd=[str(binary),'--input',str(out/'input.txt'),'--cutoff',str(cutoff),
                 '--steps',str(steps),'--output',str(run/'states')]
            record=dict(command=cmd,started_utc=utc(),cutoff=cutoff,steps=steps)
            t=time.perf_counter()
            with (run/'stdout').open('xb') as stdout,(run/'stderr').open('xb') as stderr:
                child=subprocess.Popen(cmd,stdout=stdout,stderr=stderr,env=env,start_new_session=True)
                timed_out=False
                interrupted_by=None
                try:
                    code=child.wait(timeout=remaining)
                except subprocess.TimeoutExpired:
                    timed_out=True
                    os.killpg(child.pid,signal.SIGKILL)
                    code=child.wait()
                except BaseException as error:
                    interrupted_by=repr(error)
                    if child.poll() is None:
                        os.killpg(child.pid,signal.SIGKILL)
                    code=child.wait()
            record.update(finished_utc=utc(),wall_seconds=time.perf_counter()-t,
                          exit_code=code,timed_out=timed_out,
                          interrupted_by=interrupted_by,
                          stdout=artifact(run/'stdout'),stderr=artifact(run/'stderr'))
            write_json(run/'record.json',record)
            require(pins(source,binary)==initial_pins,'source/binary mutation after child')
            require(artifact(out/'input.txt')==input_pin,'generated input mutation after child')
            require(not timed_out and interrupted_by is None and code==0 and (run/'stderr').stat().st_size==0,
                    'numerical process failed: '+label)
            result=load_json_bytes((run/'stdout').read_bytes())
            validate(result,cutoff,steps,places,oracle,model)
            endpoints(run/'states',cutoff)
            record['result']=result
            record['files']={n:artifact(run/'states'/n) for n in ('endpoints.bin','basis.json')}
            write_json(run/'validated.json',record)
            results.append(dict(label=label,cutoff=cutoff,steps=steps,record=record))
            write_json(out/(label+'-complete.json'),dict(label=label,utc=utc()))
    except Exception as error:
        status='INCOMPLETE'
        failure=repr(error)
    comparisons={}
    available={x['label']:x for x in results}
    for name,left,right in (('cutoff','L4-N128','L6-N128'),
                             ('time_coarse','L6-N128','L6-N256'),
                             ('time_fine','L6-N256','L6-N512')):
        if left in available and right in available:
            comparisons[name]=compare_states(out/left/'states',available[left]['cutoff'],
                                            out/right/'states',available[right]['cutoff'])
    require(pins(source,binary)==initial_pins,'source/binary mutation')
    norm_error=max((b['max_norm_error'] for row in results
                    for b in row['record']['result']['branches']),default=None)
    converged=(status=='COMPLETE' and len(comparisons)==3
               and comparisons['cutoff']['maximum']<=1e-4
               and comparisons['time_fine']['maximum']<=1e-4
               and norm_error<=1e-6)
    summary=dict(status=status,failure=failure,results=results,comparisons=comparisons,
                 engineering_convergence_screen='PASS' if converged else 'UNRESOLVED',
                 maximum_norm_error=norm_error,
                 thermal_tail=1-sum(math.comb(n+6,6)*(20/21)**7*(1/21)**n for n in range(4)),
                 wall_seconds=time.perf_counter()-started,finished_utc=utc(),
                 continuous_time_certificate=False,rigorous_dynamic_tail_bound=False,
                 all_25_branches_tested=False,hardware_admission=False)
    write_json(out/'result.json',summary)
    print(json.dumps(dict(status=status,completed_configurations=len(results),
                          wall_seconds=summary['wall_seconds']),sort_keys=True))
    return 0 if status=='COMPLETE' else 2


def validate(result,cutoff,steps,places,oracle,model):
    require(type(result) is dict and result.get('status')=='COMPLETED','kernel status')
    finite_tree(result)
    for name,value in dict(cutoff=cutoff,steps_per_segment=steps,thermal_cutoff=3,
                           thermal_columns=120,dimension=math.comb(cutoff+7,7),
                           cases=6,tasks=90,threads=80).items():
        require(type(result.get(name)) is int and result[name]==value,'dimension: '+name)
    check_map(result['thread_map'],places)
    fixture_names={'dense_displacement_error','adjoint_error','zero_error',
                   'hermiticity_error','single_mode_error'}
    require(set(result['fixtures'])==fixture_names,'fixture inventory')
    require(all(0<=v<=1e-11 for v in result['fixtures'].values()),'operator fixture error')
    mass=sum(math.comb(n+6,6)*(20/21)**7*(1/21)**n for n in range(4))
    require(abs(result['retained_thermal_weight']-mass)<=1e-12,'retained weight')
    require(abs(result['omitted_thermal_weight']-(1-mass))<=1e-12,'omitted weight')
    require(len(result['branches'])==6,'branch inventory')
    max_alpha=max_phase=0.0
    for case,(branch,ref) in enumerate(zip(result['branches'],oracle)):
        require(branch['case']==case and branch['sign']==ref['sign']
                and branch['labels']==ref['labels'],'branch identity')
        require(branch['active_steps']==(32 if case%3==0 else 16)*steps,'active chronology')
        require(len(branch['linear_alpha'])==7,'alpha shape')
        error=max(abs(complex(*a)-complex(*b))
                  for a,b in zip(branch['linear_alpha'],ref['alpha']))
        phase_error=abs(branch['linear_phase']-ref['phase'])
        max_alpha=max(max_alpha,error);max_phase=max(max_phase,phase_error)
        require(error<=1e-9 and phase_error<=1e-8,'independent full-linear endpoint')
        for name in ('max_norm_error','max_boundary_weight','sampled_projection_residual_integral'):
            require(branch[name]>=0,'negative diagnostic: '+name)
        require(len(branch['retained_same_branch_overlap'])==2,'complex echo shape')
    pairs=[(3*s+a,3*s+b) for s in range(2) for a in range(3) for b in range(a+1,3)]
    require([tuple(p['cases']) for p in result['pair_coherences']]==pairs,'pair panel')
    for pair,(a,b) in zip(result['pair_coherences'],pairs):
        aa=[complex(*z) for z in oracle[a]['alpha']]
        ab=[complex(*z) for z in oracle[b]['alpha']]
        phase=oracle[a]['phase']-oracle[b]['phase']+sum((y.conjugate()*x).imag for x,y in zip(aa,ab))
        decay=sum((model['nbar']+0.5)*abs(x-y)**2 for x,y in zip(aa,ab))
        expected=cmath.exp(complex(-decay,phase))
        linear=complex(*pair['linear_full']);sine=complex(*pair['sine_retained'])
        require(abs(linear-expected)<=1e-8,'independent analytic thermal coherence')
        require(abs(pair['witness_center']-abs(sine-linear)/2)<=1e-12,'pair witness definition')
        require(abs(pair['thermal_radius']-(1-mass)/2)<=1e-12,'thermal witness radius')
    result['independent_endpoint_oracle']={'max_alpha_error':max_alpha,'max_phase_error':max_phase}


if __name__=='__main__':
    sys.exit(main())
