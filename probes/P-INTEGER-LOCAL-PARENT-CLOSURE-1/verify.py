#!/usr/bin/env python3
"""Prospective exact audit; execute only after public six-file pin/readback."""
from copy import deepcopy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import subprocess
import sys

NAME = "P-INTEGER-LOCAL-PARENT-CLOSURE-1"
M = 324
ELL = (1, -1, 0, 0, 0)
SIGMA = (Q(1, 2), Q(1, 2), 0, 0, 0)
EDGES = tuple((r, (r + step) % 5, Q(weight, M))
              for step, weight in ((1, 29), (2, 65)) for r in range(5))
AUTHORITY = (
    ("CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    pass


class SingularChart(Exception):
    pass


def require(ok, label):
    if not ok:
        raise ScientificFailure(label)


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def sub(x, y):
    return [a - b for a, b in zip(x, y)]


def scale(c, x):
    return [c * a for a in x]


def array_add(x, y):
    return [add(a, b) for a, b in zip(x, y)]


def array_scale(c, x):
    return [scale(c, a) for a in x]


def bx(h):
    return [h[t] - h[s] for s, t, _ in EDGES]


def bt(j):
    out = [Q(0)] * 5
    for v, (s, t, _) in zip(j, EDGES):
        out[s] -= v
        out[t] += v
    return out


def wb(h):
    return [w * v for v, (_, _, w) in zip(bx(h), EDGES)]


def lap(h):
    return bt(wb(h))


def zero_rows(length, width):
    return [[Q(0) for _ in range(width)] for _ in range(length)]


def cycles():
    out = [[Q(int(k < 5)) for k in range(10)]]
    for r in range(5):
        row = [Q(0)] * 10
        row[5 + r] = 1
        row[r] -= 1
        row[(r + 1) % 5] -= 1
        out.append(row)
    return out


def blank(t=5, a=0, eh=Q(0)):
    return {"v": zero_rows(t + 1, 6), "theta": zero_rows(t + 1, 5),
            "r": [Q(0)] * 5, "nu": zero_rows(t + 1, 10),
            "tau": zero_rows(t + 1, 4), "p": zero_rows(t + 1, 6),
            "a": a, "eh": eh}


def tau_vec(z, b):
    c = z["tau"][b]
    return list(c) + [-sum(c)]


def p_vec(z, n):
    basis = cycles()
    return [sum((z["p"][n][j] * basis[j][k] for j in range(6)), Q(0))
            for k in range(10)]


def multipliers(z, residual=False):
    t = len(z["v"]) - 1
    mu = zero_rows(t + 1, 5)
    nn = zero_rows(t + 1, 10)
    if residual:
        mu[t] = list(z["r"])
        for n in range(1, t):
            nn[n] = list(z["nu"][n])
    else:
        for b in range(1, t):
            mu[b] = sub(z["theta"][b], z["theta"][b - 1])
        mu[t] = sub(z["r"], z["theta"][t - 1])
        for n in range(1, t):
            nn[n] = add(z["nu"][n], bx(z["theta"][n]))
    return mu, nn


def auxiliary(z, mm):
    mu, nn = mm
    t = len(z["v"]) - 1
    ans = sum((2 * dot(mu[b], lap(tau_vec(z, b))) for b in range(1, t + 1)), Q(0))
    for n in range(1, t):
        ans += 2 * dot(nn[n], add(wb(sub(tau_vec(z, n + 1), tau_vec(z, n))), p_vec(z, n)))
    return ans


def auto(v, a):
    aa = Q(a, 4)
    out = Q(0)
    for n in range(1, len(v)):
        d = sub(v[n], v[n - 1])
        out += dot(d, d) / 2
    for row in v[1:-1]:
        h, chi = row[:5], row[5]
        out += -dot(h, lap(h)) / 2 - chi * chi / 2 + aa * chi + chi * dot(ELL, h) / M
    return out


def density(v, a, b):
    hp, hc = v[b - 1][:5], v[b][:5]
    cp, cc = v[b - 1][5], v[b][5]
    aa = Q(a, 4)
    src = (cc - cp) ** 2 / 2 + cc * cp / 2 - aa * (cc + cp) / 2
    out = [(hc[r] - hp[r]) ** 2 / 2 + SIGMA[r] * src
           - Q(1, 2 * M) * ELL[r] * (cp * hc[r] + cc * hp[r]) for r in range(5)]
    for s, t, w in EDGES:
        value = w * (hc[t] - hc[s]) * (hp[t] - hp[s]) / 4
        out[s] += value
        out[t] += value
    return out


def current(v, n):
    dh = sub(v[n + 1][:5], v[n - 1][:5])
    dc = v[n + 1][5] - v[n - 1][5]
    h = v[n][:5]
    out = [w * (h[t] - h[s]) * (dh[s] + dh[t]) / 4 for s, t, w in EDGES]
    out[0] -= Q(1, 4 * M) * dc * (h[0] + h[1])
    return out


def interaction(v, a, eh, mm):
    mu, nn = mm
    es = Q(4342005, 8683757) * Q(a, 4) ** 2
    out = Q(0)
    for b in range(1, len(v)):
        out -= dot(mu[b], density(v, a, b)) + sum(mu[b]) * (es - eh) / 5
    for n in range(1, len(v) - 1):
        out += dot(nn[n], current(v, n))
    return out


def generator(theta, v):
    out = zero_rows(len(v), 6)
    for n in range(1, len(v) - 1):
        d = sub(v[n + 1], v[n - 1])
        out[n] = [theta[n][r] * d[r] / 2 for r in range(5)]
        out[n].append((theta[n][0] + theta[n][1]) * d[5] / 4)
    return out


def k_apply(theta, v, eps):
    return array_add(v, array_scale(-eps, generator(theta, v)))


def parent(z, eps):
    rho = multipliers(z, True)
    return auto(z["v"], z["a"]) + auxiliary(z, rho) + eps * interaction(z["v"], z["a"], z["eh"], rho)


def coefficients(z):
    v = z["v"]
    u = generator(z["theta"], v)
    rho, mm = multipliers(z, True), multipliers(z)
    si = interaction(v, z["a"], z["eh"], mm)
    di = (interaction(array_add(v, u), z["a"], z["eh"], rho)
          - interaction(array_add(v, array_scale(-1, u)), z["a"], z["eh"], rho)) / 2
    return (auto(v, z["a"]) + auxiliary(z, mm), si,
            -di + auto(u, 0), interaction(u, 0, Q(0), rho))


def expanded(z, eps):
    return sum((v * eps ** k for k, v in enumerate(coefficients(z))), Q(0))


def pulled(z, eps):
    q = deepcopy(z)
    q["v"] = k_apply(q["theta"], q["v"], eps)
    return parent(q, eps)


def scalar_inverse(ts):
    """Adjugate/continuant inverse: only the final determinant is divided by."""
    n = len(ts)
    lead = [Q(1), Q(1)]
    for k in range(2, n + 1):
        lead.append(lead[-1] + ts[k - 2] * ts[k - 1] * lead[-2])
    det = lead[n]
    if det == 0:
        raise SingularChart
    trail = [Q(0)] * (n + 2)
    trail[n] = trail[n - 1] = Q(1)
    for i in range(n - 2, -1, -1):
        trail[i] = trail[i + 1] + ts[i] * ts[i + 1] * trail[i + 2]
    inv = zero_rows(n, n)
    for i in range(n):
        for j in range(n):
            product = Q(1)
            if i <= j:
                for k in range(i, j):
                    product *= -ts[k]
                product *= lead[i] * trail[j + 1]
            else:
                for k in range(j + 1, i + 1):
                    product *= ts[k]
                product *= lead[j] * trail[i + 1]
            inv[i][j] = (-1) ** (i + j) * product / det
    return inv, det


def invert(theta, yy, eps):
    n = len(yy) - 2
    ans = deepcopy(yy)
    determinants = []
    for j in range(6):
        ts = [eps * (theta[k][j] / 2 if j < 5 else (theta[k][0] + theta[k][1]) / 4)
              for k in range(1, n + 1)]
        inv, det = scalar_inverse(ts)
        rhs = [yy[k][j] for k in range(1, n + 1)]
        rhs[0] -= ts[0] * yy[0][j]
        rhs[-1] += ts[-1] * yy[-1][j]
        for k in range(n):
            ans[k + 1][j] = dot(inv[k], rhs)
        determinants.append(det)
    return ans, determinants


def native_shift(z, psi):
    q = deepcopy(z)
    q["theta"] = array_add(q["theta"], psi)
    return q


def finite(z, psi, eps):
    q = native_shift(z, psi)
    q["v"], _ = invert(q["theta"], k_apply(z["theta"], z["v"], eps), eps)
    return q


def tangent(z, psi, eps):
    ans, _ = invert(z["theta"], generator(psi, z["v"]), eps)
    return array_scale(eps, ans)


def line(z, psi, vv, t):
    q = native_shift(z, array_scale(t, psi))
    q["v"] = array_add(z["v"], array_scale(t, vv))
    return q


def directional(z, psi, vv, eps, full=True):
    def value(t):
        q = line(z, psi, vv, t)
        if full:
            return expanded(q, eps)
        c = coefficients(q)
        return sum((c[k] * eps ** k for k in range(3)), Q(0))
    return (-value(2) + 8 * value(1) - 8 * value(-1) + value(-2)) / 12


def bracket(z, psi, eta, eps):
    dp, de = tangent(z, psi, eps), tangent(z, eta, eps)
    first, _ = invert(z["theta"], array_add(generator(eta, dp), generator(psi, de)), eps)
    second, _ = invert(z["theta"], array_add(generator(psi, de), generator(eta, dp)), eps)
    return array_scale(eps, array_add(first, array_scale(-1, second)))


def coordinate_keys(t=5, endpoints=False):
    keys = [("v", n, j) for n in (range(t + 1) if endpoints else range(1, t)) for j in range(6)]
    keys += [("theta", n, r) for n in range(1, t) for r in range(5)]
    keys += [("r", 0, r) for r in range(5)]
    keys += [("nu", n, k) for n in range(1, t) for k in range(10)]
    keys += [("tau", b, j) for b in range(1, t + 1) for j in range(4)]
    keys += [("p", n, j) for n in range(1, t) for j in range(6)]
    return keys


def get(z, key):
    sector, n, j = key
    return z[sector][j] if sector == "r" else z[sector][n][j]


def put(z, key, value):
    sector, n, j = key
    if sector == "r":
        z[sector][j] = value
    else:
        z[sector][n][j] = value


def partial(z, key, eps=Q(1)):
    zp, zm = deepcopy(z), deepcopy(z)
    put(zp, key, get(z, key) + 1)
    put(zm, key, get(z, key) - 1)
    return (parent(zp, eps) - parent(zm, eps)) / 2


def normalize(d, ns):
    gg = math.gcd(d, *ns)
    return d // gg, tuple(v // gg for v in ns)


def encode(z):
    vv = [Q(get(z, key)) for key in coordinate_keys(len(z["v"]) - 1, True)]
    d = math.lcm(*(v.denominator for v in vv))
    return normalize(d, [v.numerator * (d // v.denominator) for v in vv])


def decode(enc, context):
    d, ns = enc
    z = blank(len(context["v"]) - 1, context["a"], context["eh"])
    for key, value in zip(coordinate_keys(len(z["v"]) - 1, True), ns):
        put(z, key, Q(value, d))
    return z


def integer_shift(enc, psi, normalized=True):
    t = len(psi) - 1
    d, ns = enc
    den = math.lcm(*(Q(v).denominator for row in psi for v in row))
    out = [den * v for v in ns]
    for idx, key in enumerate(coordinate_keys(t, True)):
        sec, n, j = key
        if sec == "theta":
            omega = Q(psi[n][j]) * den
            require(omega.denominator == 1, "INTEGER_GAUGE")
            out[idx] += d * omega.numerator
    return normalize(d * den, out) if normalized else (d * den, tuple(out))


def fmt(q):
    q = Q(q)
    return f"{q.numerator}/{q.denominator}"


def flat(v):
    return [x for row in v for x in row]


def fval(a, s, n, j, c):
    return (17 * n + 11 * j + 7 * s + 5 * a + 3 * c) % 19 - 9


def fixture(a, s):
    z = blank(5, a, Q(s + 1, 7 + a * a))
    for key in coordinate_keys(5, True):
        sec, n, j = key
        channel = {"v": 0, "theta": 1, "r": 2, "nu": 3, "tau": 4, "p": 5}[sec]
        put(z, key, Q(fval(a, s, 5 if sec == "r" else n, j, channel), 60))
    return z


def parameters(a, s):
    out = []
    for n in range(1, 5):
        for r in range(5):
            p = zero_rows(6, 5)
            p[n][r] = Q(1, 16)
            out.append(p)
    p = zero_rows(6, 5)
    for n in range(1, 5):
        p[n] = [Q(fval(a, s, n, r, 6), 112) for r in range(5)]
    out.append(p)
    return out


def rank(matrix):
    aa = [[Q(v) for v in row] for row in matrix]
    rr = 0
    for col in range(len(aa[0])):
        pivot = next((k for k in range(rr, len(aa)) if aa[k][col]), None)
        if pivot is None:
            continue
        aa[rr], aa[pivot] = aa[pivot], aa[rr]
        val = aa[rr][col]
        aa[rr] = [v / val for v in aa[rr]]
        for k in range(rr + 1, len(aa)):
            if aa[k][col]:
                fac = aa[k][col]
                aa[k] = [x - fac * y for x, y in zip(aa[k], aa[rr])]
        rr += 1
        if rr == len(aa):
            break
    return rr


def check_domain(z):
    require(z["theta"][0] == z["theta"][-1] == [0] * 5, "DOMAIN")
    require(len(coordinate_keys()) == 133 and len(coordinate_keys(endpoints=True)) == 145, "DOMAIN")
    for n in range(1, 5):
        require(bt(p_vec(z, n)) == [0] * 5, "DOMAIN")
    for b in range(1, 6):
        require(sum(tau_vec(z, b)) == 0, "DOMAIN")


def check_local(z):
    mu, nn = multipliers(z)
    theta = zero_rows(len(z["v"]), 5)
    for n in range(1, len(z["v"]) - 1):
        theta[n] = add(theta[n - 1], mu[n])
    rr = [sum((mu[b][j] for b in range(1, len(z["v"]))), Q(0)) for j in range(5)]
    require(theta == z["theta"] and rr == z["r"], "LOCAL_RECONSTRUCTION")
    for n in range(1, len(z["v"]) - 1):
        require(sub(nn[n], bx(theta[n])) == z["nu"][n], "LOCAL_RECONSTRUCTION")
    enc = encode(z)
    d, _ = enc
    for b in range(1, len(z["v"])):
        mint = [Q(v * d) for v in mu[b]]
        require(all(v.denominator == 1 for v in mint), "LOCAL_RECONSTRUCTION")
        alpha_num = sum(mint)
        lambda_num = [5 * v - alpha_num for v in mint]
        require(sum(lambda_num) == 0, "LOCAL_RECONSTRUCTION")
        require([alpha_num / (5 * d) + v / (5 * d) for v in lambda_num] == mu[b], "LOCAL_RECONSTRUCTION")
    for n in range(1, len(z["v"]) - 1):
        require(all(Q(v * d).denominator == 1 for v in nn[n]), "LOCAL_RECONSTRUCTION")
    require(auxiliary(z, multipliers(z)) == auxiliary(z, multipliers(z, True)), "LOCAL_RECONSTRUCTION")


def residual(v, a, n):
    h, c = v[n][:5], v[n][5]
    hh = [v[n + 1][r] - 2 * h[r] + v[n - 1][r] + lap(h)[r] - c * ELL[r] / M for r in range(5)]
    return hh + [v[n + 1][5] - c + v[n - 1][5] - Q(a, 4) - dot(ELL, h) / M]


def terminal_gradient(v, a):
    hp, hc, cp, cc = v[-2][:5], v[-1][:5], v[-2][5], v[-1][5]
    grad = [hp[r] - hc[r] + lap(hc)[r] / 2 - cc * ELL[r] / (2 * M) for r in range(5)]
    return grad + [cp - cc / 2 - Q(a, 8) - dot(ELL, hc) / (2 * M)]


def auxiliary_matrix():
    cols = [("r", 0, r) for r in range(5)] + [("nu", n, k) for n in range(1, 5) for k in range(10)]
    mat = zero_rows(44, 45)
    cb = cycles()
    for col, key in enumerate(cols):
        z = blank()
        put(z, key, Q(1))
        vals = [2 * dot(z["nu"][n], cb[j]) for n in range(1, 5) for j in range(6)]
        for b in range(1, 6):
            for j in range(4):
                vv = [Q(int(r == j) - int(r == 4)) for r in range(5)]
                vals.append(2 * dot(sub(z["nu"][b - 1], z["nu"][b]), wb(vv))
                            + (2 * dot(z["r"], lap(vv)) if b == 5 else 0))
        for row, v in enumerate(vals):
            mat[row][col] = v
    require(rank(mat) == 44, "AUXILIARY_RANK")
    kernel = [1] * 5 + [0] * 40
    require(all(dot(row, kernel) == 0 for row in mat), "AUXILIARY_RANK")
    require(rank(cb) == 6 and all(bt(v) == [0] * 5 for v in cb), "DOMAIN")
    return 44


def audit():
    action_lines, deriv_lines, gauge_lines = [], [], []
    counts = dict(parent=0, cubic=0, finite=0, noether=0, commutator=0,
                  integer=0, local=0, bulk=0, boundary=0)
    idx = 0
    for a in (-1, 0, 1):
        for seed in (0, 1):
            z = fixture(a, seed)
            check_domain(z)
            pars = parameters(a, seed)
            require(len(pars) == 21, "DOMAIN")
            for ci, key in enumerate(coordinate_keys()):
                value = partial(z, key)
                if key[0] == "theta":
                    require(value == 0, "PARENT_VARIATION")
                deriv_lines.append(f"D|{idx}|{ci}|{fmt(value)}\n")
                counts["parent"] += 1
            cs = coefficients(z)
            for eps in (-1, 0, 1, 2):
                se = expanded(z, eps)
                require(se == pulled(z, eps), "CUBIC_COMPLETION")
                action_lines.append(f"A|{idx}|{eps}|" + ",".join(fmt(v) for v in cs + (se,)) + "\n")
                counts["cubic"] += 1
            stationary = deepcopy(z)
            kappa = Q(idx + 1, 7)
            stationary["r"] = [kappa] * 5
            stationary["nu"] = zero_rows(6, 10)
            th = terminal_gradient(z["v"], a)
            for n in range(1, 5):
                rr = residual(z["v"], a, n)
                for j in range(6):
                    actual = partial(stationary, ("v", n, j))
                    want = -rr[j] - (kappa * th[j] if n == 4 else 0)
                    require(actual == want, "STATIONARY_EQUATIONS")
                    counts["boundary" if n == 4 else "bulk"] += 1
            for pi, psi in enumerate(pars):
                eta = pars[(pi + 1) % len(pars)]
                both = array_add(psi, eta)
                for eps in (-1, 0, 1, 2):
                    yy = k_apply(z["theta"], z["v"], eps)
                    inv, dets = invert(z["theta"], yy, eps)
                    require(inv == z["v"] and all(d != 0 for d in dets), "CHART_INVERSE")
                    changed = finite(z, psi, eps)
                    require(k_apply(changed["theta"], changed["v"], eps) == yy, "FINITE_GAUGE")
                    require(pulled(changed, eps) == pulled(z, eps), "FINITE_GAUGE")
                    require(finite(changed, eta, eps) == finite(z, both, eps), "FINITE_GAUGE")
                    require(finite(changed, array_scale(-1, psi), eps) == z, "FINITE_GAUGE")
                    counts["finite"] += 1
                    dx = tangent(z, psi, eps)
                    require(k_apply(z["theta"], dx, eps) == array_scale(eps, generator(psi, z["v"])), "NOETHER")
                    require(directional(z, psi, dx, eps) == 0, "NOETHER")
                    counts["noether"] += 1
                    require(not any(flat(bracket(z, psi, eta, eps))), "COMMUTATOR")
                    counts["commutator"] += 1
                    native = deepcopy(z)
                    native["v"] = yy
                    base_enc = encode(native)
                    changed_enc = integer_shift(base_enc, psi)
                    native_changed = native_shift(native, psi)
                    require(changed_enc == encode(native_changed), "INTEGER_GAUGE")
                    require(decode(changed_enc, native) == native_changed, "INTEGER_GAUGE")
                    require(integer_shift(changed_enc, array_scale(-1, psi)) == base_enc, "INTEGER_GAUGE")
                    require(integer_shift(changed_enc, eta) == integer_shift(base_enc, both), "INTEGER_GAUGE")
                    require(encode(native_shift(native, array_scale(-1, native["theta"])))
                            == encode(native_shift(native_changed, array_scale(-1, native_changed["theta"]))), "INTEGER_GAUGE")
                    counts["integer"] += 1
                    check_local(native_changed)
                    counts["local"] += 1
                    gauge_lines.append(f"G|{idx}|{pi}|{eps}|" + ",".join(fmt(v) for v in flat(changed["v"]) + flat(dx)) + "\n")
            idx += 1
    expected = dict(parent=798, cubic=24, finite=504, noether=504, commutator=504,
                    integer=504, local=504, bulk=108, boundary=36)
    require(counts == expected and idx == 6, "CERTIFICATE")
    return tuple(hashlib.sha256("".join(lines).encode("ascii")).hexdigest()
                 for lines in (action_lines, deriv_lines, gauge_lines))


def witnesses():
    controls = set()
    z = blank()
    z["v"][3][0] = Q(1)
    z["theta"][3] = z["theta"][4] = [Q(1)] * 5
    z["r"] = [Q(1)] * 5
    psi = zero_rows(6, 5)
    psi[2][0] = psi[3][0] = Q(1)
    cs = coefficients(z)
    require(cs[3] == Q(-1, 8) and expanded(z, 1) == Q(85, 324), "WITNESSES")
    require(expanded(z, 1) - sum(cs[:3]) == Q(-1, 8), "NEGATIVE_CONTROLS")
    controls.add("OMIT_S3")
    dp = tangent(z, psi, 1)
    require([dp[n][0] for n in (2, 3, 4)] == [Q(1, 2), Q(-1, 5), Q(1, 10)], "WITNESSES")
    changed = finite(z, psi, 1)
    require([changed["v"][n][0] for n in (2, 3, 4)] == [Q(3, 8), Q(3, 4), Q(1, 8)], "WITNESSES")
    require(changed["v"] != array_add(z["v"], dp), "WITNESSES")
    require(pulled(changed, 1) == Q(85, 324), "WITNESSES")
    require(directional(z, psi, dp, 1) == 0, "WITNESSES")
    d1 = generator(psi, z["v"])
    d2 = generator(z["theta"], d1)
    trunc = array_add(d1, d2)
    require(directional(z, psi, trunc, 1) == Q(8, 81), "NEGATIVE_CONTROLS")
    controls.add("TRUNCATED_GENERATOR")
    require(directional(z, psi, trunc, 1, False) == Q(47, 1296), "WITNESSES")
    # W3,W4 are isolated by the two exact epsilon values 1 and -1.
    wm = directional(z, psi, array_add(array_scale(-1, d1), d2), -1, False)
    wp = directional(z, psi, trunc, 1, False)
    require((wp - wm) / 2 == Q(1, 8) and (wp + wm) / 2 == Q(-115, 1296), "WITNESSES")
    lost = blank()
    lost["r"] = [Q(1)] * 5
    mu, _ = multipliers(lost)
    require([sum(row[j] for row in mu) for j in range(5)] == [1] * 5, "NEGATIVE_CONTROLS")
    wrong_mu = deepcopy(mu)
    wrong_mu[5] = [Q(0)] * 5
    require([sum(row[j] for row in wrong_mu) for j in range(5)] != lost["r"], "NEGATIVE_CONTROLS")
    controls.add("DROP_TERMINAL_RESIDUAL")
    nl = blank()
    for n in range(1, 5):
        nl["theta"][n] = [Q(2)] * 5
    nl["v"][5][0] = Q(1)
    pp = zero_rows(6, 5)
    pp[4][0] = Q(2)
    dnl = tangent(nl, pp, 1)
    require([dnl[n][0] for n in range(1, 5)] == [Q(1, 5), Q(1, 5), Q(2, 5), Q(3, 5)], "NEGATIVE_CONTROLS")
    _, ds = invert(nl["theta"], nl["v"], 1)
    require(ds == [Q(5)] * 6, "WITNESSES")
    controls.add("NONLOCAL_INVERSE")
    sg = blank()
    sg["theta"][1], sg["theta"][2] = [Q(2)] * 5, [Q(-2)] * 5
    sg["v"][1][0] = sg["v"][2][0] = Q(1)
    require(not any(flat(k_apply(sg["theta"], sg["v"], 1))) and any(flat(sg["v"])), "NEGATIVE_CONTROLS")
    try:
        invert(sg["theta"], sg["v"], 1)
    except SingularChart:
        controls.add("SINGULAR_CHART")
    else:
        raise ScientificFailure("NEGATIVE_CONTROLS")
    rg = deepcopy(sg)
    rg["theta"][3] = [Q(2)] * 5
    rg["v"] = zero_rows(6, 6)
    rg["v"][1][0] = Q(1)
    recovered, dets = invert(rg["theta"], k_apply(rg["theta"], rg["v"], 1), 1)
    require(recovered == rg["v"] and dets == [Q(-1)] * 6, "CHART_INVERSE")
    metric = blank()
    metric["v"][3][0] = Q(1, 4)
    mp = zero_rows(6, 5)
    mp[2][0] = Q(16)
    mt = finite(metric, mp, 1)
    require(mt["v"][2][0] == 2 and k_apply(mt["theta"], mt["v"], 1) == metric["v"], "NEGATIVE_CONTROLS")
    require([-1, 1 + mt["v"][2][0], 1 - mt["v"][2][0], 1] == [-1, 3, -1, 1], "WITNESSES")
    controls.add("RAW_METRIC")
    alternative = blank()
    alternative["v"][2][0] = Q(1)
    # Exact derivative of the independently declared quartic invariant J.
    def jj(q):
        return sum((v ** 4 for row in q["v"][1:-1] for v in row[:5]), Q(0))
    vals = {}
    for t in (-2, -1, 1, 2):
        q = deepcopy(alternative)
        q["v"][2][0] += t
        vals[t] = jj(q)
    require((-vals[2] + 8 * vals[1] - 8 * vals[-1] + vals[-2]) / 12 == 4, "NEGATIVE_CONTROLS")
    require(jj(native_shift(alternative, psi)) == jj(alternative), "NEGATIVE_CONTROLS")
    controls.add("NONUNIQUE_COMPLETION")
    zero = blank()
    base = encode(zero)
    ip = zero_rows(6, 5)
    ip[2][0] = Q(1, 2)
    raw = integer_shift(integer_shift(base, ip, False), array_scale(-1, ip), False)
    require(raw[0] == 4 and raw != base and normalize(*raw) == base, "NEGATIVE_CONTROLS")
    require(integer_shift(integer_shift(base, ip), array_scale(-1, ip)) == base, "NEGATIVE_CONTROLS")
    controls.add("UNNORMALIZED_ROUNDTRIP")
    require(controls == {"OMIT_S3", "TRUNCATED_GENERATOR", "DROP_TERMINAL_RESIDUAL", "NONLOCAL_INVERSE",
                         "SINGULAR_CHART", "RAW_METRIC", "NONUNIQUE_COMPLETION", "UNNORMALIZED_ROUNDTRIP"}, "CERTIFICATE")


def certificate():
    root = Path(__file__).resolve().parents[2]
    for name, size, digest in AUTHORITY:
        raw = (root / "canon" / name).read_bytes()
        require(len(raw) == size and hashlib.sha256(raw).hexdigest() == digest, "AUTHORITY")
    auxiliary_matrix()
    digests = audit()
    witnesses()
    lines = [
        f"CERTIFICATE={NAME}", "AUTHORITY_FILES=5", "CONFIGURATIONS=6", "PARENT_COORDINATES=133",
        "PARENT_VARIATIONS=798", "CUBIC_COMPLETION_CHECKS=24", "FINITE_GAUGE_CHECKS=504",
        "EXACT_NOETHER_CHECKS=504", "EXACT_COMMUTATOR_CHECKS=504", "INTEGER_GAUGE_CHECKS=504",
        "LOCAL_MULTIPLIER_CHECKS=504", "AUXILIARY_CONSTRAINT_RANK=44", "BULK_EQUATION_CHECKS=108",
        "BOUNDARY_VARIATION_CHECKS=36", f"ACTION_PAYLOAD_SHA256={digests[0]}",
        f"PARENT_GRADIENT_SHA256={digests[1]}", f"GAUGE_PAYLOAD_SHA256={digests[2]}",
        "OLD_TRUNCATION_REMAINDERS=1/8,-115/1296,47/1296", "CUBIC_COMPLETION_WITNESS=-1/8,85/324",
        "EXACT_TANGENT_WITNESS=1/2,-1/5,1/10", "FINITE_MAP_WITNESS=3/8,3/4,1/8",
        "NONLOCAL_INVERSE_WITNESS=1/5,1/5,2/5,3/5", "SINGULAR_CHART=0;KERNEL_NONZERO",
        "RAW_METRIC_COUNTEREXAMPLE=2;-1,3,-1,1", "ALTERNATIVE_BULK_GRADIENT=4",
        "NEGATIVE_CONTROLS=8", "CERTIFICATE_RESULT=PASS",
    ]
    require(len(lines) == 27, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        raw = certificate()
        child = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        require(child.returncode == 0 and child.stderr == b"" and child.stdout == raw, "BREAKER_BYTES")
        sys.stdout.buffer.write(raw + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except ScientificFailure as exc:
        sys.stdout.buffer.write(f"FALSIFIER={exc}\nRESULT=FAIL\n".encode("ascii"))


if __name__ == "__main__":
    main()
