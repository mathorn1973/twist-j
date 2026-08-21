# P-CARRY-QUADRATIC-SYMMETRY-2 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
pin_commit: 288cd914be3b79737af5dff3c0699fdf7e6f1311
verifier_sha256: 6c7fbf48a88d9b29683993849d7e911ba1eda84c2ea07f8552972d89f39e4ca5
command: python3 probes/P-CARRY-QUADRATIC-SYMMETRY-2/verify.py
platform: Ubuntu 22.04.5 LTS; WSL2 Linux 6.6.87.2
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: c99c87a7c7618cc3fbfc3a8ef4a0a5f26290bdf8668d1d291cf8a9bebaa60e21
stdout_bytes: 623
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 5e077db1a33924bbaaeb8498046605a21e1b0a0d
prereg_sha256: 7bbebc3f597434dce1e64cfec7b5062dd504557d3e1f4c3d3ec3bd36a98128c5
prereg_bytes: 11584
prereg_lines: 329
prereg_blob: bc8924857eb288adcb5d22b01c13a251984de2e1
verify_bytes: 9680
verify_lines: 278
verify_blob: 66d8b33900b98d9c906f1cab3d0a41bbc6d7fd55
public_pin_comment: issue 507 comment 5373824547
public_run_comment: issue 507 comment 5373825156
```

Both accepted files were read back from the exact public pin before execution.
Their remote branch SHA, Git blob IDs, SHA-256 hashes, byte counts, and bytes
matched the local pin. Both files have LF endings, no CR bytes, and a final LF.
Three independent static reviews returned no findings after two mathematical
clarifications and one complete-GL-carrier correction were made before the
pin. Static AST parsing passed; the accepted verifier was not executed or
imported before the pin.

The accepted verifier was executed exactly once after public readback. The
process returned zero and wrote empty stderr. `EXPECTED.txt` is the complete
raw stdout with LF endings and final LF. The verifier was not rerun.

## Rejected infrastructure attempt

One preceding shell-wrapper setup attempt lost its temporary-directory
variable and tried to open `/stdout.txt`. POSIX redirection failed with
`Permission denied` before process launch. Python and the accepted verifier
were not started, so this is rejected as an infrastructure attempt rather than
a verifier run. The accepted run used fresh explicit `/tmp` paths and exposed
the verifier process exit code directly.

## Accepted run

```text
checks: 9/9 ALL PASS
decision: THEOREM-CERTIFIED IN THE FROZEN CLASS
direct_boolean_vectors: 2044
direct_widths: every n=2..10
direct_singular_counts: 2,3,5,11,27,63,135,271,527
full_q4_automorphisms: 120
full_q4_induced_permutations: 120
large_boundary_audit: n=8..64
layer: L1 only
```
