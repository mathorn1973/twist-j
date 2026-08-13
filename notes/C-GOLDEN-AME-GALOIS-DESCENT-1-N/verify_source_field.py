#!/usr/bin/env python3
"""Exact G0/G1 verifier for the pinned AME(4,6) source.

No numerical tolerance is used.  Arithmetic is performed in
    K = Q[z] / (Phi_40(z)),  Phi_40 = z^16-z^12+z^8-z^4+1,
with rational coefficients represented by fractions.Fraction.

The source parser intentionally reads the two 36 x 36 MATLAB literals rather
than copying their data into this verifier.  It therefore also checks that the
pinned source has the expected byte and Git-blob hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable


EXPECTED_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
EXPECTED_GIT_BLOB_SHA1 = "e0d0e171d58b3360c39595d677ffc401a466112d"
EXPECTED_BYTES = 8515
PINNED_COMMIT = "1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8"

# Low-to-high coefficients of Phi_40(x)=x^16-x^12+x^8-x^4+1.
MODULUS = tuple(
    Fraction(x)
    for x in (1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1)
)
DEGREE = 16


def _trim(p: list[Fraction]) -> list[Fraction]:
    while p and p[-1] == 0:
        p.pop()
    return p


def _padd(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return _trim([
        (a[i] if i < len(a) else Fraction(0))
        + (b[i] if i < len(b) else Fraction(0))
        for i in range(n)
    ])


def _psub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return _trim([
        (a[i] if i < len(a) else Fraction(0))
        - (b[i] if i < len(b) else Fraction(0))
        for i in range(n)
    ])


def _pmul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] += ai * bj
    return _trim(out)


def _pdivmod(a: list[Fraction], b: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    a = _trim(a[:])
    b = _trim(b[:])
    if not b:
        raise ZeroDivisionError("polynomial division by zero")
    if len(a) < len(b):
        return [], a
    q = [Fraction(0)] * (len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        q[k] += c
        for j, bj in enumerate(b):
            a[k + j] -= c * bj
        _trim(a)
    return _trim(q), a


def _reduce(coeffs: Iterable[Fraction | int]) -> tuple[Fraction, ...]:
    p = [Fraction(x) for x in coeffs]
    # x^16 = x^12 - x^8 + x^4 - 1.
    for k in range(len(p) - 1, DEGREE - 1, -1):
        c = p[k]
        if c:
            p[k] = Fraction(0)
            p[k - 4] += c
            p[k - 8] -= c
            p[k - 12] += c
            p[k - 16] -= c
    p += [Fraction(0)] * (DEGREE - len(p))
    return tuple(p[:DEGREE])


@dataclass(frozen=True, slots=True)
class K40:
    """An exact element of Q(zeta_40) in the power basis."""

    c: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "c", _reduce(self.c))

    @staticmethod
    def scalar(q: int | Fraction) -> "K40":
        return K40((Fraction(q),))

    def __bool__(self) -> bool:
        return any(self.c)

    def __add__(self, other: "K40 | int | Fraction") -> "K40":
        other = coerce(other)
        return K40(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self) -> "K40":
        return K40(tuple(-a for a in self.c))

    def __sub__(self, other: "K40 | int | Fraction") -> "K40":
        return self + (-coerce(other))

    def __rsub__(self, other: "K40 | int | Fraction") -> "K40":
        return coerce(other) - self

    def __mul__(self, other: "K40 | int | Fraction") -> "K40":
        other = coerce(other)
        raw = [Fraction(0)] * (2 * DEGREE - 1)
        for i, ai in enumerate(self.c):
            if ai:
                for j, bj in enumerate(other.c):
                    if bj:
                        raw[i + j] += ai * bj
        return K40(tuple(raw))

    __rmul__ = __mul__

    def inverse(self) -> "K40":
        return _inverse(self)

    def __truediv__(self, other: "K40 | int | Fraction") -> "K40":
        return self * coerce(other).inverse()

    def __rtruediv__(self, other: "K40 | int | Fraction") -> "K40":
        return coerce(other) * self.inverse()

    def __pow__(self, n: int) -> "K40":
        if not isinstance(n, int):
            return NotImplemented
        if n < 0:
            return self.inverse() ** (-n)
        out = ONE
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def short(self) -> str:
        terms: list[str] = []
        for i, q in enumerate(self.c):
            if not q:
                continue
            if i == 0:
                terms.append(str(q))
            else:
                terms.append(f"({q})z^{i}")
        return " + ".join(terms) if terms else "0"


def coerce(x: K40 | int | Fraction) -> K40:
    return x if isinstance(x, K40) else K40.scalar(x)


@lru_cache(maxsize=None)
def _inverse(x: K40) -> K40:
    if not x:
        raise ZeroDivisionError("inverse of zero")
    r0 = list(MODULUS)
    r1 = _trim(list(x.c))
    t0: list[Fraction] = []
    t1: list[Fraction] = [Fraction(1)]
    while r1:
        q, r2 = _pdivmod(r0, r1)
        r0, r1 = r1, r2
        t0, t1 = t1, _psub(t0, _pmul(q, t1))
    if len(r0) != 1:
        raise ZeroDivisionError("nonunit modulo Phi_40")
    inv_gcd = Fraction(1) / r0[0]
    return K40(tuple(q * inv_gcd for q in t0))


ZERO = K40.scalar(0)
ONE = K40.scalar(1)
Z = K40((Fraction(0), Fraction(1)))
ZPOW = tuple(Z ** k for k in range(40))


@lru_cache(maxsize=None)
def conjugate(x: K40) -> K40:
    # Under the selected cyclotomic embedding, conjugation sends z to z^-1.
    out = ZERO
    for k, q in enumerate(x.c):
        if q:
            out += q * ZPOW[(-k) % 40]
    return out


def parse_rows(block: str, allowed: str) -> list[list[str]]:
    rows = [r.strip() for r in block.split(";") if r.strip()]
    token_re = re.compile(allowed)
    out: list[list[str]] = []
    for number, row in enumerate(rows, 1):
        tokens = token_re.findall(row)
        residue = token_re.sub("", row).replace(",", "")
        if residue.strip():
            raise ValueError(f"unexpected syntax in row {number}: {residue!r}")
        if len(tokens) != 36:
            raise ValueError(f"row {number}: got {len(tokens)} entries, expected 36")
        out.append(tokens)
    if len(out) != 36:
        raise ValueError(f"got {len(out)} rows, expected 36")
    return out


def parse_source(data: bytes) -> tuple[list[list[str]], list[list[int]]]:
    text = data.decode("utf-8")
    match = re.search(
        r"U\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise ValueError("could not find the two U matrix literals")
    base = parse_rows(match.group(1), r"(?<![A-Za-z0-9_])(0|a|b|c)(?![A-Za-z0-9_])")
    exponent_s = parse_rows(match.group(2), r"(?<![A-Za-z0-9_])(\d+)(?![A-Za-z0-9_])")
    exponent = [[int(x) for x in row] for row in exponent_s]
    if any(not 0 <= e < 20 for row in exponent for e in row):
        raise ValueError("phase exponent outside [0,19]")
    return base, exponent


Sparse = list[dict[int, K40]]


def build_matrix(base: list[list[str]], exponent: list[list[int]]) -> tuple[Sparse, dict[str, K40]]:
    w = ZPOW[2]
    c = (ZPOW[5] + ZPOW[-5]) / 2
    a = c / (w + w ** -1)
    b = (w**2 + w**-2) * a
    values = {"0": ZERO, "a": a, "b": b, "c": c}
    matrix: Sparse = []
    for r in range(36):
        row: dict[int, K40] = {}
        for col in range(36):
            x = values[base[r][col]] * (w ** exponent[r][col])
            if x:
                row[col] = x
        matrix.append(row)
    return matrix, {**values, "w": w, "z": Z}


def reshuffle(matrix: Sparse, d: int = 6) -> Sparse:
    out: Sparse = [dict() for _ in range(d * d)]
    for row, entries in enumerate(matrix):
        i, j = divmod(row, d)
        for col, x in entries.items():
            k, ell = divmod(col, d)
            out[d * i + k][d * j + ell] = x
    return out


def partial_transpose_second(matrix: Sparse, d: int = 6) -> Sparse:
    out: Sparse = [dict() for _ in range(d * d)]
    for row, entries in enumerate(matrix):
        i, j = divmod(row, d)
        for col, x in entries.items():
            k, ell = divmod(col, d)
            out[d * i + ell][d * k + j] = x
    return out


def columns(matrix: Sparse) -> Sparse:
    out: Sparse = [dict() for _ in range(len(matrix))]
    for r, entries in enumerate(matrix):
        for c, x in entries.items():
            out[c][r] = x
    return out


def check_orthonormal(vectors: Sparse, label: str) -> int:
    failures = 0
    for r, left in enumerate(vectors):
        for s, right in enumerate(vectors):
            total = ZERO
            # Sparse scalar product: row_r * conjugate(row_s)^T.
            if len(left) <= len(right):
                for k, x in left.items():
                    y = right.get(k)
                    if y is not None:
                        total += x * conjugate(y)
            else:
                for k, y in right.items():
                    x = left.get(k)
                    if x is not None:
                        total += x * conjugate(y)
            expected = ONE if r == s else ZERO
            if total != expected:
                failures += 1
                if failures <= 3:
                    print(f"FAIL {label}[{r},{s}] = {total.short()}")
    return failures


def check_unitary(matrix: Sparse, name: str) -> None:
    row_fail = check_orthonormal(matrix, f"{name}*{name}^dagger")
    col_fail = check_orthonormal(columns(matrix), f"{name}^dagger*{name}")
    if row_fail or col_fail:
        raise AssertionError(f"{name} is not unitary: row={row_fail}, col={col_fail}")
    print(f"PASS {name}: exact left and right unitarity (0 residual entries)")


def assert_eq(left: K40, right: K40 | int | Fraction, label: str) -> None:
    if left != coerce(right):
        raise AssertionError(f"{label}: {left.short()} != {coerce(right).short()}")
    print(f"PASS {label}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    data = args.source.read_bytes()

    sha256 = hashlib.sha256(data).hexdigest()
    blob_header = f"blob {len(data)}\0".encode("ascii")
    blob_sha1 = hashlib.sha1(blob_header + data).hexdigest()
    if len(data) != EXPECTED_BYTES or sha256 != EXPECTED_SHA256 or blob_sha1 != EXPECTED_GIT_BLOB_SHA1:
        raise AssertionError(
            f"source pin mismatch: bytes={len(data)}, sha256={sha256}, git_blob={blob_sha1}"
        )
    print(f"PASS source pin: commit {PINNED_COMMIT}")
    print(f"PASS source bytes: {len(data)}; sha256 {sha256}; git-blob {blob_sha1}")

    base, exponent = parse_source(data)
    nonzero = sum(token != "0" for row in base for token in row)
    active_exponents = [
        exponent[r][c]
        for r in range(36)
        for c in range(36)
        if base[r][c] != "0"
    ]
    print(
        f"PASS parser: base=36x36, exponent=36x36, nonzero={nonzero}, "
        f"active phase range=[{min(active_exponents)},{max(active_exponents)}]"
    )

    matrix, q = build_matrix(base, exponent)
    a, b, c, w, z = q["a"], q["b"], q["c"], q["w"], q["z"]
    phi = w**2 + w**-2
    sqrt5 = 2 * phi - 1

    # The source's positive-real radical definitions, checked algebraically.
    assert_eq(conjugate(a), a, "a is real")
    assert_eq(conjugate(b), b, "b is real")
    assert_eq(conjugate(c), c, "c is real")
    assert_eq(c * c, Fraction(1, 2), "c^2=1/2")
    assert_eq(a * a, (1 - 1 / sqrt5) / 4, "a^2=(1-1/sqrt(5))/4")
    assert_eq(b * b, (1 + 1 / sqrt5) / 4, "b^2=(1+1/sqrt(5))/4")
    assert_eq(a * a, (3 - phi) / 10, "a^2=(3-phi)/10")
    assert_eq(b * b, (2 + phi) / 10, "b^2=(2+phi)/10")
    assert_eq(b / a, phi, "b/a=phi")
    assert_eq((w**3) ** 7, w, "w=(zeta_20^3)^7=(T_pl/2)^7")

    u_r = reshuffle(matrix)
    u_g = partial_transpose_second(matrix)
    check_unitary(matrix, "U")
    check_unitary(u_r, "U^R")
    check_unitary(u_g, "U^Gamma_2")

    # G1, both inclusions and a concrete extraction of zeta_40 from entries.
    assert_eq(matrix[0][1], c, "entry U[1,2]=c")
    assert_eq(matrix[1][2], c * w**17, "entry U[2,3]=c*w^17")
    w_from_entries = (matrix[1][2] / matrix[0][1]) ** 13
    assert_eq(w_from_entries, w, "w=(U[2,3]/U[1,2])^13")
    z_from_entries = matrix[0][1] * (1 + w_from_entries**5) * w_from_entries**-2
    assert_eq(z_from_entries, z, "zeta_40=c*(1+w^5)*w^-2")

    # Converse containment: every source symbol is explicitly in Q(zeta_40).
    assert_eq(w, z**2, "w=zeta_40^2")
    assert_eq(c, (z**5 + z**-5) / 2, "c=(zeta_40^5+zeta_40^-5)/2")
    assert_eq(a, c / (w + w**-1), "a=c/(w+w^-1)")
    assert_eq(b, (w**2 + w**-2) * a, "b=(w^2+w^-2)*a")
    assert_eq(z**16 - z**12 + z**8 - z**4 + 1, 0, "Phi_40(zeta_40)=0")
    assert_eq(z**20, -1, "zeta_40^20=-1")
    assert_eq(z**40, 1, "zeta_40^40=1")
    zeta5 = z**8
    zeta8 = z**5
    assert_eq(zeta5**2 * zeta8**-3, z, "zeta_40=zeta_5^2*zeta_8^-3")
    print(
        "PASS minimal entry field: Q(entries)=Q(zeta_40), degree 16 over Q "
        "(Phi_40 is the irreducible 40th cyclotomic polynomial)"
    )
    print("PASS two-place identity: Q(zeta_40)=Q(zeta_5,zeta_8)")
    print("RESULT G0=PASS G1=PASS")


if __name__ == "__main__":
    main()
