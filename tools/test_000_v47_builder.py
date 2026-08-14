#!/usr/bin/env python3
"""Temporary Public Canon v47 prep builder.

This file is mutable prep only. It rewrites the checkout in memory/on disk so
existing repository checkers can validate the exact candidate bytes. It is
removed before the release content commit is frozen.
"""

from __future__ import annotations

import base64
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"
TOOLS = ROOT / "tools"

CLAIM = "TM-SYM2-PHYSICAL-MEASURE"
EVIDENCE_ID = "EV-TM-SYM2-PHYSICAL-MEASURE"
PROBE = "probes/P-TM-SYM2-BORN-HALVING-1"
BUNDLE_SHA = "acc598e670eb7e57f689a6ecc970438ce7211d1a097514a78847100e8871fa59"
SCOPE_SHA = "f9ad8efe676d58a167f84d3ccfb873e511945fd0a7c301a1113aa275032278d0"

SCOPE = (
    "the owner-approved typed L5-to-L6 physical dictionary bridge on the frozen "
    "length-three Thue-Morse window carrier W3: the complete selector-gauge "
    "record C_sel = Sel_class/G with four classes retains epsilon_read = chi_Q "
    "chi_F, the current W3 word, and omega(a,b,c) = c-a; the separately frozen "
    "monomial verb-lift class v_t = delta_t + delta_(t+1) for t in Z/5Z has "
    "F(v_t)_k = zeta_5^(t k)(1 + zeta_5^k), with 1 + zeta_5^k = sigma_(3k)(J) "
    "for k != 0 and k = 0 separately 2, and its coefficient-coordinate Born "
    "square gives the same normalized two-sheet law for every t; combining that "
    "derived conditional with only the public uniform stationary W3 law from "
    "TM-SYM2-PROJECTIVE-FOURFOLD yields a total normalized word measure whose "
    "pushforward is coherent on all 48 frozen selectors and has six equal line "
    "weights 1/6 only as an output; no selector representative is chosen, no "
    "postcomposition gauge is enlarged, orientation is retained at L5 and the "
    "scalar L6 measure is orientation-blind only as a proved output; a "
    "same-modulus nonmonomial lift has unequal coefficient Born weights, so the "
    "registered modulus data alone do not select the monomial lift; no uniqueness "
    "among all amplitude lifts, M_TM confirmation, GYRON identification, D_matter, "
    "decoder-completion, or SI claim is made"
)

D_BLOCK = r'''
### TM-SYM2-PHYSICAL-MEASURE [D]

The surviving TM-SYM2 measure route is closed only as a physical dictionary,
not as a selector theorem. Two L5 objects are frozen as definitions for this
bridge. First,

```text
C_sel  = Sel_class/G,            |C_sel| = 4,
Q_word = W3/<N>,                 |Q_word| = 3,
omega(a,b,c) = c-a.
```

`C_sel` is the four-class selector-gauge record and `Q_word` is the three-shell
word quotient. They are different types and no map `C_sel -> Q_word` is
introduced. The complete L5 source retains the whole `C_sel` record,
`epsilon_read = chi_Q chi_F`, the current word in `W3`, and `omega`. On `W3`,
`omega` is anti-invariant under both complement `N` and reversal `R`, and the
rational joint `(-1,-1)` function sector is one-dimensional, spanned by
`omega`. The `N`, `R`, and `NR` actions remain comparison actions and are not
adopted as gauge. This is `DEF-TM-SYM2-ORIENTATION-SOURCE`.

Second, put `j = zeta_5`, use the exact five-point Fourier convention

```text
F(a)_k = sum_(r in Z/5Z) a_r j^(rk),
v_t = delta_t + delta_(t+1),     t in Z/5Z.
```

The separately frozen monomial verb-lift class obeys

```text
F(v_t)_k = j^(tk) (1+j^k).
```

For `k != 0`, `1+j^k = sigma_(3k)(J)` with
`sigma_a(j)=j^a`; the `k=0` slot is separately `2` and is not called a Galois
conjugate. Exact inverse Fourier transform returns the two-term coefficient
vectors. This is `DEF-TM-SYM2-MONOMIAL-VERB-LIFT`.

The public `ABELIAN-FACE-DICTIONARY [D]` fixes the corresponding face moduli,
but it does not select a phase lift. The distinction is necessary: the frozen
negative control conjugates only the `k=1` spectral slot, preserves all five
pointwise spectral moduli, and has full inverse-Fourier support with unequal
coefficient Born weights. Therefore the modulus data alone do not force the
halving and no uniqueness among all amplitude lifts is claimed.

Within the frozen monomial class, every `v_t` has two equal nonzero coefficient
amplitudes. `MEASURE-BORN-VERB [D]` constrains the physical read to the Born
square of this typed verb. Normalized coordinate square on its support is
independent of `t` and of sheet order and, only after that equality is proved,
is

```text
Born_t = (1/2,1/2).
```

For the other factor, import only the public L5 stationary law on `W3` from
`TM-SYM2-PROJECTIVE-FOURFOLD [T]`. Its already known six-line pushforward and
`M_TM` are not construction inputs. Form the three `N`-orbit marginals of that
window law and then apply the derived two-sheet Born conditional. This gives a
total normalized word measure. Only after construction and normalization its
six word weights, and hence the six line weights under every selector chart,
are read as

```text
mu_B(w) = 1/6,      w in W3.
```

Because the word measure is constant, every one of the 48 frozen selector
charts has the same normalized pushforward. No selector representative is
chosen and no postcomposition gauge is enlarged. The complete L5 source still
contains `epsilon_read`; the scalar L6 measure is orientation-blind only as a
proved output of the total map. The fired N2 conclusion of `TM-SYM2-MEASURE
[F]` remains terminal and is not repaired.

This closes `GATE-L5-L6-TM-SYM2-BORN-MEASURE` as a `DICTIONARY_LIFT` at status
D. The exact finite algebra and the two-architecture audit are evidenced by
`probes/P-TM-SYM2-BORN-HALVING-1`. The status does not rise above D because the
physical Born-of-the-verb assignment is the registered dictionary reading and
the monomial lift is frozen here as the typed bridge input, not selected from
all same-modulus lifts. `GYRON-DENSITY` is not a dependency or confirmation of
this bridge. No `M_TM` confirmation, `D_matter`, decoder-completion, SI, or
all-lift uniqueness claim follows.
'''.lstrip()

OLD_FRONTIER_BLOCK = r'''TM-SYM2-PHYSICAL-MEASURE [O] is the surviving physical L5-to-L6
obligation. A future successor must start from the complete four-orbit
projective-gauge record, retain epsilon_read as typed L5
reading-orientation data, prove coherence on all 48 selectors without
choosing a representative or enlarging the gauge, and derive a normalized
physical measure. Whether that measure agrees with the exact
selector-independent mathematical image mu_i = 1/6 and
M_TM = (1/3)P1 + (2/15)P5, proved by TM-SYM2-PROJECTIVE-FOURFOLD, is an
outcome of the bridge and is not required of it; a closure that assumes
those values, or the typed factorization 1/6 = (1/2)(1/3), is CIRCULAR.
MEASURE-BORN-VERB and GYRON-DENSITY constrain the type of the physical
measure clause; they do not select its values. No successor L5 source
schema is currently frozen. The Born gate remains open but the scheduler
is STOP while a separately reviewed owner definition is absent.

'''

V47_CHANGELOG = r'''Public Canon v47 closes exactly one live measure obligation at dictionary
status. `TM-SYM2-PHYSICAL-MEASURE` moves from O to D. No theorem,
computation, hypothesis, falsification, or other status changes.

The closure uses the completed two-architecture public probe
`P-TM-SYM2-BORN-HALVING-1`. The fold freezes two typed L5 definitions: the
orientation-retaining source on the complete four selector-gauge classes, and
the five-member monomial J-verb lift. The exact coefficient Born square of
every frozen monomial lift gives the same two-sheet conditional. A pinned
same-modulus nonmonomial control has unequal coefficient Born weights, so the
public modulus dictionary does not select the lift phase and no all-lift
uniqueness is claimed.

Only the L5 stationary W3 law is imported from
`TM-SYM2-PROJECTIVE-FOURFOLD [T]`. The physical line value `1/6` is read only
after the typed Born conditional and the stationary word law have been
composed and normalized. All 48 frozen selector charts then agree without a
representative choice or gauge enlargement. The fired N2 selector result is
preserved.

The former `TM-SYM2-PHYSICAL-MEASURE -> GYRON-DENSITY` dependency is removed.
`GYRON-DENSITY` explicitly concerns a different carrier and contributes no L6
physical-measure premise here. `M_TM` and the GYRON numeral are not counted as
confirmation. The closed bridge remains D and adds no `D_matter`, decoder
completion, SI, or physical uniqueness claim.
'''

RATIONAL = (
    "Public Canon v47 closes the typed TM-SYM2 L5-to-L6 Born dictionary at D "
    "from the merged two-architecture P-TM-SYM2-BORN-HALVING-1 result: the "
    "complete four-class orientation record and monomial J-verb lift are frozen, "
    "the public W3 stationary law is imported only at L5, the normalized six-line "
    "1/6 is derived only after the bridge, all 48 selectors are coherent, the "
    "same-modulus control forbids phase selection from ABELIAN-FACE-DICTIONARY "
    "alone, GYRON-DENSITY is removed as a cross-carrier dependency, and the fired "
    "N2 selector result remains terminal; no T promotion, all-lift uniqueness, "
    "D_matter, decoder completion, SI, or gauge enlargement"
)

OUTPUT_FILES = (
    "canon/CANON.md",
    "canon/CORE.md",
    "canon/FRONTIER.md",
    "canon/CHANGELOG.md",
    "canon/SHA256SUMS",
    "canon/EVIDENCE.tsv",
    "canon/HISTORY.tsv",
    "canon/STATUS_COUNTS.tsv",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or ()), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fields, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def patch_evidence() -> None:
    path = CANON / "EVIDENCE.tsv"
    fields, rows = read_tsv(path)
    hits = 0
    for row in rows:
        if row["claim_id"] != CLAIM:
            continue
        hits += 1
        row.update(
            evidence_id=EVIDENCE_ID,
            evidence_kind="PUBLIC_PROBE",
            location=PROBE,
            sha256=BUNDLE_SHA,
            hash_mode="bundle-manifest-sha256-v1",
            architecture_requirement="two-architecture",
        )
    if hits != 1:
        raise AssertionError(f"evidence hits={hits}")
    write_tsv(path, fields, rows)


def patch_history() -> None:
    path = CANON / "HISTORY.tsv"
    fields, rows = read_tsv(path)
    own = [row for row in rows if row["claim_id"] == CLAIM]
    if [int(row["event_sequence"]) for row in own] != [1, 2]:
        raise AssertionError("unexpected TM-SYM2 history chain")
    if any(row["release"] == "canon-v47" and row["claim_id"] == CLAIM for row in rows):
        raise AssertionError("v47 event already exists")
    rows.append(
        {
            "event_id": "CANON47-STATUS-TM-SYM2-PHYSICAL-MEASURE-3",
            "event_sequence": "3",
            "event_date": "2026-08-14",
            "release": "canon-v47",
            "claim_id": CLAIM,
            "event_type": "STATUS_CHANGE",
            "previous_status": "O",
            "new_status": "D",
            "scope_sha256": SCOPE_SHA,
            "evidence_id": EVIDENCE_ID,
            "evidence_location": PROBE,
            "evidence_sha256": BUNDLE_SHA,
            "rationale": RATIONAL,
        }
    )
    write_tsv(path, fields, rows)


def patch_canon() -> None:
    path = CANON / "CANON.md"
    text = path.read_text(encoding="utf-8")
    if text.count("Public Canon v46") < 4:
        raise AssertionError("unexpected v46 release-reference count")
    text = text.replace("Public Canon v46", "Public Canon v47")
    if "### TM-SYM2-PHYSICAL-MEASURE [D]" in text:
        raise AssertionError("D block already present")
    anchor = "The conformal mode prefactor K_chi5 =\n"
    if text.count(anchor) != 1:
        raise AssertionError("TM-SYM2 insertion anchor drift")
    text = text.replace(anchor, D_BLOCK + "\n" + anchor)
    if text.count(OLD_FRONTIER_BLOCK) != 1:
        raise AssertionError("old O frontier block drift")
    text = text.replace(OLD_FRONTIER_BLOCK, "")
    path.write_text(text, encoding="utf-8")


def patch_changelog() -> None:
    path = CANON / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    if "## Public Canon v47" in text:
        raise AssertionError("v47 changelog already present")
    text = re.sub(
        r"\n?<!-- BEGIN GENERATED CURRENT COUNTS -->.*?<!-- END GENERATED CURRENT COUNTS -->\n?",
        "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    anchor = "# Canon changelog (public series)\n"
    if not text.startswith(anchor):
        raise AssertionError("changelog heading drift")
    body = text[len(anchor):].lstrip("\n")
    text = (
        anchor
        + "\n\n## Public Canon v47\n\n"
        + V47_CHANGELOG
        + "\n\n"
        + body
    )
    path.write_text(text, encoding="utf-8")


def write_sha256s() -> None:
    names = ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")
    lines = []
    for name in names:
        digest = sha256_bytes((CANON / name).read_bytes())
        lines.append(f"{digest}  canon/{name}\n")
    (CANON / "SHA256SUMS").write_text("".join(lines), encoding="utf-8")


def temporary_release_form() -> None:
    canon_bytes = (CANON / "CANON.md").read_bytes()
    canon_sha = sha256_bytes(canon_bytes)
    canon_len = len(canon_bytes)

    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    status = status.replace("CANON:          Public Canon v46", "CANON:          Public Canon v47")
    status = status.replace("TAG:            canon-v46", "TAG:            canon-v47")
    status = re.sub(r"^CANON_SHA256:\s+[0-9a-f]{64}$", f"CANON_SHA256:   {canon_sha}", status, flags=re.MULTILINE)
    status = re.sub(r"^CANON_BYTES:\s+[0-9]+$", f"CANON_BYTES:    {canon_len}", status, flags=re.MULTILINE)
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = readme.replace("Public Canon v46", "Public Canon v47")
    readme = readme.replace("canon-v46", "canon-v47")
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    citation = citation.replace("Public Canon v46", "Public Canon v47")
    citation = re.sub(r'^version:\s*"46"\s*$', 'version: "47"', citation, flags=re.MULTILINE)
    citation = re.sub(r"^date-released:\s*\d{4}-\d{2}-\d{2}\s*$", "date-released: 2026-08-14", citation, flags=re.MULTILINE)
    (ROOT / "CITATION.cff").write_text(citation, encoding="utf-8")


def run_checked(*args: str) -> str:
    result = subprocess.run(
        [sys.executable, *args], cwd=ROOT, capture_output=True, text=True
    )
    if result.returncode:
        raise AssertionError(
            f"command failed: {' '.join(args)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result.stdout


def print_transport_package() -> None:
    payload: dict[str, str] = {}
    for relative in OUTPUT_FILES:
        data = (ROOT / relative).read_bytes()
        payload[relative] = base64.b64encode(data).decode("ascii")
        print(
            f"V47_FILE {relative} bytes={len(data)} sha256={sha256_bytes(data)}"
        )
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("ascii")
    packed = base64.b64encode(zlib.compress(raw, 9)).decode("ascii")
    print(f"V47_PACKAGE_RAW_BYTES={len(raw)}")
    print(f"V47_PACKAGE_ZLIB_B64_CHARS={len(packed)}")
    print("V47_PACKAGE_ZLIB_B64_BEGIN")
    for i in range(0, len(packed), 1600):
        print(packed[i:i+1600])
    print("V47_PACKAGE_ZLIB_B64_END")


class V47ContentBuilder(unittest.TestCase):
    def test_build_and_validate_content_candidate(self) -> None:
        registry_fields, registry = read_tsv(CANON / "REGISTRY.tsv")
        self.assertTrue(registry_fields)
        row = next(row for row in registry if row["claim_id"] == CLAIM)
        self.assertEqual(row["status"], "D")
        self.assertEqual(row["scope"], SCOPE)
        self.assertEqual(sha256_bytes(SCOPE.encode("utf-8")), SCOPE_SHA)

        patch_evidence()
        patch_history()
        patch_canon()
        patch_changelog()

        generated = run_checked(str(TOOLS / "generate_canon_views.py"), "--apply")
        self.assertIn("GENERATED VIEWS UPDATED", generated)
        write_sha256s()

        ledger = run_checked(str(TOOLS / "check_ledger.py"))
        self.assertIn("claims=241", ledger)
        self.assertIn("items=259", ledger)
        self.assertIn("dependencies=384", ledger)
        self.assertIn("evidence=241", ledger)
        self.assertIn("history=756", ledger)
        self.assertIn("gates=10", ledger)

        # Validate the complete release-facing bytes under a temporary v47
        # release form. These three temporary files are not transported into the
        # content commit; the real release-form commit is made only after the
        # content commit has a stable Git SHA.
        temporary_release_form()
        canon_check = run_checked(str(TOOLS / "check_canon.py"))
        self.assertIn("CANON PASS v47 claims=241", canon_check)

        print("V47_LEDGER=" + ledger.strip())
        print("V47_CANON=" + canon_check.strip())
        print_transport_package()


if __name__ == "__main__":
    unittest.main()
