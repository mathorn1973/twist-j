#!/usr/bin/env python3
"""Exact audit of the selector-free bridge contract for SQRT-PHI-TIME-GRAVITY.

Incubation work, NON-CANONICAL, no authority. The registry row stays O.
Python standard library only. Exact arithmetic only: F_25 as integer pairs
mod 5, Q(sqrt5) and rational ratios as Fraction pairs, Z[zeta_5] as integer
4-vectors. No float appears anywhere.

Frozen inputs (Public Canon v101):
  SQRT-PHI-DIGIT-LIFT [T]  F_25 = F_5[tau]/(tau^2 - 2), eta = tau^3,
                           roots r_+ = eta, r_- = -eta of r^2 = phi.
  METRO-TICK [T]           1/5 cycle per tick, five ticks close the cycle.
  GRAVITY-BRIDGE-LAW [D]   g = 2^5 phi^2 sqrt(3 - phi),
                           g^2 = 1024 phi^4 (3 - phi).
  native U                 theta_n = s_2(n) mod 2,
                           sigma(n, psi) = z_6(psi) + 2 theta_n mod 5,
                           U(n, psi) = (n + 1, g_sigma(psi)).
"""

from fractions import Fraction

P = 5
N_MAX = 10 ** 4
TABLE_ROWS = 20

checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


# ---------------------------------------------------------------- F_25 ----
ZERO = (0, 0)
ONE = (1, 0)
MINUS_ONE = (4, 0)
PHI_F5 = (3, 0)          # phi = 1/2 = 3 in F_5
J_F5 = (2, 0)            # J_lambda = 2
TAU = (0, 1)


def mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % P, (a * d + b * c) % P)


def neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def power(x, k):
    out, base = ONE, x
    while k:
        if k & 1:
            out = mul(out, base)
        base = mul(base, base)
        k >>= 1
    return out


def inv(x):
    return power(x, 23)


def norm_frobenius(x):
    """N(x) = x^(1+5) = x^6, path one."""
    return power(x, 6)


def norm_formula(x):
    """N(a + b tau) = a^2 - 2 b^2, path two."""
    a, b = x
    return ((a * a - 2 * b * b) % P, 0)


def q_bit(t):
    """F_5^* -> C2, square class: 0 on {1,4}, 1 on {2,3}."""
    if t[1] != 0 or t[0] == 0:
        raise ValueError("q expects an embedded F_5 unit")
    return 0 if t[0] in (1, 4) else 1


def order(x):
    for k in range(1, 25):
        if power(x, k) == ONE:
            return k
    raise ArithmeticError("no order")


def fmt(x):
    a, b = x
    if b == 0:
        return str(a)
    if a == 0:
        return f"{b}t"
    return f"{a}+{b}t"


ETA = power(TAU, 3)
R = {+1: ETA, -1: neg(ETA)}

# Gate 01: frozen field data.
check("01 FIELD   eta=tau^3=(0,2), eta^2=phi=3, order 8, N(eta)=2, -eta is the other root",
      ETA == (0, 2) and mul(ETA, ETA) == PHI_F5 and order(ETA) == 8
      and norm_formula(ETA) == J_F5 and norm_frobenius(ETA) == J_F5
      and {x for x in [(a, b) for a in range(P) for b in range(P)]
           if mul(x, x) == PHI_F5} == {ETA, neg(ETA)})


# ------------------------------------------------------ digit sequence ----
def s2(n):
    return bin(n).count("1")


def nu2(m):
    return (m & -m).bit_length() - 1


Y = {}
for eps, r in R.items():
    seq = [ONE] * (N_MAX + 1)
    for n in range(1, N_MAX + 1):          # recursion, no digit sum used
        seq[n] = seq[n >> 1] if not (n & 1) else mul(r, seq[n >> 1])
    Y[eps] = seq

# theta along the U orbit by the local carry law only (independent path):
# s_2(n+1) - s_2(n) = 1 - nu_2(n+1)  =>  theta_{n+1} = theta_n + 1 + nu_2(n+1) mod 2
theta_U = [0] * (N_MAX + 2)
for n in range(N_MAX + 1):
    theta_U[n + 1] = (theta_U[n] + 1 + nu2(n + 1)) % 2

# theta by the odometer recursion (third path)
theta_rec = [0] * (N_MAX + 1)
for n in range(1, N_MAX + 1):
    theta_rec[n] = theta_rec[n >> 1] if not (n & 1) else 1 - theta_rec[n >> 1]

fail = {k: 0 for k in (
    "closed", "theta_norm2", "theta_def", "Y2", "Y4", "branch_rel",
    "inv_Theta", "inv_theta", "bridge_vs_s2", "bridge_vs_U", "bridge_vs_rec",
    "sigma")}

rows = []
for n in range(N_MAX + 1):
    k = s2(n)
    Yp, Ym = Y[+1][n], Y[-1][n]
    Tp1, Tp2 = norm_frobenius(Yp), norm_formula(Yp)
    Tm = norm_frobenius(Ym)
    tb_p, tb_m = q_bit(Tp1), q_bit(Tm)
    tc = k % 2
    sign = MINUS_ONE if tc else ONE
    if Yp != power(R[+1], k) or Ym != power(R[-1], k):
        fail["closed"] += 1
    if Tp1 != Tp2:
        fail["theta_norm2"] += 1
    if Tp1 != power(J_F5, k):
        fail["theta_def"] += 1
    if mul(Yp, Yp) != inv(Tp1) or mul(Ym, Ym) != inv(Tm):
        fail["Y2"] += 1
    if power(Yp, 4) != sign or power(Ym, 4) != sign:
        fail["Y4"] += 1
    if Ym != mul(sign, Yp):
        fail["branch_rel"] += 1
    if Tp1 != Tm:
        fail["inv_Theta"] += 1
    if tb_p != tb_m:
        fail["inv_theta"] += 1
    if tb_p != tc:
        fail["bridge_vs_s2"] += 1
    if tb_p != theta_U[n]:
        fail["bridge_vs_U"] += 1
    if tb_p != theta_rec[n]:
        fail["bridge_vs_rec"] += 1
    # pre-update: sigma at checkpoint (n, psi) uses the bridge bit of the same n
    if any((z + 2 * tb_p) % 5 != (z + 2 * tc) % 5 for z in range(P)):
        fail["sigma"] += 1
    if n < TABLE_ROWS:
        rows.append((n, k, fmt(Yp), fmt(Ym), fmt(Tp1), fmt(Tm), tb_p, tb_m, tc, theta_U[n]))

check("02 CLOSED  Y_n^eps (recursion) = r_eps^s_2(n), both branches", fail["closed"] == 0)
check("03 NORM    x^6 = a^2 - 2b^2 on every Y_n^+", fail["theta_norm2"] == 0)
check("04 THETA   Theta_n := N(Y_n) = J_lambda^s_2(n) = 2^s_2(n)", fail["theta_def"] == 0)
check("05 LAWS    Y_n^2 = Theta_n^-1 and Y_n^4 = (-1)^theta_n, both branches",
      fail["Y2"] == 0 and fail["Y4"] == 0)
check("06 BRANCH  Y_n^- = (-1)^theta_n Y_n^+", fail["branch_rel"] == 0)
check("07 INVAR   Theta_n^+ = Theta_n^- and q(Theta_n^+) = q(Theta_n^-)",
      fail["inv_Theta"] == 0 and fail["inv_theta"] == 0)
check("08 CLOCK   q(N(Y_n)) = s_2(n) mod 2", fail["bridge_vs_s2"] == 0)
check("09 CLOCK   q(N(Y_n)) = carry-law theta along the U orbit", fail["bridge_vs_U"] == 0)
check("10 CLOCK   q(N(Y_n)) = odometer recursion theta", fail["bridge_vs_rec"] == 0)
check("11 SIGMA   z + 2 q(N(Y_n)) = z + 2 theta_n mod 5 for all z in F_5", fail["sigma"] == 0)

# ----------------------------------- universality of R = Theta on C8 ----
C8 = [power(ETA, k) for k in range(8)]
fibres_ok = True
for t in {norm_frobenius(x) for x in C8}:
    fibre = {x for x in C8 if norm_frobenius(x) == t}
    y = next(iter(fibre))
    fibres_ok &= fibre == {y, neg(y)}
image = sorted(norm_frobenius(x) for x in C8)
check("12 UNIV    on C8 every N-fibre is exactly {y,-y}; N(C8) = F_5^*; so every "
      "branch-invariant function of Y factors uniquely through Theta",
      fibres_ok and set(image) == {(1, 0), (2, 0), (3, 0), (4, 0)})
qhom = all(q_bit(mul((a, 0), (b, 0))) == (q_bit((a, 0)) + q_bit((b, 0))) % 2
           for a in range(1, 5) for b in range(1, 5))
check("13 QHOM    q : F_5^* -> C2 is a surjective homomorphism", qhom
      and {q_bit((a, 0)) for a in range(1, 5)} == {0, 1})
seen_k = {s2(n) % 8 for n in range(N_MAX + 1)}
check("14 IMAGE   s_2(n) mod 8 takes all 8 values, so the source image is all of C8",
      seen_k == set(range(8)))

# ------------------------------------------------------------ tick leg ----
def homs(m, k):
    return [c for c in range(k) if (m * c) % k == 0]


ratio = Fraction(1, 5) / Fraction(1, 8)
check("15 TICK    Hom(C8,C5) = Hom(C4,C5) = Hom(C2,C5) = {0}; (1/5)/(1/8) = 8/5 not integer",
      homs(8, 5) == [0] and homs(4, 5) == [0] and homs(2, 5) == [0]
      and ratio == Fraction(8, 5) and ratio.denominator != 1)
not_hom = (2 * ((1 + 1) % 2)) % 5 != (2 * 1 + 2 * 1) % 5
check("16 TICK    t -> 2t mod 5 is a set map {0,1} -> {0,2}, not a homomorphism C2 -> C5",
      not_hom)
tick = Fraction(1, 5)
check("17 TICK    per U step the counter advances by 1 and the tick fraction by 1/5 "
      "independently of eps; 5 * 1/5 = 1",
      5 * tick == 1 and all(
          (n + 1) - n == 1 for n in range(N_MAX)))

# --------------------------------------------- pre-update convention ----
post_mismatch = sum(1 for n in range(N_MAX + 1) if theta_U[n + 1] != theta_U[n])
check("18 CONV    post-update reading theta_{n+1} differs from the sigma bit at some n "
      "(pre-update is the only reading equal to sigma's bit)", post_mismatch > 0)


# native U on the checkpoint, generators from canon section 3
def gen(i, x):
    p1, p4, p1p, p4p, qq, rr = x
    if i == 0:
        y = (p4, p1, p4p, p1p, qq, rr)
    elif i == 1:
        y = (-p1p, -p4p, -p1, -p4, -qq, -rr)
    elif i == 2:
        y = (-p1p + 2, -p4p + 1 + rr, -p1 + 2, -p4 + 1 - rr, 1 - qq, -rr)
    elif i == 3:
        y = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - qq, 1 - rr)
    else:
        y = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - qq, 1 - rr)
    return tuple(v % P for v in y)


def run_U(theta_source, steps):
    psi = (0, 0, 0, 0, 0, 0)
    trace = []
    for n in range(steps):
        sig = (sum(psi) + 2 * theta_source(n)) % P
        trace.append((n, sig, psi))
        psi = gen(sig, psi)
    return trace


trace_canon = run_U(lambda n: s2(n) % 2, N_MAX)
trace_bridge_p = run_U(lambda n: q_bit(norm_frobenius(Y[+1][n])), N_MAX)
trace_bridge_m = run_U(lambda n: q_bit(norm_frobenius(Y[-1][n])), N_MAX)
trace_post = run_U(lambda n: q_bit(norm_frobenius(Y[+1][n + 1])), N_MAX)
first_div = next((i for i, (a, b) in enumerate(zip(trace_canon, trace_post)) if a != b), None)
check("19 NATIVE  origin-zero native U driven by the bridge bit, either branch, equals the "
      "canonical orbit for 10^4 steps", trace_canon == trace_bridge_p == trace_bridge_m)
check("20 NATIVE  post-update driving diverges from the canonical orbit (control)",
      first_div is not None)

# ---------------------------------------------------------- gravity leg ----
class QS5:
    """a + b sqrt5 with Fraction a, b."""

    def __init__(self, a, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(s, o):
        return QS5(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        return QS5(s.a - o.a, s.b - o.b)

    def __mul__(s, o):
        return QS5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)

    def __eq__(s, o):
        return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b))

    def pow(s, k):
        out = QS5(1)
        for _ in range(k):
            out = out * s
        return out

    def positive(s):
        a, b = s.a, s.b
        if b >= 0:
            return a > 0 or (b > 0 and 5 * b * b > a * a)
        return a > 0 and a * a > 5 * b * b

    def __repr__(s):
        return f"{s.a} + {s.b} sqrt5"


PHI = QS5(Fraction(1, 2), Fraction(1, 2))
THREE_MINUS_PHI = QS5(3) - PHI
SQRT5 = QS5(0, 1)
G2 = QS5(1024) * PHI.pow(4) * THREE_MINUS_PHI

check("21 GRAV    g^2 = 1024 phi^4 (3 - phi) = 5120 + 2048 sqrt5, positive (so g > 0 is the "
      "positive root)", G2 == QS5(5120, 2048) and G2.positive() and THREE_MINUS_PHI.positive())
check("22 READING phi (3 - phi) = sqrt5 and g^2 = 2^10 phi^3 sqrt5 (a reading, not a derivation)",
      PHI * THREE_MINUS_PHI == SQRT5 and G2 == QS5(1024) * PHI.pow(3) * SQRT5)


# Z[zeta_5] in the basis 1, j, j^2, j^3 with j^4 = -1 - j - j^2 - j^3
def zmul(x, y):
    acc = [0] * 7
    for i in range(4):
        for k in range(4):
            acc[i + k] += x[i] * y[k]
    # reduce j^6 = j, j^5 = 1, j^4 = -1-j-j^2-j^3
    acc[1] += acc[6]
    acc[0] += acc[5]
    out = acc[:4]
    for i in range(4):
        out[i] -= acc[4]
    return tuple(out)


one_minus_j = (1, -1, 0, 0)
one_minus_j4 = (2, 1, 1, 1)            # 1 - j^4 = 2 + j + j^2 + j^3
phi_z = (0, 0, -1, -1)                 # phi = -j^2 - j^3
three_minus_phi_z = (3, 0, 1, 1)
check("23 GRAV    |1 - zeta_5|^2 = (1 - j)(1 - j^4) = 3 - phi exactly in Z[zeta_5]",
      zmul(one_minus_j, one_minus_j4) == three_minus_phi_z
      and tuple(a - b for a, b in zip((3, 0, 0, 0), phi_z)) == three_minus_phi_z)

# gravity record of the bridge: built from no n and no eps
def gravity_leg(n, eps):
    return QS5(1024) * PHI.pow(4) * (QS5(3) - PHI)


grav_values = {gravity_leg(n, eps) for n in range(0, N_MAX + 1, 97) for eps in (+1, -1)}
check("24 GRAV    gravity readout is the constant g^2 on the sampled domain "
      "(constancy holds by construction: the leg has no n or eps input)",
      grav_values == {G2})

# ------------------------------------------------------------ breakers ----
succ_dep = 0
for n in range(1, 500):
    e = 1 - nu2(n + 1)
    mp = power(R[+1], e % 8)
    mm = power(R[-1], e % 8)
    succ_dep += mp != mm
odd_dep = sum(1 for n in range(N_MAX + 1) if Y[+1][n] != Y[-1][n])
E_not_fn = None
seenE = {}
for n in range(5001):
    E = s2(n) + s2(n + 2) + nu2(n + 1) + nu2(n + 2)
    key = Y[+1][n]
    if key in seenE and seenE[key][1] != E:
        E_not_fn = (seenE[key][0], n)
        break
    seenE.setdefault(key, (n, E))
check("25 BREAK   bare successor multiplier is branch dependent (n = 1..499)", succ_dep > 0)
check("26 BREAK   Y itself is branch dependent exactly when theta_n = 1",
      odd_dep == sum(theta_U[n] for n in range(N_MAX + 1)))
check("27 BREAK   E(n) is not a function of Y_n (witness pair found)", E_not_fn is not None)

# ------------------------------------------------------------- report ----
print("SQRT-PHI-TIME-GRAVITY selector-free bridge audit, NON-CANONICAL")
print(f"domain n = 0..{N_MAX}, branches eps = +, -; F_25 pairs a+b t, t = tau")
print()
print("first rows (pre-update reading at checkpoint n)")
hdr = ("n", "s2", "Y+", "Y-", "Th+", "Th-", "q+", "q-", "s2%2", "thU")
print("  ".join(f"{h:>5}" for h in hdr))
for row in rows:
    print("  ".join(f"{str(v):>5}" for v in row))
print()
print("failure counters:", " ".join(f"{k}={v}" for k, v in fail.items()))
print(f"successor multiplier branch-dependent cases n=1..499: {succ_dep}")
print(f"Y^+ != Y^- cases n<={N_MAX}: {odd_dep}")
print(f"E(n) not a function of Y_n, witness n pair: {E_not_fn}")
print(f"post-update bit != sigma bit cases n<={N_MAX}: {post_mismatch}")
print(f"post-update native U first divergence at step: {first_div}")
print(f"g^2 = {G2}")
print()
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
passed = sum(ok for _, ok in checks)
print()
print(f"summary: {passed}/{len(checks)} PASS")
raise SystemExit(0 if passed == len(checks) else 1)
