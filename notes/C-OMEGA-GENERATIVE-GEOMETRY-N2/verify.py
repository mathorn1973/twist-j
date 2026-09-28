#!/usr/bin/env python3
"""Prospective exact audit. Universal claims are in PROOF.md, not the census."""
import hashlib
import importlib.util
import sys
from itertools import product
from pathlib import Path

p=Path(__file__).with_name('generate.py')
spec=importlib.util.spec_from_file_location('generative_geometry',p)
g=importlib.util.module_from_spec(spec);sys.modules[spec.name]=g;spec.loader.exec_module(g)


def main():
    root=Path(__file__).resolve().parents[2]
    for name,digest in (
        ('probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md','19435a7bd5b33f2b7995262c2dbfc8eb8fa36b6112723fe15dc957aed60ef5c4'),
        ('probes/P-SNAP-OCCURRENCE-IDENTITY-1/PROOF.md','81106a51b4b40da00f4f1eeff847159c9563d85288206275d2e2b841665b9a19'),
        ('notes/C-HODGE-EVENT-CAUCHY-N/PROOF.md','6ebac7c63bcadba55791db017d273aa2136cdbf8867a72b3006c1d46bae823af')):
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
    loaded=g.dependencies();native,M=loaded;Q=M.Q
    hex_count=0
    for r in range(9):
        H=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)
           if max(abs(x),abs(y),abs(x-y))<=r]
        assert len(H)==3*r*(r+1)+1
        image={g.phi(r,x,y) for x,y in H}
        target={z for z in product(range(r+1),repeat=3) if max(z)==r}
        assert image==target and len(image)==len(H)
        for x,y in H:assert g.phi_inverse(g.phi(r,x,y))==(r,x,y)
        for bit in (False,True):
            S=g.shell(r,bit)
            assert len(S)==(1 if r==0 else 24*r*r+2)
            assert len(S)==len(set(S))
            assert set(S)=={z for z in product(range(-r,r+1),repeat=3) if max(map(abs,z))==r}
        hex_count+=len(H)
    # Native heads and all prefixes, no repeated/replaced vertices or edges.
    completed=[];orders=[];prefix_count=0
    for phase in range(5):
        head=(phase,0,0,0,0,0)
        writer=g.Generator(head,3,loaded=loaded)
        history=[head];present=set();edges=set();saved=None
        for i in range(g.spatial_size(3)):
            before=tuple(writer.records)
            rec=writer.advance();history.append(writer.current)
            assert tuple(writer.records[:-1])==before
            assert rec.ordinal==i and rec.address[0]==0 and rec.address not in present
            if i:assert rec.prior_links
            assert all(a in present for a in rec.prior_links)
            for a in rec.prior_links:
                edge=tuple(sorted((a,rec.address)))
                assert edge not in edges;edges.add(edge)
            present.add(rec.address)
            assert M.admitted(M.event_label(3,0,rec.address[1]))
            if i==26:saved=tuple(writer.records)
            for r in range(4):
                if i+1==g.spatial_size(r):
                    assert present=={(0,z) for z in product(range(-r,r+1),repeat=3)}
                    expected_edges={tuple(sorted((a,(0,v)))) for a in present
                                    for v in g.adjacent(a[1]) if (0,v) in present}
                    assert edges==expected_edges
            prefix_count+=1
        assert tuple(writer.records[:27])==saved
        assert g.decode_prefix(history[:28],h=3,loaded=loaded)==saved
        completed.append(present)
        orders.append(tuple(r.address for r in writer.records))
        snapshot=tuple(writer.records)
        try:writer.advance((9,)*6)
        except ValueError:pass
        else:raise AssertionError('Illegal native input accepted')
        assert tuple(writer.records)==snapshot
    assert all(x==completed[0] for x in completed)
    assert len(set(orders))>1
    # Positive projected metric, exact rational-square bounds; immutable scale.
    norm_sq=[M.inner(v,v) for v in M.frame[1:]]
    samples=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(-1,2,0),(3,-2,1),(-3,-2,-1)]
    metric_count=0
    for h in (3,5,8):
        points={z:tuple(M.event(h,0,z)) for z in samples}
        for i,z in enumerate(samples):
            for w in samples[:i]:
                d=g.squared_spatial_distance(M,points[z],points[w])
                ideal=sum((a*(x-y)**2 for a,x,y in zip(norm_sq,z,w)),Q(0))/h**2
                assert M.sign(d)>0
                assert M.sign(d-Q(25)*ideal/81)>=0
                assert M.sign(Q(169)*ideal/81-d)>=0
                metric_count+=1
    # Full dependency-closed field patches, independently computed sparse solution.
    R=4
    size=g.spacetime_size(R)
    assert size==sum((2*r+1)**3 for r in range(R+1))
    f0={(0,0,0):Q(2),(1,0,0):Q(-1)}
    f1={(0,0,0):Q(1),(0,1,0):Q(1)/2}
    forces={1:{(0,0,0):Q(2)/7},2:{(-1,0,0):Q(-1)/5}}
    comparisons=0
    for forced in (False,True):
        source=lambda m,z:forces.get(m,{}).get(z,Q(0)) if forced else Q(0)
        initial=lambda m,z:(f0 if m==0 else f1).get(z,Q(0))
        full=[f0,f1]
        for m in range(1,R):
            drive={z:v/9 for z,v in forces.get(m,{}).items()} if forced else {}
            full.append(M.step(full[-2],full[-1],drive))
        writer=g.Generator((0,)*6,3,'field',initial,source,loaded)
        seen=set();patches={}
        for i in range(size):
            prior=tuple(writer.records)
            rec=writer.advance();m,z=rec.address
            assert tuple(writer.records[:-1])==prior and rec.address not in seen
            assert all(a in seen for a in rec.prior_links)
            assert rec.value==g.pack(full[m].get(z,Q(0)))
            seen.add(rec.address);comparisons+=1
            assert M.admitted(M.event_label(3,m,z))
            for r in range(R+1):
                if i+1==g.spacetime_size(r):
                    expected={(m,z) for m in range(r+1)
                              for z in product(range(-(r-m),r-m+1),repeat=3)}
                    assert seen==expected
                    patches[r]=tuple(writer.records)
        for r,saved in patches.items():assert tuple(writer.records[:g.spacetime_size(r)])==saved
    # Exact serial budget and independent metric-nonselection controls.
    for r in range(31):
        assert g.spacetime_size(r)==sum((2*k+1)**3 for k in range(r+1))
        for volume in (g.spatial_size(r),g.spacetime_size(r)):
            for c in (1,2,7,31):
                ticks=(volume+c-1)//c
                assert (ticks-1)*c<volume<=ticks*c
    vectors=list(product(range(-2,3),repeat=3))
    unit0=sum(sum(v*v for v in z)==1 for z in vectors)
    unit1=sum(sum(a*v*v for a,v in zip((1,2,3),z))==1 for z in vectors)
    assert (unit0,unit1)==(6,2)
    print(f'PASS G1: tagged hexagon/cube bijection; {hex_count} exact pairs; signed shells r=0..8')
    print(f'PASS G2: {prefix_count} native-prefix appends; connected immutable graphs; complete C_3 for five heads')
    print(f'PASS G3: {metric_count} exact projected-metric controls at h=3,5,8; rational 5/9 and 13/9 bounds')
    print(f'PASS G4: {comparisons} exact field records on K_4 match independent sparse evolution; no boundary substitution')
    print('PASS G5: cubic spatial/quartic spacetime record counts and sharp batch completion costs')
    print('PASS G6: native selectors change partial order, not completed geometry; inequivalent metric controls 6 versus 2')
    print('NON-CANONICAL: generator and stable scalar continuation exist; native metric selection and physical memory are not supplied')

if __name__=='__main__':main()
