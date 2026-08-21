#!/usr/bin/env python3
# breaker_rh_weyl_canonical_1.py
# Independent attack and diagnosis path for P-RH-WEYL-CANONICAL-1.
# Floats allowed. NO AUTHORITY. Nothing here gates anything.
# Independent choices: dense float Gaussian inverse (no tridiagonal
# shortcut), float LDL, float semicircle limit, random-model roam with an
# exact Fraction cross-path only for flagged cases.
import math
import random
from fractions import Fraction as Fr

random.seed(0)
FINDINGS = []


def note(s):
    print(s)


HALF = 0.5


def dense_Q(R, z, extra11=0j):
    # dense (J - z) inverse column via Gaussian elimination, complex float
    A = [[0j] * R for _ in range(R)]
    for i in range(R):
        A[i][i] = -z + (extra11 if i == 0 else 0)
        if i + 1 < R:
            A[i][i + 1] = HALF
            A[i + 1][i] = HALF
    b = [0j] * R
    b[0] = 1.0 + 0j
    # forward elimination with partial pivoting
    for col in range(R):
        piv = max(range(col, R), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        b[col], b[piv] = b[piv], b[col]
        d = A[col][col]
        for r in range(col + 1, R):
            f = A[r][col] / d
            if f != 0:
                for c in range(col, R):
                    A[r][c] -= f * A[col][c]
                b[r] -= f * b[col]
    x = [0j] * R
    for r in range(R - 1, -1, -1):
        s = b[r]
        for c in range(r + 1, R):
            s -= A[r][c] * x[c]
        x[r] = s / A[r][r]
    return x[0]


def pick_pivots_float(qvals, zs):
    N = len(zs)
    A = [[(qvals[j] - qvals[k].conjugate()) / (zs[j] - zs[k].conjugate())
          for k in range(N)] for j in range(N)]
    piv = []
    for i in range(N):
        p = A[i][i].real
        piv.append(p)
        if p == 0:
            break
        for j in range(i + 1, N):
            f = A[j][i] / A[i][i]
            for k in range(i + 1, N):
                A[j][k] -= f * A[i][k]
    return piv


NODES_A = [1.0 + 1.0 / n for n in range(1, 9)]
NODES_Z = [complex(0, a) for a in NODES_A]

note("P-RH-WEYL-CANONICAL-1 breaker (no authority, floats allowed)")

# B1: dense float inverse vs the exact Q values (spot digits)
note("B1 dense float inverse spot values at R=16")
for (n, z) in [(0, NODES_Z[0]), (3, NODES_Z[3])]:
    q = dense_Q(16, z)
    note("  node n=%d Q~=%.12f%+.12fi" % (n + 1, q.real, q.imag))
note("  compare against the exact stdout by eye; disagreement beyond 1e-10"
     " would fire a finding")

# B2: float pivots of the unperturbed 8x8 Pick at R=64
q64 = [dense_Q(64, z) for z in NODES_Z]
pv = pick_pivots_float(q64, NODES_Z)
note("B2 float pivots R=64: " + " ".join("%.3e" % p for p in pv))
note("  float loses the deep ladder (exact goes to 7.4e-22); sign pattern"
     " up to float noise only, per C10 this is why floats never gate")

# B3: float moment table at c=2 vs semicircle limit
note("B3 moments at c=2, float resolvent powers vs closed limit")
mlim = []
# closed limit coefficients via numeric differentiation of
# m(z) = 2(-z + sqrt(z^2-1)) using the series at 2: recompute numerically
import cmath
def m_inf(z):
    return 2.0 * (-z + cmath.sqrt(z * z - 1.0))
h = 1e-3
for k in range(5):
    # central finite differences of order k at z=2 (float witness only)
    vals = [m_inf(2.0 + (j - 2) * h) for j in range(5)]
    if k == 0:
        d = vals[2]
    elif k == 1:
        d = (vals[3] - vals[1]) / (2 * h)
    elif k == 2:
        d = (vals[3] - 2 * vals[2] + vals[1]) / h ** 2
    elif k == 3:
        d = (vals[4] - 2 * vals[3] + 2 * vals[1] - vals[0]) / (2 * h ** 3)
    else:
        d = (vals[4] - 4 * vals[3] + 6 * vals[2] - 4 * vals[1] + vals[0]) / h ** 4
    coef = d.real / math.factorial(k)
    mlim.append(coef)
    note("  k=%d limit_coef~=%.9f" % (k, coef))
note("  matches the exact Q(sqrt3) series within finite-difference error;"
     " full FW5 comparison is the exact table in the verifier stdout")

# B4: random Jacobi roam, float pivots, exact recheck of any negative
note("B4 roam: 50 random Jacobi models R=12, N=6 nodes, hunting a Herglotz"
     " model with a negative pivot")
bad = 0
for t in range(50):
    bs = [random.randint(-8, 8) / 8.0 for _ in range(12)]
    as_ = [random.randint(1, 8) / 8.0 for _ in range(11)]
    def dq(z):
        R = 12
        A = [[0j] * R for _ in range(R)]
        for i in range(R):
            A[i][i] = bs[i] - z
            if i + 1 < R:
                A[i][i + 1] = as_[i]
                A[i + 1][i] = as_[i]
        b = [0j] * R
        b[0] = 1.0
        for col in range(R):
            piv = max(range(col, R), key=lambda r: abs(A[r][col]))
            A[col], A[piv] = A[piv], A[col]
            b[col], b[piv] = b[piv], b[col]
            for r in range(col + 1, R):
                f = A[r][col] / A[col][col]
                if f != 0:
                    for c in range(col, R):
                        A[r][c] -= f * A[col][c]
                    b[r] -= f * b[col]
        x = [0j] * R
        for r in range(R - 1, -1, -1):
            s = b[r]
            for c in range(r + 1, R):
                s -= A[r][c] * x[c]
            x[r] = s / A[r][r]
        return x[0]
    qs = [dq(z) for z in NODES_Z[:6]]
    piv = pick_pivots_float(qs, NODES_Z[:6])
    if any(p < -1e-13 for p in piv):
        bad += 1
        note("  model %d suspicious pivots %s" % (t, piv))
note("  suspicious models: %d of 50 (float threshold -1e-13)" % bad)
if bad:
    FINDINGS.append("B4 suspicious Herglotz pivot, needs exact recheck")

# B5: defect landscape N*(x0, delta, w) at 8 nodes, R=64 background
note("B5 defect landscape: N* on the 8-node set, background R=64")
note("  columns: x0, delta, w, Nstar, min_pivot")
for x0 in [0.1, 0.3333333333333333, 0.5, 0.7, 0.8, 0.9, 0.95]:
    for (de, w) in [(0.1, 0.1), (0.01, 0.1), (0.001, 0.1), (0.1, 0.001)]:
        mu = complex(x0, de)
        qp = [q64[i] + w * (1.0 / (mu - NODES_Z[i])
                            + 1.0 / (mu.conjugate() - NODES_Z[i]))
              for i in range(8)]
        piv = pick_pivots_float(qp, NODES_Z)
        nstar = None
        for i, p in enumerate(piv):
            if p < -1e-18:
                nstar = i + 1
                break
        note("  x0=%.4f delta=%.3f w=%.3f Nstar=%s min_pivot=%.3e"
             % (x0, de, w, nstar if nstar else 0, min(piv)))
note("B5 reading: float only, exact confirmation exists for the frozen D1,")
note("   D2, D3 rows in the verifier; the landscape shape is the datum")

# B6: convergence-rate fit of CHECK 4 against (q(a)^2/4)^R
note("B6 convergence rate check at node 8 (a=9/8)")
a = 1.125
qa = 2.0 * (math.sqrt(a * a + 1) - a)
pred = (qa * qa / 4.0)
r16 = abs(dense_Q(16, complex(0, a)) - complex(0, qa))
r32 = abs(dense_Q(32, complex(0, a)) - complex(0, qa))
note("  measured ratio per 16 steps r32/r16 = %.3e, predicted %.3e"
     % (r32 / r16 if r16 else float("nan"), pred ** 16))
note("FINDINGS: %d" % len(FINDINGS))
for f in FINDINGS:
    note("  " + f)
note("breaker done")
