<!-- SPDX-License-Identifier: Apache-2.0 -->

# Replay record

**NON-CANONICAL / L1; one x86_64 architecture.**

Original local source pin: 19ff593512de31d8018edfc63d87f7294da7757e.
Original local outcome: f7e2ea7dfacf9870bc1bc67f0d121d3b14019b37.
This is an editorial replacement of the incoming run summary, prepared after
the original execution. It preserves the distinction between the supplied
first-run claim and the observed replay.

## Observed checks on 2026-11-08

Environment: Windows 11, AMD64/x86_64, CPython 3.12.10.
The scripts were invoked from the repository root with Python -B, using
PYTHONHASHSEED=0, PYTHONIOENCODING=utf-8 and
PYTHONDONTWRITEBYTECODE=1. Each invocation had a 120-second timeout.
Peak RAM was not independently measured.

| Script | Source bytes | Source SHA-256 |
| --- | ---: | --- |
| verify.py | 30892 | e2daf2f53e1e2e1410bb1fdd5a09a108c081e8b7a1ecb9090809c9ea05edc692 |
| break.py | 31928 | a1dd4213b92731f7f5050eccbfc36a2cf30a2f92c4c0b2755574afcf8f96f9ec |

An initial primary replay exited zero with empty stderr but failed the strict
comparison with EXPECTED.txt. A diagnostic repeat of the primary and a replay
of the second checker established the following. The initial mismatch is
retained as a mismatch; it is not relabelled as a strict PASS.

| Script | Exit | stderr bytes | Raw stdout bytes | Lines | Direct expected comparison |
| --- | ---: | ---: | ---: | ---: | --- |
| verify.py | 0 | 0 | 585 | 9 | FAIL: CRLF versus LF |
| break.py | 0 | 0 | 585 | 9 | FAIL: CRLF versus LF |

The two raw outputs are identical to each other:
SHA-256 d8df6a228ce87298b9600836c679a18e3b821b8b4afb000d3bd8d0ff5da21d06.

Replacing each of the nine CRLF sequences with LF produces 576 bytes,
SHA-256 a9e13f041b866a4dcae3b17754e01d5c2f6184835b02b1b26d7e3e8bb204c1f4,
identical to both committed expected files. No other byte transformation is
needed. This is a diagnostic newline normalization, not raw-output equality
and not an added scientific test.

Both scripts report 676464 checks and 105300 primitive cuts. The diagnostic
runs took approximately 0.62 and 2.22 seconds respectively; these are measured
wall times, not mathematical resource guarantees.

## Original-source custody

All eleven entries in the incoming SHA256SUMS matched their files.
The original six source files were compared byte for byte with the local
source pin before intake. Git ordering and unchanged bytes support custody;
they cannot alone establish that no earlier unlogged execution occurred.
The original author reported first-pass success. This replay does not
independently certify that historical first-execution claim.

The intake preserves PROOF.md, PREREG.md, verify.py, break.py and both expected
files byte for byte. The preregistration has 7441 bytes and SHA-256
7f562d5b351a6e7bb19345ba05dca64bf3db4d518355693ffba26dd87bf667e0.
Editorial differences are mapped in PUBLICATION.md.

Policy, Canon, ledger and gate-contract checks passed on the reviewed original
outcome. The public intake undergoes those checks separately. No aarch64
scientific replay, formal public gate or independent scientific acceptance is
claimed.
