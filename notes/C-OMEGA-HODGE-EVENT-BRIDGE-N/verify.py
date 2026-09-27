#!/usr/bin/env python3
"""Finite exact corroboration of C-OMEGA-HODGE-EVENT-BRIDGE-N."""
from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util, hashlib, math

p=Path(__file__).with_name('bridge.py')
spec=importlib.util.spec_from_file_location('omega_event_bridge',p)
B=importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
N=B.NATIVE; M=B.EVENT_MODEL

def main():
    labels=list(product(range(5),repeat=5))
    sites=[B.site(x) for x in labels]
    assert len(set(sites))==3125
    assert set(sites)==set(product(range(25),range(25),range(5)))

    states=list(product(range(5),repeat=6))
    initial=[N['label_at'](0,x) for x in states]
    fibres=Counter(initial)
    assert len(fibres)==3125 and set(fibres.values())=={5}

    current=states
    commutation=0
    for n in range(9):
        for x,label in zip(current,initial):
            assert N['label_at'](n,x)==label
        # Frozen deterministic sample across the full label cube.
        for j in range(0,len(states),31):
            x=current[j]
            y=B.step_checkpoint(n,x)
            z=B.bridge_site(n,x)
            assert B.bridge_site(n+1,y)==z
            for h in (3,5,8):
                assert B.bridge_event_label(h,n+1,y)==M.event_label(h,n+1,z)
            commutation+=1
        if n<8:
            current=[B.step_checkpoint(n,x) for x in current]

    # Stable reachable slices contain one current checkpoint per ell label.
    for n in (3,4,8,15):
        reachable={N['unchart'](n,label) for label in labels}
        assert len(reachable)==3125
        assert {N['chart'](n,x) for x in reachable}==set(labels)

    # Selected faithful bridge has spacelike equal-counter samples and
    # future-timelike same-label successors in actual rounded events.
    causal=0
    sample_labels=[labels[i] for i in (0,1,17,311,1207,3124)]
    for h in (3,5,8):
        for n in (0,1,3,7):
            events=[M.event(h,n,B.site(label)) for label in sample_labels]
            for i in range(len(events)):
                for j in range(i):
                    d=[a-b for a,b in zip(events[i],events[j])]
                    assert M.sign(M.inner(d,d))>0
                    causal+=1
            for label,e in zip(sample_labels,events):
                f=M.event(h,n+1,B.site(label))
                d=[a-b for a,b in zip(f,e)]
                assert M.sign(M.time(d))>0 and M.sign(M.inner(d,d))<0
                causal+=1

    # The fixed faithful lift is intentionally nonadditive.
    u=(1,0,0,0,0); v=(4,0,0,0,0)
    uv=tuple((a+b)%5 for a,b in zip(u,v))
    assert uv==(0,0,0,0,0)
    assert tuple(a+b for a,b in zip(B.site(u),B.site(v))) != B.site(uv)

    # Whole-Omega fixed quotient has thirteen classes.
    qclasses={N['signclass']((a,b)) for a,b in product(range(5),repeat=2)}
    assert len(qclasses)==13

    # Exact bounded-batch capacity controls.
    caps=[]
    for R in (0,1,4,8,20,50):
        need=(2*R+1)**3
        c=(need+3125-1)//3125
        assert 3125*c>=need
        if c: assert c==1 or 3125*(c-1)<need
        caps.append((R,need,c))
    assert caps[-1][2]>1

    # Current-checkpoint-only clock alignment cannot have unbounded slices:
    # any such map has <=15625 output slice values. Audit the finite premise.
    assert len(states)==15625

    print('PASS G1: faithful F5^5 integer lift is bijective onto 25x25x5 = 3125 sites')
    print('PASS G2: ell_0 has 3125 fibres of five heads; stable reachable slices have 3125 states')
    print(f'PASS G3: native/event bridge commutation sample checks={commutation}')
    print(f'PASS G4: actual rounded-event spacelike/timelike witness checks={causal}')
    print('PASS G5: faithful lift is nonadditive; additive torsion-free bridge must be zero by proof')
    print('PASS G6: whole-Omega separable quotient has exactly 13 Q classes')
    print('PASS G7: bounded-batch cube capacity arithmetic verified through R=50')
    print('NON-CANONICAL: exact address bridge exists but target, resolution and spatial assignment remain inputs')

if __name__=='__main__': main()
