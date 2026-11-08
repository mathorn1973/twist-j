# Finite integer preparation, controlled response, and construction boundaries

Status: NON-CANONICAL / L1, analytical construction review. This note was
derived from the stated contact operator and the preceding proofs without
executing any scientific program. It supplies a positive preparation and
an explicit limiting protocol; it is not native admission or an energy
account for a physical actuator. No preceding package has been modified.

Sources read as text: the preceding TARGET.md, PROOF_NATIVE.md,
prior_contact/PROOF_CONTACT.md (actual displacement and impulse sections),
and prior_contact/BREAK_REVIEW.md (normalizable bound-packet extension).

## 1. What must be corrected before claiming a positive construction

The exactly bound packet used in the preceding theorem has a compact
momentum support and infinite center-position support. A nonzero finitely
supported position vector has a trigonometric-polynomial Fourier
transform and cannot have compact support in a proper momentum interval.
Thus a finite integer wave register cannot literally contain that exact
target packet at a finite stage. Replacing it by a finite preparation
requires an explicit approximation theorem, including the error after
division by the small impulse. Norm density alone does not supply that
last statement.

The construction below avoids preparing unknown coefficients of the
analytic eigenvector chi_P. The actual prepared state uses integer
binomial coefficients and the compact rest coin vector. The exactly
bound packet enters only as a comparison in the proof.

The other main boundaries are:

1. A finite-support packet has momentum tails on the whole circle. Its
   principal momentum change is not exactly eta: a wrapping correction
   must be included.
2. The gate xi^(R-Y) preserves common translations exactly, hence total
   quasimomentum modulo 2pi. An unrestricted operator identity conserving
   the sum of two principal momentum coordinates would be false.
3. The same gate factors as xi^R tensor xi^(-Y). It is a specified balanced
   pair impulse. It does not by itself derive a mutual interaction,
   entanglement production, autonomous switching or an energy debit.
4. The normalized integer-amplitude reading is one fixed current-state
   reading. Its norm, complex embedding and wave update are declared
   additional structure. They are not consequences of the original U.
5. No minimality theorem among all possible extensions has been proved.

## 2. An explicit finite integer preparation

For an integer N>=1 define

\[
b_N(R)=\binom{2N}{N+R}\quad(-N\le R\le N),
\qquad Z_N=\sum_Rb_N(R)^2=\binom{4N}{2N}.
\]

Set the actual normalized state to

\[
\psi_N(R,r)=\frac{b_N(R)\delta_{r0}}{\sqrt{2Z_N}}
\begin{pmatrix}1\\0\\0\\-1\end{pmatrix}.
\tag{2.1}
\]

Before the fixed normalization reading, every stored entry is an integer.
The support has exactly 2N+1 center sites and one relative site. The square
root in (2.1) belongs to the reading, rather than to a list of prepared
transcendental amplitudes. The same reading normalizes every nonzero
integer/algebraic coefficient vector; it is not adjusted to N, time or
impulse after observing a result.

With the preceding Fourier convention,

\[
\sum_R b_N(R)e^{-iPR}=4^N\cos^{2N}(P/2),
\qquad
\widehat\psi_N(P)=f_N(P)\chi_0,
\quad f_N(P)=\frac{4^N\cos^{2N}(P/2)}{\sqrt{Z_N}}.
\tag{2.2}
\]

All integrals below use dP/(2pi) on [-pi,pi). The density w_N=|f_N|^2
is even and normalized. The elementary integration recurrence for even
powers of cosine gives the exact identity

\[
\int\sin^2(P/2)w_N(P)\frac{dP}{2\pi}
=\frac1{4N+2}.
\tag{2.3}
\]

Indeed, the ratio of the integrals of cos^(4N+2) and cos^(4N) is
(4N+1)/(4N+2). Since |P|<=pi|sin(P/2)| on this principal interval,

\[
m_{2,N}:=\int P^2w_N(P)\frac{dP}{2\pi}
\le\frac{\pi^2}{4N+2}.
\tag{2.4}
\]

No tail fitting or approximate Fourier transform is used here.

## 3. Uniform comparison with a genuinely bound packet

Choose rho>0 so that the isolated analytic branch exists on [-2rho,2rho].
Shrink it if necessary so there are constants A_chi,A_Omega,Delta>0 with

\[
\|\chi_p-\chi_q\|\le A_\chi|p-q|,
\qquad |\Omega''(p)-\kappa|\le A_\Omega p^2,
\tag{3.1}
\]

and a spectral separation at least Delta between the branch and its
complement throughout that interval. The second estimate follows from
the even analytic phase. Fix a smooth even cutoff h with 0<=h<=1,
h=1 on [-rho/2,rho/2], and support inside [-rho,rho]. Let

\[
t_N=\|h f_N\|_2>0,
\qquad
\phi_N(P)=t_N^{-1}h(P)f_N(P)\chi_P.
\tag{3.2}
\]

This is an exactly bound, normalizable comparison packet. It is never
substituted for the actually stored integer vector (2.1).

Chebyshev's inequality and (2.4) give

\[
t_N^2\ge1-\frac{4m_{2,N}}{\rho^2}.
\tag{3.3}
\]

Write A=2/rho+A_chi. Before normalization, the cutoff loss has norm at
most 2 sqrt(m2)/rho, and the change from chi_0 to chi_P has norm at most
A_chi sqrt(m2). The reverse triangle inequality bounds the additional
normalization error by their sum. Consequently

\[
\epsilon_N:=\|\psi_N-\phi_N\|
\le2A\sqrt{m_{2,N}}
\le\frac{2A\pi}{\sqrt{4N+2}}.
\tag{3.4}
\]

If 4m2/rho^2<=1/2, the comparison packet's second momentum moment obeys

\[
m_{2,\phi_N}\le2m_{2,N}.
\tag{3.5}
\]

Unitarity preserves the norm difference exactly under every free time:

\[
\|W^t\psi_N-W^t\phi_N\|=\epsilon_N
\quad(t\in\mathbb Z).
\tag{3.6}
\]

Thus the small preparation error does not grow with the duration of the
subsequent exact walk. This is stronger than a fixed finite-time density
statement.

On the chosen compact branch interval the relative eigenvectors have
uniform exponential tails. If their tail probability outside |r|<=B is
at most C_b exp(-a_b B), then the actual finite preparation satisfies

\[
\Pr_{W^t\psi_N}(|r|>B)
\le\bigl(\sqrt{C_b}e^{-a_bB/2}+\epsilon_N\bigr)^2
\quad\text{for every }t.
\tag{3.7}
\]

This follows by applying the relative-tail projection to (3.6). It is a
uniform approximate binding statement. The finite preparation is not
claimed to lie exactly in the bound spectral subspace.

## 4. A fixed-field sequence of exact small phases

For precision index L>=1 put

\[
q_L=5^L,\qquad
\xi_L=\frac{q_L+i}{q_L-i}
=\frac{q_L^2-1+2iq_L}{q_L^2+1},
\qquad
\eta_L=2\arctan(q_L^{-1}).
\tag{4.1}
\]

Then |xi_L|=1 and xi_L=exp(i eta_L). For q>=1,

\[
q^{-1}\le\eta_L\le2q^{-1},\qquad\eta_L\longrightarrow0.
\tag{4.2}
\]

Every phase already belongs to Q(i). No roots of unity of orders 5^L
are added. For L>=1, xi_L is not a root of unity: the only roots of unity
in Q(i) are +/-1,+/-i, and its angle is strictly between zero and pi/2.
The coefficient number field Q(i,j) can therefore stay fixed. Integer
numerators and denominators, or equivalent projective integer contents,
grow with L.

On a finite support |R|<=M the exact kick K_L is multiplication by xi_L^R.
Let d=q^2+1 and a=q^2-1+2iq. A common Gaussian-integer numerator is

\[
d^{M-|R|}
\begin{cases}a^R,&R\ge0,\\\bar a^{-R},&R<0,\end{cases}
\tag{4.3}
\]

with common denominator d^M. Replacing a by its conjugate gives the
inverse. This is a finite exact arithmetic prescription on every finite
state. How equivalent denominator encodings are canonicalized must be
specified by the actual construction; an inverse only up to an unstated
rescaling is not an inverse of an unquotiented carrier.

## 5. The actual mean-current error

Let D be the actual one-tick center displacement from the previous proof.
It is independent of P, has norm one, and has zero expectation in chi_0.
Let

\[
D_T=\frac1T\sum_{t=0}^{T-1}W^{-t}DW^t,
\qquad\|D_T\|\le1.
\tag{5.1}
\]

For every normalized u,v and bounded A,

\[
|\langle u,Au\rangle-\langle v,Av\rangle|
\le2\|A\|\,\|u-v\|.
\tag{5.2}
\]

This follows by expanding the difference as <u-v,Au>+<v,A(u-v)>.
Kicks and free evolution are unitary, so (3.4) and (5.2) compare the
actual and bound-reference mean currents with error at most 2 epsilon_N,
independently of T. If a protocol subtracts two independently approximated
baseline currents, the safe bound is 4 epsilon_N; here both un-kicked
baselines are exactly zero by the common reflection symmetry.

For the exactly bound reference phi_N and |eta|<=rho, the preceding
unprojected impulse proof gives

\[
\left|v_T(\phi_N,\eta)
-\int w_{\phi_N}(p)\Omega'(p+\eta)\frac{dp}{2\pi}\right|
\le2A_\chi^2\eta^2+\frac{4A_\chi|\eta|}{T\Delta}.
\tag{5.3}
\]

The even reference density has zero mean p and zero initial current.
Integrating Omega''-kappa between p and p+eta, with (3.1), yields the
sharper moment form

\[
\left|\int w_{\phi_N}(p)\Omega'(p+\eta)\frac{dp}{2\pi}
-\kappa\eta\right|
\le A_\Omega |\eta|
\left(m_{2,\phi_N}+\frac{\eta^2}{3}\right).
\tag{5.4}
\]

The mixed term in (p+s)^2 vanishes because the density is even. Combining
(5.2)--(5.4), the ACTUAL integer-prepared, unprojected packet satisfies

\[
\boxed{
\left|\frac{v_T(\psi_N,\eta)}{\eta}-\kappa\right|
\le A_\Omega\left(m_{2,\phi_N}+\frac{\eta^2}{3}\right)
+2A_\chi^2|\eta|+\frac{4A_\chi}{T\Delta}
+\frac{2\epsilon_N}{|\eta|}.}
\tag{5.5}
\]

There is no projection after the kick. The coefficient of 1/T comes from
the spectral-gap geometric sum, not assumed pointwise decay of the other
bands. In particular the first post-kick tick still has exactly zero
mean displacement for the actual preparation. Long-time averaging is an
essential part of this stated response protocol.

The same error bound is uniform in any additional nonnegative waiting
time m before the impulse. Compare W^m psi_N with W^m phi_N; their norm
distance is still epsilon_N. The reference acquires only the scalar
fiber phase exp(-im Omega(p)), which does not change any of the post-kick
fiber current expectations. The actual un-kicked mean current remains
zero by reflection symmetry. Since the scalar kick commutes with the
P-independent displacement D, the first post-kick current is still zero.
Only the finite stored support needed to perform the extra waiting grows.

## 6. An explicit sufficient integer schedule

Choose once and for all

\[
\boxed{q_L=5^L,\qquad N_L=q_L^4,\qquad T_L=q_L.}
\tag{6.1}
\]

For all sufficiently large L, the local branch conditions and (3.5) hold.
With A=2/rho+A_chi, (2.4), (3.4), (4.2), and (5.5) give

\[
\left|\frac{v_{T_L}(\psi_{N_L},\eta_L)}{\eta_L}-\kappa\right|
\le\frac{2A\pi+4A_\chi^2+4A_\chi/\Delta}{q_L}
+\frac{4A_\Omega}{3q_L^2}
+\frac{A_\Omega\pi^2}{2q_L^4}.
\tag{6.2}
\]

Thus the differential mean response converges to the previously derived
kappa with a proved O(5^-L) error. The constants are defined by one fixed
analytic branch neighborhood and do not vary with L. This is a sufficient
resource schedule, not an optimized or minimal one. Its asymptotic proof
does not require executing the enormous N=q^4 preparations for large L.
An explicit numerical accuracy guarantee would additionally require
certified values for those branch constants; no such numerical values are
silently supplied by this note.

Before intervention the preparation is uniformly within O(q^-2) of an
exactly bound process. After intervention it is uniformly within
epsilon_N+A_chi|eta| of the corresponding shifted bound-band preparation.
Equation (3.7) consequently holds after the kick with this larger error.
This controls a small radiative component for all subsequent times.

## 7. Exact quasimomentum and the principal-coordinate correction

For eta>0 and the actual finite packet, the principal momentum change is
exactly

\[
\delta p_N(\eta)
=\eta-2\pi\int_{\pi-\eta}^{\pi}w_N(p)\frac{dp}{2\pi}.
\tag{7.1}
\]

For eta<=pi/2, the tail interval has |p|>=pi/2. Equations (2.4) and
Chebyshev give

\[
0\le1-\frac{\delta p_N(\eta)}{\eta}
\le\frac{8\pi}{\eta(4N+2)}.
\tag{7.2}
\]

Along (6.1), this is at most 2pi/q^3. The actual principal impulse is
therefore positive for all L>=1 and is asymptotic to eta. The small-angle
restriction eta<=pi/2 already holds for q=5^L, L>=1. Together with (6.2),

\[
\frac{v_{T_L}(\psi_{N_L},\eta_L)}{\delta p_{N_L}(\eta_L)}
\longrightarrow\kappa.
\tag{7.3}
\]

The exact operator conservation law for a reference coordinate Y and
V_L=xi_L^(R-Y) is

\[
[V_L,\mathsf T_R\mathsf T_Y]=0.
\tag{7.4}
\]

It preserves the complete total quasimomentum distribution. In a common
nonwrapping support chart, this also reads as opposite ordinary momentum
increments. The finite binomial packets have the explicitly bounded
wrapping correction instead. If the initial reference has the same even
momentum density as the particle, the opposite principal mean changes
cancel exactly by reflection symmetry, even though the unrestricted
principal-coordinate operator identity remains false.

## 8. Scope of the paired gate

The equality

\[
\xi_L^{R-Y}=\xi_L^R\otimes\xi_L^{-Y}
\tag{8.1}
\]

must not be hidden. This mathematical gate gives a balanced pair impulse
and a reference that can record the opposite momentum change. It does
not generate entanglement from product preparations and does not specify
an autonomous interaction energy or the cost of changing the coupling.

A genuinely nonseparable diagonal extension can be defined, if separately
desired, by an integer F_M(d) equal to d for |d|<=M and zero outside,
and V=xi_L^(F_M(R-Y)). It agrees exactly with the paired kick on every
preparation whose whole position support satisfies |R-Y|<=M, and it still
commutes with common translations. Globally it is a different finite-range
pair gate. Its range, switching and added law are new resources. This
optional alternative is not needed for (6.2) and is not admitted as
native by this review.

The construction's actual coin and streaming map supplies a real current
state evolution, rather than evaluating W^n only inside a time-dependent
decoder. Nevertheless the spatial carrier, amplitudes, arithmetic ring,
coin, contact phase reading, preparation and impulse gate all have to be
declared. An original-U conserved label selecting a phase is a genuine
source-dependent control, but does not derive the rest of those laws.

## 9. Suggested frozen falsifiers

- Verify the exact binomial coefficient recurrence and the Vandermonde
  norm Z_N, with explicit prepared coefficients, not merely a printed norm.
- Verify the actual integer coin, streaming convention and left contact,
  as well as the inverse, on multiple nontrivial finite preparations.
- Verify canonical representation after inverse operations. Retaining an
  unquotiented denominator record while returning only a scalar multiple
  is not exact reversibility of that carrier.
- Verify |a|^2=d^2 for a=q^2-1+2iq, including negative-coordinate kick
  powers and both signs of the paired impulse.
- Verify readout commutation for the actual stored update, not only for a
  pre-evaluated target orbit or an inserted list of zero residuals.
- Verify first-tick zero current and at least one actual later nonzero
  current from the same kicked finite preparation, with the full walk.
- Keep the universal approximation theorem separate from finite numeric
  convergence observations; test exact identities behind its moments and
  norms, rather than fitting a slope or choosing N after seeing outputs.
- Preserve the distinction between exact circle-translation conservation,
  the principal-coordinate correction, norm preservation and energy
  conservation. None of the first three implies an energy-transfer law.
- Count all added retained records and variable support. Do not claim a
  realization within the unchanged finite-width original-U theorem.

## Verdict

The finite integer preparation and exact Cayley-phase kicks give a
constructive positive route to the full unprojected mean inertial response
of the existing declared contact model. The limit and an explicit
sufficient resource schedule are proved without preparing an infinite
analytic eigenvector or fitting numerical data. The permanent exact
binding claim must be weakened to the uniform approximation bounds above
at every finite stage. Native admission, autonomous switching, a complete
energy account and global minimality of the extension remain distinct
construction questions.
