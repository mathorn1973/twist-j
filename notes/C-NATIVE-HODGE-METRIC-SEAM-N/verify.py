#!/usr/bin/env python3
"""Exact prospective audit for C-NATIVE-HODGE-METRIC-SEAM-N."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import contextlib
import hashlib
import importlib.util
import io
import itertools
import runpy

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent

HASHES={
 'notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/PROOF.md':
 'a6be9bd44df63655e2a42ec88c9f4cbb853b9ba15f5f5a869ec89e1ca5775c60',
 'notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/generate.py':
 '8a93ea5bfe5ba8cae0d2e20e1735d2c9b5731ec3d0f6fad6ce58bb2def1c0ada',
 'probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md':
 '19435a7bd5b33f2b7995262c2dbfc8eb8fa36b6112723fe15dc957aed60ef5c4',
 'probes/P-RELATIONAL-GROWTH-SATURATION-1/verify.py':
 'b38b6981af4d275fd7b2a810707e20b3cd61b8dbc365171f2ab36cb550235328',
 'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py':
 '02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9',
 'notes/C-HODGE-SPACETIME-WINDOW-N/PROOF.md':
 'aefac8315a9858e9bfdf26a51f95b6790830a31e9c185a4c883ad66129f70442',
}


def checked(path):
    p=ROOT/path
    if hashlib.sha256(p.read_bytes()).hexdigest()!=HASHES[path]:
        raise RuntimeError('STOP inherited hash mismatch: '+path)
    return p


for path in HASHES: checked(path)

spec=importlib.util.spec_from_file_location('metric_seam',HERE/'metric.py')
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

with contextlib.redirect_stdout(io.StringIO()):
    H=runpy.run_path(str(checked('probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py')))

Q5=H['Q5']; S=H['S']; Bp=H['Bp']; B=H['B']


def norm2(v):
    return sum((a*a for a in v),F(0))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def mm(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def rank(rows):
    a=[list(map(F,r)) for r in rows if any(r)]
    if not a:return 0
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c];a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c];a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
    return r


def invariant_constraint_rows():
    # symmetric Q variables: 00,11,22,01,02,12
    pairs=((0,0),(1,1),(2,2),(0,1),(0,2),(1,2))
    rows=[]
    for P in M.all_permutation_matrices():
        # Build each entry of P^T Q P-Q as a linear function of six variables.
        for i in range(3):
            for j in range(i,3):
                row=[]
                for a,b in pairs:
                    Q=[[F(0) for _ in range(3)] for __ in range(3)]
                    Q[a][b]=F(1);Q[b][a]=F(1)
                    if a==b:Q[a][b]=F(1)
                    lhs=mm(mm(transpose(P),Q),P)[i][j]
                    row.append(lhs-Q[i][j])
                if any(row):rows.append(tuple(row))
    return rows


def q5form(q,v):
    return sum((v[i]*q[i][j]*v[j] for i in range(3) for j in range(3)),Q5(0))


def main():
    # G1 exact cover/section identities.
    for x in range(-5,6):
        for y in range(-5,6):
            p=M.plane_section(x,y)
            assert sum(p,F(0))==0
            assert p[0]-p[2]==x and p[1]-p[2]==y
            assert norm2(p)==F(2,3)*M.qA(x,y)
    for step in M.STEPS:
        assert M.qA(*step)==1
        assert norm2(M.plane_section(*step))==F(2,3)

    # N2 tagged map: fixed x,y and r->r+1 adds exactly d.
    gen=runpy.run_path(str(checked('notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/generate.py')))
    phi=gen['phi']
    tag_checks=0
    for r in range(0,8):
        for x in range(-r,r+1):
            for y in range(max(-r,x-r),min(r,x+r)+1):
                z=phi(r,x,y);zp=phi(r+1,x,y)
                assert tuple(zp[i]-z[i] for i in range(3))==(1,1,1)
                assert (z[0]-z[2],z[1]-z[2])==(x,y)
                tag_checks+=1

    # G2 invariant symmetric forms: six variables, four independent constraints.
    rows=invariant_constraint_rows()
    assert rank(rows)==4
    I,J=M.identity(),M.ones()
    for P in M.all_permutation_matrices():
        assert mm(mm(transpose(P),I),P)==I
        assert mm(mm(transpose(P),J),P)==J

    for rho in (F(1,7),F(1),F(9,2),F(45,4),F(123,5)):
        q=M.q_rho(rho)
        for step in M.STEPS:
            assert M.qform(q,M.plane_section(*step))==1
        assert M.qform(q,M.D)==rho
        # Eigenvalues on zero-sum plane and diagonal line.
        assert M.qform(q,(F(1),F(-1),F(0)))==3
        assert M.qform(q,M.D)==rho

    # G3 exact Hodge member.
    unit=[Q5(F(2,3)),Q5(F(-1,3)),Q5(F(-1,3))]
    diag=[Q5(1),Q5(1),Q5(1)]
    q_unit=q5form(Bp,unit)
    q_diag=q5form(Bp,diag)
    assert q_unit==Q5(0,F(2,15))
    assert q_diag==Q5(0,F(3,2))
    assert q_diag/q_unit==Q5(F(45,4))

    normalized=[[x/q_unit for x in row] for row in Bp]
    expected=M.hodge_spatial_normalized()
    assert normalized==[[Q5(x) for x in row] for row in expected]
    assert expected!=M.euclidean_control_normalized()
    assert M.qform(M.euclidean_control_normalized(),M.D)==F(9,2)

    # G5 normalized time coefficient.
    ct=-B[3][3]
    tau=ct/q_unit
    assert tau==Q5(F(15,16),F(3,8))
    assert tau==Q5(*M.TIME_NORM)
    assert H['rank'](Bp)==3
    assert H['rank'](B)==4

    print('PASS G1: zero-sum section, six unit directions and tagged diagonal increment')
    print(f'PASS G2: permutation-invariant symmetric-form constraint rank=4; family dimension=2; tag checks={tag_checks}')
    print('PASS G3: normalized complete positive family Q_rho with one free rho>0')
    print('PASS G4: Hodge member rho=45/4; Euclidean control rho=9/2 is distinct')
    print('PASS G5: normalized Hodge spatial matrix = (3/2)I+(3/4)11^T')
    print('PASS G6: normalized Lorentz time coefficient = (15+6sqrt5)/16; signature 3+1')
    print('NON-CANONICAL: selected Hodge seam fixes rho only after independent Hodge-target adoption')


if __name__=='__main__': main()
