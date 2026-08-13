# SEMILOCAL IMPEDANCE LIMIT: TWO NO-GOS

```text
STATUS: NON-CANONICAL incubation negative result
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

Hence, for any fixed `1/2<sigma<1`,

```text
sum_(p<=X) ell_p(sigma) -> -infinity.
```

The archimedean and polar logarithmic derivatives are fixed functions of
`sigma` and cannot cancel an `X`-dependent divergence.

Therefore the raw finite-Euler impedance cannot converge pointwise to
`xi'/xi` in the half-strip where the target positive-real property would have
to be proved.

**Status:** exact F for `POINTWISE-EULER-IMPEDANCE-LIMIT`.

Analytic continuation / renormalization is not a technical afterthought here;
it is the missing global operation.

## 3. Direct space-identification shortcut is also unavailable

Connes--Consani prove that the semi-local Sonin spaces

```text
S(u(F))=ker u(F)_22
```

form a filtering inductive system under multiplication by

```text
D(F,F')=product_(p in F'\F)(1-p^(-s)).
```

This is an exact and useful nested structure.

However Suzuki explicitly notes in the 2025 paper `On the Hilbert space derived
from the Weil distribution` that the de Branges spaces arising in the
Connes--Consani--Moscovici construction and his `H(E_xi)` have different
generators and different spectral properties and are not isomorphic.
Under RH, Suzuki's unconditional `K_0` identifies with `K(Theta_xi)`, so a
simple declaration

```text
inductive limit of semilocal Sonin spaces = Suzuki K_0
```

cannot be the missing argument.

**Status:** F for `DIRECT-SONIN-LIMIT-IDENTIFICATION` at the claimed isometric
space-identification scope. This does not exclude a nontrivial intertwiner,
compression, quotient, or defect relation.

## 4. Why the two failures point to the same missing operation

The finite local ratios

```text
u(F)=rho_inf product_(p in F)rho_p
```

are well-defined unitary boundary functions and are quasi-inner; their Sonin
spaces form an inductive system. The **half Euler products** whose logarithmic
derivatives would approximate `xi'/xi` do not converge in the critical
half-strip.

Thus the stable object is not a pointwise Euler-product limit. It is the
operator/space filtration built from the reflected local ratios and their
compact Hardy defects.

The global target `Theta_xi`, in contrast, is already an unconditional
unimodular boundary function; RH is precisely the statement that its Hardy
escape defect vanishes.

This suggests the only non-circular limit question left by the present route:

```text
Can the Hardy escape defect H_(Theta_xi)
be obtained as a rigorously renormalized operator limit / compression defect
of the finite semilocal quasi-inner systems u(F),
without first assuming that the limit is inner?
```

The desired outcome would not be an equality of the underlying Hilbert spaces.
It would be an exact defect/intertwining identity.

## 5. New gate: RENORMALIZED-HANKEL-LIMIT

A viable construction must specify:

```text
finite place filtration F_1 subset F_2 subset ...,
intertwining maps between the finite Hardy/Sonin carriers,
normalization or subtraction dictated before taking the limit,
operator topology,
common dense domain if unbounded generators occur,
and the exact target map to H_(Theta_xi).
```

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

## 6. Current ruling

```text
POINTWISE-EULER-IMPEDANCE-LIMIT     F
DIRECT-SONIN-LIMIT-IDENTIFICATION  F
RENORMALIZED-HANKEL-LIMIT           OPEN
```

This is a narrowing of the scattering route, not an RH result.
