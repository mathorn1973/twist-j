# SEMILOCAL IMPEDANCE LIMIT: TWO NO-GOS

```text
STATUS: NON-CANONICAL candidate-T bounded shortcut no-gos
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Target being tested

`XI-CAYLEY-HARDY-DEFECT.md` rewrites the global Suzuki/de Branges phase as

```text
Theta_xi=(1-ell)/(1+ell),
ell(s)=xi'(s)/xi(s).
```

A tempting construction is to approximate the target impedance `ell` by the
finite Euler/local-factor logarithmic derivatives whose lossless scattering
ratios have already been factorized in this incubation.

The naive construction fails before the RH wall.

## 2. Pointwise finite-Euler impedance diverges in the critical half-strip

For a rational prime

```text
gamma_p(s)=(1-p^(-s))^(-1),
ell_p(s)=gamma_p'(s)/gamma_p(s)
        =-(log p)p^(-s)/(1-p^(-s)).
```

Fix a real

```text
1/2 < sigma < 1.
```

Then every finite-prime contribution is strictly negative:

```text
ell_p(sigma)<0.
```

Moreover

```text
-ell_p(sigma)
 >= (log p) p^(-sigma).
```

The sum

```text
sum_p (log p) p^(-sigma)
```

diverges for `sigma<=1` (equivalently, the logarithmic derivative of the Euler
product has abscissa of convergence `1`; this follows for example from the
standard Chebyshev prime-counting bounds by partial summation).

Hence, for any fixed real `1/2<sigma<1`,

```text
sum_(p<=X) ell_p(sigma) -> -infinity.
```

The archimedean and polar logarithmic derivatives are fixed functions of
`sigma` and cannot cancel an `X`-dependent divergence.

Therefore the prime-ordered raw finite-Euler impedance already fails to
converge on the real segment `1/2<sigma<1`; in particular it cannot converge
pointwise throughout the half-strip where the target positive-real property
would have to be proved.

**Status:** candidate-T exact no-go for the explicitly stated raw
`POINTWISE-EULER-IMPEDANCE-LIMIT` shortcut. This post-prereg label is not a
public `F` claim.

Analytic continuation / renormalization is not a technical afterthought here;
it is the missing global operation.

## 3. Direct space-identification shortcut is also unavailable

Connes--Consani prove that the semi-local Sonin spaces

```text
S(u(F))=ker u(F)_22
```

form a filtering inductive system under the specified injective multiplier
maps

```text
D(F,F')=product_(p in F'\F)(1-p^(-s)).
```

This is an exact and useful comparison system; the spaces are not being
asserted to be literal nested subspaces or the maps to intertwine every Hardy
off-diagonal block.

However Suzuki explicitly notes in the 2025 paper `On the Hilbert space derived
from the Weil distribution` that the particular de Branges spaces arising in
the Connes--Consani--Moscovici construction and his `H(E_xi)` have different
generators and different spectral properties and are not isomorphic in that
source-typed sense. This rules out the literal generator- and
spectrum-preserving declaration

```text
source CCM B_lambda^S = Suzuki H(E_xi)
```

as the missing argument. It does **not** rule out an abstract Hilbert-space
isometry, a nontrivial inductive-limit intertwiner, compression, quotient, or
defect relation involving Suzuki's unconditional `K_0`.

**Status:** candidate-T source-bounded no-go for the literal
generator-/spectrum-preserving `CCM-B-TO-H(E_XI)` identification. This overlaps
the earlier direct-isometry boundary in `SONIN-INTERTWINER-AUDIT.md`; it is not
counted as an independent no-go for every Sonin limit.

## 4. Why the two failures point to the same missing operation

The finite local ratios

```text
u(F)=rho_inf product_(p in F)rho_p
```

are well-defined unitary boundary functions and are quasi-inner; their Sonin
spaces form an inductive system. The **half Euler products** whose logarithmic
derivatives would approximate `xi'/xi` do not converge in the critical
half-strip.

Thus one stable alternative to the failed raw pointwise limit is the
operator/space filtration built from the reflected local ratios. It is the
product `u(F)`, not an individual `rho_p`, that has the cited quasi-inner
property; the relevant off-diagonal Hardy defects are compact in their source
orientation.

The global target `Theta_xi`, in contrast, is already an unconditional
unimodular boundary function; RH is precisely the statement that its Hardy
escape defect vanishes.

This suggests one deferred question within this impedance shortcut:

```text
Can the Hardy escape defect H_(Theta_xi)
be obtained as a rigorously renormalized operator limit / compression defect
of the finite semilocal quasi-inner systems u(F),
without first assuming that the limit is inner?
```

The desired outcome would not be an equality of the underlying Hilbert spaces.
It would be an exact defect/intertwining identity.

## 5. Deferred RENORMALIZED-HANKEL-LIMIT comparison (not a gate)

Frozen G3 remains UNDECIDED, so G4 and G6 are blocked. No new #357 gate is
opened or executed here. A later separately locked construction would have to
specify:

```text
finite place filtration F_1 subset F_2 subset ...,
intertwining maps between the finite Hardy/Sonin carriers,
normalization or subtraction dictated before taking the limit,
operator topology,
common dense domain if unbounded generators occur,
and the exact target map to H_(Theta_xi).
```

It must also type the orientation before any equality is meaningful:

```text
Connes--Consani Sonin kernel: 22 block
  (1-P_-) M_(u(F)) (1-P_-),
quasi-inner defect: 21 block
  (1-P_-) M_(u(F)) P_-,
Suzuki target in the companion note:
  (1-P_+) M_(Theta_xi) P_+.
```

The reflection/conjugation unitary implementing the `s`- to `z`-coordinate
change, the choice among `u,u^*,rho` and reflected multipliers, and the exact
block/topology/domain must be frozen. The Sonin comparison maps alone do not
prove that the 21 blocks intertwine.

Positive outcome:

```text
renormalized defect limit = H_(Theta_xi)
```

with every finite object built only from local factors and source cutoff
geometry.

This identity alone would not prove RH. The further proof that the limit
vanishes must come from an independent structural reason.

Falsifiers:

1. the normalization is chosen after comparison with `Theta_xi`;
2. the limit exists only for `Re s>1`;
3. compactness of finite defects is promoted to norm convergence to zero;
4. the Sonin inductive maps fail to intertwine the proposed defects;
5. the target is reached only by an assumed de Branges-space isomorphism;
6. the construction imports RH, real zero locations, Weil positivity, or
   innerness of `Theta_xi`.

## 6. Current bounded ruling

```text
raw POINTWISE-EULER shortcut              candidate-T no-go
literal CCM-B-TO-H(E_XI) identification   candidate-T bounded no-go
RENORMALIZED-HANKEL-LIMIT comparison       deferred; not a gate
```

The first result strengthens the placewise sign obstruction in
`XI-CAYLEY-HARDY-DEFECT.md`; the second overlaps existing direct-isometry and
quasi-inner boundaries. This is a narrowing of named shortcuts, not an RH or
G3 result.
