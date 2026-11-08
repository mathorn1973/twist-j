#!/usr/bin/env python3
"""Prospective exact second-order Noether and extended commutator audit.

No scientific execution or import before the public six-file pin.
Primary encoding: incidence arrays, form (3.7a) of S_2, analytic polarized
gradients, four-point directional derivatives, and common-denominator integer lifts.
"""
from fractions import Fraction as F
import hashlib
from pathlib import Path
import subprocess
import sys


PROBE = "P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-1"
M = 324
G = F(1, M)
ONE = (F(1),) * 5
ELL = (1, -1, 0, 0, 0)
SIG = (F(1, 2), F(1, 2), F(0), F(0), F(0))
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
FALSIFIERS = frozenset((
    "AUTHORITY", "DOMAIN", "INCIDENCE", "GLOBAL_GRADIENT", "CONTINUITY",
    "CONSTRAINT_PROPAGATION", "INTEGER_CONTINUITY", "AUXILIARY_GAUGE",
    "NOETHER", "SECOND_ORDER_NOETHER", "INTEGER_SECOND_ORDER_NOETHER",
    "DEFORMATION", "FIELD_REDEFINITION", "INTEGER_TANGENT", "COMMUTATOR",
    "NEIGHBOR_WITNESS", "REMAINDER_WITNESS", "CENTRAL_WITNESS", "CONTROL",
    "NONCLOSURE", "CERTIFICATE", "BREAKER_BYTES",
))


class Falsifier(Exception):
    def __init__(self, key):
        if key not in FALSIFIERS:
            raise ValueError(f"unregistered falsifier: {key}")
        super().__init__(key)


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
    return tuple(188 * x[r] - 29 * (x[(r - 1) % 5] + x[(r + 1) % 5])
                 - 65 * (x[(r - 2) % 5] + x[(r + 2) % 5]) for r in range(5))


def ladj(x):
    return tuple(188 * x[r] - 65 * (x[(r - 1) % 5] + x[(r + 1) % 5])
                 - 29 * (x[(r - 2) % 5] + x[(r + 2) % 5]) for r in range(5))


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
    cur, prev = x["h"][b], x["h"][b - 1]
    c, v = x["chi"][b], x["chi"][b - 1]
    out = [z * z / 2 for z in sub(cur, prev)]
    bc, bp = incidence(cur), incidence(prev)
    for k, (tail, head) in enumerate(zip(TAIL, HEAD)):
        z = WEIGHT[k] * bc[k] * bp[k] / 4
        out[tail] += z
        out[head] += z
    scalar = (c - v) ** 2 / 2 + c * v / 2 - F(x["a"], 4) * (c + v) / 2
    return tuple(out[r] + SIG[r] * scalar - G * ELL[r] * (v * cur[r] + c * prev[r]) / 2
                 for r in range(5))


def density_deriv(x, y, b):
    """Directional derivative D_x e_loc,b[x][y] at bond b."""
    cur, prev = x["h"][b], x["h"][b - 1]
    ycur, yprev = y["h"][b], y["h"][b - 1]
    c, v = x["chi"][b], x["chi"][b - 1]
    yc, yv = y["chi"][b], y["chi"][b - 1]
    out = [(cur[r] - prev[r]) * (ycur[r] - yprev[r]) for r in range(5)]
    bc, bp = incidence(cur), incidence(prev)
    ybc, ybp = incidence(ycur), incidence(yprev)
    for k, (tail, head) in enumerate(zip(TAIL, HEAD)):
        z = WEIGHT[k] * (bc[k] * ybp[k] + ybc[k] * bp[k]) / 4
        out[tail] += z
        out[head] += z
    scalar = (c - v) * (yc - yv) + (c * yv + yc * v) / 2 - F(x["a"], 4) * (yc + yv) / 2
    return tuple(
        out[r] + SIG[r] * scalar
        - G * ELL[r] * (v * ycur[r] + yv * cur[r] + c * yprev[r] + yc * prev[r]) / 2
        for r in range(5)
    )


def current(x, n, include_interaction=True):
    q = sub(x["h"][n + 1], x["h"][n - 1])
    b = incidence(x["h"][n])
    j = [WEIGHT[k] * b[k] * (q[u] + q[v]) / 4
         for k, (u, v) in enumerate(zip(TAIL, HEAD))]
    if include_interaction:
        j[0] -= G * (x["chi"][n + 1] - x["chi"][n - 1]) * (x["h"][n][0] + x["h"][n][1]) / 4
    return tuple(j)


def current_deriv(x, y, n, include_interaction=True):
    """Directional derivative D_x j_n[x][y] at slice n."""
    q = sub(x["h"][n + 1], x["h"][n - 1])
    yq = sub(y["h"][n + 1], y["h"][n - 1])
    b = incidence(x["h"][n])
    yb = incidence(y["h"][n])
    j = [WEIGHT[k] * (b[k] * (yq[u] + yq[v]) + yb[k] * (q[u] + q[v])) / 4
         for k, (u, v) in enumerate(zip(TAIL, HEAD))]
    if include_interaction:
        qc = x["chi"][n + 1] - x["chi"][n - 1]
        yqc = y["chi"][n + 1] - y["chi"][n - 1]
        j[0] -= G * (qc * (y["h"][n][0] + y["h"][n][1])
                     + yqc * (x["h"][n][0] + x["h"][n][1])) / 4
    return tuple(j)


def residuals(x, n, homogeneous=False):
    h, chi = x["h"], x["chi"]
    rh = add(sub(add(h[n + 1], h[n - 1]), scale(2, h[n])),
             sub(lap(h[n]), scale(G * chi[n], ELL)))
    force = F(0) if homogeneous else F(x["a"], 4)
    rc = chi[n + 1] - chi[n] + chi[n - 1] - force - G * dot(ELL, h[n])
    return rh, rc


def auto_action(x):
    total = F(0)
    for b in range(1, x["T"] + 1):
        dh = sub(x["h"][b], x["h"][b - 1])
        dc = x["chi"][b] - x["chi"][b - 1]
        total += (dot(dh, dh) + dc * dc) / 2
    for n in range(1, x["T"]):
        h, c = x["h"][n], x["chi"][n]
        total += -dot(h, lap(h)) / 2 - c * c / 2 + F(x["a"], 4) * c + G * c * dot(ELL, h)
    return total


def hessian_bilinear(t, u, v):
    out = F(0)
    for b in range(1, t + 1):
        duh = sub(u["h"][b], u["h"][b - 1])
        dvh = sub(v["h"][b], v["h"][b - 1])
        duc = u["chi"][b] - u["chi"][b - 1]
        dvc = v["chi"][b] - v["chi"][b - 1]
        out += dot(duh, dvh) + duc * dvc
    for n in range(1, t):
        uh, uc = u["h"][n], u["chi"][n]
        vh, vc = v["h"][n], v["chi"][n]
        out += -dot(uh, lap(vh)) - uc * vc + G * (uc * dot(ELL, vh) + vc * dot(ELL, uh))
    return out


def hessian(x, u):
    return hessian_bilinear(x["T"], u, u)


def gauge0(psi):
    t = len(psi) - 1
    d = zeros(t)
    for b in range(1, t + 1):
        diff = sub(psi[b], psi[b - 1])
        d["alpha"][b] = mean(diff)
        d["lam"][b] = project(diff)
    for n in range(1, t):
        d["N"][n] = incidence(psi[n])
    return d


def dressing(x):
    """Prefix-sum multiplier dressing Psi[M] with Psi_0 = Psi_T = 0."""
    t = x["T"]
    psi = [(F(0),) * 5 for _ in range(t + 1)]
    running = (F(0),) * 5
    for b in range(1, t):
        mu = tuple(x["alpha"][b] + u for u in x["lam"][b])
        running = add(running, mu)
        psi[b] = running
    return psi


def residual_multipliers(x):
    """M_tilde[M] = M - Gamma(Psi[M])."""
    g = gauge0(dressing(x))
    out = zeros(x["T"])
    for b in range(1, x["T"] + 1):
        out["alpha"][b] = x["alpha"][b] - g["alpha"][b]
        out["lam"][b] = sub(x["lam"][b], g["lam"][b])
    for n in range(1, x["T"]):
        out["N"][n] = sub(x["N"][n], g["N"][n])
    return out


def generator(x, psi):
    t = len(psi) - 1
    d = zeros(t)
    for n in range(1, t):
        d["h"][n] = scale(F(1, 2), had(psi[n], sub(x["h"][n + 1], x["h"][n - 1])))
        d["chi"][n] = dot(SIG, psi[n]) * (x["chi"][n + 1] - x["chi"][n - 1]) / 2
    return d


def generator_adjoint(z, psi):
    """Interior adjoint G_psi^T on interior covectors z (z_0 = z_T = 0)."""
    t = len(psi) - 1
    out = zeros(t)
    for n in range(1, t):
        left_h = had(psi[n - 1], z["h"][n - 1]) if n > 1 else (F(0),) * 5
        right_h = had(psi[n + 1], z["h"][n + 1]) if n + 1 < t else (F(0),) * 5
        out["h"][n] = scale(F(1, 2), sub(left_h, right_h))
        left_c = dot(SIG, psi[n - 1]) * z["chi"][n - 1] if n > 1 else F(0)
        right_c = dot(SIG, psi[n + 1]) * z["chi"][n + 1] if n + 1 < t else F(0)
        out["chi"][n] = (left_c - right_c) / 2
    return out


def generator2(x, psi):
    """Second-order field generator delta_2^(psi) x = G_(Psi[M]) G_psi x."""
    return generator(generator(x, psi), dressing(x))


def sint_field_deriv(x, mult, y, include_interaction=True):
    """Exact directional derivative D_x S_int[x, mult][y]."""
    t = x["T"]
    total = F(0)
    for b in range(1, t + 1):
        de = density_deriv(x, y, b)
        total -= mult["alpha"][b] * sum(de, F(0))
        total -= dot(mult["lam"][b], de)
    for n in range(1, t):
        dj = current_deriv(x, y, n, include_interaction)
        total += dot(mult["N"][n], dj)
    return total


def s2_action(x):
    """Form (3.7a): -D_x S_int[x, M_tilde[M]][G_(Psi[M]) x] + (1/2) Hess[G_Psi x, G_Psi x]."""
    psi_m = dressing(x)
    y = generator(x, psi_m)
    mtilde = residual_multipliers(x)
    return -sint_field_deriv(x, mtilde, y) + hessian(x, y) / 2


def parts(x, include_interaction=True):
    s0 = auto_action(x)
    sint = F(0)
    off = energy_offset(x["a"])
    for b in range(1, x["T"] + 1):
        en = density(x, b)
        s0 += 2 * dot(x["lam"][b], lap(x["tau"][b]))
        sint -= x["alpha"][b] * (sum(en, F(0)) + off - x["Ehom"])
        sint -= dot(x["lam"][b], en)
    for n in range(1, x["T"]):
        momentum = add(weighted(incidence(sub(x["tau"][n + 1], x["tau"][n]))), x["p"][n])
        s0 += 2 * dot(x["N"][n], momentum)
        sint += dot(x["N"][n], current(x, n, include_interaction))
    return s0, sint, s2_action(x)


def action(x, epsilon=F(1)):
    s0, sint, s2 = parts(x)
    return s0 + epsilon * sint + (epsilon ** 2) * s2


def sint_grad_x(x, mult, homogeneous=False):
    """Analytic interior field gradient of S_int[x, mult]."""
    t = x["T"]
    out = zeros(t)
    force_a = F(0) if homogeneous else F(x["a"], 8)
    for b in range(1, t + 1):
        mu = tuple(mult["alpha"][b] + u for u in mult["lam"][b])
        for center, neighbor in ((b, b - 1), (b - 1, b)):
            if not 0 < center < t:
                continue
            h, hb = x["h"][center], x["h"][neighbor]
            c, cb = x["chi"][center], x["chi"][neighbor]
            edge = tuple(WEIGHT[k] * (mu[u] + mu[v]) * incidence(hb)[k] / 4
                         for k, (u, v) in enumerate(zip(TAIL, HEAD)))
            dh = sub(add(had(mu, sub(h, hb)), divergence(edge)),
                     scale(G * cb / 2, had(mu, ELL)))
            dc = dot(SIG, mu) * (c - cb / 2 - force_a) - G * dot(had(mu, ELL), hb) / 2
            out["h"][center] = sub(out["h"][center], dh)
            out["chi"][center] -= dc
    for k in range(1, t):
        nshift = mult["N"][k]
        h = x["h"][k]
        q = sub(x["h"][k + 1], x["h"][k - 1])
        qc = x["chi"][k + 1] - x["chi"][k - 1]
        edge = tuple(WEIGHT[j] * nshift[j] * (q[u] + q[v]) / 4
                     for j, (u, v) in enumerate(zip(TAIL, HEAD)))
        central = sub(divergence(edge), scale(G * qc * nshift[0] / 2, SIG))
        out["h"][k] = add(out["h"][k], central)
        endpoints = [F(0)] * 5
        bh = incidence(h)
        for j, (u, v) in enumerate(zip(TAIL, HEAD)):
            z = WEIGHT[j] * nshift[j] * bh[j] / 4
            endpoints[u] += z
            endpoints[v] += z
        source = -G * nshift[0] * (h[0] + h[1]) / 4
        for n, sign in ((k + 1, 1), (k - 1, -1)):
            if 0 < n < t:
                out["h"][n] = add(out["h"][n], scale(sign, endpoints))
                out["chi"][n] += sign * source
    return out


def psi_pairing(z, w, t):
    """Vertex covector u_n such that <z, G_psi w> = sum_n <u_n, psi_n>."""
    out = [(F(0),) * 5 for _ in range(t + 1)]
    for n in range(1, t):
        qh = sub(w["h"][n + 1], w["h"][n - 1])
        qc = w["chi"][n + 1] - w["chi"][n - 1]
        out[n] = scale(F(1, 2), add(had(z["h"][n], qh), scale(z["chi"][n] * qc, SIG)))
    return out


def s2_gradient(x):
    """Exact analytic ambient gradient of S_2[x, M]."""
    t = x["T"]
    out = zeros(t)
    psi_m = dressing(x)
    y = generator(x, psi_m)
    mtilde = residual_multipliers(x)
    # 1. Interior field gradient nabla_x S_2[x, M].
    gx_mtilde = sint_grad_x(x, mtilde)
    gy_hom = sint_grad_x(y, mtilde, homogeneous=True)
    rhom_y = zeros(t)
    rx = zeros(t)
    for n in range(1, t):
        rh_y, rc_y = residuals(y, n, homogeneous=True)
        rhom_y["h"][n], rhom_y["chi"][n] = rh_y, rc_y
        rh_x, rc_x = residuals(x, n, homogeneous=False)
        rx["h"][n], rx["chi"][n] = rh_x, rc_x
    combined = combine(gx_mtilde, rhom_y, F(1))
    adj = generator_adjoint(combined, psi_m)
    for n in range(1, t):
        out["h"][n] = sub( scale(-1, gy_hom["h"][n]), adj["h"][n])
        out["chi"][n] = -gy_hom["chi"][n] - adj["chi"][n]
    # 2. Multiplier gradient nabla_M S_2[x, M].
    gm_alpha = [F(0)] * (t + 1)
    gm_lam = [(F(0),) * 5 for _ in range(t + 1)]
    for b in range(1, t + 1):
        de = density_deriv(x, y, b)
        gm_alpha[b] = sum(de, F(0))
        gm_lam[b] = de
    for n in range(1, t):
        out["N"][n] = scale(-1, current_deriv(x, y, n))
    u_rx = psi_pairing(rx, y, t)
    u_mtilde = psi_pairing(gx_mtilde, x, t)
    v = [(F(0),) * 5 for _ in range(t + 1)]
    for n in range(1, t):
        v[n] = sub(u_rx[n], u_mtilde[n])
    suffix = (F(0),) * 5
    suffix_by_b = [(F(0),) * 5 for _ in range(t + 1)]
    for b in range(t - 1, 0, -1):
        suffix = add(suffix, v[b])
        suffix_by_b[b] = suffix
    for b in range(1, t + 1):
        out["alpha"][b] = gm_alpha[b] + sum(suffix_by_b[b], F(0))
        out["lam"][b] = add(gm_lam[b], suffix_by_b[b])
    return out


def gradient(x, epsilon=F(1)):
    """All GLOBAL ambient derivatives of S_<=2(epsilon); caller restricts to V and K bases."""
    t = x["T"]
    out = zeros(t)
    for n in range(1, t):
        rh, rc = residuals(x, n)
        out["h"][n] = scale(-1, rh)
        out["chi"][n] = -rc
    gx_int = sint_grad_x(x, x)
    for n in range(1, t):
        out["h"][n] = add(out["h"][n], scale(epsilon, gx_int["h"][n]))
        out["chi"][n] += epsilon * gx_int["chi"][n]
    for b in range(1, t + 1):
        en = density(x, b)
        out["alpha"][b] = epsilon * (x["Ehom"] - energy_offset(x["a"]) - sum(en, F(0)))
        out["lam"][b] = sub(scale(2, lap(x["tau"][b])), scale(epsilon, en))
        n_left = x["N"][b - 1] if b > 1 else (F(0),) * 10
        n_right = x["N"][b] if b < t else (F(0),) * 10
        out["tau"][b] = scale(2, add(lap(x["lam"][b]), divergence(weighted(sub(n_left, n_right)))))
    for k in range(1, t):
        out["p"][k] = scale(2, x["N"][k])
        out["N"][k] = add(
            scale(2, add(weighted(incidence(sub(x["tau"][k + 1], x["tau"][k]))), x["p"][k])),
            scale(epsilon, current(x, k)),
        )
    if epsilon != 0:
        g2 = s2_gradient(x)
        out = combine(out, g2, epsilon * epsilon)
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
    for key, times, basis in (("tau", range(1, t + 1), VB), ("p", range(1, t), KB)):
        for n in times:
            for b in basis:
                d = zeros(t)
                d[key][n] = b
                result.append(d)
    for n in range(1, t + 1):
        d = zeros(t)
        d["alpha"][n] = F(1)
        result.append(d)
    for n in range(1, t + 1):
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
    return ((17 * t + 11 * i + 7 * seed + 5 * a + 3 * c) % 19) - 9


def fixture(a, seed):
    x = blank(a=a, d=60)
    x["s"] = seed
    x["Ehom"] = F(seed + 1, 7 + a * a)
    for t in range(6):
        x["h"][t] = tuple(F(fnum(t, i, 0, a, seed), 60) for i in range(5))
        x["chi"][t] = F(fnum(t, 0, 1, a, seed), 60)
    for t in range(1, 6):
        for key, c in (("tau", 2), ("lam", 5)):
            x[key][t] = tuple(F(sum(fnum(t, i, c, a, seed) * VB[i][r] for i in range(4)), 60)
                              for r in range(5))
        x["alpha"][t] = F(fnum(t, 0, 4, a, seed), 60)
    for t in range(1, 5):
        x["p"][t] = tuple(F(sum(fnum(t, i, 3, a, seed) * KB[i][k] for i in range(6)), 60)
                          for k in range(10))
        x["N"][t] = tuple(F(fnum(t, k, 6, a, seed), 60) for k in range(10))
    return x


def parameters(a, seed):
    out = []
    for n in range(1, 5):
        for r in range(5):
            psi = [(F(0),) * 5 for _ in range(6)]
            psi[n] = tuple(F(int(i == r)) for i in range(5))
            out.append((psi, 1))
    psi = ([(F(0),) * 5]
           + [tuple(F(fnum(n, r, 7, a, seed), 7) for r in range(5)) for n in range(1, 5)]
           + [(F(0),) * 5])
    out.append((psi, 7))
    return out


def directional4(x, d, epsilon=F(1)):
    return (-action(move(x, d, 2), epsilon) + 8 * action(move(x, d, 1), epsilon)
            - 8 * action(move(x, d, -1), epsilon) + action(move(x, d, -2), epsilon)) / 12


def part_derivative(x, d, part, include_interaction=True):
    return (parts(move(x, d, 1), include_interaction)[part]
            - parts(move(x, d, -1), include_interaction)[part]) / 2


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
    p = [tuple(integer(d * v) for v in h) for h in x["h"]]
    y = [integer(d * v) for v in x["chi"]]
    energy, flow, rhs = {}, {}, {}
    for b in range(1, x["T"] + 1):
        cur, prev = p[b], p[b - 1]
        bc, bp = incidence(cur), incidence(prev)
        e = [2 * M * (cur[r] - prev[r]) ** 2 for r in range(5)]
        for k, (tail, head) in enumerate(zip(TAIL, HEAD)):
            z = WEIGHT_INT[k] * bc[k] * bp[k]
            e[tail] += z
            e[head] += z
        for r in range(5):
            e[r] += (2 * SIG[r]) * (
                M * (y[b] - y[b - 1]) ** 2 + M * y[b] * y[b - 1] - 81 * x["a"] * d * (y[b] + y[b - 1])
            )
            e[r] -= 2 * ELL[r] * (y[b - 1] * cur[r] + y[b] * prev[r])
        energy[b] = tuple(integer(v) for v in e)
    for n in range(1, x["T"]):
        q = sub(p[n + 1], p[n - 1])
        qc = y[n + 1] - y[n - 1]
        bh = incidence(p[n])
        j = [WEIGHT_INT[k] * bh[k] * (q[u] + q[v]) for k, (u, v) in enumerate(zip(TAIL, HEAD))]
        j[0] -= qc * (p[n][0] + p[n][1])
        flow[n] = tuple(integer(v) for v in j)
        ah = sub(add(scale(M, sub(add(p[n + 1], p[n - 1]), scale(2, p[n]))), lint(p[n])),
                 scale(y[n], ELL))
        ac = M * (y[n + 1] - y[n] + y[n - 1]) - 81 * x["a"] * d - dot(ELL, p[n])
        rhs[n] = tuple(integer(2 * q[r] * ah[r] + 2 * SIG[r] * qc * ac) for r in range(5))
    return p, y, energy, flow, rhs


def integer_second_order_noether_check(x, psi, qp, d0s2, d1si, d2s0):
    d = x["D"]
    scale_int = 16 * M * (d ** 3) * qp
    p = [tuple(integer(d * z) for z in row) for row in x["h"]]
    yn = [integer(d * z) for z in x["chi"]]
    v = [tuple(integer(qp * z) for z in row) for row in psi]
    psi_hat = [(0,) * 5 for _ in range(x["T"] + 1)]
    running = (0,) * 5
    for b in range(1, x["T"]):
        ab = integer(d * x["alpha"][b])
        lb = tuple(integer(d * z) for z in x["lam"][b])
        mb = tuple(ab + z for z in lb)
        running = tuple(r + m_r for r, m_r in zip(running, mb))
        psi_hat[b] = running
    ytilde_h = [(0,) * 5 for _ in range(x["T"] + 1)]
    ytilde_c = [0] * (x["T"] + 1)
    for n in range(1, x["T"]):
        qh = tuple(p[n + 1][r] - p[n - 1][r] for r in range(5))
        qc = yn[n + 1] - yn[n - 1]
        ytilde_h[n] = tuple(v[n][r] * qh[r] for r in range(5))
        ytilde_c[n] = (v[n][0] + v[n][1]) * qc
    delta_hat_2 = 0
    for n in range(1, x["T"]):
        z2_h = tuple(psi_hat[n][r] * (ytilde_h[n + 1][r] - ytilde_h[n - 1][r]) for r in range(5))
        z2_c = (psi_hat[n][0] + psi_hat[n][1]) * (ytilde_c[n + 1] - ytilde_c[n - 1])
        rh_int = sub(add(scale(M, sub(add(p[n + 1], p[n - 1]), scale(2, p[n]))), lint(p[n])),
                     scale(yn[n], ELL))
        rc_int = M * (yn[n + 1] - yn[n] + yn[n - 1]) - 81 * x["a"] * d - sum(
            ELL[r] * p[n][r] for r in range(5)
        )
        delta_hat_2 -= 4 * sum(rh_int[r] * z2_h[r] for r in range(5)) + rc_int * z2_c
    delta_hat_0 = integer(scale_int * d0s2)
    delta_hat_1 = integer(scale_int * d1si)
    require(delta_hat_2 == integer(scale_int * d2s0), "INTEGER_SECOND_ORDER_NOETHER")
    require(delta_hat_0 + delta_hat_1 + delta_hat_2 == 0, "INTEGER_SECOND_ORDER_NOETHER")


def tangent_integer_check2(x, psi, qp, epsilon, d0, d1, d2):
    d = x["D"]
    dn = 80 * (d ** 2) * qp
    v = [tuple(integer(qp * z) for z in row) for row in psi]
    pn = [tuple(integer(d * z) for z in row) for row in x["h"]]
    yn = [integer(d * z) for z in x["chi"]]
    psi_hat = [(0,) * 5 for _ in range(x["T"] + 1)]
    running = (0,) * 5
    for b in range(1, x["T"]):
        ab = integer(d * x["alpha"][b])
        lb = tuple(integer(d * z) for z in x["lam"][b])
        running = tuple(r + ab + z for r, z in zip(running, lb))
        psi_hat[b] = running
    ytilde_h = [(0,) * 5 for _ in range(x["T"] + 1)]
    ytilde_c = [0] * (x["T"] + 1)
    for n in range(1, x["T"]):
        qh = sub(pn[n + 1], pn[n - 1])
        qc = yn[n + 1] - yn[n - 1]
        ytilde_h[n] = had(v[n], qh)
        ytilde_c[n] = (v[n][0] + v[n][1]) * qc
    direction = combine(combine(d0, d1, F(epsilon)), d2, F(epsilon * epsilon))
    updated = move(x, direction)
    lifted = dict(x)
    for key in SCALARS:
        lifted[key] = [integer(dn * z) for z in x[key]]
    for key in VECTORS:
        lifted[key] = [tuple(integer(dn * z) for z in row) for row in x[key]]
    for n in range(1, x["T"]):
        inc_h = add(
            scale(40 * d * epsilon, ytilde_h[n]),
            scale(20 * (epsilon ** 2), had(psi_hat[n], sub(ytilde_h[n + 1], ytilde_h[n - 1]))),
        )
        inc_c = (
            20 * d * epsilon * ytilde_c[n]
            + 5 * (epsilon ** 2) * (psi_hat[n][0] + psi_hat[n][1]) * (ytilde_c[n + 1] - ytilde_c[n - 1])
        )
        lifted["h"][n] = add(lifted["h"][n], inc_h)
        lifted["chi"][n] += inc_c
        lifted["N"][n] = add(lifted["N"][n], scale(80 * (d ** 2), incidence(v[n])))
    for b in range(1, x["T"] + 1):
        dv = sub(v[b], v[b - 1])
        sv = sum(dv)
        lifted["alpha"][b] += 16 * (d ** 2) * sv
        lifted["lam"][b] = add(lifted["lam"][b], tuple(16 * (d ** 2) * (5 * z - sv) for z in dv))
    for key in SCALARS:
        require(all(F(z, dn) == w for z, w in zip(lifted[key], updated[key])), "INTEGER_TANGENT")
    for key in VECTORS:
        require(all(tuple(F(z, dn) for z in row) == w for row, w in zip(lifted[key], updated[key])),
                "INTEGER_TANGENT")
    require(all(sum(row) == 0 for row in updated["tau"] + updated["lam"]), "INTEGER_TANGENT")
    require(all(divergence(row) == (0,) * 5 for row in updated["p"]), "INTEGER_TANGENT")


def hat_vector_field(x, psi, epsilon=F(1)):
    d0 = gauge0(psi)
    d1 = generator(x, psi)
    d2 = generator2(x, psi)
    return combine(combine(d0, d1, F(epsilon)), d2, F(epsilon * epsilon))


def lie_commutator(x, psi, eta, epsilon=F(1)):
    """Exact state-space Lie bracket [hat_delta_psi, hat_delta_eta] z."""
    v_psi = hat_vector_field(x, psi, epsilon)
    v_eta = hat_vector_field(x, eta, epsilon)
    d_psi_eta = combine(
        hat_vector_field(move(x, v_psi, F(1)), eta, epsilon),
        hat_vector_field(move(x, v_psi, F(-1)), eta, epsilon),
        F(-1),
    )
    d_eta_psi = combine(
        hat_vector_field(move(x, v_eta, F(1)), psi, epsilon),
        hat_vector_field(move(x, v_eta, F(-1)), psi, epsilon),
        F(-1),
    )
    return move(zeros(x["T"]), combine(d_psi_eta, d_eta_psi, F(-1)), F(1, 2))


def commutator_residuals(x, psi, eta):
    """Closed formulas (5.4) for C_3(psi, eta; x, M) and C_4(psi, eta; x, M)."""
    psi_m = dressing(x)
    g_psi = generator(x, psi)
    g_eta = generator(x, eta)
    g_m_psi = generator(g_psi, psi_m)
    g_m_eta = generator(g_eta, psi_m)
    bare = combine(generator(g_psi, eta), generator(g_eta, psi), F(-1))
    cross_3 = combine(generator(g_m_psi, eta), generator(g_m_eta, psi), F(-1))
    c3 = combine(cross_3, generator(bare, psi_m), F(1))
    c4 = generator(cross_3, psi_m)
    return bare, c3, c4


def check_witnesses():
    unit = (F(1), F(0), F(0), F(0), F(0))
    edge0 = (F(1),) + (F(0),) * 9
    # 1. GLOBAL_NEIGHBOR_GRADIENT
    x = blank(d=40)
    x["h"][1] = tuple(F(v, 40) for v in (6, 11, 11, 6, 6))
    old = gradient(x)
    x["N"][1] = edge0
    new = gradient(x)
    require(sub(new["h"][2], old["h"][2]) == (F(29, 10368), F(29, 10368), 0, 0, 0), "NEIGHBOR_WITNESS")
    require(new["chi"][2] - old["chi"][2] == F(-17, 51840), "NEIGHBOR_WITNESS")
    off = dict(x)
    off["N"] = [(F(0),) * 10 for _ in range(6)]
    for key, r, expected in (("h", 0, F(29, 10368)), ("h", 1, F(29, 10368)), ("chi", None, F(-17, 51840))):
        d = zeros(5)
        d[key][2] = F(1) if r is None else tuple(int(i == r) for i in range(5))
        got = (action(move(x, d)) - action(move(x, d, -1))
               - action(move(off, d)) + action(move(off, d, -1))) / 2
        require(got == expected, "NEIGHBOR_WITNESS")

    # 2, 3, 4, 5, 6. SECOND_ORDER_SPLIT, OMIT_S2_DEFECT, OMIT_DELTA2_DEFECT,
    # THIRD_FOURTH_REMAINDERS, QUARTIC_CENTRAL_DEFECT, PURE_GAUGE_S2_COMPLETION,
    # OMIT_HOMOGENEOUS_LAPSE.
    x = blank()
    x["h"][3] = unit
    x["alpha"][3] = F(1)
    psi = [(F(0),) * 5 for _ in range(6)]
    psi[2] = psi[3] = unit
    d0, d1, d2 = gauge0(psi), generator(x, psi), generator2(x, psi)
    require((part_derivative(x, d0, 2), part_derivative(x, d1, 1), part_derivative(x, d2, 0))
            == (F(0), F(115, 324), F(-115, 324)), "REMAINDER_WITNESS")
    # Control: omitting delta_2 leaves 115/324
    require(part_derivative(x, d0, 2) + part_derivative(x, d1, 1) == F(115, 324), "CONTROL")
    d1s2 = part_derivative(x, d1, 2)
    d2si = part_derivative(x, d2, 1)
    w3 = d1s2 + d2si
    w4 = part_derivative(x, d2, 2)
    require((d1s2, d2si, w3, w4, w3 + w4)
            == (F(-1, 8), F(1, 4), F(1, 8), F(-115, 1296), F(47, 1296)), "REMAINDER_WITNESS")
    joint = combine(combine(d0, d1), d2)
    exact = directional4(x, joint)
    naive = (action(move(x, joint, 1)) - action(move(x, joint, -1))) / 2
    require(exact == F(47, 1296) and naive - exact == F(1, 32), "CENTRAL_WITNESS")
    pg = pure_gauge(x, d0)
    require(s2_action(pg) == F(115, 648)
            and action(pg) - auto_action(move(x, d1, -1)) == F(0), "FIELD_REDEFINITION")
    bad = dict(d0)
    bad["alpha"] = [F(0)] * 6
    require(part_derivative(x, bad, 1) + part_derivative(x, d1, 0) == F(-1, 10), "CONTROL")

    # Case B of SECOND_ORDER_SPLIT and OMIT_S2_DEFECT (alpha_2 = alpha_3 = 1)
    x_both = blank()
    x_both["h"][3] = unit
    x_both["alpha"][2] = F(1)
    x_both["alpha"][3] = F(1)
    d0_b, d1_b, d2_b = gauge0(psi), generator(x_both, psi), generator2(x_both, psi)
    split = (part_derivative(x_both, d0_b, 2),
             part_derivative(x_both, d1_b, 1),
             part_derivative(x_both, d2_b, 0))
    require(split == (F(115, 324), F(115, 324), F(-115, 162)) and sum(split) == 0,
            "REMAINDER_WITNESS")
    require(split[1] + split[2] == F(-115, 324), "CONTROL")

    # 7. OMIT_INTERACTION_CURRENT
    x = blank()
    x["h"][2] = unit
    x["chi"][3] = F(1)
    psi_cur = [(F(0),) * 5 for _ in range(6)]
    psi_cur[2] = unit
    d0_c, d1_c = gauge0(psi_cur), generator(x, psi_cur)
    require(part_derivative(x, d0_c, 1, False) + part_derivative(x, d1_c, 0) == F(-1, 1296),
            "CONTROL")

    # 8. DROP_COCLOSURE
    x = blank()
    x["p"][2] = edge0
    require(part_derivative(x, d0_c, 0) == -2, "CONTROL")

    # 9, 10. EXTENDED_COMMUTATOR_CANCELLATION, WRONG_DELTA2_ORDER,
    # THIRD_ORDER_COMMUTATOR_RESIDUAL, FIXED_MEAN_ESCAPE
    x = blank()
    x["h"] = [(F(1, 5),) * 5 for _ in range(6)]
    x["h"][4] = add(x["h"][4], ELL)
    x["alpha"][1] = F(1)
    x["alpha"][2] = F(-1)
    psi_nc = [(F(0),) * 5 for _ in range(6)]
    eta_nc = [(F(0),) * 5 for _ in range(6)]
    psi_nc[2], eta_nc[3] = ELL, ELL
    bare, c3, c4 = commutator_residuals(x, psi_nc, eta_nc)
    cross = combine(generator(generator(x, eta_nc), psi_nc),
                    generator(generator(x, psi_nc), eta_nc), F(-1))
    require(bare["h"][2] == (F(-1, 4), F(1, 4), 0, 0, 0), "COMMUTATOR")
    require(cross["h"][2] == (F(1, 4), F(-1, 4), 0, 0, 0), "COMMUTATOR")
    require(add(bare["h"][2], cross["h"][2]) == (0, 0, 0, 0, 0), "COMMUTATOR")
    # Reversing delta_2 operator order to G_psi G_(Psi[M]) x doubles the defect
    wrong_cross = combine(generator(generator(x, psi_nc), eta_nc),
                          generator(generator(x, eta_nc), psi_nc), F(-1))
    require(add(bare["h"][2], wrong_cross["h"][2]) == (F(-1, 2), F(1, 2), 0, 0, 0), "CONTROL")
    require(c3["h"][1] == (F(-1, 8), F(1, 8), 0, 0, 0) and c4["h"][1] == (0, 0, 0, 0, 0),
            "NONCLOSURE")
    full_comm = lie_commutator(x, psi_nc, eta_nc, F(1))
    require(full_comm["h"][1] == c3["h"][1], "NONCLOSURE")
    require(sum(generator(x, eta_nc)["h"][3]) == 1, "CONTROL")


def certificate():
    root = Path(__file__).resolve().parents[2]
    for name, size, sha in AUTHORITY:
        raw = (root / name).read_bytes()
        require(len(raw) == size and hashlib.sha256(raw).hexdigest() == sha, "AUTHORITY")
    for basis in VB:
        require(sum(basis) == 0 and lap(basis) == scale(F(1, M), lint(basis)), "INCIDENCE")
        require(lint(ladj(basis)) == scale(53605, basis), "INCIDENCE")
    for basis in KB:
        require(divergence(basis) == (0,) * 5, "INCIDENCE")
    require(tuple(row[4 + i] for i, row in enumerate(KB)) == (1,) * 6, "INCIDENCE")
    coords = coordinates(5)
    require(len(coords) == 133, "DOMAIN")
    grads_payload, second_order_payload = [], []
    counters = {k: 0 for k in (
        "GLOBAL_CONFIGURATIONS", "GLOBAL_VARIATIONS", "CONTINUITY_VERTICES",
        "CONSTRAINT_PROPAGATION_VERTICES", "INTEGER_CONTINUITY_VERTICES",
        "FIRST_ORDER_NOETHER", "SECOND_ORDER_NOETHER", "INTEGER_SECOND_ORDER_NOETHER",
        "DEFORMATION_CHECKS", "PURE_GAUGE_REDEFINITION_CHECKS",
        "INTEGER_SECOND_ORDER_TANGENT_CHECKS", "EXTENDED_COMMUTATOR_CHECKS",
    )}
    for a in (-1, 0, 1):
        for seed in (0, 1):
            x = fixture(a, seed)
            require(all(sum(v) == 0 for v in x["tau"] + x["lam"]), "DOMAIN")
            require(all(divergence(v) == (0,) * 5 for v in x["p"]), "DOMAIN")
            counters["GLOBAL_CONFIGURATIONS"] += 1
            grad1 = gradient(x, F(1))
            grad0 = gradient(x, F(0))
            for i, d in enumerate(coords):
                val1 = pairing(grad1, d)
                diff1 = (action(move(x, d, 1), F(1)) - action(move(x, d, -1), F(1))) / 2
                val0 = pairing(grad0, d)
                diff0 = (action(move(x, d, 1), F(0)) - action(move(x, d, -1), F(0))) / 2
                require(val1 == diff1 and val0 == diff0, "GLOBAL_GRADIENT")
                grads_payload.append(f"{a}|{seed}|{i}|{val1}\n")
                counters["GLOBAL_VARIATIONS"] += 1
            _, _, energy, flow, rhs = integer_records(x)
            for n in range(1, 5):
                rh, rc = residuals(x, n)
                qh = sub(x["h"][n + 1], x["h"][n - 1])
                qc = x["chi"][n + 1] - x["chi"][n - 1]
                cn = tuple((qh[r] * rh[r] + SIG[r] * qc * rc) / 2 for r in range(5))
                lhs = add(sub(density(x, n + 1), density(x, n)), divergence(current(x, n)))
                h_next = sub(scale(2, lap(x["tau"][n + 1])), project(density(x, n + 1)))
                h_curr = sub(scale(2, lap(x["tau"][n])), project(density(x, n)))
                m_flux = add(
                    scale(2, add(weighted(incidence(sub(x["tau"][n + 1], x["tau"][n]))), x["p"][n])),
                    current(x, n),
                )
                prop = sub(sub(divergence(m_flux), scale(2, divergence(x["p"][n]))), project(cn))
                for r in range(5):
                    require(lhs[r] == cn[r], "CONTINUITY")
                    require(h_next[r] - h_curr[r] == prop[r], "CONSTRAINT_PROPAGATION")
                    require(energy[n + 1][r] - energy[n][r] + divergence(flow[n])[r] == rhs[n][r],
                            "INTEGER_CONTINUITY")
                    counters["CONTINUITY_VERTICES"] += 1
                    counters["CONSTRAINT_PROPAGATION_VERTICES"] += 1
                    counters["INTEGER_CONTINUITY_VERTICES"] += 1
            params = parameters(a, seed)
            g_s2 = s2_gradient(x)
            for index, (psi, qp) in enumerate(params):
                d0 = gauge0(psi)
                d1 = generator(x, psi)
                d2 = generator2(x, psi)
                require(part_derivative(x, d0, 0) == 0, "AUXILIARY_GAUGE")
                d0si = part_derivative(x, d0, 1)
                d1s0 = part_derivative(x, d1, 0)
                require(d0si + d1s0 == 0, "NOETHER")
                counters["FIRST_ORDER_NOETHER"] += 1
                d0s2 = part_derivative(x, d0, 2)
                d1si = part_derivative(x, d1, 1)
                d2s0 = part_derivative(x, d2, 0)
                require(d0s2 == pairing(g_s2, d0), "SECOND_ORDER_NOETHER")
                require(d0s2 + d1si + d2s0 == 0, "SECOND_ORDER_NOETHER")
                counters["SECOND_ORDER_NOETHER"] += 1
                integer_second_order_noether_check(x, psi, qp, d0s2, d1si, d2s0)
                counters["INTEGER_SECOND_ORDER_NOETHER"] += 1
                w3 = part_derivative(x, d1, 2) + part_derivative(x, d2, 1)
                w4 = part_derivative(x, d2, 2)
                second_order_payload.append(
                    f"{a}|{seed}|{index}|{d0s2}|{d1si}|{d2s0}|{w3}|{w4}\n"
                )
                pg = pure_gauge(x, d0)
                for epsilon in (-1, 0, 1, 2):
                    direction = combine(combine(d0, d1, F(epsilon)), d2, F(epsilon * epsilon))
                    actual = directional4(x, direction, F(epsilon))
                    expected_rem = (epsilon ** 3) * w3 + (epsilon ** 4) * w4
                    require(actual == expected_rem, "DEFORMATION")
                    require(actual == pairing(gradient(x, F(epsilon)), direction), "DEFORMATION")
                    require(action(pg, F(epsilon)) == auto_action(move(x, d1, -F(epsilon))),
                            "FIELD_REDEFINITION")
                    tangent_integer_check2(x, psi, qp, epsilon, d0, d1, d2)
                    counters["DEFORMATION_CHECKS"] += 1
                    counters["PURE_GAUGE_REDEFINITION_CHECKS"] += 1
                    counters["INTEGER_SECOND_ORDER_TANGENT_CHECKS"] += 1
            for i in range(20):
                psi = params[i][0]
                for j in range(i + 1, 20):
                    eta = params[j][0]
                    bare, c3, c4 = commutator_residuals(x, psi, eta)
                    cross = combine(generator(generator(x, eta), psi),
                                    generator(generator(x, psi), eta), F(-1))
                    require(all(add(u, v) == (0,) * 5 for u, v in zip(bare["h"], cross["h"])),
                            "COMMUTATOR")
                    require(all(u + v == 0 for u, v in zip(bare["chi"], cross["chi"])),
                            "COMMUTATOR")
                    comm = lie_commutator(x, psi, eta, F(1))
                    form = combine(c3, c4, F(1))
                    require(comm["h"] == form["h"] and comm["chi"] == form["chi"], "COMMUTATOR")
                    for key in ("tau", "p", "alpha", "lam", "N"):
                        require(comm[key] == zeros(5)[key], "COMMUTATOR")
                    counters["EXTENDED_COMMUTATOR_CHECKS"] += 1
    expected = (6, 798, 120, 120, 120, 126, 126, 126, 504, 504, 504, 1140)
    require(tuple(counters.values()) == expected, "CERTIFICATE")
    check_witnesses()
    lines = ["CERTIFICATE=" + PROBE, "AUTHORITY_FILES=5"]
    lines += [f"{key}={value}" for key, value in counters.items()]
    lines += [
        "GLOBAL_S2_GRADIENT_SHA256=" + hashlib.sha256("".join(grads_payload).encode("ascii")).hexdigest(),
        "SECOND_ORDER_PAYLOAD_SHA256=" + hashlib.sha256("".join(second_order_payload).encode("ascii")).hexdigest(),
        "GLOBAL_NEIGHBOR_GRADIENT=29/10368,29/10368,0,0,0;-17/51840",
        "SECOND_ORDER_SPLIT=115/324,115/324,-115/162",
        "THIRD_FOURTH_REMAINDERS=1/8,-115/1296,47/1296",
        "QUARTIC_CENTRAL_DEFECT=1/32",
        "PURE_GAUGE_S2_COMPLETION=115/648;0",
        "EXTENDED_COMMUTATOR_CANCELLATION=-1/4,1/4,0,0,0;1/4,-1/4,0,0,0;0,0,0,0,0",
        "THIRD_ORDER_COMMUTATOR_RESIDUAL=-1/8,1/8,0,0,0",
        "NEGATIVE_CONTROLS=10",
        "CERTIFICATE_RESULT=PASS",
    ]
    require(len(lines) == 25, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        raw = certificate()
        child = subprocess.run(
            [sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(child.returncode == 0 and child.stderr == b"" and child.stdout == raw, "BREAKER_BYTES")
        sys.stdout.buffer.write(raw + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except Falsifier as exc:
        sys.stdout.buffer.write((f"FALSIFIER={exc}\nRESULT=FAIL\n").encode("ascii"))


if __name__ == "__main__":
    main()
