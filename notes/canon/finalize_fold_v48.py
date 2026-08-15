#!/usr/bin/env python3
"""
finalize_fold_v48.py  --  QDD Route A insertion package, fold finalization.

Run AFTER notes/canon/apply_qdd_insertion_delta.py on a clean checkout of
canon-v47 (a235978) placed on the branch release/canon-v48.  It

  1. updates tools/test_architecture_map_report.py to the folded-tree counts,
  2. updates reproduce/status-separation/README.md (thirty-three checks, v48 sentence),
  3. writes the Public Canon v48 CHANGELOG entry (generated counts block moves to the top),
  4. regenerates canon/SHA256SUMS,
  5. commits "Fold QDD Route A dictionary into Canon v48",
  6. stages the activation form (STATUS.md, README.md, CITATION.cff) and commits
     "Stage Public Canon v48 activation",
  7. runs check_policy, unittest, check_canon, check_ledger and check_activation --full.

It never tags and never pushes.  Usage: python3 notes/canon/finalize_fold_v48.py <tree root>
"""
import hashlib, re, subprocess, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
canon = ROOT / "canon"
def run(*args, check=True):
    r = subprocess.run(list(args), cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        print(r.stdout[-2000:]); print(r.stderr[-2000:]); raise SystemExit(f"command failed: {' '.join(args)}")
    return r
def rw(path, subs):
    t = path.read_text(encoding="utf-8")
    for old, new in subs:
        assert t.count(old) == 1, (path.name, t.count(old), old[:60])
        t = t.replace(old, new)
    path.write_text(t, encoding="utf-8")

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

# ------------------------------------------------------------------ 2. status-separation README
rw(ROOT / "reproduce" / "status-separation" / "README.md", [
    ("Its thirty-two checks cover the current", "Its thirty-three checks cover the current"),
    ("The v47 count and TM-SYM2 checks additionally require",
     "The v48 count check reads the folded tree (246 claims, 23 reproductions, 11 gates), the "
     "CENTRAL, CM-2I and J-SEAM checks read QUADRATIC-DECODER-DATA as a dictionary with the "
     "instrument apparatus as the open DECODER_CORE row, and the new QDD-ROUTE-A check requires "
     "the three L1 theorems, the L6 Born reading behind its DICTIONARY_LIFT gate, the separate "
     "apparatus obligation, the two-architecture qdd-route-a evidence and the exact scope phrases "
     "of the slot boundary and of the measure.\n\nThe v47 count and TM-SYM2 checks additionally require"),
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
Public Canon v48 folds the QDD Route A dictionary. `QUADRATIC-DECODER-DATA`
moves from O to D. Three L1 theorems, one L6 dictionary and one open
apparatus obligation are declared; no other status changes.

The fourteen data the open row required are now public definitions in
section 2 (`DEF-QDD-*`): the pointed-orbit domain, the balanced piston head,
the B0 amplitude, the coefficient field with three distinct typed involutions,
the trace pairing and its Gram `G = I - (1/5) 1 1^T`, dagger, transpose, the
ordered quadratic pair and its carrier equality, the LOW LINE `Q lambda_B`
with `lambda_B = -zeta_5^4`, the two projectors as ALGEBRAIC_READOUT, the
branch-weight pairing, the five-field tagged record, the direct write and the
factor map, plus the explicit bridge `DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION`.

`QDD-ALGEBRAIC-FACTORIZATION [T]` states the exact identity of the direct
cyclotomic write and the Gram/projector factor route on all 15625
checkpoints, with totality, normalization, the 313 fibres and two negative
controls. `QDD-PROJECTOR-PAIR-TR4 [T]` states that `E_low` is the unique
G-self-adjoint idempotent with kernel `ker Tr_4`. `QDD-QCARRIER-DIAGONAL-
BOUNDARY [T]` records that both typed slots coincide on the frozen carrier
and that no central phase is derived from it. `QDD-BORN-READOUT-MEASURE [D]`
reads only the normalized NONZERO branch as a two-outcome measure through the
new direct gate `GATE-L1-L6-QDD-BORN-READOUT`; the ZERO branch stays a tag.
The value 1/6 in the value table is a numerical witness with no role. The
physical instrument family is `QDD-INSTRUMENT-APPARATUS [O]`, registered
separately so that the dictionary carries no unregistered blocker.

Evidence is the new two-architecture reproduction `reproduce/qdd-route-a`
(fifteen checks). The status-separation witness gains a thirty-third check.
No uniqueness-from-J, apparatus, occurrence law, sampling, post-state, SI,
totality or completeness claim is made.


"""
t = t.replace("# Canon changelog (public series)\n\n\n", "# Canon changelog (public series)\n\n\n" + entry, 1)
cl.write_text(t, encoding="utf-8")

# ------------------------------------------------------------------ 3b. version bump in CANON.md and regenerated views
rw(canon / "CANON.md", [
    ("# TWIST-J Public Canon v47\n", "# TWIST-J Public Canon v48\n"),
    ("**Release identity.** Public Canon v47. Normative authority and activation", "**Release identity.** Public Canon v48. Normative authority and activation"),
    ("algebraic axiom is J. Public Canon v47 also declares the discrete", "algebraic axiom is J. Public Canon v48 also declares the discrete"),
    ("seed of the two algebraic projections. Public Canon v47 does not claim", "seed of the two algebraic projections. Public Canon v48 does not claim"),
    ("deriving the architecture from J; Public Canon v47 contains no such", "deriving the architecture from J; Public Canon v48 contains no such"),
])
run(sys.executable, "tools/generate_canon_views.py", "--apply")

# ------------------------------------------------------------------ 4. SHA256SUMS
def sha256_file(p): return hashlib.sha256(p.read_bytes()).hexdigest()
(canon / "SHA256SUMS").write_text("".join(f"{sha256_file(canon / n)}  canon/{n}\n" for n in ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")), encoding="utf-8")

# ------------------------------------------------------------------ 5. fold commit
run("git", "add", "-A")
run("git", "commit", "-q", "-m", "Fold QDD Route A dictionary into Canon v48")
content_commit = run("git", "rev-parse", "HEAD").stdout.strip()
canon_bytes = (canon / "CANON.md").read_bytes()
canon_sha = hashlib.sha256(canon_bytes).hexdigest()
print("content commit", content_commit, "canon sha", canon_sha, "bytes", len(canon_bytes))

# ------------------------------------------------------------------ 6. staging commit
st = ROOT / "STATUS.md"
rw(st, [
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
run("git", "add", "-A")
run("git", "commit", "-q", "-m", "Stage Public Canon v48 activation")
print("staging commit", run("git", "rev-parse", "HEAD").stdout.strip())

# ------------------------------------------------------------------ 7. checks
for tool in ("check_policy.py", "check_canon.py", "check_ledger.py", "check_status_labels.py"):
    r = run(sys.executable, f"tools/{tool}", check=False)
    print(f"[{tool}] " + ((r.stdout + r.stderr).strip().splitlines() or ["(no output)"])[-1])
r = run(sys.executable, "-m", "unittest", "discover", "-s", "tools", "-p", "test_*.py", check=False)
print("[unittest] " + (r.stderr.strip().splitlines() or ["(no output)"])[-1])
r = run(sys.executable, "tools/check_activation.py", "--full", check=False)
lines = (r.stdout + r.stderr).strip().splitlines()
print("[check_activation --full] exit", r.returncode); print("\n".join(lines[-8:]))
