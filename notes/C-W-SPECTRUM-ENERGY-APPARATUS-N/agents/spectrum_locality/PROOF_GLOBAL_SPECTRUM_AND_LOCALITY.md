# Global spectrum of the actual contact walk and an exponentially local logarithm

Status: analytical derivation for the declared contact walk. No scientific program, numerical spectral calculation, or verifier was executed to obtain this proof. This note changes neither the contact convention nor the original walk. It does not identify the comparison walk with the native TWIST-J update.

## 1. Model and constants

Work on `ell^2(Z_R x Z_r) tensor C^4`. Let

\[
G=\frac{(I+2iX)\otimes(I+2iX)}5,
\quad W=\Gamma W_f,\quad W_f=SG,
\quad \Gamma=e^{-igV},\quad g=2\pi/5,
\]

where `V` is the projection onto `r=0` in all four coin channels. Contact follows streaming. The Fourier symbol of the free walk is

\[
W_f(P,q)=\operatorname{diag}(e^{iP},e^{iq},e^{-iq},e^{-iP})G.
\]

Define

\[
a=\arctan2,\qquad b=\pi-2a=2\arctan(1/2),
\]

\[
\delta=\pi-2b=4\arctan2-\pi=\arccos(7/25),
\qquad
\omega=\frac{\delta-g}{2},
\qquad
\alpha=\frac{\pi-g}{2}=3\pi/10.
\]

Here `arctan2` means the ordinary positive real number `arctan(2)`, not a two-argument programming function.

The constant `omega` is strictly positive. Indeed `delta,g` both lie in `(0,pi)`, and

\[
\cos g=\frac{\sqrt5-1}{4}>\frac7{25}=\cos\delta.
\]

The strict inequality is equivalent to `25 sqrt(5)>53`, whose squares are `3125>2809`.

## 2. Exact free spectral arcs

For the one-copy unitary

\[
U_1(k)=e^{ikZ}(I+2iX)/\sqrt5
\]

the two eigenvalues are `exp(+-i theta(k))`, with

\[
\cos\theta(k)=\cos k/\sqrt5,
\qquad \theta(k)\in[a,\pi-a].
\]

Put `k_1=(P+q)/2`, `k_2=(P-q)/2`. Then

\[
W_f(P,q)=U_1(k_1)\otimes U_1(k_2).
\]

The torus map from `(k_1,k_2)` to `(P,q)` is onto, and its two-to-one ambiguity changes both one-copy unitaries by a minus sign, leaving their tensor product unchanged. Hence it causes no spectral restriction.

The sum and difference of two independently variable angles in `[a,pi-a]` fill the intervals

\[
[2a,2\pi-2a]=[\pi-b,\pi+b],
\qquad [-\pi+2a,\pi-2a]=[-b,b].
\]

Consequently the spectrum of the full translation-invariant free walk is exactly

\[
\sigma(W_f)=
\{e^{i\phi}:\phi\in[-b,b]\cup[\pi-b,\pi+b]\}.
\tag{1}
\]

This is a statement about the whole direct integral over both momenta, not merely the rest fiber.

## 3. Two gaps survive the entire contact perturbation

Because `V` is an orthogonal projection,

\[
e^{ig/2}\Gamma-I
=(e^{ig/2}-1)(I-V)+(e^{-ig/2}-1)V,
\]

and therefore

\[
\|e^{ig/2}W-W_f\|=2\sin(g/4).
\tag{2}
\]

For completeness, if `B` is normal and `dist(z,sigma(B))>||A-B||`, then

\[
z-A=(z-B)\big[I-(z-B)^{-1}(A-B)\big]
\]

is invertible by a norm-convergent geometric series. Thus every spectral point of `A` lies within `||A-B||` of `sigma(B)`. Apply this to the two unitary operators in (2). On the unit circle chord distance at most `2 sin(g/4)` means angular distance at most `g/2`. Rotating back gives the rigorous spectral inclusion

\[
\sigma(W)\subseteq
\left\{e^{i\phi}:
\phi\in[-b-g,b]\cup[\pi-b-g,\pi+b]
\right\}.
\tag{3}
\]

This inclusion is sufficient; it is not asserted to be an equality. In particular the two open arcs

\[
(b,\pi-b-g)=(\alpha-\omega,\alpha+\omega)
\tag{4}
\]

and their translate by `pi` contain no spectrum of the full contact walk. The lower bound on each gap width is `2 omega=delta-g>0`. There is no finite-box approximation, no assumption about how a bound band behaves far from rest, and no extrapolation from its local gap in this argument.

## 4. One exact logarithm for all spectral sectors

Let `Log_alpha` have argument in `(alpha-2pi,alpha)` and define

\[
H=i\operatorname{Log}_{\alpha}W.
\tag{5}
\]

The cut runs through the proved gap (4). This is the analytic functional calculus of the actual `W`, not a logarithm of a discretized spectrum. It is a bounded self-adjoint operator and

\[
e^{-iH}=W,
\qquad
\sigma(H)\subset[-\alpha+\omega,2\pi-\alpha-\omega]
\subset(-3\pi/10,17\pi/10).
\tag{6}
\]

On the contact bound branch near rest, (5) gives exactly `H(P) chi_P=Omega(P) chi_P` with `Omega(0)=g`. In particular it preserves the previously proved branch curvature. If a nonnegative bookkeeping Hamiltonian is desired, `H+alpha I` is nonnegative, has width at most `2pi`, and has identical energy differences and commutators. Its exponential differs from `W` by the declared scalar phase `exp(-i alpha)`. Equation (5), rather than this shifted operator, is the exact logarithm in (6).

### An explicit global first-moment bound

Put

\[
U=e^{-i\alpha}W,
\qquad K=i(I+U)(I-U)^{-1}.
\]

The gap gives `dist(1,sigma(U))>=2 sin(omega/2)`. The Cayley transform `K` is bounded and self-adjoint, and scalar spectral calculus gives

\[
H=(\pi-\alpha)I-2\arctan K.
\tag{7}
\]

The identity

\[
\arctan A=\int_0^\infty e^{-t}\frac{\sin(tA)}t\,dt
\]

holds in norm for bounded self-adjoint `A`. Duhamel's identity implies
`||sin(tA)-sin(tB)||<=|t| ||A-B||`, so

\[
\|\arctan A-\arctan B\|\le\|A-B\|.
\]

Also `K=i[2(I-U)^(-1)-I]`, so two such Cayley transforms obey

\[
\|K_1-K_2\|
\le\frac{\|U_1-U_2\|}{2\sin^2(\omega/2)}.
\]

The same uniform spectral gap applies to every momentum fiber because its spectrum is contained in the global spectrum. Since

\[
W(P+\eta)=e^{i\eta Q}W(P),
\qquad Q=\operatorname{diag}(1,0,0,-1),
\]

we obtain

\[
\boxed{\quad
\|H(P+\eta)-H(P)\|
\le 2 C_H|\sin(\eta/2)|
\le C_H|\eta|,
\qquad C_H=\csc^2(\omega/2).
\quad}
\tag{8}
\]

In particular `H(P)` is norm differentiable with bounded derivative, preserves the natural domain of `R=i partial_P`, and its commutator with `R` extends to a bounded operator of norm at most `C_H`.

For the original scalar momentum kick `V_eta=exp(i eta R)`, (8) says

\[
\|V_\eta^\dagger H V_\eta-H\|
=\|[H,V_\eta]\|
\le2C_H|\sin(\eta/2)|.
\tag{9}
\]

For an independently moving reference carrying another copy of the same walk, use
`H_pair=H tensor I+I tensor H` and `V_eta=exp[i eta(R-Y)]`. The right sides of (8)-(9) are then multiplied by two. These are whole-space operator bounds and therefore include all scattering and bound spectral sectors.

## 5. Exponential spatial tails, with explicit constants

The functional calculus in (5) is exponentially local in both original integer coordinates. Here is a proof with conservative explicit constants.

Set

\[
\rho=\tfrac12\sin(\omega/2),
\qquad \mu=\log(1+\rho/2).
\]

Take the boundary `C` of the annular sector

\[
1-\rho<|z|<1+\rho,
\quad \alpha-2\pi+\omega/2<\arg_\alpha z<\alpha-\omega/2.
\]

It encloses all of `sigma(W)` and avoids the logarithm cut and zero. Its distance to the spectrum is at least `rho`: the circular edges have radial distance `rho`; on the radial edges the angular separation is at least `omega/2`, so the distance is at least `sin(omega/2)=2rho`. Its length and a bound on its logarithm are

\[
\ell_C=4\pi-2\omega+4\rho,
\qquad
F_C=2\pi-\alpha-\log(1-\rho).
\]

Let `d(x,F)` be the lattice `ell^1` distance from the spatial point `x=(R,r)` to a set `F`, and let
`M_N(x)=exp[mu min(d(x,F),N)]` act trivially on the coin. These bounded weights commute with `Gamma` and `G`. Every streaming displacement has lattice length at most one, so

\[
\|M_N W M_N^{-1}-W\|\le e^\mu-1=\rho/2.
\]

The resolvent geometric series and the Cauchy formula therefore yield, uniformly in `N`,

\[
\|M_N H M_N^{-1}\|
\le C_0:=\frac{\ell_C F_C}{\pi\rho}.
\tag{10}
\]

For a vector supported in `F`, passage to the limit in the weights gives

\[
\|1_{\{d(x,F)\ge l\}}H\psi\|
\le C_0 e^{-\mu l}\|\psi\|.
\tag{11}
\]

In particular every matrix entry of `H` decays exponentially in the original spatial distance. The bound is deliberately conservative and is not a claim of an optimized physical interaction length. The pre-existing no-go theorem for a *strictly finite-range* autonomous logarithm is respected: exponential tails are nonzero at arbitrarily large distances.

For later propagation estimates, the resolvent identity also gives

\[
\|M_NHM_N^{-1}-H\|
\le K_\mu:=\frac{\ell_C F_C}{2\pi}
\frac{e^\mu-1}{\rho[\rho-(e^\mu-1)]}
=\frac{\ell_C F_C}{2\pi\rho}.
\tag{12}
\]

Since `H` is self-adjoint, a Dyson bound then gives

\[
\|M_Ne^{itH}M_N^{-1}\|\le e^{K_\mu|t|}.
\tag{13}
\]

These formulas extend to two independent copies with the sum lattice metric and at most twice `K_mu` for their sum Hamiltonian.

## 6. What this does and does not give the spectral battery

In the Fourier-conjugate time coordinate `t` of an ideal continuous energy weight, the energy-conserving lift of a spatially diagonal kick has conditional system action

\[
U(t)=e^{itH}V_\eta e^{-itH}
\]

up to the harmless opposite sign convention for `t`. For each fixed `t`, (13), and the commutation of `V_eta` with the spatial weights, give

\[
\|M_N U(t)M_N^{-1}\|\le e^{2K_\mu|t|}.
\tag{14}
\]

A compact sine profile of energy width `L`,

\[
\beta_L(E)=\sqrt{2/L}\sin[\pi(E-E_0)/L]
\quad(E_0\le E\le E_0+L),
\]

and zero elsewhere, has `||beta_L'||=pi/L`. Its unitary Fourier transform obeys
`integral t^2 |beta_tilde(t)|^2 dt=pi^2/L^2`. Thus, for any normalized input supported in `F`, the ideal lifted output satisfies for every `T>0`

\[
\|1_{d(x,F)\ge l}\,U(\psi\otimes\beta_L)\|
\le e^{-\mu l+2K_\mu T}+\frac\pi{LT}.
\tag{15}
\]

For `l>0`, the choice `T=mu l/(4K_mu)` gives

\[
\|1_{d(x,F)\ge l}\,U(\psi\otimes\beta_L)\|
\le e^{-\mu l/2}+\frac{4\pi K_\mu}{L\mu l}.
\tag{16}
\]

The same result applies to a bounded positive battery construction on input states for which that construction exactly agrees with the ideal lift; the energy margin in the separate spectral-lift proof supplies this condition.

Equations (14)-(16) are state-dependent spatial tail bounds. They do not make the whole battery unitary a finite-range quantum circuit, nor a uniform finite-time local interaction on all battery states. Its conjugate time variable is unbounded, and all values occur in the Fourier representation. A complete spatial apparatus implementation and an internal stopping clock are additional constructions, not consequences of a spectral change of basis.

## 7. Exponential locality does not select a unique energy

The two spectral clusters in (3) remain separated by both gaps. Define

\[
A=\operatorname{Re}(e^{ig/2}W),
\qquad P_-=1_{(-\infty,0)}(A).
\]

If `c=b+g/2=pi/2-omega`, then the spectrum of `A` lies in
`[-1,-sin(omega)] union [sin(omega),1]`. Thus `P_-` is a Riesz projection onto the second spectral cluster. Its functional calculus is analytic on disjoint neighborhoods of the two clusters; the same weighted-resolvent argument proves exponential spatial decay of its matrix entries.

For every fixed integer `m`,

\[
H_m=H+2\pi mP_-
\tag{17}
\]

is bounded, self-adjoint, exponentially local, and has `exp(-i H_m)=W`. The contact bound branch near rest belongs to the positive cluster of `A`, since its centered phase at rest is `-g/2`, and therefore every `H_m` has the *same* bound energy `Omega(P)` near rest. Locality plus the branch energy does not remove this freedom.

It also produces an observable work ambiguity for a bare kick. At rest write

\[
\chi_0=\delta_{r0}(|++\rangle-|--\rangle)/\sqrt2,
\qquad s_0=\delta_{r0}(|++\rangle+|--\rangle)/\sqrt2.
\]

The exact coin/contact action gives

\[
\langle s_0,W(0)s_0\rangle=-\tfrac35 e^{-ig},
\quad
\langle s_0,A(0)s_0\rangle=-\tfrac35\cos(g/2).
\]

Since `A>=-P_-`, it follows that

\[
\|P_-(0)s_0\|^2\ge\tfrac35\cos(g/2)>0.
\tag{18}
\]

The prior contact proof gives in a parallel gauge

\[
\chi'_0=i\gamma(\gamma-W_b)^{-1}s_0,
\qquad \gamma=e^{-ig},
\]

where `W_b` is the restriction orthogonal to the rest bound state. On the negative cluster `|gamma-lambda|<=2`; its spectral measure therefore gives

\[
\beta_-:=\|P_-(0)\chi'_0\|^2
\ge\tfrac14\|P_-(0)s_0\|^2
\ge\frac3{20}\cos(g/2)>0.
\tag{19}
\]

The analytic identity `P_-(P) chi_P=0` implies

\[
\|P_-(\eta)\chi_0\|^2
=\beta_-\eta^2+O(\eta^3).
\tag{20}
\]

Thus the same bare rest-fiber kick has a work difference between the energy readings (17) equal to

\[
\Delta\mathcal W_m-\Delta\mathcal W_0
=2\pi m\beta_-\eta^2+O_m(\eta^3).
\tag{21}
\]

The leading coefficient is strictly positive for positive `m`. The existing finite-binomial-packet argument transfers this to the earlier actual preparations: for `N=q^4`, `eta~2/q`, an even momentum density has second moment `O(q^-4)`, and the additional packet correction is `O_m(q^-4)=o(eta^2)` for every fixed `m`. The projections in (17) are now global analytic spectral projections, so this is a stronger locality statement than one obtained from an arbitrary measurable branch assignment.

The role of (17)-(21) is precise. A battery attached to the chosen `H` can conserve that energy exactly. The same `W`, its local bound energy and its exponential spatial locality do not by themselves determine that choice.

