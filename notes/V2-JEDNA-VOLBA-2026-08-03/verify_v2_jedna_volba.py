#!/usr/bin/env python3
# NON-CANONICAL informal witness for the note V2_JEDNA_VOLBA_NADHLED.
# Exact integer and rational arithmetic only; Python standard library only.
# This is not a preregistered verifier and earns no public status.
import sys
from fractions import Fraction
from math import gcd

PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    print(("PASS " if ok else "FAIL ") + name)
    if ok:
        PASS += 1
    else:
        FAIL += 1


def v2(m):
    assert m >= 1
    return (m & -m).bit_length() - 1


def s2(n):
    return bin(n).count("1")


# G01: the ramified image of the axiom at lambda = 1 - zeta_5 is the
# rational prime 2, and its multiplicative order in F_5^x is 4.
phi5_at_1 = sum(1 for _ in range(5))  # Phi_5(x) = 1+x+x^2+x^3+x^4 at x = 1
j_at_1 = 1 + 1 ** 2                   # J = 1 + zeta_5^2 under zeta_5 -> 1
check("G01 RAMIFIED-IMAGE  N(1-zeta_5) = Phi_5(1) = 5; J mod lambda = 2;"
      " ord(2 mod 5) = 4 with 2^2 = -1",
      phi5_at_1 == 5 and j_at_1 == 2
      and pow(2, 2, 5) == 4 and pow(2, 4, 5) == 1
      and all(pow(2, d, 5) != 1 for d in (1, 2)))

# G02: Lemma A. The chronological four-phase increment is an exact readout
# of v_2(n+1) mod 4 through the ramified image 2:
#   Theta_n = 2^s_2(n) mod 5,  Theta_(n+1) * Theta_n^-1 = 2^(1 - v_2(n+1)).
TABLE = {c: pow(2, (1 - c) % 4, 5) for c in range(4)}
lemma_a = TABLE == {0: 2, 1: 1, 2: 3, 3: 4} and len(set(TABLE.values())) == 4
theta = 1  # Theta_0 = 2^s_2(0) = 1
N_RANGE = 1 << 18
for n in range(N_RANGE):
    inc = TABLE[v2(n + 1) % 4]
    theta_next = (theta * inc) % 5
    lemma_a = lemma_a and theta_next == pow(2, s2(n + 1), 5)
    theta = theta_next
check("G02 V2-READOUT      c mod 4 -> 2^(1-c) mod 5 is a bijection onto"
      " F_5^x; iterated increments match Theta_n = 2^s_2(n) for"
      " n < 2^18", lemma_a)

# G03: the readout inverts: the increment determines v_2(n+1) mod 4.
INV = {value: c for c, value in TABLE.items()}
recovery = all(INV[TABLE[v2(n + 1) % 4]] == v2(n + 1) % 4
               for n in range(N_RANGE))
check("G03 RECOVERY        the phase increment determines v_2(n+1) mod 4"
      " exactly; inverse table verified on the same range", recovery)

# G04: Lemma B finite witness. The increment stream is not periodic with
# any period p <= 128 anywhere past n = 0 (full proof in the note).
stream = [TABLE[v2(n + 1) % 4] for n in range(4096 + 129)]
nonper = all(any(stream[n + p] != stream[n] for n in range(4096))
             for p in range(1, 129))
check("G04 NONPERIODIC     for every period candidate p = 1..128 the"
      " increment stream breaks it at some n <= 4096", nonper)

# G05: exact mass law. On dyadic windows [0, 2^M) the counts of
# v_2(n+1) mod 4 match the closed formula and converge to (8,4,2,1)/15.
LIMIT = [Fraction(2 ** (3 - j), 15) for j in range(4)]
mass_ok = sum(LIMIT) == 1
counts = [0, 0, 0, 0]
M_MAX = 20
snapshots = {}
for n in range(1 << M_MAX):
    counts[v2(n + 1) % 4] += 1
    if (n + 1) & n == 0 and (n + 1).bit_length() - 1 >= 4:
        snapshots[(n + 1).bit_length() - 1] = tuple(counts)
for M, snap in snapshots.items():
    for j in range(4):
        closed = sum(2 ** (M - 1 - c) for c in range(j, M, 4))
        closed += 1 if M % 4 == j else 0
        mass_ok = mass_ok and snap[j] == closed
        gap = abs(Fraction(snap[j], 2 ** M) - LIMIT[j])
        mass_ok = mass_ok and gap <= Fraction(1, 2 ** (M - 1))
check("G05 HAAR-MASSES     window counts equal the closed formula for"
      " M = 4..20 and approach (8,4,2,1)/15 within 2^(1-M)", mass_ok)

# G06: the denominator 15 = 2^4 - 1 is the unit count of the residue
# field of the inert prime 2 in Q(zeta_5); the residue degree equals the
# four-phase order.
f = next(f for f in range(1, 5) if (2 ** f - 1) % 5 == 0)
check("G06 RESIDUE-DEGREE  the least f with 5 | 2^f - 1 is f = 4, so 2"
      " is inert with residue field F_16 and |F_16^x| = 15 is the mass"
      " denominator", f == 4 and 2 ** 4 - 1 == 15)

# G07: static audit of the frozen public affine table of
# probes/P-ENTROPY-BRIDGE-4 (EXPECTED_AFFINE, public data). The rows for
# k = 1..10 repeat with period four and the translation sets are a
# function of 2^k mod 5.
EXPECTED_AFFINE = (
    (0, 0, ((4, 0), (4, 2))),
    (0, 1, ((4, 0), (4, 2))),
    (1, 0, ((1, 0), (1, 3))),
    (1, 1, ((1, 0), (1, 3))),
    (2, 0, ((1, 1), (1, 3))),
    (2, 1, ((1, 1), (1, 3))),
    (3, 0, ((1, 1), (1, 4))),
    (3, 1, ((1, 1), (1, 4))),
    (4, 0, ((1, 0), (1, 3))),
    (4, 1, ((1, 0), (1, 3))),
    (5, 0, ((1, 0), (1, 3))),
    (5, 1, ((1, 0), (1, 3))),
    (6, 0, ((1, 1), (1, 3))),
    (6, 1, ((1, 1), (1, 3))),
    (7, 0, ((1, 1), (1, 4))),
    (7, 1, ((1, 1), (1, 4))),
    (8, 0, ((1, 0), (1, 3))),
    (8, 1, ((1, 0), (1, 3))),
    (9, 0, ((1, 0), (1, 3))),
    (9, 1, ((1, 0), (1, 3))),
    (10, 0, ((1, 1), (1, 3))),
    (10, 1, ((1, 1), (1, 3))),
)
rows = {(k, eps): pairs for k, eps, pairs in EXPECTED_AFFINE}
period4 = all(rows[(k, eps)] == rows[(k + 4, eps)]
              for eps in (0, 1) for k in range(1, 7))
bset = {}
functional = True
for k in range(1, 11):
    key = pow(2, k, 5)
    value = tuple(sorted({b for a, b in rows[(k, 0)]}))
    if key in bset:
        functional = functional and bset[key] == value
    else:
        bset[key] = value
level0 = all(a == 4 for a, b in rows[(0, 0)] + rows[(0, 1)])
check("G07 FROZEN-TABLE    the public bridge-4 affine rows repeat with"
      " period four for k = 1..10, the translation set is a function of"
      " 2^k mod 5, and only k = 0 has multiplier -1", period4
      and functional and level0
      and bset == {2: (0, 3), 4: (1, 3), 3: (1, 4), 1: (0, 3)})

# G08: independent audit of the registered TIME-QUANTUM-TOWER cases
# k = 1, 2: M_J^(5^k) is the scalar i_5 I with i_5 = 2 mod 5, i_5^4 = 1,
# and the period of M_J mod 5^k is exactly 4 * 5^k.  Also det M_J = 1.
M_J = (  # multiplication by J = 1 + zeta^2 on the basis 1, z, z^2, z^3
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)


def mat_mul(a, b, mod=0):
    n = len(a)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            s = sum(a[i][t] * b[t][j] for t in range(n))
            row.append(s % mod if mod else s)
        out.append(tuple(row))
    return tuple(out)


def mat_pow(a, e, mod):
    n = len(a)
    r = tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))
    base = tuple(tuple(x % mod for x in row) for row in a)
    while e:
        if e & 1:
            r = mat_mul(r, base, mod)
        base = mat_mul(base, base, mod)
        e >>= 1
    return r


def det4(a):
    def det(rows):
        if len(rows) == 1:
            return rows[0][0]
        total = 0
        for j in range(len(rows)):
            minor = [r[:j] + r[j + 1:] for r in rows[1:]]
            total += (-1) ** j * rows[0][j] * det(minor)
        return total
    return det([list(r) for r in a])


tower_ok = det4(M_J) == 1
for k in (1, 2):
    mod = 5 ** k
    ident = tuple(tuple(1 if i == j else 0 for j in range(4))
                  for i in range(4))
    p5 = mat_pow(M_J, 5 ** k, mod)
    scalar = p5[0][0]
    tower_ok = tower_ok and p5 == tuple(
        tuple(scalar if i == j else 0 for j in range(4)) for i in range(4))
    tower_ok = tower_ok and scalar % 5 == 2 and pow(scalar, 4, mod) == 1
    order = 4 * 5 ** k
    tower_ok = tower_ok and mat_pow(M_J, order, mod) == ident
    for q in (2, 5):
        tower_ok = tower_ok and mat_pow(M_J, order // q, mod) != ident
check("G08 TOWER-PERIOD    det M_J = 1; M_J^(5^k) = i_5 I with"
      " i_5 = 2 mod 5, i_5^4 = 1, and exact period 4 * 5^k for"
      " k = 1, 2", tower_ok)

# G09: rational identities behind the labeled numerical observation.
obs = (Fraction(1, 3) + Fraction(2, 15) * 5 == 1
       and sum(LIMIT) == 1
       and LIMIT[0] == Fraction(1, 3) + Fraction(1, 5)
       and LIMIT[2] == Fraction(2, 15))
check("G09 RATIONAL-IDS    (1/3) + (2/15)*5 = 1; 8/15 = 1/3 + 1/5; the"
      " third phase mass equals the registered M_TM coefficient 2/15"
      " as a number only", obs)

print()
print("RESULT %d/%d %s" % (PASS, PASS + FAIL,
                           "ALL PASS" if FAIL == 0 else "SOME FAIL"))
sys.exit(0 if FAIL == 0 else 1)
