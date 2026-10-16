# First exact pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: 0803c167d5e903a216b3cd96d9f7c6fcf4e62345
verifier_sha256: 65ec7e05b0b6c6089be5424cff33efd163967e1dced6b4c50bed6119209173fa
command: python3 probes/P-TWO-USE-READOUT-FAILURE-REGRESSION-2/verify.py
platform: Darwin
architecture: aarch64
python: 3.13.13
exit_code: 0
stdout_sha256: 5bc83612d7364bd85c5b967a3187a96d0228f604f7bc994605a39670574e8f08
stdout_bytes: 3631
stdout_lines: 22
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Public pin/readback receipt: https://github.com/mathorn1973/twist-j/issues/1526#issuecomment-6198956479

Run from the clean pinned repository root after remote byte-for-byte readback of all 5 pinned files (`CODE_SHA256SUMS`, `PREREG.md`, `PROOF.md`, `SOURCES.tsv`, and `verify.py`) at `0803c167d5e903a216b3cd96d9f7c6fcf4e62345`, with `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`. All 4 local pinned files and all 19 upstream `SOURCES.tsv` records (`probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/` and normative repository files at `b79143fb00839b870686f6cea34e174959060df1`) were byte-identical before and after execution. `EXPECTED.txt` is the exact captured stdout (`3631` bytes, `22` lines). No scientific or pinned file was modified after the pin.
