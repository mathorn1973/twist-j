#!/usr/bin/env python3
"""Independent rational/dual audit, derived only from the frozen text.

No companion or predecessor program is read or imported.  The action
Hessian is assembled from kinetic squares, edge squares and cross terms.
Multiplier derivatives are dual derivatives of the actual S2 formula;
its inner field derivative is expanded by the product rule, so no nested
dual variables or finite differences are needed.
"""

from fractions import Fraction as Q
from hashlib import sha256
from math import lcm
from pathlib import Path
import sys


Z = Q(0)
O = Q(1)
g = Q(1, 324)
ell = (O, -O, Z, Z, Z)
sigma = (Q(1, 2), Q(1, 2), Z, Z, Z)
EDGES = tuple((r, (r + 1) % 5, Q(29, 324)) for r in range(5)) + tuple(
    (r, (r + 2) % 5, Q(65, 324)) for r in range(5))
AUTHORITY = (
    ("CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class Failure(Exception):
    pass


def check(condition, code):
    if not condition:
        raise Failure(code)


class Dual:
    __slots__ = ("value", "derivative")

    def __init__(self, value, derivative=Z):
        self.value = Q(value)
        self.derivative = Q(derivative)

    @staticmethod
    def cast(other):
        return other if isinstance(other, Dual) else Dual(other)

    def __add__(self, other):
        other = self.cast(other)
        return Dual(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        other = self.cast(other)
        return Dual(self.value * other.value,
                    self.derivative * other.value + self.value * other.derivative)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.cast(other)
        return Dual(self.value / other.value,
                    (self.derivative * other.value - self.value * other.derivative)
                    / (other.value * other.value))


def tangent(value):
    return value.derivative if isinstance(value, Dual) else Z


def dot(a, b):
    return sum((u * v for u, v in zip(a, b)), Z)


def flat(rows):
    return [v for row in rows for v in row]


def flat_M(M):
    return list(M[0]) + flat(M[1]) + flat(M[2])


def serial(values):
    return ",".join(map(str, values))


def identity(n):
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(column) for column in zip(*a)]


def matvec(a, v):
    return [dot(row, v) for row in a]


def matmul(a, b):
    bt = transpose(b)
    return [[dot(row, column) for column in bt] for row in a]


def matsub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def inverse(a):
    n = len(a)
    aug = [list(row) + ident for row, ident in zip(a, identity(n))]
    for c in range(n):
        pivot = next((r for r in range(c, n) if aug[r][c]), None)
        check(pivot is not None, "F_CARRIER")
        aug[c], aug[pivot] = aug[pivot], aug[c]
        divisor = aug[c][c]
        aug[c] = [v / divisor for v in aug[c]]
        for r in range(n):
            if r == c:
                continue
            factor = aug[r][c]
            aug[r] = [u - factor * v for u, v in zip(aug[r], aug[c])]
    return [row[n:] for row in aug]


def project(v):
    mean = sum(v, Z) / len(v)
    return [value - mean for value in v]


def make_geometry():
    B = [[(O if r == head else Z) - (O if r == tail else Z)
          for r in range(5)] for tail, head, _ in EDGES]
    Bt = transpose(B)
    W = [[weight if i == j else Z for j in range(10)]
         for i, (_, _, weight) in enumerate(EDGES)]
    WB = matmul(W, B)
    L = matmul(Bt, WB)
    mean = [[Q(1, 5)] * 5 for _ in range(5)]
    pi = matsub(identity(5), mean)
    shifted = [[L[i][j] + mean[i][j] for j in range(5)] for i in range(5)]
    lp = matsub(inverse(shifted), mean)
    P = matsub(identity(10), matmul(matmul(WB, lp), Bt))
    pcyc = matsub(identity(10), [[value / 5 for value in row]
                               for row in matmul(B, Bt)])
    V = [L[r] + [-g * ell[r]] for r in range(5)] + [[-g * v for v in ell] + [O]]
    C = [[(O if i == j else Z) - V[i][j] / 2 for j in range(6)] for i in range(6)]
    return {"B": B, "Bt": Bt, "W": W, "WB": WB, "L": L,
            "lp": lp, "P": P, "pcyc": pcyc, "pi": pi, "C": C}


def geometry_check(a):
    B, Bt, L, lp, P = (a[key] for key in ("B", "Bt", "L", "lp", "P"))
    check(matmul(L, lp) == a["pi"] == matmul(lp, L), "F_CARRIER")
    check(matvec(lp, [O] * 5) == [Z] * 5, "F_CARRIER")
    check(matmul(Bt, B) == [[5 * v for v in row] for row in a["pi"]], "F_CARRIER")
    check(matmul(Bt, P) == [[Z] * 10 for _ in range(5)], "F_CARRIER")
    check(matmul(P, P) == P and matmul(a["pcyc"], a["pcyc"]) == a["pcyc"], "F_CARRIER")
    check(matmul(Bt, a["pcyc"]) == [[Z] * 10 for _ in range(5)], "F_CARRIER")
    explicit = [[Q(188 if r == s else (-29 if (r - s) % 5 in (1, 4) else -65), 324)
                 for s in range(5)] for r in range(5)]
    check(L == explicit and transpose(lp) == lp, "F_CARRIER")


def action_hessian(T):
    rows = [dict() for _ in range(6 * (T + 1))]

    def add(i, j, value):
        rows[i][j] = rows[i].get(j, Z) + value

    def square(i, j, coefficient):
        add(i, i, coefficient)
        add(j, j, coefficient)
        add(i, j, -coefficient)
        add(j, i, -coefficient)

    for b in range(1, T + 1):
        for r in range(6):
            square(6 * b + r, 6 * (b - 1) + r, O)
    for n in range(1, T):
        for tail, head, weight in EDGES:
            square(6 * n + head, 6 * n + tail, -weight)
        add(6 * n + 5, 6 * n + 5, -O)
        for r in range(5):
            add(6 * n + r, 6 * n + 5, g * ell[r])
            add(6 * n + 5, 6 * n + r, g * ell[r])
    return rows


def hessian_vector(hessian, v):
    return [sum((value * v[j] for j, value in row.items()), Z) for row in hessian]


def euler(x, hessian):
    T = len(x) - 1
    result = [[Z] * 6 for _ in range(T + 1)]
    values = hessian_vector(hessian, flat(x))
    for n in range(1, T):
        result[n] = values[6 * n:6 * n + 6]
    return result


def blank_M(T):
    return ([Z] * (T + 1), [[Z] * 5 for _ in range(T + 1)],
            [[Z] * 10 for _ in range(T + 1)])


def add_M(a, b):
    return ([x + y for x, y in zip(a[0], b[0])],
            [[x + y for x, y in zip(ar, br)] for ar, br in zip(a[1], b[1])],
            [[x + y for x, y in zip(ar, br)] for ar, br in zip(a[2], b[2])])


def dual_M(M, direction):
    return ([Dual(x, y) for x, y in zip(M[0], direction[0])],
            [[Dual(x, y) for x, y in zip(ar, br)] for ar, br in zip(M[1], direction[1])],
            [[Dual(x, y) for x, y in zip(ar, br)] for ar, br in zip(M[2], direction[2])])


def dual_x(x, variation):
    return [[Dual(u, v) for u, v in zip(row, delta)] for row, delta in zip(x, variation)]


def gamma(psi, a):
    T = len(psi) - 1
    alpha, lam, N = blank_M(T)
    for b in range(1, T + 1):
        difference = [u - v for u, v in zip(psi[b], psi[b - 1])]
        alpha[b] = sum(difference, Z) / 5
        lam[b] = project(difference)
    for n in range(1, T):
        N[n] = matvec(a["B"], psi[n])
    return alpha, lam, N


def G(x, psi):
    T = len(x) - 1
    out = [[Z] * 6 for _ in range(T + 1)]
    for n in range(1, T):
        q = [u - v for u, v in zip(x[n + 1], x[n - 1])]
        out[n] = [psi[n][r] * q[r] / 2 for r in range(5)] + [dot(sigma, psi[n]) * q[5] / 2]
    return out


def density(previous, following):
    out = [(following[r] - previous[r]) * (following[r] - previous[r]) / 2 for r in range(5)]
    for tail, head, weight in EDGES:
        term = weight * (following[head] - following[tail]) * (previous[head] - previous[tail]) / 4
        out[tail] += term
        out[head] += term
    dchi = following[5] - previous[5]
    for r in range(5):
        out[r] += sigma[r] * (dchi * dchi + following[5] * previous[5]) / 2
        out[r] -= g * ell[r] * (previous[5] * following[r] + following[5] * previous[r]) / 2
    return out


def density_derivative(previous, following, dp, df):
    """Product-rule coefficient, also valid over outer multiplier duals."""
    out = [(following[r] - previous[r]) * (df[r] - dp[r]) for r in range(5)]
    for tail, head, weight in EDGES:
        term = weight * ((df[head] - df[tail]) * (previous[head] - previous[tail])
                         + (following[head] - following[tail]) * (dp[head] - dp[tail])) / 4
        out[tail] += term
        out[head] += term
    for r in range(5):
        out[r] += sigma[r] * ((following[5] - previous[5]) * (df[5] - dp[5])
                             + (df[5] * previous[5] + following[5] * dp[5]) / 2)
        out[r] -= g * ell[r] * (dp[5] * following[r] + previous[5] * df[r]
                                + df[5] * previous[r] + following[5] * dp[r]) / 2
    return out


def current(x, n):
    q = [u - v for u, v in zip(x[n + 1], x[n - 1])]
    out = [weight * (x[n][head] - x[n][tail]) * (q[tail] + q[head]) / 4
           for tail, head, weight in EDGES]
    out[0] -= g * q[5] * (x[n][0] + x[n][1]) / 4
    return out


def current_derivative(x, v, n):
    q = [u - w for u, w in zip(x[n + 1], x[n - 1])]
    dq = [u - w for u, w in zip(v[n + 1], v[n - 1])]
    out = [weight * ((v[n][head] - v[n][tail]) * (q[tail] + q[head])
                    + (x[n][head] - x[n][tail]) * (dq[tail] + dq[head])) / 4
           for tail, head, weight in EDGES]
    out[0] -= g * (dq[5] * (x[n][0] + x[n][1]) + q[5] * (v[n][0] + v[n][1])) / 4
    return out


def interaction(x, M):
    T = len(x) - 1
    alpha, lam, N = M
    result = Z
    for b in range(1, T + 1):
        eb = density(x[b - 1], x[b])
        result -= alpha[b] * sum(eb, Z) + dot(lam[b], eb)
    for n in range(1, T):
        result += dot(N[n], current(x, n))
    return result


def interaction_derivative(x, M, v):
    T = len(x) - 1
    alpha, lam, N = M
    result = Z
    for b in range(1, T + 1):
        deb = density_derivative(x[b - 1], x[b], v[b - 1], v[b])
        result -= alpha[b] * sum(deb, Z) + dot(lam[b], deb)
    for n in range(1, T):
        result += dot(N[n], current_derivative(x, v, n))
    return result


def baux(M, tau, p, a):
    T = len(tau) - 1
    result = Z
    for b in range(1, T + 1):
        result += 2 * dot(M[1][b], matvec(a["L"], tau[b]))
    for n in range(1, T):
        difference = [u - v for u, v in zip(tau[n + 1], tau[n])]
        wb = matvec(a["WB"], difference)
        result += 2 * dot(M[2][n], [u + v for u, v in zip(wb, p[n])])
    return result


def decomposition(M, a):
    T = len(M[0]) - 1
    alpha, lam, N = M
    z = [[Z] * 5 for _ in range(T + 1)]
    cycle = [[Z] * 10 for _ in range(T + 1)]
    for n in range(1, T):
        z[n] = matvec(a["lp"], matvec(a["Bt"], matvec(a["W"], N[n])))
        bz = matvec(a["B"], z[n])
        cycle[n] = [u - v for u, v in zip(N[n], bz)]
    l = [[Z] * 5 for _ in range(T + 1)]
    for b in range(1, T + 1):
        l[b] = [lam[b][r] - z[b][r] + z[b - 1][r] for r in range(5)]
    return z, (alpha, l, cycle)


def hom_action(x, M, a):
    result = Z
    for b in range(1, len(x)):
        cb = matvec(a["C"], x[b])
        cp = matvec(a["C"], x[b - 1])
        k = dot([u - v for u, v in zip(cb, x[b - 1])],
                [u - v for u, v in zip(x[b], cp)])
        result += M[0][b] * M[0][b] * k / 2
    return result


def second_action(x, M, a, hessian):
    z, residual_M = decomposition(M, a)
    w = G(x, z)
    vector = flat(w)
    return (-interaction_derivative(x, residual_M, w)
            + dot(vector, hessian_vector(hessian, vector)) / 2 + hom_action(x, M, a))


def variations(x, M, psi, a, hessian):
    T = len(x) - 1
    z, _ = decomposition(M, a)
    t = [sum(row, Z) / 5 for row in psi]
    uniform = [[value] * 5 for value in t]
    U = G(x, uniform)
    gz_gpsi = G(G(x, psi), z)
    gt_gz = G(G(x, z), uniform)
    Xhom = [[Z] * 6 for _ in range(T + 1)]
    Xraw = [[Z] * 6 for _ in range(T + 1)]
    Xadj = [[Z] * 6 for _ in range(T + 1)]
    skew = [[Z] * 6 for _ in range(T + 1)]
    f = euler(x, hessian)
    for n in range(1, T):
        cnext = matvec(a["C"], x[n + 1])
        cprev = matvec(a["C"], x[n - 1])
        for r in range(6):
            Xhom[n][r] = t[n] * (M[0][n + 1] * (x[n][r] - cnext[r])
                                         - M[0][n] * (x[n][r] - cprev[r])) / 2
            Xraw[n][r] = gz_gpsi[n][r] - gt_gz[n][r] + Xhom[n][r]
            skew[n][r] = (M[0][n + 1] * (t[n] + t[n + 1]) * f[n + 1][r]
                          - M[0][n] * (t[n - 1] + t[n]) * f[n - 1][r]) / 8
            Xadj[n][r] = Xraw[n][r] + skew[n][r]
    F = [[Z] * 5 for _ in range(T + 1)]
    J = [[Z] * 10 for _ in range(T + 1)]
    ux = dual_x(x, U)
    for b in range(1, T + 1):
        de = [tangent(value) for value in density(ux[b - 1], ux[b])]
        F[b] = [value / 2 for value in matvec(a["lp"], project(de))]
    for n in range(1, T):
        dj = [tangent(value) for value in current(ux, n)]
        J[n] = [-value / 2 for value in matvec(a["P"], dj)]
    return {"raw": Xraw, "adjusted": Xadj, "skew": skew, "F": F, "J": J,
            "hom": Xhom, "U": U, "multiplier": blank_M(T)}


def bracket(x, M, psi, eta, a, hessian):
    T = len(x) - 1
    eta_var = variations(x, dual_M(M, gamma(psi, a)), eta, a, hessian)
    psi_var = variations(x, dual_M(M, gamma(eta, a)), psi, a, hessian)
    first = G(G(x, psi), eta)
    second = G(G(x, eta), psi)
    raw = [[Z] * 6 for _ in range(T + 1)]
    adjusted = [[Z] * 6 for _ in range(T + 1)]
    for n in range(T + 1):
        for r in range(6):
            base = first[n][r] - second[n][r]
            raw[n][r] = base + tangent(eta_var["raw"][n][r]) - tangent(psi_var["raw"][n][r])
            adjusted[n][r] = (base + tangent(eta_var["adjusted"][n][r])
                               - tangent(psi_var["adjusted"][n][r]))
    auxiliary = ([tangent(u) - tangent(v) for u, v in zip(flat(eta_var["F"]), flat(psi_var["F"]))]
                 + [tangent(u) - tangent(v) for u, v in zip(flat(eta_var["J"]), flat(psi_var["J"]))])
    auxiliary += [tangent(u) - tangent(v) for u, v in zip(
        flat_M(eta_var["multiplier"]), flat_M(psi_var["multiplier"]))]
    # delta1 M=0 and Gamma is state-independent, so the remaining
    # order0/order1 commutator coefficients vanish identically.
    return raw, adjusted, auxiliary


def predicted_bracket(x, psi, eta, hessian):
    T = len(x) - 1
    f = euler(x, hessian)
    t = [sum(row, Z) / 5 for row in psi]
    s = [sum(row, Z) / 5 for row in eta]
    out = [[Z] * 6 for _ in range(T + 1)]
    for n in range(1, T):
        for r in range(6):
            out[n][r] = (-(s[n] * t[n + 1] - t[n] * s[n + 1]) * f[n + 1][r]
                         - (s[n] * t[n - 1] - t[n] * s[n - 1]) * f[n - 1][r]) / 4
    return out


def zeta(q, n, r):
    return Q(((q + 2) * (n + 1) * (r + 3) + (n - r) ** 2) % 17 - 8, q + 2)


def fixture(T, q, a):
    x = [[zeta(q, n, r) for r in range(6)] for n in range(T + 1)]
    alpha, lam, N = blank_M(T)
    tau = [[Z] * 5 for _ in range(T + 1)]
    p = [[Z] * 10 for _ in range(T + 1)]
    for b in range(1, T + 1):
        alpha[b] = zeta(q, b, 6)
        lam[b] = project([zeta(q, b, 7 + r) for r in range(5)])
        tau[b] = project([zeta(q + 1, b, 12 + r) for r in range(5)])
    for n in range(1, T):
        N[n] = [zeta(q, n, 17 + e) for e in range(10)]
        p[n] = matvec(a["pcyc"], [zeta(q + 1, n, 27 + e) for e in range(10)])
    return x, (alpha, lam, N), tau, p


def parameter_list(T, q):
    parameters = []
    for n in range(1, T):
        for r in range(5):
            psi = [[Z] * 5 for _ in range(T + 1)]
            psi[n][r] = O
            parameters.append(psi)
    dense = [[Z] * 5 for _ in range(T + 1)]
    eta = [[Z] * 5 for _ in range(T + 1)]
    for n in range(1, T):
        dense[n] = [zeta(q + 2, n, 37 + r) for r in range(5)]
        eta[n] = [zeta(q + 3, n, 42 + r) for r in range(5)]
    parameters.append(dense)
    return parameters, eta


def state_check(x, M, tau, p, a, hessian):
    geometry_check(a)
    T = len(x) - 1
    z, residual_M = decomposition(M, a)
    for b in range(1, T + 1):
        check(sum(M[1][b], Z) == sum(tau[b], Z) == sum(residual_M[1][b], Z) == 0,
              "F_CARRIER")
        H = (dot(x[b], x[b]) + dot(x[b - 1], x[b - 1])) / 2 - dot(x[b - 1], matvec(a["C"], x[b]))
        check(sum(density(x[b - 1], x[b]), Z) == H, "F_CARRIER")
    for n in range(1, T):
        cycle = residual_M[2][n]
        check(sum(z[n], Z) == 0 and matvec(a["Bt"], p[n]) == [Z] * 5, "F_CARRIER")
        check(matvec(a["Bt"], matvec(a["W"], cycle)) == [Z] * 5, "F_CARRIER")
        check(matvec(transpose(a["P"]), cycle) == cycle, "F_CARRIER")
    decomposed = sum((2 * dot(residual_M[1][b], matvec(a["L"], tau[b]))
                      for b in range(1, T + 1)), Z)
    decomposed += sum((2 * dot(residual_M[2][n], p[n]) for n in range(1, T)), Z)
    check(baux(M, tau, p, a) == decomposed, "F_CARRIER")
    f = euler(x, hessian)
    for n in range(1, T):
        cx = matvec(a["C"], x[n])
        check(f[n] == [2 * cx[r] - x[n - 1][r] - x[n + 1][r] for r in range(6)], "F_CARRIER")


def tangent_check(psi, M, var, a):
    T = len(psi) - 1
    change = gamma(psi, a)
    check(all(value == 0 for value in flat_M(var["multiplier"])), "F_CARRIER")
    for key in ("raw", "adjusted", "skew", "hom", "U"):
        check(var[key][0] == [Z] * 6 and var[key][T] == [Z] * 6, "F_CARRIER")
    for b in range(1, T + 1):
        check(sum(var["F"][b], Z) == sum(change[1][b], Z) == 0, "F_CARRIER")
    for n in range(1, T):
        check(matvec(a["Bt"], var["J"][n]) == [Z] * 5, "F_CARRIER")
    dual_z, dual_residual = decomposition(dual_M(M, change), a)
    for n in range(T + 1):
        check([tangent(v) for v in dual_z[n]] == project(psi[n]), "F_CARRIER")
        check(all(tangent(v) == 0 for v in dual_residual[2][n]), "F_CARRIER")
    check(all(tangent(v) == 0 for row in dual_residual[1] for v in row), "F_CARRIER")


def authority_check():
    root = Path(__file__).resolve().parents[2]
    for name, size, expected in AUTHORITY:
        try:
            data = (root / "canon" / name).read_bytes()
        except OSError:
            raise Failure("F_AUTHORITY") from None
        check(len(data) == size and sha256(data).hexdigest() == expected, "F_AUTHORITY")


def run():
    authority_check()
    a = make_geometry()
    payload = []
    controls = [False] * 8
    counts = {key: 0 for key in (
        "OFF_SHELL_STATES", "LOWER_ORDER_CASES", "SCALAR_WARD_CASES", "RAW_WARD_CASES",
        "ADJUSTED_WARD_CASES", "SKEW_WORK_CASES", "TANGENT_CASES", "COMMUTATOR_PAIRS",
        "DISTANT_MULTIPLIER_PAIRS", "INTEGER_WARD_CASES")}
    for T in (3, 4, 5, 7):
        hessian = action_hessian(T)
        for q in (1, 2, 3):
            authority_check()
            x, M, tau, p = fixture(T, q, a)
            state_check(x, M, tau, p, a, hessian)
            counts["OFF_SHELL_STATES"] += 1
            f = euler(x, hessian)
            A = dot(flat(x), hessian_vector(hessian, flat(x))) / 2
            Baux = baux(M, tau, p, a)
            I = interaction(x, M)
            S2 = second_action(x, M, a, hessian)
            payload.append(f"S|{T}|{q}|{A}|{Baux}|{I}|{S2}\n")
            parameters, eta = parameter_list(T, q)
            for index, psi in enumerate(parameters):
                change = gamma(psi, a)
                gx = G(x, psi)
                check(gx[0] == gx[T] == [Z] * 6, "F_CARRIER")
                var = variations(x, M, psi, a, hessian)
                tangent_check(psi, M, var, a)
                counts["TANGENT_CASES"] += 1
                d0s0 = baux(change, tau, p, a)
                d0i = tangent(interaction(x, dual_M(M, change)))
                d1s0 = dot(flat(f), flat(gx))
                check(d0s0 == 0 and d0i + d1s0 == 0, "F_LOWER")
                counts["LOWER_ORDER_CASES"] += 1
                d0s2 = tangent(second_action(x, dual_M(M, change), a, hessian))
                d1i = tangent(interaction(dual_x(x, gx), M))
                # Independent product-rule expression is checked against Dual.
                check(d1i == interaction_derivative(x, M, gx), "F_CARRIER")
                empty_tau = [[Z] * 5 for _ in range(T + 1)]
                empty_p = [[Z] * 10 for _ in range(T + 1)]
                tau_work = baux(M, var["F"], empty_p, a)
                p_work = baux(M, empty_tau, var["J"], a)
                raw_work = dot(flat(f), flat(var["raw"])) + tau_work + p_work
                adjusted_work = dot(flat(f), flat(var["adjusted"])) + tau_work + p_work
                skewwork = dot(flat(f), flat(var["skew"]))
                check(skewwork == 0, "F_SKEW")
                counts["SKEW_WORK_CASES"] += 1
                check(d0s2 + d1i + raw_work == 0, "F_WARD")
                counts["RAW_WARD_CASES"] += 1
                check(d0s2 + d1i + adjusted_work == 0, "F_WARD")
                counts["ADJUSTED_WARD_CASES"] += 1
                scalar_M = blank_M(T)
                scalar_M[0][:] = M[0]
                d0hom = tangent(hom_action(x, dual_M(M, change), a))
                scalar_i = tangent(interaction(dual_x(x, var["U"]), scalar_M))
                check(d0hom + scalar_i + dot(flat(f), flat(var["hom"])) == 0, "F_SCALAR")
                counts["SCALAR_WARD_CASES"] += 1
                terms = [d0s0, d0i, d1s0, d0s2, d1i, raw_work, adjusted_work, skewwork]
                denominator = lcm(*(term.denominator for term in terms))
                integers = [denominator * term for term in terms]
                check(all(term.denominator == 1 for term in integers)
                      and integers[3] + integers[4] + integers[5] == 0
                      and integers[3] + integers[4] + integers[6] == 0, "F_INTEGER")
                counts["INTEGER_WARD_CASES"] += 1
                payload.append(f"W|{T}|{q}|{index}|" + "|".join(map(str, terms)) + "\n")
                generated = flat(var["adjusted"]) + flat(var["F"][1:T + 1]) + flat(var["J"][1:T])
                payload.append(f"G|{T}|{q}|{index}|{serial(generated)}\n")
                raw, adjusted, auxiliary = bracket(x, M, psi, eta, a, hessian)
                check(raw == predicted_bracket(x, psi, eta, hessian)
                      and all(value == 0 for value in flat(adjusted))
                      and all(value == 0 for value in auxiliary), "F_BRACKET")
                check(dot(flat(f), flat(raw)) == 0, "F_BRACKET")
                counts["COMMUTATOR_PAIRS"] += 1
                payload.append(f"B|{T}|{q}|{index}|{serial(flat(raw))}\n")
                defects = [d1i + adjusted_work,
                           d0s2 + d1i + adjusted_work - tau_work,
                           d0s2 + d1i + adjusted_work - p_work,
                           d0s2 + d1i + adjusted_work - 2 * tau_work,
                           d0s2 - 2 * d0hom + d1i + adjusted_work,
                           d0hom + d1i + adjusted_work]
                for control_index, defect in enumerate(defects):
                    controls[control_index] = controls[control_index] or defect != 0

    T = 5
    x, _, _, _ = fixture(T, 1, a)
    hessian = action_hessian(T)
    basis = []
    labels = []
    for b in range(1, T + 1):
        M = blank_M(T)
        M[0][b] = O
        basis.append(M)
        labels.append(b)
    for b in range(1, T + 1):
        for r in range(4):
            M = blank_M(T)
            M[1][b][r], M[1][b][4] = O, -O
            basis.append(M)
            labels.append(b)
    for n in range(1, T):
        for edge in range(10):
            M = blank_M(T)
            M[2][n][edge] = O
            basis.append(M)
            labels.append(n)
    check(len(basis) == 65, "F_COUNTS")
    singles = [second_action(x, M, a, hessian) for M in basis]
    check(second_action(x, blank_M(T), a, hessian) == 0, "F_LOCALITY")
    for i in range(len(basis)):
        for j in range(i + 1, len(basis)):
            if abs(labels[i] - labels[j]) <= 1:
                continue
            mixed = second_action(x, add_M(basis[i], basis[j]), a, hessian) - singles[i] - singles[j]
            check(mixed == 0, "F_LOCALITY")
            counts["DISTANT_MULTIPLIER_PAIRS"] += 1
            payload.append(f"L|{i}|{j}|{mixed}\n")

    T = 4
    hessian = action_hessian(T)
    x = [[Z] * 6 for _ in range(T + 1)]
    x[3] = [O, Z, -O, Z, Z, Z]
    psi = [[Z] * 5 for _ in range(T + 1)]
    eta = [[Z] * 5 for _ in range(T + 1)]
    psi[1], eta[2] = [O] * 5, [O] * 5
    raw, adjusted, auxiliary = bracket(x, blank_M(T), psi, eta, a, hessian)
    expected = [[Z] * 6 for _ in range(T + 1)]
    expected[1] = [Q(-1, 4), Z, Q(1, 4), Z, Z, Z]
    check(raw == expected and all(value == 0 for value in flat(adjusted))
          and all(value == 0 for value in auxiliary), "F_BRACKET")
    # Reversing the added skew term changes raw+(adjusted-raw) into
    # raw-(adjusted-raw).  Both operands are actual transformation derivatives.
    reversed_adjustment = [2 * u - v for u, v in zip(flat(raw), flat(adjusted))]
    controls[6] = raw == expected and any(value != 0 for value in flat(raw))
    controls[7] = reversed_adjustment == [2 * value for value in flat(expected)] and any(reversed_adjustment)
    payload.append(f"E|RAW|{serial(flat(raw))}\n")
    payload.append(f"E|ADJUSTED|{serial(flat(adjusted))}\n")
    check(all(controls), "F_CONTROL")
    payload.extend(f"N|NC{index:02d}|DETECTED\n" for index in range(1, 9))
    expected_counts = {key: (12 if key == "OFF_SHELL_STATES" else
                            900 if key == "DISTANT_MULTIPLIER_PAIRS" else 237) for key in counts}
    check(counts == expected_counts, "F_COUNTS")
    digest = sha256("".join(payload).encode("ascii")).hexdigest()
    lines = ["CERTIFICATE=P-INTEGER-LOCAL-AUXILIARY-NOETHER-1", "AUTHORITY_FILES=5"]
    lines.extend(f"{key}={value}" for key, value in counts.items())
    lines.extend(("RAW_WITNESS=-1/4,0,1/4,0,0,0", "ADJUSTED_WITNESS=0,0,0,0,0,0",
                  f"PAYLOAD_SHA256={digest}", "NEGATIVE_CONTROLS=8", "CERTIFICATE_RESULT=PASS"))
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))


if __name__ == "__main__":
    try:
        run()
    except Failure as failure:
        sys.stdout.buffer.write((str(failure) + "\nRESULT=FAIL\n").encode("ascii"))
