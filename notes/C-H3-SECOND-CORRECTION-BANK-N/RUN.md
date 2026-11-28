# Informal exact audit

NON-CANONICAL. Issue #2133 froze A-C before computation;
comments 7238879872 and 7238893279 separately froze D and E.
No earlier failed threshold altered.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

prior.py and alternate_prior.py are exact copies respectively
of verify.py and break.py at
f96db81df668f138d7242ddfa2c7d946ea892833,
notes/C-H3-INTEGRATED-SILENT-ARCHIVE-N/. Apache-2.0 repository
license applies. They are reused engine inputs, not new
independent evidence. Hashes checked before initial execution.

Initial runs: Linux aarch64, Python 3.11.2. Primary A-C, D,
E and alternate exited zero with empty stderr. Alternate
recomputes the distinguishing time scan, all12 response vectors
and their exact rank-one span, all24 clock pairings, actual
selected integrated restoration/second histories, all21000 D
cases, and E's matrix and independent integer annihilator and
rank-minor certificates. It has its own compact output, not
the primary print format. E primary's nonuniform sample
and RREF print are not separately duplicated. Result-exposed,
not blind independent review. No formal public runner invoked.

Exact archived bytes:
```text
29826845142b36d24ef2571ba53d2f2a6e2bb5b5c4066057f5314f1a6b03c550  prior.py
d92e1d6b859efe5a2c49f9bc65959a51202c8cb32d4a015594c50603086bb99b  alternate_prior.py
4b1f8abc83559eba75a2f37fab402a120d1d89e85ce51cca636291f8ca2d33f2  verify.py
3d49de145814cc73d3722c177b3081b7c8ebaac14a7f7051b553467af330b496  nonlinear.py
d92aa903c4bd00c83650a84db01b2f0cdfa7e8106fbd719c920ffd09da2ad40a  mean_clock.py
9e8036e4da86c2e3b5dcf5cf24e4743af6af4e410cf0db116337ab798e2bddb6  break.py
dbc4e4394020f60238d7ee1c5050168bfb9339a2f1af82335ddeedb4e08b10f2  EXPECTED.txt
6d52418201010c3b6fbfa8544366e1cc29a876f6e740168cadf083ab0c178942  D.txt
10055bb88d2cc5a9cb8c6d7a95ed5705749379dc6f0680c9239d50b5359cc9b7  E.txt
354888bb50e570a4377fb1d360bdcf19291d1f8e770bf13b5f3dc329b945623c  BREAK.txt
```

No registry/Canon change; no authority or formal gate claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit 8c047afe950fdb2bdc65d0dc169feeec35ecc377 and the immutable
public H3 source at the base were fetched as raw files. All eleven
source and transcript SHA-256 values were checked before execution.
Primary A-C, D, E and alternate A-E exited zero with empty stderr.
Each complete stdout matches its own archived transcript byte for
byte across architectures. The separately implemented alternate
recomputes the principal results in its own print format. This is
result-exposed reproduction, not blind independent review or the
formal public scientific gate. At packaging only trailing whitespace
in the copied issue preregistration was removed; the scientific
criteria were unchanged.
