#!/usr/bin/env python3
"""Exact accepted verifier for P-TM-FOURPHASE-HULL-NONDESCENT-1.

This file is result-exposed and proof-first. The unbounded statements are
proved in PREREG.md. This program audits their exact finite certificates and
symbolic identities. It uses no files, network, subprocesses, floats,
randomness, arguments, or environment-dependent scientific inputs.
"""

from itertools import permutations, product
import sys


FAILURES = []


def report(tag, ok, statement, detail=""):
    line = ("PASS " if ok else "FAIL ") + tag + " " + statement
    if detail:
        line += " | " + detail
    print(line)
    if not ok:
        FAILURES.append(tag)


def tau_word(word):
    """Apply tau(a)=a(a+1) modulo four to a finite word."""
    return tuple(y for x in word for y in (x, (x + 1) % 4))


def rotate_word(word, c):
    return tuple((x + c) % 4 for x in word)


def iota_word(word):
    return tuple((-x) % 4 for x in reversed(word))


def binary_word(word):
    return tuple(x % 2 for x in word)


def phi_symbol(x):
    return pow(2, x % 4, 5)


def factors(word, length):
    return {word[j:j + length] for j in range(len(word) - length + 1)}


def reversal_image(word, g):
    return tuple(g[x] for x in reversed(word))


def preserves_l3(g, language3):
    return all(reversal_image(word, g) in language3 for word in language3)


# An affine index/value operator is the exact tuple (ia, ib, va, vb) for
#
#     (T r)_m = va * r_(ia*m+ib) + vb mod 4.
#
# Index data are integers, not residues. Value offsets are normalized mod 4.
def compose(left, right):
    """Return left o right for affine index/value operators."""
    lia, lib, lva, lvb = left
    ria, rib, rva, rvb = right
    return (
        ria * lia,
        ria * lib + rib,
        lva * rva,
        (lva * rvb + lvb) % 4,
    )


def rotation_operator(c):
    return (1, 0, 1, c % 4)


IDENTITY = (1, 0, 1, 0)
SHIFT = (1, 1, 1, 0)
SHIFT_INVERSE = (1, -1, 1, 0)
IOTA = (-1, -1, -1, 0)
RHO_BINARY = (-1, -1, 1, 0)


def reduce_values_mod2(operator):
    ia, ib, va, vb = operator
    return (ia, ib, va % 2, vb % 2)


# D1. Substitution, rotations, primitivity, and the digit-sum fixed point.
letter_factor = all(
    binary_word(tau_word((a,))) == (a % 2, (a + 1) % 2)
    for a in range(4)
)
letter_rotation = all(
    tau_word(((a + c) % 4,)) == rotate_word(tau_word((a,)), c)
    for a in range(4)
    for c in range(4)
)
primitive_depth_three = all(
    set(tau_word(tau_word(tau_word((a,))))) == set(range(4))
    for a in range(4)
)

fixed = (0,)
for _ in range(16):
    fixed = tau_word(fixed)
digit_sum = tuple(n.bit_count() % 4 for n in range(1 << 16))
binary_tm = tuple(n.bit_count() % 2 for n in range(1 << 16))
digit_recursion = all(
    digit_sum[2 * n] == digit_sum[n]
    and digit_sum[2 * n + 1] == (digit_sum[n] + 1) % 4
    for n in range(1 << 15)
)
report(
    "D1",
    letter_factor
    and letter_rotation
    and primitive_depth_three
    and fixed == digit_sum
    and binary_word(fixed) == binary_tm
    and digit_recursion,
    "tau/pi/rotation identities and u_n=s_2(n) mod 4",
    "letters=65536",
)


# D2. Exact L2 and L3 certificates.
tau7 = (0,)
for _ in range(7):
    tau7 = tau_word(tau7)
all_pairs = set(product(range(4), repeat=2))
pairs_in_tau7 = factors(tau7, 2)
pair_witnesses = {
    pair: next(
        (j for j in range(len(tau7) - 1) if tau7[j:j + 2] == pair),
        None,
    )
    for pair in all_pairs
}
language3 = {
    word
    for a, b in all_pairs
    for word in (
        (a, (a + 1) % 4, b),
        ((a + 1) % 4, b, (b + 1) % 4),
    )
}
tau9 = (0,)
for _ in range(9):
    tau9 = tau_word(tau9)
report(
    "D2",
    pairs_in_tau7 == all_pairs
    and all(position is not None for position in pair_witnesses.values())
    and len(language3) == 28
    and factors(tau9, 3) == language3,
    "exact L2=(Z/4Z)^2 and exact 28-word L3 certificate",
    "pairs=16 triples=28",
)


# D3. N1, N2, and the local degree of freedom used by the all-length N3 proof.
a2_non_descent = all(
    (x + 2) % 2 == x % 2
    and phi_symbol(x + 2) == (-phi_symbol(x)) % 5
    and phi_symbol(x + 2) != phi_symbol(x)
    for x in range(4)
)
quotient = {1: 0, 2: 1, 3: 1, 4: 0}
c2_descent = all(quotient[phi_symbol(x)] == x % 2 for x in range(4))
first_letter_fibers = all(
    {phi_symbol(x) for x in range(4) if x % 2 == bit}
    == {phi_symbol(bit), (-phi_symbol(bit)) % 5}
    for bit in range(2)
)
report(
    "D3",
    a2_non_descent and c2_descent and first_letter_fibers,
    "A2 fixes pi and flips Phi; q descends; each block fiber has two reads",
)


# D4. N4 with exact affine index composition, not only residue negation.
iota_involution = compose(IOTA, IOTA) == IDENTITY
reversal_conjugacy_left = compose(IOTA, compose(SHIFT, IOTA))
reversal_conjugacy_right = compose(compose(IOTA, SHIFT), IOTA)
shift_reversal = (
    reversal_conjugacy_left == SHIFT_INVERSE
    and reversal_conjugacy_right == SHIFT_INVERSE
)
binary_cover = reduce_values_mod2(IOTA) == RHO_BINARY
phase_inversion = all(
    phi_symbol((-x) % 4) == pow(phi_symbol(x), -1, 5)
    for x in range(4)
)
letter_intertwining = all(
    iota_word(tau_word((a,)))
    == rotate_word(tau_word(iota_word((a,))), -1)
    for a in range(4)
)
word_intertwining = all(
    iota_word(tau_word(word))
    == rotate_word(tau_word(iota_word(word)), -1)
    for word in product(range(4), repeat=3)
)
iterate_intertwining = True
word = (0,)
for n in range(13):
    iterate_intertwining &= iota_word(word) == rotate_word(word, -n)
    word = tau_word(word)
report(
    "D4",
    iota_involution
    and shift_reversal
    and binary_cover
    and phase_inversion
    and letter_intertwining
    and word_intertwining
    and iterate_intertwining,
    "exact index composition proves iota^2=id and iota S iota=S^-1; pi and Phi intertwine",
)


# D5. Complete classification in the three frozen one-block classes.
affine_family = [
    (eps, c, tuple((eps * x + c) % 4 for x in range(4)))
    for eps in (1, -1)
    for c in range(4)
]
affine_survivors = [
    (eps, c)
    for eps, c, g in affine_family
    if preserves_l3(g, language3)
]

parity_family = list(product((0, 2), (1, 3), (0, 2), (1, 3)))
parity_survivors = [g for g in parity_family if preserves_l3(g, language3)]

permutation_family = list(permutations(range(4)))
permutation_survivors = [
    g for g in permutation_family if preserves_l3(g, language3)
]

want_affine = [(-1, c) for c in range(4)]
want_parity = [
    tuple((-x + c) % 4 for x in range(4)) for c in (0, 2)
]
want_permutations = [
    tuple((-x + c) % 4 for x in range(4)) for c in range(4)
]

excluded_have_witness = True
for family, survivors in (
    ([g for _eps, _c, g in affine_family], want_permutations),
    (parity_family, want_parity),
    (permutation_family, want_permutations),
):
    for g in family:
        if g not in survivors:
            witness = next(
                (
                    word
                    for word in sorted(language3)
                    if reversal_image(word, g) not in language3
                ),
                None,
            )
            excluded_have_witness &= witness is not None

survivors_are_rotated_iota = all(
    (-1, -1, -1, c) == compose(rotation_operator(c), IOTA)
    for c in range(4)
)
projection_scope = all(
    ((-x + c) % 4) % 2
    == (x % 2 if c % 2 == 0 else 1 - (x % 2))
    for c in range(4)
    for x in range(4)
)
phase_scope = all(
    phi_symbol((-x + c) % 4)
    == (phi_symbol(c) * pow(phi_symbol(x), -1, 5)) % 5
    for c in range(4)
    for x in range(4)
)
report(
    "D5",
    sorted(affine_survivors) == sorted(want_affine)
    and sorted(parity_survivors) == sorted(want_parity)
    and sorted(permutation_survivors) == sorted(want_permutations)
    and excluded_have_witness
    and survivors_are_rotated_iota
    and projection_scope
    and phase_scope,
    "one-block reversal classes: affine 4/8, rho-covering parity maps 2/16, permutations 4/24",
    "affine=" + repr(sorted(affine_survivors))
    + " parity=" + repr(sorted(parity_survivors)),
)


# D6. Bounded consistency only. No all-length proof depends on this scan.
bounded_ok = True
tm_prefix = binary_word(fixed)
counts = []
for length in range(1, 25):
    k4_factors = factors(fixed, length)
    tm_factors = factors(tm_prefix, length)
    counts.append(len(k4_factors))
    bounded_ok &= all(
        {rotate_word(word, c) for word in k4_factors} == k4_factors
        for c in range(4)
    )
    bounded_ok &= {binary_word(word) for word in k4_factors} == tm_factors
    bounded_ok &= {iota_word(word) for word in k4_factors} == k4_factors
    for block in tm_factors:
        reads = {
            phi_symbol(word[0])
            for word in k4_factors
            if binary_word(word) == block
        }
        bounded_ok &= reads == {
            phi_symbol(block[0]),
            (-phi_symbol(block[0])) % 5,
        }
report(
    "D6",
    bounded_ok,
    "bounded scan agrees with the written all-length proof at lengths 1..24",
    "K_TM4 counts=" + ",".join(map(str, counts)),
)


if FAILURES:
    print("RESULT FAIL " + ",".join(sorted(set(FAILURES))))
    sys.exit(1)

print("RESULT 6/6 ALL PASS")
sys.exit(0)
