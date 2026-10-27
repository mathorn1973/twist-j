# Equal spectral energy and a finite phase-sensitive occupied record

**Status:** NON-CANONICAL, L1, candidate-T.
**Owner:** A. M. Thorn, session `C-FINITE-PHASE-OCCUPIED-RECORD-N`.
**Claim:** [#1775](https://github.com/mathorn1973/twist-j/issues/1775).
**Method:** analytical derivation. No scientific executable was run to
establish the results in this file. Same-session review is not external
independent acceptance or public promotion.

## 1. Fixed model and scope

Use exactly `HOMOGENEOUS-CAPTURE-CURRENT-RECORD` in
[Public Canon v105](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
The worktree base is `3abf054e435e31c51e6e50528b09fe3cf7cffe13`.
The authoritative Canon content remains the v105 content commit
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`, with 1,295,029 bytes and
SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.

There is one object pair, one carrier, the unchanged receiver at `z=100`,
the unchanged contact and synchronized macrostep, and the full
26-dimensional memory carrier. The primary experiment admits arbitrary
old memory in \(\mathcal K=\operatorname{span}\{d_1,\ldots,d_{25}\}\),
including arbitrary reference correlations, and reserves \(d_0\) as its
receiver-only arrival flag. All auxiliary/reference factors are
identities. No gate or Hamiltonian is added. A symmetry used to prove a
statement is not an additional operation that the apparatus must execute.

The experiment is a finite phase-sensitive calibration using an already
prepared pulse. Its object state lies in an exactly invariant sector on
which the conversion contact is inactive. It is not a demonstration of
capture from an initially standing token, and it does not improve the
Canon's asymptotic capture bound. Its output is the model's squared-norm
event weight and coherent record map; native preparation, physical
occurrence and an empirical Born-law derivation are not supplied.

The selected energy is the same fixed Borel reading used in the
[full-record scale note](https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/SPECTRAL.md):

\[
 f:\mathbb T\longrightarrow[0,2\pi),\qquad
 e^{-if(z)}=z,\quad f(1)=0,\qquad H_*=f(U_{\rm rec}).
\]

No numerical evaluation of this spectral function is needed. The proof
establishes equality of the complete spectral measures of the full
\(U_{\rm rec}\), which implies equality for this energy and every other
fixed Borel function of the same step.

## 2. Definitions of the unchanged step

Object coordinates are \((R,r)\in\mathbb Z^2\), with physical positions
\(x_A=R+r\), \(x_B=R-r\). In coin order \((++,+-,-+,--)\), put

\[
 M_2=\frac{(I+2iX)\otimes(I+2iX)}5,\qquad
 S(P,q)=\operatorname{diag}(e^{iP},e^{iq},e^{-iq},e^{-iP}),
\]
\[
 \Gamma=I+(e^{-ig}-1)P_0,\qquad g=2\pi/5,\qquad
 W=\Gamma SM_2.
\]

Here \(P_0\) projects onto \(r=0\). Streaming displacements are
\((-1,0),(0,-1),(0,1),(1,0)\), respectively.

The carrier is either a token at \(y\), with label \(t_j\), or a pulse
at \(x\), with two banks and label \(p_j\). Memory basis vectors are
\(d_j\), where \(0\le j<26\). With the Fourier convention
\(|x\rangle\mapsto e^{-ikx}\), the pulse step is

\[
 c=1/\sqrt5,\quad s=2/\sqrt5,\qquad
 Q=\begin{pmatrix}c&-s\\s&c\end{pmatrix},\qquad
 E(k)=\begin{pmatrix}c&-se^{ik}\\se^{-ik}&c\end{pmatrix},
 \qquad V(k)=E(k)Q.
\]

Write \(A=(e_1-e_4)/\sqrt2\), \(B=(e_2-e_3)/\sqrt2\). At every
site \(a\) and label \(j\), the contact ports are

\[
 \alpha_{a,j}=|R=a,r=0,iB;\ y=a,t_j\rangle,
 \qquad
 \gamma_{a,j}=|R=a,r=0,A;\ x=a,e_1,p_j\rangle.
\]

The contact \(C\) is identity off these orthogonal port pairs and has
matrix \(\left(\begin{smallmatrix}3/5&-4/5\\4/5&3/5\end{smallmatrix}\right)\)
on each pair. Set

\[
 \beta=4\pi/5,\qquad
 U_0=(e^{-i\beta}W\otimes I_{\rm tok})
       \oplus(e^{-i\beta}W\otimes V),\qquad U=U_0C.
\]

The receiver calibration \(\mathcal T=\mathcal T^*=\mathcal T^{-1}\)
exchanges the carrier label with the memory label on the carrier half-line
\(y\ge100\) or \(x\ge100\), respectively, and is identity on the
left half-line. The complete step is

\[
 U_{\rm rec}=\mathcal T(U\otimes I_{\rm mem,ref})\mathcal T^*.
\]

These definitions fix the physical positions, operator order, phase,
arrangements, receiver edge and internal labels throughout the proof.

## 3. An exactly reducing object-odd pulse sector

Define the object exchange involution

\[
 \mathsf P_o|R,r,e_j\rangle=|R,-r,F e_j\rangle,
 \qquad
 F e_1=e_1,\quad F e_2=e_3,\quad F e_3=e_2,\quad F e_4=e_4.
\]

It exchanges the two object constituents. It is unitary and
self-adjoint. Put \(P_-=(I-\mathsf P_o)/2\), and let \(P_D\) project
onto pulses whose object factor is in \(\operatorname{Ran}P_-\), with
arbitrary pulse position, banks, labels, memory and reference.

**Proposition 1.** The subspace \(\mathscr D=\operatorname{Ran}P_D\)
reduces the complete \(U_{\rm rec}\). The contact is identity on this
subspace, and

\[
 U_{\rm rec}|_{\mathscr D}
 =\mathcal T\bigl(e^{-i\beta}W_-\otimes V\otimes I\bigr)
   \mathcal T^*|_{\mathscr D},\qquad
 W_-=W|_{\operatorname{Ran}P_-}.
\]

**Proof.** The coin permutation \(F\) exchanges the tensor factors of
\(M_2\), so it commutes with \(M_2\). Reflection of \(r\), together
with exchange of coins 2 and 3, preserves each streaming displacement.
It also preserves \(r=0\), so it commutes with \(\Gamma\). Hence
\([\mathsf P_o,W]=0\).

At \(r=0\), the pulse contact object vector \(A\) is exchange-even.
Every vector in \(\mathscr D\) is therefore orthogonal to every
\(\gamma_{a,j}\). It is orthogonal to every \(\alpha_{a,j}\) by
arrangement type. Consequently
\(CP_D=C^*P_D=P_D\), and taking adjoints also gives
\(P_DC=P_DC^*=P_D\). Thus \(\mathscr D\) reduces \(C\), not just
its forward action.

The operator \(U_0\) preserves arrangement type and commutes with
object exchange, so \(\mathscr D\) reduces it as well. Finally,
\(\mathcal T\) acts on carrier position and labels, not on object
exchange. It commutes with \(P_D\). Combining these facts proves the
claim. QED.

The assertion is exact for all times. Keeping the first few supports away
from a contact would not, by itself, establish this reducing-subspace
statement or any exact equality of full spectral measures.

## 4. A symmetry of the full apparatus

Let

\[
 J_c=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 \mathsf R_{x_0}|x\rangle=|2x_0-x\rangle,\qquad
 \Pi_{x_0}=J_c\mathsf R_{x_0}.
\]

These act on pulse banks and position. They are unitary;
\(J_c^2=-I\), so \(\Pi_{x_0}^2=-I\).

**Lemma 2.** For every integer \(x_0\),
\([\Pi_{x_0},V]=0\).

**Proof.** Since \(Q=cI+sJ_c\), it commutes with \(J_c\). Direct
matrix multiplication gives

\[
 J_cE(-k)J_c^{-1}=E(k),\qquad
 J_cV(-k)J_c^{-1}=V(k).
\]

Reflection about \(x_0\) acts in Fourier space as
\(\widehat\psi(k)\mapsto e^{-2ikx_0}\widehat\psi(-k)\).
The scalar factor commutes with every coin matrix, proving the lemma.
QED.

On the uncalibrated full space define the block-diagonal unitary

\[
 S_0|_{\mathscr D}=I_{\rm obj}\otimes\Pi_{x_0}\otimes I,
 \qquad S_0|_{\mathscr D^\perp}=I.
\]

Proposition 1 and Lemma 2 imply \([S_0,U]=0\): on \(\mathscr D\)
the contact is identity and the free factors commute with the pulse
symmetry; on its reducing complement \(S_0\) is identity. Hence

\[
 \boxed{S_{\rm rec}=\mathcal T S_0\mathcal T^*,\qquad
 [S_{\rm rec},U_{\rm rec}]=0.}                         \tag{F1}
\]

This is a symmetry of the full operator, not a replacement generator,
an approximate bulk symmetry or a gate added to its evolution.

## 5. Two finite preparations differing only by a relative sign

Freeze \(x_0=99\) and the normalized finite object state

\[
 \chi_-=
 \frac{|R=0,r=3,e_1\rangle-|R=0,r=-3,e_1\rangle}{\sqrt2}.
\]

It is object-odd. Freeze the incoming carrier label to \(p_0\), and put

\[
 v_+=\frac1{\sqrt2}\binom11,\qquad
 v_-=\frac1{\sqrt2}\binom1{-1}.
\]

Let the old memory in \(\mathcal K\) and the reference be an arbitrary
normalized joint state

\[
 |\Xi\rangle=\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle,
 \qquad\sum_j\|\phi_j\|^2=1.
\]

The vectors \(\phi_j\) need not be orthogonal or individually
normalized. A mixed state is admitted by purification, with an additional
identity reference factor. Define

\[
 |\Psi_\pm\rangle=
 |\chi_-\rangle\otimes|x=99,v_\pm,p_0\rangle
 \otimes|\Xi\rangle.                                  \tag{F2}
\]

Every position, initial population, object state, label, old memory and
reference is the same for the two preparations. Only the relative sign
between the two pulse banks differs. Their common apparatus is unchanged.

**Proposition 3.** For every Borel set \(B\subset\mathbb T\),

\[
 \boxed{\langle\Psi_+,E_{U_{\rm rec}}(B)\Psi_+\rangle
       =\langle\Psi_-,E_{U_{\rm rec}}(B)\Psi_-\rangle.} \tag{F3}
\]

**Proof.** At the input site \(99<100\), \(\mathcal T\) is identity
on every admitted memory. Reflection about 99 fixes the input position,
and \(J_cv_+=-v_-\). It also leaves that position left of the receiver.
Thus (F1) gives
\(S_{\rm rec}\Psi_+=-\Psi_-\), with the same old-memory/reference
factor. A unitary commuting with a normal operator commutes with its
spectral projections. Taking their expectations proves (F3). The global
minus sign has no effect. QED.

The same spectral equality also holds if the old memory is enlarged to
all 26 labels. That auxiliary fact does not enlarge the primary flag
contract: an initially occupied \(d_0\) would already trigger its
receiver-only projector.

The equality is for the full spectral distribution of the complete
apparatus. It is not just equality of the native occupation charge, the
raw norm, a mean energy, or the first few moments.

## 6. Every normalized real coin has that same spectral law

**Proposition 4.** Keep any fixed normalized object-odd state, any integer
input site \(x_0<100\), a fixed carrier label, and the same arbitrary
old-memory/reference state, even on all 26 memory labels for this
spectral statement alone. All normalized real pulse-bank vectors
\(v\in\mathbb R^2\) have the same full spectral law of
\(U_{\rm rec}\).

**Proof.** The input receiver calibration is identity. Proposition 1
identifies its spectral measure with that of
\(e^{-i\beta}W_-\otimes V\), tensor identity on labels and memory.
For a Borel spectral projection, compress to the fixed object state and
the fixed pulse position. The result is a Hermitian \(2\)-by-\(2\)
matrix \(K_B\) on the pulse banks.

The symmetry \(\Pi_{x_0}\) commutes with the projection and fixes the
input position while acting there as \(J_c\). Therefore
\(J_c^*K_BJ_c=K_B\), equivalently \([K_B,J_c]=0\).
Solving that elementary matrix commutation gives
\(K_B=a_BI+b_BJ_c\), with the Hermiticity restrictions on its
coefficients understood. For every real normalized \(v\),

\[
 v^*K_Bv=a_B\|v\|^2+b_Bv^{\mathsf T}J_cv=a_B,
\]

because a real skew-symmetric form vanishes on a repeated vector.
The expectation is independent of \(v\). The identity action on the
old-memory/reference factor and purification complete the claim. QED.

This assertion does not say that every complex coin has the same spectral
law. For a complex vector, \(v^*J_cv\) need not vanish.

## 7. Consequences for the fixed energy and its moments

For the Borel reading fixed in Section 1, (F3) implies equality of the
complete spectral measures of \(H_*\) and \(E_0H_*\) for every specified
\(E_0>0\). In particular,

\[
 \langle\Psi_+,F(H_*)\Psi_+\rangle
 =\langle\Psi_-,F(H_*)\Psi_-\rangle
\]

for every bounded Borel \(F\). Since \(0\le H_*\le2\pi I\), this
includes every nonnegative integer moment, all variances, and every
spectral interval weight. The same statement holds for the preparations
in Proposition 4. Each of these laws is preserved by every integer step
of the unchanged evolution.

No explicit value of their common energy distribution or mean is asserted
or needed. The proof uses the exact spectral theorem and full-operator
symmetry, rather than estimating the Borel logarithm by a finite number
of time steps. It does not select the physical energy scale \(E_0\).

## 8. One-step arrival and the occupied reference-preserving record

Let

\[
 Q_{\rm arr}=1_{\{\text{pulse at }x=100,\ \text{bank }2\}}
             \otimes I_{\rm obj,label,mem,ref}.
\]

This auxiliary arrival event accepts every old-memory output label. The
primary readout is the receiver-only projector

\[
 P_{\rm write}:=P_W:=P_0^{\rm mem}
   =I_{\rm obj,carrier,label}\otimes|d_0\rangle\langle d_0|
    \otimes I_{\rm ref}.
\]

The notation \(P_W\) agrees with `EXPERIMENT.md`; neither notation
denotes the object-contact projector \(P_0\) from Section 2.
It is not the same operator as \(Q_{\rm arr}\) on the full carrier.
Their exact agreement on the following one-step output family is proved
below and uses the frozen restriction of old memory to \(\mathcal K\).

The complete pulse update for an input at \(x\) with coin
\(v=(v_1,v_2)^{\mathsf T}\) is

\[
 V|x,v\rangle=
 \frac{-4v_1-2v_2}{5}|x-1,1\rangle
 +\frac{v_1-2v_2}{5}|x,1\rangle
 +\frac{2v_1+v_2}{5}|x,2\rangle
 +\frac{2v_1-4v_2}{5}|x+1,2\rangle.                  \tag{F4}
\]

It follows directly by applying \(Q\) and then \(E\) in the fixed
Fourier convention. On \(\mathscr D\) the contact is identity, so the
object factor is the same normalized vector \(W\chi_-\) for both
preparations. The arrival amplitude in (F4) is

\[
 a_+=-\frac2{5\sqrt2},\qquad
 a_-=\frac6{5\sqrt2}.
\]

**Proposition 5.** After one unchanged macrostep,

\[
 \boxed{p_+=\|P_{\rm write}U_{\rm rec}\Psi_+\|^2=\frac2{25},
 \qquad
 p_-=\|P_{\rm write}U_{\rm rec}\Psi_-\|^2=\frac{18}{25}.} \tag{F5}
\]

The left-arrival weights at \(x=98\) are, respectively, \(18/25\) and
\(2/25\); the total weight retained at \(x=99\) is \(1/5\) for both.
Thus all one-step pulse weights sum to one. The two preparations reverse
their directional bias without changing their full energy distributions.

At \(x=100\), the receiver calibration acts as the exact label swap

\[
 |p_0\rangle\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle
 \longmapsto
 \sum_{j=1}^{25}|p_j\rangle|d_0\rangle|\phi_j\rangle. \tag{F6}
\]

Consequently the normalized conditional output on either nonzero arrival
branch is, up to its irrelevant global phase,

\[
 |W\chi_-\rangle\otimes|x=100,2\rangle
 \otimes\sum_{j=1}^{25}|p_j\rangle|d_0\rangle|\phi_j\rangle.
\]

This is an isometry on the complete old-memory/reference state, including
coherent correlations and mixed states by purification. It is the same
conditional record operation for both phases; their event weights differ.
The old memory is transferred, not erased.

The other one-step pulse outputs are at 98 and 99, where the receiver
calibration is identity and memory remains in \(\mathcal K\). The only
output at or beyond the receiver is bank 2 at 100, where (F6) puts memory
in \(d_0\). Consequently, on the complete frozen output family,

\[
 P_{\rm write}U_{\rm rec}\Psi_\pm
   =Q_{\rm arr}U_{\rm rec}\Psi_\pm.
\]

This proves (F5) from the computed arrival amplitudes and proves an exact
receiver-only flag. Allowing old memory to contain \(d_0\) would preserve
the spectral and swap identities but destroy that flag equivalence.

For any input coin at this same site, the selected arrival branch uses the
same isometry (F6), provided its amplitude is nonzero. Coin preparation
errors alone therefore do not alter this conditional label-transfer rule.

## 9. Sharp contrast within the fixed phase-only preparation class

Freeze a population \(p\in[0,1]\), and allow only its relative phase:

\[
 v_\varphi=
 \binom{\sqrt p}{e^{i\varphi}\sqrt{1-p}}.
\]

From (F4),

\[
 p_{\rm arr}(\varphi)=
 \frac{4p+16(1-p)-16\sqrt{p(1-p)}\cos\varphi}{25}.
\]

The full phase contrast at fixed \(p\) is therefore

\[
 \max_\varphi p_{\rm arr}(\varphi)
 -\min_\varphi p_{\rm arr}(\varphi)
 =\frac{32\sqrt{p(1-p)}}{25}\le\frac{16}{25},
\]

using \(p(1-p)\le1/4\). Equality holds at \(p=1/2\), with phases
\(0\) and \(\pi\). These are exactly the real vectors in (F2), so the
maximal contrast is compatible with their equal full spectral laws:

\[
 \boxed{p_--p_+=16/25.}
\]

This sharpness is restricted to a pulse at this one fixed input site, its
two existing banks, a change of relative phase at fixed bank populations,
one unchanged macrostep, old memory in \(\mathcal K\), and the
receiver-only event \(P_{\rm write}\), which equals the auxiliary
arrival read on this output family. It is not an
optimization over arbitrary preparations, additional carriers, gates or
waiting times.

## 10. Exact charge account and arithmetic preparation

The Canon's active native occupation charge is \(4+4+2=10\): four for
the object pair, four for the carrier and two for any admitted memory
label. It is the same in both preparations and conserved by the same
law. An admitted spectator's occupied charge is included separately and
is unchanged.

For the actual physical cut \(\ell=99\), both object constituents start
near zero and remain left of the cut after one step. The receiver's charge
two is unchanged, and the only transported charge is the pulse charge
four. Hence the Canon's full current identity gives, on these states,

\[
 \langle J_{99}\rangle_+=4p_+=8/25,\qquad
 \langle J_{99}\rangle_-=4p_-=72/25.
\]

This is the occupation-charge current. It is not identified with a local
current of the spectral energy \(H_*\).

For a fixed memory basis state, the product \(\chi_-\otimes v_\pm\)
has four coefficients \(\pm1/2\). It is therefore the common Hilbert
normalization of a finite raw coefficient table with four entries
\(\pm1\) in \(\mathbb Z[\zeta_{20}]\). The same normalization
\(1/2\) applies to the entire state; no branch is separately normalized.
The two raw tables have the same trace height. More general admitted
arithmetic memory/reference inputs preserve this exact finite arithmetic
description with their own one common preparation normalization.

The arbitrary complex old-memory/reference statement in (F6) is an
operator identity in the Hilbert-space extension. It does not claim that
every such state has a finite integer coefficient representation.

## 11. Preparation-error bounds

Use trace distance
\(D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1\), and total variation
for probability measures in the convention
\(\|\mu-\nu\|_{\rm TV}=\sup_B|\mu(B)-\nu(B)|\).
Let \(\rho_\pm\) be the ideal complete states above and
\(\widetilde\rho_\pm\) actual normalized states with

\[
 D(\widetilde\rho_\pm,\rho_\pm)\le\delta_\pm.
\]

These are conditions on the complete state, including the admitted
reference. A uniform apparatus error is not inferred from errors known
only for a smaller set of preparations.

Unitary evolution preserves trace distance, and each effect's expectation
changes by at most that distance. Therefore

\[
 \bigl|\widetilde p_+-2/25\bigr|\le\delta_+,
 \qquad
 \bigl|\widetilde p_--18/25\bigr|\le\delta_-,
\]
\[
 \boxed{\widetilde p_--\widetilde p_+
       \ge16/25-\delta_--\delta_+.}                    \tag{F7}
\]

Measuring the full spectral projection-valued measure is also a quantum
measurement, so (F3) and the triangle inequality give

\[
 \|\mu_{H_*,\widetilde\rho_+}
    -\mu_{H_*,\widetilde\rho_-}\|_{\rm TV}
 \le\delta_++\delta_-.
\]

Since \(0\le H_*\le2\pi I\),

\[
 \left|\operatorname{tr}H_*
       (\widetilde\rho_+-\widetilde\rho_-)\right|
 \le2\pi(\delta_++\delta_-),
\]

and for every positive integer \(m\) the same argument gives
\((2\pi)^m(\delta_++\delta_-)\) for the difference of the
\(m\)-th moments. For \(E_0H_*\), replace \(2\pi\) by \(2\pi E_0\).
For normalized pure preparations, a vector-norm error bound
\(\|\widetilde\Psi_\pm-\Psi_\pm\|\le\varepsilon_\pm\)
implies \(\delta_\pm\le\varepsilon_\pm\).

These inequalities are stability estimates for a supplied error bound.
They do not supply a physical preparation method or assert that a
particular laboratory error bound has been achieved.

## 12. Established result and remaining boundary

The unchanged complete operator admits finite preparations with identical
positions, populations, arbitrary occupied memory in \(\mathcal K\),
reference and full spectral energy law, but one-step receiver-only flag
weights \(2/25\) and \(18/25\). The admitted old memory excludes the
reserved \(d_0\) flag; the incoming carrier label is \(p_0\).
Their conditional occupied-memory/reference transfer is the same exact
isometry. The contrast \(16/25\) is sharp in the stated phase-only class.

The proof uses an actual reducing sector and an exact full-operator
symmetry. The selected energy's known failure of a uniform exponential
configuration bound causes no gap in this argument: no finite-time
approximation to its spectral measure was used.

The contact is inactive in this calibration, and the pulse is an input.
Phase-sensitive capture, native preparation of this source, occurrence,
physical energy selection, finite receiver retention and renewal remain
separate tasks. No statement here changes their registered status or
identifies the supplied apparatus with a derivation from the original
six-pentit update.
