# First author audit

NON-CANONICAL L1, design-exposed exact audit, not a blind confirmation.

- prospective pin: `22a907f2d16cffc9b6f9e139fdc43fdc92c8b179`
- platform: Linux
- architecture: aarch64
- Python: 3.12.3
- command: `python3 reproduce/C-THERMAL-LAUNCH-CAPACITY-N/verify.py`
- deterministic environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC
- verifier SHA-256: `f06ed5fb2177cc6eb99015d449ccf793a6da8be9e8b998dda3fbe62693e0835e`
- exit: 0
- stdout: 2378 bytes, SHA-256 `633e4ce8dc7a4e21f8502d851abfb84890f36b250bb0cf6d34ca17392a29d8c8`
- stderr: 0 bytes, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- assertions: 33360

The public pin was pushed and read back before this first scientific execution.
The tree was clean before and after. There was no scientific retry or code/
threshold repair. The unguarded relaunch is an intentionally frozen negative
control and was detected. Exact general claims rest on PROOF.md, not finite
example extrapolation. Same-code replay is reproduction, not independent code.
