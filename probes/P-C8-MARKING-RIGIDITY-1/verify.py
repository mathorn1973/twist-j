#!/usr/bin/env python3
"""Exact L1 audit for P-C8-MARKING-RIGIDITY-1.

Standard library only. Exact residue arithmetic in F_p and
F_25 = F_5[t]/(t^2 - 2), exact rational arithmetic in Q[z]/(z^4 + 1).
No floating point, numerical approximation, network, files, subprocesses,
random choice or external package. Scopes are finite and exhausted exactly.
"""

from fractions import Fraction as F

FAILURES: list[str] = []


def gate(name: str, ok: bool, message: str) -> None:
    if not ok:
        FAILURES.append(name)
    print(f"{name} {'PASS' if ok else 'FAIL'}: {message}")


# ---------- F_p and F_25 = F_5[t]/(t^2 - 2) ----------

def f25_mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % 5, (a * d + b * c) % 5)


def f25_pow(x, n):
    r = (1, 0)
    for _ in range(n):
        r = f25_mul(r, x)
    return r


def f25_order(x):
    for n in range(1, 25):
        if f25_pow(x, n) == (1, 0):
            return n
    return 0


def order_mod(a: int, p: int) -> int:
    r, n = a % p, 1
    while r != 1:
        r, n = (r * a) % p, n + 1
    return n


def is_prime(n: int) -> bool:
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


# ---------- Q(zeta_8) = Q[z]/(z^4 + 1) ----------

ZERO = (F(0), F(0), F(0), F(0))
ONE = (F(1), F(0), F(0), F(0))


def q_add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def q_smul(s, x):
    return tuple(F(s) * a for a in x)


def q_mul(x, y):
    r = [F(0)] * 8
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            r[i + j] += a * b
    for i in range(7, 3, -1):
        r[i - 4] -= r[i]
        r[i] = F(0)
    return tuple(r[:4])


def zeta(k: int):
    k %= 8
    s = 1
    if k >= 4:
        k -= 4
        s = -1
    v = [F(0)] * 4
    v[k] = F(s)
    return tuple(v)


def q_conj(x):
    r = ZERO
    for i, a in enumerate(x):
        r = q_add(r, q_smul(a, zeta(-i)))
    return r


def q_rational(x) -> bool:
    return x[1] == 0 and x[2] == 0 and x[3] == 0


INV_SQRT2 = q_smul(F(1, 2), q_add(zeta(1), q_smul(-1, zeta(3))))

I2 = ((ONE, ZERO), (ZERO, ONE))
XG = ((ZERO, ONE), (ONE, ZERO))
YG = ((ZERO, q_smul(-1, zeta(2))), (zeta(2), ZERO))
ZG = ((ONE, ZERO), (ZERO, q_smul(-1, ONE)))
PAULI = (("I", I2), ("X", XG), ("Y", YG), ("Z", ZG))


def T(k):
    return ((ONE, ZERO), (ZERO, zeta(k)))


def kron(A, B):
    return tuple(
        tuple(q_mul(A[i // 2][j // 2], B[i % 2][j % 2]) for j in range(4))
        for i in range(4)
    )


def apply4(A, v):
    return tuple(
        q_add(q_add(q_mul(A[i][0], v[0]), q_mul(A[i][1], v[1])),
              q_add(q_mul(A[i][2], v[2]), q_mul(A[i][3], v[3])))
        for i in range(4)
    )


def inner4(u, v):
    r = ZERO
    for a, b in zip(u, v):
        r = q_add(r, q_mul(q_conj(a), b))
    return r


# ---------- G1, the marked datum ----------

tau = (0, 1)
squares = sorted({(x * x) % 5 for x in range(1, 5)})
nonsquares = sorted(a for a in range(1, 5) if a not in squares)
gate(
    "G1",
    f25_pow(tau, 2) == (2, 0)
    and f25_pow(tau, 4) == (4, 0)
    and f25_order(tau) == 8
    and order_mod(2, 5) == 4
    and nonsquares == [2, 3],
    "marked datum exact: tau^2=2, tau^4=-1, ord(tau)=8, ord_5(2)=4, nonsquares {2,3}",
)

# ---------- G2, rigidity of the prime ----------

divisor_primes = sorted(p for p in range(2, 16) if 15 % p == 0 and is_prime(p))
surviving = [p for p in divisor_primes if (2 ** 2 - 1) % p != 0]
scan = [p for p in range(3, 20000) if is_prime(p) and order_mod(2, p) == 4]
gate(
    "G2",
    divisor_primes == [3, 5]
    and surviving == [5]
    and order_mod(2, 3) == 2
    and scan == [5],
    "rigidity: ord_p(2)=4 forces p|15 and p not|3, so p=5; scan below 20000 confirms",
)

# ---------- G3, the converse over F_5 ----------

roots = {m: [(a, b) for a in range(5) for b in range(5)
             if f25_mul((a, b), (a, b)) == (m, 0)] for m in range(1, 5)}
orders = {m: sorted({f25_order(r) for r in roots[m]}) for m in range(1, 5)}
gate(
    "G3",
    all(len(roots[m]) == 2 for m in range(1, 5))
    and orders[2] == [8] and orders[3] == [8]
    and 8 not in orders[1] and 8 not in orders[4],
    "converse: over F_5 a nonsquare marking gives order exactly 8 and a square never does",
)

# ---------- G4, the source-side orientation ----------

gate(
    "G4",
    (2 * 3) % 5 == 1
    and nonsquares == [2, 3]
    and f25_pow(tau, 6) == (3, 0)
    and f25_pow(tau, 14) == (3, 0)
    and f25_pow(tau, 10) == (2, 0),
    "source orientation is the marking 2 versus 2^-1=3: (tau^3)^2=(tau^7)^2=3, (tau^5)^2=2",
)

# ---------- G5, the (Z/8)* arithmetic ----------

units = [1, 3, 5, 7]
frob, conj_exp = 5, 7
group = sorted({(frob ** a * conj_exp ** b) % 8 for a in (0, 1) for b in (0, 1)})
orbit = [sorted({(u * frob ** a * conj_exp ** b) % 8
                 for a in (0, 1) for b in (0, 1)}) for u in units]
coincide = sorted(r for r in units if r == conj_exp)
trivial = sorted(r for r in units if r == 1)
gate(
    "G5",
    frob != conj_exp
    and group == units
    and all(o == units for o in orbit)
    and coincide == [7]
    and trivial == [1],
    "Frobenius exponent 5 and conjugation exponent 7 act freely and transitively on {1,3,5,7}",
)

# ---------- G6, the target-side orientation no-go ----------

bell = (INV_SQRT2, ZERO, ZERO, INV_SQRT2)
psi_1 = apply4(kron(T(1), T(1)), bell)
psi_7 = apply4(kron(T(7), T(7)), bell)
conjugate_pair = psi_7 == tuple(q_conj(a) for a in psi_1)
separating, rational_separating, values_rational = [], [], True
for na, a in PAULI:
    for nb, b in PAULI:
        observable = kron(a, b)
        rational_entries = all(q_rational(entry) for row in observable for entry in row)
        v1 = inner4(psi_1, apply4(observable, psi_1))
        v7 = inner4(psi_7, apply4(observable, psi_7))
        if not (q_rational(v1) and q_rational(v7)):
            values_rational = False
        if v1 != v7:
            separating.append(f"{na}{nb}")
            if rational_entries:
                rational_separating.append(f"{na}{nb}")
separating.sort()
gate(
    "G6",
    conjugate_pair
    and values_rational
    and rational_separating == []
    and "XY" in separating
    and "YX" in separating
    and inner4(psi_1, apply4(kron(XG, YG), psi_1)) == ONE
    and inner4(psi_7, apply4(kron(XG, YG), psi_7)) == q_smul(-1, ONE),
    "no-go: the two orientation states are conjugate, no rational observable separates them, "
    f"separating set {','.join(separating)}",
)

TOTAL = 6
print(
    f"RESULT {TOTAL - len(FAILURES)}/{TOTAL} "
    f"{'ALL PASS' if not FAILURES else 'FAIL ' + ','.join(FAILURES)}: "
    "exact arithmetic rigidity and one relative no-go; no physical bridge, "
    "marking remains a dictionary input"
)
raise SystemExit(1 if FAILURES else 0)
