# PREREG-AUDIT-WIDDER-DEPTH-1B (correction leg)

```text
KIND:      correction leg of AUDIT-EULER-WIDDER-DEPTH, opened because gate
           WA7 of leg 1 FIRED (recorded, exit code 2, AUDIT-DISAGREEMENT on
           the audit's own auxiliary claim, not on the owner's branch).
WHAT FIRED: WA7 predicted that a small on-line background would rescue every
           sampled negative value of an off-line pair at its first negative
           degree. It did not. Diagnosis to be tested here: the level-k
           weight of a pole decays like A^(-k), so at high k the hierarchy is
           dominated by the LOWEST poles. In leg 1 the off-line pair sat at
           height 2, BELOW the whole background, so it dominated and could
           not be rescued. The prediction was right in mechanism and wrong in
           configuration.
CLAIM UNDER TEST (the corrected one):
           for an off-line pair placed ABOVE part of the on-line spectrum,
           the positive contributions of the lower on-line poles dominate its
           negative contribution at its own first negative degree, by an
           exponentially large factor. If this holds, the failure of the
           hierarchy is exponentially masked exactly where it first appears.
AUTHORITY: none. NON-CANONICAL. RH stays O. Canon v57 untouched.
BASIS:     unchanged, main 4ef54f0c; audited branch head f0a455a1.
PROCEDURE: this file and audit_widder_depth_1b.py frozen together, ast.parse
           only beforehand, pin in AUDIT_PIN-WIDDER-1B.txt, exactly one run,
           fixed gate order, no fail-fast, no time or path in stdout.
           Codes 0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT.
DATE:      2026-08-20
```

## Falsifiers

```text
XF1  the weight ordering fails: at a declared level and sampled u, a pole of
     greater height does not have strictly smaller contribution magnitude
     than a pole of lesser height.
XF2  the masking claim fails: the off-line pair at height 50 with beta = 3/4,
     at its exact first negative degree, is NOT dominated by the declared
     lower on-line background at some sampled u > 0, that is the aggregate
     goes negative.
XF3  the leg-1 diagnosis fails: the leg-1 configuration, whose off-line pair
     sits below the whole background, does NOT stay negative in aggregate,
     so the stated reason for the WA7 firing is wrong.
XF4  the domination is not exponential: the ratio of the dominant positive
     term to the negative term fails to exceed the declared floor of 10^6 at
     the tested level.
```

## Gates

```text
XA1  weight ordering in height, at fixed level and u                 [candidate-C]
XA2  masking of an off-line pair at height 50 by lower on-line poles [candidate-C]
XA3  leg-1 configuration reproduced: off-line pair below the whole
     background stays negative in aggregate, which is exactly why WA7
     fired                                                          [candidate-C]
XA4  the domination ratio at the masked level exceeds 10^6          [candidate-C]
XA5  the closed reading: at level k a pair contributes with weight
     (2k-1)! |z|^(-k) times a bounded phase factor, so the hierarchy at
     depth k is governed by the lowest poles                        [candidate-T]
```

## Code, carrier, systematics

One program, standard library only, integers and Fraction only, Q(i) pairs,
no float, no math import, no zero table: all heights are declared rationals.

```text
off-line probe    rho = 3/4 + 50i, exact first negative degree from leg 1
background        on-line poles at gamma in
                  {14, 21, 25, 30, 32, 37, 40, 43, 48}, unit masses
leg-1 control     rho = 3/4 + 2i against the same background
u grid            1/1000, 1/100, 1/10, 1/2, 1, 2, 10, 100
ratio floor       10^6
```

Single platform, candidate labels only. Nothing here moves RH, the branch, or
any public row. The masking statement is about this frozen synthetic
configuration; it is evidence about the mechanism, not a theorem about the
true zero set, whose density is not modelled here.
