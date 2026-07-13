# Cutover audit (working document, GENESIS)

Review material, not part of the normative Canon. This file may name
internal artifacts once; the public series never inherits their
numbering. Session synthesis-canon-v1-s1, 2026-07-12.

## Frozen synthesis basis

```
internal version   v184 (sealed)
source HEAD        f51955d7 (mathorn1973/twistj-jam, main)
lock               2e2c399e83effd2f24051da01ea1608ba80cf903
Canon file         TWIST_J_Canon_v184_ALL_IN_ONE.md
SHA-256            cd92b8bba54658e154e8fc05eb562749f04c70b134dcc728c7236ed10378ef80
byte count         230406
```

Reading surface: the sealed internal consolidation at v1/ of the
internal repository (canon pin 7c41d949, gate commit f51955d7), byte
equal to v184 content with the dated fold parts retired. If the
internal basis moves during synthesis, stop and re-freeze.

## Claim mapping (grows with the registry)

Rule: every public claim maps to an internal claim of equal or
stronger status and at least the same scope. Missing support lowers or
omits; nothing is invented. Public statuses here are deliberately
conservative pending public probe machinery.

```
public claim id                internal source (status)             public
J-UNIT                         Part I unit facts (T)                T
J-PROJECTIONS                  Part I two projections (T)           T
PI-FROM-J                      Part I, Li_1(J) = i pi/5 (T)         T
J-GOLDEN-BRIDGE                kernel facts, glossary (T)           T
J-STEP                         step map, M_J columns (T)            T
J-MODULUS-CHORD                J Jbar = 2 - phi (T)                 T
J-TENTH-ROOT                   T-J-SHADOW rung 7 (T)                T
J-RAMIFIED-CHORD               T-PLENUM-RAMIFIED-CHORD (T)          T
PLENUM-POINT                   T-PLENUM-J-FORM, -BACKBONE-VALUE,
                               -INTEGER-SKELETON (T, LOCK cand)     T
ALPHA-SEED                     the alpha exact lemma (T-LOCK)       T
BORN-FACE-WEIGHTS              D-KCM-MAGNETIC-EMERGENCE weights;
                               the eight exact identities (T)       T
CENSUS-313                     SS85.12 census; hosting corollary (T)
                               conservative public grade            C
CENSUS-Z5-SHEET                D-CENSUS-Z5-SHEET (D)                C
CENSUS-PAIRING                 D-PAIR-MAP (D)                       C
CENSUS-HOSTING                 T-HOSTING (T)                        C
BORN-HALF-ANGLE                T-BORN-HALF-ANGLE (T-LOCK); the norm
                               gate now publicly evidenced          T
BORN-RESIDUAL-SPLIT            T-BORN-RESIDUAL-SPLIT (T-LOCK)       T
SPIN-BISECTOR                  T-SPIN-BISECTOR (T-LOCK); finite
                               shadow scope, no positivity          T
BORN-ORDER-STAIRCASE           T-BORN-ORDER-STAIRCASE (T-LOCK)      T
DIRAC-LADDER                   O-DIRAC-LADDER closed at D; the
                               checkerboard [D] reading             D
LADDER-LIGHTCONE               T-LADDER-LIGHTCONE (T)               T
SPINOR-FLOOR                   T-SPINOR-FLOOR (T)                   T
FIB-ROOT-TIES                  T-FIB-ROOT-NORM, T-FIB-ROOT-JET (T)  T
FIB-ROOT-CARRIER               D-FIB-ROOT-CARRIER (D)               D
DIRAC-STEP-THEOREMS            T-DIRAC-STEP-INVARIANTS, -GENERATOR,
                               T-REST-COIN-INFINITE-ORDER (T)       T
DIRAC-STEP                     D-DIRAC-STEP (D)                     D
LADDER-SPIN-PLACES             PLACE-ID PASS-B (T); the fired
                               F-LADDER-SIGN-IS-SPIN boundary       T
CHECKERBOARD-GAUSS-TOWER       T-CHECKERBOARD-SKELETON,
                               -ALTERNATOR-SPLIT, -GAUSS-TOWER (T)  T
FERMIONIZER                    T-FERMIONIZER (T)                    T
LADDER-ALTERNATOR-BASIS        T-LADDER-ALTERNATOR-BASIS (T)        T
TM-BREATH-TOWER                T-TM-BREATH-TOWER (T)                T
COLOR-RETURN-D5                T-H1-DIHEDRAL, T-D5-GOLDEN-TABLE,
                               T-D5-MASS-LAW (T)                    T
COLOR-TORSOR-HOLONOMY          T-D5-TORSOR, T-SP-HOLONOMY,
                               T-SP-ORIENTATION (T)                 T
COLOR-SPLIT-12                 D-SP-SPLIT12 (D)                     D
COLOR-DYNAMICAL-COLOR          F-RUNG3-TRIVIAL-DYNAMICAL (fired)   F
COLOR-KIN-NORMALIZER           T-KIN-COLOR-NORMALIZER (T)          T
COLOR-KINEMATICAL-GL2          D-KIN-COLOR-GL2,
                               D-KIN-CENSUS-COVARIANCE (D)         D
COLOR-CORE-2I                  T-COLOR-CORE-2I,
                               T-COLOR-RAMIFIED-TRACE (T)           T
COLOR-GOLDEN-TABLE             T-2I-GOLDEN-TABLE, T-LOOP-SPIN-LIFT,
                               T-2I-READOUTS,
                               T-2I-BRAUER-SHADOW (T)              T
COLOR-MCKAY-E8                 T-MCKAY-E8, T-CATALAN-BRIDGE,
                               T-VERB-TRANSPORT (T)                T
COLOR-MOMENT-FINGERPRINT       T-FINGERPRINT-RATIONAL,
                               T-MOMENT-LUCAS, T-J-SHADOW (T)      T
COLOR-SPECTRAL-INVARIANTS      T-SPECTRAL-MEASURE, T-KOSTANT-VFE,
                               T-PLATONIC-EXPONENTS (T)            T
COLOR-DICKSON-RAMIFICATION     T-DICKSON-FORMS, T-MODULAR-HILBERT,
                               T-VFE-PRIME (T)                     T
COLOR-KLEIN-REDUCTION          T-KLEIN-RELATION-Z, T-REDUCTION-SHAPE,
                               T-SYZYGY-SHADOW, T-AS-TOWER (T)     T
COLOR-INTEGRAL-LIFT            T-INTEGRAL-MODEL, T-GOOD-REDUCTION,
                               T-SYZYGY-CHANNEL,
                               T-ORBIT-REALIZED (T)                T
COLOR-MEASURE-TRANSPORT        T-2I-READOUTS, T-VERB-TRANSPORT,
                               T-SPECTRAL-MEASURE (T)              T
KAHLER-CAPACITY                the capacity result (v117); T-KC-J,
                               T-KAHLER-GEOMETRIC (T-LOCK)          T
FRW-CANONICAL-FORM             the FRW rank-1 (00) canonical form
                               (T); the fiber wall and multiplier
                               closures                             T
GRAVITY-BRIDGE-LAW             the Part VII bridge block; the
                               O-ELL-G-SI equation registration
                               (value stays O); D-SS40-TIER1-OPTIMUM
                               (D)                                  D
MU-TAU-COEFFICIENT             T-MU-COEF 89/5 (T-LOCK, v115)        T
MU-EXCHANGE-IDENTITY           the exchange identity (T, exact
                               in Q, Part VI)                       T
MASS-LADDER-FORMS              the Part VI committed ladder block
                               (D at the dictionary; sigma
                               comparisons fenced)                  D
PARITY-LAW                     the SS-DELTA parity law and register
                               census (Part VI)                     T
BRIDGE-DEFECT                  the SS-DELTA bridge defect and the
                               exact bridges (Part VI)              T
WEINBERG-TREE                  the Part V Weinberg block, exact
                               layer (T); the counting chain ties    T
HYPERCHARGE-LAW                the Part V hypercharge law and the
                               trace kernel dimension (T)            T
WEINBERG-FORM                  the Part V committed form (D at the
                               dictionary; comparison fenced)        D
MAXWELL-BIANCHI                T-BIANCHI-SYMBOLIC (T, v158)         T
MAXWELL-GAUSS-CHAIN            T-GAUSS-CHAIN-EXACT (T, v158)        T
MAXWELL-AMPERE-CHAIN           T-AMPERE-CHAIN-EXACT (T, v158)       T
MAXWELL-OBSTRUCTION-P          the v158 obstruction pair, counted
                               in p (T layer of the closure)        T
MAXWELL-CLOSED                 D-MAXWELL-CLOSED (D, v158)           D
ALPHA-PREFACTOR-UNIFICATION    T-ALPHA-PREFACTOR-UNIFICATION
                               (T, v162 fold)                       T
ALPHA-FORM                     the Part V Queen block (D at the
                               dictionary; comparison fenced)        D
ALPHA-VALUE-DIGITS             the Part V committed digit string,
                               enclosed at finite precision          C
TT-LINEAR-ZERO                 T-TT-LINEAR-ZERO (T-LOCK, v171)      T
TT-QUADRATIC-INDUCED           D-TT-QUADRATIC-INDUCED-POWER (D)     D
GYRON-DENSITY                  rho = 1/6 (T-LOCK SS80, SS86.1,
                               quadruply confirmed); the gyron gate
                               SS78.1; T-BASEL-TM-GATE (T)           T
COSMOLOGY-REGISTER             the Part VIII committed register
                               (w LOCK; the ratio theorem; N clock
                               at D and C); comparisons fenced       D
CONFORMAL-PREFACTOR            K_chi5 = K_L5 (D; v183 seal;
                               O-CHI5-KINETIC-COEF closed at the
                               homogeneous L5 scope)                 D
TT-SQUARING-DECODER            the v166 GW arc: D-TT-VECTOR-DOUBLET
                               and the squaring map rows (D)         D
RINGDOWN-EXPONENTIAL-DEAD      F-RINGDOWN-IMR (F, v166, WKB3
                               grade, labeled)                       F
SCHWARZSCHILD-TT-ENDPOINT      the Stage A rows: RW coefficients
                               forced; Lichnerowicz uniqueness at
                               scope (T)                             T
TT-QUADRATIC-GERM              the Stage B germ at mu = 1; Z_L2 =
                               1/2; the free Gaussian exclusion
                               (D with computed F boundary)          D
COUPLINGS-DETERMINE            the Part XXXIV arc: density and
                               Born branch norm (T);
                               T-MEAS-GYRON-CARRIER-NOGO;
                               F-QD-INSTRUMENT-UNIQUE (fired v172)   T
DEWITT-TWELVES                 the covariant DeWitt coefficient
                               12 = d(d+1) at lambda = -1 (T); the
                               inheritance chain of twelves          T
METRO-TICK                     the Part XLI tick clause (T at
                               scope); the admissibility quartet
                               with the gyron window pair            T
MEASURE-SPATIAL-ONLY           T-MEASURE-SPATIAL-ONLY (T, v133)      T
STRONG-SEED                    alpha_s root 3/4 (D, v133 home
                               direction rule)                       D
METRO-ADMISSIBILITY            O-METRO-ADMISSIBILITY residual       O
METRO-EDGE-SCALE               O-METRO-EDGE-SCALE + SI clause       O
LORENTZ-A2A3                   O-LORENTZ-A2A3                       O
QUANT-SUBSTRATE                O-QUANT-SUBSTRATE                    O
COLOR-MEASURE-SELECTION        O-A18-COLOR-MEASURE-SELECTION        O
TT-GAUGE-PULLBACK              O-TT-GAUGE-PULLBACK (Stage B)        O
TT-SOURCE                      O-TT-SOURCE                          O
QNM-LEAVER-MU                  O-QNM-LEAVER-MU                      O
POL-READ                       O-POL-READ                           O
TT-VECTOR-STATE-NORMALIZATION  O-TT-VECTOR-STATE-NORMALIZATION      O
FRW-INHOM                      O-FRW-INHOM                          O
DRESS-CROSSCOUNT               O-DRESS-CROSSCOUNT                   O
NS-TILT                        O-NS-TILT (H, falsifier live)        H
DE-CONFORMAL-WEIGHT            O-DE-CONFORMAL-WEIGHT                O
ALPHA-S-RUNNING                O-ALPHA-S-RUNNING                    O
SCHEME-DICTIONARY              O-SCHEME-DICTIONARY                  O
FIBER-THRESHOLD                O-FIBER-THRESHOLD                    O
GENERATIONS-L3                 generations at the E_SM L3 frontier  O
ETA-ALTERNATOR-BRIDGE          CB4 + O-ETA-ALTERNATOR-BRIDGE        O
SPIN-LIFT-FORCED               O-SPIN-LIFT-FORCED                   O
KC3-PLENUM-READOUT             H-KC3-PLENUM-READOUT                 H
QUADRATIC-ENVELOPE-DECODER     H-QUADRATIC-ENVELOPE-DECODER         H
TM-SYM2-MEASURE                H-TM-SYM2-MEASURE                    H
QUADRATIC-DECODER-DATA         O-QUADRATIC-DECODER-DATA residual    O
NEUTRON-DELTA-EM               O-NEUTRON-DELTA-EM                   O
PROTON-RESIDUAL-IS-QCD         O-PROTON-RESIDUAL-IS-QCD             O
SQRT-PHI-TIME-GRAVITY          O-SQRT-PHI-TIME-GRAVITY              O
OBSERVER-WRITE-PORT            AX-CW at H; the write port test      H
PHOTON-RADIATIVE-INDEPENDENCE  O-PHOTON-RADIATIVE-INDEPENDENCE      O
HYPERPLANE-BOUNDARY-CLASS      T-HYPERPLANE (T-LOCK, v101, the
                               boundary class |S| = 1250); carried
                               at public T by full enumeration       T
HYPERPLANE-BOUNDARY-REALIZATION  T-63-MERSENNE-FACE and the v101
                               realization; conservatively lowered
                               to C at the census window scope       C
CODEC-TR4                      T-CODEC-TR4 (T-LOCK), the readout
                               core: doubling and uniqueness;
                               carried at public T; the rate clause
                               is split out, not promoted            T
CODEC-RATE-SCOPE               the rate 4/5 clause of T-CODEC-TR4;
                               no spelled public coding scope in the
                               sealed corpus; held open, no
                               promotion by shorthand                O
PHIBIT-NOT-TAU                 F-PHIBIT-NOT-TAU (the v122
                               corrigendum); carried at F with the
                               finite fusion ring boundary inline    F
KERNEL-WEDGE-AFFINITY          T-O17-WEDGE.1 (T, machine verified
                               both architectures); carried at T     T
KERNEL-WEDGE-COUPLING          T-O17-WEDGE.2 (T); carried at T       T
KERNEL-WEDGE-LINEAR-STRATA     T-O17-WEDGE.3 (T); carried at T       T
KERNEL-WEDGE-AFFINE-MIX        T-O17-WEDGE.4 (T); carried at T       T
KERNEL-CELL-COMPONENTS         the single cell battery of the O17
                               connectivity patch (C); carried at C  C
KERNEL-MACRO-READING           D-O17-READING (D); carried at D       D
KERNEL-CONNECT-ALL-K           H-O17-MIN-ALL-K (H); T-O17-MIN (k = 2,
                               exact table) and C-O17-K3 with
                               C-O17-K3-MIN (k = 3, single platform,
                               1332 GiB engine) stay internal at the
                               sealed scope; F-O17-MIN-3SUBSET stands
                               as an internal guard                  H
ODOMETER-INTERNALIZED          the v153 internalized counter (D);
                               carried at D                          D
READING-SPLIT                  T-LQ-READING-SPLIT (T-LOCK, v133
                               seal); carried at T, inline, each leg
                               separately witnessed                  T
TIME-QUANTUM-TOWER             T-FROB-TIME-QUANTUM (T-LOCK);
                               conservatively lowered to C at the
                               computed range k = 1 to 4             C
CURVATURE-TRACE-VALUE          SS103 space is a commutator (T-LOCK)
                               with the trace value at O per the
                               sealed erratum; the public operator
                               witness is open, conservative O       O
DEGREES-BY-PRIME               the two places degree split (T);
                               carried at T                          T
Z2-PLACES-SPLIT                the Z2 family seal (T); carried at T  T
I-BILOCATED                    the bilocation reading (D); carried
                               at D                                  D
SILVER-RING-FACTS              the finite computations at the two
                               places (norm, element orders,
                               cyclicity, F_25 census); public C     C
SILVER-SIBLING                 the dictionary mirror reading,
                               public D, resting on the
                               SILVER-RING-FACTS C                   D
LOG-AXES-INDEPENDENCE          pi and ln phi linearly independent
                               over the algebraic numbers by Baker,
                               inline; linear only, public T         T
FORCE-WEYL-HOLONOMY           Part IV finite Heisenberg identity;
                               carried at public T by exact witness T
COULOMB-GREEN-COMPUTATION     SS9.2 exact C4 pseudoinverse (sealed T);
                               conservatively carried at public C   C
COULOMB-PROJECTION            Part IV common-propagator force
                               reading; continuum dictionary only   D
FORCE-POLAR-SIGN              Part IV polar decomposition reading  D
ABELIAN-FACE-DICTIONARY       D-KCM-TICK-ELECTRIC-LAW and
                               D-KCM-MAGNETIC-EMERGENCE; the sealed
                               six-ensemble uniqueness is omitted   D
MEASURE-BORN-VERB             D-MEASURE-BORN-VERB, resting on the
                               exact public Born weight layer       D
KERNEL-CELL-DICTIONARY        D-KCM-ORBIT-MAP                       D
SUBSTRATE-KNIT                T-QS-BORN-FACES, T-QS-GRAM, T-QS-MUB;
                               exact public witness                  T
PHOTON-WINDOW-COORDINATES     T-P5.1 to T-P5.4 (v155 fold), the
                               exact point and dual                  T
PHOTON-UNIVERSAL-BIT          T-P8.4 with the T-P8.3 closure
                               ladder                                T
MONOPOLE-FIFTHS               T-MONO-FIFTHS (v155 fold, P7)          T
MONOPOLE-COST                 T-MONO-LB17 and T-MONO-UB21;
                               conservatively carried at C as the
                               computed bracket; the exact minimum
                               stays the internal micro item         C
KAPPA-BOUNDS                  T-KAPPA-STRAIGHT, T-KAPPA-LADDER,
                               T-KAPPA-GREEDY                        T
KAPPA-SHAPES                  C-KAPPA-SHAPES, the exact library
                               reconstructed as nine explicit
                               loops realizing the pinned table      C
CENTER-SPLIT-RECIPROCITY      T-P8.1 and T-P8.2                      T
CENTER-SPLIT-CLOSURE          T-P8.3 with the p = 2 freeze and the
                               p = 3 full support                    T
CENTER-SPLIT-SELECTION        T-P8.5 with the standing self
                               duality import; carried at D because
                               door 1 is the labeled import          D
ELECTRON-G-RATIO              T-G-RATIO (the sixteen identity
                               block, carried at the algebraic
                               layer with angles in pi/10 units)     T
ELECTRON-G-DOUBLE-COVER       T-G-DOUBLE-COVER (PS-G-1)              T
ELECTRON-G-TREE               D-ELECTRON-G-TREE; the Schwinger
                               residual stays inside
                               QUANT-SUBSTRATE                       D
ELECTRON-SIGN-LAWS            seven of the eight sealed P10 laws;
                               the gyron window count law
                               (counts only 999 or 1000) is not
                               carried publicly by author decision;
                               the parity law is carried through
                               the structural derivation            T
ELECTRON-SIGN                 D-ELECTRON-SIGN; the eps totality on
                               event free survivors (the joint
                               readout with the signature
                               families) stays internal              D
PHOTON-WINDOW-PROOF           O-PWP-KAPPA and O-PWP-ROUGH, merged
                               to one public row with both
                               conditions explicit and the import
                               declared                              O
```

## Intentional omissions so far (to be resolved before the PR)

Internal claims stated in the Canon text with their labels but not yet
registered, pending public evidence (reproduction or inline
derivation): the narrative digest labels inventoried in the synthesis
notes; the foundations and places cluster resolved the twelve label
lines of sections 1, 2 and 4 (ten registered, the gyron density
line woven to GYRON-DENSITY, the transfer trichotomy rewritten as a
definition, the closed whole energy statement rewritten as a sealed
scope report, the charge conjugation clause folded into
Z2-PLACES-SPLIT). The force and Born dictionary group resolves eight
further unmapped occurrences through the eight rows above. The photon
and electron cluster resolves the seven occurrences of section 9
(five bracketed labels and the two unbracketed markers); the internal
gyron window count law and the signature family constants stay
internal by author decision, recorded on the ELECTRON-SIGN-LAWS and
ELECTRON-SIGN rows above. The gate measures 11 remaining unmapped
occurrences, in sections 10, 11 and 16, awaiting the pre PR
reconciliation. Explicitly omitted
from the public frontier, with reasons: SIGMA3-PRIMITIVE (author
decision: an optional enrichment, not a gap; stays internal);
W1-INTERFACE-PRINCIPLE, KERNEL-BRAID, and TIMEQUANTUM-POTENTIAL
(deferred: no faithful public decision condition is stated yet; each
returns only with a concrete falsifier or decision condition). The
internal O17 residual is resolved by the kernel connectivity
cluster: the structure rows carried at T, the census at C, the
reading at D, and the all k hypothesis registered live with its
concrete falsifier; T-O17-MIN and the k = 3 counts stay internal at
the sealed scope (single platform, beyond the public budget). No claim is silently dropped. Each candidate is registered,
conservatively lowered, rewritten as non-claim material, or
explicitly omitted with a reason. The queue is
notes/synthesis-canon-v1.md.
