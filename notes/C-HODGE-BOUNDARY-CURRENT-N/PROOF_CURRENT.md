# Boundary current, complete pulse transfer, and the fixed-cut Hodge obstruction

**C-HODGE-BOUNDARY-CURRENT-N. NON-CANONICAL. L1.**

**Status of this text: candidate-T analytical derivation.** This proof was
written from the pinned source definitions before execution of the successor's
scientific programs. No computational conclusion is used below. The theorem
classifies a declared boundary-reading class; it does not classify all physical
apparatuses, the complete capture law, or the public decoder.

## 1. Sources and the contract being tested

The source relation is the pulse and receiver construction in
`mathorn1973/twistj-handoff`, commit
`0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`, path
`homogeneous-capture-2026-10-22/proofs/homogeneous_source.md`.
Its equations (3)--(4) specify

\[
c=1/\sqrt5,\qquad s=2/\sqrt5,\qquad
Q=\begin{pmatrix}c&-s\\s&c\end{pmatrix},
\]

\[
E(k)=\begin{pmatrix}c&-s e^{ik}\\s e^{-ik}&c\end{pmatrix},
\qquad V(k)=E(k)Q,\qquad \widetilde V=e^{-i\beta}V,
\qquad \beta=4\pi/5.
\tag{1}
\]

The same source's equations (43)--(46) specify the receiver edge and the
involutive exchange of the complete pulse and receiver labels. The accompanying
`proofs/native_completion_static_review.md` states its occupied-memory scope.

The question was formulated in `mathorn1973/twist-j`, commit
`31aad8fd834ca17a98d853081a8891a029b32fd5`, path
`notes/C-HODGE-PULSE-TRANSFER-N/README.md`, section 7. That note's sections
2, 3 and 6 fix the original marked regrouping, the target polynomial and an
alternative signed regrouping. Its target is the marked real four-dimensional
action of the registered `J-HODGE-HERM2-LOXODROME` construction:

\[
\chi_{L_J}(z)=(z^2-3z+1)(z^2-\varphi z+1),
\qquad \varphi=(1+\sqrt5)/2.
\tag{2}
\]

The frozen class in this proof consists of total linear, lossless,
two-amplitude boundary graphs at one common current-normalized spatial cut.
Both ends have the same nondegenerate Hermitian current of signature (1,1).
The four-coordinate reading is the complete Hermitian congruence
`X -> A X A^dagger` on `Herm_2(C)`. A claimed identification with the marked
Hodge action is a real-linear isomorphism intertwining these endomorphisms.
It may additionally be required to preserve a specified quadratic form, but
the obstruction below already holds without that additional requirement.

The class permits all complex phases, not just real transfer matrices. It is
complete under this stated graph/current contract. It is not asserted that
the particular source gates generate every member of the class, or that every
physical boundary reading must obey this contract.

## 2. General lossless relation and marked regrouping

Let `L` be a finite-dimensional label Hilbert space, possibly one-dimensional,
and consider a unitary two-port relation

\[
\binom{a'}{b'}=S\binom a b,
\qquad S=\begin{pmatrix}u&v\\w&z\end{pmatrix},
\qquad S^\dagger S=I,
\tag{3}
\]

where each block acts on `L`. If `v` is invertible, solving the first equation
for `b` gives the marked boundary graph

\[
\binom{b'}b=T\binom a{a'},\qquad
T=\begin{pmatrix}
w-zv^{-1}u&zv^{-1}\\
-v^{-1}u&v^{-1}
\end{pmatrix}.
\tag{4}
\]

Define

\[
\Sigma_L=\operatorname{diag}(I_L,-I_L).
\]

Unitary norm balance in (3) is precisely

\[
\|a\|^2-\|a'\|^2=\|b'\|^2-\|b\|^2.
\]

Because (4) is a total graph on its independent data, this proves

\[
\boxed{T^\dagger\Sigma_LT=\Sigma_L.}
\tag{5}
\]

This is a source-side current identity. It does not identify current with the
positive native charge, Hilbert norm, spectral energy, or Lorentz determinant.

Conversely, every matrix `T` satisfying (5) gives a lossless relation of the
form (3) through this regrouping. Write its blocks as `T_ij`. The lower-right
block is invertible because

\[
T_{22}^\dagger T_{22}=I+T_{12}^\dagger T_{12}.
\]

Solving for `a'` gives

\[
S=\begin{pmatrix}
-T_{22}^{-1}T_{21}&T_{22}^{-1}\\
T_{11}-T_{12}T_{22}^{-1}T_{21}&T_{12}T_{22}^{-1}
\end{pmatrix}.
\tag{6}
\]

Equation (5) now gives norm preservation of (6); in finite equal dimensions
this is unitarity. Thus (5) is an exact characterization of this total
lossless boundary-graph class, not merely a necessary check on sample words.

If `v` in (3) is singular, the original unitary relation remains meaningful,
but the marked regrouping need not be a total graph. Such a point is not an
additional invertible transfer matrix and cannot be used as one by a limiting
or partial-inverse convention. Another regrouping is a separately specified
boundary contract.

## 3. All phases and the source receiver relation

For the source pulse relation, (4) gives

\[
T_Q=\frac1s\begin{pmatrix}1&-c\\c&-1\end{pmatrix}.
\tag{7}
\]

For the Fourier edge in (1), direct substitution gives

\[
\boxed{T_{E(k)}=e^{-ik}T_Q.}
\tag{8}
\]

A scalar phase in the time-update relation must be treated before regrouping.
It need not remain a scalar phase of the resulting transfer. In particular,

\[
\boxed{
T_{e^{-i\beta}E(k)}=e^{-ik}D_\beta T_QD_\beta,
\qquad D_\beta=
\operatorname{diag}(e^{-i\beta/2},e^{i\beta/2}).}
\tag{9}
\]

Both `D_beta` and the scalar in (8) preserve the same current. Arbitrary
source-side unitary phase conventions therefore do not escape (5).

For the receiver, let

\[
L=\mathbb C^{26}_{\rm pulse}\otimes
\mathbb C^{26}_{\rm memory},\qquad
\mathsf J|i,j\rangle=|j,i\rangle.
\]

The source specifies `J^dagger=J`, `J^2=I` on the entire label space and

\[
Q_{\mathsf J}=\begin{pmatrix}cI&-s\mathsf J\\
s\mathsf J&cI\end{pmatrix}.
\tag{10}
\]

Its marked transfer is exactly

\[
\boxed{T_{\rm rec}=T_Q\otimes\mathsf J.}
\tag{11}
\]

The phase-complete versions of (8)--(9) are tensorized with this same
`J`. No label sector is projected out. The formulas hold for all occupied
encoded memories, superpositions, and entanglement with additional identity
factors. This is the 26-code memory sector of the source, not a new claim of
identical receiver behavior on every raw memory configuration.

The alternative signed regrouping in predecessor section 6 gives

\[
T_{\rm alt}=\frac1c
\begin{pmatrix}1&-s\\-s&1\end{pmatrix},\qquad
T_{\rm alt}^\dagger\Sigma T_{\rm alt}=\Sigma.
\tag{12}
\]

Its different positive eigenvalues do not remove the common-current
constraint. A simultaneous reversal of the two cut orientations is a change
of convention on both ends. A one-sided reversal instead transports opposite
current conventions and must be recorded as such; see section 8.

## 4. Deriving the actual spatial transfer of the full pulse

Regrouping the on-site coin alone is not yet the spatial transfer of the
complete pulse. We now derive that transfer from the real-space form of (1).

Use the source Fourier convention
`hat(a)(k)=sum_x exp(-ikx) a_x`. Write the on-site intermediate amplitudes as

\[
u_x=ca_x-sb_x,\qquad v_x=sa_x+cb_x.
\tag{13}
\]

For physical stationary energy `E`, define

\[
\lambda=e^{-i(E-\beta)}.
\]

The edge equations following from (1) are

\[
\lambda a_x=cu_x-sv_{x+1},\qquad
\lambda b_{x+1}=su_x+cv_{x+1}.
\tag{14}
\]

Take the fixed cut data

\[
w_x=\binom{a_x}{u_x}.
\]

Eliminating the other two amplitudes gives

\[
v_{x+1}=\frac{cu_x-\lambda a_x}{s},\qquad
b_{x+1}=\frac{u_x}{s\lambda}-\frac{ca_x}{s}.
\]

Using (13) at `x+1`, or equivalently (7), therefore proves

\[
\boxed{w_{x+1}=A(\lambda)w_x,\qquad
A(\lambda)=\frac1{s^2}
\begin{pmatrix}
c^2-\lambda&c(1-\lambda^{-1})\\
c(1-\lambda)&c^2-\lambda^{-1}
\end{pmatrix}.}
\tag{15}
\]

This formula is total for every nonzero `lambda`, since the source `s` is
nonzero. Direct expansion, using `c^2+s^2=1`, gives `det A=1`.

For real physical energy, `|lambda|=1`. The actual rightward stationary
current through the edge is

\[
j_x=\|u_x\|^2-\|\lambda a_x\|^2
=-w_x^\dagger\Sigma w_x,
\qquad \Sigma=\operatorname{diag}(1,-1).
\tag{16}
\]

Unitarity of the edge in (14) makes this equal to
`||lambda b_(x+1)||^2-||v_(x+1)||^2`. Unitarity of the on-site relation
at `x+1` makes that equal to
`||u_(x+1)||^2-||a_(x+1)||^2`. Hence

\[
\boxed{j_{x+1}=j_x,\qquad A(\lambda)^\dagger\Sigma A(\lambda)=\Sigma.}
\tag{17}
\]

The current is therefore derived at the actual spatial cut, including the
complete pulse period and its time phase. It is not inferred solely from
the determinant of an auxiliary Hermitian matrix.

The trace of (15) is

\[
\operatorname{tr}A(\lambda)
=\frac{2c^2-\lambda-\lambda^{-1}}{s^2}
=\frac{1-5\cos(E-\beta)}2.
\tag{18}
\]

A propagating spatial eigenphase `k` therefore obeys

\[
2\cos k=\operatorname{tr}A,
\qquad \cos(E-\beta)=\frac{1-4\cos k}{5},
\tag{19}
\]

which is precisely the source dispersion. In this calculation `k` is a
transfer eigenphase; it is not a second phase available for independent
selection after fixing `E`. In a spectral gap the same transfer describes
evanescent solutions. Nothing here asserts a propagating Bloch mode at a
gap energy.

## 5. Spatial receiver transfer and arbitrary retained labels

On the receiver edge, (14) becomes

\[
\lambda a_x=cu_x-s\mathsf Jv_{x+1},\qquad
\lambda b_{x+1}=s\mathsf Ju_x+cv_{x+1}.
\tag{20}
\]

All receiver labels are energy-degenerate in the pinned source, so the same
scalar `lambda` applies to the whole label space. Solving (20) and then
using the on-site relation gives

\[
\boxed{w_{x+1}=[A(\lambda)\otimes\mathsf J]w_x.}
\tag{21}
\]

Consequently a finite source pulse segment with its receiver has directional
transfer `A(lambda)^N` and a retained unitary label factor. More generally,
a declared finite sequence of factorized directional transfers and unitary
label operations has total transfer

\[
\mathcal A=A_{\rm tot}\otimes U_L,
\qquad A_{\rm tot}^\dagger\Sigma A_{\rm tot}=\Sigma.
\tag{22}
\]

The order of the label operations is retained in `U_L`; they need not commute.
This general network statement is not a claim that the full many-particle
capture scattering problem has been solved by (22).

If the explicitly selected four-coordinate reading is the directional
marginal of a complete boundary coherency,

\[
r(X)=\operatorname{Tr}_L X,
\]

then for every Hermitian `X`, including correlated or entangled data,

\[
\boxed{
r(\mathcal AX\mathcal A^\dagger)
=A_{\rm tot}\,r(X)\,A_{\rm tot}^\dagger.}
\tag{23}
\]

This follows from unitary invariance of the partial trace on `L`. The full
labels continue to exist in the apparatus; the marginal is a declared reading,
not a physical erasure. Equation (23) does not assert that every possible
four-coordinate reading of the joint directional/label state is this marginal.

## 6. The complete same-cut class and finite networks

For the scalar boundary carrier define

\[
\mathcal A_\Sigma=
\{A\in\operatorname{GL}_2(\mathbb C):A^\dagger\Sigma A=\Sigma\}.
\tag{24}
\]

Sections 2--5 place all the displayed source graphs in this class whenever
their independent variables define the stated total graph. The class is
closed under products and inverses and admits all complex phases. By (6), it
is exactly the class of total lossless linear graphs with this marked current
contract. This is completeness of a mathematical contract, not a physical
completeness assertion about all TWIST-J apparatuses.

The inclusion extends to a finite lossless network with internal unitary
connections at a real stationary phase whenever internal elimination gives a
total external incoming-to-outgoing map. Sum the norm identities of all nodes.
Every internal connection appears once as an output and once as an input with
the same norm, so it cancels. The external map preserves norm and is unitary
in the finite equal-dimensional external spaces. If its transmitting block
is invertible, (4)--(5) put its transfer in (24). At a singular graph or an
unresolved internal resonance this conclusion is conditional on the existence
of the specified total external map; no inverse is supplied by convention.

For a different but fixed nondegenerate current of signature (1,1), a fixed
basis change transports it to `Sigma`. The conclusions below are invariant
under that simultaneous basis change on input and output.

## 7. Universal Hermitian-congruence obstruction

For `A in A_Sigma`, define the real four-dimensional action

\[
R_A:\operatorname{Herm}_2(\mathbb C)\longrightarrow
\operatorname{Herm}_2(\mathbb C),\qquad R_A(X)=AXA^\dagger.
\tag{25}
\]

Inverting `A^dagger Sigma A=Sigma` and multiplying by `A` and `A^dagger`
gives

\[
\boxed{R_A(\Sigma^{-1})=\Sigma^{-1}.}
\tag{26}
\]

The nonzero current vector is fixed for every admitted transfer, independently
of its phases, length, label state in (23), or factorization.

For the target (2),

\[
\chi_{L_J}(1)=-(2-\varphi)\ne0.
\tag{27}
\]

Suppose a real-linear isomorphism `I` satisfied `I R_A=L_J I`. Applying it
to (26) would make the nonzero vector `I(Sigma^-1)` a fixed vector of `L_J`,
contradicting (27). Thus

\[
\boxed{\text{No member of }\mathcal A_\Sigma\text{ admits the proposed
full four-coordinate intertwiner.}}
\tag{28}
\]

The result is pointwise in every admitted phase context. A context-dependent
similarity using the same context map on both sides also fails pointwise.
A quadratic-form equation cannot repair the absent intertwiner. In particular,
the difference between signatures (1,3) and (3,1), and any explicitly fixed
overall sign, have no bearing on this obstruction. Those issues would still
require resolution in any other route that survives the action test.

### 7.1 Full characteristic-polynomial classification

There is a stronger universal identity:

\[
\boxed{
\chi_{R_A}(z)=(z-1)^2
\left[z^2-\bigl(|\operatorname{tr}A|^2-2\bigr)z+1\right].}
\tag{29}
\]

To prove it, take a unit-modulus scalar `eta` with `eta^2=det A` and put
`A0=eta^-1 A`. Such an `eta` exists because (24) gives `|det A|=1`.
Then `A0 in SU(1,1)` and the congruence is unchanged. The inverse formula
for a determinant-one matrix, compared with
`A0^-1=Sigma A0^dagger Sigma`, shows

\[
A_0=\begin{pmatrix}\alpha&\gamma\\
\overline\gamma&\overline\alpha\end{pmatrix},
\qquad |\alpha|^2-|\gamma|^2=1.
\]

Thus `t=tr A0` is real, `t^2=|tr A|^2`, and the two eigenvalues of `A0`
are `r,r^-1`. Its characteristic polynomial is real. The complexification
of (25) has matrix `bar(A0) tensor A0` after vectorization. Its eigenvalues,
with algebraic multiplicity, are therefore `r^2,1,1,r^-2`. This eigenvalue
statement for a tensor product holds also for repeated or nondiagonalizable
matrices by triangularization. Finally

\[
r^2+r^{-2}=(r+r^{-1})^2-2=t^2-2,
\]

which proves (29) without a diagonalizability restriction.

The real parameter in the last quadratic is at least `-2`. The action may
have a hyperbolic pair, an elliptic pair, or a parabolic degeneracy, but it
always retains the two unit eigenvalues. It cannot have the simultaneous
nontrivial hyperbolic and compact factors in (2). This includes the actual
full spatial transfer (15), not merely the positive polar factor of one coin.

## 8. Scope exclusions that are essential to the theorem

1. **Full capture channels.** The source capture contact couples a two-object
   relative state, token and pulse arrangements. Those are additional channels.
   They do not automatically form a closed two-amplitude boundary graph at the
   pulse cut. An effective pulse map obtained by omitting open channels need
   not belong to (24). The theorem does not exclude the full capture law.
2. **General joint label readings.** Equation (23) proves the result for an
   explicitly chosen directional marginal of a factorized transfer. Other
   readings of retained label coherences are not classified by (23). Choosing
   an eigenlabel sector also requires a declared preparation and cannot replace
   the source's arbitrary occupied-memory contract without being recorded.
3. **Higher channel number.** A `2m`-amplitude transfer preserves `Sigma_m` and
   fixes `Sigma_m^-1` under full congruence, but its full Hermitian carrier has
   real dimension `4m^2`. A four-dimensional quotient or invariant reading may
   annihilate that fixed vector. If a linear reading `r` intertwines with `L_J`,
   a necessary condition is `r(Sigma_m^-1)=0`; it is not a contradiction by
   itself. The associated form, preparation, and record preservation require
   separate proof.
4. **Different current forms at the two ends.** The relation
   `A^dagger Sigma_out A=Sigma_in` implies transport
   `A Sigma_in^-1 A^dagger=Sigma_out^-1`, not a fixed vector in one already
   identified fiber. Identifying those fibers is additional source data.
5. **Orientation reversal on only one side.** If a declared endomorphism obeys
   `A^dagger Sigma A=-Sigma`, its congruence has eigenvalue `-1`. The target also
   excludes this because `chi_LJ(-1)=5(2+phi) != 0`. Ordinary coherent
   reorientation of both ends returns the plus-current contract. This statement
   does not erase the need to record which convention is used.
6. **Singular or non-total relations.** A boundary relation with no total
   invertible transfer is not a counterexample to (28); the proposed
   four-coordinate endomorphism has not been supplied there.
7. **Other layers and arithmetic reductions.** This real-linear obstruction
   does not alter the residual `Phi` comparison, the first-order finite-field
   trace form, or any canonical status. No star-compatible integral reduction,
   physical spacetime, original-U realization, or occurrence law is asserted.

## 9. An admissible next covariant class

A source-derived covariant successor can declare a context set `C`, a context
transition `f`, a two-amplitude fiber `V_xi` and its nondegenerate current
`Sigma_xi` for every context. Its actual source transfer must satisfy

\[
T_\xi^\dagger\Sigma_{f(\xi)}T_\xi=\Sigma_\xi.
\tag{30}
\]

It must also supply the context-dependent form and any integral lattice and
involution required by the target comparison. A proposed covariant Hodge map
would obey

\[
I_{f(\xi)}R_{T_\xi}=L_J I_\xi.
\tag{31}
\]

The current vectors then give a necessary equation

\[
u_\xi=I_\xi(\Sigma_\xi^{-1})\ne0,
\qquad u_{f(\xi)}=L_Ju_\xi.
\tag{32}
\]

Thus periodic source contexts supply a further exact test. If `f^N(xi)=xi`
with the same marked fiber and map on return, then `L_J^N u_xi=u_xi`.
The target's hyperbolic eigenvalues are `phi^2,phi^-2`, and its compact
eigenvalues are the primitive tenth roots `zeta_10,zeta_10^-1`. Therefore a
nonzero returned current vector requires `10` to divide `N`. For such an `N`,
the fixed-vector test permits only the compact target plane; it does not
construct the rest of the covariant identification. This observation applies
only when the stated target step is used at every context transition.

The source must determine the contexts, metrics, transitions and identifications
independently. Setting `I_n` recursively using a desired `L_J`, or defining
`Sigma_out` from an arbitrary desired transfer, would make (30)--(31) a
tautological representation choice rather than a positive physical result.

## 10. A precise positive boundary for additional channels

There is no general obstruction to accommodating a complex two-amplitude
action inside a larger lossless transfer. For any `K in GL_2(C)`, set

\[
\mathcal A=\operatorname{diag}\bigl(K,(K^\dagger)^{-1}\bigr),
\qquad H=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}.
\]

Then direct block multiplication proves

\[
\mathcal A^\dagger H\mathcal A=H.
\tag{33}
\]

The conserved current has signature (2,2), and the first two-amplitude
subspace is totally isotropic for that current. Its separate Hermitian
congruence is `X -> K X K^dagger`, which need not have a fixed current vector.
This is an algebraic boundary witness for the scope of (28), not a source
construction, a selected reading, or permission to insert the desired Hodge
matrix `K`. The complementary channels remain part of the full accounting.

A worthwhile positive successor would derive a genuine additional coherent
channel and its relative phase from the actual capture/receiver relations,
then establish a complete reading, its form and lattice, and compatibility
with occupied records. The existing scalar phase or an unrecorded change of
port grouping cannot perform that task.
