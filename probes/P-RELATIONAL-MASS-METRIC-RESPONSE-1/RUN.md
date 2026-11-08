# First formal run

pin_commit: b5c8466118e546f8d93ea2071cb42ef018b6b2b6
verifier_sha256: a7b4c639d8eaad088a1c146a841dc345dc5c911cc28f7cdd7084e3da21f26eba
command: python3 probes/P-RELATIONAL-MASS-METRIC-RESPONSE-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 8d2398f9422160f6a3690c500fa750d15e16e9acd9182de1f01d9ddecdd973bc
stdout_bytes: 466
stdout_lines: 18
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-20T16:21:30.575553+00:00
finished_utc: 2026-10-20T16:23:36.542186+00:00

The first execution followed the six-file public readback receipt on issue
#1684, comment 6295661391, itself read back before execution:
https://github.com/mathorn1973/twist-j/issues/1684#issuecomment-6295661391.
All six complete public files at the full pin matched local bytes and Git
blob identities. The exact-pin worktree was clean. Only analytical proof,
source review, AST parsing and byte/hash checks preceded that receipt;
neither program had been imported or executed and no fixture evaluated.

The primary invoked its independently authored frozen sibling with the same
interpreter and -I, timeout 540 seconds, no shell. It required exit 0,
empty stderr and equality of the complete raw certificate bytes. The
600-second enclosing run completed in 125.967 seconds. The environment set
LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.
The worktree remained clean after execution; EXPECTED.txt is a byte copy
of captured stdout. All six prospective files remain unchanged.

At this first-run record the required x86_64 and aarch64 pull-request
replays are pending. Their exact-head acceptance belongs on the pull
request and does not modify these frozen scientific files or run record.
