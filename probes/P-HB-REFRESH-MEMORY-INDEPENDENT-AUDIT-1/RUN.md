# First exact run: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: bda14aabb495be1db5790c86b6a68d6721cb1fab
verifier_sha256: 01923a20d10472c502604b8542a8cb553f48f502fc3a4228be7718cd47ecddee
command: python3 probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1/verify.py
platform: POSIX-compatible Python 3.12 runtime (x86_64)
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: b102ec4e67f71aeea94db2b0e716497d505fadf254f8de5874f3e4ba50a80224
stdout_bytes: 628
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

First execution started `2026-10-16T22:29:50.461509+00:00` and ended `2026-10-16T22:29:52.321644+00:00`; elapsed `1.860780` seconds, timeout `600` seconds, no timeout. The checkout was clean before and after the run at the publicly read-back pin commit `bda14aabb495be1db5790c86b6a68d6721cb1fab` (sole parent `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, Public Canon v102). All seven pinned files passed `INPUTS.sha256` verification in `STAGE custody PASS files=7 sources=14`. The command ran from the repository root with `LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, `TZ=UTC`. `EXPECTED.txt` is the unedited 628-byte stdout.

The run completed the frozen false-target reporting path (`exit_code: 0`, `stderr_bytes: 0`, `VERDICT SCIENTIFIC_FAIL`): Stages 1–3 (`custody`, `geometry_and_operators`, and all `7130` exact coefficients of `refresh_identities_target1`) passed, and in Stage 4 (`rank_minors_and_criteria_target2`) both `det3` (`-3/5248800`) and the factored `det4-target` (`(3/5)*(-1/(10*324))*(-1/(10*324^2)) = 1/5668704000`) passed, after which the redundant hand-multiplied literal assertion `det4-value` (`Q(3, 1698693120000)` instead of `Q(3, 17006112000) = Q(1, 5668704000)`) fired, leaving `far_counterexample_target3` and `finite_contact_predictor_target4` as `NOT_RUN`. See `RESULT.md`.
