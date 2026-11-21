# A fixed family of weighted dual certificates at diameter two

**NON-CANONICAL. L1. Conditional analytical certificate.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1790](https://github.com/mathorn1973/twist-j/issues/1790).
The prospective execution contract is [PREREG.md](PREREG.md).
Independent scientific acceptance is not asserted.

This proof fixes 66 sufficient comparisons: both original source
signs, witness powers m=0,1,2, and error exponents a=0,...,10. It
replaces the preceding full-vector error allowance by a bound on the
error in each declared dual direction. All comparisons belong to the
prospective family and are reported separately. No passing value is
assumed and no source or threshold is changed after a result.

The original geometry and parity certificate is frozen in
[PR1789 PROOF.md at 538341e0](https://github.com/mathorn1973/twist-j/blob/538341e03bd18fecdaf0eeaa6d88d154eb8e851f/probes/P-SOURCE-PARITY-RANGE2-1/PROOF.md).
Its two dispositions were INCONCLUSIVE. The present baseline m=0,a=0
is algebraically the same comparison; the other members have the
stronger weights and witnesses specified below.

## 1. Unchanged source, energy and physical comparison

The authority remains ACTIVE
[Public Canon v105](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
The source is the conditional
[PR1777 pair at 191ab035](https://github.com/mathorn1973/twist-j/tree/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-FINITE-PHASE-OCCUPIED-RECORD-N),
and the nominated positive logarithm is retained from
[PR1772 at 3abf054e](https://github.com/mathorn1973/twist-j/tree/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N).
Keep

\[
 U=U_{\rm rec},\qquad Q=E_0f(U),\quad E_0>0,
 \qquad f(e^{-i\theta})=\theta\quad(0\le\theta<2\pi),
 \qquad f(1)=0,
 \tag{D1}
\]
\[
 \psi_\sigma(\Xi)
 =\frac{[I+\sigma(U^2-U^{-2})]\chi(\Xi)}{\sqrt Z},
 \quad \sigma\in\{+1,-1\},
 \quad Z=\frac{39521+154\sqrt5}{15625},
\]
\[
 \chi(\Xi)=|R=97,r=0,iB;c=97,\mathrm{token},l=0\rangle\otimes\Xi,
 \qquad B=(e_2-e_3)/\sqrt2.
 \tag{D2}
\]

Xi is any normalized state of the full 26-label old memory and a
passive reference. Mixed inputs are included by purification. The
25-label exclusion of d0 belongs only to the inherited fresh-write
contrast. It is not imposed on this energy comparison.

The original occupation isometry
\(\mathcal I=\mathsf{Emb}\,\Gamma^{-1}D_2^*\) and its diagonal gauge
are unchanged. Physical object positions are x_A=R+r and x_B=R-r.
The carrier kind is token, pulse bank 1 or pulse bank 2 at position c;
the receiver is at 100. Object, carrier and memory occupy disjoint
onsite subbanks. Passive references and the original identity
spectators remain accounted for.

For any fixed normalized ancillary ready state a_ready independent
of the data, let \(V\phi=\mathcal I\phi\otimes a_{\rm ready}\).
Ancillary factors have declared physical locations and may be
entangled across them. The comparator is any admitted sum
\(\widetilde H=\sum_X H_X\), each term acting as identity outside X,
with diam(X)<=2 in the original integer lattice. Finite sums suffice.
For infinite sums, the source action must exist and its used matrix
elements must agree with the limits of partial sums. Strong
convergence on the compared source is sufficient; strong resolvent
convergence alone is not substituted for this requirement.

The necessary bounds below do not assume positivity, charge
conservation, bounded term strength or bounded ancillary dimension.
They include the desired smaller positive charge-conserving class.
The source and the bare encoding are not dressed or physically
filtered by this test.

## 2. The fixed common geometric projection

Use exactly the common projection F of the pinned predecessor proof.
For clarity, its computable predicate is restated here. Collect the
exact nonzero coefficients of both source vectors before discarding
coin, then form their common support union

\[
 \mathcal S=\bigcup_{\sigma=\pm1}
 \{(R_b,r_b,c_b,k_b):\text{some source coin coefficient is nonzero}\}.
 \tag{D3}
\]

The carrier kind is denoted k_b here to distinguish it from the error
exponent a below. Every source object position is odd and lies in
{95,97,99}; every source carrier lies in [95,99]. The forward and
inverse complete steps each flip both object parities and move c
by at most one, which proves these bounds for the seed powers 0,2,-2.

For a target alpha=(R,r,c,o,k) with R+r even, put

\[
 D_o(\alpha,\beta)=\{R+r,R-r,R_b+r_b,R_b-r_b\},
\]
\[
 D_c(\alpha,\beta)=
 \begin{cases}\varnothing,&(c,k)=(c_b,k_b),\\
 \{c,c_b\},&(c,k)\ne(c_b,k_b),\end{cases}
 \qquad D=D_o\cup D_c.
 \tag{D4}
\]

F selects alpha exactly when its object parity is even and diam(D)>2
for every beta in S. Otherwise it gives zero. Its definition ignores
labels, memory and references; this remains a conservative forbidden
projection, not a claim of maximal physical reachability.

Source and selected target object sites have opposite parity, so
their occupied sites are disjoint. Every site of D_o changes from
object occupation to vacuum or conversely, independently of coin.
A changed carrier position or kind requires every site of D_c as
well. Separate subbanks prevent cancellation. Any term with a
nonzero matrix element must include all those mandatory changed
sites. The predicate makes that impossible at diameter two against
every nonzero source component. Extra carrier-label or memory
changes can add sites and cannot remove D.

The diagonal physical gauge preserves these zeros. Fixed ancillary
entanglement cannot alter a data factor outside a term's support.
The pinned predecessor proof gives the complete memory/reference and
sum-domain argument. Consequently, for either sign and every admitted
Xi,

\[
 F V^*\widetilde H V\psi_\sigma=0,
 \qquad
 \|\widetilde H V\psi_\sigma-VQ\psi_\sigma\|
       \ge E_0\|Ff(U)\psi_\sigma\|.
 \tag{D5}
\]

All uses of F in this family are the same fixed projection (D3)-(D4).
Neither its support nor the source is retuned for m, a or sign.

## 3. Parity and the unchanged sign polynomial

Let Pi multiply a coordinate ket by (-1)^(R+r), and put P_e=(I+Pi)/2.
The original step and sources satisfy

\[
 \Pi U\Pi=-U,\qquad \Pi\psi_\sigma=-\psi_\sigma,
 \qquad F=P_eF=FP_e.
 \tag{D6}
\]

For the real Borel function

\[
 s(z)=\frac{f(z)-f(-z)}\pi,\qquad S=s(U),
\]

one has S=S^*, S^2=I and

\[
 s(e^{-i\theta})=
 \begin{cases}-1,&0\le\theta<\pi,\\
               +1,&\pi\le\theta<2\pi,
 \end{cases}
 \quad s(1)=-1,\quad s(-1)=+1.
 \tag{D7}
\]

Borel functional calculus gives Pi f(U) Pi=f(-U). Thus

\[
 Ff(U)\psi_\sigma=\frac\pi2 FS\psi_\sigma.
 \tag{D8}
\]

Define the commuting self-adjoint contractions

\[
 A=\frac{U-U^*}{2i},\qquad C=\frac{U+U^*}{2},
 \qquad A^2+C^2=I,
\]
\[
 p_4(x)=\frac{315x-420x^3+378x^5-180x^7+35x^9}{128},
 \qquad E=S-p_4(A).
 \tag{D9}
\]

At angle theta, A=-sin(theta), C=cos(theta). Away from A=0, S is
the sign of A. The assigned signs at A=0 remain those of (D7),
including any spectral atoms there. Since
p4'(x)=(315/128)(1-x^2)^4 on [0,1], with p4(0)=0 and p4(1)=1,
the polynomial is monotone from zero to one there and odd on the
whole real line. In particular |p4(x)|<=1 for |x|<=1.

The predecessor's scalar bound |E|<=C^10 is retained. The next
section proves a sharper weighted envelope directly and also
recovers that bound. No cut-mass or no-atom premise is needed.

## 4. Positive Taylor coefficients give all eleven error envelopes

For 0<=y<=1, define

\[
 e(y)=1-p_4(\sqrt{1-y}).
 \tag{D10}
\]

Then e(0)=0, e(1)=1 and e(y)>=0. In spectral notation y=C^2,
the exact absolute error is |E|=e(C^2), including A=0. For 0<=y<1,

\[
 e'(y)=\frac{315}{256}\frac{y^4}{\sqrt{1-y}}.
\]

Expanding the binomial series and integrating from zero gives

\[
 e(y)=\sum_{n=5}^{\infty} e_n y^n,
 \qquad
 e_n=\frac{315}{256n}
       \frac{\binom{2(n-5)}{n-5}}{4^{n-5}}>0.
 \tag{D11}
\]

The positive coefficients sum to e(1)=1 by monotone convergence.
Their Cauchy product therefore gives

\[
 e(y)^2=\sum_{n=10}^{\infty}q_n y^n,
 \qquad q_n=\sum_{j=5}^{n-5}e_j e_{n-j}>0,
 \qquad\sum_{n=10}^{\infty}q_n=1.
 \tag{D12}
\]

In particular e5=63/256 and q10=(63/256)^2. The equalities extend to
y=1 because all terms are nonnegative and their total sums are finite.

For each fixed integer a=0,...,10 set

\[
 Q_a=\sum_{n=10}^{a+9}q_n,
 \qquad
 r_a(y)=\sum_{n=10}^{a+9}q_n y^{n-a}+(1-Q_a)y^{10}.
 \tag{D13}
\]

An empty sum, at a=0, is zero. Every coefficient is nonnegative,
the coefficients sum to one, and r_a has degree at most ten.
For 0<y<=1 the remaining tail terms satisfy y^(n-a)<=y^10
when n>=a+10. Hence

\[
 \frac{e(y)^2}{y^a}\le r_a(y)\le y^{10-a}.
 \tag{D14}
\]

The second inequality follows because all retained exponents are
at least 10-a. The first inequality has a finite continuous
extension at y=0; at a=10 its limiting left side is q10.
This endpoint statement concerns the scalar envelope, not a need
to divide an operator by zero.

Define a Borel function h_a on the spectrum of U by

\[
 h_a=E/C^a\quad\text{where }C\ne0,
 \qquad h_a=0\quad\text{where }C=0.
 \tag{D15}
\]

For a=0 this assignment agrees with E at C=0, because A=+1 or -1
there and p4(A)=S. For every a in the declared range,

\[
 E=C^a h_a(U),\qquad |h_a(U)|^2\le r_a(C^2).
 \tag{D16}
\]

The sign of C for odd a is retained by (D15); the square estimate
uses C^(2a). At C=0 both sides of the factorization vanish. At
A=0, equivalently C^2=1, the error is exactly one and r_a(1)=1.
Thus all endpoint atoms are covered by the stated Borel definitions.

For each source define the full moments

\[
 R_{\sigma,j}=\|C^j\psi_\sigma\|^2,
 \qquad 0\le j\le10,
\]
\[
 \boxed{
 \mathcal R_{\sigma,a}
 =\langle\psi_\sigma,r_a(C^2)\psi_\sigma\rangle
 =\sum_{n=10}^{a+9}q_n R_{\sigma,n-a}
       +(1-Q_a)R_{\sigma,10}.
 }
 \tag{D17}
\]

This is a LINEAR COMBINATION of squared norms. It is not
\(\|r_a(C^2)\psi_\sigma\|^2\), and no spatial projection is
inserted in any R_sigma,j. Equations (D16)-(D17) give
\(\|h_a(U)\psi_\sigma\|^2\le\mathcal R_{\sigma,a}\).
The simple checks at a=0 and a=1 are

\[
 \mathcal R_{\sigma,0}=R_{\sigma,10},
 \qquad
 \mathcal R_{\sigma,1}
 =(63/256)^2R_{\sigma,9}
       +[1-(63/256)^2]R_{\sigma,10}.
 \tag{D18}
\]

The sharper envelope always satisfies
\(\mathcal R_{\sigma,a}\le R_{\sigma,10-a}\).
It uses only e_n with 5<=n<=14 and q_n with 10<=n<=19, all rational,
and requires no additional source propagation beyond j=10.

## 5. Three forbidden witnesses from a positive compression

For each source sign, fix

\[
 v_\sigma=F p_4(A)\psi_\sigma,
 \qquad L=F A^2 F,
 \qquad w_{\sigma,m}=L^m v_\sigma,
 \quad m=0,1,2.
 \tag{D19}
\]

Because 0<=A^2<=I and F is an orthogonal projection,
0<=L<=F<=I. Every w_sigma,m stays in Ran F. Define

\[
 X_{\sigma,m}=\operatorname{Re}\langle w_{\sigma,m},v_\sigma\rangle,
 \qquad N_{\sigma,m}=\|w_{\sigma,m}\|^2,
 \qquad B_{\sigma,m,a}=\|C^a w_{\sigma,m}\|^2.
 \tag{D20}
\]

Inner products use the convention linear in the second argument.
Self-adjointness and positivity of L imply

\[
 X_{\sigma,m}=\langle v_\sigma,L^m v_\sigma\rangle\ge0,
 \qquad N_{\sigma,m}=\langle v_\sigma,L^{2m}v_\sigma\rangle\ge0.
 \tag{D21}
\]

The expression for X is real; the real-part notation in (D20)
does not discard a theoretically nonzero imaginary contribution.
The B values are FULL norms. There is no F after, before, or between
the C steps beyond the F already contained in the defined w_sigma,m.
Inserting such projections would change the error bound.

For each sign and each m,a pair, abbreviate

\[
 P_{\sigma,m,a}=B_{\sigma,m,a}\mathcal R_{\sigma,a}\ge0.
 \tag{D22}
\]

Since E=C^a h_a(U), self-adjointness of C^a and Cauchy--Schwarz give

\[
 |\langle w_{\sigma,m},E\psi_\sigma\rangle|
 =|\langle C^a w_{\sigma,m},h_a(U)\psi_\sigma\rangle|
 \le\sqrt{P_{\sigma,m,a}}.
 \tag{D23}
\]

Moreover w_sigma,m lies in Ran F, so
\(\langle w_{\sigma,m},p_4(A)\psi_\sigma\rangle
=\langle w_{\sigma,m},v_\sigma\rangle=X_{\sigma,m}\).
For N_sigma,m>0, using the normalized dual vector in Ran F yields

\[
 \|FS\psi_\sigma\|
 \ge\frac{|\langle w_{\sigma,m},S\psi_\sigma\rangle|}
          {\sqrt{N_{\sigma,m}}}
 \ge\frac{X_{\sigma,m}-\sqrt{P_{\sigma,m,a}}}
          {\sqrt{N_{\sigma,m}}}.
 \tag{D24}
\]

Combining (D5), (D8) and (D24) proves the family of physical bounds

\[
 \boxed{
 \frac{\|\widetilde H V\psi_\sigma-VQ\psi_\sigma\|}{E_0}
 \ge\frac\pi2
      \frac{X_{\sigma,m}-\sqrt{P_{\sigma,m,a}}}
           {\sqrt{N_{\sigma,m}}}.
 }
 \tag{D25}
\]

A negative right side is only the trivial bound. If N=0, that
particular normalized witness is unavailable and cannot pass.
This construction supplies mathematical dual vectors, not a
physical filtering or modified preparation of the original source.

## 6. Four exact guards and baseline equivalence

Use the same fixed dimensionless threshold t=1/1800. For each of
the 66 triples (sigma,m,a), suppress indices and form

\[
 d=X^2-P-t^2N,
 \qquad e=d^2-4t^2NP.
 \tag{D26}
\]

For the nonnegative quantities defined above, the sufficient
comparison is exactly

\[
 \boxed{N>0,\quad X>0,\quad d>0,\quad e>0.}
 \tag{D27}
\]

Indeed, for N>0 the desired inequality is
X>sqrt(P)+t sqrt(N). Its right side is nonnegative. Requiring X>0
permits the first squaring, giving
d>2t sqrt(NP). Requiring d>0 then permits the second squaring,
which is e>0. Reversing these steps proves equivalence. Neither
of the two sign guards may be dropped merely because a square is
positive. A passing profile therefore gives, using pi>3,

\[
 \|\widetilde H V\psi_\sigma-VQ\psi_\sigma\|
 >\frac32 E_0\frac1{1800}=\frac{E_0}{1200}.
 \tag{D28}
\]

At m=0, w=v and X=N=W=||v||^2. At a=0, B=N=W and
mathcal R=R10. Thus (D24) becomes exactly

\[
 \sqrt W-\sqrt{R_{\sigma,10}},
 \tag{D29}
\]

the preceding parity certificate. This baseline must have the same
disposition as the pinned predecessor when evaluated with the same
source, projection and exact coefficients. It is not reinterpreted
as a new successful test.

All 2*3*11 profiles are fixed in advance and retain the same target.
Any passing profile supplies its declared sign's obstruction; it
does not establish that the other sign fails. Failure of a profile
or of the entire sufficient family is INCONCLUSIVE, not evidence
for a physical construction. All exact comparisons and dispositions
are retained rather than selecting only favorable output.

## 7. Finite implementation scope and exact identities

The source polynomial and p4(A) make v a combination of seed powers
through |k|<=11, followed by F. The remainder moments R_j use
C^j psi_sigma and require seed powers only through j+2<=12.
Each L stage uses

\[
 A^2=(2I-U^2-U^{-2})/4,
 \qquad Lw=F A^2w\quad\text{for }w\in\operatorname{Ran}F.
 \tag{D30}
\]

F is applied after each complete A^2 combination in a witness
stage. It is not inserted inside the U^2 or U^-2 propagation.
After m stages and a further C^a propagation, the coordinate
propagation budget is at most

\[
 11+2m+a\le25.
 \tag{D31}
\]

In particular |R-97|, |r| and |c-97| are at most 25 in these
finite vector calculations. This is a propagation bound for the
test vectors, not a change of the physical comparator diameter
from two or a claim of a 25-site apparatus. Intermediate F
projections remove entries and never move positions. The original
infinite-lattice step is used without a cyclic wrap or boundary
identification.

If the existing exact arithmetic gauge writes U25=25U, then on
Ran F the integral recurrence is

\[
 2500Lw=F\bigl(1250w-U25^2w-(U25^*)^2w\bigr).
 \tag{D32}
\]

All scale factors must be included before computing X,N,B or the
guards. A common unit complex scalar multiplying v and every w_m
leaves these quantities unchanged. Thus an implementation may use
i p4(A) to keep Laurent coefficients in its fixed arithmetic field,
provided this same scalar is carried through the entire witness
family. The theoretical dual can be rotated back by that scalar;
it is not an independently chosen phase at each stage.

Useful exact consistency identities include

\[
 X_{\sigma,0}=N_{\sigma,0}=B_{\sigma,0,0}=W_\sigma,
 \quad R_{\sigma,0}=1,
 \quad B_{\sigma,m,0}=N_{\sigma,m},
\]
\[
 B_{\sigma,m,1}
 =N_{\sigma,m}-\langle w_{\sigma,m},Lw_{\sigma,m}\rangle.
 \tag{D33}
\]

The last identity follows from C^2=I-A^2 and w in Ran F. Positivity
also gives 0<=N_m<=X_m<=W, and contractivity of C gives
0<=R_(j+1)<=R_j and 0<=B_(m,a+1)<=B_(m,a). These are mathematical
identities and inequalities, not permission for an additional
unpinned scientific execution.

## 8. Calibration, references and limits of the conclusion

The original receiver calibration T preserves R,r,c,coin and carrier
kind and swaps the complete labels only when c>=100. It satisfies

\[
 U_{\rm rec}=T(U_{\rm src}\otimes I_{\rm mem,ref})T,
 \qquad T\chi(\Xi)=\chi(\Xi).
 \tag{D34}
\]

F commutes with T because its predicate uses only preserved spatial
and kind data. Every operator used to build A,C,L,v,w_m and their
moments therefore transforms by the same conjugation. Their norms
and X inner products factor out the normalized Xi exactly. All
reported quantities are uniform over all 26 old-memory labels and
arbitrary passive reference correlations, including mixed inputs
by purification. No unknown memory is used as clean workspace.

A comparator's actual error may depend on its memory couplings;
the same certified lower bound nevertheless applies to each
admitted Xi. With retained orthogonal settings both pure signs
remain admitted inputs, including reference-correlated settings.
The proof can also be applied to a different local Hamiltonian
or data-independent ready state chosen separately for a given
sign, since the forbidden matrix elements are zero for every such
comparator. No cancellation between the two source errors is used.

This certificate leaves data-dependent dressed encodings, another
declared energy, and other specified interaction diameters outside
its scope. Passing a necessary energy-action obstruction would
not invalidate the original discrete step or the compact simulator
with its own conserved Hamiltonian. Failure would not supply a
local physical generator, a full trajectory estimate, preparation
from equilibrium, funded final readout, retention or renewal.

## 9. Separate review obligations

1. Check the exact predecessor pin and unchanged source, energy cut,
   normalization, authority and conditional scientific status.
2. Check reuse of the common support union and conservative geometric
   predicate, including both signs and all carrier kinds.
3. Check original occupation subbanks, diagonal gauge, fixed ancillary
   entanglement and the source-domain/matrix-element assumptions.
4. Check parity functional calculus and both endpoint values of S;
   no cut atom is discarded.
5. Check p4, the scalar definition e(y), its derivative, and the
   positive coefficients e_n with their endpoint sum one.
6. Check convolution q_n, tail indices a+9 and a+10, degree ten and
   both inequalities in (D14), including a=0 and a=10.
7. Check the signed factorization through C^a, the definition at C=0
   and the weighted operator bound (D16).
8. Check that mathcal R is a linear combination of full R_j norms,
   not a norm square of r_a applied to the source.
9. Check positivity of L=FA^2F, placement of F after each A^2 stage,
   retained forbidden support and reality/nonnegativity of X.
10. Check the full B norms without intermediate F, the dual error
    pairing and its normalization in (D23)-(D25).
11. Check all four guards, both reversible squarings, the exact fixed
    threshold and the pi>3 allowance.
12. Check m=0,a=0 equivalence with the previous INCONCLUSIVE baseline
    and reporting of all 66 predetermined profiles.
13. Check propagation through seed radius 12 and witness radius 25,
    the integral recurrence and every denominator and common phase.
14. Check calibration/reference uniformity and preserve the distinction
    between a passing necessary obstruction and an INCONCLUSIVE test.

No scientific executable, import, numerical search or simulation was
run to author this proof. Exact execution and its reported outputs
require the separately published prospective pin. Same-session
authoring and adversarial checks do not constitute independent
external scientific acceptance or change Public Canon v105.
