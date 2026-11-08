# First formal run

pin_commit: e330ac7cbc715c0cd809483aac0f2277fb657118
verifier_sha256: e7998014b8511614fac3dc419979feeefb73260b2ba16a3282517b81528e1cce
command: python3 probes/P-INTEGER-SCALAR-LAPSE-RIGIDITY-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 047384f51d04ad9da329031b1a12fe116075da2b047f6c04f4d25c273999a661
stdout_bytes: 551
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first execution followed the public six-file readback receipt on issue
#1665 (comment 6279840863), itself read back before execution. The checkout
was clean at the exact pin. All public bytes and Git blob IDs matched the
local frozen files. Before that receipt only analytical derivation, textual
review, source inspection, AST parsing and byte checks occurred; neither
scientific program was executed or imported and no fixture was evaluated.

The primary invoked its independently authored frozen breaker using the
same interpreter with -I and a 540-second timeout. It required exit zero,
empty stderr and equality of unmodified certificate bytes. The enclosing
run used the 600-second repository limit and completed in 2.955 seconds.
LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC were
set. The worktree was still clean immediately after execution. EXPECTED.txt
is a byte copy of captured stdout. None of the six frozen files changed.
