# Independent exact preparation audit

**PUBLIC, NON-CANONICAL. One actual first run of the frozen finite audit.**
Original work, Apache-2.0. Owner: A. M. Thorn.

Specification pin: `7809098069d4c4ff9f362048cf92c3e8b4714493`.
Complete independent source pin: `4e5d56faac8fcd8bbbde7bed6d5b3783383f15eb`.
The independent source was publicly frozen and read back, then this first run completed before author proof/code/output exposure.
All source bytes were matched to the public Git blobs before execution.
The runner used an exact clean checkout with its own Git metadata on Linux;
the checked-out verifier bytes matched its immutable Git source.

```text
python3 reproduce/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/verify.py
```

Date (UTC): 2026-10-01. Ubuntu 22.04.5 LTS; x86_64; Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
External timeout: 120 seconds. Elapsed: 4.732 seconds.
Exit: 0. Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Source or output | Bytes | SHA-256 |
|---|---:|---|
| notes/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/PREREG.md | 10303 | `de69658eadf4acbc168bd8bc84bf8046db1cb9b480e045326dcb35200be93cd3` |
| notes/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/PROOF.md | 15302 | `b80c1dd6a5101982c98deb719085425e04ea5229a5f8052e41e92e6a6091fc4a` |
| reproduce/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/verify.py | 21335 | `660ec02ce86b0b84346c7aded071b8c37e3a650f56ec6f9021128f07cc485702` |
| reproduce/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/README.md | 1458 | `95eed2d1ef25c3a9e0cdeb0d291b8ff85558a0997e0d7a325e57149c0c8f88fe` |
| EXPECTED.txt (actual stdout) | 455 | `c08168efaf82b2ffa50d8717f6963acc431935871d593a26323eb88b810671a0` |

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
