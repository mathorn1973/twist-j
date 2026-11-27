# Informal exact audit

NON-CANONICAL. Issue #2119 froze A-C before computation;
comments 7221902605 and 7221916857 separately froze D and E.
The earlier static late-capture failure in #2118 and failed C
prediction remain unchanged.

Pinned public H3 source:
6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
reproduce/h3-referenced-record/verify.py,
Git blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The Apache-2.0 public source is imported unchanged and not copied.

B_PREV.txt is an exact copy of the Apache-2.0 predecessor's
B.txt at 873c5cd84d1a4dd059e01915e42df2660e17e850,
notes/C-H3-SOURCE-ECHO-N/B.txt. It is the frozen input roster
needed for A; its SHA-256 is verified before use. It is not
presented as new output or independent evidence.

Initial run: Linux aarch64, Python 3.11.2. All primary and alternate
scripts exited zero. C's scientific failure is explicitly recorded
rather than turned into a successful prediction. Primary B's
frozen-order first-success search was executed once here; selected
B is separately rechecked by the five-power alternate via D.
The alternate A and C extracts and complete D and E transcripts
match the primary outputs byte for byte. The alternate is
result-exposed, not a blind independent reviewer. No formal
scientific runner was invoked.

Exact archived bytes:
```text
eb4c0ec1d0b8f7528b9c0d724e7c797af23615e2878397adc1b742a4e0775af4  verify.py
f0c0d7b0eba63790072cfe3b1ab2139efb48ecb8b72f727a4b536f095abf84bc  controls.py
8f7bb082735a3567469af04122b7193d39dfa1d03ad90dccdc95b641543f722e  phase_gate.py
d9b56e24110e7ba22f34ea595cb4899830d09db3929dd7349bcef01e1f396dea  break.py
2ad5f52adc0c44a7c33a65f5ae3edc9fb64d8fb1f5a56974917828ef7e6f2615  EXPECTED.txt
c689dd80a2a4ac5a594173abcf21980ce348c587b0cded77ecb72a09342c1fdb  D.txt
62c939ce2c514d39baf7163e01df07cbab293749145c8804274a7ccced6fa478  E.txt
509ba5e68e73c53d84d98170164a0af84c59f18c498fb5bff632a31fda0260d9  BREAK.txt
83a3879a57fa20e6975f2dad47294f357854ff0d7caf673081e14d55dc2c3488  B_PREV.txt
```

No registry/Canon change. No authority or formal gate claimed.
