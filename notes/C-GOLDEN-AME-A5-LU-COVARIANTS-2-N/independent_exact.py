#!/usr/bin/env python3
"""Exact Q(zeta_40) lift of the first independent n=4 hard witness.

The computation reconstructs each diagonal entry from evaluations at all 16
primitive 40th roots over four split finite fields.  A fifth split field and
a different binary contraction order verify the reconstruction.  A separate
nonnegative support contraction proves all off-diagonal entries vanish before
any finite-field cancellation is possible.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

import independent_mod41 as audit


UNITS40 = (1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39)
DEG = 16
DEN = 10**8


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # More than sufficient here (all candidates are below 2^32).
    for a in (2, 3, 5, 7, 11):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def split_primes(count: int, start: int = 1_000_001) -> list[int]:
    n = start + ((1 - start) % 40)
    ans = []
    while len(ans) < count:
        if is_prime(n):
            ans.append(n)
        n += 40
    return ans


def primitive_40_root(p: int) -> int:
    for seed in range(2, p):
        z = pow(seed, (p - 1) // 40, p)
        if pow(z, 40, p) == 1 and pow(z, 20, p) != 1 and pow(z, 8, p) != 1:
            return z
    raise ValueError(f"no primitive 40th root mod {p}")


def solve_mod(a: list[list[int]], b: list[int], p: int) -> list[int]:
    aug = [[int(x) % p for x in row] + [int(y) % p] for row, y in zip(a, b)]
    n = len(aug)
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        inv = pow(aug[col][col], p - 2, p)
        aug[col] = [x * inv % p for x in aug[col]]
        for r in range(n):
            if r == col or aug[r][col] == 0:
                continue
            factor = aug[r][col]
            aug[r] = [(x - factor * y) % p for x, y in zip(aug[r], aug[col])]
    return [aug[i][-1] for i in range(n)]


def interpolate_primitive(values: list[int], base_z: int, p: int) -> list[int]:
    roots = [pow(base_z, u, p) for u in UNITS40]
    vandermonde = [[pow(r, j, p) for j in range(DEG)] for r in roots]
    return solve_mod(vandermonde, values, p)


def crt_pair(x: int, modulus: int, residue: int, p: int) -> tuple[int, int]:
    k = ((residue - x) % p) * pow(modulus % p, p - 2, p) % p
    return x + modulus * k, modulus * p


def reduce40(raw: list[int]) -> tuple[int, ...]:
    """Reduce modulo Phi_40=x^16-x^12+x^8-x^4+1."""
    a = list(raw)
    if len(a) < DEG:
        a.extend([0] * (DEG - len(a)))
    for k in range(len(a) - 1, DEG - 1, -1):
        c = a[k]
        if c:
            # x^16 = x^12 - x^8 + x^4 - 1.
            a[k - 4] += c
            a[k - 8] -= c
            a[k - 12] += c
            a[k - 16] -= c
        a[k] = 0
    return tuple(a[:DEG])


def kmul(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    raw = [0] * (2 * DEG - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            raw[i + j] += a * b
    return reduce40(raw)


def kadd(*xs: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(x[i] for x in xs) for i in range(DEG))


def kscale(x: tuple[int, ...], n: int) -> tuple[int, ...]:
    return tuple(n * a for a in x)


def kconjugate(x: tuple[int, ...]) -> tuple[int, ...]:
    return kadd(*(kscale(monomial(-i), a) for i, a in enumerate(x) if a))


def keval(x: tuple[int, ...], z: int, p: int) -> int:
    ans = 0
    for a in reversed(x):
        ans = (ans * z + a) % p
    return ans


def exact_input_polynomials() -> dict[str, tuple[int, ...]]:
    """Numerators over denominator 10 in the power basis."""
    data = {
        "0": {},
        "a": {1: 1, 3: 1, 5: -2, 7: 3, 9: 3, 11: -2, 13: -4, 15: 1},
        "b": {1: 3, 3: 3, 5: -1, 7: -1, 9: -1, 11: 4, 13: -2, 15: -2},
        "c": {5: 5, 15: -5},
    }
    ans = {}
    for label, sparse in data.items():
        row = [0] * DEG
        for i, value in sparse.items():
            row[i] = value
        ans[label] = tuple(row)
    return ans


def monomial(e: int) -> tuple[int, ...]:
    e %= 40
    raw = [0] * (e + 1)
    raw[e] = 1
    return reduce40(raw)


def source_l1_bound(amp: list[str], phase: np.ndarray) -> int:
    polys = exact_input_polynomials()
    bound = 0
    for label, e in zip(amp, phase.reshape(-1)):
        for sign in (1, -1):
            shifted = kmul(polys[label], monomial(sign * 2 * int(e)))
            bound = max(bound, sum(abs(x) for x in shifted))
    return bound


def support_certificate(amp: list[str]) -> np.ndarray:
    support = np.fromiter((x != "0" for x in amp), dtype=np.int64, count=1296).reshape(6, 6, 6, 6)
    # Counts remain tiny, so this large modulus never affects them.
    return audit.covariant(support, support, 0, audit.CORES[1], 2**62 - 57)


def evaluated_diagonal(
    amp: list[str], phase: np.ndarray, p: int, base_z: int, method: str
) -> list[list[int]]:
    all_values = [[] for _ in range(6)]
    for u in UNITS40:
        z = pow(base_z, u, p)
        A = audit.tensor_at_root(amp, phase, p, z, False)
        B = audit.tensor_at_root(amp, phase, p, z, True)
        for i in range(6):
            v = audit.covariant(A, B, 0, audit.CORES[1], p, method, i, i)
            all_values[i].append(int(v) % p)
    return all_values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("INDEPENDENT_EXACT.json"),
    )
    args = parser.parse_args()
    amp, phase = audit.parse_matlab_source(args.source)
    inputs = exact_input_polynomials()
    # Direct algebraic audit of the source constants in K=Q[z]/(Phi_40):
    # c=(z^5+z^-5)/2, a(z^2+z^-2)=c,
    # b=(z^4+z^-4)a, and a,b,c are fixed by conjugation z->z^-1.
    if kscale(kadd(monomial(5), monomial(-5)), 5) != inputs["c"]:
        raise AssertionError("c power-basis formula")
    if kmul(inputs["a"], kadd(monomial(2), monomial(-2))) != inputs["c"]:
        raise AssertionError("a power-basis formula")
    if kmul(inputs["a"], kadd(monomial(4), monomial(-4))) != inputs["b"]:
        raise AssertionError("b power-basis formula")
    if any(kconjugate(inputs[x]) != inputs[x] for x in ("a", "b", "c")):
        raise AssertionError("amplitude conjugation formula")
    support = support_certificate(amp)
    if np.count_nonzero(support - np.diag(np.diag(support))) != 0:
        raise AssertionError("support permits an off-diagonal monomial")

    # A rigorous coefficient bound: reduction of any basis monomial product
    # has L1 norm <=4; each entry numerator has L1<=B0; the support count is
    # the exact number of summands for each output entry.
    reduction_l1 = max(sum(abs(x) for x in monomial(i + j)) for i in range(16) for j in range(16))
    B0 = source_l1_bound(amp, phase)
    max_paths = int(support.max())
    coefficient_bound = max_paths * reduction_l1**7 * B0**8

    primes = split_primes(5)
    reconstruction_primes, verification_prime = primes[:4], primes[4]
    residues: list[list[list[int]]] = [[] for _ in range(6)]
    prime_records = []
    for p in reconstruction_primes:
        z = primitive_40_root(p)
        diagonal_values = evaluated_diagonal(amp, phase, p, z, "frozen")
        independent_values = evaluated_diagonal(amp, phase, p, z, "greedy")
        if independent_values != diagonal_values:
            raise AssertionError(f"independent contraction ordering differs at p={p}")
        coeffs = [interpolate_primitive(row, z, p) for row in diagonal_values]
        for i in range(6):
            residues[i].append([c * pow(DEN, 1, p) % p for c in coeffs[i]])
        prime_records.append({"p": p, "primitive_root_40": z})
        print(f"reconstruction prime p={p}, z={z}", flush=True)

    modulus = math.prod(reconstruction_primes)
    if modulus <= 2 * coefficient_bound:
        raise AssertionError(f"CRT modulus {modulus} does not dominate bound {coefficient_bound}")
    numerators = []
    for i in range(6):
        row = []
        for k in range(DEG):
            x, m = 0, 1
            for j, p in enumerate(reconstruction_primes):
                x, m = crt_pair(x, m, residues[i][j][k], p)
            if x > m // 2:
                x -= m
            if abs(x) > coefficient_bound:
                raise AssertionError("reconstructed coefficient violates the rigorous bound")
            row.append(x)
        numerators.append(tuple(row))

    # Independent-order check at a split prime excluded from reconstruction.
    vp = verification_prime
    vz = primitive_40_root(vp)
    alternative_values = evaluated_diagonal(amp, phase, vp, vz, "greedy")
    for i in range(6):
        for root_index, u in enumerate(UNITS40):
            root = pow(vz, u, vp)
            predicted = keval(numerators[i], root, vp) * pow(DEN, vp - 2, vp) % vp
            if predicted != alternative_values[i][root_index]:
                raise AssertionError((i, root_index, predicted, alternative_values[i][root_index]))

    # Materialize the distinct alternative contraction tree for the record.
    trace: list[dict] = []
    A = audit.tensor_at_root(amp, phase, vp, vz, False)
    B = audit.tensor_at_root(amp, phase, vp, vz, True)
    nodes = audit.build_network(A, B, 0, audit.CORES[1], 0, 0)
    audit.contract_greedy(nodes, vp, trace)

    # Full matrix in Q(zeta_40): support proves every omitted entry exactly 0.
    zero = (0,) * DEG
    full_matrix = [[numerators[i] if i == j else zero for j in range(6)] for i in range(6)]
    squares = [kmul(x, x) for x in numerators]
    # det [[1,1,1],[m0,m1,m3],[m0^2,m1^2,m3^2]], denominator DEN^3.
    ids = (0, 1, 3)
    n0, n1, n3 = (numerators[i] for i in ids)
    s0, s1, s3 = (squares[i] for i in ids)
    determinant = kadd(
        kmul(n1, s3),
        kscale(kmul(n3, s1), -1),
        kscale(kmul(n0, s3), -1),
        kmul(n3, s0),
        kmul(n0, s1),
        kscale(kmul(n1, s0), -1),
    )
    if all(x == 0 for x in determinant):
        raise AssertionError("exact minor vanished")

    # Replay the exact lift at the preregistered reduction z->6 in F_41.
    p41, z41 = 41, 6
    diag41 = [keval(x, z41, p41) * pow(DEN, p41 - 2, p41) % p41 for x in numerators]
    det41 = keval(determinant, z41, p41) * pow(DEN**3, p41 - 2, p41) % p41
    if diag41 != [4, 19, 19, 1, 1, 4] or det41 != 31:
        raise AssertionError((diag41, det41))

    simplified_diagonal = []
    simplified_denominators = []
    for x in numerators:
        g = math.gcd(DEN, math.gcd(*[abs(a) for a in x]))
        simplified_diagonal.append([a // g for a in x])
        simplified_denominators.append(DEN // g)
    minor_den = DEN**3
    minor_gcd = math.gcd(minor_den, math.gcd(*[abs(a) for a in determinant]))
    diagram = {
        "q": 0,
        "open_matching": [0, 1, 2, 3],
        "remaining_colors_in_order": [1, 2, 3],
        "permutations": [list(x) for x in audit.CORES[1]],
    }
    diagram_encoding = json.dumps(diagram, sort_keys=True, separators=(",", ":")).encode("ascii")

    result = {
        "descriptor": {
            "q": 0,
            "core": "R1",
            "core_triple": [list(x) for x in audit.CORES[1]],
            "witness": "det of flattened columns (0,0),(1,1),(3,3) in rows I,M,M^2",
            "power_basis": "1,z,...,z^15; Phi_40(z)=z^16-z^12+z^8-z^4+1",
        },
        "input_power_basis_common_denominator": 10,
        "input_power_basis_numerators": {k: list(v) for k, v in inputs.items()},
        "input_formula_identities_checked": True,
        "diagram_canonical_json": diagram,
        "diagram_sha256": hashlib.sha256(diagram_encoding).hexdigest(),
        "support_count_matrix": support.tolist(),
        "support_offdiagonal_zero": True,
        "reduction_l1_constant": reduction_l1,
        "source_entry_numerator_l1_bound": B0,
        "max_support_paths": max_paths,
        "rigorous_output_coefficient_bound": coefficient_bound,
        "crt_modulus": modulus,
        "crt_unique_condition": f"modulus > 2*bound: {modulus > 2*coefficient_bound}",
        "reconstruction_fields": prime_records,
        "verification_field": {"p": vp, "primitive_root_40": vz},
        "alternative_greedy_trace_for_entry_00": trace,
        "independent_order_equal_at_all_64_reconstruction_evaluations": True,
        "independent_order_equal_at_all_16_verification_evaluations": True,
        "matrix_common_denominator": DEN,
        "matrix_power_basis_numerators": [[list(x) for x in row] for row in full_matrix],
        "diagonal_power_basis_numerators": [list(x) for x in numerators],
        "simplified_diagonal_denominators": simplified_denominators,
        "simplified_diagonal_power_basis_numerators": simplified_diagonal,
        "minor_common_denominator": DEN**3,
        "minor_power_basis_numerators": list(determinant),
        "simplified_minor_denominator": minor_den // minor_gcd,
        "simplified_minor_power_basis_numerators": [a // minor_gcd for a in determinant],
        "mod41_replay": {"z": z41, "matrix_diagonal": diag41, "minor": det41},
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"diag mod41={diag41}; minor mod41={det41}")
    print(f"minor numerator={list(determinant)}")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
