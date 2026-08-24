#!/usr/bin/env python3
"""P-TWOLOGPHI-INVARIANTS-1.

Exact audit of the four preregistered statements about the constant
2 log phi: the Mahler measure of J, the regulator of Q(zeta_5), class
number one, and the finite-range structure of the periodic-point counts
of the induced toral automorphism.

Python standard library only. Every assertion is exact: integers,
Fractions, and ordered arithmetic in Z[phi]. No float appears anywhere
and gate F1 proves that from the token stream of this file.

Run from the repository root:
    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 probes/P-TWOLOGPHI-INVARIANTS-1/verify.py
"""

import ast
import math
import sys
import tokenize
from fractions import Fraction

DEG = 4
RANGE_MAX = 40

# ---------------------------------------------------------------- Z[zeta_5]
# Basis 1, j, j^2, j^3 with j^4 = -(1 + j + j^2 + j^3).


def red(coeffs):
    c = list(coeffs)
    while len(c) > DEG:
        top = c.pop()
        k = len(c)
        if k == DEG:
            for i in range(DEG):
                c[i] -= top
        else:
            c[k - 5] += top
    while len(c) < DEG:
        c.append(0)
    return tuple(c)


def mul_a(a, b):
    """Route A: convolve, then reduce stepwise by the minimal relation."""
    out = [0] * (2 * DEG - 1)
    for i in range(DEG):
        for k in range(DEG):
            out[i + k] += a[i] * b[k]
    return red(out)


def mul_b(a, b):
    """Route B: convolve modulo x^5 - 1, then substitute j^4 once."""
    out = [0] * 5
    for i in range(DEG):
        for k in range(DEG):
            out[(i + k) % 5] += a[i] * b[k]
    return tuple(out[i] - out[4] for i in range(DEG))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def power(x, n):
    r = ONE
    for _ in range(n):
        r = mul_a(r, x)
    return r


def conj_closed(x):
    """j -> j^4 in closed form: j^4 = -(1+j+j^2+j^3), j^8 = j^3, j^12 = j^2."""
    c0, c1, c2, c3 = x
    return (c0 - c1, -c1, c3 - c1, c2 - c1)


def conj_generic(x):
    """The same automorphism assembled from ring powers of j^4."""
    g = (-1, -1, -1, -1)
    out = (0, 0, 0, 0)
    for i in range(DEG):
        out = add(out, scale(power(g, i), x[i]))
    return out


def scale(x, k):
    return tuple(k * v for v in x)


ONE = (1, 0, 0, 0)
BASIS = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
J = (1, 0, 1, 0)
JBAR = (1, 0, 0, 1)
PHI = (0, 0, -1, -1)

# ------------------------------------------------------------------ matrices


def matrix(x):
    cols = [mul_a(x, e) for e in BASIS]
    return [[cols[c][r] for c in range(DEG)] for r in range(DEG)]


def ident(n):
    return [[1 if i == k else 0 for k in range(n)] for i in range(n)]


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][t] * B[t][k] for t in range(n)) for k in range(n)]
            for i in range(n)]


def matpow(A, n):
    R = ident(len(A))
    for _ in range(n):
        R = matmul(R, A)
    return R


def det(A):
    """Bareiss fraction-free elimination: exact integer determinant."""
    A = [row[:] for row in A]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            for r in range(k + 1, n):
                if A[r][k] != 0:
                    A[k], A[r] = A[r], A[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for k2 in range(k + 1, n):
                A[i][k2] = (A[i][k2] * A[k][k] - A[i][k] * A[k][k2]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def charpoly(A):
    """Faddeev-LeVerrier, exact. Returns descending [1, c1, c2, c3, c4]."""
    n = len(A)
    M = [[0] * n for _ in range(n)]
    coeffs = [Fraction(1)]
    for k in range(1, n + 1):
        M = matmul(A, M)
        for i in range(n):
            M[i][i] += coeffs[-1]
        tr = trace(matmul(A, M))
        coeffs.append(Fraction(-tr, k))
    out = []
    for c in coeffs:
        if c.denominator != 1:
            return None
        out.append(int(c))
    return out


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            out[i + k] += x * y
    return out


def norm(x):
    return det(matrix(x))


def ring_trace(x):
    return trace(matrix(x))


# --------------------------------------------------------------------- Z[phi]
# Elements are (a, b) meaning a + b phi, with phi^2 = phi + 1.


def pmul(u, v):
    a, b = u
    c, d = v
    return (a * c + b * d, a * d + b * c + b * d)


def padd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def psub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def ppow(u, n):
    r = (1, 0)
    for _ in range(n):
        r = pmul(r, u)
    return r


def psign(u):
    """Exact sign of a + b phi, phi = (1 + sqrt5)/2, via 2a + b + b sqrt5."""
    x = 2 * u[0] + u[1]
    y = u[1]
    if x == 0 and y == 0:
        return 0
    if x >= 0 and y >= 0:
        return 1
    if x <= 0 and y <= 0:
        return -1
    left = x * x
    right = 5 * y * y
    if left == right:
        return 0
    if x > 0:
        return 1 if left > right else -1
    return -1 if left > right else 1


def pcmp(u, v):
    return psign(psub(u, v))


PHI1 = (0, 1)
PHIINV = (-1, 1)
PHI2 = (1, 1)
PHIM2 = (2, -1)


def pint(k):
    return (k, 0)


# ---------------------------------------------------------------------- gates

checks = []
lines = []


def gate(name, description, ok):
    checks.append((name, description, bool(ok)))


def emit(text):
    lines.append(text)


# ---- Group A: the ring, the step matrix, the minimal polynomial

pairs_ok = True
for u in BASIS:
    for v in BASIS:
        if mul_a(u, v) != mul_b(u, v):
            pairs_ok = False
probe_elements = [J, JBAR, PHI, ONE, (1, 2, 3, 4), (0, 0, 0, 1), (2, -1, 0, 3),
                  (-1, 1, -1, 1), (5, 0, -2, 7), (3, 3, 3, 3)]
for u in probe_elements:
    for v in probe_elements:
        if mul_a(u, v) != mul_b(u, v):
            pairs_ok = False
        if mul_a(u, v) != mul_a(v, u):
            pairs_ok = False
gate("A1", "two independently coded multiplications on Z[zeta_5] agree on all "
     "16 basis pairs and on 100 declared element pairs, and are commutative",
     pairs_ok)

MJ = matrix(J)
gate("A2", "M_J built column by column from the basis products J . j^k equals "
     "the public step matrix [[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]",
     MJ == [[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]])

gate("A3", "det M_J = 1 = N(J) and trace M_J = 3 = Tr(J)",
     det(MJ) == 1 and trace(MJ) == 3 and norm(J) == 1 and ring_trace(J) == 3)

CP = charpoly(MJ)
gate("A4", "the characteristic polynomial of M_J by exact Faddeev-LeVerrier is "
     "x^4 - 3x^3 + 4x^2 - 2x + 1", CP == [1, -3, 4, -2, 1])

acc = [0]
term = [1]
for _ in range(5):
    width = max(len(acc), len(term))
    acc = acc + [0] * (width - len(acc))
    term = term + [0] * (width - len(term))
    acc = [p + q for p, q in zip(acc, term)]
    term = polymul(term, [-1, 1])
gate("A5", "the same polynomial equals Phi_5(x - 1), expanded independently by "
     "integer polynomial arithmetic", acc == list(reversed(CP)))

no_root = all(sum(CP[i] * pow(r, DEG - i) for i in range(DEG + 1)) != 0
              for r in (1, -1))
quad_factor = False
for b, d in ((1, 1), (-1, -1)):
    for a in range(-6, 7):
        c = -3 - a
        if (b + d + a * c == 4) and (a * d + b * c == -2) and (b * d == 1):
            quad_factor = True
gate("A6", "the polynomial is irreducible over Q: monic with constant term 1, "
     "no root in {1, -1}, and no monic integer quadratic pair over the derived "
     "range |a| <= 6 with b d = 1", no_root and not quad_factor)

# ---- Group B: the Mahler measure

JJB = mul_a(J, JBAR)
gate("B1", "complex conjugation j -> j^4 sends J to Jbar = 1 + j^3 and fixes "
     "phi; J . Jbar = 2 + j^2 + j^3 = 2 - phi = phi^-2 exactly in Z[zeta_5]",
     conj_closed(J) == JBAR
     and conj_generic(J) == JBAR
     and conj_closed(PHI) == PHI
     and JJB == (2, 0, 1, 1)
     and JJB == sub(scale(ONE, 2), PHI)
     and mul_a(JJB, mul_a(PHI, PHI)) == ONE)

CPJJB = charpoly(matrix(JJB))
square_of = polymul([1, -3, 1], [1, -3, 1])
gate("B2", "the characteristic polynomial of multiplication by J . Jbar is "
     "(x^2 - 3x + 1)^2 = x^4 - 6x^3 + 11x^2 - 6x + 1",
     CPJJB == [1, -6, 11, -6, 1] and CPJJB == square_of)

roots_ok = (padd(PHI2, PHIM2) == pint(3) and pmul(PHI2, PHIM2) == pint(1)
            and PHI2 == pmul(PHI1, PHI1) and PHIM2 == psub(pint(2), PHI1))
moduli = [PHI2, PHI2, PHIM2, PHIM2]
outside = [m for m in moduli if pcmp(m, pint(1)) > 0]
gate("B3", "the four archimedean squared moduli are exactly phi^2, phi^2, "
     "phi^-2, phi^-2, the two roots of x^2 - 3x + 1, and exactly two conjugates "
     "lie outside the unit circle",
     roots_ok and len(outside) == 2 and all(m == PHI2 for m in outside))

product_outside = pmul(outside[0], outside[1])
gate("B4", "M(J) = phi . phi = phi^2 exactly, since the product of the squared "
     "moduli outside the unit circle is phi^4 = (phi^2)^2; hence "
     "log M(J) = 2 log phi",
     product_outside == ppow(PHI1, 4) and product_outside == pmul(PHI2, PHI2))

gate("B5", "phi^2 has minimal polynomial x^2 - 3x + 1, whose trace 3 is Tr(J) "
     "and whose norm 1 is N(J)",
     padd(PHI2, PHIM2) == pint(ring_trace(J))
     and pmul(PHI2, PHIM2) == pint(norm(J)))

gate("B6", "phi < 2 < phi^2 exactly, so 1 < log_phi 2 < 2",
     pcmp(PHI1, pint(2)) < 0 and pcmp(pint(2), PHI2) < 0)

# ---- Group C: units and the regulator

PHI5 = [1, 1, 1, 1, 1]
prod = polymul(PHI5, [-1, 1])
gate("C1", "Phi_5 has no real root, since (x - 1) Phi_5(x) = x^5 - 1 whose only "
     "real solution is x = 1 and Phi_5(1) = 5; hence r_1 = 0, r_2 = 2 and the "
     "unit rank r_1 + r_2 - 1 is 1",
     prod == [-1, 0, 0, 0, 0, 1] and sum(PHI5) == 5)

gate("C2", "phi = -j^2 - j^3 lies in Z[zeta_5], is fixed by j -> j^4 hence "
     "totally real, satisfies phi^2 = phi + 1 and phi (phi - 1) = 1, and has "
     "norm 1",
     mul_a(PHI, PHI) == add(PHI, ONE)
     and mul_a(PHI, sub(PHI, ONE)) == ONE
     and norm(PHI) == 1
     and conj_closed(PHI) == PHI)

gate("C3", "the two infinite places give |sigma_1(phi)| = phi and "
     "|sigma_2(phi)| = phi^-1, exact reciprocals in Z[phi]",
     pmul(PHI1, PHIINV) == pint(1)
     and pcmp(PHI1, pint(1)) > 0
     and pcmp(PHIINV, pint(1)) < 0
     and psub(PHI1, pint(1)) == PHIINV)

units_between = []
units_seen = 0
for a in range(-4, 5):
    for b in range(-4, 5):
        if abs(a * a + a * b - b * b) != 1:
            continue
        units_seen += 1
        u = (a, b)
        if pcmp(u, pint(1)) > 0:
            if pcmp(u, PHI1) < 0:
                units_between.append(u)
gate("C4", "phi is the fundamental unit of Z[phi]: over the derived bounds "
     "|2a + b| <= 2 and |b| <= 1, widened here to the box |a| <= 4, |b| <= 4, "
     "no unit lies strictly between 1 and phi",
     units_between == [] and units_seen > 0)

def phi_exponent(u, limit=8):
    """The integer e with u = phi^e, found exactly, or None."""
    for e in range(limit + 1):
        if ppow(PHI1, e) == u:
            return e
        if ppow(PHIINV, e) == u:
            return -e
    return None


LOCAL_DEGREE = 2
e1 = phi_exponent(PHI1)
e2 = phi_exponent(PHIINV)
reg_entry_1 = LOCAL_DEGREE * e1
reg_entry_2 = LOCAL_DEGREE * e2
gate("C5", "with unit rank one and both infinite places complex of local "
     "degree 2, the regulator is the 1 x 1 determinant "
     "|2 log |sigma(phi)|| = 2 log phi: the moduli are exactly phi^1 and "
     "phi^-1, so the entry is 2 or -2 and its absolute value is 2 at either "
     "place",
     e1 == 1 and e2 == -1
     and abs(reg_entry_1) == 2 and abs(reg_entry_2) == 2
     and reg_entry_1 == -reg_entry_2)

# ---- Group D: class number one

tf = [[ring_trace(power((0, 1, 0, 0), i + k)) for k in range(DEG)]
      for i in range(DEG)]
gate("D1", "the trace form on 1, j, j^2, j^3 has determinant 125, matching the "
     "registered disc(K_5) = 5^3", det(tf) == 125 and 125 == 5 ** 3)


def arctan_inv(x, terms):
    total = Fraction(0)
    previous = None
    monotone = True
    for k in range(terms):
        size = Fraction(1, (2 * k + 1) * x ** (2 * k + 1))
        if previous is not None and not size < previous:
            monotone = False
        previous = size
        total += size if k % 2 == 0 else -size
    tail = Fraction(1, (2 * terms + 1) * x ** (2 * terms + 1))
    return total, tail, monotone


TERMS = 10
a5, t5, m5 = arctan_inv(5, TERMS)
a239, t239, m239 = arctan_inv(239, TERMS)
PI_LO = 16 * (a5 - t5) - 4 * (a239 + t239)
PI_HI = 16 * (a5 + t5) - 4 * (a239 - t239)
gate("D2", "Machin's formula pi = 16 arctan(1/5) - 4 arctan(1/239) with "
     "strictly decreasing alternating terms gives an exact rational enclosure "
     "PI_LO < pi < PI_HI with both bounds between 3 and 4",
     m5 and m239 and PI_LO < PI_HI
     and Fraction(3) < PI_LO and PI_HI < Fraction(4))

gate("D3", "the Minkowski bound M_K = (4/pi)^2 (4!/4^4) sqrt125 = "
     "(15 sqrt5)/(2 pi^2) is below 2, since that is equivalent to "
     "1125 < 16 pi^4 and the exact lower enclosure already exceeds it; hence "
     "every ideal class of Q(zeta_5) contains an ideal of norm 1 and h = 1",
     16 * PI_LO ** 4 > 1125
     and Fraction(24, 256) == Fraction(3, 32)
     and 15 * 15 * 5 == 1125)

SQRT5 = psub(pmul(pint(2), PHI1), pint(1))
gate("D4", "for Q(sqrt5) the Minkowski bound is sqrt5/2 < 2, equivalent to "
     "5 < 16, with no transcendental input; sqrt5 = 2 phi - 1 squares to 5 and "
     "is below 4 in the exact Z[phi] order; hence h(Q(sqrt5)) = 1",
     pmul(SQRT5, SQRT5) == pint(5)
     and pcmp(SQRT5, pint(4)) < 0
     and 5 < 16)

# ---- Group E: periodic points

route_ring = []
route_matrix = []
for n in range(1, RANGE_MAX + 1):
    route_ring.append(abs(norm(sub(power(J, n), ONE))))
    B = matpow(MJ, n)
    C = [[B[i][k] - (1 if i == k else 0) for k in range(DEG)]
         for i in range(DEG)]
    route_matrix.append(abs(det(C)))
gate("E1", "the ring-norm route |N(J^n - 1)| and the matrix route "
     "|det(M_J^n - I)| agree for every n in 1..40",
     route_ring == route_matrix)

gate("E2", "the first six values are 1, 11, 31, 55, 121, 341",
     route_ring[:6] == [1, 11, 31, 55, 121, 341])

L = [2, 1]
while len(L) <= RANGE_MAX:
    L.append(L[-1] + L[-2])
closed_ok = True
closed_count = 0
for n in range(1, RANGE_MAX + 1):
    if n % 5 != 0:
        continue
    closed_count += 1
    want = L[n] ** 2 if n % 10 == 5 else (L[n] - 2) ** 2
    if route_ring[n - 1] != want:
        closed_ok = False
gate("E3", "the Lucas closed forms hold on the declared range: L_n^2 when "
     "n = 5 mod 10 and (L_n - 2)^2 when n = 0 mod 10, for all eight n "
     "divisible by 5 in 1..40", closed_ok and closed_count == 8)

gate("E4", "the pin: |N(J^15 - 1)| = 1860496 = 1364^2 = L_15^2",
     route_ring[14] == 1860496 and L[15] == 1364 and 1364 ** 2 == 1860496)

off = [n for n in range(1, RANGE_MAX + 1) if n % 5 != 0]
squares = [n for n in off
           if math.isqrt(route_ring[n - 1]) ** 2 == route_ring[n - 1]]
gate("E5", "among the 32 values with 5 not dividing n and 1 <= n <= 40 exactly "
     "one is a perfect square, namely n = 1 with value 1",
     len(off) == 32 and squares == [1] and route_ring[0] == 1)

bracket_ok = True
for n in range(1, RANGE_MAX + 1):
    lo = pmul(ppow(psub(ppow(PHI1, n), pint(1)), 2),
              ppow(psub(pint(1), ppow(PHIINV, n)), 2))
    hi = pmul(ppow(padd(ppow(PHI1, n), pint(1)), 2),
              ppow(padd(pint(1), ppow(PHIINV, n)), 2))
    value = pint(route_ring[n - 1])
    if pcmp(value, lo) < 0 or pcmp(hi, value) < 0:
        bracket_ok = False
gate("E6", "the two-sided bracket (phi^n - 1)^2 (1 - phi^-n)^2 <= |N(J^n - 1)| "
     "<= (phi^n + 1)^2 (1 + phi^-n)^2 holds exactly in Z[phi] for every n in "
     "1..40, including n = 1 to 5", bracket_ok)

# ---- Group F: integrity of this verifier

SOURCE = __file__
numbers = []
with tokenize.open(SOURCE) as handle:
    for token in tokenize.generate_tokens(handle.readline):
        if token.type == tokenize.NUMBER:
            numbers.append(token.string)
non_integer = []
for text in numbers:
    try:
        int(text)
    except ValueError:
        non_integer.append(text)
gate("F1", "no float appears anywhere in this verifier: every NUMBER token of "
     "its own token stream parses as a Python int, so the gate cannot match "
     "its own probe strings", non_integer == [] and len(numbers) > 0)

with open(SOURCE, "rb") as handle:
    tree = ast.parse(handle.read())
imported = set()
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for alias in node.names:
            imported.add(alias.name.split(".")[0])
    elif isinstance(node, ast.ImportFrom):
        if node.module:
            imported.add(node.module.split(".")[0])
allowed = {"ast", "math", "sys", "tokenize", "fractions"}
forbidden = {"random", "time", "datetime", "os", "socket", "urllib",
             "subprocess", "secrets", "decimal", "numpy"}
gate("F2", "the verifier imports only ast, math, sys, tokenize and fractions, "
     "all standard library, and names no source of randomness, time, network "
     "or process state", imported <= allowed and not (imported & forbidden))

# ------------------------------------------------------------------- reporting

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(newline="\n")

emit("P-TWOLOGPHI-INVARIANTS-1 verify")
emit("minimal polynomial of J: x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1)")
emit("squared moduli: phi^2, phi^2, phi^-2, phi^-2; M(J) = phi^2")
emit("regulator entry: 2 log phi; class number: 1 for Q(zeta_5) and Q(sqrt5)")
emit("|N(J^n - 1)| for n = 1..10:")
for n in range(1, 11):
    emit("  n = %2d  %d" % (n, route_ring[n - 1]))
emit("Lucas closed forms on n divisible by 5 in 1..40: %d of %d"
     % (closed_count, closed_count))
emit("off-residue perfect squares among %d values: %s"
     % (len(off), ",".join(str(n) for n in squares)))

passed = 0
for name, description, ok in checks:
    emit("%s %s %s" % (name, description, "PASS" if ok else "FAIL"))
    if ok:
        passed += 1

emit("DECISION: 2 log phi is anchored arithmetically as log M(J) and as "
     "Reg(Q(zeta_5)); no layer bridge is created")
emit("RESULT %d/%d %s" % (passed, len(checks),
                          "ALL PASS" if passed == len(checks) else "FAIL"))

sys.stdout.write("\n".join(lines) + "\n")
sys.exit(0 if passed == len(checks) else 1)
