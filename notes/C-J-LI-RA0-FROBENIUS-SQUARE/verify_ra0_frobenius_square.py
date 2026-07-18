#!/usr/bin/env python3
"""PRE_FREEZE notes-lane audit for the fired RA0 Frobenius-square proposal.

MACHINE STATUS: NOT RUN.  A later PIN.md would be required before execution.
The file encodes a scoped falsification audit; its presence is not a machine
result.  It does not construct A_J, evaluate zeta, read zero or prime tables,
or make a public claim.  All finite prime-like objects below are derived as
multiplicative atoms of a bounded integer monoid and are only test fixtures.
"""

from fractions import Fraction
from itertools import permutations
from math import isqrt


LIMIT = 125
LAMBDA1_UPPER = Fraction(23095708972138893, 10**18)
PRIMITIVE_OUTPUT_BRIDGE_CLOSED = False


def gate(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS " + label)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def atoms_up_to(limit):
    atoms = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            atoms.append(n)
    return atoms


ATOMS = atoms_up_to(LIMIT)


def factor_vector(n):
    """Formal log(n) in the free module on the derived atoms."""
    out = {}
    value = n
    for p in ATOMS:
        if p * p > value:
            break
        while value % p == 0:
            out[p] = out.get(p, 0) + 1
            value //= p
    if value > 1:
        out[value] = out.get(value, 0) + 1
    return out


def is_atom_power(n):
    factors = factor_vector(n)
    if len(factors) != 1:
        return None
    return next(iter(factors))


def add_vectors(*vectors):
    out = {}
    for vector in vectors:
        for key, value in vector.items():
            out[key] = out.get(key, 0) + value
            if out[key] == 0:
                del out[key]
    return out


def scale_vector(scale, vector):
    return {key: scale * value for key, value in vector.items() if scale * value}


def lambda_vector(n):
    p = is_atom_power(n)
    return {} if p is None else {p: 1}


def raw_p0_log_vector(n):
    raw = lambda_vector(n)
    value = n
    exponent = 0
    while value % 5 == 0:
        value //= 5
        exponent += 1
    if value == 1 and exponent >= 1:
        raw = add_vectors(raw, {5: -n})
    return raw


def filter_tower_vector(n):
    value = n
    exponent = 0
    while value % 5 == 0:
        value //= 5
        exponent += 1
    return {5: n} if value == 1 and exponent >= 1 else {}


# Polynomials are low-to-high tuples of Fractions.
def ptrim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def padd(a, b):
    size = max(len(a), len(b))
    return ptrim(tuple((a[i] if i < len(a) else 0) +
                       (b[i] if i < len(b) else 0) for i in range(size)))


def pneg(a):
    return tuple(-x for x in a)


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    return ptrim(tuple(out))


def ppow(a, exponent):
    out = (Fraction(1),)
    for _ in range(exponent):
        out = pmul(out, a)
    return out


def permutation_sign(perm):
    inversions = sum(perm[i] > perm[j]
                     for i in range(len(perm))
                     for j in range(i + 1, len(perm)))
    return -1 if inversions % 2 else 1


def det_poly(matrix):
    n = len(matrix)
    total = (Fraction(0),)
    for perm in permutations(range(n)):
        term = (Fraction(permutation_sign(perm)),)
        for row, col in enumerate(perm):
            term = pmul(term, matrix[row][col])
        total = padd(total, term)
    return ptrim(total)


def c4_left_matrix(residue):
    # C4 is represented by residues (1,2,4,3) under multiplication mod 5.
    group = (1, 2, 4, 3)
    matrix = [[Fraction(0) for _ in group] for _ in group]
    for col, value in enumerate(group):
        row = group.index((residue * value) % 5)
        matrix[row][col] = Fraction(1)
    return matrix


def det_i_minus_x(matrix):
    out = []
    for row in range(len(matrix)):
        out_row = []
        for col in range(len(matrix)):
            constant = Fraction(1 if row == col else 0)
            out_row.append((constant, -matrix[row][col]))
        out.append(out_row)
    return det_poly(out)


def order_mod_5(residue):
    value = 1
    for order in range(1, 5):
        value = (value * residue) % 5
        if value == 1:
            return order
    raise AssertionError("not a unit mod 5")


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def coupled_block_polynomial():
    # Exact finite model K: Q^3 -> Q^2.  The infinite ideal statement is not
    # asserted here; this checks only the determinant algebra.
    k = [[Fraction(1), Fraction(2), Fraction(0)],
         [Fraction(0), Fraction(1), Fraction(1)]]
    kt = transpose(k)
    size_a = 3
    size_inf = 2
    block = []
    for i in range(size_a):
        row = []
        for j in range(size_a):
            row.append((Fraction(1 if i == j else 0),))
        for j in range(size_inf):
            row.append((Fraction(0), kt[i][j]))
        block.append(row)
    for i in range(size_inf):
        row = []
        for j in range(size_a):
            row.append((Fraction(0), k[i][j]))
        for j in range(size_inf):
            row.append((Fraction(1 if i == j else 0),))
        block.append(row)

    kkt = matmul(k, kt)
    schur = []
    for i in range(size_inf):
        row = []
        for j in range(size_inf):
            constant = Fraction(1 if i == j else 0)
            row.append((constant, Fraction(0), -kkt[i][j]))
        schur.append(row)
    trace_perturbation = (Fraction(0),)
    for index in range(size_a + size_inf):
        trace_perturbation = padd(
            trace_perturbation,
            psub(block[index][index], (Fraction(1),)),
        )
    return det_poly(block), det_poly(schur), trace_perturbation


def main():
    print("C-J-LI-RA0-FROBENIUS-SQUARE exact recon audit")
    print("scope: notes-only FIRED construction; no A_J, RH, Canon, or probe claim")
    print("arithmetic: integers/Fraction/exact polynomials only")

    # Finite regression only: both sides encode the already established
    # f_5 quotient identity.  This is not an independent analytic proof.
    # f_5 has Dirichlet coefficients -1 at 1 and +5 at 5.  Convolution with
    # the all-ones series gives c_J(n)=5[5|n]-1.
    quotient_ok = True
    for n in range(1, LIMIT + 1):
        convolution = -1 + (5 if n % 5 == 0 else 0)
        expected = 4 if n % 5 == 0 else -1
        quotient_ok &= convolution == expected
    gate("R01 encoded root-filter quotient regression exact for n<=125",
         quotient_ok)

    # Finite encoded-identity regression: Lambda(p^k)=log p in the formal
    # {log p} module.  Both sides are derived by this file; the check guards
    # bookkeeping changes and is not independent evidence for an Euler law.
    # The formal logarithmic derivative has sum_{d|n} Lambda(d)=log n, and
    # raw P0 plus the tower correction recovers Lambda.
    log_ok = True
    tower_ok = True
    for n in range(1, LIMIT + 1):
        reconstructed = add_vectors(*(lambda_vector(d) for d in divisors(n)))
        log_ok &= reconstructed == factor_vector(n)
        tower_ok &= add_vectors(raw_p0_log_vector(n),
                                filter_tower_vector(n)) == lambda_vector(n)
    gate("R02 encoded von-Mangoldt/tower identity regression exact for n<=125",
         log_ok and tower_ok)

    c4_ok = True
    trivial = [[Fraction(1, 4) for _ in range(4)] for _ in range(4)]
    for residue in (1, 2, 3, 4):
        frobenius = c4_left_matrix(residue)
        order = order_mod_5(residue)
        expected = ppow((Fraction(1),) + (Fraction(0),) * (order - 1) +
                        (Fraction(-1),), 4 // order)
        c4_ok &= det_i_minus_x(frobenius) == expected
        c4_ok &= matmul(frobenius, trivial) == trivial
        c4_ok &= matmul(trivial, frobenius) == trivial
    gate("R03 C4 regular Frobenius blocks and trivial projector exact", c4_ok)

    local5_det = (Fraction(1), Fraction(-1))
    gate("R04 ramified p=5 inertia line is a separate factor 1-x",
         local5_det == det_i_minus_x([[Fraction(1)]]))

    gate("R05 strict G0 guard records missing primitive-output bridge",
         PRIMITIVE_OUTPUT_BRIDGE_CLOSED is False)

    # Finite exponent-list sanity only.  The proof-first imported criterion
    # says that for |K|^m with prime-like singular values p^-m, trace class
    # means m>1 and its square root is trace class iff m/2>1.  This loop does
    # not prove either infinite-dimensional assertion; it only checks m=1..8.
    admissible_powers = [m for m in range(1, 9)
                         if Fraction(m) > 1 and Fraction(m, 2) <= 1]
    gate("R06 finite m=1..8 sanity selects only m=2 under imported inequalities",
         admissible_powers == [2])

    b2 = Fraction(4, 17)
    gate("R07 K1 FIRED exactly: b_2=4/17 > 3/125 > upper(lambda_1)",
         b2 > Fraction(3, 125) > LAMBDA1_UPPER)

    # Finite witness only: atoms are derived, not supplied.  It pins the
    # exact w-chart formula and the monotone partial-trace obstruction.
    b_values = [Fraction(4, 4 * p * p + 1) for p in ATOMS]
    gate("R08 derived-atom w-chart partial trace already exceeds lambda_1",
         ATOMS[:3] == [2, 3, 5] and sum(b_values) >= b2 > LAMBDA1_UPPER)

    coupled, schur, trace_perturbation = coupled_block_polynomial()
    # In this finite model C(t)=block-I has zero trace, so
    # det_2(I+C)=det(I+C) exp(-Tr C)=det(I+C).  The polynomial comparison is
    # then the ordinary Schur-complement identity; no infinite S2 claim is
    # machine-certified here.
    gate("R09 finite block trace is zero and det_2 reduces to Schur determinant",
         trace_perturbation == (Fraction(0),) and coupled == schur)

    print("witness atoms<=125", len(ATOMS), "first", ATOMS[:5], "last", ATOMS[-1])
    print("witness b_2", f"{b2.numerator}/{b2.denominator}")
    print("lambda_1 upper", f"{LAMBDA1_UPPER.numerator}/{LAMBDA1_UPPER.denominator}")
    print("coupled polynomial", ",".join(str(value) for value in coupled))
    print("RESULT 9/9 PASS: RA0 scoped falsification reproduced")


if __name__ == "__main__":
    main()
