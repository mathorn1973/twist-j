# Informal exact audit

NON-CANONICAL. Issue #2106 was posted before numerical audit.
No formal repository probe or formal scientific runner was invoked.

Public source commit 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The public source is Apache-2.0 licensed and is imported without
modification, not copied into this package.

First audit: Linux aarch64, Python 3.11.2. Both scripts were written
and hashed before either execution. The native source Git blob was
verified before import. Both scripts exited zero. The exact
transcripts match byte for byte with cmp; all 132 histories and
121 paired outputs passed. The alternate implementation uses a
five-power representation, separately implemented local laws and
row symmetry, rather than importing the first verifier or the
public H3 source. This is result-exposed and not blind review.

SHA-256:
```text
01be5abf46c099f438c7c5ad6e966121c59e838220c759e50bd77e27a55f90e8  verify.py
2faf79f49b6afb59a01bc92643881603e0e7a778f0e1e0899cce891630055f37  break.py
8a7df011eae586ba5b167454c312ab707c72f6ecede61bfe32ddf3bc2fe07579  EXPECTED.txt
8a7df011eae586ba5b167454c312ab707c72f6ecede61bfe32ddf3bc2fe07579  BREAK.txt
```

No formal public computation gate, status promotion or physical
inference is claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit c5608ca67f0999a22140980a78b84dc900bfcade and the immutable
public H3 source at the base were fetched as raw files. All five source
and transcript SHA-256 values were checked before execution. Both
scripts exited zero with empty stderr, and all four outputs (two
implementations on two architectures) match the same expected 135-line
transcript byte for byte. This is reproduction, not blind independent
review or the repository's formal two-architecture scientific gate.
