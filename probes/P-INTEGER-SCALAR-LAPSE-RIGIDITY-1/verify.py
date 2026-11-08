#!/usr/bin/env python3
"""Exact primary audit. Scientific execution requires the public six-file pin.

The implementation uses Fraction matrix powers, formal polynomial convolution,
and direct differentiation of the rational and polynomial generating functions.
It neither imports nor reads any other scientific program.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial, lcm
from pathlib import Path
import subprocess
import sys

N = 6
ZERO = Q(0)
ONE = Q(1)
AUTHORITY = (
    ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class GateFailure(Exception):
    pass


def require(condition, tag):
    if not condition:
        raise GateFailure(tag)


def zm(n, m=None):
    return tuple(tuple(ZERO for _ in range(n if m is None else m)) for _ in range(n))


def eye(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def mt(a):
    return tuple(zip(*a))


def ma(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def ms(a, s):
    return tuple(tuple(s * x for x in row) for row in a)


def mm(a, b):
    out = [[ZERO] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x * y
    return tuple(tuple(row) for row in out)


def inv(a):
    n = len(a)
    rows = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [x / scale for x in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[col])]
    return tuple(tuple(row[n:]) for row in rows)


def va(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vs(a, s):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), ZERO)


def mv(a, v):
    return tuple(dot(row, v) for row in a)


def quad(a, v):
    return dot(v, mv(a, v))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def block(a, b, c, d):
    return tuple(tuple(ar) + tuple(br) for ar, br in zip(a, b)) + tuple(
        tuple(cr) + tuple(dr) for cr, dr in zip(c, d))


def upper_blocks(m):
    return tuple(row[:6] for row in m[:6]), tuple(row[6:] for row in m[:6])


def flat(a):
    return tuple(x for row in a for x in row)


def csv(a):
    return ",".join(str(x) for x in a)


def series_mul(a, b, order=N):
    out = []
    for k in range(order + 1):
        acc = zm(len(a[0]), len(b[0][0]))
        for j in range(k + 1):
            acc = ma(acc, mm(a[j], b[k - j]))
        out.append(acc)
    return out


def series_inverse(a, order=N):
    out = [inv(a[0])]
    for k in range(1, order + 1):
        acc = zm(len(a[0]))
        for j in range(1, k + 1):
            acc = ma(acc, mm(a[j], out[k - j]))
        out.append(ms(mm(out[0], acc), -ONE))
    return out


def generating_series(mseries):
    ub = [upper_blocks(m) for m in mseries]
    u = [pair[0] for pair in ub]
    b = [pair[1] for pair in ub]
    e = series_inverse(b)
    a = series_mul(e, u)
    return u, b, e, a


def ldl_pivots(a):
    n = len(a)
    lower = [[ZERO] * n for _ in range(n)]
    pivots = []
    for i in range(n):
        lower[i][i] = ONE
        d = a[i][i] - sum((lower[i][k] ** 2 * pivots[k] for k in range(i)), ZERO)
        require(d > 0, "F_CARRIER")
        pivots.append(d)
        for j in range(i + 1, n):
            lower[j][i] = (a[j][i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)), ZERO)) / d
    ld = tuple(tuple(lower[i][j] * pivots[j] for j in range(n)) for i in range(n))
    require(mm(ld, mt(tuple(tuple(row) for row in lower))) == a, "F_CARRIER")
    return pivots


def fixture(seed, n, r):
    return Q(((seed + 2) * (n + 1) * (r + 3) + (n - r) ** 2) % 17 - 8, seed + 2)


def zeros_field(tmax):
    return tuple((ZERO,) * 6 for _ in range(tmax + 1))


def field_add(a, b):
    return tuple(va(x, y) for x, y in zip(a, b))


def field_scale(a, s):
    return tuple(vs(x, s) for x in a)


def field_dot(a, b):
    return sum((dot(x, y) for x, y in zip(a, b)), ZERO)


def power_derivative(a, k, da):
    return ZERO if k == 0 else k * a ** (k - 1) * da


def audit():
    root = Path(__file__).resolve().parents[2]
    for name, count, digest in AUTHORITY:
        try:
            data = (root / name).read_bytes()
        except OSError:
            raise GateFailure("F_AUTHORITY") from None
        require(len(data) == count and sha256(data).hexdigest() == digest, "F_AUTHORITY")
    payload = []
    controls = [False] * 8
    counts = dict(states=0, bonds=0, ward=0, integer=0, mixed=0, composition=0, energy=0)

    # Incidence construction is independent of the displayed circulant formula.
    lap = [[ZERO] * 5 for _ in range(5)]
    for jump, numerator in ((1, 29), (2, 65)):
        for tail in range(5):
            head = (tail + jump) % 5
            incidence = [ZERO] * 5
            incidence[tail], incidence[head] = -ONE, ONE
            for i in range(5):
                for j in range(5):
                    lap[i][j] += Q(numerator, 324) * incidence[i] * incidence[j]
    lap = tuple(tuple(row) for row in lap)
    explicit = tuple(tuple(Q(188 if i == j else -29 if (i-j) % 5 in (1, 4) else -65, 324)
                           for j in range(5)) for i in range(5))
    require(lap == explicit and mt(lap) == lap, "F_CARRIER")
    ell = (ONE, -ONE, ZERO, ZERO, ZERO)
    vmat = tuple(tuple(lap[i]) + (-ell[i] / 324,) for i in range(5)) + (
        tuple(-x / 324 for x in ell) + (ONE,),)
    i6, z6, i12 = eye(6), zm(6), eye(12)
    c = ma(i6, ms(vmat, -Q(1, 2)))
    c2, c3 = mm(c, c), mm(mm(c, c), c)
    d = ma(i6, ms(c2, -ONE))
    k = block(z6, i6, ms(d, -ONE), z6)
    m0 = block(c, i6, ms(d, -ONE), c)
    jform = block(z6, i6, ms(i6, -ONE), z6)
    gform = block(d, z6, z6, i6)
    uniform = (ONE, ONE, ONE, ONE, ONE, ZERO)
    zvec = (ZERO,) * 6
    require(all(mt(a) == a for a in (vmat, c, d)), "F_CARRIER")
    require(mm(mm(mt(m0), jform), m0) == jform, "F_CARRIER")
    require(mm(mm(mt(m0), gform), m0) == gform, "F_CARRIER")
    require(mm(m0, k) == mm(k, m0), "F_CARRIER")
    require(trace(d) == Q(163223, 52488) and trace(mm(k, k)) == -Q(163223, 26244), "F_CARRIER")
    require(mv(d, uniform) == zvec, "F_CARRIER")
    basis = tuple(tuple(Q(i == j) - Q(i == 4) if j < 4 else Q(i == 5)
                        for j in range(5)) for i in range(6))
    pivots = ldl_pivots(mm(mm(mt(basis), d), basis))
    payload.append("P|" + csv(pivots) + "\n")

    powers = [i12]
    for degree in range(1, N + 1):
        powers.append(mm(powers[-1], k))
    rseries = [ms(powers[degree], Q(1, factorial(degree))) for degree in range(N + 1)]
    mseries = [mm(m0, r) for r in rseries]
    useries, bseries, eseries, aseries = generating_series(mseries)
    for form in (jform, gform):
        contracted = series_mul([mm(mt(r), form) for r in rseries], rseries)
        require(contracted == [form] + [zm(12)] * N, "F_SERIES")
    for i in range(N + 1):
        for j in range(N + 1 - i):
            require(mm(rseries[i], rseries[j]) == ms(rseries[i+j], Q(comb(i+j, i))), "F_SERIES")
            counts["composition"] += 1
    u2, b2 = series_mul(useries, useries), series_mul(bseries, bseries)
    ae, e2 = series_mul(aseries, eseries), series_mul(eseries, eseries)
    for degree in range(N + 1):
        require(ma(u2[degree], mm(d, b2[degree])) == (i6 if degree == 0 else z6), "F_SERIES")
        require(mt(eseries[degree]) == eseries[degree] and mt(aseries[degree]) == aseries[degree], "F_SERIES")
        if degree < N:
            require(ms(eseries[degree+1], Q(degree+1)) == ms(ae[degree], -ONE), "F_SERIES")
            require(ms(aseries[degree+1], Q(degree+1)) == ms(e2[degree], -ONE), "F_SERIES")
    for label, series in (("R", rseries), ("E", eseries), ("A", aseries)):
        for degree, matrix in enumerate(series):
            payload.append(f"{label}|{degree}|" + csv(flat(matrix)) + "\n")

    def bond_coefficients(q, bigq):
        return tuple((quad(aa, q) + quad(aa, bigq)) / 2 - dot(q, mv(ee, bigq))
                     for aa, ee in zip(aseries, eseries))

    def action(x, alpha):
        result = [ZERO] * (N + 1)
        result[0] = (quad(vmat, x[0]) + quad(vmat, x[-1])) / 4
        for bond in range(1, len(x)):
            for degree, coeff in enumerate(bond_coefficients(x[bond-1], x[bond])):
                result[degree] += alpha[bond-1] ** degree * coeff
        return tuple(result)

    def gradient(x, alpha, degree, da=None):
        out = list(zeros_field(len(x)-1))
        aa, ee = aseries[degree], eseries[degree]
        for n in range(1, len(x)-1):
            left = va(mv(aa, x[n]), vs(mv(ee, x[n-1]), -ONE))
            right = va(mv(aa, x[n]), vs(mv(ee, x[n+1]), -ONE))
            if da is None:
                facl, facr = alpha[n-1] ** degree, alpha[n] ** degree
            else:
                facl = power_derivative(alpha[n-1], degree, da[n-1])
                facr = power_derivative(alpha[n], degree, da[n])
            out[n] = va(vs(left, facl), vs(right, facr))
        return tuple(out)

    def skew(t, alpha, field):
        out = list(zeros_field(len(field)-1))
        for n in range(1, len(field)-1):
            right = vs(field[n+1], alpha[n] * (t[n] + t[n+1]) / 8)
            left = vs(field[n-1], -alpha[n-1] * (t[n-1] + t[n]) / 8)
            out[n] = va(left, right)
        return tuple(out)

    def generator(x, alpha, t, degree, adjusted=False, da=None):
        out = list(zeros_field(len(x)-1))
        if degree == 0:
            return tuple(out)
        j = degree - 1
        for n in range(1, len(x)-1):
            pl = va(mv(aseries[j], x[n]), vs(mv(eseries[j], x[n-1]), -ONE))
            pr = va(mv(eseries[j], x[n+1]), vs(mv(aseries[j], x[n]), -ONE))
            if da is None:
                al, ar = alpha[n-1] ** j, alpha[n] ** j
            else:
                al = power_derivative(alpha[n-1], j, da[n-1])
                ar = power_derivative(alpha[n], j, da[n])
            out[n] = vs(va(vs(pl, al), vs(pr, ar)), t[n] / 2)
        out = tuple(out)
        if adjusted and degree >= 2:
            if da is None:
                correction = skew(t, alpha, gradient(x, alpha, degree-2))
            else:
                correction = field_add(skew(t, da, gradient(x, alpha, degree-2)),
                                       skew(t, alpha, gradient(x, alpha, degree-2, da)))
            out = field_add(out, correction)
        return out

    for tmax in (3, 4, 5):
        for seed in (1, 2):
            x = tuple(tuple(fixture(seed, n, r) for r in range(6)) for n in range(tmax+1))
            alpha = tuple(fixture(seed, b, 6) for b in range(1, tmax+1))
            counts["states"] += 1
            bondjets = []
            for b in range(1, tmax+1):
                q, bigq = x[b-1], x[b]
                coeff = bond_coefficients(q, bigq)
                bondjets.append(coeff)
                hbond = (dot(q, q) + dot(bigq, bigq)) / 2 - dot(q, mv(c, bigq))
                kbond = dot(va(mv(c, bigq), vs(q, -ONE)), va(bigq, vs(mv(c, q), -ONE)))
                tbond = -quad(ma(i6, ms(c2, Q(2))), q) - quad(ma(i6, ms(c2, Q(2))), bigq)
                tbond += dot(q, mv(ma(ms(c, Q(5)), c3), bigq))
                expected = ((quad(c, q)+quad(c, bigq))/2-dot(q, bigq), -hbond, kbond/2, tbond/6)
                require(coeff[:4] == expected, "F_JET")
                counts["bonds"] += 1
            scoeff = action(x, alpha)
            autonomous = sum((dot(va(x[b], vs(x[b-1], -ONE)), va(x[b], vs(x[b-1], -ONE)))/2
                              for b in range(1, tmax+1)), ZERO)
            autonomous -= sum((quad(vmat, x[n])/2 for n in range(1, tmax)), ZERO)
            require(scoeff[0] == autonomous, "F_JET")
            payload.append(f"S|{tmax}|{seed}|" + csv(scoeff) + "\n")
            gradients = [gradient(x, alpha, j) for j in range(N+1)]
            parameters = [tuple(Q(n == i) for n in range(tmax+1)) for i in range(1, tmax)]
            parameters.append(tuple(fixture(seed+2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax+1)))
            for index, t in enumerate(parameters):
                da = tuple(t[b]-t[b-1] for b in range(1, tmax+1))
                pwork = tuple(sum((power_derivative(alpha[b], j, da[b]) * bondjets[b][j]
                                   for b in range(tmax)), ZERO) for j in range(N+1))
                raw = [generator(x, alpha, t, j) for j in range(N+1)]
                adjusted = [generator(x, alpha, t, j, True) for j in range(N+1)]
                rawwork = tuple(sum((field_dot(gradients[j], raw[k-j]) for j in range(k+1)), ZERO)
                                for k in range(N+1))
                adjwork = tuple(sum((field_dot(gradients[j], adjusted[k-j]) for j in range(k+1)), ZERO)
                                for k in range(N+1))
                require(all(pwork[j]+rawwork[j] == pwork[j]+adjwork[j] == 0 for j in range(N+1)), "F_WARD")
                require(all(adjwork[j]-rawwork[j] == 0 for j in range(N+1)), "F_WARD")
                # Independent displayed jets, including the predecessor's Xhom.
                jet1, jet2, jet3, grad_i = [list(zeros_field(tmax)) for _ in range(4)]
                for n in range(1, tmax):
                    jet1[n] = vs(va(x[n+1], vs(x[n-1], -ONE)), t[n]/2)
                    left = vs(va(x[n], vs(mv(c, x[n-1]), -ONE)), -alpha[n-1])
                    right = vs(va(x[n], vs(mv(c, x[n+1]), -ONE)), alpha[n])
                    jet2[n] = vs(va(left, right), t[n]/2)
                    left3 = va(vs(mv(c, x[n]), Q(2)), vs(mv(ma(i6, c2), x[n-1]), -ONE))
                    right3 = va(mv(ma(i6, c2), x[n+1]), vs(mv(c, x[n]), -Q(2)))
                    jet3[n] = vs(va(vs(left3, alpha[n-1]**2), vs(right3, alpha[n]**2)), t[n]/4)
                    grad_i[n] = va(left, vs(right, -ONE))
                require(raw[1:4] == [tuple(jet1), tuple(jet2), tuple(jet3)], "F_JET")
                require(gradients[1] == tuple(grad_i), "F_JET")
                require(adjusted[1] == tuple(jet1), "F_JET")
                require(adjusted[2] == field_add(tuple(jet2), skew(t, alpha, gradients[0])), "F_JET")
                require(adjusted[3] == field_add(tuple(jet3), skew(t, alpha, tuple(grad_i))), "F_JET")
                for degree in range(1, N+1):
                    values = (pwork[degree], rawwork[degree], adjwork[degree])
                    denominator = lcm(*(value.denominator for value in values))
                    cleared = tuple(value * denominator for value in values)
                    require(all(value.denominator == 1 for value in cleared), "F_INTEGER")
                    require(cleared[0]+cleared[1] == cleared[0]+cleared[2] == 0, "F_INTEGER")
                    counts["integer"] += 1
                # Deleting S_j removes its degree-j parameter derivative.
                # Its field gradient first contributes at degree j+1, since
                # every field generator starts at degree one.
                controls[0] |= adjwork[2] != 0
                controls[1] |= adjwork[3] != 0
                counts["ward"] += 1
                payload.append(f"W|{tmax}|{seed}|{index}|" + csv(pwork) + "|" + csv(rawwork) + "|" + csv(adjwork) + "\n")

    xlocal = tuple(tuple(fixture(1, n, r) for r in range(6)) for n in range(6))
    a0 = (ZERO,) * 5
    s0 = action(xlocal, a0)
    units = [tuple(Q(i == j) for j in range(5)) for i in range(5)]
    singles = [action(xlocal, unit) for unit in units]
    for i in range(5):
        for j in range(i+1, 5):
            pair = action(xlocal, va(units[i], units[j]))
            for degree in range(2, N+1):
                mixed = pair[degree]-singles[i][degree]-singles[j][degree]+s0[degree]
                require(mixed == 0, "F_LOCALITY")
                payload.append(f"L|{i}|{j}|{degree}|{mixed}\n")
                counts["mixed"] += 1

    def cayley(s):
        inverse = inv(ma(i12, ms(k, -s/2)))
        rc = mm(inverse, ma(i12, ms(k, s/2)))
        derivative = mm(mm(inverse, ms(k, Q(1, 2))), ma(rc, i12))
        return rc, mm(m0, rc), mm(m0, derivative)

    def rational_coefficients(s):
        rc, mc, mdot = cayley(s)
        u, b = upper_blocks(mc)
        udot, bdot = upper_blocks(mdot)
        e = inv(b)
        edot = ms(mm(mm(e, bdot), e), -ONE)
        a = mm(e, u)
        adot = ma(mm(edot, u), mm(e, udot))
        return a, e, adot, edot

    def action_derivative(q, bigq, adot, edot):
        return (quad(adot, q)+quad(adot, bigq))/2-dot(q, mv(edot, bigq))

    cayley_values = {}
    for s in (Q(-1, 2), ZERO, Q(1, 2), ONE, Q(2)):
        rc, mc, mdot = cayley(s)
        cayley_values[s] = (rc, mc)
        require(mm(mm(mt(rc), jform), rc) == jform, "F_RATIONAL")
        require(mm(mm(mt(rc), gform), rc) == gform, "F_RATIONAL")
        require(mm(mm(mt(mc), jform), mc) == jform and mm(mm(mt(mc), gform), mc) == gform, "F_RATIONAL")
        require(mm(rc, cayley(-s)[0]) == i12 and mm(rc, m0) == mm(m0, rc), "F_RATIONAL")
        ecden = ma(i6, ms(d, s*s/4))
        nc = ma(ma(i6, ms(c, s)), ms(d, -s*s/4))
        numerator = ma(ma(c, ms(d, -s)), ms(mm(c, d), -s*s/4))
        upper, right = upper_blocks(mc)
        require(right == mm(nc, inv(ecden)) and upper == mm(numerator, inv(ecden)), "F_RATIONAL")
        aa, ee, adot, edot = rational_coefficients(s)
        require(ee == mm(ecden, inv(nc)) and aa == mm(numerator, inv(nc)), "F_RATIONAL")
        effective = block(inv(ecden), z6, z6, inv(ecden))
        require(mm(mdot, inv(mc)) == mm(k, effective), "F_RATIONAL")
        payload.append(f"C|{s}|" + csv(flat(rc)) + "|" + csv(flat(mc)) + "\n")
    denominator_series = [i12, ms(k, -Q(1, 2))] + [zm(12)] * (N-1)
    numerator_series = [i12, ms(k, Q(1, 2))] + [zm(12)] * (N-1)
    rcseries = series_mul(series_inverse(denominator_series), numerator_series)
    _, _, ecseries, acseries = generating_series([mm(m0, r) for r in rcseries])
    require(ecseries[:3] == eseries[:3] and acseries[:3] == aseries[:3], "F_RATIONAL")
    rc1, mc1 = cayley_values[ONE]
    rc2 = cayley_values[Q(2)][0]
    defect = ma(mm(rc1, rc1), ms(rc2, -ONE))
    require(defect != zm(12), "F_RATIONAL")
    free_p = zvec + uniform
    require(mv(rc1, free_p) == uniform + uniform, "F_RATIONAL")
    require(mv(mm(rc1, rc1), free_p) == vs(uniform, Q(2)) + uniform, "F_RATIONAL")
    require(mv(rc2, free_p) == vs(uniform, Q(2)) + uniform, "F_RATIONAL")
    controls[3] = defect != zm(12)

    echi = (ZERO,) * 5 + (ONE,)
    phase1 = zvec + echi
    phases = [mv(inv(mc1), phase1), phase1, mv(m0, phase1)]
    phases.append(mv(m0, phases[-1]))
    xc = tuple(z[:6] for z in phases)
    local_coeff = [rational_coefficients(s) for s in (ONE, ZERO, ZERO)]
    for n in (1, 2):
        al, el, _, _ = local_coeff[n-1]
        ar, er, _, _ = local_coeff[n]
        gradient_c = va(va(mv(al, xc[n]), vs(mv(el, xc[n-1]), -ONE)),
                        va(mv(ar, xc[n]), vs(mv(er, xc[n+1]), -ONE)))
        require(gradient_c == zvec, "F_STATIONARY")
    derivatives = [action_derivative(xc[b], xc[b+1], local_coeff[b][2], local_coeff[b][3]) for b in range(3)]
    stationary_residual = derivatives[0] - derivatives[1]
    predicted_residual = (ONE-dot(echi, mv(inv(ma(i6, ms(d, Q(1, 4)))), echi)))/2
    require(stationary_residual == predicted_residual and stationary_residual > 0, "F_RATIONAL")
    payload.append("CW|" + str(stationary_residual) + "\n")
    controls[4] = stationary_residual != 0

    def energy(z):
        return (dot(z[6:], z[6:])+quad(d, z[:6]))/2

    u = (ONE, ZERO, -ONE, ZERO, ZERO, ZERO)
    phase = zvec + u
    for n in range(9):
        h = energy(phase)
        require(h == 1, "F_STATIONARY")
        payload.append(f"EN|{n}|" + csv(phase) + "|" + str(h) + "\n")
        counts["energy"] += 1
        phase = mv(m0, phase)
    static_phase = uniform + zvec
    require(mv(m0, static_phase) == static_phase and mv(k, static_phase) == (ZERO,)*12, "F_STATIONARY")
    _, mcminus, _ = cayley(-ONE)
    require(mv(upper_blocks(mcminus)[1], uniform) == zvec, "F_STATIONARY")
    require(mm(cayley(-ONE)[0], rc1) == i12, "F_STATIONARY")
    require(mv(mm(k, k), static_phase) == (ZERO,)*12 and mv(mm(k, k), free_p) == (ZERO,)*12, "F_STATIONARY")
    require(mv(bseries[0], uniform) == uniform and mv(bseries[1], uniform) == uniform, "F_STATIONARY")
    require(all(mv(bseries[j], uniform) == zvec for j in range(2, N+1)), "F_STATIONARY")
    require(va(mv(bseries[0], uniform), vs(mv(bseries[1], uniform), -ONE)) == zvec, "F_STATIONARY")
    lapse_residual = action_derivative(zvec, u, aseries[1], eseries[1])
    require(lapse_residual == -energy(zvec+u) == -ONE and lapse_residual+ONE == 0, "F_STATIONARY")
    controls[7] = lapse_residual == -ONE and lapse_residual+ONE == 0

    # Differentiate the actual generator: parameter derivative plus the
    # convolution of its linear field Jacobian with the other vector field.
    xw = list(zeros_field(4))
    xw[3] = u
    xw = tuple(xw)
    aw = (ZERO, ZERO, ONE, ZERO)
    tw = (ZERO, ONE, ZERO, ZERO, ZERO)
    sw = (ZERO, ZERO, ONE, ZERO, ZERO)
    dt = tuple(tw[b]-tw[b-1] for b in range(1, 5))
    ds = tuple(sw[b]-sw[b-1] for b in range(1, 5))

    def bracket(degree, adjusted):
        value = field_add(generator(xw, aw, sw, degree, adjusted, dt),
                          field_scale(generator(xw, aw, tw, degree, adjusted, ds), -ONE))
        for j in range(1, degree):
            xt = generator(xw, aw, tw, j, adjusted)
            xs = generator(xw, aw, sw, j, adjusted)
            value = field_add(value, generator(xt, aw, sw, degree-j, adjusted))
            value = field_add(value, field_scale(generator(xs, aw, tw, degree-j, adjusted), -ONE))
        return value

    raw2, adj2, raw3, adj3 = bracket(2, False), bracket(2, True), bracket(3, False), bracket(3, True)
    expected_raw2, expected_raw3, expected_adj3 = [list(zeros_field(4)) for _ in range(3)]
    expected_raw2[1] = vs(u, -Q(1, 4))
    expected_raw3[1] = vs(mv(c, u), Q(1, 4))
    expected_adj3[1] = vs(mv(c, u), -Q(1, 8))
    cubic_slice = (Q(-395, 5184), ZERO, Q(395, 5184), Q(-1, 144), Q(1, 144), Q(-1, 5184))
    require(raw2 == tuple(expected_raw2) and adj2 == zeros_field(4), "F_BRACKET")
    require(raw3 == tuple(expected_raw3) and adj3 == tuple(expected_adj3) and adj3[1] == cubic_slice, "F_BRACKET")
    for label, field in (("RAW2", raw2), ("ADJUSTED2", adj2), ("RAW3", raw3), ("ADJUSTED3", adj3)):
        payload.append("B|" + label + "|" + csv(flat(field)) + "\n")
    controls[5] = raw2 != zeros_field(4)
    controls[6] = adj3 != zeros_field(4) and adj3[1] == cubic_slice
    wrong_k = block(z6, i6, d, z6)
    controls[2] = ma(mm(mt(wrong_k), gform), mm(gform, wrong_k)) != zm(12)
    require(all(controls), "F_CONTROL")
    for number in range(1, 9):
        payload.append(f"N|NC{number:02d}|DETECTED\n")
    require(counts == dict(states=6, bonds=24, ward=24, integer=144, mixed=50, composition=28, energy=9), "F_COUNTS")
    digest = sha256("".join(payload).encode("ascii")).hexdigest()
    certificate = (
        "CERTIFICATE=P-INTEGER-SCALAR-LAPSE-RIGIDITY-1\n"
        "AUTHORITY_FILES=5\nSERIES_ORDER=6\nSERIES_COEFFICIENTS=7\n"
        "COMPOSITION_PAIRS=28\nPOSITIVE_PIVOTS=5\nOFF_SHELL_STATES=6\n"
        "BOND_JETS=24\nWARD_PARAMETER_CASES=24\nINTEGER_WARD_COEFFICIENTS=144\n"
        "MIXED_LAPSE_COEFFICIENTS=50\nCAYLEY_PARAMETERS=5\nPOSITIVE_ENERGY_STATES=9\n"
        "COMMUTATOR_WITNESSES=1\n"
        "CUBIC_ADJUSTED_WITNESS=" + csv(cubic_slice) + "\n"
        "PAYLOAD_SHA256=" + digest + "\nNEGATIVE_CONTROLS=8\nCERTIFICATE_RESULT=PASS\n"
    )
    return certificate.encode("ascii")


def main():
    try:
        certificate = audit()
        try:
            other = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("breaker.py"))],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=540, check=False)
        except (OSError, subprocess.TimeoutExpired):
            raise GateFailure("F_BYTES") from None
        require(other.returncode == 0 and other.stderr == b"" and other.stdout == certificate, "F_BYTES")
    except GateFailure as failure:
        sys.stdout.write(str(failure) + "\nRESULT=FAIL\n")
        return
    sys.stdout.buffer.write(certificate + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")


if __name__ == "__main__":
    main()
