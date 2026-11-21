# First pinned Linux run

NON-CANONICAL / L1. Completed exact audit and bounded construction attempt.

pin_commit: ce3ce82b49478c1f65fda8cfc2e412e8feb4f7f8
verifier_sha256: 9ba91e9c933470d8c63bd8c88a09d53f30ba2c2da347ce67b43bf070046295d7
command: python3 probes/P-POLE-HEIGHT-COMMON-ODD-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 966de8e350775121ab6d2b38379a82f6206205d919661976415249da0189fcaf
stdout_bytes: 18997
stdout_lines: 118
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All seven immutable source contents and Git blobs were read back publicly
before execution, as recorded in issue1901. A clean detached Linux clone
verified every source hash before the command and remained clean afterward.
This was the first scientific execution. No failed run or retry occurred.
No pinned source, limit, target or expected outcome was changed.

Assertions were enabled. LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 were set. Inherited PYTHONOPTIMIZE,
PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR were removed.
The external600-second timeout was not reached. Actual wall duration was
approximately1.486seconds, operational metadata rather than physical time.
The fixed20-round beam horizon was reached with no common-five witness.
That LIMIT_LAYER_BUDGET outcome is the registered scientific non-finding,
not an execution failure or a common-word impossibility.

## Frozen source custody

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 10377 | 5b5c25646d87e98f1928af85d60285025b60716246828d048787b3453e03559b |
| README.md | 1636 | b5abc08762818231395f0d02f6f754fa40af890bcb78f557018e15a6c563dbf3 |
| PROVENANCE.md | 2958 | 9f981af2db3697759a10d768ade398ba6ee23d71e45ef352fea0757e2e5f2469 |
| PROOF.md | 12741 | eecb658588aa876fc16d4fad989d7436cb40c4855d6ac6bbe6cfaccbc291adfb |
| STABILIZER.md | 6526 | e9f3ff1e7aaa39014ca75f576bdea5450ff282a5699c5b3c65068efa0668e94f |
| SOURCES.tsv | 2386 | 6023fd8d1224eda95166462909148067e1950897093005beccde5a3990edba81 |
| verify.py | 26727 | 9ba91e9c933470d8c63bd8c88a09d53f30ba2c2da347ce67b43bf070046295d7 |

EXPECTED.txt is the exact captured scientific stdout. Only EXPECTED.txt,
RUN.md and RESULT.md are appended after execution. Actual local repository
checks and required architecture CI are reported after their completion.
Two arithmetic routes and same-session static reviews are authoring checks,
not independent-session scientific acceptance or Canon promotion.
