# PREREG DRAFT for public probe P-CM-2I-QCARRIER-1

NON-CANONICAL DRAFT. This is a proposal for a future formal public
probe under POLICY section 3; it is NOT a preregistration pin. A formal
probe would create branch probe/P-CM-2I-QCARRIER-1 and directory
probes/P-CM-2I-QCARRIER-1/ with a fresh PREREG.md and verify.py,
committed and pushed before any formal gate execution. Incubation
provenance: notes/C-CM-2I-QCARRIER-1 (10 gates) and
notes/C-CM-2I-QCARRIER-2 (11 gates), both single-leg x86_64.

## 1. Equation (claim set to be frozen)

On the frozen tuple (O_K^2, S, T, A_J, H0, Q) with K = Q(zeta5),
G = <S, T> the registered integral 2I lift, A_J = diag(J, 1),
H0 = sum g-dagger g, and equivalence = GL2(K)-conjugacy with markings
(trace-preserving on labeled elements):

- E1 (descent): the subgroup of Gal(K/Q) = C4 descending to the single
  marked lift is exactly ker chi5; the nontrivial coset descends only
  through the outer 5a <-> 5b swap.
- E2 (pair closure): the branch pair 2a (+) 2b is C4-stable with
  Q-valued character.
- E3 (cocycle): every G-equivariant tau-semilinear operator on the
  pair has the antidiagonal Schur form; its cocycle scalar is
  mu = -phi^2 up to N_{K/F}(K^x), totally negative; the minimal
  closure is nu^4 = -1, nu^8 = 1 (order eight), never order four.
- E4 (Gram): the invariant sigma-Hermitian form is a single F-line,
  totally positive definite; nu is a semilinear similitude with
  totally positive multipliers.

Decision structure (replacing the plain UNIQUE/NONUNIQUE/EMPTY
trichotomy, which the incubation slices showed is not the right
partition): the probe closes positively when E1-E4 are reproved by the
pinned two-architecture verifier; it closes negatively if any of the
named falsifiers fires (an order-4 equivariant semilinear structure;
a marked trace-preserving tau-conjugacy; a second invariant Gram line;
an equivariant semilinear map outside the Schur ansatz); it is STOP
while the equivalence, markings, or carrier tuple are not frozen
publicly.

## 2. Code

A fresh verify.py rederiving, in exact stdlib arithmetic with no
randomness: the 120-element closure, the descent class-function facts,
the intertwiner line, mu = -phi^2 with total negativity, the norm
equation decision, the explicit nu with nu^4 = -1 and nu^8 = 1,
equivariance, branch swap, and the Gram transport. Gate count and
hashes pinned at probe creation; the incubation verifiers are
provenance, not the pin.

## 3. Carrier / data

Exact synthetic objects only (Z[zeta5] matrices); no external data, no
floats, no sampling. Coefficient ring Z[zeta5]; carrier O_K^2 (+)
O_K^2; markings: T in class 5a, S the geometric quarter-turn.

## 4. Systematics

Deterministic picks frozen in the verifier: primitive integral C from
the reduced nullspace with fixed free-column convention; d the smallest
solution of N(d) = phi^2 in the fixed box; the exhaustive box |c_i| <= 3
for the unsolvability audit (the proof is total positivity, the box is
an independent audit).

## 5. Failure threshold

Exit 0, empty stderr, stdout byte-identical to EXPECTED.txt on both
required architectures; any FAIL line fires the named falsifier. No
numeric tolerances exist.

## 6. Action layer

L4 support-level structure (carrier, group actions, semilinear
descent, invariant form). No L5 stream, no L6 measure, no lift between
layers. The orbit-to-amplitude bridge and MatterData writing belong to
QUADRATIC-DECODER-DATA and are expressly out of scope.
