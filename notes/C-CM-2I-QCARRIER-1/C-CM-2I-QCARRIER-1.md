# C-CM-2I-QCARRIER-1: the arithmetic C4 on the registered lift (rev 1)

NON-CANONICAL. Incubation-lane candidate against Public Canon v30. No
authority, no Canon change, no canon/ file touched. First exact slice of
the audit-proposed probe P-CM-2I-QCARRIER-1: which part of the
arithmetic Galois C4 of K = Q(zeta5) is compatible with the registered
integral 2I lift <S, T> over Z[zeta5] (COLOR-INTEGRAL-LIFT), under
GL2(K)-conjugacy as the frozen equivalence. All gates exact and
deterministic (verify_cm_2i_qcarrier.py, 10 gates).

## Candidate claims

1. Rational core (Q1-Q2). The lift closes to 120 det-1 matrices; NO
   Galois twist fixes it setwise, and each twist meets it in exactly
   {+-I, +-S} = <S>: the arithmetic Galois branches of the lift
   intersect precisely in the GEOMETRIC C4. The Herm2 finding that the
   arithmetic C4 and the rotoreflection S are different C4 realizations
   holds verbatim at the integral carrier level.
2. Descent dichotomy (Q3-Q5, Q10). Every trace of the lift lies in F
   and is sigma-fixed pointwise, so the CM involution descends to the
   single carrier with markings intact (Noether-Deuring conjugacy
   intertwining g -> sigma(g)). The quarter-turn tau moves EVERY golden
   trace (exactly the 48 elements of orders 5 and 10), so it descends
   only through the OUTER automorphism swapping the golden classes
   5a <-> 5b. The descent subgroup of C4 with markings intact is
   exactly ker chi5 = {1, sigma}: THE BIT IS THE MARKING OBSTRUCTION
   OF THE ARITHMETIC QUARTER-TURN. Consistent with the fired
   SPIN-LIFT-FORCED (marked lifts are not unique); the audit's
   compatibility trichotomy resolves to neither EMPTY nor UNIQUE but
   to this kernel/coset split.
3. Multiset lesson (Q4). The (order, trace) MULTISET of the lift is
   invariant under all four twists -- the golden classes only swap --
   so multiset-level data cannot see the branch. This also sharpens the
   exposition of C-COMMON-CARRIER-ICOSIAN-1 gate L4: the subgroup
   conjugacy proved there holds, but the marked identification
   (which branch) is carried by the character values at the pinned
   elements (gate L5 there), not by the multiset.
4. The pair is Galois-closed (Q6). chi_2a + chi_2b is Q-valued on every
   element: the branch pair carries the full arithmetic C4. Carrier-
   level echo of Herm2 finding A: the pair, not the single slot, is the
   Galois-closed object.
5. The invariant Gram (Q7-Q9). H0 = sum g-dagger g over the 120 lift
   elements is sigma-Hermitian, invariant, totally positive definite,
   and the space of invariant Hermitian forms is EXACTLY 1-dimensional
   over F (rank-6 linear system on 8 rational parameters,
   machine-checked): the Gram of the common carrier is unique up to a
   positive F-scalar -- the audit's H0 uniqueness as a theorem-grade
   gate. By this uniqueness and the GL2(K) identification of
   C-COMMON-CARRIER-ICOSIAN-1 (gate L4), H0 is the canonical icosian
   CM-Hermitian form h up to positive scale: the audit's coordinate-free
   Gram and the icosian h are the same object.

## Status separation

candidate-T: all ten gates. [T, literature]: Noether-Deuring (equal
irreducible characters over K imply conjugacy). [D]: reading the
kernel/coset split as "the bit rides the branch exchange". [O]: the
remaining P-CM-2I-QCARRIER-1 obligations -- the explicit semilinear
order-4 operator on the pair carrier with its cocycle trivialization,
the frozen equivalence class list, and the orbit-to-amplitude bridge;
none of these is claimed here. QUADRATIC-DECODER-DATA and
COLOR-MEASURE-SELECTION remain untouched open rows.

## Falsifiers

- F-QC-1: any FAIL gate of verify_cm_2i_qcarrier.py.
- F-QC-2: an exact GL2(K)-conjugacy intertwining g -> tau(g) with
  markings intact (would collapse the descent dichotomy).
- F-QC-3: a second F-line of invariant Hermitian forms (would break
  the Gram uniqueness).

No falsifier fired. No threshold moved. PROMO deferred.
