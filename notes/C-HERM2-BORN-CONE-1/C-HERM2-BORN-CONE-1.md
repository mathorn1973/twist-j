# C-HERM2-BORN-CONE-1: the Herm2 quadratic reading (rev 1)

NON-CANONICAL. Incubation-lane candidate against Public Canon v30. No
authority, no Canon change, no canon/ file touched. This bundle is the
durable landing of a consolidation developed 2026-08-02 in a container
session outside the repository; the primary document is the verbatim
handover HANDOVER-HERM2-ANALYTIC-ATTACK_2026-08-02.md (Czech), whose
verification artifacts are committed here byte-identically.

## Candidate claim (summary of the handover)

The quadratic reading of the split unit (notes/C-SPLIT-UNIT-1 lane) is
Herm2(C): its positive cone is simultaneously the Born cone and the
future causal cone, and J acts on it as the multiplier of one loxodromic
Lorentz step. Exact backbone, all candidate-T, pinned by the 47 gates of
herm2_consolidation_verify.py (exact arithmetic in Z[zeta5], Q(sqrt5)
and complex rationals; the rows named "numeric witness" are labeled
witnesses standing on the exact rows cited next to them):

1. J Jbar = J + Jbar = 2 - phi = phi^-2, hence cos arg J = (phi-1)/2 and
   arg J = 2 pi/5 with no numerics; J^5 = 5 phi - 8 = phi^-5 > 0 decided
   by the integers 125 > 121: the fifth power of the loxodromic step is a
   pure boost. (Z1-Z13, L1-L3; the registered J-UNIT, J-MODULUS-CHORD,
   J-PROJECTIONS, J-GOLDEN-BRIDGE identities reproduced.)
2. det X = t^2 - x^2 - y^2 - z^2 proved exactly on a 3^4 interpolation
   grid; X >= 0 iff t >= 0 and det X >= 0: Born cone = future causal
   cone; the boundary det = 0 is pure = null. (M1-M3)
3. Boost data of the J-step in Q(sqrt5): cosh eta = sqrt5/2,
   sinh eta = 1/2, eta = ln phi, beta^2 = 1/5, gamma = sqrt5/2. (B1-B5)
4. Rigidity: the A5-invariant symmetric form on 1 + W has exactly two
   parameters and invariance under the single J-boost forces b = -a
   (lever cosh sinh = sqrt5/4 != 0); the Euclidean choice is not
   invariant. Minkowski is forced, not chosen. (B6-B8, A4)
5. Lambda^2 W = W with dim Hom_A5(Lambda^2 W, W) = 1: the unique
   equivariant bracket; Zolotarev p = 5: the bit is the orientation of
   3-space, det(m_a|W5) = chi5(a); Cauchy-Binet exactly: the pure branch
   is null, non-collinear mixture is timelike. (A1-A3, O1-O2, CB1-CB2)

Three transported findings:

A. The arithmetic Galois C4, phi_g(z1, z2) = (z2, conj z1), does NOT
   stabilize Herm alone: on coherences it is the 4-cycle
   (w, s) -> (s, conj w). Stable is only the PAIR
   (Psi Psi^dagger, Psi Psi^T): the two-slot decoder is Galois-forced.
   The rotoreflection S(t, z, w) = (t, -z, i w) is a different,
   geometric realization of C4 (antiunitary spinor lift of order 8);
   the earlier identification "Galois = S on Herm" was unproved and is
   wrong. (G1-G2 vs C1-C5)
B. Q(zeta5) has exactly 4 CM types, all primitive, one Galois orbit:
   the CM type is unique up to Galois. (K1)
C. The Galois quarter-turn conjugates g_J to diag(1/sqrt J, conj sqrt J):
   multiplier phi, a pure expanding boost; what is "rotation" and what is
   "boost" is decided by the complex structure, and the bit moves it,
   consistent with the chi5 split of the conjugate moduli. (L4)

## Canon anchors and scoping

- QUADRATIC-DECODER-DATA [O] owns Q(psi) = (psi psi^dagger, psi psi^T).
  Finding A is candidate support for exactly that pair being forced; this
  bundle proposes candidate data for the row's open fields (effective
  carrier, dagger, transpose, Gram) and claims no closure and no scope
  move. READING-SPLIT and DEF-DECODER-COMPLETION-CONTRACT scoping is
  respected; nothing here lets other legs inherit anything.
- The only registered cone is LADDER-LIGHTCONE (uv = 4 in Q(sqrt5)).
  The Herm2 determinant cone here is NEW [D]-layer material tied to the
  quadratic leg, not a reinterpretation of that row.
- TWO-PLACE-PHYSICS / DEGREES-BY-PRIME: i is not in Q(zeta5); Herm2(C)
  with dagger is a v2-side (Clifford/Born) structure built over v5-side
  golden data, a cross-place construction under the declared dictionary.
  The det dictionary is pinned: the Lorentzian det on Herm2 and the
  definite quadratic of the carriers agree only after complexification
  and are kept separate.
- WALL-LI2-RUNG registers the C4 Galois action on J and the {1,4} vs
  {2,3} CM pairing of embeddings used throughout.
- COUPLINGS-DETERMINE is the registered theorem-level use of
  psi psi^dagger (Gram-normalized density); the Born reading here reduces
  to it and does not re-register it.
- No archimedean place is chosen in any exact row; rows that need one
  (Herm2(C), the L-witnesses) are labeled witnesses. The two completions
  are Galois-swapped; the swap is the chi5 bit.

## Status separation

candidate-T: the exact backbone (Z, M, B, A, O, CB, G, K, C gates).
Labeled witnesses: L1-L4, C5, RA2, D1 (floats with stated tolerance on
an exact backbone). [D]: the ontological cone reading. [H]: mass =
non-collinearity; completeness of the two-slot decoder reading. [O]:
the four hard points as recorded in the handover (common carrier: now
attacked in notes/C-COMMON-CARRIER-ICOSIAN-1; CM type: closed at
classification level by K1; positivity: reduced to decoder shape;
spatial vs internal phase: open dictionary).

## Probe proposals carried by this lane

```text
P-COMMON-CARRIER-ICOSIAN-1   A5 (via 2I in the icosians) and g_J on one
                             Z[phi]-carrier; falsifier: no compatible
                             realization. Candidate-level realization:
                             notes/C-COMMON-CARRIER-ICOSIAN-1.
P-DECODER-SOS-FORM-1         the census D_matter output is a weighted sum
                             of squares sum w psi psi^dagger; falsifier:
                             a registered field outside this shape.
P-U1-DICTIONARY-1            exact dictionary for arg J: spatial little
                             group vs internal U(1) on the symmetric
                             slot; falsifier: a binding prediction that
                             fails on registered data.
```

## Falsifiers

- F-HERM2-1: any FAIL gate of herm2_consolidation_verify.py.
- F-HERM2-2: a registered census output outside the sum-of-squares
  decoder shape (fires the positivity reduction, hard point 3).
- F-HERM2-3: a proved identification "Galois C4 = S on Herm" would
  contradict finding A and fires this bundle's correction claim.

No falsifier fired. No threshold moved. PROMO deferred.
