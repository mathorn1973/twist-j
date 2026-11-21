# Execution record

The [public readback of all 18 frozen files](https://github.com/mathorn1973/twist-j/issues/2027#issuecomment-6976937363) preceded execution. The main verifier builds four C++20 programs with g++ 11.4 and uses exact Python ring arithmetic for the independent trajectory comparisons, binary constructor and sparse controls. The live and measured runs are separately reversible.

```text
pin_commit: 6129a14896af5e456fa55a482f7349f425a36812
command: python3 probes/P-H3-THIRD-CELL-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 31d9a1bb8c83f938512086fb9fde8c20c2cb00b04e9e9c3c6d3075532d7a72c3
started_utc: 2026-11-18T11:14:43.096173+00:00
ended_utc: 2026-11-18T11:15:01.984262+00:00
exit_code: 0
stdout_bytes: 51804
stdout_lines: 7
stdout_sha256: 5b7d773d9d80f636128911ad83b363a5e0d246944b5e37ee041a6fbf0724bcf2
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The seven JSON lines in [EXPECTED.txt](EXPECTED.txt) cover the inputs, causal histories, inverse-based preparation, unchanged natural writes, donor relocation, compact binary switch and sparse families. The C++ comparison covers 409,600 primary live ticks plus the three types of controlled histories. Its first coefficients and events were compared against 285 Python records, within the shared 512-tick window. Python also confirmed ten selected natural encounter pairs. The coordinates of the matched 6303 witness were replayed separately from both initializations.

After the primary run, a second implementation of the compact switch and a short original-worker trace were added as supplementary evidence. From the root run `python3 probes/P-H3-THIRD-CELL-1/followup.py`. Its stdout has SHA-256 `bb2aae05999341316da27c9bed5f774d4745a45dfadbbc5e83a09ec3b14cf8aa` (Linux x86_64). It checks the four-coordinate C++ dynamics against the two-tick predictions for all 340 signed launches, including the inverse of each preceding tick. It also displays how long the 181 material word persists and when differences first reach radiation at 28 and 29.
