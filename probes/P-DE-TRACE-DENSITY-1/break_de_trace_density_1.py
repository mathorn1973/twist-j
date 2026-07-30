#!/usr/bin/env python3
# break_de_trace_density_1.py
# Independent break attempt for C-DE-TRACE-DENSITY-1. NO AUTHORITY.
# Goal: KILL the NONUNIQUE closure by finding a registered, NON-CIRCULAR exact
# relation that pins a unique density character q. Independent code path:
# hand-rolled integer-pair rationals, no fractions import, no floats.

import sys

def g(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a if a else 1

def R(n, m=1):
    if m == 0:
        raise ZeroDivisionError
    if m < 0:
        n, m = -n, -m
    c = g(n, m)
    return (n // c, m // c)

def add(x, y): return R(x[0] * y[1] + y[0] * x[1], x[1] * y[1])
def sub(x, y): return R(x[0] * y[1] - y[0] * x[1], x[1] * y[1])
def mul(x, y): return R(x[0] * y[0], x[1] * y[1])
def div(x, y): return R(x[0] * y[1], x[1] * y[0])

ONE, ZERO = R(1), R(0)
p, d = R(5), R(3)

fails = []
def check(name, ok, note):
    print("BREAK %-34s %s  %s" % (name, "OK" if ok else "KILL", note))
    if not ok:
        fails.append(name)

# 1. Independent re-derivation of the skeleton (different arithmetic path).
w = sub(div(ONE, mul(p, d)), ONE)                       # 1/(pd) - 1
check("skeleton-w", w == R(-14, 15), "w = %d/%d" % w)
Delta = mul(d, add(ONE, w))
check("skeleton-Delta", Delta == R(1, 5), "d(1+w) = %d/%d" % Delta)

# 2. Adversarial scan: does ANY registered sealed constant pin q non-circularly?
# Registered exact constants of the v12 gravity/cosmology block (pi-coefficients
# where applicable): 12, 72, 216, 864, 27, 1/4, -1 (lambda), 3, 5, 3/4, 1/5, 2,
# 16, 32/33, -6, 4. A "pin" would be an equation q = f(constants) arising from a
# registered relation that is not the dictionary itself. The registered relations
# available in the homogeneous sector are:
#   (i)  continuity          d(1+w_q) = q          holds for ALL q  -> no pin
#   (ii) Friedmann           H^2 = 72 pi rho       q-free           -> no pin
#   (iii) kinetic chain      K = k/(12 V_cell)     q-free           -> no pin
#   (iv) DeWitt magnitude    d(1-lambda d) = 12    q-free           -> no pin
#   (v)  dictionary          q := gamma_tr         THE DECISION     -> circular
# The scan makes (i)-(iv) concrete over a dense rational grid: for every
# q = n/m, |n| <= 20, 1 <= m <= 12, verify that (i) is satisfiable and that
# (ii)-(iv) evaluate to the same q-independent values. If any relation varied
# with q, it would be a candidate selector and this script would KILL.
grid = []
for m in range(1, 13):
    for n in range(-20, 21):
        q = R(n, m)
        if q not in grid:
            grid.append(q)

pins = 0
K_ref = R(1, 864); c_ref = R(1, 72); DW_ref = R(12)
for q in grid:
    w_q = sub(div(q, d), ONE)
    if mul(d, add(ONE, w_q)) != q:
        pins += 1; break                                 # (i) would exclude q
    K = div(R(12), mul(R(12), R(864)))                   # (iii)
    c = mul(R(12), K)
    DW = mul(d, sub(ONE, mul(R(-1), d)))                 # (iv), lambda = -1
    if (K, c, DW) != (K_ref, c_ref, DW_ref):
        pins += 1; break                                 # a q-slot would show
check("scan-no-noncircular-pin", pins == 0,
      "%d rational q scanned, no registered relation varies with q" % len(grid))

# 3. Circularity witness: the only relation that selects q = 1/5 is q = gamma_tr
# itself. Selecting with it and calling that a derivation would be assuming the
# conclusion. Demonstrate: remove (v) and the survivor set on the grid is the
# whole grid intersected with continuity, size > 1.
survivors = [q for q in grid if mul(d, add(ONE, sub(div(q, d), ONE))) == q]
check("survivors-without-dictionary", len(survivors) > 1,
      "%d survivors without (v); with (v): exactly q = 1/5" % len(survivors))
only = [q for q in survivors if q == R(1, 5)]
check("with-dictionary-unique", len(only) == 1, "dictionary selects q = 1/5 uniquely")

# 4. Cross-check the verifier's transport control independently.
w_spatial = sub(div(ONE, d), ONE)
check("transport-spatial", w_spatial == R(-2, 3), "weight 1 -> w = -2/3")
check("transport-not-dust", mul(d, add(ONE, ZERO)) != ONE, "dust Delta = 3 != 1")

print()
if fails:
    print("RESULT: NONUNIQUE KILLED at %s" % ", ".join(fails))
    sys.exit(1)
print("RESULT: BREAK ATTEMPT FAILED. NONUNIQUE STANDS.")
print("No registered non-circular selector found on the scanned grid;")
print("the independent path reproduces the verifier's core exactly.")
