# P-ENTROPY-MIRROR-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision at the recorded leg

```text
RESULT 6/6 ALL PASS, exit 0, stderr empty.
```

All six preregistered gates passed on the first formal execution of the pinned
verifier. The immutable preregistration pin is
`6000f11c1ef29e74c14b1111c394336c5ed497ad`, public lock issue 36, initial
base `ebc5c06f4d0bc5c0d01b931e4f26cccd72b60325`. The formal evidence commit
`20f92573a17126d32661272c6209f8e02d676419` adds only `EXPECTED.txt` and
`RUN.md`; it does not alter `PREREG.md` or `verify.py`.

Recorded aarch64 leg:

```text
platform:       Ubuntu 24.04.4 LTS
architecture:   aarch64
python:         3.12.3
stdout sha256:  d6bdffd691c98e8aa7d4233b5eac5ec1816d76d86eeeab0c30ab2aae5b66ae8c
stdout bytes:   1139
stdout lines:   14
stderr bytes:   0
result:         6/6 ALL PASS
```

Two-architecture record:

```text
aarch64 leg    Ubuntu 24.04.4 LTS, CPython 3.12.3, neutral environment;
               first formal execution; RUN.md in this directory.
x86_64 leg     GitHub check on pull request 37, head
               18d90f33129612c25f2aaef90353002360d379a5;
               run 29393659986, job 87282274811, conclusion success;
               Ubuntu 24.04 runner, CPython 3.12.13; verifier
               byte-identical (4fe37f77...), stdout byte-identical
               (d6bdffd6..., 1139 bytes); log carries
               VERIFY PASS P-ENTROPY-MIRROR-1.
gate:          PASS. The aarch64 and GitHub x86_64 outputs are byte-identical.
```

## Recorded finite outcomes

```text
M01 CORE
    The public census reconstructs a recurrent core of 6250 states on 313
    branch-invariant components: 312 of size 20 and one of size 10. The two
    living halves are disjoint and have 3125 states each.

M02 MIRROR
    Each branch letter restricted to its own living half is an involution
    with cycle type {1: 1, 2: 1562}. Its unique fixed state lies in the
    singlet component. The diagnostic witnesses are 10366 on H_0 and 11616
    on H_1.

M03 ALTERNATION
    The frozen cross restrictions are mutually inverse in the exact stated
    directions: F_1 o F_0 = id on H_1 and F_0 o F_1 = id on H_0.

M04 SWAP
    On its own half, each one-tick letter fixes the singlet pentagon and
    swaps the two canonical pentagons in every size-20 component-half. The
    induced cell cycle type is {1: 1, 2: 312}.

M05 REFLECTION
    In the preregistered coherent level-2 gauge, every one-tick cell map is
    affine over F_5 with multiplier 4 = -1. The ordered letter-map pairs are
    ((4,0),(4,2)) and ((4,2),(4,0)), each on exactly 625 of the 1250 source
    cells.

M06 CONSISTENCY
    On both source halves, T_0 o T_1 = T_0 o T_0 and
    T_1 o T_0 = T_1 o T_1. All four frozen cell-map comparisons pass.
```

No preregistered falsifier fired on the recorded leg.

## Scope and non-conclusions

The earned statement is finite and computation-grade only: the
own-half involutions, directional alternating inverses, canonical-pentagon
swap, and gauge-specific affine reflection law on the declared carrier. In
particular:

- no measurable, ergodic, spectral, or all-scale mirror theorem is claimed;
- no inverse-limit factor, cohomology decision, or gauge-independent normal
  is established;
- the reflection coefficient is not identified with a lambda digit;
- no equivariant selection family, measure transport, L2 lift, or physical
  interpretation follows;
- `ENTROPY-LAYER-BRIDGE` remains open.

Folding a reproduced outcome into the registry, frontier, or Canon is a
separate public step. This probe changes only
`probes/P-ENTROPY-MIRROR-1/`.
