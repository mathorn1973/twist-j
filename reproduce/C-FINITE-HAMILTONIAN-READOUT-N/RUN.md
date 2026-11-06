# First author audit

NON-CANONICAL L1 conditional candidate-T. Design exposed, not blind
confirmation. The general statements require analytical review.

- public prospective pin: `0f471eb885b98236449da5566e82f7935468a3ee`
- platform: Linux
- architecture: aarch64
- Python: 3.12.3
- command: `python3 reproduce/C-FINITE-HAMILTONIAN-READOUT-N/verify.py`
- environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC
- verifier SHA-256: `3347c840cf7f4e5f7f7048eb76bbe34e070e9cbb52893045db4e0aa51fb10a5f`
- exit code: 0
- stdout: 655 bytes; SHA-256 `22f4ba04c3a9c98a165efa988a2eb0a6f24c3af72e3a28f8184aebfaa61766c8`
- stderr: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- exact assertions passed: 12628

The code, analytical proof and contract were pushed and read back before this
first execution. It ran in a clean checkout of exactly that pin. The tree
remained clean afterward. No scientific retry, post-run code edit or threshold
change occurred. EXPECTED.txt reproduces the exact first stdout bytes.

The small finite checks cover the stated audit scope, not the complete
1,638,410-gate circuit, a physical spatial implementation, or independent
acceptance of #1746's source/spectral claims. Later identical executions are
reproduction. Cross-architecture evidence must be reported from actual jobs,
not inferred merely from this platform declaration.
