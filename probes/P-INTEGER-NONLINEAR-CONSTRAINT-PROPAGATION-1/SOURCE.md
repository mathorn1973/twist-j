# Authority, mathematical provenance and declared choices

Status: NON-CANONICAL  
Action layer: L1  
Probe: P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1651  
Owner: A. M. Thorn, session antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3

## Normative authority actually inspected

STATUS.md was read before scientific work. Public Canon v103 is active.
Public main and the peeled canon-v103 tag both identify
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The declared content commit is
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66, an ancestor of this base. The
successful main architecture and aggregate checks are in run 39022927713;
the successful tag/release publication checks are in runs 39022952253 and
39033710211. These checks establish the authority context, not a result
for this new probe.

The actual five normative byte strings are checked by both new programs:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

POLICY.md SHA-256:
da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d.
AGENTS.md SHA-256:
7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1.
The existing public issue, PR, probe and registry inventory and the explicit
remote-head scan were checked before the ownership claim. The exact new
identifier had no collision.

The selected canonical mathematical inputs from
[canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md)
are:
1. `DEF-K1-LINEAR-METRIC` and `K1-LINEAR-METRIC-COMPLETION`: the five marked
   sites, ten canonical word shapes, their two initial slices, the rational
   operator L, the chosen real algebraic first derivative, the full quadratic
   metric action A_2, and the plus-TT metric representative.
2. `DEF-K1-HYBRID-FRW-CELL-METRIC` and `TT-ISOLATED-EMISSION-WORK-BALANCE`:
   the five-site planar incidence operator `B_5` on the ten oriented edges
   `E_5 = {(r, k) : r in Z/5, k in {1, 2}}`, edge weights `w_1 = 29/324` and
   `w_2 = 65/324`, exact factorization `L = B_5^T W_e B_5`, co-closed edge
   space `K_E = ker B_5^T`, endpoint-polarized TT vertex energy density
   `e_h` and edge current `j_h`, and the cubic constraint-coupling structure
   for the mean-zero lapse `ell_lapse`, scalar constraint potential `tau`,
   homogeneous lapse perturbation `ell_hom`, edge shift `N_shift`, and
   co-closed edge momentum `p`.

In Canon v103 those constraint couplings are formulated for the free K1 TT
field (or isolated two-step emission). Here they are extended to the
autonomous positive-kinetic reciprocally coupled TT-and-scalar-source
system with continuous backreaction at every step, and lifted to an exact
autonomous integer representation.

## Non-canonical companion evidence

1. [P-INTEGER-SOURCE-HOLONOMY-1, PR #1633](https://github.com/mathorn1973/twist-j/pull/1633),
   issue #1632, pin b3de2d7886a00bc7d6b2f5fe470516424be8b046, head
   1ffe24aab9f4bbe070dfbb23b914244c9b68aa02. Supplies the Hermitian
   commutator M(t), positive trace cost, and domain/bank reflection
   mechanism, restated here.
2. [P-INTEGER-PRIMITIVE-SOURCE-METRIC-1, PR #1641](https://github.com/mathorn1973/twist-j/pull/1641),
   issue #1640, pin 7ffee4939346221e2d43ed386f33bdfa47cd509f, head
   af88c702baf6c31bf4bb51c9768a07bc261c3dc6. Earlier one-way source/TT
   comparison.
3. [P-INTEGER-RECIPROCAL-SOURCE-ACTION-2, PR #1644](https://github.com/mathorn1973/twist-j/pull/1644),
   issue #1642, pin 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7, post-review
   disposition head f0e3a2e460668b03e53400bfc81ae5d78cb53399, reviewed in
   [6267871040](https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6267871040),
   [6270220560](https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6270220560),
   and [6272358961](https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6272358961).
4. [P-INTEGER-JOINT-VARIATION-1, PR #1646](https://github.com/mathorn1973/twist-j/pull/1646),
   issue #1645, pin fe5456f1aac8adcc3fdb0222df81f7e2fc773977, head
   d4a707bd1ecab7d839e2d32371aed7bde6885f31.
5. [P-INTEGER-POSITIVE-KINETIC-JOINT-1, PR #1648](https://github.com/mathorn1973/twist-j/pull/1648),
   issue #1647, pin bd7e1dada3a4869ecfae76c0aea03c0a88c9983f, post-review
   disposition head a934c57db29507d7885e3886bcbfe854ce531bd2, reviewed in
   [6270208985](https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6270208985)
   and [6272438292](https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6272438292).
6. [P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1, PR #1650](https://github.com/mathorn1973/twist-j/pull/1650),
   issue #1649, pin edfedd7e75c515d6d318032f526f381f66317da3, head
   a17fe5f2198f1693277b45bcf7c55458e8c2c381. Independently replayed and
   reviewed in [6272491077](https://github.com/mathorn1973/twist-j/pull/1650#issuecomment-6272491077).
   Supplies the autonomous constant-coupling joint equations, positive
   interaction-inclusive bond energy Htot_n around the coupled equilibrium,
   symplectic physical map, 21-coordinate integer core (Z,R,D,H), and
   attenuated prepared family. Its open gravitational obligation—adding the
   first nonlinear (cubic) constraint-coupled action terms and proving
   Hamiltonian and momentum constraint propagation—is the exact subject of
   this successor probe.

There are no runtime imports from companion probe directories. All necessary
mathematics and algorithms are restated in this prospective bundle.

## Explicit new choices and exact scope

| Item | Origin and precise interpretation |
| --- | --- |
| Planar incidence B_5, edge weights W_e, L = B_5^T W_e B_5 | Canonical five-site planar restriction from DEF-K1-HYBRID-FRW-CELL-METRIC and TT-ISOLATED-EMISSION-WORK-BALANCE |
| Autonomous coupled (h, chi) law with g=1/324, A_src=a/4 | Inherited from P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1 (#1650) |
| Dipole vertex support sigma = (1/2, 1/2, 0, 0, 0) | NEW_DECLARED symmetric localization of the scalar source bond energy on the two dipole endpoints r=0,1 |
| Local interaction density e_int,n(r) and dipole current j_int,n(e) | NEW_DECLARED vertex/edge resolution of the reciprocal dipole coupling; j_int,n is supported on e_0=(0,1) |
| Exact off-shell local divergence identity | Exact algebraic consequence on (Q^5 x Q)^3 without continuum or statistical approximation |
| Cubic constraint-coupled action A_constr | NEW_DECLARED extension of A_auto coupling ell_hom,n, ell_lapse,n, N_shift,n to Htot_n, e_tot,n, j_tot,n and auxiliary (tau_n, p_n) |
| 48-coordinate two-bond local cubic action A_cubic,loc | Exact finite-support local action verified by central unit differences both on-shell/on-gauge and off-shell/off-gauge |
| Circulant Green identity L_int L_adj = 53605 Pi_0 | Exact algebraic inverse of 324 L on e^perp without numerical linear solving |
| Discrete Bianchi / co-closure identity B_5^T p_n = 0 | Exact on-shell propagation of the Hamiltonian constraint between adjacent bonds |
| Integer constraint lift (E_int, Theta, J_int, Pi_int) | NEW_DECLARED autonomous integer lift of local energy density, scalar constraint potential, edge current, and co-closed momentum on the unrestricted integer carrier |

This probe establishes the first nonlinear (cubic) constraint-coupling
correction and exact discrete constraint propagation for the autonomous
coupled integer metric-and-source model on the five-site planar ring. Full
non-perturbative 4D Einstein equations, three-dimensional 125-site spatial
coupling of the active source, derivation of the coupling from native U,
continuum manifold limits, and physical SI calibration remain open.

## Implementation independence and custody

The primary (`verify.py`) uses the autonomous integer recurrence, polynomial
quotient ring `Z[j]`, 2x2 Hermitian matrices, the closed-form circulant
operator `L_adj` for `Theta_n` and `tau_n`, and direct integer/rational
evaluation of the 48-coordinate cubic local action.

The secondary (`breaker.py`) is written separately from `PREREG.md`. It
evolves the rational physical slices, reconstructs the integer core, uses
direct 8-coordinate Hermitian transformations, solves the Hamiltonian
constraint `2 L tau_n = Pi_0 e_tot,n` on `e^perp` by explicit rational
Gaussian elimination on the 4x4 Gram matrix of `L` (checking agreement with
the integer lift), and independently evaluates all local continuity,
Bianchi, and 48-coordinate cubic action checks.

Before any execution or import of `verify.py` or `breaker.py`, all six
frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`,
`breaker.py`, `FROZEN.sha256`) are committed, pushed to the branch, read
back from GitHub, and recorded in the prospective pin receipt on issue #1651.
