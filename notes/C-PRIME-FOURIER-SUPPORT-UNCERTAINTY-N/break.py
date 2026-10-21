#!/usr/bin/env python3
"""Self-break for C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N by second code paths.

NON-CANONICAL, layer L1. Standard library only, exact arithmetic only.
Written by the same author as verify.py, so it is a second code path and not
an independent review. It shares no ring code with verify.py.

B1  Reduction certificates. For q in {11, 31, 41, 61, 71} (all q = 1 mod 5)
    and every element w of order five in F_q, the map zeta_5 -> w is a ring
    map Z[zeta_5] -> F_q. A minor whose image is nonzero for some (q, w) is
    nonzero in Z[zeta_5]. Determinants are computed by Gaussian elimination
    over F_q, not by expansion.
B2  Brute force on integer signals f in {-2,...,2}^5. The transform is
    computed in the five-coefficient model Z[t]/(t^5 - 1) modulo the
    all-ones vector: a sum c_0 + c_1 z + ... + c_4 z^4 vanishes exactly when
    all c_e are equal. The minimum of |supp f| + |supp fhat| is searched.
B3  Composite search at N = 4 over Z[i] as integer pairs: every nonzero
    f in {-1,0,1}^4 is scanned for support sums at most 4.

Run from the repository root:
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/break.py
"""

from itertools import combinations, product
import sys


def det_mod(mat, q):
    m = [row[:] for row in mat]
    n = len(m)
    det = 1
    for c in range(n):
        piv = None
        for r in range(c, n):
            if m[r][c] % q:
                piv = r
                break
        if piv is None:
            return 0
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            det = -det
        det = det * m[c][c] % q
        inv = pow(m[c][c], q - 2, q)
        for r in range(c + 1, n):
            fac = m[r][c] * inv % q
            if fac:
                for k in range(c, n):
                    m[r][k] = (m[r][k] - fac * m[c][k]) % q
    return det % q


results = []


def gate(name, ok, detail):
    results.append(ok)
    print(f"BREAK {name} {'HOLDS' if ok else 'BROKEN'} {detail}")


print("C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N break")

# B1
primes = (11, 31, 41, 61, 71)
embeddings = []
for q in primes:
    for w in range(2, q):
        if pow(w, 5, q) == 1:
            embeddings.append((q, w))
certified = 0
total = 0
vanishing_reductions = 0
for k in range(1, 6):
    for rows in combinations(range(5), k):
        for cols in combinations(range(5), k):
            total += 1
            hit = False
            for q, w in embeddings:
                mat = [[pow(w, r * c, q) for c in cols] for r in rows]
                if det_mod(mat, q):
                    hit = True
                else:
                    vanishing_reductions += 1
            if hit:
                certified += 1
gate(
    "B1_REDUCTION_CERTIFIES_ALL_P5_MINORS",
    certified == total == 251,
    f"embeddings={len(embeddings)} minors={total} certified={certified} "
    f"vanishing_reductions={vanishing_reductions}",
)


# B2
def vanishes(c):
    return all(x == c[0] for x in c)


min_sum = None
attain = 0
scanned = 0
for f in product(range(-2, 3), repeat=5):
    if not any(f):
        continue
    scanned += 1
    sf = sum(1 for v in f if v)
    sfh = 0
    for k in range(5):
        c = [0] * 5
        for x in range(5):
            c[(-x * k) % 5] += f[x]
        if not vanishes(c):
            sfh += 1
    s = sf + sfh
    if min_sum is None or s < min_sum:
        min_sum, attain = s, 0
    if s == min_sum:
        attain += 1
gate(
    "B2_BRUTE_FORCE_INTEGER_SIGNALS_P5",
    min_sum == 6,
    f"scanned={scanned} min_support_sum={min_sum} attaining={attain}",
)

# B3: powers of i as (re, im)
ipow = [(1, 0), (0, 1), (-1, 0), (0, -1)]
below = 0
scanned4 = 0
for f in product((-1, 0, 1), repeat=4):
    if not any(f):
        continue
    scanned4 += 1
    sf = sum(1 for v in f if v)
    sfh = 0
    for k in range(4):
        re = im = 0
        for x in range(4):
            a, b = ipow[(-x * k) % 4]
            re += f[x] * a
            im += f[x] * b
        if re or im:
            sfh += 1
    if sf + sfh <= 4:
        below += 1
gate(
    "B3_COMPOSITE_N4_HAS_SUB_BOUND_SIGNALS",
    below > 0,
    f"scanned={scanned4} support_sum_at_most_4={below}",
)

broken = sum(1 for r in results if not r)
print(f"BREAK_VERDICT {len(results) - broken}/{len(results)} "
      f"{'HOLDS' if broken == 0 else 'BROKEN'}")
sys.exit(0 if broken == 0 else 1)
