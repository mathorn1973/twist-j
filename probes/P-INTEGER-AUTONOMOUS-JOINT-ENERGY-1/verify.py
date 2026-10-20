#!/usr/bin/env python3
"""Prospective exact gate: integer recurrence and polynomial-ring matrices.

Do not execute/import before the complete public pin is read back.
The separate breaker uses rational evolution and direct Hermitian coordinates.
Shared mathematical specification and assisted-session context are disclosed.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as Q
from hashlib import sha256
from functools import lru_cache
from itertools import combinations
from math import lcm
from pathlib import Path
import subprocess
import sys

PROBE = "P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1"
M = 324
ELL = (1, -1, 0, 0, 0)
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
J = (1, 0, 1, 0)
J_INV = (0, -1, -1, 0)
PHI_INV = (-1, 0, -1, -1)
LOOP_V = (-2, 1, -1, 0)
A = ((J, ZERO), (ZERO, PHI))
A_INV = ((J_INV, ZERO), (ZERO, PHI_INV))
IDENTITY = ((ONE, ZERO), (ZERO, ONE))
D_H = (0, 0, 1, 0, 0, 0, 0, 0)
REGISTERED_KEYS = frozenset((
    "AUTHORITY", "RING", "TRANSPORT", "HOLONOMY", "COST", "INITIAL_DATA",
    "INTEGER", "BARE_INVERSE", "FUNDED_INVERSE", "CONSERVATION", "BRANCH",
    "IMAGE_GUARD", "RECURRENCE", "MEAN", "SOURCE_READER", "LORENTZ",
    "SOURCE_BOUND", "EQUILIBRIUM", "ENERGY", "PRECISION", "GRAM",
    "ACTION", "OFFSHELL_ACTION", "CANONICAL", "SYMPLECTIC", "FIXED_COUNTER",
    "CONTROL", "SHARP_BUDGET", "PERIOD", "CERTIFICATE", "BREAKER_BYTES",
))


class ScientificFailure(Exception):
    def __init__(self, key):
        if key not in REGISTERED_KEYS:
            raise RuntimeError("UNREGISTERED_FALSIFIER")
        super().__init__(key)


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def times(n, x):
    return tuple(n * a for a in x)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm(x):
    return dot(x, x)


def rmul(x, y):
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


def rtrace(x):
    return 4 * x[0] - x[1] - x[2] - x[3]


def mmul(x, y):
    return tuple(tuple(add(rmul(x[i][0], y[0][j]),
                           rmul(x[i][1], y[1][j]))
                       for j in range(2)) for i in range(2))


def dagger(x):
    return tuple(tuple(rconj(x[j][i]) for j in range(2)) for i in range(2))


def real(a, b):
    return add((a, 0, 0, 0), times(b, PHI))


def real_pair(x):
    require(x[1] == 0 and x[2] == x[3], "RING")
    return (x[0], -x[2])


def unpack(h):
    return ((real(h[0], h[1]), h[4:]),
            (rconj(h[4:]), real(h[2], h[3])))


def pack(h):
    require(h == dagger(h), "TRANSPORT")
    v = real_pair(h[0][0]) + real_pair(h[1][1]) + h[0][1]
    require(len(v) == 8 and all(type(t) is int for t in v), "TRANSPORT")
    return v


def shear(t):
    return ((ONE, (t, 0, 0, 0)), (ZERO, ONE))


def loop(t):
    return ((ONE, times(t, LOOP_V)), (ZERO, ONE))


def transport(mat, h):
    return pack(mmul(mmul(mat, unpack(h)), dagger(mat)))


def determinant(h):
    x = unpack(h)
    det = sub(rmul(x[0][0], x[1][1]), rmul(x[0][1], x[1][0]))
    real_pair(det)
    return det


def cost(h):
    a, b, d, e, *c = h
    return (4*a*a + 4*a*b + 6*b*b + 4*d*d + 4*d*e + 6*e*e
            + 10*norm(c) - 2*sum(c)**2)


def trace_cost(h):
    squared = mmul(unpack(h), unpack(h))
    return rtrace(add(squared[0][0], squared[1][1]))


def ready_h(y):
    return (9*y*y, -5*y*y, 1, 0, -2*y, y, -y, 0)


def capply(p):
    return tuple(460*p[r] + 29*(p[(r-1) % 5]+p[(r+1) % 5])
                 + 65*(p[(r-2) % 5]+p[(r+2) % 5]) for r in range(5))


def lap(p):
    return tuple(Q(648*v-c, M) for v, c in zip(p, capply(p)))


def bapply(z):
    return add(capply(z[:5]), times(z[5], ELL)) + (dot(ELL, z[:5])+M*z[5],)


def kapply(z):
    return sub(lap(z[:5]), times(Q(z[5], M), ELL)) + (z[5]-Q(dot(ELL, z[:5]), M),)


@lru_cache(maxsize=None)
def equilibrium(a):
    amplitude = Q(a, 4)
    h = tuple(Q(1, 5)+amplitude*Q(v, 8683757)
              for v in (40986, -40986, 5832, 0, -5832))
    return h + (amplitude*Q(8684010, 8683757),)


def bond_energy(previous, current, a):
    center = equilibrium(a)
    x, y = sub(previous, center), sub(current, center)
    return Q(norm(sub(y, x))+dot(x, kapply(y)), 2)


@dataclass(frozen=True)
class Core:
    P: tuple
    W: tuple
    Y: int
    V: int
    H: tuple
    D: int


def in_carrier(x):
    coordinates = x.P+x.W+(x.Y, x.V)+x.H+(x.D,)
    return (len(x.P) == len(x.W) == 5 and len(x.H) == 8
            and len(coordinates) == 21 and x.D >= 1
            and all(type(t) is int for t in coordinates))


def energy(x):
    return 1+x.D+norm(x.P)+norm(x.W)+x.Y*x.Y+x.V*x.V+cost(x.H)


def decode(x):
    return tuple(Q(t, x.D) for t in x.P), Q(x.Y, x.D)


def decode_pair(x):
    return (tuple(Q(t, x.D) for t in x.W+(x.V,)),
            tuple(Q(t, x.D) for t in x.P+(x.Y,)))


@lru_cache(maxsize=None)
def physical_energy(x, a):
    return bond_energy(*decode_pair(x), a)


def advance(x, a, field=1, feedback=1, monitor=True):
    p = tuple(c-M*w+field*x.Y*ell for c, w, ell in zip(capply(x.P), x.W, ELL))
    y = M*x.Y-M*x.V+81*a*x.D+feedback*dot(ELL, x.P)
    h = transport(loop(y-x.Y), x.H) if monitor else x.H
    return Core(p, times(M, x.P), y, M*x.Y, h, M*x.D)


def backward(x, a):
    if x.D % M or any(t % M for t in x.W+(x.V,)):
        return None
    d, p, y = x.D//M, tuple(t//M for t in x.W), x.V//M
    num_w = tuple(c+y*ell-current for c, ell, current in zip(capply(p), ELL, x.P))
    num_v = M*y+81*a*d+dot(ELL, p)-x.Y
    if any(t % M for t in num_w+(num_v,)):
        return None
    h = transport(loop(y-x.Y), x.H)
    return Core(p, tuple(t//M for t in num_w), y, num_v//M, h, d)


def bare(x, a, direction=1):
    require(direction in (-1, 1), "BRANCH")
    return advance(x, a) if direction == 1 else backward(x, a)


def rev(s):
    x, bank, direction = s
    return x, bank, -direction


def funded(s, a):
    x, bank, direction = s
    y = bare(x, a, direction)
    if y is None:
        return rev(s)
    new_bank = bank+energy(x)-energy(y)
    return rev(s) if new_bank < 0 else (y, new_bank, direction)


def finverse(s, a):
    return rev(funded(rev(s), a))


def initial(word):
    bits = tuple(int(t) for t in word)
    return tuple(tuple(int(r in ((bits[n+2]-bits[n]) % 5,
                                 (bits[n+2]-bits[n]+1) % 5)) for r in range(5))
                 for n in (0, 1))


def ready(word, a):
    p0, p1 = initial(word)
    return Core(tuple(6+5*t for t in p1), tuple(6+5*t for t in p0),
                10*a, 0, transport(loop(10*a), D_H), 40)


def hermitian_fixtures():
    out = [(0,)*8]
    for i in range(8):
        for sign in (1, -1):
            out.append(tuple(sign if j == i else 0 for j in range(8)))
    out.extend(((1, -1, 2, 0, -2, 1, 0, 1), (0, 1, -1, 2, 1, 0, -1, 2)))
    require(len(out) == 19, "CERTIFICATE")
    return tuple(out)


def audit_authority():
    root = Path(__file__).resolve().parents[2]
    for path, size, digest in AUTHORITY:
        data = (root/path).read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest, "AUTHORITY")
    return len(AUTHORITY)


def audit_ring(hf):
    require(rmul(J, J_INV) == ONE and rmul(PHI, PHI_INV) == ONE, "RING")
    require(rmul(PHI, PHI) == add(PHI, ONE), "RING")
    require(mmul(A, A_INV) == IDENTITY and rmul(J, PHI) == ROOT, "RING")
    require(sub(rmul(J, PHI_INV), ONE) == LOOP_V, "RING")
    require(rmul(LOOP_V, rconj(LOOP_V)) == real(9, -5), "RING")
    transports = holonomies = 0
    pairs = [(A, A_INV), (A_INV, A)]
    pairs += [(shear(t), shear(-t)) for t in (-2, -1, 0, 1, 2)]
    for h in hf:
        for gate, inverse in pairs:
            y = transport(gate, h)
            require(transport(inverse, y) == h and determinant(y) == determinant(h), "TRANSPORT")
            for z in (h, y):
                require(cost(z) == trace_cost(z) and cost(z) >= 2*norm(z)
                        and (cost(z) == 0) == (z == (0,)*8), "COST")
            transports += 1
        for t in (-2, -1, 0, 1, 2):
            factor = mmul(mmul(mmul(A, shear(t)), A_INV), shear(-t))
            require(factor == loop(t), "HOLONOMY")
            y = transport(loop(t), h)
            require(y == transport(factor, h) and transport(loop(-t), y) == h
                    and determinant(y) == determinant(h), "HOLONOMY")
            holonomies += 1
    require((transports, holonomies) == (133, 95), "CERTIFICATE")
    return transports, holonomies


def audit_core(hf):
    base = []
    for a in (-1, 0, 1):
        for i, h in enumerate(hf):
            for d in (1, 2, 40):
                base.append((a, Core((i-9, 1, -2, 0, 3), (2, -1, 0, 1, 9-i),
                                     i % 5-2, (i//5) % 5-2, h, d)))
    down = Core((0,)*5, (0,)*5, 100, 100, ready_h(100), 1)
    require(energy(advance(down, 0)) < energy(down), "BRANCH")
    fixtures = base+[(0, down)]
    count = defects = 0
    branches = set()
    for a, x in fixtures:
        require(in_carrier(x), "INTEGER")
        y = advance(x, a)
        require(in_carrier(y) and y.D == M*x.D and backward(y, a) == x, "BARE_INVERSE")
        require(backward(x, a) is None, "IMAGE_GUARD")
        for z in (x, y):
            delta = energy(advance(z, a))-energy(z)
            banks = (0, 1, 772, max(0, delta-1), max(0, delta), max(0, delta+1))
            for bank in banks:
                for direction in (-1, 1):
                    state = z, bank, direction
                    target = bare(z, a, direction)
                    if target is None:
                        branches.add("domain-")
                        expected = rev(state)
                    elif bank+energy(z) < energy(target):
                        branches.add("bank"+str(direction))
                        expected = rev(state)
                    else:
                        branches.add("move"+str(direction))
                        expected = target, bank+energy(z)-energy(target), direction
                    out = funded(state, a)
                    require(out == expected, "BRANCH")
                    require(in_carrier(out[0]) and type(out[1]) is int
                            and out[1] >= 0 and out[2] in (-1, 1), "INTEGER")
                    require(energy(z)+bank == energy(out[0])+out[1], "CONSERVATION")
                    require(physical_energy(z, a) == physical_energy(out[0], a), "ENERGY")
                    require(finverse(out, a) == state
                            and funded(finverse(state, a), a) == state, "FUNDED_INVERSE")
                    count += 1
    require(branches == {"domain-", "bank1", "bank-1", "move1", "move-1"}, "BRANCH")
    for a, x in base:
        y = advance(x, a)
        corruptions = [replace(y, D=y.D+1)]
        for attr in ("W", "P"):
            for r in range(5):
                values = list(getattr(y, attr))
                values[r] += 1
                corruptions.append(replace(y, **{attr: tuple(values)}))
            name = "V" if attr == "W" else "Y"
            corruptions.append(replace(y, **{name: getattr(y, name)+1}))
        require(len(corruptions) == 13, "CERTIFICATE")
        for corrupt in corruptions:
            require(backward(corrupt, a) is None, "IMAGE_GUARD")
            state = corrupt, 1000000000, -1
            require(funded(state, a) == rev(state), "IMAGE_GUARD")
            defects += 1
    require((len(fixtures), count, defects) == (172, 4128, 2223), "CERTIFICATE")
    return len(fixtures), count, defects


def history(word, a, end=12, field=1, feedback=1, first_only=False, monitor=True):
    x = ready(word, a)
    cores = [None, x]
    fields = [tuple(Q(t, 40) for t in x.W), decode(x)[0]]
    sources = [Q(0), Q(a, 4)]
    for step in range(1, end):
        back = 0 if first_only and step >= 2 else feedback
        x = advance(x, a, field=field, feedback=back, monitor=monitor)
        cores.append(x)
        h, chi = decode(x)
        fields.append(h)
        sources.append(chi)
    return cores, fields, sources


def free_history(word, a, end=12):
    x = ready(word, a)
    h = [tuple(Q(t, 40) for t in x.W), decode(x)[0]]
    chi = [Q(0), Q(a, 4)]
    for _ in range(1, end):
        h.append(tuple(2*v-old-l for v, old, l in zip(h[-1], h[-2], lap(h[-1]))))
        chi.append(chi[-1]-chi[-2]+Q(a, 4))
    return h, chi


def local_action(v, xi, hp, hn, cp, cn, a):
    return (Q(norm(sub(v, hp))+norm(sub(hn, v)), 2)-Q(dot(v, lap(v)), 2)
            +Q((xi-cp)**2+(cn-xi)**2, 2)-Q(xi*xi, 2)+Q(a, 4)*xi
            +Q(xi, M)*dot(ELL, v))


def central_gradients(v, xi, hp, hn, cp, cn, a):
    out = []
    for r in range(5):
        e = tuple(int(i == r) for i in range(5))
        out.append((local_action(add(v, e), xi, hp, hn, cp, cn, a)
                    -local_action(sub(v, e), xi, hp, hn, cp, cn, a))/2)
    out.append((local_action(v, xi+1, hp, hn, cp, cn, a)
                -local_action(v, xi-1, hp, hn, cp, cn, a))/2)
    return tuple(out)


def exact_gradients(v, xi, hp, hn, cp, cn, a):
    metric = tuple(2*t-p-f-l+Q(xi*ell, M)
                   for t, p, f, l, ell in zip(v, hp, hn, lap(v), ELL))
    return metric+(xi-cn-cp+Q(a, 4)+Q(dot(ELL, v), M),)


def csv(values):
    return ",".join(str(t) for t in values)


def valuation_three(value):
    require(value > 0 and type(value) is int, "PRECISION")
    count = 0
    while value % 3 == 0:
        value //= 3
        count += 1
    return count


def audit_histories():
    digest = sha256()
    count = variations = precision = bonds = 0
    histories = {}
    for word, u0, u1 in WORDS:
        p0, p1 = initial(word)
        for p, u in ((p0, u0), (p1, u1)):
            require(p[u % 5] == p[(u+1) % 5] == 1
                    and sorted(p) == [0, 0, 0, 1, 1], "INITIAL_DATA")
        for a in (-1, 0, 1):
            cores, fields, sources = history(word, a)
            histories[(word, a)] = cores, fields, sources
            h_initial = physical_energy(cores[1], a)
            for n in range(13):
                d = 40 if n == 0 else 40*M**(n-1)
                p = tuple(6+5*t for t in p0) if n == 0 else cores[n].P
                y = 0 if n == 0 else cores[n].Y
                h8 = D_H if n == 0 else cores[n].H
                h, chi = fields[n], sources[n]
                require(tuple(Q(t, d) for t in p) == h and Q(y, d) == chi, "INTEGER")
                require(sum(p) == d and sum(h) == 1, "MEAN")
                require(h8 == ready_h(y) and Q(h8[5], d) == chi
                        and determinant(h8) == ZERO, "SOURCE_READER")
                require(cost(h8) == 294*y**4+52*y*y+4, "COST")
                require(abs(chi) < Q(3, 4), "SOURCE_BOUND")
                for value in h:
                    require(Q(-1, 4) < value < Q(13, 20)
                            and abs(value-Q(1, 5)) < Q(9, 20)
                            and -(1-value*value) < Q(-231, 400), "LORENTZ")
                if n >= 1:
                    x = cores[n]
                    expected_previous = (tuple(6+5*t for t in p0) if n == 1
                                         else times(M, cores[n-1].P))
                    require(in_carrier(x) and x.D == d and x.W == expected_previous
                            and x.V == (0 if n == 1 else M*cores[n-1].Y)
                            and sum(x.W) == d, "INTEGER")
                    require(5*energy(x) >= d*d, "COST")
                    require(physical_energy(x, a) == h_initial
                            and 0 < h_initial < Q(3, 50), "ENERGY")
                    bonds += 1
                    lcd = lcm(*(value.denominator for value in h+(chi,)))
                    require(valuation_three(lcd) == 4*(n-1), "PRECISION")
                    primitive = tuple(value*lcd for value in h+(chi,))
                    require(all(value.denominator == 1 for value in primitive)
                            and sum(primitive[:5]) == lcd
                            and 5*(norm(primitive)+lcd*lcd) >= 6*3**(8*(n-1)), "PRECISION")
                    precision += 1
                line = (word+"|"+str(a)+"|"+str(n)+"|"+csv(p)+"|"+str(y)
                        +"|"+str(d)+"|"+csv(h8)+"\n")
                digest.update(line.encode("ascii"))
                count += 1
            for n in range(1, 12):
                rh = tuple(f-2*v+p+l-Q(sources[n]*ell, M)
                           for f, v, p, l, ell in zip(fields[n+1], fields[n],
                                                      fields[n-1], lap(fields[n]), ELL))
                rc = sources[n+1]-sources[n]+sources[n-1]-Q(a, 4)-Q(dot(ELL, fields[n]), M)
                require(rh == (0,)*5 and rc == 0, "RECURRENCE")
            for n in (1, 2, 5, 11):
                point = (fields[n], sources[n], fields[n-1], fields[n+1],
                         sources[n-1], sources[n+1], a)
                require(central_gradients(*point) == (0,)*6, "ACTION")
                variations += 6
    require((count, variations, bonds, precision) == (390, 720, 360, 360), "CERTIFICATE")
    return count, digest.hexdigest(), variations, bonds, precision, histories


def audit_offshell(histories):
    _, h, c = histories[("0011", 0)]
    center = (h[2], c[2], h[1], h[3], c[1], c[3], 0)
    cases = []
    for field, value in ((0, add(h[2], (1, 0, 0, 0, 0))),
                         (1, c[2]+1), (5, c[3]+1),
                         (3, add(h[3], (0, 0, 1, 0, 0))), (4, c[1]-1)):
        point = list(center)
        point[field] = value
        cases.append(tuple(point))
    cases.append(((Q(1, 3), Q(-2, 5), Q(0), Q(3, 7), Q(-1)), Q(-2, 3),
                  (Q(0),)*5, (Q(1),)*5, Q(1, 2), Q(-3, 4), 1))
    for point in cases:
        expected = exact_gradients(*point)
        require(any(t != 0 for t in expected)
                and central_gradients(*point) == expected, "OFFSHELL_ACTION")
    require(len(cases)*6 == 36, "CERTIFICATE")
    return 36


def qdet(matrix):
    data = [[Q(t) for t in row] for row in matrix]
    determinant_value = Q(1)
    for k in range(len(data)):
        pivot = next((r for r in range(k, len(data)) if data[r][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            data[k], data[pivot] = data[pivot], data[k]
            determinant_value = -determinant_value
        value = data[k][k]
        determinant_value *= value
        for r in range(k+1, len(data)):
            factor = data[r][k]/value
            for c in range(k+1, len(data)):
                data[r][c] -= factor*data[k][c]
            data[r][k] = Q(0)
    return determinant_value


def audit_stiffness():
    basis = [tuple(int(j == i)-int(j == 4) for j in range(6)) for i in range(4)]
    basis.append((0, 0, 0, 0, 0, 1))
    operators = (
        lambda v: sub(kapply(v), times(Q(59, 100), v)),
        lambda v: sub(times(Q(201, 200), v), kapply(v)),
        lambda v: sub(sub(kapply(v), times(Q(1, 4), kapply(kapply(v)))), times(Q(1, 2), v)),
    )
    count = 0
    for operator in operators:
        gram = tuple(tuple(dot(u, operator(v)) for v in basis) for u in basis)
        require(all(gram[i][j] == gram[j][i] for i in range(5) for j in range(5)), "GRAM")
        for size in range(1, 6):
            require(qdet(tuple(row[:size] for row in gram[:size])) > 0, "GRAM")
            count += 1
    for a in (-1, 0, 1):
        require(kapply(equilibrium(a)) == (0,)*5+(Q(a, 4),), "EQUILIBRIUM")
    require(count == 15, "CERTIFICATE")
    return count


def audit_canonical(histories):
    count = 0
    for (_, a), (_, h, c) in histories.items():
        center = equilibrium(a)
        for n in range(1, 12):
            q = sub(h[n]+(c[n],), center)
            previous = sub(h[n-1]+(c[n-1],), center)
            following = sub(h[n+1]+(c[n+1],), center)
            p, pnext = sub(q, previous), sub(following, q)
            require(pnext == sub(p, kapply(q)) and following == add(q, pnext), "CANONICAL")
            # dF2/dq and dF2/dpnext in the equilibrium-centered coordinates.
            require(add(pnext, kapply(q)) == p and add(q, pnext) == following, "CANONICAL")
            count += 1
    require(count == 330, "CERTIFICATE")
    return count


def omega(previous1, current1, previous2, current2):
    return dot(previous1, current2)-dot(current1, previous2)


def centered_omega(first, second, n, a):
    _, h, c = first
    _, v, d = second
    center = equilibrium(a)
    return omega(sub(h[n-1]+(c[n-1],), center), sub(h[n]+(c[n],), center),
                 sub(v[n-1]+(d[n-1],), center), sub(v[n]+(d[n],), center))


def audit_symplectic(histories):
    identity6 = [tuple(int(i == j) for i in range(6)) for j in range(6)]
    jacobian_columns = [tuple(Q(t, M) for t in bapply(e))+e for e in identity6]
    jacobian_columns += [times(-1, e)+(0,)*6 for e in identity6]
    for i in range(12):
        for j in range(12):
            u, v = jacobian_columns[i], jacobian_columns[j]
            expected = int(i >= 6 and j == i-6)-int(i < 6 and j == i+6)
            require(omega(u[6:], u[:6], v[6:], v[:6]) == expected, "SYMPLECTIC")
    count = 0
    for a in (-1, 0, 1):
        for first, second in combinations((word for word, _, _ in WORDS), 2):
            one, two = histories[(first, a)], histories[(second, a)]
            initial_omega = centered_omega(one, two, 1, a)
            for n in range(1, 13):
                require(centered_omega(one, two, n, a) == initial_omega, "SYMPLECTIC")
                count += 1
    # Integer homogeneous Wronskian has degree-two scale, not integer invariance.
    one, two = histories[("0010", 0)][0], histories[("0011", 0)][0]
    for n in range(1, 12):
        x, y, xn, yn = one[n], two[n], one[n+1], two[n+1]
        old = omega(x.W+(x.V,), x.P+(x.Y,), y.W+(y.V,), y.P+(y.Y,))
        new = omega(xn.W+(xn.V,), xn.P+(xn.Y,), yn.W+(yn.V,), yn.P+(yn.Y,))
        require(new == M*M*old and Q(new, xn.D*xn.D) == Q(old, x.D*x.D), "SYMPLECTIC")
    require(count == 1620, "CERTIFICATE")
    return count


def components(hp, h, cp, c):
    field = Q(norm(sub(h, hp))+dot(hp, lap(h)), 2)
    source = Q((c-cp)**2+cp*c, 2)
    interaction = -Q(cp*dot(ELL, h)+c*dot(ELL, hp), 2*M)
    return field, source, interaction


def audit_controls(histories):
    neg, pos = histories[("0010", -1)], histories[("0010", 1)]
    require(neg[0][2].P == (4379, 2779, 794, 2594, 2414)
            and pos[0][2].P == (4399, 2759, 794, 2594, 2414)
            and neg[0][2].Y == -6480 and pos[0][2].Y == 6480, "FIXED_COUNTER")
    direct = sub(pos[1][2], neg[1][2])
    require(direct == times(Q(1, 648), ELL), "FIXED_COUNTER")
    cores, h, c = histories[("0011", 0)]
    require(cores[2].P == (2414, 2769, 2769, 2414, 2594) and cores[2].Y == -5
            and cores[2].D == 12960, "FIXED_COUNTER")
    require(cores[3].P == (973001, 594836, 594831, 973006, 1063366)
            and cores[3].Y == -1975 and cores[3].D == 4199040, "FIXED_COUNTER")
    free, _ = free_history("0011", 0)
    reciprocal = sub(h[3], free[3])
    require(c[2] == Q(-1, 2592) and h[2] == free[2]
            and reciprocal == times(Q(-1, 839808), ELL), "FIXED_COUNTER")
    no_back = history("0011", 0, end=3, feedback=0)
    require(no_back[2] == [Q(0)]*4 and no_back[1] == free[:4], "CONTROL")
    point = (no_back[1][1], no_back[2][1], no_back[1][0], no_back[1][2],
             no_back[2][0], no_back[2][2], 0)
    require(central_gradients(*point)[5] == Q(-1, 2592), "CONTROL")
    first = history("0011", 0, end=3, first_only=True)
    continued = c[3]-first[2][3]
    require(first[2][3] == Q(-1, 2592) and continued == Q(-71, 839808), "CONTROL")
    no_field = history("0011", 0, end=3, field=0)
    point = (no_field[1][2], no_field[2][2], no_field[1][1], no_field[1][3],
             no_field[2][1], no_field[2][3], 0)
    require(no_field[1] == free[:4]
            and central_gradients(*point)[:5] == times(Q(-1, 839808), ELL), "CONTROL")
    reverse_back = history("0011", 0, end=2, feedback=-1)
    point = (reverse_back[1][1], reverse_back[2][1], reverse_back[1][0], reverse_back[1][2],
             reverse_back[2][0], reverse_back[2][2], 0)
    require(central_gradients(*point)[5] == Q(-1, 1296), "CONTROL")
    no_monitor = history("0011", 0, end=2, monitor=False)
    require(no_monitor[0][2].H[5] != no_monitor[0][2].Y, "CONTROL")
    degenerate = Core((1, 0, 0, 0, 0), (0,)*5, 0, 0, D_H, 1)
    require(in_carrier(degenerate) and decode(degenerate)[0][0] == 1
            and -(1-decode(degenerate)[0][0]**2) == 0, "CONTROL")
    e1, e2 = components(h[0], h[1], c[0], c[1]), components(h[1], h[2], c[1], c[2])
    exchange = sub(e2, e1)
    total = physical_energy(cores[1], 0)
    require(e1 == (Q(53, 6912), 0, 0) and total == Q(53, 6912)
            and sum(e2) == total and exchange == (0, Q(1, 13436928), Q(-1, 13436928))
            and sum(e2[:2])-sum(e1[:2]) == Q(1, 13436928), "ENERGY")
    e3 = components(h[2], h[3], c[2], c[3])
    require(sub(e3, e2) == tuple(Q(v, 2*839808**2) for v in (-180609, 28045, 152564))
            and sum(e3) == total, "ENERGY")
    one, two = histories[("0010", 1)], histories[("0011", 1)]
    raw = []
    for n in (2, 3):
        raw.append(omega(one[1][n-1]+(one[2][n-1],), one[1][n]+(one[2][n],),
                         two[1][n-1]+(two[2][n-1],), two[1][n]+(two[2][n],)))
    drift = raw[1]-raw[0]
    require(drift == Q(1, 10368) and drift != 0
            and centered_omega(one, two, 3, 1) == centered_omega(one, two, 2, 1), "CONTROL")
    bank = energy(cores[2])-energy(cores[1])
    require(energy(cores[1]) == 745 and energy(cores[2]) == 70657990
            and bank == 70657245, "SHARP_BUDGET")
    require(cost(cores[2].H) == 185054 and norm(cores[2].P) == 33718350
            and norm(cores[2].W)+(cores[2].V)**2 == 36741600, "FIXED_COUNTER")
    require(funded((cores[1], bank, 1), 0) == (cores[2], 0, 1)
            and funded((cores[1], bank-1, 1), 0) == (cores[1], bank-1, -1), "SHARP_BUDGET")
    return direct, c[2], reciprocal, continued, total, exchange, drift, bank


def audit_cycles(histories):
    periods = []
    for a in (-1, 0, 1):
        cores = histories[("0011", a)][0]
        require(energy(cores[1]) < energy(cores[2]) < energy(cores[3]), "PERIOD")
        for horizon in (1, 2):
            bank = max(energy(x) for x in cores[1:horizon+1])-energy(cores[1])
            start = cores[1], bank, 1
            current, seen = start, set()
            for step in range(2*horizon):
                require(current not in seen, "PERIOD")
                seen.add(current)
                require(physical_energy(current[0], a) == physical_energy(start[0], a), "ENERGY")
                current = funded(current, a)
                if step+1 < 2*horizon:
                    require(current != start, "PERIOD")
            require(current == start and len(seen) == 2*horizon, "PERIOD")
            periods.append(2*horizon)
    require(periods == [2, 4, 2, 4, 2, 4], "CERTIFICATE")
    return periods


def certificate():
    authority = audit_authority()
    hf = hermitian_fixtures()
    transports, holonomies = audit_ring(hf)
    core_count, funded_cases, defects = audit_core(hf)
    records, digest, variations, bonds, precision, histories = audit_histories()
    offshell = audit_offshell(histories)
    minors = audit_stiffness()
    canonical = audit_canonical(histories)
    symplectic = audit_symplectic(histories)
    direct, chi2, reciprocal, continued, total, exchange, drift, bank = audit_controls(histories)
    periods = audit_cycles(histories)
    lines = (
        "CERTIFICATE="+PROBE, "AUTHORITY_FILES="+str(authority),
        "TRANSPORT_CHECKS="+str(transports), "HOLONOMY_CHECKS="+str(holonomies),
        "CORE_FIXTURES="+str(core_count), "FUNDED_CASES="+str(funded_cases),
        "IMAGE_DEFECTS="+str(defects), "HISTORY_RECORDS="+str(records),
        "HISTORY_SHA256="+digest, "JOINT_VARIATIONS="+str(variations),
        "OFFSHELL_VARIATIONS="+str(offshell), "K_MINOR_CHECKS="+str(minors),
        "ENERGY_BONDS="+str(bonds), "PRECISION_CHECKS="+str(precision),
        "CANONICAL_STEPS="+str(canonical), "SYMPLECTIC_CHECKS="+str(symplectic),
        "DIRECT_CONTRAST="+csv(direct), "ZERO_SOURCE_CHI2="+str(chi2),
        "RECIPROCAL_CONTRAST="+csv(reciprocal), "CONTINUED_SOURCE_CONTRAST="+str(continued),
        "ZERO_SOURCE_TOTAL_ENERGY="+str(total), "ZERO_SOURCE_ENERGY_EXCHANGE="+csv(exchange),
        "AFFINE_WRONSKIAN_DRIFT="+str(drift), "ZERO_SOURCE_FIRST_BANK="+str(bank),
        "CYCLE_PERIODS="+csv(periods), "NEGATIVE_CONTROLS=PASS", "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 27, "CERTIFICATE")
    return ("\n".join(lines)+"\n").encode("ascii")


def main():
    try:
        own = certificate()
        child = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if child.returncode != 0:
            raise RuntimeError("BREAKER_EXIT")
        if child.stderr:
            raise RuntimeError("BREAKER_STDERR")
        if child.stdout != own:
            sys.stdout.buffer.write(("FALSIFIER=BREAKER_BYTES\nBREAKER_STDOUT_HEX="
                                     +child.stdout.hex()+"\nRESULT=FAIL\n").encode("ascii"))
            return
        sys.stdout.buffer.write(own+b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except ScientificFailure as failure:
        sys.stdout.buffer.write(("FALSIFIER="+str(failure)+"\nRESULT=FAIL\n").encode("ascii"))


if __name__ == "__main__":
    main()


