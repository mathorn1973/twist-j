#!/usr/bin/env python3
"""Exact prospective audits; universal arguments are in PROOF.md."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util

p=Path(__file__).with_name('model.py')
spec=importlib.util.spec_from_file_location('event_cauchy_model',p)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def main():
    M=mod.Model(); Q=M.Q; Z=M.zero; O=M.one
    norms=[M.inner(v,v) for v in M.frame]
    assert norms==[-M.ct,Q(0,F(2,5)),Q(0,F(6,5)),Q(0,F(3,2))]
    for i in range(4):
        for j in range(i):assert M.inner(M.frame[i],M.frame[j])==Z
    assert tuple(M.ct/a for a in norms[1:])==M.alpha
    assert M.total==Q(F(1,2),F(1,5))
    assert M.sign(O-M.total)>0 and M.sign(M.R)>0 and M.sign(M.R-6)<0
    assert all(M.sign(a-M.ct)>0 for a in norms[1:])
    count=0
    for n in (3,4,8):
        seen=set()
        for m in (-1,0,1,2):
            for z in product((-1,0,1),repeat=3):
                label=M.event_label(n,m,z)
                assert M.admitted(label) and label not in seen
                seen.add(label); count+=1
                x=M.event(n,m,z); y=M.event(n,m+1,z)
                d=[b-a for a,b in zip(x,y)]
                assert M.sign(M.time(d))>0 and M.sign(M.inner(d,d))<0
        x=M.event(n,0,(0,0,0))
        for z in ((1,0,0),(0,1,0),(0,0,1)):
            d=[b-a for a,b in zip(x,M.event(n,0,z))]
            assert M.sign(M.inner(d,d))>0
    # Exact sparse evolution, inverse and energy, all on the infinite grid.
    u0={(0,0,0):Q(2),(1,0,0):Q(-1)}
    u1={(0,0,0):Q(1),(0,1,0):Q(F(1,2))}
    energy=M.energy(u0,u1); assert M.sign(energy)>0
    old,cur=u0,u1
    for m in range(1,6):
        nxt=M.step(old,cur)
        assert M.energy(cur,nxt)==energy
        assert M.step(nxt,cur)==old
        v=M.combine((1,cur),(-1,old)); a=M.combine((Q(F(1,2)),cur),(Q(F(1,2)),old))
        expression=(M.dot(v,v)-M.dot(v,M.K(v))/4+M.dot(a,M.K(a)))/2
        assert expression==energy
        assert M.sign(energy-(1-M.total)*M.dot(v,v)/2)>=0
        old,cur=cur,nxt
    drive={(0,0,0):Q(F(2,7)),(0,0,1):Q(F(-1,5))}
    nxt=M.step(u0,u1,drive)
    assert M.energy(u1,nxt)-M.energy(u0,u1)==M.dot(drive,M.combine((1,nxt),(-1,u0)))/2
    # Independent direct neighbor formula on a periodic audit fixture.
    sites=list(product(range(3),repeat=3))
    f={z:Q(F((3*z[0]+2*z[1]+z[2])%5-2,3)) for z in sites}
    def periodic_K(v):
        out={}
        for z in sites:
            s=Z
            for i,a in enumerate(M.alpha):
                l=list(z);r=list(z);l[i]=(l[i]-1)%3;r[i]=(r[i]+1)%3
                s+=a*(2*v[z]-v[tuple(l)]-v[tuple(r)])
            out[z]=s
        return out
    dense={z:Z for z in sites}
    for z,v in f.items():
        dense[z]+=2*M.total*v
        for i,a in enumerate(M.alpha):
            for step in (-1,1):
                q=list(z);q[i]=(q[i]+step)%3
                dense[tuple(q)]-=a*v
    assert dense==periodic_K(f)
    f2={z:Q(F((z[0]+z[1]+3*z[2])%7-3,4)) for z in sites}
    assert M.dot(f,periodic_K(f2))==M.dot(periodic_K(f),f2)
    assert M.sign(M.dot(f,periodic_K(f)))>=0
    assert M.sign(4*M.total*M.dot(f,f)-M.dot(f,periodic_K(f)))>=0
    # Retarded kernel, support, and Duhamel on a genuinely forced prefix.
    greens=[{}, {(0,0,0):O}]
    for r in range(1,6):greens.append(M.step(greens[-2],greens[-1]))
    for r,g in enumerate(greens[1:],1):
        assert all(sum(abs(x) for x in z)<=r-1 for z in g)
    forces={1:drive,3:{(1,0,0):Q(F(1,9))}}
    old,cur=u0,u1
    for m in range(1,5):
        total=M.combine((1,M.convolution(greens[m],u1)),(-1,M.convolution(greens[m-1],u0)))
        for j in range(1,m):total=M.combine((1,total),(1,M.convolution(greens[m-j],forces.get(j,{}))))
        assert total==cur
        old,cur=cur,M.step(old,cur,forces.get(m,{}))
    # Exact polynomial identity underlying the all-momentum group-speed bound.
    speed_checks=0
    for us in product((F(0),F(1,4),F(1,2),F(1)),repeat=3):
        U=sum((a*u for a,u in zip(M.alpha,us)),Z)
        S2=sum((a*u*u for a,u in zip(M.alpha,us)),Z)
        rhs=(1-M.total)*S2+sum((M.alpha[i]*M.alpha[j]*(us[i]-us[j])**2 for i in range(3) for j in range(i+1,3)),Z)
        assert S2-U*U==rhs and M.sign(rhs)>=0
        assert 4*U*(1-U)-4*(U-S2)==4*rhs
        speed_checks+=1
    # Central difference moment certificates: first odd terms cancel.
    assert sum(((-1)**k for k in (0,1)),0)==0
    for degree in range(5):
        moment=sum((weight*F(offset)**degree for offset,weight in ((-1,1),(0,-2),(1,1))),F(0))
        assert moment=={0:F(0),1:F(0),2:F(2),3:F(0),4:F(2)}[degree]
    # A nonzero one-hop scalar response is not microscopic Lorentz support.
    impulse={(0,0,0):O}; after=M.step({},impulse)
    assert after[(1,0,0)]==M.alpha[0]
    n=8
    x=M.event(n,1,(0,0,0)); y=M.event(n,2,(1,0,0))
    d=[b-a for a,b in zip(x,y)]
    assert M.sign(M.inner(d,d))>0 and M.sign(M.time(d))>0
    print('PASS G1: exact orthogonal Hodge frame and metric-derived positive weights')
    print('PASS G2: sum(alpha)=1/2+sqrt5/5<1; positive stability margin')
    print(f'PASS G3: {count} rounded integer events admitted and distinct; slice/time checks')
    print('PASS G4: sparse Cauchy evolution, reverse step, positive conserved energy and source work')
    print('PASS G5: independent periodic matrix/neighbor comparison; self-adjoint positivity bounds')
    print('PASS G6: retarded Green recursion, finite support and forced Duhamel identity')
    print(f'PASS G7: {speed_checks} exact group-speed polynomial controls and Taylor moments')
    print('PASS G8: rounded-event spacelike one-hop witness; no microscopic light-cone claim')
    print('NON-CANONICAL: selected scalar field on an event subcarrier; no native/physical photon closure')

if __name__=='__main__':main()
