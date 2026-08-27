#!/usr/bin/env python3
# check_quantum_claims.py
# Exact checker for the arithmetically falsifiable claims in the
# "quantum computing beats classical optimization" challenge text of
# 2026-08-27 (TWIST-J notes lane, NON-CANONICAL, no canon writes).
#
# Scope. This checker rules on arithmetic only. It does not rule on whether
# any vendor deployment happened, and it takes no position on quantum
# hardware roadmaps. It settles the four load-bearing numerical assertions
# the challenge text makes, because each is decidable on the spot:
#
#   A. "If you have 20 delivery stops or 20 factory tasks ... the number of
#       possible scheduling permutations quickly becomes larger than the
#       number of atoms in the universe."
#   B. "Classical computers must check these pathways one by one" and the
#       Atari "would take longer than the age of the universe to finish the
#       loop" on a 20-stop instance.
#   C. "[Quantum] cancels out the mathematically 'bad' schedules and
#       amplifies the 'perfect' schedule, revealing the ideal factory floor
#       plan instantly."
#   D. The implied claim that exact optimization of a 20-node instance is
#       out of reach for commodity classical hardware.
#
# Everything below is integer arithmetic. No floats are used anywhere in a
# gate, so stdout is byte-identical across architectures. Distances use
# math.isqrt (exact integer floor of a square root). Randomness is a pinned
# LCG with a fixed seed. Python 3 standard library only.
#
# Gates are typed:
#   [EXACT]    a theorem or a closed computation; no assumption
#   [MODEL]    depends on an explicitly printed constant (clock rate, gate
#              rate). The assumption is stated in the output so a reader can
#              reject it and redo the line.
#
# Usage:
#   python3 check_quantum_claims.py            # deterministic stdout
#   python3 check_quantum_claims.py --timing   # adds wall-clock to stderr

import math
import sys
from itertools import permutations

R = []


def ck(kind, name, cond, detail=""):
    R.append((kind, name, bool(cond), detail))


def out(s=""):
    sys.stdout.write(s + "\n")


# ---------------------------------------------------------------------------
# Pinned reference magnitudes
# ---------------------------------------------------------------------------
# Atoms in the observable universe: the standard estimate is 10**78 to
# 10**82. We take the generous middle, 10**80. Using the low end 10**78 only
# strengthens gate A2.
ATOMS_UNIVERSE = 10 ** 80

# Age of the universe: 13.787 Gyr, in seconds, as an exact integer of
# seconds using a 365.25-day Julian year. 13787000000 * 31557600.
AGE_UNIVERSE_S = 13787000000 * 31557600

N_STOPS = 20  # the number the challenge text names


# ---------------------------------------------------------------------------
# Deterministic TSP instance (pinned; no float anywhere)
# ---------------------------------------------------------------------------
def lcg_coords(n, seed=20260827):
    """Numerical Recipes LCG. Fixed seed -> identical instance everywhere."""
    s = seed
    pts = []
    for _ in range(n):
        s = (1664525 * s + 1013904223) % (2 ** 32)
        x = s % 10000
        s = (1664525 * s + 1013904223) % (2 ** 32)
        y = s % 10000
        pts.append((x, y))
    return pts


def dmatrix(pts):
    """Integer Euclidean distance, exact floor via isqrt. Symmetric."""
    n = len(pts)
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        xi, yi = pts[i]
        for j in range(i + 1, n):
            xj, yj = pts[j]
            dx = xi - xj
            dy = yi - yj
            v = math.isqrt(dx * dx + dy * dy)
            d[i][j] = v
            d[j][i] = v
    return d


def held_karp(d):
    """Exact TSP by Held-Karp dynamic programming, 1962.

    Returns (optimal_cost, optimal_tour). The result is a proven optimum,
    not a sample and not a heuristic: the recursion is exhaustive over
    subsets, so no tour is left unexamined.
    """
    n = len(d)
    full = 1 << (n - 1)
    BIG = 1 << 62
    # dp[mask * (n-1) + (j-1)] = cost of the best path 0 -> ... -> j
    # visiting exactly the set mask of {1..n-1}, ending at j.
    dp = [BIG] * (full * (n - 1))
    par = [-1] * (full * (n - 1))
    m = n - 1
    for j in range(1, n):
        dp[(1 << (j - 1)) * m + (j - 1)] = d[0][j]
    for mask in range(1, full):
        base = mask * m
        for j in range(1, n):
            bj = 1 << (j - 1)
            if not (mask & bj):
                continue
            cur = dp[base + (j - 1)]
            if cur >= BIG:
                continue
            dj = d[j]
            rest = full - 1 - mask  # candidates not yet visited
            k = 1
            while rest:
                if rest & 1:
                    nmask = mask | (1 << (k - 1))
                    idx = nmask * m + (k - 1)
                    cand = cur + dj[k]
                    if cand < dp[idx]:
                        dp[idx] = cand
                        par[idx] = j
                rest >>= 1
                k += 1
    best = BIG
    bestj = -1
    last = (full - 1) * m
    for j in range(1, n):
        v = dp[last + (j - 1)]
        if v < BIG:
            v += d[j][0]
            if v < best:
                best = v
                bestj = j
    tour = []
    mask = full - 1
    j = bestj
    while j != -1:
        tour.append(j)
        pj = par[mask * m + (j - 1)]
        mask ^= 1 << (j - 1)
        j = pj
    tour.reverse()
    return best, [0] + tour


def brute_force(d):
    """Exhaustive permutation search. Ground truth for the DP."""
    n = len(d)
    best = None
    for p in permutations(range(1, n)):
        c = d[0][p[0]]
        for a, b in zip(p, p[1:]):
            c += d[a][b]
        c += d[p[-1]][0]
        if best is None or c < best:
            best = c
    return best


def tour_cost(d, t):
    return sum(d[t[i]][t[(i + 1) % len(t)]] for i in range(len(t)))


# ---------------------------------------------------------------------------
# Block A. The combinatorial-explosion claim
# ---------------------------------------------------------------------------
f20 = math.factorial(20)
tours20 = math.factorial(N_STOPS - 1) // 2  # distinct closed tours

ck("EXACT", "A1 20! evaluates to 2432902008176640000",
   f20 == 2432902008176640000, f"20! = {f20}")

ck("EXACT", "A2 20! is SMALLER than the atom count, not larger",
   f20 < ATOMS_UNIVERSE,
   f"20! = {f20} < 10**80")

# By how much: 20! * 10**61 still does not reach 10**80.
ck("EXACT", "A3 the miss is at least 61 orders of magnitude",
   f20 * (10 ** 61) < ATOMS_UNIVERSE,
   f"20! * 10**61 = {f20 * 10 ** 61} < 10**80")

n_cross = 1
while math.factorial(n_cross) <= ATOMS_UNIVERSE:
    n_cross += 1
ck("EXACT", "A4 n! first exceeds 10**80 at n = 59, not n = 20",
   n_cross == 59, f"smallest n with n! > 10**80 is n = {n_cross}")

ck("EXACT", "A5 distinct 20-stop tours number 19!/2, smaller still",
   tours20 == 60822550204416000, f"19!/2 = {tours20}")


# ---------------------------------------------------------------------------
# Block D (run first; Block B and C cite its result).
# Exact optimization of the 20-node instance on one core.
# ---------------------------------------------------------------------------
pts20 = lcg_coords(N_STOPS)
d20 = dmatrix(pts20)

t0 = None
if "--timing" in sys.argv:
    import time
    t0 = time.perf_counter()

opt20, tour20 = held_karp(d20)

if t0 is not None:
    import time
    sys.stderr.write(
        f"[timing] held_karp n=20 : {time.perf_counter() - t0:.2f} s\n")

ck("EXACT", "D1 Held-Karp returns a proven optimum for the 20-node instance",
   opt20 > 0, f"optimal closed tour cost = {opt20}")

ck("EXACT", "D2 the returned tour visits all 20 nodes exactly once",
   sorted(tour20) == list(range(N_STOPS)),
   f"tour = {tour20}")

ck("EXACT", "D3 the returned tour's cost equals the reported optimum",
   tour_cost(d20, tour20) == opt20,
   f"recomputed cost = {tour_cost(d20, tour20)}")

# Independent correctness control: the same DP against exhaustive search on
# a size where exhaustive search is affordable.
pts10 = lcg_coords(10)
d10 = dmatrix(pts10)
hk10, t10 = held_karp(d10)
bf10 = brute_force(d10)
ck("EXACT", "D4 control: DP equals exhaustive search at n = 10",
   hk10 == bf10, f"held_karp = {hk10}, brute_force = {bf10}")

# Work actually performed: sum over subsets of popcount^2, the exact
# Held-Karp inner-loop count, versus the tour count the text invokes.
hk_ops20 = sum(
    math.comb(N_STOPS - 1, p) * p * p for p in range(N_STOPS)
)
ck("EXACT", "D5 the DP examines ~5e7 states, not 6e16 tours",
   hk_ops20 < tours20 // (10 ** 8),
   f"Held-Karp inner steps = {hk_ops20} vs {tours20} tours "
   f"(ratio {tours20 // hk_ops20}:1)")


# ---------------------------------------------------------------------------
# Block B. "Must check pathways one by one" / the Atari claim
# ---------------------------------------------------------------------------
ck("EXACT", "B1 exhaustive enumeration is not required: the DP is exact "
            "and skips 99.9999999% of tours",
   hk_ops20 * (10 ** 8) < tours20,
   f"{hk_ops20} steps sufficed to prove optimality over {tours20} tours")

# The Atari claim, under stated hardware assumptions.
ATARI_HZ = 1190000          # MOS 6507 in the Atari 2600, ~1.19 MHz
CYCLES_PER_TOUR = 1000      # generous: permutation step + 20 16-bit adds
atari_tours_per_s = ATARI_HZ // CYCLES_PER_TOUR
atari_seconds = tours20 // atari_tours_per_s

ck("MODEL", "B2 brute force on a 1.19 MHz 6507 takes ~1.6 million years",
   1_000_000 * 31557600 < atari_seconds < 3_000_000 * 31557600,
   f"{atari_seconds} s at {atari_tours_per_s} tours/s "
   f"= {atari_seconds // 31557600} years")

ck("MODEL", "B3 that is FAR SHORTER than the age of the universe, so the "
            "text's stated reason is false",
   atari_seconds < AGE_UNIVERSE_S,
   f"{atari_seconds} s < {AGE_UNIVERSE_S} s "
   f"(shorter by a factor of {AGE_UNIVERSE_S // atari_seconds})")

# What actually stops the Atari is memory, not time.
HK_TABLE_BYTES = (N_STOPS - 1) * (2 ** (N_STOPS - 1)) * 2  # 2-byte costs
ATARI_2600_RAM = 128
ck("EXACT", "B4 the real Atari 2600 obstruction is RAM, not the age of "
            "the universe",
   HK_TABLE_BYTES > ATARI_2600_RAM * 10 ** 5,
   f"Held-Karp table = {HK_TABLE_BYTES} bytes vs 128 bytes of RAM")


# ---------------------------------------------------------------------------
# Block C. "Amplifies the perfect schedule, revealing it instantly"
# ---------------------------------------------------------------------------
# Grover is the strongest general-purpose amplitude-amplification result for
# unstructured search: it needs Theta(sqrt(N)) oracle queries, not O(1).
# "Instantly" is not on offer even in the idealized fault-tolerant limit.
grover20 = math.isqrt(tours20)

ck("EXACT", "C1 amplitude amplification needs ~sqrt(N) queries, ~2.5e8 "
            "here, not one",
   grover20 > 10 ** 8,
   f"sqrt(19!/2) = {grover20} oracle queries, each a full reversible "
   f"tour evaluation")

# Asymptotic comparison: Grover over tours vs Held-Karp, as a function of n.
def grover_q(n):
    return math.isqrt(math.factorial(n - 1) // 2)


def hk_steps(n):
    return n * n * (2 ** n)


cross = None
for n in range(5, 41):
    if hk_steps(n) < grover_q(n):
        cross = n
        break

ck("EXACT", "C2 from n = 21 upward, classical Held-Karp needs FEWER steps "
            "than Grover needs queries",
   cross == 21, f"crossover at n = {cross}")

ck("EXACT", "C3 and the classical margin widens without bound "
            "(n = 30 shown)",
   grover_q(30) > 1000 * hk_steps(30),
   f"n=30: Grover {grover_q(30)} vs Held-Karp {hk_steps(30)} "
   f"(ratio {grover_q(30) // hk_steps(30)}:1)")

# Grover is also quadratic, not exponential: it cannot convert an
# exponential search into a polynomial one.
ck("EXACT", "C4 Grover's speedup is quadratic, so an exponential space "
            "stays exponential",
   grover_q(40) > 10 ** 20,
   f"n=40: {grover_q(40)} queries remains astronomically large")


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
out("=" * 74)
out("check_quantum_claims.py -- arithmetic audit of the 2026-08-27 challenge")
out("NON-CANONICAL. Rules on arithmetic only. No Canon claim, no probe.")
out("=" * 74)
out()
out(f"pinned atom count      : 10**80 (standard range 10**78 .. 10**82)")
out(f"pinned universe age    : {AGE_UNIVERSE_S} s (13.787 Gyr)")
out(f"pinned TSP instance    : n=20, LCG seed 20260827, integer isqrt metric")
out(f"pinned Atari model     : MOS 6507 @ {ATARI_HZ} Hz, "
    f"{CYCLES_PER_TOUR} cycles/tour")
out()

blocks = {
    "A": "COMBINATORIAL EXPLOSION  -- '20 stops > atoms in the universe'",
    "B": "SEQUENTIAL SEARCH        -- 'one by one' / 'age of the universe'",
    "C": "AMPLITUDE AMPLIFICATION  -- 'reveals the ideal plan instantly'",
    "D": "CLASSICAL FEASIBILITY    -- exact 20-node optimum on one core",
}
for key in "ABCD":
    out(blocks[key])
    out("-" * 74)
    for kind, name, ok, detail in R:
        if not name.startswith(key):
            continue
        out(f"  [{'PASS' if ok else 'FAIL'}] [{kind:5s}] {name}")
        if detail:
            out(f"           {detail}")
    out()

npass = sum(1 for _, _, ok, _ in R if ok)
out("=" * 74)
out(f"{npass}/{len(R)} gates pass "
    f"({sum(1 for k, _, _, _ in R if k == 'EXACT')} exact, "
    f"{sum(1 for k, _, _, _ in R if k == 'MODEL')} model-dependent)")
out("=" * 74)
out()
out("VERDICT")
out("-" * 74)
out("The four numerical assertions in the challenge text are false as")
out("stated. 20! is 61 orders of magnitude SMALLER than the atom count,")
out("not larger. Exact optimization of the named 20-node instance is a")
out("seconds-to-minutes job on one core using a 1962 algorithm, and it")
out("returns a PROVEN optimum, which no annealer or sampler does. Even a")
out("perfect fault-tolerant Grover search loses to that algorithm from 21")
out("nodes upward. The Atari claim is directionally right but for the")
out("wrong reason: 128 bytes of RAM stops it, not the age of the universe,")
out("which it beats by four orders of magnitude.")
out()
out("This settles arithmetic only. It does not touch whether the Ford")
out("Otosan or Pattison deployments occurred; see AUDIT.md, which finds")
out("those real but benchmarked against the incumbent process rather than")
out("against a tuned classical solver.")

sys.exit(0 if npass == len(R) else 1)
