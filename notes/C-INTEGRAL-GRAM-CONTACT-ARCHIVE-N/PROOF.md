# Integral Gram contact and occupied archive: analytical proof

Candidate: C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N.
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Status: NON-CANONICAL / L1 / conditional analytical candidate-T.
Reservation: #1844. Public basis: a193e389fb1ddb0bdc89165b015c95a17eb1e425,
Public Canon v106.

This text proves the mathematical claims A-D of [PREREG.md](PREREG.md)
on exactly their declared carriers. It records an authored analytical
argument, not independent theorem acceptance or an executed audit. The
analytical reviewer saw the proposed formulas and preregistration but did
not read the builder's verifier. Any later independent implementation,
finite execution and architecture replay have separate records.

The contact itself is supplied by #1833 at the pinned source named in
[REFERENCES.md](REFERENCES.md). The inherited binary norm descent and
quadratic-reading results are credited there. The proposed narrow delta is
that this contact's complete arithmetic branch descends to its full,
unnormalized Gram record, with exact forward and backward continuation and
one explicit two-use archive program. The carrier, gate alphabet, graph,
program, preparation and reading window remain additional premises.

## 1. Rings, involution and the exact account

Let

\[
 \mathcal O=\mathbb Z[j]
   =\mathbb Z[X]/(1+X+X^2+X^3+X^4),\qquad K=\mathbb Q(j),
 \qquad \bar j=j^{-1},\qquad \rho=j^2.
\]

The ordered integral coefficient basis is \(1,j,j^2,j^3\). Equality and
divisibility in this text are literal equalities and divisibilities in
that ring. Put \(F=K^{\bar{\phantom{x}}}\) and
\(\mathcal O_F=\mathcal O\cap F\).
The identities \(\rho^5=1\) and \(\rho\bar\rho=1\) hold exactly.
Also \(J=1+\rho\), \(J^{-1}=-j-j^2\), and \((J-1)^3=j\).

For \(a=\sum_{k=0}^3a_kj^k\), the field trace of \(j^r\) is \(4\) when
\(5\mid r\) and \(-1\) otherwise. Expanding \(a\bar a\) therefore gives

\[
 \operatorname{Tr}_{K/\mathbb Q}(a\bar a)
 =4\sum_k a_k^2-2\sum_{k<l}a_ka_l
 =5\sum_k a_k^2-\left(\sum_k a_k\right)^2.
\]

Thus the account used throughout is precisely

\[
 \boxed{\quad
 q(a)=\frac{\operatorname{Tr}_{K/\mathbb Q}(a\bar a)}2
     =\frac{5\sum_k a_k^2-(\sum_k a_k)^2}{2}.
 \quad}                                                     \tag{1}
\]

It is not the unhalved field trace. The numerator is even because
\(x^2\equiv x\pmod2\). By
\((\sum_k a_k)^2\le4\sum_k a_k^2\),

\[
 q(a)\ge\frac12\sum_k a_k^2.                                  \tag{2}
\]

Consequently \(q\) is a nonnegative integer, vanishes only at zero,
and has finite bounded sublevel sets on \(\mathcal O\). For an integer
\(r\), \(q(ra)=r^2q(a)\). For a unit phase \(u\) with \(u\bar u=1\),
\(q(ua)=q(a)\).

On the complete Cartesian carrier \(\mathcal O^N\), define

\[
 h(z)=\sum_{k=1}^N z_k\bar z_k\in\mathcal O_F,\qquad
 E(z)=\sum_{k=1}^Nq(z_k)
     =\frac{\operatorname{Tr}_{K/\mathbb Q}h(z)}2,\qquad
 S(z)=\sum_{k=1}^N z_k\in\mathcal O.                           \tag{3}
\]

These are declared arithmetic accounts. In particular \(E\) is not
identified with a physical Hamiltonian or with an account of native \(U\).

Fix any finite \(N\ge2\). The record carrier is exactly

\[
 \mathcal G_N=\{zz^\dagger:z\in\mathcal O^N\},
 \qquad G(z)=zz^\dagger.                                    \tag{4}
\]

No characterization of this image by arbitrary integral positive
hermitian matrices is assumed. Every matrix statement below is on this
actual image unless a larger domain is explicitly stated.

## 2. Claim A: the complete admission branch is a Gram observable

### 2.1 The inherited residue fields, with a direct proof

Modulo \(2\), \(\Phi_5(X)=1+X+X^2+X^3+X^4\) has no root in
\(\mathbb F_2\). If it were reducible without a linear factor, it would
be the product of two irreducible quadratics. The only monic
irreducible quadratic over \(\mathbb F_2\) is \(X^2+X+1\), whose square
is \(X^4+X^2+1\), different from \(\Phi_5\). Hence

\[
 \mathcal O/2\mathcal O\simeq\mathbb F_{16}.                    \tag{5}
\]

On this field conjugation is fourth-power Frobenius. Both maps fix
\(\mathbb F_2\) and send the generator \(j\) to \(j^4=j^{-1}\).
Therefore, for the residue \(a\) of any \(d\in\mathcal O\),

\[
 \overline a=a^4,\qquad a\overline a=a^5.                     \tag{6}
\]

For completeness the fixed integral ring has the expected binary
reduction. Conjugation of the coefficient vector gives

\[
 \overline{a_0+a_1j+a_2j^2+a_3j^3}
  =(a_0-a_1)-a_1j+(a_3-a_1)j^2+(a_2-a_1)j^3.
\]

An integral element is fixed exactly when \(a_1=0\) and \(a_2=a_3\).
With \(\varphi=-j^2-j^3\), this gives
\(\mathcal O_F=\mathbb Z[\varphi]\), and
\(\varphi^2-\varphi-1=0\). Its reduction is the irreducible polynomial
\(X^2+X+1\), so

\[
 \mathcal O_F/2\mathcal O_F\simeq\mathbb F_4.                  \tag{7}
\]

The inclusion of this residue field into (5) is injective. Indeed,
if \(b\in\mathcal O_F\) and \(b=2c\) with \(c\in\mathcal O\), then
\(\bar c=c\), so \(c\in\mathcal O_F\). Its image is the fixed field
of fourth-power Frobenius. Equation (6) is therefore precisely the
relative norm \(\mathbb F_{16}\to\mathbb F_4\).

These field facts and the associated trace reduction are inherited
from J-BINARY-NORM-DESCENT. They are restated to make the application
to the contact self-contained.

### 2.2 Norm admission, including the factor four

For any \(d\in\mathcal O\), put \(D=d\bar d\in\mathcal O_F\).
The field (5) has no nonzero nilpotents. Equations (5)-(6) give

\[
 D\equiv0\pmod{2\mathcal O_F}
 \quad\Longleftrightarrow\quad a^5=0
 \quad\Longleftrightarrow\quad a=0
 \quad\Longleftrightarrow\quad d\in2\mathcal O.               \tag{8}
\]

If \(d=2e\), then \(D=4e\bar e\in4\mathcal O_F\). Conversely,
membership of \(D\) in \(4\mathcal O_F\) implies its zero reduction
modulo \(2\), and (8) applies. Thus, on the full integral domain,

\[
 \boxed{
 d\in2\mathcal O
 \iff d\bar d\in2\mathcal O_F
 \iff d\bar d\in4\mathcal O_F.}                              \tag{9}
\]

The equivalence of divisibility by two and four in (9) is special
to these norm elements. It is not asserted for arbitrary elements
of \(\mathcal O_F\).

For distinct slots \(i,j\), let \(v=e_i-e_j\) and \(d=z_i-z_j\).
For every actual record \(G=zz^\dagger\),

\[
 D_{ij}(G)=v^TGv
 =G_{ii}+G_{jj}-G_{ij}-G_{ji}
 =(z_i-z_j)(\bar z_i-\bar z_j)=d\bar d.                     \tag{10}
\]

For a fixed integral element \(D\in\mathcal O_F\), membership in
\(2\mathcal O_F\) is equivalent to every coefficient in the ordered
basis of \(\mathcal O\) being even: the forward implication is
immediate, and the reverse implication follows by dividing by two
and using conjugation as above. This proves exactly the
coefficientwise admission test in the preregistration.

In particular this test requires the full norm \(D_{ij}(G)\), not
its scalar trace.

### 2.3 Why the scalar trace loses the branch

Since \([K:F]=2\) and \(D\in F\), equation (1) gives

\[
 q(d)=\operatorname{Tr}_{F/\mathbb Q}(D).
\]

For \(D=b_0+b_1\varphi\), this is \(2b_0+b_1\). Reducing modulo two
is exactly the finite-field trace \(\operatorname{Tr}_{\mathbb F_4/
\mathbb F_2}(D\bmod2)\). Hence

\[
 q(d)\bmod2
 =\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}
     \bigl(N_{\mathbb F_{16}/\mathbb F_4}(a)\bigr).            \tag{11}
\]

The trace kernel in \(\mathbb F_4\) is \(\{0,1\}\). On nonzero
elements the norm \(a\mapsto a^5\) from the cyclic multiplicative
group of order \(15\) onto the group of order \(3\) has five
preimages of \(1\). Thus (11) has exactly five nonzero zeros,
although the full norm has none. This describes the reduced
half-trace account \(q\bmod2\). The unhalved trace
\(\operatorname{Tr}_{K/\mathbb Q}(d\bar d)\) is always even and is
not the scalar in this assertion.

This completes Claim A and explains its required negative control.

## 3. Claim B: an integral invertible Gram factor

For \(e\in\{+1,-1\}\), put \(u=\rho^e\), and set

\[
 P^-_{ij}=\frac12vv^T,\qquad
 A_{ij}^e=I+(u-1)P^-_{ij}.                                  \tag{12}
\]

The matrix \(P^-_{ij}\) is hermitian and idempotent because
\(v^Tv=2\). On the two marked slots, (12) is

\[
 \frac12
 \begin{pmatrix}
  1+u&1-u\\
  1-u&1+u
 \end{pmatrix}.                                             \tag{13}
\]

The total supplied contact is

\[
 C_{ij}^e(z)=
 \begin{cases}
  A_{ij}^e z,&z_i-z_j\in2\mathcal O,\\
  z,&z_i-z_j\notin2\mathcal O.
 \end{cases}                                               \tag{14}
\]

This is exactly the preregistered completion, including identity
on the entire refused complement. On the admitted branch
\(s=(z_i+z_j)/2\) and \(t=(z_i-z_j)/2\) both belong to
\(\mathcal O\): if \(z_i-z_j\) is even, then
\(z_i+z_j=2z_j+(z_i-z_j)\) is even. The updated pair
\((s+ut,s-ut)\) is therefore integral.

### 3.1 Inverse, fifth power and invariants on all states

The admitted difference becomes

\[
 d'=u d.                                                    \tag{15}
\]

Since \(u\) is a unit, it preserves membership in \(2\mathcal O\).
The refused complement is fixed. Applying the same rule with
exponent \(-e\) reverses every admitted state and fixes every
refused state. Thus \(C_{ij}^e\) is a bijection of the whole
\(\mathcal O^N\), with inverse \(C_{ij}^{-e}\).

On an admitted pair its \(k\)-th iterate is
\((s+u^kt,s-u^kt)\); the complement remains fixed. Since \(u^5=1\),

\[
 (C_{ij}^e)^5=I                                             \tag{16}
\]

on all states. No empty-register assumption is used.

The pair sum is \(2s\) before and after the contact. At the level
of the complete norm in \(\mathcal O_F\),

\[
 \begin{aligned}
 (s+ut)\overline{(s+ut)}+(s-ut)\overline{(s-ut)}
  &=2s\bar s+2u\bar u\,t\bar t\\
  &=2s\bar s+2t\bar t .
 \end{aligned}                                             \tag{17}
\]

This is the original pair norm. Equations (3), (14) and (17)
prove preservation of \(h,E,S\) for every complete state,
including occupied inputs and refused contacts.

Equivalently \((A_{ij}^e)^\dagger A_{ij}^e=I\), since the
eigenvalue on \(P^-_{ij}\) is \(u\) and the complementary
eigenvalue is \(1\). This matrix identity does not assert that
\(A_{ij}^e\) maps every integral vector to an integral vector;
the branch (14) is essential.

### 3.2 The record map and exact intertwining

Define, on exactly \(\mathcal G_N\),

\[
 \widehat C_{ij}^e(G)=
 \begin{cases}
  A_{ij}^eG(A_{ij}^e)^\dagger,
       &D_{ij}(G)\in2\mathcal O_F,\\
  G,&D_{ij}(G)\notin2\mathcal O_F.
 \end{cases}                                               \tag{18}
\]

Claim A makes the branch identical for every representative
\(z\) of a given \(G\). On its admitted branch (14) is integral;
hence (18) belongs to \(\mathcal G_N\) and has integral entries.
In particular every division by two or four in (18) is exact on
its declared domain. No rounding, choice of representative,
discarded output or implicit residue is required.

Direct substitution now proves

\[
 \boxed{
 G(C_{ij}^e z)=\widehat C_{ij}^e(G(z))
 \quad\text{for every }z\in\mathcal O^N.}                     \tag{19}
\]

The inverse contact and (19) give
\(\widehat C_{ij}^{-e}\widehat C_{ij}^e=I\) and the reverse
composition on the entire \(\mathcal G_N\).
Also \((\widehat C_{ij}^e)^5=I\). Thus the record operation is
both well-defined and invertible, not merely a forward
comparison on initialized states.

The full norm \(h=\operatorname{tr}G\) and account
\(E=\operatorname{Tr}_{K/\mathbb Q}(\operatorname{tr}G)/2\)
are read from \(G\) and are preserved. The literal scalar \(S\)
is preserved on vectors but need not be readable from \(G\);
its optional addition is treated in Section 5.

## 4. Complete integral Gram fibres, including nonunit ratios

The preceding construction proves descent without classifying
fibres. The following independent fibre argument rules out
a hidden primitive-vector or unit-only restriction.

If \(z,w\in K^N\) and \(zz^\dagger=ww^\dagger\ne0\), choose \(k\)
with \(z_k\ne0\). The corresponding diagonal entry makes
\(w_k\ne0\). Put \(\lambda=w_k/z_k\). The diagonal equality gives

\[
 \lambda\bar\lambda=1.
\]

For each \(i\), equality of the \(ik\) entries gives

\[
 w_i\bar w_k=z_i\bar z_k,
 \qquad w_i=z_i/\bar\lambda=\lambda z_i.                     \tag{20}
\]

The converse follows by multiplication. The zero Gram has only
the zero vector as its representative. Thus the full integral
fibre of a nonzero vector is exactly

\[
 \{\lambda z:\lambda\in K^\times,\quad
      \lambda\bar\lambda=1,\ \lambda z\in\mathcal O^N\}.       \tag{21}
\]

There is no requirement that \(\lambda\in\mathcal O\), that it
be an integral unit, or that the common content of the
coordinates be fixed. The wider full-lattice fibres already
occur in QPAIR-HERM-INTEGER-NONDESCENT.

An explicit nonintegral ratio is included in the frozen audit.
Let \(a=2+j\) and \(\bar a=2+j^{-1}\). The homomorphism

\[
 \pi:\mathcal O\longrightarrow\mathbb F_{11},
 \qquad j\longmapsto-2
\]

is well-defined because \(\Phi_5(-2)=11\). It satisfies
\(\pi(a)=0\) and
\(\pi(\bar a)=2+(-2)^{-1}=2+5=7\ne0\).
Therefore \(a\) does not divide \(\bar a\) in \(\mathcal O\).
The ratio \(\lambda=\bar a/a\) is nonintegral and satisfies
\(\lambda\bar\lambda=1\). For every integral vector \(w\),

\[
 (aw)(aw)^\dagger=(\bar a w)(\bar a w)^\dagger.               \tag{22}
\]

These are valid full-lattice fibre pairs.

For any pair of integral representatives related by (21),
equation (10) gives the same admission value, because

\[
 (\lambda d)\overline{(\lambda d)}=d\bar d.
\]

Hence both representatives take the same branch. The admitted
linear matrix \(A_{ij}^e\) commutes with the scalar \(\lambda\);
the refused branch is identity. Thus

\[
 C_{ij}^e(\lambda z)=\lambda C_{ij}^e(z)                      \tag{23}
\]

whenever both inputs are integral and \(\lambda\bar\lambda=1\).
No integrality of \(\lambda\) has been assumed in this argument.
The same statement holds for coordinate permutations. It
establishes complete fibre preservation and, in particular,
all prescribed paired continuations of (22).

A contact can change a representative while leaving its Gram
unchanged. For example, on a two-slot zero-sum pair
\((x,-x)\), the admitted contact multiplies the entire pair
by \(\rho\). This is an intended identification in (21), not
lost information needed by another allowed contact on the
same complete carrier. It becomes relevant if a new
absolute-phase reference is supplied later, as Section 7.5
shows.

## 5. Claim C: whole programs and the optional sum reader

A coordinate permutation \(P\) acts exactly by

\[
 G(Pz)=PG(z)P^\dagger.                                      \tag{24}
\]

Every elementary contact and permutation has an exact inverse,
preserves the same complete accounts, and satisfies (19) or
(24). Induction proves forward intertwining for every fixed
finite word of these operations. Reversing the word and
inverting its letters proves backward intertwining. This
is an all-input result, with no ready-state restriction.

For a supplied program of period \(L\) with gates \(g_c\),
define the complete state and update by

\[
 (c,z)\in\mathbb Z/L\mathbb Z\times\mathcal O^N,\qquad
 F(c,z)=(c+1,g_cz).
\]

Then

\[
 R(c,z)=(c,G(z)),\qquad
 \widehat F(c,G)=(c+1,\widehat g_cG)                          \tag{25}
\]

satisfy \(RF=\widehat FR\) exactly. The inverses are

\[
 F^{-1}(c,z)=(c-1,g_{c-1}^{-1}z),\qquad
 \widehat F^{-1}(c,G)=(c-1,\widehat g_{c-1}^{-1}G).             \tag{26}
\]

All clock indices in these formulas are modulo \(L\). The
program is determined by the supplied clock, not by a hidden
choice of Gram representative.

The literal conserved sum \(S\) may be included as additional
data:

\[
 R_+(c,z)=(c,G(z),S(z)),\qquad S'=S.                          \tag{27}
\]

At \(S\ne0\), it restores the complete vector because

\[
 \sum_jG_{ij}=z_i\bar S,\qquad
 z_i=\frac{\sum_jG_{ij}}{\bar S}.                            \tag{28}
\]

The division in (28) is a field reconstruction on the stated
consistent image; its result is the original integral
coordinate. At \(S=0\), injectivity need not hold. The distinct
two-slot vectors \((1,-1)\) and \((j,-j)\) have the same Gram
and the same zero sum. Trailing zeros embed this example for
any \(N\ge2\).

Neither (25) nor (27) asserts minimality, a finite modulus
encoding, or physical acquisition of the full Gram. The
stronger record (27) is almost a complete vector encoding
on its \(S\ne0\) part, rather than an automatically economical
physical description.

## 6. Claim D: a seven-slot two-use apparatus

### 6.1 Complete law on every state

Use the ordered slots

\[
 (S_1,S_2,L_1,L_2,R,A_0,A_1)
\]

and the full state space \(\mathbb Z/14\mathbb Z\times\mathcal O^7\).
Write \(T_{X,Y}\) for a whole-slot swap, and let
\(B_1=C_{S_1,R}^{+1}\), \(B_2=C_{S_2,R}^{+1}\).
The supplied program is:

| Clock before step | Gate |
| --- | --- |
| 0 | \(T_{R,A_0}\) |
| 1 | \(T_{R,L_1}\) |
| 2 | \(B_1\) |
| 3 | \(T_{R,A_1}\) |
| 4 | \(T_{R,L_2}\) |
| 5 | \(B_2\) |
| 6 | identity |
| 7 | identity |
| 8 | \(B_2^{-1}\) |
| 9 | \(T_{R,L_2}\) |
| 10 | \(T_{R,A_1}\) |
| 11 | \(B_1^{-1}\) |
| 12 | \(T_{R,L_1}\) |
| 13 | \(T_{R,A_0}\) |

Every nontrivial data gate uses one edge of the supplied
seven-vertex star with centre \(R\). This is locality of
the declared data operations on that graph. It is not a
construction of a local physical clock, a homogeneous
lattice, or three-dimensional space.

Let the first-six-step word be

\[
 W=B_2T_{R,L_2}T_{R,A_1}B_1T_{R,L_1}T_{R,A_0},
\]

with rightmost gate performed first. The last six steps
are exactly \(W^{-1}\), following two identities.
Consequently the complete fourteen-step product from
clock zero is \(W^{-1}W=I\) on all of \(\mathcal O^7\).
This uses the full inverses of the contacts, including
their refused branches, not an inverse restricted to
a prepared image.

The same conclusion holds from every clock. Let
\(P_c=g_{c-1}\cdots g_0\) and \(P_0=I\). Since
\(g_{13}\cdots g_0=I\),

\[
 g_{13}\cdots g_c=P_c^{-1}.
\]

The fourteen-step data word starting at clock \(c\) is
\(P_c(g_{13}\cdots g_c)=I\). The clock also returns.
Therefore

\[
 \boxed{F^{14}=I
 \quad\text{on }\mathbb Z/14\mathbb Z\times\mathcal O^7.}       \tag{29}
\]

This covers dirty archives, arbitrary occupied receivers,
all refused contacts, zero states, and every clock.
The Gram program inherits the same return identity.
Each step preserves \(h,E,S\) by Claims B-C.

### 6.2 Prepared family and its exact endpoints

Prepare at the common origin \(c=0\)

\[
 z^{(0)}=(2u_1,2u_2,2v_1,2v_2,m,0,0),
 \qquad u_1,u_2,v_1,v_2,m\in\mathcal O,                      \tag{30}
\]

with all five entries arbitrary and independent.
Define

\[
 a_k=(1+\rho)u_k+(1-\rho)v_k,\qquad
 b_k=(1-\rho)u_k+(1+\rho)v_k,\quad k=1,2.                    \tag{31}
\]

The forward contact inputs are respectively
\((2u_1,2v_1)\) and \((2u_2,2v_2)\), so they are always
admitted. Direct application of the six gates gives:

| Boundary \(n\) | Data state in the fixed slot order |
| --- | --- |
| 0 | \((2u_1,2u_2,2v_1,2v_2,m,0,0)\) |
| 1 | \((2u_1,2u_2,2v_1,2v_2,0,m,0)\) |
| 2 | \((2u_1,2u_2,0,2v_2,2v_1,m,0)\) |
| 3 | \((a_1,2u_2,0,2v_2,b_1,m,0)\) |
| 4 | \((a_1,2u_2,0,2v_2,0,m,b_1)\) |
| 5 | \((a_1,2u_2,0,0,2v_2,m,b_1)\) |
| 6 | \((a_1,a_2,0,0,b_2,m,b_1)\) |
| 7 | \((a_1,a_2,0,0,b_2,m,b_1)\) |
| 8 | \((a_1,a_2,0,0,b_2,m,b_1)\) |
| 9 | \((a_1,2u_2,0,0,2v_2,m,b_1)\) |
| 10 | \((a_1,2u_2,0,2v_2,0,m,b_1)\) |
| 11 | \((a_1,2u_2,0,2v_2,b_1,m,0)\) |
| 12 | \((2u_1,2u_2,0,2v_2,2v_1,m,0)\) |
| 13 | \((2u_1,2u_2,2v_1,2v_2,0,m,0)\) |
| 14 | \((2u_1,2u_2,2v_1,2v_2,m,0,0)\) |

For the two backward contacts, admission follows either
from the full inverse theorem or from
\(a_k-b_k=2\rho(u_k-v_k)\).
The table therefore holds for every preparation (30),
including every zero value, without a generic-nonzero
qualification.

The first new output \(b_1\) is in \(R\) at boundary \(3\).
It moves to \(A_1\) at boundary \(4\) and stays there through
boundary \(8\). The previous receiver value \(m\) moves to
\(A_0\) at boundary \(1\) and remains literally unchanged
through all stated reading boundaries. The second output
\(b_2\) is in the same continuing slot \(R\) at boundaries
\(6,7,8\).

No value is erased or replaced by a freshly external value.
All swaps are on existing slots. Both source/reference
pairs were present in (30), and both archive blanks were
supplied at that same origin. The complete inverse recovers
all original data.

By (1)-(3) and \(q(2u)=4q(u)\), the exact conserved account is

\[
 E=4\bigl[q(u_1)+q(u_2)+q(v_1)+q(v_2)\bigr]+q(m).             \tag{32}
\]

The complete conserved sum is
\(2(u_1+u_2+v_1+v_2)+m\), also evident from
\(a_k+b_k=2(u_k+v_k)\).
The full \(h\) in (3), not only its trace, is conserved.

### 6.3 The record-only finite-window reader

Define a reader on \((c,G)\) alone. If
\(c\notin\{6,7,8\}\), it returns NOT_IN_WINDOW.
If \(c\in\{6,7,8\}\), it returns VALID together with the
principal submatrix whose ordered indices are
\((A_0,A_1,R)\).

For (30), at these boundaries the returned matrix is exactly

\[
 \begin{pmatrix}m\\b_1\\b_2\end{pmatrix}
 \begin{pmatrix}\bar m&\bar b_1&\bar b_2\end{pmatrix}.          \tag{33}
\]

This proof uses only the actual state table and the
definition of the Gram; the reader itself consumes no
initial source data or hidden representative. It reports
retained norms and mutual relative records, not the
absolute scalar phases \(m,b_1,b_2\).

The VALID tag depends on the supplied clock window,
not on a nonzero numerical value. A zero matrix in
(33) remains VALID. In particular the completely zero
preparation supplies an explicit valid zero record at
all three boundaries. The rule does not silently identify
stored zero with absence.

For dirty states outside (30), the complete update, its
Gram factor, its inverse and (29) still hold. The reader
has the same phase-dependent definition, but the
initialized endpoint formula and blank interpretation
are not asserted there.

The archive is retained for the stated finite window.
Equation (29) explicitly reverses it later. This is
neither permanent storage nor repeated loading of fresh
independent messages. It also is not a rule selecting
one physically occurring outcome.

## 7. Exact retained negative controls

The following exact calculations are analytical witnesses
fixed before execution. They delimit this theorem rather
than enlarging its gate alphabet.

For a nontrivial fifth root \(u\), the trace identities
in Section 1 immediately give

\[
 q(1)=2,\qquad q(2)=8,\qquad
 q(1+u)=3,\qquad q(1-u)=5.                                  \tag{34}
\]

### 7.1 Binary-trace loss

For \(d=1\), the scalar account \(q(d)=2\) is even, but
\(d\notin2\mathcal O\). The pair \((1,0)\) is therefore
refused and fixed. Its full norm is \(D=1\), which is
not in \(2\mathcal O_F\). Replacing (9) by evenness of
\(q(d)\) would admit this pair incorrectly.

### 7.2 Normalization loss

The pairs \((1,0)\) and \((2,0)\) have Grams in ratio
\(1:4\), so their matrices normalized by the matrix trace
are equal. The first is refused, with receiver account
zero. The second is admitted and gives

\[
 C(2,0)=(1+\rho,1-\rho),
 \qquad q(1-\rho)=5.                                       \tag{35}
\]

Their future normalized Grams also differ: the first
receiver diagonal stays zero, whereas the second receiver
diagonal is \((1-\rho)(1-\bar\rho)\ne0\).
Thus even normalized future Gram continuation fails for
this scale-free input identification. This is a scoped
obstruction for the same total contact, not an impossibility
claim about all normalized theories.

### 7.3 Phase-sensitive transfer at equal diagonal records

The inputs \((2,2\rho)\) and \((2,2\rho^{-1})\) each have
diagonal Gram entries \((4,4)\) and total account \(16\).
They are both admitted. The first output is

\[
 (1+2\rho-\rho^2,\ 1+\rho^2),
\]

so its receiver account is \(3\) by (34) and its source
account is \(16-3=13\).

The second output is

\[
 (\rho+\rho^{-1},\ 2-\rho+\rho^{-1}).
\]

Here
\((\rho+\rho^{-1})\overline{(\rho+\rho^{-1})}
=2+\rho^2+\rho^{-2}\), whose half-trace is \(3\).
The receiver account is therefore \(13\). Equivalently
its full norm is \(6-\rho^2-\rho^{-2}\), with half-trace
\(13\).

Thus the ordered source/receiver accounts are exactly
\((13,3)\) and \((3,13)\), while their totals agree.
Discarding the off-diagonal relative record would lose
this distinction. It is retained by the full \(G\).

### 7.4 A known map outside the admitted alphabet

On two slots define
\(\Phi(x,y)=(y,\bar x)\). The vectors \((1,1)\) and
\((j,j)\) have identical Grams. Their images are
\((1,1)\) and \((j,j^{-1})\), with off-diagonal Gram
entries \(1\) and \(j^2\), respectively. Therefore
\(\Phi\) does not descend to the Gram image.

This is the inherited QPAIR-HERM-INTEGER-NONDESCENT
witness. It is retained here to prevent a claim about
arbitrary integral gates. \(\Phi\) is not a word
whose Gram descent has been established by this
candidate's permitted alphabet.

### 7.5 Fresh-reference extension is not a hidden Gram operation

The one-slot inputs \(2\) and \(2\rho\) have the same
Gram \(4\). Append the same new absolute-phase
reference \(2\) and apply the pair contact.

For \((2,2)\), the contact is unchanged and the receiver
account is \(q(2)=8\). For \((2\rho,2)\), exchange
covariance of (13)-(14), or direct substitution, gives
receiver \(1+2\rho-\rho^2\), with account \(13\) by
Section 7.3.

Hence this proposed append-and-contact operation cannot
be computed from the old one-slot Gram. The missing
new cross terms with the reference carry relative
phase. This is a negative control on an extension
operation, not a change to the fixed \(N\ge2\) domain
of Claims A-C: the two complete two-slot input Grams
are different, and the positive theorem distinguishes
them correctly.

The apparatus of Section 6 avoids this hidden extension
by including both references and both archive cells
at its common origin. A different preparation or
loading operation needs its own contract.

## 8. Scientific scope and remaining interfaces

The mathematical closure just proved is conditional
on a specified complete system. It includes every
integral state, every refused contact, every actual
Gram fibre, arbitrary old receiver data, dirty
archives, and exact backward continuation. It has
no fitted threshold or nonzero-input exception.

Its extra premises are explicit:

- the full Cartesian carrier and marked slots;
- the #1833 sum/difference law, phase \(\rho=j^2\),
  and identity completion on refused inputs;
- the unnormalized complete global Gram;
- the chosen arithmetic interpretation of \(E\);
- the star graph, cyclic program and clock;
- the prepared source/reference values and two blanks;
- the three-boundary reading window and its status tag.

The record contains all pairwise entries, including
cross terms between sources, references and archives.
A local contact on \(z\) need not be a locally
acquirable measurement of that entire matrix.
The candidate proves no physical acquisition of \(G\),
no unique or minimal decoder, no source of new
independent data and no indefinite archive.

The fixed cyclic clock is part of the supplied
finite apparatus. Its explicit program is not
derived from the Thue-Morse selector, native \(U\),
a homogeneous local Hamiltonian, or Lorentz proper
time. The integer account is not asserted to be
physical energy, and the coefficient amplitudes
are not assigned a Born occurrence law.

The construction changes neither the fired
restrictions of native \(U\) nor the carrier of
the contact walk \(W\). It supplies no L2-L6 lift,
spatial dimension, particle identity, sampling
law or physical apparatus-owner closure. Prior
common-apparatus and occupied-archive constructions
are credited in [REFERENCES.md](REFERENCES.md);
a claim to the first such construction is expressly
not made.

Universal Claims A-D rest on the arguments above.
The finite audit in the preregistration is a
supplementary exact check of its frozen inventory.
It cannot replace the proof, and an unchanged-source
replay cannot by itself be called independent
mathematical confirmation.
