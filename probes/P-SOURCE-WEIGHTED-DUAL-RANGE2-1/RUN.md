# First pinned exact run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn; Apache-2.0.

pin_commit: b5ebcd6276d538710d3ff19534b67e46a04bda18
verifier_sha256: c637973a805bddbf38071d3e758416454ca7bd3821bd074d72d08640993c46ad
command: python3 probes/P-SOURCE-WEIGHTED-DUAL-RANGE2-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 33a03e3b6a194dde05bb9e132e05fde5244792cd4a3a36aaa0f3b4e102301fbd
stdout_bytes: 28742
stdout_lines: 381
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The three prospective files were committed, pushed and publicly read back
byte for byte before the first scientific execution. The branch ref matched
the pin; local HEAD, clean worktree and accepted verifier hash were checked
before launch. The exact command ran once with enabled assertions,
PYTHONHASHSEED=0, LC_ALL=C.UTF-8 and a 600-second timeout. Stdout and stderr
were captured separately. EXPECTED.txt is the unchanged first stdout,
including its final LF. The first run completed in approximately 143 seconds.

This local x86_64 run completed all 66 fixed comparisons: 31 certified
obstructions and 35 inconclusive cases. Both source-sign aggregates are
CERTIFIED_OBSTRUCTION. No early stop or post-pin change occurred.
Subsequent unchanged repository and GitHub x86_64/aarch64 replays are
reproduction, not new selected trials. Their actual verifier-selection and
byte-identity evidence are reported in the pull request after completion.
Same-session authoring and review are not external independent acceptance.
