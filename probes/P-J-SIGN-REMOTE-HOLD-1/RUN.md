# First run: P-J-SIGN-REMOTE-HOLD-1

NON-CANONICAL / L1. This record describes the first scientific execution of
the frozen source set. The finite result is candidate-C; it is not a Canon
promotion or independent acceptance of the analytical proof.

```text
pin_commit: 015c6b6f68cb8e005f0833f8a1f6f71b051215a1
verifier_sha256: c554f070f254fdfc177f3c81ec1ff071258b61266a9a23ac2764d2cb1beed18e
command: python3 probes/P-J-SIGN-REMOTE-HOLD-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 86671fa7c21d5b5e3a696bf977636fd2c5f57e515bd1920b59455df249252b56
stdout_bytes: 1351
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Source custody

The complete scientific source set was committed and published at
[the exact source pin](https://github.com/mathorn1973/twist-j/commit/015c6b6f68cb8e005f0833f8a1f6f71b051215a1).
All three public file contents and Git blobs were read back and matched
byte for byte before execution, with readback completed at
2026-11-09T07:32:46.001906Z. The checkout was clean at that exact pin before
and after the scientific command; all three source hashes remained unchanged.

| Frozen source | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 17128 | f8dea6b82ebad491662b166e386a9383270762d43efef25b6ec8b23dde4dbe29 |
| PROOF.md | 24103 | d7ffeaf4b9e2a9f528fcaaecfc945cd9f7eea30ac8f868734dbf406f9f5a0f39 |
| verify.py | 22516 | c554f070f254fdfc177f3c81ec1ff071258b61266a9a23ac2764d2cb1beed18e |

Before this first run the new verifier was read, parsed with `ast.parse`,
and hashed. It was not imported or scientifically executed. Static authoring
reviews preceded the pin; they are not independent scientific acceptance.

## Execution and capture

The command ran from the repository root with assertions enabled. Inherited
`PYTHON*` and `TWISTJ*` environment variables were removed, then the following
reproducibility values were set:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
LC_ALL=C
LANG=C
TZ=UTC
```

The first scientific process started at 2026-11-09T07:34:08.533825Z and ended
at 2026-11-09T07:34:17.927622Z. Measured capture duration was 9.393783 seconds,
below the fixed 600-second timeout. No timeout, interruption, retry or
scientific source change occurred. The process wrote one compact sorted-key
JSON report followed by one LF, and no stderr. EXPECTED.txt is a verbatim
byte copy of that first stdout, not regenerated expected output.

At the first run's recording, the two-architecture repository gate and
external independent mathematical review were pending. The subsequent CI
receipt is recorded below. External independent mathematical review remains
pending. The two arithmetic paths and the proof-derived oracle are author-side
checks; they do not constitute independent proof review.

## Recorded two-architecture CI

The required architecture jobs and aggregate passed in
[run 42580693180, attempt 1](https://github.com/mathorn1973/twist-j/actions/runs/42580693180/attempts/1).
The reviewed PR head was
[1595a0986453eea93acd5bb00e10a99b5bdc54ed](https://github.com/mathorn1973/twist-j/commit/1595a0986453eea93acd5bb00e10a99b5bdc54ed),
with base 629a9d4058501f938dc91a690c3eb59a914493d1. GitHub checked the PR's
synthetic merge with that base. Its probe contained the same three frozen
scientific sources and original EXPECTED.txt; the CI merge is not a new
scientific source pin.

| Architecture | Actual job | Runner platform | Python | Measured verifier replay | Outcome |
|---|---|---|---|---:|---|
| x86_64 | [129038414804](https://github.com/mathorn1973/twist-j/actions/runs/42580693180/job/129038414804) | Ubuntu 26.04.1 | 3.12.16 | 11.070 seconds | PASS |
| aarch64 | [129038415139](https://github.com/mathorn1973/twist-j/actions/runs/42580693180/job/129038415139) | Ubuntu 24.04.5 ARM | 3.12.16 | 17.789 seconds | PASS |

The actual logs for both architecture jobs were read. Both contain the
architecture marker and successful verifier replay with verifier SHA-256
c554f070f254fdfc177f3c81ec1ff071258b61266a9a23ac2764d2cb1beed18e and stdout
SHA-256 86671fa7c21d5b5e3a696bf977636fd2c5f57e515bd1920b59455df249252b56,
matching the original 1351-byte expected report exactly. Both pass all
219 repository unit tests and the required policy, Canon, ledger and gate
checks. The [aggregate job 129038827797](https://github.com/mathorn1973/twist-j/actions/runs/42580693180/job/129038827797)
also passed.

These are actual x86_64 and aarch64 byte-identical computation receipts.
They satisfy the two-architecture computation gate for this frozen finite
audit. They do not replace external independent review of the all-parameter
proof and do not themselves authorize a Canon promotion or release. The
flat fields above continue to describe the original first local execution.
