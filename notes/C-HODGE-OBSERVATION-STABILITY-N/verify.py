#!/usr/bin/env python3
"""Exact local audit of a scoped, non-canonical Hodge synthesis.

Standard library only. No physical interpretation is checked here.
"""
from fractions import Fraction as Q
from itertools import combinations


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def transpose(a):
    return [list(r) for r in zip(*a)]


def wedge(a):
    pairs = list(combinations(range(len(a)), 2))
    return [[a[i][k] * a[j][l] - a[i][l] * a[j][k]
             for k, l in pairs] for i, j in pairs]


def root_action(p):
    a = [[0] * 4 for _ in range(4)]
    for col, j in enumerate(range(1, 5)):
        if p[j]:
            a[p[j] - 1][col] += 1
        if p[0]:
            a[p[0] - 1][col] -= 1
    return a


# A quadratic field element is a pair (a,b), representing a+b*sqrt(5).
def fa(x, y):
    return (x[0] + y[0], x[1] + y[1])


def fm(x, y):
    return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def fs(c, x):
    return (c*x[0], c*x[1])


def dot(x, y):
    s = (Q(0), Q(0))
    for a, b in zip(x, y):
        s = fa(s, fm(a, b))
    return s


def main():
    h = [[1 + int(i == j) for j in range(4)] for i in range(4)]
    s = [[0] * 6 for _ in range(6)]
    for i, j, sign in [(0, 5, 1), (1, 4, -1), (2, 3, 1)]:
        s[i][j] = s[j][i] = sign
    g = wedge(h)
    k = mm(s, g)
    assert mm(k, k) == [[5*x for x in r] for r in eye(6)]
    c = root_action((1, 2, 3, 4, 0))
    l = wedge(add(eye(4), mm(c, c)))
    assert mm(mm(transpose(l), s), l) == s
    print('PASS marked integer Hodge identities and wedge preservation')

    chosen = None
    for idx in range(6):
        u = [int(i == idx) for i in range(6)]
        ku = mv(k, u)
        lu, klu = mv(l, u), mv(k, mv(l, u))
        lku, klku = mv(l, ku), mv(k, mv(l, ku))
        # P_+ L P_-u = (5Lu-KLKu + sqrt(5)*(KLu-LKu))/20.
        bn = [(5*lu[i] - klku[i], klu[i] - lku[i]) for i in range(6)]
        if any(a or b for a, b in bn):
            chosen = idx
            break
    assert chosen is not None
    print('PASS nonzero conjugate channel at integral basis index', chosen)
    print('CROSS_NUMERATOR_DENOMINATOR_20', bn)
    an = [(5*lu[i] + klku[i], klu[i] + lku[i]) for i in range(6)]

    a, b = 1, 0
    for n in range(33):
        assert a*a - 5*b*b == 1
        w = [a*u[i] - b*ku[i] for i in range(6)]
        kw, lw, klw = mv(k, w), mv(l, w), mv(k, mv(l, w))
        for i in range(6):
            # 10 P_+w = (a-b*sqrt(5)) (5u+sqrt(5)*Ku).
            assert (5*w[i], kw[i]) == fm((a, -b), (5*u[i], ku[i]))
            # 20 P_+Lw = (a-b*sqrt(5))*20A+(a+b*sqrt(5))*20B.
            rhs = fa(fm((a, -b), an[i]), fm((a, b), bn[i]))
            assert (10*lw[i], 2*klw[i]) == rhs
        a, b = 9*a + 20*b, 4*a + 9*b
    print('PASS Pell integral-source and output identities for n=0,...,32')
    print('LIMIT_STATUS proof only; finite checks do not prove convergence')

    zero, one = (Q(0), Q(0)), (Q(1), Q(0))
    p = [one, zero, zero]
    q = [(Q(0), Q(1, 5)), (Q(0), Q(2, 5)), zero]
    assert dot(p, p) == dot(q, q) == one
    pq = dot(p, q)
    assert fm(pq, pq) == (Q(1, 5), Q(0))
    w = [fa(q[i], fs(-1, fm(pq, p[i]))) for i in range(3)]
    assert dot(p, w) == zero
    assert dot(q, w) == (Q(4, 5), Q(0))
    print('PASS same-source atlas collision: pi_P(w)=0, pi_Q(w)=(4/5)t_Q')

    # Three normalized line vectors: Gram determinant 1-3/5 +/-2/(5sqrt5).
    for sign in (-1, 1):
        det = (Q(2, 5), Q(sign*2, 25))
        assert det[0] > 0 and det[0]**2 > 5*det[1]**2
    print('PASS both possible three-line Gram determinants are positive')
    print('RANK_CONSEQUENCE conditional on inherited atlas: 4,5,6')
    print('STATUS NON-CANONICAL candidate-C; one architecture; no physical gate')


if __name__ == '__main__':
    main()
