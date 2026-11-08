# First formal run

pin_commit: 79d2247fd8e6937347e367b922de1c6e24a54cb4
verifier_sha256: dca77be0c45671fcd2c78f6873bc8970984a93839475170a230d0873df0b7fae
command: python3 probes/P-RELATIONAL-MASS-STABLE-BINDING-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: cefaf22c7a6112835ccf1e4b4114e3b8ac0393445c7df7d6fa6c9582efef33ec
stdout_bytes: 455
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-20T17:29:56.537967+00:00
finished_utc: 2026-10-20T17:30:48.826110+00:00

The first execution followed complete six-file public byte/blob readback
at the immutable pin and receipt #1688 comment 6297016370, created at
2026-10-20T17:29:48Z. The receipt itself was read back before execution:
https://github.com/mathorn1973/twist-j/issues/1688#issuecomment-6297016370.
The exact-pin worktree was clean before execution. All six prospective
files were unchanged after the completed run; post-run records were
written only after completion.
Only analytical derivation, source inspection, AST parsing and byte/hash
checks preceded the receipt. Neither program was imported or executed,
and no finite scientific fixture was evaluated before the pin receipt.

The primary invoked its separately authored frozen sibling with the same
interpreter and -I, no shell, closed standard input, captured output/error,
a fixed minimal deterministic environment and a 540-second timeout.
It required exit zero, empty stderr and raw certificate byte identity.
The enclosing 600-second run completed in 52.288 seconds. Its environment
set LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.
EXPECTED.txt is an exact copy of captured stdout. All six prospective
files remain unchanged. No scientific rerun was used to edit this record.

At this first-run record, required public x86_64 and aarch64 replays are
pending. Their exact-head acceptance belongs on the pull request and does
not alter this historical run record or the frozen scientific files.
