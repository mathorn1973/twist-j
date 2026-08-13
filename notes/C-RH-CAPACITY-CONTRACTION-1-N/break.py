#!/usr/bin/env python3
"""Exact finite breaker/audit for C-RH-CAPACITY-CONTRACTION-1-N.

This is NON-CANONICAL incubation code. It proves no infinite-dimensional
positivity statement and carries no RH status. It checks only algebraic gates
whose content is finite and exact.
"""
from fractions import Fraction as F


def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def quad(M,x):
    return sum(x[i]*M[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))


def norm2(v):
    return sum(x*x for x in v)


def test_local_inertia():
    # Normalized delayed bilinear block w[[0,-1],[-1,0]].
    M=[[F(0),F(-1)],[F(-1),F(0)]]
    assert det2(M)==F(-1)
    assert quad(M,[F(1),F(-1)])==F(2)   # positive direction
    assert quad(M,[F(1),F(1)])==F(-2)   # negative direction
    print("PASS G1-break: one delayed prime block has both signs; det=-1")


def test_schur_sign():
    # For positive diagonal B, -C B^-1 C^T is negative semidefinite.
    # Use a generic exact 2x3 rational witness and test a spanning set of x.
    C=[[F(1),F(2),F(-1)],[F(3),F(-2),F(4)]]
    Binv=[[F(1,2),F(0),F(0)],[F(0),F(1,3),F(0)],[F(0),F(0),F(1,5)]]
    S=matmul(matmul(C,Binv),transpose(C))
    S=[[-v for v in row] for row in S]
    for x in ([F(1),F(0)],[F(0),F(1)],[F(1),F(1)],[F(2),F(-3)]):
        assert quad(S,x)<=0
    assert det2(S)>=0 and S[0][0]<0 and S[1][1]<0
    print("PASS G2-break: positive-lower-block Schur correction is negative semidefinite")


def test_disjoint_cutoff_increment():
    # Exact discrete analogue of a newly admitted translation on the full
    # zero-extended carrier.  The old and translated supports are disjoint,
    # but translation preserves norm.  Therefore V- and V+ each acquire the
    # full diagonal mass w*||v||^2 (here w=1), not half that mass.
    v=[F(1),F(-2),F(3),F(1)]
    k=len(v)
    e0=v+[F(0)]*k
    ek=[F(0)]*k+v
    N=norm2(v)
    assert norm2(e0)==norm2(ek)==N
    assert sum(x*y for x,y in zip(e0,ek))==0
    minus=F(1,2)*norm2([x-y for x,y in zip(e0,ek)])
    plus =F(1,2)*norm2([x+y for x,y in zip(e0,ek)])
    assert minus==plus==N
    print("PASS G5-break: disjoint translated channel adds equal V-/V+ mass = ||v||^2")


def main():
    test_local_inertia()
    test_schur_sign()
    test_disjoint_cutoff_increment()
    print("ALL EXACT FINITE BREAKER GATES PASS; G3 UNIVERSAL POSITIVITY UNDECIDED")


if __name__ == "__main__":
    main()
