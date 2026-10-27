# Native charge and current after the exact causal reduction

**A. M. Thorn. Analytical candidate-T, NON-CANONICAL, L1.**

This proof is part of the pre-execution contract. Any subsequent finite
audit disposition is recorded separately in RESULT.md and RUN.md.

This proof uses the complete encoded source law of `twistj-handoff@0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`, `homogeneous-capture-2026-10-22/proofs/homogeneous_source.md`, and the full spatial-cut identities of the preceding note. It preserves all object positions and directions, both arrangements, all 26 carrier labels and 26 receiver labels, arbitrary receiver positions, and every unchanged ancillary factor. It makes no restriction to a chosen momentum, outgoing band, or bright scalar scattering matrix.

The causal amplitude reduction is recorded separately in `PROOF_REDUCTION.md`. Here its reconstructed token amplitude is used to derive explicit native-charge and current kernels, including interference between different past inputs and between coupled and dark initial object states.

## 1. Source blocks and exact reconstruction

Write the complete active Hilbert space as \(\mathcal H_T\oplus\mathcal H_P\), with token position \(y\) and pulse position \(x\). The receiver and ancillary spaces are factors of both summands. Let \(V_T,V_P\) be the source contact isometries from the common position/label space, so that

\[
P_T=V_TV_T^\dagger,\qquad P_P=V_PV_P^\dagger,\qquad
K=V_PV_T^\dagger,
\quad K^\dagger K=P_T,\quad KK^\dagger=P_P.
\]

At site \(n\), their object vectors are \(\alpha_n=|R=n,r=0;iB\rangle\) on the token side and \(\beta_n=|R=n,r=0;A\rangle\otimes\eta\) on the pulse side. Both are normalized. Put \(h=2/5\), \(\kappa=4/5\), and let \(U_T,U_P\) be the complete free arrangement steps, including \(e^{-i\beta}\) and the actual receiver edge on the pulse side. The exact full step is

\[
U_{\rm rec}=\begin{pmatrix}A&B\\G&D\end{pmatrix},\qquad
\begin{aligned}
A&=U_T(I-hP_T),& B&=-\kappa U_TK^\dagger,\\
G&=\kappa U_PK,&D&=U_P(I-hP_P).
\end{aligned}
\tag{HC1}
\]

The symbol G is the pulse-from-token block; the source contact is still denoted C elsewhere. Let \(t_0,p_0\) be an arbitrary initial state, including arbitrary dark object content in \(t_0\). For time \(m\ge0\), define

\[
E_m=A^m,\qquad F_{m,j}=A^{m-1-j}B\quad(0\le j<m),
\]

\[
\boxed{\rho_m=E_mt_0+\sum_{j=0}^{m-1}F_{m,j}p_j,\qquad
p_{m+1}=D p_m+G\rho_m.}
\tag{HC2}
\]

An empty sum is zero. This formula reconstructs the complete token amplitude exactly. It does not set the incoming token to zero or invert \(\lambda-A\). The identities \(\rho_{m+1}=A\rho_m+Bp_m\) and \((\rho_m,p_m)=U_{\rm rec}^m(t_0,p_0)\) follow by induction.

For a finite history \(H_m=(t_0,p_0,\ldots,p_m)\), the explicit reduction/reconstruction map is

\[
\boxed{L_m H_m=
\begin{pmatrix}
E_m&F_{m,0}&\cdots&F_{m,m-1}&0\\
0&0&\cdots&0&I
\end{pmatrix}H_m=(\rho_m,p_m).}
\tag{HC3}
\]

The histories under consideration obey (HC2); arbitrary independent values of the past pulse amplitudes are not additional source states. In particular, the correct norm of an admissible history is \(\|\rho_m\|^2+\|p_m\|^2\), not the sum of the pulse norms at all past times. That correct norm equals \(\|t_0\|^2+\|p_0\|^2\).

## 2. The actual physical half-space charge

For the physical cut between \(\ell\) and \(\ell+1\), let \(\chi_\ell(q)=\mathbf1_{q>\ell}\). The arrangement charges are

\[
\begin{aligned}
N^T_\ell&=2\chi_\ell(x_A)+2\chi_\ell(x_B)+4\chi_\ell(y)
 +2\chi_\ell(z)+N_{{\rm anc},\ell},\\
N^P_\ell&=2\chi_\ell(x_A)+2\chi_\ell(x_B)+4\chi_\ell(x)
 +2\chi_\ell(z)+N_{{\rm anc},\ell}.
\end{aligned}
\tag{HC4}
\]

Thus \(N_\ell=\operatorname{diag}(N^T_\ell,N^P_\ell)\). These are the original native weights \((2,2,4,2)\), not a probability assigned to the arrangement label. The active total charge is 10. The unchanged ancillary charge is additional. This local charge is not identified with the separately chosen spectral Hamiltonian.

For two admissible histories H and \(\widetilde H\), the charge pairing is

\[
\boxed{\mathcal Q^{(m)}_\ell(H,\widetilde H)
=\langle\rho_m,N^T_\ell\widetilde\rho_m\rangle
 +\langle p_m,N^P_\ell\widetilde p_m\rangle.}
\tag{HC5}
\]

This has the following explicit history kernels. Denote the initial-token slot by \(*\), past pulse slots by \(j,k<m\), and the current pulse slot by m:

| Charge kernel | Exact operator |
|---|---|
| \(Q^{(m)}_{**}\) | \(E_m^\dagger N^T_\ell E_m\) |
| \(Q^{(m)}_{*j}\) | \(E_m^\dagger N^T_\ell F_{m,j}\) |
| \(Q^{(m)}_{j*}\) | \(F_{m,j}^\dagger N^T_\ell E_m\) |
| \(Q^{(m)}_{jk}\) | \(F_{m,j}^\dagger N^T_\ell F_{m,k}\) |
| \(Q^{(m)}_{mm}\) | \(N^P_\ell\) |
| \(Q^{(m)}_{*m},Q^{(m)}_{jm}\) and their adjoints | \(0\) |

In particular,

\[
\boxed{Q^{(m)}_{jk}
=B^\dagger(A^\dagger)^{m-1-j}N^T_\ell A^{m-1-k}B.}
\tag{HC6}
\]

The off-diagonal kernels \(j\ne k\), and the initial-token/past-pulse kernels, are required. They retain interference between histories that arrive in the same token/object state. They cannot be replaced by a sum of probabilities of separate delayed paths.

For additional explicitness, on a fixed carrier site n let

\[
T=e^{-i\beta}W,\qquad A_n=T(I-h|\alpha_n\rangle\langle\alpha_n|),\qquad
v_r^{(n)}=A_n^r T\alpha_n.
\]

Writing \(N^{\rm obj}_\ell=2\chi_\ell(x_A)+2\chi_\ell(x_B)\), the contact-to-contact history kernel in (HC6) is \(\kappa^2\) times the contact projection with the following operator on the retained receiver and ancillary factors:

\[
\boxed{
q_{rs}^{(n)}(\ell)
=\langle v_r^{(n)},N^{\rm obj}_\ell v_s^{(n)}\rangle I
 +\langle v_r^{(n)},v_s^{(n)}\rangle
 [4\chi_\ell(n)+2\chi_\ell(z)+N_{{\rm anc},\ell}].}
\tag{HC7}
\]

Different standing-token sites are orthogonal and the charge is diagonal in that site. All carrier/memory label identities remain in (HC7). The object-position matrix element in its first term is essential: a scalar return amplitude alone does not determine the physical charge carried during the object's excursion.

## 3. Explicit current kernels and continuity

Define the three source current blocks

\[
\begin{aligned}
J_{TT,\ell}&=A^\dagger N^T_\ell A+G^\dagger N^P_\ell G-N^T_\ell,\\
J_{TP,\ell}&=A^\dagger N^T_\ell B+G^\dagger N^P_\ell D,\\
J_{PP,\ell}&=B^\dagger N^T_\ell B+D^\dagger N^P_\ell D-N^P_\ell,
\qquad J_{PT,\ell}=J_{TP,\ell}^\dagger.
\end{aligned}
\tag{HC8}
\]

These have a direct local-circuit expression. Put \(a_T=I-hP_T\), \(a_P=I-hP_P\), and let

\[
j^T_\ell=U_T^\dagger N^T_\ell U_T-N^T_\ell,
\qquad j^P_\ell=U_P^\dagger N^P_\ell U_P-N^P_\ell.
\]

The contact preserves the local charge, so block multiplication gives

\[
\boxed{
\begin{aligned}
J_{TT,\ell}&=a_Tj^T_\ell a_T+\kappa^2K^\dagger j^P_\ell K,\\
J_{TP,\ell}&=-\kappa a_Tj^T_\ell K^\dagger
               +\kappa K^\dagger j^P_\ell a_P,\\
J_{PP,\ell}&=\kappa^2Kj^T_\ell K^\dagger+a_Pj^P_\ell a_P.
\end{aligned}}
\tag{HC9}
\]

Here \(j^T_\ell=M_2^\dagger j_{S,\ell}M_2\) and
\(j^P_\ell=(M_2\otimes Q)^\dagger(j_{S,\ell}+j_{E,\ell})(M_2\otimes Q)\), with all position and label factors understood. The actual unpulled local currents are

\[
\begin{aligned}
j_{S,\ell}&=2\sum_{d=1}^{4}
 [\Delta_\ell(x_A,v_A(d))+\Delta_\ell(x_B,v_B(d))]|d\rangle\langle d|,\\
v_A&=(-1,-1,+1,+1),\qquad v_B=(-1,+1,-1,+1),\\
\Delta_\ell(q,+1)&=\mathbf1_{q=\ell},\qquad
\Delta_\ell(q,-1)=-\mathbf1_{q=\ell+1},\\
j_{E,\ell}&=4\begin{pmatrix}s^2I&sc\mathsf J_\ell\\sc\mathsf J_\ell&-s^2I\end{pmatrix},
\qquad c=1/\sqrt5,\quad s=2/\sqrt5.
\end{aligned}
\tag{HC10}
\]

The last matrix acts on pulse bank 1 at \(\ell\) and bank 2 at \(\ell+1\); it is zero off that edge. The controlled swap \(\mathsf J_\ell\) acts on all 676 label pairs if \(z=\ell+1\), and is identity otherwise. Thus (HC8)–(HC10) specify the current from the physical source gates, including all constituent and receiver-memory coherences.

The reduced current is explicitly

\[
\boxed{
\begin{aligned}
\mathfrak j^{(m)}_\ell(H,\widetilde H)
={}&\langle\rho_m,J_{TT,\ell}\widetilde\rho_m\rangle
 +\langle\rho_m,J_{TP,\ell}\widetilde p_m\rangle\\
 &+\langle p_m,J_{PT,\ell}\widetilde\rho_m\rangle
 +\langle p_m,J_{PP,\ell}\widetilde p_m\rangle.
\end{aligned}}
\tag{HC11}
\]

Its initial/past history kernels are the first four rows of the table in section 2 with \(N^T_\ell\) replaced by \(J_{TT,\ell}\). The additional kernels coupling to the current pulse are

\[
\boxed{
\mathcal J^{(m)}_{*m}=E_m^\dagger J_{TP,\ell},\quad
\mathcal J^{(m)}_{jm}=F_{m,j}^\dagger J_{TP,\ell},\quad
\mathcal J^{(m)}_{mm}=J_{PP,\ell},}
\tag{HC12}
\]

with the reverse kernels given by adjoints. These formulas include the full incoming-token term and every interference term; they are more than an unspecified effective metric.

Substitute \(\rho_{m+1}=A\rho_m+Bp_m\) and \(p_{m+1}=G\rho_m+Dp_m\) into (HC5). Expanding the four pairings produces respectively the three diagonal/cross operators in (HC8). Therefore, for every two admissible histories,

\[
\boxed{\mathcal Q^{(m+1)}_\ell(H_{m+1},\widetilde H_{m+1})
       -\mathcal Q^{(m)}_\ell(H_m,\widetilde H_m)
       =\mathfrak j^{(m)}_\ell(H_m,\widetilde H_m).}
\tag{HC13}
\]

Taking the difference between cuts \(\ell-1\) and \(\ell\) gives the exact bilinear site continuity law: the change of stored charge at site \(\ell\) is the incoming current through \(\ell-1\) minus the outgoing current through \(\ell\). Summing over a finite interval leaves its two physical boundary currents. The current is not claimed to commute with the temporal evolution.

All sums in (HC2) are finite, and the causal amplitude identities hold for arbitrary Hilbert-space initial data. On the active sector the charges in (HC4) are bounded by 10. For arbitrary unchanged ancillary contents, the charge pairings and (HC13) are defined on the form domain \(D(N_{{\rm anc},\ell}^{1/2})\), which contains the finite-charge vectors and is invariant because the ancillary factor evolves identically. Thus no boundary resolvent, energy-dependent limiting absorption argument, or subtraction of divergent stationary norms is needed for (HC13).

## 4. Explicit nonzero history interference

The kernels above are not merely permitted to have off-diagonal entries: the source gives nonzero ones. Fix carrier site n, receiver \(z=n+1\), cut \(\ell=n\), and no ancillary charge. Use normalized \(\alpha_n\). Then

\[
v_0=T\alpha_n,\quad v_2=A_n^2T\alpha_n,\qquad
N^T_n v_0=4v_0.
\]

The first object step separates its two charge-2 constituents across the cut; the receiver contributes the other 2. The source moments satisfy \(\langle\alpha_n,T\alpha_n\rangle=0\) and \(\langle\alpha_n,T^2\alpha_n\rangle=4/5\). Consequently

\[
\boxed{\langle v_0,v_2\rangle=\frac{12}{25},\qquad
\langle v_0,N^T_n v_2\rangle=\frac{48}{25}.}
\tag{HC14}
\]

Indeed, unitarity of T moves the leading T from both vectors, the rank-one term annihilates \(T\alpha_n\), and the remaining left contact factor multiplies by \(1-h=3/5\). Multiplication by \(\kappa^2=16/25\) gives the corresponding nonzero charge kernel between past pulse contact inputs whose lags differ by two. In the unnormalized convention \(\|\alpha_0\|^2=2\), the two values in (HC14) are \(24/25\) and \(96/25\).

A directly admissible initial-state example is

\[
t_0=\alpha_n/\sqrt2,\qquad p_0=\beta_n/\sqrt2.
\]

The two contributions to the next token are \((3/5)T\alpha_n/\sqrt2\) and \(-(4/5)T\alpha_n/\sqrt2\). Their individual right-charge expectations sum to 2, whereas their coherent sum has right charge \(2/25\). The omitted cross term would be \(-48/25\).

For the complete state the first physical current is also phase-sensitive. Here \(\langle U_P\beta_n,N^P_nU_P\beta_n\rangle=116/25\): the object contributes 2, the receiver 2, and the pulse contributes \(4s^2c^2=16/25\). The coherent plus input above therefore has

\[
\boxed{\mathfrak j_n^{(0)}=\frac{1642}{625}.}
\tag{HC15}
\]

The incoherent mixture of the two separately prepared initial arrangements has current \(58/25\), differing by \(192/625\). These comparisons do not discard any label; any one fixed pair of encoded labels supplies the witness, and the identities tensor with the entire label and ancillary space.

## 5. Return amplitudes and their physical meaning

The scalar amplitude kernel in the pulse recurrence is simpler than its native-charge kernel. With

\[
\nu_r=\langle\alpha_n,A_n^rT\alpha_n\rangle,
\]

translation covariance and the fixed token position give

\[
\boxed{GA^rB=-\kappa^2\nu_r\,U_PP_P.}
\tag{HC16}
\]

The source parity flips at each object step, hence \(\nu_{2j}=0\). The first returns are

\[
\nu_1=\frac45,\qquad
\nu_3=\frac{48-28e^{ig}}{125},\qquad g=\frac{2\pi}{5}.
\tag{HC17}
\]

The two-step identity follows from \(\langle\alpha,W^2\alpha\rangle=(4/5)e^{-ig}\) and \(2\beta+g=2\pi\). The four-step moment and its single contact correction are derived in the accompanying return/port proof. Thus the first nonzero pulse-to-token-to-pulse feedback is delayed by three macrosteps and has coefficient \(-64/125\) multiplying \(U_PP_P\). At five macrosteps the coefficient is

\[
-\frac{16(48-28e^{ig})}{3125},
\]

which has a nonzero imaginary part because \(\sin g\ne0\). This phase is fixed by the original object and contact law. These are delayed temporal kernels, not a separately inserted rotation or a proof that a target Hodge action has been obtained.

Crucially, knowing all the scalar \(\nu_r\) is not a substitute for (HC6)–(HC7). Return amplitudes describe what re-enters the pulse contact; the physical current also records where the object charge traveled while the token stood, and the coherent pairing with all incoming token content.

## 6. Dark states: an exact obstruction to pulse-history-only current

This section gives a source-specific counterexample, rather than merely declining to assume that a projection commutes with charge.

At fixed token site n, define the inversion

\[
\mathcal R_n|R,r,d\rangle=|2n-R,-r,5-d\rangle,
\qquad d=1,2,3,4.
\tag{DN1}
\]

It commutes with the source W: the coin commutes with the simultaneous coin flip, the streaming directions are reversed together with the positions, and the contact phase depends only on \(r=0\). Moreover \(\mathcal R_n\alpha_n=-\alpha_n\). Therefore the cyclic space

\[
\mathcal K_n=\overline{\operatorname{span}\{W^k\alpha_n:k\in\mathbb Z\}}
\]

is odd under \(\mathcal R_n\). Every even state is in its orthogonal complement and is dark to this token contact at all times.

Use the abbreviations \(|R,r,d\rangle\) for the object only. Directly applying the four source coin/streaming components twice gives

\[
\begin{aligned}
\chi:=W^2\alpha_n={}&\frac45e^{-ig}\alpha_n
 +\frac{i}{5\sqrt2}(|n,-2,2\rangle-|n,2,3\rangle)\\
 &+\frac{2}{5\sqrt2}\bigl(-|n-1,-1,1\rangle+|n-1,1,1\rangle
 -|n+1,-1,4\rangle+|n+1,1,4\rangle\bigr).
\end{aligned}
\tag{DN2}
\]

Define the normalized even state

\[
\boxed{d=\frac12\bigl(|n-1,-1,1\rangle+|n+1,1,4\rangle
 -|n-1,1,1\rangle-|n+1,-1,4\rangle\bigr).}
\tag{DN3}
\]

It is orthogonal to \(\mathcal K_n\). Keep the token at n, receiver at \(n+1\), any fixed pair of labels, and the cut \(\ell=n\). The two left-center terms in (DN2) have object charge 0 to the right; the two right-center terms have object charge 2. The split-relative terms have object charge 2, but remain odd and do not contribute to the pairing with d. Receiver charge 2 is constant and also gives no odd/even cross term. Hence

\[
\boxed{\langle\chi,N^T_n d\rangle=\frac{2\sqrt2}{5}\ne0.}
\tag{DN4}
\]

Equivalently, \(\|P_{\rm even}N^T_n\chi\|^2=8/25\). Thus the projection onto the source-generated cyclic space does not commute with the physical half-space charge. Dropping its dark complement changes the charge observable unless the full pulled-back observable and appropriate initial-domain restriction are retained.

There is also an exact nonzero current witness. Put

\[
\chi_0=W\alpha_n,\qquad d_0=W^\dagger d.
\]

Both vectors have zero overlap with \(\alpha_n\); \(\chi_0\) by one-step parity and \(d_0\) by inversion. The first capture step consequently acts as identity on them, with no pulse produced. Also \(N^T_n\chi_0=4\chi_0\), so \(\langle\chi_0,N^T_nd_0\rangle=0\). After one complete step they are \(e^{-i\beta}\chi\) and \(e^{-i\beta}d\). Therefore

\[
\boxed{\langle(\chi_0,0),\mathcal J_n(d_0,0)\rangle
=\frac{2\sqrt2}{5}.}
\tag{DN5}
\]

The normalized initial states \(\psi_\pm=((\chi_0\pm d_0)/\sqrt2,0)\) have identical entire future pulse histories: the dark component never couples to a pulse, and their coupled initial component is the same. Yet their first physical currents are different. In (DN2), the object right charge has expectation \(2/5\), while the state d has object right charge 1. Both preceding states have object right charge 2; for \(d_0\) this follows from even inversion and the fact that the preceding object parity puts neither constituent at n. Thus

\[
\boxed{\langle\psi_\pm,\mathcal J_n\psi_\pm\rangle
=-\frac{13}{10}\pm\frac{2\sqrt2}{5}.}
\tag{DN6}
\]

Their difference is \(4\sqrt2/5\). This proves that the pulse history alone cannot determine the physical native current on the full source domain. The retained full \(t_0\) in (HC2), and its cross kernels in (HC5)–(HC12), are necessary. This obstruction concerns the specified pulse-history-only reduction, not every possible reduced description.

## 7. Exact scope of the reduction

The reducing dynamical sector \((\bigoplus_n\mathcal K_n)\oplus\mathcal H_P\) is fixed by the source contact, without reference to a target spectrum. If initial data are restricted to it in advance, its charge is the compression of (HC4) by the inclusion of that sector. The physical position projectors do not become commuting scalar labels in its cyclic spectral representation. For arbitrary initial data, the dark token evolution and its physical-charge cross terms must remain. Equations (HC2)–(HC13) do so automatically.

The result is an exact causal reduction for finite-time normalizable states at all energies. It is not asserted to be a finite-dimensional Markov map or a stationary two-port transfer. An on-shell outgoing construction has the additional tasks of specifying its boundary limits and reconstructing the full token/object state before evaluating these native kernels. Its spectral-port norm identity alone is not the native spatial-current identity.

Finally, this proof is an explicit reduction of the complete one-object-pair / one-carrier / one-encoded-receiver sector. The larger native occupied-state circuit still has the exact charge \(2\sum\ell(h)^2\) and gatewise telescoping continuity, as in the preceding native proof. The four encoded charge weights are not assigned to arbitrary many-particle native codes by this reduction.
