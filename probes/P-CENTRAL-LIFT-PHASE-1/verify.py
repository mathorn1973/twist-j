#!/usr/bin/env python3
"""Accepted exact verifier for public probe P-CENTRAL-LIFT-PHASE-1.

Claimed in issue #251 against Public Canon v31. The incubation output was
known before the public pin, so this verifier is confirmatory. It audits
the exact certificates for PREREG.md E1-E3 and deliberately excludes the
Herm2 cone, split-unit rigidity, icosian glue, integral ticks, U(1),
decoder data, and every cross-layer lift.
"""

import sys
from fractions import Fraction as F


RESULTS = []


def check(name, condition):
    ok = bool(condition)
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name)


# K = Q(zeta_5), exact in the basis 1,zeta,zeta^2,zeta^3.
def reduce_phi5(coefficients):
    top = coefficients[4]
    return tuple(coefficients[index] - top for index in range(4))


def zadd(left, right):
    return tuple(a + b for a, b in zip(left, right))


def zsub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def zneg(value):
    return tuple(-entry for entry in value)


def zint(value):
    return (F(value), F(0), F(0), F(0))


def zmul(left, right):
    coefficients = [F(0)] * 5
    for left_index in range(4):
        if left[left_index] == 0:
            continue
        for right_index in range(4):
            if right[right_index] == 0:
                continue
            coefficients[(left_index + right_index) % 5] += (
                left[left_index] * right[right_index]
            )
    return reduce_phi5(tuple(coefficients))


def zpow(value, exponent):
    result = zint(1)
    for _ in range(exponent):
        result = zmul(result, value)
    return result


def galois(value, exponent):
    coefficients = [F(0)] * 5
    for index in range(4):
        coefficients[(index * exponent) % 5] += value[index]
    return reduce_phi5(tuple(coefficients))


def residue_lambda(value):
    residue = sum(value)
    if residue.denominator != 1:
        return None
    return int(residue) % 5


ONE = zint(1)
ZETA = (F(0), F(1), F(0), F(0))
J = (F(1), F(0), F(1), F(0))
PHI = (F(0), F(0), F(-1), F(-1))
INV_PHI = zsub(PHI, ONE)
NORM_J = zsub(zint(2), PHI)
CONJUGATE_J = galois(J, 4)
INVERSE_J = zmul(PHI, galois(ZETA, 4))
ZETA_10 = zneg(zpow(ZETA, 3))


# Inherited public T inputs, audited but not claimed again.
check(
    "R1 inherited J projection identities: J+Jbar=J Jbar=2-phi",
    zadd(J, CONJUGATE_J) == NORM_J
    and zmul(J, CONJUGATE_J) == NORM_J,
)
check(
    "R2 inherited polarization: phi J=zeta pins the principal branch",
    zmul(PHI, J) == ZETA
    and zmul(INV_PHI, ZETA) == J
    and zmul(PHI, CONJUGATE_J) == galois(ZETA, 4),
)


# E1: the exact spinor sign, without evaluating sqrt(phi).
check(
    "E1 zeta10^2=zeta, zeta10^5=-1, zeta10^10=1; s^2=J and the fifth spinor power carries the central minus sign",
    zpow(ZETA_10, 2) == ZETA
    and zpow(ZETA_10, 5) == zneg(ONE)
    and zpow(ZETA_10, 10) == ONE
    and zmul(zpow(ZETA_10, 2), INV_PHI) == J,
)
check(
    "R3 inherited golden magnitude: J^5 phi^5=1",
    zmul(zpow(J, 5), zpow(PHI, 5)) == ONE,
)


# E2: exact coefficients of the normalized actions.
check(
    "E2A square-root-free Herm action of A_J has coefficients (phi^-1,phi,zeta)",
    zmul(PHI, NORM_J) == INV_PHI and zmul(PHI, J) == ZETA,
)
check(
    "E2B five normalized Herm steps give (phi^-5,phi^5,1)",
    zmul(zpow(INV_PHI, 5), zpow(PHI, 5)) == ONE
    and zpow(ZETA, 5) == ONE,
)
check(
    "E2C A_J^2=J diag(J,J^-1), so the normalized Herm action is projective",
    zmul(J, INVERSE_J) == ONE,
)
check(
    "E2D the corresponding normalized Sym central factor is J^2/N(J)=zeta^2",
    zmul(J, J) == zmul(NORM_J, zpow(ZETA, 2))
    and zpow(zmul(J, PHI), 2) == zpow(ZETA, 2),
)


# E3: finite terminal certificate for the universal proof in PREREG 7.5.
MU5 = {zpow(ZETA, exponent) for exponent in range(5)}
MU10 = MU5 | {zneg(value) for value in MU5}
RESIDUE_ONE_ROOTS = {
    value for value in MU10 if residue_lambda(value) == 1
}
ATTAINED_PHASES = {zpow(ZETA, 2 * exponent) for exponent in range(5)}

check(
    "E3A finite terminal certificate: mu10 has ten roots, its residue-one subset is exactly mu5, and unit roots attain all mu5 phases",
    len(MU10) == 10
    and all(zpow(value, 10) == ONE for value in MU10)
    and RESIDUE_ONE_ROOTS == MU5
    and ATTAINED_PHASES == MU5,
)

TENTH_ROOT = zneg(zpow(ZETA, 2))
check(
    "E3B 1-J=-zeta^2 is primitive in mu10 and lies outside the unit-scalar phase image mu5",
    zsub(ONE, J) == TENTH_ROOT
    and TENTH_ROOT not in MU5
    and zpow(TENTH_ROOT, 5) == zneg(ONE)
    and zpow(TENTH_ROOT, 10) == ONE,
)


total = len(RESULTS)
passed = sum(RESULTS)
print(f"SUMMARY {passed}/{total} PASS")
sys.exit(0 if passed == total else 1)
