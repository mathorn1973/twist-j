# Exact physical charge current through a spatial cut

**A. M. Thorn. NON-CANONICAL, candidate-T, L1.**

This proof is frozen before the first execution of the accompanying finite
audits. Execution evidence, when present, is recorded separately in `RUN.md`.

This calculation uses the complete one-object-pair / one-carrier / one-receiver law, not its two bright asymptotic arrangement channels. The source is [the homogeneous capture law](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md), especially equations (1)–(12) and (43)–(46), at the immutable source commit `0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`. The distinction between this complete sector and the still larger native occupied-state extension follows the source section 3 and its [native completion review](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/native_completion_static_review.md).

## 1. Actual physical cut and complete channel space

Put the physical cut between sites \(\ell\) and \(\ell+1\), and write \(\chi_\ell(n)=\mathbf1_{n>\ell}\). The example immediately before the prepared receiver is \(\ell=99,z=100\). The law and the proof keep arbitrary \(z\), including superpositions of receiver positions; fixing \(z=100\) is a preparation, not a change of law.

The complete encoded sector is

\[
\mathscr H=\left[
  \ell^2(\mathbb Z_R\times\mathbb Z_r\times\mathbb Z_y)
    \otimes\mathbb C^4\otimes\mathbb C^{26}
  \;\oplus\;
  \ell^2(\mathbb Z_R\times\mathbb Z_r\times\mathbb Z_x)
    \otimes\mathbb C^4\otimes\mathbb C^2\otimes\mathbb C^{26}
\right]
\otimes\ell^2(\mathbb Z_z)\otimes\mathbb C^{26}_{\rm mem}
\otimes\mathscr H_{\rm anc}.
\tag{C1}
\]

The first summand is the token arrangement and the second the pulse arrangement. Both colors of the object are retained through this direct sum. Both arrangements have all four object coin directions. All 26 carrier labels, all 26 receiver labels, all relative and center positions, both pulse banks, every direction orthogonal to the capture vectors, and every unchanged ancillary state are retained. No bound-state projection or spectral bright-channel projection is made.

The physical constituent positions are \(x_A=R+r\) and \(x_B=R-r\). In this source sector they have the same parity. Define the carrier position operator as \(y\) in the first summand and \(x\) in the second; denote it by \(x_c\). The physical charge to the right is

\[
\boxed{N_{R,\ell}=2\chi_\ell(x_A)+2\chi_\ell(x_B)
 +4\chi_\ell(x_c)+2\chi_\ell(z)+N_{{\rm anc},R,\ell}.}
\tag{C2}
\]

The weights are the native charges. The object pair carries 4, the token or pulse 4, and the encoded receiver 2. The total active charge is 10; the unchanged ancillary charge is additional. Receiver energy zero does not remove its native charge 2.

This is the local current of the source's native charge \(H_N\). It is not automatically the energy current of the separately constructed spectral Hamiltonian \(H_{{\rm full},{\rm rec}}\). The source does not claim spatial locality for its interaction Hamiltonian. No such extra locality or energetic interpretation is required for the charge continuity proved here.

In particular, \(N_{R,\ell}\) is not 10 times a projector onto “the complete configuration lies to the right”. A configuration can place its two constituents, carrier and receiver on different sides. Such configurations are essential channels of the physical cut. A cut in \(R\), or in \(R-x_c\), measures a different quantity.

## 2. Factorization by the actual local layers

Let \(\mathcal E_{\mathsf J}\) denote the pulse edge layer, including the receiver modification and the identity on the token summand. Let

\[
\mathcal D=(M_2\otimes I_{26})
\oplus(M_2\otimes Q\otimes I_{26})
\tag{C3}
\]

with identities on positions, receiver and ancillas understood. Let \(\mathcal S\) be the object streaming layer in both arrangements and \(\Gamma\) its contact phase. The complete macrostep has the exact order

\[
U_{\rm rec}=e^{-i\beta}\Gamma\mathcal S\mathcal E_{\mathsf J}\mathcal D C.
\tag{C4}
\]

The object and pulse edge layers commute, so their displayed ordering is a legitimate factorization of the source law. The ordering \(\Gamma\mathcal S M_2\) inside the object is not changed.

Every local charge term in (C2) commutes with \(\Gamma\), \(\mathcal D\), the common phase and \(C\). For \(C\), both contact vectors have \(x_A=x_B=x_c=n\) and charge 8 at that same site; the receiver and ancillary contents are spectators. Thus contact can change the later flux by changing amplitudes, but it creates no direct flux across a spatial edge. The auxiliary label calibration \(\mathcal T\) also commutes with (C2): it swaps labels without moving charge. The only flux-producing layers are therefore the actual object streaming and pulse edge layers.

Define their unpulled currents by

\[
j_{S,\ell}=\mathcal S^\dagger N_{R,\ell}\mathcal S-N_{R,\ell},
\qquad
j_{E,\ell}=\mathcal E_{\mathsf J}^\dagger N_{R,\ell}\mathcal E_{\mathsf J}-N_{R,\ell}.
\tag{C5}
\]

The first acts only on object positions and directions and the second only on pulse positions, banks and carrier/receiver labels. Consequently they commute with one another and with the other system's streaming. Layer telescoping gives the exact macrostep current

\[
\boxed{\mathcal J_\ell
 =U_{\rm rec}^\dagger N_{R,\ell}U_{\rm rec}-N_{R,\ell}
 =C^\dagger\mathcal D^\dagger
       (j_{S,\ell}+j_{E,\ell})\mathcal D C.}
\tag{C6}
\]

The pullback by \(\mathcal D C\) is necessary. Adding currents computed on inconsistent macrostep times would lose the capture and coin coherences.

## 3. Object streaming, including its two constituent charges

The source Fourier convention is \(\widehat\psi(P)=\sum_R e^{-iPR}\psi(R)\). Accordingly \(e^{+iP}\) shifts a ket to \(R-1\), not to \(R+1\). From the source symbol \(\operatorname{diag}(e^{iP},e^{iq},e^{-iq},e^{-iP})\), the four physical direction pairs are

| Object coin index | \(v_A\) | \(v_B\) |
|---|---:|---:|
| 1 | −1 | −1 |
| 2 | −1 | +1 |
| 3 | +1 | −1 |
| 4 | +1 | +1 |

For \(v=\pm1\), put

\[
\Delta_\ell(n,v)=\chi_\ell(n+v)-\chi_\ell(n)
 =\begin{cases}\mathbf1_{n=\ell},&v=+1,\\
 -\mathbf1_{n=\ell+1},&v=-1.\end{cases}
\tag{C7}
\]

Then

\[
\boxed{j_{S,\ell}=2\sum_{i=1}^{4}
 [\Delta_\ell(x_A,v_{A,i})+\Delta_\ell(x_B,v_{B,i})]
 |i\rangle\langle i|.}
\tag{C8}
\]

All the coordinates and labels not displayed are summed over or carried as identity factors. Thus both arrangements contribute, including a standing token accompanied by a moving object.

More explicitly, write \(u_A=\mathbf1_{x_A=\ell}\), \(w_A=\mathbf1_{x_A=\ell+1}\), and similarly for B. The diagonal entries of (C8) are

\[
(k_1,k_2,k_3,k_4)=
\bigl(-2(w_A+w_B),\;-2w_A+2u_B,\;2u_A-2w_B,\;2(u_A+u_B)\bigr).
\tag{C9}
\]

A crossing constituent carries charge 2. Two simultaneous crossings in the same direction carry charge 4, even though they occur in one configuration amplitude. Simultaneous opposite constituent crossings across this same edge would require \(x_A\) and \(x_B\) to occupy \(\ell\) and \(\ell+1\), and are excluded by the source's common-parity sector. A simultaneous object crossing and pulse crossing is allowed and is included by the sum in (C6).

Equivalently, restriction maps onto the four constituent crossing sets give

\[
\langle\alpha,j_{S,\ell}\alpha\rangle
 =2\bigl(\|\alpha_{A,+}\|^2+\|\alpha_{B,+}\|^2
          -\|\alpha_{A,-}\|^2-\|\alpha_{B,-}\|^2\bigr).
\tag{C10}
\]

Here A,+ means \(x_A=\ell\) and coin 3 or 4; A,− means \(x_A=\ell+1\) and coin 1 or 2; B,+ means \(x_B=\ell\) and coin 2 or 4; B,− means \(x_B=\ell+1\) and coin 1 or 3. These are constituent-marked restrictions of one state. They are not independent free amplitudes: if both constituents cross, the same configuration amplitude occurs in both marked restrictions, with the correct total charge 4.

## 4. Pulse edge and all receiver memory channels

Immediately before the edge layer, let \(a\) be the pulse bank-1 amplitude at site \(\ell\), and \(b\) the bank-2 amplitude at site \(\ell+1\). These are vectors carrying the complete object, carrier-label, receiver-position, receiver-label and ancillary spectator factors. Define

\[
\mathsf J_\ell=\mathbf1_{z=\ell+1}\mathsf J
              +\mathbf1_{z\ne\ell+1}I,
\qquad \mathsf J^\dagger=\mathsf J,\quad\mathsf J^2=I,
\tag{C11}
\]

where \(\mathsf J\) swaps the two 26-valued labels. At the prepared cut \(\ell=99,z=100\), it is exactly \(\mathsf J\). The actual local gate is

\[
\binom{a'}{b'}=
\begin{pmatrix}cI&-s\mathsf J_\ell\\s\mathsf J_\ell&cI\end{pmatrix}
\binom a b,
\qquad c=1/\sqrt5,\quad s=2/\sqrt5.
\tag{C12}
\]

The receiver remains at its site with charge 2. On an encoded receiver edge, the right-half charges of the two native pulse/receiver basis states are 2 and 6 respectively. Hence the receiver's charge cancels in the current and the transported weight is 4:

\[
\begin{aligned}
\langle\alpha,j_{E,\ell}\alpha\rangle
 &=4(\|b'\|^2-\|b\|^2)\\
 &=4\bigl[s^2(\|a\|^2-\|b\|^2)
       +2cs\operatorname{Re}\langle b,\mathsf J_\ell a\rangle\bigr]\\
 &=4(\|a\|^2-\|a'\|^2).
\end{aligned}
\tag{C13}
\]

Thus, on this pulse edge and with zero on its complement,

\[
\boxed{j_{E,\ell}=4
\begin{pmatrix}s^2I&sc\mathsf J_\ell\\sc\mathsf J_\ell&-s^2I\end{pmatrix}.}
\tag{C14}
\]

The cross term is fixed by the actual coherent edge law. Replacing (C13) by the difference of incoming populations alone is incorrect. For example, \(a=b\) and \(\mathsf J_\ell a=a\) has a nonzero positive current despite equal input populations.

Every pair \((i,j)\) of carrier and receiver labels belongs to the block \(\{|p_i,0,d_j\rangle,|0,p_j,d_i\rangle\}\). There are 676 such disjoint two-dimensional blocks. In a fixed position fiber the token arrangement has \(4\cdot676=2704\) internal dimensions, and the pulse arrangement \(4\cdot2\cdot676=5408\). The count is multiplied by the full spatial and ancillary spectator factors; those factors are not discarded. The label swap has symmetric multiplicity 351 and antisymmetric multiplicity 325, and both occur.

If \(K_E=j_{E,\ell}/4\), then direct multiplication gives \(K_E^2=s^2I\). Thus the pulse current matrix itself has eigenvalues \(\pm4s=\pm8/\sqrt5\), with 676 of each per fixed object coin and fixed remaining spatial/ancillary data. This is an instantaneous charge-change operator; it is distinct from the port metric \(4\operatorname{diag}(I,-I)\) used when regrouping (C12) into a spatial transfer relation.

## 5. Exact bilinear continuity law

For two arbitrary states \(\psi,\varphi\) in (C1), define \(\alpha=\mathcal D C\psi\) and \(\widetilde\alpha=\mathcal D C\varphi\). The mixed charge flux is

\[
\begin{aligned}
\mathfrak j_\ell(\psi,\varphi)
&=\langle\psi,\mathcal J_\ell\varphi\rangle\\
&=2\sum_i\sum_{\text{all positions, arrangements and spectators}}
 [\Delta_\ell(x_A,v_{A,i})+\Delta_\ell(x_B,v_{B,i})]
 \overline{\alpha_i}\,\widetilde\alpha_i\\
&\quad+4s^2(\langle a,\widetilde a\rangle-\langle b,\widetilde b\rangle)
 +4sc(\langle a,\mathsf J_\ell\widetilde b\rangle
         +\langle b,\mathsf J_\ell\widetilde a\rangle).
\end{aligned}
\tag{C15}
\]

No trace over the old memory and no selection of a carrier label is taken. Therefore (C15) also retains arbitrary entanglement with ancillary systems. The pulse terms may be evaluated before the object streaming because the latter is a unitary on their fully retained spectator factor.

Equation (C6) is equivalent to the exact bilinear half-space balance

\[
\boxed{\langle U_{\rm rec}\psi,N_{R,\ell}U_{\rm rec}\varphi\rangle
 -\langle\psi,N_{R,\ell}\varphi\rangle
 =\mathfrak j_\ell(\psi,\varphi).}
\tag{C16}
\]

Define the physical site charge \(n_m=N_{R,m-1}-N_{R,m}\). Then the operator continuity equation is

\[
\boxed{U_{\rm rec}^\dagger n_mU_{\rm rec}-n_m
       =\mathcal J_{m-1}-\mathcal J_m.}
\tag{C17}
\]

Summing over a finite interval gives change of stored charge equal to incoming current minus outgoing current. For normalizable packets this is a bounded active-sector identity. Ancillary charge may be handled on finite-charge vectors or its natural form domain; it commutes with the entire evolution and cancels exactly.

“Conserved current” means this continuity law and the corresponding stationary boundary balance. It does not assert \([\mathcal J_\ell,U_{\rm rec}]=0\). Time-dependent packets can temporarily store charge between two cuts. For stationary solutions with the same unit-modulus eigenvalue, (C17) gives equality of their mixed fluxes at different cuts whenever the relevant spectator sums or scattering boundary forms are defined. Generalized stationary solutions must not be inserted into a divergent half-space norm.

## 6. A useful all-channel negative control

At fixed object coordinates \(x_A=x_B=\ell\), the post-coin, pre-streaming object current (C9) is \(\operatorname{diag}(0,2,2,4)\). On the two pulse ports of the cut, the full current before the pullback in (C6) therefore has eigenvalues

\[
k_i\pm\frac8{\sqrt5},\qquad k_i\in\{0,2,2,4\}.
\tag{C18}
\]

Since \(2<8/\sqrt5<4\), its signature on this local fiber is \((5,3)\) for each pair of labels: \((3380,2028)\) with all 676 labels. At \(x_A=x_B=\ell+1\), the object currents are \((-4,-2,-2,0)\) and the signature is \((3,5)\) per pair: \((2028,3380)\). When no object coin entry is \(\pm4\), each object coin contributes one positive and one negative eigenvalue on the pulse edge.

This is a compression of the current immediately after \(\mathcal D C\), not an invariant sector of \(U_{\rm rec}\), not the signature of the entire infinite channel operator, and not by itself a no-go theorem for a separately justified reduction. It is a concrete control against replacing the simultaneous object and pulse charge transport by one pulse two-port metric. It also checks that charge 2 per constituent has not silently become charge 4 per whole configuration crossing.

## 7. The complete native occupied-state extension

Outside (C1), the source defines a larger local native circuit by the specified nontrivial charge-preserving blocks and their declared complements. In particular, object routing uses full SWAP gates on all values, not identity on non-unit codes. The abstract one-carrier formula (C4) and its label calibration are not claimed on arbitrary many-carrier occupations. Active bank populations can block or change which of the declared pulse/contact blocks acts. One must not extend (C8) or the fixed charges \((2,2,4,2)\) to that larger space without checking its actual occupied code. [PROOF_NATIVE.md](PROOF_NATIVE.md) supplies the complete tensor-port relation and the explicit full-value SWAP current.

There is nevertheless a complete and exact physical current formula for that circuit. On finite-charge configurations use

\[
N^{\rm native}_{R,\ell}
 =2\sum_{m>\ell}\sum_{a=1}^{38}\ell(h_{m,a})^2,
\qquad \ell(0,1,2,3,4)=(0,1,2,-2,-1).
\tag{C19}
\]

For the actual finite-depth layer factorization \(F=G_L\cdots G_1\), put \(F_{k-1}=G_{k-1}\cdots G_1\), \(F_0=I\). Then

\[
\boxed{F^\dagger N^{\rm native}_{R,\ell}F-N^{\rm native}_{R,\ell}
 =\sum_{k=1}^{L}F_{k-1}^\dagger
 (G_k^\dagger N^{\rm native}_{R,\ell}G_k-N^{\rm native}_{R,\ell})F_{k-1}.}
\tag{C20}
\]

For a layer of disjoint local gates, only gates crossing this cut contribute. Gates wholly to one side preserve that side's charge because they preserve total charge on their support. Onsite contact and phase gates contribute zero. Identity complements contribute zero. Every declared nontrivial receiver block contributes its actual \(g^\dagger N_R g-N_R\), with the charge-6 block giving exactly (C14). On the encoded-memory complement the gate is the original free pulse edge, so \(\mathsf J\) in that block is replaced by \(I\); it is not an identity propagation layer. Arbitrary untouched ancillary occupations contribute zero current.

Equation (C20), with the exact local block charge diagonal, covers all native occupied sectors of the declared circuit. It asserts no unproved many-body scattering theorem and no replacement of their actual charges by the four weights of (C2). Restricting it to the complete sector (C1) yields the explicit formula (C6). Its sitewise difference gives the same exact continuity equation (C17) with the native density from (C19).

## 8. What this establishes for a subsequent spatial transfer calculation

The source law fixes a physical cut and its Hermitian flux without any chosen Hodge metric: it is (C6), or the native expression (C20) before sector restriction. It retains the coherences produced by capture and by the receiver edge. It includes stationary zero-flux sectors and simultaneous transport of different constituents.

A stationary spatial relation must preserve the corresponding bilinear boundary current on its allowed boundary data. That current cannot be obtained by identifying the two arrangements with the two sides of space. Nor can the single pulse port form be promoted to the complete current while the object crossing amplitudes or stationary constraints are discarded. An eventual reduced nondegenerate form requires an explicit invariant or constrained reduction, followed by a check that the pullback of its form equals this physical current on the actual solution data.
