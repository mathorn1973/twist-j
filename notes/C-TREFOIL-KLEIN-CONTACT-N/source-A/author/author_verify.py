#!/usr/bin/env python3
"""Auxiliary exact checks of the frozen marked Klein coordinate candidate.

Not a public P-probe. Arithmetic: Q[j]/Phi_5, represented in the power basis.
Homogeneous binary forms are represented by coefficients of u^i v^(n-i).
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json
import platform
import sys

ROOT = Path(__file__).resolve().parent
PREREG_HASH = "d64ab46179bfe2acfaae3f61cbfdc9adc3c3c6a9e1048a92987d0e5bf7218053"
ZERO = (Q(0),) * 4

def ki(n):
    return (Q(n), Q(0), Q(0), Q(0))

ONE = ki(1)
JROOT = (Q(0), Q(1), Q(0), Q(0))

def add(x, y):
    return tuple(x[i] + y[i] for i in range(4))

def neg(x):
    return tuple(-v for v in x)

def sub(x, y):
    return add(x, neg(y))

def scale(q, x):
    return tuple(q * v for v in x)

def mul(x, y):
    z = [Q(0)] * 7
    for i, xi in enumerate(x):
        if xi:
            for k, yk in enumerate(y):
                if yk:
                    z[i + k] += xi * yk
    for degree in range(6, 3, -1):
        lead = z[degree]
        if lead:
            for k in range(4):
                z[degree - 4 + k] -= lead
    return tuple(z[:4])

def powk(x, n):
    result = ONE
    while n:
        if n & 1:
            result = mul(result, x)
        x = mul(x, x)
        n >>= 1
    return result

def galois(x, k):
    result = ZERO
    for i, xi in enumerate(x):
        result = add(result, scale(xi, powk(JROOT, i * k)))
    return result

def norm(x):
    result = ONE
    for k in (1, 2, 3, 4):
        result = mul(result, galois(x, k))
    assert result[1:] == (0, 0, 0)
    return result[0]

def inv(x):
    if x == ZERO:
        raise ZeroDivisionError("zero in K")
    product = ONE
    for k in (2, 3, 4):
        product = mul(product, galois(x, k))
    return scale(1 / norm(x), product)

def valuation(x):
    if x == ZERO:
        return None
    n = norm(x)
    num, den = abs(n.numerator), n.denominator
    value = 0
    while num % 5 == 0:
        value += 1
        num //= 5
    while den % 5 == 0:
        value -= 1
        den //= 5
    return value

def integral(x):
    return all(v.denominator == 1 for v in x)

def residue(x):
    assert integral(x)
    return sum(v.numerator for v in x) % 5

def matmul(A, B):
    return tuple(tuple(add(mul(A[i][0], B[0][k]), mul(A[i][1], B[1][k]))
                       for k in range(2)) for i in range(2))

def det(A):
    return sub(mul(A[0][0], A[1][1]), mul(A[0][1], A[1][0]))

def matinv(A):
    d = inv(det(A))
    return ((mul(d, A[1][1]), neg(mul(d, A[0][1]))),
            (neg(mul(d, A[1][0])), mul(d, A[0][0])))

def adjoint(A):
    return tuple(tuple(galois(A[k][i], 4) for k in range(2)) for i in range(2))

def matvec(A, v):
    return tuple(add(mul(A[i][0], v[0]), mul(A[i][1], v[1])) for i in range(2))

def form(n, terms):
    return (n, tuple(terms.get(i, ZERO) for i in range(n + 1)))

def padd(p, q):
    assert p[0] == q[0]
    return (p[0], tuple(add(x, y) for x, y in zip(p[1], q[1])))

def pscale(c, p):
    return (p[0], tuple(mul(c, x) for x in p[1]))

def psub(p, q):
    return padd(p, pscale(ki(-1), q))

def pmul(p, q):
    result = [ZERO] * (p[0] + q[0] + 1)
    for i, x in enumerate(p[1]):
        if x != ZERO:
            for k, y in enumerate(q[1]):
                if y != ZERO:
                    result[i + k] = add(result[i + k], mul(x, y))
    return (p[0] + q[0], tuple(result))

PONE = form(0, {0: ONE})

def ppow(p, n):
    result = PONE
    for _ in range(n):
        result = pmul(result, p)
    return result

def pdiff(p, variable):
    n, coeff = p
    if variable == 0:
        return (n - 1, tuple(scale(i + 1, coeff[i + 1]) for i in range(n)))
    return (n - 1, tuple(scale(n - i, coeff[i]) for i in range(n)))

def jacobian(p, q):
    return psub(pmul(pdiff(p, 0), pdiff(q, 1)),
                pmul(pdiff(p, 1), pdiff(q, 0)))

def hessian(p):
    pu, pv = pdiff(p, 0), pdiff(p, 1)
    return psub(pmul(pdiff(pu, 0), pdiff(pv, 1)), ppow(pdiff(pu, 1), 2))

def substitute(p, A):
    # Column action: u -> A00*u+A01*v, v -> A10*u+A11*v.
    linear_u = form(1, {0: A[0][1], 1: A[0][0]})
    linear_v = form(1, {0: A[1][1], 1: A[1][0]})
    up, vp = [PONE], [PONE]
    for _ in range(p[0]):
        up.append(pmul(up[-1], linear_u))
        vp.append(pmul(vp[-1], linear_v))
    result = form(p[0], {})
    for i, coefficient in enumerate(p[1]):
        if coefficient != ZERO:
            result = padd(result, pscale(coefficient, pmul(up[i], vp[p[0] - i])))
    return result

def peval(p, vector):
    result = ZERO
    for i, coefficient in enumerate(p[1]):
        result = add(result, mul(coefficient, mul(powk(vector[0], i),
                                                 powk(vector[1], p[0] - i))))
    return result

def pvaluation(p):
    return min(valuation(x) for x in p[1] if x != ZERO)

def pintegral(p):
    return all(integral(x) for x in p[1])

def pred(p):
    return tuple(residue(x) for x in p[1])

checks = []

def check(name, condition, observed=None):
    item = {"id": name, "pass": bool(condition)}
    if observed is not None:
        item["observed"] = observed
    checks.append(item)

def main():
    actual_prereg = hashlib.sha256((ROOT / "PREREG.md").read_bytes()).hexdigest()
    check("PREREG_SHA256", actual_prereg == PREREG_HASH, actual_prereg)
    if actual_prereg != PREREG_HASH:
        raise RuntimeError("preregistration changed")
    j = JROOT
    a = add(j, powk(j, 4))
    s = sub(powk(j, 2), powk(j, 3))
    r = sub(j, powk(j, 4))
    J = add(ONE, powk(j, 2))
    check("a_quadratic", add(powk(a, 2), a) == ONE)
    check("s_square", powk(s, 2) == sub(a, ki(2)))
    check("s_fourth", powk(s, 4) == scale(5, powk(a, 2)))
    check("r_ratio", r == mul(s, inv(a)))
    check("a_square_plus_s_square", add(powk(a, 2), powk(s, 2)) == ki(-1))
    check("conjugation", galois(a, 4) == a and galois(s, 4) == neg(s))
    check("J_identity", J == mul(a, j))
    check("scalar_valuations", [valuation(s), valuation(ki(5))] == [1, 4])

    S = ((ZERO, ki(-1)), (ONE, ZERO))
    T = ((j, ONE), (ZERO, powk(j, 4)))
    P = ((ONE, neg(a)), (ZERO, s))
    B = ((s, a), (ZERO, ONE))
    D = ((j, ZERO), (ZERO, powk(j, 4)))
    E = ((inv(r), inv(s)), (inv(s), neg(inv(r))))
    I = ((ONE, ZERO), (ZERO, ONE))
    MINUS_I = ((ki(-1), ZERO), (ZERO, ki(-1)))
    Pinv = matinv(P)
    check("P_B_determinants", det(P) == s and det(B) == s)
    check("P_nonunit_determinant", valuation(det(P)) == 1)
    check("B_scaled_inverse", B == tuple(tuple(mul(s, z) for z in row) for row in Pinv))
    check("T_conjugacy", matmul(matmul(Pinv, T), P) == D)
    check("S_conjugacy", matmul(matmul(Pinv, S), P) == E)
    check("B_intertwines_T", matmul(B, T) == matmul(D, B))
    check("B_intertwines_S", matmul(B, S) == matmul(E, B))
    check("standard_determinants", det(D) == ONE and det(E) == ONE)
    check("E_square", matmul(E, E) == MINUS_I)
    check("standard_unitarity", matmul(adjoint(D), D) == I and matmul(adjoint(E), E) == I)
    red_T = [[residue(z) for z in row] for row in T]
    red_D = [[residue(z) for z in row] for row in D]
    check("ramified_conjugacy_obstruction", red_T == [[1, 1], [0, 1]] and red_D == [[1, 0], [0, 1]],
          {"T": red_T, "D": red_D})

    f0 = form(12, {11: ONE, 6: ki(11), 1: ki(-1)})
    H0 = form(20, {20: ki(-1), 0: ki(-1), 15: ki(228), 5: ki(-228), 10: ki(-494)})
    W0 = form(30, {30: ONE, 0: ONE, 25: ki(522), 5: ki(-522), 20: ki(-10005), 10: ki(-10005)})
    check("standard_klein_relation", padd(ppow(W0, 2), ppow(H0, 3)) == pscale(ki(1728), ppow(f0, 5)))
    check("standard_hessian", hessian(f0) == pscale(ki(121), H0))
    check("standard_jacobian", jacobian(f0, H0) == pscale(ki(20), W0))

    fhat, Hhat, What = (substitute(polynomial, B) for polynomial in (f0, H0, W0))
    F, H, W = (pscale(inv(powk(s, power)), polynomial)
               for polynomial, power in zip((fhat, Hhat, What), (10, 20, 25)))
    all_forms = {"fhat": fhat, "Hhat": Hhat, "What": What, "F": F, "H": H, "W": W}
    for name, polynomial in all_forms.items():
        check(name + "_integral", pintegral(polynomial))
        check(name + "_S_invariant", substitute(polynomial, S) == polynomial)
        check(name + "_T_invariant", substitute(polynomial, T) == polynomial)
    vals_hat = [pvaluation(p) for p in (fhat, Hhat, What)]
    vals_primitive = [pvaluation(p) for p in (F, H, W)]
    check("hat_valuations", vals_hat == [10, 20, 25], vals_hat)
    check("primitive_valuations", vals_primitive == [0, 0, 0], vals_primitive)
    check("marked_unscaled_relation", padd(ppow(What, 2), ppow(Hhat, 3)) == pscale(ki(1728), ppow(fhat, 5)))
    check("marked_primitive_relation", padd(ppow(W, 2), pscale(powk(s, 10), ppow(H, 3))) == pscale(ki(1728), ppow(F, 5)))
    check("marked_jacobian", W == pscale(scale(Q(1, 4), powk(a, 2)), jacobian(F, H)))

    E6 = form(6, {5: ONE, 1: ki(-1)})
    P5 = form(5, {5: ONE, 1: ki(-1)})
    D20 = padd(ppow(P5, 4), form(20, {0: ONE}))
    check("F_reduction", pred(F) == pred(pscale(ki(2), ppow(E6, 2))))
    check("H_reduction", pred(H) == pred(pscale(ki(4), D20)))
    check("W_reduction", pred(W) == pred(pscale(ki(4), ppow(E6, 5))))

    fK, HK, WK = pscale(inv(powk(s, 2)), F), H, pscale(inv(powk(s, 5)), W)
    check("K_pullbacks", all(p == substitute(q, Pinv) for p, q in zip((fK, HK, WK), (f0, H0, W0))))
    check("K_standard_relation", padd(ppow(WK, 2), ppow(HK, 3)) == pscale(ki(1728), ppow(fK, 5)))
    vals_K = [pvaluation(p) for p in (fK, HK, WK)]
    check("K_valuations", vals_K == [-2, 0, -5], vals_K)

    v0 = (neg(a), powk(j, 2))
    M = ((ONE, mul(a, inv(s))), (neg(mul(a, inv(s))), ONE))
    check("M_pullback", M == matmul(adjoint(Pinv), Pinv))
    check("fixed_J_point_transport", matvec(B, v0) == (mul(powk(j, 2), J), powk(j, 2)))
    check("fixed_J_point_branch", peval(f0, (J, ONE)) == ZERO and peval(F, v0) == ZERO)
    check("M_determinant_trace", det(M) == neg(inv(powk(s, 2))) and add(M[0][0], M[1][1]) == ki(2))
    check("M_S_invariance", matmul(matmul(adjoint(S), M), S) == M)
    check("M_T_invariance", matmul(matmul(adjoint(T), M), T) == M)
    Mv0 = matvec(M, v0)
    norm_v0 = add(mul(galois(v0[0], 4), Mv0[0]), mul(galois(v0[1], 4), Mv0[1]))
    check("fixed_J_point_unit_norm", norm_v0 == ONE)

    serialized = {}
    for name, polynomial in {**all_forms, "fK": fK, "HK": HK, "WK": WK}.items():
        serialized[name] = {"degree": polynomial[0], "coefficients_u_power_ascending":
                            [[str(v) for v in coefficient] for coefficient in polynomial[1]]}
    (ROOT / "author-polynomials.json").write_text(json.dumps(serialized, indent=2, sort_keys=True) + "\n")

if __name__ == "__main__":
    main()
    passed = all(item["pass"] for item in checks)
    report = {"status": "PASS" if passed else "FAIL", "classification": "NON-CANONICAL auxiliary exact checks",
              "prereg_sha256": PREREG_HASH,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "python": platform.python_version(), "architecture": platform.machine(),
              "arithmetic": "exact rational power basis modulo Phi_5; no floating-point scientific evaluation",
              "check_count": len(checks), "checks": checks}
    content = json.dumps(report, indent=2, sort_keys=True) + "\n"
    (ROOT / "author-report.json").write_text(content)
    print(content, end="")
    sys.exit(0 if passed else 1)
