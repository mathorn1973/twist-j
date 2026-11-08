# Proposed v107 contact and Gram sections

**NON-CANONICAL / L1 / proposed analytical text, pending independent review.**
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

This proposal changes no public claim, registry row or authority. Its working
session review is not independent theorem acceptance. The current public basis
is Public Canon v106 at `a193e389fb1ddb0bdc89165b015c95a17eb1e425`.

## Scope of the proposed fold

Section 1 is necessary for the narrow preparation-and-renewal fold: it states
the exact supplied law used by the four-slot minimum computation and the
residue invariant used by the renewal boundary. Sections 2 and 3 are optional
extensions. They require separate acceptance of the Gram and archive proofs;
they are not prerequisites of the sharp preparation minima.

The 26-slot preparation result and the seven-slot archive below have different
prepared families. This proposal supplies no common preparation, response,
record and renewal theorem joining them for varied inputs. Neither finite
return of the archive nor reversal of a preparation word proves auxiliary
restoration while retaining a separately exported output.

Exact sources:

- Contact: [PR #1833](https://github.com/mathorn1973/twist-j/pull/1833),
  `d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0`,
  `notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/PROOF.md` and its frozen
  `PREREG.md`, `verify.py`, `RUN.md`, `REPLAY-x86_64.md`, `EXPECTED.txt`.
  Scientific input pin: `898160aab70bc8908174df56ddca7afec39fa42f`.
- Gram and archive: [PR #1845](https://github.com/mathorn1973/twist-j/pull/1845),
  `80623637571ee0e1ef4785406f0b0a2e52f8ec75`,
  `notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/PROOF.md`, `PREREG.md`,
  `REFERENCES.md` and the two recorded finite audits.
  Scientific input pin: `2670e0ef4deaea22d41eef588ea24aec5e68cb3d`.

The trace account and earlier phase contacts are credited in the first source
to PR #1419. The binary norm descent, general Gram-fibre boundary and earlier
occupied-record constructions are credited in the second source. No priority
claim is part of this proposal.

## 1. Necessary: the supplied integral relative contact

### Definition and exact accounts

Let

\[
 O=\mathbb Z[j]=\mathbb Z[X]/(1+X+X^2+X^3+X^4),\qquad
 K=\mathbb Q(j),\qquad \bar j=j^{-1},\qquad \rho=j^2=J-1.
\]

Use the marked coefficient basis \((1,j,j^2,j^3)\). The full state carrier is
\(O^N\), with a specified finite number of labelled slots. Define

\[
 q(a)=\frac{\operatorname{Tr}_{K/\mathbb Q}(a\bar a)}2
      =\frac{5\sum_{k=0}^3a_k^2-(\sum_{k=0}^3a_k)^2}{2},\qquad
 E(z)=\sum_iq(z_i),\qquad h(z)=\sum_i z_i\bar z_i,\qquad
 S(z)=\sum_i z_i.
\]

The trace formula follows from
\(\operatorname{Tr}(j^r)=4\) for \(5\mid r\) and \(-1\) otherwise.
Its numerator is even. Cauchy's inequality gives
\(q(a)\ge\sum_k a_k^2/2\), so \(q\) is a nonnegative integer,
vanishes only at zero, and has finite bounded sublevel sets.

The carrier, labelled slots and these accounts are supplied model data.
In particular \(E\) is an arithmetic trace account; identifying it with
physical energy or an account of native \(U\) is not part of the statement.

Prescribe the pair equations

\[
 x'+y'=x+y,\qquad x'-y'=\rho(x-y).
\]

They have the unique field solution
\(x'=y+J(x-y)/2\), \(y'=x+y-x'\).
Since \(J^{-1}=-j-j^2\in O\), the solution is integral exactly when
\(x-y\in2O\). The admitted sublattice
\(\Gamma=\{(x,y):x-y\in2O\}\) has index \(16\) in \(O^2\):
the difference map onto \(O/2O\) is surjective and has kernel \(\Gamma\).
This index is not an occurrence probability.

Supply identity on the whole refused complement, defining the total contact

\[
 C(x,y)=
 \begin{cases}
 (s+\rho t,s-\rho t),&x-y\in2O,
       \quad s=(x+y)/2,\quad t=(x-y)/2,\\
 (x,y),&x-y\notin2O.
 \end{cases}
\]

All divisions here are exact. Identity refusal is an additional choice;
it is not derived from the requirement of reversibility.

### Proposed universal statement and proof

The total contact is a bijection. Its inverse replaces \(\rho\) by
\(\rho^{-1}\), and \(C^5=I\). It preserves \(S\), \(h\) and \(E\)
on every complete state, including occupied and refused states. Every
individual slot residue modulo \(\pi=1-j\) is unchanged.

Indeed, an admitted difference becomes \(\rho(x-y)\), which remains in
\(2O\); multiplication by the unit \(\rho\) preserves admission in both
directions. The refused complement is fixed. Thus inversion never confuses
the two branches. On the admitted branch

\[
 C^k(x,y)=(s+\rho^kt,s-\rho^kt),\qquad \rho^5=1,
\]

and

\[
 (s+\rho t)\overline{(s+\rho t)}+
 (s-\rho t)\overline{(s-\rho t)}
 =2s\bar s+2t\bar t=x\bar x+y\bar y.
\]

The pair sum is \(2s\). These identities prove the account claims before
and after taking the trace. Finally
\(x'-x=(\rho-1)t\) and \(y'-y=-(\rho-1)t\).
Because \(\rho-1=j^2-1\in(\pi)\), both residues are fixed.
Here \(O/(\pi)\simeq\mathbb F_5\), by setting \(j=1\) in \(\Phi_5\).
This quotient differs from coefficientwise reduction modulo \(5\).

Applying these contacts to specified pairs and allowing whole-slot
permutations gives conservative bijections on \(O^N\). The inverse of a
finite word reverses its order and inverts each letter. The histogram of
all \(N\) residues in \(O/(\pi)\) is invariant, since contacts fix the
individual residues and permutations merely reassign their positions.
This includes every data, auxiliary and archive slot in the declared carrier.

The supplied law is nonlinear on the full Cartesian lattice:
\(C(1,0)=(1,0)\), whereas
\(C(2,0)=(1+\rho,1-\rho)\ne(2,0)\).
Neither this law nor its slot order, graph or program is an implementation
of native \(U\) or contact walk \(W\). Conservation of the account permits
loss of a particular preparation capability; no energy dissipation follows.

**Falsifier at this scope:** an integral solution outside \(\Gamma\), a
nonintegral admitted output, a failure of either inverse composition, or a
failure of the displayed full-state account or residue identities.

## 2. Optional: full Gram admission and reversible continuation

Fix \(N\ge2\), and retain the entire unnormalized record

\[
 G(z)=zz^\dagger,\qquad
 \mathcal G_N=\{zz^\dagger:z\in O^N\}.
\]

The domain is this actual image, not an asserted characterization by arbitrary
positive integral Hermitian matrices. For slots \(i\ne j\), put

\[
 D_{ij}(G)=G_{ii}+G_{jj}-G_{ij}-G_{ji}.
\]

**Proposed universal statement.** On \(\mathcal G_N\), the record determines
admission of the complete contact, and supports a well-defined integral
bijective update and its inverse. The factor includes zero, refused states,
occupied states and every actual integral Gram fibre.

**Proof.** The polynomial \(\Phi_5\) has no root over \(\mathbb F_2\).
Its only possible factorization without a linear factor would be the square
of the unique monic irreducible quadratic \(X^2+X+1\); that square differs
from \(\Phi_5\). Hence \(O/2O\simeq\mathbb F_{16}\). Conjugation is
fourth-power Frobenius because both maps send \(j\) to \(j^4\).

Let \(F=K^{\bar{\phantom{x}}}\) and \(O_F=O\cap F\).
Direct conjugation in the marked basis gives
\(O_F=\mathbb Z[\varphi]\), \(\varphi=-j^2-j^3\),
\(\varphi^2-\varphi-1=0\). Its binary residue field is \(\mathbb F_4\).
The inclusion into \(O/2O\) is injective: if a fixed element equals
\(2b\) with \(b\in O\), then conjugation also fixes \(b\).
For any \(d\in O\), its reduced norm is therefore
\(a\bar a=a^5\), where \(a=d\bmod2O\). A field has no nonzero element
with fifth power zero. Consequently

\[
 d\in2O\quad\Longleftrightarrow\quad
 d\bar d\in2O_F\quad\Longleftrightarrow\quad d\bar d\in4O_F.
\]

The last equivalence is special to norm elements: \(d=2e\) implies
\(d\bar d=4e\bar e\), and divisibility by four implies divisibility by two.
Since \(D_{ij}(G(z))=(z_i-z_j)\overline{(z_i-z_j)}\), this is precisely
the required branch test. Equivalently, every coefficient of \(D_{ij}\)
in the marked basis must be even.

For \(e\in\{1,-1\}\), write

\[
 v=e_i-e_j,\qquad A_{ij}^{e}=I+(\rho^e-1)vv^T/2.
\]

Define \(\widehat C_{ij}^{e}(G)=A_{ij}^{e}G(A_{ij}^{e})^\dagger\)
when the Gram admission test passes and \(\widehat C_{ij}^{e}(G)=G\)
otherwise. Every representative of one Gram takes the same branch. On the
accepted branch its vector output is integral, so the resulting matrix is
an integral member of \(\mathcal G_N\), with all divisions exact. Thus

\[
 G(C_{ij}^{e}z)=\widehat C_{ij}^{e}(G(z))
\]

for every integral input. Applying the vector inverse proves both record
inverse compositions on the entire image. Slot permutations act by
simultaneous row and column permutation. These identities compose for every
fixed contact/permutation word and for every supplied cyclic program when
its clock is included in the record.

No unit-only fibre assumption is needed. If
\(zz^\dagger=ww^\dagger\ne0\), comparison of one nonzero diagonal and
its column gives \(w=\lambda z\),
\(\lambda\in K^\times\), \(\lambda\bar\lambda=1\).
The integral fibre consists of exactly those multiples for which
\(\lambda z\in O^N\). The same norm admission test applies even when
\(\lambda\notin O\); the admitted matrix commutes with \(\lambda\).
The zero Gram has only the zero representative.

The matrix trace reads \(h\) and its field half-trace reads \(E\).
The literal scalar sum \(S\) is conserved on vectors but is not generally
recoverable from \(G\). If supplied additionally and nonzero, it recovers
\(z_i=(\sum_jG_{ij})/\bar S\). This is not a minimality claim.

The following exact controls delimit the record:

| Discarded information or changed interface | Witness under the same contact |
| --- | --- |
| Full norm replaced by half-trace account parity \(q\bmod2\) | \(d=1\) has even \(q(d)=2\), but \((1,0)\) is refused. |
| Overall scale discarded | \((1,0)\) and \((2,0)\) have equal normalized Grams; their output receiver accounts are \(0\) and \(5\). |
| Off-diagonal entries discarded | \((2,2\rho)\) and \((2,2\rho^{-1})\) have equal diagonal Grams; their ordered output accounts are \((13,3)\) and \((3,13)\). |
| Fresh absolute-phase reference appended | The one-slot Grams of \(2\) and \(2\rho\) agree; appending the same reference \(2\) and contacting gives receiver accounts \(8\) and \(13\). |
| Arbitrary integral gate substituted | \(\Phi(x,y)=(y,\bar x)\) sends equal Grams of \((1,1)\) and \((j,j)\) to off-diagonal entries \(1\) and \(j^2\). |

The theorem concerns the permitted alphabet on the fixed complete carrier.
It supplies no physical acquisition of its global Gram, Born occurrence law,
or unique decoder. A different loading or reference-extension operation needs
its own complete contract.

**Falsifier at this scope:** a disagreement between full-norm and vector
admission, a nonintegral record continuation on \(\mathcal G_N\), a failed
intertwining or inverse identity, or two integral representatives of the same
Gram whose permitted updates have different Grams.

## 3. Optional: one occupied receiver used twice in a finite window

Take the ordered slots \((S_1,S_2,L_1,L_2,R,A_0,A_1)\) and the full carrier
\(\mathbb Z/14\mathbb Z\times O^7\). For a supplied program \(g_c\),
set \(F(c,z)=(c+1\bmod14,g_cz)\). Let \(T_{X,Y}\) swap whole slots and
\(B_k=C_{S_k,R}\). Choose

| Clock before the step | Gate |
| --- | --- |
| 0 | \(T_{R,A_0}\) |
| 1 | \(T_{R,L_1}\) |
| 2 | \(B_1\) |
| 3 | \(T_{R,A_1}\) |
| 4 | \(T_{R,L_2}\) |
| 5 | \(B_2\) |
| 6, 7 | Identity |
| 8 | \(B_2^{-1}\) |
| 9 | \(T_{R,L_2}\) |
| 10 | \(T_{R,A_1}\) |
| 11 | \(B_1^{-1}\) |
| 12 | \(T_{R,L_1}\) |
| 13 | \(T_{R,A_0}\) |

For arbitrary independent \(u_1,u_2,v_1,v_2,m\in O\), prepare once at
clock zero

\[
 z^{(0)}=(2u_1,2u_2,2v_1,2v_2,m,0,0).
\]

Both source/reference pairs and both blank archive slots are included at this
origin. Put

\[
 a_k=(1+\rho)u_k+(1-\rho)v_k,\qquad
 b_k=(1-\rho)u_k+(1+\rho)v_k.
\]

**Proposed conditional statement.** At boundaries \(6,7,8\), the full state
is exactly \((a_1,a_2,0,0,b_2,m,b_1)\). The first output appears in the
continuing receiver \(R\) at boundary 3 and in \(A_1\) from boundary 4
through 8. The old receiver value \(m\) remains literally in \(A_0\) from
boundary 1 through the reading window. Every complete state, with any initial
clock and arbitrary dirty archives, returns after fourteen steps.

**Proof.** The initial swap exports \(m\) into the first blank. The next swap
presents \(2v_1\) to the receiver; its contact with \(2u_1\) is admitted and
produces \((a_1,b_1)\). A swap exports \(b_1\) into the second blank.
The next swap presents \(2v_2\); the second admitted contact produces
\((a_2,b_2)\). This is the displayed state at boundary 6; two identities
retain it at 7 and 8. The remaining gates reverse the first six exactly,
on the full domain by Section 1. Thus the fourteen-gate product is identity.
Every cyclic shift of a product of bijections with product identity also
has product identity, proving the assertion from every clock.

All steps preserve the complete \(S,h,E\), with

\[
 E=4\bigl(q(u_1)+q(u_2)+q(v_1)+q(v_2)\bigr)+q(m).
\]

The record \((c,G)\) has the exact continuation of Section 2. A reader
returns NOT_IN_WINDOW outside \(c\in\{6,7,8\}\); inside that window it
returns VALID and the principal submatrix in the ordered slots
\((A_0,A_1,R)\). On the prepared family this is exactly

\[
 (m,b_1,b_2)^T(\bar m,\bar b_1,\bar b_2).
\]

Zero is still VALID in the window. The reader reports norms and mutual
relative records, not absolute scalar phases. On dirty states the same
complete update and reader definition remain valid, but the clock tag does
not certify preparation or a new writing event.

The star graph, clock, program, references, blanks and reading window are
supplied resources. The later inverse removes the new archive as it restores
the preparation. This finite-window construction supplies neither permanent
storage nor fresh independent input on subsequent cycles. It closes no
physical apparatus or native-contact obligation.

**Falsifier at this scope:** an admitted prepared input failing the stated
endpoint or old-memory identity, any complete state or clock failing
\(F^{14}=I\), or disagreement between the record-only reader and the actual
ordered Gram submatrix.

## Review and evidence disposition

The universal arguments above are proposed analytical statements. Neither
their inclusion here nor the working session's static review accepts them
independently. The source contact audit records matching arm64 and x86_64
stdout. The Gram/archive source records two separately structured programs
on x86_64, with matching frozen pair and program certificates; its ordinary
repository CI did not execute those notes programs. Any later replay must be
reported separately at its exact pin and actual architecture.

For the narrow v107 fold, obtain independent acceptance of Section 1 and of
the preparation/renewal evidence before assigning public statuses. Include
Sections 2 and 3 only if their separately identified proof and evidence gates
are also satisfied. Otherwise preserve them as this optional NON-CANONICAL
proposal. In either case, the common varied-input apparatus remains an open
obligation with its own preparation, reading, retention and renewal contract.
