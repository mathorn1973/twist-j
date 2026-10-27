# Proposed contact-energy and complete-source claims for v106

**NON-CANONICAL / L1 / proposed conditional T.** This proposal registers
no claim and changes no Canon status. Author: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

The two statements below extract only the reviewed mathematical scope of
[PR #1793](https://github.com/mathorn1973/twist-j/pull/1793), exact source
commit `6f8e8e93a3b459695262c50c2ccbd120cdeb7e99`. The
[published review](https://github.com/mathorn1973/twist-j/pull/1793#pullrequestreview-5657041628)
reports PASS for its six questions and equations (1)-(28), in GitHub state
COMMENTED. The [readback](https://github.com/mathorn1973/twist-j/pull/1793#issuecomment-6424557940)
records two presentation clarifications without changing the proof.
The source itself remains NON-CANONICAL; its review is not a Canon fold.

Pinned evidence: [PROOF.md][proof], [CONTRACT.md][contract] and
[PROMO.md][promo]. `PROOF.md` SHA-256 is
`e1133dbf1fb8226390c2b5eccbc3681fe56368d2ba23c3764248b9a5a9f0d7fd`.
All proofs here are analytical. No scientific executable or new
computation-grade acceptance is supplied.

## Common declared model

Let $L$ be a positive multiple of four, $\mu>0$, $g\in\mathbb R$,
and $k=2\pi j/L$. With Pauli matrices $X,Y,Z$, set

$$
r=\sqrt{1+\mu^2},\quad U_\mu(k)=e^{ikZ}(I+i\mu X)/r,
\quad H(k)=\frac{r(U_\mu(k)^*-U_\mu(k))}{2i}
=-\mu\cos k\,X+\sin k\,(\mu Y-Z).
$$

The carrier is the full tensor product of TWO distinguishable walks,
each on $\ell^2(\mathbb Z/L\mathbb Z)\otimes\mathbb C^2$. Define

$$
H_0=H\otimes I+I\otimes H,\quad
P=\sum_x|x,x\rangle\langle x,x|\otimes I_4,\quad
K_g=e^{-igP},\quad V_g=K_g(U_\mu\otimes U_\mu).
$$

The normalized input is $a=|0,-x\rangle\otimes|\pi,+x\rangle$,
where the coin labels are $X$-eigenstates. Write

$$
s=\sin^2(g/2),\quad b=e^{-ig}-1,\quad \phi_g=V_ga.
$$

There is no positive-band selection, outcome rejection or identical-particle
restriction. $H_0$ is the specified signed sine-energy reading, not a
uniquely selected physical Hamiltonian. At $L=4,\mu=2$, let $S$ denote
the FULL invariant total-momentum-$\pi$ sector, of dimension 16, and let
$\Pi_E$ be its complete $H_0$ spectral projectors.

## Proposal A: complete energy law and sharp five-level completion

Suggested identifier: `DIRAC-CONTACT-COMPLETE-ACCOUNT`.

For the model above the actual full-period output satisfies

$$
\langle H_0\rangle_{\phi_g}=2\mu(1-4s/L),\quad
\Delta\langle H_0\rangle=-8\mu s/L,
$$
$$
\langle H_0^2\rangle_{\phi_g}=4\mu^2+4(1-\mu^2)s/L,\quad
\operatorname{Var}_{\phi_g}(H_0)
=4(1+7\mu^2)s/L-64\mu^2s^2/L^2.
$$

At $L=4,\mu=2$ the complete output law, for every real $g$, is

| Unshifted energy $E$ | Multiplicity in $S$ | $w_E=\Vert \Pi_E\phi_g\Vert ^2$ |
| --- | ---: | ---: |
| $4$ | 2 | $1-3s/4$ |
| $-4$ | 2 | $s/4$ |
| $2\sqrt5$ | 2 | $s/8$ |
| $-2\sqrt5$ | 2 | $s/8$ |
| $0$ | 8 | $s/4$ |

Thus its mean and variance are $4(1-s)$ and $29s-16s^2$.
At $g=2\pi/5$, $s=(5-\sqrt5)/8$, these become
$(3+\sqrt5)/2$ and $(85-9\sqrt5)/8$, respectively.

Set $H_S=H_0|_S+2\sqrt5 I_S$. There is an exactly unitary completion
on the entire 80-dimensional carrier $S\otimes\mathbb C^5$, with
nonnegative additive account $A_{\rm tot}=H_S\otimes I+I\otimes H_B$,
that preserves this whole output law. An explicit construction is

$$
H_B|b_E\rangle=(2\sqrt5-E)|b_E\rangle,\quad
T\psi=\sum_E\Pi_E\psi\otimes|b_E\rangle,\quad Q=TT^*,
$$
$$
W_g=TV_g|_S T^*+(I-Q),\quad [W_g,A_{\rm tot}]=0,\quad
W_g(a\otimes|b_4\rangle)=T\phi_g.
$$

The battery levels are $0,2\sqrt5-4,2\sqrt5,2\sqrt5+4,4\sqrt5$,
with initial energy $2\sqrt5-4$. Its mean gain at $g=2\pi/5$ is
$(5-\sqrt5)/2$. Tracing out the battery gives exactly

$$
\rho_{S,\mathrm{out}}=\sum_E\Pi_E|\phi_g\rangle\langle\phi_g|\Pi_E.
$$

This retains coherence within each energy block, but not between different
energies in the reduced system. For $s>0$ it is not the original pure output.

For $s>0$, both the five distinct battery levels and the initial-energy
lower bound $2\sqrt5-4$ are minimal in this exact class: initial system
energy 4, initially sharp battery energy, nonnegative battery spectrum,
exact additive energy conservation, all five prescribed output weights,
and no additional energy store. The minimum does not cover arbitrary
non-sharp sources or a changed target distribution.

**Proof.** $H$ contains only single-site shifts, so each summand of
$H_0$ takes a coincident pair outside the coincidence subspace:
$PH_0P=0$. Also $H_0a=2\mu a$, $(U_\mu\otimes U_\mu)a=-a$,
and $\langle a,Pa\rangle=1/L$. Expanding $K_ga=a+bPa$, with
$|b|^2=4s$ and $b+\bar b=-4s$, gives, for every spectral function $F$,

$$
\langle F(H_0)\rangle_{\phi_g}
=F(2\mu)+4s\{\langle Pa,F(H_0)Pa\rangle-F(2\mu)/L\}.
$$

Writing $Pa=L^{-1}\sum_k|k,\pi-k\rangle\otimes|-x,+x\rangle$,
put $v=|-x,+x\rangle$ and $A=\mu Y-Z$. Since
$(-X_1+X_2)v=2v$ and $\langle v,(A_1+A_2)^2v\rangle=2(1+\mu^2)$,
the squared norm $\Vert H_0(k,\pi-k)v\Vert^2$ is
$4\mu^2\cos^2k+2(1+\mu^2)\sin^2k$. The discrete sine-square and
cosine-square averages are both $1/2$, so Fourier orthogonality gives
$\langle Pa,H_0^2Pa\rangle=(1+3\mu^2)/L$, proving the moments.
At $L=4,\mu=2$, the original and reversed momentum pairs carry the
given coin at energies 4 and -4. Each remaining pair divides its weight
in proportions $1/4,1/2,1/4$ among $2\sqrt5,0,-2\sqrt5$.
Their coefficients are $b/4$, while the original coefficient is
$1+b/4$. This proves the table; the common minus in $\phi_g=-K_ga$
does not affect probabilities.

For the completion, $T^*T=I_S$ and $A_{\rm tot}T=4\sqrt5T$.
The image of $T$ is exactly that full energy shell. $W_g$ is unitary
there and the identity on its orthogonal complement, proving unitarity
and conservation on the complete carrier. Orthogonality of the battery
labels proves the reduced-state formula. Finally, if its initial energy
is $b_0$, each occupied output energy $E$ requires battery energy
$4+b_0-E$. For $s>0$ all five are distinct and nonnegativity at
$E=2\sqrt5$ forces $b_0\ge2\sqrt5-4$. The construction attains both
bounds. Evidence: [source proof][proof], sections 1-4, equations (1)-(22).

## Proposal B: stationary-source obstruction and necessary energy spread

Suggested identifier: `DIRAC-CONTACT-SOURCE-COHERENCE`.

Retain $L=4,\mu=2$ and $s>0$. Let $B$ now denote any COMPLETE
source, including its controller, clocks, references and energy-bearing
auxiliaries. Assume the input is the product
$|a\rangle\langle a|\otimes\rho_B$, the source is stationary under
$e^{-itH_B}$, and a unitary $W$ commutes with
$e^{-it(H_S\otimes I+I\otimes H_B)}$ for all real $t$.
This group formulation also covers unbounded source Hamiltonians.

Then the reduced system output $\rho$ is stationary under $H_S$,
so it cannot equal $|\phi_g\rangle\langle\phi_g|$. Its squared fidelity
and half trace distance obey

$$
\langle\phi_g,\rho\phi_g\rangle\le1-3s/4,\qquad
\tfrac12\Vert \rho-|\phi_g\rangle\langle\phi_g|\Vert _1\ge3s/4.
$$

The fidelity ceiling is attained in the unrestricted stationary-output
class by $|a\rangle\langle a|$. If the exact weights $w_E$ are also
required, the sharp ceiling is instead

$$
\langle\phi_g,\rho\phi_g\rangle\le\sum_Ew_E^2
=1-3s/2+23s^2/32,
$$

attained by the reduced state in Proposal A. No sharpness is asserted
for the trace-distance lower bound.

Dropping stationarity but retaining initial independence and exact additive
conservation, any source producing the exact pure target and having finite
second energy moments must satisfy

$$
\operatorname{Var}(H_{B,\mathrm{in}})
=29s-16s^2+\operatorname{Var}(H_{B,\mathrm{out}})\ge29s-16s^2.
$$

At $g=2\pi/5$, the two fidelity ceilings are
$(17+3\sqrt5)/32$ and $(409+77\sqrt5)/1024$; the required variance
is at least $(85-9\sqrt5)/8$. Variance is necessary, not sufficient:
a stationary mixed source may have arbitrarily large variance.

**Proof.** The initial joint state is invariant under total time translation;
conservation preserves this invariance, and partial trace makes $\rho$
stationary. The pure target has five nonzero distinct-energy components.
Writing $\phi_E=\Pi_E\phi_g$ and $\rho_E=\Pi_E\rho\Pi_E$, positivity gives
$\sum_E\langle\phi_E,\rho_E\phi_E\rangle
\le\sum_Ew_E\operatorname{Tr}\rho_E\le\max_Ew_E$.
Here $\Pi_4\phi_g=-(1+b/4)a$, proving sharpness by the unchanged input.
Fixing $\operatorname{Tr}\rho_E=w_E$ gives the second ceiling; testing
the pure-target projector gives the distance bound. For the variance
statement, a pure final system marginal forces a product final joint
state. Energy conservation and additivity of variance in both product
states give the displayed identity, because the initial system energy is
sharp. Evidence: [source proof][proof], section 5, equations (23)-(28).

## Generator boundary, dependencies and exclusions

The conserved account of Proposal A is NOT its contact generator:
$e^{-itA_{\rm tot}}T\psi=e^{-it4\sqrt5}T\psi$. It only gives a common
phase on the active shell, whereas $W_g$ produces a nontrivial output
for $s>0$. An interaction/control generator and its preparation need
a further account. This does not prove impossibility of such a generator.
Evidence: [source proof][proof], section 6.

Proposed dependencies: A uses the explicit model and source proof sections
1-4; B uses A's output law and source proof section 5. The comparison
model is pinned in [#1605 at da39ea38][comparison]. General covariance and
the sharp/coherent source distinction are inherited background, not new
general theorems. Source review acceptance does not transfer to an altered
carrier, energy reading or preparation. Identifiers require registry
collision checks before a later fold; they are not registered here.

Pending follow-up only: [#1795 at e4d165c5][rotor] supplies finite rotor
clocks for a DIFFERENT, one-particle four-channel infinite-lattice carrier.
It awaits independent mathematical acceptance and contributes no T claim
here. Its $H_M$ is not identified with this $H_S+H_B$. PRs #1799,
#1800 and #1801 remain outside this proposed fold.

No spatially local battery compilation, native-U derivation, phase/sine
energy selection, particle identity, physical mass, SI calibration,
occurrence law or physical preparation follows from these proposals.

[proof]: https://github.com/mathorn1973/twist-j/blob/6f8e8e93a3b459695262c50c2ccbd120cdeb7e99/notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/PROOF.md
[contract]: https://github.com/mathorn1973/twist-j/blob/6f8e8e93a3b459695262c50c2ccbd120cdeb7e99/notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/CONTRACT.md
[promo]: https://github.com/mathorn1973/twist-j/blob/6f8e8e93a3b459695262c50c2ccbd120cdeb7e99/notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/PROMO.md
[comparison]: https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/CONTACT-KINEMATICS.md
[rotor]: https://github.com/mathorn1973/twist-j/blob/e4d165c5c5471ea5746013f7f8f5c394512f9884/notes/C-DIRAC-FINITE-ROTOR-CLOCK-N/README.md
