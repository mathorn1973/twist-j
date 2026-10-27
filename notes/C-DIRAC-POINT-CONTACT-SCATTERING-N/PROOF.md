# Point-contact resolvent, scattering and continuation poles

Status: NON-CANONICAL. Layer: L1. Candidate: candidate-T.
All theorems below are conditional statements about the declared operator.
No particle identification or Canon authority is asserted.

The operator is the non-canonical input from PR #1795 at
`e4d165c5c5471ea5746013f7f8f5c394512f9884`. This proof is self-contained and
does not use a finite-clock approximation. The public scope is issue #1796.

## 1. Operator and conventions

Let

\[
\mathcal H=\ell^2(\mathbb Z)\otimes\mathbb C^2_{\rm dir}
                         \otimes\mathbb C^2_{\rm port},\qquad
t=1/\sqrt5,\quad r=2/\sqrt5.
\]

Use the port basis in which `R = X_port` has eigenvalues plus and minus.
In this basis the original `Z_port` interchanges the two sectors. Set

\[
S(z)=\operatorname{diag}(z^{-1},z),\quad
U_0(z)=S(z),\quad U_2(z)=S(z)(tI+irX),\quad
\mathcal U=U_0\oplus U_2.
\]

Here `X` denotes the direction Pauli matrix, not the port matrix. Write

\[
c=\cos g,\quad s=\sin g,\quad d=1-c,\qquad
K=\begin{pmatrix}cI&-isI\\-isI&cI\end{pmatrix},\qquad
V=[I+Q(K-I)]\mathcal U,
\]

where `Q` is the spatial projector at the origin. `K` acts on the internal
four-dimensional fiber. Both the free step and the contact are unitary.

A plane wave is `z^x u`, with `z = exp(ik)`. Its eigenvalue is
`lambda = exp(-i E)`. The variable `E` is a dimensionless step phase, modulo
`2 pi`. No equality with a different sinusoidal energy reading is assumed.
With this convention direction 1 of `U_0` propagates toward increasing x.

## 2. Open channels and exact current

The massless channels have phases `E = k` and `E = -k`, with velocities
`+1` and `-1`. The massive dispersion is

\[
\det(\lambda-U_2(k))=\lambda^2-2t\lambda\cos k+1,
\qquad \cos E=t\cos k.                                      \tag{2.1}
\]

Consequently:

* `|cos E| > t`: two massless open channels and no massive open channel;
* `|cos E| < t`: two massless and two massive open channels;
* `|cos E| = t`: massive thresholds, excluded from flux-normalized formulas
  requiring nonzero velocity and treated by one-sided limits only.

Inside an open massive band choose the two roots `k = +/- kappa`, where
`cos(kappa) = cos(E)/t`, `0 < kappa < pi`. A normalized eigenvector and its
velocity are

\[
u(k,E)=\frac{(ir,\lambda e^{ik}-t)^T}
 {\sqrt{r^2+|\lambda e^{ik}-t|^2}},\qquad
v(k,E)=\frac{t\sin k}{\sin E}.                              \tag{2.2}
\]

These roots include both signs of velocity. The denominator in the spinor
is nonzero because `r != 0`.

For an arbitrary state let `q(x)` be the state after the on-site free coin
and before the conditional shift. Each `q_j(x)` includes both port entries.
The contact preserves the direction-wise norms at the origin. Therefore

\[
\rho_{n+1}(x)-\rho_n(x)=j_n(x-\tfrac12)-j_n(x+\tfrac12),
\qquad
j_n(x+\tfrac12)=\|q_1(x)\|^2-\|q_2(x+1)\|^2.                \tag{2.3}
\]

This follows by writing the two shifted squared norms at x and subtracting
the two unshifted ones. It is valid also at the contact. For a stationary
unit-norm plane wave, the current is
`|u_1|^2 - |u_2|^2 = v(k,E)`; this follows directly from (2.2), or by
differentiating its unitary eigenvalue equation. Thus `u/sqrt(|v|)` has
unit absolute flux. A finite contact preserves the same current and does
not alter the free propagation velocity outside its support.

## 3. Exact local free resolvent

For `|lambda| > 1` define

\[
G(\lambda)=\langle0|(\lambda-\mathcal U)^{-1}|0\rangle,
\qquad F(\lambda)=\lambda G(\lambda)-I.
\]

The port blocks are diagonal. The directed shifts give

\[
G_0(\lambda)=I/\lambda,\qquad F_0(\lambda)=0.                \tag{3.1}
\]

Define

\[
\Delta(\lambda)^2=(\lambda^2+1)^2-4t^2\lambda^2,
\qquad \Delta(\lambda)\sim\lambda^2\quad(\lambda\to\infty).
                                                                    \tag{3.2}
\]

This fixes the exterior branch. Its four branch points are
`lambda = +/- t +/- i r`, on the unit circle. The local massive resolvent is

\[
G_2(\lambda)=
\frac{\lambda^2-1+\Delta}{2\lambda\Delta}I
+i\frac{\lambda^2+1-\Delta}{\lambda\Delta}X.                 \tag{3.3}
\]

To derive it, invert the two by two symbol. Its denominator is
`A - B cos(k)`, with `A = lambda^2 + 1`, `B = 2t lambda`.
The contour integral on `z = exp(ik)` has one enclosed root and yields

\[
I_0=\int_{-\pi}^{\pi}\frac{dk}{2\pi(A-B\cos k)}=1/\Delta,
\quad
I_1=\int_{-\pi}^{\pi}\frac{\cos k\,dk}{2\pi(A-B\cos k)}
     =\frac{A/\Delta-1}{B}.
\]

The inverse symbol has diagonal average `lambda I_0 - t I_1` and
off-diagonal average `i r I_1`; substitution gives (3.3). The branch in
(3.2) is exactly the one for which `I_0 ~ 1/lambda^2`.

Let `X v_sigma = sigma v_sigma`, `sigma = +/-1`, and put

\[
a_\sigma=\frac{-3+4i\sigma}{5},\qquad b_\sigma=1+2i\sigma.
\]

The two eigenvalues of `F_2` are

\[
f_\sigma(\lambda)=\frac{b_\sigma}{2}
 \left(\frac{\lambda^2-a_{-\sigma}}{\Delta(\lambda)}-1\right),
\qquad
\Delta^2=(\lambda^2-a_+)(\lambda^2-a_-).                    \tag{3.4}
\]

The formulas at `lambda = 0` require the continuation specified in section
6, not substitution into the exterior physical resolvent of the full step.

## 4. Finite scattering system and all-channel matrix

Let `phi` be a free on-shell incident plane wave, initially regularized by
the exterior resolvent. Put `D = K - I`, `a = (mathcal U psi)(0)` and let
`eta` be the contact source. The stationary equations are exactly

\[
\psi=\phi+(\lambda-\mathcal U)^{-1}|0\rangle\eta,
\quad \eta=Da,
\quad (I-FD)a=\lambda\phi(0).                              \tag{4.1}
\]

The last equation is an explicit four by four linear system. It follows
from `mathcal U(lambda-mathcal U)^(-1) = lambda(lambda-mathcal U)^(-1)-I`.

Define `B = D(I-FD)^(-1)`. In the direction `X` eigenbasis its port blocks
are the explicit matrices

\[
D_\sigma=1+d f_\sigma,\qquad
B_\sigma=\frac1{D_\sigma}
 \begin{pmatrix}
 -d(1+2f_\sigma)&-is\\-is&-d
 \end{pmatrix}.                                            \tag{4.2}
\]

In particular `eta = lambda B phi(0)`. These formulas include all return
visits through the massive channel; they are not a second-order expansion.

For every open channel j form the internal column
`w_j = u_j/sqrt(|v_j|)`, embedded in its port sector, and let `W` be the
matrix of these columns. For massless channels these columns are the two
direction basis vectors in the plus sector. Evaluate `F` and `B` at the
radial boundary value `lambda = (1+epsilon) exp(-iE)`,
`epsilon -> 0+`. Then the complete scattering matrix is

\[
\boxed{\mathsf S(E)=I+W(E)^\dagger B(e^{-iE}+0)W(E).}        \tag{4.3}
\]

Here incoming and outgoing channels are ordered by their free traveling
mode, so the free scattering matrix is the identity. A convention ordering
outgoing channels by left and right instead permutes its rows.

For completeness, near an open root k_j,
`d lambda_j/dk = -i lambda v_j`. The exterior point-source resolvent has,
on the outgoing side `sign(x) = sign(v_j)`, the residue

\[
e^{ik_j x}\frac{u_j u_j^\dagger\eta}{\lambda |v_j|}.
\]

Relative to the normalized traveling wave `w_j`, its coefficient is
`w_j^dagger eta/lambda`. This proves the normalization and sign in (4.3).
The pole is displaced toward the half-plane selected by the outgoing side;
the opposite side has no contribution from that mode.

### Exact flux unitarity

The spectral boundary identity for this same normalization is

\[
F+F^\dagger=WW^\dagger-I.                                  \tag{4.4}
\]

It can be obtained by adding the two boundary values of
`u/(lambda-u)` in the spectral resolution. Its smooth real part is `-1/2`;
the on-shell delta contribution has precisely the weights `1/|v_j|` from
the preceding residue calculation. The massless block reads `0 = I-I`.
An independent explicit check of the massive block is given below.

For `g` not a multiple of `2 pi`, `D` is invertible and unitarity of `K`
gives `D^(-1)+D^(-dagger)=-I`. Hence

\[
B^{-1}+B^{-\dagger}=-WW^\dagger,
\qquad B+B^\dagger+B^\dagger WW^\dagger B=0.
\]

Substituting in (4.3) proves `S^dagger S = I`. The contact-free value follows
by continuity, or directly from `D = 0`. This proves current conservation
including conversion between every open channel.

### Useful closed forms on the real phase axis

Write `lambda = exp(-iE)` and `h = Delta/(2 lambda)`. On a massive gap,

\[
h=\operatorname{sgn}(\cos E)\sqrt{\cos^2E-t^2},\qquad
f_\sigma=-\tfrac12+i y_\sigma,
\quad y_\sigma=\frac{2\sigma\cos E-\sin E}{2h}-\sigma.        \tag{4.5}
\]

Only the two massless channels are open. In their fixed `X` eigenbasis,

\[
\boxed{\mathsf S_{++,\sigma}
 =\frac{c-d f_\sigma}{1+d f_\sigma}
 =\frac{(1+c)/2-i d y_\sigma}{(1+c)/2+i d y_\sigma}.}        \tag{4.6}
\]

Both eigenvalues have modulus one. In the original direction basis,
transmission and reflection amplitudes are respectively
`(S_{++,+}+S_{++,-})/2` and `(S_{++,+}-S_{++,-})/2`, with the free-traversal
ordering just stated.

Inside a massive open band put `q = sqrt(t^2-cos^2 E)`. The outgoing
boundary value instead has

\[
h=-i\operatorname{sgn}(\sin E)q,
\quad f_\sigma=-\tfrac12+\tfrac12\rho_\sigma-i\sigma,
\quad
\rho_\sigma=\frac{|\sin E|-2\sigma\operatorname{sgn}(\sin E)\cos E}{q}>0.
                                                                    \tag{4.7}
\]

Direct substitution of (2.2) gives massive `WW^dagger` eigenvalues
`rho_sigma`, which verifies (4.4) explicitly. The inequality follows from
`|sin E| > 2|cos E|` in the open band.

After a unitary change of the two massive channel coordinates and the fixed
`X` change of the massless coordinates, the full four by four matrix is
the direct sum of

\[
\mathsf S_\sigma=\frac1{1+d f_\sigma}
 \begin{pmatrix}
 c-d f_\sigma&-is\sqrt{\rho_\sigma}\\
 -is\sqrt{\rho_\sigma}&c-d\overline{f_\sigma}
 \end{pmatrix}.                                            \tag{4.8}
\]

One precise choice of the massive coordinate change is the polar
decomposition of its two-column local matrix W: its positive factor in the
`X` basis is `diag(sqrt(rho_+),sqrt(rho_-))`. The unitary factor acts on both
incoming and outgoing channel coefficients. This change can depend on E;
one must retain that dependence when calculating a delay in these
coordinates. Formula (4.3) fixes the original traveling-channel convention.

## 5. No spatial square-summable eigenstate when sin(g) is nonzero

Suppose `V psi = lambda psi` with `psi in H`. Unitarity implies
`|lambda| = 1`. Away from the origin, each component of `psi_+` satisfies a
one-way shift recurrence. On each relevant half-line its modulus is
constant, and square summability makes it zero. The recurrence at the
neighboring site also forces the value at the origin to vanish. Thus
`psi_+ = 0` everywhere.

The plus-sector equation at the origin is then

\[
0=-is(U_2\psi_-)(0).
\]

If `s != 0`, this gives `(U_2 psi_-)(0)=0`. The minus-sector equation gives
`psi_-(0)=0`. Consequently the entire remaining state satisfies the free
equation `U_2 psi_- = lambda psi_-` on all sites. Its Fourier determinant
(2.1) is not identically zero for any fixed lambda. Its zero set in k has
measure zero, so an L2 Fourier eigenfunction must be zero. This proves:

**Conditional theorem.** For `sin(g) != 0`, this four-channel point-contact
step has no nonzero spatial l2 eigenstate, including at band thresholds.

This excludes an exactly stable localized eigenstate of this step. It does
not exclude a transient, a scattering delay or a pole on a nonphysical
continuation, and it says nothing about a different multi-contact carrier
or the full finite-clock Hamiltonian.

## 6. Continuation sheets and the unsquared pole equation

The full unitary resolvent is analytic both outside and inside the unit
circle. Its physical massless local block inside is `G_0 = 0`, not `I/lambda`.
Accordingly no pole below the unit circle derived by retaining `I/lambda`
is a physical resolvent eigenvalue.

For scattering continuation, retain the exterior expression `G_0=I/lambda`.
This is the outgoing continuation of the massless channel. For the massive
factor distinguish:

1. `Delta_in`, analytic for `|lambda| < 1`, with `Delta_in(0)=1`.
   Continuation from the exterior through a massive gap reaches this branch.
2. `-Delta_in`, reached by local outgoing continuation from the exterior
   through a massive open-band arc.

These are statements about analytic continuation, not alternate physical
values of the same interior resolvent. A path through a gap and a path
through an open arc reach different points of the massive two-sheet surface.

On the massless-outgoing continuation, `F_0=0` reduces the determinant of
(4.1) to

\[
\det(I-FD)=D_+(\lambda)D_-(\lambda),\qquad
D_\sigma=1+d f_\sigma(\lambda).                            \tag{6.1}
\]

The branch value of f in this equation is part of the equation. To avoid
spurious threshold roots introduced by squaring, define

\[
\chi_\sigma=\frac{\lambda^2-a_{-\sigma}}{\Delta},\qquad
\chi_\sigma^2=\frac{\lambda^2-a_{-\sigma}}{\lambda^2-a_\sigma}.
\]

For `d != 0`, the original unsquared pole equation is

\[
\boxed{\chi_\sigma=1-\frac{2}{d(1+2i\sigma)}.}              \tag{6.2}
\]

Its right side is neither plus nor minus one for real c in `[-1,1)`.
Solving for `lambda^2` gives the sole possible finite nonthreshold location
for each sigma:

\[
\boxed{\lambda^2=p_\sigma(c)
 =a_\sigma\frac{c[1-2i\sigma(1-c)]}{c-2i\sigma(1-c)}.}      \tag{6.3}
\]

The denominator cannot vanish for such real c. The sheet must still satisfy
(6.2); equation (6.3) alone is insufficient.

For `-1 < c < 1`, `c != 0`,

\[
|\lambda|^4=|p_\sigma(c)|^2
 =\frac{c^2[1+4(1-c)^2]}{c^2+4(1-c)^2}<1.                  \tag{6.4}
\]

The four locations are `lambda = +/- sqrt(p_sigma(c))`. They are distinct
and nonzero: writing `d=1-c`,

\[
\Re p_\sigma=-\frac{c(3c+20d^2)}{5(c^2+4d^2)},\qquad
\Im p_\sigma=\frac{2\sigma c(2c+5d^2)}{5(c^2+4d^2)},
\]

and `2c+5d^2 = 5c^2-8c+5 > 0` for all real c.

Every one satisfies (6.2) on `Delta_in`. To check the sign without an
assumption, start at c=0. Then `p_sigma=0`, `Delta_in=1`, and both sides of
(6.2) equal `(3+4i sigma)/5`. Continue c over `(-1,1)`: the locations stay
strictly inside the circle, where Delta has no zero. The two algebraic
branch signs cannot interchange along this path. This proves the assignment
to `Delta_in`, including both square roots of p.

The poles in `S_{++,sigma}` are genuine on this assigned continuation:
at `D_sigma=0`, its numerator is `1+c != 0`. The roots are simple for
nonzero c because the map from `lambda^2` to `chi_sigma` has nonzero
derivative there and `lambda != 0`.

### Gap resonances versus mixed-sheet poles

For `-1 < c < 0`, the phase of each nonzero pole projects into a massive
gap. Indeed `Re p_sigma > 0`, so its projected `cos^2 E` exceeds `1/2`,
and hence exceeds `t^2`. On this arc the sheet just proved is precisely
outgoing for the open massless channel and decaying for the closed massive
channel. The poles are ordinary gap resonances of this specified
continuation. Their step-variable widths are

\[
\Gamma=-2\log|\lambda|
 =-\tfrac12\log\!
  \left(\frac{c^2[1+4(1-c)^2]}{c^2+4(1-c)^2}\right)>0.      \tag{6.5}
\]

This describes the exponential factor of a resonance pole. It is not a
proof that an arbitrary survival probability is a pure exponential at all
times; branch cuts and preparation also contribute.

For `0 < c < 1`, the projected phase instead lies strictly in a massive
open band. One exact way to check this is

\[
(3c+20d^2)^2-9(c^2+4d^2)(1+4d^2)
 =4d^2(55c^2-98c+55)>0.
\]

It implies `Re(p_sigma)/|p_sigma| < -3/5`, equivalently
`cos^2 E < 1/5`. The all-open outgoing continuation across that arc uses
`-Delta_in`, not `Delta_in`. Under this sign change

\[
f_\sigma\longmapsto -b_\sigma-f_\sigma.
\]

At a zero of the previously assigned denominator the other denominator is
`2-d b_sigma`, which is nonzero. Since (6.3) exhausts the possible finite
nonthreshold zeros, there are no nonzero denominator poles on this
specified all-open outgoing interior sheet for `0 < c < 1`.

Thus the positive-c poles are genuine poles on a mixed sheet, reached from
a massless-only gap, often called shadow poles. They must not be reported
as all-open outgoing resonances or used as a lifetime. In particular the
exact angle `g = 2 pi/5` has `0 < c < 1` and belongs to this case. This
finite-sheet pole statement does not exclude delays or transients.

### Exceptional contacts and thresholds

* `c=1`: the contact is the identity. `B=0`, `S=I`, and there are no contact
  poles. Taking the limit of (6.3) to a branch point does not create a pole.
* `c=0`: on `Delta_in`,
  `Delta=1+(3/5)lambda^2+O(lambda^4)` and
  `D_sigma=((4+2i sigma)/5)lambda^2+O(lambda^4)`.
  Consequently `S_{++,sigma}=1/D_sigma-1` has a genuine double pole at
  lambda=0 on this continuation. There is no finite logarithmic phase or
  finite width at zero, and no metastable lifetime is assigned to it.
* `c=-1`: the port sectors decouple. The massless matrix is exactly `-I`,
  including removable cancellations of the apparent poles in (4.6).
  The massive block has four genuine bound eigenvalues
  `lambda = +/- (9-2i sigma)/sqrt(85)`. Their squared values are
  `(77-36i sigma)/85`, and `cos^2 E=81/85>1/5`, so they lie in massive gaps.
  At these values `f_sigma=-1/2`; the nonzero point source in (4.1) produces
  an exponentially decreasing massive resolvent eigenfunction. The two
  roots for each sigma and the two sigmas are distinct. They are embedded
  in the full massless continuum but protected here by exact decoupling.
* At a branch point, `chi_sigma` is zero for one direction eigenchannel and
  divergent for the other. For real `d>0`, neither gives a zero of (6.2):
  `1-d b_sigma/2` cannot vanish, and a divergent term is not a zero. Such
  threshold branch singularities are not extra poles obtained by
  multiplying or squaring (6.2). Flux normalization at zero velocity is
  excluded rather than divided by zero.

No continuation pole off the unit circle is an eigenvalue of the full
unitary operator. The entire distinction relies on the named continuation
and is consistent with section 5.

## 7. Phase delay in the massive gaps

For `-1 < c < 1` and a compact interval strictly inside a massive gap, the
massless channel basis in (4.6) is fixed and its eigenphases are smooth.
The Wigner-Smith matrix in this convention is
`-i S^dagger partial_E S`. Its two eigenvalues are exactly

\[
\boxed{\tau_\sigma(E)
 =-\frac{s^2 y'_\sigma(E)}{[(1+c)/2]^2+d^2y_\sigma(E)^2},
\qquad
y'_\sigma(E)=\frac{\sigma\sin E-2\cos E}{5h(E)^3}.}         \tag{7.1}
\]

This follows by logarithmically differentiating (4.6); differentiating
`h^2=cos^2 E-t^2` gives the displayed derivative. In a massive gap,
`|sin E|<2|cos E|`, and `h` has the sign of `cos E`. Hence `y'_sigma<0`
and both delays are strictly positive when `s != 0`. They describe the
phase delay accumulated at the contact, in the declared time-step unit.

At `c=1` the delay is zero. At `c=-1` reduce the massless matrix to `-I`
before differentiating; its delay is zero, and an apparent `0/0` at a
decoupled massive bound-state phase is not a massless delay. No claim of
finite differentiability is made at a massive threshold. In open massive
bands (4.3) provides the complete smooth matrix away from thresholds, so
`-i S^dagger partial_E S` is defined in its fixed traveling-channel
convention; an E-dependent channel-coordinate change must include its
derivative and cannot be ignored.

## 8. Scope of the result

The point contact has an exact flux-unitary scattering solution. For
nonzero sector mixing it has no spatial l2 eigenstate. The closed-channel
correction, delay and gap resonance are local effects; the free step and
its velocities remain unchanged away from the contact.

The proof establishes neither a bulk mass term nor neutrino flavor,
fermionic statistics, a proton, a neutron or a beta-decay channel. It uses
one fixed one-particle carrier. A finite Fourier clock approximation is not
a premise and no failure of its error bound is used as a decay law.

All algebra above was derived symbolically in the text. No scientific
program, numerical run or two-architecture gate is claimed. A separate
in-session reviewer checked the local resolvent, pole algebra, sheet
distinction, endpoint contacts, phase derivative and flux normalization
after seeing the proposed formulas. This is an exposed algebraic
cross-check, not blind independent validation or formal acceptance.
