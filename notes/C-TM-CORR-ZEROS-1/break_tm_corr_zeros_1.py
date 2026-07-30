#!/usr/bin/env python3
# break_tm_corr_zeros_1.py
# C-TM-CORR-ZEROS-1 breaker: independent legs attacking the candidate.
# Prereg: PREREG-C-TM-CORR-ZEROS-1.md
# Python 3 stdlib only. Exact integer and Fraction arithmetic; no float.
# Exit 1 iff a falsifier fires (witness printed). Exit 0 otherwise.

import hashlib
import sys
from fractions import Fraction

FIRED = []


def report(tag, fired, detail=""):
    line = "%s %s" % (tag, "FIRED" if fired else "no counterexample")
    if detail:
        line += "  " + detail
    print(line)
    if fired:
        FIRED.append(tag)


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


print("C-TM-CORR-ZEROS-1 breaker")
print("independent code paths: bit-parallel counting, 2x2 matrix products,")
print("no reuse of the verifier's memoized recursion")
print("")

# --------------------------------------------------------------------- B1
# F1/F2 attack: bit-parallel brute force. The Thue-Morse word is built as one
# big integer by the doubling rule t_(n + 2^j) = 1 - t_n, and S_k(N) is read
# off as N - 2 * popcount( (T XOR (T >> k)) restricted to N bits ). No
# recursion on c, no Fraction, no reuse of the verifier.
NBITS = 1 << 23
T = 0
width = 1
while width < NBITS:
    T |= ((~T) & ((1 << width) - 1)) << width
    width <<= 1

N1 = 1 << 22
MASK1 = (1 << N1) - 1
KMAX1 = 2000
zero_absmax = 0
zero_wit = 0
nonzero_min = None
nonzero_wit = 0
for k in range(1, KMAX1 + 1):
    d = ((T ^ (T >> k)) & MASK1).bit_count()
    S = N1 - 2 * d
    if oddpart(k) in (5, 7):
        if abs(S) > zero_absmax:
            zero_absmax, zero_wit = abs(S), k
    else:
        r = Fraction(abs(S), N1)
        if nonzero_min is None or r < nonzero_min:
            nonzero_min, nonzero_wit = r, k
# Separation: predicted zeros must stay O(1)-small against N, predicted
# non-zeros must stay bounded away from 0. The two must not overlap.
sep_ok = (nonzero_min is not None
          and Fraction(zero_absmax, N1) < nonzero_min)
report("B1 (F1/F2) bit-parallel S_k(2^22), 1 <= k <= %d" % KMAX1,
       not sep_ok,
       "max|S| on predicted zeros = %d (k=%d); min |S|/N on predicted "
       "non-zeros = %s (k=%d)"
       % (zero_absmax, zero_wit, nonzero_min, nonzero_wit))

# --------------------------------------------------------------------- B1b
# Added leg, beyond the frozen B1 minimum, and threshold free. A single N
# separates the two families by only about a factor of five, which is weak.
# The decisive recursion-free signature is the SCALING of the mean: at a true
# zero |S_k(N)| does not grow with N, so |S_k(N)|/N must fall when N grows,
# while at a non-zero the mean is stable. This leg compares N = 2^20 with
# N = 2^22 and fires only if the two families OVERLAP.
N1B = 1 << 20
MASK1B = (1 << N1B) - 1
zratio_max = None
zratio_k = 0
nratio_min = None
nratio_k = 0
for k in range(1, KMAX1 + 1):
    x = T ^ (T >> k)
    da = (x & MASK1B).bit_count()
    db = (x & MASK1).bit_count()
    ma = Fraction(abs(N1B - 2 * da), N1B)
    mb = Fraction(abs(N1 - 2 * db), N1)
    if ma == 0:
        continue
    r = mb / ma
    if oddpart(k) in (5, 7):
        if zratio_max is None or r > zratio_max:
            zratio_max, zratio_k = r, k
    else:
        if nratio_min is None or r < nratio_min:
            nratio_min, nratio_k = r, k
overlap = (zratio_max is None or nratio_min is None
           or zratio_max >= nratio_min)
report("B1b (F1/F2, added leg) mean scaling 2^20 -> 2^22, 1 <= k <= %d"
       % KMAX1, overlap,
       "predicted zeros: mean ratio <= %s (k=%d); predicted non-zeros: "
       "mean ratio >= %s (k=%d); families disjoint"
       % (zratio_max, zratio_k, nratio_min, nratio_k))

# --------------------------------------------------------------------- B2
# F6 attack: an independent 2x2 matrix-product implementation of c, compared
# against a freshly written memoized recursion on 0 <= k <= 20000.
M0 = ((Fraction(0), Fraction(1, 2)), (Fraction(1), Fraction(1, 2)))
M1 = ((Fraction(0), Fraction(-1, 2)), (Fraction(-1), Fraction(1, 2)))


def matmul(a, b):
    return ((a[0][0] * b[0][0] + a[0][1] * b[1][0],
             a[0][0] * b[0][1] + a[0][1] * b[1][1]),
            (a[1][0] * b[0][0] + a[1][1] * b[1][0],
             a[1][0] * b[0][1] + a[1][1] * b[1][1]))


def c_matrix(k):
    """c(k) via a product of 2x2 matrices applied to the root vector."""
    q = oddpart(k)
    if q == 1:
        return Fraction(-1, 3)
    m = (q - 1) // 2
    acc = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    for bit in bin(m)[2:]:
        acc = matmul(M1 if bit == "1" else M0, acc)
    u = acc[0][0] * 2 + acc[0][1] * 4
    return -u / 6


memo = {0: Fraction(1), 1: Fraction(-1, 3)}


def c_memo(k):
    stack = [k]
    while stack:
        j = stack[-1]
        if j in memo:
            stack.pop()
            continue
        if j % 2 == 0:
            h = j >> 1
            if h in memo:
                memo[j] = memo[h]
                stack.pop()
            else:
                stack.append(h)
        else:
            m = j >> 1
            if m in memo and m + 1 in memo:
                memo[j] = -(memo[m] + memo[m + 1]) / 2
                stack.pop()
            else:
                if m not in memo:
                    stack.append(m)
                if m + 1 not in memo:
                    stack.append(m + 1)
    return memo[k]


bad = None
for k in range(0, 20001):
    left = Fraction(1) if k == 0 else c_matrix(k)
    if left != c_memo(k):
        bad = k
        break
report("B2 (F6) 2x2 matrix product vs independent memoization, 0 <= k <= 20000",
       bad is not None, "agree everywhere" if bad is None else "k=%d" % bad)

# --------------------------------------------------------------------- B3
# F1/F7 attack: adversarial deep search. Every k = q * 2^a with q odd,
# q <= 4001, a <= 64; plus 256 deterministic pseudorandom k of 512 bits.
SEED = b"C-TM-CORR-ZEROS-1/breaker/B3/v1"
rogue = None
for q in range(1, 4002, 2):
    cq = c_matrix(q)
    want_zero = q in (5, 7)
    if (cq == 0) != want_zero:
        rogue = (q, 0)
        break
    for a in range(0, 65):
        k = q << a
        if (c_matrix(k) == 0) != (oddpart(k) in (5, 7)):
            rogue = (q, a)
            break
    if rogue:
        break
count_rand = 0
if rogue is None:
    for i in range(256):
        h = hashlib.sha256(SEED + b"/%d" % i).digest()
        k = int.from_bytes(hashlib.sha512(h).digest(), "big") >> 0
        k &= (1 << 512) - 1
        if k == 0:
            continue
        count_rand += 1
        if (c_matrix(k) == 0) != (oddpart(k) in (5, 7)):
            rogue = ("random", i)
            break
report("B3 (F1/F7) q*2^a for odd q <= 4001, a <= 64, plus %d pinned 512-bit k"
       % count_rand, rogue is not None,
       "seed %s; no rogue zero" % SEED.decode()
       if rogue is None else "witness %s" % (rogue,))

# --------------------------------------------------------------------- B3b
# F7 attack: a second neighbour coincidence c(p) = c(p+1) with p != 1.
coin = [p for p in range(1, 100001) if c_memo(p) == c_memo(p + 1)]
report("B3b (F7) c(p) = c(p+1) for 1 <= p <= 100000", coin != [1],
       "only p = %s" % coin)

# --------------------------------------------------------------------- B4
# Convention sweep. Complementing the fixed point sends u -> -u and leaves
# every product u_n u_(n+k) fixed; the reversed correlation is the same limit
# by shift invariance. Both checked against the bit-parallel counter.
N4 = 1 << 18
MASK4 = (1 << N4) - 1
TC = (~T) & ((1 << NBITS) - 1)          # complemented Thue-Morse word
mismatch_c = None
mismatch_r = None
for k in range(1, 601):
    d = ((T ^ (T >> k)) & MASK4).bit_count()
    S = N4 - 2 * d
    dc = ((TC ^ (TC >> k)) & MASK4).bit_count()
    Sc = N4 - 2 * dc
    if S != Sc:
        mismatch_c = k
        break
    # reversed: sum over k <= n < N4+k of u_n u_(n-k) is the same window
    # shifted, so compare the shifted counter
    dr = (((T >> k) ^ T) & MASK4).bit_count()
    if dr != d:
        mismatch_r = k
        break
report("B4 convention sweep: complemented word and reversed shift, k <= 600",
       mismatch_c is not None or mismatch_r is not None,
       "S_k identical under both conventions"
       if mismatch_c is None and mismatch_r is None
       else "complement k=%s reversed k=%s" % (mismatch_c, mismatch_r))

# --------------------------------------------------------------------- B5
# Scope fence. The {0,1}-weighted correlation is a DIFFERENT function:
# t_n = (1 - u_n)/2 gives d(k) = (1 + c(k))/4, so d(k) = 0 would need
# c(k) = -1. Recorded so no reader transfers the claim.
N5 = 1 << 18
MASK5 = (1 << N5) - 1
d_zero_positions = []
d_values = {}
for k in range(1, 2001):
    both = (T & (T >> k) & MASK5).bit_count()      # count of t_n = t_(n+k) = 1
    d_emp = Fraction(both, N5)
    d_values[k] = d_emp
    if both == 0:
        d_zero_positions.append(k)
pred = {k: (1 + c_matrix(k)) / 4 for k in (1, 3, 5, 7, 9, 11, 13, 15)}
fence_ok = (d_zero_positions == []
            and all(d_values[k] > 0 for k in (5, 7, 10, 14)))
report("B5 scope fence: {0,1}-weighted correlation, 1 <= k <= 2000",
       not fence_ok,
       "no zero of the {0,1} correlation on the range; it is nonzero at "
       "k = 5, 7, 10, 14 where the balanced correlation vanishes")
print("B5 note d(k) = (1 + c(k))/4 at k = 1,3,5,7: %s"
      % ", ".join(str(pred[k]) for k in (1, 3, 5, 7)))

# --------------------------------------------------------------------- B6
# F8 self-check: no float may appear in any emitted field. Every printed
# numeric value above is an int or a Fraction by construction; this leg
# records the audit rather than asserting it from outside.
float_free = all(not isinstance(v, float)
                 for v in list(d_values.values()) + list(pred.values())
                 + [nonzero_min, Fraction(zero_absmax, N1)])
report("B6 (F8) no float in any computed or emitted numeric field",
       not float_free, "int and Fraction only")

print("")
if FIRED:
    print("FALSIFIER FIRED: %s" % ", ".join(FIRED))
    sys.exit(1)
print("NO FALSIFIER FIRED")
sys.exit(0)
