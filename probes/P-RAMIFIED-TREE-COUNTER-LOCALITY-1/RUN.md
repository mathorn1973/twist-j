# Formal local run

pin_commit: 8666200ef2b8680885c113e40a19061681e04193
base_commit: af8dc5956e26917b265fd0070f500c841c326512
public_lock: issue 1296
pin_custody: issue comment 5891512443
command: python3 probes/P-RAMIFIED-TREE-COUNTER-LOCALITY-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
prereg_sha256: 5f2a073e1ce66d2492e842a7853f05319d1deb27fc02bec0bfbd834f4a7cb589
prereg_bytes: 11282
prereg_git_blob: d380ea8babe053135e852cb83772dbe47d3b2237
proof_sha256: 3a059dbd70dc8b42bb95809f378628f869eb131ad6169ba87515bb41541db767
proof_bytes: 19659
proof_git_blob: da44a1935bec0713664ec4cb63c5fdb104149779
verifier_sha256: cfd8137b9a2a50a373e48521f99e20b24793f3b374763ca00213d374176c7fa4
verifier_bytes: 10816
verifier_git_blob: 829d6b3a0be57dfda09a5419ca6e48d4c2d24cf3
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 4a81ca12c12fe7c7856d3d175c9190d9453b36a3a44cbf256f35df7470b1d5a1
stdout_bytes: 962
stdout_lines: 31
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
run_started_at: 2026-09-29T13:42:07.696860+00:00
run_finished_at: 2026-09-29T13:42:09.101384+00:00
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
stdout_cr_bytes: 0
stdout_final_byte: 0a
result: RAMIFIED-TREE-TRANSPORT-BOUNDARY; VERDICT PASS

The accepted preregistration, proof and verifier were read back from the public
Git tree before this first scientific execution. Exact stdout and empty stderr
were captured outside the clean worktree; only the stdout is retained here.
No frozen file changed. Platform descriptors are neutral metadata.

The local leg is x86_64. Required GitHub x86_64 and aarch64 jobs independently
replay the same verifier against EXPECTED.txt at the pull-request head. Their
public run records supply the separate architecture gate; no unobserved CI
result is asserted by this local record.
