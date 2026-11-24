# A finite rotor clock for repeated local Dirac steps

**NON-CANONICAL, L1. Conditional analytical candidate-T; independent
mathematical acceptance pending.** Author: A. M. Thorn. Apache-2.0.

Public reservation: [#1794](https://github.com/mathorn1973/twist-j/issues/1794).

## Purpose and frozen scope

This note gives a constructive finite-clock approximation to repeated
execution of the nominated four-channel walk with contact,
`V = C_g U`, on the unchanged infinite spatial lattice. For every prescribed
finite integer horizon `N >= 1` and tolerance `epsilon > 0`, it specifies one
finite clock, one ready clock vector, and one positive bounded static
Hamiltonian. The Hamiltonian couples only equal or neighboring system
positions. At every tick `n tau`, `0 <= n <= N`, the complete clock/system
output is within `epsilon` of the same ready clock vector tensored with
`V^n psi`, up to the stated input-independent scalar phase.

The bound is an operator-norm estimate on input isometries. It is uniform
over all system inputs on the infinite lattice, both internal regimes,
and arbitrary passive references. No fixed spatial source, finite spatial
box, successful measurement outcome, or postselection is assumed.

The proof is self-contained in [PROOF.md](PROOF.md). It defines the walk,
the pulse generators, the intermediate circle clock, the positive rotor,
the finite Fourier compression, the resource choices, and the actual
finite-carrier energy bounds. The continuous rotor is a comparison device
in the proof; the final model uses only the displayed finite clock matrices.
The abbreviation `H_M` below denotes `H_{Lambda,M}` in that proof.

## Main statement

For fixed `g in R` and `tau > 0`, and each `N, epsilon` as above, the
construction supplies a finite dimension `d_C = 2M+1`, a normalized vector
`f_M`, and a Hamiltonian `H_M` on

```text
C^(2M+1) tensor ell^2(Z) tensor C^2_dir tensor C^2_port
```

such that `0 <= H_M <= B_M I`, its system spatial range is at most one,
and, with `J_M psi = f_M tensor psi`,

```text
|| exp(-i n tau H_M) J_M
   - exp[-i n tau (Lambda/2+h)] J_M V^n || < epsilon
                         for every integer 0 <= n <= N.
```

The parameters are selected once before evolution. The construction does
not reset or replace the clock between ticks. This is the quantifier order
`for every N, epsilon there exists one apparatus for all n <= N`, not one
fixed finite apparatus with arbitrarily accurate operation for all time.

## What is counted and what is not claimed

- The clock has exactly `2M+1` admitted levels, including all raw states of
  that finite register. The system lattice remains infinite.
- The pulse program, exact coefficients, ready vector, energy scale,
  Fourier cutoff, and time unit are supplied resources. Their native
  preparation or selection is not derived.
- Spatial range refers to the original system position. The finite clock
  matrices need not be nearest-neighbor in their Fourier-mode labels.
- Clock return and implementation of `V^n` have the displayed nonzero
  error. Exact reusable finite-clock implementation is not asserted.
- The finite ready vector has tails outside the ideal idle interval. Its
  mean energy need not equal the comparison rotor's input-independent
  energy. The proof gives separate uniform bounds for the finite model.
- The conserved energy is `H_M` itself. It is not identified with the
  earlier sine-energy account `H_sin + H_B`, a unique physical energy
  reading, or a photon/electron identification.
- Finite Hamiltonian range is not an assertion of an exact continuous-time
  light cone. No many-body locality, spin, charge, or statistics theorem is
  supplied.

## Proof obligations and falsifiers

The candidate fails within its frozen scope if any of the following occurs:

1. The stated local pulse product differs from the nominated full `V`,
   including its scalar phase or either internal sector.
2. The circle-clock monodromy or ready-subspace identity fails, or an
   operator-domain step requires stronger regularity than is supplied.
3. The rotor comparison bound has an uncounted dependence on the system
   input, reference, spatial extent, or number of elapsed periods.
4. The positive compression fails to preserve boundedness or system
   spatial range one, or the omitted Fourier modes create an additional
   coupling not included in the cutoff estimate.
5. The normalization and resource inequalities fail to imply the full
   joint-state bound for even one admitted input and tick.
6. A claimed finite ready-state energy or variance bound fails after
   accounting for its nonzero initial interaction tails.

Independent review should check these six points against the exact proof
revision. A numerical finite-box example would not establish the universal
infinite-lattice claim.

## Provenance and authority

The publication base is public `main` at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, ACTIVE Public Canon v105.
Its declared content commit is
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`; the declared Canon SHA-256 is
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`
and its size is 1295029 bytes. These are authority pins, not evidence that
this new note is canonical.

Relevant predecessors are credited with their original scope:

- [Public Canon at the base commit](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md)
  contains the established walk and selected spectral-energy work.
- [#1779, COMPACT_MODEL.md, section 4](https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md)
  already gives a positive finite autonomous history-clock construction.
- [#1768, FINITE_MODEL.md](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/FINITE_MODEL.md)
  gives a finite compression for a fixed spatial source and one specified
  complete source word. Its source contract differs from the uniform
  repeated-walk contract proved here.

The two note predecessors remain NON-CANONICAL / L1. General positive
autonomous clocks and finite compression are not claimed as new. The
specific contribution proposed here is the finite Fourier-clock
construction and its uniform repeated-step, locality, normalization, and
resource estimates. No global novelty claim is made.

## Validation and publication boundary

This is a proof-only note. No new scientific executable, numerical
experiment, formal computation gate, or claimed independent reproduction
is included. Preparation and same-session adversarial review do not confer
independent theorem acceptance. Repository policy/CI checks are separate
from mathematical acceptance.

The pull request is a draft for review. It changes only this note package;
it does not modify the Canon, registry, frontier, workflows, or an existing
probe, and it does not grant a new canonical status.
