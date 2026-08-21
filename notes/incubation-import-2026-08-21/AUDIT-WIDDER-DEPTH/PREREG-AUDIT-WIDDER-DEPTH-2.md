# PREREG-AUDIT-WIDDER-DEPTH-2 (correction leg after the owner review)

```text
KIND:       correction leg of AUDIT-EULER-WIDDER-DEPTH, opened on the owner
            review that found two precise errors in the audit's auxiliary
            claims (per-level sign criterion; ceiling form of the depth law)
            and derived the stronger finite-prefix no-go. This leg verifies
            the owner's corrections independently, attempts to break them,
            and records exactly what in the first audit falls, what stands,
            and what is strengthened.
SESSION:    AUDIT-EULER-WIDDER-DEPTH (same named session, leg 2).
AUTHORITY:  none. NON-CANONICAL. No registry motion, no probe, no fold.
            RH stays O. Canon v57 untouched.
BASIS:      Public Canon v57 ACTIVE; current main d44645a2 (moved past the
            e6845b96 named in the review by one further QDD probe merge;
            normative delta from the v57 activation commit is zero, checked).
            Owner correction branch notes/c-rh-widder-angle-sweep-correction-
            1-n at 5d89e26c, STOP recorded before verifier execution; the
            remote accepted-verifier blob is 98973ce7.., matching the
            mismatch value in the STOP record.
LAYER:      L6 only. No lift.
DATE:       2026-08-20
DISCLOSURE: RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
PROCEDURE:  this file and audit_widder_depth_2.py frozen together, ast.parse
            only beforehand, pin in AUDIT_PIN-WIDDER-2.txt with sha256,
            bytes, LF, CR, final-LF for each, exactly one run, fixed gate
            order, no fail-fast, no time or path in stdout.
            Codes 0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT.
```

## The two accepted corrections, stated as the claims under test

With z = -A + iB, A > 0, B > 0, theta = arctan(B/A) and
P_k(A,B;u) = 2(2k-1)! Re[(A-iB)^k/(u+A-iB)^(2k)]:

```text
C1 (per-level criterion, corrected)
   P_k < 0 for some u > 0
   iff k theta > pi/2
   iff some j <= k has Re[(A-iB)^j] < 0.
   The first audit's per-level form (iff Re[(A-iB)^k] < 0) is FALSE in
   general: the endpoint power can return to the right half-plane while the
   swept angle interval already contains the negative cosine window.
C2 (depth law, corrected)
   k_min = floor(pi/(2 theta)) + 1 = min{k >= 1 : Re[(A-iB)^k] < 0}.
   The first audit's ceiling form fails exactly at resonance, where
   pi/(2 theta) is an integer; there the resonant level is positive for
   every finite u with unattained infimum zero.
C3 (finite-prefix no-go, the owner's strengthening)
   For rho_N = 3/4 + iN: A_N = N^2 + 3/16, B_N = N/2, and
   B_N/A_N < 1/(2N), so theta_N < 1/(2N) and k theta_N < 1/2 < pi/2 for
   every k <= N. One symmetric off-critical configuration alone therefore
   passes the first N Widder levels as full functions of u. No finite
   prefix of the hierarchy characterizes RH in the symmetric pole class.
   No masking by other poles is needed.
```

## Falsifiers, each a first-class outcome if fired

```text
CF1  the owner counterexample fails: at A = B = 1, k = 8, u = 1/2 either
     Re[(1-i)^8] is not 16, or P_8 is not negative, or its exact value is
     not -172056926056081143103488000/51185893014090757.
CF2  the resonance certificate fails: (1-i)^4 != -4, or the polynomial
     identity Re[(1-i)^2 ((u+1)+i)^4] = 8u(u+1)(u+2) fails, or
     min{k: Re[(1-i)^k] < 0} != 3, while pi/(2 theta) = 2 exactly.
CF3  the non-resonant counterexample fails: at A = 2, B = 1, k = 14,
     Re[(2-i)^14] is not 76443, or no j <= 14 has Re[(2-i)^j] < 0, or no
     exact rational u > 0 with P_14 < 0 is found.
CF4  corrected criterion C1 disagrees with the empirical sign search
     anywhere on the declared (A, B, k) grid, in either direction.
CF5  the floor-plus-one form and the min-Re form of k_min disagree anywhere
     on the declared grid, resonant points included; or the two owner
     control points shift from 2 and 32.
CF6  the N-family chain fails: some declared N has B/A >= 1/(2N), or some
     k <= N has a j <= k with Re[(A_N - i B_N)^j] < 0, or a sampled
     negative value appears.
CF7  the no-induction witness fails: rho = 9/10 + i/2 does not give W_1 > 0
     at every sample together with W_2 < 0 at some exact sample.
```

## Gates and ceilings

```text
CG1  owner counterexample verified to the exact reduced fraction [candidate-C]
CG2  resonance: integer certificate theta = pi/4 via (1-i)^4 = -4; the
     polynomial identity Q_2 = 8u(u+1)(u+2) over Q[u]; k_min = 3; the
     ceiling formula demonstrably gives 2 and is wrong        [candidate-T]
CG3  non-resonant endpoint-return counterexample with exact witness
                                                              [candidate-C]
CG4  corrected criterion against empirical search, both directions, grid
     (A,B) in {(1,1),(2,1),(3,2),(5,1),(7,4)}, k = 1..20; negative cases
     need an exact witness u (dense grid first, then a certified
     arctan-bracket bisection fallback); positive cases assert strict
     positivity at every sample, the sweep proof carrying the quantifier
                                                              [candidate-T]
CG5  k_min forms agree on the grid plus resonant (1,1), (4,4); owner
     control points 2 and 32 unchanged                        [candidate-C]
CG6  N-family for N in {1, 2, 5, 10, 100, 10^6}: exact chain
     B/A < 1/(2N), prefix-Re nonnegative for all k <= N (tested k <= 40
     for the large N, full range for N <= 10), samples positive for N = 5
                                                              [candidate-T]
CG7  W_1 > 0 everywhere sampled and W_2 < 0 at an exact witness for
     rho = 9/10 + i/2: no level-to-level induction            [candidate-C]
```

## Code, carrier, systematics

One program, audit_widder_depth_2.py: standard library only, integers and
Fraction, Q(i) pairs, polynomial pairs over Q[u] for the sign polynomial
Q_k(u) = Re[(A-iB)^k ((u+A)+iB)^(2k)], whose sign equals the sign of P_k.
No float, no math import, no zero table. Pi enters only through the Machin
enclosure computed inside the program and only where a transcendental
comparison is genuinely needed; the resonance defect is certified purely by
integers. Single platform, candidate labels only; nothing here moves RH, the
owner branch, or any public row. The prefix no-go quantifier over all u rests
on the corrected sweep theorem, whose proof is in the owner's PROOF.md and is
re-derived in the correction record; the program certifies its exact inputs
and witnesses.
