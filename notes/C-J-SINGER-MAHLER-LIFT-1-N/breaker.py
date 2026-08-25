#!/usr/bin/env python3
"""Blind exact breaker for C-J-SINGER-MAHLER-LIFT-1-N.

Written only from the frozen PREREG.md at public pin
49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a.

All tier decisions use Fraction/integer arithmetic.  numpy roots are printed
only after an exact negative certificate has been obtained and are labelled
RECON_ONLY.
"""

from fractions import Fraction as F
from itertools import product
from math import comb, prod as multiply
import hashlib
import json
import pathlib


TARGET = (-3, 4, -2)
P_L = 0b10011                 # X^4 + X + 1
P_R = 0b11001                 # X^4 + X^3 + 1


# ---------- Exact univariate polynomial arithmetic (ascending coefficients)

def trim(p):
    p = [F(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def deg(p):
    return len(trim(p)) - 1


def peval(p, x):
    x = F(x)
    y = F(0)
    for c in reversed(p):
        y = y * x + c
    return y


def pderiv(p):
    return trim([F(i) * p[i] for i in range(1, len(p))] or [0])


def pdivmod(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    if deg(a) < deg(b):
        return [F(0)], a
    q = [F(0)] * (deg(a) - deg(b) + 1)
    r = a[:]
    while r != [0] and deg(r) >= deg(b):
        k = deg(r) - deg(b)
        c = r[-1] / b[-1]
        q[k] += c
        for j, bj in enumerate(b):
            r[j + k] -= c * bj
        r = trim(r)
    return trim(q), trim(r)


def pmonic(p):
    p = trim(p)
    if p == [0]:
        return p
    return trim([x / p[-1] for x in p])


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, r = pdivmod(a, b)
        a, b = b, r
    return pmonic(a)


def squarefree(p):
    p = trim(p)
    g = pgcd(p, pderiv(p))
    q, r = pdivmod(p, g)
    assert r == [0]
    return pmonic(q)


def sturm_sequence(p):
    p = squarefree(p)
    seq = [p, pderiv(p)]
    while seq[-1] != [0]:
        _, r = pdivmod(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append(trim([-x for x in r]))
    return seq


def variations(values):
    s = []
    for x in values:
        if x > 0:
            s.append(1)
        elif x < 0:
            s.append(-1)
    return sum(s[i] != s[i - 1] for i in range(1, len(s)))


def sturm_count(seq, lo, hi):
    """Distinct real roots in (lo, hi); endpoints must not be roots."""
    assert peval(seq[0], lo) != 0 and peval(seq[0], hi) != 0
    return variations(peval(p, lo) for p in seq) - variations(
        peval(p, hi) for p in seq
    )


def ceil_fraction(x):
    x = F(x)
    return -((-x.numerator) // x.denominator)


def cauchy_bound(p):
    p = trim(p)
    lead = abs(p[-1])
    return 2 + max([ceil_fraction(abs(c) / lead) for c in p[:-1]] or [0])


def divide_linear(p, r):
    q, rem = pdivmod(p, [-F(r), F(1)])
    assert rem == [0]
    return q


def isolate_all_real(p, width=F(1, 10**8)):
    """Disjoint exact rational isolators for distinct real roots.

    Inputs here are monic integer divisors of monic constant-one polynomials,
    so the only possible rational roots are +1 and -1.  Those are extracted
    before dyadic bisection.
    """
    q = squarefree(p)
    exact = []
    for r in (F(-1), F(1)):
        if peval(q, r) == 0:
            exact.append((r, r))
            q = divide_linear(q, r)
    if deg(q) <= 0:
        return sorted(exact)
    seq = sturm_sequence(q)
    R = F(cauchy_bound(q))
    while peval(q, -R) == 0 or peval(q, R) == 0:
        R += 1
    out = []

    def rec(lo, hi, n):
        if n == 0:
            return
        if n == 1 and hi - lo <= width:
            out.append((lo, hi))
            return
        mid = (lo + hi) / 2
        # Any rational root would have been +/-1 and removed.
        assert peval(q, mid) != 0
        nl = sturm_count(seq, lo, mid)
        rec(lo, mid, nl)
        rec(mid, hi, n - nl)

    rec(-R, R, sturm_count(seq, -R, R))
    return sorted(exact + out)


def interval_product(i, j):
    vals = [i[0] * j[0], i[0] * j[1], i[1] * j[0], i[1] * j[1]]
    return min(vals), max(vals)


def overlaps(i, j):
    return max(i[0], j[0]) <= min(i[1], j[1])


def frac_text(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def interval_text(i):
    return f"[{frac_text(i[0])},{frac_text(i[1])}]"


# ---------- Cayley transform and exact unit-circle / side count

def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return trim(out)


def padd(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i in range(len(a)):
        out[i] += a[i]
    for i in range(len(b)):
        out[i] += b[i]
    return trim(out)


def ppow(p, n):
    out = [F(1)]
    for _ in range(n):
        out = pmul(out, p)
    return out


def cayley_coeffs(a, b, c):
    """h(s)=(1-s)^4 f((1+s)/(1-s)), ascending."""
    f = [F(1), F(c), F(b), F(a), F(1)]
    h = [F(0)]
    for k, fk in enumerate(f):
        term = pmul(ppow([1, 1], k), ppow([1, -1], 4 - k))
        h = padd(h, [fk * x for x in term])
    h += [F(0)] * (5 - len(h))
    return h[:5]


def positive_roots_quadratic(p):
    """Exact count of distinct positive roots for degree <= 2 p."""
    p = trim(p)
    if deg(p) <= 0:
        return 0
    seq = sturm_sequence(p)
    R = F(cauchy_bound(p))
    assert peval(p, F(0)) != 0
    while peval(p, R) == 0:
        R += 1
    return sturm_count(seq, F(0), R)


def has_unit_circle_root(a, b, c):
    h = cayley_coeffs(a, b, c)
    E, D, C, B, A = h
    if A == 0 or E == 0:        # x=-1 or x=+1
        return True, {"route": "endpoint", "h": tuple(h)}
    # h(i t) = (A t^4-C t^2+E) + i(-B t^3+D t).
    if B != 0:
        y = D / B
        hit = y > 0 and A * y * y - C * y + E == 0
        return hit, {"route": "imaginary-resultant", "h": tuple(h), "y": y}
    if D != 0:
        return False, {"route": "imaginary-resultant", "h": tuple(h)}
    n = positive_roots_quadratic([E, -C, A])
    return n > 0, {"route": "even-imaginary", "h": tuple(h), "positive_y": n}


def routh_generic(A, B, C, D, E):
    """RHP count for a quartic whose imaginary axis is root-free."""
    assert A != 0 and B != 0 and E != 0
    delta = B * C - A * D
    if delta == 0:
        # s^2 row first entry is epsilon -> 0+.
        signs = [A, F(1), -B * E, E]
        return variations(signs), ("epsilon-s2", signs)
    f2 = delta / B
    gamma = D * delta - B * B * E
    if gamma == 0:
        # Entire s^1 row vanishes.  Derivative of f2*s^2+E gives 2*f2.
        signs = [A, B, f2, 2 * f2, E]
        return variations(signs), ("auxiliary-s1", signs)
    g1 = gamma / delta
    signs = [A, B, f2, g1, E]
    return variations(signs), ("ordinary", signs)


def outside_root_count(a, b, c):
    unit, cert = has_unit_circle_root(a, b, c)
    if unit:
        return None, cert
    E, D, C, B, A = cayley_coeffs(a, b, c)
    if B != 0:
        n, route = routh_generic(A, B, C, D, E)
    elif D != 0:
        # Replace B by epsilon -> 0+.  Limiting first-column signs.
        signs = [A, F(1), -A * D, D, E]
        n, route = variations(signs), ("epsilon-s3", signs)
    else:
        # Entire s^3 row: derivative of A*s^4+C*s^2+E.
        n, route = routh_generic(A, 4 * A, C, 2 * C, E)
        route = ("auxiliary-s3", route)
    cert = {"h": tuple((A, B, C, D, E)), "routh": route}
    return n, cert


# ---------- Exact exterior-square root and Mahler comparison

def fpoly(a, b, c):
    return [F(1), F(c), F(b), F(a), F(1)]


def wedge_poly(a, b, c):
    # prod_{i<j}(Y-alpha_i alpha_j), ascending coefficients.
    return [
        F(1), F(-b), F(a * c - 1), F(2 * b - a * a - c * c),
        F(a * c - 1), F(-b), F(1),
    ]


def theta_cmp_rational(x):
    """Sign of rational x - theta, theta=(3+sqrt(5))/2."""
    x = F(x)
    if x <= F(3, 2):
        return -1
    q = (2 * x - 3) ** 2 - 5
    return 1 if q > 0 else (-1 if q < 0 else 0)


def factor_divides(p, q):
    _, r = pdivmod(p, q)
    return r == [0]


def signed_outside_product_interval(a, b, c):
    """Exact isolator for product of the two outside roots.

    The caller has exactly two outside roots and no unit-circle roots.
    Returns a real-root isolator of the exterior-square polynomial plus the
    product-box isolator used to identify it.
    """
    fp = fpoly(a, b, c)
    gp = wedge_poly(a, b, c)
    if deg(pgcd(fp, pderiv(fp))) > 0:
        raise RuntimeError("multiple f-root requires a separate certificate")
    for digits in (4, 6, 8, 10, 12, 14, 16):
        width = F(1, 10**digits)
        fr = isolate_all_real(fp, width)
        real_out = [i for i in fr if i[1] < -1 or i[0] > 1]
        undecided = [i for i in fr if i[0] <= -1 <= i[1] or i[0] <= 1 <= i[1]]
        if undecided:
            continue
        gr = isolate_all_real(gp, width)
        if len(real_out) == 0:
            candidates = [i for i in gr if i[0] > 1]
            if len(candidates) == 1:
                return candidates[0], candidates[0], {
                    "case": "outside-conjugate-pair",
                    "f_real_isolators": fr,
                    "wedge_real_isolators": gr,
                }
        elif len(real_out) == 2:
            box = interval_product(real_out[0], real_out[1])
            candidates = [i for i in gr if overlaps(i, box)]
            if len(candidates) == 1 and (candidates[0][1] < -1 or candidates[0][0] > 1):
                return candidates[0], box, {
                    "case": "two-real-outside",
                    "f_real_isolators": fr,
                    "wedge_real_isolators": gr,
                }
        else:
            raise RuntimeError(f"impossible distinct real-outside count {len(real_out)}")
    raise RuntimeError("failed to isolate signed outside product")


def compare_mahler(a, b, c):
    gp = wedge_poly(a, b, c)
    for digits in (5, 7, 9, 11, 13, 15, 17):
        qint, product_box, route = signed_outside_product_interval(a, b, c)
        if qint[0] > 1:
            mint = qint
            eqfactor = [F(1), F(-3), F(1)]
        elif qint[1] < -1:
            mint = (-qint[1], -qint[0])
            eqfactor = [F(1), F(3), F(1)]
        else:
            raise RuntimeError("outside product not separated from unit magnitude")
        if theta_cmp_rational(mint[1]) < 0:
            cmp = "LT"
        elif theta_cmp_rational(mint[0]) > 0:
            cmp = "GT"
        elif factor_divides(gp, eqfactor) and theta_cmp_rational(mint[0]) < 0 \
                and theta_cmp_rational(mint[1]) > 0:
            cmp = "EQ"
        else:
            # signed_outside_product_interval refines internally; in the rare
            # close case force narrower root isolation by continuing via a
            # local specialised refinement below.
            width = F(1, 10**digits)
            gr = isolate_all_real(gp, width)
            matches = [i for i in gr if overlaps(i, qint)]
            if len(matches) != 1:
                continue
            qint = matches[0]
            mint = qint if qint[0] > 0 else (-qint[1], -qint[0])
            if theta_cmp_rational(mint[1]) < 0:
                cmp = "LT"
            elif theta_cmp_rational(mint[0]) > 0:
                cmp = "GT"
            elif factor_divides(gp, eqfactor) and theta_cmp_rational(mint[0]) < 0 \
                    and theta_cmp_rational(mint[1]) > 0:
                cmp = "EQ"
            else:
                continue
        return cmp, {
            "wedge": tuple(gp),
            "signed_product": qint,
            "mahler": mint,
            "product_box": product_box,
            "route": route,
            "equality_factor": tuple(eqfactor) if cmp == "EQ" else None,
        }
    raise RuntimeError("Mahler comparison did not separate")


# ---------- F_2 controls

def gf2_deg(p):
    return p.bit_length() - 1


def gf2_mod(a, m):
    while a and gf2_deg(a) >= gf2_deg(m):
        a ^= m << (gf2_deg(a) - gf2_deg(m))
    return a


def gf2_mul(a, b, m):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
    return gf2_mod(out, m)


def gf2_pow(a, n, m):
    out = 1
    while n:
        if n & 1:
            out = gf2_mul(out, a, m)
        a = gf2_mul(a, a, m)
        n >>= 1
    return out


def gf2_gcd(a, b):
    while b:
        a, b = b, gf2_mod(a, b)
    return a


def gf2_irreducible_quartic(p):
    x = 0b10
    x4 = gf2_pow(x, 4, p)
    return gf2_pow(x, 16, p) == x and gf2_gcd(x4 ^ x, p) == 1


def gf2_order_x(p):
    x = 0b10
    y = 1
    for n in range(1, 16):
        y = gf2_mul(y, x, p)
        if y == 1:
            return n
    return None


def parity_poly(a, b, c):
    return 1 | ((c & 1) << 1) | ((b & 1) << 2) | ((a & 1) << 3) | (1 << 4)


# ---------- Frozen classes and decisions

def coefficient_member(tier, a, b, c):
    pp = parity_poly(a, b, c)
    if tier == 0:
        return pp in (P_L, P_R)
    if tier == 1:
        return pp == P_R
    if tier == 2:
        return pp == P_R and a == -3
    if tier == 3:
        return pp == P_R and a == -3 and b + c == 2
    raise ValueError(tier)


def coefficient_candidates(tier):
    out = []
    for a, b, c in product(range(-10, 11), range(-15, 16), range(-10, 11)):
        if coefficient_member(tier, a, b, c):
            out.append((a, b, c))
    # Frozen, witness-independent order: increasing L1 distance from f_J,
    # followed by lexicographic coefficients.
    return sorted(out, key=lambda t: (sum(abs(t[i] - TARGET[i]) for i in range(3)), t))


def serialize_cert(cert):
    def conv(x):
        if isinstance(x, F):
            return frac_text(x)
        if isinstance(x, tuple):
            return [conv(v) for v in x]
        if isinstance(x, list):
            return [conv(v) for v in x]
        if isinstance(x, dict):
            return {k: conv(v) for k, v in x.items()}
        return x
    return conv(cert)


def exact_record(t):
    a, b, c = t
    unit, ucert = has_unit_circle_root(a, b, c)
    if unit:
        return {"coeff": t, "state": "EXCLUDED_UNIT", "unit_cert": ucert}
    nout, rcert = outside_root_count(a, b, c)
    if nout != 2:
        return {"coeff": t, "state": "EXCLUDED_SPLIT", "outside": nout, "routh": rcert}
    cmp, mcert = compare_mahler(a, b, c)
    return {
        "coeff": t,
        "state": "IN_CLASS",
        "outside": nout,
        "comparison": cmp,
        "routh": rcert,
        "mahler_cert": mcert,
    }


def decide_tier(tier):
    rows = []
    first_negative = None
    for t in coefficient_candidates(tier):
        try:
            row = exact_record(t)
        except Exception as exc:
            return {"tier": tier, "decision": "UNDECIDED", "error_at": t, "error": repr(exc), "rows": rows}
        rows.append(row)
        if row["state"] == "IN_CLASS" and first_negative is None:
            if row["comparison"] == "LT":
                first_negative = {"tier": tier, "decision": "NEGATIVE_F_LOWER", "witness": row}
            if row["comparison"] == "EQ" and t != TARGET:
                first_negative = {"tier": tier, "decision": "NEGATIVE_F_TIE", "witness": row}
    if first_negative is not None:
        first_negative["rows_checked"] = len(rows)
        return first_negative
    return {
        "tier": tier,
        "decision": "POSITIVE_COMPLETE_WINDOW",
        "rows_checked": len(rows),
        "members_le_target": [r for r in rows if r.get("comparison") in ("LT", "EQ")],
        "complete_rows": rows,
    }


def recon_only(t):
    try:
        import numpy as np
    except Exception as exc:
        return {"label": "RECON_ONLY", "error": repr(exc)}
    a, b, c = t
    roots = np.roots([1.0, float(a), float(b), float(c), 1.0])
    mods = sorted((abs(complex(z)) for z in roots), reverse=True)
    return {
        "label": "RECON_ONLY",
        "roots": [[float(complex(z).real), float(complex(z).imag)] for z in roots],
        "moduli_desc": [float(x) for x in mods],
        "mahler_float": float(multiply(x for x in mods if x > 1.0)),
    }


def control_report():
    # Phi_5(X-1) expansion by exact binomial coefficients.
    shifted = [F(0)] * 5
    for k in range(5):
        for j in range(k + 1):
            shifted[j] += F(comb(k, j) * ((-1) ** (k - j)))
    control = exact_record(TARGET)
    return {
        "pL_irreducible": gf2_irreducible_quartic(P_L),
        "pR_irreducible": gf2_irreducible_quartic(P_R),
        "pL_order": gf2_order_x(P_L),
        "pR_order": gf2_order_x(P_R),
        "fJ_parity": parity_poly(*TARGET),
        "fJ_trace": -TARGET[0],
        "fJ_at_1": 2 + sum(TARGET),
        "Phi5_X_minus_1": tuple(shifted),
        "fJ_exact": control,
    }


def main():
    here = pathlib.Path(__file__).resolve()
    print("BREAKER_SHA256", hashlib.sha256(here.read_bytes()).hexdigest())
    print("EXACT_CONTROL", json.dumps(serialize_cert(control_report()), sort_keys=True))
    decisions = []
    for tier in range(4):
        d = decide_tier(tier)
        decisions.append(d)
        print("EXACT_DECISION", json.dumps(serialize_cert(d), sort_keys=True))
        if d["decision"].startswith("NEGATIVE"):
            print("RECON", json.dumps(recon_only(tuple(d["witness"]["coeff"])), sort_keys=True))
    assert all(d["decision"] != "UNDECIDED" for d in decisions)


if __name__ == "__main__":
    main()
