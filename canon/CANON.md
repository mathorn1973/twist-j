# TWIST-J Public Canon v1

**Status.** Candidate. This repository is in GENESIS; authority is
declared by STATUS.md at the repository root. This document becomes
the public Canon only at the declared activation.

**What TWIST-J is.** TWIST-J tests one risky hypothesis: physical
reality is a closed, exact, deterministic integer system; continuum,
geometry, probability, and fields are readings of it. One axiom, one
operator, one universe. Zero free dimensionless parameters; one SI
calibration anchor, the electron mass m_e.

**Axiom (A0).** Reality is the closed integer J-Cayley plenum. The
whole physical object is the canonical integer Cayley system generated
by J = 1 + zeta_5^2, with no external boundary, no external clock, and
only internal readout. J is the generator of the plenum and the seed
of the two projections. Under A0, E_total = 0 is a theorem of the
closed whole, not a second axiom; that theorem stands at the sealed
internal basis with its pinned verifier, and the internalized counter
that removes the external clock is registered below as
ODOMETER-INTERNALIZED.

CZ: A0. Skutecnost je uzavrene celociselne J-plenum. Cely fyzikalni
objekt je kanonicky Cayleyuv system dany jednotkou J = 1 + zeta_5^2,
bez vnejsi hranice, bez vnejsiho casu a jen s vnitrnim ctenim.

**Reading.** Time is a counter. Space is a commutator. J is the verb;
phi and pi are projections of J, not primitives. Two forces are two
J-projections: the modulus gives gravity and scale, the argument gives
electromagnetism and phase. Plenum, not vacuum.

**Conventions.** No em dashes. No decimals unless justified: integers
and ratios are primary; decimals appear only as computed or measured
witnesses, engineering readouts, or measured comparisons, never in a
conclusion, and are labeled as such. If it cannot be calculated in
integers, it is not physics. Falsification is first class progress.
Assertions use exact arithmetic; preregistration precedes computation;
a computation only theorem requires byte identical output on two
architectures; the action layer protocol names six layers (L1 state,
L2 manifold, L3 boundary, L4 support, L5 stream, L6 measure) and any
lift between layers requires its own named gate.

**Statuses.** Rigid order T-LOCK > T > D > C > H > O > F. T-LOCK
immutable theorem; T theorem; D derived; C computed at finite range;
H hypothesis with an explicit falsifier; O open obligation; F
falsified. Every claim carries a label; no summary is stronger than
the label it summarizes. The machine readable registry is
canon/REGISTRY.tsv; its claim identifiers are status neutral and
stable. The registry is the authoritative public ledger: a bracketed
status in the narrative without a registered claim identifier is not
thereby a registered public claim, and this sentence does not
legalize it; every such label is reconciliation debt, registered with
evidence, rewritten, or removed before the synthesis pull request
opens.

**Notation.** j = zeta_5, j^5 = 1. J = 1 + j^2. phi = (1 + sqrt5)/2 =
1/|J|. pi = -5 i Li_1(J), with Li_1(J) = i pi/5 exactly. tau = sqrt(J)
in F_25; m = zeta_8 = sqrt(i) at prime 2. p = 5 and d = 3 throughout.
K_chi5 = 1/(864 pi) is the conformal mode prefactor.

**The five stones.**

```
1. J = 1 + zeta_5^2                       the axiom
2. L = Re Li_2(J) = pi^2 / (2p)^2         the L-value, the action
3. The Klein-100 typology                 the foam structure
4. D = D_clock o D_geom o D_matter        the decoder
5. The plenum T = s + i phi = 2i(1 - J)   structured space itself
```

---

## 1. The axiom and the two projections

J = 1 + zeta_5^2 is a cyclotomic unit: N(J) = 1 and Tr(J) = 3 in
Q(zeta_5), with Galois conjugate moduli (phi^-1, phi, phi, phi^-1)
(J-UNIT [T], reproduce/kernel). The two projections of the unit are
the two forces:

```
|J|    = 1/phi        the modulus projection    gravity and scale
arg(J) = 2 pi / 5     the argument projection   electromagnetism and phase
```

Derivation (J-PROJECTIONS [T]): with j = e^(2 pi i/5), J = 1 + j^2 =
2 cos(2 pi/5) e^(2 pi i/5); 2 cos(2 pi/5) = phi - 1 = 1/phi, so
|J| = 1/phi and arg J = 2 pi/5. The algebraic half is exact in the
kernel witness as J Jbar = 2 - phi = phi^-2 (J-MODULUS-CHORD [T],
reproduce/kernel).

pi enters from the argument side (PI-FROM-J [T]): 1 - J = -j^2 is a
primitive tenth root of unity (J-TENTH-ROOT [T], reproduce/kernel),
1 - J = e^(-i pi/5), so Li_1(J) = -log(1 - J) = i pi/5 exactly and
pi = -5 i Li_1(J). A third transcendental enters from the modulus
side: ln phi, the boost rapidity. The two logarithmic axes pi and
ln phi are linearly independent over the algebraic numbers
(LOG-AXES-INDEPENDENCE [T]): i pi = Log(-1) and ln phi = Log(phi) are
logarithms of algebraic numbers, Q-linearly independent, hence
independent over the algebraic numbers by Baker. No algebraic
independence claim is made.

The golden bridge (J-GOLDEN-BRIDGE [T], reproduce/kernel): J phi = j,
(J - 1)^3 = j, and J^5 phi^5 = 1. Multiplication by J on the integer
lattice Z^4 in the basis {1, j, j^2, j^3} is the canonical step
(J-STEP [T], reproduce/kernel):

```
(a, b, c, d) -> (a - c + d, b - c, a, b - c + d),  det = N(J) = 1, trace = 3
```

The plenum point (PLENUM-POINT [T]): T = s + i phi = 2i(1 - J) with
s^2 = 1 + J Jbar = 3 - phi = sqrt5/phi. Derivation: J Jbar = 2 - phi
gives s^2 = 3 - phi, and (3 - phi) phi = 2 phi - 1 = sqrt5. |T| = 2;
arg T = 3 pi/10; zeta_5 T^2 + 4 = 0, since T^2 = -4 j^4; T^10 = -2^10;
T/2 = zeta_20^3, and the CRT split T/2 = zeta_4^-1 zeta_5^2 says prime
5 writes, prime 2 reads, and they meet at the archimedean place in the
plenum point itself. s = |1 - zeta_5| is the ramified chord:
N(1 - zeta_5) = 5 (J-RAMIFIED-CHORD [T], reproduce/kernel), while the
modulus chord is a unit chord: gravity reads the unit chord, space
reads the ramified chord [T]. At the magic prime the axiom has a
square root: sqrt(J) = tau in F_25 (section 11).

## 2. Time, space, and the decoder

The dynamics is the verb: the running whole has exactly two memory
primitives, the Log stream (one bit per tick) and the checkpoint
psi_n in F_5^6 (15625 states):

```
psi_{n+1} = Pi_{t_n}(M_J psi_n),   t_n = popcount(n) mod 2  (Thue-Morse),
Pi_1 = Id (Flow),  Pi_0 = Snap (the sole source of irreversibility);
selector i = (z_n + 2 t_n) mod 5, the offset 2 the exponent in J = 1 + j^2;
about 25 integer operations per tick; zero multiplications, zero floats.
```

Under A0 the counter is internalized (ODOMETER-INTERNALIZED [D],
reproduce/foundations-places): the tick is a 2-adic odometer register
inside the state, the drive bit is the register parity with the exact
recursions t_2n = t_n and t_2n+1 = 1 - t_n and the carry parity law,
and the dynamics is one autonomous closed map with no external
parameter.

Space is a commutator: the commutator of translations is the discrete
curvature with golden spectrum in Q(sqrt5); the sealed corpus carries
the statement with spectrum {0^27, +- i phi^n / d} and denominator
20 = 4p, and its public witness is an open obligation together with
the trace value -21/8 of the squared curvature
(CURVATURE-TRACE-VALUE [O]).

The decoder D = D_clock o D_geom o D_matter has structure 1 + 3 + 0
and is acyclic: no feedback from output to state; time emerges as the
terminal accumulator. The gyron density is rho = 1/6 (GYRON-DENSITY
[T], registered in section 13). The reading split (READING-SPLIT [T],
inline): the decoder reads the kernel by linear projection, the
driver by binary Thue-Morse cut, the gauge housing by quadratic
registration; three sectors, one rule, and each leg is separately
registered: the linear readout is CODEC-TR4, the binary cut drives
the census, the quadratic registration is the Born square. The self
similar time quantum (TIME-QUANTUM-TOWER [C],
reproduce/foundations-places): on the ring Z/5^k the step operator
satisfies T^(5^k) = i_5 I with i_5^4 = 1 and period exactly 4 x 5^k,
computed for k = 1 to 4; the all k statement stands at the sealed
scope; explicit non claim: no generic exponentiation speedup.

## 3. The kernel and the census

F_5^6, 15625 states; the Klein-100 typology; 313 attractors. The
kernel is the concrete Cayley realization of the verb: the state space
is Z_5^6 with coordinates (p1, p4, p1p, p4p, q, t) and five involutive
generators, all arithmetic mod 5:

```
a  swap             (p1, p4, p1p, p4p, q, t) -> (p4, p1, p4p, p1p, q, t)
b  time inversion   x -> (-p1p, -p4p, -p1, -p4, -q, -t)
c  transport        piston -> b4(piston) + s + t u;  q -> 1 - q;  t -> -t
d  mirror           x -> c_d - x
e  shifted mirror   x -> (c_d + v_e) - x

s = (2, 1, 2, 1),  u = (0, 1, 0, -1),  c_d = (2, 1, 3, 4, 1, 1),
v_e = (0, 0, 0, 0, 1, 0);  b4 is the piston part of b.
Relations: a^2 = b^2 = c^2 = d^2 = e^2 = id and (bc)^5 = id.
Drive: t_n = popcount(n) mod 2 (Thue-Morse); phase z5(x) = sum of the
six coordinates mod 5; selection law i_n = (z5(psi_n) + 2 t_n) mod 5,
psi_{n+1} = g_{i_n}(psi_n) with (g_0, ..., g_4) = (a, b, c, d, e).
```

The census (CENSUS-313 [C], reproduce/census): the full enumeration of
all 15625 seeds, warmup 400 ticks and window 300, yields exactly 313
attractors: 312 of size 20 with basins of 50, and one singlet of size
10 with a basin of 25; the attractor support has 6250 states, the
basins cover all of Z_5^6, and 313 = 13^2 + 12^2. Every recurrent
state lies on the z5 sheet {1, 4}, so the selection law fires only b,
d, and e on the attractor: the recurrent algebra is the mirror algebra
(CENSUS-Z5-SHEET [C], reproduce/census). The piston pairing Phi =
(b4 d4 on pistons, identity on the fiber) is an involution that
permutes the 313 attractors with cycle type 144 transpositions plus 25
fixed points, the fixed points being 24 attractors of size 20 and the
singlet, so the classes modulo the pairing number 169 = 13^2
(CENSUS-PAIRING [C], reproduce/census). The hosting formula holds on
all 313 (CENSUS-HOSTING [C], reproduce/census): the return group
H1 = <d, b e b> has order 10, d o (b e b) is the line translation
T0 = (0, 0, 0, 0, 3, 2), and every attractor is the exact two coset
set A = H1 x' union b H1 x'. The boundary hyperplane: with s the
piston sum Tr_4 and M the z5 sheet, the boundary class
S = M cap {s = 0} has size 1250 exactly, the charged complement 5000
in two sheets of 2500, the boundary fibers 625 + 625, by full
enumeration of all 15625 states (HYPERPLANE-BOUNDARY-CLASS [T],
reproduce/hyperplane-codec); the census window realizes S as the
union of the 63 = (p^3 + 1)/2 boundary attractors, 62 of size 20 with
the singlet, and the charged sector as the remaining 250
(HYPERPLANE-BOUNDARY-REALIZATION [C], reproduce/hyperplane-codec).
The unique M_J readout is the trace character: the step matrix is
multiplication by J column by column, its characteristic polynomial
is Phi_5(x - 1) with det(2I - M_J) = 5 = p, the piston sum doubles,
Tr_4(M_J x) = 2 Tr_4(x), and the scalar multiples of Tr_4 are the
only covectors reading any multiplier at all (CODEC-TR4 [T],
reproduce/hyperplane-codec). The internal seal carries a further
clause, rate 4/5 exact, whose precise coding scope is not yet
reconstructed publicly; the clause is held open and unclaimed
(CODEC-RATE-SCOPE [O]).

Macro space is the coupled kernel. Cells couple on the entanglement
axis by the two way CSUM transvections, and the wedge
w_ij = x0_i x1_j - x0_j x1_i is the inter cell symplectic area. The
structure is exact (KERNEL-WEDGE-AFFINITY [T], KERNEL-WEDGE-COUPLING
[T], KERNEL-WEDGE-LINEAR-STRATA [T], KERNEL-WEDGE-AFFINE-MIX [T],
reproduce/kernel-connectivity): every generator is affine,
g(x) = M_g x + v_g with det M_g = 1, a and b linear, c, d, e strictly
affine; the two transvections generate SL2(F_5), order 120, the group
of the color door bridge, preserving all 15 wedges; the linear sector
acts by congruence W -> M_g W M_g^T and preserves the wedge rank
strata, with rank 0 exactly on dependent pairs; only the affine
translations cross strata, lifting exactly 62480 of the 78125
dependent pairs each for c, d, and e, and none for a or b. The single
cell component census over all seventeen recorded generator subsets
is exact (KERNEL-CELL-COMPONENTS [C], reproduce/kernel-connectivity),
from {ac} at 945 components down to the full verb {abcde} at 1: one
cell is connected by the five letters alone. Connected macro space is
the affine translational sector breaking inter cell symplectic
parallelism, organized by the SL2(F_5) coupling, with the wedge
automorphism a completing transitivity (KERNEL-MACRO-READING [D]);
this refines the commutator reading of space. The sealed corpus
carries the k = 2 theorem that the minimal connecting set is
{a, c, d, e} and the k = 3 full enumeration, both at internal scope
beyond the public budget; publicly the all k statement is a live
hypothesis with its falsifier (KERNEL-CONNECT-ALL-K [H]).

## 4. The two places

The framework lives at two arithmetic places, disjoint over Q:
Q(zeta_5) cap Q(zeta_8) = Q.

```
v_5 WRITES: home Q(zeta_5), real floor Q(sqrt5), state F_5^6; geometry,
    gravity, the native pentit substrate, the native magic C_5 (order 5,
    prime 5).
v_2 READS the quadratic mode: home Q(zeta_8), real floor Q(sqrt2), with i
    and the foreign qubit magic m = zeta_8 (order 8, prime 2); Clifford,
    Born, the outside read.
They meet only over Q. The layer boundary IS the field boundary.
```

The reading is not globally prime 2: the degrees split by prime,
linear to 5, quadratic to 2, cubic to 5, foreign magic to 2
(DEGREES-BY-PRIME [T], reproduce/foundations-places): sqrt5 lives at
zeta_5 by (2 phi - 1)^2 = 5, sqrt2 and i live at zeta_8 by
(m + m^-1)^2 = 2 and m^2 = i, and neither sqrt2 nor i lies in
Q(sqrt5), the unique quadratic subfield of Q(zeta_5). The Z2
symmetries split into two families (Z2-PLACES-SPLIT [T],
reproduce/foundations-places): cyclotomic Galois involutions at
exactly two places (one involution at zeta_5, the single order 2
element of the cyclic Galois group, where the forces split; a
complete Klein four at zeta_8, where every nontrivial element is an
involution), and the Thue-Morse time reversal, which is not Galois;
CPT = CP (Galois, zeta_5) composed with T (Thue-Morse); zeta_3 is
disjoint but unrealized: there is no third place. i is bilocated
(I-BILOCATED [D], reproduce/foundations-places): the order 4 element
of F_5* at v_5 and zeta_8^2 at v_2, identified only over Q, never
merged. Every genuine cross place transfer descends to Q; the Born
square is the descent operator; a transfer is rational, integer, or a
ratio: a definition, with the descent values carried by the Born
rows. The silver ring facts (SILVER-RING-FACTS [C],
reproduce/foundations-places): inside F_25 = F_5(sqrt 2), where the
step collapses to the doubling J = 2, tau = sqrt(J) has tau^4 = -1
with ord(tau) = 8, and F_25* is cyclic of order 24; norm, orders,
cyclicity, and census are finite computations. The silver sibling
(SILVER-SIBLING [D], reproduce/foundations-places) is the dictionary
reading resting on those facts: m = zeta_8 = sqrt(i) at prime 2 with
the silver unit 1 + sqrt2 of norm -1 mirrors tau = sqrt(J) at prime 5;
sqrt(i) is the square root of the axiom read at the foreign place. Charge conjugation is the swap
of the two Gaussian primes above p: 5 = (2 + i)(2 - i), the swap is
conjugation, carried inside Z2-PLACES-SPLIT; forces at sqrt5, spin at
sqrt2, charge conjugation at i.

## 5. The force is the curvature

A force is not added; it is the curvature of the genesis phase space.
The finite Weyl holonomy is exact on all five basis states
(FORCE-WEYL-HOLONOMY [T], reproduce/force-born-dictionary):

```
Z X Z^-1 X^-1 = j I;   the flux quantum is arg j = 2 pi / 5.
```

J = 1 + j^2 packages the force quantum; its two projections are the
two abelian forces (J-PROJECTIONS [T]).

Gravity is closed by three legs: the action leg (the cell action
864 pi at k = d(d + 1) = 12, derived from J); the observational leg
(quadrupole power against the Hulse-Taylor binary pulsar, 99.84
percent match [measured comparison]); the kernel leg (A_GD =
1/(8 pi) on the A_3 lattice, with lambda = 216 pi derived, not
fitted). Closed form:

```
G_nat = d^3 = 27 = 864 pi x 2 / (4 pi x 16).
```

The Coulomb layer separates the finite computation from the continuum
reading. On the finite decoder graph C4, the Moore-Penrose Green
kernel is

```
16 G = circ(5, -1, -3, -1),   L G = I - (1/4) 1 1^T,
```

with zero row sum (COULOMB-GREEN-COMPUTATION [C],
reproduce/force-born-dictionary). The continuum Green law
1/(4 pi r) is the same-propagator dictionary: gravity reads the
modulus and Coulomb the argument (COULOMB-PROJECTION [D]); it is a
scaling reading, not a value asserted on finite C4. The sign
structure is the polar dictionary (FORCE-POLAR-SIGN [D]): mass is a
modulus, one sign, universal attraction; charge is an argument, two
signs.

The classical Maxwell system closes exactly [MAXWELL-CLOSED at D,
the chain layer at T; reproduce/maxwell]: the Bianchi identity
holds identically in the 32 edge symbols and gauge invariance is
an identity (MAXWELL-BIANCHI); Gauss is the boundary equation on
the closed spatial torus, with a constructive dipole
(MAXWELL-GAUSS-CHAIN); the inhomogeneous pair closes with
conservation an identity in the 96 face symbols
(MAXWELL-AMPERE-CHAIN). The obstruction pair is counted in p
(MAXWELL-OBSTRUCTION-P): Gauss is solvable iff the total charge
vanishes mod 5; the current pair iff the current is conserved and
all four winding numbers vanish mod 5.

The abelian face dictionary (ABELIAN-FACE-DICTIONARY [D],
reproduce/force-born-dictionary) reads the electric half as P = J/2
on the 12 electric faces from the bare tick. The magnetic public
reading begins after the sealed six-ensemble selection; that
selection is not reconstructed or claimed here. The selected axiom
pair, stay or twist once, reads

```
Psi(k) = 1 + zeta^k,   mu(k) = |Psi(k)|^2 / 10 = w(k)/10
       = (2/5, (3+sqrt5)/20, (3-sqrt5)/20, (3-sqrt5)/20, (3+sqrt5)/20)
```

entrywise exact in Q(sqrt5) (BORN-FACE-WEIGHTS [T],
reproduce/born-faces); the slot 4 pair lands on the sigma_2 Galois
image exactly; the tilt magnitude is exactly sqrt5/5, with sign set by
the Thue-Morse slot orientation; the Legendre symbol (2|5) = -1 is
realized on this face.

Coupling seeds: the coupling root of a sector is the Gram weight of
its carrier direction; trace and conformal directions carry 1/p, the
spatial base carries 1; the 3/4 = d/(d + 1) measure attaches to
spatial gauge sectors only (MEASURE-SPATIAL-ONLY) [T]. alpha* = 1/p;
the strong root is 1 x 3/4 x 1 = 3/4 (STRONG-SEED) [D]; the seed
ratio EM to strong is 15 : 4. Dark
energy w = -14/15. Running and scheme are frontier rows
(ALPHA-S-RUNNING, SCHEME-DICTIONARY).

## 6. Alpha and the observable register

```
alpha = 5 S / ((8 pi)^2 sqrt(s)),   sqrt(s) = (3 - phi)^(1/4),
S = (1 + X/5)^-5,   X = 1 / (32 pi^2 phi^4)
alpha^-1 = 137.035999190;  CODATA 2022: 137.035999177(21)
                                            [measured comparison]
```

(ALPHA-FORM at D; the enclosure witness ALPHA-VALUE-DIGITS at C;
reproduce/alpha-value. The digit string and the CODATA window are
labeled witnesses of the committed form; no value is claimed beyond
it.)

The exact lemma (ALPHA-SEED [T], reproduce/alpha-exact-lemma): the
dimensionless trace target is exact, alpha* = 1/p, via the cyclotomic
Galois-trace Gram G = p I - 1 1^T with normalized spectrum {1/p
(once), 1 (p - 2 times)}, the all ones trace direction the
eigenvector; exact for p in {3, 5, 7, 11, 13}. Scope: alpha* = 1/p is
the dimensionless seed; the physical alpha^-1 lives at the bridge
level. Prefactor unification (ALPHA-PREFACTOR-UNIFICATION) [T]: with
B_{2,chi5} = 4/5 exactly, the Gauss sum tau = 2 phi - 1 = sqrt5
exactly in Z[zeta_5], and L(2, chi5) = 4 pi^2 / (25 sqrt5), the
witness formula and the formula above are one formula; no independent
L value enters the alpha sector; the prefactor reads
(1 + J Jbar)^(1/4): the gravity modulus inside the electromagnetic
number.

Weinberg (WEINBERG-FORM at D on the exact layer WEINBERG-TREE and
HYPERCHARGE-LAW at T; reproduce/weinberg): sin^2 theta_W = 3/13 +
1/(32 pi^2 phi^4), the committed form with its comparison fenced; the
tree value 3/13 = deg_f / (V + 1) with deg_f = Tr(J) = 3 and
V = 12 = d(d + 1). All seven standard model hypercharges follow
from Y_F = (B - L) + 2 T_3^R; B_quark = 1/3 = 1/dim ker(Tr), the
trace kernel of dimension 3. alpha is
built from L and X, both pi even, hence delta free (section 7).

## 7. The mass ladder and the parity law

With the single SI anchor m_e (the committed forms at MASS-LADDER-FORMS,
D; the theorem layer at T; reproduce/mass-ladder):

```
C_mu_tau = 89/5 = 18 - 1/p          (MU-TAU-COEFFICIENT)  [T]
mu_mu  = 2688/13 - (89/5) alpha^2     (+0.042 sigma)      [measured comparison]
mu_tau = 3477 + 240 (89/5) alpha^2    (-0.011 sigma)      [measured comparison]
exchange identity: delta mu_tau + 240 delta mu_mu = 0     [T, exact in Q]
         (MU-EXCHANGE-IDENTITY)
mu_p   = 6 pi^5 (1 + alpha^2 / 3)     the single bare pi^5, an odd carrier
mu_n   = mu_p + deg_v / chi - Delta_EM;  the bare neutron at -17.93 ppm
         [measured comparison];  Delta_EM open (NEUTRON-DELTA-EM)
the electron at the Dirac step:  det = 1 + m^2 = 5 = p
```

The parity law (PARITY-LAW) [T]: the bridge defect delta = 6 phi^2 - 5 pi
= (9 + 3 sqrt5) - 5 pi is nonzero by Lindemann-Weierstrass (about
+2.4 x 10^-4, a gap witness, labeled) (BRIDGE-DEFECT). Exact bridges: xi phi^2 = 5 =
p; script-Q phi^2 = 2 pi; script-Q / xi = 2 pi/5 = arg J. Under
complex conjugation every fundamental on the register is a pure parity
eigenvector: seventeen even and delta free (among them alpha^-1,
sin^2 theta_W, w = -14/15, L, Omega_b = pi^2/200, the slip X, mu_mu,
mu_tau, G, PMNS, the dark matter ratio, the zeta_K residue); three odd
delta carriers, the ladder pi^1, pi^3, pi^5 (the capacity 2 pi/phi^2,
the Kahler capacity 64 pi^3 phi^2, the proton 6 pi^5); one mixed
composite, the neutron, the boundary witness. The neutrino register
341/10 and the PMNS sector are carried at their committed labels, both
pi even and delta free; the sector waits on the mass mechanism
frontier.

## 8. The measure and Born

The Born quartet unpacks into four registered results, reproduce/born-quartet: BORN-HALF-ANGLE [T], BORN-RESIDUAL-SPLIT [T], SPIN-BISECTOR [T], and BORN-ORDER-STAIRCASE [T]. The Born unit group of
the read place residual algebra A_8 = Z[zeta_8]/5 is cyclic of order
24, and the unit square root of a phase is the Born normalized
bisector: (1 + u)^2 = u N_B(1 + u) on every Born unit; the bisector
normalizes to a unit square root exactly on the 11 non antipodal
units of the norm gated half, the squares of the unit group (at
u = -1 the bisector vanishes, so normalization is undefined there);
zeta_8 itself is ungated, so its halving forces the quadratic step
(BORN-HALF-ANGLE). The Born faithful
residuals are A_4 = Z[i]/5 and A_8 = Z[zeta_8]/5, split rings whose
two factors are swapped by conjugation, the Born involution
(BORN-RESIDUAL-SPLIT). The quarter turn spinor is R = (1 - B)/sqrt2
with det R = 1, carried exactly as det(1 - B) = 2 and (1 - B)^2 = -2 B
over Z and as an order 8 element of SL_2(F_25), the finite shadow of
the double cover (SPIN-BISECTOR). Each Born halving is one quadratic
step: the staircase of root orders 4 -> 8 -> 16 is first realized at
F_5 -> F_25 -> F_625, with minimality against every smaller degree
(16 divides none of 4, 24, 124), gated by the square condition on the
bisector norm (BORN-ORDER-STAIRCASE). No positivity is claimed in the finite
read: probabilities are the decoder step.

The measure dictionary reads the Born square of the verb
(MEASURE-BORN-VERB [D], reproduce/force-born-dictionary):
w(k) = |1 + zeta^k|^2, with its exact identities carried by
BORN-FACE-WEIGHTS [T] (reproduce/born-faces). The identikit: eight preregistered strikes died
first class and carved the survivor clause by clause: integer
amplitudes, a quadratic Born reading, Galois breaking, irrational in
position; counts may enter only as amplitudes. The kernel to cell
dictionary (KERNEL-CELL-DICTIONARY [D]): time is the clock tick;
space is the three F_5
directions of the trace kernel, isotropic under the Galois Gram; the
fiber is the Z_5 edge variable with F = dA; deposits are additive,
valued in fifths, flux quantum zeta_5; amplitudes are unimodular; the
measure is the Born square.

The substrate knit (SUBSTRATE-KNIT [T],
reproduce/force-born-dictionary): the two abelian faces are the two
conjugate Born readouts C_+ = I + S and C_- = C_+^T of a single verb
state; C_+ C_+^T = circ(2, 1, 0, 0, 1) with exact spectrum w; the
position and Fourier face bases are mutually unbiased, 1/5 on all 25
pairs; the Plancherel masses are 2 and 10, in the ratio p = 5.

## 9. The photon and the electron

The quantum is an integer path count, one bit per tick, on an RP
Hilbert space. The photon window has exact coordinates
(PHOTON-WINDOW-COORDINATES [T], reproduce/photon-electron): the point
w = (4, phi^2, phi^-2, phi^-2, phi^2) and its Kramers-Wannier dual
what = 5 (2, 1, 0, 0, 1) with chat = w exactly, w not self dual, and
the tilt w(1) - w(2) = sqrt5. The quantum costs one bit per tick on
every center, what(1)/what(0) = 1/2, and every class |k| >= 2 is
exactly closed for p >= 5 (PHOTON-UNIVERSAL-BIT [T]). Monopole charge
exists only in lumps of five (MONOPOLE-FIFTHS [T]); the elementary
monopole costs between 17 and 21 occupied faces (MONOPOLE-COST [C]).
The window proof is reduced to one combinatorial lemma with the two
integer gap 32 < 2401 < 131072: straight runs cost 5 bits per
segment, the 1 x K ladder bound is exactly 9K + 8, and the greedy
incidence identity holds (KAPPA-BOUNDS [T]); the nine shape library
realizes the exact bound table with minimum 31/8 bits per segment and
the integer margin 2^31 > 7^8 (KAPPA-SHAPES [C]). The remaining lemma
and the electric face certificate are the frontier row
PHOTON-WINDOW-PROOF (section 18). The center split: conjugation swaps
the residue channels exactly for p = 3 mod 4 and preserves them for
p = 1 mod 4, with Gauss sums g^2 = -3, +5, -7
(CENTER-SPLIT-RECIPROCITY [T]); the same verb freezes p = 2 and
leaves p = 3 with full dual support (CENTER-SPLIT-CLOSURE [T]); with
the declared self duality import (the 4D Z_N window opens only for
N >= 5), the first prime passing both doors is p = 5
(CENTER-SPLIT-SELECTION [D]). The photon belongs to the null light
branch, E+ E- = 0 identically.

The electron: g = 2 = (2 pi/5) / (pi/5) is the vertex flux over the
spinor half angle, the reading ELECTRON-G-TREE [D] on exact pillars:
sixteen identities with the pivot 1 - J = e^(-i pi/5) and the polylog
ladder halving 2 pi/5 -> pi/5 -> pi/10 (ELECTRON-G-RATIO [T],
reproduce/photon-electron); one drive arg j, spinor pi/5 per step
through the diagonal bridge, ratio 2 at every step, closure pair
(5, 10), R^5 = -I (ELECTRON-G-DOUBLE-COVER [T]). The electron sign is
measured into existence (ELECTRON-SIGN [D]): the charge sign is the
orientation, ghost {a, c} against live {b, d}, of the single gyron
anchored engagement of a defect worldline, pair neutrality is
realized through the annihilation sink, and the sign Z_2 equals the
initial datum [z5(B_0) = 4]. Seven exhaustive public laws carry it
(ELECTRON-SIGN-LAWS [T], reproduce/photon-electron): the count parity
as initial datum; the forced event slot with the phase locked forever
after; the annihilation census decided by tick 3; the eps ledger
summing to zero; one Z_2 across the five readouts; the closed 20
state pair cycles with equal stable supports; and the transient shift
and Galois images.

The Dirac ladder closes [DIRAC-LADDER at D, the theorem layer at T;
reproduce/dirac-ladder]:

```
G1  u = 2 phi^n, v = 2 phi^-n, u v = 4      the light cone           [T]
    (LADDER-LIGHTCONE)
G2  N(phi) = -1                             the spinor floor         [T]
    (SPINOR-FLOOR)
G3  the ladder root is the cat map carrier: F^2 = C over Z; mod 5 one
    Jordan block; towers of order 20 = 4p and 10 = 2p, -I at half    [D, T]
    (FIB-ROOT-CARRIER at D on the exact ties FIB-ROOT-TIES at T)
G4  D_J(m) = S (I + i m X), zero free parameters: streaming is the
    counter, the coin modulus is the rest rung, the phase i is the
    plenum ellipticity; massless is the one sided shift; det = 1 + m^2
    = 5 for the electron; the mass shell is exact; the rest coin has
    infinite order                                                   [D, T]
    (DIRAC-STEP at D on the theorem layer DIRAC-STEP-THEOREMS at T)
G5  the ladder Z_2 (conductor 5) and the spin Z_2 (conductor 8) are
    distinct place attached Galois involutions (LADDER-SPIN-PLACES)  [T]
```

The checkerboard between the rungs is a Gaussian tower [D at the
reading, within DIRAC-LADDER; T at the tower, CHECKERBOARD-GAUSS-TOWER]:
one binomial pair per case; the diagonal lives in Z with pair weight
-4, the cross in iZ; the totals are (1 + 2i)^n with recursion
x^2 - 2x + 5 and c^2 + d^2 = 5^n; zone edges -5I for the electron and
-I for the photon. The eta naming clause stays a remark; only its
named gate can move it (ETA-ALTERNATOR-BRIDGE). The fermionizer
Phi_f(s) = 1 - 2^(1-s) (FERMIONIZER) [T]: the two that makes matter
out of light. One beat is one boost times one alternator tick
(LADDER-ALTERNATOR-BASIS) [T]; the alternator is breath at one scale
and Thue-Morse at every scale (TM-BREATH-TOWER) [T].

## 10. Relativity as counting

The group generated by the icosahedral rotations and the J boost is
dense in SO+(3,1); the boost rapidity is ln phi. The exact boost
reading split (BOOST-READING-SPLIT [T]; reproduce/observer-boost) is

```
C_n = phi^n + phi^-n,   S_n = phi^n - phi^-n,
(C_n, S_n) = (L_n, sqrt(5) F_n)        for n even,
(C_n, S_n) = (sqrt(5) F_n, L_n)        for n odd.
```

Indeed psi = -phi^-1, while the Binet identities are
L_n = phi^n + psi^n and sqrt(5) F_n = phi^n - psi^n; substitution
proves the split for every nonnegative integer n. Consequently
beta_n = S_n/C_n obeys the exact addition law
beta_(m+n) = (beta_m + beta_n)/(1 + beta_m beta_n), and
C_n^2 - S_n^2 = 4 is the parity-resolved form of
L_n^2 - 5 F_n^2 = 4 (-1)^n.

The count ladder (BOOST-COUNT-LADDER [D]) reads n as the substrate's
integer rapidity count and beta_n as the decoder velocity; the
dictionary rests on the exact split and the exponent law
B_J^m B_J^n = B_J^(m+n). The observer alternator
(OBSERVER-ALTERNATOR [D]) reads mu_4 as 1 + 3, whereas multiplication
by lambda = -1 has the two orbits {1, -1} and {i, -i}, giving the
substrate partition 2 + 2. In the commuting diagonal model
B_J = diag(phi, phi^-1), A = diag(1, -1), the name boost axis
(BOOST-AXIS [D]) is the reading of the two exact A eigendirections.
No claim that any of these three dictionary choices is forced is made.

## 11. The pentit ring and the magic boundary

sqrt(phi) = tau^3 [T]; sqrt(J) = tau [D]; the valuations add as
0 + 1 = 1 [T]. F_25* = C_24 = C_8 x C_3; the golden content sits on
the gate line, the clock is norm one; the argument is not the clock,
and the time quantum lives on the gate, not the clock. The magic prime
gate [T]: N(tau^k) = 3^k = 2^-k in F_5*; the source closes after two
time quanta, half the Frobenius period; sqrt(J) sqrt(phi) = tau^4 =
-1; phi = J^-1 in F_5.

The qubit from F_5 [T]: C^(F_5*)/Z_2 = V_+. The magic boundary at
F_25: Eastin-Knill as arithmetic; magic is the stabilizer dimension
deficit; the native magic is the cubic C_5 (order 5, prime 5), the
foreign qubit magic is m (order 8, prime 2). Bell and Tsirelson:
zeta_5 caps at (sqrt5 + 1)/2, the zeta_8 magic reaches Tsirelson [T].
The Fibonacci category with central charge c = 14/5 is mathematical
background; its physical reading fired: the phibit is abelian Z_5, not
the tau anyon (PHIBIT-NOT-TAU [F], reproduce/hyperplane-codec). The
boundary proof is finite: the phibit fusion ring is the group ring of
Z_5, five simples, all invertible with dimension 1; the Fibonacci
ring obeys tau tau = 1 + tau, its dimension satisfies d^2 = d + 1
with no rational root, d = phi, and tau has no fusion inverse; five
invertible simples cannot land on a ring with one. The dead physical
reading is archived, not deleted.

## 12. The color door

The non abelian bridge is structural. Z[zeta_5] supplies the
icosahedral torus; the binary icosahedral group 2I = SL_2(F_5) is the
finite color core; color su(3) is read on the traceless endomorphisms
of the three dimensional trace kernel. This section closes the exact
eleven-rung ladder to the core. It does not close QCD running,
confinement, or the measure lift from the core to the full
SL_3(F_5) carrier.

Rungs 1 and 2 (COLOR-RETURN-D5 and COLOR-TORSOR-HOLONOMY [T],
COLOR-SPLIT-12 [D], reproduce/color-ladder): the return group is
D5 of order 10 with integer Plancherel mass M(E) = 10 |E|. The 312
size-20 attractors have a free D5 half; the singlet half is the five
reflection axes. The recurrent spatial holonomy is a Klein four
group, orientation is tick parity, and the pairing involution Phi lies
in SL_3(F_5). Its eigenspaces give the dictionary split 3 = 1 + 2.

Rung 3 is the binding negative turn. COLOR-DYNAMICAL-COLOR [F]
(reproduce/color-ladder): within the registered dynamical candidate
families the generated census symmetry group has order 20 and its
special-linear spatial image is only {I, Phi} = Z_2; the non abelian
dynamical-color falsifier fired. The surviving kinematical statement
is exact. COLOR-KIN-NORMALIZER [T]: the filtered product-affine
normalizer has 40 x 480 = 19200 elements and every one permutes the
313 attractor supports. COLOR-KINEMATICAL-GL2 [D]: its special-linear
image is read as GL_2(F_5), order 480, on the antisymmetric plane,
embedded by g -> (det g)^-1 direct-sum g along 3 = 1 + 2.

Rung 4 (COLOR-CORE-2I [T], reproduce/color-ladder): the special-linear
core has order 120, is perfect, has center {I, -I}, and has class
sizes (1, 1, 12, 12, 12, 12, 20, 20, 30), hence is
2I = SL_2(F_5). The block trace by element order is
{1:2, 2:3, 3:4, 4:0, 5:2, 6:1, 10:3}; the pentagonal values {2, 3}
are the ramified shadow of the golden pair.

Rung 5 (COLOR-GOLDEN-TABLE [T], reproduce/color-ladder): the full
9 x 9 character table is exact over Q(sqrt5), orthogonal by rows and
columns, and Galois stable. The core has one involution, so D5 does
not embed; the loop pair lifts through Dic_5 and reflections acquire
order 4. The spin-lifted pair reads the icosahedral edge module, the
pentagonal spin weights are the Born squares of the golden
amplitudes, and the 5-regular block traces are the ramified Brauer
shadow of the golden spin row.

Rung 6 (COLOR-MCKAY-E8 [T], reproduce/color-ladder): tensoring by the
spin row gives affine E8 with marks equal to representation
dimensions. Its closed-walk moments equal the Catalan numbers through
degree 10; finiteness first appears at degree 12 by one,
133 = 132 + 1. The verb weights are {4 phi^-2, 4 phi^2}, with product
16.

Rung 7 (COLOR-MOMENT-FINGERPRINT [T], reproduce/color-ladder): the
moment series is N/D, where N and D are the matching polynomials of
finite and affine E8, and

```
120 m_n = 2^(n+1) + 40 + 24 L_n
```

for even n. Also 1 - J = -zeta_5^2 is a primitive tenth root of
unity, joining the D5 order to the J shadow without a new parameter.

Rung 8 (COLOR-SPECTRAL-INVARIANTS [T], reproduce/color-ladder): the
partial-fraction weights are exactly the class masses |C|/120. The
Molien series is

```
(1 + t^30) / ((1 - t^12)(1 - t^20)),
```

so the invariant degrees are (12, 20, 30) = (vertices, faces, edges)
with one relation at 60. The Platonic excess is
1/2 + 1/3 + 1/5 - 1 = 1/30 = 1/h(E8).

Rung 9 (COLOR-DICKSON-RAMIFICATION [T], reproduce/color-ladder): at
the ramified place the invariant forms are

```
E_6 = u^5 v - u v^5,
D_20 = (u^5 - u v^4)^4 + v^20.
```

They are algebraically independent and the modular invariant ring is
free on degrees (6, 20). In general
(V, F, E) = (2(p+1), p(p-1), p(p+1)) and V - E + F = 2 identically.

Rung 10 (COLOR-KLEIN-REDUCTION [T], reproduce/color-ladder):
T^2 + H^3 = 1728 f^5 holds exactly in Z[u,v], with 1728 = 12^3.
At the ramified place invariant reduction has shape
(alpha E_6^2, beta D_20, gamma E_6^5); freeness forces beta = 0 and
gamma^2 = 3 alpha, with good alpha in {2, 3}. The modular invariant
tower is the Artin-Schreier tower t -> t^5 - t.

Rung 11 (COLOR-INTEGRAL-LIFT [T], reproduce/color-ladder): the two
matrices

```
S = ((0, -1), (1, 0)),   T = ((zeta, 1), (0, zeta^4))
```

close to exactly 120 matrices over Z[zeta_5], and reduction modulo
(1 - zeta) is a bijection onto SL_2(F_5). The engine identity is
(1 - zeta)^4 = 5(zeta^2 - zeta - zeta^3). The Hessian reduces to the
Dickson form; in the Klein gauge the explicit orbit realizes
gamma^2 = 3 alpha.

COLOR-MEASURE-TRANSPORT [T] (reproduce/color-ladder): the golden dual
measure is transported from D5 onto the 2I core through the exact
character, verb, and spectral class measures of rungs 5 to 8. The
remaining lift from the core to the SL_3(F_5) carrier with its
2 pi U(1) circle remains COLOR-MEASURE-SELECTION [O].

## 13. Gravity and cosmology

The bridge law alpha B g = 1; G proportional to alpha^20 with the
geometric factor (32/33)^2 = (2^5/(2^5 + 1))^2; m_e the single SI
anchor (GRAVITY-BRIDGE-LAW at D: the equation layer, with
g = 2^5 phi^2 sqrt(3 - phi) carried exactly through its square; the
SI value of G stays on the frontier; reproduce/gravity-chain). The
Kahler capacity V_geo = (4 pi)^3 phi^2 = 64 pi^3 phi^2
(KAHLER-CAPACITY) [T]: from the single Kahler metric
h(z) = (J Jbar)^-1 (1 + |z|^2)^-1, the order 2 jet gives Fubini-Study
(4 pi)^3 and the order 0 jet gives h(0) = phi^2, since
J Jbar = phi^-2 exactly. The FRW rank 1 canonical form
(FRW-CANONICAL-FORM) [T]: H^2 = 72 pi rho_phys with lambda = 216 pi
from the rank 1 lapse action; the fiber multiplier k_f = 1 is forced
by the master closure against G_nat = 27 = d^3, with the cell volume
864 pi carrying exactly one fiber 2 pi; the source projector is
unique; the source is a matter amplitude, rho = rho_0 ell^2. E_total =
0 is a theorem of the closed whole under A0. The ell-G wall is a
mechanism wall: ell_P / lambda_e = (32/33) alpha^10 / sqrt(g), with
the exponent identity G_T = alpha^(20 + sigma) (GRAVITY-BRIDGE-LAW).

Cosmology (reproduce/cosmology-register): the tilt is n_s - 1 =
-p alpha = -5 alpha at H (NS-TILT, falsifier live at CMB-S4). The
deformation J -> J e^(i eps) freezes the modulus, so r = 0 at linear
order about the isotropic background (TT-LINEAR-ZERO) [T]; the
bilinear TT decoder permits induced tensor power at quadratic field
order (TT-QUADRATIC-INDUCED) [D]; a numerical r(k) waits on the
vector state normalization (TT-VECTOR-STATE-NORMALIZATION). Dark
energy w = -14/15; Omega_b = pi^2 / 200; Omega_DM / Omega_b =
18 p^3 ln^2(phi) / pi^4, and the dark matter ratio 5 : 1 follows from
Thue-Morse pair statistics (COSMOLOGY-REGISTER at D, the committed
forms with fenced comparisons); the gyron density rho = 1/6
(GYRON-DENSITY) [T, quadruply confirmed]: the gyron gate is the
Thue-Morse pair (0, 0), and 1/rho = 6 = p + 1 is the proton
prefactor of the mass ladder. The conformal mode prefactor K_chi5 =
1/(864 pi) is derived at the homogeneous L5 scope from the single
layer 5 action, with c_hom = 12 K_chi5 = 1/(72 pi)
(CONFORMAL-PREFACTOR) [D]; the
inhomogeneous scalar action and the SI clause stay open (FRW-INHOM,
METRO-EDGE-SCALE). N is the cosmic clock, carried at its committed
labels within COSMOLOGY-REGISTER.

## 14. The gravitational wave program

The TT decoder is the complex squaring map with kernel {+-1}, the spin
double cover; volume neutrality is det = 1 - |h|^2 exactly; one
propagation law c = 1 - s^2: breathing +1, photon 0, TT square -3
(TT-SQUARING-DECODER) [D; reproduce/coupling-metrology]. The minimal
exponential ringdown reading is dead in the GW channel
(RINGDOWN-EXPONENTIAL-DEAD) [F; 7.8 sigma at WKB3 grade, labeled
engineering]. Stage A, the Schwarzschild TT endpoint: the
Regge-Wheeler coefficients (1, 0, -3) are forced at scope, V_2 =
f (L/r^2 - 6M/r^3), and Lichnerowicz uniqueness holds at the family
and witness scope (SCHWARZSCHILD-TT-ENDPOINT) [T at scope]; covariance
alone is not sufficient, a computed boundary. Stage B input: the
quadratic germ of the action is sealed at scope mu = 1 with the
pairing dictionary Z_L2 = 1/2, and the free Gaussian vector reading is
a computed fired boundary (TT-QUADRATIC-GERM) [D]; the single
remaining input is g_mu (TT-GAUGE-PULLBACK). The mu corridor: mu at least 0.804 at 3 sigma and
shadow excess in [0, +0.93 percent], ngEHT decides [measured
comparison]. The emission map, the quasinormal mu decision, and the
polarization readout stand open (TT-SOURCE, QNM-LEAVER-MU, POL-READ).

## 15. Couplings, instruments, and metrology

Couplings determine instruments; effects are the shadow; the
density against the Gram form is rho_psi = psi psi^dagger G /
(psi^dagger G psi), and the Born value is the branch G norm; the
gyron carrier admits no alternative at its scope; instrument
uniqueness resolved by falsification: effects underdetermine,
couplings determine, fired as registered (COUPLINGS-DETERMINE) [T,
with the fired boundary carried at scope; reproduce/coupling-metrology].
The covariant canonical form: the dressing coefficient is the DeWitt
norm, 12 = d(d + 1) at lambda = -1, and the level 1 to level 2
normalization inheritance is closed, the chain of twelves exact
(DEWITT-TWELVES) [T at scope]. Metrological
admissibility is closed for normalized one dimensional rational finite
state protocols by a sealed quartet of theorems with the sharp gyron
window pair; the residual is METRO-ADMISSIBILITY. The
tick clause is closed dimensionless: delta tau hat = 1/5 cycle =
2 pi/5 per tick (METRO-TICK) [T at scope]; the remainder is the canonical selector on the
commutator phi ladder and the SI clause (METRO-EDGE-SCALE). The
dressing insertion bookkeeping carries the exact witness 72 alpha^4
(about 0.204 ppm, labeled) with the form decision gated on the integer
crossing count (DRESS-CROSSCOUNT). The Lorentz burden of the dynamics
from action chain stands (LORENTZ-A2A3); the finite chain itself is
sealed end to end. The state update, Gram, and dagger clauses of the
quadratic decoder are closed at scope; the effects on data clause
stands (QUADRATIC-DECODER-DATA).

## 16. p = 5 and the wall

Thirteen independent witnesses lock p = 5: seven selectors and six
structural theorems; root selection [T]; the Fermat collapse; the
1/p trace spectrum; the ramified residue phi^2 = -1; the Diophantine
p^2 + p + 2 = 2^p; ord(2 mod 5) = phi(5); the native Z_5 qudit;
1/rho_0 = d(d + 1)/2 = 6; the qubit from F_5; the magic boundary at
F_25; the Lorentz density unique to Z[zeta_5]. The two logarithmic
axes: pi on the argument (c odd), ln phi on the modulus (c even,
transcendental by Baker); linearly independent over the algebraic
numbers (LOG-AXES-INDEPENDENCE [T]). No algebraic independence claim
is made.

The wall is one archimedean wall, and it is understood: the shadow is
the polylogarithm ladder of J. What stands on it: the quantum
substrate gates, Larmor and the Schwinger term, the term carrying the
hypothesis value J Jbar / script-Q = 1/(2 pi) (QUANT-SUBSTRATE); the
non abelian measure lift (COLOR-MEASURE-SELECTION); and the shared
2 pi U(1) circle itself, with pi the locked shadow.

## 17. Engineering witnesses

Witnesses, not theorem promotions; every number here is an engineering
readout or a measured comparison, labeled by this sentence.

```
random circuit sampling   bit exact in Z[zeta_24] and Z[zeta_360];
                          four way bit exact
native Z_5 qudit suite    tableau, dense, shadows, magic, Wigner;
                          110000000 circuits, zero failures; three
                          independent invariants forced to agree
integer Clifford+T        bit exact statevector across six platforms
Z_5 gate set              ZX = j XZ; Bell, GHZ, Grover; the 313
                          attractors reproduced on independent code
exact chemistry bridge    hydrogen to 6 significant figures; helium to
                          0.19 mHa; alpha reproduced to 0.095 ppb
```

The standing bar for a computation only theorem is byte identical
stdout on two architectures; in this repository that bar is the public
check plus a local run on a different architecture.

## 18. The frontier

The live obligations and hypotheses of the program. Each identifier is
a registry row with status O or H; the registry carries for every row
a concrete falsifier or a decision condition: what closes it
positively and what closes it negatively.

```
MEASUREMENT AND METROLOGY
  METRO-ADMISSIBILITY        beyond one dimensional rational finite
                             state protocols: higher dimensional
                             supports, non finite state streams,
                             unbounded memory, stochastic protocols,
                             irrational carriers, cross layer
                             normalization, physical units
  METRO-EDGE-SCALE           the canonical selector on the commutator
                             phi ladder; the SI clause (the second and
                             the meter over the single m_e bridge)
  DRESS-CROSSCOUNT           the integer crossing count per observable;
                             witness 72 alpha^4, labeled
  QUADRATIC-DECODER-DATA     the effects on data clause; state update,
                             Gram, and dagger clauses closed at scope
DYNAMICS AND RELATIVITY
  LORENTZ-A2A3               the Lorentz burden of the dynamics from
                             action chain
THE WALL
  QUANT-SUBSTRATE            the Larmor gate and the Schwinger term gate
  COLOR-MEASURE-SELECTION    the measure lift onto SL_3(F_5): 24 carrier
                             orbits, 16 observable types; the minimal
                             new datum is a weight vector
GRAVITATIONAL WAVE
  TT-GAUGE-PULLBACK          Stage B, gated on the single input g_mu
  TT-SOURCE                  the emission map
  QNM-LEAVER-MU              the quasinormal mu decision
  POL-READ                   the polarization readout
  TT-VECTOR-STATE-NORMALIZATION  the only gate yielding a numerical r(k)
COSMOLOGY
  FRW-INHOM                  the inhomogeneous sector, the named
                             classical horizon
  NS-TILT                    n_s - 1 = -5 alpha; falsifier live, CMB-S4
  DE-CONFORMAL-WEIGHT        the dark energy conformal weight
COLOR
  ALPHA-S-RUNNING            the running above the 3/4 seed
  SCHEME-DICTIONARY          exact seeds to measured couplings
  FIBER-THRESHOLD            the fiber doublet threshold
  GENERATIONS-L3             the generation structure at the L3 frontier
ELECTRON AND LADDER
  ETA-ALTERNATOR-BRIDGE      the eta naming clause and its gate
  SPIN-LIFT-FORCED           whether the dicyclic spin lift is forced
PLENUM AND KERNEL
  KC3-PLENUM-READOUT         the residue class readout of the ramified
                             place
  SQRT-PHI-TIME-GRAVITY      the dynamical face of the time gravity door
  CODEC-RATE-SCOPE           the rate 4/5 clause of the internal codec
                             seal, held open until its precise coding
                             scope is reconstructed or the clause is
                             struck
  KERNEL-CONNECT-ALL-K       {a, c, d, e} with the two way CSUM ring
                             coupling connects every (F_5^6)^k; the
                             k = 2 and k = 3 witnesses live at the
                             sealed scope
  CURVATURE-TRACE-VALUE      the trace value -21/8 of the squared
                             discrete curvature; the commutator
                             operator and its golden spectrum stand at
                             the sealed scope
MEASURE
  QUADRATIC-ENVELOPE-DECODER the full decoder carrier hypothesis
  TM-SYM2-MEASURE            the symmetric square measure; residual the
                             Born phase halving 1/6 = (1/2)(1/3)
MATTER
  NEUTRON-DELTA-EM           the interior compression channel
  PROTON-RESIDUAL-IS-QCD     gated on QCD dynamics
OBSERVER
  OBSERVER-WRITE-PORT        armed, algebraic; ordered after the
                             metrology closure
STANDING PREREGISTRATION
  PHOTON-RADIATIVE-INDEPENDENCE  radiative independence
EMPIRICAL HORIZON
  DESI DR3 (w = -14/15); MOLLER (sin^2 theta_W); ngEHT (the mu
  corridor); CMB-S4 (the tilt)
```

## 19. Verification and the registry

Every registered claim lives in canon/REGISTRY.tsv with its status,
scope, canon section, evidence, and falsifier. Claim identifiers are
status neutral and never change; statuses move in the registry.
Evidence is inline (a self contained derivation in this document), a
minimal reproduction under reproduce/, or a named external manifest.
Run any reproduction from the repository root:

```
python3 reproduce/kernel/verify.py
python3 reproduce/alpha-exact-lemma/verify.py
python3 reproduce/born-faces/verify.py
python3 reproduce/census/verify.py
```

Each must exit 0 with byte identical stdout against its EXPECTED.txt.
During synthesis, a status-labelled statement without a registry
identifier is unfinished draft material, not a public claim. Before
the synthesis pull request opens, it must be registered with
evidence, rewritten as a definition or remark, or removed. The
reconciliation audit maps every public claim to an internal claim of
equal or stronger status and scope. Simplicity is the ultimate
perfection. Truth is not rude. Truth is just true.
