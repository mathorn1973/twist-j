# Analytical and static review receipt

Status: NON-CANONICAL, L1 review context  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-2  
Pin: 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7

This receipt describes analytical and static verification performed before the
first formal execution of P-INTEGER-RECIPROCAL-SOURCE-ACTION-2. A later public
reviewer can inspect the immutable pin, proofs, code, and exact run record
without relying on these statements.

## Predecessor pin disclosure

An earlier probe directory P-INTEGER-RECIPROCAL-SOURCE-ACTION-1 was pinned on
issue #1642 at commit a369fbf85feb79a2a10716b8bd7efd9ff8da5814 and failed its
first formal execution with FALSIFIER=INITIAL_DATA because the literal beta(w)
table had 0 instead of +1 for word 0100 and 0 instead of -1 for word 1101. In
accordance with POLICY.md Section 3, P-INTEGER-RECIPROCAL-SOURCE-ACTION-1 was
preserved and closed as Status: FAIL on its own branch and Draft PR #1643.
P-INTEGER-RECIPROCAL-SOURCE-ACTION-2 was then created as a new probe directory
with corrected literal beta(w) values and re-pinned prospectively before any
scientific execution.

## Separation of implementation encodings

- verify.py implements the 8-coordinate integer realization of Herm_2(Z[j]),
  direct block-matrix evaluation of L, and rational arithmetic via Python
  fractions.Fraction.
- breaker.py implements an independent polynomial-ring quotient module Z[j]
  with explicit 2x2 Hermitian matrix multiplication, independent finite-difference
  stencil evaluation on Z_5, and independent linear-system Green inversions via
  rational Gaussian elimination.

## Pre-pin static audit

Before committing and pushing pin 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7:

- Every literal initial slice and beta(w) entry in PREREG.md, verify.py, and
  breaker.py was checked statically via AST against the canonical bit formula
  and the parity-dipole functional.
- All five theorems B1-B5 in PROOF.md were checked analytically, including the
  representation decomposition of Herm_2(Z[j]) under Ad_{M_0}, the exact
  commutation of phase-6 backreaction with the inverse step, the mod-2 and
  mod-3 primitive denominator invariants under arbitrary integer forcing, the
  zero-sum norm bound for |chi_n|<=4, and the joint stationarity equations.
- Both Python files were checked with ast.parse without importing or executing
  scientific code before the pin was pushed and read back from GitHub.
