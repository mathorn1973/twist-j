# TWIST-J at Public Canon v109: a thematic synthesis

**NON-CANONICAL.** This note is a reading aid written during the 2026-11-07
consolidation. It creates no claim, status, scope, dependency, gate or
evidence. Every status below is copied from `canon/REGISTRY.tsv` at
`main` `d4d3637` (Public Canon v109, tag `canon-v109`); every registered
scope is the one in the registry, and where this note is shorter or looser
than the registry, the registry wins. Authority is declared only by
`STATUS.md`.

The note answers three questions: what TWIST-J posits, what it has
established, and what has died or stays open. It is organized by physics
theme, not by Canon section or by release.

## 1. The bet

TWIST-J tests one risky hypothesis: physical reality is a closed, exact,
deterministic integer system, and continuum, geometry, probability and fields
are readings of it. Its single algebraic axiom is `J = 1 + zeta_5^2`. The
house rules are part of the bet: exact arithmetic, preregistration before
computation, byte-identical output on two architectures for computational
theorems, six action layers (L1 state to L6 measure) with a named gate for
every lift, and falsification as first-class progress.

## 2. What is posited, not derived

| Kind | Content | Status of the choice |
|---|---|---|
| Axiom | `J = 1 + zeta_5^2` | primitive; no theorem derives it |
| Architecture | `Omega = N_0 x F_5^6`, update `U`, five kernel generators `a..e`, the selector `z_6 + 2 theta_n mod 5` | declared; not claimed to be forced by J |
| Decoder | typed partial interface `D_matter -> D_geom -> D_clock` | declared; totality and classification open |
| Calibration | electron mass `m_e` | the single SI anchor |
| Effective-theory adoptions | ETH-QDD-1, ETH-QDD-2 (measurement), ETH-TT-1, ETH-COS-1 (tensor and cosmology) | adopted dictionaries at [D] |
| Physical dictionaries | e.g. AXIOM-PROJECTION-DICTIONARY [D]: modulus of J read as gravity and scale, argument as electromagnetism and phase | readings at [D], not theorems |

The architecture introduces no fitted dimensionless parameter. The Canon is
explicit that restoring a stronger slogan ("everything from J") would need a
public theorem deriving the architecture from J, and no such theorem exists.

## 3. The ledger at a glance

609 registered claims: 465 T, 59 D, 40 C, 2 H, 24 O, 19 F, 0 T-LOCK.
Evidence: 188 inline proofs in the Canon, 302 public probes, 119 minimal
reproductions (38 reproduction bundles); 381 claims carry a two-architecture
requirement.

| Canon section | Claims | T | D | C | H | O | F | Share of Canon text |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1. Axiom and the two projections | 17 | 16 | 1 | | | | | 0.9% |
| 2. Time, space, and the decoder | 195 | 174 | 5 | 9 | | 5 | 2 | 48.4% |
| 3. Kernel and census | 68 | 47 | 1 | 17 | | | 3 | 6.4% |
| 4. The two places | 41 | 37 | 3 | 1 | | | | 7.0% |
| 5. Force is the curvature | 14 | 7 | 6 | 1 | | | | 0.4% |
| 6. Alpha and the observable register | 7 | 4 | 2 | 1 | | | | 0.1% |
| 7. Mass ladder and parity law | 6 | 4 | 1 | | | 1 | | 0.2% |
| 8. Measure and Born | 20 | 11 | 9 | | | | | 3.1% |
| 9. Photon and electron | 52 | 35 | 7 | 5 | | 2 | 3 | 3.4% |
| 10. Relativity as counting | 35 | 27 | 4 | 3 | | 1 | | 4.1% |
| 11. Pentit ring and magic boundary | 20 | 17 | 2 | | | | 1 | 1.4% |
| 12. Color door | 29 | 21 | 3 | | | 1 | 4 | 1.7% |
| 13. Gravity and cosmology | 28 | 19 | 7 | | | | 2 | 4.8% |
| 14. Gravitational wave program | 18 | 10 | 8 | | | | | 3.9% |
| 15. Couplings, instruments, metrology | 29 | 24 | | 2 | | 3 | | 10.1% |
| 16. p = 5 and the wall | 17 | 12 | | 1 | | | 4 | 1.4% |
| 18. Frontier | 13 | | | | 2 | 11 | | 1.8% |

The asymmetry is the main structural fact of the current Canon: the
decoder, record and finite-apparatus program (sections 2 and 15) carries 224
claims and almost 60 percent of the text, while the constants register
(sections 6 and 7) that most outside readers look for fits in about 5 KB.

## 4. What is established, by theme

### 4.1 The algebra of J

Unconditional number theory about `J` and `Z[zeta_5]`, all at [T]:
J-PROJECTIONS (modulus `1/phi`, principal argument `2 pi/5`), PI-FROM-J
(`pi = -5 i Li_1(J)`), J-MAHLER-MEASURE (`M(J) = phi^2`),
REGULATOR-TWO-LOG-PHI (`Reg Q(zeta_5) = 2 log phi`),
CYCLOTOMIC-CLASS-NUMBER-ONE (proved, not imported), LOG-AXES-INDEPENDENCE
(`pi` and `ln phi` independent over the algebraic numbers), PLENUM-POINT,
ZETA5-DEDEKIND-RESIDUE, and the residue, norm and trace calculi of sections 1
and 4. These are the most durable results in the corpus: they do not depend on
any reading.

### 4.2 The machine and its census

The autonomous state is `omega = (n, psi)` with `U(n, psi) = (n+1,
g_(z_6(psi) + 2 theta_n mod 5)(psi))`, where `theta_n` is the Thue-Morse bit.
Established: CENSUS-313 [C] (313 attractors of the Thue-Morse driven kernel
on `Z_5^6`), KERNEL-CONNECT-ALL-K [T], KERNEL-Z6-SYNCHRONIZATION [T],
CODEC-TR4 [T] (the unique `M_J` readout), HYPERPLANE-BOUNDARY-CLASS [T],
KERNEL-WEDGE-* [T], TM-ENTROPY-ZERO [T]. The entropy route from the substrate
to a measure closed negatively: ENTROPY-MEASURABLE-OBSTRUCTION [T] proves the
complete Route A class empty, so ENTROPY-LAYER-BRIDGE is [F].

### 4.3 Two places

Z2-PLACES-SPLIT [T]: the cyclotomic Galois involutions sit at exactly two
places, `v_5` and `v_2`. TWO-PLACE-PHYSICS [D] reads `v_5` as the write side
(geometry, gravity, the pentit substrate) and `v_2` as the read side;
I-BILOCATED [D] and SILVER-SIBLING [D] are the companion readings. The CM5
cluster (CM5-POLARIZATION-DICTIONARY and its Hecke and reachability
consequences, all [T]) is a separate exact mathematical reading of a specified
CM model.

### 4.4 Force as curvature

MAXWELL-BIANCHI, MAXWELL-GAUSS-CHAIN, MAXWELL-AMPERE-CHAIN and
MAXWELL-OBSTRUCTION-P [T] put the Maxwell system on a finite chain complex,
with the obstruction counted in `p = 5`. FORCE-WEYL-HOLONOMY [T]: the finite
Weyl pair has commutator phase `zeta_5`. The physical statements are readings:
MAXWELL-CLOSED, FORCE-AS-CURVATURE, COULOMB-PROJECTION, FORCE-POLAR-SIGN [D].

### 4.5 The constants register

This is the part with numerical contact to measurement. The exact layers are
theorems; the committed physical forms are [D]; numerical agreement is a
labeled measured comparison, never a conclusion.

| Quantity | Exact layer | Committed form | Comparison (labeled witness) |
|---|---|---|---|
| fine structure | ALPHA-SEED [T] (`alpha* = 1/p`), ALPHA-PREFACTOR-UNIFICATION [T] | ALPHA-FORM [D]: `alpha = 5S/((8 pi)^2 sqrt(s))`, `sqrt(s) = (3-phi)^(1/4)`, `S = (1+X/5)^-5`, `X = 1/(32 pi^2 phi^4)` | ALPHA-VALUE-DIGITS [C]: `alpha^-1 = 137.035999190` vs CODATA 2022 `137.035999177(21)` |
| weak mixing | WEINBERG-TREE [T] (`3/13`), HYPERCHARGE-LAW [T] | WEINBERG-FORM [D]: `3/13 + 1/(32 pi^2 phi^4)` | fenced |
| lepton masses | MU-TAU-COEFFICIENT [T] (`89/5`), MU-EXCHANGE-IDENTITY [T] | MASS-LADDER-FORMS [D] on the anchor `m_e` | muon `-0.023 sigma`, tau `-0.011 sigma` vs CODATA 2018 |
| parity of forms | PARITY-LAW [T], BRIDGE-DEFECT [T] | thirteen named entries are pi-even and delta-free | none |
| proton residual | | PROTON-RESIDUAL-IS-QCD [O] | none retained |

### 4.6 Measure, Born and Bell

BORN-FACE-WEIGHTS [T] and the Born half-angle and staircase theorems are the
exact layer; MEASURE-BORN-VERB [D] reads the measure as the Born square of the
verb. Measurement is closed as an adopted effective theory, not derived:
ETH-QDD-1 and ETH-QDD-2 (QDD-SELECTED-SOURCE, -RECORD, -BORN, -PAIR-* at [D])
with their exact consequences QDD-SELECTED-INSTRUMENT-LAW,
-ORDERED-HISTORY, -BIPARTITE-LAW [T]. QDD-FIVE-CONTEXT-BELL-SEPARATION [T]:
five contexts exclude the whole setting-independent Bell-local class although
every CHSH slice is nonviolating; BELL-CAUSAL-ACCOUNTING closes at [D];
COUNTER-BELL-PRICE [T] gives the exact overlap price 1/16.

### 4.7 Electron, photon and relativity

DIRAC-STEP [D] with DIRAC-STEP-THEOREMS [T] (`det = 1 + m_D^2 = 5 = p` for
the electron), LADDER-LIGHTCONE [T], SPINOR-FLOOR [T], ELECTRON-G-TREE [D]
(`g = 2` as flux over spinor half-angle). Relativity as counting:
BOOST-COUNT-LADDER [D] reads the integer exponent as rapidity `n ln phi`;
COIN-MINIMAL-READ [D] adopts `beta_1` by the minimal-read rule, and whether the
architecture forces it is MINIMAL-READ-DERIVATION [O]. The photon continuum is
the largest open physics item: the frozen photon-window route died
(PHOTON-WINDOW-PROOF [F], PHOTON-KAPPA-LEMMA [F]) and PHOTON-CONE-CONVERGENCE
and PHOTON-MASSLESS-PHASE remain [O].

### 4.8 Color and the nonabelian door

COLOR-LADDER-DICTIONARY [D] reads the exact `D5 -> 2I -> affine E8` ladder as
the color door, with COLOR-SPLIT-12 and COLOR-KINEMATICAL-GL2 [D]. Four
routes are dead: COLOR-DYNAMICAL-COLOR, SPIN-LIFT-FORCED,
QPAIR-2I-ONLY-PAIR-FORCING, QPAIR-MIXED-C4-NORMALIZES-2I [F]. COLOR-MEASURE-SELECTION,
GENERATIONS-L3 and ALPHA-S-RUNNING stay [O].

### 4.9 Gravity, cosmology and gravitational waves

GRAVITY-BRIDGE-LAW [D] (`alpha B g = 1` on the anchor). COSMOLOGY-REGISTER [D]
commits `w = -14/15`, `Omega_b = pi^2/200`,
`Omega_DM/Omega_b = 18 p^3 ln^2(phi)/pi^4`. The constant dark-energy reading
`w_DE(a) = -14/15` was falsified by the frozen DESI DR2 headline fit
(DE-W-CONSTANT [F]: `|z| = 365/108 > 322/125`); the register form survives as a
committed target only, and its dictionary DE-CONFORMAL-WEIGHT is [O]. NS-TILT
(`n_s - 1 = -5 alpha`) is one of the two live hypotheses, armed against
CMB-S4. The tensor program is a set of adopted dictionaries:
TT-SQUARING-DECODER, TT-SOURCE, POL-READ, TT-VECTOR-STATE-NORMALIZATION [D]
(exact ratios `60 +- 24 sqrt5` in the selected planar model).
TM-SYM2-MEASURE [F] closed the old selector route to a measure.

### 4.10 p = 5 and the wall

The zeta and Riemann-hypothesis adjacent program has produced exact
arithmetic (ZETA5-DEDEKIND-RESIDUE [T], O-R2-K-JUNCTION-PIN [C]) and four
clean negatives: MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER,
LAMBDA-BOUNDARY-HS-KOOPMAN, LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER,
PENTAGON-ONLY-DILATIONS [F]. Only the cocycle-vector form
LAMBDA-COCYCLE-ANGLES [H] and TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O] remain.

### 4.11 Decoder, records and finite apparatus

Most recent releases added their claims here. The results are exact L1
constructions and no-go theorems on declared architectures:

- native readback: U-NATIVE-RAW-RESIDUE-READOUT [T] recovers the residue sum
  of arbitrary piston inputs from receiver and counter;
  U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO [T] shows no fixed receiver-only reading
  keeps it; U-GALOIS-FIBER-CODE [T] preserves the full QDD Gram;
- relative contact: RELATIVE-CONTACT-INTEGRAL-LAW,
  RELATIVE-CONTACT-FOUR-SLOT-MINIMUM (sharp accounts 12 and 27),
  RELATIVE-CONTACT-COMMON-APPARATUS-OPEN (two experiments, 100 pairs, one read
  core) and RELATIVE-CONTACT-FINITE-WORKBANK-REUSE (`26+25k` slots, account
  `68+74k`), all [T];
- composed records: RESIDUAL-STEP-RECORD [T],
  HOMOGENEOUS-CAPTURE-CURRENT-RECORD [T] (joint asymptotic probability greater than `2/10^28`),
  FIELD-CONSERVATIVE-CHAIN-LAW [T], U-CARRY-MIRROR-FINITE-CIRCUIT [C].

Every one of these keeps its supplied operations, preparations and resources
as premises. None identifies a physical interface: QDD-INSTRUMENT-APPARATUS,
QDD-INSTRUMENT-CLASS-COMPLETENESS, QDD-TERMINAL-EVENT-SEMANTICS and
QUADRATIC-MEMORY-NATIVE-CONTACT are [O] and all at STOP.

## 5. What has been falsified

Falsification is progress. The 19 fired items, grouped:

| Group | Claims [F] | What died |
|---|---|---|
| curvature readout | CURVATURE-TRACE-READOUT-UNIQUE, CURVATURE-TRACE-VALUE | uniqueness of the trace readout; the proposed value `-21/8` (exact `-881/8`) |
| entropy bridge | ENTROPY-LAYER-BRIDGE, ENTROPY-CYLINDER-CUT, ENTROPY-LIFT-DEFECT | measurable Route A reader; finite-cylinder cut; literal integer lift of `(bc)^5 = 1` |
| photon | PHOTON-WINDOW-PROOF, PHOTON-KAPPA-LEMMA, TM-HANKEL-K3-UNIVERSAL-TRANSFER | the Kappa occupancy route to the photon window; balanced transfer at k = 3 |
| color and spin | COLOR-DYNAMICAL-COLOR, SPIN-LIFT-FORCED, QPAIR-2I-ONLY-PAIR-FORCING, QPAIR-MIXED-C4-NORMALIZES-2I | dynamical color from census symmetries; forced D5 lift; two pairing propositions |
| pentit | PHIBIT-NOT-TAU | the phibit as Fibonacci tau anyon |
| measure and cosmology | TM-SYM2-MEASURE, DE-W-CONSTANT | canonical TM selector; constant `w = -14/15` against DESI DR2 |
| the wall | MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER, LAMBDA-BOUNDARY-HS-KOOPMAN, LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER, PENTAGON-ONLY-DILATIONS | four operator-carrier routes |

## 6. What stays open

The 26 live H/O items and their decision conditions are listed once, in
`canon/FRONTIER.md`; they are not repeated here. By program: DECODER_CORE 13,
NONABELIAN_QCD 4, COSMOLOGY 2, QUANTUM_EM 2, PHOTON_CONTINUUM 2,
ENRICHMENT 2, TENSOR 1. Only two are READY for preregistration work
(GENERATIONS-L3, QUANT-SUBSTRATE); 16 are at STOP, meaning they need a
definition before any computation is meaningful, and 8 are BLOCKED.

## 7. Where the value is (assessment, non-normative)

1. **Durable mathematics.** The arithmetic of `J` and `Z[zeta_5]`
   (sections 1, 3, 4) is unconditional and reusable outside TWIST-J.
2. **The constants register.** The committed forms for `alpha`, the weak
   mixing angle and the lepton ladder, with exact theorem layers underneath,
   are the most externally legible content. They are [D], and their contact
   with data is a labeled comparison. This content is very short in the Canon
   and deserves a prominent, separate presentation.
3. **The falsifications.** DE-W-CONSTANT against DESI DR2 is the program's
   clearest empirical event; the photon, color, entropy and wall negatives
   delimit the theory and should stay visible.
4. **The decoder and apparatus program** is the largest investment and the
   least connected to measurement. It has produced many exact boundaries of
   what a reading can do, but every route to a physical interface is an open
   owner at STOP. More constructions of the same kind do not move those owners;
   the definition work they ask for does.
5. **The open physics** that would change the picture is concentrated in
   five places: the photon continuum, the nonabelian and generation structure,
   the dark-energy dictionary after DE-W-CONSTANT, NS-TILT against CMB-S4,
   and a decoder interface that reaches an apparatus.
