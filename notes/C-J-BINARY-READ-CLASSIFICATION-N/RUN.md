# C-J-BINARY-READ-CLASSIFICATION-N: run record

**NON-CANONICAL, L1.**

## Pin and readback

```text
base          main e6240e2689bb22aab5f02bad90b75d3692bb96d9 (Public Canon v104)
pin commit    e77187f1fead01ccd8e043730352abf5bb8e4787
author        A. M. Thorn <thorn@twistj.com>
branch        notes/c-j-binary-read-classification-n
reservation   https://github.com/mathorn1973/twist-j/issues/1728
```

The pin was pushed, and an independent shallow clone of the branch read back
the commit and all six files before any execution. Every SHA-256 matched:

| File at pin | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 8319 | 2d77e8d49f7cf372e2425aad0802c0368b1456b306bd14b8437ab8b7b57cd11b |
| PROOF.md | 6061 | 2fcb16ce4a2066da3795b29f2fc490037a53f54973903f839b45227d3dc8beaf |
| README.md | 1194 | 97299baf3948afd1b78f43d9836331522073117e25d7a6cdfca43b6c43aec7db |
| verify.py | 12154 | d3db55615719452324d6f26f6674b7fafc69a7b4470b204c945a00dddd45ccc5 |
| break.py | 13008 | 6e24103a61199727d7261bfe22338a70aa3f8c6b0b2cd2dec8932c99d84173ee |
| compare.py | 1413 | a5ed83ef6471b1a7811da3be809e61405725bacb87787b4bf9a73b1cc1ce629b |

Before the pin only text review, syntax parsing, pyflakes and the
repository checks were run: check_policy PASS, check_canon PASS v104 and
check_ledger PASS. No scientific program was imported or executed.

## First and only execution

All three programs ran from the repository root at the pin commit with a
clean worktree:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
python3 notes/C-J-BINARY-READ-CLASSIFICATION-N/verify.py  > EXPECTED.txt
python3 notes/C-J-BINARY-READ-CLASSIFICATION-N/break.py   > BREAK_EXPECTED.txt
python3 notes/C-J-BINARY-READ-CLASSIFICATION-N/compare.py > COMPARE.txt
```

Environment: platform Linux, architecture x86_64, CPython 3.13.17.

| Program | Exit | Wall time | Stdout bytes | Stdout lines | Stdout SHA-256 | Stderr |
|---|---:|---:|---:|---:|---|---|
| verify.py | 0 | 0.07 s | 29350 | 431 | 1566855c5b5f273d72ae640e49fee7b987a4e799cf22007a5249f4b7d850aef3 | empty |
| break.py | 0 | 13.5 s | 29495 | 432 | 631afe8af9628164f8365b57537b1d33cb3bf3601b2ed365298866ebe7df4b04 | empty |
| compare.py | 0 | below 1 s | 224 | 5 | 45d7414468dbb06a5031c31966ac14d849900a22da644e3fe05960be073bc079 | empty |

Wall times are engineering readouts only. The stderr files are retained
empty (SHA-256 e3b0c442...b855).

No rerun, repair or threshold change occurred. All three programs are by one
session and ran on one architecture. This is a reproduction-grade record,
not a two-architecture gate.

## Cosmetic observation, not repaired

break.py prints the characteristic polynomial of phi^-1 with signed
coefficients substituted literally, as `x^4 - -2 x^3 + -1 x^2 - 2 x + 1`.
That is x^4+2x^3-x^2-2x+1=(x^2+x-1)^2, the correct polynomial. The line is
informational and enters no comparison.
