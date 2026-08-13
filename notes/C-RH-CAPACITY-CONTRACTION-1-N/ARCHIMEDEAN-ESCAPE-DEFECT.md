# ARCHIMEDEAN ESCAPE DEFECT

```text
STATUS: NON-CANONICAL incubation result, source convention corrected twice
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 0. Correction history

The first draft incorrectly called the projection in the Connes--Consani
archimedean prolate identity a Hardy half-space projection. Primary-source
readback shows that, after their unitary map to `L2(R)_ev`, the relevant
projection `P1` is already the two-sided interval cutoff `[-1,1]`.

A second overly cautious draft described `u_inf^g` as a possibly differently
gauged phase. The source notation is more precise and simpler: superscript `g`
means **geometric representation** (source equations (22)--(23)),

```text
T^g = F_mu^(-1) T F_mu.
```

The underlying multiplier `u_inf` is exactly the standard archimedean local
factor ratio on the critical line. Thus there is no unknown phase gauge and no
extra gauge-derivative term. What remains open is only the exact comparison of
cutoff/test-function representations.

`TWO-SIDED-HARDY-ESCAPE.md` retains only a generic projection lemma and is not
source evidence for the prolate pair.

## 1. Exact source scattering multiplier

Connes--Consani define

```text
u_inf(s)=exp(2 i theta(s)),
```

where `theta` is the Riemann--Siegel angle. In Appendix E, equations
(159)--(160), they give exactly

```text
u_inf(s)
 = [pi^(-z/2) Gamma(z/2)]
   /[pi^(-(1-z)/2) Gamma((1-z)/2)],

z=1/2+i s.
```

Therefore, in the notation of this incubation,

```text
u_inf(s)=rho_inf(1/2+i s)
        =Gamma_R(1/2+i s)/Gamma_R(1/2-i s).
```

The superscript `g` is the geometric/Mellin representation

```text
u_inf^g=F_mu^(-1) u_inf F_mu,
```

not multiplication by a different phase.

The source also records that the derivative of `2 theta(s)` is

```text
-log pi + Re psi(1/4+i s/2),
```

which is exactly the archimedean Weil/Suzuki multiplier used independently in
this incubation.

**Status:** candidate-T source dictionary; no RH input.

## 2. Exact source projection identity

In the multiplicative model `L2(R_+^*,d^*lambda)`, let

```text
P      = multiplication by 1_[1,infinity),
P_hat  = (F_eR^w)^(-1) P F_eR^w.
```

The source identities (in particular equations (62)--(63) and (69)--(70))
imply

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

**Status:** candidate-T (direct source import; no project novelty).

## 3. The prolate pair is an exact scattering escape square

Remain first in the multiplicative source representation and define

```text
B = P u_inf^g (1-P).
```

Then

```text
B^*B
 = (1-P)(u_inf^g)^*P u_inf^g(1-P)
 = (1-P)(1-P_hat)(1-P).
```

After conjugating by `w`, this is exactly

```text
B^*B=P1 P1_hat P1.
```

Connes--Consani show that if `lambda(n)` are the eigenvalues of the truncated
Fourier transform on the prolate basis, then

```text
P1 P1_hat P1 xi_n=lambda(n)^2 xi_n.
```

Therefore the singular values of the escape block `B` are exactly
`|lambda(n)|`.

**Status:** candidate-T as an operator-algebra consequence of the displayed
source identity.

## 4. The trace remainder at rho=1 is escape energy

The source proves, for `rho>=1`,

```text
delta(rho)=Tr(Theta_scale(rho^(-1)) P1_hat P1).
```

At `rho=1`, trace cyclicity on the trace-class compression gives

```text
delta(1)
 =Tr(P1_hat P1)
 =Tr(P1 P1_hat P1)
 =Tr(B^*B)
 =||B||_HS^2.
```

Thus the nonzero prolate remainder at the identity is exactly the
Hilbert--Schmidt escape energy of the source cutoff scattering block.

For `rho>=1`, `delta(rho)` is the scaling correlation

```text
Tr(Theta_scale(rho^(-1)) P1_hat P1),
```

not a plain pointwise defect norm. Here `Theta_scale` denotes the scaling
representation and is deliberately distinguished from the Riemann--Siegel
angle `theta`. For `0<rho<1`, the source symmetry
`delta(rho^(-1))=delta(rho)` reduces the statement to the reciprocal scale;
the displayed operator ordering is not silently extended outside `rho>=1`.

**Status:** candidate-T for the `rho=1` escape-energy identity and for the
directly imported scaled trace formula on its stated source domain.

## 5. Operator Pythagoras on the actual interval cutoff

Because `u_inf^g` is unitary,

```text
u_inf^g(1-P)
 =(1-P)u_inf^g(1-P)+P u_inf^g(1-P).
```

The two output ranges are orthogonal. Hence

```text
[(1-P)u_inf^g(1-P)]^*[(1-P)u_inf^g(1-P)]
 +B^*B
 =1-P.
```

After the `w` conjugation this is directly a Pythagorean decomposition of an
input supported in `[-1,1]` into retained and escaped scattering output. The
source prolate compression is the escape square.

**Status:** candidate-T.

This interval escape identity does not represent the corrected signed pole

```text
2 Re[M_+ conjugate(M_-)]
 = ||(M_++M_-)/sqrt(2)||^2
   -||(M_+-M_-)/sqrt(2)||^2,
```

does not identify the frozen capacity carrier, and does not prove
`q_A,a>=0`.

## 6. Relation to the frozen Suzuki gamma multiplier

There is no phase-normalization mismatch:

```text
-i conjugate(u_inf) d/ds u_inf
 =d/ds arg u_inf
 =Re psi(1/4+i s/2)-log pi,
```

up to the already-frozen Fourier/quantized-differential sign convention. The
source Appendix E explicitly derives the same logarithmic derivative and uses
it in the archimedean local trace formula.

Thus the **local boundary scattering phase and its infinitesimal Weil
multiplier are already exactly the same object on both sides**. This says
nothing yet about equality of the cutoff realizations.

What is not yet identified is the cutoff carrier:

```text
Connes cutoff:
  P1 in L2(R)_ev, support |x|<=1 together with Fourier-band projection P1_hat,

Suzuki cutoff:
  v in C_c^infty(-a,a) in the additive logarithmic/test-function variable.
```

These cannot be identified by notation alone.

**Status:** candidate-T for the multiplier/logarithmic-velocity identity; OPEN
cutoff-carrier intertwiner.

## 7. HOLD: CUTOFF-CARRIER-INTERTWINER comparison

Frozen G3 remains UNDECIDED; therefore G4 and G6 are blocked. The comparison
below is source recon only. It is not an opened or executed gate and would
require a separate lock before use.

A later exact comparison would be:

1. write the full chain of source unitary maps `F_mu`, inversion `I`, `w`, and
   the even Fourier transform;
2. transport the Suzuki test vector/autocorrelation convention through that
   chain;
3. determine the exact relation between support `(-a,a)` and the source cutoff
   pair `(P1,P1_hat)`, including the scaling parameter;
4. transport the escape block `B` and its phase-delay derivative back to the
   Suzuki carrier;
5. compare the resulting quadratic form coefficient-by-coefficient with
   `q_gamma` and both corrected signed pole legs, including every source
   boundary condition.

Falsifiers:

- support `(-a,a)` does not map to the claimed source cutoff without an extra
  transform or restriction;
- the scaling parameter is moved after the comparison;
- evenness removes or duplicates an admitted Suzuki direction;
- the transformed generator has the wrong digamma or `log pi` normalization;
- a prolate correction or pole term remains unmatched;
- any step assumes Weil positivity.

Even a successful carrier bridge would not settle G3: the signed pole pair and
the frozen capacity choice would still require a separate positivity argument.
