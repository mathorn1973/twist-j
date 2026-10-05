#!/usr/bin/env python3
"""Independent implementation companion for P-KERNEL-MIRROR-TRIANGLE-CENSUS-1.

Adapted from the supplied, previously computed NON-CANONICAL census breaker;
SOURCE.md records custody. This is a second code path, not an independent
experiment or author. It imports no formulas or routines from verify.py.

Coordinate permutations, cycle orders, orbit/stabilizer Schreier generators,
and the doubled action recompute the 21 census records. Faithful six-point
stabilizer frames rely on affinity, checked exhaustively before use. The
bounded word search is deliberately omitted; the all-word exclusion follows
from the order theorem, not a word-length sample. Exact standard library only.
Run verify.py as the single public entry point.
"""

from fractions import Fraction
from itertools import combinations
from math import gcd

Q = 5
DIM = 6
SIZE = Q ** DIM
C = (2, 1, 3, 4, 1, 1)
CE = (2, 1, 3, 4, 2, 1)


def L_a(x):
    return (x[1], x[0], x[3], x[2], x[4], x[5])


def L_b(x):
    return (-x[2], -x[3], -x[0], -x[1], -x[4], -x[5])


def L_c(x):
    return (2 - x[2], 1 + x[5] - x[3], 2 - x[0], 1 - x[5] - x[1],
            1 - x[4], -x[5])


def L_d(x):
    return tuple(C[i] - x[i] for i in range(DIM))


def L_e(x):
    return tuple(CE[i] - x[i] for i in range(DIM))


FORMULAS = {"a": L_a, "b": L_b, "c": L_c, "d": L_d, "e": L_e}


def enc(x):
    n = 0
    for i in range(DIM - 1, -1, -1):
        n = n * Q + (x[i] % Q)
    return n


def dec(n):
    x = []
    for _ in range(DIM):
        x.append(n % Q)
        n //= Q
    return tuple(x)


POINTS = None
PERM = None
ZERO = 0
UNITS = [Q ** i for i in range(DIM)]

def expect(name, cond):
    if not cond:
        raise RuntimeError("independent crosscheck: " + name)


def lcm(a, b):
    return a * b // gcd(a, b)


def perm_order(p):
    seen = bytearray(len(p))
    o = 1
    for s in range(len(p)):
        if not seen[s]:
            n, k = 0, s
            while not seen[k]:
                seen[k] = 1
                k = p[k]
                n += 1
            o = lcm(o, n)
    return o


def times(p, q):
    """p after q."""
    return [p[q[i]] for i in range(len(q))]


def group_order(perms, base, frame):
    """|<perms>| = |orbit of base| * |stabilizer of base|.

    perms: list of involutive permutations (lists). frame: points whose
    images determine an element that fixes base.
    """
    word = {base: ()}
    order = [base]
    i = 0
    while i < len(order):
        p = order[i]
        i += 1
        for gi, g in enumerate(perms):
            q = g[p]
            if q not in word:
                word[q] = word[p] + (gi,)
                order.append(q)

    def run(w, pt):
        for gi in w:
            pt = perms[gi][pt]
        return pt

    ident = tuple(frame)
    schreier = {}
    for p in order:
        wp = word[p]
        for gi, g in enumerate(perms):
            q = g[p]
            wq = word[q]
            if wq == wp + (gi,):
                continue                       # tree edge, trivial
            full = wp + (gi,) + tuple(reversed(wq))
            img = tuple(run(full, pt) for pt in frame)
            if img != ident and img not in schreier:
                schreier[img] = full
    gens = list(schreier.values())
    elems = {ident}
    stack = [ident]
    while stack:
        f = stack.pop()
        for w in gens:
            f2 = tuple(run(w, pt) for pt in f)
            if f2 not in elems:
                elems.add(f2)
                stack.append(f2)
    return len(order) * len(elems), len(order), len(elems)


def doubled(p):
    n = len(p)
    return [p[i] + n for i in range(n)] + [p[i] for i in range(n)]


def tri_type(l, m, n):
    if min(l, m, n) == 1:
        return "DEGENERATE"
    s = Fraction(1, l) + Fraction(1, m) + Fraction(1, n)
    twos = (l == 2) + (m == 2) + (n == 2)
    if s > 1:
        return "SPHERICAL-REDUCIBLE" if twos >= 2 else "SPHERICAL-PLATONIC"
    if s == 1:
        return "FLAT"
    return "HYPERBOLIC"


def compute_records():
    """Return exact records after checks; emit no stdout and write no files."""
    global POINTS, PERM
    POINTS = [dec(n) for n in range(SIZE)]
    PERM = {k: [enc(f(x)) for x in POINTS] for k, f in FORMULAS.items()}
    expect("every letter has exact order two",
           all(p != list(range(SIZE)) and all(p[p[i]] == i for i in range(SIZE))
               for p in PERM.values()))
    ok_add = True
    for p in PERM.values():
        g0 = POINTS[p[ZERO]]
        lin = [tuple((POINTS[p[n]][i] - g0[i]) % Q for i in range(DIM))
               for n in range(SIZE)]
        for n in range(SIZE):
            x = POINTS[n]
            for u in range(DIM):
                y = list(x)
                y[u] = (y[u] + 1) % Q
                total = tuple((lin[n][i] + lin[UNITS[u]][i]) % Q for i in range(DIM))
                if lin[enc(y)] != total:
                    ok_add = False
    expect("g(x)-g(0) is additive on all states", ok_add)
    expect("registered fired commutators agree as permutations",
           all(times(times(PERM[g], PERM[h]), times(PERM[g], PERM[h]))
               == [enc(tuple(POINTS[n][i] + w[i] for i in range(DIM)))
                   for n in range(SIZE)]
               for g, h, w in (("d", "e", (0, 0, 0, 0, 3, 0)),
                               ("b", "d", (0, 0, 0, 0, 3, 3)),
                               ("b", "e", (0, 0, 0, 0, 1, 3)))))
    pairs = {g+h: perm_order(times(PERM[g], PERM[h]))
             for g, h in combinations("abcde", 2)}
    triples = {}
    for g, h, k in combinations("abcde", 3):
        name = g+h+k
        l, m, n = pairs[g+h], pairs[g+k], pairs[h+k]
        typ = tri_type(l, m, n)
        expect(name + " is nondegenerate", typ != "DEGENERATE")
        perms = [PERM[g], PERM[h], PERM[k]]
        order, _, _ = group_order(perms, ZERO, UNITS)
        dbl, _, _ = group_order([doubled(p) for p in perms], ZERO, UNITS)
        excess = Fraction(1, l) + Fraction(1, m) + Fraction(1, n) - 1
        chi = Fraction(order, 2) * excess
        if dbl == order:
            orientable, genus = True, (2-chi)/2
        elif dbl == 2*order:
            orientable, genus = False, 2-chi
        else:
            raise RuntimeError("independent crosscheck: doubled order is inconsistent")
        expect(name + " chi and genus are valid integers",
               chi.denominator == 1 and genus.denominator == 1
               and genus >= (0 if orientable else 1))
        triples[name] = ((l, m, n), excess, typ, order, int(chi), orientable, int(genus))
    full = group_order([PERM[k] for k in "abcde"], ZERO, UNITS)
    return {"pairs": pairs, "triples": triples, "full": full}
