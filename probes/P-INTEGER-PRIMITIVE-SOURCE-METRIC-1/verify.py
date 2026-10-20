#!/usr/bin/env python3
"""Exact prospective audit; standalone polynomial/matrix implementation.

Do not execute or import before the public pin is remotely read back.
The independent breaker is executed only as a subprocess, never imported.
"""

from dataclasses import dataclass, replace
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from math import gcd, lcm
import subprocess
import sys


PROBE = "P-INTEGER-PRIMITIVE-SOURCE-METRIC-1"
M = 324
DIPOLE = (1, -1, 0, 0, 0)
WORDS = (
    ("0010", 1, 0), ("0011", 1, 1), ("0100", 0, -1),
    ("0101", 0, 0), ("0110", 1, -1), ("1001", -1, 1),
    ("1010", 0, 0), ("1011", 0, 1), ("1100", -1, -1),
    ("1101", -1, 0),
)
AUTHORITY = (
    ("canon/CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)
PHI = (0, 0, -1, -1)
UNIT_J = (1, 0, 1, 0)
UNIT_J_INV = (0, -1, -1, 0)
PHI_INV = (-1, 0, -1, -1)
A = ((UNIT_J, ZERO), (ZERO, PHI))
A_INV = ((UNIT_J_INV, ZERO), (ZERO, PHI_INV))
IDENTITY = ((ONE, ZERO), (ZERO, ONE))
D8 = (0, 0, 1, 0, 0, 0, 0, 0)
Z08 = (1, 0, 1, 0, 0, 1, 0, 0)


class ScientificFailure(Exception):
    pass


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


def radd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def rneg(x):
    return tuple(-a for a in x)


def rsub(x, y):
    return radd(x, rneg(y))


def rmul(x, y):
    # Polynomial convolution followed by monic Phi_5 reduction.
    z = [0] * 7
    for i in range(4):
        for j in range(4):
            z[i + j] += x[i] * y[j]
    for degree in range(6, 3, -1):
        c = z[degree]
        for offset in range(1, 5):
            z[degree - offset] -= c
        z[degree] = 0
    return tuple(z[:4])


def rconj(x):
    return (x[0] - x[1], -x[1], x[3] - x[1], x[2] - x[1])


def rscale(n, x):
    return tuple(n * a for a in x)


def rtrace(x):
    return 4 * x[0] - x[1] - x[2] - x[3]


def mmul(x, y):
    return tuple(tuple(radd(rmul(x[i][0], y[0][j]),
                           rmul(x[i][1], y[1][j]))
                       for j in range(2)) for i in range(2))


def mdag(x):
    return tuple(tuple(rconj(x[j][i]) for j in range(2)) for i in range(2))


def real_ring(a0, a1):
    return radd((a0, 0, 0, 0), rscale(a1, PHI))


def real_pair(x):
    require(x[1] == 0 and x[2] == x[3], "RING")
    return (x[0], -x[2])


def unpack(h):
    a = real_ring(h[0], h[1])
    d = real_ring(h[2], h[3])
    c = h[4:]
    return ((a, c), (rconj(c), d))


def pack(h):
    require(h == mdag(h), "TRANSPORT")
    result = real_pair(h[0][0]) + real_pair(h[1][1]) + h[0][1]
    require(len(result) == 8 and all(type(v) is int for v in result),
            "TRANSPORT")
    return result


def shear(q):
    return ((ONE, (q, 0, 0, 0)), (ZERO, ONE))


def transport(matrix, h):
    return pack(mmul(mmul(matrix, unpack(h)), mdag(matrix)))


def determinant(h):
    mat = unpack(h)
    result = rsub(rmul(mat[0][0], mat[1][1]),
                  rmul(mat[0][1], mat[1][0]))
    real_pair(result)
    return result


def cost(h):
    a0, a1, d0, d1, *c = h
    return (4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
            + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
            + 10 * sum(t * t for t in c) - 2 * sum(c) ** 2)


def trace_cost(h):
    squared = mmul(unpack(h), unpack(h))
    return rtrace(radd(squared[0][0], squared[1][1]))


def vadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vsub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def capply(p):
    return tuple(460 * p[r]
                 + 29 * (p[(r - 1) % 5] + p[(r + 1) % 5])
                 + 65 * (p[(r - 2) % 5] + p[(r + 2) % 5])
                 for r in range(5))


def coefficient(k):
    return M if k == 1 else M * M


@dataclass(frozen=True)
class Core:
    s: int
    q: int
    H: tuple
    R: tuple
    Z: tuple
    P: tuple
    Q: tuple
    k: int
    p: int


def chi(x):
    return x.H[5] - x.R[5]


def energy(x):
    return (1 + x.s * x.s - x.s * x.q + x.q * x.q
            + cost(x.H) + cost(x.R) + cost(x.Z) + x.k
            + sum(t * t for t in x.P) + sum(t * t for t in x.Q))


def height(x):
    return 7 * (x.k - 1) + x.p


def in_carrier(x):
    integers = (x.s, x.q) + x.H + x.R + x.Z + x.P + x.Q + (x.k, x.p)
    return (len(integers) == 38 and all(type(v) is int for v in integers)
            and len(x.H) == len(x.R) == len(x.Z) == 8
            and len(x.P) == len(x.Q) == 5 and x.k >= 1 and 0 <= x.p < 7)


def bare(x, direction=1, coupling=1):
    """Total forward injection; None denotes missing backward image."""
    if direction == 1:
        if x.p == 0:
            y = replace(x, s=x.s - x.q, q=x.s)
        elif x.p == 1:
            y = replace(x, H=transport(shear(-x.q), x.H))
        elif x.p == 2:
            y = replace(x, H=transport(A_INV, x.H))
        elif x.p == 3:
            y = replace(x, H=transport(shear(x.q), x.H))
        elif x.p == 4:
            y = replace(x, H=transport(A, x.H))
        elif x.p == 5:
            y = replace(x, Z=vsub(vadd(x.Z, x.H), x.R))
        else:
            force = 2 * coupling * chi(x)
            new_p = tuple(c - coefficient(x.k) * q + force * ell
                          for c, q, ell in zip(capply(x.P), x.Q, DIPOLE))
            y = replace(x, P=new_p, Q=x.P, k=x.k + 1)
        return replace(y, p=(x.p + 1) % 7)
    require(direction == -1, "BRANCH")
    if x.p == 0:
        if x.k == 1:
            return None
        denom = coefficient(x.k - 1)
        force = 2 * coupling * chi(x)
        numer = tuple(c - p + force * ell
                      for c, p, ell in zip(capply(x.Q), x.P, DIPOLE))
        if any(t % denom for t in numer):
            return None
        return replace(x, P=x.Q, Q=tuple(t // denom for t in numer),
                       k=x.k - 1, p=6)
    previous = x.p - 1
    if previous == 0:
        y = replace(x, s=x.q, q=x.q - x.s)
    elif previous == 1:
        y = replace(x, H=transport(shear(x.q), x.H))
    elif previous == 2:
        y = replace(x, H=transport(A, x.H))
    elif previous == 3:
        y = replace(x, H=transport(shear(-x.q), x.H))
    elif previous == 4:
        y = replace(x, H=transport(A_INV, x.H))
    else:
        y = replace(x, Z=vadd(vsub(x.Z, x.H), x.R))
    return replace(y, p=previous)


def rev(state):
    x, bank, direction = state
    return (x, bank, -direction)


def funded(state, coupling=1):
    x, bank, direction = state
    y = bare(x, direction, coupling)
    if y is None:
        return rev(state)
    proposed_bank = bank + energy(x) - energy(y)
    if proposed_bank < 0:
        return rev(state)
    return (y, proposed_bank, direction)


def funded_inverse(state, coupling=1):
    return rev(funded(rev(state), coupling))


def initial_slices(word):
    bits = tuple(int(c) for c in word)
    return tuple(tuple(int(r == (bits[t + 2] - bits[t]) % 5)
                       + int(r == (bits[t + 2] - bits[t] + 1) % 5)
                       for r in range(5)) for t in (0, 1))


def ready(word, sign):
    p0, p1 = initial_slices(word)
    return Core(sign, 0, D8, D8, Z08, p1, p0, 1, 0)


def denominator(n):
    return 2 if n == 0 else 2 * M ** (n - 1)


def read_field(x):
    d = denominator(x.k)
    return tuple(Fraction(p, d) for p in x.P)


def norm2(v):
    return sum(t * t for t in v)


def laplacian(v):
    return tuple(Fraction(648 * x - y, M) for x, y in zip(v, capply(v)))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def audit_authority():
    root = Path(__file__).resolve().parents[2]
    count = 0
    for path, size, digest in AUTHORITY:
        data = (root / path).read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest,
                "AUTHORITY")
        count += 1
    return count


def hermitian_fixtures():
    fixtures = [(0,) * 8]
    for i in range(8):
        fixtures.append(tuple(int(i == j) for j in range(8)))
        fixtures.append(tuple(-int(i == j) for j in range(8)))
    fixtures.extend(((1, -1, 2, 0, -2, 1, 0, 1),
                     (0, 1, -1, 2, 1, 0, -1, 2)))
    require(len(fixtures) == 19, "CERTIFICATE")
    return fixtures


def audit_transport(fixtures):
    require(rmul(UNIT_J, UNIT_J_INV) == ONE, "RING")
    require(rmul(PHI, PHI_INV) == ONE, "RING")
    require(rmul(PHI, PHI) == radd(PHI, ONE), "RING")
    require(mmul(A, A_INV) == IDENTITY, "RING")
    require(rmul(rmul(UNIT_J, PHI), ONE) == ROOT, "RING")
    count = 0
    gates = [(A, A_INV), (A_INV, A)]
    gates.extend((shear(q), shear(-q)) for q in (-2, -1, 0, 1, 2))
    for h in fixtures:
        require(cost(h) >= 2 * norm2(h), "COST")
        require((cost(h) == 0) == (h == (0,) * 8), "COST")
        require(cost(h) == trace_cost(h), "COST")
        for gate, inverse in gates:
            y = transport(gate, h)
            require(transport(inverse, y) == h, "TRANSPORT")
            require(determinant(y) == determinant(h), "TRANSPORT")
            require(cost(y) == trace_cost(y) and cost(y) >= 2 * norm2(y),
                    "COST")
            count += 1
    require(count == 133, "CERTIFICATE")
    return count


def general_core(fixtures, i, k, p):
    return Core(i % 3 - 1, (i // 3) % 3 - 1,
                fixtures[i], fixtures[(i + 5) % 19], fixtures[(i + 11) % 19],
                (i - 9, 1, -2, 0, 3), (2, -1, 0, 1, 9 - i), k, p)


def audit_carrier(fixtures):
    core_count = funded_count = defect_count = 0
    for i in range(19):
        for k in (1, 2, 3):
            for phase in range(7):
                x = general_core(fixtures, i, k, phase)
                y = bare(x)
                require(in_carrier(x) and in_carrier(y), "BARE_INVERSE")
                require(bare(y, -1) == x and height(y) == height(x) + 1,
                        "BARE_INVERSE")
                core_count += 1
                for z in (x, y):
                    require(energy(z) > 0, "COST")
                    delta = energy(bare(z)) - energy(z)
                    banks = (0, 1, 772, max(0, delta - 1),
                             max(0, delta), max(0, delta + 1))
                    for bank in banks:
                        for direction in (-1, 1):
                            state = (z, bank, direction)
                            after = funded(state)
                            require(funded_inverse(after) == state,
                                    "FUNDED_INVERSE")
                            require(funded(funded_inverse(state)) == state,
                                    "FUNDED_INVERSE")
                            require(in_carrier(after[0]) and after[1] >= 0
                                    and after[2] in (-1, 1), "BRANCH")
                            require(energy(after[0]) + after[1]
                                    == energy(z) + bank, "CONSERVATION")
                            target = bare(z, direction)
                            if target is None:
                                expected = rev(state)
                            else:
                                balance = bank + energy(z) - energy(target)
                                expected = ((target, balance, direction)
                                            if balance >= 0 else rev(state))
                            require(after == expected, "BRANCH")
                            funded_count += 1
        boundary = general_core(fixtures, i, 1, 0)
        require(bare(boundary, -1) is None, "IMAGE_GUARD")
        boundary_state = (boundary, 1000000000, -1)
        require(funded(boundary_state) == rev(boundary_state), "IMAGE_GUARD")
        for previous_k in (1, 2):
            image = bare(general_core(fixtures, i, previous_k, 6))
            corrupted_p = list(image.P)
            corrupted_p[2] += 1
            corrupt = replace(image, P=tuple(corrupted_p))
            require(bare(corrupt, -1) is None, "IMAGE_GUARD")
            state = (corrupt, 1000000000, -1)
            require(funded(state) == rev(state), "IMAGE_GUARD")
            defect_count += 1
    require((core_count, funded_count, defect_count) == (399, 9576, 38),
            "CERTIFICATE")
    return core_count, funded_count, defect_count


def audit_initial_data():
    require(len(WORDS) == 10 and len({w for w, _, _ in WORDS}) == 10,
            "INITIAL_DATA")
    for word, u0, u1 in WORDS:
        bits = tuple(int(c) for c in word)
        require((bits[2] - bits[0], bits[3] - bits[1]) == (u0, u1),
                "INITIAL_DATA")
        slices = initial_slices(word)
        for p, u in zip(slices, (u0, u1)):
            expected = tuple(int(r == u % 5) + int(r == (u + 1) % 5)
                             for r in range(5))
            require(p == expected and sum(p) == 2
                    and sorted(p) == [0, 0, 0, 1, 1], "INITIAL_DATA")


def build_history(word, sign):
    """Integer gate and separate rational recurrence, through counter 24."""
    p0, p1 = initial_slices(word)
    nums = [p0, p1]
    fields = [tuple(Fraction(t, 2) for t in p0),
              tuple(Fraction(t, 2) for t in p1)]
    sources = {}
    x = ready(word, sign)
    pattern = (1, 2, 2, 1, 0, 0)
    for n in range(1, 24):
        require(x.k == n and x.p == 0, "RECURRENCE")
        for _ in range(6):
            x = bare(x)
            require(determinant(x.H) == determinant(D8), "TRANSPORT")
        require(x.p == 6 and x.k == n, "SOURCE_PATTERN")
        c = chi(x)
        require(c == sign * pattern[(n - 1) % 6], "SOURCE_PATTERN")
        sources[n] = tuple(Fraction(c * ell, M ** n) for ell in DIPOLE)
        reference = tuple(cp / M - old + j
                          for cp, old, j in
                          zip(capply(fields[n]), fields[n - 1], sources[n]))
        x = bare(x)
        actual = read_field(x)
        require(actual == reference and x.Q == nums[-1], "RECURRENCE")
        require(energy(x) >= norm2(x.P), "COST")
        nums.append(x.P)
        fields.append(actual)
    return nums, fields, sources


def check_metric(h):
    for value in h:
        require(Fraction(-299, 500) < value < Fraction(499, 500), "LORENTZ")
        require(1 + value > Fraction(201, 500)
                and 1 - value > Fraction(1, 500), "LORENTZ")
        require(-(1 - value * value) < Fraction(-999, 250000), "LORENTZ")


def local_action(v, previous, following, source):
    kinetic = (norm2(vsub(v, previous)) + norm2(vsub(following, v))) / 2
    return kinetic - dot(v, laplacian(v)) / 2 + dot(source, v)


def audit_histories():
    audit_initial_data()
    histories = {}
    digest = sha256()
    record_count = variation_count = 0
    for word, _, _ in WORDS:
        for sign in (-1, 0, 1):
            nums, fields, sources = build_history(word, sign)
            histories[(word, sign)] = (nums, fields, sources)
            for n, (p, h) in enumerate(zip(nums, fields)):
                d = denominator(n)
                require(sum(p) == d and sum(h) == 1, "MEAN")
                require(gcd(d, *p) == 1 and gcd(*p) == 1, "DENOMINATOR")
                require(lcm(*(t.denominator for t in h)) == d, "DENOMINATOR")
                require(5 * norm2(p) >= d * d
                        and 5 * (norm2(p) + d * d) >= 6 * d * d,
                        "DENOMINATOR")
                require(max(abs(t) for t in p) >= (d + 4) // 5, "DENOMINATOR")
                check_metric(h)
                record = (word + "|" + str(sign) + "|" + str(n) + "|"
                          + ",".join(str(t) for t in p) + "|" + str(d) + "\n")
                digest.update(record.encode("ascii"))
                record_count += 1
            for n in range(1, 24):
                residual = tuple(future - 2 * now + past + l
                                 for future, now, past, l in
                                 zip(fields[n + 1], fields[n], fields[n - 1],
                                     laplacian(fields[n])))
                require(residual == sources[n], "RECURRENCE")
                if sign == 0:
                    require(residual == (0,) * 5, "CONTROL")
            for n in (1, 2, 7, 23):
                for site in range(5):
                    plus = list(fields[n])
                    minus = list(fields[n])
                    plus[site] += 1
                    minus[site] -= 1
                    derivative = (
                        local_action(tuple(plus), fields[n - 1],
                                     fields[n + 1], sources[n])
                        - local_action(tuple(minus), fields[n - 1],
                                       fields[n + 1], sources[n])) / 2
                    require(derivative == 0, "ACTION")
                    variation_count += 1
        free = histories[(word, 0)][1]
        for sign in (-1, 1):
            for h, h_free in zip(histories[(word, sign)][1], free):
                require(all(abs(t - f) < Fraction(1, 125)
                            for t, f in zip(h, h_free)), "RESPONSE_BOUND")
    require(record_count == 750 and variation_count == 600, "CERTIFICATE")
    return record_count, digest.hexdigest(), variation_count


def first_block(sign, coupling=1):
    cores = [ready("0010", sign)]
    for _ in range(7):
        cores.append(bare(cores[-1], coupling=coupling))
    return cores


def audit_witnesses():
    blocks = {sign: first_block(sign) for sign in (-1, 1)}
    prefixes = tuple(tuple(energy(x) for x in blocks[sign])
                     for sign in (-1, 1))
    require(prefixes == (
        (31, 31, 43, 63, 147, 377, 747, 344440),
        (31, 31, 43, 63, 147, 377, 803, 347088)), "PREFIX")
    p2s = tuple(blocks[sign][-1].P for sign in (-1, 1))
    require(p2s == ((487, 167, -230, 130, 94),
                    (491, 163, -230, 130, 94)), "FIXED_COUNTER")
    sharp_banks = tuple(max(e) - e[0] for e in prefixes)
    require(sharp_banks == (344409, 347057), "SHARP_BUDGET")
    common_banks = []
    common_fields = []
    for sign, sharp in zip((-1, 1), sharp_banks):
        block = blocks[sign]
        written = block[6]
        require(written.Z[5] == (0 if sign == -1 else 2), "DETECTOR")
        require(vadd(vsub(written.Z, written.H), written.R) == Z08,
                "DETECTOR")
        for bank, complete in ((sharp, True), (sharp - 1, False),
                               (347057, True)):
            state = (block[0], bank, 1)
            for step in range(1, 8):
                state = funded(state)
                if step <= 6:
                    require(state[0] == block[step] and state[2] == 1,
                            "SHARP_BUDGET")
            if complete:
                require(state[0] == block[7] and state[2] == 1,
                        "SHARP_BUDGET")
            else:
                require(state[0] == block[6] and state[2] == -1,
                        "SHARP_BUDGET")
            if bank == sharp and complete:
                require(state[1] == 0, "SHARP_BUDGET")
        state = (block[0], 347057, 1)
        for _ in range(7):
            state = funded(state)
        require(state[0].k == 2 and state[0].p == 0 and state[2] == 1,
                "FIXED_COUNTER")
        common_banks.append(state[1])
        common_fields.append(read_field(state[0]))
        # Genuine image is accepted; the source-free congruence is not.
        image = block[-1]
        require(bare(image, -1) == block[-2], "IMAGE_GUARD")
        omitted = vsub(capply(image.Q), image.P)
        require(any(v % M for v in omitted), "CONTROL")
        # Wrong first divisor changes the mean, even with the same source.
        start = block[0]
        wrong = tuple(cp - M * M * q + 2 * sign * ell
                      for cp, q, ell in zip(capply(start.P), start.Q, DIPOLE))
        require(sum(wrong) != denominator(2), "CONTROL")
    contrast = vsub(common_fields[1], common_fields[0])
    require(contrast == (Fraction(1, 162), Fraction(-1, 162), 0, 0, 0),
            "FIXED_COUNTER")
    require(tuple(common_banks) == (2648, 0), "SHARP_BUDGET")
    controls = []
    for sign in (-1, 1):
        state = (ready("0010", sign), 347057, 1)
        for _ in range(7):
            state = funded(state, coupling=0)
        require(state[0].k == 2 and state[0].p == 0 and state[2] == 1,
                "CONTROL")
        require(state[0].Z[5] == (0 if sign == -1 else 2), "CONTROL")
        controls.append(state[0].P)
    require(controls[0] == controls[1] == (489, 165, -230, 130, 94),
            "CONTROL")
    degenerate = replace(ready("0010", 1), P=(2, 0, 0, 0, 0), k=1)
    degenerate_h = read_field(degenerate)[0]
    require(degenerate_h == 1 and 1 - degenerate_h == 0, "CONTROL")
    return prefixes, p2s, sharp_banks, tuple(common_banks), contrast


def audit_cycles():
    cases = ((-1, 772, 14), (-1, 344409, 18), (-1, 347057, 24),
             (-1, 344408, 14), (1, 772, 14), (1, 344409, 14),
             (1, 347057, 18), (1, 347056, 14))
    periods = []
    for sign, bank, expected in cases:
        initial = (ready("0010", sign), bank, 1)
        total = energy(initial[0]) + bank
        state = initial
        seen = {initial}
        for tick in range(1, expected + 1):
            state = funded(state)
            require(energy(state[0]) + state[1] == total, "CONSERVATION")
            if tick < expected:
                require(state not in seen, "PERIOD")
                seen.add(state)
            else:
                require(state == initial and len(seen) == expected, "PERIOD")
                periods.append(tick)
    require(len(periods) == 8, "CERTIFICATE")
    return tuple(periods)


def csv(values):
    return ",".join(str(value) for value in values)


def certificate():
    authority_count = audit_authority()
    fixtures = hermitian_fixtures()
    transports = audit_transport(fixtures)
    cores, funding, defects = audit_carrier(fixtures)
    records, history_hash, variations = audit_histories()
    prefixes, p2s, sharp, common, contrast = audit_witnesses()
    periods = audit_cycles()
    lines = (
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=" + str(authority_count),
        "TRANSPORT_CHECKS=" + str(transports),
        "CORE_FIXTURES=" + str(cores),
        "FUNDED_CASES=" + str(funding),
        "IMAGE_DEFECTS=" + str(defects),
        "HISTORY_RECORDS=" + str(records),
        "HISTORY_SHA256=" + history_hash,
        "ACTION_VARIATIONS=" + str(variations),
        "PREFIX_NEG=" + csv(prefixes[0]),
        "PREFIX_POS=" + csv(prefixes[1]),
        "P2_NEG=" + csv(p2s[0]),
        "P2_POS=" + csv(p2s[1]),
        "SHARP_BANKS=" + csv(sharp),
        "COMMON_FINAL_BANKS=" + csv(common),
        "METRIC_CONTRAST=" + csv(contrast),
        "CYCLE_PERIODS=" + csv(periods),
        "NEGATIVE_CONTROLS=PASS",
        "CERTIFICATE_RESULT=PASS",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        own = certificate()
        child = subprocess.run(
            [sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if child.returncode != 0:
            raise RuntimeError("BREAKER_EXIT")
        if child.stderr != b"":
            raise RuntimeError("BREAKER_STDERR")
        # Deliberately compare unmodified bytes, including every newline.
        if child.stdout != own:
            sys.stdout.buffer.write(
                ("FALSIFIER=BREAKER_BYTES\nBREAKER_STDOUT_HEX="
                 + child.stdout.hex() + "\nRESULT=FAIL\n").encode("ascii"))
            return
        sys.stdout.buffer.write(own + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except ScientificFailure as failure:
        sys.stdout.buffer.write(
            ("FALSIFIER=" + str(failure) + "\nRESULT=FAIL\n").encode("ascii"))


if __name__ == "__main__":
    main()
