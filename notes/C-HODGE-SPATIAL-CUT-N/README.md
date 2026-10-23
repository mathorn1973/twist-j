# C-HODGE-SPATIAL-CUT-N: the physical cut and its native current

**A. M. Thorn. NON-CANONICAL. L1. Analytical candidate-T; finite audits
candidate-C.** Claim [#1720](https://github.com/mathorn1973/twist-j/issues/1720).
No public scientific status is promoted by this note.

The concrete cut is between sites **99 and 100**, immediately before the
receiver in the original preparation. The derivation holds for every cut
\(\ell+1/2\), every receiver position and their coherent superpositions.
Site 100 enters the preparation, not the local law.

**Result.** The actual circuit gives an explicit spatial *relation*, together
with an exactly determined native-charge current. The pulse edge has a
golden transfer factor. The complete relation also carries the two object
constituents, the token constraint, the old receiver memory and all dark
directions. In the original energy window the complete token arrangement
cannot be eliminated by a bounded inverse on its full object slice.

The source is the unchanged [homogeneous capture and receiver law](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md).
Exact upstream definitions, hashes and predecessor boundaries are in
[SOURCES.md](SOURCES.md).

## 1. The physical quantity that crosses the cut

In the full encoded sector, with \(x_A=R+r\), \(x_B=R-r\), carrier position
\(x_c=y\) for the token and \(x_c=x\) for the pulse, the right-hand charge is

\[
N_{R,\ell}=2\mathbf1_{x_A>\ell}+2\mathbf1_{x_B>\ell}
 +4\mathbf1_{x_c>\ell}+2\mathbf1_{z>\ell}+N_{{\rm anc},R,\ell}.
\]

This is additive physical charge. A configuration may straddle the cut and
may transport more than one constituent in the same period. The two
arrangements are not the two spatial sides.

The entire source sector is retained: all object positions and four
directions, both arrangements, all 26 token/pulse labels, both pulse banks,
all 26 old receiver labels, every receiver position, and arbitrary identity
ancillary factors. Its fixed-position token and pulse fibers have 2704 and
5408 internal dimensions respectively. No spectral, bound-state, bright,
label or receiver-parity selection is used.

Write

\[
\mathcal D=M_2\otimes(I_T\oplus Q),\qquad
U_{\rm rec}=e^{-i\beta}\Gamma\mathcal S\mathcal E_{\mathsf J}\mathcal D C.
\]

Object streaming and pulse-edge evolution commute. The actual current,
referred to the state at the beginning of the period, is

\[
\boxed{\mathcal J_\ell
 =U_{\rm rec}^\dagger N_{R,\ell}U_{\rm rec}-N_{R,\ell}
 =C^\dagger\mathcal D^\dagger(j_{S,\ell}+j_{E,\ell})\mathcal D C.}
\]

The local capture contact creates no direct spatial charge flux; it changes
the coherent amplitudes that subsequently cross. This is why the pullback
through \(\mathcal D C\) is part of the answer.

The object velocities in source coin order are
\((-1,-1),(-1,+1),(+1,-1),(+1,+1)\). With
\(\Delta_\ell(n,v)=\mathbf1_{n+v>\ell}-\mathbf1_{n>\ell}\),

\[
j_{S,\ell}=2\sum_{d=1}^4
 [\Delta_\ell(x_A,v_{A,d})+\Delta_\ell(x_B,v_{B,d})]|d\rangle\langle d|.
\]

Each constituent transports charge 2; simultaneous crossings add. The
standing token transports no carrier charge until converted, but the
object accompanying a token can still cross the cut.

At the pulse edge, let \(a,b\) be the incident bank amplitudes at \(\ell\)
and \(\ell+1\). For \(z=\ell+1\), \(\mathsf J\) swaps the carrier and old
memory labels. The pulse current is

\[
j_{E,\ell}=4\begin{pmatrix}s^2I&sc\mathsf J\\sc\mathsf J&-s^2I\end{pmatrix},
\quad c=1/\sqrt5,\quad s=2/\sqrt5,
\]

so its expectation includes the fixed coherent term
\(8sc\operatorname{Re}\langle b,\mathsf J a\rangle\). It is not determined
by the two incident populations alone. All 676 label pairs remain in the
form. Away from the receiver edge, \(\mathsf J\) is replaced by identity.

The exact conservation law is

\[
U^\dagger n_mU-n_m=\mathcal J_{m-1}-\mathcal J_m,
\qquad n_m=N_{R,m-1}-N_{R,m}.
\]

It gives charge continuity for packets and stationary equality of mixed
fluxes where their traces exist. It does not say that an instantaneous
current operator commutes with the time step. This is the current of local
native \(H_N\); spatial locality of the source's separate logarithmic
energy Hamiltonian is not presumed. See [PROOF_CURRENT.md](PROOF_CURRENT.md).

## 2. The physical pulse transfer is golden, but one gate is not a period

The actual receiver edge obeys

\[
\binom{a'}{b'}=\begin{pmatrix}cI&-s\mathsf J\\s\mathsf J&cI\end{pmatrix}
\binom ab.
\]

Regrouping these same four physical ports gives

\[
\boxed{\binom{b'}b=T_E\binom a{a'},\qquad
T_E={1\over s}\begin{pmatrix}\mathsf J&-c\mathsf J\\
c\mathsf J&-\mathsf J\end{pmatrix}.}
\]

Exactly \(T_E^\dagger\Sigma T_E=\Sigma\),
\(\Sigma=\operatorname{diag}(I,-I)\), with physical port form \(4\Sigma\).
Its singular values are \(\varphi,\varphi^{-1}\), and \(T_E^2=I\).
The object crossing gates have their own \(2\Sigma\) forms and retain the
other constituent as a shifted spectator. These port families are
restrictions of one physical state and cannot be assigned independent
amplitudes where their configuration supports overlap.

Even in a decoupled free pulse channel the complete period has a different
transfer. If the object factor is an eigenmode \(w\) and
\(\zeta=\lambda e^{i\beta}/w\), the exact free-period matrix is

\[
M_\zeta={1\over s^2}
\begin{pmatrix}
c^2-\zeta^{-1}&c(\zeta^{-1}-1)\\
c(\zeta-1)&c^2-\zeta
\end{pmatrix}.
\]

It preserves \(\Sigma\), has determinant 1, and its trace is
\((1-5\operatorname{Re}\zeta)/2=2\cos k\) on the source dispersion.
Thus propagating free modes have spatial eigenvalues \(e^{\pm ik}\).
The golden singular values of one edge neither remove nor determine the
phases obtained after the actual period is closed.

## 3. Explicit capture matching, with the token still present

For carrier position \(n\), retain the full object Hilbert space and set

\[
\alpha_n=|R=n,r=0;iB\rangle,\quad
\beta_n=|R=n,r=0;A\rangle,\quad K_n=|\beta_n\rangle\langle\alpha_n|.
\]

Write \(P_{\alpha,n}=|\alpha_n\rangle\langle\alpha_n|\), and similarly
for \(P_{\beta,n}\). In the carrier order (token, pulse a, pulse b), the
complete onsite matching operator is

\[
F_n=\operatorname{diag}(W,W,W)
\begin{pmatrix}
I-\frac25P_{\alpha,n}&-\frac45K_n^\dagger&0\\
\frac45cK_n&c(I-\frac25P_{\beta,n})&-sI\\
\frac45sK_n&s(I-\frac25P_{\beta,n})&cI
\end{pmatrix}.
\]

All label and memory factors are retained as identities here. For
\(\zeta=\lambda e^{i\beta}\), the exact equations are

\[
F_n\begin{pmatrix}\tau_n\\a_n\\b_n\end{pmatrix}
=\begin{pmatrix}\zeta\tau_n\\u_n\\v_n\end{pmatrix},
\qquad
\binom{\zeta b_{n+1}}{v_{n+1}}=T_{E,n}\binom{u_n}{\zeta a_n}.
\]

These are genuine operator equations, with all of \(W\) present. The token
row is an explicit constraint:

\[
[\zeta I-W(I-\tfrac25P_{\alpha,n})]\tau_n
=-\tfrac45WK_n^\dagger a_n.
\]

The relation also retains the object-coordinate crossings. A charge-marked
description records A, B, carrier and receiver separately, with weights
\(2,2,4,2\), while requiring all marked data to come from the same physical
\(\psi\). The exact Green identity supplies the corresponding full
Hermitian flux form. [PROOF_RELATION.md](PROOF_RELATION.md) gives the complete
gate network, explicit slice coefficients and proof of compatibility with
the current above.

## 4. Why a global token elimination fails in the stated energy window

For every \(E\in[8\pi/5-1/1000,8\pi/5+1/1000]\),
\(\zeta=e^{-i(E-\beta)}\) lies on the free object branch at \(P=0\):

\[
\cos q=4+5\cos(E-\beta)\in(-1,1).
\]

Normalized plane-wave boxes placed arbitrarily far from object contact
and from \(P_{\alpha,n}\) satisfy

\[
\|\psi_N\|=1,\qquad
\|[\zeta I-W(I-\tfrac25P_{\alpha,n})]\psi_N\|
 =O(N^{-1/2})\longrightarrow0.
\]

Therefore the operator in the token row has **no bounded inverse on the
full object slice throughout this window**. A stationary token is
accompanied by an open moving-object continuum. Deleting that whole
arrangement as a closed internal memory would lose a physical channel.

This does not exclude outgoing resolvent boundary values, weighted spaces,
or a justified reduction. Such a construction must carry the omitted
object-channel flux. The Hilbert-space norm cancellation in lossless
onsite matching cannot be applied as an undefined infinity-minus-infinity
operation to continuum plane waves.

## 5. Every native code, including occupied non-unit values

The larger native circuit has the actual half-space charge

\[
Q_R^{\rm nat}=2\sum_{x>\ell}\sum_{j=1}^{38}\operatorname{lift}(h_{x,j})^2,
\qquad\operatorname{lift}(0,1,2,3,4)=(0,1,2,-2,-1).
\]

It is not exhausted by the encoded sector's four particle weights. At the
cut, the object edge swaps the entire two-coordinate ports
\(L_\ell=(h_{\ell,1},h_{\ell,3})\) and
\(R_{\ell+1}=(h_{\ell+1,2},h_{\ell+1,4})\). For every one of their 625
input patterns, its exact flux before the edge is

\[
j_{m obj}^{\rm nat}=\nu(L_\ell)-\nu(R_{\ell+1}),
\qquad\nu(l)=2[\operatorname{lift}(l_1)^2+\operatorname{lift}(l_2)^2].
\]

For example, a value 2 in a crossing port carries charge 8. The pulse gate
retains every encoded-memory swap block, free propagation on unencoded
memory, and the prescribed identity on the other pulse patterns. Untouched
ancillary contents and the chart control registers remain present.

[PROOF_NATIVE.md](PROOF_NATIVE.md) gives their full tensor-port relation,
the native gate order and the exact current pulled back through the local
layer. The same gate equations, glued with the stationary period closure,
define the native spatial relation in every finite-charge sector. No
unproved many-body scattering or energy-branch theorem is asserted.

## 6. What the next Hodge test must use

The phase is now visible in the actual matching through \(M_2\),
\(e^{-ig}\), \(e^{-i\beta}\), \(\lambda\), and the capture feedback.
It has not been fitted to the target. The current form is also fixed by
the actual native charge, rather than selected to match a Lorentz metric.
Neither result yet supplies a four-dimensional Hodge action.

A further test must name a transmitting invariant or constrained domain
of this relation, justify its treatment of the open object/token channels,
and derive its induced nondegenerate current form. Only then can an
explicit map test both the complete action and the target form on the
whole admitted preparation class. The single-edge golden factor is a
valid local result; it does not complete this reduction.

## Evidence and reproduction boundary

[PREREG.md](PREREG.md) freezes the scope, exact audits and failure rule.
`verify.py` uses its own exact cyclotomic arithmetic to audit complete
encoded-circuit columns and mixed currents. `break_certificate.py` is an
independently written, code-blind exact control program for deliberately
wrong reductions and all native object crossing patterns. Neither imports
the other. The proofs supply the universal claims; the finite programs
audit them within their declared finite domains.

`RUN.md`, `EXPECTED.txt`, `BREAK_EXPECTED.txt` and `RESULT.md`, when present,
record the original executions and their outcome. Ordinary repository CI
does not execute these programs under `notes/`; its architecture jobs are
not a two-architecture scientific run of this note.
