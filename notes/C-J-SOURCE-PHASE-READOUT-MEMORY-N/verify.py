#!/usr/bin/env python3
"""Exact local checks for C-J-SOURCE-PHASE-READOUT-MEMORY-N.

Python 3.10+, standard library only. No network, no float tolerance, no random
sampling, no native U kernel, no Canon mutation. Run without -O.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import product
import model as a


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def qscale(c: Q, x):
    return tuple(c * y for y in x)


def phase_kernel(eigen: int, initial: int, output: int):
    total = tuple(Q(0) for _ in range(4))
    for t in range(5):
        term = a.power(a.ZETA, (t * (eigen + initial - output)) % 5)
        total = tuple(x + y for x, y in zip(total, term))
    return qscale(Q(1, 5), total)


def matmul(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(len(y)))
             for j in range(len(y[0]))] for i in range(len(x))]


def identity(n: int):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def det(m):
    m = [[Q(x) for x in row] for row in m]
    n = len(m)
    out = Q(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if m[i][k] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            out = -out
        p = m[k][k]
        out *= p
        for i in range(k + 1, n):
            f = m[i][k] / p
            for j in range(k + 1, n):
                m[i][j] -= f * m[k][j]
            m[i][k] = 0
    return out


def main() -> None:
    if not __debug__:
        raise RuntimeError("Run verify.py without Python -O.")

    require(a.mul(a.J, a.J_INV) == a.ONE, "J inverse")
    require(a.add(a.J, a.J_INV) == a.sub(a.ONE, a.ZETA),
            "J + J^-1 identity")
    for v in product(range(-2, 3), repeat=4):
        require(a.multiply_j(v) == a.mul(a.J, v), "J integer matrix")
        require(a.multiply_j_inverse(a.multiply_j(v)) == v, "J inverse matrix")
    print("PASS: exact J arithmetic and integer carrier matrix/inverse on 625 signed addresses")

    states = tuple(product(range(5), repeat=4))
    eps = a.sub(a.ZETA, a.ONE)
    require(a.residue(a.power(eps, 4)) == a.ZERO, "epsilon^4 mod 5")
    require(a.residue(a.power(eps, 3)) != a.ZERO, "epsilon^3 nonzero mod 5")
    require(a.residue(a.power(a.J, 5)) == (2, 0, 0, 0), "J^5 mod 5")
    require(a.residue(a.power(a.J, 10)) == (4, 0, 0, 0), "J^10=-1 mod 5")
    require(a.residue(a.power(a.J, 20)) == a.ONE, "J^20 mod 5")
    require(all(a.residue(a.power(a.J, k)) != a.ONE for k in range(1, 20)),
            "exact order 20")
    print("PASS: O/5O ramification witness and exact order 20 of J modulo 5")

    for source in a.SOURCE_ALPHABET:
        outputs = set()
        for carrier in states:
            dest = a.residue(a.step(carrier, source))
            outputs.add(dest)
            require(a.residue(a.step_inverse(dest, source)) == carrier,
                    "fixed-source inverse")
        require(len(outputs) == 625, "fixed-source permutation")
    print("PASS: all 15,625 fixed-source/carrier finite-ring transitions and inverses")

    pairing = [[0, 0, 0, 1], [0, 0, 1, -1], [0, 1, -1, 0], [1, -1, 0, 0]]
    inverse_pairing = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
    require(det(pairing) == 1, "trace-pairing determinant")
    require(matmul(pairing, inverse_pairing) == identity(4), "trace-pairing inverse")
    for eig, initial, output in product(range(5), repeat=3):
        expected = tuple(Q(x) for x in (a.ONE if output == (eig + initial) % 5 else a.ZERO))
        require(phase_kernel(eig, initial, output) == expected, "phase kernel")
    for carrier in states:
        require(a.read_residue_to_pointer(carrier) == carrier, "four-coordinate residue read")
    print("PASS: determinant-one trace pairing and all 125 exact cyclotomic phase-reader entries")

    lm = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
    require(det(lm) == 1, "det L")
    blocks = tuple(product(a.SOURCE_ALPHABET, repeat=2))
    checked = 0
    for carrier in states:
        seen = set()
        for s0, s1 in blocks:
            dest = a.residue(a.step(a.step(carrier, s0), s1))
            seen.add(dest)
            delta = a.residue(a.sub(dest, a.multiply_j(a.multiply_j(carrier))))
            expected = a.residue(s0 + s1)
            require(a.residue(a.block_decode(delta)) == expected, "Theorem A decode")
            new_ref, ptr, archive = a.record_gates(dest, carrier, a.ZERO, a.ZERO)
            require(new_ref == dest, "reference stores final residue")
            require(ptr == a.ZERO, "pointer reset")
            require(archive == expected, "archive stores decoded source block")
            require(a.record_gates_inverse(dest, new_ref, ptr, archive) ==
                    (carrier, a.ZERO, a.ZERO), "whole-cycle inverse")
            checked += 1
        require(len(seen) == 625, "two-step residue reachability")
    print(f"PASS: Theorem A and complete record cycle on all {checked:,} initial-residue/source blocks")
    print("PASS: register semantics -- reference holds carrier residue; archive holds source block")

    general = 0
    for i, carrier in enumerate(states):
        for t in range(20):
            reference = states[(7 * i + 3 * t) % 625]
            pointer = states[(11 * i + 17 * t + 23) % 625]
            memory = states[(13 * i + 19 * t + 41) % 625]
            out = a.record_gates(carrier, reference, pointer, memory)
            require(a.record_gates_inverse(carrier, *out) == (reference, pointer, memory),
                    "arbitrary-register inverse")
            general += 1
    print(f"PASS: {general:,} deterministic arbitrary-register inverse checks")

    # Exact three-step collisions from zero.
    zero_words = []
    for s0, s1, s2 in product(a.SOURCE_ALPHABET, repeat=3):
        x = a.ZERO
        for s in (s0, s1, s2):
            x = a.step(x, s)
        if x == a.ZERO:
            zero_words.append((s0, s1, s2))
    require(len(zero_words) == 13, "length-three zero-return census")
    require(((1, 0), (-1, 1), (1, 0)) in zero_words, "displayed collision")
    pulse_identity = a.add(a.add(a.power(a.J, 2), a.mul(a.J, a.sub(a.ZETA, a.ONE))), a.ONE)
    require(pulse_identity == a.ZERO, "three-step identity")
    print("PASS: exactly 13 length-three zero-return words; displayed nonzero collision included")

    counts = Counter({a.ZERO: 1})
    expected_counts = (25, 625, 5449, 27233)
    for n in range(1, 5):
        new = Counter()
        for x, multiplicity in counts.items():
            for source in a.SOURCE_ALPHABET:
                new[a.step(x, source)] += multiplicity
        counts = new
        require(sum(counts.values()) == 25 ** n, "word census")
        require(len(counts) == expected_counts[n - 1], "endpoint census")
        print(f"PASS: length {n}: {25**n:,} source words -> {len(counts):,} exact endpoints")

    pulse = a.Apparatus()
    quiet = a.Apparatus()
    pulse.run_block((1, 0), (-1, 1)); pulse.run_block((1, 0), (0, 0))
    quiet.run_block((0, 0), (0, 0)); quiet.run_block((0, 0), (0, 0))
    require(pulse.carrier == quiet.carrier == a.ZERO, "equal final carrier")
    require(pulse.archive != quiet.archive, "history retained in archive")
    print("PASS: equal exact final carriers can coexist with different archives")

    sequence = [a.SOURCE_ALPHABET[(7 * n + n * n) % 25] for n in range(256)]
    long = a.Apparatus((3, -2, 5, 1))
    for n in range(0, len(sequence), 2):
        long.run_block(sequence[n], sequence[n + 1])
    require(long.recovered_symbols() == sequence, "256-input archive recovery")
    require(long.reconstruct_carrier() == long.carrier, "integer history reconstruction")
    require(long.pointer == a.ZERO and long.reference == a.residue(long.carrier),
            "final ready state")
    print("PASS: 256-input integer history, growing archive, ready pointer and synchronized reference")

    alias0 = a.Apparatus(a.ZERO)
    alias5 = a.Apparatus((5, 0, 0, 0))
    for n in range(0, 20, 2):
        alias0.run_block(sequence[n], sequence[n + 1])
        alias5.run_block(sequence[n], sequence[n + 1])
    require(alias0.archive == alias5.archive, "fixed-modulus aliases have same source records")
    require(alias0.carrier != alias5.carrier, "mod-five readout is not full carrier")
    print("PASS: negative control -- modulo-five readout does not resolve initial 5O aliases")

    require(sum((k - l) ** 2 for k in range(5) for l in range(5)) == 100,
            "phase-error coefficient")
    print("PASS: exact phase-error coefficient sum_(k,l)(k-l)^2 = 100")

    actual = a.ZERO
    reference = a.ZERO
    previous_error = a.ZERO
    wrong_blocks = []
    for k in range(8):
        s0 = a.SOURCE_ALPHABET[(3 * k + 1) % 25]
        s1 = a.SOURCE_ALPHABET[(7 * k + 2) % 25]
        actual = a.step(a.step(actual, s0), s1)
        error = (1, 0, 0, 0) if k == 3 else a.ZERO
        reference, pointer, record = a.record_gates(actual, reference, error, a.ZERO)
        discrepancy = a.residue(a.sub(record, a.residue(s0 + s1)))
        expected = a.residue(a.block_decode(a.sub(error,
            a.multiply_j(a.multiply_j(previous_error)))))
        require(discrepancy == expected, "two-block error locality")
        require(reference == a.residue(a.add(actual, error)), "reference state")
        require(pointer == a.ZERO, "pointer reset under injected digital error")
        if discrepancy != a.ZERO:
            wrong_blocks.append(k)
        previous_error = error
    require(wrong_blocks == [3, 4], "one injected error affects two adjacent records")
    print("PASS: injected digital read error affects only two adjacent records in the exact witness")

    def mock_kernel(n: int, psi: tuple[int, ...]):
        return n + 1, tuple((x + 1) % 5 for x in psi)

    psi = (0, 1, 2, 3, 4, 0)
    extended = a.extend_native_step(0, psi, a.ONE, mock_kernel)
    require(extended[:2] == mock_kernel(0, psi), "native projection")
    require(extended[2] == a.step(a.ONE, (0, 1)), "chosen port adapter")
    print("PASS: read-only adapter API with a MOCK kernel; native U not supplied or tested")

    print("SCOPE: exact local construction under stated apparatus choices.")
    print("NOT CLAIMED: native realization, Born derivation, event law, endpoint lower bound, Canon update, or public pin.")


if __name__ == "__main__":
    main()
