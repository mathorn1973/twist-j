# TWIST-J core

**Release identity:** Public Canon v13. Normative authority and activation
state are declared exclusively by [STATUS.md](../STATUS.md).

TWIST-J tests whether physical reality can be modeled as a closed,
exact, deterministic integer system whose continuum, geometry,
probability, and fields are readings. Its single algebraic axiom is

```
J = 1 + zeta_5^2.
```

Public Canon v13 also declares a discrete architecture. It does not
claim that the checkpoint space, the five kernel generators, the
selector, or the decoder are uniquely derived from J. The architecture
contains no fitted dimensionless parameter; its one SI calibration
anchor is the electron mass.

The complete autonomous state and update are

```
Omega = N_0 x F_5^6,                    omega = (n, psi),
theta_n = s_2(n) mod 2,
z_6(psi) = sum_k psi_k mod 5,
U(n, psi) = (n + 1, g_(z_6(psi) + 2 theta_n mod 5)(psi)),
(g_0, ..., g_4) = (a, b, c, d, e).
```

`N_0` is the forward orbit of zero under the 2-adic odometer. No
Thue-Morse parity function on all of `Z_2` is asserted. The projection
to `F_5^6` is the finite checkpoint; it is not the whole autonomous
state. Log streams are derived orbit records.

The decoder is a typed partial interface. Its functional order is
matter, then geometry, then clock:

```
D_matter : dom(D_matter) subset K -> MatterData
D_geom   : dom(D_geom) subset K x MatterData -> GeometryData
D_clock  : dom(D_clock) subset K x MatterData x GeometryData
           -> ObservableHistory
```

Here `K` is the set of forward `U`-orbits. Decoder outputs never feed
the state update. Totality, uniqueness, and completeness remain open;
the public reading split is a dictionary at its registered legs
(READING-SPLIT [D]), not a completeness theorem.

<!-- BEGIN GENERATED CORE CLAIMS -->
The stable orientation claims are generated from the registry:

- READING-SPLIT [D]: the partial decoder interface reads the registered legs by linear projection, binary Thue-Morse cut, and quadratic registration; the linear leg is CODEC-TR4, the binary cut drives the census, and the quadratic leg is the Born square; no totality, uniqueness, or completeness of the decoder is claimed
- J-UNIT [T]: Q(zeta_5)
- J-PROJECTIONS [T]: in the principal archimedean embedding, J = 1 + zeta_5^2 has modulus 1/phi and principal argument 2 pi/5
- PLENUM-POINT [T]: in Z[i, zeta_5], T_pl = s_J + i phi = 2i(1 - J), with s_J^2 = 3 - phi, abs(T_pl) = 2, arg(T_pl) = 3 pi/10, zeta_5 T_pl^2 + 4 = 0, T_pl^10 = -2^10, and T_pl/2 = zeta_20^3 = zeta_4^-1 zeta_5^2
- J-GOLDEN-BRIDGE [T]: Z[zeta_5]
- J-STEP [T]: Z^4, the regular representation
- AXIOM-PROJECTION-DICTIONARY [D]: the modulus projection read as gravity and scale, the argument projection as electromagnetism and phase, the CRT factors of T_pl as the prime 5 write and prime 2 read, and the unit and ramified chords as gravity and space channels; a dictionary resting on J-PROJECTIONS, PLENUM-POINT, J-MODULUS-CHORD, and J-RAMIFIED-CHORD, with no uniqueness claim
- CENSUS-313 [C]: the full enumeration of Z_5^6 under the Thue-Morse driven kernel, warmup 400, window 300, closure and stability checked
- BORN-HALF-ANGLE [T]: every Born unit of A_8 = Z[zeta_8]/5; the normalized root on the 11 non antipodal units of the norm gated half (the squares of the cyclic unit group of order 24); at u = -1 the bisector vanishes and normalization is undefined
- BORN-RESIDUAL-SPLIT [T]: the residual rings Z[i]/5 and Z[zeta_8]/5 and their conjugation swap
- SPIN-BISECTOR [T]: the integer skeleton and the SL_2(F_25) shadow of order 8; no positivity claim
- BORN-ORDER-STAIRCASE [T]: root orders 4, 8, 16 first realized at F_5, F_25, F_625, with minimality against every smaller degree (16 divides none of 4, 24, 124); the gate is the square condition on the bisector norm
- MEASURE-BORN-VERB [D]: the measure read as the Born square of the verb, resting on the exact BORN-FACE-WEIGHTS theorem layer
- MAXWELL-BIANCHI [T]: on the 3+1 tesseract the Bianchi identity dF = d(dA) = 0 holds identically in the 32 independent edge symbols on all 8 cubes, and gauge invariance F[A + d Lambda] = F[A] is an identity in 16 more vertex symbols on all 24 faces
- MAXWELL-GAUSS-CHAIN [T]: Gauss as the boundary equation bd E = rho on the closed 2 x 2 x 2 spatial torus: the Smith form of the boundary has all seven elementary divisors equal to 1, a constructive two edge dipole solves the point pair exactly, and the integrated law holds on every one of the 256 vertex regions
- MAXWELL-AMPERE-CHAIN [T]: the inhomogeneous pair as the face boundary equation on the 2^4 spacetime torus: conservation bd1 bd2 = 0 is an exact identity in the 96 face symbols, the Smith form of the face boundary has all 45 divisors equal to 1, and H_1 is free of rank 4 with the four winding certificates pairing to the identity on the elementary winding currents
- MAXWELL-OBSTRUCTION-P [T]: the obstruction pair is counted in p = 5: over F_5 Gauss is solvable iff the total charge vanishes mod 5 (rank 7 with the augmentation annihilating the image, constructive solution and exhibited obstruction), and the current pair is solvable iff the current is conserved and all four winding numbers vanish mod 5 (the exact rank identity 45 = 64 - 19, the single winding obstructed, five parallel windings solved)
- MAXWELL-CLOSED [D]: the dictionary reading: the classical Maxwell system of the decoder closes exactly on the chain complex, the electric and magnetic laws as boundary equations with their obstructions counted in p; no continuum limit is claimed
- Z2-PLACES-SPLIT [T]: the cyclotomic Galois involutions sit at exactly two places: one involution at zeta_5 (the single order 2 element of the cyclic Galois group) and a complete Klein four at zeta_8; 5 = (2 + i)(2 - i) in Z[i] with conjugation swapping the two Gaussian primes above 5
- TWO-PLACE-PHYSICS [D]: the v_5 place read as the write side for geometry, gravity, and the pentit substrate, the v_2 place as the read side for Clifford, Born, and the foreign qubit; CP read from zeta_5 and Gaussian conjugation, T from Thue-Morse reversal, and CPT as their composition; the Born square declared as the cross-place descent reading; no uniqueness or physical CPT-operator theorem is claimed
- FORCE-WEYL-HOLONOMY [T]: the finite Weyl pair on five basis states satisfies Z X Z^-1 X^-1 = zeta_5 I exactly; the commutator phase is primitive of order 5 with principal argument 2 pi/5
- FORCE-AS-CURVATURE [D]: the finite Weyl commutator read as a force curvature and, through AXIOM-PROJECTION-DICTIONARY, the two J projections read as the two abelian force channels; no uniqueness or completeness of the force dictionary is claimed
- FRW-CANONICAL-FORM [T]: the rank 1 lapse action closes the displayed (00) constraint algebra: the lapse variation gives 3 H^2 = lambda rho, lambda = 216 pi gives H^2 = 72 pi rho, the coefficient 3 = C(3,2) counts the spatial 2-planes, continuity gives the second Friedmann equation, and the Hamiltonian constraint takes the canonical form; the fiber multiplier k_f = 1 is forced by the displayed master identity against G_nat = 27 = d^3 with V_cell = 864 pi carrying exactly one fiber 2 pi; no source-projector uniqueness, amplitude ansatz, or E_total claim is included
- GRAVITY-BRIDGE-LAW [D]: the equation layer of the SI bridge on the single anchor m_e: alpha B g = 1 identically with B = alpha^-1/g; g = 2^5 phi^2 sqrt(3 - phi) with g^2 = 1024 phi^4 (3 - phi) and 3 - phi = |1 - zeta_5|^2 exactly; G_T = (32/33)^2 alpha^20 / g with (32/33)^2 = (2^5/(2^5 + 1))^2 and alpha content exactly alpha^20; the wall spelling ell_P / lambda_e = (32/33) alpha^10 / sqrt(g) is equivalent under ell_P^2 = 27 ell_G^2; the SI value of G is not claimed and stays on the frontier
- COSMOLOGY-READING-DICTIONARY [D]: the zero linear variation in TT-LINEAR-ZERO read as zero linear tensor response and r_T = 0 at the declared isotropic dictionary layer, GYRON-DENSITY read as the mass-ladder prefactor, and the committed COSMOLOGY-REGISTER forms read as cosmological observables; no unique decoder or full perturbation theorem is claimed
- BOOST-READING-SPLIT [T]: for every n >= 0 in Q(sqrt5), C_n = phi^n + phi^-n and S_n = phi^n - phi^-n read as (L_n, sqrt5 F_n) for even n and (sqrt5 F_n, L_n) for odd n; beta_n = S_n/C_n obeys the exact index-addition law and C_n^2 - S_n^2 = 4
- BOOST-COUNT-LADDER [D]: the integer exponent n read as the substrate rapidity count n ln phi and beta_n as the decoder velocity; Einstein composition read as index addition, resting on BOOST-READING-SPLIT
- COLOR-MCKAY-E8 [T]: tensoring by the spin row gives affine E8 with dimension marks; the moments are Catalan through degree 10 and first differ at degree 12 by 133 = 132 + 1; the verb weights are {4 phi^-2, 4 phi^2}
- COLOR-LADDER-DICTIONARY [D]: the exact D5 to 2I to affine E8 representation and invariant ladder read as the nonabelian color door, with color su(3) on the traceless endomorphisms of the three dimensional trace kernel; no unique color assignment, QCD running, confinement, or complete measure lift is claimed
- COLOR-KINEMATICAL-GL2 [D]: the special-linear kinematical image read as GL_2(F_5) of order 480 on the antisymmetric plane, embedded by g -> (det g)^-1 direct-sum g along 3 = 1 + 2

<!-- END GENERATED CORE CLAIMS -->
Time is a counter. Space is read through commutators. The modulus and
argument of J provide two exact algebraic projections. Their physical
interpretations are only as strong as the registered dictionary rows.

The authoritative current state is `canon/REGISTRY.tsv`.
`canon/CANON.md` gives complete scopes and `canon/FRONTIER.md` gives
the live obligations. Reproductions under `reproduce/` must exit zero
with byte-identical stdout.
