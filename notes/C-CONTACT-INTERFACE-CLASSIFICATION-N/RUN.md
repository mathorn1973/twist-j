# First execution record

NON-CANONICAL / NO AUTHORITY. Local one-architecture audit only.

Both programs were frozen before either first scientific execution. No prior
scientific dry run occurred. Only static syntax/compilation checks preceded
the pins. No code correction or rerun was needed.

## Pins

| Artifact | Git commit | SHA-256 |
|---|---|---|
| PREREG.md | b2ec1f81459829c2541ca38c59acd45c63e9f4fb | 594b871504191af2b1f3d9ab70ca1398032bad6b767ab1c85e6e92a864790f6b |
| verify.py | 2a2f74c2e47e911e92825468f476f006d10b96bc | 3485005c57c899c23c785e1a1245c50acb69266a55fb321db69818c521afc99c |
| break.py | 3ced9591630916bbed8d08c438c4179b12296e10 | aed38cf0c64534aabf2214067d9dbab36a6e465133b5627f3efe654a6f5ad548 |
| Corrected PROOF.md | b7ae04f0fd32391d080b4c5847cc76c9665259af | 8c7de381aab7fddfd151a0b63dc7fecee961fa5679e18329c20da7dbc1541234 |

Both first executions used clean checkout
`b7ae04f0fd32391d080b4c5847cc76c9665259af`.
The original program hashes were checked before and after execution.

## Environment and process limits

Operating system: Ubuntu 24.04.3 LTS.
Architecture: x86_64.
Runtime: CPython 3.12.14.
Real wall timeout: 180 seconds for each program, enforced by an external
`subprocess.run(..., timeout=180)` runner. Programs ran sequentially.
Timeout would have been recorded as incomplete, not a scientific exclusion.

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Each command was `python3 -I notes/C-CONTACT-INTERFACE-CLASSIFICATION-N/NAME.py`
from the repository root, with NAME=verify and then NAME=break.
Fresh stdout/stderr files were opened exclusively before each first run;
no previous transcript could be overwritten.

## Observed first runs

| Field | Primary | Independent breaker |
|---|---|---|
| Start UTC | 2026-10-06T17:17:04.267523+00:00 | 2026-10-06T17:17:43.834628+00:00 |
| Elapsed nanoseconds | 15763834233 | 7844376484 |
| Exit code | 0 | 0 |
| Timeout | False | False |
| Stdout bytes | 571 | 571 |
| Stderr bytes | 0 | 0 |

Both stdout streams are byte-identical to EXPECTED.txt, including one final
newline. Their common SHA-256 is
`4480997f001ee8781237422e44a66aaf31a46a8a076bd0e7fa50b007721b22ee`.
Both empty stderr streams have SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Control census SHA-256:
`83bfd84ee71a9eb13a0b179175f8fb75e57d47920db7858853c96deaa7affe59`.
Reader census SHA-256:
`f721d7500218861fd4580c6b0576b74430fffc898f8e6a2a1992f7307bdea3eb`.

## Independence and public custody

The breaker was implemented from the frozen preregistration and its source
identities in a separate agent context. Its author had not read the primary
program, expected counts, output or another repository verifier before the
breaker pin. The coordinator integrated the unmodified Git commit and then
executed both programs. The analytical reviewer read neither implementation
nor its output. These are agent-context independence statements within this
session, not claims of external human review.

The exact preregistration text was publicly posted and read back before any
execution:
https://github.com/mathorn1973/twist-j/issues/1396#issuecomment-6021434665
Both implementation pins and hashes were publicly posted and read back before
either execution:
https://github.com/mathorn1973/twist-j/issues/1396#issuecomment-6021556269

The local Git objects themselves were not pushed: HTTPS Git had no credentials;
the connected commit API exposed no override for its nonconforming default
commit email. SSH lookup was also unavailable. No wrong-identity commit was
created remotely, and no public branch/PR/CI is claimed. The complete local
Git history preserves the mandated author identity and all immutable pins.
The public issue comments timestamp the disclosures but are not a fetched
Git branch or a formal two-architecture staging lane.

## Status ceiling

Finite evidence: candidate-C on x86_64 only. Written proof and its exact
review are separate candidate-T evidence within NON-CANONICAL notes.
No scientific aarch64 execution or public two-architecture gate occurred.
Ordinary notes policy checks cannot replace that gate. These audit runtimes
are not word-length or implementation-cost results for T_alg or V.
