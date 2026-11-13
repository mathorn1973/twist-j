# Authority, provenance and choice manifest

Status: NON-CANONICAL  
Action layer: L1  
Probe: P-INTEGER-POSITIVE-KINETIC-JOINT-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1647

## Actual normative input

STATUS.md was read before scientific work. Public Canon v103 is active; main and
peeled canon-v103 identify dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. Its
declared content commit is 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66, an ancestor
of the base.

Both implementations verify the following actual local bytes at runtime:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

POLICY.md has SHA-256
da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d;
AGENTS.md has SHA-256
7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1.

The canonical source is DEF-K1-LINEAR-METRIC and K1-LINEAR-METRIC-COMPLETION in
canon/CANON.md: the ten words, two initial slices, rational circulant L, marked
plus-TT metric, full quadratic metric action A_2, and free all-counter interval
-59/100<h<99/100.

## Non-canonical mathematical companions

1. P-INTEGER-SOURCE-HOLONOMY-1 (#1633, issue #1632, pin b3de2d78, head 1ffe24aa):
   supplies the commutator M(t)=A B(t) A^(-1) B(-t), the Hermitian trace cost,
   and the reversible admission account mechanism.
2. P-INTEGER-PRIMITIVE-SOURCE-METRIC-1 (#1641, issue #1640, pin 7ffee493, head
   af88c702): supplies the one-way source-to-TT comparison and prescribed-source
   metric variation.
3. P-INTEGER-RECIPROCAL-SOURCE-ACTION-2 (#1644, issue #1642, pin 3ae3ea66, head
   561216f3): supplies the one-time parity-impulse and coordinatewise integer
   optimality precursor.
4. P-INTEGER-JOINT-VARIATION-1 (#1646, issue #1645, pin fe5456f1, head
   d4a707bd): supplies the 21/23-coordinate integer carrier with common scale
   D_n=2*m^(n(n-1)/2) and continuous joint variation with a negative relative
   source kinetic sign. Its explicit open obligation regarding the negative
   source kinetic sign and action-derived physical Hamiltonian motivates this
   probe.

All companion branches and frozen results remain untouched. There are no
foreign-probe runtime dependencies.

## Declared choices and earned scope

| Choice | Origin and precise scope |
| --- | --- |
| Five marked sites, ten word pairs, L, free A_2 and plus-TT reading | Selected canonical L1 comparison inputs |
| Positive-kinetic scalar source action +(1/2)(Delta chi_n)^2 - (chi_n^2/2 - a chi_n) | NEW_DECLARED positive-kinetic discrete Klein-Gordon source action matching the TT metric kinetic sign |
| Coupled equations (Delta_c^2+L)h_n = chi_n ell/m^n and (Delta_c^2+1)chi_n = a + <ell,h_n>/m^n | Derived by simultaneous continuous variation of A_pos with respect to all metric, lapse, shift, and source variables |
| Action-derived positive-definite physical Hamiltonian H_phys,n = H_h,n + H_chi,n | Derived from the second-order discrete Lagrangian of A_pos on e^perp x R; strictly positive-definite and obeys the exact discrete Noether work identity |
| Positive-signature canonical symplectic Wronskian Omega_n^+ = Omega_h,n + Omega_chi,n | Exact conserved bilinear invariant across all homogeneous coupled trajectories |
| Common scale D_n=2*m^(n(n-1)/2), 21-coordinate core, 6-congruence partial inverse, and 23-coordinate funded carrier | Exact algebraic integer lift and reversible admission account |
| Hermitian register H transported by M(Y'-Y) | Invertible cyclotomic amplitude realization/monitor |

While H_phys,n is a strictly positive-definite quadratic Hamiltonian derived
from the joint action and Omega_n^+ is an exactly conserved positive-signature
symplectic form, the integer admission account E(x)+b remains a separate
arithmetic storage/admission budget rather than H_phys,n itself. Full nonlinear
Einstein dynamics, a 3+1 covariant stress-energy tensor derived from native
TWIST-J U, primitive-denominator optimality for D_n, and a continuum manifold
limit remain separate open obligations.

## Implementation independence

- verify.py uses the scaled integer recurrence and 6-congruence inverse,
  polynomial quotient arithmetic in Z[j], 2x2 Hermitian matrix conjugation, and
  direct operator evaluation of the local action, physical Hamiltonian, and
  symplectic Wronskian.
- breaker.py independently advances rational Fraction fields and sources, checks
  backward integrality without the primary's congruence formula, uses direct
  8-coordinate Hermitian gates and edge-square potential expansions, and
  computes the physical Hamiltonian and symplectic form from independent
  bond-variable definitions.
