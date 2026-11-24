# Common zero windows and the complete power-saving gap

**NON-CANONICAL. No authority. Candidate-D paper deductions.**
Owner: A. M. Thorn / ChatGPT arithmetic-kernel session, 24 November 2026.
Same claim [#2087](https://github.com/mathorn1973/twist-j/issues/2087)
and draft [#2089](https://github.com/mathorn1973/twist-j/pull/2089).
Action layer: NOT_APPLICABLE. The complete all-epsilon bound remains **O**.

This continuation proves further cancellations in the actual coefficients,
including all original numerators on specified periodic time windows. It
also absorbs the repeated-large-prime operator in an equivalent arithmetic
criterion. It does not prove the complete power saving. The exact remaining
quantity below retains every mixed term and the original prime correction.

## 1. Frozen problem and quantifiers

The input is the [round-seven candidate](../round7/REPORT.md) at
`6649670532e4d69858bc92994a55a54682f5d619`. Write

\[
 D=4X,\quad z=D^{1/3},\quad
 T(n)=\sum_{m\le n}t(m),\quad t=\chi_5*s,
\]

where \(s(d)=(-2)^{\omega(d)}\) on squarefree products of primes
\(p\equiv1,4\pmod5\), and is zero otherwise. The taper \(w\) equals
one on \([X,2X)\), vanishes outside \([7X/8,17X/8]\), and is unchanged.
Use \(\|F\|_w^2=\sum_nw(n)|F(n)|^2\) and its inner product. All block
estimates mean every fixed \(\varepsilon>0\) and all sufficiently late
dyadic \(X\), with constants and onset allowed to depend on that epsilon.

The frozen spectrum is

\[
 G_7(n)=\sum_{r\in\mathcal G_7}\sum_{a\in\mathcal A_r}
 A_r b(r,a)m_X\!\left(\frac{a}{5r}\right)e\!\left(\frac{an}{5r}\right).
 \tag{1}
\]

Here \(\mathcal G_7\), the signed primitive numerator sets
\(\mathcal A_r\), the cofactor coefficients \(A_r\), and the even
Jackson multiplier \(m_X\) are precisely the earlier ones. No threshold
in those sets changes. The original correction, including repeated pairs,
is

\[
 C_z(n)=-2\sum_{\substack{p>z\\p\equiv1,4\ (5)}}T(\lfloor n/p\rfloor)
        -4\sum_{\substack{z<p\le q\\p,q\equiv1,4\ (5)}}
                    T(\lfloor n/(pq)\rfloor).
 \tag{2}
\]

All sums end where the incoming floor is zero. Round seven gives

\[
 \|T-(G_7+C_z)\|_w^2\ll_\varepsilon X^{2+\varepsilon},\qquad
 Q_7=P_7+2\operatorname{Re}\langle G_7,C_z\rangle_w+\|C_z\|_w^2
     =\|G_7+C_z\|_w^2+O_\varepsilon(X^{2+\varepsilon}).
 \tag{3}
\]

The outstanding problem is \((Q_7)_+\ll_\varepsilon X^{2+\varepsilon}\)
with these quantifiers. Its equivalence to the earlier complete arithmetic
criterion is inherited; it is not an available premise for any new bound.

## 2. Whole-numerator cancellation on common zero windows

**Candidate-D.** Put \(D_0=\lfloor X^{2/3}\rfloor\) and, for each actual
conductor, define the periodic indicator

\[
 W_r^0(n)=\mathbf1\{n=5kr+u\text{ for some }k\in\mathbb Z,
                         \ -D_0\le u<D_0\}.
 \tag{4}
\]

For any fixed outer subset of \(\mathcal G_7\), the packet formed by
multiplying each complete original conductor packet by \(W_r^0(n)\)
has squared taper norm \(O_\varepsilon(X^{2+\varepsilon})\). The
bound includes every original retained numerator and applies on every
original shell. It requires no upper bound on the largest proper divisor.
The proof is [PERIODIC-SHARP-CAP](PERIODIC-SHARP-CAP.md).

The reason for the common window is exact. Let
\(H(j)=\sum_{m\le j}\chi_5(m)\), extended with period five, so its
residues are \((0,1,0,-1,0)\), and let \(K_d(n)=H(\lfloor n/d\rfloor)\).
If \(d\mid r\) and \(d\ge D_0\), then on (4)

\[
 \left\lfloor\frac nd\right\rfloor
 =5k(r/d)+\left\lfloor\frac ud\right\rfloor,
 \qquad \left\lfloor\frac ud\right\rfloor\in\{-1,0\}.
\]

Both residues have \(H=0\). Thus all such raw divisor terms vanish
simultaneously. The mask is held fixed at the evaluation time before
smoothing. The first absolute moment of the Jackson kernel and a divisor
bound pay the shift error. For the remaining \(d<D_0\), the exact
primitive expansion and the reflection \(n\mapsto-1-n\) cancel the
zero Fourier mode before a large sieve is applied. The resulting squared
bound is

\[
 O_\varepsilon\bigl(X^\varepsilon(XD_0+D_0^3)\bigr)
 =O_\varepsilon(X^{2+\varepsilon}).
\]

The separate sharp-cap argument pays all the omitted original numerators
at the same precision. This step is essential: a smooth cutoff alone
would not establish the bound on (4) for the original packet.

The family includes actual conductors beyond the earlier proper-divisor
ceiling. Choose the largest original shell base \(R\le X/1000\) and
\(r=11p_1p_2p_3\), with distinct split primes

\[
 (6R/55)^{1/3}\le p_i\le(7R/55)^{1/3}.
\]

Then \(6R/5\le r\le7R/5\), \(r/P^-(r)=r/11\asymp X\), and the
original small-prime exclusions keep these conductors. Their actual
cofactor coefficient is nonzero. Fixed-modulus prime counts and complete
periods inside \([X,2X)\) give
\(\gg X^{5/3}/(\log X)^3\) selected conductor-time incidences already
at numerator one. This is a count, not a lower bound on energy. The
unselected times remain in the complete problem; some upper conductors
have no selected time on the taper at all.

## 3. Exact proper-frequency removal on a smooth subpacket

**Candidate-D.** There is a stronger norm bound on a narrower, explicitly
weighted packet. Fix an integer \(\ell\ge3\), keep the above shell
\(R\asymp X/1000\), and take products of \(\ell\) distinct split primes
in \([(6R/5)^{1/\ell},(7R/5)^{1/\ell}]\). Fix

\[
 B=X^{1-1/(2\ell)},\qquad L=\lfloor R/100\rfloor,
\]

and a fixed real even smooth \(0\le\eta\le1\), equal to one on
\([-1,1]\) and supported on \([-2,2]\). Add the weight
\(\eta(Ba/(5r))\) to the original modes and select only those times
whose whole integer interval \([n-L,n+L]\) stays inside a zero plateau
of \(K_r\). Call the resulting moving packet \(V_\ell\). Then

\[
 \boxed{\ \|V_\ell\|_w^2\ll_{\ell,\varepsilon}X^\varepsilon.\ }
 \tag{5}
\]

The exact identity

\[
 \Phi_r-K_r=-\sum_{\substack{e\mid r\\e<r}}\frac er\Phi_e
\]

has no constant term. Every frequency of \(\Phi_e\) has circular
distance at least \(1/(5e)\) from zero. The largest proper divisor is
\(E\ll_\ell R^{1-1/\ell}\), whereas \(B>10E\) for sufficiently late
\(X\). The added multiplier therefore kills every proper-divisor term
exactly. The smoothed raw term then has only its tail beyond \(L\),
bounded by \(O(X^{-3/2})\) after choosing a fixed differentiation order
greater than \(3\ell+1\). Its total raw mass is
\(O_\varepsilon(RX^\varepsilon)\), giving a pointwise bound
\(O_{\ell,\varepsilon}(X^{-1/2+\varepsilon})\) and (5).

For each such conductor at least \(X/2\) central times are selected,
and numerator one remains nonzero. There are
\(\gg_\ell X^2/(\log X)^\ell\) actual incidences. The full proof and
the earlier interval estimates are in
[MOVING-RESIDUE-ZEROS](MOVING-RESIDUE-ZEROS.md).

The value of \(\ell\), constants, derivative order and starting block
are fixed before the estimate. No uniform claim for \(\ell=\ell(X)\)
follows. This smooth packet can overlap other deletions, so it is stated
separately and is not subtracted a second time in Section 5. On its own,
the trivial bound \(\|G_7+C_z\|_w\ll_\varepsilon X^{3/2+\varepsilon}\)
and (5) even give an additive change
\(O_{\ell,\varepsilon}(X^{3/2+\varepsilon})\) in the complete quadratic
expression after the exact cross terms are included.

## 4. Actual numerator cancellation and small determinants

**Candidate-D.** Let \(N=\max\operatorname{supp}w\). For every fixed
conductor family with \(r/P^-(r)\le z^2\), replacing its full retained
primitive packet by \(\sum_r A_rK_r\) costs
\(O_\varepsilon(X^{2+\varepsilon})\) in squared norm. In particular
all three-prime conductors \(r>N\) may be removed at this scale, since
their raw kernels vanish on the taper. Here the upper bound on each
prime is \(z\), so every proper divisor has size at most \(z^2\).

This contains actual large cancellation across numerators. For the
three-prime conductors in \((3X,4X]\), the original ordered pair subtotal
with both numerators equal to one is
\(\gg X^3/(\log X)^6\), while their complete signed restricted pair sum
is \(O_\varepsilon(X^{2+\varepsilon})\). Conversely, for three-prime
conductors in \([5X/4,4X/3]\), the complete packet itself has squared
norm \(\gg X^3/(\log X)^6\). On the central interval
\([3X/2,7X/4]\) their raw kernels all equal one and \(A_r=-8\).
Thus deleting this entire interior family as a separately small amplitude
would be false. Its joint complement \(G_7-V_{\rm in}+C_z\) must
compensate for this interior packet \(V_{\rm in}\). This does not by
itself bound the norm of the union of all three-prime conductors.

There is also an absolute deletion inside the original fixed pair mask.
For an admitted unequal-conductor pair \((r,a),(s,b)\) on shells
\(R,S\), write

\[
 g=\gcd(r,s),\quad l=\gcd(|a|,|b|),\quad
 L_{a,b}=\min(R/|a|,S/|b|).
\]

The total absolute contribution of pairs satisfying

\[
 0<\frac{|as-br|}{gl}\le\frac{X}{L_{a,b}}
 \tag{6}
\]

is \(O_\varepsilon(X^{2+\varepsilon})\). The estimate counts the
actual integer determinant and the one-dimensional lattice of solutions,
uses the original strip for one part of the count and (6) for the other,
and then sums the divisor and harmonic factors. Actual four-prime
conductors beyond the proper-divisor ceiling supply
\(\gg X/(\log X)^8\) nonzero admitted ordered pairs of this type.
The count alone makes no claim about their signed energy. Both deductions
and both large three-prime examples are proved in
[PROPER-DIVISORS-AND-DETERMINANTS](PROPER-DIVISORS-AND-DETERMINANTS.md).

## 5. One complete successor with every cross term

**Candidate-D, equivalence only.** Use the following fixed order, to avoid
counting overlapping removals twice. Let \(V_{\rm out}\) contain every
three-prime conductor of \(G_7\) with \(r>N\), with all its original
numerators. Set \(G_*=G_7-V_{\rm out}\). Restrict the original ordered
pair sum \(P_7\) to the coordinates still in \(G_*\), removing both
crossing orders as well as the within-removed block. From this fixed sum
delete the scalar subtotal (6), and denote the result by \(\widehat P\).
The fixed-mask bounds give

\[
 \widehat P=\|G_*\|_w^2+O_\varepsilon(X^{2+\varepsilon}).
 \tag{7}
\]

Now form \(V_0\) by (4), over the remaining conductors in \(G_*\), and
put \(G_8=G_*-V_0\). Define the single real quantity

\[
 \boxed{\begin{split}
 Q_8={}&\widehat P+2\operatorname{Re}\langle G_*,C_z\rangle_w
                 +\|C_z\|_w^2\\
       &-2\operatorname{Re}\langle V_0,G_*+C_z\rangle_w
                 +\|V_0\|_w^2.
 \end{split}}
 \tag{8}
\]

Expansion, without a new Fourier assertion about the moving mask, gives

\[
 Q_8-\|G_8+C_z\|_w^2
   =\widehat P-\|G_*\|_w^2=O_\varepsilon(X^{2+\varepsilon}).
 \tag{9}
\]

The triangle inequality applied to (3), \(V_{\rm out}\) and \(V_0\)
also gives

\[
 \|T-(G_8+C_z)\|_w^2\ll_\varepsilon X^{2+\varepsilon}.
 \tag{10}
\]

Consequently the all-epsilon bound for \((Q_8)_+\) is equivalent to the
one for \((Q_7)_+\), on the same sufficiently late dyadic blocks. The
proof uses comparison of amplitudes in norm and the error in (9). It does
not assert an unconditional target-scale additive bound for \(Q_7-Q_8\),
nor apply the original fixed-frequency pair mask directly to \(G_8\).
In particular the mixed term \(-2\operatorname{Re}\langle V_0,C_z\rangle_w\)
and the repeated-prime terms in (2) are retained.

**O.** No bound \((Q_8)_+\ll_\varepsilon X^{2+\varepsilon}\) for the
complete expression has been proved. The complementary time windows,
their mutual interaction and their interaction with \(C_z\) still need
the signed estimate. See [the successor review](REVIEW-FINAL-SUCCESSOR.md).

## 6. Repeated prime squares can be absorbed

**Candidate-D.** There is a separate exact arithmetic regrouping of the
same profile. Let \(T_z(n)\) sum the actual \(t(m)\) restricted to
\(P^+(m)\le z\). This is distinct from the raw \(B_z\). On \(n\le D\)
at most two prime factors, counted with multiplicity, can exceed \(z\).
Using the actual local values of \(t\) gives

\[
 \begin{split}
 T(n)&=\mathcal J_z(n)+\mathcal R_z(n),\\
 \mathcal J_z(n)&=T_z(n)-\sum_{p>z}T(\lfloor n/p\rfloor)
                         -\sum_{z<p<q}T(\lfloor n/(pq)\rfloor),\\
 \mathcal R_z(n)&=-2\sum_{\substack{p>z\\p\equiv1,4\ (5)}}
                               T(\lfloor n/p^2\rfloor).
 \end{split}
 \tag{11}
\]

The unqualified sums here run over both prime classes. Inert repeated
pairs cancel exactly; split repeated pairs retain coefficient minus two.
This is an identity for \(T\), not a change to the fixed correction (2).

Define, for \(\sigma\ge1/2\),

\[
 E_{\sigma,X}(F)=X^{1/2-\sigma}
       \left(\int_X^{2X}|F(u)|^2\frac{du}{u^2}\right)^{1/2}.
\]

The integral uses the usual floor extension. The repeated-pair operator
satisfies

\[
 E_{\sigma,X}(\mathcal R_z)\le\rho_\sigma(X)
       \max_{Y\le2X/z^2}E_{\sigma,Y}(T),\qquad
 \rho_\sigma(X)=2\sqrt{1+2^{2\sigma-1}}
       \sum_{\substack{z<p\le\sqrt{2X}\\p\equiv1,4\ (5)}}p^{-2\sigma},
 \tag{12}
\]

with dyadic \(Y\). For \(\sigma>1/2\) this factor tends to zero. At
the arithmetic critical norm,

\[
 \rho_{1/2}(X)\longrightarrow\sqrt2\log(3/2)<1.
 \tag{13}
\]

All arguments on the right of (12) are smaller than the incoming block,
so an induction absorbs them. In particular, for each fixed
\(\sigma>1/2\),

\[
 (Q_7)_+=O_\sigma(X^{1+2\sigma})
 \quad\Longleftrightarrow\quad
 E_{\sigma,X}(\mathcal J_z)=O_\sigma(1).
 \tag{14}
\]

The transfer uses an error exponent in (3) smaller than \(2\sigma-1\).
The strict contraction at \(\sigma=1/2\) is proved for the exact
arithmetic norm; the inherited error does not give a strict \(O(X^2)\)
Fourier transfer at that boundary.

The regrouping still has a large drift to cancel. The two all-prime sums
together equal
\(\kappa(\log2-1/2)n/(\log n)^2+O(X/(\log X)^3)\),
where \(\kappa=1/U(1)>0\). Their squared norm has order
\(X^3/(\log X)^4\); \(T_z\) has the opposite leading term. The
first-prime coefficient has the same sign in both classes. No separate
absolute estimate of those sectors supplies (14). The full derivation,
the lower-argument induction and the drift are in
[COUPLED-CUTS](COUPLED-CUTS.md).

## 7. Two negative squares and the remaining linear form

**Candidate-D.** The same paper transfers the neighboring large-factor
orientation to the actual inverse \(f=t^{-1}=\mathbf1*u\). Its local
coefficients give \(f(k)\ge0\). Put \(A=\lfloor X^{1/14}\rfloor\),
\(h_A=\sum_{m\le A}t(m)/m\), and \(D_A(v)=T(v)-T(A)\). Define

\[
 \begin{split}
 d_A(n,j)&=\sum_{\substack{a\mid j\\A<a\le n/j}}f(j/a)t(a),\\
 \mathcal L_A(n)&=2\sum_{j\le n/(A+1)}
                       d_A(n,j)D_A(\lfloor n/j\rfloor),\\
 \mathcal S_A(n)&=\sum_{k\le n/(A+1)^2}
                       f(k)D_A(\lfloor\sqrt{n/k}\rfloor)^2\ge0.
 \end{split}
\]

Uniformly throughout the taper,

\[
 \boxed{\ T(n)=\mathcal L_A(n)-nU(1)h_A^2
                         -\mathcal S_A(n)+O(\sqrt X).\ }
 \tag{15}
\]

The two explicit squares have nonpositive signs and all their states
come from this same \(t\). The inverse-weight prefix estimate used in
the proof is

\[
 \sum_{k\le y}f(k)=U(1)y+C_U\zeta(1/3)y^{1/3}+O(y^{5/12}).
\]

Its displayed cubic term lies below its error and is not a resolved
secondary asymptotic. After the short rectangle is summed, its absolute
contribution is \(O(X^{3/7})\), while the remaining error is
\(O(X^{1/2})\). This is why the explicit cutoff in (15) is admissible.

The inherited complete-window one-sided criterion makes
\(\|(\mathcal L_A)_+\|_w^2\ll_\varepsilon X^{2+\varepsilon}\)
sufficient for the full target. That bound remains **O**. The displayed
negative squares alone do not prove it. For a prime
\(A<p\le\sqrt n\), the actual coefficient is \(d_A(n,p)=-1\) in
both classes, and the linear term can evaluate \(T(n/p)\) beyond
\(\sqrt n\). Every state inside the overlap squares is at most
\(\sqrt n\). Any domination must account for this mismatch and for
the signs of the actual prefixes.

## 8. Evidence, ownership and stopping point

The four proof files and seven review records are paper deductions in one
research session. The helpers comprised an Astra for proper divisors and
determinants, a Sol for actual coupled cuts, and a Sol for moving
numerator sums; root supplied the common synthesis and a further paper
audit. The root and lane questions were frozen before authoring. No
scientific numerical, symbolic or formal executable ran in this round.
Repository integrity checks do not verify these analytic arguments.

The neighboring draft [#2093](https://github.com/mathorn1973/twist-j/pull/2093)
was read at `ceb77e3632ec4617c54d8e1fd504d3b1c99dd106`; its complete
thirty-file package and twenty-nine-entry manifest were checked. Its
Möbius factor orientation motivated Section 7. The present inverse
weights and the transfer to the original \(t\) are derived explicitly;
the neighboring owner and its different coefficients are preserved.
External prime-count input and the existing analytic premises are
identified in [SOURCES](../SOURCES.md).

The [root audit](REVIEW-SYNTHESIS.md), individual opposition records and
[promotion handoff](PROMO-C-RH-ARITHMETIC-KERNEL-N.md) specify what was
checked. Same-session review is neither blind confirmation nor independent
external mathematical acceptance. All new conclusions remain candidate-D.
The complete successor (8), the equivalent arithmetic criterion (14) and
the signed profile in (15) leave the complete bound open. The one-sided
linear-form bound in Section 7 is sufficient and remains open. No full
power saving, new RH proof, Canon promotion or physical layer lift is
claimed.
