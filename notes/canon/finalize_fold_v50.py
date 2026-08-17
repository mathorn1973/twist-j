#!/usr/bin/env python3
"""
Finalize the Public Canon v50 Suzuki local capacity no-go fold.

Run on release/canon-v50 at the exact public v49 main
4e050f167f83e78d2c5b4a5c244fd6c8eead694b (after the merged public probe
P-SUZUKI-LOCAL-CAPACITY-NOGO-1). The script:
  1. folds SUZUKI-LOCAL-CAPACITY-NOGO [T] at L1 plus the two finite
     computations SUZUKI-PRIME-FREE-WINDOW [C] and SUZUKI-EVENT-COUNT [C];
  2. updates the Canon ledgers, generated views, status-separation audit and hashes;
  3. runs decisive repository checks;
  4. creates exactly one content commit and one release-form commit;
  5. runs check_activation --full and never pushes, merges, tags or releases.

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
BASE = "4e050f167f83e78d2c5b4a5c244fd6c8eead694b"
PROBE = "probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1"
PROBE_DIGEST = "0891418a788e7e2d1d4795af8883020dbcd78c7ea2f9f9fefb41b055131deb65"
FINALIZER = "notes/canon/finalize_fold_v50.py"


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


def rw_re(path: Path, substitutions: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    for pattern, repl in substitutions:
        text, count = re.subn(pattern, repl, text)
        if count != 1:
            raise SystemExit(f"{path}: expected one regex match, found {count}: {pattern!r}")
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


def place_rows(path: Path, anchor_id: str, new_rows: list[str]) -> None:
    values = lines(path)
    positions = [i for i, row in enumerate(values) if row.startswith(anchor_id + "\t")]
    if len(positions) == 1:
        insert_before_row(path, anchor_id, new_rows)
    else:
        print(f"note: {path.name} lacks unique anchor {anchor_id}; appending")
        append_rows(path, new_rows)


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
if branch != "release/canon-v50" or head != BASE:
    raise SystemExit(f"wrong release base: branch={branch} head={head}")
if changed_paths() != {FINALIZER}:
    raise SystemExit(f"initial tree must differ only by {FINALIZER}: {sorted(changed_paths())}")
if bundle_sha256(ROOT / PROBE) != PROBE_DIGEST:
    raise SystemExit("public probe bundle hash mismatch; STOP")

theorem_scope = (
    "at L1 over the classical Riemann zeta function, with "
    "P(t) = sum_(p^k <= e^t) (log p) p^(-k/2) (t - k log p), "
    "S(z) = sum_(k >= 0) z^k/(4k+1)^2, "
    "A(t) = 8(cosh(t/2) - 1) - alpha t + C - 4 e^(-t/2) S(e^(-2t)), "
    "alpha = (log pi - psi(1/4))/2, C = psi'(1/4)/4, Psi = A - P and "
    "K_F(s,t) = F(s) + F(t) - F(|s-t|): every locally finite event family "
    "gives a direct-sum curve with norm-square F, inner product F(min) and "
    "orthogonal increments, specializing to P; the reproduced curvature "
    "A''(t) = e^(t/2) + e^(-t/2) - e^(-t/2)/(1 - e^(-2t)) changes sign once "
    "at log rho, rho^3 = rho + 1; a certified three-point convexity "
    "violation at (1/20, 1/4, 1/2) proves the nonnegative ramp class is "
    "empty; A(1/4) > A(1/2) kills every filtration model and the single "
    "exact prime ramp on [log 2, 4/5] kills increment domination and every "
    "nonnegative per-place budget at the first event q = 2; both screw "
    "kernels K_A and K_P are separately indefinite at the certified pair "
    "(3, 6); any contraction T with T Z_t = Y_t and ||T|| <= 1 - delta "
    "forces Psi >= delta(2 - delta) A against the prime number theorem "
    "bound, so the norm is exactly one; hence every Gram realization of "
    "the capacity dominating the prime curve is nonlocal in t; written "
    "proofs with twelve certified exact gates, prime-event counting as "
    "motivation only, no Riemann hypothesis or zero statement, "
    "no J-coupling, no L2--L6 lift"
)
theorem_falsifier = (
    "fires on any exact instance violating the orthogonal-increment "
    "identities, on a certified opposite sign in any pinned curvature, "
    "convexity, monotonicity, domination or kernel gate, or on a proof of "
    "a uniform strict contraction, which would refute the prime number "
    "theorem import; a non-separating enclosure at the frozen precision is "
    "UNDECIDED and fires nothing; the pinned verifier failing on re-run or "
    "the two architecture transcripts differing is an integrity stop"
)
window_scope = (
    "certified finite range: A(t) > 0 for every t in [1/128, 45/64], where "
    "Psi = A on (0, log 2), by a 100-leaf adaptive outward-interval cover "
    "at scale 2^-192 with zero undecided leaves; an independent code path "
    "reproducing one corner of the certified event-segment strip of the "
    "cited record; the interval (0, 1/128) carries no gate"
)
window_falsifier = (
    "fires on a certified negative leaf, which is first an integrity stop "
    "pending independent audit since it would contradict the cited strip "
    "record and, through the screw criterion, the Riemann hypothesis; "
    "fires if the pinned verifier fails on re-run or the aarch64 and "
    "x86_64 transcripts differ; status remains C absent protocol "
    "independence"
)
count_scope = (
    "N(10^6) = 78734 prime-power events p^k <= 10^6 by direct enumeration "
    "and by sum_k pi(floor(10^(6/k))), exact integer equality of two "
    "independent counting paths"
)
count_falsifier = (
    "fires if the two exact counting paths disagree; fires if the pinned "
    "verifier fails on re-run or the aarch64 and x86_64 transcripts "
    "differ; status remains C absent an independent implementation"
)

SECTION = "10. Relativity as counting"
registry = CANON / "REGISTRY.tsv"
place_rows(registry, "QDD-ALGEBRAIC-FACTORIZATION", [
    "\t".join(("SUZUKI-LOCAL-CAPACITY-NOGO", "T", theorem_scope, SECTION, PROBE, theorem_falsifier)),
    "\t".join(("SUZUKI-PRIME-FREE-WINDOW", "C", window_scope, SECTION, PROBE, window_falsifier)),
    "\t".join(("SUZUKI-EVENT-COUNT", "C", count_scope, SECTION, PROBE, count_falsifier)),
])

canon_path = CANON / "CANON.md"
section_tail = (
    "measure, physical or SI reading, or L2--L6 lift.\n"
    "\n"
    "## 11. The pentit ring and the magic boundary\n"
)
suzuki_block = (
    "measure, physical or SI reading, or L2--L6 lift.\n"
    "\n"
    "### SUZUKI-LOCAL-CAPACITY-NOGO [T]\n"
    "\n"
    "One classical no-go complex on the screw function of the Riemann zeta\n"
    "function, in Suzuki's normalization. Freeze\n"
    "\n"
    "```text\n"
    "P(t) = sum_(p^k <= e^t) (log p) p^(-k/2) (t - k log p)          t >= 0\n"
    "S(z) = sum_(k >= 0) z^k / (4k+1)^2                              0 < z < 1\n"
    "A(t) = 8 (cosh(t/2) - 1) - alpha t + C - 4 e^(-t/2) S(e^(-2t))  t > 0\n"
    "alpha = (log pi - psi(1/4)) / 2,     C = psi'(1/4) / 4\n"
    "Psi = A - P,     K_F(s,t) = F(s) + F(t) - F(|s-t|).\n"
    "```\n"
    "\n"
    "The positivity criterion for Psi and the screw kernel K_A - K_P are\n"
    "Suzuki's; the curvature closed form and the plastic transition below are\n"
    "Mittermeier's, reproduced here by an independent implementation with no\n"
    "novelty claimed. Six statements, written proofs pinned in the public\n"
    "probe, finite gates certified by outward interval arithmetic at scale\n"
    "`2^-192`:\n"
    "\n"
    "```text\n"
    "N1  for every locally finite event family {(tau_q, omega_q)} the\n"
    "    direct-sum curve Y_t = (+)_q omega_q 1_[tau_q,t] has\n"
    "    ||Y_t||^2 = F(t), <Y_s,Y_t> = F(min(s,t)), orthogonal increments\n"
    "    and ||Y_t - Y_u||^2 = F(t) - F(u); prime powers give P\n"
    "R2  A''(t) = e^(t/2) + e^(-t/2) - e^(-t/2)/(1 - e^(-2t)); the sign\n"
    "    changes once, at log rho with rho^3 = rho + 1, rho in (13/10, 4/3)\n"
    "N3  no c0, c1 and locally finite Borel measure mu >= 0 give\n"
    "    A = c0 + c1 t + integral (t-a)_+ dmu on (0, inf): a certified\n"
    "    three-point convexity violation at (1/20, 1/4, 1/2) empties the\n"
    "    nonnegative ramp class\n"
    "N4  A(1/4) > A(1/2), so dA is not a nonnegative measure and no\n"
    "    filtration model exists on (0, log 2); on [log 2, 4/5] the single\n"
    "    exact prime ramp exceeds the capacity increment, so increment\n"
    "    domination dP <= dA and every nonnegative per-place budget die at\n"
    "    the first event q = 2\n"
    "N5  4A(3) - A(6) < 0 < A(6) and 4P(3) - P(6) < 0 < P(6), with e^3 in\n"
    "    (20, 23) and e^6 in (401, 409): both screw kernels are separately\n"
    "    indefinite; only the difference can be a screw geometry\n"
    "N8  T Z_t = Y_t with ||Z_t||^2 = A, ||Y_t||^2 = P and\n"
    "    ||T|| <= 1 - delta forces Psi >= delta (2 - delta) A against\n"
    "    Psi = o(e^(t/2)) from the prime number theorem, so ||T|| = 1\n"
    "```\n"
    "\n"
    "Together: the completion capacity is not a positive superposition of\n"
    "prime-type ramp atoms, admits no filtration or per-place domination\n"
    "reading, and is not itself a screw geometry; every Gram realization\n"
    "dominating the prime curve has operator norm exactly one and is\n"
    "nonlocal in `t`. The prime-event counting frame is motivation only. No\n"
    "statement about the Riemann hypothesis or its zeros, no least-gap or\n"
    "prime-distribution result, no decoder, measure, physical or SI\n"
    "reading, no J-coupling, and no L2--L6 lift.\n"
    "\n"
    "### SUZUKI-PRIME-FREE-WINDOW [C]\n"
    "\n"
    "`A(t) > 0` for every `t` in `[1/128, 45/64]`, where `Psi = A` on\n"
    "`(0, log 2)`: a 100-leaf adaptive outward-interval cover with zero\n"
    "undecided leaves, an independent code path reproducing one corner of\n"
    "Mittermeier's certified event-segment strip; the interval\n"
    "`(0, 1/128)` carries no gate.\n"
    "\n"
    "### SUZUKI-EVENT-COUNT [C]\n"
    "\n"
    "`N(10^6) = 78734` prime-power events `p^k <= 10^6`, by direct\n"
    "enumeration and by `sum_k pi(floor(10^(6/k)))`, exact integer equality\n"
    "of two independent counting paths.\n"
    "\n"
    "At L1, `P-SUZUKI-LOCAL-CAPACITY-NOGO-1` supplies the written proofs,\n"
    "the byte-identical two-architecture audit, twelve certified gates and\n"
    "the two finite computations above, with frozen attribution to Suzuki\n"
    "and to Mittermeier in its preregistration. It makes no statement about\n"
    "the Riemann hypothesis.\n"
    "\n"
    "## 11. The pentit ring and the magic boundary\n"
)
rw(canon_path, [(section_tail, suzuki_block)])

normative = CANON / "NORMATIVE.tsv"
place_rows(normative, "QDD-ALGEBRAIC-FACTORIZATION", [
    "\t".join(("SUZUKI-LOCAL-CAPACITY-NOGO", "THEOREM", "SUZUKI-LOCAL-CAPACITY-NOGO", "T", "L1", "", "canon/CANON.md::SUZUKI-LOCAL-CAPACITY-NOGO [T]")),
    "\t".join(("SUZUKI-PRIME-FREE-WINDOW", "COMPUTATION", "SUZUKI-PRIME-FREE-WINDOW", "C", "L1", "", "canon/CANON.md::SUZUKI-PRIME-FREE-WINDOW [C]")),
    "\t".join(("SUZUKI-EVENT-COUNT", "COMPUTATION", "SUZUKI-EVENT-COUNT", "C", "L1", "", "canon/CANON.md::SUZUKI-EVENT-COUNT [C]")),
])

evidence = CANON / "EVIDENCE.tsv"
place_rows(evidence, "QDD-ALGEBRAIC-FACTORIZATION", [
    "\t".join(("SUZUKI-LOCAL-CAPACITY-NOGO", "EV-SUZUKI-LOCAL-CAPACITY-NOGO", "PUBLIC_PROBE", PROBE, PROBE_DIGEST, "bundle-manifest-sha256-v1", "two-architecture")),
    "\t".join(("SUZUKI-PRIME-FREE-WINDOW", "EV-SUZUKI-PRIME-FREE-WINDOW", "PUBLIC_PROBE", PROBE, PROBE_DIGEST, "bundle-manifest-sha256-v1", "two-architecture")),
    "\t".join(("SUZUKI-EVENT-COUNT", "EV-SUZUKI-EVENT-COUNT", "PUBLIC_PROBE", PROBE, PROBE_DIGEST, "bundle-manifest-sha256-v1", "two-architecture")),
])

history = CANON / "HISTORY.tsv"
append_rows(history, [
    "\t".join((
        "CANON50-DECLARE-SUZUKI-LOCAL-CAPACITY-NOGO", "1", "2026-08-17",
        "canon-v50-candidate", "SUZUKI-LOCAL-CAPACITY-NOGO", "DECLARE", "-", "T",
        scope_sha(theorem_scope), "EV-SUZUKI-LOCAL-CAPACITY-NOGO", PROBE, PROBE_DIGEST,
        "Public Canon v50 registers the L1 local no-go complex for the completion capacity of the Suzuki screw function from the merged two-architecture public probe: orthogonal-increment prime curve, reproduced curvature and plastic transition, empty nonnegative ramp class, filtration and per-place domination dead at the first event, both screw kernels separately indefinite, operator norm exactly one by the prime number theorem import, hence every dominating Gram realization is nonlocal in t; no Riemann hypothesis or zero statement and no J-coupling is added",
    )),
    "\t".join((
        "CANON50-DECLARE-SUZUKI-PRIME-FREE-WINDOW", "1", "2026-08-17",
        "canon-v50-candidate", "SUZUKI-PRIME-FREE-WINDOW", "DECLARE", "-", "C",
        scope_sha(window_scope), "EV-SUZUKI-PRIME-FREE-WINDOW", PROBE, PROBE_DIGEST,
        "Public Canon v50 registers the certified positivity of the capacity on [1/128, 45/64] by a 100-leaf adaptive outward-interval cover with zero undecided leaves, an independent code path reproducing one corner of the cited certified strip record",
    )),
    "\t".join((
        "CANON50-DECLARE-SUZUKI-EVENT-COUNT", "1", "2026-08-17",
        "canon-v50-candidate", "SUZUKI-EVENT-COUNT", "DECLARE", "-", "C",
        scope_sha(count_scope), "EV-SUZUKI-EVENT-COUNT", PROBE, PROBE_DIGEST,
        "Public Canon v50 registers the exact two-path equality N(10^6) = 78734 for prime-power events, direct enumeration against the prime-counting sum",
    )),
])

rw(canon_path, [
    ("# TWIST-J Public Canon v49\n", "# TWIST-J Public Canon v50\n"),
    ("**Release identity.** Public Canon v49. Normative authority and activation",
     "**Release identity.** Public Canon v50. Normative authority and activation"),
    ("algebraic axiom is J. Public Canon v49 also declares the discrete",
     "algebraic axiom is J. Public Canon v50 also declares the discrete"),
    ("seed of the two algebraic projections. Public Canon v49 does not claim",
     "seed of the two algebraic projections. Public Canon v50 does not claim"),
    ("deriving the architecture from J; Public Canon v49 contains no such",
     "deriving the architecture from J; Public Canon v50 contains no such"),
])

changelog = CANON / "CHANGELOG.md"
change_text = changelog.read_text(encoding="utf-8")
match = re.search(
    r"## Public Canon v49\n\n"
    r"(<!-- BEGIN GENERATED CURRENT COUNTS -->\n.*?"
    r"<!-- END GENERATED CURRENT COUNTS -->\n)\n",
    change_text,
    re.S,
)
if not match:
    raise SystemExit("v49 generated counts block not found")
counts_block = match.group(1)
change_text = change_text.replace(match.group(0), "## Public Canon v49\n\n", 1)
entry = f"""## Public Canon v50

{counts_block}
Public Canon v50 registers three rows from the completed public probe
`P-SUZUKI-LOCAL-CAPACITY-NOGO-1`, all at layer L1 over the classical
Riemann zeta function. `SUZUKI-LOCAL-CAPACITY-NOGO [T]` is the local no-go
complex for the completion capacity of the Suzuki screw function: the
prime side is a canonical orthogonal-increment path; the reproduced
curvature closed form changes sign once at the plastic constant; a
certified convexity violation empties the nonnegative ramp class;
filtration and per-place increment domination die at the first event
`q = 2`; both screw kernels are separately indefinite; and any
contraction realizing capacity over the prime curve is forced to operator
norm exactly one by the prime number theorem import, so every dominating
Gram realization is nonlocal in `t`.

`SUZUKI-PRIME-FREE-WINDOW [C]` certifies `A > 0` on `[1/128, 45/64]` by a
100-leaf adaptive outward-interval cover with zero undecided leaves, an
independent code path reproducing one corner of the cited certified strip
record. `SUZUKI-EVENT-COUNT [C]` fixes `N(10^6) = 78734` by two exact
counting paths.

The screw function, its positivity criterion and its kernel follow
Suzuki; the curvature closed form, the plastic transition and the strip
record follow Mittermeier; the reproductions claim no novelty, with
attribution frozen in the probe preregistration. The prime-event counting
frame stays motivation. No statement about the Riemann hypothesis or its
zeros, no J-coupling, no new H or O row, and no change to any existing
row is made.


"""
change_text = change_text.replace(
    "# Canon changelog (public series)\n\n\n",
    "# Canon changelog (public series)\n\n\n" + entry,
    1,
)
changelog.write_text(change_text, encoding="utf-8")

status_verify = ROOT / "reproduce" / "status-separation" / "verify.py"
rw(status_verify, [
    ('expected_counts = {"T": 139, "D": 42, "C": 27, "F": 13,\n'
     '                       "O": 23, "H": 2}',
     'expected_counts = {"T": 140, "D": 42, "C": 29, "F": 13,\n'
     '                       "O": 23, "H": 2}'),
    ('"registry and companion-ledger counts match Public Canon v49",',
     '"registry and companion-ledger counts match Public Canon v50",'),
    ("len(rows) == 246", "len(rows) == 249"),
    ("and len(normative) == 281", "and len(normative) == 284"),
    ("and len(evidence) == 246", "and len(evidence) == 249"),
    ("and two_architecture == 165", "and two_architecture == 168"),
    ("and len(history) == 762", "and len(history) == 765"),
])

check_anchor = """    fw_requires = {}
    for row in dependencies:
"""
new_check = """    suzuki = "SUZUKI-LOCAL-CAPACITY-NOGO"
    suzuki_path = "probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1"
    suzuki_digest = (
        "0891418a788e7e2d1d4795af8883020dbcd78c7ea2f9f9fefb41b055131deb65"
    )
    suzuki_window = "SUZUKI-PRIME-FREE-WINDOW"
    suzuki_count = "SUZUKI-EVENT-COUNT"
    suzuki_rows = (suzuki, suzuki_window, suzuki_count)
    suzuki_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] in suzuki_rows
    }
    checks.append((
        "SUZUKI-CAPACITY-NOGO",
        "the L1 no-go complex for the Suzuki completion capacity enters at T with two finite C computations, all pinned to the two-architecture public probe bundle and free of dependency, gate and frontier ownership",
        has_status(index, suzuki, "T")
        and has_status(index, suzuki_window, "C")
        and has_status(index, suzuki_count, "C")
        and normative.get(suzuki, {}).get("item_type") == "THEOREM"
        and normative.get(suzuki, {}).get("status") == "T"
        and normative.get(suzuki, {}).get("layer") == "L1"
        and normative.get(suzuki, {}).get("gate_ids") == ""
        and normative.get(suzuki_window, {}).get("item_type") == "COMPUTATION"
        and normative.get(suzuki_count, {}).get("item_type") == "COMPUTATION"
        and all(index.get(row, {}).get("evidence") == suzuki_path for row in suzuki_rows)
        and all(evidence.get(row, {}).get("evidence_kind") == "PUBLIC_PROBE" for row in suzuki_rows)
        and all(evidence.get(row, {}).get("location") == suzuki_path for row in suzuki_rows)
        and all(evidence.get(row, {}).get("sha256") == suzuki_digest for row in suzuki_rows)
        and all(
            evidence.get(row, {}).get("architecture_requirement") == "two-architecture"
            for row in suzuki_rows
        )
        and all(row not in programs for row in suzuki_rows)
        and all(row["owner_item_id"] not in suzuki_rows for row in gates.values())
        and suzuki_dependencies == set()
        and scope_contains_all(
            index, suzuki,
            ("orthogonal increments",
             "the nonnegative ramp class is empty",
             "at the first event q = 2",
             "separately indefinite",
             "the norm is exactly one",
             "nonlocal in t",
             "no J-coupling, no L2--L6 lift"),
        )
        and scope_contains_all(
            index, suzuki_window,
            ("[1/128, 45/64]", "zero undecided leaves"),
        )
        and scope_contains_all(
            index, suzuki_count,
            ("78734", "two independent counting paths"),
        ),
    ))

""" + check_anchor
rw(status_verify, [(check_anchor, new_check)])

status_readme = ROOT / "reproduce" / "status-separation" / "README.md"
v50_paragraph = (
    "The v50 count check reads the folded tree (249 claims, 23 reproductions, "
    "10 gates). The new SUZUKI-CAPACITY-NOGO check pins the L1 no-go theorem "
    "and its two finite computations to the completed two-architecture public "
    "probe bundle. It requires the empty nonnegative ramp class, first-event "
    "domination failure, separately indefinite kernels, the forced unit norm "
    "and the nonlocality consequence in the registered scopes, and requires "
    "absence of dependency, gate and frontier ownership.\n\n"
)
rw(status_readme, [
    ("Its thirty-five checks cover the current", "Its thirty-six checks cover the current"),
    ("Expected: byte-identical output to `EXPECTED.txt`, `RESULT 35/35 ALL PASS`,",
     "Expected: byte-identical output to `EXPECTED.txt`, `RESULT 36/36 ALL PASS`,"),
    ("The v49 count check reads the folded tree", v50_paragraph + "The v49 count check reads the folded tree"),
])

run(sys.executable, "tools/generate_canon_views.py", "--apply")

sys.path.insert(0, str(ROOT / "tools"))
import architecture_map_report as architecture  # noqa: E402

report = architecture.audit(ROOT)
sc = report.status_counts
ec = report.evidence_counts
rw_re(ROOT / "tools" / "test_architecture_map_report.py", [
    (r"self\.assertEqual\(self\.report\.claims, \d+\)",
     f"self.assertEqual(self.report.claims, {report.claims})"),
    (r'\{"C": \d+, "D": \d+, "F": \d+, "H": \d+, "O": \d+, "T": \d+\}',
     '{"C": %d, "D": %d, "F": %d, "H": %d, "O": %d, "T": %d}'
     % (sc["C"], sc["D"], sc["F"], sc["H"], sc["O"], sc["T"])),
    (r'"none": \d+,\n( *)"one-architecture": \d+,\n( *)"recorded-audit": \d+,\n( *)"two-architecture": \d+,',
     '"none": %d,\n\\1"one-architecture": %d,\n\\2"recorded-audit": %d,\n\\3"two-architecture": %d,'
     % (ec["none"], ec["one-architecture"], ec["recorded-audit"], ec["two-architecture"])),
    (r"self\.assertEqual\(len\(self\.report\.direct_architecture_requires\), \d+\)",
     f"self.assertEqual(len(self.report.direct_architecture_requires), {len(report.direct_architecture_requires)})"),
    (r"len\(self\.report\.transitive_architecture_dependents\), \d+",
     f"len(self.report.transitive_architecture_dependents), {len(report.transitive_architecture_dependents)}"),
    (r"self\.assertEqual\(len\(self\.report\.dependency_terminals\), \d+\)",
     f"self.assertEqual(len(self.report.dependency_terminals), {len(report.dependency_terminals)})"),
])

audit = run(sys.executable, "reproduce/status-separation/verify.py", check=False)
if audit.returncode or audit.stderr:
    print((audit.stdout + audit.stderr)[-3000:])
    raise SystemExit("status-separation audit failed or wrote stderr")
(ROOT / "reproduce" / "status-separation" / "EXPECTED.txt").write_text(
    audit.stdout, encoding="utf-8"
)
if "RESULT 36/36 ALL PASS\n" not in audit.stdout:
    raise SystemExit("status-separation did not produce 36/36")

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

commit_named(fold_allow, "Fold Suzuki local capacity no-go into Canon v50")
content_commit = run("git", "rev-parse", "HEAD").stdout.strip()
canon_bytes = canon_path.read_bytes()
canon_hash = sha256_bytes(canon_bytes)
print("content commit", content_commit)
print("canon sha", canon_hash)
print("canon bytes", len(canon_bytes))

rw(ROOT / "STATUS.md", [
    ("CANON:          Public Canon v49", "CANON:          Public Canon v50"),
    ("TAG:            canon-v49", "TAG:            canon-v50"),
    ("CONTENT_COMMIT: dc80228522a4ccb9495550dfbef8ba73b33b2157",
     f"CONTENT_COMMIT: {content_commit}"),
    ("CANON_SHA256:   d456c42575375774200b08dafc3b4225643f526f5f1826292f1255f39d332f9e",
     f"CANON_SHA256:   {canon_hash}"),
    ("CANON_BYTES:    237233", f"CANON_BYTES:    {len(canon_bytes)}"),
    ("Public Canon v49 is the normative public ledger of TWIST-J.",
     "Public Canon v50 is the normative public ledger of TWIST-J."),
    ("commit is published under the tag `canon-v49`; the same form on any other",
     "commit is published under the tag `canon-v50`; the same form on any other"),
])
rw(ROOT / "README.md", [
    ("**State: ACTIVE. Public Canon v49 is the normative public ledger.**",
     "**State: ACTIVE. Public Canon v50 is the normative public ledger.**"),
    ("the public `main` branch at the tag `canon-v49`; see [STATUS.md](STATUS.md) and",
     "the public `main` branch at the tag `canon-v50`; see [STATUS.md](STATUS.md) and"),
    ("- [Canon](canon/CANON.md): the normative Public Canon v49 text.",
     "- [Canon](canon/CANON.md): the normative Public Canon v50 text."),
    ("The current release is Public Canon v49, tagged `canon-v49`.",
     "The current release is Public Canon v50, tagged `canon-v50`."),
])
rw(ROOT / "CITATION.cff", [
    ('message: "If you use TWIST-J Public Canon v49, cite it as below."',
     'message: "If you use TWIST-J Public Canon v50, cite it as below."'),
    ('version: "49"', 'version: "50"'),
    ("date-released: 2026-08-16", "date-released: 2026-08-17"),
])

decisive([sys.executable, "tools/check_canon.py"], "check_canon")
commit_named(stage_allow, "Stage Public Canon v50 activation", exact=True)

if run("git", "rev-list", "--count", f"{BASE}..HEAD").stdout.strip() != "2":
    raise SystemExit("release branch does not carry exactly two commits")
if set(run("git", "diff", "--name-only", f"{content_commit}..HEAD").stdout.splitlines()) != set(stage_allow):
    raise SystemExit("release-form commit changed paths differ from exact three-file set")

activation = run(sys.executable, "tools/check_activation.py", "--full", check=False)
print("\n".join((activation.stdout + activation.stderr).strip().splitlines()[-10:]))
if activation.returncode:
    raise SystemExit("check_activation --full failed; DO NOT PUSH")
print("finalize complete: exactly two frozen commits; activation check PASS")
