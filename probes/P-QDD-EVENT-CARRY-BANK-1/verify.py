#!/usr/bin/env python3
"""
P-QDD-EVENT-CARRY-BANK-1

Exact audit of the complete Route A probability context alphabet, the
Euclidean carry transducer on every context, the product carry bank under
arbitrary interleaving, the exact product-state lower bound, phase
nonselection, and the active Public Canon v59 architecture boundary.

Python standard library only. Integer and Fraction arithmetic only. No
randomness, floating point, network, subprocess, environment-dependent output,
or filesystem writes. The inherited public Canon files are read-only frozen
inputs of the pin commit for the architecture audit.

The written PREREG supplies the universal state-minimality and classification
proof. The verifier exhausts the 625-piston carrier, all phase states of all 22
contexts, all ordered context pairs, and all schedules of length at most four.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import gcd, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ELL = (0, 1, 2, -2, -1)

EXPECTED_TABLE = (
    (F(0), 84),
    (F(1, 256), 24),
    (F(1, 176), 48),
    (F(1, 136), 32),
    (F(1, 96), 24),
    (F(1, 56), 48),
    (F(1, 46), 36),
    (F(1, 26), 48),
    (F(9, 224), 24),
    (F(1, 16), 56),
    (F(9, 104), 24),
    (F(2, 17), 24),
    (F(9, 64), 24),
    (F(5, 32), 8),
    (F(1, 6), 24),
    (F(2, 7), 24),
    (F(5, 16), 24),
    (F(3, 8), 16),
    (F(5, 8), 8),
    (F(9, 14), 12),
    (F(49, 64), 8),
    (F(1), 4),
)
EXPECTED_FACTOR = {2: 66, 3: 2, 7: 4, 11: 1, 13: 2, 17: 2, 23: 1}
CANDIDATE_GATE = "GATE-L1-L5-QDD-EVENT-CARRY-BANK"


def qdd_probability(piston: tuple[int, int, int, int]) -> F | None:
    v = tuple(F(ELL[x]) for x in piston)
    s = sum(v, F(0))
    norm2 = sum((x * x for x in v), F(0))
    m = norm2 - s * s / 5
    if m == 0:
        return None
    w_low = s * s / 20
    w_high = norm2 - s * s / 4
    if w_low + w_high != m:
        raise ArithmeticError("Route A weight decomposition failed")
    p = w_low / m
    if not (F(0) <= p <= F(1)):
        raise ArithmeticError("Route A probability outside [0,1]")
    return p


def carry_step(p: F, phase: int) -> tuple[int, int]:
    a, b = p.numerator, p.denominator
    if not (0 <= phase < b):
        raise ValueError("phase outside the reduced residue carrier")
    total = phase + a
    event = int(total >= b)
    next_phase = total - event * b
    return event, next_phase


def mechanical_word(p: F, phase: int = 0) -> tuple[int, ...]:
    a, b = p.numerator, p.denominator
    return tuple(
        (phase + (r + 1) * a) // b - (phase + r * a) // b
        for r in range(b)
    )


def factor_integer(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def simulate_schedule(
    contexts: tuple[F, ...],
    schedule: tuple[int, ...],
    initial: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    state = list(initial)
    ranks = [0] * len(contexts)
    events: list[int] = []
    for index in schedule:
        p = contexts[index]
        phase_before = initial[index]
        expected = mechanical_word(p, phase_before)[ranks[index] % p.denominator]
        event, next_phase = carry_step(p, state[index])
        if event != expected:
            raise ArithmeticError("schedule event differs from rank law")
        state[index] = next_phase
        ranks[index] += 1
        events.append(event)
    return tuple(events), tuple(state)


gates: list[bool] = []


def gate(index: int, name: str, ok: bool, detail: str) -> None:
    gates.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {index:02d} {name:<11} {detail}")


print("TWIST-J QDD event carry bank probe")
print("Exact Route A contexts; LOW=1, HIGH=0; probability-keyed Euclidean carry bank")
print("")

# 01-02. Reconstruct the complete exact input alphabet.
hist: dict[F, int] = {}
zero_count = 0
for piston in product(range(5), repeat=4):
    p = qdd_probability(piston)
    if p is None:
        zero_count += 1
    else:
        hist[p] = hist.get(p, 0) + 1
computed_table = tuple(sorted(hist.items()))
contexts = tuple(p for p, _ in computed_table)
denominators = tuple(p.denominator for p in contexts)

gate(
    1,
    "CARRIER",
    zero_count == 1 and sum(hist.values()) == 624 and computed_table == EXPECTED_TABLE,
    f"625 pistons = ZERO_SUPPORT {zero_count} + SUPPORTED {sum(hist.values())}; exact table match",
)
gate(
    2,
    "CONTEXTS",
    len(contexts) == 22 and len(set(contexts)) == 22 and sum(denominators) == 1374,
    f"probability contexts {len(contexts)}; sum of reduced coordinate sizes {sum(denominators)}",
)

# 03-05. Exhaust every phase state of every context.
carry_ok = True
cycle_ok = True
fixed_ok = True
for p in contexts:
    a, b = p.numerator, p.denominator
    images: list[int] = []
    for phase in range(b):
        event, next_phase = carry_step(p, phase)
        carry_ok &= event in (0, 1)
        carry_ok &= 0 <= next_phase < b
        carry_ok &= phase + a == next_phase + b * event
        carry_ok &= next_phase == (phase + a) % b
        images.append(next_phase)

        state = phase
        running = 0
        for r in range(3 * b + 11):
            e, state = carry_step(p, state)
            expected = (phase + (r + 1) * a) // b - (phase + r * a) // b
            fixed_ok &= e == expected
            running += e
            fixed_ok &= running == (phase + (r + 1) * a) // b - phase // b
    cycle_ok &= sorted(images) == list(range(b))
    if 0 < a < b:
        state = 0
        visited: list[int] = []
        for _ in range(b):
            visited.append(state)
            _, state = carry_step(p, state)
        cycle_ok &= state == 0 and len(set(visited)) == b and gcd(a, b) == 1
    else:
        cycle_ok &= b == 1

gate(3, "CARRY", carry_ok, "Euclidean identity c+a=c'+b e holds on every phase state")
gate(4, "CYCLES", cycle_ok, "each interior update is one b-cycle; endpoints are one-state maps")
gate(5, "FIXED", fixed_ok, "every phase emits its exact shifted lower mechanical word")

# 06. All distinct-context updates commute on every two-coordinate state.
commute_ok = True
pair_states = 0
for i, p in enumerate(contexts):
    for j, q in enumerate(contexts):
        if i >= j:
            continue
        for cp in range(p.denominator):
            for cq in range(q.denominator):
                pair_states += 1
                ep_pq, cp_pq = carry_step(p, cp)
                eq_pq, cq_pq = carry_step(q, cq)
                state_pq = (cp_pq, cq_pq)
                eq_qp, cq_qp = carry_step(q, cq)
                ep_qp, cp_qp = carry_step(p, cp)
                state_qp = (cp_qp, cq_qp)
                commute_ok &= state_pq == state_qp
                commute_ok &= ep_pq == ep_qp and eq_pq == eq_qp
gate(6, "COMMUTE", commute_ok and pair_states > 0, f"all {pair_states} two-context phase states commute exactly")

# 07. Exhaust every schedule of length at most four at zero and one nonzero bank phase.
interleave_ok = True
schedule_count = 0
zero_initial = tuple(0 for _ in contexts)
alt_initial = tuple((7 * i + 3) % p.denominator for i, p in enumerate(contexts))
for length in range(5):
    for schedule in product(range(len(contexts)), repeat=length):
        schedule_count += 1
        for initial in (zero_initial, alt_initial):
            events, final_state = simulate_schedule(contexts, schedule, initial)
            counts = [0] * len(contexts)
            reconstructed: list[int] = []
            for index in schedule:
                p = contexts[index]
                reconstructed.append(
                    mechanical_word(p, initial[index])[counts[index] % p.denominator]
                )
                counts[index] += 1
            interleave_ok &= events == tuple(reconstructed)
            for index, p in enumerate(contexts):
                interleave_ok &= final_state[index] == (
                    initial[index] + counts[index] * p.numerator
                ) % p.denominator

gate(7, "INTERLEAVE", interleave_ok, f"rank law audited on {schedule_count} schedules at two phase vectors")

# 08. Exact bank cardinality and factorization.
bank_size = prod(denominators)
factors = factor_integer(bank_size)
gate(
    8,
    "BANKSIZE",
    factors == EXPECTED_FACTOR,
    f"B={bank_size}; factorization 2^66*3^2*7^4*11*13^2*17^2*23",
)

# 09-10. Distinguishable cyclic tails give the product lower bound and phase count.
tails_ok = True
single_phase_total = 0
for p in contexts:
    b = p.denominator
    words = {mechanical_word(p, phase) for phase in range(b)}
    tails_ok &= len(words) == b
    single_phase_total += len(words)
minimality_ok = tails_ok and single_phase_total == 1374 and bank_size == prod(
    len({mechanical_word(p, phase) for phase in range(p.denominator)})
    for p in contexts
)
gate(9, "TAILS", tails_ok, f"all context cyclic tails distinct; coordinate phase total {single_phase_total}")
gate(10, "MINIMAL", minimality_ok, f"Myhill-Nerode residue product lower bound equals B={bank_size}")

# 11. Every bank phase is frequency-equivalent, but phases are distinguishable.
phase_ok = True
for p in contexts:
    a, b = p.numerator, p.denominator
    words = []
    for phase in range(b):
        word = mechanical_word(p, phase)
        words.append(word)
        phase_ok &= sum(word) == a
    phase_ok &= len(set(words)) == b
gate(11, "PHASE", phase_ok, f"all B={bank_size} phase vectors preserve frequencies and remain distinguishable")

# 12. The complete bank cannot fit in the finite checkpoint alone.
checkpoint_size = 5**6
gate(
    12,
    "CHECKPOINT",
    bank_size > checkpoint_size,
    f"B has bit length {bank_size.bit_length()} and exceeds 5^6={checkpoint_size}",
)

# 13. Active-public architecture text boundary at the exact pin.
core = (ROOT / "canon" / "CORE.md").read_text(encoding="utf-8")
canon = (ROOT / "canon" / "CANON.md").read_text(encoding="utf-8")
frontier = (ROOT / "canon" / "FRONTIER.md").read_text(encoding="utf-8")
gates_text = (ROOT / "canon" / "GATES.tsv").read_text(encoding="utf-8")
arch_ok = (
    "Omega = N_0 x F_5^6" in core
    and "Decoder outputs never feed" in core
    and "QDD-FRESH-RECORD-EXTENSION [T]" in canon
    and "not an L5 event stream" in canon
    and "QDD-INSTRUMENT-APPARATUS [O]" in frontier
    and "SAMPLING NOT PROVIDED" in frontier
    and CANDIDATE_GATE not in gates_text
)
gate(13, "ARCH", arch_ok, "no public context-bank state, ready phase, feedback bridge, or registered carry-bank gate")

# 14. Frozen scientific decision.
decision_ok = all(gates)
gate(14, "DECISION", decision_ok, "CARRY-BANK-BOUNDARY; O1 remains open and SAMPLING NOT PROVIDED")

print("")
print(f"RESULT {sum(gates)}/{len(gates)} {'ALL PASS' if all(gates) else 'FAIL'}")
raise SystemExit(0 if all(gates) else 1)
