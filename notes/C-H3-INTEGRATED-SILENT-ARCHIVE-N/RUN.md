# Informal exact audit

NON-CANONICAL. Issue #2131 froze A-C before computation;
comment 7237214323 froze D after A-C and before its target
inspection. Earlier failed thresholds remain unchanged.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

Initial execution: Linux aarch64, Python 3.11.2.
Primary A-C, D and alternate exited zero with empty stderr.
The alternate recomputes all local censuses and both
selected full histories, including all second-input
multiplicities, account and inverse checks, and D.
All common scientific census/result lines and D match
the primary byte for byte. Alternate has a compact
print format (omits the SELECT dictionaries).
It was written after the primary results and is
result-exposed, not blind independent review.
D's target is unavailable, so its conditional 1210
candidate search was not executed. No formal scientific
runner invoked.

Exact archived bytes:
```text
29826845142b36d24ef2571ba53d2f2a6e2bb5b5c4066057f5314f1a6b03c550  verify.py
be22d6bd7a28b26760597a8ccf754bddbecb30d6af879fab41a497b09c09bd47  second_bank.py
d92e1d6b859efe5a2c49f9bc65959a51202c8cb32d4a015594c50603086bb99b  break.py
1110c470af5a479769e5488a46d0ac844ed38fa41dbaf4933faf0ac158e9009c  EXPECTED.txt
282580ac3591a607d65ac7a51cb468ee3b50db8110e0e5cb5788dc2bcdf0c3a5  D.txt
69b82b1513ed4b4836e83f553e7bd2c42c204029369381f969327f3706b703d2  BREAK.txt
```

EXPECTED.txt: 25 lines, 8340 bytes.
D.txt: 2 lines, 117 bytes.
BREAK.txt: 25 lines, 5944 bytes.
No registry/Canon change; no authority or formal gate claimed.
