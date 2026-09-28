#!/usr/bin/env python3
"""Exact rational part of the native-cover / Hodge spatial metric seam."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import permutations

Vector=tuple[F,F,F]
Matrix=tuple[tuple[F,F,F],tuple[F,F,F],tuple[F,F,F]]
D=(F(1),F(1),F(1))
STEPS=((1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1))


def plane_section(x:int|F,y:int|F)->Vector:
    x,y=F(x),F(y)
    return ((2*x-y)/3,(-x+2*y)/3,(-x-y)/3)


def qA(x:int|F,y:int|F)->F:
    x,y=F(x),F(y)
    return x*x+y*y-x*y


def identity()->Matrix:
    return tuple(tuple(F(int(i==j)) for j in range(3)) for i in range(3))  # type: ignore


def ones()->Matrix:
    return tuple(tuple(F(1) for _ in range(3)) for __ in range(3))  # type: ignore


def madd(a:Matrix,b:Matrix)->Matrix:
    return tuple(tuple(a[i][j]+b[i][j] for j in range(3)) for i in range(3))  # type: ignore


def mscale(c:F,a:Matrix)->Matrix:
    return tuple(tuple(c*a[i][j] for j in range(3)) for i in range(3))  # type: ignore


def qform(q:Matrix,v:Vector,w:Vector|None=None)->F:
    w=v if w is None else w
    return sum((v[i]*q[i][j]*w[j] for i in range(3) for j in range(3)),F(0))


def q_rho(rho:F|int)->Matrix:
    rho=F(rho)
    if rho<=0:
        raise ValueError('rho must be positive')
    return madd(mscale(F(3,2),identity()),
                mscale(rho/F(9)-F(1,2),ones()))


def hodge_spatial_normalized()->Matrix:
    return q_rho(F(45,4))


def euclidean_control_normalized()->Matrix:
    return q_rho(F(9,2))


def perm_matrix(p:tuple[int,int,int])->Matrix:
    return tuple(tuple(F(int(i==p[j])) for j in range(3)) for i in range(3))  # type: ignore


def all_permutation_matrices()->tuple[Matrix,...]:
    return tuple(perm_matrix(p) for p in permutations(range(3)))


TIME_NORM=(F(15,16),F(3,8))  # 15/16 + (3/8)sqrt(5)
