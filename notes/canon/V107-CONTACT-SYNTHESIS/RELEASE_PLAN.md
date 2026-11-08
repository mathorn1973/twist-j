# v107 review handoff and release procedure

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

Status: NON-CANONICAL / L1 / release preparation. No activation, tag or release
is asserted by this document. Mathematical acceptance is pending the author's
separate review session. The present session's subagent reports are internal
working reviews, not that independent acceptance.

## Frozen sources

| Source | Exact reviewed input |
| --- | --- |
| Public main and v106 activation | `a193e389fb1ddb0bdc89165b015c95a17eb1e425` |
| v106 content | `9242db4f040d67d9417eacd06612230b74248cff` |
| PR #1833 contact | `d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0` |
| PR #1845 Gram/archive | `80623637571ee0e1ef4785406f0b0a2e52f8ec75` |
| PR #1847 price/renewal | `12062dc44287bd3f97b4fdc0ca4a931a56a16bcd` |
| PR #1849 complete minimum | `c9af56ae7f9ede45da9ff709f8663aaa1ae95105` |
| PR #1849 prospective execution pin | `ed90ffd1826190b1fe04af0cf172d2886be21067` |

These sources are available at
[PR #1833](https://github.com/mathorn1973/twist-j/pull/1833),
[PR #1845](https://github.com/mathorn1973/twist-j/pull/1845),
[PR #1847](https://github.com/mathorn1973/twist-j/pull/1847) and
[PR #1849](https://github.com/mathorn1973/twist-j/pull/1849).
At the audit, all four were open drafts with zero submitted GitHub reviews.
A later reviewer must refresh their heads, comments and checks before accepting
any input. Changed bytes require a new assessment, not silent substitution.

Current v106 Canon is 1,370,107 bytes with SHA-256
`52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7`.
Annotated tag object `8f2d16a216524a04be3e1210821ab1e27535ed77` peels to the
activation above. Content and tag target are ancestors of main.

## Independent mathematical handoff

The reviewer should record actual prior exposure, the exact source and proposal
hashes, and a verdict for each item. A rerun alone is not proof review.

1. **Contact:** check integral admission, refused-state identity, complete
   inverse, order, conserved sum/Hermitian norm/positive trace account,
   slot residues and the precise chosen operation alphabet. The contact and
   slot frame remain supplied L1 premises.
2. **Minima:** audit the coefficient bound, completeness of initial and final
   bank enumerations, all 26 slots, the permutation/multiset quotient, parity
   exclusions and complete-component certificates. A capped search is UNKNOWN,
   never an exclusion. Check the positive and signed witnesses and labelled
   inverses against the contact definition without trusting their PASS text.
   Distinguish power contacts, individual contacts and free permutations.
3. **Renewal and capacity:** inspect the retained-output hypothesis, complete
   residue inventory and fixed-word two-input restriction. Energy conservation
   is compatible with loss of a reusable prepared bank. The amounts 12 and 27
   are initial auxiliary trace accounts, not dissipated energy.
4. **Gram/archive:** check admission from the actual integral Gram image,
   forward/backward continuation and all occupied receiver states, references,
   clock phases and retention boundaries. This is a separate apparatus scope.
   Joining it to the preparation words requires a same-carrier composition
   proof; adjacency of the two constructions is insufficient.
5. **Scope:** retain every existing live H/O owner and boundary. Identify
   exactly which proofs support universal statements and which results depend
   on finite computation. No native-U realization, SI energy, Born occurrence,
   common physical apparatus or cross-layer promotion follows.

The requested review output is a public-safe acceptance table with exact
statement, dependencies, proposed status, proof location, computation pin and
verdict; explicit counterexamples or unresolved obligations; a separate manual
security review; and source/proposal SHA-256 values. The reviewer should identify
whether acceptance covers source statements only or the final folded text too.

Proposed statuses remain conditional until acceptance:

| Content | Possible earned disposition |
| --- | --- |
| Supplied contact law | Explicit definition/premise; no claim that J or native U forces it |
| Conservation/inverse/residue proofs | T at reviewed conditional L1 scope |
| Signed minimum 12 and positive four-slot minimum 27 | T only after accepted finite-reduction/witness proof and completed scientific replay; finite output alone remains computational evidence |
| Retained-output renewal and capacity boundaries | T only at their reviewed complete-carrier hypotheses |
| Gram continuation and seven-slot archive | Separate conditional T if independently accepted; no implied composition |
| Historical 130/294-word inventories and new shortest-word distributions | Excluded from earned v107 claims until their actual source bytes and evidence are supplied and reviewed |
| Unified physical preparation/response/record/renewal apparatus | Remains open |

## Existing computation and v106 publication evidence

PR #1849's actual scientific
[two-architecture run 41285912012](https://github.com/mathorn1973/twist-j/actions/runs/41285912012)
passed on its stated head. Its verifier SHA-256 is
`461b29dc6d3282a00fcccfd0cc194b198f856b688f78841658c93e49ecccac8f`;
stdout SHA-256 is
`95ee2135ecb491ab7f0702d603ea94013d00beb28e70668a3c418c0f21478178`
(1,755 bytes). Its local recorded runtime was about 6 seconds. Refresh the
actual job/log evidence rather than treating this paragraph as a new run.

PR #1833 records matching arm64 and x86_64 scientific notes replays. PR #1845 records
two implementations on x86_64 only. Ordinary notes CI does not execute their
scientific programs. PR #1847's small script covers two words, not the historical
complete census.

v106 main run 40556926452 and tag run 40557096572 succeeded. Release run
40834503295 was cancelled; its cancelled outcome remains recorded. The
[pinned recovery 40876195785](https://github.com/mathorn1973/twist-j/actions/runs/40876195785)
succeeded using controller
`c35b37195851a96c778c1284a6ba03a9183d62b3` and the unchanged v106 scientific
checkout. Publication job 123455520147 confirms 211 tests, 280 completed probes,
28 retained ABANDONED dispositions, 37 reproductions, static activation and
published-asset verification. The complete recovery took 45 minutes 47 seconds.
Controller CI 40876145049 also succeeded on both architectures.

Recovery [PR #1828](https://github.com/mathorn1973/twist-j/pull/1828) remains a
separate draft. Its 60-minute publication controller is not current main.
Do not merge it or change workflows as part of this review rehearsal. Current
main retains the 45-minute architecture and 40-minute publication budgets.

## Complete integration rehearsal, without a Canon fold

Use a fresh full-history Linux clone, Python 3.12, an isolated integration branch
and the exact public source heads above. Preserve original commits; do not amend,
squash or rebase pinned probes. Freeze and record the resulting integration SHA
and tree. Keep captured logs outside the checkout and do not run another worker
inside the same clone. This rehearsal changes no scientific status.

First verify the clean checkout, all four source heads as ancestors, unchanged
source bundles and unchanged current Canon. Existing pinned scripts may be
replayed; no new scientific executable is authorized by this plan.

The following commands use the tools' actual interfaces. Neither replay tool
has an `--all` option: omitting `--base` selects its entire inventory.

```sh
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
export LC_ALL=C LANG=C TZ=UTC
unset TWISTJ_EVIDENCE_DIR PYTHONIOENCODING PYTHONUNBUFFERED
test -z "$(git status --porcelain)"
git rev-parse HEAD HEAD^{tree}
python3 --version
uname -m

python3 tools/check_policy.py
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/check_canon.py
python3 tools/check_ledger.py
python3 tools/check_gate_contract.py
python3 tools/check_genesis_recon.py
python3 tools/check_external_sources.py
python3 tools/check_preregistration.py
python3 tools/generate_canon_views.py --check-dir canon
python3 -u tools/check_verifier.py
python3 -u tools/check_reproduce.py
test -z "$(git status --porcelain)"
```

With only these source additions, the expected inventory is 281 completed public
probes, 28 retained ABANDONED dispositions and 37 minimal reproductions. Verify
actual counts from the logs. ABANDONED dispositions are not successful runs.
The repository's unmodified probe runner enforces 600 seconds per probe and its
source-bound concurrency schedule; the reproduction runner enforces 120 seconds
per reproduction. Do not skip a slow verifier or broaden these budgets.

The historical Ward qualification probe rejects extra Python ambient variables, including PYTHONIOENCODING. The initial rehearsal failure and successful clean-environment supplemental replay are preserved in VALIDATION.md. Keep the full runner environment separate from any notes helper that sets additional encoding variables.

The full runners do not select `notes/` programs. Run the following separate
byte comparisons from the same clean integration root, preserving the exact
frozen scripts and records. This helper is an execution wrapper, not a new
scientific verifier; it delegates all assertions to the pinned sources.

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib
import os
import subprocess
import sys

env = os.environ.copy()
env.update(PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
           PYTHONIOENCODING="utf-8", LC_ALL="C.UTF-8")
cases = [
    ("notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/verify.py",
     "notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/EXPECTED.txt"),
    ("notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/verify.py",
     "notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/EXPECTED.txt"),
    ("notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/break.py",
     "notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/BREAK_EXPECTED.txt"),
]
for script, expected_file in cases:
    result = subprocess.run([sys.executable, "-B", script],
                            env=env, capture_output=True)
    expected = Path(expected_file).read_bytes()
    assert result.returncode == 0, (script, result.returncode)
    assert not result.stderr, (script, result.stderr)
    assert result.stdout == expected, script
    print("NOTES REPLAY PASS", script, len(result.stdout),
          hashlib.sha256(result.stdout).hexdigest())

script = "notes/canon/C-RELATIVE-CONTACT-FOUR-SLOT-PRICE-N/verify.py"
result = subprocess.run([sys.executable, "-B", script],
                        env=env, capture_output=True)
expected = (
    "PASS signed: 15 power contacts, auxiliary account 12\n"
    "PASS positive: 16 power contacts, auxiliary account 27\n"
    "PASS auxiliary histogram changes: retained-output clean reset forbidden\n"
).encode("utf-8")
assert result.returncode == 0, (script, result.returncode)
assert not result.stderr, (script, result.stderr)
assert result.stdout == expected, script
print("NOTES REPLAY PASS", script, len(result.stdout),
      hashlib.sha256(result.stdout).hexdigest())
PY
test -z "$(git status --porcelain)"
```

PR #1847 has no committed EXPECTED file; its comparison above uses the exact
three-line content already declared in its README. Report that distinction.
Do not confuse its 15-power signed witness with PR #1849's different 14-power
witness. No claim that either is globally shortest is made.

A source-integration checkout retaining v106 STATUS is not a release-form
candidate. Running the active gate against v106's content pin there would fail
its exact post-content three-file delta because newly integrated source files
exist. The constituent checks above are the appropriate full rehearsal.

For a separate unchanged v106 baseline, the actual full activation command is:

```sh
python3 -u tools/check_activation.py --full --post-activation \
  --content-commit 9242db4f040d67d9417eacd06612230b74248cff \
  --expected-tag canon-v106
```

A fresh whole baseline replay is optional when the integration rehearsal and
existing pinned recovery already answer the verification question. If performed,
report it separately rather than counting it as v107 acceptance.

Runtime planning is based on the successful v106 recovery log, not a guarantee.
Its longest probes took approximately 377 seconds
(P-CURVATURE-GAUSS-SPLIT-1), 360 seconds
(P-TWO-USE-TYPED-READOUT-CLOSURE-1), 188 seconds
(P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1), 157 seconds
(P-QDD-INSTRUMENT-U-INDUCED-1) and 140 seconds
(P-NIST-LOCAL-OBSERVED-INTERVAL-1). Its 308 probe timing records sum to about
2,689 worker seconds; wall time also includes scheduling, reproductions and
other gates. Budget roughly 45 to 60 minutes on comparable infrastructure for
one complete rehearsal, with architecture and load variation. Do not implement
a new scheduler or workflow to meet this estimate.

## Fold preparation after independent acceptance

A separate accepted-source consolidation preserves source provenance and
required checks. Then prepare the complete fold on current main, after another
collision and authority check. The content includes:

- Self-contained accepted statements/proofs, exact source links and explicit
  resource/composition boundaries in CANON; a brief consistent CORE account.
- REGISTRY, NORMATIVE, DEPENDENCIES, EVIDENCE and HISTORY additions with matching
  scopes, evidence identities, layers and hashes. Preserve earlier rows unless
  a separately justified change has been reviewed.
- CORE_SELECTION where useful, generated views and STATUS_COUNTS, CHANGELOG,
  and normative SHA256SUMS. Keep all live H/O scopes, gates and Frontier
  obligations intact unless an applicable accepted proof actually closes one.
- An extension of `reproduce/status-separation/verify.py`. It currently pins
  thirteen complete v106 Canon inputs, exact accepted source files and the
  37-directory reproduction inventory, then reconstructs earlier Canon bytes.
  Build a v107 outer adapter with exact current/prior byte hashes and explicit
  inverse edits. Preserve all 192 existing predicates, constants and output
  descriptions. Never bypass a mismatch, read old bytes as a fallback, or
  replace historical checks with current counts.
- Matching preauthored EXPECTED additions and README for that structural audit.
  Freeze the complete candidate before its first execution. This audit does
  not execute the new scientific sources.
- Update `tools/test_architecture_map_report.py` with the exact accepted claim,
  evidence, count and dependency additions. It currently binds 593 claims and
  T450/D59/C39/H2/O24/F19; do not weaken its assertions to accommodate unknown
  additions.

Use `python3 tools/generate_canon_views.py --apply` only during mutable fold
preparation, then recompute SHA256SUMS. Hash inputs in byte form, with LF output.
Audit exact staged paths and diff, author/committer identity, source ancestry and
public safety before freezing.

## Frozen release and publication, only after acceptance

The release branch has exactly two frozen commits over accepted source main:

1. Complete content fold, including its structural audit and tests.
2. Release-form commit changing exactly STATUS.md, README.md and CITATION.cff,
   identifying the content commit, v107 hash/bytes and canon-v107.

No content patch follows the content pin in this lane. If content needs repair,
preserve the failed candidate and use a newly frozen successor. `--dry-run`
is GENESIS-only and is not the v107 gate.

On a clean exact release-form head, run the static/unit checks above and:

```sh
: "${CONTENT_SHA:?set the exact frozen v107 content SHA}"
python3 -u tools/check_activation.py --full --content-commit "$CONTENT_SHA"
```

Both required PR architecture jobs must succeed with the entire replay inventory;
a Canon change widens their unchanged selectors automatically. Record a review
of the exact final head/tree, not only the source drafts. Merge without squash
or rebase, fetch public main and verify its tree equals that reviewed tree.

Only then create the immutable canon-v107 tag on the activation merge. Its
publication job must pass the unchanged full post-activation readback. Assemble
the release as a draft using only that successful tag-job
`activation-manifest.json` and tagged `canon/SHA256SUMS`. Download both draft
assets, validate the manifest with:

```sh
python3 tools/check_release_manifest.py /path/to/activation-manifest.json \
  --expected-tag canon-v107
cmp canon/SHA256SUMS /path/to/SHA256SUMS
```

Publish only after those comparisons pass, then verify the published assets and
release-event job. A locally generated manifest cannot replace the tag artifact.
If the current 40-minute publication budget causes cancellation, record the
cancellation and stop the affected publication step. Existing authorization to
release does not silently change the explicit workflow-policy contract.
