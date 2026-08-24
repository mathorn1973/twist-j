# RESULT: C-WEIL-GRAM-TOWER-1, frozen run + R6 addendum (project reading copy)

```
Status     reading copy; byte authorities are RESULT-C-WEIL-GRAM-
           TOWER-1.md and RESULT-ADDENDUM-R6.md on the handoff branch.
           The R6 leg is CLOSED under its pinned procedure (attempt 2
           passed per ANO-10(b)). Standing state until the owner's
           candidate-C ruling over the complete frozen scope:
           [C, certified, two-platform] all measured inertias valid;
           [NON-CANONICAL] no public state changes; [NO candidate-C]
           pending the owner's closing ruling.
Chain      c1810302 frozen draft (ANO-7; sha 8a1a5114..., 13961 B)
           66a7b4d  FREEZE + runner v1 pin; R6 defect declared pre-run
           d02faf2  runner v2 pin (v1 precision defect recorded)
           71827c7  post-pin frozen run (main scope): starts
                    16:27:06/07Z after the 16:00:09Z pin, exit 0 both
                    platforms, stdout BYTE-IDENTICAL, sha a019ed91...
           d2e8aa4  FREEZE Amendment 2 (owner: v2 timing defect;
                    ANO-8 NO, ANO-9 YES)
           279aaea  ADDENDUM R6 pinned pre-execution (engineQ
                    b2a5f00c... derived deterministically from the
                    pinned engine; runner 46d62f6d...; run_robust
                    scope: q = log(phi)/2, N=12, xi_0..2 at K=3,
                    DH- at K=6, nmax = phi^12, prec 96)
           27b223a  RESULT ADDENDUM R6 attempt 1: gates pass, xi
                    blocks certified PD identically, E4 does not fire,
                    45 certified negative in DH- on both platforms
                    with identical witness; the equal-stdout clause
                    FIRED on the (und, pos) lower-bound split
                    (5/118 vs 4/119, platform LAPACK subspace choice)
           d2e8aa4->4e86749  ANO-10(b): clause not weakened; repair =
                    pin the certified subspaces themselves. Pinned
                    before execution: exact dyadic certificate
                    r6_dh_certificate.json sha f4e1ab81... (45 neg +
                    118 pos columns + witness; LAPACK used only in the
                    pre-pin proposal stage, verified there in balls),
                    DH-only binding runner 0b47cbd0... (no LAPACK, no
                    numpy at run time), Amendment 3.
           bea4253  attempt 2 PASSED: starts 17:16:37/38Z after the
                    17:16:26Z pin, exit 0 both platforms, stdout
                    BYTE-IDENTICAL (sha 491b0357...), fixed
                    compressions LDL-definite (45 and 118), pinned
                    witness Q(w) in [-5234.523321 +/- 4.09e-7]
                    certified < 0, reported triple (45, 5, 118)
                    exactly as owner-fixed.
```

## Main frozen scope (71827c7, byte-identical stdout both platforms)

R1: zeta, chi5, xi_0..xi_6 at (N',3), N'=2,4,6: every section
certified positive definite, zero undecided. R3: certified entrywise
(xi_0 - chi5) == zeta. R4 branch-resolved guard: dh_minus (6,3)
certified (16,0,32), witness [-7948.377445 +/- 4.62e-7] < 0; dh_plus
(6,3) certified PD, the below-height control; dh_plus (6,14) certified
(2,50,128), witness [-2.85387454 +/- 4.43e-9] < 0; Euler gates
certified for both branches. R5: prime-power-only DH shell certified
(25,0,23). R7 vacuous (full rank). R8 non-comparable diagnostics.
Endings E1, E2, E3 not fired.

## R6 leg, closed

Attempt 1 (27b223a): gates G-compat and G-cross pass on both
platforms; xi_0..2 at q = log(phi)/2, (12,3): certified (0,0,96)
identically; E4 does NOT fire; DH- keeps 45 certified negative
directions on both platforms with the identical witness. The pinned
equal-stdout clause fired on the (und, pos) lower-bound split;
retained as fired, not weakened.

Attempt 2 (4e86749 pin, bea4253 result), per ANO-10(b): the certified
subspaces pinned as exact dyadic bases; the binding run only verifies
the fixed compressions in ball arithmetic. Both platforms exit 0 with
byte-identical stdout, triple (45, 5, 118), witness certified
negative. All requirements of the ruling met; xi blocks and gates not
rerun, their agreement stands.

## Pending

The owner's candidate-C ruling over the complete frozen scope (main
run 71827c7 + R6 leg closed at bea4253) is the only open item. No
public state changes; the public probe remains unopened.
