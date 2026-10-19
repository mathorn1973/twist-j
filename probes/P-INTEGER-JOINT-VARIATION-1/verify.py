#!/usr/bin/env python3
"""Prospective exact gate: integer recurrence and polynomial-ring matrices.

Do not execute/import before the complete public pin is read back.
The separate breaker uses rational evolution and direct Hermitian coordinates.
Shared mathematical specification and assisted-session context are disclosed.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

PROBE = "P-INTEGER-JOINT-VARIATION-1"
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


class ScientificFailure(Exception):
    pass


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


def scale(n):
    return 2 * M ** (n * (n - 1) // 2)


def capply(p):
    return tuple(460*p[r] + 29*(p[(r-1) % 5] + p[(r+1) % 5])
                 + 65*(p[(r-2) % 5] + p[(r+2) % 5]) for r in range(5))


def lap(p):
    return tuple(Q(648*v - c, M) for v, c in zip(p, capply(p)))


@dataclass(frozen=True)
class Core:
    P: tuple
    W: tuple
    Y: int
    V: int
    H: tuple
    k: int


def in_carrier(x):
    coordinates = x.P + x.W + (x.Y, x.V) + x.H + (x.k,)
    return (len(x.P) == len(x.W) == 5 and len(x.H) == 8
            and len(coordinates) == 21 and x.k >= 1
            and all(type(t) is int for t in coordinates))


def energy(x):
    return 1 + x.k + norm(x.P) + norm(x.W) + x.Y*x.Y + x.V*x.V + cost(x.H)


def advance(x, a, field=1, feedback=1, first_only=False, monitor=True):
    r = M ** (2*x.k - 1)
    back = 0 if first_only and x.k >= 2 else feedback
    p = tuple(M**(x.k-1)*c - r*w + field*x.Y*ell
              for c, w, ell in zip(capply(x.P), x.W, ELL))
    y = M**x.k*x.Y - r*x.V + a*scale(x.k+1) - back*dot(ELL, x.P)
    h = transport(loop(y - x.Y), x.H) if monitor else x.H
    return Core(p, x.P, y, x.Y, h, x.k + 1)


def backward(x, a):
    if x.k == 1:
        return None
    n = x.k - 1
    r = M ** (2*n - 1)
    num_w = tuple(M**(n-1)*c + x.V*ell - p
                  for c, ell, p in zip(capply(x.W), ELL, x.P))
    num_v = M**n*x.V + a*scale(n+1) - dot(ELL, x.W) - x.Y
    if any(t % r for t in num_w + (num_v,)):
        return None
    h = transport(loop(x.V - x.Y), x.H)
    return Core(x.W, tuple(t // r for t in num_w), x.V, num_v // r, h, n)


def bare(x, a, direction=1):
    require(direction in (-1, 1), "BRANCH")
    return advance(x, a) if direction == 1 else backward(x, a)


def rev(s):
    x, bank, direction = s
    return (x, bank, -direction)


def funded(s, a):
    x, bank, direction = s
    y = bare(x, a, direction)
    if y is None:
        return rev(s)
    new_bank = bank + energy(x) - energy(y)
    if new_bank < 0:
        return rev(s)
    return (y, new_bank, direction)


def finverse(s, a):
    return rev(funded(rev(s), a))


def initial(word):
    bits = tuple(int(t) for t in word)
    slices = []
    for n in (0, 1):
        u = bits[n+2] - bits[n]
        slices.append(tuple(int(r in (u % 5, (u+1) % 5)) for r in range(5)))
    return tuple(slices)


def ready(word, a):
    p0, p1 = initial(word)
    return Core(p1, p0, 2*a, 0, transport(loop(2*a), D_H), 1)


def decode(x):
    d = scale(x.k)
    return tuple(Q(t, d) for t in x.P), Q(x.Y, d)


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
        data = (root / path).read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest,
                "AUTHORITY")
    return len(AUTHORITY)


def audit_ring(hf):
    require(rmul(J, J_INV) == ONE and rmul(PHI, PHI_INV) == ONE, "RING")
    require(rmul(PHI, PHI) == add(PHI, ONE), "RING")
    require(mmul(A, A_INV) == IDENTITY and rmul(J, PHI) == ROOT, "RING")
    require(sub(rmul(J, PHI_INV), ONE) == LOOP_V, "RING")
    require(rmul(LOOP_V, rconj(LOOP_V)) == real(9, -5), "RING")
    transport_count = holonomy_count = 0
    pairs = [(A, A_INV), (A_INV, A)]
    pairs += [(shear(t), shear(-t)) for t in (-2, -1, 0, 1, 2)]
    for h in hf:
        for gate, inverse in pairs:
            y = transport(gate, h)
            require(transport(inverse, y) == h and determinant(y) == determinant(h),
                    "TRANSPORT")
            for z in (h, y):
                require(cost(z) == trace_cost(z) and cost(z) >= 2*norm(z)
                        and (cost(z) == 0) == (z == (0,)*8), "COST")
            transport_count += 1
        for t in (-2, -1, 0, 1, 2):
            factor = mmul(mmul(mmul(A, shear(t)), A_INV), shear(-t))
            require(factor == loop(t), "HOLONOMY")
            y = transport(loop(t), h)
            require(y == transport(factor, h)
                    and transport(loop(-t), y) == h
                    and determinant(y) == determinant(h), "HOLONOMY")
            holonomy_count += 1
    require((transport_count, holonomy_count) == (133, 95), "CERTIFICATE")
    return transport_count, holonomy_count


def audit_core(hf):
    base = []
    for a in (-1, 0, 1):
        for i, h in enumerate(hf):
            for k in (1, 2, 3):
                base.append((a, Core((i-9, 1, -2, 0, 3), (2, -1, 0, 1, 9-i),
                                     i % 5 - 2, (i//5) % 5 - 2, h, k)))
    down = Core((0, 0, 324, 0, 0), (65, 29, 460, 29, 65), 0, 0, D_H, 1)
    require(energy(advance(down, 0)) < energy(down), "BRANCH")
    fixtures = base + [(0, down)]
    count = defects = 0
    branches = set()
    for a, x in fixtures:
        require(in_carrier(x), "INTEGER")
        y = advance(x, a)
        require(in_carrier(y) and y.k == x.k + 1 and backward(y, a) == x,
                "BARE_INVERSE")
        old = backward(x, a)
        if old is not None:
            require(advance(old, a) == x, "BARE_INVERSE")
        if x.k == 1:
            require(old is None, "IMAGE_GUARD")
        for z in (x, y):
            delta = energy(advance(z, a)) - energy(z)
            banks = (0, 1, 772, max(0, delta-1), max(0, delta), max(0, delta+1))
            for bank in banks:
                for direction in (-1, 1):
                    state = (z, bank, direction)
                    target = bare(z, a, direction)
                    if target is None:
                        branches.add("domain-")
                        expected = rev(state)
                    elif bank + energy(z) < energy(target):
                        branches.add("bank" + str(direction))
                        expected = rev(state)
                    else:
                        branches.add("move" + str(direction))
                        expected = (target, bank + energy(z) - energy(target), direction)
                    out = funded(state, a)
                    require(out == expected, "BRANCH")
                    require(in_carrier(out[0]) and type(out[1]) is int
                            and out[1] >= 0 and out[2] in (-1, 1), "INTEGER")
                    require(energy(z)+bank == energy(out[0])+out[1], "CONSERVATION")
                    require(finverse(out, a) == state
                            and funded(finverse(state, a), a) == state,
                            "FUNDED_INVERSE")
                    count += 1
    require(branches == {"domain-", "bank1", "bank-1", "move1", "move-1"},
            "BRANCH")
    for a, x in base:
        if x.k not in (1, 2):
            continue
        y = advance(x, a)
        for coordinate in range(6):
            if coordinate < 5:
                p = list(y.P)
                p[coordinate] += 1
                corrupt = replace(y, P=tuple(p))
            else:
                corrupt = replace(y, Y=y.Y+1)
            require(backward(corrupt, a) is None, "IMAGE_GUARD")
            s = (corrupt, 1000000000, -1)
            require(funded(s, a) == rev(s), "IMAGE_GUARD")
            defects += 1
    require((len(fixtures), count, defects) == (172, 4128, 684), "CERTIFICATE")
    return len(fixtures), count, defects


def history(word, a, end=12, **controls):
    p0, _ = initial(word)
    x = ready(word, a)
    cores = [None, x]
    fields = [tuple(Q(v, 2) for v in p0), decode(x)[0]]
    sources = [Q(0), Q(a)]
    for _ in range(1, end):
        x = advance(x, a, **controls)
        cores.append(x)
        h, chi = decode(x)
        fields.append(h)
        sources.append(chi)
    return cores, fields, sources


def free_history(word, a, end=12):
    p0, p1 = initial(word)
    h = [tuple(Q(v, 2) for v in p0), tuple(Q(v, 2) for v in p1)]
    chi = [Q(0), Q(a)]
    for _ in range(1, end):
        h.append(tuple(2*v - old - l for v, old, l in zip(h[-1], h[-2], lap(h[-1]))))
        chi.append(chi[-1] - chi[-2] + a)
    return h, chi


def local_action(v, xi, hp, hn, cp, cn, n, a):
    return (Q(norm(sub(v, hp)) + norm(sub(hn, v)), 2) - Q(dot(v, lap(v)), 2)
            - Q((xi-cp)**2 + (cn-xi)**2, 2) + Q(xi*xi, 2) - a*xi
            + Q(xi, M**n)*dot(ELL, v))


def central_gradients(v, xi, hp, hn, cp, cn, n, a):
    out = []
    for r in range(5):
        e = tuple(int(i == r) for i in range(5))
        out.append((local_action(add(v, e), xi, hp, hn, cp, cn, n, a)
                    - local_action(sub(v, e), xi, hp, hn, cp, cn, n, a))/2)
    out.append((local_action(v, xi+1, hp, hn, cp, cn, n, a)
                - local_action(v, xi-1, hp, hn, cp, cn, n, a))/2)
    return tuple(out)


def exact_gradients(v, xi, hp, hn, cp, cn, n, a):
    metric = tuple(2*t - p - f - l + Q(xi*ell, M**n)
                   for t, p, f, l, ell in zip(v, hp, hn, lap(v), ELL))
    return metric + (cn-xi+cp-a+Q(dot(ELL, v), M**n),)


def audit_histories():
    digest = sha256()
    count = variations = 0
    histories = {}
    for word, u0, u1 in WORDS:
        p0, p1 = initial(word)
        for p, u in ((p0, u0), (p1, u1)):
            require(p[u % 5] == p[(u+1) % 5] == 1
                    and sorted(p) == [0, 0, 0, 1, 1], "INITIAL_DATA")
        for a in (-1, 0, 1):
            cores, fields, sources = history(word, a)
            histories[(word, a)] = (cores, fields, sources)
            free, auto = free_history(word, a)
            for n in range(13):
                d = scale(n)
                p = p0 if n == 0 else cores[n].P
                y = 0 if n == 0 else cores[n].Y
                h8 = D_H if n == 0 else cores[n].H
                h, chi = fields[n], sources[n]
                require(tuple(Q(t, d) for t in p) == h and Q(y, d) == chi,
                        "INTEGER")
                require(sum(p) == d and sum(h) == 1, "MEAN")
                require(h8 == ready_h(y) and Q(h8[5], d) == chi
                        and determinant(h8) == ZERO, "SOURCE_READER")
                require(cost(h8) == 294*y**4+52*y*y+4, "COST")
                if n >= 1:
                    require(in_carrier(cores[n]) and cores[n].W == (p0 if n == 1 else cores[n-1].P)
                            and cores[n].V == (0 if n == 1 else cores[n-1].Y), "INTEGER")
                    require(5*energy(cores[n]) >= d*d, "COST")
                require(abs(chi-auto[n]) < Q(2, 323)
                        and abs(chi) < Q(648, 323) < 3, "SOURCE_BOUND")
                for value, f in zip(h, free[n]):
                    require(Q(-299, 500) < value < Q(499, 500)
                            and -(1-value*value) < Q(-999, 250000), "LORENTZ")
                    require(abs(value-f) < Q(1630, 209304) < Q(1, 125),
                            "RESPONSE_BOUND")
                line = (word+"|"+str(a)+"|"+str(n)+"|"+csv(p)+"|"+str(y)
                        +"|"+str(d)+"|"+csv(h8)+"\n")
                digest.update(line.encode("ascii"))
                count += 1
            for n in range(1, 12):
                rh = tuple(f-2*v+p+l-Q(sources[n]*ell, M**n)
                           for f, v, p, l, ell in zip(fields[n+1], fields[n],
                                                      fields[n-1], lap(fields[n]), ELL))
                rc = sources[n+1]-sources[n]+sources[n-1]-a+Q(dot(ELL, fields[n]), M**n)
                require(rh == (0,)*5 and rc == 0, "RECURRENCE")
            for n in (1, 2, 5, 11):
                point = (fields[n], sources[n], fields[n-1], fields[n+1],
                         sources[n-1], sources[n+1], n, a)
                require(central_gradients(*point) == (0,)*6, "ACTION")
                variations += 6
    require((count, variations) == (390, 720), "CERTIFICATE")
    return count, digest.hexdigest(), variations, histories


def audit_offshell(histories):
    _, h, c = histories[("0011", 0)]
    center = (h[2], c[2], h[1], h[3], c[1], c[3], 2, 0)
    cases = []
    for field, value in ((0, add(h[2], (1, 0, 0, 0, 0))),
                         (1, c[2]+1), (5, c[3]+1),
                         (3, add(h[3], (0, 0, 1, 0, 0))), (4, c[1]-1)):
        point = list(center)
        point[field] = value
        cases.append(tuple(point))
    cases.append(((Q(1, 3), Q(-2, 5), Q(0), Q(3, 7), Q(-1)), Q(-2, 3),
                  (Q(0),)*5, (Q(1),)*5, Q(1, 2), Q(-3, 4), 2, 1))
    count = 0
    for point in cases:
        expected = exact_gradients(*point)
        require(any(t != 0 for t in expected)
                and central_gradients(*point) == expected, "OFFSHELL_ACTION")
        count += 6
    require(count == 36, "CERTIFICATE")
    return count


def audit_controls(histories):
    neg = histories[("0010", -1)]
    pos = histories[("0010", 1)]
    require(neg[0][2].P == (487, 167, -230, 130, 94)
            and pos[0][2].P == (491, 163, -230, 130, 94)
            and neg[0][2].Y == -1296 and pos[0][2].Y == 1296, "FIXED_COUNTER")
    direct = sub(pos[1][2], neg[1][2])
    require(direct == times(Q(1, 162), ELL), "FIXED_COUNTER")
    cores, h, c = histories[("0011", 0)]
    require(cores[2].P == (94, 165, 165, 94, 130) and cores[2].Y == 1,
            "FIXED_COUNTER")
    require(cores[3].P == (22236121, -2269621, -2269620, 22236120, 28091448)
            and cores[3].Y == 105047 and scale(3) == 68024448, "FIXED_COUNTER")
    free, _ = free_history("0011", 0)
    reciprocal = sub(h[3], free[3])
    require(c[2] == Q(1, 648) and h[2] == free[2]
            and reciprocal == times(Q(1, 68024448), ELL), "FIXED_COUNTER")

    no_back = history("0011", 0, end=3, feedback=0)
    require(no_back[2] == [Q(0)]*4 and no_back[1] == free[:4], "CONTROL")
    point = (no_back[1][1], no_back[2][1], no_back[1][0], no_back[1][2],
             no_back[2][0], no_back[2][2], 1, 0)
    require(central_gradients(*point)[5] == Q(-1, 648), "CONTROL")
    first = history("0011", 0, end=3, first_only=True)
    continued = c[3] - first[2][3]
    require(first[2][3] == Q(1, 648) and continued == Q(71, 68024448), "CONTROL")
    no_field = history("0011", 0, end=3, field=0)
    point = (no_field[1][2], no_field[2][2], no_field[1][1], no_field[1][3],
             no_field[2][1], no_field[2][3], 2, 0)
    require(no_field[1] == free[:4]
            and central_gradients(*point)[:5] == times(Q(1, 68024448), ELL), "CONTROL")
    reverse_back = history("0011", 0, end=2, feedback=-1)
    point = (reverse_back[1][1], reverse_back[2][1], reverse_back[1][0], reverse_back[1][2],
             reverse_back[2][0], reverse_back[2][2], 1, 0)
    require(central_gradients(*point)[5] == Q(-1, 324), "CONTROL")
    no_monitor = history("0011", 0, end=2, monitor=False)
    require(no_monitor[0][2].H[5] != no_monitor[0][2].Y, "CONTROL")
    image = cores[2]
    bad_nums = tuple(c0 + image.V*ell - p for c0, ell, p in zip(capply(image.W), ELL, image.P))
    bad_nums += (M*image.V - dot(ELL, image.W) - image.Y,)
    require(any(t % (M*M) for t in bad_nums) and backward(image, 0) == cores[1], "CONTROL")
    degenerate = replace(cores[1], P=(2, 0, 0, 0, 0))
    require(decode(degenerate)[0][0] == 1 and -(1-decode(degenerate)[0][0]**2) == 0, "CONTROL")

    require(energy(cores[1]) == 10 and energy(cores[2]) == 89378, "SHARP_BUDGET")
    bank = energy(cores[2]) - energy(cores[1])
    s = (cores[1], bank, 1)
    require(bank == 89368 and funded(s, 0) == (cores[2], 0, 1)
            and funded((cores[1], bank-1, 1), 0) == (cores[1], bank-1, -1),
            "SHARP_BUDGET")
    return direct, c[2], reciprocal, continued, bank


def audit_cycles(histories):
    periods = []
    for word, a in (("0010", -1), ("0010", 1), ("0011", 0)):
        cores = histories[(word, a)][0]
        for target in (1, 2, 3):
            ceiling = max(energy(cores[n]) for n in range(1, target+1))
            require(energy(cores[target+1]) > ceiling, "SHARP_BUDGET")
            start = (cores[1], ceiling-energy(cores[1]), 1)
            state = start
            seen = {start}
            for t in range(1, 2*target+1):
                state = funded(state, a)
                require(energy(state[0])+state[1] == ceiling, "CONSERVATION")
                if t < 2*target:
                    require(state not in seen, "PERIOD")
                    seen.add(state)
                else:
                    require(state == start, "PERIOD")
            periods.append(2*target)
    require(periods == [2, 4, 6]*3, "CERTIFICATE")
    return tuple(periods)


def csv(values):
    return ",".join(str(t) for t in values)


def certificate():
    authority = audit_authority()
    hf = hermitian_fixtures()
    transports, holonomies = audit_ring(hf)
    cores, funded_cases, defects = audit_core(hf)
    records, digest, variations, histories = audit_histories()
    offshell = audit_offshell(histories)
    direct, chi2, reciprocal, continued, bank = audit_controls(histories)
    periods = audit_cycles(histories)
    lines = (
        "CERTIFICATE="+PROBE, "AUTHORITY_FILES="+str(authority),
        "TRANSPORT_CHECKS="+str(transports), "HOLONOMY_CHECKS="+str(holonomies),
        "CORE_FIXTURES="+str(cores), "FUNDED_CASES="+str(funded_cases),
        "IMAGE_DEFECTS="+str(defects), "HISTORY_RECORDS="+str(records),
        "HISTORY_SHA256="+digest, "JOINT_VARIATIONS="+str(variations),
        "OFFSHELL_VARIATIONS="+str(offshell), "DIRECT_CONTRAST="+csv(direct),
        "ZERO_SOURCE_CHI2="+str(chi2), "RECIPROCAL_CONTRAST="+csv(reciprocal),
        "CONTINUED_SOURCE_CONTRAST="+str(continued), "ZERO_SOURCE_FIRST_BANK="+str(bank),
        "CYCLE_PERIODS="+csv(periods), "NEGATIVE_CONTROLS=PASS", "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 19, "CERTIFICATE")
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
