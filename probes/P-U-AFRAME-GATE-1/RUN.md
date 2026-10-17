# First run

PUBLIC / NON-CANONICAL / L1. Issue #1550.

```text
pin_commit: 7b06ea6b377930f6edeb84cb330b9d69f1b82c51
verifier_sha256: d9fe50b340e527f08003dcaaacab8d798a5d3b306157f48aa189fbd67d0743a0
command: python3 probes/P-U-AFRAME-GATE-1/verify.py
platform: Ubuntu 22.04 (Linux, glibc 2.35)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 9be841f9aeb89c9962ea43387d52d8d9cc9aca3b74e2d916824e6607deff8e36
stdout_bytes: 1295
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Before this first scientific execution all six initial files were fetched
from the public ref and compared byte for byte, and the pin receipt was
posted in #1550. The run used a fresh clone checked out detached at the
pin with a clean worktree, environment LC_ALL=C LANG=C TZ=UTC
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1. INPUTS.sha256 verified all
five custody files. One default run; no frozen input changed, no rerun.

The required v102 release-event check had succeeded before the pin.
Required public x86_64/aarch64 replay is pending at this first-run record.
