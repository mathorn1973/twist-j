# C-NATIVE-FIBRE-PENTIT-WIGNER-N

**NON-CANONICAL. Incubation note. Action layer L1 only.**

[SCOPE] Exact phase-point representation of one pentit on the native fibre,
line counting with a supplied fresh coordinate, and a bounded prohibition of
point counting for the declared QDD reading. This note grants no Canon status.

[CLAIMED] Public issue [#1342](https://github.com/mathorn1973/twist-j/issues/1342).
Publication owner: A. M. Thorn / `CODEX-W3-NOTE-20261002`. The owner authorized
this note on 2026-10-02. Merge remains the owner's decision.

## Current evidence

| Item | Status | Evidence |
| --- | --- | --- |
| Original base and addendum | PASS, incubation | 38 base assertions, 12 addendum assertions, 21 base breaker checks and 11 addendum breaker checks |
| W1 second architecture | PASS, byte identity | All four frozen programs agree on x86_64 and native aarch64; exit zero and empty stderr for each |
| W2 independent author | PASS, independent local audit | Ten audit groups, a direct shear proof for S3, and one byte-identical repeat on x86_64 |
| Fired frozen-claim falsifiers | NONE OBSERVED | Within the declared finite audits and proof review |
| Public probe or status promotion | NOT PERFORMED | This publication is a note; the incubation pins and executions precede it |

[CURRENT RECORD] Read this README and [RUN.md](RUN.md), then the unchanged
[promotion proposal](PROMO-rev2.md), [base result](RESULT.md),
[addendum result](RESULT-ADDENDUM-1.md), and [W2 result](W2/RESULT.md).
Statements in the original proposal and results that W1 or W2 are pending
describe their earlier recording time. Their bytes are preserved. The W2
statement that public landing requires an owner decision is also historical;
the authorization above covers this note only.

## Boundaries

[STOP] `C-OCCURRENCE-CYCLE-COUNT-N` remains
`STOP_APPLICABILITY / H_NOT_TESTED`. Nothing here passes its Gate 0 or supplies
an occurrence law.

[STOP] No native contract of repeated events or native renewal of the fresh
coordinate is established. Ensemble counts are not trajectory frequencies.

[CONDITIONAL] The real sum-zero reading of the QDD four-vector remains a
declared premise. S6 and the LOW/HIGH tables of S7 remain conditional on it.
This note does not adopt that premise as a Canon row.

[QUALIFICATION: S8] The lower bound of five equally counted continuations per
point applies to a universal, preparation-independent point/current-direction
kernel that leaves the point ready for arbitrary subsequent line readings.
A terminal two-outcome marginal alone does not require its unused final
refresh. History-aware or preparation-aware updates may skip a refresh in
cases outside this kernel class. U1 and the audited joint and final-point
laws remain intact. Conditional states are defined only for positive-count
histories. See [W2's scope qualifications](W2/RESULT.md).

[QUALIFICATION: S5] The substantive odd dimensions are at least three;
dimension one has no nonzero real sum-zero state.

[SCOPE] The point-counting obstruction is the uniqueness of line inversion on
25 points. No wider contextuality theorem is imported. Generator bijectivity
does not imply bijectivity of the selected U. Negativity explains neither the
number 31 of incidence channels nor their minimality. The parity split 3 + 2
characterizes p = 5 and selects no dimension.

## Files and immutable provenance

[PRESERVED] Every imported file is byte-identical to its source. The complete
54-file mapping, hashes and byte counts are in [SOURCE-MAP.tsv](SOURCE-MAP.tsv).
The `package` group refers to the supplied incubation package; the `review`
group refers to the subsequent W1/W2 work. Only names and directory placement
changed. The original archive SHA-256 is
`d1afc4e1bbf0bca130117e5cd91d359f3ae9081b67fa6eac6d588e6b3d6396ee`.

| Landed file or directory | Contents |
| --- | --- |
| `PREREG.md`, `ADDENDUM-1.md` | Original frozen preregistrations |
| `verify.py`, `verify_addendum1.py` | Original frozen verifiers |
| `EXPECTED.txt`, `EXPECTED-ADDENDUM-1.txt` | Original verifier stdout |
| `break_check.py`, `break_check_addendum1.py` and corresponding `.stdout` | Original same-author breakers and outputs |
| `PIN.sha256`, `PIN-ADDENDUM-1.sha256` | Original pins, including original filename references |
| `RESULT.md`, `RESULT-ADDENDUM-1.md`, `PROMO-rev2.md` | Original results and current incubation proposal |
| `exposure/` | Pre-freeze reconnaissance code and output, retained as exposure evidence |
| `W1/x86_64/`, `W1/aarch64/` | Neutral architecture records, exact stdout and stderr, and execution metadata |
| `W2/` | Independent preregistration, proof audit, breaker, pins, results and exact execution records |
| `README.md`, `RUN.md`, `SOURCE-MAP.tsv`, `SHA256SUMS`, `.gitattributes` | Publication overview, consolidated record and byte-preservation support |

[MAPPING] Frozen documents and pins name their programs using the original
project filenames, sometimes without the `claude_` transport prefix. Resolve
those names through SOURCE-MAP.tsv; the documents and pins were not rewritten
to use the shorter landed names. W1 records refer to the original package and
capture wrapper at execution time. The direct replay below uses landed names.

[INTEGRITY] The note's `SHA256SUMS` inventories all landed files except itself.
It is a publication manifest, not a retrospective preregistration pin. The
local `.gitattributes` disables newline conversion within this directory to
preserve both the original LF files and W2's native CRLF records.

## Replay

[RECIPE] From the repository root on Linux, first check the note manifest:

```sh
(cd notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N && sha256sum -c SHA256SUMS)
export LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
python3 notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/verify.py
python3 notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/verify_addendum1.py
python3 notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/break_check.py
python3 notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/break_check_addendum1.py
```

[REQUIREMENT] Capture raw stdout and stderr separately, check each exit code,
and compare stdout bytes and hashes against RUN.md and the corresponding
recorded output. Do not normalize newlines. A mismatch is a finding; preserve
it and stop rather than altering a frozen program. The base verifier requires
the pinned `reproduce/census/verify.py`; the other three need no repository file.

[EXPOSURE DECLARED] Original targets were seen before their freezes and all
four programs ran before public landing. The original breakers were written
by the verifier author. W2 used a different author and mathematical statements,
without reading the original Python code, but its targets were exposed too.
Neither W1 nor W2 is a blind public probe. Repository CI checks the note's
policy compliance; it does not automatically replay verifiers under `notes/`.

## Work that remains separate

[O] Whether `(1+sqrt5)/10` is the sharp infimum over all nonzero real sum-zero
states at dimension five remains open. The proven lower bound is `sqrt5/20`.
The finite censuses do not close this question.

[OWNER DECISION] Adoption of the QDD reading, a fresh public probe with full
exposure declaration and its own public pin, and any integer-versioned fold
with registry rows remain separate decisions. This note changes no normative
file or registered scope.
