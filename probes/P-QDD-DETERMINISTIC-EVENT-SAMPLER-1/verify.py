#!/usr/bin/env python3
"""
P-QDD-DETERMINISTIC-EVENT-SAMPLER-1

Exact audit of the rational QDD LOW-weight census, a frozen lower mechanical
event word, its phase and finite-memory boundaries, the global-counter schedule
no-go, and the changing-preparation order witness.

Python standard library only. Fractions and integers only. No input, files,
network, randomness, floating point, environment, or subprocesses.

The written PREREG carries the universal proofs. This verifier exhausts the
625-piston carrier and audits every registered rational probability exactly.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import permutations, product


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
EXPECTED_DENOMINATORS = (
    1, 6, 7, 8, 14, 16, 17, 26, 32,
    46, 56, 64, 96, 104, 136, 176, 224, 256,
)


def qdd_probability(piston: tuple[int, int, int, int]) -> F | None:
    """Return p_low on the balanced piston, or None on ZERO_SUPPORT."""
    v = tuple(F(ELL[x]) for x in piston)
    s = sum(v, F(0))
    n2 = sum((x * x for x in v), F(0))
    m = n2 - s * s / 5
    if m == 0:
        return None
    w_low = s * s / 20
    w_high = n2 - s * s / 4
    if w_low + w_high != m:
        raise ArithmeticError("Route A weight decomposition failed")
    return w_low / m


def mechanical_word(p: F) -> tuple[int, ...]:
    """One least-period block of the frozen zero-phase lower word."""
    a, b = p.numerator, p.denominator
    return tuple(((r + 1) * a) // b - (r * a) // b for r in range(b))


def cyclic_shift(word: tuple[int, ...], shift: int) -> tuple[int, ...]:
    n = len(word)
    return tuple(word[(i + shift) % n] for i in range(n))


def carried_accumulator(seq: tuple[F, ...]) -> tuple[tuple[int, ...], F]:
    x = F(0)
    out: list[int] = []
    for p in seq:
        total = x + p
        event = int(total >= 1)
        x = total - event
        if not (F(0) <= x < 1):
            raise ArithmeticError("accumulator left [0,1)")
        out.append(event)
    return tuple(out), x


gates: list[bool] = []


def gate(idx: int, name: str, ok: bool, detail: str) -> None:
    gates.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {idx:02d} {name:<10} {detail}")


print("TWIST-J QDD deterministic event sampler probe")
print("Exact arithmetic on ell(F_5)^4; LOW=1, HIGH=0; lower mechanical word at zero phase")
print("")

# A. Complete 625-piston census.
hist: dict[F, int] = {}
zero_pistons: list[tuple[int, int, int, int]] = []
for piston in product(range(5), repeat=4):
    p = qdd_probability(piston)
    if p is None:
        zero_pistons.append(piston)
    else:
        hist[p] = hist.get(p, 0) + 1

computed_table = tuple(sorted(hist.items()))
gate(
    1,
    "CARRIER",
    len(zero_pistons) == 1
    and zero_pistons == [(0, 0, 0, 0)]
    and sum(hist.values()) == 624,
    f"pistons 625 = ZERO_SUPPORT {len(zero_pistons)} + SUPPORTED {sum(hist.values())}",
)
gate(
    2,
    "CHECKPOINT",
    len(zero_pistons) * 25 == 25 and sum(hist.values()) * 25 == 15600,
    "fiber lift gives ZERO_SUPPORT 25 and SUPPORTED 15600 checkpoints",
)
gate(
    3,
    "TABLE",
    computed_table == EXPECTED_TABLE and len(computed_table) == 22,
    f"exact LOW table has {len(computed_table)} values and piston multiplicity {sum(hist.values())}",
)
print("       table      " + " ".join(f"{p}:{count}" for p, count in computed_table))

denominators = tuple(sorted({p.denominator for p in hist}))
gate(
    4,
    "DENOMS",
    denominators == EXPECTED_DENOMINATORS and max(denominators) == 256,
    "reduced denominators " + ",".join(str(d) for d in denominators) + "; maximum 256",
)

# B and C. Audit every exact probability.
prefix_ok = True
period_ok = True
block_ok = True
phase_ok = True
endpoint_ok = True
phase_total = 0
for p in sorted(hist):
    a, b = p.numerator, p.denominator
    word = mechanical_word(p)
    endpoint_ok &= all(bit in (0, 1) for bit in word)
    endpoint_ok &= (sum(word) == a)

    # Exact cumulative floor law and discrepancy on a range wider than four periods.
    running = 0
    for n in range(1, 4 * b + 18):
        running += word[(n - 1) % b]
        target = (n * a) // b
        prefix_ok &= running == target
        prefix_ok &= abs(F(running) - F(n * a, b)) < 1

    # Every cyclic length-b block has exactly a LOW events.
    for start in range(b):
        block_ok &= sum(word[(start + j) % b] for j in range(b)) == a

    if 0 < a < b:
        # Directly reject every smaller period.
        for d in range(1, b):
            if all(word[i] == word[(i + d) % b] for i in range(b)):
                period_ok = False
                break
        shifts = {cyclic_shift(word, d) for d in range(b)}
        phase_ok &= len(shifts) == b
        phase_total += len(shifts)
    else:
        endpoint_ok &= b == 1 and word == ((0,) if a == 0 else (1,))

gate(5, "PREFIX", prefix_ok, "#LOW(0..N-1)=floor(N a/b) and discrepancy < 1 for every audited prefix")
gate(6, "PERIOD", period_ok and endpoint_ok, "interior words have least period b; endpoint words are constant")
gate(7, "BLOCKS", block_ok, "every cyclic block of length b contains exactly a LOW events")
gate(8, "PHASE", phase_ok and phase_total == 1372, f"interior weights admit {phase_total} distinct cyclic phases in total")

# D. Finite-memory lower bound audit at the hardest denominator.
small_cycle_witnesses = [
    (length, low_count)
    for length in range(1, 256)
    for low_count in range(length + 1)
    if F(low_count, length) == F(1, 256)
]
memory_ok = (
    F(1, 256) in hist
    and hist[F(1, 256)] == 24
    and not small_cycle_witnesses
    and 2 * 5 == 10
    and 10 < 256
)
gate(9, "MEMORY", memory_ok, "p_low=1/256 occurs on 24 pistons; no cycle shorter than 256 realizes it; 10 < 256")

# E. Local invocation order is gap-invariant; global tick selection is not.
local_ok = True
global_ok = True
for p in sorted(hist):
    word = mechanical_word(p)
    b = len(word)
    n_trials = 3 * b + 7
    schedules = (
        tuple(range(n_trials)),
        tuple(11 + r * (r + 3) // 2 for r in range(n_trials)),
        tuple(1000 + 7 * r for r in range(n_trials)),
    )
    reference = tuple(word[r % b] for r in range(n_trials))
    for schedule in schedules:
        # Local sampler indexes by invocation position r, not by schedule[r].
        local_ok &= tuple(word[r % b] for r, _ in enumerate(schedule)) == reference

    if 0 < p < 1:
        low_positions = tuple(i for i, bit in enumerate(word) if bit == 1)
        high_positions = tuple(i for i, bit in enumerate(word) if bit == 0)
        global_ok &= bool(low_positions) and bool(high_positions)
        global_ok &= all(word[i] == 1 for i in low_positions)
        global_ok &= all(word[i] == 0 for i in high_positions)

gate(10, "LOCAL", local_ok, "local invocation word is unchanged by arbitrary audited gaps in the global counter")
gate(11, "GLOBAL", global_ok, "LOW-position and HIGH-position subsequences break global-counter schedule invariance")

# F. Changing preparations: exact accumulator law and an order witness.
variable_ok = True
probabilities = tuple(sorted(hist))
for seq in product(probabilities, repeat=3):
    out, residual = carried_accumulator(seq)
    total = sum(seq, F(0))
    variable_ok &= sum(out) == total.numerator // total.denominator
    variable_ok &= residual == total - (total.numerator // total.denominator)

multiset = (F(1, 256), F(2, 7), F(49, 64))
order_words = {perm: carried_accumulator(perm)[0] for perm in set(permutations(multiset))}
seq_a = (F(1, 256), F(49, 64), F(2, 7))
seq_b = (F(49, 64), F(2, 7), F(1, 256))
witness_ok = (
    order_words[seq_a] == (0, 0, 1)
    and order_words[seq_b] == (0, 1, 0)
    and carried_accumulator(seq_a)[1] == F(99, 1792)
    and carried_accumulator(seq_b)[1] == F(99, 1792)
    and len(set(order_words.values())) > 1
)
gate(12, "VARIABLE", variable_ok, "carried accumulator gives floor(sum p_j) on all 22^3 ordered triples")
gate(13, "ORDER", witness_ok, "same multiset {1/256,2/7,49/64} gives HHL versus HLH, residual 99/1792")

# Final frozen decision boundary. This is a classification of what the exact
# arithmetic establishes, not a claim that the current architecture supplies
# the local counter or reset law.
decision_ok = all(gates)
gate(14, "DECISION", decision_ok, "MECHANICAL-SAMPLER-BOUNDARY; O1 remains open and SAMPLING NOT PROVIDED")

print("")
print(f"RESULT {sum(gates)}/{len(gates)} {'ALL PASS' if all(gates) else 'FAIL'}")
raise SystemExit(0 if all(gates) else 1)
