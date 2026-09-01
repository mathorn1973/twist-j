# RUN

## Immutable pin

pin_commit: fe74bf9d9cc8666b569d4618efd2149215c19c3d
verifier_sha256: 6c55ef8162c2c9f96088dbe084a32c0619660f87143c687907b34422dcbbc03a
command: python3 probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/verify.py

## Local execution record

platform: Linux
architecture: x86_64
python: Python 3.13.5
exit_code: 0
stdout_sha256: a15a0aed27d6a6c5bd54d4707c9ae6a8ebd6874d470b04c3d53ab04b81eb0ec3
stdout_bytes: 683
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The written proof in `PREREG.md` owns the general reversibility and ergodicity
claim. This run is a deterministic finite audit of the frozen implementation
and small-lattice cycle ranks. It has zero phase-evidential weight. The public
CI must independently rerun the pinned verifier on both required architectures.
