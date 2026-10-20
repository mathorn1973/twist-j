# First formal run

pin_commit: 45648ac0d495a55a6c76e90dfd0fe56e042bf224
verifier_sha256: 4e0851457983a344f3ab8d6544b6837abb8df2b06fc89cbd5fad8e4d86f5cd03
command: python3 probes/P-INTEGER-LOCAL-AUXILIARY-NOETHER-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 4049702b5a4f64374dd560a45c51889bd7eefdba4ac6f8f52aeae86bb7e3ebd9
stdout_bytes: 506
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first execution followed the public six-file readback receipt on issue
#1663 (comment 6279633121). The checkout was clean at the exact pin. Before
that receipt only textual derivation/review, source inspection, AST parsing
and byte checks occurred; no scientific fixture was evaluated or imported.

The primary invoked its independently authored frozen breaker using the
same interpreter with -I and a 540-second timeout. Exit zero, empty stderr
and equality of unmodified certificate bytes were required. The enclosing
run used the 600-second repository limit and completed in 30.643 seconds.
LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC were
set. This packaging changes none of the six frozen scientific files.
