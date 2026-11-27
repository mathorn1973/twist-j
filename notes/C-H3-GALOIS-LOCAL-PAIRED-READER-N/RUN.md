# Informal exact audit

NON-CANONICAL. Issue #2111 froze A-C before computation, comments
7219919260 and 7219949923 froze the result-exposed D and E diagnostics
before their respective computations. No earlier failed threshold
was changed.

Public source commit 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The public Apache-2.0 source is imported unchanged and not copied
into this package. The alternate code implements five cyclic
coefficients and independent local updates.

First completed execution: Linux aarch64, Python 3.11.2.
The first A-C audit and both completed D/E successors exited zero
with empty stderr. D's first attempt stopped on NameError (missing
rsum), E's first attempt stopped on TypeError (shift constant
shadowed by the read weights). Original scripts and partial
stdout/exception records are preserved. D adds only rsum=V.rsum;
E renames only the global shift constant to SHIFT and its four
uses. No scientific input, formula, threshold or output condition
is altered. The corrected scripts were rerun in full.

The alternate script does not import the first verifier or public
source. It replays all 224 fields through four strokes, checks
the A,C,D core census aggregates and first material witnesses,
and reproduces the entire E transcript byte for byte. It was
written after the primary results and is result-exposed, not
a blind second-agent review.

Exact executed source and transcript SHA-256 values:
```text
3baf745825e14a883c6443807dd4c3a371df59e366e4b8d21adf2fd6542dd1fb  verify.py
56b1424610942b817ea8a486b69cca224a4b943d05c69522569b3d32ee31f54b  local_material.py
4d476f163788d48036c216aaf4f545c6577219869055294a33f0bb10f9a642c7  local_material_original.py
e25cad917dccdbe43e915714f4f6dc79d27bc14afafae932dbb2a93ab55a4690  dual_basis.py
77f9b548a17ec7a55eed05d4c2b6f8f4d0c6c9c3cb083e9c1cdd62d26c7e7cb4  dual_basis_original.py
d2a4ef31bcdf8c991fb68d88bbfc6ae5ef12e424f621d4b0510f2d69cbbbe8cd  break.py
3c600da875238c289a52fc17c5d5ebc4d74b17d2cdada59c8f7d119cf338c387  EXPECTED.txt
7b71faefb385eb01f489cf4b7abf252dc9b6874b47f7dc8d1367b9b04bee52d3  D.txt
441c0ce21f1d94d4bf7851fb77d975ba11981a7986ec2c76316b3c32a39d6016  E.txt
dced45f309ab6d34c74a20d44d97a1c941fcb2981bd046e94fad7bfdce3f0d30  BREAK.txt
beb32b6d47763790df311fe986b99b2ac8142329f3c3c523ad35aabf73b37e71  D_FIRST_PARTIAL.txt
62113bf3df420834039ee0957bd87200684f7b0278d4e78e92e99d1f22004a26  D_FIRST_ERROR.txt
091d8d4f96f0b9b3c9b85865152df24fadae79ff9f84680aa47de1b350d882e7  E_FIRST_PARTIAL.txt
0029e2db41b6b580259c94d7964af5b31336148bafe91ad6ddece38e55207669  E_FIRST_ERROR.txt
```

No formal scientific gate or registry/Canon change is claimed.
