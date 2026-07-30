# P-TM-SYM2-SEMILINEAR-GAUGE-1 formal run record

pin_commit: 3d3521fe1ed557cc0b2c271baea9a67787aa7951
base_commit: 87c1a0a42a23ad68612cabcddd1c91fd784c9150
prereg_sha256: 034a2da5c56036700cea2e166f7b4c7306da2f12ddee863ab2cdce1c4de38d5a
prereg_bytes: 16719
prereg_git_blob: 1f39dc22566ef31386738779303b465c4be3f960
verifier_sha256: f526af796e0fd2951d5b136b17f786045a932214744040dfd0b86e47c50b3590
verifier_bytes: 49641
verifier_git_blob: ff48eb78ffa2b25ad1abd62cb83eb23163289631
checker_sha256: 4f3aa42695b96a7f79170401a8e56180820358ece146a858520afcf5ca549724
checker_bytes: 18954
checker_git_blob: f20b8f97b8ddad39f93c46fe99c3f5735f30409c
source_predefinition_sha256: 9f5dfe902bb0ff9fc19c4bdc4fb1095301a55bd00201f770ab81a36899c2273f
source_predefinition_bytes: 25896
source_predefinition_git_blob: f8ac57bc5d85505615fd03edaf341446dd2ba976
source_measure1_sha256: 395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f
source_measure1_bytes: 9879
source_measure1_git_blob: b2b3250550dd78af0479db114499392c86812b13
command: python3 probes/P-TM-SYM2-SEMILINEAR-GAUGE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-07-23T12:30:34Z
run_finished_utc: 2026-07-23T12:30:39Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19
stdout_bytes: 29205
stdout_lines: 146
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 7c25fe30b9217719837b30f6ded56599408abfc1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
case_table_sha256: ce9252a773ac3f05425d62afa81d2ea6016b29461adf8e29f2eede52f53d6289
accepted_realizations: 24
route_count: 1
route: ROUTE: SEMILINEAR-DOUBLE
gamma_sl_order: 24
exponent_one_count: 12
coset_character: (1,1)
residual_invariant: chi_Q chi_F
selector_orbit_count: 2
selector_orbit_sizes: 24,24
result: PASS / SEMILINEAR-DOUBLE
architecture_gate: PASS
public_lock: issue 134
public_pin_comment: 5058369843
public_run_return: issue comment 5059483579
x86_workflow_run: 30015742345
x86_workflow_job: 89235142494
x86_tested_merge_commit: 4c1b0d4278b0b6357a6b3d39b23a311c92429952
x86_platform: Ubuntu 24.04.4 LTS
x86_runner_image: ubuntu-24.04 20260714.240.1
x86_runner: 2.336.0
x86_python: CPython 3.12.13
x86_architecture: x86_64
x86_exit_code: 0
x86_stderr_bytes: 0
x86_verifier_sha256: f526af796e0fd2951d5b136b17f786045a932214744040dfd0b86e47c50b3590
x86_stdout_sha256: 47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19
x86_byte_identity: PASS

The formal run used a fresh public clone and a clean detached checkout of
the exact immutable pin. Before process start, the public commit, complete
five-file inventory, verifier and support hashes, architecture, and clean
state were checked. The verifier was invoked exactly once. No Studio
execution and no deterministic rerun occurred.

`EXPECTED.txt` is the exact 29205-byte LF-only stdout. It contains all 146
lines, has no CR bytes, ends in LF, and has SHA-256
`47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19`.
Stderr is the exact empty byte string.

The complete neutral metadata and exact raw stdout were returned publicly on
issue #134 in comment `5059483579` before these records were created.
Public readback of that comment recovered all 29205 raw bytes exactly,
including 146 LF bytes and the final LF.

The structural certificates passed. The complete 96-case table has SHA-256
`ce9252a773ac3f05425d62afa81d2ea6016b29461adf8e29f2eede52f53d6289`.
There are 24 accepted realizations: the 12-element exponent-zero group and a
12-element exponent-one coset with common character `(1,1)`. The resulting
effective semilinear image has order 24 and two free selector orbits of size
24. The residual two-orbit invariant is `chi_Q chi_F`.

The first GitHub Linux x86_64 pull-request replay used the identical pinned
verifier at tested merge commit
`4c1b0d4278b0b6357a6b3d39b23a311c92429952`. Workflow run `30015742345`,
job `89235142494`, exited zero with empty stderr and reproduced
`EXPECTED.txt` byte for byte. Together with the sole formal aarch64
execution, the required two-architecture computation gate is PASS.
