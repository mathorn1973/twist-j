#!/usr/bin/env python3
"""Static anatomy of the frozen QDD target law and of the Canon v49 selector.

NON-CANONICAL incubation-lane script for notes/C-QDD-U-INDUCED-NULL-ANATOMY-1-N.
It is not a public probe and claims no POLICY section 4 two-architecture gate.

Everything computed here is definitional arithmetic on formulas published in
Public Canon v49 (sections 2, 3, KERNEL-Z6-SYNCHRONIZATION, DEF-QDD-*), plus
two arithmetic consequences of published probe counts.  No orbit is iterated,
no window is read and no seed is swept.

Gates A1 to A6 use only Canon formulas and reproduce the published Canon-level
audit expectations 313 / 25 / 22 as a transcription check.  Gate A7 additionally
consumes one published integer of P-QDD-INSTRUMENT-U-INDUCED-1, the C8 count
SEED-DEPENDENT-271350, and derives a bound on that probe's own unpublished
restricted quantifier; its two displayed forms are algebraically equivalent
readings of that one count, not independent evidence.  Gate A8 uses only the
Canon target law and the two frozen window lengths, and publishes the
divisibility data a later probe needs; it asserts no unreachability, because
the decisive test is dynamic and per seed.

Python 3 standard library only.  Exact integers and Fractions.  Deterministic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

MOD = 5
ELL = {0: 0, 1: 1, 2: 2, 3: -2, 4: -1}
BALANCED = tuple(ELL[i] for i in range(MOD))

CD = (2, 1, 3, 4, 1, 1)
VE = (0, 0, 0, 0, 1, 0)
S_C = (2, 1, 2, 1)
U_C = (0, 1, 0, -1)

LAMBDAS = ((1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4))

CANON_SHEET_TABLE = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))

PAIRS = 900
SEED_DEPENDENT_C8 = 271350

failures = 0


def gate(name: str, ok: bool, detail: str) -> None:
    global failures
    if not ok:
        failures += 1
    print(f"{'PASS' if ok else 'FAIL'} {name} {detail}")


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p) % MOD, (-p4p) % MOD, (-p1) % MOD, (-p4) % MOD,
            (-q) % MOD, (-r) % MOD)


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % MOD, (-p4p) % MOD, (-p1) % MOD, (-p4) % MOD)
    piston = tuple((b4[i] + S_C[i] + r * U_C[i]) % MOD for i in range(4))
    return piston + ((1 - q) % MOD, (-r) % MOD)


def gen_d(x):
    return tuple((CD[i] - x[i]) % MOD for i in range(6))


def gen_e(x):
    return tuple(((CD[i] + VE[i]) - x[i]) % MOD for i in range(6))


GENERATORS = (gen_a, gen_b, gen_c, gen_d, gen_e)
GENERATOR_NAMES = "abcde"

STATES = tuple(tuple(t) for t in product(range(MOD), repeat=6))


def piston_sum(x):
    return (x[0] + x[1] + x[2] + x[3]) % MOD


def fiber_sum(x):
    return (x[4] + x[5]) % MOD


def z6(x):
    return sum(x) % MOD


def beta(x):
    return tuple(ELL[x[i]] for i in range(4))


def negate(v):
    return tuple(-t for t in v)


def m_form(v):
    return sum(t * t for t in v) - Fraction(1, 5) * sum(v) ** 2


def w_low(v):
    return Fraction(1, 20) * sum(v) ** 2


def w_high(v):
    return sum(t * t for t in v) - Fraction(1, 4) * sum(v) ** 2


def compose(*maps):
    def applied(x):
        for f in reversed(maps):
            x = f(x)
        return x
    return applied


# ---------------------------------------------------------------- A1
identity_ok = True
for name, g in zip(GENERATOR_NAMES, GENERATORS):
    if any(g(g(x)) != x for x in STATES):
        identity_ok = False
bc = compose(gen_b, gen_c)
power = list(STATES)
order_ok = True
current = {x: x for x in STATES}
for _ in range(5):
    current = {x: bc(v) for x, v in current.items()}
order_ok = all(current[x] == x for x in STATES)
bc4 = {x: x for x in STATES}
for _ in range(4):
    bc4 = {x: bc(v) for x, v in bc4.items()}
order_exact = order_ok and any(bc4[x] != x for x in STATES)
gate("A1 GENERATORS",
     identity_ok and order_exact,
     f"states={len(STATES)} involutions={'YES' if identity_ok else 'NO'} "
     f"bc_order_5={'EXACT' if order_exact else 'NO'}")

# ---------------------------------------------------------------- A2
classes = {}
for v in product(BALANCED, repeat=4):
    classes.setdefault(min(v, negate(v)), []).append(v)
zero_rep = (0, 0, 0, 0)
nonzero_reps = sorted(rep for rep in classes if rep != zero_rep)
class_id = {rep: index + 1 for index, rep in enumerate(nonzero_reps)}
zero_checkpoints = sum(1 for x in STATES if beta(x) == zero_rep)
occ_values = {(w_low(rep) / m_form(rep), w_high(rep) / m_form(rep))
              for rep in nonzero_reps}
gate("A2 CLASSES",
     len(classes) == 313 and zero_checkpoints == 25 and len(occ_values) == 22,
     f"classes={len(classes)} zero_checkpoints={zero_checkpoints} "
     f"oriented_pre_cells={1 + 2 * len(nonzero_reps)} "
     f"nonzero_occ_values={len(occ_values)}")

# ---------------------------------------------------------------- A3
low_zero = [class_id[rep] for rep in nonzero_reps if w_low(rep) == 0]
high_zero = [class_id[rep] for rep in nonzero_reps if w_high(rep) == 0]
both_positive = [class_id[rep] for rep in nonzero_reps
                 if w_low(rep) != 0 and w_high(rep) != 0]
disjoint = not (set(low_zero) & set(high_zero))
partition_ok = len(low_zero) + len(high_zero) + len(both_positive) == 312
m_positive = all(m_form(rep) > 0 for rep in nonzero_reps)
gate("A3 ZERO_TARGET",
     disjoint and partition_ok and m_positive
     and len(low_zero) == 42 and len(high_zero) == 2,
     f"low_zero={len(low_zero)} high_zero={len(high_zero)} "
     f"both_positive={len(both_positive)} disjoint=YES m_positive=YES")
print("LOW-ZERO-CLASSES " + ",".join(str(i) for i in low_zero))
print("HIGH-ZERO-CLASSES " + ",".join(
    f"{i}:{''.join(str(t) for t in nonzero_reps[i - 1])}" for i in high_zero))

# ---------------------------------------------------------------- A4
piston_closed = True
fiber_closed = True
piston_maps = []
fiber_maps = []
for g in GENERATORS:
    p_map = {}
    f_map = {}
    for x in STATES:
        key_p, val_p = piston_sum(x), piston_sum(g(x))
        key_f, val_f = fiber_sum(x), fiber_sum(g(x))
        if p_map.setdefault(key_p, val_p) != val_p:
            piston_closed = False
        if f_map.setdefault(key_f, val_f) != val_f:
            fiber_closed = False
    piston_maps.append(tuple(p_map[i] for i in range(MOD)))
    fiber_maps.append(tuple(f_map[i] for i in range(MOD)))
gate("A4 SPLIT_CLOSURE",
     piston_closed and fiber_closed,
     f"piston_sum_closed={'YES' if piston_closed else 'NO'} "
     f"fiber_sum_closed={'YES' if fiber_closed else 'NO'}")
for name, p_map, f_map in zip(GENERATOR_NAMES, piston_maps, fiber_maps):
    print(f"SPLIT-MAP {name} S->{''.join(str(t) for t in p_map)} "
          f"s->{''.join(str(t) for t in f_map)}")

# ---------------------------------------------------------------- A5
sheet_ok = True
derived = []
for theta in (0, 1):
    row = []
    for z in range(MOD):
        selector = (z + 2 * theta) % MOD
        witness = next(x for x in STATES if z6(x) == z)
        row.append(z6(GENERATORS[selector](witness)))
        for x in STATES:
            if z6(x) == z and z6(GENERATORS[selector](x)) != row[-1]:
                sheet_ok = False
    derived.append(tuple(row))
sheet_ok = sheet_ok and tuple(derived) == CANON_SHEET_TABLE
recovered = all(
    (piston_maps[i][piston_sum(x)] + fiber_maps[i][fiber_sum(x)]) % MOD
    == z6(GENERATORS[i](x))
    for i in range(5) for x in STATES)
gate("A5 SHEET_TABLE",
     sheet_ok and recovered,
     f"t0={''.join(str(t) for t in derived[0])} "
     f"t1={''.join(str(t) for t in derived[1])} "
     f"canon_match={'YES' if tuple(derived) == CANON_SHEET_TABLE else 'NO'} "
     f"z6_is_S_plus_s={'YES' if recovered else 'NO'}")

# ---------------------------------------------------------------- A6
autonomous = []
for alpha, gamma in LAMBDAS:
    ok = True
    for g in GENERATORS:
        seen = {}
        for x in STATES:
            key = (alpha * x[4] + gamma * x[5]) % MOD
            val = (alpha * g(x)[4] + gamma * g(x)[5]) % MOD
            if seen.setdefault(key, val) != val:
                ok = False
    autonomous.append(ok)
selector_coupled = [index for index, pair in enumerate(LAMBDAS)
                    if pair == (1, 1)]
gate("A6 FIBER_FUNCTIONALS",
     all(autonomous) and selector_coupled == [2],
     f"autonomous={sum(autonomous)}/6 "
     f"selector_coupled_index=L{selector_coupled[0]} "
     f"selector_coupled_form=q+r")
for index, (alpha, gamma) in enumerate(LAMBDAS):
    print(f"LAMBDA L{index} ({alpha},{gamma}) "
          f"autonomous={'YES' if autonomous[index] else 'NO'} "
          f"in_selector={'YES' if (alpha, gamma) == (1, 1) else 'NO'}")

# ---------------------------------------------------------------- A7
total_triples = PAIRS * len(classes)
independent = total_triples - SEED_DEPENDENT_C8
complement_form = independent // len(both_positive)
off_pos = (1 + len(low_zero) + len(high_zero)) * PAIRS
inside_pos = SEED_DEPENDENT_C8 - off_pos
pigeonhole_form = PAIRS - -(-inside_pos // len(both_positive))
gate("A7 SEED_BOUND",
     independent == 10350 and complement_form == 38
     and pigeonhole_form == complement_form,
     f"triples={total_triples} dependent={SEED_DEPENDENT_C8} independent={independent} "
     f"pos_classes={len(both_positive)} complement_form={complement_form} "
     f"pigeonhole_form={pigeonhole_form} forms_independent=NO")
print("SEED-BOUND POS-REALIZED-SINGLE<=38 "
      "note=the two forms are algebraically equivalent readings of the single "
      "published C8 count and are not independent evidence")

# ---------------------------------------------------------------- A8
denominators = {}
for rep in nonzero_reps:
    low = w_low(rep) / m_form(rep)
    high = w_high(rep) / m_form(rep)
    assert low.denominator == high.denominator
    denominators[class_id[rep]] = low.denominator
pos_denominators = sorted(denominators[i] for i in both_positive)
total_denominator = sum(pos_denominators)


def visit_cap(window, multiplicity):
    used = 0
    count = 0
    for q in sorted(pos_denominators * multiplicity):
        if used + q <= window:
            used += q
            count += 1
    return count


caps = {(w, k): visit_cap(w, k) for w in (1536, 14336) for k in (1, 2)}
gate("A8 DIVISIBILITY_DATA",
     total_denominator == 19688 and min(pos_denominators) == 6
     and max(pos_denominators) == 256
     and sum(1 for q in pos_denominators if q >= 6) == 268
     and sum(1 for q in pos_denominators if q >= 8) == 244
     and caps[(1536, 1)] == 107 and caps[(14336, 1)] == 245
     and caps[(1536, 2)] == 138 and caps[(14336, 2)] == 401
     and all(denominators[i] == 1 for i in low_zero + high_zero),
     f"pos_denominator_sum={total_denominator} min_q=6 max_q=256 "
     f"q_ge_6={sum(1 for q in pos_denominators if q >= 6)} "
     f"q_ge_8={sum(1 for q in pos_denominators if q >= 8)} "
     f"zero_target_denominator=1")
print(f"VISIT-CAP W=1536 classes<={caps[(1536, 1)]}/268 "
      f"oriented_cells<={caps[(1536, 2)]}/536")
print(f"VISIT-CAP W2=14336 classes<={caps[(14336, 1)]}/268 "
      f"oriented_cells<={caps[(14336, 2)]}/536")
print("VISIT-CAP note=these bound how many positive classes a realizing seed "
      "may VISIT; REAL-POS quantifies only over visited classes, so they are "
      "weak certificates and assert no unreachability")
histogram = {}
for q in pos_denominators:
    histogram[q] = histogram.get(q, 0) + 1
print("POS-DENOMINATORS " + ",".join(
    f"{q}:{n}" for q, n in sorted(histogram.items())))

print(f"SUMMARY {8 - failures}/8 {'ALL PASS' if failures == 0 else 'FAIL'}")
raise SystemExit(1 if failures else 0)
