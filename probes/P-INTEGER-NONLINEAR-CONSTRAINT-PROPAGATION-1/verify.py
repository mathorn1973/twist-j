#!/usr/bin/env python3
"""Prospective exact gate: cubic constraint-coupled action and Bianchi propagation.

Do not execute or import before the complete public pin is read back.
The separate breaker uses rational evolution, direct Hermitian coordinates, and
Gaussian elimination on the mean-zero subspace for the Hamiltonian constraint.
Shared mathematical specification and assisted-session context are disclosed.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import subprocess
import sys

PROBE = "P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1"
M = 324
ELL = (1, -1, 0, 0, 0)
SIGMA = (Q(1, 2), Q(1, 2), Q(0), Q(0), Q(0))
TWO_SIGMA = (1, 1, 0, 0, 0)
EDGES = tuple((r, (r + k) % 5, 29 if k == 1 else 65)
              for k in (1, 2) for r in range(5))
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
    "GREEN", "CONTINUITY", "HAMILTONIAN_CONSTRAINT", "MOMENTUM_CONSTRAINT",
    "BIANCHI", "INTEGER_CONSTRAINT", "ACTION", "OFFSHELL_ACTION",
    "CANONICAL", "SYMPLECTIC", "FIXED_COUNTER", "CONTROL",
    "SHARP_BUDGET", "PERIOD", "CERTIFICATE", "BREAKER_BYTES",
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


def csv(values):
    return ",".join(str(t) for t in values)


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


def b5(f):
    return tuple(f[head] - f[tail] for tail, head, _ in EDGES)


def b5t(j):
    out = [0] * 5
    for (tail, head, _), val in zip(EDGES, j):
        out[tail] -= val
        out[head] += val
    return tuple(out)


def we_apply(j):
    return tuple(Q(mw, M) * val for (_, _, mw), val in zip(EDGES, j))


def mwe_apply(j):
    return tuple(mw * val for (_, _, mw), val in zip(EDGES, j))


def capply(p):
    return tuple(460*p[r] + 29*(p[(r-1) % 5]+p[(r+1) % 5])
                 + 65*(p[(r-2) % 5]+p[(r+2) % 5]) for r in range(5))


def lint_apply(p):
    return tuple(188*p[r] - 29*(p[(r-1) % 5]+p[(r+1) % 5])
                 - 65*(p[(r-2) % 5]+p[(r+2) % 5]) for r in range(5))


def ladj_apply(p):
    return tuple(188*p[r] - 65*(p[(r-1) % 5]+p[(r+1) % 5])
                 - 29*(p[(r-2) % 5]+p[(r+2) % 5]) for r in range(5))


def lap(p):
    return tuple(Q(v, M) for v in lint_apply(p))


def pi0(v):
    mean = Q(sum(v), 5)
    return tuple(Q(t) - mean for t in v)


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


@lru_cache(maxsize=None)
def e_star(a):
    amplitude = Q(a, 4)
    return Q(4342005, 8683757) * amplitude * amplitude


def bond_energy(previous, current, a):
    center = equilibrium(a)
    x, y = sub(previous, center), sub(current, center)
    return Q(norm(sub(y, x))+dot(x, kapply(y)), 2)


def local_energy_pair(hp, cp, h, c, a):
    dh = sub(h, hp)
    bhp, bh = b5(hp), b5(h)
    edge_share = [Q(0)] * 5
    for idx, (tail, head, mw) in enumerate(EDGES):
        val = Q(mw, 4 * M) * bh[idx] * bhp[idx]
        edge_share[tail] += val
        edge_share[head] += val
    eh = tuple(Q(dh[r]*dh[r], 2) + edge_share[r] for r in range(5))
    echi_scalar = Q((c - cp)**2, 2) + Q(cp * c, 2) - Q(a, 8) * (cp + c)
    echi = tuple(SIGMA[r] * echi_scalar for r in range(5))
    eint = tuple(-Q(ELL[r], 2 * M) * (cp * h[r] + c * hp[r]) for r in range(5))
    eloc = tuple(eh[r] + echi[r] + eint[r] for r in range(5))
    offset = e_star(a) / 5
    etot = tuple(eloc[r] + offset for r in range(5))
    return eloc, etot


def total_current(hp, cp, h, c, hn, cn, include_int=True):
    qh = sub(hn, hp)
    qc = cn - cp
    bh = b5(h)
    jh = tuple(Q(mw, 4 * M) * bh[idx] * (qh[tail] + qh[head])
               for idx, (tail, head, mw) in enumerate(EDGES))
    jint_0 = -Q(1, 4 * M) * qc * (h[0] + h[1]) if include_int else Q(0)
    jint = (jint_0,) + (Q(0),) * 9
    return add(jh, jint), jh, jint


def tau_from_eloc(eloc):
    return tuple(Q(162, 53605) * v for v in ladj_apply(eloc))


def p_from_constraints(tau_cur, tau_next, jtot):
    return sub(times(Q(-1, 2), jtot), we_apply(b5(sub(tau_next, tau_cur))))


def residuals_three_slice(hp, cp, h, c, hn, cn, a):
    rh = tuple(hn[r] - 2*h[r] + hp[r] + l - Q(c * ell, M)
               for r, (l, ell) in enumerate(zip(lap(h), ELL)))
    rc = cn - c + cp - Q(a, 4) - Q(dot(ELL, h), M)
    return rh, rc


def offshell_continuity_rhs(hp, cp, h, c, hn, cn, a):
    qh = sub(hn, hp)
    qc = cn - cp
    rh, rc = residuals_three_slice(hp, cp, h, c, hn, cn, a)
    return tuple(Q(1, 2) * qh[r] * rh[r] + Q(1, 2) * SIGMA[r] * qc * rc
                 for r in range(5))


def offshell_bianchi_rhs(hp, cp, h, c, hn, cn, a):
    rhs = offshell_continuity_rhs(hp, cp, h, c, hn, cn, a)
    return times(Q(-1, 2), pi0(rhs))


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


def e_int_core(x, a):
    bp, bw = b5(x.P), b5(x.W)
    edge_share = [0] * 5
    for idx, (tail, head, mw) in enumerate(EDGES):
        val = mw * bp[idx] * bw[idx]
        edge_share[tail] += val
        edge_share[head] += val
    src = M * (x.Y - x.V)**2 + M * x.Y * x.V - 81 * a * x.D * (x.Y + x.V)
    return tuple(2 * M * (x.P[r] - x.W[r])**2
                 + edge_share[r]
                 + TWO_SIGMA[r] * src
                 - 2 * ELL[r] * (x.V * x.P[r] + x.Y * x.W[r])
                 for r in range(5))


def theta_core(x, a):
    return ladj_apply(e_int_core(x, a))


def j_int_core(x, y):
    qdh = sub(y.P, times(M, x.W))
    qdc = y.Y - M * x.V
    bp = b5(x.P)
    return tuple(mw * bp[idx] * (qdh[tail] + qdh[head])
                 - (qdc * (x.P[0] + x.P[1]) if idx == 0 else 0)
                 for idx, (tail, head, mw) in enumerate(EDGES))


def pi_int_core(x, y, a):
    th_x = theta_core(x, a)
    th_y = theta_core(y, a)
    j_x = j_int_core(x, y)
    d_th = sub(th_y, times(M * M, th_x))
    return sub(times(-53605 * M, j_x), mwe_apply(b5(d_th)))


def check_integer_constraints_on_pair(x, y, a):
    e_x = e_int_core(x, a)
    e_y = e_int_core(y, a)
    th_x = theta_core(x, a)
    th_y = theta_core(y, a)
    j_x = j_int_core(x, y)
    pi_x = pi_int_core(x, y, a)
    require(len(e_x) == len(th_x) == 5 and len(j_x) == len(pi_x) == 10, "INTEGER_CONSTRAINT")
    require(all(type(t) is int for t in e_x + e_y + th_x + th_y + j_x + pi_x),
            "INTEGER_CONSTRAINT")
    require(sum(th_x) == 0 and sum(th_y) == 0, "HAMILTONIAN_CONSTRAINT")
    rhs_x = tuple(10721 * (5 * val - sum(e_x)) for val in e_x)
    rhs_y = tuple(10721 * (5 * val - sum(e_y)) for val in e_y)
    require(lint_apply(th_x) == rhs_x and lint_apply(th_y) == rhs_y, "HAMILTONIAN_CONSTRAINT")
    cont = add(sub(e_y, times(M * M, e_x)), times(M, b5t(j_x)))
    require(cont == (0,) * 5, "CONTINUITY")
    require(b5t(pi_x) == (0,) * 5, "BIANCHI")
    return e_x, th_x, j_x, pi_x


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
        check_integer_constraints_on_pair(x, y, a)
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
                    if out[0] == z:
                        require(theta_core(out[0], a) == theta_core(z, a), "HAMILTONIAN_CONSTRAINT")
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


def exact_gradients(v, xi, hp, hn, cp, cn, a):
    metric = tuple(2*t-p-f-l+Q(xi*ell, M)
                   for t, p, f, l, ell in zip(v, hp, hn, lap(v), ELL))
    return metric+(xi-cn-cp+Q(a, 4)+Q(dot(ELL, v), M),)


def unpack_cubic_point(point):
    require(len(point) == 48, "ACTION")
    v = point[0:5]
    xi = point[5]
    tau_n = point[6:11]
    tau_n1 = point[11:16]
    p_n = point[16:26]
    lhom_n = point[26]
    lhom_n1 = point[27]
    llapse_n = point[28:33]
    llapse_n1 = point[33:38]
    nshift_n = point[38:48]
    return v, xi, tau_n, tau_n1, p_n, lhom_n, lhom_n1, llapse_n, llapse_n1, nshift_n


def cubic_local_action(point, hp, cp, hn, cn, a, e_hom):
    v, xi, tau_n, tau_n1, p_n, lhom_n, lhom_n1, llapse_n, llapse_n1, nshift_n = unpack_cubic_point(point)
    eloc_n, etot_n = local_energy_pair(hp, cp, v, xi, a)
    eloc_n1, etot_n1 = local_energy_pair(v, xi, hn, cn, a)
    htot_n, htot_n1 = sum(etot_n), sum(etot_n1)
    jtot_n, _, _ = total_current(hp, cp, v, xi, hn, cn)
    pmom_n = add(we_apply(b5(sub(tau_n1, tau_n))), p_n)
    aloc = local_action(v, xi, hp, hn, cp, cn, a)
    term_hom = -lhom_n * (htot_n - e_hom) - lhom_n1 * (htot_n1 - e_hom)
    term_lapse_n = 2 * dot(llapse_n, lap(tau_n)) - dot(llapse_n, pi0(eloc_n))
    term_lapse_n1 = 2 * dot(llapse_n1, lap(tau_n1)) - dot(llapse_n1, pi0(eloc_n1))
    term_shift = 2 * dot(nshift_n, pmom_n) + dot(nshift_n, jtot_n)
    return aloc + term_hom + term_lapse_n + term_lapse_n1 + term_shift


def central_cubic_gradients(point, hp, cp, hn, cn, a, e_hom):
    out = []
    pts = list(point)
    for idx in range(48):
        orig = pts[idx]
        pts[idx] = orig + 1
        plus = cubic_local_action(tuple(pts), hp, cp, hn, cn, a, e_hom)
        pts[idx] = orig - 1
        minus = cubic_local_action(tuple(pts), hp, cp, hn, cn, a, e_hom)
        pts[idx] = orig
        out.append((plus - minus) / 2)
    return tuple(out)


def exact_cubic_gradients(point, hp, cp, hn, cn, a, e_hom):
    v, xi, tau_n, tau_n1, p_n, lhom_n, lhom_n1, llapse_n, llapse_n1, nshift_n = unpack_cubic_point(point)
    eloc_n, etot_n = local_energy_pair(hp, cp, v, xi, a)
    eloc_n1, etot_n1 = local_energy_pair(v, xi, hn, cn, a)
    htot_n, htot_n1 = sum(etot_n), sum(etot_n1)
    jtot_n, _, _ = total_current(hp, cp, v, xi, hn, cn)
    pmom_n = add(we_apply(b5(sub(tau_n1, tau_n))), p_n)
    base = exact_gradients(v, xi, hp, hn, cp, cn, a)
    grad_v = list(base[:5])
    grad_xi = base[5]
    mu_n = tuple(lhom_n + t for t in pi0(llapse_n))
    mu_n1 = tuple(lhom_n1 + t for t in pi0(llapse_n1))
    for mu_b, h_nb, c_nb in ((mu_n, hp, cp), (mu_n1, hn, cn)):
        bh_nb = b5(h_nb)
        u_edge = tuple(Q(mw, 4 * M) * (mu_b[tail] + mu_b[head]) * bh_nb[idx]
                       for idx, (tail, head, mw) in enumerate(EDGES))
        bt_u = b5t(u_edge)
        for r in range(5):
            grad_v[r] -= (mu_b[r] * (v[r] - h_nb[r])
                          + bt_u[r]
                          - Q(ELL[r], 2 * M) * mu_b[r] * c_nb)
        mu_sig = (mu_b[0] + mu_b[1]) / 2
        grad_xi -= (mu_sig * (xi - Q(c_nb, 2) - Q(a, 8))
                    - Q(1, 2 * M) * sum(mu_b[s] * ELL[s] * h_nb[s] for s in range(5)))
    qh = sub(hn, hp)
    qc = cn - cp
    v_shift = tuple(Q(mw, 4 * M) * nshift_n[idx] * (qh[tail] + qh[head])
                    for idx, (tail, head, mw) in enumerate(EDGES))
    bt_v = b5t(v_shift)
    for r in range(5):
        grad_v[r] += bt_v[r] - Q(1, 2 * M) * qc * nshift_n[0] * SIGMA[r]
    bt_we_nshift = b5t(we_apply(nshift_n))
    grad_tau_n = sub(times(2, lap(llapse_n)), times(2, bt_we_nshift))
    grad_tau_n1 = add(times(2, lap(llapse_n1)), times(2, bt_we_nshift))
    grad_p_n = times(2, nshift_n)
    grad_lhom_n = -(htot_n - e_hom)
    grad_lhom_n1 = -(htot_n1 - e_hom)
    grad_llapse_n = sub(times(2, lap(tau_n)), pi0(eloc_n))
    grad_llapse_n1 = sub(times(2, lap(tau_n1)), pi0(eloc_n1))
    grad_nshift_n = add(times(2, pmom_n), jtot_n)
    return (tuple(grad_v) + (grad_xi,) + grad_tau_n + grad_tau_n1 + grad_p_n
            + (grad_lhom_n, grad_lhom_n1) + grad_llapse_n + grad_llapse_n1 + grad_nshift_n)


def valuation_three(value):
    require(value > 0 and type(value) is int, "PRECISION")
    count = 0
    while value % 3 == 0:
        value //= 3
        count += 1
    return count


def audit_histories():
    digest = sha256()
    cdigest = sha256()
    count = variations = precision = cbonds = bslices = 0
    histories = {}
    constraints = {}
    for word, u0, u1 in WORDS:
        p0, p1 = initial(word)
        for p, u in ((p0, u0), (p1, u1)):
            require(p[u % 5] == p[(u+1) % 5] == 1
                    and sorted(p) == [0, 0, 0, 1, 1], "INITIAL_DATA")
        for a in (-1, 0, 1):
            cores, fields, sources = history(word, a)
            histories[(word, a)] = cores, fields, sources
            h_initial = physical_energy(cores[1], a)
            elocs, etots, taus, eint_list, theta_list = [None], [None], [None], [None], [None]
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
                    e_int = e_int_core(x, a)
                    th_int = theta_core(x, a)
                    eloc, etot = local_energy_pair(fields[n-1], sources[n-1], h, chi, a)
                    tau = tau_from_eloc(eloc)
                    require(all(type(t) is int for t in e_int + th_int), "INTEGER_CONSTRAINT")
                    require(sum(th_int) == 0 and sum(tau) == 0, "HAMILTONIAN_CONSTRAINT")
                    require(lint_apply(th_int) == tuple(10721 * (5 * val - sum(e_int)) for val in e_int),
                            "HAMILTONIAN_CONSTRAINT")
                    require(tuple(Q(t, 4 * M * d * d) for t in e_int) == eloc, "INTEGER_CONSTRAINT")
                    require(tuple(Q(t, 8 * 53605 * d * d) for t in th_int) == tau, "INTEGER_CONSTRAINT")
                    require(sum(etot) == h_initial, "ENERGY")
                    require(times(2, lap(tau)) == pi0(etot) == pi0(eloc), "HAMILTONIAN_CONSTRAINT")
                    elocs.append(eloc)
                    etots.append(etot)
                    taus.append(tau)
                    eint_list.append(e_int)
                    theta_list.append(th_int)
                    cbonds += 1
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
            p_list = [None]
            j_list = [None]
            for n in range(1, 12):
                rh, rc = residuals_three_slice(fields[n-1], sources[n-1],
                                               fields[n], sources[n],
                                               fields[n+1], sources[n+1], a)
                require(rh == (0,)*5 and rc == 0, "RECURRENCE")
                e_x, th_x, j_int, pi_int = check_integer_constraints_on_pair(cores[n], cores[n+1], a)
                require(e_x == eint_list[n] and th_x == theta_list[n], "INTEGER_CONSTRAINT")
                d = cores[n].D
                jtot, _, _ = total_current(fields[n-1], sources[n-1],
                                           fields[n], sources[n],
                                           fields[n+1], sources[n+1])
                p_n = p_from_constraints(taus[n], taus[n+1], jtot)
                require(tuple(Q(t, 4 * M * M * d * d) for t in j_int) == jtot, "INTEGER_CONSTRAINT")
                require(tuple(Q(t, 8 * 53605 * M * M * M * d * d) for t in pi_int) == p_n,
                        "INTEGER_CONSTRAINT")
                require(add(sub(etots[n+1], etots[n]), b5t(jtot)) == (0,) * 5, "CONTINUITY")
                pmom = add(we_apply(b5(sub(taus[n+1], taus[n]))), p_n)
                require(add(times(2, pmom), jtot) == (0,) * 10, "MOMENTUM_CONSTRAINT")
                require(b5t(p_n) == (0,) * 5, "BIANCHI")
                p_list.append(p_n)
                j_list.append(jtot)
                cline = (word+"|"+str(a)+"|"+str(n)+"|"+csv(e_x)+"|"+csv(th_x)
                         +"|"+csv(j_int)+"|"+csv(pi_int)+"\n")
                cdigest.update(cline.encode("ascii"))
                bslices += 1
            constraints[(word, a)] = elocs, etots, taus, p_list, j_list, eint_list, theta_list
            for n in (1, 2, 5, 11):
                point = (fields[n] + (sources[n],) + taus[n] + taus[n+1] + p_list[n]
                         + (Q(0), Q(0)) + (Q(0),) * 5 + (Q(0),) * 5 + (Q(0),) * 10)
                grads = central_cubic_gradients(point, fields[n-1], sources[n-1],
                                                fields[n+1], sources[n+1], a, h_initial)
                exact = exact_cubic_gradients(point, fields[n-1], sources[n-1],
                                              fields[n+1], sources[n+1], a, h_initial)
                require(grads == (0,) * 48 and exact == (0,) * 48, "ACTION")
                variations += 48
    require((count, cbonds, bslices, variations, precision) == (390, 360, 330, 5760, 360),
            "CERTIFICATE")
    return (count, digest.hexdigest(), cbonds, bslices, cdigest.hexdigest(),
            variations, precision, histories, constraints)


def audit_offshell(histories, constraints):
    _, h, c = histories[("0011", 0)]
    _, _, taus, p_list, _, _, _ = constraints[("0011", 0)]
    e_hom0 = physical_energy(histories[("0011", 0)][0][1], 0)
    base_point = (h[2] + (c[2],) + taus[2] + taus[3] + p_list[2]
                  + (Q(0), Q(0)) + (Q(0),) * 5 + (Q(0),) * 5 + (Q(0),) * 10)
    cases = []
    # Case 1: v = h2 + (1,0,0,0,0), ell_lapse,2 = (1,-1,0,0,0)
    pt1 = list(base_point)
    pt1[0:5] = add(h[2], (1, 0, 0, 0, 0))
    pt1[28:33] = (Q(1), Q(-1), Q(0), Q(0), Q(0))
    cases.append((tuple(pt1), h[1], c[1], h[3], c[3], 0, e_hom0))
    # Case 2: xi = c2 + 1, ell_hom,2 = 1
    pt2 = list(base_point)
    pt2[5] = c[2] + 1
    pt2[26] = Q(1)
    cases.append((tuple(pt2), h[1], c[1], h[3], c[3], 0, e_hom0))
    # Case 3: chi_next = c3 + 1, N_shift,2 = e_0
    pt3 = list(base_point)
    pt3[38] = Q(1)
    cases.append((tuple(pt3), h[1], c[1], h[3], c[3] + 1, 0, e_hom0))
    # Case 4: h_next = h3 + (0,0,1,0,0), tau_2 += (1,-1,0,0,0), ell_lapse,3 = (0,1,-1,0,0)
    pt4 = list(base_point)
    pt4[6:11] = add(taus[2], (1, -1, 0, 0, 0))
    pt4[33:38] = (Q(0), Q(1), Q(-1), Q(0), Q(0))
    cases.append((tuple(pt4), h[1], c[1], add(h[3], (0, 0, 1, 0, 0)), c[3], 0, e_hom0))
    # Case 5: chi_prev = c1 - 1, p_2 += (1,1,1,1,1,0,0,0,0,0), N_shift,2 = (0,1,0,...,0)
    pt5 = list(base_point)
    pt5[16:26] = add(p_list[2], (1, 1, 1, 1, 1, 0, 0, 0, 0, 0))
    pt5[39] = Q(1)
    cases.append((tuple(pt5), h[1], c[1] - 1, h[3], c[3], 0, e_hom0))
    # Case 6: General rational configuration at a=1, E_hom=1/7
    pt6 = (
        (Q(1, 3), Q(-2, 5), Q(0), Q(3, 7), Q(-1))
        + (Q(-2, 3),)
        + (Q(1, 2), Q(-1, 2), Q(1, 3), Q(-1, 3), Q(0))
        + (Q(0), Q(1, 5), Q(-1, 5), Q(1, 4), Q(-1, 4))
        + (Q(1, 2), Q(-1, 3), Q(0), Q(1, 5), Q(-1, 2), Q(1, 4), Q(0), Q(-1, 4), Q(1, 6), Q(-1, 6))
        + (Q(1, 3), Q(-1, 2))
        + (Q(1), Q(-1, 2), Q(0), Q(-1, 2), Q(0))
        + (Q(0), Q(1), Q(-1), Q(1, 3), Q(-1, 3))
        + (Q(1), Q(0), Q(-1, 2), Q(0), Q(1, 3), Q(-1, 4), Q(1, 2), Q(0), Q(0), Q(-1))
    )
    cases.append((pt6, (Q(0),) * 5, Q(1, 2), (Q(1),) * 5, Q(-3, 4), 1, Q(1, 7)))
    total_checks = 0
    for point, hp, cp, hn, cn, a, e_hom in cases:
        expected = exact_cubic_gradients(point, hp, cp, hn, cn, a, e_hom)
        numeric = central_cubic_gradients(point, hp, cp, hn, cn, a, e_hom)
        require(numeric == expected, "OFFSHELL_ACTION")
        require(any(t != 0 for t in expected[:6]) and any(t != 0 for t in expected[6:]),
                "OFFSHELL_ACTION")
        v, xi = point[0:5], point[5]
        eloc_n, etot_n = local_energy_pair(hp, cp, v, xi, a)
        eloc_n1, etot_n1 = local_energy_pair(v, xi, hn, cn, a)
        jtot, _, _ = total_current(hp, cp, v, xi, hn, cn)
        cont_lhs = add(sub(etot_n1, etot_n), b5t(jtot))
        cont_rhs = offshell_continuity_rhs(hp, cp, v, xi, hn, cn, a)
        require(cont_lhs == cont_rhs, "CONTINUITY")
        tau_ham_n = tau_from_eloc(eloc_n)
        tau_ham_n1 = tau_from_eloc(eloc_n1)
        p_mom = p_from_constraints(tau_ham_n, tau_ham_n1, jtot)
        require(b5t(p_mom) == offshell_bianchi_rhs(hp, cp, v, xi, hn, cn, a), "BIANCHI")
        total_checks += 48
    require(total_checks == 288, "CERTIFICATE")
    return total_checks


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


def audit_green_and_stiffness():
    # Check L = B_5^T W_e B_5 and L_int L_adj = L_adj L_int = 53605 Pi_0 on Q^5.
    for i in range(5):
        ei = tuple(int(j == i) for j in range(5))
        require(b5t(we_apply(b5(ei))) == lap(ei), "GREEN")
        pi0_scaled = tuple(10721 * (5 * int(j == i) - 1) for j in range(5))
        require(lint_apply(ladj_apply(ei)) == pi0_scaled
                and ladj_apply(lint_apply(ei)) == pi0_scaled, "GREEN")
    require(lint_apply((1,)*5) == (0,)*5 and ladj_apply((1,)*5) == (0,)*5, "GREEN")
    require(ladj_apply(ELL) == (253, -253, 36, 0, -36), "GREEN")
    # 4x4 Gram matrix of L on e^perp in basis e_i - e_4 (i=0..3).
    basis4 = [tuple(int(j == i) - int(j == 4) for j in range(5)) for i in range(4)]
    gram_l = tuple(tuple(dot(u, lap(v)) for v in basis4) for u in basis4)
    require(all(gram_l[i][j] == gram_l[j][i] for i in range(4) for j in range(4)), "GREEN")
    count = 0
    for size in range(1, 5):
        require(qdet(tuple(row[:size] for row in gram_l[:size])) > 0, "GREEN")
        count += 1
    # Also check rank(B_5^T) = 4 (dim K_E = 6) via B_5 B_5^T on e^perp.
    gram_b = tuple(tuple(dot(b5(u), b5(v)) for v in basis4) for u in basis4)
    require(qdet(gram_b) > 0 and b5((1,)*5) == (0,)*10, "GREEN")
    # 15 coupled stiffness minors on e^perp x R.
    basis = [tuple(int(j == i)-int(j == 4) for j in range(6)) for i in range(4)]
    basis.append((0, 0, 0, 0, 0, 1))
    operators = (
        lambda v: sub(kapply(v), times(Q(59, 100), v)),
        lambda v: sub(times(Q(201, 200), v), kapply(v)),
        lambda v: sub(sub(kapply(v), times(Q(1, 4), kapply(kapply(v)))), times(Q(1, 2), v)),
    )
    for operator in operators:
        gram = tuple(tuple(dot(u, operator(v)) for v in basis) for u in basis)
        require(all(gram[i][j] == gram[j][i] for i in range(5) for j in range(5)), "GRAM")
        for size in range(1, 6):
            require(qdet(tuple(row[:size] for row in gram[:size])) > 0, "GRAM")
            count += 1
    for a in (-1, 0, 1):
        require(kapply(equilibrium(a)) == (0,)*5+(Q(a, 4),), "EQUILIBRIUM")
    require(count == 19, "CERTIFICATE")
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


def audit_controls(histories, constraints):
    neg, pos = histories[("0010", -1)], histories[("0010", 1)]
    require(neg[0][2].P == (4379, 2779, 794, 2594, 2414)
            and pos[0][2].P == (4399, 2759, 794, 2594, 2414)
            and neg[0][2].Y == -6480 and pos[0][2].Y == 6480, "FIXED_COUNTER")
    direct = sub(pos[1][2], neg[1][2])
    require(direct == times(Q(1, 648), ELL), "FIXED_COUNTER")
    cores, h, c = histories[("0011", 0)]
    elocs, etots, taus, p_list, j_list, eint_list, theta_list = constraints[("0011", 0)]
    require(cores[2].P == (2414, 2769, 2769, 2414, 2594) and cores[2].Y == -5
            and cores[2].D == 12960, "FIXED_COUNTER")
    require(cores[3].P == (973001, 594836, 594831, 973006, 1063366)
            and cores[3].Y == -1975 and cores[3].D == 4199040, "FIXED_COUNTER")
    # Witness 1 & 2: Initial vertex energy density and tau_1 at word 0011, a=0, n=1
    expected_eint1 = (2350, 3975, 3975, 2350, 3250)
    expected_etot1 = (Q(47, 41472), Q(53, 27648), Q(53, 27648), Q(47, 41472), Q(65, 41472))
    expected_theta1 = (-211250, 173775, 173775, -211250, 74950)
    expected_tau1 = (Q(-845, 2744576), Q(6951, 27445760), Q(6951, 27445760),
                     Q(-845, 2744576), Q(1499, 13722880))
    require(eint_list[1] == expected_eint1 and etots[1] == expected_etot1
            and sum(etots[1]) == Q(53, 6912), "FIXED_COUNTER")
    require(theta_list[1] == expected_theta1 and taus[1] == expected_tau1, "FIXED_COUNTER")
    # Witness 3: Nonzero dipole interaction current at n=1
    jtot1, jh1, jint1 = total_current(h[0], c[0], h[1], c[1], h[2], c[2], include_int=True)
    require(jtot1 == j_list[1] and jint1[0] == Q(17, 134369280)
            and jint1[1:] == (Q(0),) * 9, "FIXED_COUNTER")
    j_int1 = j_int_core(cores[1], cores[2])
    require(j_int1 == (-47040, 0, 47125, 0, 0, -105625, 105625, 47125, 0, -47125),
            "FIXED_COUNTER")
    # Witness 4 (Control 5): Omit dipole interaction current from j_tot,1
    p1_no_int = p_from_constraints(taus[1], taus[2], jh1)
    defect_no_int = b5t(p1_no_int)
    expected_defect_no_int = (Q(-17, 268738560), Q(17, 268738560), Q(0), Q(0), Q(0))
    require(defect_no_int == expected_defect_no_int and any(defect_no_int), "CONTROL")
    # Control 6: Omit source and interaction energy densities from tau
    eloc2_free, _ = local_energy_pair(h[1], Q(0), h[2], Q(0), 0)
    tau2_free = tau_from_eloc(eloc2_free)
    p1_no_src_tau = p_from_constraints(taus[1], tau2_free, jtot1)
    require(b5t(p1_no_src_tau) == times(-1, expected_defect_no_int), "CONTROL")
    # Witness 6 (Control 7): Off-gauge cubic shift-to-field backreaction at n=1
    pt_shift = (h[1] + (c[1],) + taus[1] + taus[2] + p_list[1]
                + (Q(0), Q(0)) + (Q(0),) * 5 + (Q(0),) * 5
                + (Q(1),) + (Q(0),) * 9)
    shift_grad = central_cubic_gradients(pt_shift, h[0], c[0], h[2], c[2], 0, Q(53, 6912))[:5]
    expected_shift_grad = (Q(943, 1679616), Q(-157, 279936), Q(0), Q(0), Q(0))
    require(shift_grad == expected_shift_grad
            and exact_cubic_gradients(pt_shift, h[0], c[0], h[2], c[2], 0, Q(53, 6912))[:5]
            == expected_shift_grad, "CONTROL")
    # Controls 1, 2, 3, 4 (disabled/modified dynamical laws and their Bianchi defects)
    free, _ = free_history("0011", 0)
    reciprocal = sub(h[3], free[3])
    require(c[2] == Q(-1, 2592) and h[2] == free[2]
            and reciprocal == times(Q(-1, 839808), ELL), "FIXED_COUNTER")
    no_back = history("0011", 0, end=3, feedback=0)
    require(no_back[2] == [Q(0)]*4 and no_back[1] == free[:4], "CONTROL")
    require(exact_gradients(no_back[1][1], no_back[2][1], no_back[1][0], no_back[1][2],
                            no_back[2][0], no_back[2][2], 0)[5] == Q(-1, 2592), "CONTROL")
    first = history("0011", 0, end=3, first_only=True)
    continued = c[3]-first[2][3]
    require(first[2][3] == Q(-1, 2592) and continued == Q(-71, 839808), "CONTROL")
    require(any(offshell_bianchi_rhs(first[1][1], first[2][1], first[1][2], first[2][2],
                                     first[1][3], first[2][3], 0)), "CONTROL")
    no_field = history("0011", 0, end=3, field=0)
    require(no_field[1] == free[:4]
            and exact_gradients(no_field[1][2], no_field[2][2], no_field[1][1], no_field[1][3],
                                no_field[2][1], no_field[2][3], 0)[:5]
            == times(Q(-1, 839808), ELL), "CONTROL")
    require(any(offshell_bianchi_rhs(no_field[1][1], no_field[2][1], no_field[1][2], no_field[2][2],
                                     no_field[1][3], no_field[2][3], 0)), "CONTROL")
    # Witness 5 (Control 4): Reversed feedback sign at n=1
    reverse_back = history("0011", 0, end=2, feedback=-1)
    require(exact_gradients(reverse_back[1][1], reverse_back[2][1], reverse_back[1][0],
                            reverse_back[1][2], reverse_back[2][0], reverse_back[2][2], 0)[5]
            == Q(-1, 1296), "CONTROL")
    eloc_rev1, _ = local_energy_pair(reverse_back[1][0], reverse_back[2][0],
                                     reverse_back[1][1], reverse_back[2][1], 0)
    eloc_rev2, _ = local_energy_pair(reverse_back[1][1], reverse_back[2][1],
                                     reverse_back[1][2], reverse_back[2][2], 0)
    jtot_rev1, _, _ = total_current(reverse_back[1][0], reverse_back[2][0],
                                    reverse_back[1][1], reverse_back[2][1],
                                    reverse_back[1][2], reverse_back[2][2])
    p_rev1 = p_from_constraints(tau_from_eloc(eloc_rev1), tau_from_eloc(eloc_rev2), jtot_rev1)
    defect_rev = b5t(p_rev1)
    expected_defect_rev = (Q(-1, 44789760), Q(-1, 44789760), Q(1, 67184640),
                           Q(1, 67184640), Q(1, 67184640))
    require(defect_rev == expected_defect_rev
            and defect_rev == offshell_bianchi_rhs(
                reverse_back[1][0], reverse_back[2][0],
                reverse_back[1][1], reverse_back[2][1],
                reverse_back[1][2], reverse_back[2][2], 0), "CONTROL")
    # Controls 8, 9, 10
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
    return (direct, expected_etot1, expected_tau1, jint1[0],
            expected_defect_no_int, expected_defect_rev, expected_shift_grad,
            drift, bank)


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
    (records, digest, cbonds, bslices, cdigest,
     variations, precision, histories, constraints) = audit_histories()
    offshell = audit_offshell(histories, constraints)
    minors = audit_green_and_stiffness()
    canonical = audit_canonical(histories)
    symplectic = audit_symplectic(histories)
    (direct, etot1, tau1, jint1_0, defect_no_int,
     defect_rev, shift_grad, drift, bank) = audit_controls(histories, constraints)
    periods = audit_cycles(histories)
    lines = (
        "CERTIFICATE="+PROBE,
        "AUTHORITY_FILES="+str(authority),
        "TRANSPORT_CHECKS="+str(transports),
        "HOLONOMY_CHECKS="+str(holonomies),
        "CORE_FIXTURES="+str(core_count),
        "FUNDED_CASES="+str(funded_cases),
        "IMAGE_DEFECTS="+str(defects),
        "HISTORY_RECORDS="+str(records),
        "HISTORY_SHA256="+digest,
        "CONSTRAINT_BONDS="+str(cbonds),
        "BIANCHI_SLICES="+str(bslices),
        "CONSTRAINT_SHA256="+cdigest,
        "CUBIC_VARIATIONS="+str(variations),
        "OFFSHELL_CUBIC_VARIATIONS="+str(offshell),
        "GREEN_MINOR_CHECKS="+str(minors),
        "PRECISION_CHECKS="+str(precision),
        "CANONICAL_STEPS="+str(canonical),
        "SYMPLECTIC_CHECKS="+str(symplectic),
        "DIRECT_CONTRAST="+csv(direct),
        "ZERO_SOURCE_ENERGY_DENSITY="+csv(etot1),
        "ZERO_SOURCE_TAU1="+csv(tau1),
        "ZERO_SOURCE_INTERACTION_CURRENT="+str(jint1_0),
        "NO_INTERACTION_CURRENT_BIANCHI_DEFECT="+csv(defect_no_int),
        "REVERSED_FEEDBACK_BIANCHI_DEFECT="+csv(defect_rev),
        "SHIFT_CUBIC_BACKREACTION="+csv(shift_grad),
        "AFFINE_WRONSKIAN_DRIFT="+str(drift),
        "ZERO_SOURCE_FIRST_BANK="+str(bank),
        "CYCLE_PERIODS="+csv(periods),
        "NEGATIVE_CONTROLS=PASS",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 30, "CERTIFICATE")
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
