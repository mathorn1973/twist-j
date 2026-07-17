# C-WEIL-REALIZATION-1. Exact anchors for the attack on J-WEIL-POSITIVE-REALIZATION

```
REVISION:       rev3, 2026-07-15. Changes per the owner's second verdict
                (audit; archived verbatim in section 13): ramification
                wording made exact (dim V^I_5 = 1, Z_5(s) = (1-5^-s)^-1,
                both zeta_K conventions with chi_0 principal, the 4*[5|n]
                link labeled [D] structural analogy); H_K vs H_xi = H_chi0
                sector distinction; the F row scoped as
                IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM; ledger crosswalk to
                the owner's audited J-LI-*/J-ARTIN-* names; amendment 2
                verifier (section 13) pins the corrections machine-exactly;
                provenance note on the audited external artifact
                (170cb04a..., not in this project). rev2 history follows.
                rev2, 2026-07-15. rev1 archived as
                claude/ARCHIVE_C-WEIL-REALIZATION-1_rev1.md. Changes per the
                owner verdict of 2026-07-15 (archived verbatim in section 11):
                full-plane Gauss bridge with the ramified term 4*[5|n]; the
                Gauss sign identity g(chi)g(chibar) = -5; explicit toral
                carrier T_J and period-dividing note; label corrections
                (dynamical-RH analog is D, not T); discriminant notation
                5^([K:Q]-1); scope option (a) CHOSEN; C_4 sector-identity
                requirement; five-way public split; lambda_2 gate executed
                (amendment verifier, section 12).
CANDIDATE ID:   C-WEIL-REALIZATION-1
DATE:           2026-07-15
SESSION:        pentagon-weil-anchor-1 (same session as C-PENTAGON-WEIL-1)
PARENT:         C-PENTAGON-WEIL-1 (frozen normalization xi_J = xi) and the
                public probe P-PENTAGON-WEIL-1 (G0 accounting, reproduced)
TARGET LINE:    public (mathorn1973/twist-j) on promotion; nothing promoted now
LAYERS:         pillars A and B are finite exact computations (L5 grade
                statements about the plenum); pillar C is an exact real
                interval attached to the sealed normalization; the target O
                is L6 (measure). Every lift between layers needs its own
                named gate; none is claimed here.
AUTHORITY:      none. Candidate document per the project contract.
```

## 0. Claim and scope

The owner directed an attack on the two open rows of the frozen pentagon
ledger: J-WEIL-POSITIVE-REALIZATION [O] and RH [O]. This candidate does not
close them and does not claim to. It delivers three exact anchors that give
the realization program a concrete J-native shape, and it restates the O row
with a falsifiable spine.

```
Pillar A                Algebraic core candidate-T: the toral carrier
                        T_J : T^4 -> T^4, [x] -> [M_J x], has fixed point
                        counts F_m = |det(M_J^m - I)| = N(J^m - 1) (points
                        of period DIVIDING m), a rational Artin-Mazur zeta,
                        and the exact middle-sector split (z^2 - 3z + 1)
                        * Phi_10(z). The phrase "the plenum passes its own
                        RH" is a finite dynamical analog, label D, not T:
                        the full zeta also carries the phi^{+1} and phi^{-1}
                        circles and the phi^{+-2} poles. This is not
                        automatically the zeta of the full time-driven step
                        Prod_{t_n} M_J; that lift is its own gate.
Pillar B                Strong candidate-T: finite-index M_J-invariant
                        sublattices of O_K are exactly the nonzero integral
                        ideals, because Z[J] = Z[zeta_5] = O_K; hence the
                        invariant-sublattice zeta IS zeta_K = zeta * L(chi)
                        L(chi^2) L(chi^3). The Gauss bridge holds in its
                        full-plane form with the mandatory ramified term
                        4*[5|n]. "Primes are outputs of the step" is D with
                        a strong T core (B6).
Pillar C (candidate-T)  lambda_1(xi_J) = 1 + gamma/2 - log(4 pi)/2 > 0 by
                        exact integer interval arithmetic, with no zero
                        list and no prime table. Calibration vector, not
                        progress: no finite Li prefix moves RH.
The O restated          Build a J-native positive structure whose
                        trace/moment ladder reproduces the exact lambda_n
                        ladder of xi_J, gate by gate, uniformly in n, with
                        the C_4 sector identity of section 5. Pillar A is
                        the in-house exemplar; pillar B pins what the trace
                        formula must emit; pillars C and the lambda_2 gate
                        (section 12) calibrate. RH stays [O].
```

## 1. Preregistration (candidate grade, five fields)

```
Equation           the exact statements A1-A6, B1-B6, C0-C1 exactly as named
                   in the pinned verifier (sections 2-4 below)
Code version       verify_weil_realization.py
                   sha256 44b90dd0cbb98169beca9941b37f3ba01193b3ea6897a6bf0d9a476802db6a4d
                   21101 bytes, pinned before its single execution
Dataset            none. No zero lists, no prime tables, no external data as
                   inputs to any claimed structure. Primes appear only as
                   internal verification devices (a sieve, a spot table)
                   inside finite checks, never as inputs to the constructions.
Systematics        Z[zeta_5] integer 4-tuples (j^4 reduction); Z[phi] pairs
                   with phi^2 = phi + 1; Z[zeta_20] integer 8-tuples with
                   x^8 = x^6 - x^4 + x^2 - 1; quartic character fixed by
                   chi(2) = i; exterior powers on ordered pair/triple bases;
                   charpoly convention det(zI - A) by exact integer
                   Faddeev-LeVerrier; Artin-Mazur convention
                   exp(sum N_m z^m / m); directed integer intervals at scale
                   S = 10^18. Imported brackets: Machin formula with
                   alternating-tail bracketing; the harmonic bracket
                   1/(2(N+1)) < H_N - ln N - gamma < 1/(2N); atanh series
                   with geometric tail bound.
Failure threshold  any single exact assertion FAIL fires the falsifier of
                   its pillar; thresholds never move.
```

Sequence disclosure, for honesty of the freeze: a hand derivation and one
scratch computation pass preceded the freeze of the verifier (the expected
constants in the assertions were derived first, then frozen). The pinned
file then ran exactly once and returned all PASS on that first run. Single
platform (Linux x86_64, Python 3.11.15, runtime 1.8 s, exit 0, empty
stderr). Candidate grade; two-architecture byte identity is deferred to
public validation.

```
stdout sha256      fcd03da7ff8240aab49281ad3abf823ae641fa3dc8373788491c85a53b1ed812
                   2164 bytes (Appendix B)
environment        LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

## 2. Pillar A. The plenum's own zeta function

The step operator of the axiom, (a,b,c,d) -> (a-c+d, b-c, a, b-c+d), is
multiplication by J on the plenum lattice Z^4 = Z[zeta_5] (A1, exhaustive
box check). The carrier is explicitly the toral automorphism

```
T_J : T^4 -> T^4,   [x] -> [M_J x],
```

and its periodic structure defines the Artin-Mazur zeta

```
zeta_plenum(z) = exp( sum_{m>=1} F_m z^m / m ),
F_m = # Fix(T_J^m) = |det(M_J^m - I)| = N(J^m - 1),
```

where F_m counts points of period DIVIDING m, not exact period m; the last
equality holds by two independent code paths for m = 1..30 (A3; the
determinant is positive outright because the eigenvalues come in complex
conjugate pairs). The counts begin 1, 11, 31, 55, 121, 341, 911, 2255,
5611, 14641, ... and F_1 = 1 anchors aperiodicity (the origin is the only
fixed point). Standard reference for dynamical zeta functions of toral
endomorphisms via exterior powers and |det(I - M^m)|: Baake, Lau,
Paskunas, arXiv:0810.1855 (owner-provided pointer; pin the citation at
probe time). Caveat: this is the zeta of the autonomous step M_J, not
automatically of the full time-driven product Prod_{t_n} M_J of the
Thue-Morse stream; that lift is its own named gate.

The zeta is the rational function (A6, exact series identity to order 16;
the rational-function formalism is the Lefschetz trace formula, imported):

```
zeta_plenum(z) = (1 - 3z + 4z^2 - 2z^3 + z^4)(1 - 2z + 4z^2 - 3z^3 + z^4)
                 -----------------------------------------------------------
                 (1 - z)^2 (1 - 3z + z^2)(1 - z + z^2 - z^3 + z^4)
```

The weight structure is rigid and fully exact (A4, A5):

```
0-form and 4-form sector   weight 1 (the two (1-z) factors)
1-form and 3-form sectors  the conjugates of J and their inverses,
                           moduli {phi, phi, phi^-1, phi^-1} each
2-form (middle) sector     charpoly z^6 - 4z^5 + 5z^4 - 5z^3 + 5z^2 - 4z + 1
                           = (z^2 - 3z + 1) * Phi_10(z), palindromic:
                           the hyperbolic area classes phi^2 and phi^-2
                           (exact roots of z^2 - 3z + 1, product 1, sum 3),
                           and four eigenvalues that are EXACTLY the
                           primitive 10th roots of unity: mu_i mu_j = -zeta^k
                           for the mixed pairs, verified in Z[zeta_5].
```

The middle-sector rigidity is exact and machine-checked (T core): the
nontrivial middle spectrum lies exactly on the unit circle and is moreover
torsion (primitive 10th roots, the 2p argument cycle); the off-circle
middle classes are exactly the hyperbolic pair phi^{+-2}, whose logarithm
is the sealed entropy 2 log phi (the dominant pole of zeta_plenum at
z = phi^-2 gives F_m ~ phi^{2m}). The palindromy of the middle factor is
the symmetry z <-> 1/z. Total product of the 1-form eigenvalues is
N(J) = 1 (A5).

Label discipline (owner verdict 2026-07-15): the summary phrase "the
plenum passes its own RH" is a finite dynamical ANALOG and carries label
D, not T. The full Artin-Mazur zeta also carries the phi^{+1} and phi^{-1}
circles (1-form and 3-form sectors) and the phi^{+-2} poles; only the
mixed 2-form sector statement (exactly the primitive 10th roots) is clean
T. What remains true and useful for the O: the weight rigidity is DERIVED
from a declared architecture (hyperbolicity of the step, duality of the
torus, unimodularity N(J) = 1), with nothing about zeros imported. G6
demands that phenomenon one layer up. The gap between the layers is the
whole problem, and it is named, not hidden (F-guard in section 5, and the
public no-go probe P-J-FINITE-DILATION-NOGO-1 in section 9: a finite
rational dynamical determinant cannot BE xi, whose divisor is infinite).

Note (D, elementary, imported Lucas-style theory): the rank of apparition
governs which primes enter the periodic spectrum: p | N_m iff the order of
J in the residue field at a prime above p divides m. The B7 witness line in
the verifier output shows every prime factor of N_1..N_12 is 5 or 1 mod 5;
higher m admit the other classes when their orders arrive. The periodic
points of the plenum meet the split primes first.

## 3. Pillar B. The plenum's ideal zeta and the Gauss bridge

The strongest result of this candidate (owner verdict: strong
candidate-T), boxed:

```
finite-index M_J-invariant sublattices of O_K  =  nonzero integral ideals
of O_K, exactly, because Z[J] = Z[zeta_5] = O_K
```

(invariance under M_J makes a sublattice a Z[J]-module; J = 1 + zeta^2
generates the full ring of integers since zeta = (zeta^2)^3; standard
ideal-norm zeta formalism per Kedlaya's Dedekind zeta notes,
owner-provided pointer). Counting them is therefore the Dedekind zeta of
K = Q(zeta_5), the J-native origin of the arithmetic side, and it factors
over the mod-5 characters:

```
zeta_inv(s) = zeta_K(s) = zeta(s) L(s,chi) L(s,chi^2) L(s,chi^3),
a_K = 1 * chi * chi^2 * chi^3   (Dirichlet convolution),
disc K = 125 = 5^3 = 5^([K:Q]-1)   (B1, exact: prod (zeta^i - zeta^j)^2)
```

Notation frozen per owner verdict: the discriminant is written
5^([K:Q]-1), NOT p^d, because d is reserved elsewhere for the
three-dimensional carrier. (The pinned rev1 verifier's B1 label string
still reads "p^d"; the pin is immutable, the notation rule binds all new
text.)

Machine-exact at finite range (B2, B4, B5, B6):

```
B4  a_K(n) is real, integral, nonnegative for all n <= 3000, and matches
    the splitting law on 18 spot values (including a_K(11) = 4,
    a_K(121) = 10, a_K(361) = 2, a_K(16) = 1, a_K(605) = 10).
B5  the von Mangoldt bookkeeping of zeta_K holds exactly as identities of
    integer vectors over log-prime symbols for all n <= 3000:
    sum_{d|n} Lambda_K(d) a_K(n/d) = a_K(n) log n, with Lambda_K generated
    from the splitting law (5: log 5; p = 1 mod 5: 4 log p; p = 4 mod 5:
    4 log p at even exponents; p = 2,3 mod 5: 4 log p at exponents
    divisible by 4). Two independent paths: splitting law vs character
    convolution. No floats; log p is a formal symbol.
B6  degree-1 primes are the step operator's invariant hyperplanes: the
    number of roots of Phi_5 mod p equals a_K(p) for every prime p < 200,
    including the ramified p = 5. The prime data comes out of the step
    operator; no prime table goes in.
```

The Gauss bridge, FULL-PLANE FORM (mandatory correction, owner verdict
2026-07-15; machine-checked in the amendment verifier, AM1-AM3): with
g(chi^j) = sum_a chi^j(a) zeta_5^a,

```
4 zeta_5^n = 4*[5|n] + sum_{j=0}^{3} chibar^j(n) g(chi^j)   for ALL n,
g(chi^j) conj(g(chi^j)) = 5   for j = 1, 2, 3,    g(chi^0) = -1,
g(chi) g(chibar) = chi(-1) * 5 = -5   (odd quartic character),
conj(g(chi)) = chi(-1) g(chibar),     g(chi^2)^2 = +5 (even character).
```

The restricted identity without the 4*[5|n] term holds only for 5 not
dividing n; at n = 5 the left side is 4 and the uncorrected right side is
0 (AM2, asserted as a negative control). This is not cosmetic: the
multiplicative DFT is blind to the ramified class 0 mod 5, which is why
the semilocal {infinity, 5} block is MANDATORY in any realization
bookkeeping.

Ramification, exact wording (owner audit, fix 4): this is not
"one-dimensional ramification"; precisely, dim V^{I_5} = 1 (the inertia
invariants of the induced packet are the chi_0 line; machine-pinned as
rank(P - I) = 3 in AN4) and the local factor is Z_5(s) = (1-5^{-s})^{-1}.
Both conventions are frozen and machine-verified equal (AN4, n <= 500):

```
zeta_K(s) = zeta(s) prod_{r=1..3} L(s, chi_r)
          = (1 - 5^{-s})^{-1} prod_{r=0..3} L(s, chi_r),
```

with chi_0 the principal Dirichlet character mod 5 in the second form.
The link between this local block and the additive term 4*[5|n] of the
bridge is a STRUCTURAL ANALOGY, label [D], not an identical local
identity; the counterfeit 5^m tower of the G0 probe lives at the same
place, which motivates but does not prove the identification.

The additive pentagon root filter (the carrier of C-PENTAGON-WEIL-1 and of
the public probe P-PENTAGON-WEIL-1) and the multiplicative character
decomposition of zeta_K are the same data away from the ramified class,
linked with weight exactly 5 = p, plus the explicit ramified term. This
fixes the dictionary between the G0 normalization and the plenum field's
L-functions.

Scope decision: OPTION (a) CHOSEN by the owner, 2026-07-15.

```
The main O stays J-WEIL-POSITIVE-REALIZATION over W_xi. The zeta_K form
is a different, broader commitment (its positivity would settle the whole
mod-5 Dirichlet packet, strictly stronger than RH) and must never be
silently substituted for W_xi.

Frozen bridge requirement (C_4 SECTOR IDENTITY): any realization built on
the plenum field must be C_4-equivariant, H_K = direct sum over chi in
C_4-hat of H_chi, with the named target sector H_xi = H_chi0, and the
TRIVIAL SECTOR must exactly reproduce, each as its own named check:
  1. W_xi itself,
  2. Lambda(n) including p = 5,
  3. the standard archimedean term,
  4. the poles and trivial zeros.
Sector precision (owner audit, fix 5): exact positivity of the WHOLE
zeta_K form would already imply RH for zeta; what it does not supply is
the identity with W_xi or the construction of the trivial sector, which
is why the sector identity is the requirement, not total positivity
alone. The quartic sectors chi and chibar pair because of the real
structure and real moments, not because of positivity. Without the
sector identity, positivity of the total form can mask a negative trivial
sector, and any claimed positivity is void for RH.
```

## 4. Pillar C. The first vector of the wall, exact

```
lambda_1(xi_J) = sum_rho 1/rho = 1 + gamma/2 - log(4 pi)/2
              in [23095708964233559, 23095708972138893] * 10^-18
              (width 7.9e-12), strictly positive.                      (C1)
```

Derivation path is zero-free and prime-free: gamma by the harmonic bracket
at N = 10^5 and N = 2 * 10^5 with an overlap consistency gate (C0); pi by
Machin with alternating-tail brackets; log(4 pi) by the atanh series with a
geometric tail bound; all in directed integer interval arithmetic at scale
10^18. Imported classical facts: the bracket inequalities; zeros pair
rho <-> conj(rho) with 0 < Re rho < 1, so lambda_1 > 0 holds unconditionally
(each pair contributes 2 Re rho / |rho|^2); RH is equivalent to lambda_n >= 0
for ALL n (Li; Bombieri-Lagarias), so this rung is evidence of nothing
beyond itself: it is the pipeline, exact, with the Gamma, pi, and pole
bookkeeping of xi_J emitted correctly and no spectrum imported.

The constants gamma and log(4 pi) enter exactly through the archimedean and
pole terms of the explicit formula, i.e. pillar C exercises the G4-grade
bookkeeping of the sealed normalization at the first Li vector.

## 5. The O row, restated with a falsifiable spine

```
J-WEIL-POSITIVE-REALIZATION [O], restated.
Deliver a J-native object: an operator H_J >= 0, or a positive measure
nu_J, or a canonical system, constructed from the declared architecture
(plenum lattice, step operator, pentagon filter, entropy 2 log phi), with
no zeta, no zero list, no prime table, and no standard Weil form as input,
such that its trace/moment ladder reproduces the exact Li ladder of xi_J:

    gate n:   lambda_n(construction) = lambda_n(xi_J)
              as exact rational intervals, one named gate per n.

Falsifier: the first n where the construction's ladder leaves the exact
interval of lambda_n(xi_J), or any admissible vector with negative form
value before G2-G4 close (kills the construction, not RH; the frozen
negative-vector discipline applies). Matching every n is RH-hard
(Bombieri-Lagarias, imported); no finite prefix is ever more than C-grade.

Uniformity clause (owner verdict): the only real hit on the G5 wall is a
UNIFORM construction positive for ALL n simultaneously (public id
J-LI-ALL-N [O]), C_4 sector-resolved per section 3 if it routes through
the plenum field: the trivial sector must itself reproduce W_xi, Lambda(n)
including p = 5, the archimedean term, and the poles and trivial zeros.
Finite prefixes are calibration and falsification instruments only.
```

Guard rows:

```
F-guard PLENUM-RH-AS-RIEMANN-RH      claiming pillar A settles anything
                                     about zeta is falsified by definition:
                                     it is a renaming across layers. The
                                     lift IS the open problem.
F IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM  scoped per owner audit (fix 3): only
                                     the unexponentiated additive branch
                                     sum_chi L(s,chi) != zeta_K (or a single
                                     trace F_l) is dead; the determinant and
                                     exp-trace packaging det(I-xF)^{-1} =
                                     exp(sum Tr(F^m) x^m/m) and L(s,+chi) =
                                     prod L(s,chi) are standard identities
                                     (machine-pinned, AN3: first coefficient
                                     divergence of the additive sum at
                                     n = 16, agreement at n = 11).
F RAW-P0-WITHOUT-FILTER-SUBTRACTION  inherited from the frozen ledger.
F RENAMED-STANDARD-WEIL-AS-NEW-PROOF inherited from the frozen ledger.
```

Name crosswalk: the uniform target named J-LI-ALL-N in rev2 is the row the
owner's audited ledger names J-LI-COCYCLE-REALIZATION [O]. Same
obligation: one J-native uniform positive construction for the whole
ladder. The audited names bind from rev3 on.

## 6. Break attempts (contract item 4)

```
BR1  character-choice trap: rebuilt a_K with chi(2) = -i instead of +i;
     identical through n = 2500. The triple product is choice-invariant.
BR2  untabled tower poke: p = 7 (order 4 mod 5): a_K(7) = a_K(49) =
     a_K(343) = 0 and a_K(2401) = 1, as the splitting law demands.
BR3  sensitivity control: corrupting one Lambda_K rule (p = 4 mod 5 at odd
     exponents) is detected by the B5 identity at the first affected n.
     The identity is not tautological.
BR4  corrupting one entry of M_J breaks the A2 assertion; the dynamical
     asserts are sensitive.
BR5  the imported harmonic bracket checked at N = 10, 100, 1000 (float
     witness only): gamma inside every bracket.
BR6  float cross-check of lambda_1 (witness only): 0.023095708966121,
     inside the pinned exact interval.
Sequence risk (self-declared): the scratch pass preceded the freeze, so
     the freeze could in principle have been fitted to a bug reproduced in
     both passes. Mitigations: two-path assertions inside the verifier
     (A3, B5, B6), independent re-derivations (A4 hand vs machine), and
     the negative controls BR3, BR4. Public validation re-runs everything
     on a second architecture.
```

Nothing broke.

## 7. Live falsifiers, candidate scope

```
F-a  any m with det(M_J^m - I) != N(J^m - 1), or any N_m <= 0
F-b  any n <= 3000 with a_K(n) negative, non-integral, or violating B5
F-c  any prime p < 200 with root count of Phi_5 mod p != a_K(p)
F-d  a correct evaluation showing lambda_1 outside the pinned interval
     (would fire on the interval machinery, not on positivity)
F-e  for the restated O: the ladder falsifier of section 5
```

## 8. Gate map after this candidate

```
G0  closed (C-PENTAGON-WEIL-1; public probe P-PENTAGON-WEIL-1 reproduced)
G1  closed as accounting (ibid.)
G2  open: freeze of the five Weil-form conventions still pending
G3  open globally; pillar B pins the exact arithmetic side the trace
    formula must emit (zeta_K bookkeeping to n = 3000, extendable)
G4  open globally; pillar C and the lambda_2 gate emit the
    archimedean/pole constants exactly at the first two Li vectors
    (lambda_2 sits at G3/G4 per the owner verdict, not at G5)
G5  open: the wall, untouched. Two rungs (n = 1, 2) machine-pinned
    positive, both unconditional classically, zero evidence for RH by
    themselves; only a uniform all-n construction (J-LI-ALL-N) with the
    C_4 sector identity would hit the wall
G6  open: pillar A is the in-house existence proof of the demanded
    phenomenon one layer down; the lift is the entire problem
RH  [O], untouched
```

## 9. Promotion posture

No fold by this document. Public decomposition FROZEN per owner verdict
2026-07-15 (A and B are two different zetas with no proven lift and must
not share one probe):

```
1. P-J-CARRIER-IDEAL-ZETA-1   invariant sublattices, zeta_K, splitting,
                              Gauss bridge WITH the 4*[5|n] ramified term
2. P-J-TORAL-ZETA-1           periodic points, Artin-Mazur zeta, exterior
                              powers, the mixed Phi_10 sector
3. P-J-FINITE-DILATION-NOGO-1 the falsifier row: a finite rational
                              dynamical determinant cannot be xi, whose
                              divisor is infinite
4. J-LI-LAMBDA-2              the calibration interval gate (executed at
                              candidate grade in section 12; G3/G4, not G5)
5. J-LI-ALL-N [O]             the single uniform positive construction for
                              the whole ladder; the only real hit on the
                              wall
```

## 11. Owner verdict of 2026-07-15 (archived verbatim)

Archived copy: OWNER_VERDICT_2026-07-15.md, sha256
55ffde279b0e34d5018fe662f8a4c1d9346f6aef38db9065d50517c8a2a8462f, 5948
bytes (standalone UTF-8 file, trailing newline; hash pins this session's
transcription). Summary of the binding content, all applied in this rev2:
scope option (a) chosen; full-plane Gauss bridge mandatory; Gauss sign
identities distinguished; T_J carrier and period-dividing explicit; the
dynamical-RH phrase downgraded to D; invariant-sublattice = ideals kept as
strong candidate-T with the Z[J] = O_K reason; discriminant notation
5^([K:Q]-1); C_4 sector-identity requirement; lambda_2 convention and
formula frozen with the sign of -2 gamma_1 as the critical falsifier;
five-way public decomposition; verdict that the three pillars are anchors,
not a crack in G5.

## 12. Amendment 1: corrected bridge and the lambda_2 calibration gate

```
verifier        verify_weil_realization_amend1.py
file sha256     d3e82c432dee8833367aa8d29259e84a145a33bae49887bcdbf869efa501686e
                10483 bytes, pinned before its single execution; all PASS
                on the first run; runtime 0.7 s, exit 0, empty stderr
stdout sha256   94237d8051f3aabe2b48b017cc3f728027a1aba8fb9b8237af62638ecd0f40a3
                1238 bytes
environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC; Linux x86_64, Python 3.11.15
```

Frozen statements and results (6 of 6 PASS):

```
AM1  full-plane bridge 4 zeta_5^n = 4*[5|n] + sum_r chibar^r(n) g(chi^r),
     n = 1..15, exact in Z[zeta_20].
AM2  negative control: uncorrected right side is 0 at n = 5 against left
     side 4; restricted identity regression for 5 not dividing n.
AM3  g(chi) conj(g(chi)) = 5 but g(chi) g(chibar) = chi(-1)*5 = -5 (odd
     quartic); conj(g(chi)) = chi(-1) g(chibar); g(chi^2)^2 = +5.
AM4  symbolic reduction, exact vector algebra: lambda_2 = 2 lambda_1 -
     sum_rho 1/rho^2 = 1 + gamma - gamma^2 - 2 gamma_1 + pi^2/8 -
     log(4 pi), under the frozen convention zeta(1+t) = 1/t + gamma -
     gamma_1 t + O(t^2). Imported: sum_rho 1/rho^2 = 1 + gamma^2 +
     2 gamma_1 - pi^2/8.
AM5  gamma_1 strictly negative by an elementary two-sided bracket:
     f(x) = ln x / x decreasing for x >= 3, A_N = sum_{k<=N} f(k) -
     ln^2(N)/2, then A_N - f(N) <= gamma_1 <= A_N for N >= 4 (telescoping
     of t_k = f(k) - int_{k-1}^k f in (f(k) - f(k-1), 0)). At N = 10^5,
     directed integer intervals:
     gamma_1 in [-0.072873410205792217, -0.072758280940973182]
     (reference -0.0728158454836767 inside). The critical falsifier of
     the frozen lambda_2 formula, the sign of -2 gamma_1, is settled:
     strictly negative gamma_1, so -2 gamma_1 > 0.
AM6  lambda_2(xi_J) in [0.092230606084387762, 0.092460864725386214],
     strictly positive (reference 0.09234573522804... inside).
     Calibration gate at G3/G4, explicitly NOT a G5 result; no finite Li
     prefix is progress toward RH.
```

The rev1 pinned verifier (44b90dd0..., 14 assertions) and its stdout stay
immutable and valid; the amendment adds gates, it does not amend pins.
Full amendment stdout:

```
PASS AM1 full-plane bridge 4 zeta_5^n = 4*[5|n] + sum_r chibar^r(n) g(chi^r), n = 1..15, exact in Z[zeta_20]
PASS AM2 uncorrected right side is 0 at n = 5 (left side 4): the multiplicative DFT is blind to the ramified class; restricted identity regression for 5 not dividing n
PASS AM3 g(chi)conj(g(chi)) = 5 but g(chi)g(chibar) = chi(-1)*5 = -5 (odd quartic); conj g(chi) = chi(-1) g(chibar); g(chi^2)^2 = +5
PASS AM4 lambda_2 = 2 lambda_1 - sum 1/rho^2 reduces exactly to 1 + gamma - gamma^2 - 2 gamma_1 + pi^2/8 - log(4 pi) (imported: sum 1/rho^2 = 1 + gamma^2 + 2 gamma_1 - pi^2/8; convention zeta(1+t) = 1/t + gamma - gamma_1 t + O(t^2))
PASS AM5 gamma_1 strictly negative: elementary bracket A_N - f(N) <= gamma_1 <= A_N at N = 10^5, directed integer intervals; the sign that the lambda_2 falsifier watches
AM5 witness gamma_1 in [-72873410205792217, -72758280940973182] * 10^-18 (reference -0.0728158454836767)
PASS AM6 lambda_2(xi_J) > 0 by exact interval assembly (calibration gate, G3/G4 bookkeeping; NOT a G5 result; no finite Li prefix is progress toward RH)
AM6 witness lambda_2 in [92230606084387762, 92460864725386214] * 10^-18 (reference 0.09234573522804...)
FAILED: none
VERDICT: PASS amendment 1 of C-WEIL-REALIZATION-1
```

## 13. Second owner verdict (audit) and amendment 2

Archived verbatim: OWNER_VERDICT_2_2026-07-15.md, sha256
cce48fbd204511850708fbeee299503cb72759decf9a829fa9701ee86b4845e4, 3844
bytes; project copy claude/OWNER_VERDICT_2_C-WEIL-REALIZATION-1_2026-07-15.md.

PROVENANCE NOTE, stated plainly. The audited verdict reports a verifier
with source sha256 170cb04a...61bb8f, stdout 1dff8214...992e3, 6/6 PASS on
x86_64 and aarch64 (Python 3.12.3), containing gamma, gamma_1 AND
determinant bounds, and an audited ledger with rows J-LI-CND-EQUIVALENCE,
J-LI-TOEPLITZ-EQUIVALENCE, J-LI-COCYCLE-NORMAL-FORM,
J-ARTIN-FROBENIUS-DETERMINANT, J-ARTIN-SYMMETRIC-FOCK,
J-PHI10-SCHOENBERG-EXEMPLAR, J-LI-SCHOENBERG-2. None of these pins or
documents match any artifact of this session (pins here: 44b90dd0/fcd03da7,
d3e82c43/94237d80, 38c0f823/2c5d8171), and a full project scan
(2026-07-15) finds no CND, Schoenberg, Toeplitz, cocycle, or Fock candidate
document and no file hashing to 170cb04a. The audited artifact is a
parallel lane (owner-side or another session) not yet deposited in this
project. Per contract (one owner per candidate, no claims without the
artifact), this document records the audited ledger as OWNER-SIDE rows,
claims none of them, and requests deposit of the 170cb04a verifier and the
CND/cocycle candidate doc into the project or a repo path so this lane can
third-run and cross-check them. The five mandatory corrections themselves
are adopted and, where verifiable inside this lane, machine-pinned below.

Owner-audited ledger, recorded (not claimed by this session):

```
J-LI-CND-EQUIVALENCE            T after the complex-equation fix
J-LI-TOEPLITZ-EQUIVALENCE       T
J-LI-COCYCLE-NORMAL-FORM        T as equivalence
J-ARTIN-FROBENIUS-DETERMINANT   T
J-ARTIN-SYMMETRIC-FOCK          T
J-PHI10-SCHOENBERG-EXEMPLAR     T algebraically, D as model of the wall
J-LI-SCHOENBERG-2               two-architecture PASS, candidate-T-ready
J-LI-COCYCLE-REALIZATION        O   (the uniform target; = J-LI-ALL-N)
RH                              O
```

Amendment 2 verifier (this lane, machine-exact pins for the corrections):

```
verifier        verify_weil_realization_amend2.py
file sha256     38c0f823298e1ca32458b5a1f3c2aaae9d72fbfd3761991bc00c1b37f47a7fc1
                11836 bytes, pinned before its single run; 6/6 PASS on the
                first run; 0.1 s, exit 0, empty stderr
stdout sha256   2c5d81710f36c61f37d497932e27b4a609783167812389c64a65a72c7b9de540
                1153 bytes
environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC; Linux x86_64, Python 3.11.15
project copy    claude/C-WEIL-REALIZATION-1_verifier_amend2.py
```

```
AN1  corrected complex CND identity (owner fix 1): for zero-sum complex a,
     sum a_k conj(a_l) (1 - cos((k-l)theta)) = -(1/2)(|A+|^2 + |A-|^2),
     exact (doubled) in Z[zeta_20] at theta = 2 pi/10 (the Phi_10 angle),
     four vectors; the value is self-conjugate. PASS
AN2  scoping control: the single-modulus form FAILS for two genuinely
     complex vectors and HOLDS for the real vector. The correction is
     necessary and exactly scoped: single modulus is the real-coefficient
     special case. PASS
AN3  owner fix 3 pinned: det/exp-trace packaging is an identity (order 16,
     exact Fractions; Artin factorization 1 - x^4 = prod(1 - i^k x) in
     Z[i][x]); the additive sector sum is the only dead branch, first
     coefficient divergence at n = 16 (4 vs a_K = 1), agreement at n = 11.
     PASS
AN4  owner fix 4 pinned: the two zeta_K conventions agree as coefficients
     to n = 500 (chi_0 principal); dim V^I_5 = 1 via rank(P - I) = 3.
     PASS
AN5  owner fix 2 frame: L_N unimodular (det = 1, N <= 8), so
     K_N = (1/2) L_N T_{N-1} L_N^* is an invertible congruence and
     K_N >= 0 iff T_{N-1} >= 0 (Sylvester, imported); K_2 <-> T_1. The
     full K_N/T_{N-1} definitions bind once the parallel candidate doc is
     deposited. PASS
AN6  regression: the amendment-1 full-plane bridge holds, n = 1..10. PASS
```

Additional frozen conventions received from the audit, recorded for the
future CND lane: state the zero pairing with multiplicities and absolute
convergence under RH for each fixed n; the converse direction runs through
the two-point test and the Li criterion.

Public-pin status per the audit: the computational part of the audited
artifact satisfies the two-architecture condition and is candidate-T
grade, not public T: no registration exists yet and the corrected
RESULT.md must be re-pinned. No public registration or repository change
was made by the owner or by this session.

## 14. Third owner verdict (2026-07-15) and rev4 corrections

Archived verbatim: OWNER_VERDICT_3_2026-07-15.md, sha256
66ba8b0eb3f0c7021ef34083de279ab20e8b38e95d0cc80eb445c9b79851bebc, 3460
bytes; project copy claude/OWNER_VERDICT_3_C-WEIL-REALIZATION-1_2026-07-15.md.
Binding content applied here:

ERRATUM to the AN3 label (fix 3 wording). The pinned amendment-2 file is
immutable and its in-code assertions were value-correct, but the label
word "first" overclaims. Corrected ledger sentence, binding from rev4:

```
Among the selected unramified prime powers the first distinguishing
witness used is n = 16 (b = 4 against a_K = 1, with agreement at the
split prime 11); as global Dirichlet series the additive sum and zeta_K
diverge earlier: already b(1) = 4 against a_K(1) = 1, b(5) = 0 against
a_K(5) = 1 without the ramified block, and b(6) = 4 against a_K(6) = 0.
```

Machine pins for the corrected sentence live in the successor candidate
(C-LI-COCYCLE-1, gate CO5).

STATUS PRECISION (audit): AN1, AN3, AN4 and their kin are finite-range
machine audits; the T grade belongs to the algebraic identities they
audit (the two-modulus CND display, K_N = (1/2) L_N T_{N-1} L_N^*, the
det/exp-trace identity, the Artin factorization). No finite verifier run
is itself the theorem.

PROVENANCE CLOSURE: the owner unified the parallel lane in a permanent
Library folder, TWIST - J/J-LI-SCHOENBERG-2/ (corrected candidate rev3,
verifier 170cb04a..., stdout 1dff8214..., SHA256SUMS, git patch), with a
repo-ready local branch agent/j-li-schoenberg-2-incubation (base
6bb013ba = canon-v6 head, commit 913d1ea6, patch sha 68056050...),
UNPUSHED pending an authenticated gh. Owner-side checks all PASS
(SHA256SUMS, verifier = EXPECTED, both architectures 6/6, byte-identical
stdout, POLICY, CANON v6 176 claims, LEDGER, 38 unit tests, git diff
--check). This session's independent third-run remains pending until the
branch is pushed or the files land in this project's document list
(Library folders are not visible to this session's project tools;
checked 2026-07-16). Per the owner's rule, no historical run will be
retroactively formalized: the public probe requires a new PREREG and a
new pin before its first public run.

The continuation directed by the owner (the J-native uniform cocycle)
is executed in the successor candidate claude/C-LI-COCYCLE-1.md.

## Appendix A. Pinned verifier source

sha256 44b90dd0cbb98169beca9941b37f3ba01193b3ea6897a6bf0d9a476802db6a4d (21101 bytes)

The source is stored alongside this document in the session workspace and
reproduced in the project as part of this candidate's record; it is 480
lines and stdlib-only. Reproduce by byte-identical copy and run under
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

## Appendix B. Pinned verifier stdout (sha256 fcd03da7ff8240aab49281ad3abf823ae641fa3dc8373788491c85a53b1ed812, 2164 bytes)

```
PASS A1 axiom step (a,b,c,d)->(a-c+d, b-c, a, b-c+d) equals multiplication by J, exhaustive box +-2
PASS A2 charpoly(M_J) = z^4 - 3z^3 + 4z^2 - 2z + 1, det = 1, trace = 3
PASS A3 N_m = det(M^m - I) = N(J^m - 1) > 0, two independent code paths, m = 1..30; N_1 = 1
PASS A4 charpoly(Lambda^2 M) = z^6-4z^5+5z^4-5z^3+5z^2-4z+1 = (z^2-3z+1)*Phi_10(z), palindromic; charpoly(Lambda^3 M) = reciprocal of charpoly(M)
PASS A5 weights exact: {phi^2, phi^-2} solve z^2-3z+1, product 1, sum 3; mixed 2-form eigenvalues are -zeta^k (primitive 10th roots); total product N(J) = 1
PASS A6 Artin-Mazur zeta of the plenum step is the rational function (charM * charL3) / ((1-z)^2 * charL2), exact series match to order 16
PASS B1 disc Q(zeta_5) = prod (zeta^i - zeta^j)^2 = 125 = 5^3 = p^d, exact in Z[zeta_5]
PASS B2 quartic character mod 5: multiplicative, orthogonality sum_j chi^j(a) = 4[a=1], exact in Z[i]
PASS B3 Gauss sums: |g(chi^j)|^2 = 5 exactly in Z[zeta_20]; g(chi^0) = -1; bridge 4 zeta_5^n = sum_j chibar^j(n) g(chi^j)
PASS B4 a_K = 1*chi*chi^2*chi^3 is real, integral, nonnegative through 3000; 18 spot values match the splitting law exactly
PASS B5 Lambda_K * a_K = a_K log identity exact over log-prime symbols for all n <= 3000 (splitting-law path vs character path)
PASS B6 invariant hyperplanes of M_J mod p (roots of Phi_5) = a_K(p) = degree-1 primes, all p < 200 including p = 5
B7 witness N_1=1=; N_2=11=11(r1); N_3=31=31(r1); N_4=55=5(r0)*11(r1); N_5=121=11^2(r1); N_6=341=11(r1)*31(r1)
B7 witness N_7=911=911(r1); N_8=2255=5(r0)*11(r1)*41(r1); N_9=5611=31(r1)*181(r1); N_10=14641=11^4(r1); N_11=39161=39161(r1); N_12=104005=5(r0)*11(r1)*31(r1)*61(r1)
PASS C0 gamma intervals from N = 1e5 and N = 2e5 overlap (bracket consistency)
PASS C1 lambda_1(xi_J) = 1 + gamma/2 - log(4 pi)/2 > 0, exact integer interval, width < 2e-9, no zeros imported
C1 witness lambda_1 in [23095708964233559, 23095708972138893] * 10^-18 (approx 0.0230957089...)
C1 witness gamma    in [577215664897758041, 577215664913568443] * 10^-18
C1 witness log(4pi) in [2531024246969290658, 2531024246969290922] * 10^-18
FAILED: none
VERDICT: PASS all exact anchors of C-WEIL-REALIZATION-1
```
