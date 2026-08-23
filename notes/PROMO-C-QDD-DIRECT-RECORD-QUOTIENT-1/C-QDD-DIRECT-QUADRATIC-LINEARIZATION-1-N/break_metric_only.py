#!/usr/bin/env python3
"""Scope breaker: the total metric alone does not select the LOW/HIGH split."""

from fractions import Fraction as F


def eye(n):
    return tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))


def outer(v, w):
    return tuple(tuple(v[i] * w[j] for j in range(len(w))) for i in range(len(v)))


def mmul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))) for i in range(len(a)))


def msub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def mscale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def mt(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def mv(a, v):
    return tuple(sum((a[i][j] * v[j] for j in range(len(v))), F(0)) for i in range(len(a)))


def dot(v, w):
    return sum((x * y for x, y in zip(v, w)), F(0))


def projector(u, g):
    gu = mv(g, u)
    den = dot(u, gu)
    # E(x)=u (u^T G x)/(u^T G u)
    return mscale(F(1, 1) / den, outer(u, gu))


def main():
    one = (F(1),) * 4
    j = outer(one, one)
    g = msub(eye(4), mscale(F(1, 5), j))
    e_public = mscale(F(1, 4), j)
    e_alt = projector((F(1), F(0), F(0), F(0)), g)
    assert e_alt != e_public
    assert mmul(e_alt, e_alt) == e_alt
    assert mmul(mt(e_alt), g) == mmul(g, e_alt)
    print("METRIC_ONLY_PROJECTOR_NONSELECTION FIRED expected")
    print("public_line=span(1,1,1,1)")
    print("alternative_line=span(1,0,0,0)")
    print("both_rank_one_idempotent_and_G_self_adjoint=1")
    print("VERDICT direct LOW subrecord is necessary for effect recovery")


if __name__ == "__main__":
    main()
