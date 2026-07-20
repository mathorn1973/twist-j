# TWIST-J Public Canon v12

**Release identity.** Public Canon v12. Normative authority and activation
state are declared exclusively by [STATUS.md](../STATUS.md). An identical
tree on any other ref is a release candidate, not a second authority.

**What TWIST-J is.** TWIST-J tests one risky hypothesis: physical
reality is a closed, exact, deterministic integer system; continuum,
geometry, probability, and fields are readings of it. Its single
algebraic axiom is J. Public Canon v12 also declares the discrete
architecture used to read that axiom. Those architectural definitions
are inventoried below and are not claimed to be uniquely derived from
J. No fitted dimensionless parameter is introduced in the stated
forms; the single SI calibration anchor is the electron mass m_e.

**Axiom (A0).** Reality is the closed integer J-Cayley plenum. Its
algebraic generator is J = 1 + zeta_5^2. The public model has no
external boundary and no external clock: after the architecture below
is declared, one state determines its successor by one map U. J is the
seed of the two algebraic projections. Public Canon v12 does not claim
that the checkpoint space, the five kernel generators, the selector,
or the decoder interface are uniquely forced by J or M_J.

CZ: A0. Skutecnost je uzavrene celociselne J-plenum. Jeho algebraickym
generatorem je J = 1 + zeta_5^2; diskretni architektura je ve verejnem
Canonu v1 deklarovana zvlast a neni vydavana za jednoznacny dusledek J.
System nema vnejsi hranici ani vnejsi hodiny.

**Reading.** Time is a counter. Space is a commutator. J is the verb;
phi and pi are projections of J, not primitives. The assignment of
the modulus to gravity and scale and of the argument to
electromagnetism and phase is the public dictionary
AXIOM-PROJECTION-DICTIONARY [D], not part of the algebraic theorem.
Plenum, not vacuum.

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
in F_25; m_8 = zeta_8 = sqrt(i) at prime 2. The Dirac mass variable is
m_D. The clock counter is n, its Thue-Morse bit is theta_n, and the
sixth finite-kernel coordinate is r. T_pl denotes the plenum point;
M_J denotes multiplication by J. The finite phase character is z_6 =
Tr_6 and the piston character is Tr_4. The ramified chord is s_J and
the kernel transport offset is s_c. p = 5 and d = 3 throughout.
The tensor-to-scalar ratio is r_T(k), distinct from the finite-kernel
coordinate r and the radial coordinate used in continuum formulas.
K_chi5 = 1/(864 pi) is the conformal mode prefactor.

**Primitive and architecture inventory.**

```
algebraic axiom        J = 1 + zeta_5^2
derived algebra        j, phi, pi, M_J, L, and T_pl
declared architecture  Omega, U, F_5^6, a,b,c,d,e, and the selector
decoder interface      D_matter, D_geom, D_clock (partial at v1)
calibration anchor      m_e only
```

This is a definition boundary, not an omitted reduction theorem. Every
downstream statement is conditional on the declared architecture.
Restoring a stronger compression slogan requires a public theorem
deriving the architecture from J; Public Canon v12 contains no such
theorem.

---

## 1. The axiom and the two projections

J = 1 + zeta_5^2 is a cyclotomic unit: N(J) = 1 and Tr(J) = 3 in
Q(zeta_5), with Galois conjugate moduli (phi^-1, phi, phi, phi^-1)
(J-UNIT [T], reproduce/kernel). Its two archimedean projections are:

```
|J|    = 1/phi        the modulus projection
arg(J) = 2 pi / 5     the argument projection
```

Derivation (J-PROJECTIONS [T]): with j = e^(2 pi i/5), J = 1 + j^2 =
2 cos(2 pi/5) e^(2 pi i/5); 2 cos(2 pi/5) = phi - 1 = 1/phi, so
|J| = 1/phi and arg J = 2 pi/5. The algebraic half is exact in the
kernel witness as J Jbar = 2 - phi = phi^-2 (J-MODULUS-CHORD [T],
reproduce/kernel).

AXIOM-PROJECTION-DICTIONARY [D] reads the modulus projection as
gravity and scale and the argument projection as electromagnetism and
phase. It also reads the CRT factors of T_pl as the prime 5 write and
prime 2 read and the unit and ramified chords as the gravity and space
channels. These assignments rest on the exact rows above and below;
they are neither algebraic consequences nor uniqueness claims.

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

The plenum point (PLENUM-POINT [T]): T_pl = s_J + i phi = 2i(1 - J)
with s_J^2 = 1 + J Jbar = 3 - phi = sqrt5/phi. Derivation: J Jbar =
2 - phi gives s_J^2 = 3 - phi, and (3 - phi) phi = 2 phi - 1 =
sqrt5. |T_pl| = 2; arg T_pl = 3 pi/10; zeta_5 T_pl^2 + 4 = 0,
since T_pl^2 = -4 j^4; T_pl^10 = -2^10; T_pl/2 = zeta_20^3,
and the CRT split is T_pl/2 = zeta_4^-1 zeta_5^2. The ramified chord
s_J = |1 - zeta_5| obeys N(1 - zeta_5) = 5
(J-RAMIFIED-CHORD [T], reproduce/kernel), while the modulus chord is a
unit chord. Their physical channel assignment belongs only to
AXIOM-PROJECTION-DICTIONARY [D]. At the magic prime the axiom has a
square root: sqrt(J) = tau in F_25 (section 11).

## 2. Time, space, and the decoder

The autonomous state is not the finite checkpoint alone. It is

```
Omega = N_0 x F_5^6,                    omega = (n, psi),
theta_n = s_2(n) mod 2,                 z_6(psi) = sum_k psi_k mod 5,
sigma(omega) = z_6(psi) + 2 theta_n mod 5,
U(n, psi) = (n + 1, g_{sigma(omega)}(psi)),
(g_0, g_1, g_2, g_3, g_4) = (a, b, c, d, e).
```

Here s_2(n) is the finite binary digit sum. The clock coordinate N_0
is the distinguished forward orbit 0, 1, 2, ... of the 2-adic
odometer, embedded in Z_2. No Thue-Morse parity function on all of Z_2
is asserted. The finite checkpoint projection is
pr_checkpoint(n, psi) = psi; psi by itself is not claimed to be an
autonomous state. The driver word and every registered event log are
derived orbit records, not additional state variables. For a binary
observable lambda supplied by a registered decoder claim, its Log is
(lambda(U^k omega_0))_{k >= 0}.

The counter closure (ODOMETER-INTERNALIZED [D],
reproduce/foundations-places) is exact on this forward orbit:
theta_{2n} = theta_n, theta_{2n+1} = 1 - theta_n, and the local carry
law updates theta without consulting an external list. Therefore U
has no external step parameter. This is an autonomous skew product by
definition; no extension of theta to every 2-adic integer is used.

The phrase "space is a commutator" remains a dictionary reading, not a
unique curvature construction. One historical construction is now typed
exactly. Let X = F_5^6, F = Q^X, H = <b,d>, let R_H be Reynolds averaging
over H, and let P_0 remove the constant function. With

```
V = F^H intersect 1_X^perp,             dim V = 818,
C_0 = T_a T_c - T_c T_a,
K_hist = (P_0 R_H C_0 R_H P_0)|_V,
```

two complete exact routes give

```
Tr_V(K_hist^2) = -881/8.
```

This is CURVATURE-HISTORICAL-TRACE [T], evidenced by
probes/P-CURVATURE-TRACE-VALUE-1. The registered proposal -21/8 is
therefore false for this operator (CURVATURE-TRACE-VALUE [F]); the
separately printed ten-mode historical checksum is -22 and is not
asserted as the spectrum of K_hist.

The historical compression also has an exact intrinsic/exterior split. Put
`P = P_0 R_H`, `Q = I - P`, `A = T_a`, and `C = T_c`, and restrict every
displayed endomorphism to `V`. Then

```
K_amb = P(AC - CA)P = K_hist,
K_int = [PAP,PCP],
K_ext = PAQCP - PCQAP,
K_amb = K_int + K_ext.
```

Two complete exact routes and byte-identical aarch64 and x86_64 executions
give `K_ext = 0` entrywise and hence `K_amb = K_int`. The ambient and
intrinsic operators both have rank 292 and nullity 526; the exterior operator
has rank 0 and nullity 818. Their exact trace split is

```
Tr_V(K_int^2) = -881/8,
Tr_V(K_ext^2) = 0,
2 Tr_V(K_int K_ext) = 0.
```

The leakage maps `QAP|_V` and `QCP|_V` are both nonzero, so the vanishing
exterior term is exact cancellation, not invariance of `V` under `A` and
`C`. This is CURVATURE-HISTORICAL-GAUSS-SPLIT [T], evidenced by
probes/P-CURVATURE-GAUSS-SPLIT-1. It is an algebraic identity for the frozen
historical operator, not a differential-geometric Gauss equation, embedding
theorem, spectrum, or physical interpretation. None of these facts selects a
canonical spatial-curvature operator. CURVATURE-OPERATOR-CANONICAL [O]
asks whether the public architecture determines exactly one equivalence
class after the carrier, measure, projection group, and ambient versus
intrinsic commutator choice are fixed publicly. No golden spectrum or
continuum-curvature reading is asserted.

The decoder is a typed partial interface, not a completed total map.
Let K be the set of forward U-orbits. Let MatterData, GeometryData,
and ObservableHistory denote records whose fields exist only where a
registered claim defines them. Then

```
D_matter : dom(D_matter) subset K -> MatterData
D_geom   : dom(D_geom) subset K x MatterData -> GeometryData
D_clock  : dom(D_clock) subset K x MatterData x GeometryData
           -> ObservableHistory

D(kappa) = D_clock(kappa, m, g),
m = D_matter(kappa),  g = D_geom(kappa, m).
```

Functional order is matter, then geometry, then clock. D_matter reads
only the orbit and the registered quadratic/Born and matter maps;
D_geom reads the orbit plus MatterData and the registered linear,
boundary, wedge, and chain maps; D_clock reads the counter projection
plus the accumulated records and is terminal. None of these outputs
feeds U, so the declared dependency graph is acyclic. Totality,
uniqueness, and completeness of D are not claimed: they remain in
QUADRATIC-ENVELOPE-DECODER [H] and QUADRATIC-DECODER-DATA [O].

The reading split (READING-SPLIT [D], inline) is therefore a public
dictionary at the registered legs, not a completeness theorem: the
linear readout is CODEC-TR4, the binary cut drives the census, and the
quadratic registration is the Born square. The gyron density is rho =
1/6 (GYRON-DENSITY [T], registered in section 13). The self similar
time quantum (TIME-QUANTUM-TOWER [C], reproduce/foundations-places):
on Z/5^k, M_J^(5^k) = i_5 I with i_5^4 = 1 and period exactly
4 x 5^k, computed for k = 1 to 4. No all-k theorem and no generic
exponentiation speedup are claimed.

## 3. The kernel and the census

F_5^6, 15625 checkpoint states; the Klein-100 typology; 313
attractors. The finite kernel is the declared checkpoint architecture
paired with the algebraic verb. No derivation or uniqueness of this
architecture from J or M_J is claimed. Its checkpoint space is Z_5^6
with coordinates (p1, p4, p1p, p4p, q, r) and five involutive
generators, all arithmetic mod 5:

```
a  swap             (p1, p4, p1p, p4p, q, r) -> (p4, p1, p4p, p1p, q, r)
b  time inversion   x -> (-p1p, -p4p, -p1, -p4, -q, -r)
c  transport        piston -> b4(piston) + s_c + r u_c; q -> 1 - q; r -> -r
d  mirror           x -> c_d - x
e  shifted mirror   x -> (c_d + v_e) - x

s_c = (2, 1, 2, 1), u_c = (0, 1, 0, -1), c_d = (2, 1, 3, 4, 1, 1),
v_e = (0, 0, 0, 0, 1, 0);  b4 is the piston part of b.
Relations: a^2 = b^2 = c^2 = d^2 = e^2 = id and (bc)^5 = id.
Drive: theta_n = s_2(n) mod 2 (Thue-Morse); phase z_6(x) = Tr_6(x),
the sum of the six coordinates mod 5; selection law
i_n = z_6(psi_n) + 2 theta_n mod 5, with the autonomous update U
defined in section 2.
```

The census (CENSUS-313 [C], reproduce/census): the full enumeration of
all 15625 seeds, warmup 400 ticks and window 300, yields exactly 313
attractors: 312 of size 20 with basins of 50, and one singlet of size
10 with a basin of 25; the attractor support has 6250 states, the
basins cover all of Z_5^6, and 313 = 13^2 + 12^2. Every recurrent
state lies on the z_6 sheet {1, 4}, so the selection law fires only b,
d, and e on the attractor: the recurrent algebra is the mirror algebra
(CENSUS-Z5-SHEET [C], reproduce/census). The piston pairing Phi =
(b4 d4 on pistons, identity on the fiber) is an involution that
permutes the 313 attractors with cycle type 144 transpositions plus 25
fixed points, the fixed points being 24 attractors of size 20 and the
singlet, so the classes modulo the pairing number 169 = 13^2
(CENSUS-PAIRING [C], reproduce/census). The hosting formula holds on
all 313 (CENSUS-HOSTING [C], reproduce/census): the return group
`H_1 = <d, b e b>` has order 10, d o (b e b) is the line translation
T_0 = (0, 0, 0, 0, 3, 2), and for every attractor A there is a chosen
representative x_A in A such that the exact two-coset formula is
`A = H_1 x_A union b H_1 x_A`. The boundary hyperplane: with Tr_4 the
piston sum and M the z_6 sheet, the boundary class
S_hyp = M cap {Tr_4 = 0} has size 1250 exactly, the charged complement 5000
in two sheets of 2500, the boundary fibers 625 + 625, by full
enumeration of all 15625 states (HYPERPLANE-BOUNDARY-CLASS [T],
reproduce/hyperplane-codec); the census window realizes S_hyp as the
union of the 63 = (p^3 + 1)/2 boundary attractors, 62 of size 20 with
the singlet, and the charged sector as the remaining 250
(HYPERPLANE-BOUNDARY-REALIZATION [C], reproduce/hyperplane-codec).
The unique M_J readout is the trace character: the step matrix is
multiplication by J column by column, its characteristic polynomial
is Phi_5(x - 1) with det(2I - M_J) = 5 = p. For
x = (x_a, x_b, x_c, x_d) in the power basis over Z, the exact
identity is

```
Tr_4(M_J x) = 2 Tr_4(x) - 5 x_c.
```

Therefore Tr_4(M_J x) = 2 Tr_4(x) in F_5, and the scalar multiples of
Tr_4 are the only covectors reading any multiplier at all
(CODEC-TR4 [T], reproduce/hyperplane-codec).

This fixed channel has an exact ramified four-state lift. Put
`lambda = 1 - zeta_5` and `J_lambda = [J] mod lambda`. Reduction sends
`zeta_5` to 1, hence `J_lambda = 2` in `F_5^*`, with orbit
`1, 2, 4, 3` and exact order four. Define

```
Theta_0 = 1,
Theta_(2n) = Theta_n,
Theta_(2n+1) = J_lambda Theta_n.
```

Binary-length induction gives the unique solution

```
Theta_n = J_lambda^s_2(n).
```

For the sign quotient `q : F_5^* -> F_5^*/{+-1} ~= F_2`, with
`q(+-1) = 0` and `q(+-2) = 1`, one has for every `n >= 0`

```
q(Theta_n) = theta_n,
Theta_n^2 = (-1)^theta_n.
```

The four-cycle is the digit-1 transition, not the chronological successor.
If `c_n = nu_2(n+1)`, then the exact successor law is

```
Theta_(n+1) = Theta_n J_lambda^(1-c_n).
```

Moreover, for every `x_0 in Z^4` with `Tr_4(x_0) = 1 mod 5` and every
`k >= 0`, induction on the CODEC-TR4 identity gives

```
[Tr_4(M_J^k x_0)]_5 = J_lambda^k.
```

Thus `k = s_2(n)` realizes `Theta_n` on the one-dimensional fixed
`M_J/Tr_4` readout quotient. The channel selects multiplier 2; the sign
quotient alone is inversion-blind and also sends `3^s_2(n)` to `theta_n`.
Independently, the same integer is the unique universal binary carry weight:

```
x + y = (x XOR y) + 2 (x AND y)        for all x,y in N_0,
```

with uniqueness already forced by `x = y = 1`. The frozen formulas also
imply, for all `x,y in N_0`,

```
s_2(x) + s_2(y) = s_2(x XOR y) + 2 s_2(x AND y),
Theta_x Theta_y = Theta_(x XOR y) omega(x,y),
omega(x,y) := (-1)^theta_(x AND y) in {+-1} subset F_5^*.
```

On the XOR group `(N_0, XOR)`, `omega` is the symmetric normalized
bicharacter induced by the finite-support bit pairing `sum_i x_i y_i mod 2`.
Equivalently, `omega(x,y) = Theta_x Theta_y Theta_(x XOR y)^(-1)`,
so it is the normalized 2-coboundary of `Theta` and hence a 2-cocycle.
In this factorization, `x AND y` is the exact bit-intersection datum from
which the scalar factor set `omega` is read. Together these exact
statements form
RAMIFIED-TM-LIFT [T] at L1, evidenced by
probes/P-RAMIFIED-TM-LIFT-1. The equality of the two integer values is an
arithmetic consonance, not a physical carry or phase identification. No
constant chronological quarter-turn, full-state four-phase identification,
checkpoint factorization, parity on all of `Z_2`, time-arrow reading, or lift
to L2-L6 is claimed.

The checkpoint-only factorization closes negatively on the frozen full
forward carrier

```
C = {U^n(0, psi_0) : n >= 0, psi_0 in F_5^6}.
```

For every initial checkpoint, the five trace laws force `z_6(psi_3) = 1`; the
selectors at steps three, four, and five are therefore all one. The same
involution `b` acts three times, so `b^2 = id` gives `psi_4 = psi_6`, while
the inherited lift has `Theta_4 = 2` and `Theta_6 = 4`. Hence no
single-valued `h : F_5^6 -> F_5^*` factors `Theta_n` through the checkpoint
on `C` (CARRY-J-CHECKPOINT [T] at L1,
probes/P-CARRY-J-CHECKPOINT-1). The theorem decides no restricted carrier,
selector offset, physical carry, phase, time, or gravity reading, decoder
completeness, parity on all of `Z_2`, or lift to L2-L6.

The same ramified digit recursion has an exact two-branch lift through
`C8 -> C4 -> C2`. In `F_25 = F_5[tau]/(tau^2-2)`, put `eta = tau^3`.
Then `eta^2 = phi = 3`, `eta^4 = -1`, `eta` has order eight, and its norm to
`F_5` is the ramified image `J_lambda = 2`; the roots of `r^2 = phi` are
exactly `eta` and `-eta`. On `<eta>`, the norm has kernel `{+-1}` and image
`<J_lambda>`, but no section because both preimages of `J_lambda` have order
eight. For either root `r_epsilon`, define the digit recursion

```
Y_0^epsilon      = 1,
Y_(2n)^epsilon   = Y_n^epsilon,
Y_(2n+1)^epsilon = r_epsilon Y_n^epsilon.
```

Binary-length induction gives its unique solution and successor law:

```
Y_n^epsilon = r_epsilon^s_2(n),
Y_(n+1)^epsilon = Y_n^epsilon r_epsilon^(1-nu_2(n+1)).
```

For both branches and every `n >= 0`, the exact projections are

```
N(Y_n^epsilon)    = Theta_n,
q(N(Y_n^epsilon)) = theta_n,
(Y_n^epsilon)^2   = Theta_n^-1,
(Y_n^epsilon)^4   = (-1)^theta_n,
Y_n^-             = (-1)^theta_n Y_n^+.
```

Thus `Y_n -> Theta_n -> theta_n` is the exact `C8 -> C4 -> C2` tower, and
the chronological multiplier is not constant. These statements form
SQRT-PHI-DIGIT-LIFT [T] at L1, evidenced by
probes/P-SQRT-PHI-DIGIT-1. Neither sign branch is physically selected; no
checkpoint identification, physical tick, time arrow, gravity dynamics,
coupling, SI scale, or lift to L2-L6 is claimed. The typed clock and gravity
bridge remains SQRT-PHI-TIME-GRAVITY [O].

The next carry stratum has an exact pentagonal form in the frozen
four-coordinate Hamming frame. On `V = F_2^4`, put

```
w(x) = popcount(x),
t(x) = w(x) mod 2,
d(x,y) = popcount(x AND y) mod 2,
q(x) = binom(w(x),2) mod 2.
```

Then `q` is the second binary weight bit and its polarization is
`B(x,y) = t(x)t(y) + d(x,y)`. The form `B` is alternating and
nondegenerate, `Arf(q) = 1`, and the five nonzero singular vectors are
`P = {1,2,4,8,15}`; distinct members pair to one and their XOR is zero.
Consequently

```
O(q) = O^-(4,2) ~= S_5,       Sp(4,2) ~= S_6,
```

with `O(q)` the stabilizer of the selected minus-type refinement. The raw
intersection form `d` has stabilizer `S_4 x C_2` of order 48 and therefore
has no element of order five. The five-fold symmetry belongs to `q`, not to
`d` alone. With order five fixed, dimension four is the least binary linear
width admitting it, because `ord_5(2) = 4`.

The integral bridge is the augmentation root lattice
`A4 = {(z_0,...,z_4) in Z^5 : sum z_r = 0}` with the coordinate five-cycle
`C`. Under `a_i = e_i-e_0 -> zeta_5^i-1`, `A4` is the ideal
`(zeta_5-1)Z[zeta_5]`; `I+C^2` is integrally conjugate to the public `M_J`,
and for every `a in (Z/5Z)^*`,

```
char(I+C^a) = Phi_5(X-1),
g_a(I+C)g_a^-1 = I+C^a.
```

Thus the unfixed integral-isometry class does not select an exponent,
cycle, or orientation. The ramified quotient `A4/(C-I)A4` has order five,
and every `I+C^a` acts on it as multiplication by 2; its characteristic
shadow is `(X-2)^4 mod 5`. Modulo two, the even-lattice refinement is
`q_A(x)=q(x)+B(15,x)`, and the transvection
`tau_15(x)=x+B(x,15)15` is the explicit isometry from `(A4/2A4,q_A)` to
`(V,q)`. Weyl reduction gives `W(A4) ~= S_5 -> O(q_A)`, and the five
nonzero singular classes map to the five powers of `zeta_5`, whose sum is
zero. These statements form CARRY-PENTAD [T] at L1, evidenced by
`probes/P-CARRY-PENTAD-1`. The theorem is relative to the frozen frame and
fixed order-five target. It does not unconditionally select `p=5`, width
four, a five-cycle, its orientation or exponent, and it adds no decoder,
physical gauge, phase, force, spacetime, entropy, measure, or lift to L2-L6.

No coding rate is inferred
from this dimension count. The inherited phrase "rate 4/5" is retired
from Public Canon v12; any future coding claim must define its alphabet,
message space, encoder, decoder, error criterion, and rate from scratch.

Five completed public probes now delimit the entropy bridge without closing
it. Write

```
F_eps(psi) = g_{z_6(psi) + 2 eps mod 5}(psi).
```

The literal integer lift of the finite generator presentation does not
satisfy `(bc)^5 = 1`: over Z its fifth iterate is

```
(bc)^5(x) = x + (10, 5 - 5r, 10, 5 + 5r, 5, 0).
```

Thus the relation holds in the mod-5 shadow, not in that literal lift
(ENTROPY-LIFT-DEFECT [F], probes/P-ENTROPY-BRIDGE-1). On the declared
finite carrier, the same probe establishes the window-scoped joint law:
component masses equal basin sizes from tick 512, the checkpoint marginal
is exactly uniform on the 6250 recurrent states on the frozen window, and
the letter and pair masses are exactly `(2/3, 1/6, 1/6)` and `1/6`
(ENTROPY-JOINT-CESARO-LAW [C]).

No exact bridge cut depending on a finite driver window of length at most
16 exists at any lambda-depth. The pure-word constraint system has zero
solutions for every such window, and the J-invariant zero residue embeds
that obstruction at every depth (ENTROPY-CYLINDER-CUT [F],
probes/P-ENTROPY-BRIDGE-2). At the tested dyadic scales `k = 0..10`, both
renormalized block maps are exactly two-to-one on the recurrent core, one
unresolved bit per scale (ENTROPY-BLOCK-HALVING [C]).

The two branch images partition the core into halves of 3125 states, and
all four restrictions between source and target halves are bijections.
Every size-20 attractor splits `(10, 10)`, the singlet splits `(5, 5)`,
and there are `312 x 10 + 5 = 3125 = 5^5` living trajectories
(ENTROPY-LIVING-SET [C], probes/P-ENTROPY-BRIDGE-3). At the frozen anchors
through depth 12 every word-prefix composition has image 3125 with every
fiber exactly two; the backward tree is a width-two caterpillar with one
death per level, so backward indeterminacy does not accumulate in the
declared living construction (ENTROPY-UNIQUE-PAST [C]). Finally,

```
ord(J mod lambda^i) = (4, 20, 20, 20, 20, 20, 100, 100),  i = 1..8,
Spec(J on O/lambda^5) = {1: 1, 4: 1, 20: 156},
3125 = 5^5 = |O/lambda^5|.
```

This is ENTROPY-COUNT-MATCH [C]: the depth-five lambda carrier has exactly
the living-set cardinality. Cardinality is not a construction of the cut.

The fourth probe resolves a further finite quotient of that living carrier.
On every recurrent component and half, the level-`k` vertex groups for
`k = 1..10` are cyclic of order five with one constant partition into
five-cells: two cells per size-20 component half and one per singlet half,
for `625 = 5^4` cells per full living half. Both one-tick branch maps carry
cells to cells, and the induced vertex holonomy on the cell quotient is
trivial for `k = 1..8` (ENTROPY-PENTAGON-QUOTIENT [C],
probes/P-ENTROPY-BRIDGE-4).

In the preregistered coherent level-2 gauge, every level-`k` cell map for
`k = 0..10` is affine over `F_5`; all 313 components have the same frozen
`(a,b)` spectra, with period four for `k = 1..10`
(ENTROPY-AFFINE-COCYCLE [C]). This is gauge-specific and does not identify
the multipliers gauge-independently with the lambda-digit action. The same
probe finds zero component-local cylinder solutions in exactly the 900
frozen cases: the singlet and canonical size-20 component for `L = 4..16`,
three cursor positions and eleven stated clocks, plus the singlet at clock
four for `L = 17..30` at the same cursors (ENTROPY-COMPONENT-NOGO [C]).
This finite enumeration does not quantify over every component, clock, or
window. None of these computations kills the depth-five selection problem,
proves an all-scale or ergodic statement, or supplies regularity, canonicity,
or measure transport; ENTROPY-LAYER-BRIDGE [O] remains open.

The fifth probe resolves the finite mirror law on the same living carrier.
Each branch letter restricted to its own living half is an involution with
cycle type `{1: 1, 2: 1562}` and a unique fixed state in the singlet
component. The cross restrictions are mutually inverse in the exact
directions `F_1 o F_0 = id` on `H_1` and `F_0 o F_1 = id` on `H_0`. On
canonical pentagon cells, each letter fixes the singlet cell and swaps the
two cells of every size-20 component-half. In the frozen coherent level-2
gauge, every one-tick cell map is a reflection with multiplier `4 = -1`;
the two ordered letter pairs are `((4,0),(4,2))` and
`((4,2),(4,0))`, each on exactly 625 source cells
(ENTROPY-MIRROR-LAW [C], probes/P-ENTROPY-MIRROR-1). This is a finite,
gauge-specific statement. It supplies no all-scale or measurable mirror
theorem, gauge-independent normal, equivariant selection family, measure
transport, or L2 lift.

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
this refines the commutator reading of space. Connectivity of
`{a, c, d, e}` on every coupled power `(F_5^6)^k`, `k >= 2`, is exact
(KERNEL-CONNECT-ALL-K [T], probes/P-KERNEL-CONNECT-ALL-K-1). Let
`Gamma = <M_a, M_c, M_d, M_e>` and let `U` be the smallest
`Gamma`-invariant subspace of `F_5^6` containing the translations
`{v_c, v_d, v_e}`. Exact closure gives `dim U = 6`. For every affine
letter `h in {c, d, e}`, the frozen commutator identity is
`D_h R_(i-1)^4 D_h R_(i-1) = t_(delta_i tensor v_h)`; conjugation gives
`D_g t_(delta_i tensor u) D_g^(-1) =
t_(delta_i tensor M_g u)`. Thus the extracted cell factors close to all
of `U`, and the two-way ring transvections transport them to every cell,
so the translation subgroup is all of `(F_5^6)^k` for every `k >= 2`.
The lower bound is sharp: at `k = 1` the same four letters have nine
components. This is an L1 state theorem for the declared coupled carrier;
it supplies no continuum, measure, or physical lift.

## 4. The two places

The exact arithmetic uses two places, disjoint over Q:
Q(zeta_5) cap Q(zeta_8) = Q. Their physical assignment is the
TWO-PLACE-PHYSICS dictionary [D]:

```
v_5 WRITES: home Q(zeta_5), real floor Q(sqrt5), state F_5^6; geometry,
    gravity, the native pentit substrate, the native magic C_5 (order 5,
    prime 5).
v_2 READS the quadratic mode: home Q(zeta_8), real floor Q(sqrt2), with i
    and the foreign qubit magic m_8 = zeta_8 (order 8, prime 2); Clifford,
    Born, the outside read.
They meet only over Q. The dictionary reads the layer boundary as the
field boundary; it does not prove that this reading is unique.
```

The exact field facts are DEGREES-BY-PRIME [T]
(reproduce/foundations-places): sqrt5 lives at zeta_5 by
(2 phi - 1)^2 = 5, while sqrt2 and i live at zeta_8 by
(m_8 + m_8^-1)^2 = 2 and m_8^2 = i, and neither sqrt2 nor i lies in
Q(sqrt5), the unique quadratic subfield of Q(zeta_5). The linear,
quadratic, cubic, and foreign-magic assignments are readings of these
facts under TWO-PLACE-PHYSICS [D]. The Z2
symmetries split arithmetically (Z2-PLACES-SPLIT [T],
reproduce/foundations-places): there is one involution at zeta_5, the
single order 2 element of its cyclic Galois group, and a complete
Klein four at zeta_8, where every nontrivial element is an involution;
5 = (2 + i)(2 - i) in Z[i], with conjugation swapping the factors.
TWO-PLACE-PHYSICS [D] separately reads CP from the zeta_5/Gaussian
conjugation and T from the Thue-Morse reversal, hence CPT as their
composition; this is a dictionary, not a theorem identifying the
physical CPT operator. The same dictionary assigns forces to sqrt5,
spin to sqrt2, and charge conjugation to i. i is bilocated
(I-BILOCATED [D], reproduce/foundations-places): the order 4 element
of F_5* at v_5 and zeta_8^2 at v_2, identified only over Q, never
merged. TWO-PLACE-PHYSICS also declares the Born square as the descent
reading for cross-place transfers; its values are carried by the Born
rows, and no completeness claim is made. The silver ring facts
(SILVER-RING-FACTS [C],
reproduce/foundations-places): inside F_25 = F_5(sqrt 2), where the
step collapses to the doubling J = 2, tau = sqrt(J) has tau^4 = -1
with ord(tau) = 8, and F_25* is cyclic of order 24; norm, orders,
cyclicity, and census are finite computations. The silver sibling
(SILVER-SIBLING [D], reproduce/foundations-places) is the dictionary
reading resting on those facts: m_8 = zeta_8 = sqrt(i) at prime 2 with
the silver unit 1 + sqrt2 of norm -1 mirrors tau = sqrt(J) at prime 5;
sqrt(i) is the square root of the axiom read at the foreign place.

The golden and silver numbers are the positive roots of the two simplest
metallic laws `x^2 = t x + 1`, at `t = 1` and `t = 2`
(METAL-TRACE-CASCADE [T], `probes/P-METAL-TRACE-1`). Both are units of
norm `-1`. The discriminant `t^2+4` gives the fundamental discriminants
5 and 8, so the ramified prime of each law divides its own discriminant.
Their powers obey their native integer recurrences:

```
phi^n   = F_n phi + F_(n-1),
delta^n = P_n delta + P_(n-1),
```

where `F` is Fibonacci and `P_(n+1)=2P_n+P_(n-1)` is Pell. At the silver
place, `1+m_8^2 = 1+i = sqrt2 m_8 = sqrt(2i)`, so `(1+i)^2=2i`, while
its absolute field norm in `Q(zeta_8)` is 4; it is not a unit. At the
golden place `N(J)=1`.
The claim is scoped to `t in {1,2}`: trace does not select a number field
for general `t` because `t=4` also has squarefree discriminant kernel 5.
No run/record, time-arrow, force, or other physical reading is included in
this theorem.

## 5. The force is the curvature

The finite Weyl commutator is exact on all five basis states
(FORCE-WEYL-HOLONOMY [T], reproduce/force-born-dictionary):

```
Z X Z^-1 X^-1 = j I;   j has exact order 5 and arg j = 2 pi / 5.
```

FORCE-AS-CURVATURE [D] reads this holonomy as a force curvature and,
through AXIOM-PROJECTION-DICTIONARY [D], reads the two J projections
as the two abelian force channels. This physical assignment is not
part of FORCE-WEYL-HOLONOMY [T] and no uniqueness of the force
dictionary is claimed.

The gravity dictionary currently places three labeled ingredients
side by side: the cell action 864 pi at k = d(d + 1) = 12, the
quadrupole-power comparison against the Hulse-Taylor binary pulsar
(99.83 +/- 0.16 percent [measured comparison], source
SRC-PSR-B1913), and the declared kernel
coefficient A_GD = 1/(8 pi) with lambda = 216 pi. Their conjunction is
a GRAVITY-BRIDGE-LAW reading [D], not an additional theorem and not a
public value of G. Its exact displayed identity is:

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

The exact chain rows and the classical dictionary are separate. The
chain layer is at T and MAXWELL-CLOSED is its D reading
(reproduce/maxwell): the Bianchi identity
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
on the 12 electric faces from the bare tick. At public v1 scope, the
magnetic axiom pair is an explicit input to the dictionary; no
uniqueness or selection theorem is claimed. Given that input, stay or
twist once reads

```
Psi(k) = 1 + zeta^k,   mu(k) = |Psi(k)|^2 / 10 = w(k)/10
       = (2/5, (3+sqrt5)/20, (3-sqrt5)/20, (3-sqrt5)/20, (3+sqrt5)/20)
```

entrywise exact in Q(sqrt5) (BORN-FACE-WEIGHTS [T],
reproduce/born-faces); the slot 4 pair lands on the sigma_2 Galois
image exactly; the tilt magnitude is exactly sqrt5/5, with sign set by
the Thue-Morse slot orientation; the Legendre symbol (2|5) = -1 is
realized on this face.

Coupling seeds: the declared decomposition has exact Gram weights 1/p
on the trace and conformal directions and 1 on the spatial base, with
3/4 = d/(d + 1) (MEASURE-SPATIAL-ONLY [T]). STRONG-SEED [D] reads
these weights as coupling roots on the spatial gauge sector:
alpha* = 1/p and the strong root is 1 x 3/4 x 1 = 3/4; the seed
ratio EM to strong is 15 : 4. Dark
energy w = -14/15. Running and scheme are frontier rows
(ALPHA-S-RUNNING, SCHEME-DICTIONARY).

## 6. Alpha and the observable register

```
alpha = 5 S / ((8 pi)^2 sqrt(s)),   sqrt(s) = (3 - phi)^(1/4),
S = (1 + X/5)^-5,   X = 1 / (32 pi^2 phi^4)
alpha^-1 = 137.035999190;  CODATA 2022: 137.035999177(21)
                                            source SRC-CODATA-2022-ALPHA
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
mu_mu  = 2688/13 - (89/5) alpha^2     (-0.023 sigma)      [measured comparison]
         source SRC-CODATA-2018-MUON
mu_tau = 3477 + 240 (89/5) alpha^2    (-0.011 sigma)      [measured comparison]
         source SRC-CODATA-2018-TAU
exchange identity: delta mu_tau + 240 delta mu_mu = 0     [T, exact in Q]
         (MU-EXCHANGE-IDENTITY)
mu_p   = 6 pi^5 (1 + alpha^2 / 3)     the single bare pi^5, an odd carrier
mu_n   = mu_p + deg_v / chi - Delta_EM;  a numerical comparison is not
         retained until deg_v / chi and Delta_EM are public;
         Delta_EM stays open (NEUTRON-DELTA-EM)
the electron at the Dirac step:  det = 1 + m_D^2 = 5 = p
```

The parity law (PARITY-LAW) [T] lives in a formal observable register,
not under ordinary complex conjugation. Let

```text
R = A[pi, pi^-1],
iota_pi(pi) = -pi,
iota_pi(a) = a  for every a in A,
```

where `A` contains the pi-free coefficients and the other named formal
generators. Multiplicative extension makes `iota_pi` an involutive
algebra automorphism, and a monomial `c pi^k u`, with `u` in `A`, has
eigenvalue `(-1)^k`. This is a formal grading operation; it is not
complex conjugation on the complex numbers, which fixes the real number
pi. At this public scope, thirteen named entries are even and delta
free: alpha^-1, sin^2 theta_W, w = -14/15, L, Omega_b = pi^2/200, the
slip X, mu_mu, mu_tau, G, PMNS, the dark matter ratio, the zeta_K
residue, and the neutrino register 341/10. Three odd delta carriers sit
at degrees pi^1, pi^3, and pi^5: the capacity 2 pi/phi^2, the Kahler
capacity 64 pi^3 phi^2, and the proton 6 pi^5. The neutron is the unique
mixed composite among these named forms. No larger parity census is
claimed.

The bridge defect delta = 6 phi^2 - 5 pi = (9 + 3 sqrt5) - 5 pi is
nonzero by Lindemann-Weierstrass (about +2.4 x 10^-4, a labeled gap
witness) (BRIDGE-DEFECT). The exact bridges are xi phi^2 = 5 = p,
script-Q phi^2 = 2 pi, and script-Q / xi = 2 pi/5 = arg J. The PMNS
sector waits on the mass mechanism frontier.

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
algebra. Probability and measurement language belongs to the
MEASURE-BORN-VERB dictionary [D], not to any of the four theorem rows.

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
reproduce/force-born-dictionary) is the exact matrix statement:
C_+ = I + S and C_- = C_+^T obey
C_+ C_+^T = circ(2, 1, 0, 0, 1) with spectrum w; the position and
Fourier bases have squared overlap 1/5 on all 25 pairs; the Plancherel
masses are 2 and 10, in the ratio p = 5. Reading C_+ and C_- as two
abelian faces is part of KERNEL-CELL-DICTIONARY [D].

## 9. The photon and the electron

The quantum is an integer path count, one bit per tick, on an RP
Hilbert space. The photon window has exact coordinates
(PHOTON-WINDOW-COORDINATES [T], reproduce/photon-electron): the point
w = (4, phi^2, phi^-2, phi^-2, phi^2) and its Kramers-Wannier dual
w_hat = 5 (2, 1, 0, 0, 1) with w_check = w exactly, w not self dual, and
the tilt w(1) - w(2) = sqrt5. The quantum costs one bit per tick on
every center, w_hat(1)/w_hat(0) = 1/2, and every class |k| >= 2 is
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
initial datum [z_6(B_0) = 4]. Seven exhaustive public laws carry it
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
G4  D_J(m_D) = S (I + i m_D X), zero free parameters: streaming is the
    counter, the coin modulus is the rest rung, the phase i is the
    plenum ellipticity; massless is the one sided shift; det = 1 + m_D^2
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
-I for the photon. No eta identity is inferred from this tower; the
inherited naming clause is not part of Public Canon v12. The fermionizer
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

In F_25 = F_5[tau]/(tau^2 - 2), the ramified images are J = 2 and
phi = 3; tau^4 = -1, tau^6 = phi, and therefore
sqrt(phi) = tau^3 (PENTIT-ROOT-FACTS [T],
reproduce/pentit-p5-closure). Calling tau the square root of the axiom,
sqrt(J) = tau, is the gate-line dictionary
(PENTIT-ROOT-READING [D]); it does not identify the argument with the
clock. The exact magic-prime gate is the complete norm ladder
N(tau^k) = 3^k = 2^-k in F_5*, the order-four source i_5 = 2 reaching
-1 after two steps, and the reciprocity
sqrt(J) sqrt(phi) = tau^4 = -1 with phi = J^-1
(MAGIC-PRIME-GATE [T], reproduce/pentit-p5-closure).

Define V_+ as the sign quotient F_5*/{+-1}; its two classes are
{1, 4} and {2, 3}, so V_+ is cyclic of order two
(QUBIT-FROM-F5 [T], reproduce/pentit-p5-closure). The native magic is
the cubic C_5 (order 5, prime 5), while the foreign read uses m_8 of
order 8 at prime 2. For n in {5, 8}, define

```
E_n(a,b) = Re(zeta_n^(a-b)),
S_n = abs(E_n(a0,b0) + E_n(a0,b1)
          + E_n(a1,b0) - E_n(a1,b1)),
M_n = max S_n over (Z/nZ)^4.
```

Complete exact enumeration, independently certified after quotienting by
the common phase shift, gives

```
M_5 = 1/2 + sqrt(5),
M_8 = 2 sqrt(2),
2 < M_5 < M_8.
```

This is BELL-MAGIC-BOUNDARY [T] at the stated finite-functional scope,
evidenced by probes/P-BELL-MAGIC-BOUNDARY-1. It is not an unrestricted
Bell cap, a theorem about local-variable models, a continuous quantum optimum,
or a Tsirelson claim. The legacy modulus bound involving phi is a
different observable.
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

The theorem layer in this section is finite group, representation,
and invariant theory. COLOR-LADDER-DICTIONARY [D] reads its D5 to 2I
to E8 ladder as the nonabelian color door and reads color su(3) on the
traceless endomorphisms of the three dimensional trace kernel. The
dictionary rests on the exact rungs below; it proves neither a unique
color assignment nor QCD running, confinement, or the measure lift
from the core to the full SL_3(F_5) carrier.

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

The corresponding marked-pair uniqueness proposal has now been decided.
Under the pinned cover SL_2(F_5) -> PSL_2(F_5), the full A1 to A7
admissibility predicate, and simultaneous conjugacy by SL_2(F_5), exact
enumeration gives 240 admissible triples in four inequivalent classes of
size 60. Central retwist pairs classes 1 with 2 and 3 with 4, and no such
pair is conjugate. Thus the dicyclic witness exists but is not forced:
SPIN-LIFT-FORCED [F], evidenced by probes/P-SPIN-LIFT-FORCED-1. A
coarser quotient identifying retwists or base relabelings is a different
question.

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
864 pi carrying exactly one fiber 2 pi. The public theorem stops at
the displayed lapse, Hamiltonian, and fiber identities; it makes no
claim here about a unique source projector, the amplitude ansatz
rho = rho_0 ell^2, or E_total = 0. The ell-G wall is a mechanism wall:
ell_P / lambda_e = (32/33) alpha^10 / sqrt(g), with the exponent
identity G_T = alpha^(20 + sigma) (GRAVITY-BRIDGE-LAW).

Cosmology (reproduce/cosmology-register): the exact deformation
J -> J e^(i eps) freezes J Jbar at linear order
(TT-LINEAR-ZERO [T]). COSMOLOGY-READING-DICTIONARY [D] reads that
identity as zero linear tensor response about the declared isotropic
background and hence as r_T = 0 at that dictionary layer; it also reads
the gyron density as the mass-ladder prefactor and the registered
forms below as cosmological observables. It is not a uniqueness or
full perturbation theorem. The tilt n_s - 1 = -p alpha = -5 alpha is
at H (NS-TILT, falsifier live at CMB-S4); the bilinear TT decoder
permits induced tensor power at quadratic field order
(TT-QUADRATIC-INDUCED) [D]; a numerical r_T(k) waits on the vector state
normalization (TT-VECTOR-STATE-NORMALIZATION). Dark
energy w = -14/15; Omega_b = pi^2 / 200; Omega_DM / Omega_b =
18 p^3 ln^2(phi) / pi^4, and the dark matter ratio 5 : 1 follows from
Thue-Morse pair statistics (COSMOLOGY-REGISTER at D, the committed
forms with fenced comparisons); the gyron density rho = 1/6
(GYRON-DENSITY) [T]: the named Thue-Morse pair
(0, 0) has exact stationary density rho = 1/6. Its proton
and cosmology assignments belong to COSMOLOGY-READING-DICTIONARY [D].
Independently, freeze the six golden projective lines with representatives

```
v1 = (0,1,phi),       v2 = (0,1,-phi),
v3 = (1,phi,0),       v4 = (1,-phi,0),
v5 = (phi,0,1),       v6 = (phi,0,-1).
```

Put `K = Q(phi)`, `r = phi + 2`, `Pi = vi vi^T/r`, and give the six lines
equal cardinal weight. On `Sym2(K^3)` define

```
M(A)  = (1/6) sum_i Tr(Pi A) Pi,
P1(A) = Tr(A) I3/3,
P5(A) = A - P1(A).
```

The rank-one projectors sum to `2 I3` and their centered projectors form a
rank-five regular simplex. The direct sum defining `M` is Galois-stable and
descends to a rational endomorphism of `Sym2(Q^3)`. The complete exact
commutant of the rational `so(3)` action is spanned by `P1` and `P5`, and

```
M = (1/3) P1 + (2/15) P5.
```

Thus its scalar-to-per-channel coefficient ratio is `5:2`, its
scalar-to-total-traceless trace-mass ratio is `1:2`, and
`M != (1/6) I6`. For the negative control put

```
c1 = (1,1,1),     c2 = (1,1,-1),
c3 = (1,-1,1),    c4 = (-1,1,1),
Qi = ci ci^T/3,
M_cube(A) = (1/4) sum_i Tr(Qi A) Qi.
```

Then `(1/4) sum_i Qi = I3/3`, but `M_cube` is not in the rational `so(3)`
commutant. Thus second-order isotropy alone does not imply the Sym2
centrality (GOLDEN-SIX-LINE-SYM2-FRAME [T] at L1,
probes/P-TM-SYM2-FRAME-1). The six lines and their equal weights are frozen
inputs, not a selection from J, U, a checkpoint, or a Thue-Morse orbit. The
coefficient `1/6` in `M` is only the cardinal average over six lines; it is
not GYRON-DENSITY, a clock density, or a Born multiplier. This theorem
supplies no Thue-Morse measure, Born halving, physical probability, L5
stream, or L6 measure lift; TM-SYM2-MEASURE [H] remains live.
The conformal mode prefactor K_chi5 =
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
(TT-SQUARING-DECODER) [D; reproduce/coupling-metrology]. Writing
`v = v_1 + i v_2` and `h = h_+ + i h_x`, the same square gives
`h_+ = v_1^2 - v_2^2` and `h_x = 2 v_1 v_2`. For the exact input-frame
rotation `v_1' = a v_1 - b v_2`, `v_2' = b v_1 + a v_2`, with
`a^2 + b^2 = 1`, the pair transforms by

```
((a^2-b^2, -2ab), (2ab, a^2-b^2)),
```

the doubled-angle spin-2 law; conjugation fixes `h_+` and negates `h_x`.
The two coordinates are read as plus and cross (POL-READ [D]). This readout
introduces no independent propagation law, source map, detector convention,
action or state normalization, helicity selection, or numerical tensor
ratio. The inherited WKB3 ringdown grade has no public source or reproducing
test and is
therefore not a Canon claim. Stage A, the Schwarzschild TT endpoint: the
Regge-Wheeler coefficients (1, 0, -3) are forced at scope, V_2 =
f (L/r^2 - 6M/r^3) (SCHWARZSCHILD-TT-ENDPOINT) [T at the displayed
family scope]; no wider uniqueness theorem is claimed. Stage B uses
the explicit dictionary inputs mu = 1 and Z_L2 = 1/2
(TT-QUADRATIC-GERM [D]); neither the action germ, a Gaussian-state
boundary, nor a Stage B pullback is derived by that bookkeeping
identity. No numerical mu corridor is retained without a public
shadow-to-mu inference rule. The emission map and the quasinormal mu decision
after such a rule remain open (TT-SOURCE, QNM-LEAVER-MU).

## 15. Couplings, instruments, and metrology

The density against the Gram form is rho_psi = psi psi^dagger G /
(psi^dagger G psi), with trace exactly one, and the Born value is the
branch G norm (COUPLINGS-DETERMINE [T at this finite identity scope],
reproduce/coupling-metrology). No instrument-uniqueness theorem or
gyron-carrier no-go is asserted by this identity.
The covariant canonical form: the dressing coefficient is the DeWitt
norm, 12 = d(d + 1) at lambda = -1, and the level 1 to level 2
normalization inheritance is closed, the chain of twelves exact
(DEWITT-TWELVES) [T at scope]. No public metrological-admissibility
theorem is asserted; `METRO-ADMISSIBILITY` [O] asks first for a precise
criterion on the named protocol classes and then for its public
decision. The tick clause alone is closed dimensionless: delta tau hat = 1/5 cycle =
2 pi/5 per tick (METRO-TICK) [T at scope]; the remainder is the canonical selector on the
commutator phi ladder and the SI clause (METRO-EDGE-SCALE). The
dressing insertion bookkeeping carries the exact witness 72 alpha^4
(about 0.204 ppm, labeled) with the form decision gated on the integer
crossing count (DRESS-CROSSCOUNT). No end-to-end Lorentz closure is
asserted; the former compound A2/A3/K6 row is retired until its
operators can be registered as separate gates. `QUADRATIC-DECODER-DATA`
[O] asks for a
publicly typed action on data; no unregistered closure of state-update,
Gram, dagger, or data-effect clauses is asserted.

## 16. p = 5 and the wall

The retained public root selector is exact: for a positive prime p,
(p - 2)/(p + 1) = 1/2 if and only if p = 5
(P5-ROOT-SELECTION [T], reproduce/pentit-p5-closure), since clearing
the positive denominator gives p - 5 = 0. No further coincidences are
claimed as independent support for selecting p = 5. The two
logarithmic axes: pi on
the argument (c odd), ln phi on the modulus (c even,
transcendental by Baker); linearly independent over the algebraic
numbers (LOG-AXES-INDEPENDENCE [T]). No algebraic independence claim
is made.

The pentagon root-filter normalization is exact
(PENTAGON-NORMALIZATION [T], probes/P-PENTAGON-WEIL-1). Let
`j = zeta_5 = (J - 1)^3` and, for `Re(s) > 1`, put

```
c(n)   = sum_(a=1)^4 j^(a n) = 5[5 divides n] - 1,
P_0(s) = sum_(n>=1) c(n)n^(-s),
f_5(s) = 5^(1-s) - 1.
```

Absolute expansion of the four polylogarithms gives
`P_0(s) = f_5(s) zeta(s)`. With the classical meromorphic continuation of
`zeta` and its standard completion explicitly imported, define

```
Z_J(s)  = MerCont_(Re(s)>1)(P_0(s)/f_5(s)) = zeta(s),
xi_J(s) = (1/2)s(s-1)pi^(-s/2)Gamma(s/2)Z_J(s) = xi(s).
```

The zeros `s_k = 1 - 2 pi i k/log 5`, `k in Z`, of `f_5` are root-filter
artifacts removed by the normalization; the pole and trivial zeros are
handled by the imported standard zeta completion. In natural series order,
`P_0(1) = -log 5`. On `Re(s) > 1`,

```
coeff(-P_0'/P_0)(n)
  = Lambda(n) - (log 5)n[n = 5^m],
```

so the artificial `5^m log 5` tower is subtracted, not read as prime data.
The unnormalized standard completion is `Xi_raw(s) = f_5(s)xi(s)` and does
not have a constant unit-modulus root number: exactly
`f_5(2)/f_5(-1) = -1/30`.

This is a normalization identity. Meromorphic continuation, the zeta
functional equation and divisor, the standard `xi` completion, the Euler
product, and the treatment of the pole and trivial zeros are named classical
imports, not results of the verifier. No Weil test space, positive form,
operator realization, or statement about RH follows.

The standard finite-dimensional toral Haar-Koopman carrier cannot realize
the full Li norm ladder (J-LI-TORAL-HAAR-NOGO [T],
probes/P-J-LI-TORAL-HAAR-1). For every `d >= 1` and every
`A in GL_d(Z)` with no root-of-unity eigenvalue, let
`U_A f = f o T_A` on `L^2(T^d, Haar)`. There is no vector `v` such that

```
|| sum_(k=0)^(n-1) U_A^k v ||^2 = lambda_n
```

for every `n >= 1`, where `lambda_n` is the standard Li sequence.

The proof is by contradiction. An exact realization makes every
`lambda_n` nonnegative, so Li's criterion forces RH inside the argument.
On that forced branch, for each positive ordinate `gamma` of a nontrivial
zero, with multiplicity `m_gamma`, put

```
theta_gamma = 2 arctan(1/(2 gamma)),
sigma_xi = sum_(gamma>0) m_gamma/(gamma^2 + 1/4)
           (delta_(exp(i theta_gamma)) + delta_(exp(-i theta_gamma))).
```

The standard Li zero-sum formula, second differences, and Fourier uniqueness
then force only the symmetrized vector spectral measure
`mu_v + iota_* mu_v`, with `iota(z) = conjugate(z)`, to equal the purely
atomic `sigma_xi`. The toral character law
`U_A e_m = e_(A^T m)` has no finite nonzero orbit under the carrier
hypothesis: a repeat would make an eigenvalue of `A` a root of unity. Every
nonconstant orbit is therefore a bilateral-shift sector, whose vector
measures have no atoms. This contradicts the atoms of `sigma_xi` away from
`1`.

The contradiction is unconditional for the assumed realization. RH is a
forced intermediate consequence, not an assumption or conclusion. The
standard Li coefficients and zero-sum normalization, Li's criterion in both
directions, convergence of the fixed-`n` zero sum under RH, Fourier
uniqueness, the unitary spectral theorem including its atom/eigenspace
correspondence, and the toral character/bilateral-shift decomposition are
named classical imports.
The proof is all-`n`; finite fits are not excluded.

For the named TWIST-J specialization, `d = 4` and `A = M_J`; its exact
characteristic data and eigenvalue moduli `phi, phi, phi^-1, phi^-1` place it
in the root-of-unity-free class. Gauss's lemma and the standard cyclotomic
minimal-polynomial facts used by the probe's alternative exact exclusion
audit are named imports. The Riemann-von Mangoldt law and Stieltjes partial
summation belong only to the probe's conditional accumulation audit; that
asymptotic is not promoted here. This does not exclude matrices with
root-of-unity eigenvalues, non-Haar, non-Koopman, infinite-dimensional,
boundary, scattering, or enlarged carriers. No replacement realization,
moment or cocycle bridge, Weil-positive form, decoder, physical lift, or RH
result is asserted. The unsymmetrized `mu_v` is not claimed unique. The
conditional spectral target is a proof step, not a separately registered
claim.
This carrier exclusion does not alter or falsify the public algebraic and
finite-periodic statements about `M_J`.


These three verdicts delimit three declared carrier classes. They do not
complete the plenum's single-unitary map, because the compact-boundary
cocycle-vector route remains open.

- E8 functional-calculus carrier. Here `det_1` is the ordinary trace-class
  Fredholm determinant `product_j (1 - t^2 a_j)`, with no exponential
  regularization. If
  `det_1(I - t^2 A) = Xi(t)/Xi(0)` for positive trace-class
  `A = f(Delta_E8)`, equality of zero multisets forces the nonzero spectrum
  `gamma^-2` with zeta-zero multiplicities. The weakened explicit
  Riemann-von Mangoldt bound gives `N(200) >= 68` and multiplicity at most
  18 for each ordinate up to 200, hence at least four distinct
  small-multiplicity eigenvalues. But `Theta_E8 = E4` makes every nonzero
  E8 shell have size `240 sigma_3(n) >= 240`; only the one-dimensional zero
  shell can supply a smaller multiplicity. Therefore no operator in the
  frozen functional-calculus class realizes the determinant
  (J-LI-E8-SHELL-MULTIPLICITY-NOGO [T],
  probes/P-MCKAY-THETA-CARRIER-1).
  MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER [F] records exactly that fired
  route. Non-shell-constant operators and the use of the theta identity as a
  positivity source are not excluded.

- lambda-adic boundary Koopman, Hilbert-Schmidt subroute. For any unit `u`
  and any `n >= 1` with `u^n != 1`, multiplication by `u` leaves every
  additive character above the finite level `v_lambda(u^n - 1)` non-fixed.
  Thus `I - U_u^n` has infinite Hilbert-Schmidt norm. For
  `J = 1 + zeta_5^2`, the complex embedding
  `zeta_5 = exp(2 pi i/5)` gives `|J| = phi^-1 != 1`; hence `J` is not a
  root of unity and the divergence holds for every `n >= 1`. The spectrum
  is pure point on roots of unity with unbounded multiplicity, and its frozen
  order tower is `4, 20, 20, 20, 20, 20, 100, 100`, independently
  re-derived in the Eisenstein model
  `x^4 - 5x^3 + 10x^2 - 10x + 5` of discriminant 125
  (J-LI-LAMBDA-HAAR-HS-NOGO [T],
  probes/P-R2-LAMBDA-HAAR-1).
  LAMBDA-BOUNDARY-HS-KOOPMAN [F] closes only the
  Hilbert-Schmidt-perturbation and S2 forms. It does not close the
  cocycle-vector form LAMBDA-COCYCLE-ANGLES [H].

- lambda-adic scaling shift. The value group of `K_lambda^*` is `Z`.
  The unitary `U f(x) = 5^(-1/2) f(lambda x)` maps the valuation shell
  `S_n` to `S_(n-1)` and is a bilateral shift of infinite multiplicity
  and homogeneous Lebesgue type. Therefore every vector spectral measure is
  absolutely continuous, incompatible with the purely atomic measure forced
  by an exact all-n Li cocycle realization; `I - U^n` is non-Hilbert-Schmidt
  for every `n >= 1`, and every declared discrete-time tensor composite
  `U tensor V` remains absolutely continuous by convolution. For the
  boundary vector the ladder increments increase strictly toward `phi^2`
  without attaining it. After the one free rescale
  `|c|^2 = lambda_1`, the second rung
  `lambda_1 (2 + 2r)` is disjoint from
  `lambda_2 = 4 lambda_1 - M_1` by exact intervals
  (J-LI-LAMBDA-SHIFT-NOGO [T],
  probes/P-R2-SCALING-SHIFT-1).
  LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER [F] records this exact
  discrete-time class and its declared unitary tensor composites. It does
  not cover distribution or trace formalisms, moment-functional
  constructions, or genuinely global adelic objects.

The first completed-zeta K-side rung is pinned at finite enclosure scope
(O-R2-K-JUNCTION-PIN [C], probes/P-R2-K-JUNCTION-PIN-1). For
`K = Q(zeta_5)`, define

```
lambda_1^K
  = 1 + (3/2) log 5 - 2 log(2 pi) - gamma
    + sum_(chi != chi_0 mod 5) L'/L(1,chi),

lambda_1^Q
  = 1 + gamma/2 - (1/2) log(4 pi).
```

Exact rational interval arithmetic gives the computed enclosures

```
lambda_1^K in
[0.304595618542798635262524662701,
 0.304595618542798635262524662702],

sum_(chi != chi_0 mod 5) L'/L(1,chi) in
[1.143408547611871901089216,
 1.143408547611871901089217],

lambda_1^Q in
[0.023095708966121033814310,
 0.023095708966121033814311].
```

The identity `(3/2) log 5 = 6 log s_J + 3 log phi` is preserved interval by
interval. The literal modulus-five principal-character convention is a
disjoint negative control at
`[0.706955096651323728912714, 0.706955096651323728912715]`. This computed
pin constructs no R2 carrier, proves no higher Li rung, and makes no RH
claim.

The E8 multiplicity obstruction, the compact-boundary Hilbert-Schmidt
obstruction, and the scaling-shift spectral-type obstruction are now closed
only at those declared scopes. In particular, the compact lambda-adic
boundary cocycle-vector route remains LAMBDA-COCYCLE-ANGLES [H]. The program
also continues in the moment-functional (Weil positivity) frame and in
genuinely global constructions. RH remains O; none of these results proves,
assumes, or falsifies RH.

The wall is one archimedean wall, and it is understood: the shadow is
the polylogarithm ladder of J. What stands on it: the quantum
substrate gates, Larmor and the Schwinger term, the term carrying the
hypothesis value J Jbar / script-Q = 1/(2 pi) (QUANT-SUBSTRATE); the
non abelian measure lift (COLOR-MEASURE-SELECTION); and the shared
2 pi U(1) circle itself, with pi the locked shadow.

## 17. Engineering witnesses

Unregistered engineering readouts are excluded from the normative
Canon. Their non-canonical disposition record is `notes/ENGINEERING.md`;
nothing in that note is evidence for a public claim. The standing bar
for a computation-only theorem is byte-identical stdout on two
architectures through the public activation gate.

## 18. The frontier

The live obligations and hypotheses of the program. Each identifier is
a registry row with status O or H; the registry carries for every row
a concrete falsifier or a decision condition: what closes it
positively and what closes it negatively.

- LAMBDA-COCYCLE-ANGLES [H]. The compact lambda-adic boundary route remains
  open only in cocycle-vector form: an exact realization would require a
  vector `v in L^2(O_lambda,Haar)` with
  `||sum_(k=0)^(n-1) U_J^k v||^2 = lambda_n` for every `n >= 1`.
  Necessarily every Cayley angle
  `2 arctan(1/(2 gamma))` lies in `2 pi (1/4) Z[1/5]`, and the Li second
  differences approach `2 lambda_1` along `n = 4 . 5^A`. One ordinate
  proved outside that grid, failure of the stated limit, or any all-vector
  contradiction in this compact-boundary class fires the hypothesis.

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
THE WALL
  QUANT-SUBSTRATE            the Larmor gate and the Schwinger term gate
  COLOR-MEASURE-SELECTION    the measure lift onto SL_3(F_5): 24 carrier
                             orbits, 16 observable types; the minimal
                             new datum is a weight vector
GRAVITATIONAL WAVE
  TT-SOURCE                  the emission map
  QNM-LEAVER-MU              the quasinormal mu decision
  TT-VECTOR-STATE-NORMALIZATION  the only gate yielding a numerical r_T(k)
COSMOLOGY
  FRW-INHOM                  the inhomogeneous sector, the named
                             classical horizon
  NS-TILT                    n_s - 1 = -5 alpha; falsifier live, CMB-S4
  DE-CONFORMAL-WEIGHT        the dark energy conformal weight
COLOR
  ALPHA-S-RUNNING            the running above the 3/4 seed
  SCHEME-DICTIONARY          exact seeds to measured couplings
  GENERATIONS-L3             the generation structure at the L3 frontier
PHOTON
  PHOTON-WINDOW-PROOF        the closed charge 5 worldline occupancy
                             bound and electric face roughening certificate
PLENUM AND KERNEL
  KC3-PLENUM-READOUT         the residue class readout of the ramified
                             place
  SQRT-PHI-TIME-GRAVITY      the typed clock and gravity bridge remains
                             after the exact L1 digit lift
  CURVATURE-OPERATOR-CANONICAL
                             whether the public architecture determines
                             one equivalence class of spatial-curvature
                             operator after its carrier, measure,
                             projection, and commutator type are frozen
ENTROPY BRIDGE
  ENTROPY-LAYER-BRIDGE       construct the measurable, canonical and
                             measure-correct equivariant selection family
                             Psi_kappa: O/lambda^5 -> L_n; the cylinder
                             ansatz is closed negatively and the finite
                             carrier counts already match
MEASURE
  QUADRATIC-ENVELOPE-DECODER the full decoder carrier hypothesis
  TM-SYM2-MEASURE            the Thue-Morse selection and physical measure;
                             residual Born phase halving 1/6 = (1/2)(1/3)
MATTER
  NEUTRON-DELTA-EM           the interior compression channel
  PROTON-RESIDUAL-IS-QCD     gated on QCD dynamics
OBSERVER
  OBSERVER-WRITE-PORT        armed, algebraic; ordered after the
                             metrology closure
EMPIRICAL HORIZON
  DESI DR3 (w = -14/15); MOLLER (sin^2 theta_W); future shadow
  measurements after a public inference rule; CMB-S4 (the tilt)
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
cutover audit records historical provenance only; it supplies neither
evidence nor status to a public claim. Simplicity is the ultimate
perfection. Truth is not rude. Truth is just true.
