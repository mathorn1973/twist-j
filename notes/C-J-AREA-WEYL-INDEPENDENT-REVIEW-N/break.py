#!/usr/bin/env python3
"""Independent exact R1 breaker, frozen before its first execution.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
The exposed hypothesis and inventory are the author's original PREREG only.
No author implementation, proof, result or expected output was read in writing
this file. There are no runtime files, repository imports or network calls.

Ring elements use FIVE cyclic integer coefficients modulo the all-ones
relation. Operators are dense matrices with entries in that exact quotient.
Finite checks audit the separate unbounded proof; they do not replace it.
"""

from fractions import Fraction
from itertools import product
import json


class Falsifier(Exception):
    pass


def demand(condition, label):
    if not condition:
        raise Falsifier(label)


def emit(label, fields):
    print(label + " " + json.dumps(fields, sort_keys=True, separators=(",", ":")))


def cyc(values):
    """Choose the representative whose fifth cyclic coefficient is zero."""
    values = tuple(values)
    if len(values) != 5 or any(type(x) is not int for x in values):
        raise TypeError("five exact integer coefficients required")
    return tuple(x - values[4] for x in values)


ZERO = (0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0)


def plus(a, b):
    return cyc(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def minus(a, b):
    return plus(a, neg(b))


def times(a, b):
    out = [0] * 5
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            out[(i + k) % 5] += x * y
    return cyc(out)


def power(a, exponent):
    if type(exponent) is not int or exponent < 0:
        raise ValueError("nonnegative integer exponent required")
    out = ONE
    for _ in range(exponent):
        out = times(out, a)
    return out


def root(k):
    return cyc(int(i == k % 5) for i in range(5))


def residue(a):
    return sum(a) % 5


JROOT = root(1)
BIG_J = plus(ONE, root(2))
PHI = neg(plus(root(2), root(3)))
BIG_J_INV = times(PHI, root(4))
PHI_INV = times(BIG_J, root(4))


def area(u, v):
    return minus(times(u[0], v[1]), times(u[1], v[0]))


def step(u):
    return times(BIG_J, u[0]), times(PHI, u[1])


def unstep(u):
    return times(BIG_J_INV, u[0]), times(PHI_INV, u[1])


def repeat_step(u, count):
    for _ in range(count):
        u = step(u)
    return u


def farea(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % 5


def fstep(u):
    return 2 * u[0] % 5, 3 * u[1] % 5


def ring_audit():
    basis = tuple(root(k) for k in range(4))
    demand(cyc((1,) * 5) == ZERO, "cyclotomic all-ones relation")
    demand(power(JROOT, 5) == ONE, "j fifth power")
    demand(all(power(JROOT, k) != ONE for k in range(1, 5)), "j primitive order")
    demand(times(BIG_J, PHI) == JROOT, "J phi = j")
    for value, inverse in ((BIG_J, BIG_J_INV), (PHI, PHI_INV)):
        demand(times(value, inverse) == times(inverse, value) == ONE,
               "two-sided integral unit inverse")

    # These exact divisions support the separate ideal-kernel proof. They
    # are not a bounded search used to assert an infinite quotient theorem.
    factor = minus(ONE, JROOT)
    demand(times(factor, cyc((4, 3, 2, 1, 0))) == cyc((5, 0, 0, 0, 0)),
           "5 lies in the ramified ideal")
    geometric = ZERO
    for k in range(4):
        demand(minus(root(k), ONE) == times(factor, neg(geometric)),
               "j^k minus 1 belongs to the ramified ideal")
        geometric = plus(geometric, root(k))
    demand(tuple(residue(x) for x in (JROOT, BIG_J, PHI)) == (1, 2, 3),
           "ramified values of j, J, phi")
    demand(residue(ONE) == 1 and residue(factor) == 0, "residue unit and kernel")
    residue_pairs = 0
    for a, b in product(basis, repeat=2):
        demand(residue(times(a, b)) == residue(a) * residue(b) % 5,
               "residue ring-basis multiplicativity")
        demand(residue(plus(a, b)) == (residue(a) + residue(b)) % 5,
               "residue ring-basis additivity")
        residue_pairs += 1

    module_basis = tuple((e, ZERO) for e in basis) + tuple((ZERO, e) for e in basis)
    for u in module_basis:
        demand(step(unstep(u)) == unstep(step(u)) == u, "full module inverse basis")
    pairs = 0
    for u, v in product(module_basis, repeat=2):
        w = area(u, v)
        demand(area(step(u), step(v)) == times(JROOT, w), "one-step area covariance")
        demand(area(repeat_step(u, 5), repeat_step(v, 5)) == w,
               "fifth-power entire alternating form")
        demand(area(u, u) == ZERO and area(v, u) == neg(w), "alternating form")
        pairs += 1
    unit_u, unit_v = (ONE, ZERO), (ZERO, ONE)
    demand(area(step(unit_u), step(unit_v)) == JROOT != area(unit_u, unit_v),
           "negative control: one-step preservation is false")
    demand(residue(JROOT) == residue(ONE) and JROOT != ONE,
           "negative control: residue erases nontrivial complex phase")
    demand(all(residue(power(JROOT, k)) == 1 for k in range(5)),
           "all five cyclotomic phases reduce to the same residue")
    demand(residue_pairs == 16 and pairs == 64, "ring inventory")
    emit("RING", {"residue_basis_pairs": residue_pairs, "module_basis": 8,
                  "covariance_pairs": pairs, "fifth_power_pairs": pairs,
                  "two_sided_module_inverse_basis": 8,
                  "one_step_preservation": False, "residue_erases_phase": True})


def m_identity():
    return tuple(tuple(ONE if r == c else ZERO for c in range(5)) for r in range(5))


def m_product(a, b):
    rows = []
    for r in range(5):
        row = []
        for c in range(5):
            value = ZERO
            for k in range(5):
                if a[r][k] != ZERO and b[k][c] != ZERO:
                    value = plus(value, times(a[r][k], b[k][c]))
            row.append(value)
        rows.append(tuple(row))
    return tuple(rows)


def m_power(a, exponent):
    out = m_identity()
    for _ in range(exponent):
        out = m_product(out, a)
    return out


def m_scalar(value, a):
    return tuple(tuple(times(value, entry) for entry in row) for row in a)


def permutation_matrix(mapping):
    demand(sorted(mapping) == list(range(5)), "basis permutation")
    return tuple(tuple(ONE if r == mapping[c] else ZERO for c in range(5))
                 for r in range(5))


def carrier_audit():
    labels = tuple(product(range(5), repeat=2))
    z = tuple(tuple(root(c) if r == c else ZERO for c in range(5)) for r in range(5))
    x = permutation_matrix(tuple((k + 1) % 5 for k in range(5)))
    d = permutation_matrix(tuple(3 * k % 5 for k in range(5)))
    dinv = permutation_matrix(tuple(2 * k % 5 for k in range(5)))
    eye = m_identity()
    demand(m_product(d, dinv) == m_product(dinv, d) == eye, "D two-sided inverse")
    demand(m_power(z, 5) == m_power(x, 5) == eye, "Weyl generator orders")
    demand(m_product(z, x) == m_scalar(JROOT, m_product(x, z)), "ZX = j XZ")
    demand(m_product(m_product(d, z), dinv) == m_power(z, 2), "D Z D^-1 = Z^2")
    demand(m_product(m_product(d, x), dinv) == m_power(x, 3), "D X D^-1 = X^3")
    weyl = {u: m_product(m_power(z, u[0]), m_power(x, u[1])) for u in labels}
    demand(len(set(weyl.values())) == 25, "25 distinct marked Weyl operators")
    for u in labels:
        demand(m_product(m_product(d, weyl[u]), dinv) == weyl[fstep(u)],
               "complete Weyl conjugation, including central phase")
        negative_u = ((-u[0]) % 5, (-u[1]) % 5)
        inverse_u = m_scalar(root(-u[0] * u[1]), weyl[negative_u])
        demand(m_product(weyl[u], inverse_u) == m_product(inverse_u, weyl[u]) == eye,
               "explicit two-sided Weyl inverse, including central phase")
    pairs = 0
    for u, v in product(labels, repeat=2):
        omega = farea(u, v)
        demand(farea(fstep(u), fstep(v)) == omega, "complete finite area preservation")
        forward, reverse = m_product(weyl[u], weyl[v]), m_product(weyl[v], weyl[u])
        demand(forward == m_scalar(root(omega), reverse), "complete Weyl commutator")
        uv = ((u[0] + v[0]) % 5, (u[1] + v[1]) % 5)
        demand(forward == m_scalar(root(-u[1] * v[0]), weyl[uv]),
               "ordered Weyl product central cocycle")
        pairs += 1
    demand(pairs == 625, "finite carrier inventory")
    emit("CARRIER", {"labels": len(labels), "area_pairs": pairs,
                     "weyl_conjugations": len(labels), "weyl_commutator_pairs": pairs,
                     "weyl_two_sided_inverses": len(labels),
                     "ordered_product_cocycle_pairs": pairs,
                     "matrices": "dense 5 by 5 over cyclic cyclotomic quotient"})
    return labels, x, z, d, dinv


def character_audit(labels):
    characters = tuple(tuple(root(t * a) for a in range(5)) for t in range(5))
    additive_checks = 0
    for chi in characters:
        demand(chi[0] == ONE, "character identity")
        for a, b in product(range(5), repeat=2):
            demand(chi[(a + b) % 5] == times(chi[a], chi[b]), "character addition")
            additive_checks += 1
    faithful = tuple(t for t, chi in enumerate(characters) if len(set(chi)) == 5)
    demand(faithful == (1, 2, 3, 4), "exactly four faithful characters")
    demand(len(set(characters)) == 5, "all character choices distinct")
    area_checks = 0
    for t in faithful:
        chi = characters[t]
        for u, v in product(labels, repeat=2):
            demand(chi[farea(fstep(u), fstep(v))] == chi[farea(u, v)],
                   "each faithful character preserves A-area")
            area_checks += 1
    demand(additive_checks == 125 and area_checks == 2500, "character inventory")
    demand(characters[1][1] != characters[4][1], "no unprovided character orientation selector")
    emit("CHARACTERS", {"all_additive_candidates": 5, "addition_pairs": additive_checks,
                        "faithful_parameters": list(faithful), "area_checks": area_checks,
                        "physical_character_selected": False})


def diagonal_commutation_rows(matrix):
    """Exact rational linear equations for diag(h) M = M diag(h).

    Each ring coordinate of M_rc*(h_r-h_c) contributes a rational row.
    This derives the COMPLETE diagonal cost constraints, without an
    integer-box inference or a matrix-entry approximation.
    """
    rows = []
    for r in range(5):
        for c in range(5):
            for coefficient in matrix[r][c]:
                row = [Fraction(0)] * 5
                row[r] += coefficient
                row[c] -= coefficient
                if any(row):
                    rows.append(tuple(row))
    return rows


def rational_nullspace(rows):
    a = [list(map(Fraction, row)) for row in rows]
    pivots = []
    pivot_row = 0
    for col in range(5):
        source = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if source is None:
            continue
        a[pivot_row], a[source] = a[source], a[pivot_row]
        divisor = a[pivot_row][col]
        a[pivot_row] = [entry / divisor for entry in a[pivot_row]]
        for r in range(len(a)):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [entry - scale * pivot for entry, pivot in zip(a[r], a[pivot_row])]
        pivots.append(col)
        pivot_row += 1
    basis = []
    for free in range(5):
        if free in pivots:
            continue
        vector = [Fraction(int(k == free)) for k in range(5)]
        for r, col in enumerate(pivots):
            vector[col] = -a[r][free]
        basis.append(tuple(vector))
    return len(pivots), tuple(basis)


def diagonal_commutes(cost, matrix):
    # Multiplication of the dense matrix by a diagonal matrix, evaluated
    # independently of the RREF constraints and the claimed orbit formula.
    for r in range(5):
        for c in range(5):
            left = tuple(cost[r] * entry for entry in matrix[r][c])
            right = tuple(entry * cost[c] for entry in matrix[r][c])
            if left != right:
                return False
    return True


def cost_audit(x, z, d):
    drows = diagonal_commutation_rows(d)
    xrows = diagonal_commutation_rows(x)
    zrows = diagonal_commutation_rows(z)
    rank_d, kernel_d = rational_nullspace(drows)
    rank_x, kernel_x = rational_nullspace(xrows)
    rank_z, kernel_z = rational_nullspace(zrows)
    rank_all, kernel_all = rational_nullspace(drows + xrows + zrows)
    e0 = (1, 0, 0, 0, 0)
    rest = (0, 1, 1, 1, 1)
    scalar = (1, 1, 1, 1, 1)
    demand((rank_d, kernel_d) == (3, (e0, rest)), "complete rational D cost kernel")
    demand((rank_x, kernel_x) == (4, (scalar,)), "complete rational X cost kernel")
    demand(rank_z == 0 and len(kernel_z) == 5, "all diagonal costs commute with Z")
    demand((rank_all, kernel_all) == (4, (scalar,)), "complete rational shared cost kernel")

    cases = d_count = x_count = z_count = all_count = 0
    for cost in product(range(-2, 3), repeat=5):
        is_d = diagonal_commutes(cost, d)
        is_x = diagonal_commutes(cost, x)
        is_z = diagonal_commutes(cost, z)
        demand(is_d == (cost[1] == cost[2] == cost[3] == cost[4]), "cost box D classification")
        demand(is_x == (len(set(cost)) == 1) and is_z, "cost box X/Z classification")
        demand((is_d and is_x and is_z) == (len(set(cost)) == 1), "cost box shared scalar class")
        d_count += int(is_d)
        x_count += int(is_x)
        z_count += int(is_z)
        all_count += int(is_d and is_x and is_z)
        cases += 1
    demand((cases, d_count, x_count, z_count, all_count) == (3125, 25, 5, 3125, 5),
           "cost exhaustive inventory")
    gap_examples = []
    for gap in (1, 2):
        cost = (Fraction(2, 3),) + (Fraction(2, 3) + gap,) * 4
        demand(diagonal_commutes(cost, d) and diagonal_commutes(cost, z), "positive gap example D/Z")
        demand(not diagonal_commutes(cost, x), "nonconstant positive gap example not X invariant")
        demand(min(cost) > 0 and cost[1] - cost[0] == gap, "exact positive selectable gap")
        gap_examples.append(gap)
    emit("COST", {"box_vectors": cases, "D_invariant": d_count, "X_invariant": x_count,
                  "Z_invariant": z_count, "shared_invariant": all_count,
                  "rational_constraint_ranks": [rank_d, rank_x, rank_z, rank_all],
                  "D_cost_class": "diag(h0,h1,h1,h1,h1), h0,h1 rational",
                  "positive_gap_examples": gap_examples, "energy_unit_forced": False})


def main():
    ring_audit()
    labels, x, z, d, _ = carrier_audit()
    character_audit(labels)
    cost_audit(x, z, d)
    emit("SCOPE", {"action_layer": "L1", "native_T_equals_U": "UNSUPPLIED",
                   "physical_character_selection": "UNSUPPLIED",
                   "physical_action_or_SI_hbar": "NOT_DERIVED",
                   "unbounded_claims_need_separate_proof": True})
    print("AUDIT PASS independent exact R1 identities and stated negative controls")


if __name__ == "__main__":
    try:
        main()
    except Falsifier as exc:
        emit("FALSIFIER", {"check": str(exc)})
        print("AUDIT FAIL independent R1 scientific falsifier")
