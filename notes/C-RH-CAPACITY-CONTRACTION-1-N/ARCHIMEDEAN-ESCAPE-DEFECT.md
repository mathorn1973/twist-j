# ARCHIMEDEAN ESCAPE DEFECT

```text
STATUS: NON-CANONICAL incubation result, source convention corrected
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 0. Correction of the first draft

The first draft incorrectly called the projection in the Connes--Consani
archimedean prolate identity a Hardy half-space projection and silently
identified their gauged unitary `u_inf^g` with the raw critical-line multiplier
`rho_inf`. The primary PDF does not support either simplification.

The exact source convention is recorded below. The generic Hilbert-space escape
identity survives; the previous `one-sided Hardy -> two endpoints` source
interpretation is withdrawn. `TWO-SIDED-HARDY-ESCAPE.md` retains only its
generic projection lemma and is not source evidence for the prolate pair.

## 1. Exact source projection identity

In the multiplicative model `L2(R_+^*,d^*lambda)`, Connes--Consani let

```text
P      = multiplication by 1_[1,infinity),
P_hat  = (F_eR^w)^(-1) P F_eR^w.
```

Their gauged archimedean unitary `u_inf^g` satisfies exactly

```text
(u_inf^g)^* P u_inf^g = 1-P_hat.
```

After conjugation by their unitary map `w` to `L2(R)_ev`, the same symbol `P`
becomes multiplication by the characteristic function of the **complement** of
`[-1,1]`. Writing

```text
P1     = 1-P,
P1_hat = 1-P_hat,
```

one has

```text
P1     = projection onto functions supported in [-1,1],
P1_hat = F_eR^(-1) P1 F_eR.
```

Thus `P1,P1_hat` are directly the time/band cutoff pair of the classical
prolate problem. They are not Hardy half-space projections in this
representation.

**Status:** source-T import, no project novelty.

## 2. The prolate pair is an exact scattering escape square

Remain first in the multiplicative source representation and define

```text
B = P u_inf^g (1-P).
```

Then, purely algebraically,

```text
B^*B
 = (1-P)(u_inf^g)^* P u_inf^g(1-P)
 = (1-P)(1-P_hat)(1-P).
```

After conjugating by `w`, this becomes exactly

```text
B^*B = P1 P1_hat P1.
```

Hence the standard positive prolate compression is the squared escape block of
the source gauged archimedean unitary.

Connes--Consani show that if `lambda(n)` are the eigenvalues of the truncated
Fourier transform on the prolate basis, then

```text
P1 P1_hat P1 xi_n = lambda(n)^2 xi_n.
```

Therefore the singular values of `B` are exactly `|lambda(n)|`.

**Status:** candidate-T as an operator-algebra consequence of the displayed
source identity.

## 3. The trace remainder at rho=1 is escape energy

The source proves, for `rho>=1`,

```text
delta(rho)=Tr(theta(rho^(-1)) P1_hat P1).
```

At `rho=1`, trace cyclicity on the trace-class compression gives

```text
delta(1)
 = Tr(P1_hat P1)
 = Tr(P1 P1_hat P1)
 = Tr(B^*B)
 = ||B||_HS^2.
```

Thus the nonzero prolate remainder at the identity is exactly the
Hilbert--Schmidt escape energy of the source cutoff scattering block.

For general scaling, `delta(rho)` is the scaling correlation

```text
Tr(theta(rho^(-1)) P1_hat P1),
```

not a plain pointwise defect norm. No sign claim for each `delta(rho)` is made
here beyond the exact source formula.

**Status:** candidate-T for the `rho=1` escape-energy identity; source-T import
for the scaled trace formula.

## 4. Operator Pythagoras on the actual interval cutoff

Because `u_inf^g` is unitary, its output from the inside cutoff `(1-P)H`
splits orthogonally into inside and outside pieces:

```text
u_inf^g(1-P)
 = (1-P)u_inf^g(1-P) + P u_inf^g(1-P).
```

Therefore

```text
[(1-P)u_inf^g(1-P)]^*[(1-P)u_inf^g(1-P)]
 + B^*B
 = 1-P.
```

After the `w` conjugation this is directly a Pythagorean decomposition of an
input supported in `[-1,1]` into its retained and escaped scattering output.
There is no need to synthesize the prolate pair from two Hardy boundaries: the
source cutoff is already two-sided.

**Status:** candidate-T, general Hilbert-space identity applied to the exact
source cutoff.

## 5. Relation to the earlier remainder-domination no-go

`TRACE-REMAINDER-DOMINATION-NOGO.md` proved that one cannot pay for `delta`
separately by the frozen pole channels below the first-prime threshold. The
present result explains why that stronger scalar route failed: the remainder
is part of a coupled inside/escape decomposition of a unitary cutoff channel.
The source proof moves contributions through the geometry of the projection
pair rather than bounding the remainder independently.

## 6. Necessary convention gate before identifying this with the Suzuki carrier

The exact source unitary in the projection identity is the **gauged** object
`u_inf^g`. The present incubation separately uses the raw critical-line local
ratio

```text
rho_inf(s)=Gamma_R(s)/Gamma_R(1-s)
```

and its phase-delay derivative as the Suzuki gamma multiplier.

A direct statement

```text
u_inf^g = multiplication by rho_inf
```

has NOT been proved in the frozen normalization and is not assumed here. A
future bridge must write the exact unitary conjugation/gauge between the two
representations and show how its derivative affects the phase-delay generator.
A nonconstant gauge may contribute an additional generator term and therefore
cannot be dropped by saying only `unitarily equivalent`.

**Status:** OPEN convention bridge.

## 7. Sharpened next gate: ARCHIMEDEAN-GAUGE-DELAY

The next exact test is:

1. read the source definition of `u_inf^g` and the unitary maps `I,w,F_eR^w`;
2. express the source cutoff escape column in the same critical-line Fourier
   convention as `rho_inf`;
3. differentiate the exact gauge relation;
4. decide whether the resulting generator equals the Suzuki archimedean
   multiplier directly or equals it plus a typed boundary/gauge term;
5. identify that extra term, if any, with a source pole or cutoff channel rather
   than fitting it afterwards.

Falsifiers:

- a claimed equality drops a nonconstant gauge derivative;
- the transformed projection is not the frozen finite-support/Paley--Wiener
  projection;
- the generator has the wrong digamma or `log pi` normalization;
- the prolate trace correction acquires an unmatched term;
- any step assumes Weil positivity.

If this convention bridge closes, the source already supplies the correct
interval-level Pythagorean escape geometry at the archimedean place.
