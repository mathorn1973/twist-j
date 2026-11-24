# Joint signed boundaries and their dependence on the cutoff

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
The identities, diagonal estimate and reconstruction bounds below are
**candidate-D** paper deductions. The required positive energy of the
actual arithmetic residual remains **O**. No novelty or Canon promotion
is asserted.

This completes the paper scope in [SCOPE.md](SCOPE.md). The three author
notes and the separate same-session Astra [review](REVIEW.md) are retained
with their original commits. The root synthesis below uses the reviewed
identities and displays the quantitative obligation that they leave.

## 1. The entry and exit belong to the same signed interval

Let \(M(N)=\sum_{d\le N}\mu(d)\), with \(M(0)=0\). For any prime \(p\),
pair each \(p\)-free squarefree integer \(d\) with \(pd\). Their
coefficients have opposite signs. The exact identity is
\[
 M(N)=\sum_{\substack{d\ge1\\p\nmid d}}
               \mu(d)\mathbf1_{[d,pd)}(N).                    \tag{1}
\]
The contribution enters at \(N=d\) with sign \(\mu(d)\) and exits
at \(N=pd\) with sign \(-\mu(d)\). In particular it is already absent
at the right endpoint. This is a single time-dependent signed carrier,
not a separate estimate for either boundary.

For the original integer window put
\[
 A=Y,\qquad B=\lceil Y^{3/2}\rceil,\qquad
 I(Y)=[A,B)\cap\mathbb Z,\qquad w_N=\frac1{N(N+1)},
\]
where \(Y\ge11\) is an integer. These endpoints also apply if
\(Y^{3/2}\) is an integer. Two intervals \(I_d=[d,pd)\) and
\(I_e=[e,pe)\) have exact weighted overlap
\[
 K_{Y,p}(d,e)=
 \begin{cases}
 L^{-1}-U^{-1},&L<U,\\
 0,&L\ge U,
 \end{cases}
 \quad
 L=\max(A,d,e),\quad U=\min(B,pd,pe).                           \tag{2}
\]
This follows by telescoping the weights on their intersection.
Consequently every term in the squared norm has its actual coefficient
\(\mu(d)\mu(e)\) and its actual time overlap. The entrywise
nonnegative kernel does not give a sign to the sum of mixed terms.
[SIGNED-INTERVALS.md](SIGNED-INTERVALS.md) also writes the two independent
shift sums required after the original forward average.

## 2. The complete diagonal is already logarithmic

Specialize (1) to \(p=2\). On the entire original window,
\[
 E_M(Y):=\sum_{N\in I(Y)}w_N M(N)^2=D_Y+\mathcal C_Y,            \tag{3}
\]
where
\[
 \begin{split}
 D_Y&=\sum_{N\in I(Y)}w_N r_N,\qquad
 r_N=\#\{d:\ d\text{ odd and squarefree},\ N/2<d\le N\},\\
 \mathcal C_Y&=2\sum_{\substack{a<b<B\\a,b\ {\rm odd}}}
                         \mu(a)\mu(b)K_Y(a,b),\\
 K_Y(a,b)&=
 \begin{cases}
 \displaystyle\frac1{\max(A,b)}-\frac1{\min(B,2a)},
       &\max(A,b)<\min(B,2a),\\
 0,&\text{otherwise}.
 \end{cases}
 \end{split}                                                   \tag{4}
\]
In particular a nonzero off-diagonal contribution requires
\(a<b<2a\). Nonsquarefree labels vanish through their Möbius
coefficients. All sums displayed for a fixed window are finite.

Counting all odd integers, without using a prime number estimate,
gives \(r_N\le N/4+1\). Thus
\[
 \boxed{\quad
 0\le D_Y\le\frac14\log(B/A)+\frac1A=O(\log Y).
 \quad}                                                       \tag{5}
\]
Indeed \(\sum_{A\le N<B}(N+1)^{-1}\le\log(B/A)\) and
\(\sum_{A\le N<B}w_N=1/A-1/B\).
The actual diagonal meets the required subpower scale on every
sufficiently late window. This does not bound the off-diagonal sum.
The latter is signed and only the lower bound
\(\mathcal C_Y\ge-D_Y\) follows from (3).

The two-sided quantity gives the sufficient bound
\[
 Q_M(Y):=\sum_{N\in I(Y)}w_N(M(N)_+)^2
       \le D_Y+(\mathcal C_Y)_+ .                              \tag{6}
\]
A subpower bound for \((\mathcal C_Y)_+\) on arbitrarily late original
windows would therefore suffice. This sufficient route is stronger
than merely bounding the requested one-sided energy.

For an exact one-sided reduction keep the genuine sign condition
\(g_N=\mathbf1_{\{M(N)>0\}}\) inside each overlap:
\[
 \begin{split}
 K_{Y,g}(a,b)
   &=\sum_{\substack{N\in I(Y)\\a\le N<2a\\b\le N<2b}}w_Ng_N,\\
 D_{Y,g}&=\sum_{N\in I(Y)}w_Ng_Nr_N,\\
 \mathcal C_{Y,g}
   &=2\sum_{\substack{a<b<B\\a,b\ {\rm odd}}}
                    \mu(a)\mu(b)K_{Y,g}(a,b).
 \end{split}
\]
Expanding at each integer, before summing, proves
\[
 Q_M(Y)=D_{Y,g}+\mathcal C_{Y,g},\qquad 0\le D_{Y,g}\le D_Y,
\]
and hence the particularly precise comparison
\[
 \boxed{\quad
 0\le Q_M(Y)-(\mathcal C_{Y,g})_+\le D_Y.
 \quad}                                                       \tag{7}
\]
If \(\mathcal C_{Y,g}\ge0\), the difference in (7) is \(D_{Y,g}\).
If it is negative, the difference is \(Q_M\), between zero and
\(D_{Y,g}\). This proves both inequalities. The condition \(g_N\)
depends on the same Möbius coefficients as the pair products.
It is not independent sign data and has not been estimated.
Equation (7) isolates the off-diagonal obligation; it does not
establish cancellation in that obligation.

## 3. Both lower exits can be absorbed exactly

The inherited two-factor carrier uses
\[
 C_T(n)=\sum_{a,b>T}\mu(a)\mu(b)
                          \left\lfloor\frac n{ab}\right\rfloor.
 \]
Pairing \(a\) with \(pa\) while retaining this original cutoff gives
an ordinary interval \([kab,kpab)\) for \(a>T\), but a persistent
negative interval \([kpab,\infty)\) for \(T/p<a\le T\).
Dropping the latter changes the carrier.

There is an exact reallocation which absorbs these strips in both
factors. In Dirichlet convolution let
\[
 \nu_p=\mu\mathbf1_{p\nmid d},\qquad e_p=\delta_1-\delta_p,\qquad
 u'=e_p*(\nu_p\mathbf1_{d\le T}),\qquad
 g=e_p*(\nu_p\mathbf1_{d>T}).
 \]
Then \(\mu=u'+g\), \(|u'(d)|\le1\), the support of \(u'\) is
contained in \(d\le pT\), and
\[
                         \sum_d u'(d)=0.                      \tag{8}
\]
The zero is exact, without a bound on \(M(T)\). From
\(\mu*\mathbf1=\delta_1\) one obtains
\[
 \mu=2u'-u'*u'*\mathbf1+g*g*\mathbf1.
 \]
Define \(C_{p,T}\) as the summatory function of \(g*g*\mathbf1\),
put \(h_{p,T}=\sum_d u'(d)/d\), and set
\(\psi_d(n)=\{(n+1/2)/d\}-1/2\). For every integer \(n\ge pT\),
\[
 \boxed{\quad
 M(n)=C_{p,T}(n)-(n+1/2)h_{p,T}^2
            +\sum_{d\le p^2T^2}(u'*u')(d)\psi_d(n).
 \quad}                                                       \tag{9}
\]
The linear short sum and the constant from the small rectangle both
vanish by (8). The negative affine square remains. Thus the new
carrier is not obtained by simply deleting an inconvenient boundary.
Its long coefficients and compensating square change together.

The exact long coefficient combination is
\[
 \begin{split}
 C_{p,T}(n)
 &=\sum_{\substack{a,b>T\\p\nmid ab}}\mu(a)\mu(b)
       \left(\left\lfloor\frac n{ab}\right\rfloor
       -2\left\lfloor\frac n{pab}\right\rfloor
       +\left\lfloor\frac n{p^2ab}\right\rfloor\right)\\
 &=\sum_{\substack{a,b>T\\p\nmid ab}}\mu(a)\mu(b)
       \sum_{k\ge1}\left(
          \mathbf1_{[kab,pkab)}(n)
          -\mathbf1_{[pkab,p^2kab)}(n)\right).
 \end{split}                                                   \tag{10}
\]
Both adjacent pulses, with their signs and dependence on \(n\),
must remain together. The proof and the original lower-strip
formula are in [SIGNED-INTERVALS.md](SIGNED-INTERVALS.md).

## 4. The reconstruction cost stays small for a growing selection

The same construction works with a nonempty finite set \(S_X\)
of primes, fixed throughout a slab \([X,2X)\). Put
\[
 P_X=\prod_{p\in S_X}p,\quad e_{S_X}=\sum_{s\mid P_X}\mu(s)\delta_s,
 \quad \nu_{S_X}=\mu\mathbf1_{(\cdot,P_X)=1},\quad
 T_X=\lfloor X^{1/4}\rfloor.
 \]
Use \(u'=e_{S_X}*(\nu_{S_X}\mathbf1_{d\le T_X})\) and
\(g=\mu-u'\). Uniqueness of the selected-prime part and coprime
core gives \(|u'|\le1\), support at most \(P_XT_X\), and
\(\sum u'=0\). For \(n\ge P_XT_X\), the same identity (9) holds
with these coefficients, their own \(h'_X=\sum_d u'(d)/d\), and
their own long sum \(C'_X\).

Write the original averaging operator as
\(U_X f(N)=\sum_s\lambda_{X,s}f(N+s)\), and keep
\[
 L_X(N)=N+\tfrac12+\sum_s s\lambda_{X,s}
       =N+\tfrac12+J(H-1)/2,\qquad
 Z'_X=U_X C'_X-L_X(h'_X)^2.
 \]
The weights and shifts are precisely those of the inherited carrier.
In the range \(P_XT_X\le X^{1/3}\), every averaged argument is at
least \(P_XT_X\). The small rectangle has support
\(d\le(P_XT_X)^2\) and coefficients bounded by \(\tau(d)\).
The inherited short raw-denominator estimate therefore yields
\[
 \|U_XM-Z'_X\|_X^2
 \ll\frac{(X+(P_XT_X)^4)(P_XT_X)^2}{X^2}
                                         (1+\log X)^3,
 \]
 \[
 \boxed{\quad
 \|U_XM-Z'_X\|_X
 \ll P_X^3X^{-1/4}(1+\log X)^{3/2}.
 \quad}                                                       \tag{11}
\]
Here \(\|f\|_X^2=\sum_{X\le N<2X}w_N|f(N)|^2\).
The constants in the displayed support-based estimate are uniform
for the selections under consideration. The proof uses coefficient
mass, frequency separation and convexity of the given average.
It does not use a full-line norm of the actual Möbius prefix.

For fixed \(0<\delta<1/12\), the budget
\[
                         P_X\le X^{1/12-\delta}                \tag{12}
\]
makes (11) at most \(O(X^{-3\delta}(1+\log X)^{3/2})\).
For example, selecting every prime at most \(\kappa\log X\), with
fixed \(0<\kappa<1/12\), meets such a budget eventually because
\(\log P_X=\kappa\log X+o(\log X)\) by the prime number theorem.
The prime selection can thus grow while the reconstruction error
still saves a power.

Sum the squared errors on all slab intersections with \(I(Y)\),
including its two outer fragments. Their geometric decrease gives
\[
 \|U M-Z'\|_{I(Y)}
       \ll_\delta Y^{-3\delta}(1+\log Y)^{3/2}.
 \]
Using the inherited maximal short-sum comparison of \(UM\) with
\(M\), and the inherited comparison of \(M\) with \(R=R_{1/36}\),
then proves, for every fixed \(K>0\),
\[
             \boxed{\quad
 \|Z'-R\|_{I(Y)}\ll_{\delta,K}(\log Y)^{-K}.
             \quad}                                          \tag{13}
\]
This holds on every sufficiently late complete original window.
It sharpens the coarse comparison in the prime-scale author note;
the uniform proof is recorded in [REVIEW.md](REVIEW.md).
The source for the small rectangle and the two inherited comparisons
is the pinned [full coupled-energy note](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md).
The positive-part map is 1-Lipschitz, so (13) also bounds the
difference of the square roots of the positive energies. It is an
error estimate between carriers, not an estimate of their energy.

## 5. What the cube and harmonic ranks recover

For unit weights in a fixed divisor cube with least prime \(p\),
the paired subcomplex on labels \(d,pd\) contracts in the \(p\)
direction. The remaining homogeneous cycles, indexed by \(p\)-free
squarefree \(d\), are born at \(d\) and die at \(pd\).
The rank of their inclusion from \(N\) to \(M\ge N\), in each
parity, counts the corresponding labels in \(M/p<d\le N\).
[MIXED-BOUNDARIES.md](MIXED-BOUNDARIES.md) proves this with explicit
cycles and states the fixed-list and weight assumptions. The
single-cut counts agree with Björner's Theorems 2.1 and 3.1.

For \(p=2\), when the fixed list contains every prime through the
larger cutoff in the comparison, the total rank at one cutoff
is exactly \(r_N\) in (3). Across two cutoffs the sum of the two
parity ranks recovers
the diagonal in the product of the two signed interval sums.
The difference of those ranks instead equals the coefficient
of \(c_p^4\) in the mixed graded defect trace.
The pairs of distinct labels in (4) remain outside this diagonal.

Mixed traces and products of traces cannot be interchanged. For
example the harmonic inclusion from \(N=1\) to \(M=3\) at \(p=2\)
is zero, while the product of the arithmetic indices is \(-1\).
The product of scalar readouts uses a tensor of two defects;
the mixed matrix trace contracts a common intermediate label.
The unrestricted tensor trace has exact Hilbert-Schmidt dual cost
\(\sqrt{d_Nd_M}\) in dimensions \(d_N,d_M\). Moving to harmonic
space does not remove an order-\(N\) dimension at a single ordinary
cutoff. These are readout costs and rank statements, not lower
bounds on the actual residual energy.

The geometric correspondence therefore identifies which part of
the energy is controlled by counting persistent labels. That part
is already bounded in (5). A useful further estimate must also
control the actual signed interactions of different labels.

## 6. Actual prime sectors show why the signs must stay together

For the selection \(S=\{2,3\}\), the contribution of prime coprime
cores to the exact one-factor filtered sum is
\[
 -\pi_{>3}(x)+\pi_{>3}(x/2)+\pi_{>3}(x/3)-\pi_{>3}(x/6)
          \sim-\frac{x}{3\log x}.
 \]
The unit and composite coprime cores supply the opposite leading
term \(+x/(3\log x)\), using the inherited classical estimate for
\(M(x)\). These are actual arithmetic sectors, not freely chosen
test sequences. The latter sector alone has positive energy at
least order \(Y^{3/2}/(\log Y)^2\) on each late complete window.
Their leading cancellation does not provide the subpower remainder
needed in (7) or (13).
[PRIME-SCALE-CANCELLATION.md](PRIME-SCALE-CANCELLATION.md) gives
the exact pulse identities and this asymptotic.

That note also computes the exact two-sided inverse filter norm
\(\prod_{p\in S}(1-p^{-1/2})^{-1}\) on the full critical logarithmic
line. A finite-window inverse requires translated windows, and a
one-sided forward bound has no such generic local consequence.
The growing reallocation bound (11) avoids that inverse argument.
The neighboring split-prime contraction uses a different sequence
of coefficients and is not imported as a Möbius estimate.

## 7. The remaining estimate is explicit

**O.** The original target still fixes \(R=R_{1/36}\) and asks:
for every integer \(q\ge1\) and every starting cutoff \(Y_0\),
there is an integer \(Y\ge\max(11,Y_0)\) such that
\[
     Q_R(Y)^q\le Y,\qquad
     Q_R(Y)=\sum_{N\in I(Y)}w_N(R(N)_+)^2 .
 \]
By (7), its logarithmic diagonal bound, and the inherited full
norm comparison of \(M\) with \(R\), the all-exponent criterion
is equivalent to the corresponding subpower criterion for
\((\mathcal C_{Y,g})_+\). One uses a smaller exponent to absorb
the logarithmic diagonal and the square-root energy error.
The ungated upper bound in (6) remains a sufficient, stronger route.

Equivalently, one may work with the reallocated carrier and its
exact positive dual
\[
 \sqrt{Q_{Z'}(Y)}
   =\sup_{\substack{f_N\ge0\\\sum_{N\in I(Y)}w_Nf_N^2\le1}}
                       \sum_{N\in I(Y)}w_N f_N Z'(N).
 \]
Equation (10) or its multi-prime version must enter this single
sum with every sign, every shift and its compensating square.
The comparison (13) preserves the same complete windows and
the original quantifiers.

The proved progress is a joint signed time representation, exact
absorption of both lower strips, a uniform reconstruction budget,
and a logarithmic bound for the full diagonal. There is still no
subpower upper bound for the signed off-diagonal interaction or
for the displayed positive dual supremum. Repository checks and
the same-session paper review do not change that scientific status.
