#!/usr/bin/env python3
"""Scope breaker for the direct-record quotient candidate."""
from fractions import Fraction as F

# Density-only scale witness. G is positive and homogeneous, so rho(v)=rho(2v)
# while total weight and q differ. Use the public rational formulas directly.
G = tuple(tuple(F(int(i == j)) - F(1,5) for j in range(4)) for i in range(4))
def mmul(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))
def outer(v): return tuple(tuple(v[i]*v[j] for j in range(4)) for i in range(4))
def tr(a): return sum(a[i][i] for i in range(len(a)))
def rho(v):
    A=outer(v); AG=mmul(A,G); m=tr(AG)
    return tuple(tuple(x/m for x in row) for row in AG),m,A
r1,m1,a1=rho((F(1),F(0),F(0),F(0)))
r2,m2,a2=rho((F(2),F(0),F(0),F(0)))
assert r1==r2 and m2==4*m1 and a1!=a2
print("DENSITY_ONLY_QUOTIENT FALSIFIED_AS_COMPLETE expected")
print("rho(e0)=rho(2e0), m(2e0)=4m(e0), q(e0)!=q(2e0)")
print("FULL_RECORD_SCOPE survives")
