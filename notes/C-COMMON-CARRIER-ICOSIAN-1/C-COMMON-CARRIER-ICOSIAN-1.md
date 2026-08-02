# C-COMMON-CARRIER-ICOSIAN-1: the icosian common carrier (rev 1)

NON-CANONICAL. Incubation-lane candidate against Public Canon v30. No
authority, no Canon change, no canon/ file touched. Continuation of the
Herm2 analytic lane (notes/C-HERM2-BORN-CONE-1) and of the probe proposal
P-COMMON-CARRIER-ICOSIAN-1 recorded there.

## Candidate claim

Let F = Q(sqrt5), B = (-1,-1)/F the totally definite quaternion algebra,
and O the icosian ring: the Z[phi]-order spanned by the 120 icosians. Then
O is one carrier on which the public A5 (through 2I) and the J-step
coexist canonically, and the carrier itself decides how much of the
loxodromic step is integral. All claims below are candidate-T unless
labeled otherwise; every one is pinned by a named gate of
`verify_common_carrier_icosian.py` (45 gates) or refuted-break gate of
`break_common_carrier_icosian.py` (6 gates), exact arithmetic throughout,
no randomness.

### 1. The two actions and the canonical Hermitian form

- 2I is the group of the 120 units of reduced norm 1; 2I/{+-1} = A5
  (gates I1-I4, six-Sylow simplicity supplement in the gate name).
- An icosian q of multiplicative order 5 with trd(q) = phi - 1 realizes
  zeta5: Z[q] = Z[zeta5], phi = 1 + q + q^4, and the 12 such icosians form
  a single 2I-conjugacy class containing q and q^-1, so the CM embedding
  K = Q(zeta5) -> B is unique up to inner 2I and CM conjugation
  (Q1-Q5; the Sylow supplement answers the Skolem-Noether caveat).
- J = 1 + q^2 is a unit of O with nrd(J) = J Jbar = 2 - phi = phi^-2 and
  J phi = q (J1-J3; the registered J-MODULUS-CHORD and J-GOLDEN-BRIDGE
  identities reproduced on the carrier).
- On B = K + K e (e a pure icosian with e q = qbar e, e^2 = -1, E1-E2),
  the form h(x,y) = pi_K(x ybar) is the canonical CM-Hermitian form:
  Gram identity on {1, e}, Hermitian for the CM involution, definite,
  every icosian an h-unit vector (H1-H3).
- The right 2I-action is h-unitary, the left K-action is h-similitude
  (J with totally positive multiplier phi^-2), and the two actions
  commute by associativity (A1-A3). No choice enters beyond q (pinned up
  to inner and Galois) and e (any unit vector of the canonical line K e).

### 2. The free module and the ramified glue

- O is a FREE rank-2 Z[zeta5]-module: O = Z[q].1 + Z[q].omega with
  omega = (1+i+j+k)/2 (FB1). Freeness is forced abstractly by Steinitz
  and h(Q(zeta5)) = 1 [T, literature]; the gate exhibits the basis.
- The h-orthogonal splitting K.1 + K.e is NOT integral: for every
  admissible e the sublattice Z[q].1 + Z[q].e has index exactly 5 in O
  (G1, BK3). The glue sits at the ramified prime p5 = (q - q^4),
  N(2+phi) = 5, and is diagonal: O intersect K e = Z[q] e (G2, G3).
- h is inverse-different-valued: h(O,O) lies in p5^-1 Z[zeta5] and not in
  Z[zeta5] (G4, BK4). This is the E8 signature of the carrier (section 4).

### 3. The glue criterion and the twisted even tick

- Reduction mod p5 sends q -> 1, phi -> 3, J -> 2, J^-1 -> 3. The J-residue
  2 is exactly the registered ramified multiplier J_lambda of
  RAMIFIED-TM-LIFT; the golden pair shadows to {2, 3} as in COLOR-CORE-2I
  (T2).
- Criterion (T3, swept exactly over 400 diagonal pairs): a diagonal
  operator diag(D1, D2) along the h-splitting preserves O if and only if
  res(D1) = res(D2) in F5. The glue is the diagonal F5 across the
  ramified place.
- Consequence: the det-1 even tick diag(J, J^-1) is NOT integral
  (res 2 vs 3; BK1, BK2), while the sign-twisted even tick
  diag(J, -J^-1) is (res 2 = 2; T4). Its quadratic coordinate action is

      u -> (2 - phi) u,   v -> phi^2 v,   w -> (1 - J) w,

  and 1 - J = -zeta5^2 is the registered primitive TENTH root
  (J-TENTH-ROOT): the glue converts the naive fifth-root phase q^2 into
  the tenth root. The double cover appears in the phase. Five twisted
  even ticks are the pure boost with an e-slot sign, diag(phi^-5, -phi^5);
  only ten close it: diag(phi^-10, phi^10) (T5).
- Half-step obstruction (T6): y^2 = J forces nrd(y) = +-phi^-1, neither
  totally positive (sigma(phi^-1) = -phi < 0), while nrd is totally
  positive on B. The single tick has NO F-rational carrier realization;
  its field of definition is K(sqrt J) = K(sqrt phi) (T7), one golden
  square root away. The odd tick is spinorially hidden; the obstruction
  is the same Galois sign sigma(phi) < 0 that chi5 uses to split the
  conjugate moduli of J.

### 4. E8 with no new parameter

The golden-twisted trace form B(x,y) = Tr_{F/Q}(phi trd(x ybar)/sqrt5)
is integral, even, positive definite and unimodular on O (X1, X2), hence
THE E8 root lattice [T, literature: uniqueness of the even unimodular
definite rank-8 lattice]. The untwisted trace form has determinant
5^4 (BK6): the ramified prime is load-bearing. The carrier therefore
meets the registered affine-E8 ladder (COLOR-MCKAY-E8) at the lattice
level, through the same p5 that glues the h-splitting.

### 5. Bridge to the registered 2I

- The registered COLOR-INTEGRAL-LIFT generators S, T close to 120
  matrices over Z[zeta5] with det 1 and bijective reduction onto SL2(F5)
  (L1, L2; reproduced, not re-registered).
- rho(g) = right multiplication by gbar in the free basis {1, omega} is
  an integral 2x2 representation over Z[zeta5], det = nrd = 1 (L3).
- The (order, trace) class functions of rho(2I) and of the registered
  lift agree exactly and sum of tr^2 = 120 (irreducibility), so the two
  are GL2(K)-conjugate [T, literature: Noether-Deuring] (L4). The icosian
  right action IS the registered integral 2I up to base change.
- Dictionary onto COLOR-GOLDEN-TABLE (L5): tr(T) = phi - 1 = trd(q), and
  5a/5b are separated by the spin trace, so the class of q is the
  registered class 5a; with the conjugation traces (C1, C2) the
  conjugation 3-space is the canon row 3a (chi(5a) = 1 - phi), the McKay
  E8-arm row. The canon 5a/5b RESIDUE labels, by contrast, are pinned
  only by the frozen matrices: res(phi) = 3 is a non-residue, so a basis
  change of determinant phi flips the unipotent residue class (L6). This
  is an exact reason why COLOR-INTEGRAL-LIFT must freeze explicit
  generators.

## Status separation

- candidate-T: every gate listed above (exact arithmetic, single
  recorded leg; see RESULT).
- [T, literature], audited by gates: Steinitz + h(K) = 1 (freeness),
  E8 uniqueness, Noether-Deuring.
- [D]: reading the h-cone data as the Born/causal structure of the Herm2
  lane; reading the twisted tick as "the bit rides the even tick". The
  only registered cone is LADDER-LIGHTCONE (uv = 4); nothing here touches
  it.
- [H]: that O with (right 2I, left K, h) is THE common carrier of the
  quadratic reading of the registered decoder. This is exactly the
  candidate data this bundle offers to the open rows
  QUADRATIC-DECODER-DATA and COLOR-MEASURE-SELECTION; no closure, scope
  move, or status change of any registry row is claimed or implied.

## Scoping against fired and frozen rows

- COLOR-DYNAMICAL-COLOR [F]: 2I here is kinematical; no dynamical claim.
- SPIN-LIFT-FORCED [F]: no canonical marked D5/Dic5 lift is assumed; q is
  pinned only up to inner 2I and CM conjugation (Q5), and e only up to
  the canonical line.
- PHIBIT-NOT-TAU [F]: no dimension-phi physical reading is used.
- J-STEP freezes the Z^4 power-basis model of g_J; this bundle does not
  replace it. The left action of J on O restricted to Z[q] IS the
  regular representation of J-STEP under zeta5 -> q; the carrier claims
  are about the quaternionic extension, stated separately.
- CARRY-PENTAD is the registered precedent (A4 lattice, I + C^2
  integrally conjugate to M_J, Weyl S5). This bundle differs: rank-8
  icosian ring, 2I not S5, Hermitian h, and the ramified glue; the two
  should eventually be joined, which is open.
- TWO-PLACE-PHYSICS / DEGREES-BY-PRIME: i is not in Q(zeta5); the form h
  needs no i -- the CM involution supplies the dagger inside the v5
  world. Herm2(C) appears only after archimedean completion, and no
  archimedean place is chosen anywhere in this bundle: every gate is
  exact over F and K. The two completions are Galois-swapped; the swap
  is the chi5 bit. The Lorentzian det of the Herm2 lane and the definite
  nrd of the carrier are kept strictly separate (they meet only after
  complexification); the quadratic coordinates (u, v, w) carry the
  Lorentzian reading, nrd carries the definite one.

## Open continuations (probe proposals live in the Herm2 bundle)

- P-COMMON-CARRIER-ICOSIAN-1: realize the arithmetic Galois C4
  quarter-turn on THIS carrier (it acts on the CM spinor of the Herm2
  lane; here it must exchange the two archimedean completions). The glue
  criterion suggests the quarter-turn is exactly what absorbs the sign
  twist; open.
- P-DECODER-SOS-FORM-1: the decoder-shape falsifier for the [H] claim.
- P-U1-DICTIONARY-1: arg J as spatial little group vs internal U(1); on
  this carrier arg J is the rotation part of the twisted even tick, with
  the tenth-root phase 1 - J; the dictionary remains open.

## Falsifiers

- F-ICO-1: any FAIL gate of verify_common_carrier_icosian.py.
- F-ICO-2: any FAIL gate of break_common_carrier_icosian.py (for
  instance an integral untwisted even tick, an h-orthonormal free basis,
  or an O_K-valued h).
- F-ICO-3: a registered census output whose quadratic leg cannot be
  carried by (O, h, right 2I, left K) in the sense of
  QUADRATIC-DECODER-DATA; this fires the [H] claim only.

No falsifier fired. No threshold moved. PROMO deferred.
