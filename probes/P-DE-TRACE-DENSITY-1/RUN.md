# RUN. P-DE-TRACE-DENSITY-1

```text
pin commit   5958225 (PREREG.md, verify.py, break_de_trace_density_1.py,
             committed before the public execution recorded here)
platform     Ubuntu 24.04 aarch64, Python 3.12.3
environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
invocation   python3 probes/P-DE-TRACE-DENSITY-1/verify.py   (from repo root)
exit         0
stdout       EXPECTED.txt, 3313 bytes, SHA-256
             62127bf909d1d50624f77d744905f3c99287db816365a27b5ef458f3fddec0c5
files        PREREG.md  0f45fe1937f7e0ed945f48c20d554b8a71e8b247f785092df65610dc4a2bd82a
             verify.py  7eaca91f6c3d73830f86750f142e910f2fd38e404821eeaeb3ac43f16c6e2188
             break_de_trace_density_1.py
                        658f05edb2d66428af8a7bf24907cee3b25bfacdd33c6d5cb21bcca219a824af
```

Break path executed under the same environment: exit 0, stdout SHA-256
`9f0b08587543bdba48bb1d87759b2914a5a9dbdee4213e73f72b2ae1ab62fd36`,
result line: BREAK ATTEMPT FAILED. NONUNIQUE STANDS.

Cross-platform witness: the same verifier bytes previously produced the same
stdout hash on an independent x86_64 platform (Ubuntu, Python 3.11.15), per
the provenance disclosure in PREREG.md. The required GitHub x86_64 check at
PR time is the remaining gate; byte identity with EXPECTED.txt is required.
