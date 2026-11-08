# Independent run record

NON-CANONICAL / L1. One x86_64 review execution, not a new public
two-architecture scientific gate.

Target: PR #1871 head `26731e2bd7f1394b4d274528525e6d78cbe6bbf9`.
Target source pin: `4e448bb3b13c4e8f0338524e7c69ade1c01caf0f`.
Review source pin: `8199bb6297178ebeb001820d51b1a3882796ba29`.
All three review sources were publicly read back byte for byte before run.

- PREREG.md: `fcbdd315cb889a9e30aaccf62ff142cd634370e094b2090a7232103f3ea2ac90`.
- review.py: `e615346185100da3aa68bc5d6432ac5781752ce16311a97cac71378586de1eb8`.
- REVIEW-SCOPE.md: `0e9a48d6d5c41dc2def54a911c45e8a3aa8e1e6673d2b99d6c98ebb71b75f482`.

Known announced success and contract formulas were exposed. Author code,
literal word and stdout were unread before the independent source freeze
and own completed execution. Result-exposed code independence is claimed;
blind discovery is not. No target scientific module was imported or called.

Actual task-workspace command:

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -u review_1871/review.py --dump-data review_1871/review-dump.json
```

Repository replay, with optional scratch dump omitted:

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 notes/C-COMMON-APPARATUS-TWO-INPUT-REVIEW-N/review.py
```

Started UTC: `2026-11-03T07:28:05.229947+00:00`. Platform: Linux. Architecture: x86_64. Python: 3.12.14.
Exit code: 0. Stderr: 0 bytes.
Actual stdout: 1906 bytes, SHA-256 `f98d6735fd07808fe3446fa7ca33ded877fa928537fb44bf672a3b3a6b443cb0`.

EXPECTED.txt is this review's actual stdout, not the target's distinct
output format. The optional raw dump is scratch comparison material; it
is not a scientific input or required publication file. REVIEW-SCOPE.md
fixes all fingerprint serialization before execution.

Executed counts: 100 complete 56-slot preparations and inverse restorations,
4000 full read checkpoints, 2000 full step checkpoints, 100 reload checkpoints,
600 designated events, 5350000 trajectory contacts and 1000 swaps. A separate
18-contact source fixture is excluded from those trajectory counts. All 24
frozen strict-reader mutations were rejected.

Post-execution comparison with the target literal word and outputs is
recorded separately. CI-AUDIT.md checks the target's own scientific replay
on x86_64/aarch64; this review's ordinary notes-only repository CI is an
integrity check and does not add a second scientific architecture lane.
