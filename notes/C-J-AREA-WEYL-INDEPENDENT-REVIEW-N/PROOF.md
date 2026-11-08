# Independent derivation of the marked area and Weyl identities

```text
Author: A. M. Thorn
License: Apache-2.0
SPDX-License-Identifier: Apache-2.0
Visibility: PUBLIC
Scientific status: NON-CANONICAL, L1, candidate-T
Evidence status: ANALYTICAL_REVIEW_DERIVATION / BEFORE_REVIEW_EXECUTION
Review: C-J-AREA-WEYL-INDEPENDENT-REVIEW-N
Review reservation: https://github.com/mathorn1973/twist-j/issues/1587
Scientific session: Codex-R1-20261017-b053a37f
Target source pin: 6b459a66d670656bd02a09c26da666bd16c077fb
Target result head: e40b637b81f1a6fca99a543e970c83a4e0d45ebc
Public authority: Public Canon v103
Public authority base: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
```

This derivation was written from the frozen target PREREG and the named
public Canon definitions, before opening the target author's proof,
implementation, result, expected output, run record, diff or revealing
review comments. The target equations and proposed finite inventory were
already visible. The separation is therefore method-blind, not result-blind.
No scientific code execution supplies a premise of this document.
Analytical collaborators in this review session are not separate
independent scientific authors. A final review verdict requires the later
comparison and execution records; this proof does not announce that verdict.

## 1. Carriers, conventions and quantified claims

Fix the marked primitive fifth root `j` and the ring

\[
\mathcal O=\mathbb Z[j]=\mathbb Z[t]/(\Phi_5(t)),\qquad
\Phi_5(t)=1+t+t^2+t^3+t^4.
\]

The marking is fixed throughout. In the principal complex embedding it is
`j=exp(2*pi*i/5)`. The algebraic identities below do not replace that marking
by a measurement choice. Every element of O has a unique integer
coefficient expression in `1,j,j^2,j^3`. Indeed the polynomial is monic,
and `Phi_5(t+1)=t^4+5t^3+10t^2+10t+5` is Eisenstein at 5, so it is the
minimal polynomial of the primitive root. In particular O is an integral
domain of characteristic zero, and `j` has exact order 5.

Define

\[
J=1+j^2,\qquad \phi=-j^2-j^3,\qquad
T(a,b)=(Ja,\phi b),
\]
\[
\omega((a,b),(c,d))=ad-bc\quad\hbox{in }\mathcal O.
\]

This is a chosen O-bilinear alternating form on the entire infinite
rank-eight integer module O^2. It is not asserted to be a physical action,
a real energy, or the native update U. A matrix identity proved for all
`a,b,c,d in O` establishes the unbounded claim. Finite basis or residue
audits can check implementations of that identity but do not replace it.

For operators, `AB` means apply B first and then A. The five basis vectors
are indexed by the additive group F5. Exponents of Z, X and j, basis indices,
Weyl labels and central-phase exponents are reduced modulo 5. Their complex
coefficients use the marked j; residue-field scalars and complex scalars
remain different types.

## 2. Infinite-ring identity, inverse and alternating area

Expand in O, using `j^5=1`:

\[
J\phi=-(j^2+j^3+j^4+j^5)
=-(1+j^2+j^3+j^4)=j.
\]

There is an inverse inside O for each diagonal entry, not merely inside
its fraction field:

\[
J^{-1}=-j-j^2,\qquad \phi^{-1}=\phi-1=-1-j^2-j^3.
\]

For the first equality,
`(1+j^2)(-j-j^2)=-(j+j^2+j^3+j^4)=1`. For the second,

\[
\phi^2=j^4+2j^5+j^6=j^4+2+j=1-j^2-j^3=1+\phi,
\]

so `phi(phi-1)=1`. Consequently T is an automorphism of the complete
infinite module, with two-sided inverse

\[
T^{-1}(a,b)=((-j-j^2)a,(\phi-1)b).
\]

For arbitrary `u=(a,b)` and `v=(c,d)` in O^2, commutativity gives

\[
\omega(Tu,Tv)=(Ja)(\phi d)-(\phi b)(Jc)
=J\phi(ad-bc)=j\omega(u,v).
\]

Iteration, including negative powers through the displayed inverse, yields

\[
\omega(T^n u,T^n v)=j^n\omega(u,v)
\qquad(n\in\mathbb Z,\ u,v\in\mathcal O^2).
\]

For `e_1=(1,0)` and `e_2=(0,1)`, the area is 1 and the one-step area is j.
They differ. Thus exact one-step preservation of this O-valued form is
false. The complete form is preserved by `T^5`, and more generally by
`T^n` exactly when `5` divides n: sufficiency follows from `j^n=1`, and
necessity follows by substituting the unit pair.

This is a statement about the multiplier of the form. It is not the claim
`T^5=I`. The relation `phi^2=phi+1` gives `phi^5=5phi+3`, so
`phi^5-1=2-5j^2-5j^3` is nonzero by uniqueness of the integer coefficient
expression. Hence `T^5 e_2=(0,phi^5)` differs from `e_2`.
Fifth-step area preservation supplies neither a five-step return of every
state nor a physical clock identification.

## 3. The ramified residue and its exact information loss

Put `lambda=1-j`. The quotient can be computed directly from its
presentation:

\[
\mathcal O/(\lambda)
\cong\mathbb Z[t]/(\Phi_5(t),t-1)
\cong\mathbb Z/(\Phi_5(1))
=\mathbb Z/5\mathbb Z=\mathbb F_5.
\]

Thus the residue homomorphism is the well-defined surjective map

\[
\rho\left(\sum_{k=0}^3 a_kj^k\right)
=\sum_{k=0}^3a_k\pmod5,
\qquad \ker\rho=(1-j).
\]

Equivalently, polynomial evaluation at 1 is compatible with the relation
because `Phi_5(1)=5`. This is a quotient theorem, not a conclusion drawn
from checking finitely many products. It gives

\[
\rho(j)=1,\qquad \rho(J)=2,\qquad \rho(\phi)=-2=3.
\]

Let `rho_2:O^2 -> F5^2` act coordinatewise. Then

\[
\rho_2 T=A\rho_2,\qquad
A=\begin{pmatrix}2&0\\0&3\end{pmatrix},\qquad
A^{-1}=\begin{pmatrix}3&0\\0&2\end{pmatrix}.
\]

For every `u=(a,b),v=(c,d)` in F5^2, the residue alternating form obeys

\[
\omega(Au,Av)=6(ad-bc)=ad-bc=\omega(u,v).
\]

Here `det(A)=1` in F5. Reduction of the O-valued covariance is consistent
with this invariance precisely because `rho(j)=1`.

All five complex phase labels `1,j,j^2,j^3,j^4` have the same residue 1.
In particular reduction identifies the unequal areas 1 and j of the unit
pair before and after T. It erases that nontrivial complex phase. No map
back from this single residue value can invert those five distinct inputs.
The subsequent complex Weyl representation is an additional construction;
it is not a faithful transport of the element j through rho.

## 4. Literal Weyl products and all central factors

On the chosen complex vector space with basis `|k>`, define

\[
Z|k\rangle=j^k|k\rangle,\quad
X|k\rangle=|k+1\rangle,\quad
W(a,b)=Z^aX^b,\quad D|k\rangle=|3k\rangle.
\]

Their inverses are defined everywhere:
`Z^-1|k>=j^-k|k>`, `X^-1|k>=|k-1>`, and `D^-1|k>=|2k>`.
In particular all four are invertible; X and D are permutations of the
complete basis and Z has nonzero diagonal entries.

Directly on each basis vector,

\[
ZX|k\rangle=j^{k+1}|k+1\rangle
=jXZ|k\rangle,
\]

so `ZX=jXZ`, with this sign fixed by the stated composition order.
For all labels `u=(a,b)` and `v=(c,d)`, commuting the middle factors gives

\[
X^bZ^c=j^{-bc}Z^cX^b,
\qquad
W(a,b)W(c,d)=j^{-bc}W(a+c,b+d).
\tag{1}
\]

The factor in (1) must be retained. In this unsymmetrized convention,
`W(u)W(v)` is generally not `W(u+v)`. Reversing the factors gives
`W(c,d)W(a,b)=j^{-da}W(a+c,b+d)`, hence

\[
W(u)W(v)=j^{ad-bc}W(v)W(u)
=j^{\omega(u,v)}W(v)W(u).
\tag{2}
\]

The full inverse and commutator are therefore

\[
W(a,b)^{-1}=j^{-ab}W(-a,-b),\qquad
W(u)W(v)W(u)^{-1}W(v)^{-1}=j^{\omega(u,v)}I.
\tag{3}
\]

For an explicit central-extension convention, write
`G(s,a,b)=j^sW(a,b)`. Equations (1) and (3) give

\[
G(s,a,b)G(t,c,d)=G(s+t-bc,a+c,b+d),
\]
\[
G(s,a,b)^{-1}=G(-s-ab,-a,-b).
\]

These statements include every central factor, not only the phase of a
sample commutator. Equality as operators follows from equality on all five
basis vectors. Also all 25 labels give distinct W operators: equality
first forces their shifts b to agree; applying the common shift to the
input `k=1-b` then forces `j^a=j^c`, hence `a=c` in F5. With the shift
fixed, evaluation at `k=-b` also distinguishes the central scalar of G.

## 5. Exact covariance under D

Apply the three operators in their literal order to a general basis vector:

\[
DZ D^{-1}|k\rangle
=D(j^{2k}|2k\rangle)=j^{2k}|k\rangle=Z^2|k\rangle,
\]
\[
DX D^{-1}|k\rangle
=D|2k+1\rangle=|k+3\rangle=X^3|k\rangle.
\]

Conjugation is multiplicative and fixes complex scalars. Thus, without
reordering Z and X,

\[
DW(a,b)D^{-1}=Z^{2a}X^{3b}=W(2a,3b)=W(A(a,b)),
\]
\[
DG(s,a,b)D^{-1}=G(s,2a,3b).
\]

There is no omitted label-dependent central factor in this covariance.
Indeed the product factor after transforming two labels is
`j^(-(3b)(2c))=j^(-bc)`, the same cocycle as (1). Likewise the commutator
factor is unchanged because A preserves omega. This establishes the
covariance for all 25 labels and all 625 ordered pairs analytically.
The later independent enumeration must examine those entire finite sets;
the proof does not assert that such an execution has already occurred.

The permutation D has order 4, because multiplication by 3 cycles the
nonzero indices as `1 -> 3 -> 4 -> 2 -> 1` and fixes 0. This order must
not be confused with the order-five central phase or the five-step
O-valued area multiplier of T. D represents the specified residue action
on Weyl labels; no identification of D with a compiled native U is given.

## 6. Complete additive-character family

Let `mu_5={1,j,j^2,j^3,j^4}`. An additive character in the declared class
is a group homomorphism from `(F5,+)` to `(mu_5,multiplication)`.
It is determined by the image of 1, since the additive domain is cyclic.
Every possible image is `j^t` for exactly one `t in F5`, and it defines

\[
\chi_t(a)=j^{ta}.
\]

All five are characters: `chi_t(a+b)=chi_t(a)chi_t(b)` and the formula is
well defined modulo 5. For `t=0` the character is trivial. For each of
the four nonzero t, its kernel consists only of 0, since `ta=0` in F5
implies `a=0`. These four characters are faithful and pairwise distinct
already at 1. There are no other additive characters in this class.

For every t, and every ordered pair of residue vectors,

\[
\chi_t(\omega(Au,Av))=\chi_t(\omega(u,v)).
\]

One can realize the comparison without changing the residue action:
set `Z_t|k>=j^(tk)|k>` and `W_t(a,b)=Z_t^aX^b`. The same derivation gives
the product factor `chi_t(-bc)`, commutator factor `chi_t(ad-bc)`, and
`D W_t(u) D^-1=W_t(Au)`. The marked definitions in Sections 4 and 5
choose `t=1` explicitly. The existence of the other faithful characters
does not make that mathematical definition ambiguous or unmark j.
It does show that A-area invariance alone does not select a member of
this comparison family as a physical phase reading.

In particular `chi_t(rho(j))=j^t` uses a selected character on the additive
residue coordinate 1. It is not the inverse of rho on the five complex
powers of j, all of which rho sends to 1.

## 7. Complete rational diagonal costs and scalar intersection

Freeze exactly the class

\[
H=\operatorname{diag}(h_0,h_1,h_2,h_3,h_4),\qquad h_k\in\mathbb Q.
\]

On `|k>`, conjugation by D has the diagonal entry `h_(2k)`. Therefore

\[
DHD^{-1}=H\quad\Longleftrightarrow\quad
h_{2k}=h_k\quad\hbox{for every }k\in\mathbb F_5.
\]

Multiplication by 2 has precisely the orbits `{0}` and `{1,2,4,3}`.
Necessity forces equality on each orbit, and equality on those orbits
is sufficient. Thus the entire invariant rational diagonal class is

\[
\boxed{H=\operatorname{diag}(h_0,h_1,h_1,h_1,h_1),\qquad
(h_0,h_1)\in\mathbb Q^2.}
\tag{4}
\]

This is a classification for all rational entries, independent of any
bounded enumeration. Nonnegative examples with strictly positive gaps
above the zero-index state are

\[
H_1=\operatorname{diag}(0,1,1,1,1),\qquad
H_2=\operatorname{diag}(0,2,2,2,2).
\]

Their excitation gaps are exactly 1 and 2. More generally every positive
rational gap is realized by `diag(0,g,g,g,g)`. If strictly positive
entries are required, adding I to each example preserves its gap and
invariance. Neither a positive entry convention nor a zero-offset
convention singles out a nonzero gap.

Every diagonal H commutes with Z. The additional equation `HX=XH` is
equivalent, on every `|k>`, to `h_(k+1)=h_k`. Since addition by 1 is
transitive on F5, this holds exactly when all five entries coincide.
Hence within (4), and within the full declared rational diagonal class,

\[
\{H: DHD^{-1}=H,\ HX=XH,\ HZ=ZH\}=\mathbb Q I.
\]

It is specifically the stronger X-commutation condition that removes
the nonconstant diagonal costs. D-invariance alone leaves (4), rather
than forcing a scalar or a preferred positive gap. No classification of
arbitrary non-diagonal costs or of complete physical energy laws is
claimed here.

## 8. Scope of the implication and preserved negative controls

The same O, J, phi, T, residue map, area form and chosen Weyl operators
admit both H_1 and H_2. All preceding covariance and reciprocity equations
hold in both structures, while the declared excitation costs differ.
These are exact counterexamples to an implication that those equations
alone force a unique nonzero cost gap in the frozen rational diagonal
class. They are not physically realized counterexamples to every possible
additional energy law. A separately admitted physical condition could
select a narrower class; none is supplied by the identities proved here.

The result retains the following distinctions:

- T multiplies the complete O-valued area by j at one step. It does not
  preserve that form at one step, and fifth-step form preservation does
  not make T a finite-order state map.
- The residue preserves F5 area while identifying all five powers of j.
  It is not an observation of the original complex phase.
- The five-state complex module, its ordered Weyl convention, and the
  selected character are declared mathematical data. No physical
  preparation, phase observation, occurrence rule or apparatus follows.
- The diagonal-cost classification proves underdetermination only in its
  complete stated class. It does not establish a blanket impossibility
  theorem for other cost classes or physically admitted readers.
- Neither T, A nor D is identified with the original native U. Carrier
  comparison, a common native contact, autonomous realization, dimensional
  action, physical time, a photon, or any L1-to-L2/L3/L4/L5/L6 transport
  would require additional declared data and the applicable named gates.
- No SI scale, energy unit, Planck constant, hbar, electron-mass fit or
  dimensional action is derived. The equations are algebraic and
  dimensionless; this proof supplies no missing physical dictionary.

The universal proofs concern O^2, all residue vectors and labels, all
additive characters in the fixed class, and all rational diagonal costs.
A finite breaker is useful for detecting implementation errors in those
claims, especially the central signs. Its execution record, and comparison
with the author's subsequently opened files, remain separate evidence.

## 9. Public source boundary

The allowed target specification is
`probes/P-J-RAMIFIED-AREA-WEYL-1/PREREG.md` at source pin
`6b459a66d670656bd02a09c26da666bd16c077fb`, SHA-256
`d7f3900ede7eb09042ae808c6cac8443c2443d2ec10361f5e1feae10c98754ad`.

The public Canon at base
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d` supplies the registered
scope of J-PROJECTIONS, J-GOLDEN-BRIDGE, FORCE-WEYL-HOLONOMY and
KERNEL-WEDGE-COUPLING. Their distinct carrier and dictionary boundaries
are retained. In particular the kernel wedge theorem does not identify
the O^2 pair step with the native update, and the physical force reading
is not part of the finite Weyl commutator theorem.

The expansions, quotient calculation, complete operator laws, character
classification and rational cost proof above are given explicitly, so
their validity does not depend on unseen author proof text, executable
helpers, expected output, or a green author CI result. No original author
implementation is imported or reproduced by this document.
