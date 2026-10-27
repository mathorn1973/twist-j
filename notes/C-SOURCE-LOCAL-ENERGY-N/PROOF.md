# A fixed-source obstruction to nearest-neighbor energy action

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1784](https://github.com/mathorn1973/twist-j/issues/1784).
The prospective [CONTRACT.md](CONTRACT.md) is public at
`a07b8909d2926e223549433528a189a80d14bc09`.
Independent scientific acceptance is not asserted.

For the unchanged plus source, every Hamiltonian in the frozen bare
nearest-neighbor class has original-energy action error greater than
2E0/5. This exceeds the required E0/1200. The proof uses one normalized
finite-support dual vector and exact spectral inequalities. It does not
enumerate a long energy tail or use the predecessor's tiny matrix element
on unrelated inputs.

The mathematical premises are the original Canon v105 step and
nominated logarithm, together with the conditional PR1777 source and
its exact normalization. The later PR1781 and PR1783 spectral and
finite-energy constructions motivate this question but are not proof
premises: no cut-mass estimate, absence of an atom at 1, large-degree
polynomial certificate or acceptance of those successors is used.

The result concerns physical interaction diameter at most one in the
original occupation lattice. It does not decide diameter two, arbitrary
fixed microscopic ranges, data-dependent dressed encodings, or a
different declared energy law.

## 1. Frozen source, energy and physical comparison

Keep the original receiver-calibrated unitary and its nominated energy:

\[
 U=U_{\rm rec},\qquad Q=E_0 f(U),\qquad E_0>0,
 \qquad f(e^{-i\theta})=\theta\quad(0\le\theta<2\pi).
 \tag{P1}
\]

In particular f(1)=0. No branch of the logarithm is changed. Write

\[
 B=(e_2-e_3)/\sqrt2,\qquad A=(e_1-e_4)/\sqrt2,
 \qquad \beta=4\pi/5,\qquad g=2\pi/5,
\]
\[
 \chi=|R=97,r=0,iB;c=97,\text{token},l=0\rangle
       \otimes\Xi,
\]
\[
 \psi_\pm=\frac{[I\pm(U^2-U^{-2})]\chi}{\sqrt Z},
 \qquad Z=\frac{39521+154\sqrt5}{15625}.
 \tag{P2}
\]

Here Xi is any normalized state of the original 26-label old memory and
a passive reference. Both sources have the displayed normalization by
the frozen [PR1777 source identity](https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-FINITE-PHASE-OCCUPIED-RECORD-N/ACTIVE_EQUAL_SPECTRUM.md).
The 25-label restriction excluding d0 is needed for the inherited fresh
write contrast, not for the energy bound proved here. Mixed inputs are
included by purification. Operators on the model below act as identity
on every passive reference.

The original physical positions of the two object constituents are

\[
 x_A=R+r,\qquad x_B=R-r.
 \tag{P3}
\]

Retain the original occupation isometry
\(\mathcal I=\mathsf{Emb}\,\Gamma^{-1}D_2^*\), with
\(D_2=\operatorname{diag}(1,i,i,-1)\). Its diagonal phase gauge is not
discarded. The object uses its original subbank h1,...,h4, disjoint
from the token, pulse and receiver subbanks. In particular a carrier
or receiver occupation cannot fill a missing object occupation at a
site. The receiver is at 100. The nine onsite identity spectators and
outside identities retain their original convention.

For any fixed normalized ancillary ready state a independent of the
input data, put

\[
 V\phi=\mathcal I\phi\otimes a.
 \tag{P4}
\]

The ancillary state may be entangled across ancillary sites. A fixed
mixed ancillary state may be purified with another passive reference.
Ancillary factors have declared physical locations. Each physical term
H_X acts as identity on all data and ancillary factors outside X, with
diam(X)<=1 in the original integer lattice. Thus X is contained in one
site or two adjacent sites.

Finite sums \(\widetilde H=\sum_X H_X\) suffice. The same result applies
to an infinite sum if \(V\psi_+\) is in its operator domain and partial
sums converge on that vector, or if the specified sum has convergent
matrix elements giving the same action and the matrix element used
below. These are domain and convergence hypotheses, not conclusions
inferred from formal locality. Without a well-defined source action,
the comparison in the contract is not satisfied.
Strong resolvent convergence alone is not being substituted for this
action or matrix-element convergence.

Individual terms need not be positive or conserve charge for this
proof. Consequently the result includes the smaller desired class of
positive charge-conserving Hamiltonians. Neither their strengths nor
their number nor the ancillary onsite dimensions are bounded here.

## 2. Object parity and one exact backward-step vector

The unchanged ordered factors are

\[
 U=P_\beta\Gamma S_R S_r E_{\rm rec}Q_p M_2 C,
 \qquad
 M_2=\frac{(I+2iX)\otimes(I+2iX)}5.
 \tag{P5}
\]

Their complete actions are given in the frozen
[PR1779 factorization](https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md).
Here they are the original infinite-coordinate factors, without cyclic
wraps. Contact C changes no positions and rotates the pair iB token,
A pulse-bank-1 by the matrix with columns (3/5,4/5) and (-4/5,3/5).
The carrier factors change no object positions. The combined forward
object streaming changes (x_A,x_B), according to the outgoing coin, by

\[
 e_1:(-1,-1),\quad e_2:(-1,+1),\quad
 e_3:(+1,-1),\quad e_4:(+1,+1).
 \tag{P6}
\]

Inverse streaming reverses these changes; its subsequent inverse coin
and contact again change no positions. Hence every complete forward or
inverse step flips the parity of each object position. Starting from
the two objects at 97, every basis component of U^k chi has both object
positions odd for even k and even for odd k. This includes negative k.
It follows that

\[
 \mu_n:=\langle\chi,U^n\chi\rangle=0
       \quad\text{for every odd integer }n,
 \tag{P7}
\]

and every basis component in either source psi_+ or psi_- has both
object positions odd. In particular its entire object subbank is
vacuum at both even sites 96 and 98. This is a statement about the
whole source support, not only its seed component.

Define the normalized witness

\[
 w=U^{-1}\chi.
 \tag{P8}
\]

For brevity in the following expressions, kets displaying r and the
object coin also have R=97, c=97, token label 0 and the unchanged Xi.
Applying the adjoint factors in their exact order gives

\[
 \boxed{
 w=e^{i(\beta+g)}\frac{i}{\sqrt2}
       \bigl(|r=+1\rangle M_2^*e_2
              -|r=-1\rangle M_2^*e_3\bigr).
 }
 \tag{P9}
\]

Indeed P_beta^* and Gamma^* first supply the displayed phase at r=0.
The inverse center shift fixes e2,e3, and the inverse relative shift
sends them to r=+1,-1 respectively. The inverse pulse and receiver
factors fix the token. M2^* then changes only the coin; the final C^*
is identity because r is nonzero. Thus w is entirely token, with an
object constituent at each of 96 and 98 in every basis component.
The token stays at 97 and the memory remains at 100. The two displayed
relative-coordinate sectors are orthogonal, so (P9) also directly has
norm one.

## 3. The witness is forbidden for each actual phase separately

**Lemma P1.** For every admitted Xi, either source phase, every term
with diam(X)<=1 and every fixed readiness in (P4), whenever the
indicated action or matrix element is defined,

\[
 \langle Vw,H_X V\psi_\pm\rangle=0.
 \tag{P10}
\]

**Proof.** A set of diameter at most one cannot contain both 96 and
98. At an omitted site, every source component has the object subbank
in vacuum by (P7), while every witness component has a nonzero object
occupation by (P9). The term is identity on that subbank. Its matrix
element is therefore zero, regardless of its action on the other
onsite factors or on ancillas. The disjoint carrier and memory
subbanks cannot change this orthogonality.

The argument holds for each pair of occupation basis components;
linearity gives the complete superposed source and witness. The
diagonal gauge in the physical isometry changes only their phases and
preserves the zero. Entanglement within a does not change a data
factor on which the term is identity. Passive references and arbitrary
old-memory amplitudes likewise do not change the missing object
occupation. QED.

Summing (P10) for the plus source, with the stated convergence when
needed, and using
\(\|Vw\|=1\) gives

\[
 \|\widetilde H V\psi_+-VQ\psi_+\|
 \ge |\langle w,Q\psi_+\rangle|.
 \tag{P11}
\]

Equivalently w belongs to the full forbidden subspace for each source
in the contract, not merely to a coarse outside-neighborhood subspace.
Its expectation in (P11) is a concrete dual lower bound on the
forbidden energy action. No reachability sufficiency is assumed.

## 4. Exact low moments needed by the spectral bound

Let Pi_t project onto the token arrangement. Since M2 B=B, the forward
token branch is exactly

\[
 \Pi_t U\chi=\frac35e^{-i\beta}\frac{i}{\sqrt2}
        \bigl(|r=-1\rangle e_2-|r=+1\rangle e_3\bigr).
 \tag{P12}
\]

The remaining branch is pulse, orthogonal to w. In (P12) no contact
phase remains after streaming because r=+1 or -1. The two cross-coin
entries of M2 are

\[
 \langle e_2,M_2e_3\rangle
 =\langle e_3,M_2e_2\rangle=-4/5.
\]

Taking the inner product of (P9) and (P12), the two equal
relative-coordinate contributions give

\[
 \mu_2=\langle U^{-1}\chi,U\chi\rangle
       =\frac35\frac45e^{-i(2\beta+g)}
       =\boxed{12/25},
 \tag{P13}
\]

because 2beta+g=2pi. This is a two-branch symbolic overlap, not an
executed moment enumeration. The common Xi drops out as its unit norm.

For the fourth moment, only the already frozen normalization is
needed. Put D=U^2-U^{-2}, so D^*=-D. Then

\[
 (I+D)^*(I+D)=3I-U^4-U^{-4},
 \qquad Z=3-2\operatorname{Re}\mu_4.
 \tag{P14}
\]

This retains the full source, including all its pulse branches. In
particular no token-only replacement of psi_+ is being made.

## 5. A positive spectral integral for the fixed plus source

Use the seed probability measure mu_chi under the angle convention
(P1), so \(\mu_n=\int e^{-in\theta}\,d\mu_\chi(\theta)\).
The spectral theorem and commutation of Q with U give

\[
 b_+:=\langle w,Q\psi_+\rangle
   =\frac{E_0}{\sqrt Z}
      \int\theta\,(z+z^3-z^{-1})\,d\mu_\chi,
 \qquad z=e^{-i\theta}.
 \tag{P15}
\]

All integrands are bounded Borel functions on 0<=theta<2pi. The
definition at the cut is exactly (P1); neither exclusion of an atom
there nor a limiting Fourier series is required.

Since

\[
 \operatorname{Im}(z+z^3-z^{-1})
   =-2\sin\theta-\sin3\theta
   =-\sin\theta(1+4\cos^2\theta),
\]

and the odd moments mu_1 and mu_3 vanish by (P7), the integral of
\(\sin\theta(1+4\cos^2\theta)\) is zero. Therefore

\[
 \frac{\sqrt Z}{E_0}\operatorname{Im}b_+
 =\int(\pi-\theta)\sin\theta(1+4\cos^2\theta)
                                      \,d\mu_\chi.
 \tag{P16}
\]

For every theta in [0,2pi),

\[
 (\pi-\theta)\sin\theta\ge\sin^2\theta.
 \tag{P17}
\]

To see this, set x=|pi-theta| in [0,pi]. The two sides are
x sin x and sin^2 x, respectively, and x>=sin x>=0. Multiplying by
1+4cos^2(theta), then integrating, gives

\[
 \begin{aligned}
 \frac{\sqrt Z}{E_0}\operatorname{Im}b_+
 &\ge\int\bigl(\sin^2\theta+\sin^2(2\theta)\bigr)
                                             \,d\mu_\chi\\
 &=1-\frac{\operatorname{Re}\mu_2+
                   \operatorname{Re}\mu_4}{2}\\
 &=\boxed{\frac Z4+\frac1{100}}.
 \end{aligned}
 \tag{P18}
\]

The last equality uses (P13)-(P14). The right side is positive, so
the modulus of b_+ is at least this imaginary-part bound. This fixes
the failing input as psi_+; it is not a choice of a bad phase after
examining the implemented Hamiltonian.

## 6. Nearest-neighbor action theorem and its precise boundary

**Theorem P2.** For every admitted normalized old-memory/reference
state Xi and every Hamiltonian in the class of Section 1,

\[
 \boxed{
 \|\widetilde H V\psi_+(\Xi)-VQ\psi_+(\Xi)\|
 \ge E_0\frac{Z/4+1/100}{\sqrt Z}
 >\frac{259}{640}E_0>\frac25E_0.
 }
 \tag{P19}
\]

**Proof.** Combine (P11) with (P18). For the explicit rational lower
bound, elementary squaring gives 11/5<sqrt(5)<5/2. Substitution into
the exact Z of (P2) yields

\[
 51/20<Z<64/25,\qquad \sqrt Z<8/5.
\]

Consequently

\[
 \frac{Z/4+1/100}{\sqrt Z}
 >\frac{51/80+1/100}{8/5}
 =\frac{259}{640}>\frac{256}{640}=\frac25.
\]

All estimates are strict in the last comparison. QED.

Thus the frozen action requirement less than E0/1200 cannot hold even
for the fixed plus source. This lower bound is uniform over all 26
old-memory labels and their arbitrary passive reference correlations.
For a retained setting register, take its fixed plus input and the
same register state in the dual witness. Allowing a different
Hamiltonian or a different data-independent ready state for this
setting cannot avoid (P19): the proof already quantifies over every
Hamiltonian and readiness for that single source. A local term that
also acts on a counted setting register still has the same missing
object subbank outside X. No common-Hamiltonian cancellation between
the plus and minus sources is used.

The obstruction survives arbitrary finite interaction order within
each allowed site set, arbitrary coupling strengths and arbitrarily
many fixed-ready ancillary factors, including entangled readiness.
It applies to the entire physical action error, so leakage out of the
code or into ancillas cannot cancel its projected matrix element.

The theorem does not establish a lower bound for the minus source by
itself, although the same forbidden witness is available for it. It
does not rule out accurate endpoint or continuous-time simulation by
a different energy law. Nor does it rule out a construction whose
initial encoding is dressed in a data-dependent manner rather than
(P4); such a construction must account for its preparation and its
comparison with the original ports and energy.

For diameter two, a term may contain both 96 and 98, so Lemma P1 no
longer follows from the displayed witness. Whether the actual source
admits the required energy approximation at that or another specified
larger microscopic range remains open here. A small forbidden tail,
if found at a larger range, would only remove this necessary
obstruction; a positive construction would still need its full
generator, energy action and trajectory error accounts.

## 7. Separate review obligations

1. Check the fixed logarithm convention, unchanged source, normalization
   and complete 26-label memory/reference scope in (P1)-(P2).
2. Check the original physical positions, disjoint object subbank and
   retained diagonal occupation gauge.
3. Check both forward and inverse factor orders and the parity change
   of each object position in (P5)-(P7).
4. Check the full backward-step vector (P9), including phases, absence
   of a pulse branch, positions and normalization.
5. Check that the entire support of each actual phase source has vacuum
   object subbanks at both 96 and 98; no source component is omitted.
6. Check termwise orthogonality for arbitrary ancillary entanglement,
   counted physical supports, passive references and all memory labels.
7. Check the operator-domain and sum-convergence assumptions, and the
   passage from the zero matrix element to the full action bound.
8. Check the two forward token branches, the cross-coin signs and the
   exact second moment (P12)-(P13).
9. Check the fourth-moment normalization identity (P14), without
   replacing the actual source by its token branch.
10. Check the fixed-plus spectral multiplier, odd-moment subtraction,
    pointwise inequality and constants in (P15)-(P19), including the cut.
11. Check uniformity for references and retained settings, and why the
    fixed-plus result also permits a separately chosen Hamiltonian and
    data-independent readiness for that setting.
12. Preserve the distinction between the proved diameter-one action
    obstruction and the open larger-range, dressed-encoding and
    different-energy questions. No source-energy sufficiency follows.

No scientific executable, numerical search, moment enumeration,
simulation or spectral computation was run. The proof uses exact
symbolic identities and elementary inequalities under the frozen
conditional model premises. Same-session authoring and adversarial
checks do not constitute independent external acceptance or change
Public Canon v105.
