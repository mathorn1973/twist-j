# HALFANGLE PRIME KERNEL

```text
STATUS: candidate-T inside NON-CANONICAL incubation
ISSUE:  #355
PUBLIC STATUS CHANGE: none
```

## The delayed leg

For `L>0`, define

```text
h_L(t) = (|t|-L)_+.
```

The elementary identity

```text
h_L(t) = (|t-L|+|t+L|-2L)/2
```

combined with the standard Fourier representation

```text
|t| = (1/pi) integral_R (1-cos(xi t))/xi^2 dxi
```

gives

```text
h_L(t)
 = (1/pi) integral_R cos(L xi) [1-cos(xi t)]/xi^2 dxi.
```

Let

```text
phi_t(xi) = (exp(i xi t)-1)/xi.
```

For the screw polarization

```text
G_(h_L)(t,u)=h_L(t-u)-h_L(t)-h_L(-u)+h_L(0),
```

the odd Fourier part cancels and one obtains exactly

```text
G_(h_L)(t,u)
 = -(1/pi) integral_R cos(L xi) phi_t(xi) conj(phi_u(xi)) dxi.
```

## Half-angle Pythagoras

Write

```text
-cos(L xi) = sin^2(L xi/2) - cos^2(L xi/2).
```

Define two `L2(R,dxi)` feature maps

```text
S_L(t)(xi) = pi^(-1/2) sin(L xi/2) phi_t(xi),
C_L(t)(xi) = pi^(-1/2) cos(L xi/2) phi_t(xi).
```

Both are square integrable for fixed `t`. Then

```text
G_(h_L)(t,u)
 = <S_L(t),S_L(u)> - <C_L(t),C_L(u)>.
```

Thus a single delayed prime-power screw leg is not a positive Gram leg. It is exactly a **Krein difference of two positive Gram legs at half phase**.

This explains the exact negative determinant in `break.py`; the local leg is indefinite because both half-angle sectors are present with opposite signatures.

## Prime-power weight

For a prime power `n=p^k`, let

```text
w_n = Lambda(n)/sqrt(n),
L_n = log n.
```

The weighted features are

```text
sqrt(w_n) S_(L_n),
sqrt(w_n) C_(L_n),
```

with

```text
sqrt(w_n)=sqrt(Lambda(n)) n^(-1/4).
```

Hence the same quarter-power amplitude found in the scalar prime energy is also the exact amplitude multiplying the half-angle Gram factorization of each prime screw leg.

On any bounded screw interval `|t|,|u|<=a`, only prime powers with `log n<=2a` can contribute to the polarized kernel, so the prime-sector sum is locally finite. Therefore the whole finite-place screw contribution has an exact locally finite Krein-Gram decomposition obtained by direct summation of these half-angle features.

## What this says about sqrt(i)

The canonical operation here is the square root of the **variable phase**

```text
exp(i L xi) -> exp(i L xi/2).
```

There is no fixed eighth root selected by this theorem. When the original phase happens to equal `i`, its balanced half phases are precisely odd eighth roots, including `zeta_8=sqrt(i)`.

So the exact statement is narrower and stronger:

```text
half-phase is structurally forced by the prime screw kernel;
fixed zeta_8 is one special half-phase fiber, not a zeta-global selector.
```

No Born, decoder, metaplectic, physical, or RH promotion follows from this note.
