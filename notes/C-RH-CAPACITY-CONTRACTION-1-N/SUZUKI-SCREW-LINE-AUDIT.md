# SUZUKI SCREW-LINE AUDIT

```text
STATUS: NON-CANONICAL candidate-D prior-art audit with candidate-T source imports
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Source and novelty boundary

Primary source:

Masatoshi Suzuki, `On the Hilbert space derived from the Weil distribution`,
Canadian Journal of Mathematics, published online 2025-11-03, especially
(1.5)--(1.10), Section 3, Theorem 4.2 and Theorem 4.5.

Suzuki already constructs an explicit `L2(R)`-valued object without assuming
RH and shows that RH is equivalent to equality between its ordinary Hilbert
norm and the Weil Hermitian form. Therefore neither

```text
construct an unconditional positive Hilbert carrier,
construct an unconditional screw-line candidate,
or ask for a Gram factorization of the screw kernel
```

is new in the present incubation.

One possible later scoped target is to compare Suzuki's already-existing
carrier with the explicit local boundary-scattering structure recorded in
issue #357. No such factorization is claimed here.

## 2. Suzuki's vector exists in L2 without RH

Write

```text
A(z)=xi(1/2-i z),
E(z)=xi(1/2-i z)+xi'(1/2-i z),
Theta(z)=E^sharp(z)/E(z).
```

Suzuki defines

```text
S_t(z)= i(1+Theta^sharp(z))/2 * P_t(z),
```

where `P_t` is given explicitly by pole, zeta-log-derivative, finite-prime,
gamma and Hurwitz--Lerch terms in his equation (1.6), with no zero list needed
in the definition.

His Proposition 1.2 / Section 3.2 proves unconditionally that for every fixed
real `t`,

```text
S_t in L2(R),
```

with `||S_t||_2` locally uniformly bounded in `t`. The proof uses the exact
cancellation of the poles of `P_t` by `1+Theta`, and obtains

```text
S_t(z) = O(log|z|/|z|)
```

on the real axis.

Thus the first possible obstruction to the present Pythagorean program is **not**
existence or square-integrability of the vector.

**Status:** candidate-T (direct source import; no project novelty).

## 3. Unconditional positive Hilbert spaces already exist

For test functions `psi`, Suzuki defines

```text
||psi||_0
 = pi^(-1/2) || P_hat_(D psi) ||_L2,
```

where `P_hat_(D psi)` is the integral transform built from `S_t`. He proves
unconditionally that this is a norm, and defines the Hilbert completion `H_0`
and the `L2` closure `K_0` of its image.

Therefore there is already an unconditional positive Hilbert-space side of the
problem. The RH wall is the metric identification

```text
||psi||_0^2 = <psi,psi>_W
```

for every compactly supported smooth test function. Suzuki Theorem 4.5 proves
that this equality for all test functions is equivalent to RH.

**Status:** candidate-T (direct source import and classical RH equivalence; no
project novelty).

## 4. The Gram wall is prior art

Under RH, Suzuki Theorem 4.2 proves

```text
(1/pi)<S_t,S_u>_L2 = G_g(t,u),
```

so `pi^(-1/2) S_t` is a screw line for the zeta screw function. The same paper
shows that the unconditional construction may be used to state RH as a family
of norm equalities.

Suzuki's later 2026 paper `Weil's quadratic form via the screw function`
makes the same wall especially explicit: an unconditional proof of the
corresponding Gram identity would imply RH.

Hence a future TWIST-J note must not claim novelty for `RH is a Gram identity`
or `construct a screw line without zero data`.

## 5. Exact zero expansion and the true conditional step

For `t>=0`, Suzuki's explicit-form calculation gives, meromorphically and
locally uniformly in the source sense,

```text
P_t(z)
 = sum_gamma m_gamma
   (e^(-i gamma t)-1)/gamma * 1/(z-gamma),
```

and therefore

```text
S_t(z)
 = sum_gamma sqrt(pi m_gamma)
   (e^(-i gamma t)-1)/gamma * F_gamma^sharp(z),
```

with

```text
F_gamma(z)
 = sqrt(m_gamma/pi) i(1+Theta(z))/(2(z-gamma)).
```

For negative `t`, the source defines the vector by the even extension
`S_t=S_(-t)`. The unconditional result is existence of the explicit vector in
`L2`; the source's `L2` coefficient-series convergence, orthonormal-basis
diagonalization, and resulting Gram identity are proved under RH. Under RH,
`Theta` becomes inner and the family `{F_gamma}` becomes an orthonormal basis
of the model space. Only then does the ordinary `L2` norm diagonalize into the
zero sum which equals the screw kernel.

This localizes the wall:

```text
unconditional vector and L2 norm: YES,
RH-dependent orthogonality / metric identification: YES.
```

## 6. Deferred comparison boundary (not a gate)

Frozen G3 remains UNDECIDED, so G4 and G6 are blocked. This prior-art audit
does not restate the frozen #357 target and does not open or execute a new
gate. After G3/G5 and an outcome-blind G0 classification, a separately locked
comparison could ask:

```text
Do not construct another positive carrier.
Explain why Suzuki's existing positive carrier K_0 has the same metric as the
arithmetic Weil carrier by factoring its transform through unconditional local
lossless scattering data.
```

At that later scope, one possible exact subproblem is the global `Theta`
factor, rather than another reconstruction of the individual prime or gamma
symbols.

The companion recon `XI-CAYLEY-HARDY-DEFECT.md` rewrites `Theta` as the Cayley
transform of the global logarithmic derivative and records the classical RH
wall as a Hardy escape condition. Neither note proves G3, handles the corrected
signed pole pair, or bypasses the frozen gate order.

## 7. Falsifiers for the scattering-to-Suzuki route

The route fails at the claimed scope if:

1. a proposed construction merely reproduces Suzuki's unconditional `K_0`
   without proving a new factor relation;
2. it assumes orthogonality of `F_gamma` or innerness of `Theta`;
3. it uses real zero ordinates when constructing the local scattering carrier;
4. it claims novelty for the Gram criterion itself;
5. the proposed local-scattering factorization of the global `Theta` or of
   `P_hat_D` fails coefficientwise;
6. an infinite product/cascade is used beyond its proved convergence/domain.

No RH status movement follows from this audit.
