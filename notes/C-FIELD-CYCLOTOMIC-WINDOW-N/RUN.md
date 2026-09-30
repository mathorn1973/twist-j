# Frozen execution record

PUBLIC / NON-CANONICAL, L1. Issue #1301. Disposition: PARTIAL / PRIMARY STOP.
These are candidate-note executions, not formal public-probe run records.

## Public custody before execution

Preregistration pin: 713109d854693fbbc8e00e9bcb45ef4f4570c7d1.
Joint implementation pin: 40b30d87b617bf412980dcf8368f46b57407ad95.
The three public GitHub content blobs were read back before either program
executed and matched local Git blobs exactly. The checkout was clean.

| file | Git blob | bytes | SHA-256 |
| --- | --- | ---: | --- |
| PREREG.md | c0d5126291b805b4f93354c7aa33e1b9aa35af3a | 11407 | e54d7909eaa1053b180542454f86b2ccd0ad455b71a4d3b76098b2dd28125cba |
| verify.py | fa1cf569edca8d056046b3a00987e631ba860bad | 14064 | 4a62085cfd224aa7561e7c0d195aa06653fe19a59cb17da722cf2a4051202099 |
| break.py | a33ec37b97e42d120c1df72eebe8d2c7a49f033a | 23882 | 20028cf14b2aabaa87ec01de182a1e62ecd5443a914d4bd2aa82a3e7ab8cd023 |

The verifier checks the six public source hashes from PREREG. External
custody checks bound all three frozen files immediately before execution.
Neither program nor PREREG was changed after these pins.

## Environment and commands

platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
LC_ALL=C
LANG=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
per-script timeout: 120 seconds

From the repository root, in this order, once each:

```text
python3 notes/C-FIELD-CYCLOTOMIC-WINDOW-N/verify.py
python3 notes/C-FIELD-CYCLOTOMIC-WINDOW-N/break.py
```

Execution was captured with the standard-library subprocess API using the
frozen environment and timeout. That capture is not a substituted repository
formal runner. No randomness, floating point, third-party Python package,
private module or archival executable was used.

## Primary: failed, preserved

exit_code: 1
stdout_file: VERIFY.txt
stdout_bytes: 57
stdout_lines: 1
stdout_sha256: 0455d855dd82f557031a279dd45f6f9742b16459d0c6e8deab76984a81667081
stderr_bytes: 376
stderr_sha256: 86600b685ee1ed765eaa84e81e1a6a0c94869fb78af5a64a4ab07536c94b5883

The exact stdout is the one committed line in VERIFY.txt. Failure was an
AssertionError at verify.py line 290:

```python
assert member == explicit == (tuple(y) in image)
```

The full stderr is not a public artifact because its traceback contains a
local filesystem path; its original byte count and hash are retained above.
The minimal failure location, unchanged source and exact counterexample
are enough to reproduce the defect without importing a machine transcript.

The first mismatch is y=(0,0,1,1). The hand-entered predicate accepts it,
but N y=(3,1,-2,1) is not divisible by five. A second false assertion in
unreached code labels y=(0,0,1,2) a nonimage H=5 state, although its integer
preimage is (1,0,-1,1). This second diagnosis is exact static analysis,
not a second failed execution. Later primary checks and PASS lines were
not reached. There is no complete successful primary stdout, no amended
primary and no rerun.

## Independent implementation: passed

exit_code: 0
stdout_file: BREAK.txt
stdout_bytes: 3154
stdout_lines: 52
stdout_sha256: 9bd3fb7fb790083d9afbbe26b7b4ad57e904018db2c751151b73b5d88811bb7f
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

The separate challenger wrote break.py only from the frozen preregistration
and public definitions; it did not read the primary source, builder proof,
calculations or outputs before its source freeze. It reconstructed the step
from coordinate updates, computed determinantal divisors rather than the
primary Smith algorithm, and derived image admission directly from the
inverse numerator. The two sources were frozen together before comparison.
The differing static bases are unimodular changes of the same static lattice,
not a mismatch. Mathematical targets were exposed in advance.

Its successful transcript includes all 625 residues (25 admitted, 600
rejected), Smith invariants 1,1,5,5, the exact module/Hermite certificates,
empty/rank/critical/unstable controls, and actual D-based charge tests.
Finite controls are not the universal theorem; PROOF.md gives the all-C,
all-n and all-integer-lattice arguments.

## Limits and repository validation

Both programs ran on the same x86_64 environment. Independence of authorship
does not supply architectural independence. The required Python 3.12 public
two-architecture scientific computation gate is unresolved for this package.
The current workflow's changed-path runners select probes/ and reproduce/,
not these notes. Therefore notes-only CI cannot be cited as replay of either
scientific program. No shared checker, allowlist, workflow, sealed probe or
formal run invocation was modified to create such a claim.

Repository policy/Canon/ledger/gate checks and the normal PR check are
reported separately in REVIEW.md. Their outcome does not erase the failed
primary execution. SHA256SUMS binds this small candidate package.
