# Actual scientific execution

NON-CANONICAL L1, one actual architecture. The code and preregistration were
published and read back before execution. No scientific code was changed.

pin_commit: 760157f57495fb87059b3a8a8e7943be7d0793c1
command: python3 verify.py
prereg_sha256: 8230209a8727d6e7eb9ab71a4e40bef816864ef7d01bdfcf78e195176d1ae8a8
source_sha256: 80696dbadecd21e06c39505a71c6e8215c0f57db17d8f452f6ba77274fad77ec
verifier_sha256: 82c31a1e2fe9329ec4fe614d1ba42de6f454f3969d3071ce371aae84e411f8e4
platform: Linux
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_bytes: 1057
stdout_sha256: d96fda0d3800e8546dc20ebe564717475d5cf543ce8bd30a1e262dc39e716e0e
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Environment: PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, TZ=UTC,
LC_ALL=C.UTF-8. ACTUAL.txt is the captured stdout, not a manually invented
expected transcript. Standard library only. No failed scientific run occurred.

## Execution-lane disclosure

PREREG.md planned one x86_64 run. That planned lane was NOT executed: public
raw-file retrieval in the local environment was unavailable. The exact frozen
repository bytes were instead executed on Linux aarch64, Python3.11.2, as
recorded above. The plan is not retrospectively rewritten. Architecture was
not a numerical pass/fail predicate of this notes-only candidate, and no
architecture-based theorem credit is claimed. There is only ONE scientific
run, not two architectures. Repository checks on other machines are not an
additional scientific lane. The mathematics and failure thresholds did not
change with this execution-location decision.

The integer full-matrix certificate calculation is distinct from the rank-one
application inside this same test suite; it is NOT a blind independent agent.
General conclusions are supported by PROOF.md. Ordinary PR CI checks policy
and integrity and does not execute notes-only verify.py.
