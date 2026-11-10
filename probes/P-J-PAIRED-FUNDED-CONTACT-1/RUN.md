# First public-pinned execution

NON-CANONICAL / L1 / exact finite audit.

pin_commit: 378250b8d1477980a330c0f674b4de9a16a9f26c
verifier_sha256: 04eb70e322348d74266b02936c2aa10e82344ae0798bdf2636007d807afe3e71
command: python3 probes/P-J-PAIRED-FUNDED-CONTACT-1/verify.py
platform: Ubuntu 24.04.1 LTS
architecture: x86_64
python: 3.12.3
exit_code: 0
stdout_sha256: a69c115b8a54cdf69137484d956888aa8bc3feed566a07ff83c90b0380ed6e16
stdout_bytes: 1638
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-11-08T23:53:08.218858+00:00
completed_utc: 2026-11-08T23:53:09.701725+00:00

## Custody and environment

The three scientific files were published together at the pin above before
any scientific import or execution. A fresh detached worktree fetched that
public commit. Its worktree was clean, and each of the three actual Git blob
identifiers was checked against the published identifier before execution.
Static source parsing and compilation before the pin were not execution.
The connected account's default author identity was explicitly authorized.

| Source | Git blob | SHA-256 |
| --- | --- | --- |
| PREREG.md | 0d4550e5f4a3618bb7b65ce1d01f16080e45b1d3 | dc3b7b59305fe5557b3380958eaf9efe0027ce6b71a61d634308f7069f59229e |
| PROOF.md | e34061149062402e022e754a81ac5bd5656d0453 | 9d85120a2aaa91dc928c66069b4ac21da6b2af11dce2b710a213cc0e88efc172 |
| verify.py | 7e8bb76d9d21720428d0b6b061136b59cabc42fe | 04eb70e322348d74266b02936c2aa10e82344ae0798bdf2636007d807afe3e71 |

Inherited PYTHON* and TWISTJ* environment variables were removed. The run
set PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC.
Assertions were enabled. The timeout was 600 seconds. Exact stdout was
saved as EXPECTED.txt only after exit zero and empty stderr were observed.
All three scientific sources remain byte-identical to the public pin.

## What this run establishes

The four-coefficient polynomial calculation and five-coefficient cyclic
calculation agree on every audited complete transition and inverse. Both
were written by the same author. This is a cross-check using different
representations, not independently authored or blind confirmation.

The complete map audit includes 36581 cases, counting the specified
repeated examples and forward/reverse finite-stock histories. It also
checks 625 scalar fixtures, 65 pure-J powers and three negative controls.
The inventory, counts, branch counts and exact digests are preserved in
EXPECTED.txt and were fixed as a procedure before this run.

This record claims one actual x86_64 execution. The required GitHub x86_64
and aarch64 jobs are not claimed before completion. Their exact result
head, run, job markers and matching hashes are to be recorded on the pull
request after external readback. Repeated execution is reproduction, not
another independently authored implementation.
