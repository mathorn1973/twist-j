# LOCAL WEIL SYMBOLS AS SCATTERING PHASE DERIVATIVES

```text
STATUS: candidate-T exact identities; NON-CANONICAL
ISSUE:  #357
RH INPUT: none
```

## 1. Finite prime place

Fix a rational prime `p` and put

```text
r=p^(-1/2),
theta=xi log p,
z=exp(i theta),
b_r(z)=(z-r)/(1-rz).
```

On `|z|=1`, `b_r` is unitary and its phase derivative is the Poisson kernel

```text
P_r(theta)
 = d/dtheta arg b_r(exp(i theta))
 = (1-r^2)/(1-2r cos(theta)+r^2).
```

The local Euler factor and its functional-equation ratio are

```text
gamma_p(s)=(1-p^(-s))^(-1),
rho_p(s)=gamma_p(s)/gamma_p(1-s).
```

On `s=1/2+i xi`, exact algebra gives

```text
rho_p(s)=z/b_r(z).
```

Therefore

```text
d/dxi arg rho_p(1/2+i xi)
 = (log p)[1-P_r(theta)].
```

On the other hand, geometric summation gives

```text
-2(log p) sum_(k>=1) r^k cos(k theta)
 = (log p)[1-P_r(theta)].
```

Thus the completed local prime-power Weil symbol is exactly the derivative of
the local scattering phase `rho_p`.

This same symbol is the signed difference of the completed delayed amplitude
channels in `EULER-LOCAL-COMPLETION.md`.

## 2. Archimedean place

Let

```text
gamma_inf(s)=pi^(-s/2) Gamma(s/2),
rho_inf(s)=gamma_inf(s)/gamma_inf(1-s).
```

Write

```text
g(s)=log gamma_inf(s),
g'(s)=-(1/2)log pi+(1/2)psi(s/2).
```

For `s=1/2+i xi`, `1-s=conj(s)`, hence

```text
d/dxi log rho_inf(s)
 = i g'(s)+i g'(1-s)
 = i[Re psi(1/4+i xi/2)-log pi].
```

Since `rho_inf` has unit modulus on the critical line,

```text
d/dxi arg rho_inf(1/2+i xi)
 = Re psi(1/4+i xi/2)-log pi.
```

This is exactly the Fourier multiplier of the gamma/infinite-place quadratic
term derived directly in `RESULT.md`.

## 3. Semilocal sum

For a finite set of places `S` containing infinity, define the scattering
ratio

```text
rho_S(s)=product_(v in S) rho_v(s).
```

Then, on the critical line, the non-pole local part of the explicit formula is
additive because

```text
d/dxi arg rho_S = sum_(v in S) d/dxi arg rho_v.
```

Thus the finite-place prime towers and the archimedean gamma term are not two
different mechanisms. They are the finite and infinite local pieces of one
scattering-phase derivative. The pole terms remain separate rank-one/rank-two
boundary channels.

## 4. Exact lossless realization of the compensating factor

The Blaschke factor itself is the transfer function of the real orthogonal
colligation

```text
U_r = [[r, sqrt(1-r^2)],
       [sqrt(1-r^2), -r]].
```

Indeed `U_r^T U_r=I`, and the scalar transfer function with state parameter
`z` is

```text
-r + z(1-r^2)/(1-rz) = (z-r)/(1-rz)=b_r(z).
```

Hence the compensating factor `b_r=z/rho_p` admits a real orthogonal `2x2`
colligation with one-dimensional state before any RH question is asked. The
colligation does not directly realize `rho_p`: in this disk orientation
`rho_p=z/b_r` has a pole at `z=r`. Inversion, the bare phase `z`, and the
Hardy orientation remain part of any scattering realization.

## 5. Comparison with the existing semilocal literature

Connes--Consani define exactly the same local ratios
`rho_v=gamma_v/gamma_v(1-s)`. For finite sets of places including infinity
they prove the product is quasi-inner and that the associated semilocal
kernels form an inductive system as the set of places grows. The comparison
maps for adding places are local-denominator multipliers, not plain
inclusions. Their
archimedean-place work realizes a positive trace functional by compressing the
scaling action to Sonin space.

These are external comparison theorems, not imported conclusions for #357.
The geometric identification of all semilocal kernels with Sonin spaces is not
imported here. The present incubation has not proved that its corrected feature
maps `R_+` and `R_-` intertwine with those semilocal Hardy blocks.

The local relation `rho_p b_r=z` is also not a novelty claim: it is the scalar
local form of the Blaschke compensation already present in the cited
Connes--Consani analysis. The useful new content at this lane is its exact
comparison with the delayed-tower norm symbols.

## 6. Sharpened G6 target

The candidate comparison is now explicit in type:

```text
signed delayed norm symbols
       -> missing common spectral-factor map
       -> local lossless colligations for b_(p^-1/2)
       -> finite product of local scattering ratios rho_p
       -> archimedean scattering ratio rho_inf
       -> Hardy/Sonin compression
       -> compare with the corrected graph map R_+ -> R_-.
```

A positive result requires an exact intertwining identity at the quadratic-form
level. Similar vocabulary or a common phase derivative is not enough.

The hoped-for mechanism is that the target contraction is a compression or
defect map of a unitary semilocal scattering system. If so, its contractivity
would come from unitarity rather than from assuming Weil positivity. This is a
hypothesis for a later gate, not a theorem of this note. The frozen breaker
order keeps G6 blocked while G3 is undecided; an earlier comparison requires a
separate no-go/intertwiner lock.
