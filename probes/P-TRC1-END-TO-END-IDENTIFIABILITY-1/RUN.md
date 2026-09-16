# First pinned run

NON-CANONICAL. First scientific execution followed public source-byte readback.

pin_commit: 72c6d70a97c80bb5d4a03ae4c1b9f03d7d6aaa28
verifier_sha256: b33afa443896ae2d394fc1b4134497ffaa7b33ea7c331f8557599381f96db3f9
command: python3 probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/verify.py
platform: Linux
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: d4d23bda513d680a01f63f8ef8e354ce41916ca4776e9b1ecaa14bb44d3ed3b1
stdout_bytes: 4538
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Environment: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Elapsed seconds: 6.50438660295913.

## Accepted source bytes

| File | SHA-256 |
| --- | --- |
| PREREG.md | e1d2118629b5185fb47c87ab95cc13a6a7f4b154e9b92118131ea4a4aa5d357e |
| PROOF.md | 9c013feb7f1d52a9125102a4aa29356e7a2e49a27b89a41d9b87adc4a95b2d42 |
| chain.py | d6f23db8a6f28ee6b90e2544a71608e2f320770046ecdeea94418d0f64468a99 |
| verify.py | b33afa443896ae2d394fc1b4134497ffaa7b33ea7c331f8557599381f96db3f9 |

Public readback at the full pin also compared the three inherited executable
engines and both TRC1 specification files listed in PREREG.md. All bytes matched.

The deterministic audit completed with PROOF_AUDIT_PASS, 52,401 checks and zero
failures. EXPECTED.txt is the exact first stdout, including its final newline.
No scientific source was amended after the pin. This record claims only the
local Linux x86_64 execution; independent architecture results belong to CI.
