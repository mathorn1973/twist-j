# P-TM-SYM2-REVERSAL-CLOSURE-1 formal run record

pin_commit: 00235474b2b826e3f2ddd08bcfde1f42a2a3e6b1
base_commit: d8f91078760ed904ae748883dfe2b8fd98c97af9
branch: probe/P-TM-SYM2-REVERSAL-CLOSURE-1
prereg_sha256: 7c592e5ccd689e314c50fc9020b400ab78320c8ea660bcf35d8c624afbde2c82
prereg_bytes: 12271
prereg_git_blob: a274c5c768784b586c55d78ecd827759b787e1a3
verifier_sha256: 03f5cf7e49b5a03ccb9ee2a0d7383737ab0f84d0d1da7c04a6c4dce481ba77ad
verifier_bytes: 21548
verifier_git_blob: 5f24d02a8698e63bb10c816ac74fe646aa03c3f9
checker_sha256: b34f20b33baeb3711d877a91a7d743f8545210f5b7370b56a5f58d62841e4f8b
checker_bytes: 6250
checker_git_blob: e9a7132ac358e35f0b347c0d8299c0aef8433dd0
source_predefinition_sha256: 557b27c65870f25903b08c8830bfd55c0e91f5caa1221d6f2fedb2ff8e90add1
source_predefinition_bytes: 8125
source_predefinition_git_blob: d9511ffeddb063978bd92039b26eba9e5c6a2838
source_measure1_sha256: 395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f
source_measure1_bytes: 9879
source_measure1_git_blob: b2b3250550dd78af0479db114499392c86812b13
source_semilinear_sha256: 47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19
source_semilinear_bytes: 29205
source_semilinear_git_blob: 7c25fe30b9217719837b30f6ded56599408abfc1
command: python3 probes/P-TM-SYM2-REVERSAL-CLOSURE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-07-23T17:36:54Z
run_finished_utc: 2026-07-23T17:36:54Z
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 687174ea019ba5aa66ad119f581e227ac863e3dbc078312e3d6aa254dab2ea1a
stdout_bytes: 3016
stdout_lines: 41
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 08dc9ddb9d54b18f4992d3459f90baeabdbac54e
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
stderr_lf: 0
stderr_cr: 0
stderr_final_byte: EMPTY
certificate_count: 29
route_count: 1
route: ROUTE: REVERSAL-TOGGLE
translation_N: (0,1)
translation_R: (1,0)
translation_NR: (1,1)
transport_N: NONREALIZABLE
transport_R: NONREALIZABLE
transport_NR: REALIZABLE-E1
extended_orbit_count: 1
extended_orbit_sizes: 48
result: PASS / REVERSAL-TOGGLE
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
public_lock: issue 138
definition_issue: issue 136
definition_pr: PR 137
public_pin_comment: 5061456941
public_run_return: issue comment 5061491530

The formal run used a fresh public clone and a clean detached checkout of
the exact immutable pin. Before process start, the public commit, complete
six-file inventory, verifier and support hashes, architecture, and clean
state were checked. The verifier was invoked exactly once; no deterministic rerun occurred.

`EXPECTED.txt` is the exact 3016-byte LF-only stdout. It contains all 41
lines, has no CR bytes, ends in LF, and has SHA-256
`687174ea019ba5aa66ad119f581e227ac863e3dbc078312e3d6aa254dab2ea1a`.
Stderr is the exact empty byte string.

The complete neutral metadata and exact raw stdout were returned publicly on
issue #138 in comment `5061491530` before these records were created.
Public readback of that comment recovered all 3016 raw bytes exactly,
including 41 LF bytes and the final LF.

All 29 structural and scientific certificates passed. They include the
complete 96-case exact incidence scan, with projective-frame and
RREF-nullspace methods agreeing on every case. The computed route is
`REVERSAL-TOGGLE`: translations are `(0,1)`, `(1,0)`, and `(1,1)` for
N, R, and NR; the N and R transports are nonrealizable over the frozen
field, while NR is realizable at exponent one; the candidate extended
equivalence has one orbit of size 48.

The required first clean GitHub Linux x86_64 replay of the identical pinned
verifier is pending. Merge eligibility requires exit zero, empty stderr,
and byte-for-byte reproduction of `EXPECTED.txt`.
