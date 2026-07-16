# C-LI-TORAL-HAAR-1. The toral Haar-Koopman no-go and the forced spectral target

```
CANDIDATE ID:   C-LI-TORAL-HAAR-1
DATE:           2026-07-16
SESSION:        c-li-cocycle-1 debt-fold continuation (directed by the owner:
                "pust se do navrzene dalsi prace")
TARGET ROWS:    J-LI-TORAL-HAAR-CARRIER  (proposed F candidate: the standard
                toral Haar-Koopman realization is excluded)
                J-LI-SPECTRAL-TARGET     (proposed T as a necessary,
                RH-conditional characterization of the realization target)
PARENTS:        C-LI-COCYCLE-1 (through amendment 4); the corrected spine
                notes/j-li-schoenberg-2/; the carrier no-go
                J-LI-CYCLIC-CARRIER-DIMENSION
LAYER:          L6 measure statements about any proposed realization; the
                no-go itself is unconditional mathematics; no lift claimed
AUTHORITY:      none. NON-CANONICAL candidate document per POLICY.md.
```

## 0. What this candidate delivers

```
1. The forced symmetrized target measure: any realization of the Li ladder
   forces its symmetrized spectral measure to be sigma_xi, written in
   closed form with atoms at e^{+-i theta_gamma}, theta_gamma =
   2 arctan(1/(2 gamma)), and weights m_gamma/(gamma^2 + 1/4). Emphasis:
   only the SYMMETRIZED measure is forced (Fourier uniqueness); the
   non-symmetric mu_v is not determined (C-LI-COCYCLE-1 amend4, A2).
2. The exact accumulation law of sigma_xi at the point 1, with the
   correct factor and constant:
   M_xi(eps) = (eps/pi)(log(1/(2 pi eps)) + 1) + O(eps^2 log(1/eps)).
3. The closed no-go: an exact Haar cocycle realization on a hyperbolic
   toral automorphism cannot exist. Unconditional as a falsification of
   that proposed realization. It does not touch Pillar A itself, only its
   standard toral Haar representation.
4. Machine pins for the exact skeleton (verifier below, 5/5 PASS first
   run): Cayley dictionary, half-angle law, forced-measure dictionary on
   synthetic rational instances, character-orbit obstruction, and the
   accumulation-law calculus.
5. The prereg draft P-J-LI-TORAL-HAAR-1 (proof-first probe), BLOCKED on
   the owner's public claim per POLICY; no formal gate was executed.
```

## 1. Pins

```
verifier        verify_toral_haar_nogo.py
file sha256     da3bee431cfe807e62d03156f1d443735cc749d22245c04f3e01ab54658ec406
                (9054 bytes, pinned before its single run; 5/5 PASS first run)
stdout          stdout_toral_haar.txt
stdout sha256   0f159b0b04c874eed1677b40c3af08a99b98b17fd17863325476a8a7e2e08d0b
                (1563 bytes); exit 0, empty stderr
ENVIRONMENT     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC; Linux x86_64, Python 3.11.15; single platform
IMPORTED        Li's criterion (RH iff lambda_n >= 0 for all n >= 1);
                Fourier uniqueness of finite positive measures on T;
                the countable-Lebesgue decomposition of the Koopman
                operator of an ergodic hyperbolic toral automorphism
                (constants sector plus countable Lebesgue spectrum);
                the Riemann-von Mangoldt count N(T) = (T/2pi) log(T/(2pi e))
                + O(log T). All four are classical; none is asserted by
                the verifier, which pins only the exact skeleton.
```

## 2. The forced symmetrized target

Under RH write the nontrivial zeros as rho = 1/2 + i gamma, gamma real,
with multiplicity m_gamma. The Li map z_rho = 1 - 1/rho = (rho-1)/rho
sends the critical line to the unit circle: exactly (TH1, TH2)

```
|z_rho| = 1,   1 - z_rho = 1/rho,   |1 - z_rho|^2 = 1/(gamma^2 + 1/4),
z_rho = e^{i theta_gamma},   theta_gamma = 2 arctan(1/(2 gamma)).
```

Define the symmetrized target measure

```
sigma_xi = sum_{gamma > 0} m_gamma/(gamma^2 + 1/4)
           (delta_{e^{i theta_gamma}} + delta_{e^{-i theta_gamma}}).
```

Then, with t_n the second differences of the Li ladder (t_n =
lambda_{n+1} + lambda_{n-1} - 2 lambda_n; the c_n of the report
convention),

```
sigma_xi_hat(n) = t_n,        sigma_xi(T) = t_0 = 2 lambda_1,
lambda_n = (1/2) int_T |D_n(z)|^2 d sigma_xi(z),
           D_n(z) = sum_{k=0}^{n-1} z^k,
```

where the weight identity 1/(gamma^2 + 1/4) = 2 (1 - cos theta_gamma)
makes the three displays one exact computation (TH3 pins all of them on
synthetic rational zero multisets; the convergence of the total mass is
the classical sum over zeros of 1/|rho|^2).

Forcing. Suppose ANY unitary realization (U, v) reproduces the ladder,
||sum_{k<n} U^k v||^2 = lambda_n for all n. Its vector spectral measure
mu_v satisfies t_n = sigma_hat(n) with sigma = mu_v + iota_* mu_v
(the corrected normalization; C-LI-COCYCLE-1 amendment 4). A finite
positive measure on T is determined by its Fourier coefficients, so

```
sigma = mu_v + iota_* mu_v = sigma_xi        (exactly, forced).
```

It must be said precisely: the FORCED object is the symmetrized measure.
The non-symmetric mu_v itself is not determined by Fourier uniqueness
(amend4 A2 pins a separating instance). This candidate therefore always
says "forced symmetrized measure".

Status note. The closed form of sigma_xi presumes RH (zeros off the line
would break |z_rho| = 1 and the angular reading). J-LI-SPECTRAL-TARGET is
therefore proposed as T in the sense of a NECESSARY, RH-conditional
characterization: IF a realization exists (which forces RH, section 4),
THEN its symmetrized spectral measure is exactly sigma_xi. It is not an
unconditional description of an existing object.

## 3. The accumulation law at 1

The atoms of sigma_xi accumulate only at z = 1 (theta_gamma decreases to
0 as gamma grows). Let M_xi(eps) be the sigma_xi mass of the arc
{ |arg z| <= eps }. With theta_gamma = 2 arctan(1/(2 gamma)) the cutoff
is gamma >= 1/(2 tan(eps/2)) = 1/eps + O(eps), and with the imported
zero count dN(gamma) = (1/(2 pi)) log(gamma/(2 pi)) d gamma + d(error):

```
M_xi(eps) = 2 int_{~1/eps}^inf dN(gamma)/(gamma^2 + 1/4)
          = (1/pi) int_{1/eps}^inf log(gamma/(2 pi))/gamma^2 d gamma
            + (remainder)
          = (eps/pi) (log(1/(2 pi eps)) + 1) + O(eps^2 log(1/eps)).
```

The calculus core is exact: the antiderivative of
log(gamma/(2 pi))/gamma^2 is -(log(gamma/(2 pi)) + 1)/gamma, and its
value at gamma = 1/eps is -eps (log(1/(2 pi eps)) + 1) (TH5 pins both
coefficientwise). The replacement of gamma^2 + 1/4 by gamma^2, the
tan-versus-linear cutoff shift, and the N(T) error term all land in the
stated remainder. Both the factor eps/pi and the constant +1 are part of
the law; earlier drafts that dropped either are superseded by this form.

## 4. The no-go

PROPOSED REALIZATION (the standard toral Haar-Koopman form). X = T^2
with Haar measure; T_A the automorphism induced by a hyperbolic
A in SL_2(Z) (|tr A| > 2); U the Koopman operator on L^2(X, Haar),
unitary in the full sense U* U = U U* = I; and a cocycle vector v with

```
||sum_{k<n} U^k v||^2 = lambda_n   for all n >= 1, exactly.
```

THEOREM (no-go). No such (A, v) exists. The exclusion is unconditional:
it does not assume RH and it does not decide RH.

PROOF. Assume the realization exists.

```
(a) Positivity is structural: lambda_n = int |D_n|^2 d mu_v >= 0 for
    every n, since mu_v is a positive measure.
(b) lambda_n >= 0 for all n implies RH (Li's criterion, imported).
(c) Under RH, section 2 forces the symmetrized spectral measure:
    mu_v + iota_* mu_v = sigma_xi, a purely atomic measure whose atoms
    sit at e^{+-i theta_gamma}, all DIFFERENT from 1, accumulating at 1
    (section 3).
(d) The Koopman operator of an ergodic hyperbolic toral automorphism
    decomposes as (constants) + (countable Lebesgue spectrum), imported;
    TH4 pins the exact skeleton: no nonzero character m in Z^2 satisfies
    (A^T)^k m = m, because det(A^k - I) = 2 - tr(A^k) != 0 for all
    k >= 1. Consequently every vector's spectral measure is
    |<v, 1>|^2 delta_1 + (an absolutely continuous part), and so is its
    symmetrization: it has NO atom anywhere except possibly at 1.
(e) sigma_xi has atoms off 1 (any single gamma supplies one).
    Contradiction with (c) + (d). QED.
```

The chain in one line:

```
exact Haar cocycle => lambda_n >= 0 => RH => sigma = sigma_xi atomic
                                          => contradiction with (d).
```

Scope and formulation discipline (the corrections this candidate freezes):

```
UNITARY      means U* U = U U* = I, not merely U* U = I; Koopman
             operators of invertible measure-preserving maps satisfy the
             full form, and the spectral theorem used in (c)-(d) needs it.
CYCLIC       pure point structure is forced only on the cyclic subspace
             H_v = closed span {U^n v : n in Z}. The ambient operator may
             carry additional continuous sectors; the contradiction is
             run entirely on mu_v, which lives on H_v.
DENSITY      the bounded-density growth remark holds for a locally
             absolutely continuous spectral measure WITH bounded density
             and WITHOUT a further singular component near 1: there
             (1/2) int |D_n|^2 d sigma = O(n), while lambda_n =
             (n/2) log n + O(n) under RH (Lagarias, imported) - a second,
             independent exclusion route for such carriers. Stated with
             this exact scope; it is not needed for the theorem above.
BOUNDARY     "boundary or scattering realization" is a CANDIDATE
             architecture for what could replace the toral carrier. It is
             not a consequence of the no-go and nothing here proves any
             property of it.
SUZUKI       the model-space constructions of Suzuki (arXiv:2301.05779)
             do deliver norm identities of the required shape, but they
             consume xi itself as input; they are not J-native and do not
             satisfy the realization target. Named to prevent a false
             "already done" reading.
```

What the theorem kills and what it does not: it kills the standard
toral Haar-Koopman REPRESENTATION of Pillar A's realization target - a
natural construction path - and sharpens the target to "produce sigma_xi
where the carrier's spectral type can host atoms accumulating at 1".
It does not kill Pillar A, does not produce a realization, and moves
neither J-LI-MOMENT-BRIDGE nor RH.

## 5. Proposed ledger delta

```
J-LI-SPECTRAL-TARGET          T as a necessary, RH-conditional
                              characterization (sigma_xi closed form,
                              accumulation law)
J-LI-TORAL-HAAR-CARRIER       F candidate (this no-go; unconditional as
                              falsification of the proposed realization)
J-LI-MOMENT-BRIDGE            O (unchanged)
J-WEIL-POSITIVE-REALIZATION   O (unchanged)
RH                            O (unchanged)
```

Public registration of any of these rows requires the POLICY probe
procedure; nothing is registered by this candidate.

## 6. Break attempts

```
BR1  wrong-direction audit: the chain uses Li's criterion in the
     direction (all lambda_n >= 0) => RH, which is the theorem's hard
     direction and is imported as such, not rederived.
BR2  atom-at-1 escape: could v's measure be delta_1-only (constant
     component) and still match? No: sigma_xi has atoms off 1 (e), and a
     delta_1-only measure has bounded ladder, killed already by the
     carrier no-go (J-LI-CYCLIC-CARRIER-DIMENSION).
BR3  non-ergodic escape: a non-hyperbolic or reducible A is outside the
     stated carrier class; the no-go claims nothing about it. The class
     boundary is |tr A| > 2 on SL_2(Z), where TH4's obstruction is exact.
BR4  symmetrization escape: matching only cosine data with an asymmetric
     mu_v changes nothing - the argument runs on the symmetrization,
     which is what the ladder data forces (amend4 A2).
BR5  finite-cutoff escape: a family of finite fits for each cutoff n is
     not an all-n realization and is not classified by this no-go
     (same boundary as COCYCLE-BY-FINITE-FIT).
```

## 7. Live falsifiers

```
F-a  any exact assertion of verify_toral_haar_nogo.py failing on re-run
F-b  an explicit exact Haar cocycle (A, v) exhibited with ladder
     lambda_n for all n - this would fire the no-go itself and would be
     a mathematical event strictly larger than this candidate
F-c  an error found in either imported decomposition (Li's criterion;
     countable Lebesgue spectrum of hyperbolic toral Koopman operators)
F-d  a certified computation showing the accumulation law's constant or
     factor wrong at some eps (against a certified zero count)
```

## 8. Non-claims

The no-go narrows the realization space; it does not enter it. It is a
falsification of one natural construction path, not evidence about RH in
either direction. The spectral target characterization is conditional
exactly as stated in section 2. No public claim, probe, registration, or
Canon change is made by this candidate. J-LI-COCYCLE-REALIZATION stays
[O]. RH stays [O].

## 9. Next step

The proof-first probe P-J-LI-TORAL-HAAR-1 (draft in
P-J-LI-TORAL-HAAR-1_PREREG_DRAFT.md) with the single task: freeze the
toral carrier class, prove its spectral type, identify the forced
symmetrized Li measure, and close the contradiction. The exploratory
finite test to n = 32 may remain a sanity check; the no-go proof is
analytic. A broad P-PENTAGON-WEIL-2 is intentionally NOT proposed.
