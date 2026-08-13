# GLOBAL HALF-ARGUMENT PARITY FACTORIZATION

```text
STATUS: candidate-T exact classical identities assembled at one scope
ISSUE:  #357
RH INPUT: none
```

## 1. Half variable

Write

```text
s=2u.
```

The original critical line `Re(s)=1/2` becomes

```text
Re(u)=1/4.
```

This is the same quarter-power line already forced by the prime amplitude
`p^(-s/2)`.

## 2. Finite place: even/odd Euler split

For every prime `p`,

```text
1-p^(-s)
 = 1-p^(-2u)
 = [1-p^(-u)][1+p^(-u)].
```

Define the two half-level factors

```text
gamma_(p,+)(u)=[1-p^(-u)]^(-1),
gamma_(p,-)(u)=[1+p^(-u)]^(-1).
```

Then

```text
gamma_p(2u)=gamma_(p,+)(u) gamma_(p,-)(u).
```

Under the inherited reflection `s -> 1-s`, the half variable transforms as

```text
u -> 1/2-u.
```

Hence define the half scattering ratios

```text
rho_(p,+)(u)=gamma_(p,+)(u)/gamma_(p,+)(1/2-u),
rho_(p,-)(u)=gamma_(p,-)(u)/gamma_(p,-)(1/2-u).
```

They satisfy exactly

```text
rho_p(2u)=rho_(p,+)(u) rho_(p,-)(u).
```

On `u=1/4+i xi/2`, put

```text
q=p^(-1/4),
w=exp(i xi log(p)/2).
```

Then

```text
rho_(p,+)=w/b_q(w),
rho_(p,-)=w/b_(-q)(w),
```

and their product is the double-cover identity

```text
b_(q^2)(w^2)=b_q(w)b_(-q)(w).
```

## 3. Infinite place: Legendre duplication is the same parity split

Use the standard real gamma factor

```text
Gamma_R(s)=pi^(-s/2) Gamma(s/2).
```

Legendre duplication gives

```text
Gamma_R(2u)
 = 2^(u-1) Gamma_R(u) Gamma_R(u+1).
```

Thus the archimedean factor also splits into an even/odd pair on the same
half-argument cover. Define

```text
rho_(inf,+)(u)=Gamma_R(u)/Gamma_R(1/2-u),
rho_(inf,-)(u)=Gamma_R(u+1)/Gamma_R(3/2-u).
```

Then

```text
rho_inf(2u)
 = 2^(2u-1/2) rho_(inf,+)(u) rho_(inf,-)(u).
```

On the critical line `2u=s=1/2+i xi`, the prefactor is the pure phase

```text
2^(2u-1/2)=2^(i xi)=exp(i xi log 2).
```

No modulus is introduced.

## 4. Structural statement

The square-root cover therefore acts uniformly at every place:

```text
finite p:     one Euler denominator -> (+) and (-) half factors
infinity:     one Gamma_R factor    -> even and odd Gamma_R parity factors
critical line Re(s)=1/2             -> half line Re(u)=1/4
phase xi log p                       -> half phase xi log p / 2
radius p^(-1/2)                      -> quarter radius p^(-1/4).
```

The number `1/4` is thus simultaneously

1. the amplitude exponent of the prime weights;
2. the real part of the half spectral parameter `u=s/2`;
3. the radius exponent of the two Blaschke factors on the phase double cover.

This is exact algebra, not an RH consequence.

## 5. Boundary and next question

The factorization does not prove positivity. Each half scattering ratio can
still have a signed phase derivative. What it supplies is a canonical two-copy
(parity) carrier on which a metaplectic/Hardy or colligation comparison could
be attempted.

At the special boundary phase `w=exp(i pi/4)`, the cover contains
`sqrt(i)=zeta_8`; no fixed `zeta_8` is selected for general phase. Any link to
the public TWIST-J Born half-angle requires a separate theorem and is outside
this incubation.
