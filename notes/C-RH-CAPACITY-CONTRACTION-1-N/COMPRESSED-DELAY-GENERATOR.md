# COMPRESSED DELAY GENERATOR

```text
STATUS: NON-CANONICAL incubation result
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Semilocal unitary and its exact delay generator

Fix a finite place set

```text
F = {infinity} union F_fin
```

and on the critical line write

```text
u_F(xi)
 = rho_inf(1/2+i xi)
   product_(p in F_fin) rho_p(1/2+i xi).
```

Every factor has modulus one for real `xi`, hence multiplication by `u_F` is a
unitary operator `U_F` on the critical-line `L2` space.

Let

```text
Q_F(xi) = -i conjugate(u_F(xi)) d/dxi u_F(xi).
```

Then `Q_F` is real on the boundary and, by the ordinary product rule,

```text
Q_F
 = q_inf + sum_(p in F_fin) q_p,
```

where

```text
q_inf(xi)
 = Re psi(1/4+i xi/2)-log pi,

q_p(xi)
 = (log p)[1-P_(p^-1/2)(xi log p)].
```

These are exactly the archimedean and complete-Euler finite-place Weil symbols
already derived from Suzuki's source functional.

The multiplier is unbounded (`q_inf(xi)` grows logarithmically), so every
operator formula below is a quadratic-form identity on the common smooth core
unless a larger form domain is stated explicitly.

**Status:** candidate-T.

## 2. Localized Weil form as a compressed delay generator

Use the unitary Fourier convention and let `P_a` be the orthogonal projection
in the spectral variable onto the Paley--Wiener subspace obtained from
functions supported in `(-a,a)` in the additive variable. Let

```text
F_a = {infinity} union {p : log p < 2a}.
```

Every admitted prime is completed through its full Euler tower. For
`v in C_c^infty(-a,a)`, all prime-power correlations with `k log p >=2a`
vanish by disjoint support, so completing the tower does not alter the signed
localized Weil value. This is a balanced stabilization of that signed value;
it changes the individual positive Hilbert legs and is not, by itself, a
realization of the frozen capacity `q_A,a`.

Therefore, with `f=Fourier(v)`, the exact localized Weil form is

```text
Q_W^a(v)
 = 2 Re[M_+(v) conjugate(M_-(v))]
   + <f, Q_(F_a) f>.
```

Equivalently, on the Fourier image of the smooth test-function core, put

```text
R_+^pole(v)=(M_+(v)+M_-(v))/sqrt(2),
R_-^pole(v)=(M_+(v)-M_-(v))/sqrt(2).
```

Then the exact form identity is

```text
Q_W^a
 = ||R_+^pole||^2-||R_-^pole||^2
   + P_a Q_(F_a) P_a.
```

The pole contribution is an **indefinite** rank-at-most-two form. In
particular it is not the sum `|M_+|^2+|M_-|^2`.

This identity contains no zero data and no RH assumption.

**Status:** candidate-T, exact source repackaging.

## 3. Relative-generator identity

Let

```text
D_xi = -i d/dxi
```

on a common smooth core. Multiplication by `u_F` gives

```text
U_F^* D_xi U_F - D_xi
 = multiplication by Q_F.
```

Thus the local Weil multiplier is the relative logarithmic velocity of the
unconditional boundary-unitary multiplication operator:

```text
Q_F = U_F^* D_xi U_F - D_xi.
```

This is the operator form of the phase-derivative identity. It does not by
itself construct a causal/passive conservative colligation. In the additive
Fourier-dual variable, `D_xi` is multiplication by the signed delay coordinate,
up to the frozen Fourier sign convention.

**Status:** candidate-T.

## 4. Pythagoras one level up: the cutoff output column

Introduce the translated spectral family

```text
(U_F(tau)f)(xi)=u_F(xi+tau)f(xi).
```

On the localized input space `P_a H`, split the unitary output into the part
which remains in the cutoff space and the escaped part:

```text
S_a(tau)=P_a U_F(tau) P_a,
B_a(tau)=(1-P_a) U_F(tau) P_a.
```

Define the output column

```text
W_a(tau) = [ S_a(tau) ; B_a(tau) ].
```

Since `U_F(tau)` is unitary and `P_a` is an orthogonal projection,

```text
W_a(tau)^* W_a(tau)=I_(P_a H),
```

or explicitly

```text
S_a^*S_a + B_a^*B_a = I.
```

This is an exact operator Pythagoras independent of RH.

Differentiate on the smooth form core. At `tau=0`,

```text
-i W_a^* W_a'
 = P_a Q_F P_a.
```

Equivalently,

```text
P_a Q_F P_a
 = -i[S_a^*S_a' + B_a^*B_a'].
```

The path `tau -> U_F(tau)` is differentiable but need not be a one-parameter
group. The right side is self-adjoint as a whole because it is the
Wigner--Smith/logarithmic velocity of an isometric column. The individual two
summands need not be positive or self-adjoint separately.

Thus the non-polar localized Weil form contribution is exactly the
phase-delay logarithmic velocity of a Pythagorean decomposition into an
in-window output and an escape output, on the stated core.

**Status:** candidate-T, general Hilbert-space identity applied to the stated
semilocal multiplier on the stated core.

## 5. The finite interval is a difference of shifted Hardy projections

Let `C_a` denote multiplication by the characteristic function of `(-a,a)` in
the additive variable, and let `H_-` denote the projection onto the negative
half-line. Then, ignoring endpoint null sets,

```text
C_a
 = 1_(-infinity,a) - 1_(-infinity,-a).
```

If `T_c` translates the additive variable by `c`,

```text
1_(-infinity,c) = T_c H_- T_c^*.
```

Under Fourier transform, `T_c` becomes multiplication by a unit phase
`exp(-i c xi)`. Hence the Paley--Wiener interval projection has the exact form

```text
P_a
 = M_(exp(-i a xi)) P_H M_(exp(+i a xi))
   - M_(exp(+i a xi)) P_H M_(exp(-i a xi)),
```

with `P_H` the Hardy projection corresponding to `H_-` under the chosen
Fourier orientation.

Therefore every block involving the finite-interval projection `P_a` can be
expanded into a finite combination of **shifted Hardy blocks** of the same
scattering multiplier `u_F`.

This is a generic shifted-Hardy expansion of the interval projection. It is
not source evidence identifying `P_a` with the Connes--Consani prolate cutoff:
their relevant source pair is a two-sided time/band projection pair. An exact
carrier/normalization intertwiner remains open.

**Status:** candidate-T.

## 6. Why this avoids the collision-jet mismatch

`SEMILOCAL-DEFECT-MATCH.md` proves that the off-diagonal block of `u_F` itself
contains a growing finite-dimensional jet sector at the common pole `s=0`.
That killed a direct sectorwise identification with the additive Weil feature
map.

The present object instead differentiates the **phase** before applying the
localized quadratic form:

```text
u_F  ->  -i u_F^*u_F' = sum local delays.
```

The product rule removes the multiplicative collision terms exactly. The
localized form is then obtained by the independent projection `P_a`.

Thus the mixed jet is a property of the Hardy off-diagonal block of the
multiplicative scattering function, not of the uncompressed logarithmic delay
generator itself. This observation does not supply the still-missing map from
the balanced full-tower carrier to the frozen strict-cutoff capacity carrier.

## 7. What this does and does not prove

The identities above do not prove positivity. An isometric output column may
have a phase-delay generator of either sign. The signed pole pair is also still
external to the local scattering product.

What is gained is a non-circular form-level construction of the signed
localized Weil form on the smooth core:

```text
Q_W^a
 = (R_+^pole)^*R_+^pole-(R_-^pole)^*R_-^pole
   - i W_a^* W_a'.
```

Here `W_a` is built solely from known local L-factor scattering ratios and the
geometric support projection.

This is not the frozen G3 capacity:

```text
q_A,a(v) = Q_W^a(v) + ||V_a^+ v||^2,
```

where `V_a^+` is the strict-cutoff frozen feature map, not its silently
completed Euler tower. The balanced Euler completion preserves `Q_W^a`, but
changes the separate Hilbert legs from which a capacity is chosen. No zeta zero
and no Weil positivity is used in the form identity; no positivity conclusion
follows.

## 8. Deferred cutoff-carrier comparison (not a gate)

The frozen preregistration keeps G3 (unconditional positivity of `q_A,a`)
UNDECIDED. Consequently G4 and G6 remain blocked. No new gate is opened or
executed by this recon.

A separately locked future comparison could expand the exact interval identity
of Section 5 inside

```text
-i[S_a^*S_a' + B_a^*B_a']
```

and compare it with the source formulas for `rho_inf product rho_p` after an
exact carrier map has been typed.

A positive outcome would have to derive the prolate/cutoff correction from the
transported blocks, not fit it afterwards. Such a test would begin at the
archimedean place and then at `{infinity,p}`.

Falsifiers:

1. the shifted-Hardy expansion yields a boundary term absent from Suzuki's
   localized form;
2. the Connes prolate remainder has a coefficient/sign incompatible with the
   escape term `B_a`;
3. the common-pole jet survives in the final logarithmic-delay combination
   instead of canceling as required by the exact product rule;
4. the construction requires an innerness or positivity assumption;
5. the first complete-prime update violates the exact cutoff restriction law.

Even if these comparisons survive, they do not settle G3: the signed pole pair,
the capacity choice, and positivity would still require their separately
frozen arguments.
