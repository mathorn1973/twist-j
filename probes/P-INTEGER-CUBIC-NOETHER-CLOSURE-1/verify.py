#!/usr/bin/env python3
"""Prospective exact GLOBAL action / first-order Noether / nonclosure audit.

No scientific execution or import before the public six-file pin.
Primary encoding: incidence arrays, analytic global gradients, integer lifts.
"""
from fractions import Fraction as F
import hashlib
from pathlib import Path
import subprocess
import sys


M = 324
G = F(1, M)
ELL = (1, -1, 0, 0, 0)
SIG = (F(1, 2), F(1, 2), 0, 0, 0)
TAIL = tuple(range(5)) * 2
HEAD = tuple((r + k) % 5 for k in (1, 2) for r in range(5))
WEIGHT_INT = (29,) * 5 + (65,) * 5
WEIGHT = tuple(F(k, M) for k in WEIGHT_INT)
VB = tuple(tuple(int(r == i) - int(r == 4) for r in range(5)) for i in range(4))
KB = (
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (-1, -1, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, -1, -1, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, -1, -1, 0, 0, 0, 1, 0, 0),
    (1, 1, 1, 0, 0, 0, 0, 0, 1, 0),
    (0, 1, 1, 1, 0, 0, 0, 0, 0, 1),
)
SCALARS = ("chi", "alpha")
VECTORS = {"h": 5, "tau": 5, "p": 10, "lam": 5, "N": 10}
AUTHORITY = (
    ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class Falsifier(Exception):
    pass


def require(condition, key):
    if not condition:
        raise Falsifier(key)


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(t, x):
    return tuple(t * a for a in x)


def had(x, y):
    return tuple(a * b for a, b in zip(x, y))


def mean(x):
    return sum(x, F(0)) / 5


def project(x):
    v = mean(x)
    return tuple(t - v for t in x)


def incidence(x):
    return tuple(x[v] - x[u] for u, v in zip(TAIL, HEAD))


def divergence(x):
    out = [F(0)] * 5
    for u, v, z in zip(TAIL, HEAD, x):
        out[u] -= z
        out[v] += z
    return tuple(out)


def weighted(x):
    return had(WEIGHT, x)


def lap(x):
    return divergence(weighted(incidence(x)))


def lint(x):
    return tuple(188 * x[r] - 29 * (x[(r-1) % 5] + x[(r+1) % 5])
                 - 65 * (x[(r-2) % 5] + x[(r+2) % 5]) for r in range(5))


def ladj(x):
    return tuple(188 * x[r] - 65 * (x[(r-1) % 5] + x[(r+1) % 5])
                 - 29 * (x[(r-2) % 5] + x[(r+2) % 5]) for r in range(5))


def zeros(t):
    d = {k: [F(0)] * (t + 1) for k in SCALARS}
    d.update({k: [(F(0),) * width for _ in range(t + 1)]
              for k, width in VECTORS.items()})
    return d


def blank(t=5, a=0, d=1):
    x = zeros(t)
    x.update(T=t, a=a, D=d, Ehom=F(0))
    return x


def move(x, d, amount=F(1)):
    y = dict(x)
    for key in SCALARS:
        y[key] = [v + amount * w for v, w in zip(x[key], d[key])]
    for key in VECTORS:
        y[key] = [add(v, scale(amount, w)) for v, w in zip(x[key], d[key])]
    return y


def combine(d, e, amount=F(1)):
    return move(d, e, amount)


def pairing(grad, direction):
    total = F(0)
    for key in SCALARS:
        total += dot(grad[key], direction[key])
    for key in VECTORS:
        total += sum((dot(v, w) for v, w in zip(grad[key], direction[key])), F(0))
    return total


def energy_offset(a):
    return F(4342005, 8683757) * F(a, 4) ** 2


def density(x, b):
    cur, prev = x["h"][b], x["h"][b-1]
    c, v = x["chi"][b], x["chi"][b-1]
    out = [z*z / 2 for z in sub(cur, prev)]
    bc, bp = incidence(cur), incidence(prev)
    for k, (tail, head) in enumerate(zip(TAIL, HEAD)):
        z = WEIGHT[k] * bc[k] * bp[k] / 4
        out[tail] += z
        out[head] += z
    scalar = (c-v)**2/2 + c*v/2 - F(x["a"], 4)*(c+v)/2
    return tuple(out[r] + SIG[r]*scalar - G*ELL[r]*(v*cur[r]+c*prev[r])/2
                 for r in range(5))


def current(x, n, include_interaction=True):
    q = sub(x["h"][n+1], x["h"][n-1])
    b = incidence(x["h"][n])
    j = [WEIGHT[k] * b[k] * (q[u]+q[v]) / 4
         for k, (u, v) in enumerate(zip(TAIL, HEAD))]
    if include_interaction:
        j[0] -= G*(x["chi"][n+1]-x["chi"][n-1])*(x["h"][n][0]+x["h"][n][1])/4
    return tuple(j)


def residuals(x, n):
    h, chi = x["h"], x["chi"]
    rh = add(sub(add(h[n+1], h[n-1]), scale(2, h[n])),
             sub(lap(h[n]), scale(G*chi[n], ELL)))
    rc = chi[n+1]-chi[n]+chi[n-1]-F(x["a"], 4)-G*dot(ELL, h[n])
    return rh, rc


def auto_action(x):
    total = F(0)
    for b in range(1, x["T"]+1):
        dh = sub(x["h"][b], x["h"][b-1])
        dc = x["chi"][b]-x["chi"][b-1]
        total += (dot(dh, dh)+dc*dc)/2
    for n in range(1, x["T"]):
        h, c = x["h"][n], x["chi"][n]
        total += -dot(h, lap(h))/2-c*c/2+F(x["a"], 4)*c+G*c*dot(ELL, h)
    return total


def parts(x, include_interaction=True):
    s0 = auto_action(x)
    sint = F(0)
    off = energy_offset(x["a"])
    for b in range(1, x["T"]+1):
        en = density(x, b)
        s0 += 2*dot(x["lam"][b], lap(x["tau"][b]))
        sint -= x["alpha"][b]*(sum(en, F(0))+off-x["Ehom"])
        sint -= dot(x["lam"][b], en)
    for n in range(1, x["T"]):
        momentum = add(weighted(incidence(sub(x["tau"][n+1], x["tau"][n]))), x["p"][n])
        s0 += 2*dot(x["N"][n], momentum)
        sint += dot(x["N"][n], current(x, n, include_interaction))
    return s0, sint


def action(x, epsilon=F(1)):
    s0, sint = parts(x)
    return s0+epsilon*sint


def gradient(x, epsilon=F(1)):
    """All GLOBAL ambient derivatives; caller restricts to V and K bases."""
    t = x["T"]
    out = zeros(t)
    for n in range(1, t):
        rh, rc = residuals(x, n)
        out["h"][n] = scale(-1, rh)
        out["chi"][n] = -rc
    for b in range(1, t+1):
        en = density(x, b)
        mu = tuple(x["alpha"][b]+u for u in x["lam"][b])
        out["alpha"][b] = epsilon*(x["Ehom"]-energy_offset(x["a"])-sum(en, F(0)))
        out["lam"][b] = sub(scale(2, lap(x["tau"][b])), scale(epsilon, en))
        n_left = x["N"][b-1] if b > 1 else (F(0),)*10
        n_right = x["N"][b] if b < t else (F(0),)*10
        out["tau"][b] = scale(2, add(lap(x["lam"][b]), divergence(weighted(sub(n_left, n_right)))))
        for center, neighbor in ((b, b-1), (b-1, b)):
            if not 0 < center < t:
                continue
            h, hb = x["h"][center], x["h"][neighbor]
            c, cb = x["chi"][center], x["chi"][neighbor]
            edge = tuple(WEIGHT[k]*(mu[u]+mu[v])*incidence(hb)[k]/4
                         for k, (u, v) in enumerate(zip(TAIL, HEAD)))
            dh = sub(add(had(mu, sub(h, hb)), divergence(edge)),
                     scale(G*cb/2, had(mu, ELL)))
            dc = dot(SIG, mu)*(c-cb/2-F(x["a"], 8))-G*dot(had(mu, ELL), hb)/2
            out["h"][center] = sub(out["h"][center], scale(epsilon, dh))
            out["chi"][center] -= epsilon*dc
    for k in range(1, t):
        nshift = x["N"][k]
        h = x["h"][k]
        q = sub(x["h"][k+1], x["h"][k-1])
        qc = x["chi"][k+1]-x["chi"][k-1]
        edge = tuple(WEIGHT[j]*nshift[j]*(q[u]+q[v])/4
                     for j, (u, v) in enumerate(zip(TAIL, HEAD)))
        central = sub(divergence(edge), scale(G*qc*nshift[0]/2, SIG))
        out["h"][k] = add(out["h"][k], scale(epsilon, central))
        # The adjacent-current contributions absent from the old local test.
        endpoints = [F(0)]*5
        bh = incidence(h)
        for j, (u, v) in enumerate(zip(TAIL, HEAD)):
            z = WEIGHT[j]*nshift[j]*bh[j]/4
            endpoints[u] += z
            endpoints[v] += z
        source = -G*nshift[0]*(h[0]+h[1])/4
        for n, sign in ((k+1, 1), (k-1, -1)):
            if 0 < n < t:
                out["h"][n] = add(out["h"][n], scale(epsilon*sign, endpoints))
                out["chi"][n] += epsilon*sign*source
        out["p"][k] = scale(2, nshift)
        out["N"][k] = add(scale(2, add(weighted(incidence(sub(x["tau"][k+1], x["tau"][k]))), x["p"][k])),
                           scale(epsilon, current(x, k)))
    return out


def coordinates(t):
    result = []
    for n in range(1, t):
        for r in range(5):
            d = zeros(t)
            d["h"][n] = tuple(int(i == r) for i in range(5))
            result.append(d)
    for n in range(1, t):
        d = zeros(t)
        d["chi"][n] = F(1)
        result.append(d)
    for key, times, basis in (("tau", range(1, t+1), VB), ("p", range(1, t), KB)):
        for n in times:
            for b in basis:
                d = zeros(t)
                d[key][n] = b
                result.append(d)
    for n in range(1, t+1):
        d = zeros(t)
        d["alpha"][n] = F(1)
        result.append(d)
    for n in range(1, t+1):
        for b in VB:
            d = zeros(t)
            d["lam"][n] = b
            result.append(d)
    for n in range(1, t):
        for k in range(10):
            d = zeros(t)
            d["N"][n] = tuple(int(i == k) for i in range(10))
            result.append(d)
    return result


def fnum(t, i, c, a, seed):
    return ((17*t+11*i+7*seed+5*a+3*c) % 19)-9


def fixture(a, seed):
    x = blank(a=a, d=60)
    x["s"] = seed
    x["Ehom"] = F(seed+1, 7+a*a)
    for t in range(6):
        x["h"][t] = tuple(F(fnum(t, i, 0, a, seed), 60) for i in range(5))
        x["chi"][t] = F(fnum(t, 0, 1, a, seed), 60)
    for t in range(1, 6):
        for key, c in (("tau", 2), ("lam", 5)):
            x[key][t] = tuple(F(sum(fnum(t, i, c, a, seed)*VB[i][r] for i in range(4)), 60) for r in range(5))
        x["alpha"][t] = F(fnum(t, 0, 4, a, seed), 60)
    for t in range(1, 5):
        x["p"][t] = tuple(F(sum(fnum(t, i, 3, a, seed)*KB[i][k] for i in range(6)), 60) for k in range(10))
        x["N"][t] = tuple(F(fnum(t, k, 6, a, seed), 60) for k in range(10))
    return x


def parameters(a, seed):
    out = []
    for n in range(1, 5):
        for r in range(5):
            psi = [(F(0),)*5 for _ in range(6)]
            psi[n] = tuple(F(int(i == r)) for i in range(5))
            out.append((psi, 1))
    psi = [(F(0),)*5] + [tuple(F(fnum(n, r, 7, a, seed), 7) for r in range(5)) for n in range(1, 5)] + [(F(0),)*5]
    out.append((psi, 7))
    return out


def gauge0(psi):
    t = len(psi)-1
    d = zeros(t)
    for b in range(1, t+1):
        diff = sub(psi[b], psi[b-1])
        d["alpha"][b] = mean(diff)
        d["lam"][b] = project(diff)
    for n in range(1, t):
        d["N"][n] = incidence(psi[n])
    return d


def generator(x, psi):
    t = len(psi)-1
    d = zeros(t)
    for n in range(1, t):
        d["h"][n] = scale(F(1, 2), had(psi[n], sub(x["h"][n+1], x["h"][n-1])))
        d["chi"][n] = dot(SIG, psi[n])*(x["chi"][n+1]-x["chi"][n-1])/2
    return d


def directional4(x, d, epsilon=F(1)):
    return (-action(move(x, d, 2), epsilon)+8*action(move(x, d, 1), epsilon)
            -8*action(move(x, d, -1), epsilon)+action(move(x, d, -2), epsilon))/12


def part_derivative(x, d, part, include_interaction=True):
    return (parts(move(x, d), include_interaction)[part]-parts(move(x, d, -1), include_interaction)[part])/2


def hessian(x, u):
    out = F(0)
    for b in range(1, x["T"]+1):
        dh = sub(u["h"][b], u["h"][b-1])
        dc = u["chi"][b]-u["chi"][b-1]
        out += dot(dh, dh)+dc*dc
    for n in range(1, x["T"]):
        h, c = u["h"][n], u["chi"][n]
        out += -dot(h, lap(h))-c*c+2*G*c*dot(ELL, h)
    return out


def pure_gauge(x, d0):
    y = dict(x)
    for key in ("alpha", "lam", "N"):
        y[key] = d0[key]
    return y


def integer(x):
    x = F(x)
    require(x.denominator == 1, "DOMAIN")
    return x.numerator


def integer_records(x):
    d = x["D"]
    p = [tuple(integer(d*v) for v in h) for h in x["h"]]
    y = [integer(d*v) for v in x["chi"]]
    energy, flow, rhs = {}, {}, {}
    for b in range(1, x["T"]+1):
        cur, prev = p[b], p[b-1]
        bc, bp = incidence(cur), incidence(prev)
        e = [2*M*(cur[r]-prev[r])**2 for r in range(5)]
        for k, (tail, head) in enumerate(zip(TAIL, HEAD)):
            z = WEIGHT_INT[k]*bc[k]*bp[k]
            e[tail] += z
            e[head] += z
        for r in range(5):
            e[r] += (2*SIG[r])*(M*(y[b]-y[b-1])**2+M*y[b]*y[b-1]-81*x["a"]*d*(y[b]+y[b-1]))
            e[r] -= 2*ELL[r]*(y[b-1]*cur[r]+y[b]*prev[r])
        energy[b] = tuple(integer(v) for v in e)
    for n in range(1, x["T"]):
        q = sub(p[n+1], p[n-1])
        qc = y[n+1]-y[n-1]
        bh = incidence(p[n])
        j = [WEIGHT_INT[k]*bh[k]*(q[u]+q[v]) for k, (u, v) in enumerate(zip(TAIL, HEAD))]
        j[0] -= qc*(p[n][0]+p[n][1])
        flow[n] = tuple(integer(v) for v in j)
        ah = sub(add(scale(M, sub(add(p[n+1], p[n-1]), scale(2, p[n]))), lint(p[n])), scale(y[n], ELL))
        ac = M*(y[n+1]-y[n]+y[n-1])-81*x["a"]*d-dot(ELL, p[n])
        rhs[n] = tuple(integer(2*q[r]*ah[r]+2*SIG[r]*qc*ac) for r in range(5))
    return p, y, energy, flow, rhs


def tangent_integer_check(x, psi, qp, epsilon, d0, d1):
    d = x["D"]
    dn = 20*d*qp
    v = [tuple(integer(qp*z) for z in row) for row in psi]
    pn = [tuple(integer(d*z) for z in row) for row in x["h"]]
    yn = [integer(d*z) for z in x["chi"]]
    updated = move(x, combine(d0, d1, epsilon))
    lifted = dict(x)
    for key in SCALARS:
        lifted[key] = [integer(dn*z) for z in x[key]]
    for key in VECTORS:
        lifted[key] = [tuple(integer(dn*z) for z in row) for row in x[key]]
    for n in range(1, x["T"]):
        qh = sub(pn[n+1], pn[n-1])
        qc = yn[n+1]-yn[n-1]
        lifted["h"][n] = add(lifted["h"][n], scale(10*epsilon, had(v[n], qh)))
        lifted["chi"][n] += 5*epsilon*(v[n][0]+v[n][1])*qc
        lifted["N"][n] = add(lifted["N"][n], scale(20*d, incidence(v[n])))
    for b in range(1, x["T"]+1):
        dv = sub(v[b], v[b-1])
        sv = sum(dv)
        lifted["alpha"][b] += 4*d*sv
        lifted["lam"][b] = add(lifted["lam"][b], tuple(4*d*(5*z-sv) for z in dv))
    for key in SCALARS:
        require(all(F(z, dn) == w for z, w in zip(lifted[key], updated[key])), "INTEGER_TANGENT")
    for key in VECTORS:
        require(all(tuple(F(z, dn) for z in row) == w for row, w in zip(lifted[key], updated[key])), "INTEGER_TANGENT")
    require(all(sum(row) == 0 for row in updated["tau"]+updated["lam"]), "INTEGER_TANGENT")
    require(all(divergence(row) == (0,)*5 for row in updated["p"]), "INTEGER_TANGENT")


def bracket_formula(x, psi, eta):
    t = x["T"]
    out = zeros(t)
    ps = [dot(SIG, row) for row in psi]
    es = [dot(SIG, row) for row in eta]
    for n in range(1, t):
        for delta in (-1, 1):
            k = n+delta
            if not 0 < k < t:
                continue
            coeff = scale(F(1, 4), sub(had(eta[n], psi[k]), had(psi[n], eta[k])))
            out["h"][n] = add(out["h"][n], had(coeff, sub(x["h"][n+2*delta], x["h"][n])))
            out["chi"][n] += (es[n]*ps[k]-ps[n]*es[k])*(x["chi"][n+2*delta]-x["chi"][n])/4
    return out


def check_witnesses():
    unit = (F(1), F(0), F(0), F(0), F(0))
    edge0 = (F(1),)+(F(0),)*9
    x = blank(d=40)
    x["h"][1] = tuple(F(v, 40) for v in (6, 11, 11, 6, 6))
    old = gradient(x)
    x["N"][1] = edge0
    new = gradient(x)
    require(sub(new["h"][2], old["h"][2]) == (F(29, 10368), F(29, 10368), 0, 0, 0), "NEIGHBOR_WITNESS")
    require(new["chi"][2]-old["chi"][2] == F(-17, 51840), "NEIGHBOR_WITNESS")
    # Independent action differences verify both neighbor coefficients.
    off = dict(x)
    off["N"] = [(F(0),)*10 for _ in range(6)]
    for key, r, expected in (("h", 0, F(29, 10368)), ("h", 1, F(29, 10368)), ("chi", None, F(-17, 51840))):
        d = zeros(5)
        if r is None:
            d[key][2] = F(1)
        else:
            d[key][2] = tuple(int(i == r) for i in range(5))
        got = (action(move(x, d))-action(move(x, d, -1))-action(move(off, d))+action(move(off, d, -1)))/2
        require(got == expected, "NEIGHBOR_WITNESS")

    x = blank()
    x["h"][3] = unit
    x["alpha"][3] = F(1)
    psi = [(F(0),)*5 for _ in range(6)]
    psi[2] = psi[3] = unit
    d0, d1 = gauge0(psi), generator(x, psi)
    first = part_derivative(x, d0, 1)
    second = part_derivative(x, d1, 0)
    rem = part_derivative(x, d1, 1)
    require((first, second, rem) == (F(1, 2), F(-1, 2), F(115, 324)), "REMAINDER_WITNESS")
    joint = combine(d0, d1)
    exact = directional4(x, joint)
    naive = (action(move(x, joint))-action(move(x, joint, -1)))/2
    require(exact == rem and naive-exact == F(-1, 8), "CENTRAL_WITNESS")
    pg = pure_gauge(x, d0)
    require(action(pg)-auto_action(move(x, d1, -1)) == F(-115, 648), "FIELD_REDEFINITION")
    require(first-second == 1, "CONTROL")
    bad = dict(d0)
    bad["alpha"] = [F(0)]*6
    require(part_derivative(x, bad, 1)+second == F(-1, 10), "CONTROL")

    x = blank()
    x["h"][2] = unit
    x["chi"][3] = F(1)
    psi = [(F(0),)*5 for _ in range(6)]
    psi[2] = unit
    d0, d1 = gauge0(psi), generator(x, psi)
    defect = part_derivative(x, d0, 1, False)+part_derivative(x, d1, 0)
    require(defect == F(-1, 1296), "CONTROL")
    x = blank()
    x["p"][2] = edge0
    require(part_derivative(x, d0, 0) == -2, "CONTROL")

    x = blank()
    x["h"] = [(F(1, 5),)*5 for _ in range(6)]
    x["h"][4] = add(x["h"][4], ELL)
    psi = [(F(0),)*5 for _ in range(6)]
    eta = [(F(0),)*5 for _ in range(6)]
    psi[2], eta[3] = ELL, ELL
    comm = combine(generator(generator(x, psi), eta), generator(generator(x, eta), psi), -1)
    require(comm["h"][2] == (F(-1, 4), F(1, 4), 0, 0, 0), "NONCLOSURE")
    require(sub(x["h"][3], x["h"][1]) == (0,)*5, "NONCLOSURE")
    require(sum(generator(x, eta)["h"][3]) == 1, "CONTROL")


def certificate():
    root = Path(__file__).resolve().parents[2]
    for name, size, sha in AUTHORITY:
        raw = (root/name).read_bytes()
        require(len(raw) == size and hashlib.sha256(raw).hexdigest() == sha, "AUTHORITY")
    for basis in VB:
        require(sum(basis) == 0 and lap(basis) == scale(F(1, M), lint(basis)), "INCIDENCE")
        require(lint(ladj(basis)) == scale(53605, basis), "INCIDENCE")
    for basis in KB:
        require(divergence(basis) == (0,)*5, "INCIDENCE")
    require(tuple(row[4+i] for i, row in enumerate(KB)) == (1,)*6, "INCIDENCE")
    coords = coordinates(5)
    require(len(coords) == 133, "DOMAIN")
    grads_payload, noether_payload = [], []
    counters = {k: 0 for k in ("GLOBAL_CONFIGURATIONS", "GLOBAL_VARIATIONS", "CONTINUITY_VERTICES",
        "CONSTRAINT_PROPAGATION_VERTICES", "INTEGER_CONTINUITY_VERTICES", "NOETHER_IDENTITIES",
        "INTEGER_NOETHER_IDENTITIES", "DEFORMATION_CHECKS", "FIELD_REDEFINITION_CHECKS",
        "INTEGER_TANGENT_CHECKS", "COMMUTATOR_CHECKS")}
    for a in (-1, 0, 1):
        for seed in (0, 1):
            x = fixture(a, seed)
            require(all(sum(v) == 0 for v in x["tau"]+x["lam"]), "DOMAIN")
            require(all(divergence(v) == (0,)*5 for v in x["p"]), "DOMAIN")
            counters["GLOBAL_CONFIGURATIONS"] += 1
            grad1 = gradient(x)
            grad0 = gradient(x, F(0))
            for i, d in enumerate(coords):
                value = pairing(grad1, d)
                centered = (action(move(x, d))-action(move(x, d, -1)))/2
                require(value == centered, "GLOBAL_GRADIENT")
                grads_payload.append(f"{a}|{seed}|{i}|{value}\n")
                counters["GLOBAL_VARIATIONS"] += 1
            p, y, eint, jint, irhs = integer_records(x)
            cont = {}
            for n in range(1, 5):
                en, enext = density(x, n), density(x, n+1)
                j = current(x, n)
                rh, rc = residuals(x, n)
                qh = sub(x["h"][n+1], x["h"][n-1])
                qc = x["chi"][n+1]-x["chi"][n-1]
                cont[n] = add(sub(enext, en), divergence(j))
                right = scale(F(1, 2), add(had(qh, rh), scale(qc*rc, SIG)))
                require(cont[n] == right, "CONTINUITY")
                hprev = sub(scale(2, lap(x["tau"][n])), project(en))
                hnext = sub(scale(2, lap(x["tau"][n+1])), project(enext))
                mom = add(scale(2, add(weighted(incidence(sub(x["tau"][n+1], x["tau"][n]))), x["p"][n])), j)
                predicted = sub(sub(divergence(mom), scale(2, divergence(x["p"][n]))), project(cont[n]))
                require(sub(hnext, hprev) == predicted, "CONSTRAINT_PROPAGATION")
                require(sub(eint[n+1], eint[n]) == sub(irhs[n], divergence(jint[n])), "INTEGER_CONTINUITY")
                require(scale(4*M*x["D"]**2, en) == eint[n] and scale(4*M*x["D"]**2, j) == jint[n], "INTEGER_CONTINUITY")
                for key in ("CONTINUITY_VERTICES", "CONSTRAINT_PROPAGATION_VERTICES", "INTEGER_CONTINUITY_VERTICES"):
                    counters[key] += 5
            params = parameters(a, seed)
            for index, (psi, qp) in enumerate(params):
                d0, d1 = gauge0(psi), generator(x, psi)
                d0s0 = pairing(grad0, d0)
                d0si = pairing(grad1, d0)-d0s0
                d1s0 = pairing(grad0, d1)
                u = pairing(grad1, d1)-d1s0
                rhs = sum((dot(psi[n], cont[n]) for n in range(1, 5)), F(0))
                require(d0s0 == 0, "AUXILIARY_GAUGE")
                require(d0si == rhs and d1s0 == -rhs, "NOETHER")
                require(part_derivative(x, d0, 1) == d0si and part_derivative(x, d1, 0) == d1s0, "NOETHER")
                require(part_derivative(x, d1, 1) == u, "NOETHER")
                scale_int = 4*M*x["D"]**2*qp
                lhs_int = sum(dot(tuple(integer(qp*v) for v in psi[n]), add(sub(eint[n+1], eint[n]), divergence(jint[n]))) for n in range(1, 5))
                rhs_int = sum(dot(tuple(integer(qp*v) for v in psi[n]), irhs[n]) for n in range(1, 5))
                require(lhs_int == rhs_int == integer(scale_int*d0si) == -integer(scale_int*d1s0), "INTEGER_NOETHER")
                counters["NOETHER_IDENTITIES"] += 1
                counters["INTEGER_NOETHER_IDENTITIES"] += 1
                noether_payload.append(f"{a}|{seed}|{index}|{d0si}|{d1s0}|{u}\n")
                pg = pure_gauge(x, d0)
                hh = hessian(x, d1)
                for epsilon in (-1, 0, 1, 2):
                    direction = combine(d0, d1, epsilon)
                    actual = directional4(x, direction, F(epsilon))
                    require(actual == epsilon*epsilon*u, "DEFORMATION")
                    require(actual == pairing(gradient(x, F(epsilon)), direction), "DEFORMATION")
                    require(action(pg, F(epsilon)) == auto_action(move(x, d1, -epsilon))-epsilon*epsilon*hh/2, "FIELD_REDEFINITION")
                    tangent_integer_check(x, psi, qp, epsilon, d0, d1)
                    for key in ("DEFORMATION_CHECKS", "FIELD_REDEFINITION_CHECKS", "INTEGER_TANGENT_CHECKS"):
                        counters[key] += 1
            for i in range(20):
                psi = params[i][0]
                for j in range(i+1, 20):
                    eta = params[j][0]
                    comm = combine(generator(generator(x, psi), eta), generator(generator(x, eta), psi), -1)
                    form = bracket_formula(x, psi, eta)
                    require(comm["h"] == form["h"] and comm["chi"] == form["chi"], "COMMUTATOR")
                    counters["COMMUTATOR_CHECKS"] += 1
    expected = (6, 798, 120, 120, 120, 126, 126, 504, 504, 504, 1140)
    require(tuple(counters.values()) == expected, "CERTIFICATE")
    check_witnesses()
    lines = ["CERTIFICATE=P-INTEGER-CUBIC-NOETHER-CLOSURE-1", "AUTHORITY_FILES=5"]
    lines += [f"{key}={value}" for key, value in counters.items()]
    lines += ["GLOBAL_GRADIENT_SHA256="+hashlib.sha256("".join(grads_payload).encode("ascii")).hexdigest(),
              "NOETHER_PAYLOAD_SHA256="+hashlib.sha256("".join(noether_payload).encode("ascii")).hexdigest(),
              "GLOBAL_NEIGHBOR_GRADIENT=29/10368,29/10368,0,0,0;-17/51840",
              "SECOND_ORDER_REMAINDER=115/324", "NAIVE_CENTRAL_DEFECT=-1/8",
              "FIELD_REDEFINITION_DEFECT=-115/648", "GENERATOR_NONCLOSURE=-1/4,1/4,0,0,0",
              "NEGATIVE_CONTROLS=10", "CERTIFICATE_RESULT=PASS"]
    require(len(lines) == 22, "CERTIFICATE")
    return ("\n".join(lines)+"\n").encode("ascii")


def main():
    try:
        raw = certificate()
        child = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        require(child.returncode == 0 and child.stderr == b"" and child.stdout == raw, "BREAKER_BYTES")
        sys.stdout.buffer.write(raw+b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except Falsifier as exc:
        sys.stdout.buffer.write((f"FALSIFIER={exc}\nRESULT=FAIL\n").encode("ascii"))


if __name__ == "__main__":
    main()
