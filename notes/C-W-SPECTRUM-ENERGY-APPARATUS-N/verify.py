#!/usr/bin/env python3
"""Primary exact algebra audit; determinant by all permutations."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
import sys

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
E0 = (0, 0, 0)


def ga(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gm(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def mono(e=E0, re=0, im=0):
    c = (F(re), F(im))
    return {} if c == ZERO else {e: c}


def add(*args):
    out = {}
    for a in args:
        for e, c in a.items():
            out[e] = ga(out.get(e, ZERO), c)
            if out[e] == ZERO:
                del out[e]
    return out


def scale(a, re=1, im=0):
    q = (F(re), F(im))
    return {e: v for e, c in a.items() if (v := gm(q, c)) != ZERO}


def mul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            t = tuple(x + y for x, y in zip(e, f))
            out[t] = ga(out.get(t, ZERO), gm(c, d))
            if out[t] == ZERO:
                del out[t]
    return out


def conj(a):
    return {(e[0], -e[1], -e[2]): (c[0], -c[1])
            for e, c in a.items()}


def matmul(a, b):
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [[conj(a[j][i]) for j in range(len(a))]
            for i in range(len(a[0]))]


def ident(n):
    return [[mono(re=int(i == j)) for j in range(n)] for i in range(n)]


def det(a):
    n = len(a)
    out = {}
    for p in permutations(range(n)):
        term = mono(re=1)
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        for i in range(n):
            term = mul(term, a[i][p[i]])
        out = add(out, scale(term, (-1) ** inversions))
    return out


def scalar(a):
    assert set(a).issubset({E0}), a
    return a.get(E0, ZERO)


def main():
    assert len(sys.argv) == 2, "one certificate output pathname required"
    # Tensor factors formed first; no expected characteristic is used here.
    c = [[mono(re=1), mono(im=2)], [mono(im=2), mono(re=1)]]
    g = [[scale(mul(c[i//2][j//2], c[i%2][j%2]), F(1, 5))
          for j in range(4)] for i in range(4)]
    assert matmul(adj(g), g) == ident(4)
    dg = scalar(det(g))
    assert dg == ONE
    shifts = [(0, 1, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0)]
    wf = [[mul(mono(shifts[i], re=1), g[i][j])
           for j in range(4)] for i in range(4)]
    assert matmul(adj(wf), wf) == ident(4)
    lam = mono((1, 0, 0), re=1)
    characteristic = det([[add(lam if i == j else {}, scale(wf[i][j], -1))
                           for j in range(4)] for i in range(4)])
    zsum = add(mono((0, 1, 0), re=1), mono((0, -1, 0), re=1))
    wsum = add(mono((0, 0, 1), re=1), mono((0, 0, -1), re=1))
    ac = scale(add(zsum, wsum), F(1, 5))
    bc = scale(add(mul(zsum, wsum), mono(re=-6)), F(1, 5))
    expected = add(mono((4, 0, 0), re=1), mono(re=1),
                   scale(mul(ac, mono((3, 0, 0), re=1)), -1),
                   mul(bc, mono((2, 0, 0), re=1)), scale(mul(ac, lam), -1))
    assert characteristic == expected
    av = [[mono(re=x)] for x in (1, 0, 0, -1)]
    sv = [[mono(re=x)] for x in (1, 0, 0, 1)]
    assert matmul(g, av) == av
    sexp = scalar(matmul(adj(sv), matmul(g, sv))[0][0])
    snorm = scalar(matmul(adj(sv), sv)[0][0])
    assert sexp[1] == 0 and snorm == (F(2), F(0))
    sexp_value = sexp[0] / snorm[0]
    assert sexp_value == F(-3, 5)
    t = F(1, 2)
    cb = (1-t*t)/(1+t*t)
    sb = 2*t/(1+t*t)
    cd = -(cb*cb - sb*sb)
    threshold = 1 + 4*cd
    margin = 5 - threshold*threshold
    assert (cb, sb, cd) == (F(3, 5), F(4, 5), F(7, 25))
    assert threshold > 0 and margin == F(316, 625) and margin > 0
    beta_coeff = F(3, 20) * F(1, 4)
    data = {
        "schema": "w-spectrum-exact-v1",
        "coin_unitary": True,
        "coin_determinant": str(dg[0]),
        "free_symbol_unitary": True,
        "compact_rest_eigenvector": True,
        "s_coin_expectation": str(sexp_value),
        "characteristic": [[*e, str(c0), str(c1)]
                           for e, (c0, c1) in sorted(characteristic.items())],
        "gap": {"cos_b": str(cb), "sin_b": str(sb), "cos_delta": str(cd),
                "sqrt5_threshold": str(threshold), "squared_margin": str(margin),
                "strictly_positive": True},
        "beta_lower": {"rational_part": str(beta_coeff), "sqrt5_part": str(beta_coeff)},
    }
    out = Path(sys.argv[1])
    assert not out.exists(), "refusing to overwrite certificate"
    out.write_text(json.dumps(data, sort_keys=True, separators=(',', ':')) + '\n',
                   encoding='utf-8')
    print("PASS: exact full-symbol, coin, gap and coefficient identities")


if __name__ == '__main__':
    main()
