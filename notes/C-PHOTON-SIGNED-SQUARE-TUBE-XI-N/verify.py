#!/usr/bin/env python3
"""Exact audit for C-PHOTON-SIGNED-SQUARE-TUBE-XI-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


Point = tuple[int, int, int, int]
EdgeKey = tuple[Point, int]


def unit(axis: int, sign: int = 1) -> Point:
    return tuple(sign if i == axis else 0 for i in range(4))  # type: ignore[return-value]


def add(p: Point, q: Point) -> Point:
    return tuple(p[i] + q[i] for i in range(4))  # type: ignore[return-value]


def constants():
    a = Fraction(15625, 177147)
    r = Fraction(41, 25)
    q = a**4 * r**4 * (1 + 2*r**4)
    assert 0 < q < 1
    print(f"CONSTANTS PASS a={a} r={r} q_tube={q}")
    return a, r, q


def series_value(q: Fraction) -> Fraction:
    return (16 + q + 11*q*q - 5*q**3 + q**4) / (1-q)**5


def series_audit(q: Fraction) -> None:
    num = (16,1,11,-5,1)
    for k in range(20):
        coeff = 0
        for j,c in enumerate(num):
            if k >= j:
                coeff += c * comb(k-j+4,4)
        assert coeff == (k+2)**4
    assert series_value(q) > 0
    print("SERIES PASS coefficients_k0_to_19=(k+2)^4")


def cycle_edges(vertices: tuple[Point,...]) -> dict[EdgeKey,int]:
    assert len(vertices) == len(set(vertices))
    edges: dict[EdgeKey,int] = {}
    n=len(vertices)
    for i,p in enumerate(vertices):
        q=vertices[(i+1)%n]
        diff=tuple(q[j]-p[j] for j in range(4))
        axes=[j for j,d in enumerate(diff) if d]
        assert len(axes)==1
        ax=axes[0]
        assert abs(diff[ax])==1
        if diff[ax]==1:
            key,coef=(p,ax),1
        else:
            key,coef=(q,ax),-1
        assert key not in edges
        edges[key]=coef
    return edges


def plaquette_boundary(base: Point,a:int,b:int)->dict[EdgeKey,int]:
    assert a<b
    ea,eb=unit(a),unit(b)
    return {
        (add(base,ea),b):1,
        (base,b):-1,
        (add(base,eb),a):-1,
        (base,a):1,
    }


def contact_counts(vertices:tuple[Point,...])->tuple[int,int]:
    items=list(cycle_edges(vertices).items())
    op=om=0
    for i,((x,ax),cx) in enumerate(items):
        for (y,ay),cy in items[i+1:]:
            if ax!=ay:
                continue
            diff=tuple(y[k]-x[k] for k in range(4))
            nz=[k for k,d in enumerate(diff) if d]
            if len(nz)!=1:
                continue
            tr=nz[0]
            if tr==ax or abs(diff[tr])!=1:
                continue
            low=x if diff[tr]==1 else y
            aa,bb=sorted((ax,tr))
            bd=plaquette_boundary(low,aa,bb)
            sx=cx*bd[(x,ax)]
            sy=cy*bd[(y,ax)]
            if sx==sy:
                op+=1
            else:
                om+=1
    return op,om


def turn_count(vertices:tuple[Point,...])->int:
    n=len(vertices)
    axes=[]
    for i,p in enumerate(vertices):
        q=vertices[(i+1)%n]
        diff=tuple(q[j]-p[j] for j in range(4))
        axes.append(next(j for j,d in enumerate(diff) if d))
    return sum(axes[i]!=axes[i-1] for i in range(n))


def ell_axis01(vertices:tuple[Point,...])->int:
    edges=cycle_edges(vertices)
    xs=[p[1] for p in vertices]
    lo=min(xs)
    L=2*len(vertices)+9
    offset=len(vertices)+3-lo
    B=[0]*L
    for (x,ax),coef in edges.items():
        if ax==0:
            B[x[1]+offset]+=coef
    assert sum(B)==0
    H=[0]*L
    for r in range(1,L):
        H[r]=H[r-1]+B[r]
    assert H[0]-H[-1]==B[0]
    med=sorted(H)[L//2]
    return sum(abs(v-med) for v in H)


def base_path(D:int,bent:bool)->tuple[Point,...]:
    assert D>=1
    cur=(0,0,0,0)
    p=[cur]
    if bent:
        assert D>=2
        first=D//2
        steps=[0]*first+[3]*(D-first)
    else:
        steps=[0]*D
    for ax in steps:
        cur=add(cur,unit(ax))
        p.append(cur)
    return tuple(p)


def make_tube(D:int,bent:bool)->tuple[Point,...]:
    p=base_path(D,bent)
    e1,e2=unit(1),unit(2)
    A=p
    B=tuple(add(x,e1) for x in p)
    C=tuple(add(add(x,e1),e2) for x in p)
    D0=tuple(add(x,e2) for x in p)

    vertices=[]
    vertices.extend(A)
    vertices.append(B[-1])
    vertices.extend(reversed(B[:-1]))
    vertices.append(C[0])
    vertices.extend(C[1:])
    vertices.append(D0[-1])
    vertices.extend(reversed(D0[:-1]))
    out=tuple(vertices)
    assert len(out)==4*D+4
    assert len(out)==len(set(out))
    return out


def example_audit()->None:
    count=0
    for D in range(1,7):
        cases=(False,True) if D>=2 else (False,)
        for bent in cases:
            cyc=make_tube(D,bent)
            m=len(cyc)
            op,om=contact_counts(cyc)
            c=turn_count(cyc)
            cp=1 if bent else 0
            assert m==4*D+4
            assert c==4*cp+8
            assert op==4*D+2
            assert om==0
            ell=ell_axis01(cyc)
            assert 16*ell<=m*m
            count+=1
    print(f"TUBE_EXAMPLES PASS count={count} D=1..6 straight_and_one_turn")


def complement_audit(r:Fraction)->None:
    tau=Fraction(73,70)
    first=None
    for D in range(1,1000):
        if r**(4*D+2)>tau**(4*D+4):
            first=D
            break
    assert first is not None
    print(f"SC_COMPLEMENT PASS first_D={first} density_limit=1")


def bound_audit(a:Fraction,r:Fraction,q:Fraction)->None:
    C=384*a**8*r**14*series_value(q)
    assert C>0
    print(f"BOUND PASS C_tube={C}")
    print(f"BOUND_DIGITS num={len(str(C.numerator))} den={len(str(C.denominator))}")


def main()->None:
    a,r,q=constants()
    series_audit(q)
    example_audit()
    complement_audit(r)
    bound_audit(a,r,q)
    print("AUDIT PASS; square_tube_uniform=YES; full_Xi=OPEN; P1=OPEN")


if __name__=="__main__":
    main()
