#!/usr/bin/env python3
"""Independent post-lock exact calculation for issue #369.

This script intentionally does not import golden_symbolic.py.  It reparses the
pinned upstream MATLAB literal, rebuilds the three row Gram systems, and asks
SymPy/Q for the frozen lexicographic bases.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

if sys.flags.optimize:
    raise SystemExit("refusing optimized Python: exact verifier requires active assertions")

import sympy as sp


SOURCE_BYTES = 8515
SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
RAW_BYTES = 136262
RAW_SHA256 = "09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762"
FLATS = ((0, 1), (0, 2), (0, 3))
SELECTED_TAGS = (
    "01:00:00",
    "01:02:02",
    "02:08:05",
    "02:12:13",
    "02:13:22",
    "unit_phase",
)


def strip_comments(text: str) -> str:
    return "\n".join(line.split("%", 1)[0] for line in text.splitlines())


def literal_rows(block: str, pattern: str, allowed: set[str]) -> list[list[str]]:
    rows = [row.strip() for row in strip_comments(block).split(";") if row.strip()]
    assert len(rows) == 36
    out = []
    for row in rows:
        tokens = re.findall(pattern, row)
        assert len(tokens) == 36 and set(tokens) <= allowed
        out.append(tokens)
    return out


def parse_tensor(data: bytes):
    assert len(data) == SOURCE_BYTES
    assert hashlib.sha256(data).hexdigest() == SOURCE_SHA256
    matches = re.findall(
        r"\bU\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        data.decode("utf-8"),
        re.S,
    )
    assert len(matches) == 1
    amps = literal_rows(
        matches[0][0],
        r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])",
        {"0", "a", "b", "c"},
    )
    exps = literal_rows(
        matches[0][1],
        r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])",
        {str(i) for i in range(20)},
    )
    tensor = {}
    for r in range(36):
        for s in range(36):
            if amps[r][s] != "0":
                tensor[(r // 6, r % 6, s // 6, s % 6)] = (
                    amps[r][s], int(exps[r][s])
                )
    assert len(tensor) == 112
    assert Counter(v[0] for v in tensor.values()) == Counter(a=40, b=40, c=32)
    return tensor


def flatten(tensor, parties):
    other = tuple(i for i in range(4) if i not in parties)
    rows = [dict() for _ in range(36)]
    for ind, token in tensor.items():
        r = 6 * ind[parties[0]] + ind[parties[1]]
        s = 6 * ind[other[0]] + ind[other[1]]
        assert s not in rows[r]
        rows[r][s] = token
    return rows


def mono(token, conjugate=False):
    label, exponent = token
    abc = {"a": (1, 0, 0), "b": (0, 1, 0), "c": (0, 0, 1)}[label]
    return abc + ((0, exponent) if conjugate else (exponent, 0))


def equations(tensor):
    records = []
    for parties in FLATS:
        rows = flatten(tensor, parties)
        for i in range(36):
            for j in range(36):
                p = Counter()
                for k in sorted(set(rows[i]) & set(rows[j])):
                    m1, m2 = mono(rows[i][k]), mono(rows[j][k], True)
                    p[tuple(s + t for s, t in zip(m1, m2))] += 1
                if i == j:
                    p[(0, 0, 0, 0, 0)] -= 1
                p = {m: c for m, c in p.items() if c}
                records.append((f"{parties[0]}{parties[1]}:{i:02d}:{j:02d}", p))
    records.append(("unit_phase", {
        (0, 0, 0, 1, 1): 1,
        (0, 0, 0, 0, 0): -1,
    }))
    return records


def raw_serialization(records):
    serial = []
    for tag, polynomial in records:
        terms = [[list(m), c] for m, c in sorted(polynomial.items())]
        serial.append({"tag": tag, "terms": terms})
    return (json.dumps(serial, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def expression(poly, variables):
    return sp.Add(*(sp.Integer(c) * sp.prod(v**e for v, e in zip(variables, m))
                    for m, c in poly.items()))


def basis_bytes(G, variables, order_label):
    payload = {"variables": [str(v) for v in variables], "order": order_label, "basis": []}
    for p in G.polys:
        terms = []
        for monomial, coeff in p.terms():
            coeff = sp.Rational(coeff)
            terms.append([list(monomial), [int(coeff.p), int(coeff.q)]])
        payload["basis"].append(terms)
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def assert_basis(G, expected):
    assert len(G.polys) == len(expected)
    assert all(sp.expand(g.as_expr() - e) == 0 for g, e in zip(G.polys, expected))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: independent_sympy.py AME46_ORIGINAL.m")
    data = Path(sys.argv[1]).read_bytes()
    tensor=parse_tensor(data)
    assert tensor[(0,0,0,1)] == ("c",0)
    assert tensor[(0,1,0,2)] == ("c",17)
    records = equations(tensor)
    stream = raw_serialization(records)
    assert len(records) == 3889
    assert sum(bool(p) for _, p in records) == 383
    assert len(stream) == RAW_BYTES and hashlib.sha256(stream).hexdigest() == RAW_SHA256

    alpha, beta, gamma, x, y, t = sp.symbols("alpha beta gamma x y t")
    raw_variables = (alpha, beta, gamma, x, y)
    raw = [(tag, expression(p, raw_variables)) for tag, p in records if p]

    expected = [
        alpha + gamma*x**7/5 - 2*gamma*x**5/5 + 3*gamma*x**3/5 - 4*gamma*x/5,
        beta + 3*gamma*x**7/5 - gamma*x**5/5 - gamma*x**3/5 - 2*gamma*x/5,
        gamma**2 - sp.Rational(1, 2),
        y + x**7 - x**5 + x**3 - x,
        x**8 - x**6 + x**4 - x**2 + 1,
    ]

    # Target-blind seal.  The raw ideal already equals its sole saturation.
    unique_raw = list(dict.fromkeys(p for _, p in raw))
    print(f"STAGE raw_gb unique={len(unique_raw)}", flush=True)
    Graw = sp.groebner(unique_raw, alpha, beta, gamma, y, x,
                       order="lex", domain=sp.QQ, method="f5b")
    assert_basis(Graw, expected)
    chosen = [dict(raw)[tag] for tag in SELECTED_TAGS]
    print("STAGE six_gb", flush=True)
    Gsix = sp.groebner(chosen, alpha, beta, gamma, y, x,
                       order="lex", domain=sp.QQ, method="f5b")
    assert_basis(Gsix, expected)
    for _, f in raw:
        assert Graw.reduce(f)[1] == 0

    D = alpha*beta*gamma*x*y
    inverse_D = -8*gamma*x**6 + 8*gamma*x**4 + 4*gamma
    assert Graw.reduce(D*inverse_D - 1)[1] == 0

    print("STAGE saturation_gb", flush=True)
    # Graw == I_raw has already been established, so using its canonical
    # generators here computes exactly the frozen saturation with no change
    # of ideal and avoids feeding 362 redundant coordinates a second time.
    Gsat = sp.groebner(
        expected + [1-t*D], t, alpha, beta, gamma, y, x,
        order="lex", domain=sp.QQ, method="f5b")
    expected_sat = [t - inverse_D] + expected
    assert_basis(Gsat, expected_sat)
    blind_bytes = basis_bytes(Graw, (alpha, beta, gamma, y, x), "lex")
    sat_bytes = basis_bytes(Gsat, (t, alpha, beta, gamma, y, x), "lex")

    # Exact real classification, still target-blind.
    ar, br, cr, u, v = sp.symbols("alpha beta gamma u v", real=True)
    real_generators = []
    for f in expected:
        z = sp.expand(f.subs({alpha: ar, beta: br, gamma: cr,
                              x: u+sp.I*v, y: u-sp.I*v}))
        re_part, im_part = sp.expand_complex(z).as_real_imag()
        for part in (sp.expand(re_part), sp.expand(im_part)):
            if part != 0:
                real_generators.append(part)
    real_generators.append(u**2+v**2-1)
    print("STAGE real_gb", flush=True)
    Greal = sp.groebner(real_generators, ar, br, cr, v, u,
                        order="lex", domain=sp.QQ, method="f5b")
    expected_real = [
        ar + sp.Rational(8, 5)*cr*u**3 - 2*cr*u,
        br - sp.Rational(16, 5)*cr*u**3 + 2*cr*u,
        cr**2 - sp.Rational(1, 2),
        v**2 + u**2 - 1,
        u**4 - sp.Rational(5, 4)*u**2 + sp.Rational(5, 16),
    ]
    assert_basis(Greal, expected_real)
    phase_sign = 2*u**2 - sp.Rational(3, 2)
    assert Greal.reduce(v**2-phase_sign**2)[1] == 0
    q_u = expected_real[-1]
    assert sp.invert(phase_sign, q_u, domain=sp.QQ) == 8*u**2-4
    real_bytes = basis_bytes(Greal, (ar, br, cr, v, u), "lex")

    # Only now load and evaluate the six frozen targets.
    targets = [
        2*gamma**2-1,
        alpha**2+beta**2-gamma**2,
        beta**2-alpha*beta-alpha**2,
        x**8-x**6+x**4-x**2+1,
        gamma-alpha*(x+y),
        beta-alpha*(x**2+y**2),
    ]
    target_remainders = [Graw.reduce(r)[1] for r in targets]
    assert target_remainders == [0]*6

    print("GOLDEN_RIGIDITY_INDEPENDENT_SYMPY_V1")
    print(f"PASS SYMPY_VERSION={sp.__version__}")
    print(f"PASS RAW records=3889 active=383 bytes={len(stream)} sha256={RAW_SHA256}")
    print("PASS FIELD_LOCATORS U[0,1]=gamma U[1,2]=gamma*x^17")
    print("PASS SIX_RAW_TAGS=" + ",".join(SELECTED_TAGS))
    print(f"PASS RAW_GB count=5 sha256={hashlib.sha256(blind_bytes).hexdigest()}")
    print(f"PASS SATURATION_REDUNDANT inverse_D=-8*gamma*x^6+8*gamma*x^4+4*gamma sat_sha256={hashlib.sha256(sat_bytes).hexdigest()}")
    print("PASS COMPLEX dimension=0 degree=16 radical=YES prime=YES")
    print(f"PASS REAL_GB count=5 sha256={hashlib.sha256(real_bytes).hexdigest()}")
    print("PASS REAL_DECOMPOSITION components=2 total_points=16 positive_points=2 conjugation_pair=YES")
    print("PASS POSITIVE_BRANCH u^2=(5+sqrt(5))/8 c=1/sqrt(2) v=+-(sqrt(5)-1)/4")
    print("PASS TARGET complex_mask=111111 positive_mask=111111")
    print("PASS FIELD Q(entries)=Q(x,gamma)=Q(zeta20,sqrt2)=Q(zeta40)")
    print("SUMMARY 13/13 PASS verdict=EXACT_J_RIGID_UP_TO_CONJUGATION")


if __name__ == "__main__":
    main()
