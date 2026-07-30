#!/usr/bin/env python3
"""P-FIRED-COMMUTATOR-NOGO-1: the commutator structure of the fired algebra.

On the recurrent sheet the selection law i = (z5 + 2 t) mod 5 fires only the
three involutions b, d, e of the public census kernel (MIRROR-ONLY leg of
probes/P-CENSUS-REPLAY-1). This probe computes, in exact integer arithmetic,
the group commutator structure of the fired algebra <b, d, e> on Z_5^6 and
its piston (spatial) content, and audits the accompanying elementary proof:

  the linear parts of b, d, e lie in the abelian Klein group {I, -I, B, -B},
  so every group commutator in <b, d, e> is a pure translation; the three
  generator pair commutators are fiber translations with zero piston
  component and generate the full fiber plane; conjugation by b, d, e
  preserves the fiber plane; hence the derived subgroup D(<b, d, e>) is
  exactly the 25 fiber translations, the fired dynamics is spatially
  abelian, and piston-block noncommutativity cannot arise from the fired
  steps. The silent pair a, c is the negative control: its commutator is
  not a translation.

Generator definitions are byte-matching probes/P-CENSUS-REPLAY-1/verify.py.
Python standard library only; exact integers; deterministic; no files
written; no floats anywhere.
"""

import sys
from itertools import product

P = 5
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + t * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + t * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + t * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + t * U_VEC[3]) % 5,
            (1 - q) % 5, (-t) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = {"a": gen_a, "b": gen_b, "c": gen_c, "d": gen_d, "e": gen_e}
STATES = list(product(range(P), repeat=6))
IDMAT = tuple(tuple(1 if i == j else 0 for j in range(6)) for i in range(6))


def affine_of(f):
    v = f((0, 0, 0, 0, 0, 0))
    cols = []
    for j in range(6):
        e_j = tuple(1 if k == j else 0 for k in range(6))
        img = f(e_j)
        cols.append(tuple((img[i] - v[i]) % P for i in range(6)))
    M = tuple(tuple(cols[j][i] for j in range(6)) for i in range(6))
    return M, v


def mat_vec(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(6)) % P for i in range(6))


def mat_mul(M, N):
    return tuple(tuple(sum(M[i][k] * N[k][j] for k in range(6)) % P
                       for j in range(6)) for i in range(6))


def mat_neg(M):
    return tuple(tuple((-M[i][j]) % P for j in range(6)) for i in range(6))


def aff_apply(F, x):
    M, v = F
    y = mat_vec(M, x)
    return tuple((y[i] + v[i]) % P for i in range(6))


def aff_compose(F, G):
    M, u = F
    N, w = G
    Mw = mat_vec(M, w)
    return (mat_mul(M, N), tuple((Mw[i] + u[i]) % P for i in range(6)))


def word_form(word, forms):
    F = (IDMAT, (0, 0, 0, 0, 0, 0))
    for letter in word:
        F = aff_compose(F, forms[letter])
    return F


def main():
    CHECKS = []

    def check(name, ok):
        CHECKS.append((name, bool(ok)))

    forms = {k: affine_of(f) for k, f in GENS.items()}

    # 01 involutions and affine faithfulness
    ok = True
    for k, f in GENS.items():
        F = forms[k]
        for x in STATES:
            if f(f(x)) != x or aff_apply(F, x) != f(x):
                ok = False
                break
        if not ok:
            break
    check("INVOLUTIONS-AFFINE  the five census maps are involutions and"
          " equal their affine forms on all 15625 states", ok)

    # 02 the sheet fires only b, d, e
    ok = True
    for x in STATES:
        z5 = sum(x) % P
        if z5 in (1, 4):
            for t in (0, 1):
                if (z5 + 2 * t) % P not in (1, 3, 4):
                    ok = False
    check("SHEET-FIRED         on the sheet z5 in {1, 4} the selector takes"
          " only {1, 3, 4}: a and c never fire", ok)

    # 03, 04, 05 the three pair commutators, exhaustive
    b, d, e = GENS["b"], GENS["d"], GENS["e"]
    w_de = (0, 0, 0, 0, 3, 0)
    w_bd = (0, 0, 0, 0, 3, 3)
    w_be = (0, 0, 0, 0, 1, 3)
    ok3 = ok4 = ok5 = True
    for x in STATES:
        if d(e(d(e(x)))) != tuple((x[i] + w_de[i]) % P for i in range(6)):
            ok3 = False
        if b(d(b(d(x)))) != tuple((x[i] + w_bd[i]) % P for i in range(6)):
            ok4 = False
        if b(e(b(e(x)))) != tuple((x[i] + w_be[i]) % P for i in range(6)):
            ok5 = False
    check("COMM-DE             [d,e] = T_(0,0,0,0,3,0) on all 15625 states;"
          " piston zero", ok3 and w_de[:4] == (0, 0, 0, 0))
    check("COMM-BD             [b,d] = T_(0,0,0,0,3,3) on all 15625 states;"
          " piston zero", ok4 and w_bd[:4] == (0, 0, 0, 0))
    check("COMM-BE             [b,e] = T_(0,0,0,0,1,3) on all 15625 states;"
          " piston zero", ok5 and w_be[:4] == (0, 0, 0, 0))

    # 06 the mechanism: b linear, mirror centers b-fixed, fiber preserved
    Bmat, bv = forms["b"]
    Bc_d = mat_vec(Bmat, C_D)
    e_q = (0, 0, 0, 0, 1, 0)
    e_t = (0, 0, 0, 0, 0, 1)
    ok = (bv == (0, 0, 0, 0, 0, 0)
          and Bc_d[:4] == C_D[:4] == (2, 1, 3, 4)
          and mat_vec(Bmat, e_q)[:4] == (0, 0, 0, 0)
          and mat_vec(Bmat, e_t)[:4] == (0, 0, 0, 0))
    check("MECHANISM           b is linear; piston(B c_d) = piston(c_d) ="
          " (2,1,3,4); B preserves the fiber plane", ok)

    # 07 the linear parts form the abelian Klein group of exponent 2
    negI = mat_neg(IDMAT)
    ok = (forms["d"][0] == negI and forms["e"][0] == negI)
    klein = [IDMAT, negI, Bmat, mat_neg(Bmat)]
    for M in klein:
        if mat_mul(M, M) != IDMAT:
            ok = False
        for N in klein:
            MN = mat_mul(M, N)
            if MN != mat_mul(N, M) or MN not in klein:
                ok = False
    check("LINEAR-KLEIN        linear parts (B, -I, -I); the set"
          " {I, -I, B, -B} is closed, abelian, exponent 2", ok)

    # 08 the word sweep: all pairs of words up to length 3 over {b, d, e}
    letters = ("b", "d", "e")
    words = [(l1,) for l1 in letters]
    words += [(l1, l2) for l1 in letters for l2 in letters]
    words += [(l1, l2, l3) for l1 in letters for l2 in letters
              for l3 in letters]
    ok = True
    pairs = 0
    for wg in words:
        Fg = word_form(wg, forms)
        Fg_inv = word_form(tuple(reversed(wg)), forms)
        for wh in words:
            Fh = word_form(wh, forms)
            Fh_inv = word_form(tuple(reversed(wh)), forms)
            Fc = aff_compose(aff_compose(Fg, Fh),
                             aff_compose(Fg_inv, Fh_inv))
            Mc, vc = Fc
            if Mc != IDMAT or vc[:4] != (0, 0, 0, 0):
                ok = False
            pairs += 1
    check("WORD-SWEEP          all %d ordered pairs of words up to length 3:"
          " every commutator is a translation with zero piston"
          % pairs, ok and pairs == 39 * 39)

    # 09 the derived subgroup is exactly the fiber plane
    seeds = {w_de[4:], w_bd[4:], w_be[4:]}
    plane = set(seeds)
    while True:
        new = {((a1 + b1) % P, (a2 + b2) % P)
               for (a1, a2) in plane for (b1, b2) in plane}
        if new <= plane:
            break
        plane |= new
    full = {(qv, tv) for qv in range(P) for tv in range(P)}
    fq = mat_vec(Bmat, e_q)[4:]
    ft = mat_vec(Bmat, e_t)[4:]
    ok = (plane == full and fq in full and ft in full)
    check("DERIVED-PLANE       the three commutator vectors generate the"
          " full 25-element fiber plane; with 07 and 08,"
          " D(<b,d,e>) = the fiber translations exactly", ok)

    # 10 the silent control: [a, c] is not a translation
    a, c = GENS["a"], GENS["c"]
    disps = set()
    for x in STATES:
        y = a(c(a(c(x))))
        disps.add(tuple((y[i] - x[i]) % P for i in range(6)))
    check("SILENT-CONTROL      [a,c] is not a translation: %d distinct"
          " displacements; the fired-set restriction is essential"
          % len(disps), len(disps) > 1)

    print("TWIST-J fired-commutator no-go witness (exact integer arithmetic"
          " on Z_5^6)")
    print("the five public census involutions; on the recurrent sheet the"
          " selection law")
    print("i = (z5 + 2 t) mod 5 fires only b, d, e; this probe computes the"
          " commutator")
    print("structure of the fired algebra <b, d, e> and its piston content")
    print()
    passed = 0
    for i, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
