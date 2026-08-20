#!/usr/bin/env python3
# P-ENTROPY-RESIDUE-MATH-1 verify.py
# Exact audit for three carrier-independent entropy rows:
#   J-TORAL-ENTROPY [T]            h_top = h_Haar = 2 log phi for the toral
#                                  automorphism induced by the step matrix
#                                  M_J on R^4/Z^4; #Fix(T^n) = |N(J^n - 1)|.
#   TM-ENTROPY-ZERO [T]            the Thue-Morse driver has linear factor
#                                  complexity (finite audit to L = 20 with
#                                  a stabilization witness), entropy rate 0.
#   BINARY-READ-RELATIVE-ENTROPY [T]  the residue bracket
#                                  R(q) = 2 log phi - h(q) in
#                                  [log(phi^2/2), 2 log phi], floor strictly
#                                  positive since phi^2 - 2 = 1/phi.
# Universal statements are carried by the written proofs in PREREG.md with
# imports labeled; this verifier audits every exact algebraic identity and
# the finite counts.
#
# Python standard library only. Fraction arithmetic; integers; exact
# elements of Z[phi] as pairs and of Z[zeta_5] as polynomial vectors mod
# Phi_5. No float anywhere.

import sys
from fractions import Fraction

assert len(sys.argv) == 1

checks = 0

def gate(name, condition):
    global checks
    assert condition, name
    checks += 1
    print("%s PASS" % name)

print("P-ENTROPY-RESIDUE-MATH-1 verify")

# ---- the step matrix (the anchored step (a,b,c,d) -> (a-c+d, b-c, a,
# b-c+d), multiplication by J = 1 + zeta_5^2 on the integer basis) -------
M = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)

def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))

def mat_sub_id(A, s=1):
    return tuple(tuple(A[i][j] - (s if i == j else 0) for j in range(4))
                 for i in range(4))

def det4(A):
    # exact integer determinant by cofactor expansion
    def det3(a):
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    total = 0
    for j in range(4):
        minor = tuple(tuple(A[i][k] for k in range(4) if k != j)
                      for i in range(1, 4))
        total += (-1) ** j * A[0][j] * det3(minor)
    return total

def trace(A):
    return sum(A[i][i] for i in range(4))

# E1 characteristic polynomial by Faddeev-LeVerrier, exact
def charpoly(A):
    # returns coefficients [c4, c3, c2, c1, c0] of x^4+c3x^3+... with c4=1
    cs = [Fraction(1)]
    Mk = A
    prev = A
    for k in range(1, 5):
        ck = Fraction(-trace(prev), k)
        cs.append(ck)
        if k < 4:
            shifted = tuple(tuple(Fraction(prev[i][j]) +
                                  (ck if i == j else 0)
                                  for j in range(4)) for i in range(4))
            prev = tuple(tuple(sum(Fraction(A[i][t]) * shifted[t][j]
                                   for t in range(4)) for j in range(4))
                         for i in range(4))
    return cs

cp = charpoly(M)
gate("E1 char poly of the step matrix is x^4 - 3x^3 + 4x^2 - 2x + 1,"
     " with det = N(J) = 1 and trace = Tr(J) = 3",
     cp == [Fraction(1), Fraction(-3), Fraction(4), Fraction(-2),
            Fraction(1)]
     and det4(M) == 1 and trace(M) == 3)

# ---- Z[phi] arithmetic: elements a + b phi with phi^2 = phi + 1 ----------
def pmul(x, y):
    a, b = x
    c, d = y
    # (a + b phi)(c + d phi) = ac + (ad + bc) phi + bd (phi + 1)
    return (a * c + b * d, a * d + b * c + b * d)

def pnorm(x):
    a, b = x
    return a * a + a * b - b * b   # N(a + b phi)

PHI = (0, 1)
PHI2 = pmul(PHI, PHI)              # phi + 1

def psign(x):
    # exact sign of a + b phi = a + b(1+sqrt5)/2: sign of (2a+b) + b sqrt5
    p, q = 2 * x[0] + x[1], x[1]
    if q == 0:
        return (p > 0) - (p < 0)
    if p == 0:
        return (q > 0) - (q < 0)
    if p > 0 and q > 0:
        return 1
    if p < 0 and q < 0:
        return -1
    d = p * p - 5 * q * q
    assert d != 0
    if p > 0 and q < 0:
        return 1 if d > 0 else -1
    return 1 if d < 0 else -1

# E2 factorization over Z[phi]: char poly = (x^2 - phi^2 x + phi^2)
# (x^2 - (2 - phi) x + (2 - phi)); both quadratics have complex roots
# (negative discriminant), so the modulus pairs are exactly phi and 1/phi
A2 = PHI2
B2 = (2, -1)                       # 2 - phi
gate("E2a coefficient identities: with A = phi^2 and B = 2 - phi:"
     " A + B = 3, A B = 1, A + B + A B = 4, so the expanded product"
     " (x^2 - A x + A)(x^2 - B x + B) equals the char poly exactly",
     (A2[0] + B2[0], A2[1] + B2[1]) == (3, 0)
     and pmul(A2, B2) == (1, 0)
     # full expansion: (x^2 - A x + A)(x^2 - B x + B) =
     # x^4 - (A+B)x^3 + (A+B+AB)x^2 - 2AB x + AB
     and (A2[0] + B2[0] + pmul(A2, B2)[0],
          A2[1] + B2[1] + pmul(A2, B2)[1]) == (4, 0))
disc1 = pmul(A2, (A2[0] - 4, A2[1]))       # A(A - 4)
disc2 = pmul(B2, (B2[0] - 4, B2[1]))       # B(B - 4)
gate("E2b both discriminants negative (two complex conjugate pairs);"
     " squared moduli exactly phi^2 and phi^-2 = 2 - phi, so"
     " h_top = h_Haar = log(phi) + log(phi) = 2 log phi by the imported"
     " entropy formula",
     psign(disc1) < 0 and psign(disc2) < 0
     and pmul(PHI2, B2) == (1, 0))

# ---- Z[zeta_5] arithmetic mod Phi_5 = 1 + x + x^2 + x^3 + x^4 -----------
def zred(p):
    p = [Fraction(c) for c in p]
    while len(p) < 4:
        p.append(Fraction(0))
    while len(p) > 4:
        c = p.pop()
        if c:
            d = len(p)
            for i in range(d - 4, d):
                p[i] -= c
    return tuple(p[:4])

def zmul(a, b):
    out = [Fraction(0)] * 7
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return zred(out)

def zsigma(a, s):
    # Galois sigma_s: zeta^i -> zeta^(i s mod 5), then fold
    # zeta^4 = -(1 + zeta + zeta^2 + zeta^3)
    out = [Fraction(0)] * 5
    for i, x in enumerate(a):
        if x:
            out[(i * s) % 5] += x
    base = list(out[:4])
    c = out[4]
    if c:
        for i in range(4):
            base[i] -= c
    return tuple(base)

ZONE = zred([1])
J5 = zred([1, 0, 1])               # J = 1 + zeta^2

def znorm_int(a):
    # N(a) = product of the four conjugates; must be rational
    prod = ZONE
    for s in (1, 2, 3, 4):
        prod = zmul(prod, zsigma(a, s))
    assert prod[1] == prod[2] == prod[3] == 0
    v = prod[0]
    assert v.denominator == 1
    return v.numerator

def jpow_minus_one(n):
    p = ZONE
    for _ in range(n):
        p = zmul(p, J5)
    return zred([p[0] - 1, p[1], p[2], p[3]])

# E3 fixed-point counts: |det(M^n - I)| equals |N(J^n - 1)| for n <= 15,
# two independent exact paths; table printed; no eigenvalue is a root of
# unity (moduli are phi and 1/phi), so the count formula applies
fix = []
ok3 = True
Mn = M
print("fixed-point table #Fix(T^n) = |det(M^n - I)| = |N(J^n - 1)|:")
for n in range(1, 16):
    d = abs(det4(mat_sub_id(Mn)))
    nn = abs(znorm_int(jpow_minus_one(n)))
    ok3 = ok3 and (d == nn) and d > 0
    fix.append(d)
    print("  n = %2d: %d" % (n, d))
    Mn = mat_mul(Mn, M)
gate("E3 the two paths agree for n = 1..15, all counts positive;"
     " pinned witness #Fix(T^15) = %d" % fix[14], ok3)

# E4 Thue-Morse driver: exact factor counts to L = 20 with stabilization
def tm_word(length):
    return "".join("1" if bin(n).count("1") % 2 else "0"
                   for n in range(length))

W17 = tm_word(1 << 17)
W16_len = 1 << 16
pL = []
stab_ok = True
for L in range(1, 21):
    fac17 = set()
    for i in range(len(W17) - L + 1):
        fac17.add(W17[i:i + L])
    fac16 = set()
    for i in range(W16_len - L + 1):
        fac16.add(W17[i:i + L])
    stab_ok = stab_ok and (fac16 == fac17)
    pL.append(len(fac17))
print("TM factor complexity p(L), L = 1..20: %s"
      % ", ".join(str(x) for x in pL))
gate("E4 exact counts stabilized between prefixes 2^16 and 2^17;"
     " p(1..4) = 2, 4, 6, 10; p(20) = %d; p(L) < 4L for 3 <= L <= 20"
     " (linear-complexity witness; the universal linearity is the"
     " labeled import, hence entropy rate 0)" % pL[19],
     stab_ok and pL[0] == 2 and pL[1] == 4 and pL[2] == 6
     and pL[3] == 10 and all(pL[L - 1] < 4 * L for L in range(3, 21)))

# E5 the residue bracket algebra in Z[phi], exact
phim2 = (2, -1)
gate("E5a floor identity: phi^2 - 2 = phi - 1 = 1/phi exactly, and it is"
     " strictly positive, so the bracket floor log(phi^2/2) is strictly"
     " positive",
     (PHI2[0] - 2, PHI2[1]) == (-1, 1)
     and pmul((-1, 1), PHI) == (1, 0)
     and psign((-1, 1)) > 0)
gate("E5b split identity carrier: phi^2 = 2 (phi^2 / 2), i.e."
     " 2 log phi = log 2 + log(phi^2 / 2) as an exact factorization,"
     " and phi^2 = phi + 1 is irrational (x^2 - x - 1 has no rational"
     " root), so 2 log phi is the log of no rational number",
     PHI2 == (1, 1)
     and all(a * a - a - 1 != 0 for a in (1, -1))
     and PHI2[1] != 0)
gate("E5c multiplicative independence of {phi^2, 2, 5} by norms:"
     " N(phi^2) = 1, N(2) = 4, N(5) = 25, and phi has infinite order"
     " (phi > 1); hence a log(phi^2) + b log 2 + c log 5 = 0 with"
     " rational a, b, c forces a = b = c = 0; in particular"
     " 2 log phi differs from log 5 and from log 4 exactly",
     pnorm(PHI2) == 1 and pnorm((2, 0)) == 4 and pnorm((5, 0)) == 25
     and psign((PHI[0] - 1, PHI[1])) > 0)

print("DECISION: the exact skeleton of the three entropy rows holds;"
      " universal statements carried by the written proofs with imports"
      " labeled")
print("RESULT %d/%d ALL PASS" % (checks, checks))
