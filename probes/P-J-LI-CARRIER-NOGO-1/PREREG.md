# P-J-LI-CARRIER-NOGO-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / PROOF-FIRST`

One unconditional theorem: the Li ladder admits no realization on a
finite-dimensional cyclic carrier. The theorem is carried by the written
proof below with three imports labeled; the verifier is a finite exact
audit of the mechanism on exemplars living inside the program's own field
Q(zeta_10) = Q(zeta_5), not a discovery engine. The result is exposed
before execution: every gate passes.

## Public identity, authority, and action layer

```text
probe:           P-J-LI-CARRIER-NOGO-1
public claim:    issue #447
probe owner:     A. M. Thorn / delegated session cleanup-batch-2026-08-20
branch:          probe/P-J-LI-CARRIER-NOGO-1
basis:           Public Canon v54, main 70e1c480, tag canon-v54,
                 SHA256SUMS 5 of 5 OK
action layer:    L1 (exact arithmetic; enrichment lane). No layer lift,
                 no physical claim, no canon edit by this probe.
lineage:         carries in the incubation promotion
                 PROMO-J-LI-CYCLIC-CARRIER-DIMENSION (2026-07-17); this
                 probe re-derives everything fresh with new files.
```

## Falsifier, first

A finite-dimensional cyclic unitary pair (U, v) with
||sum_(k<n) U^k v||^2 = lambda_n for every n >= 1 would refute the row.
The written proof excludes it unconditionally given the named imports; no
finite numerical cutoff can establish such a pair and none is used. The
operational falsifier for the probe is a pinned-gate FAIL on rerun.

## The six fields

```text
EQUATION     for every unitary U and vector v whose cyclic subspace is
             finite dimensional:
             q_n := ||sum_(k=0)^(n-1) U^k v||^2 = a* n^2 + R_n with
             a* = ||P_(z=1) v||^2 and 0 <= R_n <= C < infinity.
             Consequence: q_n = lambda_n for all n >= 1 is impossible;
             every exact realization of the Li ladder has an
             infinite-dimensional cyclic subspace, spectral measure with
             infinite support, 1 in the support, and no atom at 1.
CODE         probes/P-J-LI-CARRIER-NOGO-1/verify.py, stdlib only, exact
             Fraction arithmetic on polynomial vectors mod Phi_10, no
             float anywhere, deterministic, well under 120 s, run from
             repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
CARRIER      none external. The audited exemplars are exact: the
             one-dimensional carrier with eigenvalue zeta_10 (bounded
             10-periodic ladder, a* = 0, period maximum exactly
             6 + 2 sqrt5 = 4/|1 - zeta_10|^2, attained), the eigenvalue-1
             carrier (q_n = n^2, a* = 1), and their orthogonal sum
             (q_n = n^2 + bounded).
SYSTEMATICS  the universal statement is carried by the proof, not the
             exemplar sweep; the exemplars audit each mechanism the proof
             uses (orthogonal spectral split, periodic boundedness, the
             n^2 branch, the exact remainder bracket). Ramanujan c_10 is
             audited as the arithmetic anchor of the mu_10 exemplar.
THRESHOLD    any gate FAIL kills the probe. Exact equality only.
LAYER        L1. The proposed row is enrichment-lane mathematics; RH
             stays O and no live row moves.
```

## The written proof

Imports, named: (I1) Li's criterion in the Bombieri-Lagarias form: RH
holds if and only if lambda_n >= 0 for every n >= 1. (I2) The Lagarias
asymptotic: under RH, lambda_n = (n/2) log n + ((gamma - 1 - log 2pi)/2) n
+ O(sqrt(n) log n); in particular lambda_n is unbounded and o(n^2).
(I3) The spectral theorem for unitaries and orthogonality of eigenspaces
on a finite-dimensional space.

Dichotomy. Let the cyclic subspace of (U, v) be finite dimensional. By
(I3), v = sum_j v_j over finitely many orthogonal eigenvectors with unit
eigenvalues z_j. Then sum_(k<n) U^k v = n v_1 + b_n, where v_1 is the
z = 1 component and b_n = sum_(z_j != 1) v_j (z_j^n - 1)/(z_j - 1) is
orthogonal to v_1. Hence exactly

```text
q_n = a* n^2 + ||b_n||^2,   a* = ||v_1||^2,
0 <= ||b_n||^2 <= C := sum_(z_j != 1) 4 ||v_j||^2 / |1 - z_j|^2.
```

Exclusion. Suppose q_n = lambda_n for all n >= 1. Then lambda_n >= 0 for
every n, so RH holds by (I1), and (I2) applies: lambda_n is unbounded and
o(n^2). If a* = 0, q_n <= C is bounded, contradicting unboundedness. If
a* > 0, q_n / n^2 tends to a* > 0, contradicting o(n^2). Both branches
close; no finite-dimensional cyclic carrier exists.

Corollaries, same two facts. For any realization (finite or not) with
spectral measure mu_v: an atom at 1 gives q_n >= n^2 mu_v({1}),
contradicting o(n^2), so mu_v({1}) = 0. If 1 is outside the support,
q_n = integral |1 - z^n|^2 / |1 - z|^2 dmu_v <= 4 mu_v(T) /
dist(1, supp)^2 is bounded, contradicting unboundedness, so 1 lies in the
support. A finite support is a finite-dimensional cyclic subspace, so the
support is infinite.

## Proposed fold edits (a later sealed fold, not this probe)

Registry, one row (tab-separated; canon section 16, p = 5 and the wall):

```text
J-LI-CYCLIC-CARRIER-DIMENSION	T	every unitary (U,v) with finite-dimensional cyclic subspace has ||sum_(k<n) U^k v||^2 = a* n^2 + R_n with a* = ||P_(z=1) v||^2 and 0 <= R_n <= C; since the Li ladder is nonnegative-forcing (Li, Bombieri-Lagarias) and under RH unbounded and o(n^2) (Lagarias), no finite-dimensional cyclic carrier realizes it: every exact realization has infinite spectral support, 1 in the support, and no atom at 1; imports labeled	16. p = 5 and the wall	probes/P-J-LI-CARRIER-NOGO-1	a finite-dimensional cyclic (U,v) with q_n = lambda_n for all n, or an exact refutation of the dichotomy q_n = a* n^2 + O(1)
```

Frontier: no change (a T no-go; no live row moves). Ledger delta:
claims +1, T +1. The row complements the registered carrier no-gos
(J-LI-TORAL-HAAR-NOGO, J-LI-LAMBDA-HAAR-HS-NOGO, J-LI-LAMBDA-SHIFT-NOGO),
which exclude specific carriers; this row excludes every finite one.

## Non-claims

No advance on RH; RH stays O. The theorem narrows the realization space
(it forces infinite cyclic dimension and the support facts); it does not
enter the space, and it says nothing about the cocycle-vector form carried
by LAMBDA-COCYCLE-ANGLES [H] beyond consistency.
