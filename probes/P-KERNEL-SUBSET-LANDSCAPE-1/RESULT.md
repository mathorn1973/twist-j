# P-KERNEL-SUBSET-LANDSCAPE-1 result

Status: `DECIDED AND AUDITED / CANON UNCHANGED`

## Disposition

```text
landscape:  the exact 32-entry table of dim U_S is decided; connectivity
            of (F_5^6)^k for every k >= 2 holds exactly at dim U_S = 6,
            and the connected subsets are exactly acde and abcde. The
            letter a is load-bearing (dim U_cde = 4, dim U_bcde = 5);
            the letter b is inert everywhere (it never raises any dim).
integrity:  no STOP. One formal execution, exit zero, empty stderr,
            7/7 gates PASS, stdout equal to EXPECTED.txt.
amendment:  the incubation lane's original lower-bound clause
            5^(k(6 - dim U_S)) FIRED in the lane (25 demanded, 2 found
            for bcde at k = 2, exhaustive union-find) and is NOT part of
            the public claim; the negative branch here says at least two
            components, carried by confinement alone. The fired clause
            stays archived lane history with its threshold unmoved.
```

## Proposed registry consequence (a later sealed fold, not this probe)

KERNEL-SUBSET-LANDSCAPE [T], exact row text frozen in PREREG.md, canon
section 3. Sharpness companion of KERNEL-CONNECT-ALL-K [T]: that row
connects with acde; this row decides which subsets connect and why. No
live row moves.

## Evidence boundary

Local formal leg x86_64 (Ubuntu 24.04.4 LTS, CPython 3.11.15); the
pull-request workflow supplies the x86_64 and aarch64 replays against
EXPECTED.txt, completing the repository two-architecture computation
gate. The dichotomy is carried by the subset-generic lemma chain written
in PREREG.md (inherited from the public KERNEL-CONNECT-ALL-K proof,
which uses only that letters are affine involutions and transvections
are present); the verifier decides the table exactly and audits the
chain's finite instances (verbatim letters on all 15625 states,
exhaustive k = 1 confinement per subset, exact commutator translations
at k = 2). No dynamics, measure, or census claim is touched.
