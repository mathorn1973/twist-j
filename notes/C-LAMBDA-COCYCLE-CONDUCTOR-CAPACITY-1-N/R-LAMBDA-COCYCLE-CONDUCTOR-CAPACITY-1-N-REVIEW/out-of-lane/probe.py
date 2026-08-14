#!/usr/bin/env python3
"""OUT OF LANE.  Numeric grid probe, NOT admissible evidence under the frozen
PREREG of C-LAMBDA-COCYCLE-CONDUCTOR-CAPACITY-1-N (no zero table is admissible).
Decision aid only.  Deterministic: no timing, no PRNG."""
from mpmath import mp, zetazero, atan, pi, nint, mpf, log10

mp.dps = 250
A_MAX = 300           # 4*5^300 ~ 10^210, ~40 digits of margin at dps=250
NZ = 30

print(f"dps={mp.dps}  A_MAX={A_MAX}  zeros=1..{NZ}")
print(f"{'n':>3} {'gamma':>22} {'min dist to grid':>20} {'argmin A':>9}")
worst = None
for n in range(1, NZ + 1):
    g = zetazero(n).imag
    theta = 2 * atan(1 / (2 * g)) / (2 * pi)      # alpha/(2 pi)
    best_d, best_A = None, None
    for A in range(0, A_MAX + 1):
        x = theta * (4 * 5**A)
        d = abs(x - nint(x))
        if best_d is None or d < best_d:
            best_d, best_A = d, A
    print(f"{n:>3} {mp.nstr(g, 18):>22} {mp.nstr(best_d, 6):>20} {best_A:>9}")
    if worst is None or best_d < worst[1]:
        worst = (n, best_d, best_A)
print(f"\nclosest approach over all {NZ} zeros and A<= {A_MAX}: "
      f"zero #{worst[0]}, dist={mp.nstr(worst[1],8)} at A={worst[2]}")
print(f"no hit  =>  B(gamma_n) > {A_MAX} for every tested zero")
print(f"implied degree bound [Q(rho):Q] >= q_B/5 = 4*5^B/5 > 4*5^{A_MAX} ~ 10^{int(A_MAX*float(log10(5)))+1}")
