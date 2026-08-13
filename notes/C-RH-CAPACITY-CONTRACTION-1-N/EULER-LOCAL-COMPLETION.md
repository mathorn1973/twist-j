# EULER-LOCAL COMPLETION OF THE DELAYED PRIME CHANNEL

```text
STATUS: candidate-T, NON-CANONICAL
ISSUE:  #357
SCOPE:  one finite prime place, all prime powers
RH INPUT: none
```

## 1. Why complete the tower

Fix `a>0`, `v in D_a`, and a rational prime `p` with `log p<2a`. Put

```text
r = p^(-1/2),
L = log p,
f = E_a v.
```

Instead of retaining only the powers `p^k` with `kL<2a`, define the two
amplitude channels for **all** `k>=1`:

```text
F_(p,k)^-(v) = sqrt((log p) r^k / 2) [f-U_(kL)f],
F_(p,k)^+(v) = sqrt((log p) r^k / 2) [f+U_(kL)f].
```

The towers are square summable because `sum_(k>=1) r^k<infinity` and
translation is unitary on `L2(R)`.

When `kL>=2a`, the supports of `f` and `U_(kL)f` are disjoint, hence

```text
||F_(p,k)^-v||^2 = ||F_(p,k)^+v||^2
                 = (log p) r^k ||v||^2.
```

Therefore adding all powers beyond the support cutoff adds the **same**
positive norm to both sides and leaves the signed Weil difference unchanged.
The full Euler-local tower is consequently an independently canonical
completion of the truncated delayed channel, not a retuning of the form.

## 2. Exact boundary symbols

On the Fourier line set

```text
theta = xi log p,
z = exp(i theta),
```

and define

```text
A_p(theta)=sum_(k>=1)(log p)r^k[1-cos(k theta)],
B_p(theta)=sum_(k>=1)(log p)r^k[1+cos(k theta)].
```

These are respectively the squared symbols of the completed minus and plus
channels. Geometric summation gives

```text
A_p(theta)
 = (log p) r(1+r)(1-cos theta)
   /[(1-r)(1-2r cos theta+r^2)].
```

Introduce the elementary Blaschke factor

```text
b_r(z)=(z-r)/(1-rz).
```

For `|z|=1`, `|b_r(z)|=1` and

```text
1-b_r(z)=(1+r)(1-z)/(1-rz),
1+b_r(z)=(1-r)(1+z)/(1-rz).
```

Hence exactly

```text
A_p(theta)
 = c_p |1-b_r(z)|^2,

B_p(theta)
 = c_p |1+b_r(z)|^2 + d_p,

c_p = (log p) r/[2(1-r^2)],
d_p = 2(log p)r^2/(1-r^2).
```

Since `|b_r|=1`, the two quadratures obey the exact local Pythagorean identity

```text
|1-b_r|^2+|1+b_r|^2=4.
```

Thus the completed prime place is controlled by one unit-modulus scattering
phase. The indefinite local Weil contribution is not an arbitrary difference
of squares; it is the signed pair of the two canonical quadratures of this
phase, plus the explicit constant `d_p` on the symmetric channel.

## 3. Exact relation to the local L-factor ratio

Let

```text
gamma_p(s)=(1-p^(-s))^(-1),
rho_p(s)=gamma_p(s)/gamma_p(1-s).
```

On the critical line write

```text
s=1/2+i xi,
z=exp(i xi log p).
```

Then

```text
p^(-s)=r z^(-1),
p^(-(1-s))=r z,
```

and therefore

```text
rho_p(s)
 = (1-rz)/(1-rz^(-1))
 = z(1-rz)/(z-r)
 = z/b_r(z).
```

Equivalently,

```text
boxed: b_r(z)=z/rho_p(s).
```

This identifies the phase discovered by the delayed-amplitude completion with
the standard local scattering ratio, up to the bare translation phase `z`.
No RH statement is involved.

## 4. Nesting by finite sets of places

For a cutoff `a`, define the finite prime set

```text
S_a={p prime : log p<2a}.
```

Completing every `p in S_a` through all powers gives a carrier indexed by

```text
{(p,k): p in S_a, k>=1}.
```

If `a<b`, then `S_a subseteq S_b`, and the prime-place carrier grows by direct
sum of **whole local Euler towers**, not by individual powers. This removes the
artificial power-by-power boundary from the carrier and gives a canonical
prime-set filtration.

This filtration is structurally aligned with the semilocal local-factor
framework of Connes--Consani: for a finite set `F` of places including the
archimedean place they study the product of the ratios
`rho_v=gamma_v/gamma_v(1-s)` and prove that the associated semilocal Sonin
spaces form an inductive system as `F` grows. That external theorem is a
comparison target only here; no identification of the present feature carrier
with their Sonin space is claimed without a separate intertwining theorem.

## 5. Consequence for G6

The next non-circular contraction search should not use independent prime-power
coordinates as primitive. The natural finite-place primitive is the completed
local phase `b_(p^-1/2)` or equivalently `rho_p`, with the whole Euler tower as
its amplitude realization.

A genuine G6 construction would need to add the archimedean local ratio and
prove an exact intertwiner between the resulting semilocal scattering/model
space and the frozen `R_+ -> R_-` feature map. Merely observing the common
local-factor vocabulary is not a proof.
