# TWIST-J core

**Status:** Public Canon v1 candidate in GENESIS. Nothing here is
canonical before the separate activation.

TWIST-J tests whether physical reality can be modeled as a closed,
exact, deterministic integer system whose continuum, geometry,
probability, and fields are readings. Its single algebraic axiom is

```
J = 1 + zeta_5^2.
```

Public Canon v1 also declares a discrete architecture. It does not
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

Stable orientation results:

- J-UNIT [T], J-PROJECTIONS [T], PLENUM-POINT [T], J-GOLDEN-BRIDGE
  [T], J-STEP [T]: exact arithmetic of J; AXIOM-PROJECTION-DICTIONARY
  [D] carries the physical projection and plenum readings.
- CENSUS-313 [C]: 313 attractors in the declared finite checkpoint.
- BORN-HALF-ANGLE [T], BORN-RESIDUAL-SPLIT [T], SPIN-BISECTOR [T],
  BORN-ORDER-STAIRCASE [T]: the finite algebraic quartet;
  MEASURE-BORN-VERB [D] is the measurement dictionary.
- MAXWELL-BIANCHI [T], MAXWELL-GAUSS-CHAIN [T],
  MAXWELL-AMPERE-CHAIN [T], MAXWELL-OBSTRUCTION-P [T]: the exact
  chain layer; MAXWELL-CLOSED [D] is its classical dictionary.
- Z2-PLACES-SPLIT [T]: the exact Galois census and Gaussian-prime
  swap; TWO-PLACE-PHYSICS [D] carries the place and CPT readings.
- FORCE-WEYL-HOLONOMY [T]: the finite Weyl commutator;
  FORCE-AS-CURVATURE [D] carries the force-curvature reading.
- FRW-CANONICAL-FORM [T]: the registered homogeneous rank-one lapse
  scope; GRAVITY-BRIDGE-LAW [D] is the SI equation dictionary, while
  COSMOLOGY-READING-DICTIONARY [D] carries the cosmological reading and
  the numerical value of G remains open.
- BOOST-READING-SPLIT [T]: exact integer-index rapidity algebra;
  BOOST-COUNT-LADDER [D] is the velocity dictionary.
- COLOR-MCKAY-E8 [T] and its registered ladder: finite group,
  representation, and invariant theory; COLOR-LADDER-DICTIONARY [D]
  and COLOR-KINEMATICAL-GL2 [D] carry the color readings.

Time is a counter. Space is read through commutators. The modulus and
argument of J provide two exact algebraic projections. Their physical
interpretations are only as strong as the registered dictionary rows.

The authoritative current state is `canon/REGISTRY.tsv`.
`canon/CANON.md` gives complete scopes and `canon/FRONTIER.md` gives
the live obligations. Reproductions under `reproduce/` must exit zero
with byte-identical stdout.
