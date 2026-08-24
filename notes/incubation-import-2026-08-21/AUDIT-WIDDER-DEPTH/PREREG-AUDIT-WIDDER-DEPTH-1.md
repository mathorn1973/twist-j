# PREREG-AUDIT-WIDDER-DEPTH-1

```text
KIND:       independent audit of the owner-completed non-canonical branch
            notes/c-rh-stieltjes-widder-euler-1-n (issue 471, head f0a455a1),
            the Euler-Widder hierarchy for RH.
SESSION:    AUDIT-EULER-WIDDER-DEPTH. One named session, this audit only.
AUTHORITY:  none. NON-CANONICAL. No repo normative edit, no registry motion,
            no probe, no fold. RH stays O. Canon v57 untouched.
BASIS:      Public Canon v57 ACTIVE, main 4ef54f0c, tag canon-v57 resolving
            to the same commit, content commit 8e8b04ab, CANON_SHA256
            c96a2ef5.., CANON_BYTES 295013. Audited object is the branch
            head f0a455a1, nine files under notes/, canon/ untouched
            (checked: zero normative files in the diff against main).
LAYER:      L6 measure and spectral only. No lift.
DATE:       2026-08-20
DISCLOSURE: RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
PROCEDURE:  this file and audit_widder_depth_1.py are frozen TOGETHER before
            any execution, ast.parse only beforehand, pin recorded in
            AUDIT_PIN-WIDDER.txt with sha256, bytes, LF, CR and final-LF for
            each, then exactly one run. Gates collected in fixed order, no
            fail-fast, no time or path in stdout.
            Return codes 0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP,
            2 AUDIT-DISAGREEMENT.
```

## Falsifiers first

```text
WF1  the pole calculus fails: for some k in the declared range the identity
     (-1)^(k-1) D^(2k-1) [u^k/(u-z)] = (2k-1)! (-z)^k/(u-z)^(2k)
     is false as an exact rational function identity.
WF2  the unconditional low-level claims fail: some admissible zero pair and
     some rational u > 0 give f-contribution <= 0 or W_1-contribution <= 0.
WF3  the exact criterion fails: for some admissible z the sign of the
     conjugate-pair contribution to W_k at some sampled rational u > 0
     disagrees with the sign predicted by Re[(-z)^k].
WF4  the owner's two recorded depths are not reproduced exactly:
     rho = 9/10 + i/2 must give first negative degree 2, and
     rho = 3/4 + 10i must give first negative degree 32.
WF5  the depth law fails: for some declared rational (beta, gamma) the exact
     first negative degree lies outside the bracket predicted by
     k_min = ceil(pi / (2 arctan(B/A))), evaluated with a certified rational
     enclosure of pi.
WF6  the vacuity claim fails: some admissible zero pair with |gamma| >= 1 and
     0 < beta < 1 has B > A, or has Re[(-z)^2] <= 0.
WF7  the background claim fails: the synthetic competition example does not
     exhibit an aggregate W_k that stays positive at the isolated first
     negative degree of its off-line pair.
```

## Field 1: what is audited, and at what ceiling

The owner's branch is the object; nothing here can raise or lower its own
labels. This audit earns candidate labels only, single platform.

```text
WA1 [candidate-T]  the pole calculus of the hierarchy: with
    z_P = rho(rho-1) and f(u) = sum_P m_P/(u - z_P),
    W_k(u) = (-1)^(k-1) D^(2k-1)[u^k f(u)]
           = sum_P m_P (2k-1)! (-z_P)^k / (u - z_P)^(2k).
    Verified as an exact rational function identity, not sampled.
WA2 [candidate-T]  unconditional positivity of the first two levels, and the
    reason: for any zero in the open critical strip,
    A := -Re z = gamma^2 + beta(1-beta) > 0, so every conjugate pair
    contributes 2(u+A)/((u+A)^2+B^2) > 0 to f and
    2[A(u+A)^2 + B^2(2u+A)]/((u+A)^2+B^2)^2 > 0 to W_1.
    The owner's f > 0 and W_1 > 0 are confirmed.
WA3 [candidate-T]  EXACT DETECTION CRITERION, new in this audit. Write
    z = -A + iB. For one conjugate pair the contribution to W_k is
    negative for some u > 0 if and only if Re[(A - iB)^k] < 0.
    Reason: the contribution is proportional to cos(k(2phi - theta)) with
    theta = arg(A - iB) and phi = arg((u+A) - iB); as u runs over (0, inf),
    2phi - theta sweeps (-theta, theta) monotonically, so the infimum of the
    cosine over u is cos(k theta), and cos(k theta) < 0 is exactly
    Re[(A - iB)^k] < 0. This replaces a scan over u by one integer test in
    Z[i], with no pi, no float and no transcendental input.
WA4 [candidate-C]  exact reproduction of the owner's two recorded depths by
    that criterion.
WA5 [candidate-T]  DEPTH LAW. The first failing level of an isolated pair is
    k_min = ceil(pi / (2 theta)), theta = arctan(B/A), with
    B/A = gamma(2 beta - 1)/(gamma^2 + beta(1-beta)).
    Consequence, in the regime that matters: for fixed beta > 1/2 and large
    gamma, theta is asymptotically (2 beta - 1)/gamma, so
    k_min ~ pi gamma / (2(2 beta - 1)).
    The depth needed to see an off-line zero grows LINEARLY in its height and
    inversely in its distance from the critical line.
WA6 [candidate-T]  VACUITY OF THE LOW LEVELS. Since arctan x < x, every zero
    with |gamma| >= 1 and 0 < beta < 1 has B <= A, hence theta <= pi/4, hence
    contributes NON-NEGATIVELY to W_2 at every u > 0. Therefore
    W_2 >= 0 holds unconditionally, with no RH input, using only the
    classical absence of zeros below height one. More sharply, with a
    verification height H (no off-line zero below H), every level
    k <= pi H / 2 is unconditionally non-negative.
WA7 [candidate-C, breaker]  isolated depth is a LOWER bound only: on-line
    poles contribute positively at every level, so an aggregate W_k can stay
    positive at the isolated first negative degree of an off-line pair.
    A synthetic exact example is exhibited.
```

## Field 2: code

One program, `audit_widder_depth_1.py`. Python standard library only,
integers and `Fraction` only, complex numbers carried as exact pairs of
rationals in Q(i). No float is formed anywhere, and `math` is not imported.
A certified rational enclosure of pi is computed inside the program by the
Machin identity pi/4 = 4 arctan(1/5) - arctan(1/239) with exact alternating
series truncation bounds; no library constant is used.

## Field 3: carrier

Rational zero parameters only; no zeta ordinate is instantiated anywhere and
no zero table is read. Frozen ranges:

```text
pole calculus         k = 1..6, exact rational function identity
u sampling grid       1/1000, 1/100, 1/10, 1/2, 1, 2, 10, 100, 1000, 10^4
owner data points     rho = 9/10 + i/2 and rho = 3/4 + 10i
depth-law grid        beta in {3/5, 2/3, 3/4, 9/10, 99/100},
                      gamma in {1/2, 1, 2, 5, 10, 20, 50, 100}
vacuity grid          same beta set, gamma in {1, 2, 5, 10, 14, 50, 1000}
breaker               one off-line pair rho = 3/4 + 2i against N on-line
                      poles at gamma in {14, 21, 25, 30, 32}, unit masses
pi enclosure          Machin, truncation depth fixed at 40 terms
```

## Field 4: systematics

The criterion of WA3 is proved in prose and certified here by exact witness
agreement on the declared grid; the sweep argument is the load-bearing
object, the samples are the regression. Existence of a negative value at
k_min is certified by an exact witness u from the grid, which is sufficient;
absence below k_min rests on the sweep argument plus grid confirmation, and
this asymmetry is disclosed rather than hidden. Widder's characterization
itself, in the Sokal form the branch cites, is a LABELLED IMPORT and is not
re-proved here; every conclusion of this audit is conditional on the operator
family W_k being the correct one, which is the branch's own frozen premise.

## Field 5: failure threshold

Any WF that fires is recorded as a finding with its exact witness and is not
deleted. No tolerance, no retry, no threshold movement after this freeze.
Single platform, so nothing here can earn a public T, and no summary may
exceed the branch's own status or scope. RH remains O in every branch of the
outcome.

## Field 6: action layer

L6 only. No physical reading, no decoder, no SI statement, no lift.
