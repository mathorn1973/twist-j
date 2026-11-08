#!/usr/bin/env python3
"""Independent pair-form audit; no companion or prior scientific code is read.

Only the five frozen normative files are runtime inputs. Rational real-field
arithmetic uses reduced integer triples, and cyclotomic arithmetic uses a
separate polynomial representation. Nothing here evaluates finite roots.
"""

from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path


PROBE = "P-RELATIONAL-MASS-METRIC-RESPONSE-1"
# Frozen normative bytes from SOURCE.md; no runtime manifest reads.
AUTHORITY = (
    ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    """A completed, declared scientific failure rather than a runtime defect."""


def require(condition, code):
    if not condition:
        raise ScientificFailure(code)


# A real-field value (a,b,d) means (a+b*phi)/d, with positive d.
def real(a=0, b=0, d=1):
    if d == 0:
        raise ZeroDivisionError("real-field denominator is zero")
    if d < 0:
        a, b, d = -a, -b, -d
    g = gcd(gcd(abs(a), abs(b)), d)
    return (a // g, b // g, d // g)


ZERO = (0, 0, 1)
ONE = (1, 0, 1)
PHI = (0, 1, 1)


def add(x, y):
    if x == ZERO:
        return y
    if y == ZERO:
        return x
    return real(x[0] * y[2] + y[0] * x[2],
                x[1] * y[2] + y[1] * x[2], x[2] * y[2])


def neg(x):
    return (-x[0], -x[1], x[2])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    if x == ZERO or y == ZERO:
        return ZERO
    a, b, d = x
    c, e, f = y
    return real(a * c + b * e, a * e + b * c + b * e, d * f)


def scale(x, p, q=1):
    return real(x[0] * p, x[1] * p, x[2] * q)


def tau(x):
    return real(x[0] + x[1], -x[1], x[2])


def inverse(x):
    a, b, d = x
    return real(d * (a + b), -d * b, a * a + a * b - b * b)


def total(xs):
    result = ZERO
    for x in xs:
        result = add(result, x)
    return result


def sign(x):
    # Twice the numerator is A+B*sqrt(5). Squaring is used only when
    # A and B have opposite signs, so its sign implications are exact.
    a, b, _ = x
    A, B = 2 * a + b, b
    if B == 0:
        return (A > 0) - (A < 0)
    if A == 0:
        return (B > 0) - (B < 0)
    if A > 0 and B > 0:
        return 1
    if A < 0 and B < 0:
        return -1
    comparison = A * A - 5 * B * B
    return ((comparison > 0) - (comparison < 0)) * (1 if A > 0 else -1)


def real_text(x):
    return str(Fraction(x[0], x[2])) + "," + str(Fraction(x[1], x[2]))


def array_text(xs):
    return ",".join(real_text(x) for x in xs)


# K uses four Fractions in the Phi_5 power basis, independently of real().
KZERO = (Fraction(0),) * 4
KONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
J = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))


def kadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def kneg(x):
    return tuple(-a for a in x)


def ksub(x, y):
    return kadd(x, kneg(y))


def kscale(x, n):
    return tuple(a * n for a in x)


def kmul(x, y):
    # Convolve in Q[j], then divide by j^4+j^3+j^2+j+1.
    coefficients = [Fraction(0) for _ in range(7)]
    for i in range(4):
        for k in range(4):
            if x[i] and y[k]:
                coefficients[i + k] += x[i] * y[k]
    for degree in range(6, 3, -1):
        lead = coefficients[degree]
        for offset in range(1, 5):
            coefficients[degree - offset] -= lead
    return tuple(coefficients[:4])


def kpower(x, n):
    result = KONE
    for _ in range(n):
        result = kmul(result, x)
    return result


def kmap(x, exponent, powers):
    result = KZERO
    for i, a in enumerate(x):
        result = kadd(result, kscale(powers[(exponent * i) % 5], a))
    return result


def embed(x):
    a, b, d = x
    return (Fraction(a, d), Fraction(0), Fraction(-b, d), Fraction(-b, d))


def extract(x):
    require(x[1] == 0 and x[2] == x[3], "F_GEOMETRY")
    a, b = x[0], -x[2]
    return real(a.numerator * b.denominator,
                b.numerator * a.denominator, a.denominator * b.denominator)


def real_part(x, powers):
    return extract(kscale(kadd(x, kmap(x, 4, powers)), Fraction(1, 2)))


def ktext(x):
    return ",".join(str(a) for a in x)


# Full row-major matrices preserve both off-diagonal entries explicitly.
def matrix_add(A, B):
    return tuple(add(a, b) for a, b in zip(A, B))


def matrix_sub(A, B):
    return tuple(sub(a, b) for a, b in zip(A, B))


def matrix_scale(A, n, d=1):
    return tuple(scale(a, n, d) for a in A)


def outer(u, v):
    return tuple(mul(u[i], v[j]) for i in range(2) for j in range(2))


def matrix_multiply(A, B):
    return tuple(total(mul(A[2 * i + k], B[2 * k + j]) for k in range(2))
                 for i in range(2) for j in range(2))


def transpose(A):
    return (A[0], A[2], A[1], A[3])


def matvec(A, u):
    return tuple(total(mul(A[2 * i + k], u[k]) for k in range(2))
                 for i in range(2))


def bilinear(u, A, v):
    Av = matvec(A, v)
    return total(mul(u[i], Av[i]) for i in range(2))


def pairing(A, B):
    return total(mul(A[2 * i + j], B[2 * j + i])
                 for i in range(2) for j in range(2))


def determinant(A):
    return sub(mul(A[0], A[3]), mul(A[1], A[2]))


def matrix_rank(A, size):
    # Actual field elimination, independent of the support prediction.
    rows = [list(A[size * i:size * (i + 1)]) for i in range(size)]
    rank = 0
    for column in range(size):
        pivot = next((r for r in range(rank, size) if rows[r][column] != ZERO), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_inverse = inverse(rows[rank][column])
        for r in range(rank + 1, size):
            if rows[r][column] == ZERO:
                continue
            factor = mul(rows[r][column], pivot_inverse)
            for c in range(column, size):
                rows[r][c] = sub(rows[r][c], mul(factor, rows[rank][c]))
        rank += 1
    return rank


def require_psd(A):
    require(A[1] == A[2] and sign(A[0]) >= 0 and sign(A[3]) >= 0
            and sign(determinant(A)) >= 0, "F_RANK")


def root_series(a):
    coefficients = [ONE, scale(a, 1, 2)]
    for degree in range(2, 5):
        coefficients.append(scale(total(mul(coefficients[i], coefficients[degree - i])
                                        for i in range(1, degree)), -1, 2))
    return tuple(coefficients)


def pair_root_series(a, b):
    # Independently solve f(e)^2=1+(a+b)e+ab e^2, coefficient by
    # coefficient. This enters D directly through unordered pairs.
    rhs = (ONE, add(a, b), mul(a, b), ZERO, ZERO)
    coefficients = [ONE]
    for degree in range(1, 5):
        interior = total(mul(coefficients[i], coefficients[degree - i])
                         for i in range(1, degree))
        coefficients.append(scale(sub(rhs[degree], interior), 1, 2))
    return tuple(coefficients)


def convolution(a, b):
    return tuple(total(mul(a[i], b[degree - i]) for i in range(degree + 1))
                 for degree in range(5))


class Payload:
    def __init__(self):
        self.digest = sha256()
        self.records = 0

    def emit(self, *parts):
        self.digest.update(("|".join(str(p) for p in parts) + "\n").encode("ascii"))
        self.records += 1


def check_authority():
    require(len(AUTHORITY) == 5, "F_AUTHORITY")
    root = Path(__file__).resolve().parents[2]
    for relative, expected_size, expected_hash in AUTHORITY:
        content = (root / relative).read_bytes()
        require(len(content) == expected_size and sha256(content).hexdigest() == expected_hash,
                "F_AUTHORITY")


def make_geometry():
    t = sub(PHI, ONE)
    G = (ONE, scale(t, 1, 2), scale(t, 1, 2), ONE)
    U = ((ONE, ZERO), (ZERO, ONE), (neg(ONE), t),
         (neg(t), neg(t)), (t, neg(ONE)))
    powers = tuple(kpower(J, k) for k in range(5))
    kphi = embed(PHI)
    require(kpower(J, 5) == KONE and
            kadd(kadd(kadd(kadd(powers[0], powers[1]), powers[2]), powers[3]), powers[4]) == KZERO
            and kmul(kphi, kphi) == kadd(kphi, KONE)
            and mul(PHI, PHI) == add(PHI, ONE)
            and kmap(kphi, 2, powers) == embed(tau(PHI)), "F_GEOMETRY")
    require(determinant(G) == scale(add(real(2), PHI), 1, 4)
            and sign(determinant(G)) > 0, "F_GEOMETRY")
    for k in range(5):
        require(kadd(embed(U[k][0]), kmul(embed(U[k][1]), J)) == powers[k]
                and bilinear(U[k], G, U[k]) == ONE, "F_GEOMETRY")
    parameters = ((ONE, KZERO), (ZERO, KONE), (ZERO, J),
                  (ONE, ksub(kscale(KONE, 2), J)))
    strains = []
    values = []
    for alpha, beta in parameters:
        h00 = add(alpha, real_part(beta, powers))
        h01 = add(mul(alpha, scale(t, 1, 2)), real_part(kmul(beta, J), powers))
        h11 = add(alpha, real_part(kmul(beta, powers[2]), powers))
        H = (h00, h01, h01, h11)
        a = tuple(bilinear(u, H, u) for u in U)
        require(all(a[k] == add(alpha, real_part(kmul(beta, powers[(2 * k) % 5]), powers))
                    for k in range(5)), "F_GEOMETRY")
        strains.append(H)
        values.append(a)
    require(strains[0] == G and
            strains[3] == matrix_sub(matrix_add(strains[0], matrix_scale(strains[1], 2)), strains[2]),
            "F_GEOMETRY")
    basis = tuple(strains[i][j] for i in range(3) for j in (0, 1, 3))
    require(matrix_rank(basis, 3) == 3, "F_GEOMETRY")
    pairs = tuple((r, q) for r in range(5) for q in range(r + 1, 5))
    root_coefficients = tuple(tuple(root_series(a) for a in row) for row in values)
    kernels = []
    for s in range(4):
        row = []
        for r, q in pairs:
            coeff = pair_root_series(values[s][r], values[s][q])
            require(coeff == convolution(root_coefficients[s][r], root_coefficients[s][q]), "F_SERIES")
            row.append((sub(coeff[0], bilinear(U[r], G, U[q])),
                        sub(coeff[1], bilinear(U[r], strains[s], U[q])), *coeff[2:]))
        kernels.append(tuple(row))
    return G, U, powers, parameters, tuple(strains), tuple(values), pairs, root_coefficients, tuple(kernels)


def preparation(n, G, U, powers):
    N = sum(n)
    Z = KZERO
    W = KZERO
    for k in range(5):
        Z = kadd(Z, kscale(powers[k], n[k]))
        W = kadd(W, kscale(powers[(2 * k) % 5], n[k]))
    P = tuple(total(scale(U[k][i], n[k]) for k in range(5)) for i in range(2))
    T = tuple(total(scale(mul(U[k][i], U[k][j]), n[k]) for k in range(5))
              for i in range(2) for j in range(2))
    PP = outer(P, P)
    R = matrix_sub(matrix_scale(T, N), PP)
    normZ = extract(kmul(Z, kmap(Z, 4, powers)))
    D = sub(real(N * N), normZ)
    Q = ksub(kscale(W, N), kmul(Z, Z))
    return {"N": N, "Z": Z, "W": W, "P": P, "T": T, "R": R,
            "D": D, "Q": Q, "normZ": normZ}


def hessian(n, N, values, pairs):
    moment = tuple(total(scale(values[i][k], n[k]) for k in range(5)) for i in range(3))
    B = []
    for i in range(3):
        for j in range(3):
            second = total(scale(mul(values[i][k], values[j][k]), n[k]) for k in range(5))
            direct = scale(sub(mul(moment[i], moment[j]), scale(second, N)), 1, 2)
            pair_value = scale(total(scale(mul(sub(values[i][r], values[i][q]),
                                                   sub(values[j][r], values[j][q])), n[r] * n[q])
                                     for r, q in pairs), -1, 2)
            require(direct == pair_value, "F_HESSIAN")
            B.append(pair_value)
    B = tuple(B)
    require(all(B[i] == ZERO for i in (0, 1, 2, 3, 6)) and B[5] == B[7], "F_HESSIAN")
    block = (B[4], B[5], B[7], B[8])
    require(sign(B[4]) <= 0 and sign(B[8]) <= 0 and sign(determinant(block)) >= 0,
            "F_HESSIAN")
    return B


def check_preparation(n, data, G, U, powers, pairs):
    N, Z, W = data["N"], data["Z"], data["W"]
    P, T, R, D, Q = (data[k] for k in ("P", "T", "R", "D", "Q"))
    require(W == kmap(Z, 2, powers), "F_RESPONSE")
    require(kadd(embed(P[0]), kmul(embed(P[1]), J)) == Z
            and bilinear(P, G, P) == data["normZ"]
            and D == sub(real(N * N), bilinear(P, G, P)), "F_RESPONSE")
    pair_R = [ZERO] * 4
    pair_D = ZERO
    for r, q in pairs:
        difference = tuple(sub(U[r][i], U[q][i]) for i in range(2))
        pair_R = matrix_add(pair_R, matrix_scale(outer(difference, difference), n[r] * n[q]))
        pair_D = add(pair_D, scale(bilinear(difference, G, difference), n[r] * n[q]))
    require(R == tuple(pair_R) and D == pair_D
            and pairing(G, T) == real(N) and pairing(G, R) == D, "F_RESPONSE")
    normW = extract(kmul(W, kmap(W, 4, powers)))
    normQ = extract(kmul(Q, kmap(Q, 4, powers)))
    require(tau(data["normZ"]) == normW
            and mul(scale(determinant(G), 4), determinant(T)) == tau(D)
            and mul(scale(determinant(G), 4), determinant(R)) == sub(mul(D, D), normQ),
            "F_RESPONSE")
    r = (Fraction(N) - sum(Z)) / 5
    reconstructed = tuple(z + r for z in Z) + (r,)
    require(r.denominator == 1 and all(v >= 0 and v.denominator == 1 for v in reconstructed)
            and reconstructed == tuple(Fraction(v) for v in n), "F_FIBER")
    equal_counts = len(set(n)) == 1
    require((Z == KZERO) == equal_counts and (P == (ZERO, ZERO)) == equal_counts, "F_FIBER")
    require_psd(T)
    require_psd(R)
    rT, rR = matrix_rank(T, 2), matrix_rank(R, 2)
    support = sum(v != 0 for v in n)
    require(rT == (0 if support == 0 else 1 if support == 1 else 2)
            and rR == (0 if support <= 1 else 1 if support == 2 else 2), "F_RANK")
    return support, rT, rR, equal_counts


def series(n, data, B, s, strains, values, parameters, powers, pairs, roots, kernels):
    E = tuple(total(scale(roots[s][k][degree], n[k]) for k in range(5))
              for degree in range(5))
    # This is the defining construction of D here: ten unordered pair
    # contributions, including all five coefficients, for every count case.
    Dcoeff = tuple(total(scale(kernels[s][index][degree], 2 * n[r] * n[q])
                         for index, (r, q) in enumerate(pairs)) for degree in range(5))
    alternate = list(convolution(E, E))
    alternate[0] = sub(alternate[0], bilinear(data["P"], strains[0], data["P"]))
    alternate[1] = sub(alternate[1], bilinear(data["P"], strains[s], data["P"]))
    require(Dcoeff == tuple(alternate), "F_SERIES")
    alpha, beta = parameters[s]
    matrix_E1 = scale(pairing(data["T"], strains[s]), 1, 2)
    matrix_D1 = pairing(data["R"], strains[s])
    cycl_E1 = scale(add(scale(alpha, data["N"]), real_part(kmul(beta, data["W"]), powers)), 1, 2)
    cycl_D1 = add(mul(alpha, data["D"]), real_part(kmul(beta, data["Q"]), powers))
    require(E[0] == real(data["N"]) and Dcoeff[0] == data["D"], "F_SERIES")
    require(E[1] == matrix_E1 == cycl_E1 and Dcoeff[1] == matrix_D1 == cycl_D1, "F_RESPONSE")
    directions = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, -1))
    direction = directions[s]
    curvature = total(scale(B[3 * i + j], direction[i] * direction[j])
                      for i in range(3) for j in range(3))
    pair_D2 = scale(total(scale(mul(sub(values[s][r], values[s][q]),
                                       sub(values[s][r], values[s][q])), n[r] * n[q])
                         for r, q in pairs), -1, 4)
    require(Dcoeff[2] == scale(curvature, 1, 2) == pair_D2 and sign(Dcoeff[2]) <= 0, "F_SERIES")
    occupied_values = [values[s][k] for k in range(5) if n[k]]
    equality = len(set(occupied_values)) <= 1
    require((Dcoeff[2] == ZERO) == equality, "F_HESSIAN")
    if len(occupied_values) >= 3:
        require(equality == (len(set(values[s])) == 1), "F_HESSIAN")
    fourth_moment = total(scale(mul(mul(a, a), mul(a, a)), n[k])
                          for k, a in enumerate(values[s]))
    responding = any(n[k] and values[s][k] != ZERO for k in range(5))
    require(E[4] == scale(fourth_moment, -5, 128) and sign(E[4]) <= 0
            and (sign(E[4]) < 0) == responding and (E[4] == ZERO) == (not responding), "F_SERIES")
    if not responding:
        require(all(c == ZERO for c in E[1:]), "F_SERIES")
    return E, Dcoeff


def main():
    check_authority()
    G, U, powers, parameters, strains, values, pairs, roots, kernels = make_geometry()
    payload = Payload()
    payload.emit("G", array_text(G), array_text(u for row in U for u in row))
    for s in range(4):
        payload.emit("B", s, array_text(strains[s]), array_text(values[s]))
    energy_ranks = [0, 0, 0]
    mass_ranks = [0, 0, 0]
    hessian_ranks = [0, 0, 0]
    rest_cases = 0
    count_cases = 0
    series_cases = 0
    controls = {}
    for n in product(range(5), repeat=5):
        data = preparation(n, G, U, powers)
        support, rT, rR, rest = check_preparation(n, data, G, U, powers, pairs)
        B = hessian(n, data["N"], values, pairs)
        rB = matrix_rank(B, 3)
        require(rB == (0 if support <= 1 else 1 if support == 2 else 2), "F_HESSIAN")
        energy_ranks[rT] += 1
        mass_ranks[rR] += 1
        hessian_ranks[rB] += 1
        rest_cases += int(rest)
        count_cases += 1
        ntext = ",".join(str(v) for v in n)
        payload.emit("C", ntext, data["N"], ktext(data["Z"]), ktext(data["W"]), real_text(data["D"]),
                     array_text(data["T"]), array_text(data["R"]), array_text(B), f"{rT},{rR},{rB}")
        case_series = []
        for s in range(4):
            E, Dcoeff = series(n, data, B, s, strains, values, parameters, powers, pairs, roots, kernels)
            case_series.append((E, Dcoeff))
            series_cases += 1
            payload.emit("S", ntext, s, array_text(E), array_text(Dcoeff))
        if n in ((1, 0, 0, 0, 0), (1, 0, 1, 0, 0)):
            controls[n] = (data, B, tuple(case_series))
    require(energy_ranks == [1, 20, 3104] and mass_ranks == [21, 160, 2944]
            and hessian_ranks == [21, 160, 2944] and rest_cases == 5
            and count_cases == 3125 and series_cases == 12500, "F_COUNTS")

    inverse_G = tuple(mul(v, inverse(determinant(G))) for v in (G[3], neg(G[1]), neg(G[2]), G[0]))
    unit_matrix = (ONE, ZERO, ZERO, ONE)
    require(matrix_multiply(G, inverse_G) == unit_matrix, "F_GEOMETRY")
    fibers = []
    for h in range(8):
        n = (1 + h, h, 1 + h, h, h)
        data = preparation(n, G, U, powers)
        fibers.append(data)
        base = fibers[0]
        expected_T = matrix_add(base["T"], matrix_scale(inverse_G, 5 * h, 2))
        require(data["Z"] == kadd(KONE, powers[2]) and data["N"] == 2 + 5 * h
                and data["D"] == add(real(2 + 20 * h + 25 * h * h), PHI)
                and data["W"] == base["W"] and data["P"] == base["P"]
                and data["T"] == expected_T
                and data["R"] == matrix_sub(matrix_scale(data["T"], data["N"]), outer(base["P"], base["P"])),
                "F_FIBER")
        payload.emit("F", h, data["N"], ktext(data["Z"]), ktext(data["W"]), real_text(data["D"]),
                     array_text(data["T"]), array_text(data["R"]))

    C = (ZERO, neg(ONE), ONE, sub(PHI, ONE))
    require(matrix_multiply(matrix_multiply(transpose(C), G), C) == G, "F_ROTATION")
    rotations = []
    Cpower = unit_matrix
    for r in range(5):
        n = tuple(int(k in (r, (r + 2) % 5)) for k in range(5))
        data = preparation(n, G, U, powers)
        rotations.append(data)
        base = rotations[0]
        require(data["N"] == 2 and data["D"] == add(real(2), PHI)
                and tau(data["D"]) == sub(real(3), PHI)
                and data["Z"] == kmul(powers[r], base["Z"])
                and data["W"] == kmul(powers[(2 * r) % 5], base["W"])
                and data["Q"] == kmul(powers[(2 * r) % 5], base["Q"])
                and base["Q"] == kmul(ksub(KONE, powers[2]), ksub(KONE, powers[2])), "F_ROTATION")
        require(data["P"] == matvec(Cpower, base["P"])
                and data["T"] == matrix_multiply(matrix_multiply(Cpower, base["T"]), transpose(Cpower))
                and data["R"] == matrix_multiply(matrix_multiply(Cpower, base["R"]), transpose(Cpower)),
                "F_ROTATION")
        payload.emit("O", r, ktext(data["Z"]), ktext(data["W"]), real_text(data["D"]),
                     ktext(data["Q"]), array_text(data["T"]), array_text(data["R"]))
        Cpower = matrix_multiply(C, Cpower)
    require(len({record["Q"] for record in rotations}) == 5
            and len({record["R"] for record in rotations}) == 5, "F_ROTATION")

    single, _, single_series = controls[(1, 0, 0, 0, 0)]
    pair, pair_B, pair_series = controls[(1, 0, 1, 0, 0)]
    bad_W_energy = scale(real_part(pair["Z"], powers), 1, 2)
    omitted_subtraction = matrix_sub(matrix_scale(pair["T"], pair["N"]), pair["R"])
    Hcross = (ZERO, ONE, ONE, ZERO)
    cross_actual = scale(total(scale(bilinear(U[k], Hcross, U[k]), (1, 0, 1, 0, 0)[k])
                               for k in range(5)), 1, 2)
    detections = (
        single_series[0][0][1] == real(1, 0, 2) and single_series[0][1][1] == ZERO,
        bad_W_energy != pair_series[1][0][1],
        omitted_subtraction != (ZERO,) * 4 and omitted_subtraction == outer(pair["P"], pair["P"]),
        len({(d["N"], d["D"], tau(d["D"])) for d in rotations}) == 1
        and len({d["R"] for d in rotations}) == 5,
        fibers[0]["Z"] == fibers[1]["Z"] and fibers[0]["W"] == fibers[1]["W"]
        and matrix_sub(fibers[1]["T"], fibers[0]["T"]) == matrix_scale(inverse_G, 5, 2)
        and fibers[0]["T"] != fibers[1]["T"],
        cross_actual == pair["T"][1] and cross_actual != scale(pair["T"][1], 1, 2),
        pair_series[1][1][2] != pair_B[4] and scale(pair_series[1][1][2], 2) == pair_B[4],
        single_series[0][0][4] == real(-5, 0, 128) and single_series[0][0][4] != ZERO,
    )
    for i, detected in enumerate(detections, 1):
        require(detected, "F_CONTROL")
        payload.emit("N", f"NC{i:02d}", "DETECTED")
    require(len(fibers) == 8 and len(rotations) == 5 and len(detections) == 8
            and payload.records == 15651, "F_COUNTS")

    certificate = (
        f"CERTIFICATE={PROBE}",
        "AUTHORITY_FILES=5",
        f"COUNT_CASES={count_cases}",
        "STRAIN_DIRECTIONS=4",
        "SERIES_ORDER=4",
        f"SERIES_CASES={series_cases}",
        "ENERGY_RANK_COUNTS=" + ",".join(map(str, energy_ranks)),
        "MASS_RESPONSE_RANK_COUNTS=" + ",".join(map(str, mass_ranks)),
        "HESSIAN_RANK_COUNTS=" + ",".join(map(str, hessian_ranks)),
        f"REST_CASES={rest_cases}",
        f"FIBER_CASES={len(fibers)}",
        f"ROTATION_CASES={len(rotations)}",
        f"NEGATIVE_CONTROLS={len(detections)}",
        f"PAYLOAD_RECORDS={payload.records}",
        "PAYLOAD_SHA256=" + payload.digest.hexdigest(),
        "CERTIFICATE_RESULT=PASS",
    )
    print("\n".join(certificate))


if __name__ == "__main__":
    try:
        main()
    except ScientificFailure as failure:
        print("FAILURE_CODE=" + str(failure))
        print("RESULT=FAIL")
