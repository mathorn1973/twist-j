# RESULT P-SUZUKI-LOCAL-CAPACITY-NOGO-1

## Local result

```text
local_status: PASS
probe_status: SURVIVED
checks: 12 of 12 PASS
fired_falsifiers: none
stop_conditions: none
reproduction_status: PASS
```

The one post-pin local execution returned 0, wrote no stderr, and reproduced
the pinned 1054-byte `EXPECTED.txt` exactly. `EXPECTED.txt` equals the
frozen candidate stdout of 2026-08-13 (x86_64, executed twice there,
byte-identical), so the same verifier bytes now have byte-identical stdout
on x86_64 and aarch64. The formal public two-architecture gate is completed
by the required GitHub x86_64 check at pull-request time and recorded in
`RUN.md` before any fold.

## Result by claim

Statuses below are the statuses proposed in `PREREG.md` Field 1; every
grade stays a probe result, not Canon, until a sealed fold.

```text
N1  prime curve orthogonal-increment path   proof + gate V1 PASS      [T]
R2  curvature and plastic transition        reproduction of M-4;
                                            V2a, V2r, V2b PASS        [T]
N3  ramp class EMPTY                        gate V3 PASS; certified
                                            convexity violation at
                                            (1/20, 1/4, 1/2)          [T]
N4  filtration and domination kill          V4a, V4b PASS; increment
                                            domination dies at q = 2  [T]
N5  both screw kernels indefinite           V5 PASS with e^3, e^6
                                            boundary guards           [T]
R6  prime-free window positivity            V6 PASS, 100-leaf adaptive
                                            cover of [1/128, 45/64],
                                            zero undecided            [C]
R7  event count N(10^6) = 78734             V7 PASS, two independent
                                            counting paths            [C]
N8  norm one forced                         written proof, PNT named
                                            import; no machine gate   [T]
X   machinery cross-gates                   X1, X2 PASS: psi(3/4) -
                                            psi(1/4) encloses pi;
                                            psi'(1/4) + psi'(3/4)
                                            encloses 2 pi^2
```

Synthesis carried in scope, no separate gate: the completion capacity is
not a positive superposition of prime-type ramp atoms (N3), admits no
filtration or per-place domination reading (N4), and is not itself a screw
geometry (N5); any Gram realization dominating the prime curve has operator
norm exactly one (N8) and must be nonlocal in t. RH is untouched; nothing
here moves it.

## Pending before fold

```text
1  claim issue opened and linked in RUN.md (credential exception
   disclosed in PREREG.md)
2  pull request opened from probe/P-SUZUKI-LOCAL-CAPACITY-NOGO-1
3  GitHub x86_64 leg recorded in RUN.md, byte identity required
4  sealed fold with the registry motion proposed in PREREG.md Field 6
```
