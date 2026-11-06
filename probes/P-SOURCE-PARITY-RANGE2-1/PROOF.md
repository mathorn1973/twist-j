# A finite parity certificate for diameter-two energy action

**NON-CANONICAL. L1. Conditional analytical certificate.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1788](https://github.com/mathorn1973/twist-j/issues/1788).
The exact execution contract is [PREREG.md](PREREG.md).
Independent scientific acceptance is not asserted.

This proof specifies a sufficient finite test for an obstruction to
the original energy action at physical interaction diameter two. It
uses one common geometrically forbidden projection for both actual
source phases. It does not select a new source, change the energy
branch or assume that the test passes. The scientific output and its
disposition belong to the separately pinned execution.

## 1. Frozen inputs and the compared physical class

The authority is ACTIVE
[Public Canon v105](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
The conditional original source is
[PR1777 at 191ab035](https://github.com/mathorn1973/twist-j/tree/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-FINITE-PHASE-OCCUPIED-RECORD-N),
and the nominated positive logarithm is
[PR1772 at 3abf054e](https://github.com/mathorn1973/twist-j/tree/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N).
The predecessor boundaries are frozen at
[PR1785, 19f1c74a](https://github.com/mathorn1973/twist-j/tree/19f1c74a27684a22bf038c1e6fc1133f638fb613/notes/C-SOURCE-LOCAL-ENERGY-N)
and
[PR1787, 16596484](https://github.com/mathorn1973/twist-j/tree/165964849b2d8f3ca6278e88755c1a8e03d6d842).
Their geometric and filtered-tail questions motivate this test. No
spectral cut-mass estimate, fitted density or absence of a cut atom is
a premise of the finite certificate proved below.

Keep the unchanged receiver-calibrated unitary and energy

\[
 U=U_{\rm rec},\qquad Q=E_0 f(U),\qquad E_0>0,
 \qquad f(e^{-i\theta})=\theta\quad(0\le\theta<2\pi).
 \tag{P1}
\]

The assigned value is f(1)=0. The normalized sources are

\[
 \psi_\sigma(\Xi)
 =\frac{[I+\sigma(U^2-U^{-2})]\chi(\Xi)}{\sqrt Z},
 \qquad \sigma\in\{+1,-1\},
 \qquad Z=\frac{39521+154\sqrt5}{15625},
\]
\[
 \chi(\Xi)=|R=97,r=0,iB;c=97,\mathrm{token},l=0\rangle
              \otimes\Xi,
 \qquad B=(e_2-e_3)/\sqrt2.
 \tag{P2}
\]

Xi is any normalized state of the original 26-label old memory and
a passive reference. All 26 labels are admitted for this energy
comparison. The restriction excluding d0 belongs to the separate
fresh-write contrast. Mixed inputs are covered by purification.
The retained orthogonal setting register, when present, is included
explicitly and does not replace the two sources by an unmarked
superposition.

The physical positions of the two object constituents are

\[
 x_A=R+r,\qquad x_B=R-r.
 \tag{P3}
\]

The carrier kind a has the three values token, pulse bank 1 and pulse
bank 2. Its position c is y in the token sector and x in the pulse
sector. The receiver stands at 100. The original occupation isometry
is \(\mathcal I=\mathsf{Emb}\,\Gamma^{-1}D_2^*\), with its diagonal
phase gauge retained. Object, carrier and memory use disjoint onsite
occupation subbanks: h1,...,h4; h5,...,h16; and h25,...,h37,
respectively. Each object constituent has nonzero occupation at its
declared position; every carrier code is nonzero at c. Different
carrier kinds have distinct codes. The nine onsite identity spectators
and passive references retain their original treatment.

Admit an optional fixed normalized ancillary state a_ready independent
of the data, with declared physical locations for its factors, and put

\[
 V\phi=\mathcal I\phi\otimes a_{\rm ready}.
 \tag{P4}
\]

Readiness may be entangled across ancillary sites. A fixed mixed ready
state can be purified with another passive reference. Each Hermitian
term H_X acts as identity outside X in the original physical lattice,
where diam(X)<=2. Thus X is contained in an interval of three
consecutive integer sites; arbitrary onsite occupation and ancillary
factors within X are permitted.

Finite sums \(\widetilde H=\sum_X H_X\) are admitted. For an infinite
sum, every compared \(V\psi_\sigma\) must be in the action domain and
the sum must agree with its partial sums on each used matrix element.
Strong convergence on the compared source vector is sufficient.
Alternatively, existence of the action together with the specified
matrix-element convergence is sufficient. Strong resolvent convergence
alone does not supply that agreement. The proof does not assume
positivity, charge conservation, bounded term strength or a bounded
number of ancillas. It therefore also applies to the smaller desired
positive charge-conserving class.

## 2. Exact source support and one common forbidden predicate

Every complete forward or inverse object step changes each physical
object position by either +1 or -1. Contact, coins, phases and carrier
factors do not change the object positions. Thus each complete step
flips the parity of both x_A and x_B. The source uses only seed powers
0,2,-2, so every source basis component has

\[
 x_A,x_B\in\{95,97,99\},\qquad 95\le c\le99.
 \tag{P5}
\]

The carrier bound follows because a complete forward or inverse step
changes c by at most one. Initial receiver calibration is therefore
identity on the full source support. The carrier label is 0 and the
old memory remains Xi there.

Form the exact coefficient vectors of both sources in the original
uncalibrated source coordinates. First collect all contributions to
each basis key (R,r,c,o,a), including cancellations, and determine
which coefficients are exactly nonzero. Only then discard the coin
entry o and take the union over both signs:

\[
 \mathcal S=\bigcup_{\sigma=\pm1}
 \{(R,r,c,a):\text{some coin coefficient of }
             [I+\sigma(U^2-U^{-2})]\chi\text{ is nonzero}\}.
 \tag{P6}
\]

The common nonzero normalization does not change this support. The
uncalibrated definition has no memory or reference input to inspect.
Taking the union is part of the fixed test: the projection is not
chosen separately after examining the results for the two signs.

For a target key alpha=(R,r,c,o,a), first require opposite object
parity, namely R+r even. Then R-r is also even. For each
beta=(R_b,r_b,c_b,a_b) in S define finite sets of physical sites

\[
 D_o(\alpha,\beta)=
 \{R+r,R-r,R_b+r_b,R_b-r_b\},
\]
\[
 D_c(\alpha,\beta)=
 \begin{cases}
 \varnothing,&(c,a)=(c_b,a_b),\\
 \{c,c_b\},&(c,a)\ne(c_b,a_b),
 \end{cases}
 \qquad D(\alpha,\beta)=D_o(\alpha,\beta)\cup D_c(\alpha,\beta).
 \tag{P7}
\]

The object set is nonempty, so its union always has a defined diameter.
Repeated positions are included only once. Define the orthogonal
diagonal projection F by the following fixed predicate:

\[
 \boxed{
 F\alpha=\alpha\quad\Longleftrightarrow\quad
 R+r\text{ is even and }
 \max D(\alpha,\beta)-\min D(\alpha,\beta)>2
 \text{ for every }\beta\in\mathcal S.
 }
 \tag{P8}
\]

Otherwise F alpha=0. The predicate ignores target coin, carrier label,
memory and references. It is a conservative geometric forbidden
projection, not a claim to be the maximal full physical projection.
For example every opposite-parity target with |r|>=2 is selected:
its two object positions already have separation 2|r|>=4. The full
predicate can also select configurations with smaller |r| through
their carrier and source-position constraints. A cutoff |r|>=3
would unnecessarily discard some of these certainly forbidden keys.

**Lemma P1.** For either actual source, every admitted old-memory and
reference state, and every physical term of diameter at most two,
all compressed matrix elements from that source to Ran F vanish.

**Proof.** Source object positions are odd, while the selected target
object positions are even. Their occupied sites are disjoint. At each
site in D_o, one of the two object patterns is vacuum and the other
has a nonzero object occupation. Every such site must therefore lie
in the support X of any term with a nonzero matrix element. This
proves the union rule for D_o without needing the object coin signs.
Discarding coin in (P6) is safe after exact support collection because
all its represented coins give the same required object sites here.

If carrier position changes, its old and new nonzero codes require
both sites c and c_b in X. If position is unchanged but kind changes,
the distinct carrier codes require that one site in X. Different
onsite subbanks cannot cancel these changes. Thus all sites of D_c
are also mandatory whenever its second case applies.
These requirements hold for every choice of carrier labels. Extra
label differences at an unchanged position and kind are intentionally
not counted in D_c.

For target c<100, the propagated carrier label is 0 and calibration
does not change it. For target c>=100, source c_b<=99 guarantees a
carrier-position change regardless of the old-memory label transferred
to the carrier. The label swap can add a memory change at 100, but
cannot remove a mandatory object or carrier change in D. Matrix
elements between different memory components of Xi may likewise add
changes and cannot remove D. Omitting labels and memory from (P7)
therefore remains conservative for every admitted Xi.

A selected alpha has diam(D)>2 against every actual source key.
No allowed X can contain the mandatory changed sites. The matrix
element is consequently zero. The diagonal occupation gauge changes
only phases, so preserves this zero. An ancillary state entangled
across sites cannot alter the data orthogonality on a factor outside
X. Passive references give the same conclusion componentwise.
Linearity proves the complete source statement. QED.

Summing under the stated convergence assumptions, applying the
contractions V^* and F, and retaining the full physical action gives

\[
 \boxed{
 \|\widetilde H V\psi_\sigma-VQ\psi_\sigma\|
 \ge E_0\|F f(U)\psi_\sigma\|.
 }
 \tag{P9}
\]

Leakage into ancillas or outside the code cannot cancel this projected
lower bound. No converse from an unselected target to realizability
of the complete required generator is asserted.

## 3. Parity isolates an exact spectral involution

Let Pi be multiplication by (-1)^(R+r) in the original coordinate
code, with identity on all other factors. The step-parity rule gives

\[
 \Pi U\Pi=-U,\qquad \Pi\psi_\sigma=-\psi_\sigma,
 \qquad P_e=(I+\Pi)/2,
 \qquad F=P_eF=FP_e.
 \tag{P10}
\]

Borel functional calculus implies Pi f(U) Pi=f(-U). Define the
real-valued spectral function and its operator

\[
 s(z)=\frac{f(z)-f(-z)}\pi,
 \qquad S=s(U).
\]

For z=exp(-i theta),

\[
 s(z)=
 \begin{cases}-1,&0\le\theta<\pi,\\
              +1,&\pi\le\theta<2\pi.
 \end{cases}
 \qquad s(1)=-1,\quad s(-1)=+1.
 \tag{P11}
\]

In particular S=S^*, S^2=I and Pi S Pi=-S, with the stated endpoint
assignments. Since each source has odd object parity,

\[
 P_e f(U)\psi_\sigma=\frac\pi2 S\psi_\sigma,
 \qquad \|P_e Q\psi_\sigma\|=\frac\pi2 E_0,
 \qquad Ff(U)\psi_\sigma=\frac\pi2 FS\psi_\sigma.
 \tag{P12}
\]

The fixed opposite-parity norm alone is not a lower bound on its
forbidden part. The finite test below bounds that particular part.

## 4. A ninth-degree approximation with a finite vector remainder

Put

\[
 A=\frac{U-U^*}{2i},\qquad C=\frac{U+U^*}{2},
 \qquad A^2+C^2=I.
 \tag{P13}
\]

A and C are commuting self-adjoint contractions. At spectral angle
theta, A=-sin(theta) and C=cos(theta). Away from A=0, s(z) is
the sign of A; at the two endpoints it has the separate assignments
in (P11).

Use the fixed odd polynomial

\[
 p_4(x)=\frac{315x-420x^3+378x^5-180x^7+35x^9}{128}.
 \tag{P14}
\]

For x in [0,1], p4(0)=0, p4(1)=1 and

\[
 p_4'(x)=\frac{315}{128}(1-x^2)^4.
\]

Hence 0<=p4(x)<=1 on that interval. To bound the error, let
g(x)=p4(x)-1+(1-x^2)^5. Its endpoint values are both zero, and

\[
 g'(x)=(1-x^2)^4\left(\frac{315}{128}-10x\right).
\]

This derivative changes sign once from positive to negative in (0,1).
Therefore g>=0 throughout [0,1]. Oddness gives the corresponding
absolute error bound for negative x. At A=0 either assigned sign in
(P11) has error exactly one, also equal to (1-A^2)^5 there. We obtain
the pointwise Borel inequality on the entire unit circle

\[
 |s(z)-p_4(A(z))|\le(1-A(z)^2)^5=C(z)^{10}.
 \tag{P15}
\]

In particular no exclusion of atoms at 1 or -1 is required. Squaring
and integrating against the source spectral measure yields

\[
 \boxed{
 \|S\psi_\sigma-p_4(A)\psi_\sigma\|
 \le\|C^{10}\psi_\sigma\|.
 }
 \tag{P16}
\]

This is a remainder on the unchanged source. Neither p4 nor C^10
is physically applied as a source filter or preparation.

## 5. Exact finite quantities and root elimination

Define separately for both nominated signs

\[
 W_\sigma=\|F p_4(A)\psi_\sigma\|^2,
 \qquad R_\sigma=\|C^{10}\psi_\sigma\|^2.
 \tag{P17}
\]

These are nonnegative real numbers with the source normalization
retained. Equations (P9), (P12), (P16) and contraction of F imply

\[
 \boxed{
 \frac{\|\widetilde H V\psi_\sigma-VQ\psi_\sigma\|}{E_0}
 \ge\frac\pi2\bigl(\sqrt{W_\sigma}-\sqrt{R_\sigma}\bigr).
 }
 \tag{P18}
\]

A negative right side is only the trivial bound. The same common F
is used for W_+ and W_-. Equal energy laws of the two sources do not
justify equating their projected W values.
R_sigma is the FULL norm of C^10 psi_sigma. It is not its projection
by F: C^10 preserves odd object parity, so that projected vector would
vanish and would not supply the error bound (P16).

All the quantities in (P17) are finite algebraic data. For an explicit
Laurent coefficient check, set z=U and define h(z)=i p4(A(z)). Direct
expansion of (P14) gives

\[
 \begin{aligned}
 65536h(z)={}&39690(z-z^{-1})
             +8820(z^3-z^{-3})\\
            &+2268(z^5-z^{-5})
             +405(z^7-z^{-7})+35(z^9-z^{-9}).
 \end{aligned}
 \tag{P19}
\]

The common factor i does not change a norm. Multiplication by
\([1+\sigma(z^2-z^{-2})]/\sqrt Z\) shows that the first vector
needs seed powers only through |k|<=11. The second uses

\[
 C^{10}=\frac1{1024}\sum_{j=0}^{10}\binom{10}{j}U^{10-2j},
 \tag{P20}
\]

and therefore seed powers only through |k|<=12 after the same source
multiplier. There is no infinite series or approximation to pi in
these vector calculations. Computing the norms by scalar moments
instead could require moments through order 24; the stated horizon
12 refers to propagation and combination of the vectors themselves.

For a purely algebraic sufficient threshold use pi>3 and set

\[
 t=1/1800,\qquad
 d_\sigma=W_\sigma-R_\sigma-t^2,\qquad
 e_\sigma=d_\sigma^2-4t^2R_\sigma.
 \tag{P21}
\]

For W_sigma,R_sigma>=0,

\[
 \sqrt{W_\sigma}-\sqrt{R_\sigma}>t
 \quad\Longleftrightarrow\quad d_\sigma>0
                              \text{ and }e_\sigma>0.
 \tag{P22}
\]

Indeed, the original inequality is equivalent to
W_sigma>R_sigma+t^2+2t sqrt(R_sigma). Subtracting the first two
terms requires d_sigma>0; only after that sign check is squaring
equivalent and gives e_sigma>0. Reversing the same steps proves the
converse. Thus the two strict algebraic sign tests imply

\[
 \boxed{
 \|\widetilde H V\psi_\sigma-VQ\psi_\sigma\|
 >\frac32 E_0\frac1{1800}=\frac{E_0}{1200}.
 }
 \tag{P23}
\]

Passing either nominated sign disproves uniform realization of the
pair in the stated physical class. Failure of these sufficient sign
tests is INCONCLUSIVE: it supplies neither a construction nor an
upper bound below the required action tolerance.

## 6. Memory, reference and setting uniformity

Let T be the original carrier-memory calibration, swapping their
complete labels when c>=100. It preserves R,r,c,coin and carrier
kind. The source and receiver unitary obey

\[
 U_{\rm rec}=T(U_{\rm src}\otimes I_{\rm mem,ref})T,
 \qquad T\chi(\Xi)=\chi(\Xi).
 \tag{P24}
\]

The predicate (P8) depends only on preserved coordinate and kind
data, so F commutes with T and acts as identity on labels and
references. For any Laurent polynomial q,

\[
 Fq(U_{\rm rec})\psi_\sigma(\Xi)
 =T\bigl(Fq(U_{\rm src})\psi_{\sigma,\rm src}\otimes\Xi\bigr).
 \tag{P25}
\]

The same identity without F also holds. Since T is unitary and Xi
has norm one, W_sigma and R_sigma are independent of all old-memory
labels and their arbitrary reference correlations. Mixed states are
covered by purification. This independence is a property of the
target certificate; an arbitrary comparator's actual error may
depend on its memory couplings. The geometric zero in Lemma P1
and (P18) nevertheless bound that error for every admitted Xi.

With a retained orthogonal setting register the squared projected
norms add with their setting weights, including reference-correlated
settings. Both pure settings remain admitted inputs. A result for
one nominated sign therefore suffices to refute a universal action
requirement, without claiming the other sign fails. It is also
permissible to test a Hamiltonian and fixed ready state chosen
separately for a given sign: Lemma P1 and the resulting bound
quantify over every such local comparator for that source. They do
not use cancellation between the actions on the two settings.

## 7. Separate review obligations and limits

1. Check the authority and exact source/energy pins, all phases and
   normalization, including the complete memory/reference scope.
2. Check parity of both physical object positions for forward and
   inverse steps and the source position bounds (P5).
3. Check exact coefficient collection before support extraction and
   the common union over both nominated signs in (P6).
4. Check the mandatory changed-site sets, including coincident sites,
   carrier-kind changes and why coin omission uses opposite parity.
5. Check the universal quantifier in (P8), the diameter-two threshold
   and the conservative treatment of labels and memory.
6. Check physical occupation subbanks, retained gauge, arbitrary fixed
   entangled ancillary readiness and all passive reference factors.
7. Check source action domains and matrix-element convergence, then
   the full physical norm lower bound (P9).
8. Check the parity functional calculus, both endpoint assignments
   and the exact opposite-parity norm in (P10)-(P12).
9. Check p4, its derivative, the scalar remainder proof including
   A=0, and the operator norm-on-vector estimate (P16).
10. Check both finite vector coefficients, source multipliers,
    normalization and the distinction between horizon 12 and moment
    order 24 in (P17)-(P20).
11. Check nonnegativity, both strict sign guards in root elimination,
    the pi>3 allowance and the fixed E0/1200 conclusion.
12. Check uniformity under calibration and references, separate
    reporting of both signs, and the INCONCLUSIVE disposition when
    a sufficient test fails.

The certificate concerns diameter two and the original bare encoding.
It does not decide other microscopic ranges, data-dependent dressed
encodings, a different energy law, preparation from equilibrium or
funded terminal readout and renewal. A passing necessary obstruction
would not invalidate the original discrete step or the separate
compact simulator with its own energy. A failed certificate would
not establish a local generator or continuous-time accuracy.

No scientific executable, import, numerical search or simulation was
run to author this proof. The finite mathematical inequalities are
conditional on the frozen model and source premises. Execution,
exact output and any earned disposition require the separately
published prospective pin. Same-session authoring and adversarial
checks are not independent external scientific acceptance.
