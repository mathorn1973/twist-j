# Exact causal reduction of the open object arrangement

**A. M. Thorn. NON-CANONICAL, L1. Analytical candidate-T.**

This derivation uses the unchanged homogeneous source and the complete
encoded receiver of [SOURCES.md](SOURCES.md). It concerns the explicit
one-object-pair, one-token-or-pulse, one-receiver sector, with every
position, object coin, pulse bank, carrier label and old-memory label.
The native charge is the restriction of the actual occupied-code charge,
not a newly assigned probability norm. The full native many-occupation
model is not claimed to admit this two-arrangement reduction.

## 1. Actual interface, including all carrier positions

Write the physical state as \(\psi=(t,p)\in\mathscr H_T\oplus\mathscr H_P\).
Let \(\mathscr K\) retain the carrier position \(n\), all 26 carrier
labels, all 26 receiver labels, receiver position and identity spectators.
Define isometries

\[
 V_T|n,\sigma\rangle=|\alpha_n;\mathrm{token}_n,\sigma\rangle,
 \qquad
 V_P|n,\sigma\rangle=|\beta_n;\mathrm{pulse}_{a,n},\sigma\rangle,
\]

where

\[
 \alpha_n=|R=n,r=0\rangle\otimes i(e_2-e_3)/\sqrt2,
 \qquad
 \beta_n=|R=n,r=0\rangle\otimes(e_1-e_4)/\sqrt2.
\]

Put \(P_T=V_TV_T^\dagger\), \(P_P=V_PV_P^\dagger\),
\(r_c=3/5\), \(\kappa=4/5\), and \(h=1-r_c=2/5\).
The contact is exactly

\[
 C=\begin{pmatrix}
 I-hP_T&-\kappa V_TV_P^\dagger\\
 \kappa V_PV_T^\dagger&I-hP_P
 \end{pmatrix}.
 \tag{1}
\]

It is the identity on the contact-orthogonal subspaces. The free steps are

\[
 U_T=e^{-i\beta}W\otimes I_{n,\sigma},\qquad
 U_P=e^{-i\beta}W\otimes V_{\rm rec},
 \quad \beta=4\pi/5,
 \tag{2}
\]

where \(W=\Gamma S M_2\), \(g=2\pi/5\), and \(V_{\rm rec}\)
is the actual pulse coin followed by the receiver edge, including its
label swap. Receiver-position and memory factors in (2) are understood
as the source's controlled direct sum; no fixed receiver or label is
selected. The token receiver calibration commutes with \(W\), so the
token free step has the displayed form.

The complete period is

\[
 U=\operatorname{diag}(U_T,U_P)C
   =\begin{pmatrix}A&B\\G&D\end{pmatrix},
 \tag{3}
\]

with

\[
 \begin{aligned}
 A&=U_T(I-hP_T),& B&=-\kappa U_TV_TV_P^\dagger,\\
 G&=\kappa U_PV_PV_T^\dagger,&D&=U_P(I-hP_P).
 \end{aligned}
 \tag{4}
\]

All four blocks are bounded. In particular \(\|A\|\leq1\), since
\(A^\dagger A=I-\kappa^2P_T\). None of (1)--(4) uses an on-shell
inverse or a selected Fourier momentum.

## 2. An exact reduced law, with its incoming object state

For arbitrary \((t_0,p_0)\) in the complete sector, iteration gives

\[
 t_m=A^m t_0+\sum_{j=0}^{m-1}A^{m-1-j}Bp_j,
 \tag{5}
\]

and the closed causal equation

\[
 \boxed{p_{m+1}=Dp_m+GA^m t_0+
     \sum_{j=0}^{m-1}GA^{m-1-j}Bp_j.}
 \tag{6}
\]

Here "closed" means an equation for the pulse history with the prescribed
incoming object state as a source. It does not mean a memoryless pulse
unitary. Every sum at finite \(m\) is finite. There is no limiting
absorption assumption, exterior spatial boundary, energy exclusion, or
resolvent on the unit circle.

**Equivalence.** A full solution of (3) satisfies (5)--(6) by induction.
Conversely, start with \(p_0,t_0\), solve (6), and reconstruct \(t_m\)
using (5). Subtract consecutive instances of (5) to obtain
\(t_{m+1}=At_m+Bp_m\); (6) is then
\(p_{m+1}=Gt_m+Dp_m\). Thus the reconstructed pair satisfies the
original complete unitary law, uniquely and at every finite time.

This proves a correct reduction even where the stationary full-slice
inverse excluded in PR #1721 does not exist. The reduced state is a
history with a fixed incoming datum. Arbitrary independently chosen
histories are not new physical states; admissible histories satisfy (6).

## 3. A source-derived contact memory

Set \(u_m=V_P^\dagger p_m\). The contact output replacing that pulse
component is \(v_m=\kappa V_T^\dagger t_m+r_cu_m\). Consequently

\[
 \begin{pmatrix}t_{m+1}\\v_m\end{pmatrix}
 =\begin{pmatrix}
 A&-\kappa U_TV_T\\
 \kappa V_T^\dagger&r_c I
 \end{pmatrix}
 \begin{pmatrix}t_m\\u_m\end{pmatrix},
 \quad
 p_{m+1}=U_P[(I-P_P)p_m+V_Pv_m].
 \tag{7}
\]

The matrix in (7) is unitary: it is the contact rotation followed by
\(U_T\) on its internal branch. Its norm balance is

\[
 \|t_{m+1}\|^2+\|v_m\|^2=\|t_m\|^2+\|u_m\|^2.
 \tag{8}
\]

Equation (8) alone is not the physical spatial-current statement.
That statement is proved with the actual \(N_{R,\ell}\) in
[PROOF_CURRENT.md](PROOF_CURRENT.md).

Eliminating \(t_m\) in (7) yields

\[
 v_m=r_cu_m+\kappa V_T^\dagger A^m t_0
       -\kappa^2\sum_{j<m}g_{m-1-j}u_j,
 \quad V_T^\dagger A^kU_TV_T=g_k I_{\mathscr K}.
 \tag{9}
\]

The scalar identity follows because the token position does not move,
the object walk is translation invariant in \(R\), and all retained
labels and receiver coordinates are spectators in \(U_T\). Different
\(n\) are orthogonal even when their object wave packets overlap.
Explicitly, at \(n=0\),

\[
 g_k=\langle\alpha_0,
 [e^{-i\beta}W(I-h|\alpha_0\rangle\langle\alpha_0|)]^k
 e^{-i\beta}W\alpha_0\rangle.
 \tag{10}
\]

The pulse memory in (6) therefore has the exact operator coefficients

\[
 GA^kB=-\kappa^2 g_k U_PP_P.
 \tag{11}
\]

They do not erase the object continuum: its return amplitudes are
precisely what determines the sequence \(g_k\).

## 4. First nonzero return fixed by the local circuit

Every object step reverses the parity of both \(x_A\) and \(x_B\).
The contact damping does not change a position. A return to the same
\(\alpha_n\) therefore requires an even number of object steps:

\[
 g_{2j}=0\quad(j\geq0).
 \tag{12}
\]

For the first return, \(M_2B=B\), with
\(B=(e_2-e_3)/\sqrt2\). The first shift gives relative positions
\(-1,+1\), so the first contact projection vanishes and the first
\(\Gamma\) acts as identity there. The two returning coin entries are both \(-4/5\).
Their pairing with \(B\) gives

\[
 \langle\alpha_0,W^2\alpha_0\rangle=\frac45e^{-ig}.
\]

The token's two free phases cancel the return phase exactly:

\[
 g_1=\frac45e^{-i(2\beta+g)}=\frac45,
 \qquad 2\beta+g=2\pi.
 \tag{13}
\]

Thus the first delayed term in the contact-output equation (9) is
\(-64u_{m-2}/125\), and the first pulse feedback in (6) is
\(-64U_PP_Pp_{m-2}/125\). The latter occurs over three complete
periods from \(p_{m-2}\) to \(p_{m+1}\). A zero-delay contact
rotation cannot represent this law.

## 5. Exactly defined active object space and the dark complement

The minimal unitary reducing space seen by the contact is

\[
 \mathscr C_T=\overline{\operatorname{span}}
 \{U_T^kV_Tf:k\in\mathbb Z,\ f\in\mathscr K\}.
 \tag{14}
\]

It reduces \(U_T\), contains \(\operatorname{ran}V_T\), and is
preserved by \(A\). Its complement \(\mathscr D_T\) reduces
\(U_T\) and obeys \(V_T^\dagger U_T^kd=0\) for every integer
\(k\). The full dynamics decomposes into
\(\mathscr C_T\oplus\mathscr H_P\) and the free dark branch
\(\mathscr D_T\). Equation (6) only needs the cyclic component of
\(t_0\) to drive the pulse.

Nevertheless a dynamical direct sum is not automatically a direct sum
for the spatial charge. The commutator
\([P_{\mathscr C_T},N_{T,\ell}]\) need not vanish. The physical
observable may have cyclic/dark interference terms. The full \(t_0\)
in (5) and the history kernels in PROOF_CURRENT retain these terms.
If one explicitly restricts the initial token state to \(\mathscr C_T\),
that is a valid invariant dynamical class; it is not a proof that arbitrary
physical incoming packets may be quotiented by \(\mathscr D_T\).

## 6. What this reduction establishes

Equations (5)--(13), together with the pulled-back native charge and
current, give an exact reduction of the specified open object channel.
It remains valid for the complete source packet and its entire declared
energy window, because the finite-time identities hold on the whole
Hilbert space. This does not assert finite radial boundary values at every
energy; that separate almost-everywhere stationary statement is treated
in [PROOF_PORT.md](PROOF_PORT.md).

No finite-dimensional memoryless transmitting carrier, four-dimensional
Hodge carrier, Lorentz metric identification, or whole-window intertwiner
is inferred. Those would require an additional proved invariant domain
and its actual current form. The exact causal reduction is already usable
without any such assertion.
