# XI CAYLEY IMPEDANCE AND HARDY ESCAPE DEFECT

```text
STATUS: NON-CANONICAL candidate-T exact/classical recon with bounded shortcut no-go
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

On the real axis `A` and `A'` are real, hence `h` is real and, almost
everywhere away from their zeros,

```text
|S_t(x)|^2 = |P_t(x)|^2/[1+h(x)^2].
```

At removable singularities this formula is read by the corresponding source
limit, not by separately evaluating a quotient of two zero values.

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

**Status:** candidate-T (direct source import; no project novelty).

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

Under RH, the theorem used by Suzuki gives that `E_xi` is Hermite--Biehler,
hence `Theta` is inner. Conversely, Proposition 3.1 of Suzuki,
`Li coefficients as norms of functions in a model space`
(`arXiv:2301.05779v2`), supplies the needed cancellation-safe argument: if
`A(z_0)=0` in the upper half-plane, the removable continuation has
`Theta(z_0)=-1`, contradicting the strict disk bound for an inner `Theta`.
Hence RH follows.

The equivalence between `H_Theta=0` and innerness uses the standard typed
Hardy lemma: a unimodular boundary multiplier preserving `H2` has a unique
`H-infinity` representative, and the meromorphic/analytic continuation of the
given `Theta` agrees with it by boundary uniqueness. This analytic-continuation
condition is part of the statement, not inferred from an arbitrary `L-infinity`
representative.

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

maps the open right half-plane in `ell` to the unit disk. Since `Im z>0` is
`Re s>1/2`, the inner/Schur condition is equivalent to `ell` being analytic
there and satisfying the classical positive-real condition

```text
Re [xi'(s)/xi(s)] > 0
```

throughout `Re s>1/2`. Interior poles are forbidden by this condition; zeros
on the boundary are encoded by the usual Herglotz boundary measure.

Thus RH is also the statement that the global logarithmic derivative is a
passive driving-point impedance on the critical half-plane.

**Status:** candidate-T classical RH-equivalent reading. It is not an
independent proof mechanism.

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

Hence each place, and every finite place set, supplies the **boundary real
parts of the corresponding logarithmic-derivative pieces**.

This is an exact finite-place dictionary, not a global analytic bridge on the
critical line. The ordinary Euler logarithmic-derivative sum equals the global
one only in its convergence half-plane `Re s>1`, together with the explicitly
typed archimedean and signed polar terms. Reaching `Re s=1/2` requires analytic
continuation, distributional interpretation, or a separately proved
renormalized operator construction.

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

Within this displayed placewise additive orientation, no prime-by-prime
positive-real proof is possible; any successful balance would have to couple
the finite terms to archimedean/signed-polar sectors or use a separately typed
nonlocal compression/limit.

**Status:** candidate-T exact no-go for the explicitly stated
`PRIME-BY-PRIME-PASSIVITY` shortcut. This post-prereg label is not a public
`F` claim.

## 8. Deferred SEMILOCAL-IMPEDANCE-LIMIT comparison (not a gate)

Frozen G3 remains UNDECIDED, so G4 and G6 are blocked. The comparison below is
not an opened or executed #357 gate. If separately locked after the frozen
order and G0 classification permit it, one possible target would be:

```text
Construct xi'/xi on Re s>1/2 as the driving-point impedance of an
independently defined passive limit of the finite semilocal boundary-unitary
systems plus the exact archimedean and signed polar channels.
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

The value of the reformulation is localization of a classical wall, not a
status change. It does not prove G3, absorb the corrected indefinite pole pair,
or construct the deferred passive limit.
