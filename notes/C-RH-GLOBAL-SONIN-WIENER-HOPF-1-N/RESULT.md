# RESULT C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N

```text
STATUS: NON-CANONICAL INCUBATION RESULT
ISSUE:  #360
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## R0. Decision state

```text
G1 GLOBAL-SONIN-IDENTIFICATION  candidate-T
G2 SOURCE-SONIN-ORIENTATION     candidate-T
G3 LOGICAL SCOPE                candidate-T
G4 TRANSPORT LEMMA              candidate-T
G5 GLOBAL-SONIN-WIENER-HOPF     OPEN
G6 TOEPLITZ-KERNEL              OPEN, exact target identified
G7 NO-GO CONTROLS               two exact/narrow F results, one STOP boundary
```

No RH, Weil-positivity, Canon, Registry, Born, decoder, or physical status
moves.

## R1. Suzuki V(0) is exactly a global Sonin kernel

Use Suzuki's unconditional boundary operator

```text
K=F^(-1) M_Theta J F,
(JF)=F^sharp,
V(0)=L2(0,infinity) intersect K L2(0,infinity).
```

Freeze

```text
H_plus=F L2(0,infinity)=H2(C_+),
H_minus=H_plus^perp,
P=proj_(H_plus),
Q=1-P.
```

Let `psi in L2(0,infinity)`, set

```text
f=F psi in H_plus,
eta=f^sharp in H_minus.
```

By definition,

```text
F K psi = Theta eta.
```

Therefore

```text
psi in V(0)
 <=> eta in H_minus and Theta eta in H_plus
 <=> Q M_Theta Q eta=0.
```

The map

```text
A psi=(F psi)^sharp
```

is antiunitary from `L2(0,infinity)` onto `H_minus`. Hence exactly

```text
V(0) ~=_antiunitary S(Theta),
S(Theta):=ker(Q M_Theta Q |_(H_minus)).
```

This calculation uses only Suzuki's definitions and Hardy support, not RH,
innerness of `Theta`, or zero locations.

**Status:** candidate-T.

### Standard Toeplitz form

Write `eta=f^sharp` with `f in H_plus`. The Sonin condition says

```text
Theta f^sharp in H_plus.
```

Apply `sharp`. Since on the real boundary

```text
Theta^sharp=Theta^(-1)=conjugate(Theta),
```

this is equivalent to

```text
conjugate(Theta) f in H_minus.
```

Thus

```text
V(0)!={0}
 <=> ker T_(conjugate Theta)!={0},
T_g=P M_g |_(H_plus).
```

**Status:** candidate-T.

## R2. Exact source Sonin orientation

Connes--Consani decompose boundary `L2` for the left critical half-plane into
its Hardy space and orthogonal complement. With their projection `P_C`, the
lower diagonal block is

```text
u_22=(1-P_C)M_u(1-P_C),
```

and their Sonin space is `ker u_22`. Their theorem further states that for
finite place sets containing infinity the corresponding kernels are infinite
dimensional and form an inductive system under their explicit multiplier maps.

To compare this with the frozen Suzuki upper-half-plane orientation, use the
affine holomorphic map

```text
s=1/2+i z.
```

For `Im z>0`, `Re s<1/2`, so this sends the upper `z` half-plane to the Connes
left critical half-plane. After the induced unitary boundary-coordinate change,
define

```text
u_F_tilde(z)=u(F)(1/2+i z).
```

Then the Connes Sonin kernel becomes exactly

```text
S(u_F_tilde)=ker(Q M_(u_F_tilde) Q |_(H_minus))
```

in the frozen abstract kernel category.

This coordinate choice matters. Suzuki's xi-function formulas often use
`s=1/2-i z`; replacing `+i z` by `-i z` without reflection/conjugation reverses
the Hardy orientation and is not allowed.

**Status:** candidate-T for the coordinate/block dictionary. No identification
of the finite semilocal spaces with Suzuki `V(0)` is claimed.

## R3. Nontrivial V(0) is strictly weaker than RH

Suzuki explicitly observes that

```text
RH -> V(0)!={0},
```

and calls unconditional proof or disproof of `V(0)!={0}` an interesting and
apparently difficult problem. He also states that `V(0)` itself can be
constructed unconditionally.

Nontriviality alone is not Suzuki's RH equivalence. His unconditional
formulation of RH requires additional metric/interpolation conditions on
`V(0)`. Thus a successful G5/G6 result would solve a genuine open structural
problem but would not prove RH.

**Status:** candidate-T logical-scope audit.

## R4. Exact finite-to-global transport lemma

Let `u,U` be unimodular boundary functions on the same oriented boundary. Let
`D,N` be multipliers on a common domain such that

```text
U D=N u,
D H_minus subset H_minus,
N H_plus  subset H_plus.
```

Then

```text
D : S(u) -> S(U).
```

Proof. If `eta in S(u)`, then

```text
eta in H_minus,
u eta in H_plus.
```

By the preservation hypotheses,

```text
D eta in H_minus,
U D eta=N u eta in H_plus.
```

Therefore `D eta in S(U)`.

To obtain a nonzero target vector one additionally needs `D eta!=0` for at
least one nonzero `eta in S(u)`.

**Status:** candidate-T, elementary typed Hardy lemma.

## R5. The exact open transport problem

For a finite Connes semilocal stage, first pull the source symbol to the Suzuki
upper-half-plane boundary:

```text
u_F_tilde(z)=u(F)(1/2+i z).
```

The open gate is to construct, without RH or zero locations,

```text
Theta(z) D_F(z)=N_F(z) u_F_tilde(z)
```

with

```text
D_F H_minus subset H_minus,
N_F H_plus subset H_plus,
```

and `D_F` nonzero on at least one vector in the known infinite-dimensional
`S(u_F_tilde)`.

Writing the tautological quotient `Theta/u_F_tilde` does not solve this gate.
The content is a Wiener--Hopf factorization with the **correct Hardy sides**.

**Status:** OPEN.

## R6. Exact Toeplitz/Wiener--Hopf target

By R1 the independent route is

```text
ker T_(conjugate Theta)!={0}.
```

Directly from the Toeplitz definition, for any unimodular boundary symbol `g`,

```text
ker T_g!={0}
```

if and only if there exist nonzero boundary Hardy functions

```text
f_+ in H_plus,
f_- in H_minus
```

such that

```text
g f_+=f_-.
```

Thus G6 is exactly a Wiener--Hopf / inner--outer factorization question for

```text
g=conjugate(Theta_xi).
```

Deep Toeplitz-kernel and Beurling--Malliavin theory may sharpen this criterion,
but no such theorem has yet been frozen or applied in this incubation.

**Status:** candidate-T for the elementary criterion; nontriviality OPEN.

## R7. No-go controls

### R7.1 Raw finite Euler impedance

For

```text
gamma_p(s)=(1-p^(-s))^(-1),
ell_p=gamma_p'/gamma_p,
```

and real `1/2<sigma<1`,

```text
ell_p(sigma)
 =-(log p)p^(-sigma)/(1-p^(-sigma))<0.
```

Moreover `-ell_p(sigma)>=(log p)p^(-sigma)` and the prime sum of the latter
diverges for `sigma<=1`. Hence

```text
sum_(p<=X) ell_p(sigma) -> -infinity.
```

A fixed archimedean/polar contribution cannot cancel this `X`-dependent
divergence. The global `xi'/xi` continuation in the critical half-strip is not
a pointwise limit of the raw finite Euler impedances.

**Status:** F for `POINTWISE-EULER-IMPEDANCE-LIMIT`.

### R7.2 Direct de Branges-space identification

Suzuki explicitly states that the Connes--Consani--Moscovici de Branges spaces
and his `H(E_xi)` have different generators, are not isomorphic, and have
different spectral properties. Therefore the specific shortcut

```text
CCM de Branges space = Suzuki H(E_xi)
```

is false.

This source statement does **not** by itself prove that no nontrivial
intertwiner, quotient, compression, or Sonin-kernel limit can connect the two
constructions. Such stronger claims remain open.

**Status:** F only for the direct de Branges-space equality.

### R7.3 One known critical zero

Suzuki's RH-dependent model-space section constructs special vectors attached
to zeros and places their inverse Fourier transforms in `V(0)`. That membership
uses the RH-dependent model-space/orthogonality structure. Therefore the
specific shortcut

```text
known real critical zero -> use Suzuki's model vector -> unconditional V(0)
```

is invalid.

This is not a theorem that no other construction from critical-line data could
work.

**Status:** F for the stated direct Suzuki-model-vector shortcut.

## R8. Current verdict

```text
SURVIVES, sharply localized.
```

The new intermediate wall is

```text
finite semilocal infinite-dimensional Sonin kernels
       |
       |  exact orientation + Wiener--Hopf transport, OPEN
       v
S(Theta_xi) ~= V(0) ~= ker T_(conjugate Theta_xi).
```

The target is strictly weaker than RH. RH would require substantially more,
including the relevant global inner/model-space or Weil-metric condition.

The next useful attack is G6: freeze one applicable Toeplitz-kernel phase/
density theorem and test its hypotheses on the unconditional boundary phase of
`Theta_xi`. G5 remains available in parallel but no explicit non-tautological
`D_F,N_F` has yet been constructed.
