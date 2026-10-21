# First formal run

pin_commit: f19fa98dc1634ce1e17b9dec402c51920d2bea8d
verifier_sha256: 64fa4fd8198d778185d5c5e4cd7429accfc2f2d002bf284746ffbc7df922e104
command: python3 probes/P-RELATIONAL-MASS-JOINT-ACTION-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: a59dd2310ae9f3bface7a738c561a7290d9fe4af2e4d39a5f048b771f1ca2642
stdout_bytes: 431
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-20T16:54:33.441922+00:00
finished_utc: 2026-10-20T16:55:06.454291+00:00

The first execution followed the complete six-file public readback and
issue #1686 receipt 6296327470, which was itself read back before execution:
https://github.com/mathorn1973/twist-j/issues/1686#issuecomment-6296327470.
All public file bytes and Git blob identities matched the committed pin.
The exact-pin worktree was clean before and after the run. Only analytical
derivation, source review, AST parsing and byte/hash checks preceded the
receipt; neither program had been imported or executed and no finite
fixture had been evaluated.

The primary invoked its separately authored frozen sibling with the same
interpreter and -I, no shell, a 540-second timeout and a fixed minimal
environment. It required exit zero, empty stderr and raw certificate byte
identity. The enclosing 600-second run completed in 33.012 seconds. The
environment set LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and TZ=UTC. EXPECTED.txt is an exact copy of captured stdout.
All six prospective files remain unchanged.

At this first-run record, required x86_64 and aarch64 PR replays are pending.
Their exact-head acceptance belongs on the pull request and does not alter
this historical run record or the frozen scientific files.
