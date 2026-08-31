# P-C8-MARKING-RIGIDITY-2 formal run record

pin_commit: 0a197f8d8b0407783241365454365e096b37470e
base_commit: 43cfd9e4ca570a51f9aa548a8b0e61dad45f5b7f
public_lock: issue 731
prereg_sha256: bd9356d3c15348269e6342cec1c46928c15795cb4a29d86bb2dc3d8588670745
prereg_bytes: 6373
verifier_sha256: c31684c7711e45064ecd06238f6b9a90b207819b8572ccdbfcc435dc86963db3
verifier_bytes: 7913
command: python3 probes/P-C8-MARKING-RIGIDITY-2/verify.py
environment: env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: CPython 3.13.5
clean_checkout: exact frozen PREREG.md and verify.py bytes materialized from the public pin; Git blob identities matched remote readback
architecture_gate: PASS; GitHub workflow run 33413792559 reproduced EXPECTED.txt on architecture-x86_64 and architecture-aarch64; aggregate check SUCCESS; publication SKIPPED
local_leg_scope: exact x86_64 reproduction only; the public two-architecture gate rests on the workflow's distinct x86_64 and aarch64 jobs
deterministic_executions: 1
exit_code: 0
stdout_sha256: 906b2bdc60e70cc4d225606609449f81c34dbb471c75b0045ac59cd3c80fc7e6
stdout_bytes: 766
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 6/6 ALL PASS
pinned_files_unchanged_after_execution: yes

The accepted verifier was executed exactly once after public pin readback. The public pull-request workflow independently replayed the same committed verifier and exact EXPECTED.txt bytes on both required architectures.
