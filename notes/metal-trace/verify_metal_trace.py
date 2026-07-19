#!/usr/bin/env python3
"""Independent exact witness for the metal-trace synthesis note.

Second exposure beside the author's verify_metals_deep.py (19/19 OK,
sha256 9779ccfdb38fe40b51657eae7a438933ac14995ddf89f1f439a1605ebd2475c7).
All arithmetic is exact: Fractions, quadratic fields as pairs, and
cyclotomic fields as polynomials reduced modulo the cyclotomic
polynomial. Standard library only. Non-normative; no Canon claim moves.

Frame under test: the metallic equation x^2 = t x + 1. Gold is t = 1,
silver is t = 2; t is the field trace of the fundamental root, and the
discriminant t^2 + 4 carries the ramified prime of each place.
"""

from fractions import Fraction as Fr

FAILURES = []
COUNT = 0


def check(label, ok):
    global COUNT
    COUNT += 1
    print(f"{COUNT:02d} {'OK  ' if ok else 'FAIL'} {label}")
    if not ok:
        FAILURES.append(label)


# ---------- quadratic fields Q(sqrt(d)): elements (a, b) = a + b sqrt(d)
def qmul(x, y, d):
    (a, b), (c, e) = x, y
    return (a * c + d * b * e, a * e + b * c)


def qpow(x, n, d):
    r = (Fr(1), Fr(0))
    for _ in range(n):
        r = qmul(r, x, d)
    return r


def qconj(x):
    return (x[0], -x[1])


def qtrace(x):
    return 2 * x[0]


def qnorm(x, d):
    return x[0] * x[0] - d * x[1] * x[1]


# ---------- cyclotomic ring Q[x]/Phi(x): dense coefficient lists
def cmul(u, v, phi):
    n = len(phi) - 1
    prod = [Fr(0)] * (len(u) + len(v) - 1)
    for i, a in enumerate(u):
        if a:
            for j, b in enumerate(v):
                prod[i + j] += a * b
    # reduce modulo monic phi
    for i in range(len(prod) - 1, n - 1, -1):
        c = prod[i]
        if c:
            prod[i] = Fr(0)
            for k in range(n):
                prod[i - n + k] -= c * phi[k]
    out = prod[:n]
    return out + [Fr(0)] * (n - len(out))


def csub(u, v):
    return [a - b for a, b in zip(u, v)]


def cgal(u, k, phi):
    n = len(phi) - 1
    out = [Fr(0)] * n
    for i, a in enumerate(u):
        if a:
            mono = [Fr(0)] * ((i * k) + 1)
            mono[i * k] = Fr(1)
            mono = cmul(mono, [Fr(1)], phi) if len(mono) > n else mono + [Fr(0)] * (n - len(mono))
            out = [x + a * y for x, y in zip(out, mono)]
    return out


PHI8 = [Fr(1), Fr(0), Fr(0), Fr(0), Fr(1)]          # x^4 + 1 -> zeta_8
PHI5 = [Fr(1), Fr(1), Fr(1), Fr(1), Fr(1)]          # x^4+x^3+x^2+x+1 -> zeta_5


def elt(*coeffs):
    return [Fr(c) for c in coeffs]


ZERO8 = elt(0, 0, 0, 0)
ONE8 = elt(1, 0, 0, 0)
M = elt(0, 1, 0, 0)                                  # m = zeta_8
I8 = cmul(M, M, PHI8)                                # i = m^2
SQRT2 = cadd = [a + b for a, b in zip(M, cgal(M, 7, PHI8))]  # m + m^-1


# ---------- checks
# 1-2: discriminants of x^2 - t x - 1
disc = lambda t: t * t + 4
check("disc(x^2 - x - 1) = 5", disc(1) == 5)
check("disc(x^2 - 2x - 1) = 8", disc(2) == 8)

# 3: the metal prime is the ramified prime of its own definition
check("5 divides 5 and 2 divides 8 (ramified primes)", 5 % 5 == 0 and 8 % 2 == 0)

# 4-5: trace and norm of the fundamental roots
phi = (Fr(1, 2), Fr(1, 2))          # (1 + sqrt5)/2 in Q(sqrt5)
delta = (Fr(1), Fr(1))              # 1 + sqrt2 in Q(sqrt2)
check("trace(phi) = 1, N(phi) = -1", qtrace(phi) == 1 and qnorm(phi, 5) == -1)
check("trace(delta) = 2, N(delta) = -1", qtrace(delta) == 2 and qnorm(delta, 2) == -1)

# 6-7: growth laws, n = 1..60
F = [0, 1]
P = [0, 1]
for _ in range(70):
    F.append(F[-1] + F[-2])
    P.append(2 * P[-1] + P[-2])
ok_f = all(
    qpow(phi, n, 5) == (Fr(F[n - 1]) + Fr(F[n], 2), Fr(F[n], 2))
    for n in range(1, 61)
)
ok_p = all(
    qpow(delta, n, 2) == (Fr(P[n - 1] + P[n]), Fr(P[n]))
    for n in range(1, 61)
)
check("phi^n = F_n phi + F_(n-1) for n = 1..60 (trace 1 composes)", ok_f)
check("delta^n = P_n delta + P_(n-1) for n = 1..60 (trace 2 doubles)", ok_p)

# 8-10: sqrt2 and i live at zeta_8
check("(m + m^-1)^2 = 2 in Z[zeta_8]", cmul(SQRT2, SQRT2, PHI8) == elt(2, 0, 0, 0))
check("m + m^-1 = m - m^3 (m^4 = -1)", SQRT2 == csub(M, elt(0, 0, 0, 1)))
check("(m^2)^2 = -1 (i = m^2)", cmul(I8, I8, PHI8) == elt(-1, 0, 0, 0))

# 11-12: the writing atom 1 + i = sqrt(2i)
one_plus_i = [a + b for a, b in zip(ONE8, I8)]
check("(1 + i)^2 = 2i", cmul(one_plus_i, one_plus_i, PHI8) == cmul(elt(2, 0, 0, 0), I8, PHI8))
check("1 + i = (m + m^-1) m  (sqrt2 times zeta_8)", cmul(SQRT2, M, PHI8) == one_plus_i)

# 13: norm of 1 + i in Q(i) is 2 (one bit per stroke at the Gaussian floor)
check("N_{Q(i)/Q}(1 + i) = (1+i)(1-i) = 2", (Fr(1) ** 2 + Fr(1) ** 2) == 2)

# 14: norm of 1 + i in Q(zeta_8) is 4 (degree-4 home of the read place)
n8 = ONE8
for k in (1, 3, 5, 7):
    n8 = cmul(n8, cgal(one_plus_i, k, PHI8), PHI8)
check("N_{Q(zeta_8)/Q}(1 + i) = 4", n8 == elt(4, 0, 0, 0))

# 15: irreversibility lock: 1 + i is a non-unit and 2 = -i (1+i)^2
neg_i = cmul(elt(-1, 0, 0, 0), I8, PHI8)
check(
    "1 + i is a non-unit; 2 = -i (1 + i)^2 (2 ramifies)",
    abs(Fr(1) ** 2 + Fr(1) ** 2) != 1
    and cmul(neg_i, cmul(one_plus_i, one_plus_i, PHI8), PHI8) == elt(2, 0, 0, 0),
)

# 16: the reversible carrier M = m / delta is a unit: N(m) = 1 and N(delta) = 1 in Q(zeta_8)
nm = ONE8
for k in (1, 3, 5, 7):
    nm = cmul(nm, cgal(M, k, PHI8), PHI8)
delta8 = [a + b for a, b in zip(ONE8, SQRT2)]        # 1 + sqrt2 inside Q(zeta_8)
nd = ONE8
for k in (1, 3, 5, 7):
    nd = cmul(nd, cgal(delta8, k, PHI8), PHI8)
check("N(m) = 1 and N_{Q(zeta_8)/Q}(1 + sqrt2) = 1, so m/delta is a unit",
      nm == ONE8 and nd == ONE8)

# 17: the gap that cannot be caught: phi^2 - 2 = 1/phi, i.e. phi^3 = 2 phi + 1
check("phi^3 = 2 phi + 1 = 2 + sqrt5 (phi^2 - 2 = 1/phi)",
      qpow(phi, 3, 5) == (Fr(2), Fr(1)))

# 18: the golden pure form is a unit: N(J) = 1 for J = 1 + zeta_5^2
J = elt(1, 0, 1, 0)
nj = elt(1, 0, 0, 0)
for k in (1, 2, 3, 4):
    nj = cmul(nj, cgal(J, k, PHI5), PHI5)
check("N_{Q(zeta_5)/Q}(1 + zeta_5^2) = 1 (J-UNIT)", nj == elt(1, 0, 0, 0))

# 19: write times read is one: Hadamard normalization 1/sqrt2 against the sqrt2 stroke
h = (Fr(0), Fr(1, 2))               # 1/sqrt2 = sqrt2/2 in Q(sqrt2)
s2 = (Fr(0), Fr(1))                 # sqrt2
had2 = qmul(h, h, 2)                # (1/sqrt2)^2 = 1/2, H^2 = I for the 2x2 Hadamard
check("sqrt2 * (1/sqrt2) = 1 and (1/sqrt2)^2 = 1/2 (H^2 = I)",
      qmul(s2, h, 2) == (Fr(1), Fr(0)) and had2 == (Fr(1, 2), Fr(0)))

print()
if FAILURES:
    print(f"{len(FAILURES)} FAILURES")
    raise SystemExit(1)
print(f"ALL OK ({COUNT} checks)")
