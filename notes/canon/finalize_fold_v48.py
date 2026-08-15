#!/usr/bin/env python3
"""
finalize_fold_v48.py  --  conservative QDD Route A fold finalization.

Run AFTER notes/canon/apply_qdd_insertion_delta.py on a clean checkout of
canon-v47 main placed on the branch release/canon-v48.  It

  1. updates tools/test_architecture_map_report.py to the folded-tree counts,
  2. updates reproduce/status-separation/README.md (thirty-three checks,
     conservative v48 sentence),
  3. writes the Public Canon v48 CHANGELOG entry (the generated counts block
     moves to the top and is refreshed by the view generator),
  4. bumps the Canon version, regenerates views and canon/SHA256SUMS,
  5. runs the decisive fast checks (policy, unittest, ledger, labels)
     fail-closed BEFORE any commit; check_canon runs fail-closed after the
     staging edits (it requires the v48 STATUS.md) and before the staging
     commit,
  6. commits "Fold QDD Route A dictionary into Canon v48" from an explicit
     path allowlist (git add -A is not used anywhere),
  7. edits exactly STATUS.md, README.md, CITATION.cff and commits
     "Stage Public Canon v48 activation" (the changed set must equal exactly
     those three paths),
  8. runs check_activation --full fail-closed; on failure it aborts with
     DO NOT PUSH.

Every decisive check aborts the script with a nonzero exit on failure.
It never tags and never pushes.  Usage:
python3 notes/canon/finalize_fold_v48.py <tree root>
"""
import hashlib, re, subprocess, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
canon = ROOT / "canon"

def run(*args, check=True):
    r = subprocess.run(list(args), cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        print(r.stdout[-2000:]); print(r.stderr[-2000:])
        raise SystemExit(f"command failed: {' '.join(args)}")
    return r

def decisive(argv, label):
    r = run(*argv, check=False)
    out = (r.stdout + r.stderr).strip()
    print(f"[{label}] " + ((out.splitlines() or ["(no output)"]))[-1])
    if r.returncode != 0:
        print(out[-2000:])
        raise SystemExit(f"decisive check failed: {label}; DO NOT COMMIT OR PUSH")
    return out

def rw(path, subs):
    t = path.read_text(encoding="utf-8")
    for old, new in subs:
        assert t.count(old) == 1, (path.name, t.count(old), old[:60])
        t = t.replace(old, new)
    path.write_text(t, encoding="utf-8")

def changed_paths():
    out = run("git", "status", "--porcelain").stdout
    paths = set()
    for line in out.splitlines():
        if not line.strip():
            continue
        if "->" in line:
            raise SystemExit("unexpected rename in the working tree: " + line)
        paths.add(line[3:].strip())
    return paths

def staged_commit(allow, message, require_exact=False):
    ch = changed_paths()
    extra = sorted(ch - set(allow))
    if extra:
        raise SystemExit(f"refusing to commit {message!r}: unexpected modified paths {extra}")
    if require_exact and ch != set(allow):
        raise SystemExit(f"refusing to commit {message!r}: expected exactly {sorted(allow)}, found {sorted(ch)}")
    to_add = sorted(ch)
    if not to_add:
        raise SystemExit(f"nothing to commit for {message!r}")
    run("git", "add", "--", *to_add)
    run("git", "commit", "-q", "-m", message)
    if run("git", "status", "--porcelain").stdout.strip():
        raise SystemExit(f"tree not clean after commit {message!r}")

FOLD_ALLOW = [
    "canon/CANON.md", "canon/CORE.md", "canon/FRONTIER.md", "canon/CHANGELOG.md",
    "canon/REGISTRY.tsv", "canon/NORMATIVE.tsv", "canon/DEPENDENCIES.tsv",
    "canon/EVIDENCE.tsv", "canon/HISTORY.tsv", "canon/FRONTIER_PROGRAMS.tsv",
    "canon/SHA256SUMS", "canon/STATUS_COUNTS.tsv",
    "reproduce/status-separation/verify.py",
    "reproduce/status-separation/EXPECTED.txt",
    "reproduce/status-separation/README.md",
    "tools/test_architecture_map_report.py",
]
STAGE_ALLOW = ["STATUS.md", "README.md", "CITATION.cff"]

# ------------------------------------------------------------------ 1. test fixture (architecture map report)
sys.path.insert(0, str(ROOT / "tools"))
import architecture_map_report as architecture   # noqa: E402
rep = architecture.audit(ROOT)
sc = rep.status_counts; ec = rep.evidence_counts
rw(ROOT / "tools" / "test_architecture_map_report.py", [
    ("self.assertEqual(self.report.claims, 241)", f"self.assertEqual(self.report.claims, {rep.claims})"),
    ('{"C": 27, "D": 42, "F": 13, "H": 2, "O": 22, "T": 135}',
     '{"C": %d, "D": %d, "F": %d, "H": %d, "O": %d, "T": %d}' % (sc["C"], sc["D"], sc["F"], sc["H"], sc["O"], sc["T"])),
    ('                "none": 40,\n                "one-architecture": 9,\n                "recorded-audit": 31,\n                "two-architecture": 161,',
     '                "none": %d,\n                "one-architecture": %d,\n                "recorded-audit": %d,\n                "two-architecture": %d,'
     % (ec["none"], ec["one-architecture"], ec["recorded-audit"], ec["two-architecture"])),
    ("self.assertEqual(len(self.report.direct_architecture_requires), 175)",
     f"self.assertEqual(len(self.report.direct_architecture_requires), {len(rep.direct_architecture_requires)})"),
    ("len(self.report.transitive_architecture_dependents), 195",
     f"len(self.report.transitive_architecture_dependents), {len(rep.transitive_architecture_dependents)}"),
    ("self.assertEqual(len(self.report.dependency_terminals), 22)",
     f"self.assertEqual(len(self.report.dependency_terminals), {len(rep.dependency_terminals)})"),
])

# ------------------------------------------------------------------ 2. status-separation README (conservative fold, dynamic counts)
n_gates = max(0, len((canon / "GATES.tsv").read_text(encoding="utf-8").rstrip("\n").splitlines()) - 1)
n_repro = sum(p.is_dir() for p in (ROOT / "reproduce").iterdir())
v48_sentence = (
    f"The v48 count check reads the folded tree ({rep.claims} claims, {n_repro} "
    f"reproductions, {n_gates} gates). The CENTRAL, CM-2I and J-SEAM checks are "
    "unchanged and keep reading QUADRATIC-DECODER-DATA as an open obligation. The "
    "new QDD-ROUTE-A check requires the three L1 theorems on two-architecture "
    "qdd-route-a evidence, the separate apparatus obligation at "
    "DECODER_CORE/FOLLOWUP/STOP, QUADRATIC-DECODER-DATA still O with its "
    "ROOT/STOP program row, the absence of any Born-readout row, effect-selection "
    "bridge or L1-L6 gate, and the exact scope phrases of the factorization, the "
    "projector pair and the slot boundary."
)
rw(ROOT / "reproduce" / "status-separation" / "README.md", [
    ("Its thirty-two checks cover the current", "Its thirty-three checks cover the current"),
    ("The v47 count and TM-SYM2 checks additionally require",
     v48_sentence + "\n\nThe v47 count and TM-SYM2 checks additionally require"),
])

# ------------------------------------------------------------------ 3. CHANGELOG entry
cl = canon / "CHANGELOG.md"
t = cl.read_text(encoding="utf-8")
m = re.search(r"## Public Canon v47\n\n(<!-- BEGIN GENERATED CURRENT COUNTS -->\n.*?<!-- END GENERATED CURRENT COUNTS -->\n)\n", t, re.S)
assert m, "v47 counts block not found"
counts_block = m.group(1)
t = t.replace(m.group(0), "## Public Canon v47\n\n", 1)
entry = f"""## Public Canon v48

{counts_block}
Public Canon v48 registers the QDD Route A algebra: three L1 theorems and
one separate obligation. `QUADRATIC-DECODER-DATA` is not modified and remains
an open obligation; no gate is added and no L6 reading is claimed.

The seventeen public definitions `DEF-QDD-*` in section 2 state the
pointed-orbit domain, the balanced piston head, the B0 amplitude, the
coefficient field with three distinct typed involutions, the trace pairing
and its Gram `G = I - (1/5) 1 1^T`, dagger, transpose, the ordered quadratic
pair and its carrier equality, the LOW LINE `Q lambda_B` with
`lambda_B = -zeta_5^4`, the frozen effect pair of the EFFECT_SHADOW_MINIMAL
owner freeze as ALGEBRAIC_READOUT projectors, the owner-frozen Born
trace pairing as a dictionary input, the five-field tagged record with the
explicit ZERO branch, the direct write under the independence firewall, and
the factor map.

`QDD-ALGEBRAIC-FACTORIZATION [T]` states the exact identity of the direct
cyclotomic write and the Gram/projector factor route on all 15625
checkpoints, with totality, exact normalization, the 313 fibres, injectivity
and two negative controls. `QDD-PROJECTOR-PAIR-TR4 [T]` states that `E_low`
is the unique G-self-adjoint idempotent with kernel `ker Tr_4`, with the
closed forms; it identifies the pair inside its algebraic class and does not
force the choice of that class. `QDD-QCARRIER-DIAGONAL-BOUNDARY [T]` records
that both typed slots coincide on the frozen carrier and that no central
phase is derived from it. `QDD-INSTRUMENT-APPARATUS [O]` is the physical
instrument family, registered separately and filling no completion-contract
field.

Per the owner rulings of 2026-07-30 and the EFFECT_SHADOW_MINIMAL freeze, the
`effects` requirement of the decoder completion contract stays UNRESOLVED and
the contract is not submitted. The value 1/6 in the normalized value table is
a numerical witness with no role. Evidence is the new two-architecture
reproduction `reproduce/qdd-route-a` (fifteen checks). The status-separation
witness gains a thirty-third check. No uniqueness-from-J, apparatus,
occurrence law, sampling, post-state, SI, totality or completeness claim is
made.


"""
t = t.replace("# Canon changelog (public series)\n\n\n", "# Canon changelog (public series)\n\n\n" + entry, 1)
cl.write_text(t, encoding="utf-8")

# ------------------------------------------------------------------ 4. version bump, regenerated views, SHA256SUMS
rw(canon / "CANON.md", [
    ("# TWIST-J Public Canon v47\n", "# TWIST-J Public Canon v48\n"),
    ("**Release identity.** Public Canon v47. Normative authority and activation", "**Release identity.** Public Canon v48. Normative authority and activation"),
    ("algebraic axiom is J. Public Canon v47 also declares the discrete", "algebraic axiom is J. Public Canon v48 also declares the discrete"),
    ("seed of the two algebraic projections. Public Canon v47 does not claim", "seed of the two algebraic projections. Public Canon v48 does not claim"),
    ("deriving the architecture from J; Public Canon v47 contains no such", "deriving the architecture from J; Public Canon v48 contains no such"),
])
run(sys.executable, "tools/generate_canon_views.py", "--apply")

t = cl.read_text(encoding="utf-8")
i48 = t.index("## Public Canon v48"); i47 = t.index("## Public Canon v47")
assert i48 < i47 and f"Registry snapshot: {rep.claims} claims" in t[i48:i47], \
    "v48 generated counts block does not show the folded claim count"

def sha256_file(p): return hashlib.sha256(p.read_bytes()).hexdigest()
(canon / "SHA256SUMS").write_text("".join(f"{sha256_file(canon / n)}  canon/{n}\n" for n in ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")), encoding="utf-8")

# ------------------------------------------------------------------ 5. decisive fast checks BEFORE any commit
decisive([sys.executable, "tools/check_policy.py"], "check_policy")
r = run(sys.executable, "-m", "unittest", "discover", "-s", "tools", "-p", "test_*.py", check=False)
print("[unittest] " + ((r.stderr.strip().splitlines() or ["(no output)"]))[-1])
if r.returncode != 0:
    print((r.stdout + r.stderr)[-2000:])
    raise SystemExit("decisive check failed: unittest; DO NOT COMMIT OR PUSH")
# check_canon requires the v48 STATUS.md and therefore runs after the
# staging edits, before the staging commit
decisive([sys.executable, "tools/check_ledger.py"], "check_ledger")
decisive([sys.executable, "tools/check_status_labels.py"], "check_status_labels")

# ------------------------------------------------------------------ 6. fold commit (explicit paths only)
staged_commit(FOLD_ALLOW, "Fold QDD Route A dictionary into Canon v48")
content_commit = run("git", "rev-parse", "HEAD").stdout.strip()
canon_bytes = (canon / "CANON.md").read_bytes()
canon_sha = hashlib.sha256(canon_bytes).hexdigest()
print("content commit", content_commit, "canon sha", canon_sha, "bytes", len(canon_bytes))

# ------------------------------------------------------------------ 7. staging commit (exactly three files)
rw(ROOT / "STATUS.md", [
    ("CANON:          Public Canon v47", "CANON:          Public Canon v48"),
    ("TAG:            canon-v47", "TAG:            canon-v48"),
    ("CONTENT_COMMIT: 95219e2ba51bdedce76b2040bb0cfcb97937edfa", f"CONTENT_COMMIT: {content_commit}"),
    ("CANON_SHA256:   5e4c454e53381e13df2bc2e894bd6e7328af9329c4b13df03106c902c7caf400", f"CANON_SHA256:   {canon_sha}"),
    ("CANON_BYTES:    225589", f"CANON_BYTES:    {len(canon_bytes)}"),
    ("Public Canon v47 is the normative public ledger of TWIST-J.", "Public Canon v48 is the normative public ledger of TWIST-J."),
    ("commit is published under the tag `canon-v47`; the same form on any other", "commit is published under the tag `canon-v48`; the same form on any other"),
])
rw(ROOT / "README.md", [
    ("**State: ACTIVE. Public Canon v47 is the normative public ledger.**", "**State: ACTIVE. Public Canon v48 is the normative public ledger.**"),
    ("the public `main` branch at the tag `canon-v47`; see [STATUS.md](STATUS.md) and", "the public `main` branch at the tag `canon-v48`; see [STATUS.md](STATUS.md) and"),
    ("- [Canon](canon/CANON.md): the normative Public Canon v47 text.", "- [Canon](canon/CANON.md): the normative Public Canon v48 text."),
    ("The current release is Public Canon v47, tagged `canon-v47`.", "The current release is Public Canon v48, tagged `canon-v48`."),
])
rw(ROOT / "CITATION.cff", [
    ('message: "If you use TWIST-J Public Canon v47, cite it as below."', 'message: "If you use TWIST-J Public Canon v48, cite it as below."'),
    ('version: "47"', 'version: "48"'),
    ("date-released: 2026-08-14", "date-released: 2026-08-15"),
])
decisive([sys.executable, "tools/check_canon.py"], "check_canon")
staged_commit(STAGE_ALLOW, "Stage Public Canon v48 activation", require_exact=True)
print("staging commit", run("git", "rev-parse", "HEAD").stdout.strip())

# ------------------------------------------------------------------ 8. decisive activation check
r = run(sys.executable, "tools/check_activation.py", "--full", check=False)
lines = (r.stdout + r.stderr).strip().splitlines()
print("\n".join(lines[-8:]))
if r.returncode != 0:
    raise SystemExit("check_activation --full FAILED on the staged release branch; DO NOT PUSH")
print("finalize complete: release branch carries exactly the two frozen commits and passed check_activation --full")
