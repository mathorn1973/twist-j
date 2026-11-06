# First pinned exact run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn; Apache-2.0.

pin_commit: c4584bb481e369338c2f90d2c2e7fd4eed3aec54
verifier_sha256: 17206c5fa79a0d9f0f3adbdffc0623e1b58bef930274ca8ba7ab2f3dd5c710c8
command: python3 probes/P-SOURCE-RANGE2-ENERGY-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: d91c1e680b7a081a5cc2c80d4912849fa649cf0f564dffd56e3e4ce38d1d216a
stdout_bytes: 936
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The verifier, PREREG.md and PROOF.md were publicly committed and read back
byte for byte before the first scientific execution. The worktree was clean
at the pin, and the verifier digest was checked before launch. The first
execution used the exact recorded command, enabled assertions,
PYTHONHASHSEED=0 and LC_ALL=C.UTF-8, with stdout and stderr captured
separately and a 600-second timeout. No scientific execution or import
preceded the public pin. EXPECTED.txt is the unchanged first stdout,
including its final LF.

This is one local x86_64 execution. Its scientific disposition is
INCONCLUSIVE for both signs, with all integrity checks passed. Unchanged
repository and required GitHub x86_64/aarch64 replays are reproduction;
their actual selection and byte-identity evidence are reported in the
pull request after completion. Same-session review and reproduction do
not constitute external independent scientific acceptance.
