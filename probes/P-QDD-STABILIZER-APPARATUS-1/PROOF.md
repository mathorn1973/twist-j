# Stabilizer circuit, flag uncompute and a retained-path control

**NON-CANONICAL / PREREGISTERED PROOF / RESULT-EXPOSED.**
Execution count at pin: zero. Public reservation: issue 854.
`P-QDD-STABILIZER-APPARATUS-1`, conditional L4 mathematical
apparatus/support scope. These are candidate proofs, not a public probe result.
The source proposal was supplied and its claimed answers were already known.
No scientific verifier was executed in preparing this package. Static review
does not constitute a formal run, independent experimental evidence or a pin.

## 1. Inputs, equality and the contribution relative to existing results

Public basis: `ac435f84b646ce8cb9a6c1601886c4f298881285`, ACTIVE Canon v77,
content `f7da754ffbcc37f1cbe02746025279ebd029520d`, Canon SHA-256
`63763a6adb6f61bb7a11b719ad61d55e2c26c6fdabd05b6bfe02b03ef1087969`,
462590 bytes. Authority is the public repository, not the supplied proposal.

Use the rational simplex space

\[
 V=\{v\in\mathbb Q^5:\mathbf1^Tv=0\},\qquad
 \langle v,w\rangle=v^Tw,\quad q(v)=v^Tv,
 \quad u_k=e_k-\mathbf1/5.
\]

Here `e_k` is a five-cell coordinate vector. Set
`Pi=I_5-11^T/5`; identity on V means Pi when represented on all five cells.
Thus `q(u_k)=4/5` and `u_i^T u_j=-1/5` for distinct labels. The independent
audit basis is `B_i=e_i-e_4`, `0<=i<4`; its Gram matrix is `I_4+11^T`.
It is different from a basis of four simplex vectors, whose Gram is
`I_4-11^T/5`. The audit never confuses these two metrics.

The complete circuit carrier is `Q^4_path tensor Q^2_flag tensor Q^5_cell`,
with 40 coordinates ordered `(path,flag,cell)`. The invariant subspace used
here has zero cell sum in each path/flag copy and dimension 32. This is a
selected mathematical apparatus type, with no physical realization
certificate. Prepared inputs are
`|0>_path tensor |0>_flag tensor v`. Source zero is allowed. All full-amplitude
equalities are literal ordered rational-coordinate equality.

For system operator comparisons, the independent domain is every rational
operator supported on V. For classical field intensities it suffices to use
outer products `vv^T`; density-operator or probability interpretation is an
additional premise. A coarse apparatus equality means equality of both linear
maps on all these operators. It excludes operations that access a retained
fine path or an earlier auxiliary record. Full auxiliary states are never
identified merely because their reduced maps agree.

The registered `QDD-J-AFFINE-APPARATUS-NONSELECTION` already owns stabilizer
averages, ranks 1/3, the comparison `k=2 -> E_low,E_high`, and four inequivalent
pure instruments at fixed weights. `QDD-INSTRUMENT-NONSELECTION` already owns
rational dilation existence and the failure of dilation existence to select
an instrument. This proof does not claim those as new. Its target is the
explicit group-controlled 40-mode circuit, the binary flag followed by exact
uncompute, the mixed retained-path alternative, complete subsequent maps,
invariance within the specified mixer class, and the fixed-lattice boundary.
The terminal-account composition is separately stated in RECORD-CONTRACT.md;
general reservoir bookkeeping is also prior work.

## 2. Controlled stabilizer circuit

Fix `k in F_5` before comparison. Let `g e_x=e_(k+2(x-k))`, so `g^4=I`.
It fixes k and cycles `(k+1,k+2,k+4,k+3)`. Define

\[
 H=\begin{pmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{pmatrix},
 \qquad W=H/2,
 \quad D_k=\operatorname{diag}(I,g,g^2,g^3),
 \quad V_k=(W\otimes I)D_k(W\otimes I).
\]

`H^T=H`, `H^2=4I`, and g is a coordinate permutation. Consequently V is
rational orthogonal, `V^-1=W D^-1 W`, and `V^4=I` on the full 20-mode
path/cell space and on its duplicated 40-mode flag extension. The circuit
implementation uses these split, route and recombine operations directly.
It contains no projector gate, target weight or numerical fitted coefficient.
Selecting the stabilizer and this architecture remains a disclosed design
choice made with the QDD targets known, not an independently established
physical selection law or a derivation from J.

On V introduce the analysis operators

\[
 P=(I+g+g^2+g^3)/4=\frac54u_ku_k^T,\quad
 R=(I-g+g^2-g^3)/4,\quad C=I-P-R,\quad Q=I-P,\quad J_C=gC.
\]

In these formulas I is identity on V. P, R and C are mutually orthogonal
projections of ranks 1,1,2. To see the ranks, the four-cycle representation
has one constant direction, one alternating direction and a two-dimensional
rotation plane. The ambient fifth fixed cell contributes another fixed
direction; the zero-sum restriction removes the global constant. Thus the
full five-cell stabilizer average has rank two, whereas P on V has rank one.
On C, `g^2=-I`, so `J_C^T=-J_C` and `J_C^2=-C`.

For a prepared path, the four output maps are the first column of V:

\[
 K_0=P,\qquad K_1=R,\qquad
 K_2=(C+J_C)/2,\qquad K_3=(C-J_C)/2.
\]

This follows by taking each signed row of H against `(I,g,g^2,g^3)/4`.
It gives `K_0^TK_0=P`, `K_1^TK_1=R`,
`K_2^TK_2=K_3^TK_3=C/2`, and `sum K_r^TK_r=I` on V.
Hence the signed outputs preserve total q; their LOW/HIGH energies are
`q(Pv)` and `q(Qv)`. The previous public simplex bridge, not a new basis
identification from this calculation, compares k=2 with the registered QDD pair.

When composing with the separate decoder source `S(z)` on the ordered sites
`Y0,...,Y4`, an additional label transport is essential. Freeze
`beta=(0,1,3,4,2)`, meaning `Yj -> beta(j)`, and `(T d)_beta(j)=d_j`.
Then `T S(z)=sum_(i<4) z_i u_beta(i)`, its missing vertex is u2 and its
coordinate at phase label 2 is `-sum(z)/5`. Consequently
`q(P_2 T S(z))=(sum z)^2/20`, whereas `q(T S(z))=z^T G z` with
`G=I_4-11^T/5`. This is a comparison after the circuit is fixed. Identifying
the decoder site order with the phase-label order without T would give a
different LOW function. The production circuit accepts F5 cell labels and
does not apply a hidden relabeling. G02 audits this transport on all four
source basis vectors and all sixteen energy polars independently.

## 3. E: binary flag and coherent uncompute

Let F flip the flag exactly on paths `r!=0`. It is a coordinate permutation
and `F^2=I`. Define the complete orthogonal circuit

\[
 \mathcal E_k=V_k^{-1}F V_k.
\]

It is self-adjoint and involutive on all 40 modes. For every v in V,

\[
 \mathcal E_k(|0,0\rangle v)
 =|0,0\rangle Pv+|0,1\rangle Qv.                 \tag{1}
\]

Indeed all powers of g fix Pv, so V leaves its prepared path unchanged.
For Qv the output on path zero is `PQv=0`; F therefore flips the whole
component's flag. Apply V inverse separately in the two flag copies. Each
component returns to path zero, and no fine path information survives there.
This proof also applies to an initially one flag, with the two flags exchanged.
F copies a property of orthogonal path labels, not an unknown system vector.

Discarding neither branch and observing the binary flag gives the system maps

\[
 \Phi^E_L(\rho)=P\rho P,\qquad \Phi^E_H(\rho)=Q\rho Q.       \tag{2}
\]

These are the usual mathematical Lueder maps under a density-operator
description. Each map is idempotent and the two cross-compositions are zero.
Fresh apparatus uses a fresh flag; passive rereading is not another interaction.
The outgoing coherent state in (1) still contains both components. Nothing in
this proof turns one component into a uniquely realized event.

## 4. R: retained fine paths and its complete subsequent map

The control stops after V; `apparatus.apply_r` also writes a redundant flag F
so the two variants have a common 40-mode interface. On a prepared input this
does not alter the four system amplitudes. LOW means r=0 and HIGH means the
three still-distinct paths r=1,2,3. A later system operation acts equally on
each retained path; the paths are not coherently recombined.

The resulting maps on every operator supported on V are

\[
 \Phi^R_L(\rho)=P\rho P,\qquad
 \Phi^R_H(\rho)=R\rho R+\tfrac12(C\rho C+J_C\rho J_C^T)
              =\mathcal T_k(\rho)-P\rho P,
 \quad \mathcal T_k(\rho)=\tfrac14\sum_{a=0}^3g^a\rho g^{-a}.     \tag{3}
\]

Expanding K2 and K3 cancels their cross terms and gives the middle expression.
Alternatively, summing all four output paths cancels cross terms between
different group powers by the orthogonality of W and gives T. Removing the
zero path gives the final expression. These identities prove whole-map
equality, not just equality on selected pure preparations or on their traces.

`T^2=T` because each power of g occurs four times in its double group sum.
Moreover `T Phi_L=Phi_L T=Phi_L`. Therefore
`(Phi_H^R)^2=(T-Phi_L)^2=T-Phi_L=Phi_H^R`; its two cross-compositions with
LOW vanish as well. This mixed idempotent map generally differs from
`Q rho Q`. It is not a counterexample inside the prior pure single-Kraus class.

For two settings k,l, either E or R at each setting and branches a,b, the
complete second-stage map is exactly `Phi_(l,b) Phi_(k,a)`. Its fine Kraus
maps are all ordered products `K_(l,s) K_(k,r)` with the specified branch
labels, not a coherent sum over different histories. Linearity proves this
for every operator, any subsequent rational system operation and further
finite compositions retaining the same auxiliary-access restriction.

## 5. All balanced rational mixers in the declared class

Let A be any rational orthogonal four-path matrix with
`A e_0=(s_0,s_1,s_2,s_3)^T/2`, where each s is +1 or -1. Let sigma be any
permutation of all four powers of g. Define
`V_A=A^T diag(g^sigma(r)) A`, with the matching inverse used for E.
For a fixed positive column its completions are exactly
`W diag(1,B)`, `B in O(3,Q)`: multiply by W transpose and use the fixed
first column. Signs are obtained by multiplying the rows of A by their signs.
This is the complete stated mixer class, not every reversible apparatus.

The output maps are `L_r=sum_t A_(t,r) A_(t,0) g^sigma(t)`.
For r=0 their coefficients are all 1/4, so `L_0=P`. Furthermore

\[
 \sum_r L_r\rho L_r^T
 =\sum_t A_{t0}^2 g^{\sigma(t)}\rho g^{-\sigma(t)}=\mathcal T_k(\rho).
\]

The cancellation uses `sum_r A_(t,r) A_(u,r)=delta_(t,u)`. Thus every such
R has exactly (3). V_A sends prepared Pv back to its prepared path, and
prepared Qv has no zero-path component. The proof of (1) therefore gives
exactly the same E for every member. Signed balanced columns and inverse
generators do not change the coarse statements. Fine path amplitudes need
not be equal; their complete records remain separately typed.

The finite verifier audits all 24 group orders, all 16 balanced column signs
and several nontrivial rational O(3) completions as separate families of
controls. It does not enumerate O(3,Q), nor claim its finite cases exhaust
all combinations. The displayed algebra carries the universal statement.

## 6. Two exact sequential discriminators

Write the g-cycle as `(a,b,c,d)` and set `v=e_a-e_c`. Then q(v)=2,
`gv=e_b-e_d` is orthogonal to v, and both lie in C. First LOW is zero and
first HIGH has unit normalized weight. E leaves v; R has the two retained
vectors `(v+gv)/2` and `(v-gv)/2`. For every j,

\[
 q(P_j x)=\tfrac54(u_j^Tx)^2.                         \tag{4}
\]

For j=b the E output vanishes. Each R vector has `u_b` inner product
+/-1/2 and projected energy 5/16; their sum divided by q(v)=2 is 5/16.
For j=a, E instead has `(5/4)/2=5/8`, while R again has 5/16. Thus

| First HIGH_k; second LOW | E | R |
|---|---:|---:|
| analyzer b | 0 | 5/16 |
| analyzer a | 5/8 | 5/16 |

For the independent preparation u_j, j!=k, the first HIGH fraction is 15/16
because normalized distinct simplex rays have squared overlap 1/16.
For E the second LOW_j amplitude coefficient is 15/16, giving joint fraction
225/256. For R, use `sum_l P_l=(5/4)I` on V and the transitive four-cycle:

\[
 \mathcal T_k(P_j)=\tfrac14\sum_{l\ne k}P_l=\tfrac5{16}I-\tfrac14P_k,
 \quad P_kP_jP_k=P_k/16,
 \quad \Phi_H^R(P_j)=\tfrac5{16}Q_k.
\]

Since `u_j u_j^T=(4/5)P_j` and `Tr(P_jQ_k)=15/16`, division by q(u_j)
gives joint fraction 75/256. Conditioning merely by division by the already
computed nonzero HIGH energy gives 15/16 for E and 5/16 for R.
These are rational energy fractions, or conditional density-model weights.
Calling them photon probabilities would require an extra occurrence law.

## 7. Single-setting lattices and a two-setting obstruction

Let `L=A_4={x in Z^5:sum x=0}` and `L_0=L^4`. With
`Lambda_*=(H^-1 tensor I)L_0`,

\[
 L_0\subseteq\Lambda_*\subseteq\tfrac14L_0,
 \qquad (H\otimes I)V_k(H^{-1}\otimes I)=D_k.
\]

H and the group permutations preserve L_0. Thus Lambda_* is a single full
lattice preserved by all V_k. It does not follow that path measurements or
the flag gate preserve that lattice. For primitive x in L, the vector with
x/4 in every path is in Lambda_*, while keeping only its path-zero component
leaves H times that vector with x/4 in every path, outside L_0.

Each default V has denominators dividing four. Consequently every default
E has denominators dividing 16. For a single fixed setting on
`L_1=L^8`, the full lattice `L_1+E_k L_1` lies between L_1 and `(1/16)L_1`
and is E_k-invariant because `E_k^2=I`. This is a lattice for the complete
single-setting operation, not one preserved by all its individual gates.
The denominator bound is for the fixed W circuit, not arbitrary rational A.

There is no common discrete full-rank lattice preserved by two distinct
default E_i,E_j in the same 32-dimensional restricted carrier. The same
obstruction rules out one in the full 40-mode extension. On the invariant
subspace `path0 tensor (flag0-flag1) tensor V`, (1) and its flag-one version
show that E_k acts as `2P_k-I`. On the plane spanned by u_i,u_j their product
has determinant one and trace `4*(1/16)-2=-7/4`. For completeness, put
`c=(u_i^Tu_j)/q(u_i)=-1/4`. In the ordered basis `(u_i,u_j)`,

\[
 2P_i-I=\begin{pmatrix}1&2c\\0&-1\end{pmatrix},\qquad
 2P_j-I=\begin{pmatrix}-1&0\\2c&1\end{pmatrix}.
\]

The product therefore has minimal polynomial

\[
 \lambda^2+\tfrac74\lambda+1,
 \quad\text{equivalently}\quad4\lambda^2+7\lambda+4.       \tag{5}
\]

Its discriminant is -15/16, hence it is irreducible over Q. Its monic
minimal polynomial has a noninteger coefficient, so its roots are not
algebraic integers. A map preserving a discrete full-rank lattice has an
integer matrix in a lattice basis and only algebraic-integer eigenvalues.
If both E's preserved the lattice, so would their product, contradicting (5).
This does not exclude larger architectures, different carriers, or an
amplitude representation with variable denominator and an explicit scale.

In particular `M_k=16E_k` is integer and `(z,s)->(M_k z,16s)` reads exactly
E_k(z/s). Its energy is `q(z)/s^2` and `q(M_k z)=256 q(z)`. This is an exact
growing-denominator representation, not a GL(Z) dynamics on a fixed lattice
and not an identification with the public Omega,U dynamics.

## 8. Audit, record support and disposition

`apparatus.py` is a direct routing implementation; it does not import the
reference maps. `verify.py` constructs separate five-cell projections,
spectral pieces and group-twirl maps. It compares the four independent
zero-sum basis vectors and all sixteen ordered products `B_i B_j^T`.
This proves equality of the finite linear maps if the exhaustive basis
checks pass; the verifier also directly feeds every ordered pair of settings
and both variants through both stages, preserving all fine paths, before
checking all four ordered binary-branch maps. The displayed numerical
discriminators are additional controls, not a substitute for these map checks.

The 40 full-coordinate bases additionally audit orthogonality, both inverse
directions, the fourth power, flag involution,
E involution and denominator divisibility. The 32 zero-sum ambient bases
audit invariance. The lattice audit checks the conjugacy, path-projection
counterexample and polynomial (5) on both basis vectors of every ordered
distinct-setting plane. Nonintegrality and the universal mixer statement
rest on the proofs above, not a numerical eigenvalue routine.

RECORD-CONTRACT.md and `record.py` attach a selected exact signed-buffer and
threshold account after the analyzers. The separate `record_audit.py`
compares its full stored histories with independently summed energy and
lifetime ordinals and is called by the verifier without a silent skip.
It supplies no physical L5 event stream, L6 measure, #539-compatible reset,
detector law or new proof of Born. Records, field energy and threshold counts
are distinct descriptions and are never counted as three energy stores.

Formal execution requires the complete frozen pin and public byte readback
on issue 854. These proofs receive no Canon status from preregistration. An exact failed
identity must be preserved; an integrity or missing-input failure is STOP.
No current QDD owner, claim, Canon byte or physical identifier changes here.

## Public references

- [QDD affine apparatus result](https://github.com/mathorn1973/twist-j/blob/ac435f84b646ce8cb9a6c1601886c4f298881285/probes/P-QDD-J-AFFINE-APPARATUS-1/RESULT.md).
- [Instrument nonselection result](https://github.com/mathorn1973/twist-j/blob/ac435f84b646ce8cb9a6c1601886c4f298881285/probes/P-QDD-INSTRUMENT-NONSELECTION-1/RESULT.md).
- [Current registered scopes](https://github.com/mathorn1973/twist-j/blob/ac435f84b646ce8cb9a6c1601886c4f298881285/canon/REGISTRY.tsv).
- [Existing reservoir accounting](https://github.com/mathorn1973/twist-j/blob/ac435f84b646ce8cb9a6c1601886c4f298881285/probes/P-DECODER-RESERVOIR-COUPLING-1/PROOF.md).
- [Existing passive optical design, noncanonical](https://github.com/mathorn1973/twist-j/blob/ac435f84b646ce8cb9a6c1601886c4f298881285/notes/DECODER-PASSIVE-REALIZATION-BRIDGE-1.md).
