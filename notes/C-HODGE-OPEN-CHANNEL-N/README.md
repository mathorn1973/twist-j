# C-HODGE-OPEN-CHANNEL-N

**A. M. Thorn. NON-CANONICAL. Action layer L1.**

**Exact reduction of the open object channel, with its physical current.**
Analytical statements below are candidate-T; the finite exact audit, when
executed under [PREREG.md](PREREG.md), is candidate-C evidence at its stated
scope. This is a separate successor to frozen
[draft #1721](https://github.com/mathorn1973/twist-j/pull/1721).
Claim: [#1722](https://github.com/mathorn1973/twist-j/issues/1722).

Throughout this note, the complete circuit means the source sector with
one object pair, one token or pulse, and one encoded receiver, retaining
every listed channel and spectator. The larger many-occupation native
circuit is not claimed to have this two-arrangement reduction.

## 1. Physical result

The token/object arrangement can be eliminated **causally and exactly**,
without an inverse on the continuum spectrum. What replaces it is a
coherent memory of the pulse together with the prescribed incoming object
state. The physical spatial charge and current become explicit bilinear
forms on that history. This keeps object transport even when no pulse is
present.

The unchanged circuit also generates a nonreal return amplitude of its
own. For its token walk \(U_T=e^{-i\beta}W\), contact vector
\(\alpha=iB\), \(g=2\pi/5\), and \(\beta=4\pi/5\),

\[
 \mu_2=\langle\alpha,U_T^2\alpha\rangle=\frac45,
 \qquad
 \mu_4=\frac{80-28e^{ig}}{125}.
\]

After contact damping the first two nonzero memory coefficients are

\[
 g_1=\frac45,\qquad g_3=\frac{48-28e^{ig}}{125}.
\]

Thus the first pulse feedback over three periods is
\(-64U_PP_P/125\), and the feedback over five periods is

\[
 \frac{-768+448e^{ig}}{3125}\,U_PP_P.
\]

Its imaginary part is nonzero. This is a source-derived coherent phase
between delayed amplitudes, not yet an identification with the Hodge
rotation or its metric.

## 2. The actual reduced law

Keep all positions, both pulse banks, all object coin states, all carrier
and old-memory labels, and every receiver position. In the token/pulse
arrangement decomposition let

\[
 U=\begin{pmatrix}A&B\\G&D\end{pmatrix},
 \qquad
 \begin{aligned}
 A&=U_T(I-\tfrac25P_T),&
 B&=-\tfrac45U_TV_TV_P^\dagger,\\
 G&=\tfrac45U_PV_PV_T^\dagger,&
 D&=U_P(I-\tfrac25P_P).
 \end{aligned}
\]

The interface isometries \(V_T,V_P\) put the same carrier position and
labels into the two actual contact vectors; \(P_T=V_TV_T^\dagger\)
and \(P_P=V_PV_P^\dagger\). The complete receiver is contained in
\(U_P\).

For the given incoming object state \(t_0\), the reduced equation is

\[
 \boxed{p_{m+1}=Dp_m+GA^mt_0+
       \sum_{j<m}GA^{m-1-j}Bp_j.}
\]

The eliminated arrangement is reconstructed by

\[
 t_m=A^mt_0+\sum_{j<m}A^{m-1-j}Bp_j.
\]

These two formulas are equivalent to the full original unitary circuit
for every initial packet and every finite time. Their proof uses no
choice of momentum, boundary condition, stationary limit or energy
subwindow. The contact memory is scalar in the retained interface labels:
\(GA^kB=-16g_kU_PP_P/25\). The object continuum survives in the return
sequence and in the charge kernels; it has not been replaced by a finite
closed oscillator.

See [PROOF_REDUCTION.md](PROOF_REDUCTION.md) for the explicit derivation,
the exact invariant contact-cyclic space and its dark complement.

## 3. What current is preserved

For the physical cut \(\ell+1/2\), use exactly the native right charge

\[
 N_{R,\ell}=2P^A_R+2P^B_R+4P^c_R+2P^z_R+N_{\rm anc,R},
 \quad x_A=R+r,\ x_B=R-r.
\]

It is block diagonal, \(N_T\oplus N_P\), on the two arrangements.
The weights are inherited from the full occupied-code charge; they are
not chosen to make a transfer matrix unitary.

The active charge is bounded by 10. If the unchanged ancillary factor has
unbounded charge, the charge forms are defined on its finite-charge form
domain, which the dynamics preserves.

Substituting the reconstructed \(t_m\) into

\[
 q_m=\langle t_m,N_Tt_m\rangle+\langle p_m,N_Pp_m\rangle
\]

produces an explicit two-time history Gram matrix. Its entries include

\[
 B^\dagger(A^\dagger)^aN_TA^bB,
 \qquad (A^\dagger)^mN_TA^bB,
\]

so interference between different delays and with the initial object
state is retained. The corresponding physical current obeys
\(q_{m+1}-q_m=j_{\ell,m}\), including the polarized bilinear and
sitewise continuity identities. It is the same current derived directly
from the source gates in #1721, including both object constituents,
pulse-edge coherence, receiver labels and simultaneous crossings.

The complete formulas and proof are in
[PROOF_CURRENT.md](PROOF_CURRENT.md). No claim is made that this native
current equals a local current of the separate spectral-logarithmic
energy reading.

## 4. Two reductions that demonstrably lose physical information

**Deleting the incoming object.** Take an incoming token arrangement with
\(x_A=99,x_B=105\), first object coin, token at 0, and receiver at 100.
The pulse remains zero for the first four periods. Nevertheless the
first current through 99.5 is exactly \(8/5\). A pulse-only account
would give zero.

**Deleting contact-dark states.** The contact-cyclic space is an exact
dynamical reducing space, but its projector does not commute with the
physical half-space charge. The proof constructs a normalized even
inversion-parity dark state \(d\) for which

\[
 \langle W^2\alpha,N_{T,\ell}d\rangle=\frac{2\sqrt2}{5}\ne0
 \quad(\ell=n).
\]

A corresponding pair of initial states has identical complete future
pulse histories and different physical currents already at the first
period. The incoming dark component must therefore remain in the
reconstruction and the observable, unless a narrower initial-state class
is explicitly imposed. The exact reduction above retains it.

## 5. The open contact response and its domain

For \(|z|<1\), define the actual token Caratheodory function

\[
 F(z)=\langle\alpha,(I+zU_T)(I-zU_T)^{-1}\alpha\rangle.
\]

The reduced contact response is exactly

\[
 \boxed{s(z)=\frac{4-F(z)}{4+F(z)}}.
\]

It follows from the causal circuit and a rank-one resolvent calculation.
For regular absolutely continuous radial boundary values, with
\(a=\operatorname{Re}F>0\),

\[
 1-|s|^2=\frac{16a}{|4+F|^2}.
\]

This defect is the retained open object port. In the source's fixed
incoming/outgoing convention, its normalized contact relation is

\[
 \begin{pmatrix}q_{\rm out}\\\eta_{\rm out}\end{pmatrix}
 =\frac1{4+F}
 \begin{pmatrix}4-F&4\sqrt a\\-4\sqrt a&4-\overline F\end{pmatrix}
 \begin{pmatrix}q_{\rm in}\\\eta_{\rm in}\end{pmatrix}.
\]

The radiation-jump derivation, domain and sign convention are supplied
in [PROOF_PORT.md](PROOF_PORT.md). This relation is unitary in its
spectral port normalization. The physical spatial current still requires
the actual charge kernels above; the two statements are not conflated.
Finite radial boundary values are an almost-everywhere statement, not
an assertion at every point of the closed source energy interval.

## 6. What is now available for a geometry test

The source provides a specific causal action, an open-channel response,
nontrivial coherent memory and a correctly transported native current.
The previous failure of a bounded full-slice stationary inverse no longer
prevents this reduction. There is no earned finite-dimensional
memoryless Lorentz/Hodge carrier yet.

A subsequent test must specify an invariant transmitting domain and show
that its actual history/current form descends to the proposed finite
carrier. Its full action and form must then satisfy the desired
intertwining equations on the declared admissible class. Matching a
single coefficient, an eigenvalue or a selected energy would not establish
that result. The noncommuting dark-current example is an explicit test
any proposed quotient must pass.

## 7. Proof and audit boundary

- [PROOF_REDUCTION.md](PROOF_REDUCTION.md): exact law, reconstruction and
  actual cyclic/dark decomposition.
- [PROOF_CURRENT.md](PROOF_CURRENT.md): expanded history charge/current,
  bilinear continuity and counterexamples to lossy quotients.
- [PROOF_PORT.md](PROOF_PORT.md): source returns, scalar response and the
  open object port.
- [PREREG.md](PREREG.md): accepted finite audits and first-execution rule.
- [SOURCES.md](SOURCES.md): immutable source and predecessor pins.
- [verify.py](verify.py) and [break_certificate.py](break_certificate.py):
  accepted exact finite audits, not proofs of a stationary whole-window
  or geometric identification.

This README is part of the pre-execution contract. The original execution
disposition and exact output, if produced, belong in the separate RESULT,
RUN and EXPECTED files. No execution outcome is assumed here. Only this
new notes directory is in scope; Canon and frozen predecessors are not
changed or promoted.
