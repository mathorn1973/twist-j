# First exact run: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: 453e4404bf987f7b5747b5bb59351ee459dade7f
verifier_sha256: bade1858b42487b79668d7b5f0864b7b1dd1ab17f0faf01dfe337699bd642b33
command: python3 probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2/verify.py
platform: POSIX-compatible Python 3.12 runtime (x86_64)
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: 4c439ab5d11b078564fee62125abedfe7abbeb02aefaca38cbff99d982be0c7c
stdout_bytes: 759
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

First execution ran on clean checkout at the publicly read-back pin commit `453e4404bf987f7b5747b5bb59351ee459dade7f` (sole parent `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, Public Canon v102); elapsed `10.712` seconds, timeout `600` seconds, no timeout. All seven pinned files passed `INPUTS.sha256` verification in `STAGE custody PASS files=7 sources=17`. The command ran from the repository root with `LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, `TZ=UTC`. `EXPECTED.txt` is the unedited 759-byte stdout.

The run completed the frozen false-target reporting path (`exit_code: 0`, `stderr_bytes: 0`, `VERDICT SCIENTIFIC_FAIL`): Stages 1–5 (`custody`, `geometry_and_operators`, `refresh_identities_target1`, `rank_minors_and_criteria_target2`, and `far_counterexample_target3`) passed completely, and in Stage 6 (`finite_contact_predictor_target4`) all `50` signed-source constants, all `70500` wave-work linear coefficients, all `2000` single-contact guarded cases, and all `480` two-contact guarded cases passed every predictor and conservation check, after which the post-loop regime-coverage assertion `missing-two-kind-zero_cost_accept` fired because the first source pair in `source_pairs` had been written as `((0, 3), (2, 4))` instead of `((0, 4), (2, 4))`. See `RESULT.md`.
