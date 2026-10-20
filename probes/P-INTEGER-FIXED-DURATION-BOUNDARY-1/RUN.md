# First formal run

pin_commit: 02ec973ecb77655e83d69b990ba22bef05df3424
verifier_sha256: f0ea3b20a7dbb5b883440e660cc4ea324344a8f6cb3e35a6db6e16f7f90f1a0f
command: python3 probes/P-INTEGER-FIXED-DURATION-BOUNDARY-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 97c9586085d4c113d1edac67889c6389122eb2d515c2d0f6447223c36cefda40
stdout_bytes: 461
stdout_lines: 18
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-20T00:00:29.777932+00:00
finished_utc: 2026-10-20T00:00:31.143338+00:00

The first execution followed the public six-file readback receipt on issue
#1668, comment 6280031996, itself read back before execution:
https://github.com/mathorn1973/twist-j/issues/1668#issuecomment-6280031996.
All six complete public files at the full pin matched local bytes, SHA-256
and Git blob identities. The exact-pin worktree was clean. Only analytical
derivation, source review, AST parsing and byte checks preceded the receipt;
neither scientific program had run or been imported and no fixture had
been evaluated.

The primary invoked the independently authored frozen breaker with the
same interpreter and -I, timeout 540 seconds. It required exit 0, no stderr
and equality of raw certificate bytes. The enclosing limit was 600 seconds;
the complete run took 1.366 seconds. The environment set LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. The checkout remained
clean after the run. EXPECTED.txt is a byte copy of captured stdout.
None of the six frozen files changed.

At this first-run record, required x86_64 and aarch64 pull-request replays
are pending. Their exact result-head records belong on the pull request;
they do not alter the frozen scientific sources or this first-run record.
