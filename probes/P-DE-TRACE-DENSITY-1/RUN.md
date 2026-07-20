# RUN. P-DE-TRACE-DENSITY-1

pin_commit: 595822545f007acb24a5d50467a5d8bfa5fe8718
base_commit: 9009a54d85672e9fca7e8356706f850bedc9c765
prereg_sha256: 0f45fe1937f7e0ed945f48c20d554b8a71e8b247f785092df65610dc4a2bd82a
verifier_sha256: 7eaca91f6c3d73830f86750f142e910f2fd38e404821eeaeb3ac43f16c6e2188
break_verifier_sha256: 658f05edb2d66428af8a7bf24907cee3b25bfacdd33c6d5cb21bcca219a824af
command: python3 probes/P-DE-TRACE-DENSITY-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04
architecture: aarch64
python: 3.12.3
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
exit_code: 0
stdout_sha256: 62127bf909d1d50624f77d744905f3c99287db816365a27b5ef458f3fddec0c5
stdout_bytes: 3313
stdout_lines: 53
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: NONUNIQUE 21/21 ALL PASS
public_lock: issue 101

Break path executed under the same environment: exit 0, stdout SHA-256
`9f0b08587543bdba48bb1d87759b2914a5a9dbdee4213e73f72b2ae1ab62fd36`,
result line: BREAK ATTEMPT FAILED. NONUNIQUE STANDS.

Cross-platform witness: the same verifier bytes previously produced the same
stdout hash on an independent x86_64 platform (Ubuntu, Python 3.11.15), per
the provenance disclosure in PREREG.md. The required GitHub x86_64 check at
PR time is the remaining gate; byte identity with EXPECTED.txt is required.
