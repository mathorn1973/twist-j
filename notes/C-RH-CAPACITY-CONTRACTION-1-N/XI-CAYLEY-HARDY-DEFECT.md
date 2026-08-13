# XI CAYLEY IMPEDANCE AND HARDY ESCAPE DEFECT

```text
STATUS: NON-CANONICAL incubation result / exact reformulation
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Exact Cayley form of Suzuki's global factor

Put

```text
s = 1/2-i z,
A(z)=xi(s),
h(z)=A'(z)/A(z).
```

Since

```text
A'(z)=-i xi'(s),
E(z)=A(z)+iA'(z),
E^sharp(z)=A(z)-iA'(z),
```

Suzuki's meromorphic boundary phase is exactly

```text
Theta(z)
 = E^sharp(z)/E(z)
 = [1-i h(z)]/[1+i h(z)].
```

Equivalently, with

```text
ell(s)=xi'(s)/xi(s),
```

one has

```text
Theta(z)=[1-ell(s)]/[1+ell(s)].
```

This is a Cayley transform of the global logarithmic derivative of `xi`.

**Status:** candidate-T, elementary exact algebra from Suzuki's definitions.

## 2. Exact simplification of the unconditional screw-line vector

Suzuki defines

```text
S_t(z)= i(1+Theta^sharp(z))/2 * P_t(z).
```

Using

```text
Theta^sharp=E/E^sharp=(1+i h)/(1-i h),
```

one obtains identically

```text
(1+Theta^sharp)/2 = 1/(1-i h),
```

and therefore

```text
S_t(z)= i P_t(z)/(1-i h(z)).
```

On the real axis `A` and `A'` are real, hence `h` is real and

```text
|S_t(x)|^2 = |P_t(x)|^2/[1+h(x)^2].
```

Thus Suzuki's unconditional `L2` carrier has the exact form of a source term
filtered through the Cayley impedance denominator of `xi'/xi`.

**Status:** candidate-T.

## 3. Boundary losslessness is unconditional

Suzuki proves directly that

```text
|Theta(x)|=1  for every real x
```

with removable singularities treated by cancellation. Therefore multiplication
by the boundary function `Theta` is an unconditional unitary operator on
`L2(R)`.

This statement is strictly weaker than `Theta` being inner in the upper half
plane. Boundary losslessness alone does not imply the Hardy orientation needed
for the de Branges/model-space argument.

**Status:** source-T import.

## 4. Pythagoras for the global xi scattering function

Let `P` be the Hardy projection onto `H2(C_+)` boundary values and `Q=1-P`.
Define

```text
T_Theta = P M_Theta P : H2 -> H2,
H_Theta = Q M_Theta P : H2 -> QL2.
```

Since `M_Theta` is unitary on `L2`, the output column is an isometry and

```text
T_Theta^*T_Theta + H_Theta^*H_Theta = I_(H2).
```

This is an unconditional operator Pythagoras.

Moreover,

```text
H_Theta=0
```

if and only if multiplication by `Theta` preserves `H2`. Together with the
unconditional unimodular boundary values, this is equivalent to `Theta` being
an inner function.

Under RH, Lagarias' theorem used by Suzuki gives that `E_xi` is
Hermite--Biehler, hence `Theta` is inner. Conversely, if `Theta` is inner, the
Cayley ratio is analytic and contractive in the upper half plane, so `E` has no
upper-half-plane zeros and satisfies `|E^sharp|<|E|`; the Hermite--Biehler
interlacing theorem then forces the zeros of

```text
A=(E+E^sharp)/2=xi(1/2-i z)
```

to be real. Hence RH follows.

Therefore the classical equivalence may be written

```text
RH
 <=> Theta_xi is inner in C_+
 <=> H_Theta = 0.
```

**Status:** candidate-T classical repackaging; no new RH result.

## 5. Positive-real / Herglotz form of the same wall

The Cayley map

```text
Theta=(1-ell)/(1+ell),
ell(s)=xi'(s)/xi(s),
s=1/2-i z
```

maps the right half-plane in `ell` to the unit disk. Since `Im z>0` is
`Re s>1/2`, the inner/Schur condition is equivalent to the classical
positive-real condition

```text
Re [xi'(s)/xi(s)] > 0
```

throughout `Re s>1/2` away from poles, with the boundary singular measure
handled in the usual Herglotz sense.

Thus RH is also the statement that the global logarithmic derivative is a
passive driving-point impedance on the critical half-plane.

**Status:** classical RH-equivalent reading. It is not an independent proof
mechanism.

## 6. Exact relation to the local scattering factors of issue #357

For each local completed factor `gamma_v(s)`, define

```text
ell_v(s)=gamma_v'(s)/gamma_v(s),
rho_v(s)=gamma_v(s)/gamma_v(1-s).
```

On the critical line `s=1/2+i xi`, conjugation symmetry gives exactly

```text
d/dxi arg rho_v(1/2+i xi)
 = 2 Re ell_v(1/2+i xi).
```

For finite primes this is

```text
(log p)[1-P_(p^-1/2)(xi log p)],
```

and at infinity it is

```text
Re psi(1/4+i xi/2)-log pi.
```

Hence the local lossless scattering cascade constructed in this incubation
already supplies the **boundary real parts of the same logarithmic-derivative
pieces** whose global analytic sum is `xi'/xi`.

This is the exact bridge between the semilocal scattering work and Suzuki's
Cayley factor `Theta`.

**Status:** candidate-T.

## 7. Local-passivity shortcut is false

The positive-real property cannot be proved prime by prime. For a finite prime
factor

```text
gamma_p(s)=(1-p^(-s))^(-1),
```

one has on the real axis `s=sigma>1/2`

```text
ell_p(sigma)
 = -(log p) p^(-sigma)/(1-p^(-sigma)) < 0.
```

Thus an individual finite prime is not a positive-real impedance in the target
orientation. This is the half-plane version of the earlier local signed-inertia
no-go.

Any proof of global passivity must mix finite and archimedean/polar sectors or
arise from a nonlocal compression/limit.

**Status:** exact F for `PRIME-BY-PRIME-PASSIVITY`.

## 8. New narrowed gate: SEMILOCAL-IMPEDANCE-LIMIT

The current scattering attack should no longer aim merely at a norm inequality.
The strongest non-circular target is:

```text
Construct xi'/xi on Re s>1/2 as the driving-point impedance of an
independently defined passive limit of the finite semilocal lossless
colligations plus the exact archimedean and polar channels.
```

A successful construction must imply

```text
Re xi'/xi >= 0
```

from passivity of the limit, not assume RH, zero locations, innerness of
`Theta`, or Weil positivity.

Equivalently it may construct the global boundary multiplier `Theta_xi` as a
Hardy-preserving limit of the local/cutoff scattering systems, which would
force

```text
H_Theta=0.
```

## 9. Falsifiers

1. termwise Euler log derivatives are declared passive despite Section 7;
2. convergence is known only for `Re s>1` and is silently extended past the
   critical half-plane;
3. the limiting colligation is defined from `xi'/xi` after the fact instead of
   constructed from the local cells;
4. contractivity or innerness is assumed at any stage;
5. a compact/quasi-inner defect is silently replaced by zero;
6. the polar or archimedean channels are omitted from the impedance balance;
7. an infinite product or operator limit lacks a typed topology/domain.

The value of the reformulation is localization of the wall, not a status
change: RH is the zero-escape / positive-real completion of a boundary-lossless
object which already exists unconditionally.
