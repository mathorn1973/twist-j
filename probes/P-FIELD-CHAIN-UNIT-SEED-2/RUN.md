# First execution record

NON-CANONICAL / L1 / candidate-C finite audit under candidate-T written
proofs (PROOF.md). Result-exposed probe, not a blind prediction.
PREREG.md and verify.py were read back byte for byte from the public
pin (issue #1553 receipt) before this first formal run. No source was
changed after the pin.

pin_commit: bc1648745323a8843d2c3cb831b0f585b4e00427
verifier_sha256: 548d0d57d28058651715360385dcfdd1a93a455d30f1314e73a7e4a5d1c81b9c
command: python3 probes/P-FIELD-CHAIN-UNIT-SEED-2/verify.py
platform: Ubuntu 22.04
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: bfaab07056c665a6d5d85d933fc4596fc06cc9d52e5f7cb3535cbda72f92645d
stdout_bytes: 2923
stdout_lines: 53
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-16T20:58:36.076704Z
finished_utc: 2026-10-16T20:58:36.125010Z

Deterministic environment: PYTHONHASHSEED=0, PYTHONUTF8=1,
PYTHONDONTWRITEBYTECODE=1, TZ=UTC. EXPECTED.txt is the exact captured
stdout (LF). This local x86_64 run is one lane; the required pull-request
workflow reruns the same head on x86_64 and aarch64 against the committed
EXPECTED.txt, which supplies the two-architecture gate. No first-run
failure occurred in this successor; the abandoned predecessor's failed
run is preserved in its own record (PR #1552) and is not overwritten.
