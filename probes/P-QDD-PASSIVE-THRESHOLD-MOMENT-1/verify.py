#!/usr/bin/env python3
"""Exact audit for P-QDD-PASSIVE-THRESHOLD-MOMENT-1.

Standalone stdlib, L1 rational ensembles, no external records or physical law.
Do not execute before this package's immutable public preregistration pin.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import sys

if not __debug__:
    raise RuntimeError('Optimized Python is not an accepted verifier environment')

sys.stdout.reconfigure(newline='\n')

ZERO = (0, 0, 0, 0)
GRID = tuple(product(range(-2, 3), repeat=4))
PARTITIONS = (
    ('PI-ALL', ((0, 1, 2),)),
    ('PI-TRACE', ((0,), (1, 2))),
    ('PI-LEG', ((0, 2), (1,))),
    ('PI-PAIR', ((0, 1), (2,))),
    ('PI-ATOMS', ((0,), (1,), (2,))),
)
TARGET_ATOMS = (F(0), F(1), F(5))
SIGMA = (
    (F(1), F(0), F(-1, 2), F(-1, 2)),
    (F(0), F(3, 2), F(-3, 2), F(0)),
    (F(-1, 2), F(-3, 2), F(5, 2), F(-1, 2)),
    (F(-1, 2), F(0), F(-1, 2), F(1)),
)
P = (((0, 1, -2, 1), F(1, 2)),
     ((0, 2, -1, -1), F(1, 4)),
     ((2, 0, -1, -1), F(1, 4)))
Q = (((1, -2, 1, 0), F(1, 4)),
     ((1, 0, 1, -2), F(1, 4)),
     ((1, 1, -2, 0), F(1, 2)))
SOURCE_SITES = ((0, 0, 0), (1, 1, 0), (1, 0, 1),
                (0, 1, 1), (2, 0, 0))
DEPOSIT_FACTOR = F(3481, 26244)
THRESHOLD = F(1, 10)


def check(condition, label):
    if not condition:
        raise AssertionError(label)


def valid_source(z):
    return (type(z) is tuple and len(z) == 4
            and all(type(x) is int and -2 <= x <= 2 for x in z))


def atoms(z):
    if not valid_source(z):
        raise ValueError('source outside the balanced grid')
    s = sum(z)
    ell = z[0] - z[1] - z[2] + z[3]
    return (F(s * s, 20), F(ell * ell, 4),
            F((z[0] - z[3]) ** 2 + (z[1] - z[2]) ** 2, 2))


def record(z, partition):
    name, blocks = partition
    a = atoms(z)
    mass = sum(a)
    weights = tuple(sum((a[i] for i in b), F(0)) for b in blocks)
    if mass == 0:
        return (name, 'ZERO_SUPPORT', F(0), weights, 'ZERO_DENOMINATOR')
    return (name, 'SUPPORTED', mass, weights,
            ('NORMALIZED', tuple(w / mass for w in weights)))


def validate(ensemble):
    if type(ensemble) is not tuple or not ensemble:
        raise ValueError('empty or ill-typed ensemble')
    seen = set()
    total = F(0)
    for item in ensemble:
        if type(item) is not tuple or len(item) != 2:
            raise ValueError('ill-typed ensemble entry')
        z, weight = item
        if not valid_source(z) or z in seen:
            raise ValueError('invalid or duplicate source')
        if type(weight) is not F or weight < 0:
            raise ValueError('weight is not a nonnegative rational')
        seen.add(z)
        total += weight
    if total != 1:
        raise ValueError('ensemble is not normalized')
    return ensemble


def expectation(ensemble, function):
    return sum((weight * function(z) for z, weight in ensemble), F(0))


def mean(ensemble):
    return tuple(expectation(ensemble, lambda z: z[i]) for i in range(4))


def moment(ensemble):
    return tuple(tuple(expectation(ensemble, lambda z: z[i] * z[j])
                       for j in range(4)) for i in range(4))


def law(ensemble, function):
    result = defaultdict(F)
    for z, weight in ensemble:
        result[function(z)] += weight
    return {value: weight for value, weight in result.items() if weight}


def combine(weighted_ensembles):
    masses = defaultdict(F)
    for coefficient, ensemble in weighted_ensembles:
        for z, weight in ensemble:
            masses[z] += coefficient * weight
    return validate(tuple(sorted((z, p) for z, p in masses.items() if p)))


def symmetrize(ensemble):
    negative = tuple((tuple(-x for x in z), p) for z, p in ensemble)
    return combine(((F(1, 2), ensemble), (F(1, 2), negative)))


def stencil_and_origin():
    shell_weights = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
    stencil = {d: F(shell_weights[sum(x*x for x in d)], 324)
               for d in product(range(-4, 5), repeat=3)
               if sum(d) % 2 == 0 and sum(x*x for x in d) in shell_weights}
    check(len(stencil) == 60, 'G2 stencil cardinality')
    check(sum(stencil.values()) == F(8, 9), 'G2 stencil total')
    coefficients = tuple((2 - sum(stencil.values())) if y == (0, 0, 0)
                         else stencil.get(y, F(0)) for y in SOURCE_SITES)
    check(coefficients == (F(10, 9), F(1, 54), F(1, 54),
                           F(1, 54), F(1, 324)), 'G2 marked coefficients')
    h = tuple(coefficients[i] - sum(coefficients) / 5 for i in range(4))
    check(h == tuple(F(x, 1620) for x in (1421, -349, -349, -349)),
          'G2 first-origin row')
    return h


def reject(ensemble):
    try:
        validate(ensemble)
    except ValueError:
        return
    raise AssertionError('G6 malformed ensemble accepted')


def main():
    check(len(GRID) == 625, 'G1 full ambient grid')
    balanced = (0, 1, 2, -2, -1)
    fibre = []
    for z in GRID:
        residue_head = tuple(x % 5 for x in z) + (0, 0)
        check(tuple(balanced[x] for x in residue_head[:4]) == z,
              'G1 native head representative')
        a = atoms(z)
        check(sum(a) == sum(x*x for x in z) - F(sum(z)**2, 5),
              'G1 mass equality')
        check(all(w >= 0 for w in a), 'G1 atom positivity')
        for partition in PARTITIONS:
            rec = record(z, partition)
            check(len(rec) == 5 and rec[0] == partition[0], 'G1 record fields')
            check(sum(rec[3]) == rec[2], 'G1 total weights')
            if z == ZERO:
                check(rec == (partition[0], 'ZERO_SUPPORT', F(0),
                              (F(0),)*len(partition[1]), 'ZERO_DENOMINATOR'),
                      'G1 literal zero record')
            else:
                check(rec[1] == 'SUPPORTED' and rec[2] > 0,
                      'G1 supported record')
                check(rec[4] == ('NORMALIZED', tuple(w/rec[2] for w in rec[3])),
                      'G1 exact normalized record')
        if a == TARGET_ATOMS:
            fibre.append(z)
    check(bool(fibre) and ZERO not in fibre, 'G1 exact nonzero fibre')

    h = stencil_and_origin()

    def deposit(z):
        return sum((h[i] * z[i] for i in range(4)), F(0)) ** 2 / 9

    def count(z):
        return deposit(z) // THRESHOLD

    for z in fibre:
        y = z[0]**2
        check(sum(z) == 0 and y in (0, 1, 4), 'G2 fibre domain')
        check(deposit(z) == DEPOSIT_FACTOR*y, 'G2 restricted deposit')
        c = count(z)
        check(c == {0: 0, 1: 1, 4: 5}[y], 'G2 exact floor')
        check(c == F(11*y+y*y, 12), 'G4 count polynomial')
        check(F(c > 0) == F(5*y-y*y, 4), 'G4 crossing polynomial')
        check(F(c == 5) == F(y*y-y, 12), 'G4 count-five polynomial')
        check(F(c == 1) == F(4*y-y*y, 3), 'G4 count-one polynomial')
        check(F(c == 0) == F(y*y-5*y+4, 4), 'G4 count-zero polynomial')
    check(1 <= 10*DEPOSIT_FACTOR < 2 and 5 <= 40*DEPOSIT_FACTOR < 6,
          'G2 exact threshold inequalities')

    target_records = tuple(record(P[0][0], pi) for pi in PARTITIONS)
    for ensemble, expected_law, expected_m4, expected_mean in (
            (P, {0: F(3, 4), 5: F(1, 4)}, F(4),
             (F(1, 2), F(1), F(-3, 2), F(0))),
            (Q, {1: F(1)}, F(1),
             (F(1), F(0), F(-1, 2), F(-1, 2)))):
        validate(ensemble)
        check(all(atoms(z) == TARGET_ATOMS for z, p in ensemble),
              'G3 endpoint support')
        check(moment(ensemble) == SIGMA, 'G3 common raw moment')
        check(mean(ensemble) == expected_mean, 'G3 raw versus centered')
        check(law(ensemble, count) == expected_law, 'G3 endpoint count law')
        check(expectation(ensemble, lambda z: z[0]**4) == expected_m4,
              'G3 endpoint fourth moment')
        for pi, rec in zip(PARTITIONS, target_records):
            check(law(ensemble, lambda z: record(z, pi)) == {rec: F(1)},
                  'G3 full passive point law')
        centered = symmetrize(ensemble)
        check(mean(centered) == (F(0),)*4, 'G3 centered mean')
        check(moment(centered) == SIGMA, 'G3 centered covariance')
        check(law(centered, count) == expected_law, 'G3 centered count law')
        check(law(centered, deposit) == law(ensemble, deposit),
              'G3 centered deposit law')
        check(expectation(centered, lambda z: z[0]**4) == expected_m4,
              'G3 centered fourth moment')
        for pi, rec in zip(PARTITIONS, target_records):
            check(law(centered, lambda z: record(z, pi)) == {rec: F(1)},
                  'G3 centered passive law')

    for a in (F(0), F(1, 16), F(1, 8), F(3, 16), F(1, 4)):
        ensemble = combine(((4*a, P), (1-4*a, Q)))
        check(moment(ensemble) == SIGMA, 'G4 affine moment preservation')
        for pi, rec in zip(PARTITIONS, target_records):
            check(law(ensemble, lambda z: record(z, pi)) == {rec: F(1)},
                  'G4 affine passive-law preservation')
        expected = {c: p for c, p in ((0, 3*a), (1, 1-4*a), (5, a)) if p}
        check(law(ensemble, count) == expected, 'G4 entire-segment construction')
        m4 = expectation(ensemble, lambda z: z[0]**4)
        check(m4 == 1+12*a and 1 <= m4 <= 4, 'G5 fourth-moment range')
        check(a == (m4-1)/12, 'G5 fourth-moment inverse')
        check(expectation(ensemble, lambda z: F(count(z) > 0)) == (5-m4)/4,
              'G5 crossing repair')
        check(expectation(ensemble, count) == (11+m4)/12, 'G5 mean-count repair')
        check(expectation(ensemble, lambda z: deposit(z)**2)
              == DEPOSIT_FACTOR**2*m4, 'G5 deposit-second-moment repair')
        repaired = {c: p for c, p in ((0, (m4-1)/4), (1, (4-m4)/3),
                                     (5, (m4-1)/12)) if p}
        check(repaired == expected, 'G5 full-law repair')
    check(law(P, count) != law(Q, count), 'G5 zero-extra-observable failure')

    for invalid in (
            (), ((ZERO, F(1, 2)),), ((ZERO, F(-1)),),
            ((ZERO, F(1, 2)), (ZERO, F(1, 2))),
            (((3, 0, 0, 0), F(1)),), (((True, 0, 0, 0), F(1)),),
            ((ZERO, True),), ((ZERO, 1.0),)):
        reject(invalid)
    ambient_zero = validate(((ZERO, F(1)),))
    check(deposit(ZERO) == 0 and count(ZERO) == 0, 'G6 ambient zero')
    check(law(ambient_zero, count) == {0: F(1)}, 'G6 zero kept in count law')

    for gate in ('G1-RECORDS', 'G2-ORIGIN', 'G3-ENDPOINTS', 'G4-SHARP-SET',
                 'G5-MOMENT-REPAIR', 'G6-TYPE-AND-ZERO'):
        print(gate + ': PASS')
    print('COUNT_LAWS: (3a,1-4a,a) on (0,1,5); 0<=a<=1/4')
    print('M4_REPAIR: a=(M4-1)/12; 1<=M4<=4; minimum_extra_expectations=1')
    print('VERDICT: PASS; CONDITIONAL_L1; NO_PHYSICAL_OCCURRENCE_CLAIM')


if __name__ == '__main__':
    main()
