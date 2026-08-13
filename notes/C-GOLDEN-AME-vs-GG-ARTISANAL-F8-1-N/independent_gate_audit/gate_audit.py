#!/usr/bin/env python3
"""Independent, deterministic G0/G1 audit for the artisanal F8 lock.

Standard-library only.  This program performs no F8 contraction and imports
nothing from the preregistration package.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re
import tarfile


GOLDEN_DEFAULT = Path("/tmp/galois_root/AME46_ORIGINAL.m")
PDF_DEFAULT = Path("/tmp/artisan_f8_prereg_source_probe_used_for_manifest/2504.15401v2.pdf")
ARCHIVE_DEFAULT = Path("/tmp/artisan_f8_prereg_source_probe_used_for_manifest/2504.15401v2.tar")
PREREG_DEFAULT = Path("/tmp/artisan_f8_prereg/PREREG.md")

PINS = {
    "golden": {
        "bytes": 8515,
        "sha256": "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae",
        "git_blob_sha1": "e0d0e171d58b3360c39595d677ffc401a466112d",
    },
    "pdf": {
        "bytes": 643554,
        "sha256": "3c423439d89a969235612bc4149069e8bfca349cf1532413ae90f19fdbf0e2be",
    },
    "archive": {
        "bytes": 49234,
        "sha256": "c67eab02dc7960e171eea723aada3554fb2869c8e07ece7ae209132cc33c86d2",
    },
    "prereg": {
        "sha256": "0ffaca441435003aeb0779160e9fcdbca6c40a25c4ea2acce836ff3eca6e0137",
    },
}


def digest(data: bytes, algorithm: str = "sha256") -> str:
    return hashlib.new(algorithm, data).hexdigest()


def verify_file(path: Path, pin: dict, git_blob: bool = False) -> dict:
    data = path.read_bytes()
    got = {"path": str(path), "bytes": len(data), "sha256": digest(data)}
    if "bytes" in pin and got["bytes"] != pin["bytes"]:
        raise AssertionError(f"byte-count mismatch for {path}: {got['bytes']}")
    if got["sha256"] != pin["sha256"]:
        raise AssertionError(f"SHA-256 mismatch for {path}: {got['sha256']}")
    if git_blob:
        header = f"blob {len(data)}\0".encode("ascii")
        got["git_blob_sha1"] = digest(header + data, "sha1")
        if got["git_blob_sha1"] != pin["git_blob_sha1"]:
            raise AssertionError(f"git-blob mismatch for {path}")
    return got


# ---------- Q(zeta_40), integer numerators over the common denominator 10 ----------

K40_ZERO = (0,) * 16
K40_ONE = (1,) + (0,) * 15


def k40_reduce(raw) -> tuple[int, ...]:
    a = list(raw)
    if len(a) < 16:
        a.extend([0] * (16 - len(a)))
    for degree in range(len(a) - 1, 15, -1):
        lead = a[degree]
        if lead:
            # Phi_40=x^16-x^12+x^8-x^4+1.
            a[degree - 4] += lead
            a[degree - 8] -= lead
            a[degree - 12] += lead
            a[degree - 16] -= lead
        a[degree] = 0
    return tuple(a[:16])


def k40_add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def k40_scale(x, n: int):
    return tuple(n * a for a in x)


def k40_mul(x, y):
    raw = [0] * 31
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                if b:
                    raw[i + j] += a * b
    return k40_reduce(raw)


def k40_monomial(power: int):
    power %= 40
    raw = [0] * (power + 1)
    raw[power] = 1
    return k40_reduce(raw)


def k40_conjugate(x):
    out = K40_ZERO
    for i, a in enumerate(x):
        if a:
            out = k40_add(out, k40_scale(k40_monomial(-i), a))
    return out


def exact_amplitudes_over_10() -> dict[str, tuple[int, ...]]:
    sparse = {
        "0": {},
        "a": {1: 1, 3: 1, 5: -2, 7: 3, 9: 3, 11: -2, 13: -4, 15: 1},
        "b": {1: 3, 3: 3, 5: -1, 7: -1, 9: -1, 11: 4, 13: -2, 15: -2},
        "c": {5: 5, 15: -5},
    }
    result = {}
    for label, terms in sparse.items():
        row = [0] * 16
        for degree, value in terms.items():
            row[degree] = value
        result[label] = tuple(row)
    # Derive/check all three amplitudes inside the quotient, rather than trust
    # the coefficient table alone.
    c_formula = k40_scale(k40_add(k40_monomial(5), k40_monomial(-5)), 5)
    if result["c"] != c_formula:
        raise AssertionError("c formula")
    if k40_mul(result["a"], k40_add(k40_monomial(2), k40_monomial(-2))) != result["c"]:
        raise AssertionError("a formula")
    if k40_mul(result["a"], k40_add(k40_monomial(4), k40_monomial(-4))) != result["b"]:
        raise AssertionError("b formula")
    if any(k40_conjugate(result[x]) != result[x] for x in "abc"):
        raise AssertionError("real-amplitude conjugation")
    return result


def parse_golden(data: bytes):
    text = data.decode("ascii")
    found = re.search(
        r"\bU\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        flags=re.S,
    )
    if not found:
        raise AssertionError("two MATLAB literals not found")
    labels = tuple(x for x in re.split(r"[,;\s]+", found.group(1).strip()) if x)
    if len(labels) != 1296 or set(labels) - {"0", "a", "b", "c"}:
        raise AssertionError("bad amplitude literal")
    phases = tuple(int(x) for x in re.findall(r"\d+", found.group(2)))
    if len(phases) != 1296 or any(not 0 <= e < 20 for e in phases):
        raise AssertionError("bad phase literal")
    amps = exact_amplitudes_over_10()
    entries = {}
    for flat, (label, exponent) in enumerate(zip(labels, phases)):
        if label == "0":
            continue
        row, col = divmod(flat, 36)
        i, j = divmod(row, 6)
        k, ell = divmod(col, 6)
        value = k40_mul(amps[label], k40_monomial(2 * exponent))
        entries[(i, j, k, ell)] = value
    return labels, phases, entries


FLATTENINGS = (
    ((0, 1), (2, 3), "ij|kl"),
    ((0, 2), (1, 3), "ik|jl"),
    ((0, 3), (1, 2), "il|jk"),
)


def sparse_rows(entries: dict, row_axes, col_axes):
    rows = [dict() for _ in range(36)]
    for index, value in entries.items():
        row = 6 * index[row_axes[0]] + index[row_axes[1]]
        col = 6 * index[col_axes[0]] + index[col_axes[1]]
        if col in rows[row]:
            raise AssertionError("duplicate tensor index")
        rows[row][col] = value
    return rows


def verify_golden_three_unitarities(entries: dict) -> dict:
    expected_one = k40_scale(K40_ONE, 100)  # entries have denominator 10
    report = {}
    for row_axes, col_axes, name in FLATTENINGS:
        rows = sparse_rows(entries, row_axes, col_axes)
        for r in range(36):
            for s in range(36):
                total = K40_ZERO
                for col in set(rows[r]) & set(rows[s]):
                    total = k40_add(total, k40_mul(rows[r][col], k40_conjugate(rows[s][col])))
                expected = expected_one if r == s else K40_ZERO
                if total != expected:
                    raise AssertionError(f"golden {name} unity failed at ({r},{s}): {total}")
        report[name] = {"rows": 36, "exact_gram": "I_36", "status": "PASS"}
    return report


# ---------- Q(zeta_6), exact direct U_lambda construction ----------

@dataclass(frozen=True)
class Z6:
    a: Fraction
    b: Fraction

    def __add__(self, other: "Z6") -> "Z6":
        return Z6(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "Z6":
        return Z6(-self.a, -self.b)

    def __sub__(self, other: "Z6") -> "Z6":
        return self + (-other)

    def __mul__(self, other: "Z6") -> "Z6":
        # zeta_6^2=zeta_6-1.
        return Z6(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def scale(self, n) -> "Z6":
        return Z6(self.a * n, self.b * n)

    def conjugate(self) -> "Z6":
        return Z6(self.a + self.b, -self.b)

    def inverse(self) -> "Z6":
        norm = self.a * self.a + self.a * self.b + self.b * self.b
        if not norm:
            raise ZeroDivisionError
        return self.conjugate().scale(Fraction(1, 1) / norm)

    def pair(self):
        def text(x: Fraction):
            return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
        return [text(self.a), text(self.b)]


Z6_ZERO = Z6(Fraction(0), Fraction(0))
Z6_ONE = Z6(Fraction(1), Fraction(0))
Z6_POWERS = (
    Z6(1, 0), Z6(0, 1), Z6(-1, 1), Z6(-1, 0), Z6(0, -1), Z6(1, -1)
)


def phase(kind: str, p: int, q: int) -> int:
    k, x = p % 3, p % 2
    ell, y = q % 3, q % 2
    base = k * k + ell * ell
    if (x, y) == (1, 1):
        return base % 3
    m = (x - y) % 3
    correction = -(k + ell + m) ** 2 if kind == "sym" else (ell + m) ** 2
    return (base + correction) % 3


def lambda_table(kind: str):
    if kind not in ("sym", "sparse"):
        raise ValueError(kind)
    return tuple(phase(kind, p, q) for p in range(6) for q in range(6))


def gl2_f3():
    return tuple(
        ((a, b), (c, d))
        for a, b, c, d in itertools.product(range(3), repeat=4)
        if (a * d - b * c) % 3
    )


def lifted_transpose_action(g, p, q):
    h00, h01 = (4 * g[0][0] + 3) % 6, (4 * g[0][1]) % 6
    h10, h11 = (4 * g[1][0]) % 6, (4 * g[1][1] + 3) % 6
    return (h00 * p + h10 * q) % 6, (h01 * p + h11 * q) % 6


def transformed_table(kind: str, g):
    return tuple(
        phase(kind, *lifted_transpose_action(g, p, q))
        for p in range(6) for q in range(6)
    )


def z6_sum_powers(exponents):
    total = Z6_ZERO
    for exponent in exponents:
        total = total + Z6_POWERS[exponent % 6]
    return total


def verify_autocorrelations(table) -> None:
    value = lambda p, q: table[6 * (p % 6) + (q % 6)]
    for ap in range(6):
        for aq in range(6):
            standard = []
            twisted = []
            for bp in range(6):
                for bq in range(6):
                    base = 2 * (value(ap + bp, aq + bq) - value(bp, bq))
                    standard.append(base)
                    symplectic = ap * bq - aq * bp
                    twisted.append(base + symplectic)
            expected = Z6(36, 0) if (ap, aq) == (0, 0) else Z6_ZERO
            if z6_sum_powers(standard) != expected:
                raise AssertionError(f"standard autocorrelation at {(ap, aq)}")
            if z6_sum_powers(twisted) != expected:
                raise AssertionError(f"twisted autocorrelation at {(ap, aq)}")


def construct_direct_tensor(kind: str):
    entries = {}
    table = lambda_table(kind)
    for i, j, k, ell in itertools.product(range(6), repeat=4):
        q = (i - j) % 6
        if q != (k - ell) % 6:
            continue
        numerator = z6_sum_powers(
            2 * table[6 * p + q] + p * (i - k) for p in range(6)
        )
        if numerator != Z6_ZERO:
            entries[(i, j, k, ell)] = numerator  # common denominator 6
    return entries


def verify_z6_three_unitarities(entries: dict) -> dict:
    report = {}
    for row_axes, col_axes, name in FLATTENINGS:
        rows = sparse_rows(entries, row_axes, col_axes)
        for r in range(36):
            for s in range(36):
                total = Z6_ZERO
                for col in set(rows[r]) & set(rows[s]):
                    total = total + rows[r][col] * rows[s][col].conjugate()
                expected = Z6(36, 0) if r == s else Z6_ZERO
                if total != expected:
                    raise AssertionError(f"direct {name} unity at ({r},{s}): {total}")
        report[name] = {"rows": 36, "exact_gram": "I_36", "status": "PASS"}
    return report


def zero_matrix(n=36):
    return [[Z6_ZERO for _ in range(n)] for _ in range(n)]


def direct_matrix(entries):
    result = zero_matrix()
    for (i, j, k, ell), value in entries.items():
        result[6 * i + j][6 * k + ell] = value
    return result  # numerator, common denominator 6


def odd_projector_numerator():
    result = zero_matrix()
    for p in (1, 3, 5):
        for q in (1, 3, 5):
            for j in range(6):
                i = (j + q) % 6
                for ell in range(6):
                    k = (ell + q) % 6
                    result[6 * i + j][6 * k + ell] = (
                        result[6 * i + j][6 * k + ell] + Z6_POWERS[p * (i - k) % 6]
                    )
    return result  # actual projector is result/6


def matrix_multiply(a, b):
    n = len(a)
    out = zero_matrix(n)
    for i in range(n):
        for k in range(n):
            if a[i][k] == Z6_ZERO:
                continue
            for j in range(n):
                if b[k][j] != Z6_ZERO:
                    out[i][j] = out[i][j] + a[i][k] * b[k][j]
    return out


def matrix_subtract(a, b):
    return [[x - y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def matrix_scale(a, n):
    return [[x.scale(n) for x in row] for row in a]


def matrix_is_zero(a):
    return all(x == Z6_ZERO for row in a for x in row)


def exact_rank(a):
    m = [list(row) for row in a]
    rows, cols = len(m), len(m[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if m[r][col] != Z6_ZERO), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        inv = m[rank][col].inverse()
        m[rank] = [x * inv for x in m[rank]]
        for r in range(rows):
            if r == rank or m[r][col] == Z6_ZERO:
                continue
            factor = m[r][col]
            m[r] = [x - factor * y for x, y in zip(m[r], m[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def verify_projectors_and_commutator(entries):
    p9 = odd_projector_numerator()
    identity_num = [[Z6(6 if i == j else 0, 0) for j in range(36)] for i in range(36)]
    p27 = matrix_subtract(identity_num, p9)
    if not matrix_is_zero(matrix_subtract(matrix_multiply(p9, p9), matrix_scale(p9, 6))):
        raise AssertionError("Pi9 idempotence")
    if not matrix_is_zero(matrix_subtract(matrix_multiply(p27, p27), matrix_scale(p27, 6))):
        raise AssertionError("Pi27 idempotence")
    if not matrix_is_zero(matrix_multiply(p9, p27)):
        raise AssertionError("projector orthogonality")
    rank9, rank27 = exact_rank(p9), exact_rank(p27)
    if (rank9, rank27) != (9, 27):
        raise AssertionError((rank9, rank27))
    u = direct_matrix(entries)
    comm = matrix_subtract(matrix_multiply(u, p9), matrix_multiply(p9, u))
    if not matrix_is_zero(comm):
        raise AssertionError("[U,Pi9] != 0")
    return {
        "Pi9_rank": rank9,
        "Pi27_rank": rank27,
        "Pi9_idempotent": True,
        "Pi27_idempotent": True,
        "orthogonal": True,
        "U_commutes_with_Pi9": True,
    }


def inspect_archive(path: Path) -> dict:
    with tarfile.open(path, "r:*") as archive:
        names = tuple(sorted(archive.getnames()))
        if "artisanal.tex" not in names or "00README.json" not in names:
            raise AssertionError(f"unexpected archive members: {names}")
        tex = archive.extractfile("artisanal.tex").read()
        # Static source anchors only; no numerical target invariant.
        anchors = (
            b"label{eqn:perfect_wh}",
            b"label{eqn:autocorr_conditions}",
            b"label{eqn:symmetric}",
            b"label{eqn:sparse}",
            b"label{eqn:whbasis}",
        )
        if any(anchor not in tex for anchor in anchors):
            raise AssertionError("normative source anchor missing")
        return {
            "members": list(names),
            "artisanal_tex_bytes": len(tex),
            "artisanal_tex_sha256": digest(tex),
            "normative_anchors_present": True,
        }


def run(args) -> dict:
    prereg = verify_file(args.prereg, PINS["prereg"])
    golden_pin = verify_file(args.golden, PINS["golden"], git_blob=True)
    pdf_pin = verify_file(args.pdf, PINS["pdf"])
    archive_pin = verify_file(args.archive, PINS["archive"])
    archive = inspect_archive(args.archive)

    golden_data = args.golden.read_bytes()
    labels, phases, golden_entries = parse_golden(golden_data)
    golden_unity = verify_golden_three_unitarities(golden_entries)

    matrices = gl2_f3()
    if len(matrices) != 48:
        raise AssertionError("GL(2,F3) cardinality")
    orbit_tables = {}
    targets = {}
    for kind in ("sym", "sparse"):
        all_tables = tuple(transformed_table(kind, g) for g in matrices)
        unique = tuple(sorted(set(all_tables)))
        if len(unique) != 24:
            raise AssertionError(f"{kind} orbit size {len(unique)}")
        for table in unique:
            verify_autocorrelations(table)
        entries = construct_direct_tensor(kind)
        unity = verify_z6_three_unitarities(entries)
        projector = verify_projectors_and_commutator(entries)
        orbit_tables[kind] = set(unique)
        targets[kind] = {
            "GL_images": 48,
            "distinct_tables": len(unique),
            "all_distinct_tables_exact_autocorrelations": True,
            "direct_U_nonzero_entries": len(entries),
            "three_unitarities": unity,
            "projector_audit": projector,
            "representative_table_sha256": digest(bytes(lambda_table(kind))),
            "sorted_orbit_tables_sha256": digest(b"".join(bytes(t) for t in unique)),
        }
    intersection = len(orbit_tables["sym"] & orbit_tables["sparse"])
    if intersection:
        raise AssertionError(f"orbit intersection size {intersection}")

    return {
        "schema": "artisan-f8-independent-g0-g1-v1",
        "scope": "source/construction integrity only; no F8 contractions",
        "public_lock": {
            "commit": "62c1e877c3817923dca6b922ebd4562f83d2bbea",
            "issue": 368,
            "prereg": prereg,
        },
        "source_integrity": {
            "golden": golden_pin,
            "gross_goedicke_pdf": pdf_pin,
            "gross_goedicke_archive": archive_pin,
            "archive_audit": archive,
        },
        "golden": {
            "shape": [36, 36],
            "nonzero_entries": len(golden_entries),
            "label_counts": {x: labels.count(x) for x in ("0", "a", "b", "c")},
            "phase_range": [min(phases), max(phases)],
            "amplitude_identities_in_Qzeta40": True,
            "three_unitarities": golden_unity,
        },
        "construction": {
            "direct_formula": "delta(i-j,k-l)/6 sum_p lambda(p,i-j) zeta6^(p(i-k))",
            "GL2_F3_count": len(matrices),
            "orbit_intersection": intersection,
            "targets": targets,
        },
        "F8_contractions": "NOT_COMPUTED",
        "status": "PASS",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--golden", type=Path, default=GOLDEN_DEFAULT)
    parser.add_argument("--pdf", type=Path, default=PDF_DEFAULT)
    parser.add_argument("--archive", type=Path, default=ARCHIVE_DEFAULT)
    parser.add_argument("--prereg", type=Path, default=PREREG_DEFAULT)
    parser.add_argument("--json", type=Path, default=Path("/tmp/artisan_f8_gate_audit/certificate.json"))
    args = parser.parse_args()
    result = run(args)
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("ARTISAN_F8_INDEPENDENT_G0_G1_V1")
    print(f"GOLDEN_SHA256={result['source_integrity']['golden']['sha256']}")
    print(f"GG_PDF_SHA256={result['source_integrity']['gross_goedicke_pdf']['sha256']}")
    print(f"GG_ARCHIVE_SHA256={result['source_integrity']['gross_goedicke_archive']['sha256']}")
    print("GOLDEN_NONZERO=" + str(result["golden"]["nonzero_entries"]))
    print("GOLDEN_THREE_EXACT_UNITARITIES=PASS")
    for kind in ("sym", "sparse"):
        target = result["construction"]["targets"][kind]
        print(f"{kind.upper()}_GL_TABLES=48->{target['distinct_tables']}")
        print(f"{kind.upper()}_NONZERO_U={target['direct_U_nonzero_entries']}")
        print(f"{kind.upper()}_AUTOCORRELATIONS=PASS")
        print(f"{kind.upper()}_THREE_EXACT_UNITARITIES=PASS")
        p = target["projector_audit"]
        print(f"{kind.upper()}_PROJECTORS={p['Pi9_rank']}+{p['Pi27_rank']};COMMUTATOR=0")
    print("ORBITS_DISJOINT=PASS")
    print("F8_CONTRACTIONS=NOT_COMPUTED")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
