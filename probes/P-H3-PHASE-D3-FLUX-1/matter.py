# SPDX-License-Identifier: Apache-2.0
"""Exact two-cut material Bloch transfer and finite native plane-wave controls."""

from fractions import Fraction

from native import cell, h3, ledger, put, reverse, step


ZERO, ONE, RHO = h3.ZERO, h3.ONE, h3.RHO
NEG_ONE = h3.scale(-1, ONE)
RHO2 = h3.mul(RHO, RHO)
A = h3.scale(Fraction(1, 2), h3.add(ONE, RHO))
B = h3.scale(Fraction(1, 2), h3.sub(ONE, RHO))
PHI = h3.scale(-1, h3.add(RHO, h3.RHO_INV))
NX, NY, TICKS = 8, 20, 8
TARGET, REFERENCE = 0, 4
SCALE = 2 ** TICKS


def matrix_mul(a, b):
    return tuple(tuple(h3.ring_sum(h3.mul(a[i][k], b[k][j]) for k in range(2))
                       for j in range(2)) for i in range(2))


def apply(matrix, vector):
    return tuple(h3.ring_sum(h3.mul(a, b) for a, b in zip(row, vector))
                 for row in matrix)


def diagonal(word):
    return ((word, ZERO), (ZERO, word))


def symbols(z):
    inv = h3.conj(z)
    even = ((A, B), (B, A))
    odd = ((A, h3.mul(B, inv)), (h3.mul(B, z), A))
    return even, odd, matrix_mul(odd, even)


def expected_trace(z):
    a_sq = h3.mul(A, A)
    b_sq = h3.mul(B, B)
    return h3.add(h3.scale(2, a_sq), h3.mul(b_sq, h3.add(z, h3.conj(z))))


def normalized_trace_check(z, trace):
    cos_k = h3.scale(Fraction(1, 2), h3.add(z, h3.conj(z)))
    rhs = h3.sub(h3.sub(h3.scale(2, ONE), PHI),
                 h3.mul(h3.add(PHI, h3.scale(2, ONE)), cos_k))
    return h3.scale(2, h3.mul(h3.RHO_INV, trace)) == rhs


def launch(z, coeffs):
    field = [ZERO] * (4 * NX * NY)
    multiplier = ONE
    for n in range(NY // 2):
        for offset, coeff in enumerate(coeffs):
            word = h3.mul(multiplier, coeff)
            put(field, NY, TARGET, 2 * n + offset, (word, ZERO, ZERO, ZERO))
            put(field, NY, REFERENCE, 2 * n + offset,
                (h3.scale(SCALE, ONE), ZERO, ZERO, ZERO))
        multiplier = h3.mul(multiplier, z)
    return tuple(field)


def edges_admitted(field, bit):
    return all(h3.even(h3.sub(cell(field, NY, TARGET, y)[0],
                              cell(field, NY, TARGET, (y + 1) % NY)[0]))
               for y in range(bit, NY, 2))


def power(unit, exponent):
    value = ONE
    for _ in range(exponent):
        value = h3.mul(value, unit)
    return value


def replay(label, z, seed, eigenvalue=None):
    even, odd, transfer = symbols(z)
    vector = tuple(h3.scale(SCALE, word) for word in seed)
    source = launch(z, vector)
    h3.require(power(z, NY // 2) == ONE, "compatible dimer root")
    h3.require(all(type(value) is int for word in source for value in word),
               "integral native launch")
    initial_stock = ledger(source)
    state = source
    trace = h3.add(transfer[0][0], transfer[1][1])
    det = h3.sub(h3.mul(transfer[0][0], transfer[1][1]),
                 h3.mul(transfer[0][1], transfer[1][0]))
    r0 = next(index for index, word in enumerate(seed) if word != ZERO)
    h3.require(seed[r0] == ONE, "literal unit reference ratio")
    cycles, checks, rest_subcuts = [], [], []
    admitted = True
    for tick in range(1, TICKS + 1):
        bit = (tick - 1) % 2
        admitted &= edges_admitted(state, bit)
        c, b, tags = step(state, NY, bit)
        h3.require(reverse(b, NY, bit) == state and ledger(b) == initial_stock,
                   "native inverse and complete accounts")
        vector = apply((even, odd)[bit], vector)
        expected = launch(z, vector)
        checks.append(c == b == expected and not tags)
        state = b
        if z == ONE:
            observed = cell(b, NY, TARGET, r0)[0]
            reference = cell(b, NY, REFERENCE, r0)[0]
            ratio = h3.mul(observed, h3.inverse(reference)) if reference != ZERO else None
            one_step_phase = RHO if eigenvalue == RHO2 else ONE
            rest_subcuts.append({
                "tick": tick,
                "ratio": [[v.numerator, v.denominator] for v in ratio]
                         if ratio is not None else None,
                "one_step_phase_match": ratio == power(one_step_phase, tick),
            })
        if tick % 2 == 0:
            observed = cell(b, NY, TARGET, r0)[0]
            reference = cell(b, NY, REFERENCE, r0)[0]
            ratio = h3.mul(observed, h3.inverse(reference)) if reference != ZERO else None
            cycles.append({
                "cycle": tick // 2,
                "native_ratio": [[v.numerator, v.denominator] for v in ratio]
                                if ratio is not None else None,
                "eigenratio_match": (ratio == power(eigenvalue, tick // 2)
                                     if eigenvalue is not None else None),
            })
    branch = all(row["eigenratio_match"] is not False for row in cycles)
    return {
        "label": label, "z": z, "trace": [[v.numerator, v.denominator] for v in trace],
        "trace_match": trace == expected_trace(z) and normalized_trace_check(z, trace),
        "det_rho_squared": det == RHO2,
        "staggered_double_scalar": transfer == diagonal(RHO) if z == NEG_ONE else None,
        "admitted": admitted, "transfer_matches": checks, "co_evolved_reference": cycles,
        "native_eigenratios": branch and all(row["one_step_phase_match"] for row in rest_subcuts),
        "unstaggered_native_subcuts": rest_subcuts,
    }


def run():
    rows = [
        replay("REST_UNIFORM", ONE, (ONE, ONE), ONE),
        replay("REST_OPTICAL", ONE, (ONE, NEG_ONE), RHO2),
        replay("STAGGERED_EVEN", NEG_ONE, (ONE, ZERO), RHO),
        replay("STAGGERED_ODD", NEG_ONE, (ZERO, ONE), RHO),
    ]
    for label, z in (("RHO", RHO), ("RHO_INV", h3.RHO_INV)):
        rows.extend(replay(label + suffix, z, seed) for suffix, seed in
                    (("_EVEN", (ONE, ZERO)), ("_ODD", (ZERO, ONE))))
    gold = h3.mul(PHI, PHI) == h3.add(PHI, ONE)
    return {
        "passed": gold and all(
            row["trace_match"] and row["det_rho_squared"] and row["admitted"]
            and all(row["transfer_matches"]) and row["native_eigenratios"]
            and row["staggered_double_scalar"] is not False for row in rows
        ),
        "geometry": [NX, NY], "initial_bit": 0, "native_steps": TICKS,
        "phi_identity": gold, "cases": rows,
    }
