# Route RA literature audit: what the standard relative models actually give

```text
STATUS:     RECON support note. NON-CANONICAL.
PURPOSE:    type-check possible imports; not a construction and not evidence.
```

## Mayer/Ruelle transfer operators

Mayer's Gauss-map operator is a parameter-dependent nuclear operator and
gives the Selberg zeta of `PSL_2(Z)` through

```text
Z_PSL2Z(s) = det(1-L_s) det(1+L_s) = det(1-L_s^2).
```

It does not give one fixed positive self-adjoint `A_J`.  Riemann zeros enter
the Selberg divisor through the scattering sector; the attribution to one
individual factor was conjectural in the original source.

Primary sources:

- D. Mayer, *The thermodynamic formalism approach to Selberg's zeta function
  for PSL(2,Z)*, Bull. AMS 25 (1991), 55-60,
  <https://doi.org/10.1090/S0273-0979-1991-16023-4>.
- D. Ruelle, *Zeta-Functions for Expanding Maps and Anosov Flows*, Invent.
  Math. 34 (1976), 231-242,
  <https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B45%5D.pdf>.

## Modular scattering and Lax-Phillips

For the modular surface the one-cusp scattering coefficient is

```text
phi(s) = Lambda(2s-1)/Lambda(2s).
```

Here the convention is

```text
Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s).
```

This is a genuine quotient architecture.  The scattering matrix is unitary
on the critical axis, while its Lax-Phillips generator is non-self-adjoint.
Friedman-Jorgenson-Smajlovic define superzeta-regularized determinants of
`zI-(I/2 +- B)`; these are not ordinary `det_1(I+K)` determinants of a
positive trace-class operator.  Uetake's reduced model uses the completed
zeta/scattering multiplier in its definition, so transplanting it would
violate `G7`.

Primary sources:

- Y. Uetake, *The Lax-Phillips infinitesimal generator and the scattering
  matrix for automorphic functions*, Ann. Polon. Math. 92 (2007), 99-122,
  <https://doi.org/10.4064/ap92-2-1>.
- J. S. Friedman, J. Jorgenson, L. Smajlovic, *The determinant of the
  Lax-Phillips scattering operator*, <https://arxiv.org/abs/1603.07613>.
- W. Mueller, *Relative zeta functions, relative determinants and scattering
  theory*, Comm. Math. Phys. 192 (1998), 309-347,
  <https://doi.org/10.1007/s002200050301>.

## Bost-Connes and adelic trace formulae

The Bost-Connes Hamiltonian satisfies

```text
Tr(exp(-beta H)) = zeta(beta),       beta > 1,
```

where the Gibbs trace is finite in the displayed range.  This is a partition
trace, not the required Xi Fredholm determinant.  It also imports the full
multiplicative semigroup and cyclotomic tower.  The Connes adelic model
realizes zeros through an absorption-spectrum trace formula, not through a
positive trace-class Fredholm determinant; its global trace-formula wall is
itself RH-hard.

Primary sources:

- J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase
  transitions with spontaneous symmetry breaking in number theory*, Selecta
  Math. 1 (1995), 411-457,
  <https://doi.org/10.1007/BF01589495>.
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*, Selecta Math. 5 (1999), 29-106,
  <https://doi.org/10.1007/s000290050042>.

## Audit verdict

None of these models supplies a `J`-only positive trace-class `A_J`.  They
remain blueprints for domain, background subtraction, scattering, and
regularization.  Importing their modular, adelic, prime, Gamma, or spectral
data as carrier definitions would hide the terminal dependency wall in
`G0/G7`.
