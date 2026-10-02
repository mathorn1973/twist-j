# First author internal-control run

**PUBLIC, NON-CANONICAL. Actual first execution of the frozen author audit.**
Original work, Apache-2.0. Owner: A. M. Thorn.

Specification pin: `e5ff31fd7296df4bf740fd27c1ac3de14b5c8148`.
Complete author proof/program pin: `f247986326d3d1e93600efa312e07ddcefdef8c0`.
All five public source blobs were read back and matched to local raw bytes
before execution. The Linux checkout was clean at this exact full pin.
The independent program had completed its first pinned run before this
one. No scientific source was edited after freeze and no local rerun occurred.

```text
python3 reproduce/C-FIELD-J-INTERNAL-CONTROL-N/verify.py
```

Date (UTC): 2026-10-02. Ubuntu 22.04.5 LTS; x86_64; Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
External timeout: 120 seconds. Elapsed: 9.771 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Source or output | Bytes | SHA-256 |
|---|---:|---|
| notes/C-FIELD-J-INTERNAL-CONTROL-N/PREREG.md | 42875 | `ebc473f087158e382fbf4864b4f20676848b1c04821dbaafba53adfffd3ea40f` |
| notes/C-FIELD-J-INTERNAL-CONTROL-N/OCCURRENCE_INTERFACE.md | 11565 | `64277d3cd9389584e8a32ec0d7d80589c9f83d46a2b466c2464a7ee83777ae91` |
| notes/C-FIELD-J-INTERNAL-CONTROL-N/PROOF.md | 33012 | `e2c5a3346de3d5092067b8a3c82a1382dc40ee65af31bd9f87b90ea0cd99bc23` |
| reproduce/C-FIELD-J-INTERNAL-CONTROL-N/verify.py | 34888 | `bdc67875fd1f044fae13e263a993b42eecc90d9f5a83c539875159b504f76ef6` |
| reproduce/C-FIELD-J-INTERNAL-CONTROL-N/README.md | 11231 | `c0a4286a0a9780ed28ef1a281512f54a10802f9a0cde275cf78a8174dbdea820` |
| EXPECTED.txt (actual stdout) | 537 | `5814abd8c3bad3e3cff923f3bc7a1bf597a254c3d4d336c7013deddee4a1a63b` |

All registered finite audit groups completed with exact assertions and
empty stderr. EXPECTED is the actual scientific stdout, including exact
loop and accounted-microtick totals. Its output differs from the independent
program's output because those are independently selected domains and
implementations. Architecture replay compares each program only against
its own EXPECTED.

This first local run supplies x86_64 evidence. The unchanged stock
`tools/check_reproduce.py` must independently replay the frozen program
against this exact EXPECTED on both x86_64 and aarch64 before the
architecture gate is claimed. RESULT records the actual workflow,
PR head/test-merge and decoded reproduction entries after they complete.

The universal exact control claim rests on operator proofs and review;
finite audit success alone does not set a physical error to zero. The
preparation error is charged once against the actual retained remainder;
actual selection and its occurrence law remain undefined. Canon v96,
physical layer gates, workflows and previous scientific sources are unchanged.
