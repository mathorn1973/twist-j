#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_epsilon_guard.py -- exact verifier for ATTACK-EPSILON-GUARD.md (lane B, 2026-09-15).

STATUS: NON-CANONICAL.  Certifies only the finite algebraic pieces of the
epsilon-shadow strength guard:

  G1  formal Dirichlet identity  zeta(s)/zeta(s+eps) = sum_k prod_{p|k}(1-u_p) k^{-s}
      (u_p formal variables standing for p^{-eps}), all k <= 400;
  G2  exact step-function Mellin (Abel summation) identity on truncated models,
      integer s (exact antiderivatives), rational s with q-th-power jump points,
      and the formal linear-form version for rational s;
  G3  Laurent bookkeeping: the pole of zeta(s) at s=1 is cancelled exactly by
      c/(s-1) (G3a-c); G3d-e are truncated-Laurent bookkeeping only: given a
      simple pole of the denominator model at s=1-eps (an INPUT of the model),
      the quotient has a simple zero there and M(1-eps) = -c/eps.  G3d-e cannot
      fail for any model coefficients and certify nothing about zeta;
  G4  rational test model of the Jacobi/Parseval identity (36): orthonormality of
      sqrt(2n+3) t R_n(t), exact sum (2n+3)|a_n|^2 = ||p||^2 for p in V_N, and the
      exact Muentz deficit 1 - S_N = 1/(N+2)^2 for the constant function;
  G5  moment identification: (35) is (34) at s = k+2-delta (formal pair identity),
      the substitution t = 1/x with weight t^{-delta} on exact monomial models
      (norm and moments), and a Riemann bracket for the one power-rule integral;
  G6  arithmetic of the shadow chain (chain length, endpoint strip, mirror pair);
  G7  exponent bookkeeping of the converse (square-integrability exponent,
      Cauchy-Schwarz exponent, three-circle geometry);
  G8  reproduction of the ten published L_N enclosures (N<=32) of the note's
      verifier by a port of its interval machinery (a port self-consistency
      gate, not an independent verification: same interval class, root
      enclosure, Euler-Maclaurin routine and parameters as
      C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py).

Of the 31 checks, G3d, G3e, G4f and the tuple comparison in G5a are Fraction
identities that cannot fail for any input (transcription/bookkeeping checks);
they are kept for the record but are not independent evidence.

The analytic theorems (Hardy-space guard, shadow chain, converse) are proved in the
markdown and are NOT verified here.  Nothing here verifies RH, any zero location, or
the L^2 membership (41).

Exact arithmetic only: int and fractions.Fraction.  The DIAGNOSTIC block at the end
uses the rigorous interval machinery (ported from
C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py) to extend the L_N table to N = 64 and prints
floats; it asserts nothing.

Protocol note: the four internal consistency guards (Laurent leading coefficient,
rational exponent of the monomial model, integer root enclosure, zeta enclosure
width) raise an explicit exception instead of using bare `assert`, so they are not
stripped by python3 -O; a violation aborts with exit 1 and a traceback.

Run from a clean shell:  LC_ALL=C PYTHONHASHSEED=0 python3 verify_epsilon_guard.py
Prints one line per check (PASS/FAIL), then "CHECKS: k of n PASS"; exit 0 iff k == n.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt

PASSED = 0
TOTAL = 0


def check(cond: bool, cid: str, text: str) -> None:
    global PASSED, TOTAL
    TOTAL += 1
    if cond:
        PASSED += 1
        print(f"PASS {cid}: {text}")
    else:
        print(f"FAIL {cid}: {text}")


# ----------------------------------------------------------------------------
# Elementary arithmetic helpers
# ----------------------------------------------------------------------------

def factor(n: int):
    """Sorted list of (p, e) with n = prod p^e."""
    f = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            f.append((d, e))
        d += 1
    if n > 1:
        f.append((n, 1))
    return f


def mobius(n: int) -> int:
    f = factor(n)
    if any(e > 1 for _, e in f):
        return 0
    return (-1) ** len(f)


# Multilinear/monomial polynomials over Q in formal variables u_p:
# dict  monomial -> Fraction,  monomial = tuple of (p, exponent) sorted by p.

def padd(a, b):
    z = dict(a)
    for m, c in b.items():
        z[m] = z.get(m, F(0)) + c
    return {m: c for m, c in z.items() if c != 0}


def pmul(a, b):
    z = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            d = dict(m1)
            for p, e in m2:
                d[p] = d.get(p, 0) + e
            m = tuple(sorted(d.items()))
            z[m] = z.get(m, F(0)) + c1 * c2
    return {m: c for m, c in z.items() if c != 0}


def pconst(c):
    return {(): F(c)} if c != 0 else {}


def pvar(p):
    return {((p, 1),): F(1)}


def peval(a, val):
    """Evaluate with every u_p := val."""
    return sum((c * F(val) ** sum(e for _, e in m) for m, c in a.items()), F(0))


# ----------------------------------------------------------------------------
# G1: formal Dirichlet identity for the coefficients of zeta(s)/zeta(s+eps)
# ----------------------------------------------------------------------------

def dirichlet_convolution(a, b, K):
    z = {k: {} for k in range(1, K + 1)}
    for d in range(1, K + 1):
        if not a[d]:
            continue
        for e in range(1, K // d + 1):
            z[d * e] = padd(z[d * e], pmul(a[d], b[e]))
    return z


def group_G1():
    K = 400
    # coefficients of 1/zeta(s+eps): mu(d) u_d, u_d = prod_{p|d} u_p (squarefree d)
    inv = {}
    for d in range(1, K + 1):
        m = mobius(d)
        inv[d] = {tuple((p, 1) for p, _ in factor(d)): F(m)} if m != 0 else {}
    one = {k: pconst(1) for k in range(1, K + 1)}
    # completely multiplicative stand-in for k^{-eps}: u_k = prod u_p^e
    ucm = {k: {tuple(factor(k)): F(1)} for k in range(1, K + 1)}

    h = dirichlet_convolution(one, inv, K)
    ok_a = True
    for k in range(1, K + 1):
        prod = pconst(1)
        for p, _ in factor(k):
            prod = pmul(prod, padd(pconst(1), {((p, 1),): F(-1)}))
        ok_a &= (h[k] == prod)
    check(ok_a, "G1a", f"(1 * mu u)(k) == prod_(p|k)(1 - u_p) as polynomials over Q in u_p, all k <= {K}")

    e = dirichlet_convolution(ucm, inv, K)
    ok_b = all(e[k] == (pconst(1) if k == 1 else {}) for k in range(1, K + 1))
    check(ok_b, "G1b", f"(u * mu u)(k) == [k==1]: mu(d)u_d is the Dirichlet inverse of the completely multiplicative u_k, all k <= {K}")

    ok_c = all(peval(h[k], 0) == 1 for k in range(1, K + 1))
    ok_d = all(peval(h[k], 1) == (1 if k == 1 else 0) for k in range(1, K + 1))
    check(ok_c and ok_d, "G1c", "specialisations: u_p=0 gives h==1 (zeta(s)); u_p=1 gives h(k)==[k==1] (zeta/zeta==1)")

    # sanity on the actual sign structure: h(k) at u_p = 1/2 for all p is 2^{-omega(k)} > 0
    ok_e = all(peval(h[k], F(1, 2)) == F(1, 2 ** len(factor(k))) for k in range(1, K + 1))
    check(ok_e, "G1d", "specialisation u_p=1/2 gives h(k) == 2^(-omega(k)), all k <= 400")


# ----------------------------------------------------------------------------
# G2: exact step-function Mellin (Abel summation) identity on truncated models
# ----------------------------------------------------------------------------

def stand_in_arrays():
    """Deterministic rational stand-in coefficient arrays (finite support)."""
    arrays = []
    arrays.append([F((-1) ** (n + 1), n) for n in range(1, 13)])          # (-1)^{n+1}/n
    arrays.append([F(mobius(n), n) for n in range(1, 31)])                # mu(n)/n
    arrays.append([F(1), F(-1, 2), F(0), F(3, 4), F(-2, 3), F(5), F(0), F(-7, 9)])
    x = 7
    lcg = []
    for _ in range(20):
        x = (1103515245 * x + 12345) % 2147483648
        lcg.append(F((x % 19) - 9, (x // 19) % 7 + 1))
    arrays.append(lcg)
    return arrays


def group_G2():
    # (b1) integer s: exact antiderivative integration of the truncated F_N on [1, inf)
    ok = True
    for h in stand_in_arrays():
        N0 = len(h)
        H = [F(0)] + [sum(h[:n], F(0)) for n in range(1, N0 + 1)]  # H[n] = sum_{k<=n} h(k)
        for s in (2, 3, 4, 5, 7):
            c = F(3, 7)  # arbitrary rational stand-in for c_eps
            lhs = F(0)
            for n in range(1, N0):
                # int_n^{n+1} (c x - H(n)) x^{-s-1} dx, exact power rule for integer s
                lhs += c * (F(1, n ** (s - 1)) - F(1, (n + 1) ** (s - 1))) / (s - 1)
                lhs -= H[n] * (F(1, n ** s) - F(1, (n + 1) ** s)) / s
            # tail [N0, inf): H(floor x) == H(N0) there
            lhs += c * F(1, N0 ** (s - 1)) / (s - 1) - H[N0] * F(1, N0 ** s) / s
            rhs = c / (s - 1) - sum((h[n - 1] * F(1, n ** s) for n in range(1, N0 + 1)), F(0)) / s
            ok &= (lhs == rhs)
    check(ok, "G2a", "integer s in {2,3,4,5,7}: int_1^inf (c x - H_N(floor x)) x^{-s-1} dx == c/(s-1) - (1/s) sum h(n) n^{-s}, exact on four stand-in arrays")

    # (b2) rational s = p/q with jump points x_j = j^q (so x_j^{-s} = j^{-p} is rational)
    ok = True
    for h in stand_in_arrays():
        J = len(h)
        G = [F(0)] + [sum(h[:j], F(0)) for j in range(1, J + 1)]
        for (p, q) in ((5, 2), (7, 3), (3, 4), (11, 5), (1, 2)):
            s = F(p, q)
            xs = [j ** q for j in range(1, J + 2)]
            pw = [F(1, j ** p) for j in range(1, J + 2)]   # x_j^{-s}
            lhs = F(0)
            for j in range(1, J):
                lhs += G[j] * (pw[j - 1] - pw[j]) / s       # int_{x_j}^{x_{j+1}} G x^{-s-1} dx
            lhs += G[J] * pw[J - 1] / s                       # tail
            rhs = sum((h[j - 1] * pw[j - 1] for j in range(1, J + 1)), F(0)) / s
            ok &= (lhs == rhs)
    check(ok, "G2b", "rational s in {5/2,7/3,3/4,11/5,1/2}, jump points j^q: int_1^inf G(x) x^{-s-1} dx == (1/s) sum_j g_j x_j^{-s}, exact")

    # (b3) formal linear-form identity in symbols v_n (Abel summation), rational s
    ok = True
    for h in stand_in_arrays():
        N0 = len(h)
        H = [F(0)] + [sum(h[:n], F(0)) for n in range(1, N0 + 1)]
        for s in (F(5, 2), F(3, 7), F(1, 3)):
            lhs = {}
            for n in range(1, N0):
                lhs[n] = lhs.get(n, F(0)) + H[n] / s
                lhs[n + 1] = lhs.get(n + 1, F(0)) - H[n] / s
            lhs[N0] = lhs.get(N0, F(0)) + H[N0] / s
            rhs = {n: h[n - 1] / s for n in range(1, N0 + 1)}
            lhs = {n: v for n, v in lhs.items() if v != 0}
            rhs = {n: v for n, v in rhs.items() if v != 0}
            ok &= (lhs == rhs)
    check(ok, "G2c", "formal Abel identity: sum_n H(n)(v_n - v_{n+1})/s + H(N0) v_{N0}/s == (1/s) sum_n h(n) v_n as linear forms in v_n, rational s")

    # (b4) the linear term: int_1^inf c x x^{-s-1} dx = c/(s-1) at integer s (exact power rule)
    ok = all(F(1, 1) / (s - 1) == sum((F(1, n ** (s - 1)) - F(1, (n + 1) ** (s - 1)) for n in range(1, 10 ** 4)), F(0)) / (s - 1) + F(1, (10 ** 4) ** (s - 1)) / (s - 1) for s in (2, 3, 4))
    check(ok, "G2d", "telescoping of the exact piecewise integral of x^{-s} on [1,10^4] plus tail equals 1/(s-1), s in {2,3,4}")


# ----------------------------------------------------------------------------
# G3: Laurent bookkeeping at s = 1 and s = 1 - eps (truncated Laurent series over Q)
# ----------------------------------------------------------------------------

T = 8  # number of retained coefficients


def ls(lo, coeffs):
    c = [F(x) for x in coeffs][:T]
    c += [F(0)] * (T - len(c))
    return (lo, c)


def ls_mul(a, b):
    lo = a[0] + b[0]
    c = [F(0)] * T
    for i, x in enumerate(a[1]):
        if x == 0:
            continue
        for j, y in enumerate(b[1]):
            if i + j < T:
                c[i + j] += x * y
    return (lo, c)


def ls_inv(a):
    """Inverse of a Laurent series whose leading retained coefficient is nonzero."""
    if a[1][0] == 0:
        raise AssertionError("ls_inv: leading retained coefficient is zero")
    lo = -a[0]
    c = [F(0)] * T
    c[0] = 1 / a[1][0]
    for n in range(1, T):
        c[n] = -sum((a[1][k] * c[n - k] for k in range(1, n + 1)), F(0)) / a[1][0]
    return (lo, c)


def ls_add(a, b):
    lo = min(a[0], b[0])
    c = [F(0)] * T
    for i, x in enumerate(a[1]):
        if i + a[0] - lo < T:
            c[i + a[0] - lo] += x
    for i, x in enumerate(b[1]):
        if i + b[0] - lo < T:
            c[i + b[0] - lo] += x
    return (lo, c)


def ls_neg(a):
    return (a[0], [-x for x in a[1]])


def ls_coef(a, n):
    i = n - a[0]
    return a[1][i] if 0 <= i < len(a[1]) else F(0)


def group_G3():
    ok_res = ok_dbl = ok_c = ok_const = True
    models = [
        # (Stieltjes stand-ins g_j, zeta(s+eps) stand-ins y_j with y_0 = zeta(1+eps) stand-in)
        ([F(577, 1000), F(-73, 1000), F(-5, 1000), F(2, 1000), F(0), F(0), F(0)],
         [F(5), F(-17), F(83), F(-411), F(2000), F(1), F(1)]),
        ([F(1, 2), F(1, 3), F(1, 4), F(1, 5), F(1, 6), F(1, 7), F(1, 8)],
         [F(17, 3), F(-2), F(7, 5), F(0), F(1), F(-1), F(3)]),
        ([F(0), F(0), F(0), F(0), F(0), F(0), F(0)],
         [F(1), F(0), F(0), F(0), F(0), F(0), F(0)]),
    ]
    for g, y in models:
        Z = ls(-1, [F(1)] + g)                       # zeta(s) = 1/w + g0 + g1 w + ...   (w = s-1)
        W1 = ls(0, [F((-1) ** j) for j in range(T)])  # 1/s = 1/(1+w)
        Y = ls(0, y)                                  # zeta(s+eps) near s=1 (regular, y0 != 0)
        c = 1 / y[0]                                  # c_eps = 1/zeta(1+eps)
        Q = ls_mul(ls_mul(Z, W1), ls_inv(Y))          # zeta(s)/(s zeta(s+eps))
        L = ls_add(ls(-1, [c]), ls_neg(Q))            # M(s) = c/(s-1) - Q(s)
        ok_res &= (ls_coef(Q, -1) == c)
        ok_dbl &= (ls_coef(Q, -2) == 0 and ls_coef(L, -2) == 0)
        ok_c &= (ls_coef(L, -1) == 0)
        ok_const &= (ls_coef(L, 0) == c * (1 + y[1] / y[0] - g[0]))
    check(ok_res, "G3a", "residue of zeta(s)/(s zeta(s+eps)) at s=1 equals c = 1/zeta(1+eps) in the exact Laurent model (three stand-in models)")
    check(ok_dbl and ok_c, "G3b", "M(s) = c/(s-1) - Q(s) has vanishing (s-1)^{-2} and (s-1)^{-1} coefficients: the pole at s=1 cancels exactly")
    check(ok_const, "G3c", "constant term M(1) == c (1 + zeta'(1+eps)/zeta(1+eps) - gamma_0) in the model (exact Laurent bookkeeping)")

    # s = 1 - eps: zeta(s+eps) has a simple pole, Q has a simple zero, M(1-eps) = -c/eps
    ok_zero = ok_lead = ok_M = True
    for eps in (F(1, 4), F(1, 16), F(1, 8)):
        for g, y in models[:2]:
            Y = ls(-1, [F(1)] + y[1:])            # zeta(s+eps) = 1/w + ...   (w = s - (1-eps))
            z = ls(0, [F(-7, 3), F(1, 2), F(-1, 5), F(2), F(0), F(0), F(0), F(0)])  # zeta(s)/s near 1-eps, z0 != 0
            Q = ls_mul(z, ls_inv(Y))
            c = F(1, 5)
            # c/(s-1) = c/(w - eps) = -(c/eps) * sum_j (w/eps)^j
            Cw = ls(0, [-(c / eps) * F(1) / eps ** j for j in range(T)])
            M = ls_add(Cw, ls_neg(Q))
            ok_zero &= (ls_coef(Q, 0) == 0 and ls_coef(Q, -1) == 0)
            ok_lead &= (ls_coef(Q, 1) == z[1][0])
            ok_M &= (ls_coef(M, 0) == -c / eps)
    check(ok_zero and ok_lead, "G3d", "truncated-Laurent bookkeeping only: given a simple pole of the denominator model at s = 1-eps (model input), the quotient zeta(s)/(s zeta(s+eps)) has a simple zero there with derivative zeta(1-eps)/(1-eps); cannot fail for any model, certifies nothing about zeta")
    check(ok_M, "G3e", "truncated-Laurent bookkeeping only: M(1-eps) == -c/eps given the model of G3d (eps in {1/4,1/16,1/8}); the nonvanishing of zeta(1-eps) is proved in the text (Lemma 3.3(b)), not here")


# ----------------------------------------------------------------------------
# G4: rational test model of the Jacobi/Parseval identity (36)
# ----------------------------------------------------------------------------

def R(n: int):
    """Coefficients b_{n,k} of the note's R_n(t) = sum_k (-1)^{n-k} C(n,k) C(n+k+2,k+2) t^k."""
    return [(-1) ** (n - k) * comb(n, k) * comb(n + k + 2, k + 2) for k in range(n + 1)]


def integral_product(a, b, weight: int = 0):
    """int_0^1 a(t) b(t) t^weight dt for coefficient lists a, b."""
    return sum((F(x * y, i + j + weight + 1) for i, x in enumerate(a) for j, y in enumerate(b)), F(0))


def polymul(a, b):
    z = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return z


def test_polynomials():
    fams = []
    for j in range(0, 11):
        p = [F(0), F(1)]
        for _ in range(j):
            p = polymul(p, [F(1), F(-1)])
        fams.append(("t(1-t)^%d" % j, p))
    for d in range(1, 13):
        fams.append(("sum_{k<=%d} t^k/(k^2+1)" % d, [F(0)] + [F(1, k * k + 1) for k in range(1, d + 1)]))
    x = 11
    for d in range(3, 16):
        coeffs = [F(0)]
        for _ in range(d):
            x = (1103515245 * x + 12345) % 2147483648
            coeffs.append(F((x % 19) - 9, (x // 19) % 7 + 1))
        fams.append(("lcg degree %d" % d, coeffs))
    return fams


def group_G4():
    NMAX = 24
    tR = {n: [F(0)] + [F(v) for v in R(n)] for n in range(NMAX + 1)}
    ok = True
    for n in range(NMAX + 1):
        for m in range(NMAX + 1):
            ok &= (integral_product(tR[n], tR[m]) == (F(1, 2 * n + 3) if n == m else 0))
    check(ok, "G4a", f"int_0^1 (t R_n)(t R_m) dt == delta_nm/(2n+3) for n,m <= {NMAX}: sqrt(2n+3) t R_n(t) is orthonormal in L^2(0,1)")

    ok_def = ok_par = ok_van = ok_mono = True
    for name, p in test_polynomials():
        deg = len(p) - 1
        norm2 = integral_product(p, p)
        moments = [integral_product(p, [F(0)] * (k + 1) + [F(1)]) for k in range(deg + 4)]  # m_k = int p t^{k+1}
        S = F(0)
        prev = F(0)
        for n in range(deg + 4):
            a_n = sum((F(b) * moments[k] for k, b in enumerate(R(n))), F(0))
            a_alt = integral_product(p, [F(0)] + [F(v) for v in R(n)])
            ok_def &= (a_n == a_alt)
            if n >= deg:
                ok_van &= (a_n == 0)
            S += (2 * n + 3) * a_n * a_n
            ok_mono &= (S >= prev and S <= norm2)
            prev = S
        ok_par &= (S == norm2)
    check(ok_def, "G4b", "a_n = sum_k b_{n,k} m_k equals int_0^1 p(t) t R_n(t) dt exactly on 36 rational test polynomials")
    check(ok_par, "G4c", "sum_n (2n+3)|a_n|^2 == ||p||_{L^2(0,1)}^2 exactly for p in V_N (no additive constant), 36 test polynomials")
    check(ok_van and ok_mono, "G4d", "a_n == 0 for n >= deg p; partial sums are monotone and bounded by ||p||^2 (Bessel)")

    # constant function 1 (not in any V_N): exact Muentz deficit 1 - S_N == 1/(N+2)^2
    ok = True
    S = F(0)
    for n in range(0, 41):
        a_n = sum((F(b, k + 2) for k, b in enumerate(R(n))), F(0))
        S += (2 * n + 3) * a_n * a_n
        ok &= (1 - S == F(1, (n + 2) ** 2))
    check(ok, "G4e", "constant function: 1 - sum_{n<=N}(2n+3)|a_n|^2 == 1/(N+2)^2 exactly for N <= 40 (Muentz distance; the sum in (36) exhausts L^2(0,1))")

    # bookkeeping of the whole-domain constant: c^2/(1+2 delta) == c^2/(1+eps)
    ok = all(F(1) / (1 + 2 * (e / 2)) == F(1) / (1 + e) for e in (F(1, 4), F(1, 16), F(1, 8), F(1, 100)))
    check(ok, "G4f", "tail energy exponent bookkeeping (Fraction identity, cannot fail): int_1^inf t^{-2-2delta} dt = 1/(1+2delta) == 1/(1+eps) with delta = eps/2")

    # Rodrigues form used in Lemma 3.4: R_n(t) == ((-1)^n / n!) t^{-2} D^n [ t^{n+2} (1-t)^n ]
    ok = True
    for n in range(0, 41):
        poly = [F(0)] * (2 * n + 3)
        for j in range(n + 1):                     # t^{n+2} (1-t)^n = sum_j (-1)^j C(n,j) t^{n+2+j}
            poly[n + 2 + j] += F((-1) ** j * comb(n, j))
        for _ in range(n):                         # n-th derivative
            poly = [i * poly[i] for i in range(1, len(poly))]
        ok &= all(x == 0 for x in poly[:2])        # divisible by t^2
        rod = [F((-1) ** n, factorial(n)) * x for x in poly[2:]]
        ok &= (rod == [F(v) for v in R(n)])
    check(ok, "G4g", "Rodrigues form R_n(t) == ((-1)^n/n!) t^{-2} D^n[t^{n+2}(1-t)^n] exactly for n <= 40 (basis of the all-n orthogonality proof)")


# ----------------------------------------------------------------------------
# G5: moment identification (35) == (34) at s = k+2-delta; substitution on monomial models
# ----------------------------------------------------------------------------

def mellin_pair(s: F, eps: F):
    """M(s) = c/(s-1) - (1/s) zeta(s)/zeta(s+eps): (coef of c, zeta numerator arg, zeta denominator arg, prefactor)."""
    return (F(1) / (s - 1), s, s + eps, F(1) / s)


def moment_pair(k: int, eps: F):
    d = eps / 2
    return (F(1) / (k + 1 - d), k + 2 - d, k + 2 + d, F(1) / (k + 2 - d))


def group_G5():
    ok = True
    for eps in (F(1, 4), F(1, 16), F(1, 8), F(1, 10), F(1, 100)):
        d = eps / 2
        for k in range(0, 41):
            ok &= (mellin_pair(k + 2 - d, eps) == moment_pair(k, eps))
            # exponent bookkeeping of t = 1/x: t^{k+1-delta} dt <-> x^{-(k+2-delta)-1} dx ; |g|^2 dt <-> x^{eps-2}|F|^2 dx
            a = k + 1 - d
            ok &= (-(a) - 2 == -(k + 2 - d) - 1)
            ok &= (2 * d - 2 == eps - 2)
    check(ok, "G5a", "transcription check (Fraction identity, cannot fail): m_k(eps) is M(s) at s = k+2-delta as a formal identity (c-coefficient, zeta arguments, prefactor), k <= 40, five eps; exponent bookkeeping of t=1/x")

    # exact monomial models with X^{delta} rational: eps = p/q, X = r^{2q}
    ok_norm = ok_mom = True
    for (p, q) in ((1, 4), (1, 16), (3, 8), (1, 2)):
        eps = F(p, q)
        d = eps / 2  # = p/(2q)
        for r in (2, 3):
            X = r ** (2 * q)

            def powX(e: F):
                # X^e with e having denominator dividing 2q: X^e = r^{2q e}
                m = e * 2 * q
                if m.denominator != 1:
                    raise AssertionError("powX: exponent denominator does not divide 2q")
                m = m.numerator
                return F(r ** m) if m >= 0 else F(1, r ** (-m))

            for j in range(0, 4):
                # norm: x-side int_1^X x^{eps-2} x^{2j} dx  vs  t-side int_{1/X}^1 t^{-2 delta - 2 j} dt
                bx = 2 * j + eps - 1
                vx = (powX(bx) - 1) / bx
                bt = 1 - 2 * d - 2 * j
                vt = (1 - powX(-bt)) / bt
                ok_norm &= (vx == vt)
                for k in range(0, 7):
                    ex = j - (k + 2 - d)          # x-side exponent + 1
                    mx = (powX(ex) - 1) / ex
                    et = k + 2 - d - j            # t-side exponent + 1
                    mt = (1 - powX(-et)) / et
                    ok_mom &= (mx == mt)
    check(ok_norm, "G5b", "substitution t=1/x, g(t)=t^{-delta}F(1/t): ||F||_eps^2 == ||g||_{L^2}^2 exactly on monomial models F=x^j on [1,X], X^{delta} rational (4 eps, 2 X, 4 j)")
    check(ok_mom, "G5c", "substitution: int_0^1 g(t) t^{k+1} dt == int_1^X F(x) x^{-(k+2-delta)-1} dx exactly on the same monomial models, k <= 6")

    # Riemann bracket for the one power-rule integral used above: int_1^X x^b dx, b = a + eps
    ok = True
    for (p, q) in ((1, 4), (3, 8)):
        eps = F(p, q)
        for a in (0, 1):
            b = a + eps
            r = 2
            X = r ** (2 * q)
            V = (F(r ** (2 * q * (a + 1) + 2 * p)) - 1) / (b + 1)
            widths = []
            for M in (2, 4, 8):
                pts = [F(i, M) ** (2 * q) for i in range(M, r * M + 1)]
                vals = [F(i, M) ** (2 * q * a + 2 * p) for i in range(M, r * M + 1)]   # x_i^b exactly
                L = sum(vals[i] * (pts[i + 1] - pts[i]) for i in range(len(pts) - 1))
                U = sum(vals[i + 1] * (pts[i + 1] - pts[i]) for i in range(len(pts) - 1))
                ok &= (L <= V <= U)
                widths.append(U - L)
            ok &= (widths[0] > widths[1] > widths[2] > 0)
    check(ok, "G5d", "power-rule bracket: the closed-form value of int_1^X x^{a+eps} dx lies between exact lower and upper Riemann sums at three refinements with shrinking width")


# ----------------------------------------------------------------------------
# G6: arithmetic of the shadow chain
# ----------------------------------------------------------------------------

def group_G6():
    ok_len = ok_end = ok_mid = True
    for eps in (F(1, 4), F(1, 16), F(1, 8), F(1, 10)):
        d = eps / 2
        top = F(1, 2) + d
        beta = top
        while beta < 1:
            # chain beta, beta-eps, ... while >= 1/2 + delta (closed half-plane version)
            j = 0
            b = beta
            while b >= top:
                j += 1
                b -= eps
            jstar = (beta - top) // eps + 1
            ok_len &= (j == jstar)
            ok_end &= (F(1, 2) - d <= b < top)
            ok_mid &= all(beta - i * eps >= top for i in range(j))
            beta += F(1, 240)
    check(ok_len and ok_mid, "G6a", "chain length j* = floor((beta-1/2-delta)/eps)+1 and every intermediate point lies in Re >= 1/2+delta, rational grid of beta, four eps")
    check(ok_end, "G6b", "the chain endpoint beta - j* eps lies in the strip [1/2-delta, 1/2+delta), rational grid of beta, four eps")

    # mirror pair: rho and 1 - conj(rho) share the ordinate; they differ by exactly eps iff Re rho = 1/2 + delta
    ok = True
    for eps in (F(1, 4), F(1, 16), F(1, 8)):
        d = eps / 2
        for num in range(0, 241):
            beta = F(num, 240)
            mirror = 1 - beta
            ok &= ((beta - mirror == eps) == (beta == F(1, 2) + d))
            ok &= ((beta != mirror) == (beta != F(1, 2)))
    check(ok, "G6c", "mirror pair arithmetic: Re rho - Re(1-conj rho) == eps iff Re rho == 1/2+delta; the two differ iff Re rho != 1/2 (the 'no shared ordinate' hypothesis is RH)")

    # ladder: for beta > 1/2, the shadows beta - eps_j for eps_j = (2beta-1)/2^j, j>=1, are distinct points of the bounded segment [1-beta, beta]
    ok = True
    for beta in (F(3, 4), F(5, 8), F(17, 32), F(1, 2) + F(1, 1000)):
        pts = set()
        for j in range(1, 31):
            e = (2 * beta - 1) / 2 ** j
            ok &= (0 < e < 2 * beta - 1)
            pt = beta - e
            ok &= (1 - beta < pt < beta)
            pts.add(pt)
        ok &= (len(pts) == 30)
    check(ok, "G6d", "ladder: for Re rho = beta > 1/2 the shadows at beta - eps_j, eps_j = (2beta-1)/2^j, are 30 distinct points of the bounded segment [1-beta, beta]")


# ----------------------------------------------------------------------------
# G7: exponent bookkeeping of the converse
# ----------------------------------------------------------------------------

def group_G7():
    ok = True
    for d in (F(1, 8), F(1, 32), F(1, 16), F(1, 20), F(1, 1000), F(1, 2) - F(1, 10 ** 6)):
        sigma = F(1, 2) - d
        expo = (1 - sigma) / 2 - 1          # |Q(sigma+it)| << t^{expo + o(1)} from convexity and |1/zeta| << t^{o(1)}
        ok &= (expo == F(-3, 4) + d / 2)
        ok &= (2 * expo < -1)               # square integrable at infinity iff delta < 1/2
        ok &= (2 * sigma + 2 * d - 1 == 0)  # Cauchy-Schwarz exponent 2 sigma + eps - 1 vanishes exactly at sigma = 1/2 - delta
    ok &= not (2 * ((1 - (F(1, 2) - F(1, 2))) / 2 - 1) < -1)  # at delta = 1/2 the exponent hits -1: the bound degenerates
    check(ok, "G7a", "square-integrability exponent 2((1-sigma)/2 - 1) = -3/2 + delta < -1 on Re s = 1/2 - delta for all delta < 1/2; Cauchy-Schwarz exponent vanishes exactly at 1/2 - delta")

    ok = True
    for theta, sigma1 in ((F(1, 2), F(5, 8)), (F(1, 2), F(17, 32)), (F(5, 8) - F(1, 100), F(5, 8)),
                          (F(17, 32) - F(1, 1000), F(17, 32)), (F(3, 4), F(7, 8)), (F(1, 2), F(1, 2) + F(1, 10 ** 6))):
        eta1 = (sigma1 - theta) / 2
        Rbig = 1 - theta
        r = 1 + eta1 - sigma1
        r1 = eta1 / 2
        r2 = (r + Rbig) / 2
        ok &= (0 < r1 < r < r2 < Rbig <= F(1, 2))
        ok &= (1 + eta1 - Rbig == theta + eta1 > theta)      # big disc stays in the zero-free half-plane with margin eta1
        ok &= (1 + eta1 - r1 > 1)                             # small disc stays in Re w > 1
        ok &= (3 - Rbig > 0)                                  # big disc stays in Im w > 0 for t >= 3
        ok &= (sigma1 - (1 + eta1 - r) == 0)                  # the circle of radius r passes through sigma1 + it
    check(ok, "G7b", "three-circle geometry of Lemma 6.2: 0 < r_1 < r < r_2 < R <= 1/2, discs inside the zero-free half-plane (margin eta_1) and inside Im w > 0, six (theta, sigma_1) pairs; hence a = log(r/r_1)/log(r_2/r_1) < 1")


# ----------------------------------------------------------------------------
# Rigorous interval machinery: a port of the interval block of C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py
# (same interval class, nthroot, root enclosure, Euler-Maclaurin with N=128, p=24, GRID_BITS=256,
# ROOT_BITS=288).  Not an independent re-implementation; G8a is a port self-consistency gate.
# ----------------------------------------------------------------------------

GRID_BITS = 256
ROOT_BITS = 288


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        lo, hi = F(self.lo), F(self.hi)
        if lo > hi:
            raise ValueError("reversed interval")
        d = 1 << GRID_BITS
        object.__setattr__(self, "lo", F((lo.numerator * d) // lo.denominator, d))
        object.__setattr__(self, "hi", F(-((-hi.numerator * d) // hi.denominator), d))

    def __add__(self, other):
        o = iv(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -iv(other)

    def __rsub__(self, other):
        return iv(other) + -self

    def __mul__(self, other):
        o = iv(other)
        v = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return I(min(v), max(v))

    __rmul__ = __mul__

    def inv(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval includes zero")
        return I(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * iv(other).inv()

    def square(self):
        if self.lo >= 0:
            return I(self.lo * self.lo, self.hi * self.hi)
        if self.hi <= 0:
            return I(self.hi * self.hi, self.lo * self.lo)
        return I(F(0), max(self.lo * self.lo, self.hi * self.hi))


def iv(a):
    return a if isinstance(a, I) else I(F(a), F(a))


def nthroot(n: int, q: int) -> int:
    if n < 0 or q < 1:
        raise ValueError("root domain")
    if n < 2 or q == 1:
        return n
    if q == 2:
        return isqrt(n)
    x = 1 << ((n.bit_length() + q - 1) // q)
    while True:
        y = ((q - 1) * x + n // (x ** (q - 1))) // q
        if y >= x:
            break
        x = y
    while x ** q > n:
        x -= 1
    while (x + 1) ** q <= n:
        x += 1
    return x


@lru_cache(None)
def root_interval(n: int, q: int) -> I:
    d = 1 << ROOT_BITS
    v = n << (ROOT_BITS * q)
    r = nthroot(v, q)
    if not (r ** q <= v < (r + 1) ** q):
        raise AssertionError("root_interval: integer root enclosure failed")
    return I(F(r, d), F(r if r ** q == v else r + 1, d))


@lru_cache(None)
def reciprocal_power(n: int, s: F) -> I:
    a = s.numerator // s.denominator
    r = s - a
    q = s.denominator
    if r == 0:
        return iv(F(1, n ** a))
    if r == F(1, q):
        return root_interval(n, q).inv() * F(1, n ** a)
    if r == 1 - F(1, q):
        return root_interval(n, q) * F(1, n ** (a + 1))
    raise ValueError("unsupported exponent")


def bernoulli(n: int):
    b = [F(1)]
    for m in range(1, n + 1):
        b.append(-sum(F(comb(m + 1, k)) * b[k] for k in range(m)) / (m + 1))
    return b


B = bernoulli(48)


@lru_cache(None)
def zeta_interval(s: F) -> I:
    """Rigorous enclosure of zeta(s), real s > 1, Euler-Maclaurin with N=128 direct terms and p=24."""
    if s <= 1:
        raise ValueError("only absolutely convergent real zeta values")
    N = 128
    p = 24
    a = reciprocal_power(N, s)
    val = sum((reciprocal_power(n, s) for n in range(1, N)), iv(0))
    val += a * (F(N) / (s - 1) + F(1, 2))
    rising = F(1)
    for k in range(1, 2 * p):
        rising *= s + k - 1
        if k % 2 == 1:
            j = (k + 1) // 2
            val += a * (B[2 * j] * rising / F(factorial(2 * j) * N ** k))
    sup = sum(F(comb(2 * p, k)) * abs(B[k]) for k in range(2 * p + 1))
    err = a.hi * sup * rising / F(factorial(2 * p) * N ** (2 * p - 1))
    out = I(val.lo - err, val.hi + err)
    if not (out.lo > 0 and out.hi - out.lo < F(1, 10 ** 40)):
        raise AssertionError("zeta_interval: enclosure not positive or too wide")
    return out


def coarse(i: I, d: int = 10 ** 12):
    return ((i.lo.numerator * d) // i.lo.denominator, -((-i.hi.numerator * d) // i.hi.denominator))


def moment_energies(eps: F, NMAX: int):
    """Returns (c, list of (n, L_n interval)) for n = 0..NMAX with the note's moments (35)."""
    d = eps / 2
    c = zeta_interval(1 + eps).inv()
    moments = []
    for k in range(NMAX + 1):
        sm = F(k + 2) - d
        sp = F(k + 2) + d
        moments.append(c / (F(k + 1) - d) - zeta_interval(sm) / (sm * zeta_interval(sp)))
    E = iv(0)
    out = []
    for n in range(NMAX + 1):
        bn = sum((moments[k] * v for k, v in enumerate(R(n))), iv(0))
        E += (2 * n + 3) * bn.square()
        out.append((n, c.square() / (1 + eps) + E))
    return c, out


PUBLISHED = {
    # coarse enclosures printed by C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py (from its _EXPECTED.txt)
    (F(1, 4), 0): (442144934508, 442144934509),
    (F(1, 4), 4): (574428336006, 574428336007),
    (F(1, 4), 8): (593159495461, 593159495462),
    (F(1, 4), 16): (602913453309, 602913453310),
    (F(1, 4), 32): (608193475644, 608193475645),
    (F(1, 16), 0): (649629624472, 649629624473),
    (F(1, 16), 4): (846886792419, 846886792420),
    (F(1, 16), 8): (865126082363, 865126082364),
    (F(1, 16), 16): (872724018346, 872724018347),
    (F(1, 16), 32): (875502085954, 875502085955),
}

TABLES = {}


def group_G8():
    ok = True
    for eps in (F(1, 4), F(1, 16)):
        c, tab = moment_energies(eps, 64)
        TABLES[eps] = tab
        for n, L in tab:
            if (eps, n) in PUBLISHED:
                ok &= (coarse(L) == PUBLISHED[(eps, n)])
    check(ok, "G8a", "port self-consistency gate: the port of the note's interval machinery reproduces all ten published coarse L_N enclosures (N in {0,4,8,16,32}, eps in {1/4,1/16}) of the note's verifier exactly")


def diagnostic():
    print("DIAGNOSTIC (rigorous-interval enclosures printed as floats; this block asserts nothing):")
    print("DIAGNOSTIC  L_N(eps) = c^2/(1+eps) + sum_{n<=N}(2n+3)|a_n(eps)|^2, enclosure midpoint, width, and increment over the previous printed N.")
    print("DIAGNOSTIC  Finiteness of the limit N -> infinity is exactly the open target (41); finite partial sums decide nothing.")
    for eps in (F(1, 4), F(1, 16)):
        tab = TABLES[eps]
        prev = None
        for n, L in tab:
            if n in (0, 4, 8, 16, 24, 32, 40, 48, 56, 64):
                mid = float((L.lo + L.hi) / 2)
                wid = float(L.hi - L.lo)
                inc = "" if prev is None else f"  increment={mid - prev:+.12f}"
                print(f"DIAGNOSTIC  eps={eps}  N={n:2d}  L_N={mid:.12f}  width={wid:.3e}{inc}")
                prev = mid
        # crude tail read: last eight one-step increments
        steps = [float((tab[n][1].lo + tab[n][1].hi) / 2 - (tab[n - 1][1].lo + tab[n - 1][1].hi) / 2) for n in range(57, 65)]
        print("DIAGNOSTIC  eps=%s  one-step increments (2n+3)|a_n|^2 for n=57..64: %s" % (eps, " ".join(f"{v:.3e}" for v in steps)))


def main():
    group_G1()
    group_G2()
    group_G3()
    group_G4()
    group_G5()
    group_G6()
    group_G7()
    group_G8()
    diagnostic()
    print(f"CHECKS: {PASSED} of {TOTAL} PASS")
    sys.exit(0 if PASSED == TOTAL else 1)


if __name__ == "__main__":
    main()
