#!/usr/bin/env python3
"""breaker_lambda_grid_audit_1.py

Attack pass for PREREG-AUDIT-LAMBDA-GRID-1 (sha256
39a3ef65576e14f41d1b408f5d662d85375f4dfb025c46a63e5dfec94230c215).

Independent representations against verify_lambda_grid_audit_1.py:
  * 4-tuple basis of Z[zeta_5] with x^4 = -1-x-x^2-x^3, written fresh;
  * lambda-division valuation with explicit precision ledger (no norms);
  * the M_J integer matrix of the axiom step map, orders in GL_4(Z/5^m);
  * direct enumeration of (O/lambda^2)^x;
  * Teichmueller construction of i in Z_5 by iterated fifth powers;
  * refutation of the naive boundary guess v(J^20 - 1) = 5, with the
    forced-cancellation mechanism res((w/lambda)^4 u) = -1 mod lambda;
  * reproduction of the two sealed public verifiers by stdout SHA-256.

A FINDING line is a fired attack. PASS means the target survived the attack.
Exact integer arithmetic only; no float is formed.
"""

import hashlib
import os
import subprocess
import sys

RESULTS = []


def record(label, survived):
    RESULTS.append((label, bool(survived)))


# ---------------------------------------------------------------------------
# 4-tuple representation, basis 1, zeta, zeta^2, zeta^3
# ---------------------------------------------------------------------------

def qmul(a, b, mod=None):
    raw = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                raw[i + j] += a[i] * b[j]
    for deg in (6, 5, 4):
        c = raw[deg]
        if c:
            raw[deg] = 0
            for s in range(4):
                raw[deg - 4 + s] -= c
    out = raw[:4]
    if mod is not None:
        out = [x % mod for x in out]
    return tuple(out)


def qadd(a, b, mod=None):
    out = [a[i] + b[i] for i in range(4)]
    if mod is not None:
        out = [x % mod for x in out]
    return tuple(out)


def qsub(a, b, mod=None):
    out = [a[i] - b[i] for i in range(4)]
    if mod is not None:
        out = [x % mod for x in out]
    return tuple(out)


def qpow(a, e, mod=None):
    r = Q_ONE
    b = a
    while e:
        if e & 1:
            r = qmul(r, b, mod)
        b = qmul(b, b, mod)
        e >>= 1
    return r


Q_ONE = (1, 0, 0, 0)
Q_J = (1, 0, 1, 0)
Q_LAM = (1, -1, 0, 0)
Q_U = (0, -1, 1, -1)          # lambda^4 / 5


def qres(a):
    # zeta -> 1 mod 5
    return sum(a) % 5


# lambda-division valuation with precision ledger. Elements carried mod 5^P.

def q_uinv():
    # u^-1 = sigma2(u) sigma3(u) sigma4(u) / N(u); N(u) = 1 checked by verifier
    def sig(a, s):
        # zeta -> zeta^s in the 4-tuple basis via 5-vector detour
        five = [a[0], a[1], a[2], a[3], 0]
        out = [0] * 5
        for i in range(5):
            out[(i * s) % 5] += five[i]
        t = out[4]
        return (out[0] - t, out[1] - t, out[2] - t, out[3] - t)
    p = Q_ONE
    for s in (2, 3, 4):
        p = qmul(p, sig(Q_U, s))
    return p


Q_UINV = q_uinv()
Q_LAM3 = qpow(Q_LAM, 3)

record("BR-00 sanity: u . u^-1 = 1 in the 4-tuple basis", qmul(Q_U, Q_UINV) == Q_ONE)


def vlam_division(a, prec_pow):
    """valuation of the class of a, carried mod 5^prec_pow; ledger enforced."""
    P = prec_pow
    a = tuple(x % 5 ** P for x in a)
    v = 0
    while True:
        if P < 3:
            raise AssertionError("precision ledger exhausted")
        if all(x % 5 ** P == 0 for x in a):
            raise AssertionError("zero class at available precision")
        if qres(a) % 5 != 0:
            return v
        b = qmul(qmul(a, Q_LAM3, 5 ** P), Q_UINV, 5 ** P)
        if any(x % 5 for x in b):
            raise AssertionError("division by lambda failed: not divisible")
        a = tuple((x // 5) % 5 ** (P - 1) for x in b)
        P -= 1
        v += 1


PREC_POW = 40

record("BR-01 division-route ladder equals the registered 1, 6, 10, 14, 18, 22, 26",
       [vlam_division(qsub(qpow(Q_J, 4 * 5 ** m, 5 ** PREC_POW), Q_ONE, 5 ** PREC_POW), PREC_POW)
        for m in range(7)] == [1, 6, 10, 14, 18, 22, 26])

record("BR-02 naive boundary guess v(J^20 - 1) = 5 is refuted (value is 6)",
       vlam_division(qsub(qpow(Q_J, 20, 5 ** PREC_POW), Q_ONE, 5 ** PREC_POW), PREC_POW) == 6)

# mechanism: w = J^4 - 1 has w/lambda a unit and res((w/lambda)^4 u) = -1 mod lambda,
# so 5 + w^4 = 5(1 + (w/lambda)^4 u) cancels at least one extra lambda power.
w = qsub(qpow(Q_J, 4, 5 ** PREC_POW), Q_ONE, 5 ** PREC_POW)
b = qmul(qmul(w, Q_LAM3, 5 ** PREC_POW), Q_UINV, 5 ** PREC_POW)
wl = tuple((x // 5) % 5 ** (PREC_POW - 1) for x in b)     # w / lambda
mech = qmul(qpow(wl, 4, 5 ** (PREC_POW - 1)), tuple(x % 5 ** (PREC_POW - 1) for x in Q_U), 5 ** (PREC_POW - 1))
record("BR-03 forced cancellation: res((w/lambda)^4 u) = 4 = -1 mod 5",
       qres(wl) != 0 and qres(mech) == 4)

# ---------------------------------------------------------------------------
# M_J matrix route from the axiom step map (a,b,c,d) -> (a-c+d, b-c, a, b-c+d)
# ---------------------------------------------------------------------------

M_J = ((1, 0, -1, 1),
       (0, 1, -1, 0),
       (1, 0, 0, 0),
       (0, 1, -1, 1))


def mat_apply(M, v, mod=None):
    out = [sum(M[i][j] * v[j] for j in range(4)) for i in range(4)]
    if mod is not None:
        out = [x % mod for x in out]
    return tuple(out)


def mat_mul(A, B, mod=None):
    out = [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    if mod is not None:
        out = [[x % mod for x in row] for row in out]
    return tuple(tuple(r) for r in out)


def mat_pow(A, e, mod):
    R = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
    B = A
    while e:
        if e & 1:
            R = mat_mul(R, B, mod)
        B = mat_mul(B, B, mod)
        e >>= 1
    return R


agree = True
basis = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 5)]
for v in basis:
    agree = agree and mat_apply(M_J, v) == qmul(Q_J, v)
record("BR-04 axiom step matrix equals multiplication by J in the 4-tuple basis", agree)

I4 = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
mat_ok = True
for m in range(1, 7):
    mod = 5 ** m
    target = 4 * 5 ** m
    # order divides 4 * 5^(4m-1); step through divisors 2^e 5^f in increasing order
    order = None
    for d in sorted(2 ** e * 5 ** f for e in range(3) for f in range(4 * m)):
        if mat_pow(M_J, d, mod) == I4:
            order = d
            break
    mat_ok = mat_ok and order == target
record("BR-05 matrix route: ord of M_J in GL_4(Z/5^m) = 4.5^m for m = 1..6", mat_ok)

# ---------------------------------------------------------------------------
# direct enumeration of (O/lambda^2)^x on the basis {1, lambda}
# ---------------------------------------------------------------------------

def l2_mul(x, y):
    a, b = x
    c, d = y
    return ((a * c) % 5, (a * d + b * c) % 5)


units = [(a, b) for a in range(1, 5) for b in range(5)]
record("BR-06 unit count at level 2 is 4 . 5 = 20", len(units) == 20)

# J = 1 + zeta^2, zeta = 1 - lambda, zeta^2 = 1 - 2 lambda + lambda^2 = 1 - 2 lambda
jl2 = (2, 3)


def l2_order(x):
    acc = (1, 0)
    for n in range(1, 25):
        acc = l2_mul(acc, x)
        if acc == (1, 0):
            return n
    return None


record("BR-07 order of J in (O/lambda^2)^x is 20 by direct enumeration", l2_order(jl2) == 20)
record("BR-08 exponent bound: every unit order at level 2 divides 20",
       all(20 % l2_order(u) == 0 for u in units))

# ---------------------------------------------------------------------------
# Teichmueller i and the mu_3 / mu_8 obstructions
# ---------------------------------------------------------------------------

TP = 12
tw = pow(2, 5 ** (TP - 1), 5 ** TP)
record("BR-09 Teichmueller: (2^(5^11))^2 + 1 = 0 mod 5^12 and = 2 mod 5",
       (tw * tw + 1) % 5 ** TP == 0 and tw % 5 == 2)

record("BR-10 mu_3 attack blocked at the residue field: x^2 + x + 1 has no root mod 5",
       all((x * x + x + 1) % 5 for x in range(5)))
record("BR-11 mu_8 attack blocked at the residue field: x^4 + 1 has no root mod 5",
       all((x ** 4 + 1) % 5 for x in range(5)))

# grid denominator shadow: q divides some 4 . 5^a  iff  strip5(q) divides 4
def strip5(q):
    while q % 5 == 0:
        q //= 5
    return q


shadow = True
for q in range(1, 2001):
    lhs = any((4 * 5 ** a) % q == 0 for a in range(7))
    rhs = 4 % strip5(q) == 0
    shadow = shadow and (lhs == rhs)
record("BR-12 grid denominators are exactly {2^e 5^f : e <= 2}, q <= 2000", shadow)

# ---------------------------------------------------------------------------
# reproduction of the sealed public verifiers
# ---------------------------------------------------------------------------

REPO = "/home/claude/twist-j"
ENV = dict(os.environ)
ENV.update({"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0", "TZ": "UTC"})

SEALED = [
    ("probes/P-LAMBDA-COCYCLE-ANGLES-1/verify.py",
     "3263191dd30c07f9895f1b2c95f347d3d9a45ecb8dfcf136e1a34997891f62b1",
     "9e46f7f56d7e4b22683e3b595707f5bb880ef707771ac75aaa35a8dcc2584688"),
    ("probes/P-LAMBDA-COCYCLE-ANGLES-2/verify.py",
     "37347d200eba27b2aa94da3e79c3705aa1e8e4d8cc6136c6347d32cd7b6306a9",
     "7c5b661401dc245e9469e9cc7b6e9129f4a773b44226410ff557770d35727eeb"),
]

for path, file_hash, stdout_hash in SEALED:
    full = os.path.join(REPO, path)
    with open(full, "rb") as fh:
        fbytes = fh.read()
    fh_ok = hashlib.sha256(fbytes).hexdigest() == file_hash
    proc = subprocess.run([sys.executable, path], cwd=REPO, env=ENV,
                          capture_output=True, timeout=120)
    sh_ok = (proc.returncode == 0 and proc.stderr == b"" and
             hashlib.sha256(proc.stdout).hexdigest() == stdout_hash)
    record("BR-13 reproduction %s: file hash sealed, exit 0, stdout byte-identical" % path.split("/")[1],
           fh_ok and sh_ok)

# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

findings = 0
for label, survived in RESULTS:
    print(("PASS " if survived else "FINDING ") + label)
    if not survived:
        findings += 1
print("FINDINGS %d of %d attacks" % (findings, len(RESULTS)))
sys.exit(1 if findings else 0)
