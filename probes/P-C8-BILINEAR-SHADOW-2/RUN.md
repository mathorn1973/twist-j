# P-C8-BILINEAR-SHADOW-2 formal run record

issue: https://github.com/mathorn1973/twist-j/issues/124
issue_created_at: 2026-07-22T17:25:05Z
pin_public_at: 2026-07-22T17:40:23Z
run_started_at: not recorded by the aarch64 runner
run_finished_at: not recorded by the aarch64 runner
pin_commit: 908e0908eea2d8f16c23c1ae00fa11d122430984
base_commit: 8445b59c3555f15e167d6769edb3c85b8ba6404e
prereg_sha256: bac41f2e407b06f5ba23ee39495ff7fd9c9529cae0608d06159a36a2118ce48f
prereg_bytes: 9003
verifier_sha256: 3c293b6571c1cf29702d28d531a789bddde11c695ce079f6ba7fe1a2b4c270ce
verifier_bytes: 6541
command: python3 probes/P-C8-BILINEAR-SHADOW-2/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
clean_checkout: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 4d8f82068cae33fedd704b68c2e4e848b0c9e206f5d64f4731f3766687041ad0
stdout_bytes: 942
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: RESULT 6/6 ALL PASS
known_predecessor_stdout_sha256: cc194c8da06d4873d6b279bbc658d2aade71be70dfa877dbdb0ab892d15c3a62
predecessor_output_match: no; the repaired verifier has deliberately changed labels and audit coverage

The runner fetched the public branch, confirmed its tip was the exact public
pin, checked out that commit in a clean detached worktree, and verified the
public PREREG and verifier hashes and byte counts before execution. This was
the first execution of the `-2` verifier. The only pre-execution operation
reported after the pin was a successful static `py_compile` check; no import
or run preceded the formal command. The verifier was executed exactly once
with the command and environment above. Its raw LF stdout is `EXPECTED.txt`;
stderr was empty.

The runner could not read the public handoff comment in that session and did
not retain exact UTC start and finish timestamps. This omission is disclosed
explicitly. Those timestamps are not a field required by `POLICY.md`,
`AGENTS.md`, `tools/check_verifier.py`, or the frozen pass threshold; no gate,
hash, byte count, platform field, or execution count is reconstructed.

Only neutral platform descriptors are recorded. The protocol-invalid
`P-C8-BILINEAR-SHADOW-1` transcript is disclosed for comparison but is not
formal evidence for this probe.
