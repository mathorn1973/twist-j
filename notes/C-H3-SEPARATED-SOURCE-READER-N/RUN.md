# Informal exact audit

NON-CANONICAL. Issue #2115 froze A-C before computation;
comment 7220474250 froze D before the successor capture search.
No earlier failed target or scientific threshold changed.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The public Apache-2.0 source is imported unchanged and not copied
into this package. The alternate implementation uses its own
five-power cyclic arithmetic, explicit inverse-neighbor coefficient
and separately implemented local updates. Exact memoization of pure
native primitives does not change them.

Initial execution: Linux aarch64, Python 3.11.2. Primary A-C,
primary D (also rechecks the primary A-C transcript) and both
alternate stages exited zero with empty stderr. The exact full
A-C and D transcripts matched their respective alternate outputs
byte for byte. All executed sources archived unchanged.
The second algorithm was written after the primary results and
is result-exposed, not blind independent review.

Exact executed source and retained transcript SHA-256 values:

```text
74a0901e9714dac512875c88fc237303de66b0f56bc361a1fe0f17b86bae334f  verify.py
42f9d31155860a0248ce8cc6880e9acb32bc03d01345a721334c7417f6e3833a  capture.py
f25a762faaea80c2996908f414879e3c1d3cfcf33135b0816ea1ba9e634265bb  break.py
6c2fe83b76182a0e32044655d66e0f6692d3056614b69dd46e8ed370ae37d2ae  EXPECTED.txt
366e200b0a1320b1c263e9aa5f4e564b6a1b11198c5558af6b6d36c3a6d54747  D.txt
```

The failed recovery tests and finite read/hold horizons are
preserved. The active source is a scaled single reference
column, not the full original periodic two-track motor.
No formal scientific gate or registry/Canon change.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit 398f57c4f7dff77199f61d84ac54d95915d121f7 and the immutable
public H3 source at the base were fetched as raw files. All six
executed script, transcript and source SHA-256 values were checked
before execution. Primary A-C, primary D and both alternate stages
passed with empty stderr. Both full output pairs match the respective
EXPECTED.txt and D.txt byte for byte. This is cross-architecture
reproduction, not blind independent review or the formal public gate.
