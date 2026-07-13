# Synthesis worklist (NON-CANONICAL)

Working notes of the Public Canon v1 synthesis. Nothing here is a
claim. Branch synthesis/canon-v1; session log at the bottom.

## Decisions

D1 basis frozen (see legacy/CUTOVER_AUDIT.md); D2 registry selection
rule; D3 neutral stable claim ids; D4 single Apache-2.0 license; D5
minimal initial reproductions: approved by the author 2026-07-12.
D6 cutover date: pending; set when Phase A is reviewable.

Standing rules of this synthesis: public statuses are conservative, at
most T in the genesis bundle, and internal sources keep their grades
in the cutover audit; no unproven independence claims (pi and ln phi
carry linear independence over the algebraic numbers only); a
status-labelled statement without a registry identifier is unfinished
draft material and must be registered with evidence, rewritten as a
definition or remark, or removed before the synthesis pull request
opens; every live registry row carries a concrete falsifier or a
decision condition, and check_canon.py rejects placeholders; a live
row whose decision condition cannot be stated faithfully is omitted
with a reason in the audit and queued here, never registered vaguely.

## Queue before the synthesis PR opens

1. Registry completion, cluster by cluster, each with evidence:
   COMPLETE: nine clusters from the kernel to the coupling and
   metrology arc; any residue falls to the pre PR inventory.
2. Deepen sections 14 and 15 from the sealed arc part bodies at the
   internal basis (they are stated here at frontier resolution).
3. Reconciliation audit rows for every added claim.
4. Deferred frontier rows, each returning only with a concrete
   falsifier or decision condition: W1-INTERFACE-PRINCIPLE,
   KERNEL-BRAID, TIMEQUANTUM-POTENTIAL (recon 2026-07-12: bare names
   in the sealed corpus, no honest condition available, stay
   internal); the internal O17 residual is RESOLVED by the kernel
   connectivity cluster (structure T, census C, reading D, the all k
   hypothesis live with its falsifier).
5. The pre PR inventory: sweep the Canon for every status-labelled
   statement without a registry identifier (grep for bracketed
   labels); each gets an identifier and registration, becomes a
   definition or remark, or is removed. Recon count 2026-07-12: 35
   label lines without a nearby identifier; the hyperplane-codec
   cluster resolves 3 (the hyperplane, codec, and phibit lines); the
   foundations-places cluster resolves the 12 lines (13 markers,
   compound brackets counted) of sections 1, 2 and 4; the
   force-born-dictionary cluster resolves eight further occurrences;
   18 unmapped occurrences remain, all in sections 9 and beyond, the
   count derived from this gate run.
6. Full local check run, security audit, PR template fields.

## Two architecture witness

Recorded per push in the session log. Platforms are named neutrally:
operating system, architecture, Python version.

Recorded at the genesis push: Debian 13 x86_64 (Python 3.13.5), all
four reproductions byte identical against EXPECTED.txt, exit 0, empty
stderr; check_policy and check_canon (hardened) pass on that platform
(2026-07-12). Author platform Ubuntu 24.04 aarch64 (Python 3.12.3),
same result.

Recorded at the Born quartet push: Debian 13 x86_64 (Python 3.13.5),
all five reproductions byte identical against EXPECTED.txt, exit 0,
empty stderr; check_policy and check_canon (with the frontier
identifier parser) pass on that platform (2026-07-12). Author platform
Ubuntu 24.04 aarch64 (Python 3.12.3), same result.

Recorded at the Dirac ladder push: verifier 3240d355 and stdout
2f8d2036 byte identical on Ubuntu 24.04 aarch64 (Python 3.12.3) and
Debian 13 x86_64 (Python 3.13.5), 16/16, exit 0, empty stderr, both
runs recorded before the commit (2026-07-12). After the push, a
fresh checkout of the pushed head on Debian 13 x86_64 passed
check_policy, check_canon (60 claims), and all six reproductions
byte identical.

Color ladder staging candidate: verifier 5cd3a40c and stdout 9031fd6a,
12/12, exit 0, empty stderr in the pre-pin dry run. Formal records
begin only after the immutable GitHub candidate commit, through the
Phase A staging protocol in AGENTS.md; both architecture records are
pending at the candidate commit.

Gravity chain staging candidate: verifier e964fb6c and stdout
e74dd895, 12/12, exit 0, empty stderr in the pre-pin dry run, byte
identical on x86_64 and aarch64. Formal records begin only after the
immutable GitHub candidate commit, through the Phase A staging
protocol in AGENTS.md; both architecture records are pending at the
candidate commit.

Mass ladder staging candidate: verifier 68593371 and stdout
1ea07225, 8/8, exit 0, empty stderr in the pre-pin dry run, byte
identical on x86_64 and aarch64. Formal records begin only after the
immutable GitHub candidate commit, through the Phase A staging
protocol in AGENTS.md; both architecture records are pending at the
candidate commit.

Weinberg staging candidate: verifier cdff7689 and stdout eaeb163e,
6/6, exit 0, empty stderr in the pre-pin dry run, byte identical on
x86_64 and aarch64. Formal records begin only after the immutable
GitHub candidate commit, through the Phase A staging protocol in
AGENTS.md; both architecture records are pending at the candidate
commit.

Maxwell closure staging candidate: verifier a84c80da and stdout
f449619e, 10/10, exit 0, empty stderr in the pre-pin dry run, byte
identical on x86_64 and aarch64. Formal records begin only after the
immutable GitHub candidate commit, through the Phase A staging
protocol in AGENTS.md; both architecture records are pending at the
candidate commit.

Alpha value staging candidate: verifier e967e5df and stdout
dcf55ac8, 7/7, exit 0, empty stderr in the pre-pin dry run, stdout
byte identical on x86_64 and aarch64. Formal records begin only after
the immutable GitHub candidate commit, through the Phase A staging
protocol in AGENTS.md; both architecture records are pending at the
candidate commit.

Cosmology register staging candidate: verifier 3cbafabf and stdout
3c6eb3dc, 7/7, exit 0, empty stderr in the pre-pin dry runs, byte
identical on x86_64 and aarch64. Built in the prep lane on the
pre-alpha base and rebased onto the post-alpha synthesis head before
pinning. Formal records begin only after the immutable GitHub
candidate commit, through the Phase A staging protocol in AGENTS.md;
both architecture records are pending at the candidate commit.

Coupling and metrology arc staging candidate: verifier 2ecad5f2 and
stdout f3e975ca, 8/8, exit 0, empty stderr in the pre-pin dry runs,
byte identical on x86_64 and aarch64. Built in the prep lane and
rebased before pinning. Formal records begin only after the immutable
GitHub candidate commit, through the Phase A staging protocol in
AGENTS.md; both architecture records are pending at the candidate
commit.

## Session log

- s15 (2026-07-13): the force and Born dictionary reconciliation:
  reproduce/force-born-dictionary (10/10: the finite Weyl
  commutator on five states; the exact C4 Green pseudoinverse; the
  Born weights, Galois pairing, tilt, and Legendre sign; conjugate
  verb readouts, their circulant Gram and exact spectrum; position
  and Fourier mutual unbiasedness; Plancherel masses 2 and 10).
  Eight registry rows: FORCE-WEYL-HOLONOMY T,
  COULOMB-GREEN-COMPUTATION C (the finite C4 kernel only),
  COULOMB-PROJECTION D (the continuum scaling dictionary, explicitly
  not a finite C4 value), FORCE-POLAR-SIGN D,
  ABELIAN-FACE-DICTIONARY D (the sealed six-ensemble uniqueness is
  not claimed), MEASURE-BORN-VERB D, KERNEL-CELL-DICTIONARY D, and
  SUBSTRATE-KNIT T. Registry 138 claims. The independent status gate
  reports 18 remaining unmapped occurrences, all in sections 9 and
  beyond. The x86_64 prep dry run is byte identical to EXPECTED:
  verifier 999f5d47 and stdout 75f69589 (752 bytes), 10/10, exit 0,
  empty stderr. Formal records begin only after the immutable
  candidate is pinned on the post-foundations synthesis base.
- s14 (2026-07-12): the foundations and places cluster, the label
  reconciliation of sections 1, 2 and 4: reproduce/foundations-places
  (8/8: odometer internalization with the recursion and carry parity
  laws; the time quantum tower T^(5^k) = i_5 I on Z/5^k for k = 1 to
  4 with exact period 4 x 5^k; the degree split by prime with the
  unique quadratic subfield exclusion; one involution at zeta_5
  against the complete Klein four at zeta_8; the Gaussian split
  5 = (2 + i)(2 - i); the bilocation of i; the silver sibling with
  the full F_25 order census). Ten registry rows:
  ODOMETER-INTERNALIZED D, READING-SPLIT T (inline, each leg
  separately witnessed), TIME-QUANTUM-TOWER C (lowered from the
  sealed T-LOCK to the computed range, k = 1 to 4),
  CURVATURE-TRACE-VALUE O (the space commutator sentence rewritten to
  the sealed scope with the trace value as a live obligation),
  DEGREES-BY-PRIME T, Z2-PLACES-SPLIT T, I-BILOCATED D,
  SILVER-RING-FACTS C (the finite F_25 computations: norm, orders,
  cyclicity, and census), SILVER-SIBLING D (the dictionary mirror
  reading, resting on SILVER-RING-FACTS C), LOG-AXES-INDEPENDENCE T
  (pi and ln phi linearly independent over the algebraic numbers by
  Baker, inline; linear independence only). The gyron density line woven to GYRON-DENSITY;
  the transfer trichotomy rewritten as a definition; the closed whole
  energy statement rewritten as a sealed scope report. Registry 130
  claims. Both platform dry runs byte identical before the pin:
  verifier ec422db6 and stdout c07adecb (2907 bytes), Ubuntu 24.04
  aarch64 (Python 3.12.3) and Debian 13 x86_64 (Python 3.13.5),
  exit 0, empty stderr.
- s13 (2026-07-12): the kernel connectivity cluster from the sealed
  O17 patches: reproduce/kernel-connectivity (7/7: affinity split
  with det 1 on all five generators; the CSUM wedge identity in 12
  variables; the coupling closure SL2(F_5) order 120 equal to the
  full determinant one count; congruence on 36 basis pairs; the rank
  dichotomy 5 + 15620 on the slice; the affine mix 62480 of 78125 for
  c, d, e and 0 for a, b; the seventeen subset census with
  monotonicity). Seven registry rows: four wedge structure rows at T,
  the component census at C, the macro reading at D, and
  KERNEL-CONNECT-ALL-K at H with the k >= 4 fragmentation falsifier;
  the k = 2 minimal set theorem and the k = 3 enumeration stay
  internal at the sealed scope. Registry 120 claims. Both platform
  dry runs byte identical before the pin: verifier 87ba627e and
  stdout 64d0a05d (2243 bytes), Ubuntu 24.04 aarch64 (Python 3.12.3)
  and Debian 13 x86_64 (Python 3.13.5), exit 0, empty stderr.
- s12 (2026-07-12): the hyperplane-codec micro cluster:
  reproduce/hyperplane-codec (8/8: the boundary class by full
  enumeration, |M| = 6250, |S| = 1250, complement 5000 in sheets of
  2500 with fibers 625 + 625; the census window realization of S as
  the 63 boundary attractors with no straddling; the step charpoly
  Phi_5(x - 1) with det(2I - M_J) = 5 and the axiom column identity;
  the doubling identity over Z and F_5; readout uniqueness over all
  625 covectors and all five multipliers; the phibit and Fibonacci
  fusion rings with the finite boundary of the fired reading). Five
  registry rows: HYPERPLANE-BOUNDARY-CLASS T,
  HYPERPLANE-BOUNDARY-REALIZATION C, CODEC-TR4 T, CODEC-RATE-SCOPE O
  (the rate 4/5 clause split out, no promotion by shorthand),
  PHIBIT-NOT-TAU F (the third public fired falsifier). The ledger
  sentence added to the Statuses block; it does not legalize
  unregistered labels, which stay reconciliation debt (32 lines).
  Registry 113 claims. Both platform dry runs byte identical before
  the pin: verifier 921ae520 and stdout bc42aa9e (3202 bytes), Ubuntu
  24.04 aarch64 (Python 3.12.3) and Debian 13 x86_64 (Python 3.13.5),
  exit 0, empty stderr.
- s11 (2026-07-12): the coupling and metrology arc:
  reproduce/coupling-metrology (8/8: the squaring decoder with kernel
  {+-1} and volume neutrality det(I + H) = 1 - |h|^2; the one
  propagation law on (+1, 0, -3); the Regge-Wheeler endpoint with the
  forced -6 = 2(1 - 4); the Stage B germ bookkeeping mu = 1 with
  Z_L2 = 1/2; the Gram density with trace exactly 1; the DeWitt
  twelves 12 = d(d + 1) at lambda = -1; the dimensionless tick
  2 pi/5; the coupling seeds 3/4 = d/(d + 1) and the 15 : 4 ratio).
  Nine registry rows: TT-SQUARING-DECODER D,
  RINGDOWN-EXPONENTIAL-DEAD F (the second public fired falsifier),
  SCHWARZSCHILD-TT-ENDPOINT T, TT-QUADRATIC-GERM D,
  COUPLINGS-DETERMINE T, DEWITT-TWELVES T, METRO-TICK T,
  MEASURE-SPATIAL-ONLY T, STRONG-SEED D; registry 108 claims. The
  audit omissions now list only the hyperplane and codec claims,
  resolved at the pre PR inventory. Built in the prep lane on the
  pre-cosmology base, rebased onto the post-cosmology synthesis head
  with the shared counts re-keyed, and pinned through the Phase A
  staging protocol.
- s10 (2026-07-12): the cosmology register prep (non-formal):
  reproduce/cosmology-register drafted (7/7 in dry runs: the frozen
  modulus under J -> J e^(i eps), so r = 0 at linear order; the TT
  quadratic onset det(I + H) - 1 = -|h|^2 with no linear term; the
  exact Thue-Morse pair census with its substitution recursion and
  the invariant 6 c_00(4N) - 4N = 6 c_00(N) - N; the gyron gate
  (0, 0) at rho = 1/6 = 1/(p + 1) with the unique stationary vector
  (1, 2, 2, 1)/6, so 1/rho = 6 is the proton prefactor; the Basel
  gate booking f_00 pi^2 = pi^2/6; the register parity, all forms pi
  even; the conformal chain K_chi5 = 1/(864 pi), c_hom = 1/(72 pi)).
  Five draft registry rows: TT-LINEAR-ZERO T, TT-QUADRATIC-INDUCED D,
  GYRON-DENSITY T, COSMOLOGY-REGISTER D, CONFORMAL-PREFACTOR D;
  registry 99 claims. Built in the prep lane on the pre-alpha base,
  rebased onto the post-alpha synthesis head with the shared counts
  re-keyed, and pinned through the Phase A staging protocol.
- s9 (2026-07-12): the alpha value candidate:
  reproduce/alpha-value (7/7: the prefactor chord 1 + J Jbar = 3 - phi
  = |1 - zeta|^2 in Z[zeta_5]; B_{2,chi5} = 4/5 by the Bernoulli
  definition; the Gauss sum tau = 2 phi - 1 = sqrt5 exactly, tau^2 =
  5, so the L normalization is computed, not cited; the unification
  80 sqrt5 L(2, chi5) = (8 pi)^2/5 exactly in Q; the Queen structure
  with X the Weinberg slip and every pi degree even; the integer
  interval enclosure at scale 10^50 with width below 10^-20 reading
  137.035999190 at the ninth decimal place; the fenced CODATA window,
  above the central value and inside one ppb). Three registry rows:
  ALPHA-PREFACTOR-UNIFICATION T, ALPHA-FORM D, ALPHA-VALUE-DIGITS C;
  registry 94 claims. The audit omissions no longer list the alpha
  value comparison. Built in the prep lane and pinned through the
  Phase A staging protocol.
- s8 (2026-07-12): the Maxwell closure candidate: reproduce/maxwell
  (10/10: the Bianchi identity and gauge invariance identically in the
  32 edge and 16 vertex symbols of the tesseract, carried as exact
  integer linear algebra; the Gauss chain on the 2 x 2 x 2 spatial
  torus with Smith divisors all 1, the constructive dipole, and the
  integrated law on all 256 regions; the Z_5 Gauss obstruction with a
  constructive solve and an exhibited obstruction; conservation as the
  exact identity bd1 bd2 = 0 in the 96 face symbols of the 2^4 torus;
  the Smith form of the face boundary with 45 unit divisors and H_1
  free of rank 4; the four winding certificates pairing to the
  identity; the single winding Z_5 obstructed while five parallel
  windings solve; the iff closed by exact ranks 45 = 64 - 19). Five
  registry rows: MAXWELL-BIANCHI T, MAXWELL-GAUSS-CHAIN T,
  MAXWELL-AMPERE-CHAIN T, MAXWELL-OBSTRUCTION-P T, MAXWELL-CLOSED D;
  registry 91 claims. The audit omissions no longer list the Maxwell
  closure. The cluster enters GitHub staging through the Phase A
  protocol.
- s7 (2026-07-12): the Weinberg candidate: reproduce/weinberg
  (6/6: the face degree deg_f = Tr(J) = 3 on the power basis; the
  trace kernel of dimension 3 over Q and 125 = 5^3 points over F_5 by
  full enumeration, so B_quark = 1/3 = 1/dim ker(Tr); the tree value
  3/13 = deg_f/(V + 1) with V = 12 = d(d + 1) by two routes; the
  hypercharge law reproducing all seven standard model hypercharges
  exactly; the correction term phi^-4 = 5 - 3 phi, exactly positive,
  over 32 = 2^5; the parity of the committed form, pi even and delta
  free, with the single positive correction above the tree value at
  the form level). Three registry rows: WEINBERG-TREE T,
  HYPERCHARGE-LAW T, WEINBERG-FORM D (comparison fenced); registry 86
  claims. The audit omissions no longer list Weinberg. The cluster
  enters GitHub staging through the Phase A protocol.
- s6 (2026-07-12): the mass ladder candidate:
  reproduce/mass-ladder (8/8: the shared coefficient 89/5 = 18 - 1/p
  with 240 C = 4272; the exact exchange identity in Q, identically and
  on a rational sweep; the committed forms with their fenced sigma
  comparisons kept outside the witness; the proton as the homogeneous
  odd pi^5 carrier; the neutron as the unique mixed composite with
  Delta_EM open; the exact bridges xi phi^2 = 5, Q phi^2 = 2 pi,
  Q/xi = 2 pi/5; the algebraic side of the bridge defect, minimal
  polynomial x^2 - 18x + 36 irreducible; the parity law on thirteen
  named even entries and the three odd carriers at pi degrees 1, 3,
  5). Five registry rows: MU-TAU-COEFFICIENT T, MU-EXCHANGE-IDENTITY
  T, MASS-LADDER-FORMS D, PARITY-LAW T, BRIDGE-DEFECT T; registry 83
  claims. The audit omissions no longer list the mass ladder values.
  The cluster enters GitHub staging through the Phase A protocol.
- s5 (2026-07-12): the gravity chain candidate:
  reproduce/gravity-chain (12/12: the modulus chord J Jbar = 2 - phi =
  phi^-2 with N(J) = 1; the Kahler jet and the exact capacity monomial
  64 pi^3 phi^2, pi odd; the rank 1 lapse action closing the (00)
  algebra with lambda = 216 pi and H^2 = 72 pi rho; the three 2-planes
  coefficient; the Euler-Lagrange chain to the second Friedmann
  equation; the canonical Hamiltonian form; the forced fiber k_f = 1
  against G_nat = 27 = d^3 with V_cell = 864 pi; the fiber circle
  J = zeta (zeta + zeta^4); the exact bridge square g^2 = 1024 phi^4
  (3 - phi); the wall spelling at the equation layer). Three registry
  rows: KAHLER-CAPACITY T, FRW-CANONICAL-FORM T, GRAVITY-BRIDGE-LAW D
  (the equation layer; the SI value of G stays on the frontier);
  registry 78 claims. The audit omissions no longer list the gravity
  chain. The cluster enters GitHub staging through the Phase A
  protocol in AGENTS.md.
- s4 (2026-07-12): the color ladder candidate:
  reproduce/color-ladder (12/12 blocks, eleven rungs). Rungs 1 and 2
  close the D5 return group, integer mass law, torsors, holonomy,
  orientation, and the 3 = 1 + 2 dictionary. Rung 3 records the fired
  dynamical-color falsifier at F, then proves the 19200-element
  product-affine normalizer and reads its special-linear image as
  GL_2(F_5) at D. Rungs 4 to 11 close the 2I core, golden character
  table and spin lift, affine E8 and Catalan bridge, the rational
  Lucas fingerprint, the spectral class measure and invariant degrees,
  the Dickson ramified pair, Klein reduction and Artin-Schreier tower,
  and the integral lift. Fifteen registry rows: 12 T, 2 D, 1 F;
  registry 75 claims. The audit omissions no longer list the color
  ladder. The expensive 19200-candidate sweep was compressed without
  changing scope: five generators close to 40 x 480 and each
  generator permutes all 313 supports. The cluster now enters GitHub
  staging: commit the immutable candidate, record x86_64 and aarch64
  through the runner tool, validate both records, then fast-forward
  synthesis.
- s3 (2026-07-12): the Dirac ladder cluster:
  reproduce/dirac-ladder (16/16: the light cone pair with Pell parity;
  the spinor floor with the quartic irreducibility and the odd rung
  witness; the Fibonacci root with its Z conjugacy to the modulus
  carrier, the mod 5 towers with -I at half period, the J_4(2) Jordan
  block and an explicit 1-jet conjugator; the step form with
  coefficient set {1, i m}; the exact invariants, the mass shell, the
  rest coin of infinite order; the two distinct places with the
  Gaussian place swap; the checkerboard skeleton and Gauss tower; the
  fermionizer; the beat factorization; the Thue-Morse breath tower);
  twelve registry rows, 9 T and 3 D (the dictionary layer of the
  ladder enters at D, the first derived grade rows of the public
  registry); registry 60 claims; the audit omissions no longer list
  the Dirac ladder.
- s2a (2026-07-12): Born layer closed by three review fixes from the
  author: the half angle scope no longer counts the antipode (the
  normalized bisector exists exactly on the 11 non antipodal gated
  units; at u = -1 the bisector vanishes, the only square root of its
  norm is 0, not invertible); the order 16 minimality now excludes
  every smaller degree (16 divides none of 4, 24, 124); the audit no
  longer lists the Born quartet among omissions. New EXPECTED; both
  platform runs recorded before the commit: verifier cf6009aa and
  stdout 228e7335 byte identical on Ubuntu 24.04 aarch64 (Python
  3.12.3) and Debian 13 x86_64 (Python 3.13.5), 11/11, exit 0, empty
  stderr.
- s2 (2026-07-12): the frontier identifier parser in check_canon now
  rejects unregistered identifiers leading FRONTIER.md list items
  (negative tested); README gained the official channels and the
  candidate review note; the Born quartet cluster:
  reproduce/born-quartet (11/11: the cyclic Born unit group of order
  24, the half angle identity on every Born unit, the norm gate
  exactly on the squares with zeta_8 ungated, the normalized bisector
  witness on all gated units, both residual splits with their
  conjugation swaps, the integer spinor skeleton and its SL_2(F_25)
  shadow of order 8, the order staircase with exhaustive
  irreducibility); four registry rows at T; registry 48 claims.
- s1 (2026-07-12): gate hardening and genesis bundle. check_canon.py
  rejects placeholder falsifiers (concrete falsifier or decision
  condition required for every H, O, F row). The bundle: Canon
  candidate in nineteen sections with the concrete kernel definition
  in section 3; registry 44 claims (11 T with evidence, 8 by
  reproduction and 3 by inline derivation; 4 C, the census cluster;
  24 O and 5 H frontier rows, each with a concrete falsifier or
  decision condition); four reproduction witnesses: kernel 15/15,
  alpha-exact-lemma 5/5, born-faces 8/8, census 11/11 (including
  closure under both transitions and second window stability); four
  frontier rows explicitly omitted with reasons in the audit; core,
  frontier, changelog, SHA256SUMS, citation, status candidate line;
  basis frozen; audit mapping for all 44 rows; all checks green
  locally on Ubuntu 24.04 aarch64 (Python 3.12.3).
