# Informal exact audit

NON-CANONICAL. Issue #2127 froze A/B before computation.
Comments 7223565203 and 7223597377 separately froze C and D.
No earlier failed scientific contract altered.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

predecessor.py and alternate_predecessor.py are exact copies
of the same names at 32d469651b9b1d0c37e097bc8c621b8081ac88ed,
notes/C-H3-TWO-INDEPENDENT-READS-N/. Their original source is
the #2122 package at 289b63b47566cafb37ccb873a7076052f0c88454.
Apache-2.0 repository license applies. They are reused engine
inputs, not new independent evidence.

Initial completed runs: Linux aarch64, Python 3.11.2.
Primary A/B, corrected C, D and alternate exited zero with
empty stderr. The initial C stopped in postprocessing with
NameError: name 'mark' is not defined, after completing the
first combined restoration and second trajectories. The only
repair was mark -> V['mark'] in the C3 write-count expression.
Original executed source and scientific partial stdout are
preserved. The raw traceback contained a private temporary
path and is not published; its original SHA-256 is below.
The full corrected C computation was rerun. No change of a
scientific input, threshold or guard. The alternate separately
recomputes the reported principal results and has its own
transcript, not a claimed byte-identical primary/alternate
print format. Both are result-exposed, not blind review.
No formal repository scientific runner invoked.

Exact archived bytes:
```text
ab59479b30fc82249aa2c65a4eeaf96199c1620780a72810fec26574729e60bf  verify.py
024f573b30f5102d937289bd877c2cfbc0eb2f951864a18e8ee610064a05282f  synthesis.py
234f921f5add00ab7b106592b6b311d3f543079b1516d443ada1ca2bc2c794c3  synthesis_original.py
8a6f331a4afaf45c11b4d6e65c26d56d03d956ee643b814a954f3c650a240c1d  diagnostic.py
f0e64dc32f20d070e3334c13acfc33509de5741fd70d8917198b3823bf9d9c9b  break.py
8bba832d22b7f910c0c7a612e2218454bf7d69088539d469f054050d927612b6  EXPECTED.txt
5a69479380bb1c98282605c87ad79bb9e42d17665a08e02ffec7975c8bb22784  C.txt
ea872a4db1a66f377b9ffd5abc3f75895e8eaed14b516a8466e88c69d3f71278  D.txt
8f42032a92684bdaa9645510c956d8ad828372cceaf89712fade216d7b796d23  BREAK.txt
e970d05d4831d464830406b5114f1b560dda46bf70ae983fa6247d0827b15ffa  C_FIRST_PARTIAL.txt
ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95  predecessor.py
48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e  alternate_predecessor.py
```

Original private-path C exception stderr SHA-256:
31084119ec0f24c8accd19e7035b7d16b93200d35c54e0345996e63129859cb6.
Not an archived public log.

No registry/Canon change. No formal scientific gate or authority claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit a423155aeee1d4bb3da8dc4c3e61c06a89794202 and the immutable
public H3 source at the base were fetched as raw files. All eleven
source and transcript SHA-256 values were checked before execution.
Primary A/B, corrected C, D and alternate A/B/C and core D passed with
empty stderr. All four complete outputs match the corresponding
EXPECTED.txt, C.txt, D.txt and BREAK.txt byte for byte across the two
architectures. The alternate has its own compact print format.
This is result-exposed reproduction, not blind independent review
or the formal public scientific gate.
