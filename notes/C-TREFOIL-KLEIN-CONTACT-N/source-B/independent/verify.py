#!/usr/bin/env python3
"""Independent exact certificates for the frozen contact/geometry contracts.

Author: independent reviewer / contact_scope_refresh, 2026-10-17.
Preregistration: 5061341dd53c3814ef87293b4a5d361600b123f53ac1892bd25005bb46b5640f.
No author verifier or author output was read while preparing this source.
Standard library only; no input files, network, randomness, or wall clock.
Scientific execution is forbidden until the shared implementation freeze.
"""

import itertools
import json
import sys


class AuditFailure(Exception):
    pass


class Audit:
    def __init__(self):
        self.counts = {}
        self.certificates = {}

    def check(self, group, name, condition):
        self.counts[group] = self.counts.get(group, 0) + 1
        if not condition:
            raise AuditFailure(group + ":" + name)


# Literal operations, transcribed from the primary native definitions.
READ = ((0, 2, 1, 3, 4), (0, 1, 2, 3, 4), (2, 1, 0, 3, 4),
        (1, 0, 2, 3, 4), (1, 0, 2, 3, 4))


def native(letter, x):
    p0, p1, p2, p3, q, r = x
    if letter == "a":
        y = (p1, p0, p3, p2, q, r)
    elif letter == "b":
        y = (-p2, -p3, -p0, -p1, -q, -r)
    elif letter == "c":
        y = (2-p2, 1+r-p3, 2-p0, 1-r-p1, 1-q, -r)
    elif letter == "d":
        y = (2-p0, 1-p1, 3-p2, 4-p3, 1-q, 1-r)
    elif letter == "e":
        y = (2-p0, 1-p1, 3-p2, 4-p3, 2-q, 1-r)
    else:
        raise ValueError("unknown native letter")
    return tuple(t % 5 for t in y)


def ucal(x):
    return x[:5] + (READ[x[4]][x[5]],)


def mixed(x, y):
    return (3 * (x[0]*y[3] + x[3]*y[0] - x[1]*y[2] - x[2]*y[1])) % 5


def word_leaf(state, name, slot=None):
    x, y, bit = state
    if name == "W":
        h = mixed(x, y)
        if h == 0:
            return state
        side = int(h in (3, 4))
        if bit != side:
            x, y = native("b", x), native("b", y)
        return x, y, side
    transform = ucal if name == "Ucal" else lambda z: native(name, z)
    if slot == 0:
        return transform(x), y, bit
    return x, transform(y), bit


def literal_contact(slot, state):
    leaves = (("Ucal", slot), ("e", slot), ("d", slot), ("W", None),
              ("b", 0), ("b", 1), ("W", None), ("d", slot),
              ("e", slot), ("W", None), ("b", 1), ("b", 0),
              ("W", None), ("Ucal", slot))
    for name, at in leaves:
        state = word_leaf(state, name, at)
    return state


def reader_table(delta, slot, qr):
    values = list(qr)
    q, r = qr[slot], qr[slot+2]
    newq = (q + 3*delta) % 5
    values[slot] = newq
    values[slot+2] = READ[newq][READ[q][r]]
    return tuple(values)


def conjugator(qr):
    return qr[:2] + (READ[qr[0]][qr[2]], READ[qr[1]][qr[3]])


def translation(delta, slot, qr):
    values = list(qr)
    values[slot] = (values[slot] + 3*delta) % 5
    return tuple(values)


def perm_product(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def imat(rows):
    return tuple(tuple(x % 5 for x in row) for row in rows)


def imul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) % 5
                       for j in range(len(b[0]))) for i in range(len(a)))


def iidentity(n):
    return imat([[int(i == j) for j in range(n)] for i in range(n)])


def ipower(a, n):
    value = iidentity(len(a))
    for unused in range(n):
        value = imul(value, a)
    return value


def iact(a, v):
    return tuple(sum(row[k]*v[k] for k in range(len(v))) % 5 for row in a)


def contact_certificates(audit):
    zero6 = (0,)*6
    affine_basis = [zero6] + [tuple(int(i == k) for i in range(6)) for k in range(6)]
    for letter in "abcde":
        for number, x in enumerate(affine_basis):
            audit.check("C0", "native-involution-" + letter + str(number),
                        native(letter, native(letter, x)) == x)
    audit.check("C0", "ucal-five-permutations",
                all(sorted(row) == list(range(5)) for row in READ))
    audit.check("C0", "ucal-five-involutions",
                all(perm_product(row, row) == tuple(range(5)) for row in READ))

    rows_c1 = 0
    for delta in (0, 1):
        for qr in itertools.product(range(5), repeat=4):
            rows_c1 += 1
            for slot in (0, 1):
                out = qr
                for unused in range(5):
                    out = reader_table(delta, slot, out)
                audit.check("C1", "fifth-power", out == qr)
                audit.check("C1", "common-conjugation",
                            reader_table(delta, slot, qr) ==
                            conjugator(translation(delta, slot, conjugator(qr))))
            audit.check("C1", "commutation",
                        reader_table(delta, 0, reader_table(delta, 1, qr)) ==
                        reader_table(delta, 1, reader_table(delta, 0, qr)))

    state0 = ((0, 1, 0, 0, 0, 0), (1, 0, 0, 1, 0, 0), 0)
    xyx = literal_contact(0, literal_contact(1, literal_contact(0, state0)))
    yxy = literal_contact(1, literal_contact(0, literal_contact(1, state0)))
    expect_x = ((0, 1, 0, 0, 1, 0), (1, 0, 0, 1, 3, 1), 0)
    expect_y = ((0, 1, 0, 0, 3, 1), (1, 0, 0, 1, 1, 0), 0)
    audit.check("C1", "literal-xyx", xyx == expect_x)
    audit.check("C1", "literal-yxy", yxy == expect_y)
    audit.check("C1", "expected-braid-obstruction", xyx != yxy)
    audit.certificates["C1"] = {"complete_qr_rows": rows_c1,
                                "literal_xyx": xyx, "literal_yxy": yxy,
                                "group_by_conjugation_and_translation_proof": "C5 x C5"}

    expected_n = ((0, 4, 2, 3, 1), (0, 1, 2, 3, 4), (4, 1, 2, 3, 0),
                  (1, 0, 2, 3, 4), (1, 0, 2, 3, 4))
    piston_basis = [(0,)*4] + [tuple(int(i == k) for i in range(4)) for k in range(4)]
    mtab, ntab = [], []
    for q, r in itertools.product(range(5), repeat=2):
        for p in piston_basis:
            x = p + (q, r)
            mx = ucal(x)
            nx = native("e", ucal(native("e", x)))
            audit.check("C2", "complete-M", mx == p + (q, READ[q][r]))
            audit.check("C2", "complete-N", nx == p + (q, expected_n[q][r]))
        mtab.append(q*5 + READ[q][r])
        ntab.append(q*5 + expected_n[q][r])
    mtab, ntab = tuple(mtab), tuple(ntab)
    identity = tuple(range(25))
    mn = perm_product(mtab, ntab)
    nm = perm_product(ntab, mtab)
    mnm = perm_product(mtab, nm)
    audit.check("C2", "M2", perm_product(mtab, mtab) == identity)
    audit.check("C2", "N2", perm_product(ntab, ntab) == identity)
    audit.check("C2", "braid", mnm == perm_product(ntab, mn))
    audit.check("C2", "MN3", perm_product(mn, perm_product(mn, mn)) == identity)
    audit.check("C2", "order-three-witness", mn[1] == 4)
    audit.check("C2", "different-meridians", mtab[2] == 1 and ntab[2] == 2)
    six = (identity, mtab, ntab, mn, nm, mnm)
    audit.check("C2", "six-distinct", len(set(six)) == 6)
    for left in six:
        for right in six:
            audit.check("C2", "six-closure", perm_product(left, right) in six)
    audit.certificates["C2"] = {"group": "S3", "meridian_order": 2,
                                "all_occupied_r": True, "piston_probe_rows": 125,
                                "M": READ, "N": expected_n, "Ucal": "SUPPLIED"}

    colswap = imat(((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)))
    negrowswap = imat(((0, 0, -1, 0), (0, 0, 0, -1), (-1, 0, 0, 0), (0, -1, 0, 0)))
    minus = imat([[-int(i == j) for j in range(4)] for i in range(4)])
    parts = {"a": colswap, "b": negrowswap, "c": negrowswap,
             "d": minus, "e": minus, "Ucal": iidentity(4)}
    qr_epsilon_c = {"a": (1, 0), "b": (-1, 0), "c": (-1, 1),
                    "d": (-1, 1), "e": (-1, 2), "Ucal": (1, 0)}
    rows_c3 = 0
    for name in ("a", "b", "c", "d", "e", "Ucal"):
        eps, shift = qr_epsilon_c[name]
        for q, r in itertools.product(range(5), repeat=2):
            if name == "c":
                offset = (2, 1+r, 2, 1-r)
            elif name in ("d", "e"):
                offset = (2, 1, 3, 4)
            else:
                offset = (0, 0, 0, 0)
            newr = READ[q][r] if name == "Ucal" else (
                r if name == "a" else -r if name in ("b", "c") else 1-r)
            for p in piston_basis:
                rows_c3 += 1
                literal = ucal(p+(q, r)) if name == "Ucal" else native(name, p+(q, r))
                predicted_p = tuple((v+t) % 5 for v, t in zip(iact(parts[name], p), offset))
                predicted = predicted_p + ((eps*q+shift) % 5, newr % 5)
                audit.check("C3", "generator-triangular-form", literal == predicted)
    eight = tuple(imul(imul(ipower(colswap, i), ipower(negrowswap, j)), ipower(minus, k))
                  for i, j, k in itertools.product((0, 1), repeat=3))
    audit.check("C3", "eight-distinct-L", len(set(eight)) == 8)
    for left in eight:
        audit.check("C3", "L-involution", imul(left, left) == iidentity(4))
        for right in eight:
            audit.check("C3", "L-commutation", imul(left, right) == imul(right, left))
            audit.check("C3", "L-closure", imul(left, right) in eight)

    diag = imat(((2, 0), (0, 3)))
    diaginv = imat(((3, 0), (0, 2)))
    for t in range(5):
        for lower in (False, True):
            elementary = imat(((1, 0), (t, 1))) if lower else imat(((1, t), (0, 1)))
            inverse = imat(((1, 0), (-t, 1))) if lower else imat(((1, -t), (0, 1)))
            expected = imat(((1, 0), (3*t, 1))) if lower else imat(((1, 3*t), (0, 1)))
            audit.check("C3", "perfectness-commutator",
                        imul(imul(imul(diag, elementary), diaginv), inverse) == expected)
    even = []
    for p in itertools.permutations(range(5)):
        inversions = sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5))
        if inversions % 2 == 0:
            even.append(p)
    double = (1, 0, 3, 2, 4)
    centralizer = {p for p in even if perm_product(p, double) == perm_product(double, p)}
    expected_v4 = {tuple(range(5)), double, (2, 3, 0, 1, 4), (3, 2, 1, 0, 4)}
    audit.check("C3", "A5-census-for-centralizer", len(even) == 60)
    audit.check("C3", "double-transposition-centralizer", centralizer == expected_v4)
    for p in sorted(centralizer):
        for q in sorted(centralizer):
            audit.check("C3", "centralizer-abelian", perm_product(p, q) == perm_product(q, p))
    audit.certificates["C3"] = {"triangular_generator_rows": rows_c3,
                                "piston_linear_group_order": 8,
                                "centralizer": sorted(centralizer),
                                "all_homomorphisms_center_killed": "ANALYTICAL_PROOF",
                                "Gamma_plus_order": "NOT_COMPUTED"}

    def chi(x):
        return sum(x) % 5, x[5]

    def factor(letter, zr):
        z, r = zr
        formulas = {"a": (z, r), "b": (-z, -r), "c": (2-z, -r),
                    "d": (2-z, 1-r), "e": (3-z, 1-r)}
        return tuple(t % 5 for t in formulas[letter])

    for letter in "abcde":
        for x in affine_basis:
            audit.check("C4", "affine-chi-factor", chi(native(letter, x)) == factor(letter, chi(x)))
    x0, x2 = (0, 0, 0, 0, 0, 0), (3, 0, 0, 0, 2, 0)
    audit.check("C4", "same-chi", chi(x0) == chi(x2) == (0, 0))
    audit.check("C4", "ucal-separates", ucal(x0)[5] == 0 and ucal(x2)[5] == 2)
    audit.certificates["C4"] = {"affine_factor_rows": 35,
                                "witness": [x0, x2],
                                "ucal_outputs": [ucal(x0), ucal(x2)],
                                "all_time_conclusion": "INDUCTION_NOT_TIME_SAMPLING"}


# Independent cyclotomic representation: cyclic coefficient vectors of length 5,
# normalized by subtracting the last coefficient times (1,1,1,1,1).
# Multiplication first uses Z[C5], then this canonical quotient.
def k(value):
    if isinstance(value, int):
        return (value, 0, 0, 0, 0)
    last = value[4]
    return tuple(c-last for c in value)


KZERO, KONE = k(0), k(1)


def kadd(a, b):
    return k(tuple(x+y for x, y in zip(a, b)))


def kneg(a):
    return tuple(-x for x in a)


def ksub(a, b):
    return kadd(a, kneg(b))


def kmul(a, b):
    out = [0]*5
    for i in range(5):
        for j in range(5):
            out[(i+j) % 5] += a[i]*b[j]
    return k(tuple(out))


def kpow(a, exponent):
    result = KONE
    for unused in range(exponent):
        result = kmul(result, a)
    return result


def ksum(values):
    out = KZERO
    for value in values:
        out = kadd(out, value)
    return out


def sigma3(value):
    out = [0]*5
    for i, coefficient in enumerate(value):
        out[(3*i) % 5] += coefficient
    return k(tuple(out))


def mat(rows):
    return tuple(tuple(k(x) for x in row) for row in rows)


KI = mat(((1, 0), (0, 1)))


def mmul(a, b):
    return tuple(tuple(ksum(kmul(a[i][n], b[n][j]) for n in range(2))
                       for j in range(2)) for i in range(2))


def madd(a, b):
    return tuple(tuple(kadd(a[i][j], b[i][j]) for j in range(2)) for i in range(2))


def mscale(scalar, a):
    return tuple(tuple(kmul(scalar, value) for value in row) for row in a)


def msub(a, b):
    return madd(a, mscale(k(-1), b))


def mpow(a, n):
    value = KI
    for unused in range(n):
        value = mmul(value, a)
    return value


def mdet(a):
    return ksub(kmul(a[0][0], a[1][1]), kmul(a[0][1], a[1][0]))


def mtrace(a):
    return kadd(a[0][0], a[1][1])


def msigma(a):
    return tuple(tuple(sigma3(value) for value in row) for row in a)


def characteristic(a):
    return KONE, kneg(mtrace(a)), mdet(a)


def padd(a, b):
    out = dict(a)
    for exponent, coefficient in b.items():
        new = kadd(out.get(exponent, KZERO), coefficient)
        if new == KZERO:
            out.pop(exponent, None)
        else:
            out[exponent] = new
    return out


def pscale(scalar, a):
    return {exponent: new for exponent, old in a.items()
            if (new := kmul(scalar, old)) != KZERO}


def pmul(a, b):
    out = {}
    for (i, j), av in a.items():
        for (l, m), bv in b.items():
            exponent = (i+l, j+m)
            new = kadd(out.get(exponent, KZERO), kmul(av, bv))
            if new == KZERO:
                out.pop(exponent, None)
            else:
                out[exponent] = new
    return out


def ppow(a, n):
    result = {(0, 0): KONE}
    for unused in range(n):
        result = pmul(result, a)
    return result


def substitute(poly, a):
    first = {e: c for e, c in (((1, 0), a[0][0]), ((0, 1), a[0][1])) if c != KZERO}
    second = {e: c for e, c in (((1, 0), a[1][0]), ((0, 1), a[1][1])) if c != KZERO}
    first_powers = [ppow(first, i) for i in range(13)]
    second_powers = [ppow(second, i) for i in range(13)]
    out = {}
    for (i, j), coefficient in poly.items():
        out = padd(out, pscale(coefficient, pmul(first_powers[i], second_powers[j])))
    return out


def reduction(a):
    return tuple(tuple(sum(value) % 5 for value in row) for row in a)


def geometry_certificates(audit):
    j = (0, 1, 0, 0, 0)
    jp = [kpow(j, i) for i in range(5)]
    a = kadd(jp[1], jp[4])
    s = ksub(jp[2], jp[3])
    S, Sinv = mat(((0, -1), (1, 0))), mat(((0, 1), (-1, 0)))
    A = mat(((j, 1), (0, jp[4])))
    B = mmul(mmul(S, A), Sinv)
    C, D = mpow(A, 2), mpow(B, 3)
    Q = mat(((a, 0), (kneg(s), 1)))
    Qinv = mat(((kadd(a, KONE), 0), (kmul(s, kadd(a, KONE)), 1)))
    R1, R2 = mscale(jp[3], C), mscale(jp[3], D)
    audit.check("F0", "j5", kpow(j, 5) == KONE)
    audit.check("F0", "cyclotomic", ksum(jp) == KZERO)
    audit.check("F0", "a2+a", kadd(kmul(a, a), a) == KONE)
    audit.check("F0", "s2", kmul(s, s) == ksub(a, k(2)))
    audit.check("F0", "a-unit", kmul(a, kadd(a, KONE)) == KONE)
    audit.check("F0", "other-trace", kadd(jp[2], jp[3]) == kneg(kadd(a, KONE)))
    audit.check("F0", "B-explicit", B == mat(((jp[4], 0), (-1, j))))

    false_det = mdet(msub(mscale(jp[3], A), KI))
    expected_false = ksum((k(2), kmul(k(2), j), jp[3]))
    audit.check("F1", "nonreflection-determinant", false_det == expected_false and false_det != KZERO)
    audit.check("F1", "original-trace", mtrace(A) == a)
    audit.check("F1", "changed-trace", mtrace(C) == kneg(kadd(a, KONE)) and mtrace(C) != a)
    audit.check("F1", "wrong-inertia-power", characteristic(mscale(j, A)) ==
                (KONE, kneg(kadd(KONE, jp[2])), jp[2]))
    audit.certificates["F1"] = {"expected_nonreflection_determinant": false_det,
                                "old_geometric_marking": "EXPECTED_NEGATIVE"}

    audit.check("F2", "C-explicit", C == mat(((jp[2], a), (0, jp[3]))))
    audit.check("F2", "D-explicit", D == mat(((jp[2], 0), (a, jp[3]))))
    audit.check("F2", "braid", mmul(mmul(C, D), C) == mmul(mmul(D, C), D))
    audit.check("F2", "different", C != D)
    for value in (C, D):
        audit.check("F2", "fifth-power", mpow(value, 5) == KI)
        audit.check("F2", "determinant", mdet(value) == KONE)
    CD = mmul(C, D)
    audit.check("F2", "product-trace", mtrace(CD) == KONE)
    audit.check("F2", "quadratic-product", madd(msub(mpow(CD, 2), CD), KI) == mscale(KZERO, KI))
    audit.check("F2", "central-cube", mpow(CD, 3) == mscale(k(-1), KI))
    audit.check("F2", "recover-A", mpow(C, 3) == A)
    audit.check("F2", "recover-B", mpow(D, 2) == B)
    difference = msub(CD, mmul(D, C))
    expected_diff = mat(((kmul(a, a), kneg(kmul(a, s))),
                         (kneg(kmul(a, s)), kneg(kmul(a, a)))))
    audit.check("F2", "irreducible-difference", difference == expected_diff)
    audit.check("F2", "irreducible-determinant", mdet(difference) == kmul(a, a) and kmul(a, a) != KZERO)

    audit.check("F3", "R1-explicit", R1 == mat(((1, kmul(jp[3], a)), (0, j))))
    audit.check("F3", "R2-explicit", R2 == mat(((1, 0), (kmul(jp[3], a), j))))
    for reflection in (R1, R2):
        audit.check("F3", "characteristic", characteristic(reflection) ==
                    (KONE, kneg(kadd(KONE, j)), j))
        audit.check("F3", "not-identity", reflection != KI)
        audit.check("F3", "fixed-line", mdet(msub(reflection, KI)) == KZERO)
        audit.check("F3", "determinant", mdet(reflection) == j)
        audit.check("F3", "fifth-power", mpow(reflection, 5) == KI)
    audit.check("F3", "braid", mmul(mmul(R1, R2), R1) == mmul(mmul(R2, R1), R2))
    product = mmul(R1, R2)
    audit.check("F3", "central-cube", mpow(product, 3) == mscale(kneg(jp[3]), KI))
    audit.check("F3", "central-sixth", mpow(product, 6) == mscale(j, KI))
    audit.check("F3", "recover-C", C == mscale(jp[2], R1))
    audit.check("F3", "recover-D", D == mscale(jp[2], R2))
    audit.certificates["F3"] = {"full_group_order": "600_BY_GENERATING_CERTIFICATES_AND_ACCEPTED_H_ORDER",
                                "H_order": "120_ACCEPTED_INPUT", "reflection_order": 5}

    audit.check("F4", "left-inverse", mmul(Q, Qinv) == KI)
    audit.check("F4", "right-inverse", mmul(Qinv, Q) == KI)
    audit.check("F4", "unit-determinant", mdet(Q) == a)
    audit.check("F4", "integral-inverse", all(isinstance(v, int) for matrix in (Q, Qinv)
                                               for row in matrix for item in row for v in item))
    audit.check("F4", "sigma-j", sigma3(j) == jp[3])
    for basis in jp[:4]:
        audit.check("F4", "sigma-fourth", sigma3(sigma3(sigma3(sigma3(basis)))) == basis)
    for original, target in ((A, C), (B, D), (mscale(j, A), R1), (mscale(j, B), R2)):
        audit.check("F4", "galois-conjugation", mmul(mmul(Q, msigma(original)), Qinv) == target)

    f0 = {(11, 1): KONE, (6, 6): k(11), (1, 11): k(-1)}
    f = substitute(f0, mat(((s, a), (0, 1))))
    audit.check("F5", "nonzero-polynomial", bool(f))
    audit.check("F5", "homogeneous-twelve", all(i+j0 == 12 for i, j0 in f))
    for value in (C, D):
        audit.check("F5", "H-invariance-coefficients", substitute(f, value) == f)
    for value in (R1, R2):
        audit.check("F5", "positive-character-coefficients", substitute(f, value) == pscale(j, f))
    audit.check("F5", "old-character-coefficients", substitute(f, mscale(j, A)) == pscale(jp[2], f))
    audit.check("F5", "weight-twenty", kpow(jp[3], 20) == KONE)
    audit.check("F5", "weight-thirty", kpow(jp[3], 30) == KONE)
    audit.check("F5", "weight-twelve", kpow(jp[3], 12) == j)
    audit.certificates["F5"] = {"degree": 12, "nonzero_monomials": len(f),
                                "polynomial_equality": "COEFFICIENTWISE",
                                "higher_invariant_forms": "ACCEPTED_INPUT_NOT_RECOMPUTED"}

    A0, B0 = imat(((1, 1), (0, 1))), imat(((1, 0), (-1, 1)))
    K0, K0inv = imat(((2, 0), (0, 1))), imat(((3, 0), (0, 1)))
    C0, D0 = imat(((1, 2), (0, 1))), imat(((1, 0), (2, 1)))
    audit.check("F6", "a-reduction", sum(a) % 5 == 2)
    audit.check("F6", "s-reduction", sum(s) % 5 == 0)
    audit.check("F6", "Q-reduction", reduction(Q) == K0)
    audit.check("F6", "Qinv-reduction", reduction(Qinv) == K0inv)
    audit.check("F6", "first-chain", reduction(C) == reduction(R1) == ipower(A0, 2) ==
                imul(imul(K0, A0), K0inv) == C0)
    audit.check("F6", "second-chain", reduction(D) == reduction(R2) == ipower(B0, 3) ==
                imul(imul(K0, B0), K0inv) == D0)
    audit.check("F6", "reduced-braid", imul(imul(C0, D0), C0) == imul(imul(D0, C0), D0))
    audit.check("F6", "reduced-center", ipower(imul(C0, D0), 3) == imat(((-1, 0), (0, -1))))
    audit.certificates["F6"] = {"quotient": "Z[j]/(1-j)=F5", "C": C0, "D": D0,
                                "K0": K0, "physical_permission": "NOT_INFERRED"}


def main():
    audit = Audit()
    report = {"schema": "twistj-contact-meridians-independent-1",
              "prereg_sha256": "5061341dd53c3814ef87293b4a5d361600b123f53ac1892bd25005bb46b5640f",
              "independence": "NEW_AUTHOR_CODE_AND_OUTPUTS_NOT_READ",
              "status": "PASS", "evidence_scope": "FINITE_EXACT_CERTIFICATES_PLUS_SEPARATE_PROOF_REVIEW"}
    returncode = 0
    try:
        contact_certificates(audit)
        geometry_certificates(audit)
    except Exception as error:
        report["status"] = "FAIL"
        report["failure"] = {"type": type(error).__name__, "detail": str(error)}
        returncode = 1
    report["checks"] = audit.counts
    report["certificates"] = audit.certificates
    print(json.dumps(report, sort_keys=True, separators=(",", ":"), ensure_ascii=True))
    return returncode


if __name__ == "__main__":
    sys.exit(main())
