# Informal exact audit

NON-CANONICAL. Issue #2123 froze A-C before computation;
comment 7222314618 froze the result-exposed relative D successor
before its computation. No original failed threshold altered.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

predecessor.py and alternate_predecessor.py are exact copies of
verify.py and break.py respectively from
289b63b47566cafb37ccb873a7076052f0c88454,
notes/C-H3-READER-ARCHIVE-RESET-N/. Apache-2.0 repository license
applies. These are pinned reusable engine inputs, not new evidence.
Both are checked by SHA-256 before import.

Initial execution: Linux aarch64, Python 3.11.2. Primary A-C,
primary D and alternate exited zero with empty stderr.
The alternate was written after the primary results and reuses
the previously separate five-coefficient engine. It recomputes
A, all620 local guard candidates and the corresponding 600
admitted final relative pairs, and the selected D whole-field
replay, asserting exact reported values and boundaries.
It does not independently replay all600 complete B histories.
This is result-exposed, not blind independent review.

Exact archived bytes:
```text
ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95  predecessor.py
48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e  alternate_predecessor.py
017f235f16ccbc041ff983d635c163b2378ff4744057db1eb4ba22a4df5efb74  verify.py
b46621295b6a520f6661d4d5f139a61258a3bb78f6eda564cf4ea92a1776f5a4  relative.py
a94a9ac552104c3f4800c207827cf68f2c1a29f225b7105da2f240673cf7e6b5  break.py
e102be57c6428d78bcd5205e0bdbdc905141484366146d9f693f86bcb5a79b1d  EXPECTED.txt
582b4bd1f2d3b4c9bebeca4a5359f7c04dc4114f546c3c34481dee7c26c9c4e8  D.txt
6f0080118f5a1e542a0cf26ec627830485e1fb2b7c3eac622b105059e2815a86  BREAK.txt
```

No registry/Canon change. No formal scientific gate or authority claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit e7194a7866834e4524d4c8cd0ada4bcc418d0da5 and the immutable
public H3 source at the base were fetched as raw files. All nine
source and transcript SHA-256 values were checked before execution.
Primary A-C, primary D and alternate A/local-B/selected-D passed
with empty stderr. All three complete outputs match the archived
EXPECTED.txt, D.txt and BREAK.txt byte for byte. The alternate does
not independently replay all600 complete B histories. This is
cross-architecture reproduction, not blind independent review or the
formal public scientific gate.
