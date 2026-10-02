# Author exact preparation audit

**PUBLIC, NON-CANONICAL. One actual first run of the frozen finite audit.**
Original work, Apache-2.0. Owner: A. M. Thorn.

Specification pin: `7809098069d4c4ff9f362048cf92c3e8b4714493`.
Complete author source pin: `4bbd66ba7b979660fe2ec3b8eb855cef8a5063c1`.
The author source was publicly frozen and read back. The separate independent implementation had already completed its first pinned run before this author run.
All source bytes were matched to the public Git blobs before execution.
The runner used an exact clean checkout with its own Git metadata on Linux;
the checked-out verifier bytes matched its immutable Git source.

```text
python3 reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/verify.py
```

Date (UTC): 2026-10-01. Ubuntu 22.04.5 LTS; x86_64; Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
External timeout: 120 seconds. Elapsed: 3.632 seconds.
Exit: 0. Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Source or output | Bytes | SHA-256 |
|---|---:|---|
| notes/C-FIELD-J-PREPARATION-MECHANISM-N/PREREG.md | 28795 | `c164cfaf7cf24537d899760e06304a9f94d269e4f376810d67c856d86cdc9b2d` |
| notes/C-FIELD-J-PREPARATION-MECHANISM-N/PROOF.md | 33420 | `ea13ff33164ad1986d0054819470c410fcbdaa5b9debe4a9cb37a44d643e20fb` |
| notes/C-FIELD-J-PREPARATION-MECHANISM-N/INTERFACE.md | 7196 | `2cdfa952ed4d81a6a3a591baecfb1c3694c7275f3e4ab1adace8bf280e894a4f` |
| reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/verify.py | 26455 | `9036378f0d5babae9d3c33f754bab5b28a03f449b309e32cda859df7fbe549fd` |
| reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/README.md | 6722 | `7d88c835a3b0bce8548b94c6bf4623e3c6baa6d0bdcf71ccedf45c5e06a2772f` |
| EXPECTED.txt (actual stdout) | 526 | `02a11e0babc33f06cdb1d5d13d2c8df54e1bbd5c1514cc78f1881ba47ef301d3` |

All six registered finite audit groups passed. EXPECTED.txt contains only
the actual deterministic scientific stdout. No source file changed after
its freeze and no local rerun was needed. The author and independent
programs have distinct domains and stdout; they are not byte-identical
replays of one implementation.

This local run is x86_64 evidence. The existing stock
`tools/check_reproduce.py` also selects this directory in the proposed PR
and requires exact verifier/EXPECTED byte comparison on x86_64 and aarch64.
Those workflow executions require their own public job evidence; they are
not inferred from this local record. No workflow or runner is changed.
The universal statement rests on the separate analytic proofs and review;
this finite audit supplies no physical preparation, actual occurrence,
empirical confirmation or Canon promotion.
