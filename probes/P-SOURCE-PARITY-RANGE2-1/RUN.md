# First pinned exact run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn; Apache-2.0.

pin_commit: 55b6472d8b3081dd22f26439f09eb31d2e8dba69
verifier_sha256: 43b2f564b97833d1d222d5a06c429d5f9ebee51f929828af67cd48a95a246aad
command: python3 probes/P-SOURCE-PARITY-RANGE2-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 49001f332e87d27caa8bc286c8804a8a998d663c3d18ef73a6ec434f1d6e74d2
stdout_bytes: 3099
stdout_lines: 29
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The three prospective files were publicly committed and read back byte for
byte before the first scientific execution. The public branch matched the
full pin. Local HEAD, clean worktree and verifier digest were checked before
launch. The exact command ran once with enabled assertions, PYTHONHASHSEED=0,
LC_ALL=C.UTF-8 and a 600-second timeout, with stdout/stderr captured separately.
EXPECTED.txt preserves the first stdout unchanged, including its final LF.

This is one local x86_64 execution. Both scientific dispositions are
INCONCLUSIVE; integrity passed. Later unchanged repository and clean GitHub
x86_64/aarch64 replays are reproduction, not additional selected trials.
Their actual selection and byte-identity evidence will be reported in the
pull request after completion. Same-session checks are not external
independent scientific acceptance.
