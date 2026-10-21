# Exact local run and reproduction

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.
Scientific source frozen before execution at commit 6b459a66d670656bd02a09c26da666bd16c077fb.
Pin receipt: https://github.com/mathorn1973/twist-j/issues/1582#issuecomment-6238930475

```text
pin_commit: 6b459a66d670656bd02a09c26da666bd16c077fb
verifier_sha256: bab58b9d4bef1aadb042a96479f893477644122817755c5d2988a5c8d5a72def
command: python3 probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 8b6b08e8ee764075d480e461d4c6696d25d301f9f05d5d48a9dfcbb28fff80a9
stdout_bytes: 520
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Environment: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. The local x86_64 run was completed with the
same pinned source whose local Git blob is
d32a2ba6dba859751e03e5ca5e8d377f9e1dd844, identical to public
readback. The very first command was `python verify.py` in the
temporary source directory; the subsequent contract-form `python3
probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py` in a temporary matching
relative root produced stdout byte-identical to the first and empty
stderr. The fields above record the contract-form reproduction using
the same Python 3 interpreter and pinned file.

`EXPECTED.txt` contains the captured exact nine lines, not a
scientifically edited or rounded summary. Zero floating-point
operations; all 16, 64, 625 and 3125 checks use integer arithmetic.
No post-pin verifier or preregistration changes. No runtime repository
imports and no user-provided data files.

This is a single x86_64 scientific lane, with same-architecture replay.
It does **not** by itself satisfy the two-architecture computation gate.
GitHub PR x86_64/aarch64 runs and aggregate `check`, if completed,
must be separately verified before a status claim is promoted.
