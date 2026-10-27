# A three-channel bound and resonant node

**NON-CANONICAL / L1 / conditional analytical candidate-T.**

Author: A. M. Thorn. License: Apache-2.0.

This proof-only candidate supplies one positive bounded graph-local
Hamiltonian with integer matrix entries. Two compact core states have
energy 1. A higher symmetric core excitation couples to a genuine spatial
continuum, has a precisely located continued-resolvent pole and escapes
with a controlled survival estimate. It is a declared construction, not
a physical proton/neutron identification or a derivation from native U.

The family, with integer K>=2, is

    H_c=I+K J3,
    H_l=(1+3K)I-K(S+S*),
    coupling=|u><0|+|0><u|,  u=(1,1,1).

The core is C^3 and the lead is ell^2(N_0). The full law has spatial range
one with the three core channels placed in one cell. It satisfies H>=I.

The complete point spectrum is energy 1 with multiplicity two. The bright
sector is purely absolutely continuous on [1+K,1+5K]. Its lower continued
pole and width are

    z_*=1+3K-3i/sqrt(K^2-3),
    Gamma_K=6/sqrt(K^2-3).

For an initially normalized bright core state b and its survival amplitude
A_K(t), the proof establishes, uniformly for all real t,

    ||A_K(t)|^2-exp(-Gamma_K|t|)|
      <=4(K/sqrt(K^2-3)-1) <=16/K^2.

This is an absolute approximation, not exact exponential decay or relative
control of the late tail. Exactly, |A_K(t)| tends to zero and the lead
probability tends to one. The dark core is never populated by this bright
initial state, so this carrier does not yet describe a residual bound object
plus emitted particles.

K=4 is a fixed algebraic illustration: the two bound energies are 1, the
continuum is [5,21], and the pole is 13-3i/sqrt(13), with residue 29/26.
K was not selected from measured particle data. Different K change the law.

## Files and review

- [PROOF.md](PROOF.md): self-contained model, spectral measure, pole,
  survival bound, current and scope.
- [PREREG.md](PREREG.md): reserved scope and exposed preparation.
- [PROMO.md](PROMO.md): proposed mathematical claims and exclusions.

Owner issue: [#1797](https://github.com/mathorn1973/twist-j/issues/1797).
Public basis: Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`.

No scientific executable or numerical computation is used. The analytical
review was nonblind and within the author session; external independent
mathematical acceptance remains pending. No Canon, registry, frontier,
formal probe, activation or release is changed.
