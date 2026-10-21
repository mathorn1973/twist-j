# First pinned exact run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn; Apache-2.0.

pin_commit: 2c618efc2e28606edb12ada2f77a06aa0d798d55
verifier_sha256: 493db96149dcba94119f273fb3d12e40a7b6a9105b6e36337cc7524e337f3558
command: python3 probes/P-COMMON-HISTORY-FUNDED-RECEIVER-1/verify.py
actual_invocation: python3 -B probes/P-COMMON-HISTORY-FUNDED-RECEIVER-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
start_utc: 2026-10-18T17:46:49.226947+00:00
end_utc: 2026-10-18T17:46:58.407140+00:00
duration_seconds: 9.180219
exit_code: 0
stdout_sha256: e21cd4fc5c84a6349b6b44912027a5c4ef41c12d0b287dfe6faec178abe0457a
stdout_bytes: 602
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The seven pre-run files and public branch ref were fully read back before
this first execution; receipt #1626/6253105699 precedes the run. The worktree
was clean at the pin. No scientific execution or import preceded it. The
command was run once with stdout/stderr captured independently. EXPECTED.txt
contains exactly the resulting stdout bytes, including its final LF.

The policy parser requires the canonical command without interpreter flags.
The actual first invocation above used the preregistered -B flag, which only
suppresses bytecode cache writes. It does not alter this program's scientific
inputs or assertions. The repository replay runs the canonical command.

This is one local x86_64 execution. Required GitHub x86_64/aarch64 replays
and their actual verifier-selection logs will be recorded separately after
they complete. Infrastructure success alone is not scientific replay evidence.
No run of a foreign source/reviewer verifier is claimed.
