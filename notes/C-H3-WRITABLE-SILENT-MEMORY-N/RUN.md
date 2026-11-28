# Informal exact audit

NON-CANONICAL. Issue #2129 froze A-C before computation.
No failed threshold changed. Public H3 source at
6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
reproduce/h3-referenced-record/verify.py,
Git blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256 4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

Initial execution: Linux aarch64, Python 3.11.2.
Primary verify.py, clock_check.py and alternate break.py
all exited zero with empty stderr. Alternate B/C stdout
matches EXPECTED.txt byte for byte. The alternate is
separately written after seeing primary results and
does not repeat clock_check.py's additional first
trajectory samples. No formal repository runner invoked.

Exact archived bytes:
```text
a38d5b8ad67ec4c8427c6461331f51360bb5f233f9e3f46ce1633f880c5eb231  verify.py
842fbdf6fb8431891fec6567d81c81fa68d5778b5cd04bae2ea6a9636652e370  clock_check.py
f1060113634271f3ca69e0734d1a08d23c3d31ebb3431d4881706ecb55486957  break.py
40b036af87f7c4a6fa6bbca6e3849eb498268ae4eea4aa19d8a6960af3ada102  EXPECTED.txt
fbadb2c23b5e09970bf18b00018919fd917b3effe0199ddbd2f834bbf19342f3  CLOCK.txt
```
EXPECTED.txt: 17 lines, 7666 bytes.
CLOCK.txt: 5 lines, 681 bytes.
No registry/Canon change; no authority or formal gate claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit 2a46d561cec90e66f7a4c647fa62902e41d41a9b and the immutable
public H3 source at the base were fetched as raw files. All six
source and transcript SHA-256 values were checked before execution.
Primary verify.py, clock_check.py and alternate break.py exited zero
with empty stderr. Both full B/C outputs match EXPECTED.txt, and the
sample output matches CLOCK.txt byte for byte on both architectures.
This is result-exposed reproduction, not blind independent review
or the formal public scientific gate.
