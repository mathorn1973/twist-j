#!/usr/bin/env python3
"""
Finalize the Public Canon v49 QDD instrument nonselection fold.

Run on release/canon-v49 at the exact public v48 main
8291fae4dab53c3b3f7507eca88e5f9668e8033b. The script:
  1. folds QDD-INSTRUMENT-NONSELECTION [T] at L4 from the completed public probe;
  2. narrows QDD-INSTRUMENT-APPARATUS [O] to independent selection and sampling;
  3. updates the Canon ledgers, generated views, status-separation audit and hashes;
  4. runs decisive repository checks;
  5. creates exactly one content commit and one release-form commit;
  6. runs check_activation --full and never pushes, merges, tags or releases.

Every write is guarded by exact anchors and every commit uses an explicit path list.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
CANON = ROOT / "canon"
BASE = "8291fae4dab53c3b3f7507eca88e5f9668e8033b"
PROBE = "probes/P-QDD-INSTRUMENT-NONSELECTION-1"
PROBE_DIGEST = "d49930ce735413cb58601d85d697b6dc049e5571f50cdf16d837206db26727e2"
FINALIZER = "notes/canon/finalize_fold_v49.py"


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(list(args), cwd=ROOT, capture_output=True, text=True)
    if check and result.returncode:
        print(result.stdout[-3000:])
        print(result.stderr[-3000:])
        raise SystemExit("command failed: " + " ".join(args))
    return result


def decisive(argv: list[str], label: str) -> str:
    result = run(*argv, check=False)
    combined = (result.stdout + result.stderr).strip()
    print(f"[{label}] " + ((combined.splitlines() or ["(no output)"])[-1]))
    if result.returncode:
        print(combined[-3000:])
        raise SystemExit(f"decisive check failed: {label}; DO NOT COMMIT OR PUSH")
    return combined


def rw(path: Path, substitutions: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in substitutions:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"{path}: expected one anchor, found {count}: {old[:100]!r}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def write_lines(path: Path, values: list[str]) -> None:
    path.write_text("\n".join(values) + "\n", encoding="utf-8")


def insert_before_row(path: Path, anchor_id: str, new_rows: list[str]) -> None:
    values = lines(path)
    positions = [i for i, row in enumerate(values) if row.startswith(anchor_id + "\t")]
    if len(positions) != 1:
        raise SystemExit(f"{path}: expected one row {anchor_id}, found {len(positions)}")
    for row in new_rows:
        if "\n" in row or row.count("\t") == 0:
            raise SystemExit(f"{path}: malformed inserted row")
        row_id = row.split("\t", 1)[0]
        if any(existing.startswith(row_id + "\t") for existing in values):
            raise SystemExit(f"{path}: duplicate row id {row_id}")
    at = positions[0]
    values[at:at] = new_rows
    write_lines(path, values)


def replace_row(path: Path, row_id: str, new_row: str) -> None:
    values = lines(path)
    positions = [i for i, row in enumerate(values) if row.startswith(row_id + "\t")]
    if len(positions) != 1:
        raise SystemExit(f"{path}: expected one row {row_id}, found {len(positions)}")
    if "\n" in new_row:
        raise SystemExit(f"{path}: replacement row contains newline")
    values[positions[0]] = new_row
    write_lines(path, values)


def append_rows(path: Path, new_rows: list[str]) -> None:
    values = lines(path)
    ids = {row.split("\t", 1)[0] for row in values[1:]}
    for row in new_rows:
        row_id = row.split("\t", 1)[0]
        if row_id in ids:
            raise SystemExit(f"{path}: duplicate appended row id {row_id}")
        values.append(row)
        ids.add(row_id)
    write_lines(path, values)


def changed_paths() -> set[str]:
    paths: set[str] = set()
    for row in run("git", "status", "--porcelain").stdout.splitlines():
        if "->" in row:
            raise SystemExit("unexpected rename: " + row)
        if row.strip():
            paths.add(row[3:].strip())
    return paths


def commit_named(allow: list[str], message: str, exact: bool = False) -> None:
    changed = changed_paths()
    unexpected = sorted(changed - set(allow))
    if unexpected:
        raise SystemExit(f"refusing {message!r}; unexpected paths: {unexpected}")
    if exact and changed != set(allow):
        raise SystemExit(
            f"refusing {message!r}; expected {sorted(allow)}, found {sorted(changed)}"
        )
    selected = sorted(changed)
    if not selected:
        raise SystemExit(f"nothing to commit for {message!r}")
    run("git", "add", "--", *selected)
    staged = set(run("git", "diff", "--cached", "--name-only").stdout.splitlines())
    if staged != set(selected):
        raise SystemExit(f"staged paths differ for {message!r}")
    run("git", "commit", "-q", "-m", message)
    if run("git", "status", "--porcelain").stdout.strip():
        raise SystemExit(f"tree is not clean after {message!r}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bundle_sha256(path: Path) -> str:
    manifest: list[str] = []
    for item in sorted(
        (candidate for candidate in path.rglob("*") if candidate.is_file()),
        key=lambda candidate: candidate.relative_to(ROOT).as_posix(),
    ):
        relative_parts = item.relative_to(path).parts
        if "__pycache__" in item.parts or item.suffix == ".pyc" or "RUNS" in relative_parts:
            continue
        relative = item.relative_to(ROOT).as_posix()
        manifest.append(f"{sha256_bytes(item.read_bytes())}  {relative}\n")
    return sha256_bytes("".join(manifest).encode("utf-8"))


def scope_sha(scope: str) -> str:
    return sha256_bytes(scope.encode("utf-8"))


branch = run("git", "branch", "--show-current").stdout.strip()
head = run("git", "rev-parse", "HEAD").stdout.strip()
if branch != "release/canon-v49" or head != BASE:
    raise SystemExit(f"wrong release base: branch={branch} head={head}")
if changed_paths() != {FINALIZER}:
    raise SystemExit(f"initial tree must differ only by {FINALIZER}: {sorted(changed_paths())}")
if bundle_sha256(ROOT / PROBE) != PROBE_DIGEST:
    raise SystemExit("public probe bundle hash mismatch; STOP")

theorem_scope = (
    "at L4 apparatus/support scope over V=Q^4 with G=I_4-(1/5)11^T, "
    "A^sharp=G^-1 A^T G, E_low=(1/4)11^T and E_high=I_4-E_low: for "
    "every nonzero G-self-adjoint idempotent E, "
    "{K:K^sharp K=E}={W E:W in O(G,Q)}; for the frozen ordered pair the raw "
    "fibre is one branchwise O(G,Q) x O(G,Q) orbit, while Gamma_ab=K_a^sharp "
    "K_b completely classifies diagonal O(G,Q) orbits and "
    "C=K_low^sharp K_high ranges over {E_low O E_high:O in O(G,Q)}; under the "
    "frozen pure density-operator post-state definition, equality inside one "
    "nonzero effect fibre is exactly K~+/-K; the rational family "
    "K_low(t)=E_low, K_high(t)=R_t E_high injects Q into physically distinct "
    "post-state instrument classes at fixed effects, fixed branch weights and "
    "C=0; every rational subspace isometry of a positive-definite rational "
    "bilinear space extends by rational reflections, hence every complete "
    "rational two-branch family has a rational orthogonal dilation on the "
    "frozen system/pointer type and unrestricted dilation existence is not an "
    "instrument-selection principle; a coupling already controlled by the "
    "target projectors is circular as independent selection evidence, and "
    "G-self-adjointness plus G-positivity uniquely gives K=E only as a "
    "mathematical positive-square-root section; K^T G K=G E reproduces the "
    "frozen occurrence weights globally; theorem-grade written proof with an "
    "exact two-architecture audit; no physical selector, no adoption of "
    "positivity or minimal disturbance as a law, no L5 realized-event stream, "
    "no L6 measure, no decoder completion, no SI statement, and SAMPLING NOT "
    "PROVIDED rather than SAMPLING IMPOSSIBLE"
)
theorem_falsifier = (
    "fires if an exact rational counterexample violates the single-branch "
    "fibre classification, branchwise raw-orbit statement, Gamma completeness, "
    "post-state equivalence K~+/-K, pairwise injectivity of the R_t family, "
    "rational reflection extension, rational orthogonal-dilation surjectivity, "
    "target-control circularity, the positive-square-root section, or "
    "K^T G K=G E; a restricted coupling class not covered by the theorem, or "
    "absence of a sampling construction, is not a falsifier"
)
apparatus_scope = (
    "the physical realization of the frozen ordered effect pair "
    "(E_low,E_high) after QDD-INSTRUMENT-NONSELECTION: exact rational apparatus "
    "existence and reduction to the Lueder pair are exhibited, but only two "
    "independent blockers remain, O2 independent physical instrument selection "
    "from an admissible law or coupling class frozen before comparison with the "
    "target effects, and O1 realized event generation / sampling; "
    "target-controlled coupling is circular as independent-selection evidence, "
    "G-positive square-root uniqueness is mathematics only, equality of effects "
    "does not identify post-state instruments; filling no field of the decoder "
    "completion contract, the row remains separate from QUADRATIC-DECODER-DATA; "
    "SAMPLING NOT PROVIDED, and SAMPLING IMPOSSIBLE is not claimed"
)
apparatus_decision = (
    "STOP until O2 supplies a public independently specified physical selector "
    "or apparatus dynamics, with its admissible class and complete acyclic "
    "dependencies frozen before comparison with E_low,E_high and with no new "
    "free dimensionless input, and O1 supplies a typed realized-event and "
    "sampling map; closes positively only when both blockers close and the "
    "selected family realizes the frozen ordered effects and occurrence law "
    "exactly; closes negatively only for a frozen complete admissible physical "
    "class proved empty or proved unable to realize the effect pair or event "
    "law; failure to provide sampling remains STOP, not a sampling-impossibility "
    "theorem"
)

registry = CANON / "REGISTRY.tsv"
old_app_row = next(row for row in lines(registry) if row.startswith("QDD-INSTRUMENT-APPARATUS\t"))
old_app_fields = old_app_row.split("\t")
if len(old_app_fields) != 6 or old_app_fields[1] != "O":
    raise SystemExit("unexpected QDD-INSTRUMENT-APPARATUS registry row")
new_theorem_row = "\t".join((
    "QDD-INSTRUMENT-NONSELECTION", "T", theorem_scope,
    "2. Time, space, and the decoder", PROBE, theorem_falsifier,
))
new_app_row = "\t".join((
    "QDD-INSTRUMENT-APPARATUS", "O", apparatus_scope,
    "2. Time, space, and the decoder", "inline", apparatus_decision,
))
insert_before_row(registry, "QDD-INSTRUMENT-APPARATUS", [new_theorem_row])
replace_row(registry, "QDD-INSTRUMENT-APPARATUS", new_app_row)

canon_path = CANON / "CANON.md"
old_apparatus_block = """QDD-INSTRUMENT-APPARATUS [O]
    the physical instrument family {K_a} with E_a = K_a^sharp K_a realizing
    the frozen ordered pair (E_low, E_high) as physical effects, from a
    public apparatus carrier, ready state, coupling, pointer and reduction,
    with occurrence law, sampling, post-state and completeness of the
    admissible class; registered separately from QUADRATIC-DECODER-DATA and
    filling no field of the decoder completion contract; reverse inference
    from effects to instruments is forbidden and equality of effects does not
    identify post-state instruments.
"""
new_instrument_block = """QDD-INSTRUMENT-NONSELECTION [T]
    At L4 apparatus/support scope over V = Q^4, freeze
    G = I_4 - (1/5) 1 1^T, A^sharp = G^-1 A^T G,
    E_low = (1/4) 1 1^T and E_high = I_4 - E_low. Every nonzero
    G-self-adjoint idempotent effect fibre is {W E : W in O(G,Q)}. The ordered raw
    two-branch fibre is one branchwise O(G,Q) x O(G,Q) orbit, not one
    diagonal orbit; Gamma_ab = K_a^sharp K_b completely classifies diagonal
    orbits, with C = K_low^sharp K_high the complete two-branch invariant.
    Under the frozen pure density-operator post-state definition, physical
    equivalence inside one nonzero effect fibre is exactly K ~ +/-K.
    The rational rotations R_t on im(E_high) therefore give an injection
    Q -> physical post-state instrument classes at fixed effects, fixed
    branch weights and C = 0. Every rational isometry between subspaces of a
    positive-definite rational bilinear space extends by rational reflections,
    so every complete rational two-branch family has a rational orthogonal
    dilation on the frozen system/pointer type. Existence of an unrestricted
    rational orthogonal dilation is therefore not an instrument-selection
    principle. A coupling already controlled by the target projectors is
    circular as independent-selection evidence. G-self-adjointness and
    G-positivity select K = E only as a mathematical positive-square-root
    section, not as a physical law. Finally K^T G K = G E reproduces the
    frozen occurrence weights globally. No physical selector, L5
    realized-event stream, L6 measure, decoder completion or SI statement;
    SAMPLING NOT PROVIDED, not SAMPLING IMPOSSIBLE.
QDD-INSTRUMENT-APPARATUS [O]
    after the nonselection theorem only two independent blockers remain:
    O2, independent physical instrument selection from a public admissible
    law or coupling class frozen before comparison with E_low and E_high;
    O1, realized event generation and sampling. An exact rational apparatus
    reducing to the Lueder pair is exhibited, but its target-controlled
    coupling is circular as independent-selection evidence. Positive-root
    uniqueness is mathematics only, equality of effects does not identify
    post-state instruments, the row remains separate from
    QUADRATIC-DECODER-DATA and fills no decoder-completion-contract field.
    SAMPLING NOT PROVIDED; SAMPLING IMPOSSIBLE is not claimed.
"""
rw(canon_path, [
    (
        "The quadratic leg of `D_matter` gains its exact algebra as public definitions\n"
        "and theorems on the finite balanced piston carrier. Everything below is L1\n"
        "exact algebra. Nothing here fills the decoder completion contract, claims an\n"
        "L6 reading, selects an apparatus, derives the architecture or the effect pair\n"
        "from J, or changes `QUADRATIC-DECODER-DATA`, which remains an open obligation\n"
        "[O]: the physical effect selection and the completion contract stay open under\n"
        "the EFFECT_SHADOW_MINIMAL owner freeze, and the physical instrument family is\n"
        "the separate obligation `QDD-INSTRUMENT-APPARATUS`.\n",
        "The quadratic leg of `D_matter` gains its exact algebra as public definitions\n"
        "and theorems on the finite balanced piston carrier. The Route A factorization\n"
        "block is L1 exact algebra. The later instrument nonselection theorem is L4\n"
        "apparatus/support mathematics. Nothing here fills the decoder completion\n"
        "contract, claims an L6 reading, selects a physical instrument, derives the\n"
        "architecture or the effect pair from J, or changes\n"
        "`QUADRATIC-DECODER-DATA`, which remains an open obligation [O]. The physical\n"
        "instrument realization remains the separate obligation\n"
        "`QDD-INSTRUMENT-APPARATUS`.\n",
    ),
    (
        "Theorems and the separate apparatus obligation.\n",
        "L1 theorems, the L4 instrument nonselection theorem, and the separate\n"
        "apparatus obligation.\n",
    ),
    (old_apparatus_block, new_instrument_block),
    (
        "  QDD-INSTRUMENT-APPARATUS   the physical instrument family {K_a} with\n"
        "                             E_a = K_a^sharp K_a realizing the frozen ordered\n"
        "                             effect pair as physical effects; apparatus\n"
        "                             carrier, ready state, coupling, pointer,\n"
        "                             reduction, occurrence law, sampling and\n"
        "                             post-state remain open; fills no completion\n"
        "                             contract field\n",
        "  QDD-INSTRUMENT-NONSELECTION\n"
        "                             the L4 rational fibre, diagonal-orbit and\n"
        "                             dilation classification; fixed effects, weights\n"
        "                             and C = 0 leave infinitely many physical\n"
        "                             post-state classes, and dilation existence does\n"
        "                             not select an instrument\n"
        "  QDD-INSTRUMENT-APPARATUS   only O2 independent physical instrument selection\n"
        "                             and O1 realized event generation / sampling remain;\n"
        "                             SAMPLING NOT PROVIDED, not impossible; fills no\n"
        "                             completion-contract field\n",
    ),
])

disclosure_anchor = (
    "byte-identical on the public x86_64 and aarch64 jobs, RESULT 15/15 ALL PASS.\n"
)
disclosure_add = (
    disclosure_anchor
    + "\nAt L4, `P-QDD-INSTRUMENT-NONSELECTION-1` supplies the theorem-grade written\n"
      "proof and exact two-architecture audit for S1a-S6. It proves an injective\n"
      "rational family of physically distinct post-state instruments at fixed effects,\n"
      "weights and C = 0 and proves rational orthogonal-dilation surjectivity. It does\n"
      "not select a physical family or create an event stream or measure.\n"
)
rw(canon_path, [(disclosure_anchor, disclosure_add)])

normative = CANON / "NORMATIVE.tsv"
insert_before_row(normative, "QDD-INSTRUMENT-APPARATUS", [
    "\t".join((
        "QDD-INSTRUMENT-NONSELECTION", "THEOREM",
        "QDD-INSTRUMENT-NONSELECTION", "T", "L4", "",
        "canon/CANON.md::QDD Route A dictionary",
    ))
])

evidence = CANON / "EVIDENCE.tsv"
insert_before_row(evidence, "QDD-INSTRUMENT-APPARATUS", [
    "\t".join((
        "QDD-INSTRUMENT-NONSELECTION", "EV-QDD-INSTRUMENT-NONSELECTION",
        "PUBLIC_PROBE", PROBE, PROBE_DIGEST, "bundle-manifest-sha256-v1",
        "two-architecture",
    ))
])
replace_row(evidence, "QDD-INSTRUMENT-APPARATUS", "\t".join((
    "QDD-INSTRUMENT-APPARATUS", "EV-QDD-INSTRUMENT-APPARATUS",
    "INLINE_CANON", "inline", scope_sha(apparatus_scope),
    "registry-scope-sha256-v1", "none",
)))

history = CANON / "HISTORY.tsv"
append_rows(history, [
    "\t".join((
        "CANON49-DECLARE-QDD-INSTRUMENT-NONSELECTION", "1", "2026-08-16",
        "canon-v49-candidate", "QDD-INSTRUMENT-NONSELECTION", "DECLARE", "-", "T",
        scope_sha(theorem_scope), "EV-QDD-INSTRUMENT-NONSELECTION", PROBE,
        PROBE_DIGEST,
        "Public Canon v49 registers the theorem-grade L4 rational fibre, diagonal-orbit and orthogonal-dilation nonselection result S1a-S6 from the merged public probe; fixed effects, weights and C=0 retain an injective rational family of distinct post-state instruments, while no physical selector, L5 stream, L6 measure, decoder completion, SI statement or sampling-impossibility theorem is added",
    )),
    "\t".join((
        "CANON49-SCOPE-QDD-INSTRUMENT-APPARATUS", "2", "2026-08-16",
        "canon-v49-candidate", "QDD-INSTRUMENT-APPARATUS", "SCOPE_CHANGE", "O", "O",
        scope_sha(apparatus_scope), "EV-QDD-INSTRUMENT-APPARATUS", "inline",
        scope_sha(apparatus_scope),
        "Public Canon v49 narrows the still-open apparatus obligation to exactly O2 independent physical instrument selection and O1 realized event generation or sampling; target-controlled coupling is circular evidence, positive-root uniqueness is mathematics only, and the permitted sampling statement is SAMPLING NOT PROVIDED rather than SAMPLING IMPOSSIBLE",
    )),
])

rw(canon_path, [
    ("# TWIST-J Public Canon v48\n", "# TWIST-J Public Canon v49\n"),
    (
        "**Release identity.** Public Canon v48. Normative authority and activation",
        "**Release identity.** Public Canon v49. Normative authority and activation",
    ),
    (
        "algebraic axiom is J. Public Canon v48 also declares the discrete",
        "algebraic axiom is J. Public Canon v49 also declares the discrete",
    ),
    (
        "seed of the two algebraic projections. Public Canon v48 does not claim",
        "seed of the two algebraic projections. Public Canon v49 does not claim",
    ),
    (
        "deriving the architecture from J; Public Canon v48 contains no such",
        "deriving the architecture from J; Public Canon v49 contains no such",
    ),
])

changelog = CANON / "CHANGELOG.md"
change_text = changelog.read_text(encoding="utf-8")
match = re.search(
    r"## Public Canon v48\n\n"
    r"(<!-- BEGIN GENERATED CURRENT COUNTS -->\n.*?"
    r"<!-- END GENERATED CURRENT COUNTS -->\n)\n",
    change_text,
    re.S,
)
if not match:
    raise SystemExit("v48 generated counts block not found")
counts_block = match.group(1)
change_text = change_text.replace(match.group(0), "## Public Canon v48\n\n", 1)
entry = f"""## Public Canon v49

{counts_block}
Public Canon v49 registers exactly one new scientific row,
`QDD-INSTRUMENT-NONSELECTION [T]`, at L4 apparatus/support scope from the
completed public probe `P-QDD-INSTRUMENT-NONSELECTION-1`. Its written proof
classifies every rational single-effect fibre, the branchwise and diagonal
two-branch orbits, physical post-state equivalence, and rational orthogonal
dilations. At fixed effects, fixed branch weights and `C = 0`, an injective
rational family of physically distinct post-state instruments remains.
Existence of an unrestricted rational orthogonal dilation therefore cannot
select a physical instrument.

The fold keeps `QDD-INSTRUMENT-APPARATUS [O]` open and narrows it to two
independent blockers: O2 independent physical instrument selection, and O1
realized event generation / sampling. A coupling controlled by the target
projectors is circular as independent-selection evidence. G-positive
square-root uniqueness remains mathematics only. The only sampling statement
is `SAMPLING NOT PROVIDED`; no sampling-impossibility theorem is claimed.

No L5 stream, L6 measure, decoder completion, new physical premise, SI
statement, uniqueness-from-J claim, or change to `QUADRATIC-DECODER-DATA`
is made.


"""
change_text = change_text.replace(
    "# Canon changelog (public series)\n\n\n",
    "# Canon changelog (public series)\n\n\n" + entry,
    1,
)
changelog.write_text(change_text, encoding="utf-8")

# Update the release audit before generated views so the whole folded tree is checked.
status_verify = ROOT / "reproduce" / "status-separation" / "verify.py"
rw(status_verify, [
    (
        'expected_counts = {"T": 138, "D": 42, "C": 27, "F": 13,\n'
        '                       "O": 23, "H": 2}',
        'expected_counts = {"T": 139, "D": 42, "C": 27, "F": 13,\n'
        '                       "O": 23, "H": 2}',
    ),
    (
        '"registry and companion-ledger counts match Public Canon v48",',
        '"registry and companion-ledger counts match Public Canon v49",',
    ),
    ("len(rows) == 245", "len(rows) == 246"),
    ("and len(normative) == 280", "and len(normative) == 281"),
    ("and len(evidence) == 245", "and len(evidence) == 246"),
    ("and two_architecture == 164", "and two_architecture == 165"),
    ("and len(history) == 760", "and len(history) == 762"),
])

check_anchor = """    fw_requires = {}
    for row in dependencies:
"""
new_check = """    nonselection = "QDD-INSTRUMENT-NONSELECTION"
    nonselection_path = "probes/P-QDD-INSTRUMENT-NONSELECTION-1"
    nonselection_digest = (
        "d49930ce735413cb58601d85d697b6dc049e5571f50cdf16d837206db26727e2"
    )
    nonselection_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == nonselection
    }
    apparatus_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == "QDD-INSTRUMENT-APPARATUS"
    }
    checks.append((
        "QDD-NONSELECTION",
        "the L4 theorem fixes rational fibre, post-state and dilation nonselection while the apparatus remains O on exactly independent selection and realized-event sampling",
        has_status(index, nonselection, "T")
        and normative.get(nonselection, {}).get("item_type") == "THEOREM"
        and normative.get(nonselection, {}).get("status") == "T"
        and normative.get(nonselection, {}).get("layer") == "L4"
        and normative.get(nonselection, {}).get("gate_ids") == ""
        and index.get(nonselection, {}).get("evidence") == nonselection_path
        and evidence.get(nonselection, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(nonselection, {}).get("location") == nonselection_path
        and evidence.get(nonselection, {}).get("sha256") == nonselection_digest
        and evidence.get(nonselection, {}).get("architecture_requirement")
        == "two-architecture"
        and nonselection not in programs
        and all(row["owner_item_id"] != nonselection for row in gates.values())
        and nonselection_dependencies == set()
        and apparatus_dependencies == {
            ("DEF-QDD-PROJECTOR-LOW", "REQUIRES"),
            ("DEF-QDD-PROJECTOR-HIGH", "REQUIRES"),
            ("DEF-QDD-GRAM", "REQUIRES"),
        }
        and scope_contains_all(
            index, nonselection,
            ("one branchwise O(G,Q) x O(G,Q) orbit",
             "injects Q into physically distinct post-state instrument classes",
             "not an instrument-selection principle",
             "mathematical positive-square-root section",
             "no L5 realized-event stream",
             "no L6 measure",
             "SAMPLING NOT PROVIDED rather than SAMPLING IMPOSSIBLE"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-APPARATUS",
            ("only two independent blockers remain",
             "O2 independent physical instrument selection",
             "O1 realized event generation / sampling",
             "target-controlled coupling is circular",
             "SAMPLING NOT PROVIDED",
             "SAMPLING IMPOSSIBLE is not claimed"),
        )
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and has_status(index, "QUADRATIC-DECODER-DATA", "O"),
    ))

""" + check_anchor
rw(status_verify, [(check_anchor, new_check)])

status_readme = ROOT / "reproduce" / "status-separation" / "README.md"
v49_paragraph = (
    "The v49 count check reads the folded tree (246 claims, 23 reproductions, "
    "10 gates). The new QDD-NONSELECTION check pins the theorem at L4 on the "
    "completed two-architecture public probe, its self-contained frozen inputs "
    "and absence of dependency, gate or frontier ownership. It requires the injective rational "
    "post-state family at fixed effects, weights and C = 0, rational "
    "orthogonal-dilation nonselection, target-control circularity and the "
    "positive-root mathematics-only boundary. QDD-INSTRUMENT-APPARATUS stays O "
    "at DECODER_CORE/FOLLOWUP/STOP with exactly O2 independent physical "
    "instrument selection and O1 realized event generation / sampling. "
    "SAMPLING NOT PROVIDED; no L5 stream, L6 measure or decoder completion.\n\n"
)
rw(status_readme, [
    ("Its thirty-four checks cover the current", "Its thirty-five checks cover the current"),
    ("Expected: byte-identical output to `EXPECTED.txt`, `RESULT 32/32 ALL PASS`,",
     "Expected: byte-identical output to `EXPECTED.txt`, `RESULT 35/35 ALL PASS`,"),
    ("The v48 count check reads the folded tree", v49_paragraph + "The v48 count check reads the folded tree"),
])

# Generated views validate the modified ledgers and update CORE, FRONTIER and counts.
run(sys.executable, "tools/generate_canon_views.py", "--apply")

# Update architecture-report anchored counts from the actual folded graph.
sys.path.insert(0, str(ROOT / "tools"))
import architecture_map_report as architecture  # noqa: E402

report = architecture.audit(ROOT)
sc = report.status_counts
ec = report.evidence_counts
rw(ROOT / "tools" / "test_architecture_map_report.py", [
    ("self.assertEqual(self.report.claims, 245)",
     f"self.assertEqual(self.report.claims, {report.claims})"),
    ('{"C": 27, "D": 42, "F": 13, "H": 2, "O": 23, "T": 138}',
     '{"C": %d, "D": %d, "F": %d, "H": %d, "O": %d, "T": %d}'
     % (sc["C"], sc["D"], sc["F"], sc["H"], sc["O"], sc["T"])),
    ('                "none": 41,\n'
     '                "one-architecture": 9,\n'
     '                "recorded-audit": 31,\n'
     '                "two-architecture": 164,',
     '                "none": %d,\n'
     '                "one-architecture": %d,\n'
     '                "recorded-audit": %d,\n'
     '                "two-architecture": %d,'
     % (ec["none"], ec["one-architecture"], ec["recorded-audit"], ec["two-architecture"])),
    ("self.assertEqual(len(self.report.direct_architecture_requires), 176)",
     f"self.assertEqual(len(self.report.direct_architecture_requires), {len(report.direct_architecture_requires)})"),
    ("len(self.report.transitive_architecture_dependents), 205",
     f"len(self.report.transitive_architecture_dependents), {len(report.transitive_architecture_dependents)}"),
    ("self.assertEqual(len(self.report.dependency_terminals), 23)",
     f"self.assertEqual(len(self.report.dependency_terminals), {len(report.dependency_terminals)})"),
])

# Regenerate the exact expected stdout of the structural audit.
audit = run(sys.executable, "reproduce/status-separation/verify.py", check=False)
if audit.returncode or audit.stderr:
    print((audit.stdout + audit.stderr)[-3000:])
    raise SystemExit("status-separation audit failed or wrote stderr")
(ROOT / "reproduce" / "status-separation" / "EXPECTED.txt").write_text(
    audit.stdout, encoding="utf-8"
)
if "RESULT 35/35 ALL PASS\n" not in audit.stdout:
    raise SystemExit("status-separation did not produce 35/35")

def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())

(CANON / "SHA256SUMS").write_text(
    "".join(
        f"{sha256_file(CANON / name)}  canon/{name}\n"
        for name in ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")
    ),
    encoding="utf-8",
)

fold_allow = [
    FINALIZER,
    "canon/CANON.md", "canon/CORE.md", "canon/FRONTIER.md",
    "canon/CHANGELOG.md", "canon/REGISTRY.tsv", "canon/NORMATIVE.tsv",
    "canon/EVIDENCE.tsv", "canon/HISTORY.tsv",
    "canon/SHA256SUMS", "canon/STATUS_COUNTS.tsv",
    "reproduce/status-separation/verify.py",
    "reproduce/status-separation/EXPECTED.txt",
    "reproduce/status-separation/README.md",
    "tools/test_architecture_map_report.py",
]
stage_allow = ["STATUS.md", "README.md", "CITATION.cff"]

decisive([sys.executable, "tools/check_policy.py"], "check_policy")
unit = run(sys.executable, "-m", "unittest", "discover", "-s", "tools", "-p", "test_*.py", check=False)
print("[unittest] " + ((unit.stderr.strip().splitlines() or ["(no output)"])[-1]))
if unit.returncode:
    print((unit.stdout + unit.stderr)[-3000:])
    raise SystemExit("decisive check failed: unittest; DO NOT COMMIT OR PUSH")
decisive([sys.executable, "tools/check_ledger.py"], "check_ledger")
decisive([sys.executable, "tools/check_status_labels.py"], "check_status_labels")

commit_named(fold_allow, "Fold QDD instrument nonselection theorem into Canon v49")
content_commit = run("git", "rev-parse", "HEAD").stdout.strip()
canon_bytes = canon_path.read_bytes()
canon_hash = sha256_bytes(canon_bytes)
print("content commit", content_commit)
print("canon sha", canon_hash)
print("canon bytes", len(canon_bytes))

rw(ROOT / "STATUS.md", [
    ("CANON:          Public Canon v48", "CANON:          Public Canon v49"),
    ("TAG:            canon-v48", "TAG:            canon-v49"),
    ("CONTENT_COMMIT: d1d0df6d08dcb6b610719bc17151aabb97cc9d96",
     f"CONTENT_COMMIT: {content_commit}"),
    ("CANON_SHA256:   65dfa8509abfdf44fdd1198c93d476d01f1c93ca3066c1f573aab6bbc70879bb",
     f"CANON_SHA256:   {canon_hash}"),
    ("CANON_BYTES:    234810", f"CANON_BYTES:    {len(canon_bytes)}"),
    ("Public Canon v48 is the normative public ledger of TWIST-J.",
     "Public Canon v49 is the normative public ledger of TWIST-J."),
    ("commit is published under the tag `canon-v48`; the same form on any other",
     "commit is published under the tag `canon-v49`; the same form on any other"),
])
rw(ROOT / "README.md", [
    ("**State: ACTIVE. Public Canon v48 is the normative public ledger.**",
     "**State: ACTIVE. Public Canon v49 is the normative public ledger.**"),
    ("the public `main` branch at the tag `canon-v48`; see [STATUS.md](STATUS.md) and",
     "the public `main` branch at the tag `canon-v49`; see [STATUS.md](STATUS.md) and"),
    ("- [Canon](canon/CANON.md): the normative Public Canon v48 text.",
     "- [Canon](canon/CANON.md): the normative Public Canon v49 text."),
    ("The current release is Public Canon v48, tagged `canon-v48`.",
     "The current release is Public Canon v49, tagged `canon-v49`."),
])
rw(ROOT / "CITATION.cff", [
    ('message: "If you use TWIST-J Public Canon v48, cite it as below."',
     'message: "If you use TWIST-J Public Canon v49, cite it as below."'),
    ('version: "48"', 'version: "49"'),
    ("date-released: 2026-08-15", "date-released: 2026-08-16"),
])

decisive([sys.executable, "tools/check_canon.py"], "check_canon")
commit_named(stage_allow, "Stage Public Canon v49 activation", exact=True)

if run("git", "rev-list", "--count", f"{BASE}..HEAD").stdout.strip() != "2":
    raise SystemExit("release branch does not carry exactly two commits")
if set(run("git", "diff", "--name-only", f"{content_commit}..HEAD").stdout.splitlines()) != set(stage_allow):
    raise SystemExit("release-form commit changed paths differ from exact three-file set")

activation = run(sys.executable, "tools/check_activation.py", "--full", check=False)
print("\n".join((activation.stdout + activation.stderr).strip().splitlines()[-10:]))
if activation.returncode:
    raise SystemExit("check_activation --full failed; DO NOT PUSH")
print("finalize complete: exactly two frozen commits; activation check PASS")
