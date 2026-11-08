#!/usr/bin/env python3
"""Exact classification of F=C23 C12 by bounded descent to a primitive orbit.

NON-CANONICAL / L1. Adapted from the already exposed 2026-11-02 source audit.
Only standard-library integer arithmetic; no independent-review claim is made.
Computational statements and stdout are unchanged from that source.
"""
from itertools import product
from random import Random
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
Z=(0,0,0,0)
ONE=(1,0,0,0)
J=(0,1,0,0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mulint(a,k): return tuple(k*x for x in a)
def rho(x):
    a,b,c,d=x
    return (d-c,-c,a-c,b-c)
def Q(x): return (5*sum(t*t for t in x)-sum(x)**2)//2

def contact(a,b):
    delta=sub(a,b)
    if any(t%2 for t in delta): return a,b,1
    total=add(a,b);rot=rho(delta)
    u=tuple((t+r)//2 for t,r in zip(total,rot))
    v=tuple((t-r)//2 for t,r in zip(total,rot))
    assert add(u,v)==total and Q(u)+Q(v)==Q(a)+Q(b)
    return u,v,0

def F(x):
    a,b,c=x
    a,b,r1=contact(a,b)
    b,c,r2=contact(b,c)
    return (a,b,c),r1+r2

def state_sum(x):return add(add(x[0],x[1]),x[2])
def energy(x):return sum(map(Q,x))
def even(x):return all(v%2==0 for a in x for v in a)
def scale(x,n):return tuple(mulint(a,n) for a in x)
def centered(x):
    s=state_sum(x)
    return tuple(sub(mulint(a,3),s) for a in x)

def depth(x):
    coefficients=[v for a in (sub(x[0],x[1]),sub(x[1],x[2])) for v in a if v]
    if not coefficients:return None
    def v2(n):
        n=abs(n);r=0
        while n%2==0:r+=1;n//=2
        return r
    return min(map(v2,coefficients))

def orbit(x,cap=150000):
    initial=x;states=[];rs=[];seen=set()
    while x not in seen:
        assert len(states)<cap,('orbit cap',cap,initial)
        seen.add(x);states.append(x)
        x,r=F(x);rs.append(r)
    assert x==initial
    return states,rs

def primitive_or_even(x):
    """Return an even state within eight ticks, or a complete 1/5 cycle."""
    assert state_sum(x)==Z
    start=x;states=[];rs=[];seen=set()
    for t in range(9):
        if even(x):return {'even_state':x,'ticks':t}
        if x in seen:
            assert x==start
            assert len(states) in (1,5)
            return {'base_states':states,'base_rejects':rs,'ticks':t}
        seen.add(x);states.append(x)
        if t==8:break
        x,r=F(x);rs.append(r)
    raise AssertionError(('eight-tick lemma failed',start))

def classify(x):
    y=centered(x)
    if y==(Z,Z,Z):
        return {'kind':'uniform','depth':None,'P':1,'R':0,'base_P':1,'base_R':0,'deep_states':1,'deep_gap':1,'descent_ticks':[]}
    d=0;levels=[]
    while True:
        result=primitive_or_even(y)
        levels.append(result['ticks'])
        if 'even_state' in result:
            y=tuple(tuple(v//2 for v in a) for a in result['even_state'])
            d+=1
            continue
        p0=len(result['base_states']);r0=sum(result['base_rejects'])
        assert (p0,r0) in ((1,1),(1,2),(5,5)),(x,p0,r0,result)
        kind={(1,1):'one_rejection_fixed',(1,2):'two_rejection_fixed',(5,5):'five_cycle'}[(p0,r0)]
        p=p0+4*r0*(4**d-1)//3
        r=r0*4**d
        return {'kind':kind,'depth':d,'P':p,'R':r,'base_P':p0,'base_R':r0,'base_start':result['base_states'][0],'deep_states':p0,'deep_gap':p//p0,'descent_ticks':levels}

def classify_relative(x):
    """Same classification using only shifts by the third slot and halving."""
    if x[0]==x[1]==x[2]:return 1,0,None
    d=0
    while True:
        start=x;seen=set();rs=[]
        for t in range(9):
            if all(v%2==0 for a in (sub(x[0],x[1]),sub(x[1],x[2])) for v in a):
                c=x[2]
                x=tuple(tuple(v//2 for v in sub(a,c)) for a in x)
                d+=1
                break
            if x in seen:
                assert x==start
                p0=len(seen);r0=sum(rs)
                assert (p0,r0) in ((1,1),(1,2),(5,5))
                return p0+4*r0*(4**d-1)//3,r0*4**d,d
            seen.add(x)
            assert t<8,('relative eight-tick lemma failed',start)
            x,r=F(x);rs.append(r)

def check(x):
    prediction=classify(x)
    assert classify_relative(x)==(prediction['P'],prediction['R'],prediction['depth'])
    states,rs=orbit(x)
    assert prediction['P']==len(states)
    assert prediction['R']==sum(rs)
    if prediction['kind']!='uniform':
        M=Q(sub(x[0],x[1]))+Q(sub(x[1],x[2]))+Q(sub(x[0],x[2]))
        assert 3*prediction['P']<=2*M-5
        multiplier=12 if prediction['kind']=='five_cycle' else 4
        assert M>=multiplier*4**prediction['depth']
        ds=[depth(y) for y in states]
        d=max(ds)
        assert prediction['depth']==d
        positions=[k for k,v in enumerate(ds) if v==d]
        assert len(positions)==prediction['deep_states']
        gaps=[(positions[(i+1)%len(positions)]-p)%len(states) or len(states) for i,p in enumerate(positions)]
        assert set(gaps)=={prediction['deep_gap']}
    return prediction,len(states)

def main():
    rng=Random(20261102)
    samples=[]
    for a,b,c in product(range(-4,5),repeat=3):
        samples.append(((a,0,0,0),(b,0,0,0),(c,0,0,0)))
    for k in range(600):
        x=tuple(tuple(rng.randrange(-4,5) for _ in range(4)) for _ in range(3))
        if k%5==0:x=scale(x,2)
        if k%11==0:x=scale(x,2)
        samples.append(x)
    base_examples=[
        (ONE,ONE,mulint(ONE,-2)),
        (ONE,J,mulint(add(ONE,J),-1)),
        (ONE,mulint(ONE,-1),Z),
    ]
    for base in base_examples:
        for d in range(6):
            samples.append(scale(base,2**d))
    rows=[];steps=0
    for x in samples:
        prediction,n=check(x);steps+=n
        rows.append({'start':x,**prediction})
    example=((4,0,0,0),Z,(2,0,0,0))
    row,_=check(example);st,rs=orbit(example)
    word=''.join(str(int(depth(y)==row['depth'])) for y in st)
    assert word=='10000'*5
    example_result={**row,'start':example,'E':energy(example),'S':state_sum(example),'deep_indicator_word':word,'deep_states_full':[y for y in st if depth(y)==row['depth']]}
    large=[]
    for d in (10,50,100):
        for base in base_examples:
            prediction=classify(scale(base,2**d))
            assert prediction['depth']==d
            large.append({'input_scale_exponent':d,**prediction})
    sharp_minimum_cases=[]
    sharp_bases=[(ONE,Z,Z),(Z,ONE,Z),(ONE,mulint(ONE,-1),Z)]
    for d in range(6):
        for index,base in enumerate(sharp_bases):
            x=scale(base,2**d)
            prediction=classify(x)
            M=Q(sub(x[0],x[1]))+Q(sub(x[1],x[2]))+Q(sub(x[0],x[2]))
            assert prediction['depth']==d
            assert M==(12 if index==2 else 4)*4**d
            assert prediction['kind']==('one_rejection_fixed','two_rejection_fixed','five_cycle')[index]
            if index==1:assert 3*prediction['P']==2*M-5
            sharp_minimum_cases.append({'depth':d,'kind':prediction['kind'],'M':M,'P':prediction['P']})
    result={
        'status':'PASS',
        'arithmetic':'integer only',
        'fully_enumerated_orbits':len(rows),
        'fully_enumerated_states':steps,
        'observed_periods':sorted(set(row['P'] for row in rows)),
        'maximum_verified_period':max(row['P'] for row in rows),
        'maximum_descent_phase_search':max(max(row['descent_ticks'],default=0) for row in rows),
        'base_types':sorted({(row['base_P'],row['base_R']) for row in rows}),
        'relative_descent_matches_centered_descent':True,
        'class_specific_M_bounds_and_global_period_bound_checked':sum(row['kind']!='uniform' for row in rows),
        'sharp_minimum_cases_checked':len(sharp_minimum_cases),
        'sharp_minimum_cases':sharp_minimum_cases,
        'counterexample_to_max_depth_marker_reading_full_period':example_result,
        'large_integer_predictions_not_orbit_enumerations':large,
        'rows':rows,
    }
    (HERE/'CLASSIFICATION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','large_integer_predictions_not_orbit_enumerations','counterexample_to_max_depth_marker_reading_full_period','sharp_minimum_cases')},indent=2))
    print(json.dumps(example_result,indent=2))

if __name__=='__main__':main()
