# P-R2-SCALING-SHIFT-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN PENDING REMOTE PIN READBACK

This document freezes one proof-first public no-go probe. It contains no
formal gate output and earns no scientific status. Formal execution is
forbidden until this exact revision and `verify.py` are committed, pushed,
and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          J-LI
probe:            P-R2-SCALING-SHIFT-1
public lock:      issue 59
owner:            A. M. Thorn
branch:           probe/P-R2-SCALING-SHIFT-1
path:             probes/P-R2-SCALING-SHIFT-1/
action layer:     L6 spectral type; discrete-time lambda-adic scaling carrier class; no further lift
scientific state: candidate proof-first no-go; RH and every replacement
                  carrier remain open
```

Authority base is Public Canon v8, tag `canon-v8`, content commit
`208124ac19dbdc65c6f1cc80616ce55dbbceac51`, Canon SHA-256
`eabf29bc8058fa42104b53b44b0e6db3f02540f48fa79b54d5873c4f4fb09d0b`,
Canon byte count 65077. The probe earns at most public status `T` by the
proof frozen below; `verify.py` is an exact audit of the finite witnesses,
not the source of the theorem. The two-architecture gate is the local
`aarch64` record plus the required GitHub `x86_64` check; no prior
run is carried in as the public pin.

## Frozen preregistration body


```
CANDIDATE:  P-R2-SCALING-SHIFT-1
SESSION:    r2-scaling-shift-2026-07-17 (third cycle of the day; this doc
            claims it; no other session owns the scaling carrier)
DIRECTIVE:  owner "Jdi na dalsi krok" on the R2 hand-off: the noncompact
            scaling flow on L^2(K_lambda) with the boundary distribution as
            the vector, composed with the archimedean place.
TARGET:     public line on promotion. This probe carries no authority until public validation.
LAYER:      L6 (spectral type of the carrier; ladder moments).
STATUS:     candidate. Expected honest outcome, stated up front: the
            discrete-time scaling carrier FIRES as candidate-F by the toral
            mechanism (absolutely continuous type against the forced atomic
            measure); the boundary-vector ladder additionally misses the
            second Li rung by exact intervals after its one free rescale.
            If instead the gates fail, the carrier survives to the next
            junction and that is the report.
```

## 0. Currency

Same authority as the two sibling probes: Public Canon v8 ACTIVE, tag
canon-v8, CONTENT_COMMIT 208124ac, CANON.md sha eabf29bc verified by
fetch-and-hash this session. Anchors: J-LI-TORAL-HAAR-NOGO [T] (the
mechanism precedent), J-RAMIFIED-CHORD [T], PLENUM-POINT [T]. Non-public
prior-lane background: J-LI-S2-NORMAL-FORM, J-LI-S2-SPECTRAL-RIGIDITY, the
carrier-dimension row, and prior cocycle-lane pins. P-R2-LAMBDA-HAAR-1 is a
non-load-bearing sibling cross-check, not a parent or import.

## 1. Claim under test (the R2 sub-route: discrete-time scaling carrier)

There exist a vector v in L^2(K_lambda, dx) and data making the unitary
time-1 scaling map

    (U f)(x) = 5^(-1/2) f(lambda x)      on L^2(K_lambda, dx)

an exact Li witness. The primary, publicly anchored form is the cocycle
form, identical to the format of the public toral no-go:

```
cocycle form  ||sum_{k<n} U^k v||^2 = lambda_n for all n >= 1.
```

A secondary S2 form, I - U Hilbert-Schmidt with
lambda_n = (1/2) ||I - U^n||_S2^2, is also treated; its exclusion conclusion
is stated CONDITIONAL on the prior-lane S2 witness normal form, which is not
yet public, and is not load-bearing here. The unconditional, self-contained
results are the cocycle-form kill (K1, K2, K3, anchored on the public toral
no-go) and the quantitative junction miss (K4).

The canonical J-native vector is the boundary distribution v = 1_{O_lambda}
(the plenum's unit ball; ||v||^2 = vol(O_lambda) = 1). The archimedean
composite (U tensor V for any unitary V of the archimedean place) is
covered as a corollary under the same discrete-time single-unitary frame.

## 2. Frozen model

```
M1  K_lambda^* = lambda^Z x O_lambda^*; shells S_n = lambda^n O_lambda^*,
    vol(S_n) = (4/5) 5^(-n); K_lambda minus 0 is the disjoint union.
M2  U transports L^2(S_n) isometrically onto L^2(S_{n-1}) (a function on
    S_n is pulled to x with lambda x in S_n, i.e. to S_{n-1}): a bilateral
    shift n -> n-1 whose multiplicity is dim L^2(O_lambda^*) = aleph_0.
    The direction convention does not affect the Gram of M3, which is
    symmetric in j and k, nor any conclusion below.
M3  Boundary vector overlaps: <U^j v, U^k v> = 5^{-(j+k)/2}
    vol(lambda^{-j} O intersect lambda^{-k} O) = 5^{-|j-k|/2} = r^{|j-k|}
    with r = 1/sqrt5.
M4  Ladder closed form: psi(n) = sum_{j,k<n} r^{|j-k|}
    = n (1+r)/(1-r) - 2 r (1 - r^n)/(1-r)^2, exactly in Q(sqrt5).
M5  Second Li rung from the pinned chart: sigma_2 = M_1 - 2 lambda_1 and
    lambda_2 = 2 lambda_1 - sigma_2 = 4 lambda_1 - M_1.
```

## 3. Kill mechanisms (stated before computing)

```
K1 (Hilbert-Schmidt divergence, unconditional). Adjacent shells are
   orthogonal, so ||(I - U^n) e||^2 = 2 on infinitely many transported
   basis vectors for every n >= 1: ||I - U^n||_S2^2 = + infinity at every
   rung. Hence I - U is not Hilbert-Schmidt and U lies outside every
   Hilbert-Schmidt-perturbation Li witness class. (The exclusion from the
   specific prior-lane S2 normal form is the conditional secondary form;
   this HS fact is unconditional and needs no external input.)
K2 (cocycle form, all vectors). A bilateral shift has homogeneous Lebesgue
   spectral type, so EVERY vector's spectral measure is absolutely
   continuous. An assumed cocycle realization forces lambda_n >= 0, hence
   RH by Li, hence the symmetrized vector measure equals the purely atomic
   sigma_xi with atoms away from 1: the toral mechanism verbatim, now with
   Lebesgue in place of Lebesgue-off-constants. Contradiction.
K3 (composites). The spectral type of U tensor V contains the convolution
   of types; Lebesgue convolved with anything is absolutely continuous, so
   every discrete-time composite with an archimedean factor dies by K2.
K4 (boundary vector, quantitative junction; self-contained, no measure
   theory). Replacing v by c v scales the whole ladder psi(n) by |c|^2.
   psi(1) = ||v||^2 = 1 misses the pinned lambda_1 interval by a factor
   above 43. Granting the single free rescale, fixed by |c|^2 = lambda_1,
   sets rung 1 to lambda_1 exactly; then rung 2 becomes
   |c|^2 psi(2) = lambda_1 (2 + 2r), which must equal
   lambda_2 = 4 lambda_1 - M_1: the gates below decide by exact intervals
   and they are disjoint. Additionally the increments Delta psi(n)
   = 1 + 2r(1 - r^n)/(1 - r) increase strictly toward the bounded J-native
   limit phi^2 = (3 + sqrt5)/2 with gap 2 r^{n+1}/(1 - r) > 0 (the limit is
   approached, never attained), against the unbounded (1/2) log N increments
   a realization requires. This kill needs only the standard lambda_1,
   lambda_2 values and no non-public input.
```

## 4. Imports

```
I1  J-LI-TORAL-HAAR-NOGO [public T]: the LOAD-BEARING anchor. It establishes
    that a cocycle realization forces the symmetrized vector measure to the
    purely atomic sigma_xi with atoms away from 1; K2 uses exactly this.
I1b J-LI-S2-NORMAL-FORM, J-LI-S2-SPECTRAL-RIGIDITY [prior lane, NOT public]:
    used ONLY for the conditional secondary S2-form remark; not required for
    any unconditional conclusion of this probe.
I3  J-LI-CYCLIC-CARRIER-DIMENSION [prior lane, NOT public]. Conditional and
    non-load-bearing here: 1 in supp, no atom at 1. It is not required for
    K1--K4 or for any unconditional conclusion of this probe.
I4  Li's criterion [classical]; bilateral shifts have homogeneous Lebesgue
    spectrum [classical]; spectral type of tensor products by convolution
    [classical]; existence of at least one nontrivial zero [classical].
I5  prior cocycle-lane pins for gamma_1 and M_1 [prior lane]. The exact EM
    machinery and containment gates are implemented self-contained here;
    P-R2-LAMBDA-HAAR-1 is a non-load-bearing sibling cross-check only.
I6  PI-ENCLOSURE and the sqrt5 enclosure
    2236067977/10^9 < sqrt5 < 2236067978/10^9 [classical].
```

## 5. Code and environment (frozen before the code exists)

```
verifier    verify.py
            Python stdlib only; exact Q(sqrt5) pair arithmetic; exact
            Fraction interval arithmetic with locally implemented atanh-log
            machinery and EM envelopes; no float in any assertion; decimal
            prints are labeled witnesses only.
run         first formal local leg must be aarch64/arm64 after remote pin
            readback and must repeat byte-identically three times. The required
            GitHub x86_64 leg is the later public gate; neither is claimed here.
env         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

## 6. Failure threshold (gates; the package FAILS to establish if any fails)

```
S0  sqrt5 enclosure verified by exact squaring; r = 1/sqrt5 interval.
S1  overlap identity: for all 0 <= j, k <= 6, doubled exponents satisfy
    -(j+k) + 2 min(j,k) = -|j-k|, so <U^j v, U^k v> = 5^{-|j-k|/2};
    adjacent shells orthogonal (the K1 divergence datum); shell volume
    bookkeeping vol(S_n) = (4/5) 5^(-n).
S2  ladder closed form M4 verified exactly in Q(sqrt5) against the direct
    double sum for n = 1..12.
S3  increment identity Delta psi(n) = 1 + 2r(1 - r^n)/(1 - r), monotone
    increasing, with phi^2 - Delta psi(n) = 2 r^{n+1}/(1 - r) > 0 and the
    exact limit (1+r)/(1-r) = (3 + sqrt5)/2 = phi^2.
S4  spectral density of the boundary vector: the Poisson kernel with
    parameter r has value (3 + sqrt5)/2 = phi^2 at theta = 0 and
    (3 - sqrt5)/2 = phi^-2 at theta = pi, exactly in Q(sqrt5); the product
    of the two extremes is 1.
S5  junction rung 1: psi(1) = 1 lies outside (0.0230957, 0.0230958), the
    lambda_1 bracket.
S6  junction rung 2 after the free rescale, decided by exact intervals:
    recompute gamma, gamma_1, lambda_1, M_1 by the EM machinery (with the
    self-contained local containment re-gates specified above); form lambda_2
    = 4 lambda_1 - M_1 and gate lambda_2 inside (0.09234573, 0.09234574);
    gate hi( lambda_1 (2 + 2r) ) < lo( lambda_2 ). If this gate FAILS the
    rescaled boundary ladder survives rung 2 and the report says so.
S7  HS divergence bookkeeping: ||(I - U) e||^2 = 2 on every transported
    basis vector (from S1 adjacency), infinitely many per shell pair.
```

## 7. Falsifiers

```
Of the package    any gate S0..S7 fails. An S6 disjointness failure is a
                  SURVIVAL of the rescaled boundary ladder past rung 2 and
                  is reported as such, per the negative-vector discipline.
Of the route      the expected outcome: the discrete-time scaling carrier
                  fires as candidate-F in both frozen forms, composites
                  included; R2 continues only in the moment-functional
                  frame and genuinely global objects.
```

## 8. Not covered (frozen honesty)

The moment-functional (Weil positivity) frame itself; flow-trace or
distribution-pairing formalisms that are not a single unitary's ladder;
non-unitary carriers; the global adelic object read as a whole. Those are
the surviving R2 frames. The formula target for the option-b junction,

```
lambda_1^K = 1 + (3/2) log 5 - 2 log(2 pi) - gamma + sum_{chi != chi_0} L'/L(1, chi),
```

with (3/2) log 5 = 6 log s_J + 3 log phi from sqrt5 = s_J^2 phi, is
derivation-grade groundwork recorded in the PROMO with its Q-case
cross-check; the Stieltjes-Hurwitz computation that would PIN it is a named
next obligation, not part of this candidate. RH [O] throughout.

## 9. Break-it-yourself plan (post-run, recorded in the PROMO)

```
a  choose a cleverer v          K2 is all-vector: absolute continuity is a
                                property of the operator's type, not of v.
b  retune the normalization     one free rescale granted and spent at rung
                                1; rung 2 decides by intervals (S6).
c  continuous-time escape       K_lambda^* has no R-flow: the value group
                                is Z; discrete time is not a choice.
d  archimedean composite        K3: convolution keeps the type absolutely
                                continuous; covered in discrete time.
e  leave the single-unitary     that is the surviving frame, named open,
   frame                        not smuggled into the kill.
```
