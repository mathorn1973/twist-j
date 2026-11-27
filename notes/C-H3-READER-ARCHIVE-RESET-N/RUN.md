# Informal exact audit

NON-CANONICAL. Issue #2121 froze A-C before computation;
comment 7222083060 froze D before its further comparisons.
A/B original targets and outcomes retained.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.
The separately implemented alternate uses five cyclic coefficients.
The primary precomputed matching edges and memoization preserve
the exact native local primitives and geometry; A and D literally
compare the full pinned update.

Initial run: Linux aarch64, Python 3.11.2. A, B, D and alternate
scripts exited zero with empty stderr. The alternate independently
replays A/D1 and selected D2 and asserts the exact reported
periods, reset times, record values, hold and selected guards.
It does not repeat the primary B enumeration. Its own transcript
is archived separately. It is result-exposed, not a blind reviewer.
The negative outcomes are scientific results, not runner errors.

Exact archived bytes:
```text
ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95  verify.py
0e64fe0a89f130feb83ba408d9372b010d5d34237665f076359780691038c4de  capture.py
b2d9ad7b106d3d54fded0d829e850b5661e36cb5ed087c6e9bb00637c027655b  delayed.py
48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e  break.py
9f72165138b5fdb77a52123c07af5ecb25977c6dee9419a9129346d25d75065b  A.txt
67e5f2478cee3eb7474d3a4797b8e92fa7b597e8251e87be3af677a2b762e87c  B.txt
c3ab196ea79e0589c25d4a2fc80b4d58ac7e252ffc368b3760deca15d321977a  D.txt
694a29adc55e93eab7e6cb1aaa9239ded7934cb74ec27ce91cff22af2f22547e  BREAK.txt
```

No registry/Canon change. No formal scientific gate or authority claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit 580c174d44607887de3cb76cb3614a1a357b5318 and the immutable
public H3 source at the base were fetched as raw files. All nine
script, source and transcript SHA-256 values were checked before
execution. Primary A, B and D and alternate A/D1 and selected D2
exited zero with empty stderr. The four complete outputs match the
archived A.txt, B.txt, D.txt and BREAK.txt byte for byte. The
alternate does not independently repeat the B search. This is
cross-architecture reproduction, not blind independent review or the
formal public scientific gate.
