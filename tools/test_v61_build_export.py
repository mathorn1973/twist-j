#!/usr/bin/env python3
"""Temporary non-canonical builder/exporter for the frozen Public Canon v61 fold."""

from __future__ import annotations

import base64
import hashlib
import io
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


V61_CANON_BLOCK = r'''
### Binary norm index

J-BINARY-NORM-INDEX [T] is an exact L1 theorem for the absolute norm at inert
rational primes. Let `K=Q(zeta_5)` and let `p` be inert, so
`O_K/(p)=F_(p^4)`. Reduction commutes with the absolute norm, hence a unit
`u` with `N_(K/Q)(u)=1` reduces into

```text
ker N_(F_(p^4)/F_p),
|ker N|=(p^4-1)/(p-1)=(p+1)(p^2+1),
[F_(p^4)^x:ker N]=p-1.
```

Therefore a norm-one algebraic unit can generate the whole inert residue
multiplicative group only when `p-1=1`, namely at `p=2`. The public unit J
attains this sole possible whole-group case: in `F_16`,
`ord(Jbar)=15=|F_16^x|`. The mechanism itself is generic in field degree and
selects neither J, degree four nor the prime five. Moreover the four elements
`1+zeta_5^a`, `a=1,2,3,4`, form one Frobenius orbit at `p=2` and all have
order fifteen, so the attainment does not select the axiom exponent or turn
characteristic two into a physical selection principle. Evidence is
`probes/P-J-BINARY-NORM-INDEX-1`.

J-BINARY-NORM-ORDER-CENSUS [C] is the finite companion on the same L1 carrier.
Among the 156 rational primes `p<2000` inert in `Q(zeta_5)`, `Jbar` generates
the complete norm-one subgroup exactly for `p=2` and `p=3`; at every other
prime in the frozen range its order is a proper divisor of `(p+1)(p^2+1)`.
This statement is finite-range only. It is not an all-prime theorem.

### Exact record quotient calculus

RECORD-QUOTIENT-CALCULUS [T] is the exact L1 theorem for finite quotient
records of `R=Z[zeta_5]`. For every nonzero proper ideal
`I=product_P P^(e_P)`:

```text
Idem(R/I) ~= P(Supp(I))
```

canonically as the prime-labelled Boolean algebra supplied by CRT and the
local-idempotent lemma. Reduction `R/I -> R/rad(I)` is bijective on
idempotents, so the exponent vector is invisible to the Boolean layer. With
`n_I=rad(I)/I` and `n_I^0=R/I`, the exact layer orders and Loewy length are

```text
|n_I^k/n_I^(k+1)| = product {N(P): e_P>k},
L(R/I)=max_P e_P.
```

A unital `R`-algebra map `R/I -> R/J` exists exactly when `I` is contained in
`J` and is then the unique canonical projection; a strict quotient has no
unital `R`-algebra section. Finally, for
`I_L=(1-zeta_5)^L(2)`, `L>=1`, the support, radical, reduced ring
`F_5 x F_16` and four-element Boolean algebra are constant while the Loewy
length is exactly L and is unbounded. The theorem selects no ideal or atom and
supplies no event semantics, orientation, decoder, measure, Born weight,
coarse-graining, RG flow, continuum statement or L2-L6 lift. Evidence is
`probes/P-RECORD-QUOTIENT-CALCULUS-1`.

### Odd-motor mediated block

J-ODD-MOTOR-MEDIATED-BRIDGE [T] is one consolidated exact L1 theorem on the
public `M_J`, `D=M_J-I`, the frozen `AGL_1(F_5)` affine simplex and the
multiplier-stabilizer sectors `P,R,C`. Over `Q(sqrt5)` the native algebra has
exactly two primitive nonzero rank-two invariant sectors, so the naive third
native mediator sector is impossible. On the affine token decomposition the
odd channel `A=D-D^-1` instead has the exact block graph

```text
P <-> C <-> R,
PAP=RAR=CAC=PAR=RAP=0,
rank(PAC)=rank(CAP)=rank(RAC)=rank(CAR)=1.
```

For `B=P A C A R`,

```text
rank(B)=1,
B^sharp B=(5/4)R,
B B^sharp=(5/4)P,
```

and the squared overlap of the two active lines in C is exactly `1/5`. None of
`D,D^2,D^3,D^4,D+D^-1` has the same frozen direct-zero / one-mediator-nonzero
pattern. For `H=g+g^-1`, the sector eigenvalues are `+2,-2,0`; exact elimination
of C gives orientation-independent magnitude `sqrt5 t^2/(2z)`, with `t` only a
formal insertion counter, and at token 2

```text
det[zI-(H+tA)] = z^4+(5t^2-4)z^2+5t^4.
```

The quadratic lift is exactly

```text
Sym^2(V) ~= 1 + epsilon + 2V,
dim End_G(Sym^2 V)=6,
```

with `q_+` invariant, `q_-` transforming by `epsilon`, the frozen pairwise Hom
vanishing and trilinear invariant census. The repeated `2V` component remains
a genuine nonselection boundary. The native two-sector no-go is retained
inside the theorem rather than hidden. The result is algebraic only: it is not
a physical resonance and supplies no material, frequency, susceptibility,
Born, probability, observer, decoder, force, spacetime, SI or L2-L6 reading.
Evidence is `probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2`.
'''.strip() + "\n\n"

REGISTRY_ROWS = (
    (
        "J-BINARY-NORM-INDEX", "T",
        "at L1, for every rational prime p inert in K=Q(zeta_5), reduction commutes with the absolute norm and the norm-one reduction lies in ker N_(F_(p^4)/F_p), a cyclic subgroup of order (p+1)(p^2+1) and index exactly p-1 in F_(p^4)^x; hence a norm-one algebraic unit can generate the whole inert residue multiplicative group only at p=2, and ord(Jbar)=15=|F_16^x| so J attains that sole possible whole-group case; the index p-1 is generic in field degree and selects neither J, degree four nor the prime five, while the four 1+zeta_5^a form one Frobenius orbit of order fifteen at p=2, so no axiom exponent or physical characteristic-two selection is claimed",
        "3. The kernel and the census", "probes/P-J-BINARY-NORM-INDEX-1",
        "fires if at an inert prime the residue norm kernel has index other than p-1, norm descent fails, an inert p>2 admits a norm-one unit generating F_(p^4)^x, ord(Jbar) at p=2 is below 15, one Galois conjugate 1+zeta_5^a has different order at p=2, or the stated no-selection controls fail; a different field degree or physical dictionary is outside scope; integrity mismatch without exact negation is STOP",
    ),
    (
        "J-BINARY-NORM-ORDER-CENSUS", "C",
        "at L1 for the finite census of the 156 rational primes p<2000 inert in Q(zeta_5), Jbar generates the complete norm-one subgroup exactly at p=2 and p=3 and has proper order in that subgroup at every other prime in the frozen range; finite range only, no all-prime theorem",
        "3. The kernel and the census", "probes/P-J-BINARY-NORM-INDEX-1",
        "fires if the exact census below 2000 contains a third inert prime with full norm-one order or fails at p=2 or p=3; any prime at or above 2000 is outside scope; integrity mismatch without exact finite-range negation is STOP",
    ),
    (
        "RECORD-QUOTIENT-CALCULUS", "T",
        "at L1 for R=Z[zeta_5] and every nonzero proper ideal I=product_P P^(e_P): CRT gives the canonical prime-labelled Boolean algebra Idem(R/I)~=P(Supp(I)); R/I->R/rad(I) is bijective on idempotents; with n_I=rad(I)/I and n_I^0=R/I, |n_I^k/n_I^(k+1)|=product{N(P):e_P>k} and L(R/I)=max_P e_P; a unital R-algebra map R/I->R/J exists uniquely exactly when I is contained in J and a strict quotient has no unital R-algebra section; for I_L=(1-zeta_5)^L(2), support, radical, reduced ring F_5 x F_16 and the four-element Boolean algebra are fixed while Loewy length L is unbounded; no ideal, atom, event semantics, decoder, measure, coarse-graining, RG or continuum reading",
        "3. The kernel and the census", "probes/P-RECORD-QUOTIENT-CALCULUS-1",
        "fires if any CRT or local-idempotent classification, radical-map bijection, layer-order or Loewy-length formula, thin unital-map criterion, no-section theorem, or fixed-support unbounded-depth family fails in the stated universal proof scope; module decompositions and physical readings are outside scope; integrity mismatch without exact negation is STOP",
    ),
    (
        "J-ODD-MOTOR-MEDIATED-BRIDGE", "T",
        "at L1 on the public M_J with D=M_J-I, the frozen AGL_1(F_5) affine simplex and multiplier-stabilizer sectors P,R,C: over Q(sqrt5) the native algebra has exactly two primitive nonzero rank-two invariant sectors, forbidding a third native mediator; for A=D-D^-1 the exact block graph is P<->C<->R with zero diagonal and direct P-R blocks and rank-one P/R-C blocks; B=P A C A R has rank one with B^sharp B=(5/4)R and B B^sharp=(5/4)P and active C-line squared overlap 1/5; D,D^2,D^3,D^4,D+D^-1 fail the same mediated-zero pattern; H=g+g^-1 has sector eigenvalues +2,-2,0 and exact C elimination gives magnitude sqrt5 t^2/(2z), t a formal insertion counter, with token-2 determinant z^4+(5t^2-4)z^2+5t^4; Sym^2(V)=1+epsilon+2V, dim End_G(Sym^2 V)=6, q_+ invariant and q_- epsilon-covariant, with pairwise Hom vanishing and the frozen trilinear census; repeated 2V remains a nonselection boundary; no physical resonance or L2-L6 reading",
        "3. The kernel and the census", "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2",
        "fires if any frozen G1-G8 identity, rank, block zero or nonzero pattern, 5/4 norm, 1/5 overlap, control-family exclusion, Schur or determinant identity, character decomposition, covariance, Hom or trilinear count fails; the native two-sector negative and repeated-2V nonselection are part of the theorem scope and may not be removed; physical resonance, material, Born, decoder and SI readings are outside scope; integrity mismatch without exact negation is STOP",
    ),
)

BUNDLES = {
    "J-BINARY-NORM-INDEX": "626f598fb7a4cdd331208d28c60ed9fc15d9ac6412ecc003c5bf4dd0dfc4682e",
    "J-BINARY-NORM-ORDER-CENSUS": "626f598fb7a4cdd331208d28c60ed9fc15d9ac6412ecc003c5bf4dd0dfc4682e",
    "RECORD-QUOTIENT-CALCULUS": "5b0c0a4327539b7426de78bb54f03d525c32c94673c5113ce1c009bb274e92ff",
    "J-ODD-MOTOR-MEDIATED-BRIDGE": "03db973566ae068b5ed8eb65f4e79ae13af398ac067f325c26a25c1553bf636b",
}

NORMATIVE_ROWS = (
    "J-BINARY-NORM-INDEX\tTHEOREM\tJ-BINARY-NORM-INDEX\tT\tL1\t\tcanon/CANON.md::3. The kernel and the census",
    "J-BINARY-NORM-ORDER-CENSUS\tCOMPUTATION\tJ-BINARY-NORM-ORDER-CENSUS\tC\tL1\t\tcanon/CANON.md::3. The kernel and the census",
    "RECORD-QUOTIENT-CALCULUS\tTHEOREM\tRECORD-QUOTIENT-CALCULUS\tT\tL1\t\tcanon/CANON.md::3. The kernel and the census",
    "J-ODD-MOTOR-MEDIATED-BRIDGE\tTHEOREM\tJ-ODD-MOTOR-MEDIATED-BRIDGE\tT\tL1\t\tcanon/CANON.md::3. The kernel and the census",
)

DEPENDENCY_ROWS = (
    "J-BINARY-NORM-INDEX\tJ-UNIT\tREQUIRES\twritten proof uses N(J)=1 and the public cyclotomic-unit setting for the J attainment clause",
    "J-BINARY-NORM-ORDER-CENSUS\tJ-BINARY-NORM-INDEX\tREQUIRES\tfinite census is the bounded computational companion to the norm-index theorem",
    "J-ODD-MOTOR-MEDIATED-BRIDGE\tAFFINE-READING-DEGREE-CENSUS\tREQUIRES\taffine token decomposition and characteristic-zero invariant census used by the frozen quadratic-lift proof",
    "J-ODD-MOTOR-MEDIATED-BRIDGE\tAFFINE-QUADRATIC-FORM-UNIQUENESS\tREQUIRES\tpositive invariant q_+ line and affine quadratic carrier used in the frozen G7-G8 proof",
)

EVIDENCE_LOCATIONS = {
    "J-BINARY-NORM-INDEX": "probes/P-J-BINARY-NORM-INDEX-1",
    "J-BINARY-NORM-ORDER-CENSUS": "probes/P-J-BINARY-NORM-INDEX-1",
    "RECORD-QUOTIENT-CALCULUS": "probes/P-RECORD-QUOTIENT-CALCULUS-1",
    "J-ODD-MOTOR-MEDIATED-BRIDGE": "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2",
}

RATIONALES = {
    "J-BINARY-NORM-INDEX": "Public Canon v61 registers the inert residue norm-index theorem, its attainment by J at p=2 and the degree/Galois no-selection controls at L1.",
    "J-BINARY-NORM-ORDER-CENSUS": "Public Canon v61 registers only the exact finite inert-prime census below 2000 at C; no all-prime statement is inferred.",
    "RECORD-QUOTIENT-CALCULUS": "Public Canon v61 registers the universal CRT, idempotent, Loewy and thin unital-reduction calculus for finite Z[zeta_5] quotients at L1 with no event or decoder reading.",
    "J-ODD-MOTOR-MEDIATED-BRIDGE": "Public Canon v61 registers one consolidated L1 odd-motor mediated-block theorem including the native two-sector no-go, exact second-order bridge, control family, quadratic lift and repeated-2V nonselection boundary.",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def append_lines(path: Path, lines: list[str] | tuple[str, ...]) -> None:
    text = path.read_text(encoding="utf-8")
    if text and not text.endswith("\n"):
        text += "\n"
    text += "\n".join(lines) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_release_status(path: Path, canon_hash: str, canon_bytes: int) -> None:
    text = path.read_text(encoding="utf-8")
    replacements = {
        "CANON:          Public Canon v60": "CANON:          Public Canon v61",
        "TAG:            canon-v60": "TAG:            canon-v61",
        "CONTENT_COMMIT: 18b21bdaf2c2236c9444b120900277ccfb63e050": "CONTENT_COMMIT: f9b7438747e612eeebf63cb3ac95283fcb2a7085",
        "CANON_SHA256:   9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0": f"CANON_SHA256:   {canon_hash}",
        "CANON_BYTES:    329876": f"CANON_BYTES:    {canon_bytes}",
    }
    for old, new in replacements.items():
        if old not in text:
            raise AssertionError(f"missing STATUS anchor: {old}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def build_candidate(root: Path, work: Path) -> tuple[list[str], str, int]:
    canon_dir = work / "canon"
    frontier_before = (canon_dir / "FRONTIER.md").read_bytes()

    canon_path = canon_dir / "CANON.md"
    canon = canon_path.read_text(encoding="utf-8")
    head, sep, tail = canon.partition("\n---\n")
    if not sep:
        raise AssertionError("CANON lacks preamble separator")
    if "# TWIST-J Public Canon v60" not in head:
        raise AssertionError("CANON current release title missing")
    head = head.replace("Public Canon v60", "Public Canon v61")
    canon = head + sep + tail
    anchor = "\n## 4. The two places\n"
    if canon.count(anchor) != 1:
        raise AssertionError("CANON section-4 anchor is not unique")
    canon = canon.replace(anchor, "\n" + V61_CANON_BLOCK + anchor, 1)
    canon_path.write_text(canon, encoding="utf-8", newline="\n")

    registry_lines = ["\t".join(row) for row in REGISTRY_ROWS]
    append_lines(canon_dir / "REGISTRY.tsv", registry_lines)
    append_lines(canon_dir / "NORMATIVE.tsv", NORMATIVE_ROWS)
    append_lines(canon_dir / "DEPENDENCIES.tsv", DEPENDENCY_ROWS)

    evidence_lines = []
    for claim, _status, _scope, _section, location, _falsifier in REGISTRY_ROWS:
        evidence_lines.append(
            "\t".join((claim, f"EV-{claim}", "PUBLIC_PROBE", location, BUNDLES[claim],
                       "bundle-manifest-sha256-v1", "two-architecture"))
        )
    append_lines(canon_dir / "EVIDENCE.tsv", evidence_lines)

    history_lines = []
    for claim, status, scope, _section, location, _falsifier in REGISTRY_ROWS:
        scope_hash = sha256_bytes(scope.encode("utf-8"))
        history_lines.append(
            "\t".join((
                f"CANON61-DECLARE-{claim}", "1", "2026-08-23", "canon-v61-candidate",
                claim, "DECLARE", "-", status, scope_hash, f"EV-{claim}", location,
                BUNDLES[claim], RATIONALES[claim],
            ))
        )
    append_lines(canon_dir / "HISTORY.tsv", history_lines)

    changelog_path = canon_dir / "CHANGELOG.md"
    changelog = changelog_path.read_text(encoding="utf-8")
    changelog_anchor = "# Canon changelog (public series)\n\n"
    if not changelog.startswith(changelog_anchor):
        raise AssertionError("CHANGELOG header mismatch")
    v61 = '''## Public Canon v61

<!-- BEGIN GENERATED CURRENT COUNTS -->
PLACEHOLDER
<!-- END GENERATED CURRENT COUNTS -->

Public Canon v61 is a narrow exact L1 consolidation of the three public probes
merged after v60. It registers three theorem rows and one finite-range
computation row. It adds no scientific run, physical dictionary, D/H/O/F row,
status move, gate, decoder completion or layer lift.

`J-BINARY-NORM-INDEX [T]` records the exact index `p-1` of the residue norm-one
subgroup at inert primes and the fact that a norm-one unit can generate the
whole inert residue multiplicative group only at `p=2`; J attains that case
with order 15 in `F_16`. The generic-degree and Galois-orbit controls are part
of the row and forbid reading this as selection of J, degree four, the prime
five, the axiom exponent or a physical characteristic-two principle.
`J-BINARY-NORM-ORDER-CENSUS [C]` records only the 156 inert primes below 2000,
where J generates the complete norm-one subgroup exactly at 2 and 3.

`RECORD-QUOTIENT-CALCULUS [T]` folds the universal R1-R6 proof: prime-labelled
Boolean idempotents from CRT, invariance under radical reduction, exact Loewy
layer orders and length, thin unital quotient maps, absence of sections for
strict quotients, and a fixed-support family with unbounded depth. It selects
no ideal, atom, event, decoder, measure or continuum reading.

`J-ODD-MOTOR-MEDIATED-BRIDGE [T]` folds G1-G8 of the corrected public successor
probe into one row. The native carrier has only two primitive nonzero sectors,
so the naive third native mediator route is negative. On the frozen affine
token decomposition the odd channel has the exact `P <-> C <-> R` block graph,
a rank-one second-order P-to-R bridge with norm factor `5/4`, active-line
squared overlap `1/5`, exact control exclusions and Schur polynomial, and the
quadratic decomposition `Sym^2(V)=1+epsilon+2V`. The repeated `2V` remains a
nonselection boundary. No physical resonance or higher-layer reading is
created.

The v61 ledger change is:

```text
claims:    320 + 3 T + 1 C = 324,
T:         199 + 3 = 202,
C:          32 + 1 = 33,
D: 43, H: 3, O: 27, F: 16, all unchanged,
live H/O:   30, unchanged,
normative items: 366 + 4 = 370,
dependencies: 577 + 4 = 581,
evidence rows: 320 + 4 = 324,
gates:      11, unchanged,
history rows: 841 + 4 = 845,
two-architecture evidence: 236 + 4 = 240,
frontier programs: 7, unchanged,
reproduction witnesses: 23, unchanged.
```

The candidate dependency audit omits the draft `RECORD-QUOTIENT-CALCULUS ->
J-UNIT` edge because the universal Dedekind/CRT proof uses the fixed ring
`Z[zeta_5]` but not the theorem `N(J)=1`; issue #529 explicitly allowed omission
of a proposed edge when exact proof review found it nongenuine. No reverse edge
or old proof lineage changes.

'''
    changelog_path.write_text(
        changelog_anchor + v61 + changelog[len(changelog_anchor):],
        encoding="utf-8", newline="\n"
    )

    subprocess.run(
        [sys.executable, "tools/generate_canon_views.py", "--root", str(work), "--apply"],
        cwd=work, check=True, text=True,
    )
    if (canon_dir / "FRONTIER.md").read_bytes() != frontier_before:
        raise AssertionError("FRONTIER changed although no live row moved")

    hashed = ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")
    sums = []
    for name in hashed:
        digest = sha256_bytes((canon_dir / name).read_bytes())
        sums.append(f"{digest}  canon/{name}\n")
    (canon_dir / "SHA256SUMS").write_text("".join(sums), encoding="utf-8", newline="\n")

    canon_hash = sha256_bytes(canon_path.read_bytes())
    canon_bytes = canon_path.stat().st_size
    replace_release_status(work / "STATUS.md", canon_hash, canon_bytes)

    readme = (work / "README.md").read_text(encoding="utf-8")
    readme = readme.replace("canon-v60", "canon-v61").replace("Public Canon v60", "Public Canon v61")
    (work / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    citation = (work / "CITATION.cff").read_text(encoding="utf-8")
    citation = citation.replace("Public Canon v60", "Public Canon v61")
    citation = citation.replace('version: "60"', 'version: "61"')
    citation = citation.replace("date-released: 2026-08-21", "date-released: 2026-08-23")
    (work / "CITATION.cff").write_text(citation, encoding="utf-8", newline="\n")

    subprocess.run([sys.executable, "tools/check_canon.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_ledger.py"], cwd=work, check=True, text=True)
    subprocess.run(
        [sys.executable, "tools/generate_canon_views.py", "--root", str(work),
         "--check-dir", str(canon_dir)], cwd=work, check=True, text=True,
    )

    export_files = [
        "canon/CANON.md", "canon/CORE.md", "canon/REGISTRY.tsv",
        "canon/NORMATIVE.tsv", "canon/DEPENDENCIES.tsv", "canon/EVIDENCE.tsv",
        "canon/HISTORY.tsv", "canon/CHANGELOG.md", "canon/STATUS_COUNTS.tsv",
        "canon/SHA256SUMS",
    ]
    return export_files, canon_hash, canon_bytes


class V61BuildExportTest(unittest.TestCase):
    def test_build_validate_and_export(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as td:
            work = Path(td) / "repo"
            shutil.copytree(
                root, work,
                ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
            )
            export_files, canon_hash, canon_bytes = build_candidate(root, work)

            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for relative in export_files:
                    archive.writestr(relative, (work / relative).read_bytes())
            payload = buffer.getvalue()
            payload_hash = sha256_bytes(payload)
            encoded = base64.b64encode(payload).decode("ascii")

            print(f"V61_BUILD_PASS canon_sha256={canon_hash} canon_bytes={canon_bytes} files={len(export_files)} zip_bytes={len(payload)} zip_sha256={payload_hash}")
            chunk = 6000
            print("V61_EXPORT_BEGIN")
            for offset in range(0, len(encoded), chunk):
                print(f"V61_EXPORT_CHUNK {offset//chunk:04d} {encoded[offset:offset+chunk]}")
            print("V61_EXPORT_END")


if __name__ == "__main__":
    unittest.main()
