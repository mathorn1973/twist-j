# P-GYRON-DISCREPANCY-LOG-3 formal run record

pin_commit: ee06791f7a0a31b28ca1958c62e2abd01a55b456
parent_commit: 1a4ae20d05cd76f93f70b2b011979b22a15fcde7
prereg_sha256: b45c42ad7f169d7c6cd01f1d6e785a5baf6ac46960dfa456d2447cc68c9b59b0
prereg_bytes: 33968
prereg_git_blob: feeb5ed04a6a3bb749ecd470e94e29aaed9d55f7
prereg_lf_cr_nul: 1114/0/0
prereg_final_byte: 0a
verifier_sha256: 10ebef3ffd10067dce0b47b95e58f6ffb8437a2d252eba0510afc39e98bee3ae
verifier_bytes: 92710
verifier_git_blob: 3d7fa53c0f187b5e2f4fe99b0efc45b2267de310
verifier_lf_cr_nul: 2708/0/0
verifier_final_byte: 0a
expected_sha256: ce10ac43276890c4978b189d830b6c989ae31b4e74cb42380a09f845e4a802b4
expected_bytes: 1735
expected_git_blob: 97b55c7212ccc7c1c3466d56c61f738fc4dce299
command: python3 probes/P-GYRON-DISCREPANCY-LOG-3/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 120
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-07-26T21:36:12Z
run_finished_utc: 2026-07-26T21:36:12Z
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
formal_executions: 1
exit_code: 0
stdout_sha256: ce10ac43276890c4978b189d830b6c989ae31b4e74cb42380a09f845e4a802b4
stdout_bytes: 1735
stdout_lines: 34
stdout_cr_bytes: 0
stdout_nul_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 97b55c7212ccc7c1c3466d56c61f738fc4dce299
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
gate_a: PROOF-SURVIVES
gate_b: PROOF-SURVIVES
gate_c_local: AUDIT-PASS
theorem_a: PROOF-SURVIVES
theorem_b: PROOF-SURVIVES
run_integrity: PASS
scientific_decision: PROOF-SURVIVES
route: PROOF-SURVIVES
counterexample: NONE
diagnostic: NONE
native_aarch64_leg: PASS
cross_architecture_gate: PENDING
x86_64_replay: PENDING
public_status: UNCHANGED
public_lock: issue 171
public_pin_comment: 5085492841
public_readback_comment: 5085499764
public_authorization_comment: 5085500991
public_run_return: 5085509668

The initial public pin contains only `PREREG.md` and `verify.py`. Both files
were fetched back from the public GitHub contents endpoint at the exact pin
commit. Their remote Git blobs, SHA-256 values, byte counts, LF/CR/NUL
counts, and final bytes matched the local files exactly before execution.

The formal run used a fresh public clone and a clean detached checkout of the
immutable pin. The runner established native Linux/aarch64, the exact commit,
the two pinned file identities, the frozen environment, and a clean worktree
before invoking the verifier. The verifier was invoked exactly once. The
checkout remained clean and both pinned SHA-256 values were unchanged after
the invocation. No retry or same-architecture rerun occurred.

`EXPECTED.txt` is the exact 1735-byte stdout returned publicly on issue #171
in comment `5085509668`. It contains 34 LF bytes, no CR or NUL bytes, ends in
one LF, and has SHA-256
`ce10ac43276890c4978b189d830b6c989ae31b4e74cb42380a09f845e4a802b4`.
Stderr is the exact empty byte string.

The sole native aarch64 leg passed with Gate A and Gate B both
`PROOF-SURVIVES`, local Gate C `AUDIT-PASS`, and overall route
`PROOF-SURVIVES`. This is not yet the completed external Gate C. The first
clean GitHub Linux/x86_64 replay of the byte-identical pinned verifier is
pending and must reproduce `EXPECTED.txt` byte for byte before the
cross-architecture gate can pass.

No Canon, registry, frontier, dependency, gate, status, release, or authority
file is changed by this run record.
