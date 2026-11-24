# Concentration through arithmetic reduction and four-dimensional quotients

**NON-CANONICAL. No authority or Canon status change. Paper deductions are candidate-D.**

Any four of the five translates of one rational subspace by a primitive fifth root form a balanced family on a four-dimensional cyclotomic field. This holds for subspaces of every dimension, including planes. One missing translate has zero cost. The result gives an upper bound on the defect of a fixed integer matrix family from data at a single inert prime. In higher dimension the test can be applied on successive four-dimensional quotients, even when no word image splits across the quotients. For the arithmetic cut of the actual period family, a modular upper bound transfers back to the full maps at a cost given by the larger discarded source or target fraction. The required graded-image data and the resulting actual concentration estimate remain **O**.

## 1. The four-translate theorem

**Candidate-D.** Let $k$ be either $\mathbb Q$ or $\mathbb F_q$ for a prime $q\equiv2,3\pmod 5$. Let $K=k[t]/(1+t+t^2+t^3+t^4)$, a field of degree four. For the finite fields the degree follows from the order four of $q$ modulo five. Over $\mathbb Q$ the shifted polynomial is Eisenstein at five. Write $t$ also for the image of the variable. For every $k$-subspace $U\le K$, every four-element set $I\subset\mathbb Z/5$, and every $k$-subspace $W\le K$,
$$
 \sum_{i\in I}\dim(t^iU\cap W)\ \le\ (\dim U)(\dim W).                 \tag{15.1}
$$
After scalar extension, (15.1) holds for **all** subspaces $W$ of the extended target, with the original $k$-defined $U$ extended along with it. In particular a rational model gives the complex inequality directly. Section 3 proves this extension step.

**Proof over $k$.** For any nonzero $v\in K$, any four of the five $t^iv$ form a basis. The only relation between the five powers, up to a scalar, is their sum. The same assertions hold for $t^a$ when $a\ne0\pmod5$. They also hold on the dual for inverse-transpose multiplication by $t$. Its minimal polynomial is the same irreducible quartic, so every nonzero covector is cyclic. Write $d=\dim U$ and $w=\dim W$. If either dimension is zero or four, the assertion follows directly.

If $d=1$, distinct translates are independent up to size four, so at most $w$ of the four lines lie in $W$. If $w=1$, at most $d$ of the inverse-translated lines lie in $U$. Annihilators give
$$
 \dim(t^i U\cap W)=d+w-4+\dim((t^i U)^\circ\cap W^\circ).
$$
Here $(t^i U)^\circ$ is the $i$th translate of $U^\circ$ under inverse-transpose multiplication. The desired bound is invariant under $(d,w)\mapsto(4-d,4-w)$ by the displayed identity summed over four indices. This settles either dimension three.

It remains to take $d=w=2$. The five translates of $U$ are distinct because no proper nonzero subspace is invariant under $t^a$ for $a\ne0\pmod5$. If $W$ equals none of the four translates, every intersection has dimension at most one. If $W=t^s U$ is selected, translate back to $U$. Whenever $U\cap t^aU\ne0$ with $a\ne0$, the plane contains $v,t^av$ for some $v\ne0$, hence equals $v\langle1,t^a\rangle$. Its intersection with $t^{2a}U$ is zero by independence of $1,t^a,t^{2a},t^{3a}$. Its intersection with $t^{-2a}U$ is also zero by translating. Among the other four planes, only the two indexed by $\pm a$ can meet it. The total is at most $2+1+1=4$, as required.

## 2. Unequal multiplicities, missing words and changed images

**Candidate-D.** Give $t^i U$ multiplicities $n_i\ge0$, put $N=\sum_i n_i>0$, $p_i=n_i/N$, and define
$$
 h(p)=\sum_i (p_i-1/4)_+,\qquad
 b(d,w)=\min(d,w,4-d,4-w).
$$
The $n_i$ may be nonnegative rational weights. Then
$$
 \sum_i n_i\dim(t^iU\cap W)
 \le N\left(\frac{dw}{4}+b(d,w)h(p)\right).                         \tag{15.2}
$$
If every $p_i\le1/4$, write $p$ as a convex combination of the uniform four-member distributions with weights $1-4p_i$ on the distributions omitting $i$. They sum to one and give coordinate $p_i$. Equation (15.1) proves (15.2) with zero cost. This includes a uniformly weighted full orbit and every uniformly weighted four-member subset, even though the latter need not be invariant under multiplication by $t$.

In general move the excess above $1/4$ into coordinates below $1/4$ until no excess remains. Total receiving capacity exceeds the amount to move since the five caps sum to $5/4$. The mass moved is $h(p)$. At given $d,w$, each intersection dimension lies between $\max(0,d+w-4)$ and $\min(d,w)$, whose difference is $b(d,w)$. Applying the proved bound to the modified weights proves (15.2). For a line $U$ the maximum over $W$ of $\sum_i p_i\dim(t^iU\cap W)-w/4$ is **exactly** $h(p)$. For $h(p)>0$ take the span of the overweight lines. There are at most three, and no other orbit line belongs to that span by four-wise independence. For $h(p)=0$ take $W=0$. Thus the cap $1/4$ is sharp uniformly in $U$. Three distinct equally weighted lines have excess $1/4$, while four have zero.

For an actual word image $X$ matched to a template $Y=t^iU$ of the same dimension,
$$
 \dim(X\cap W)\le\dim(Y\cap W)+\dim X-\dim(X\cap Y).                  \tag{15.3}
$$
The quotient of $X\cap W$ by $X\cap Y\cap W$ injects into $X/(X\cap Y)$. A word that admits no chosen match, of dimension $d$ in a layer of dimension $n$, instead satisfies
$$
 \dim(X\cap W)-\frac{d\,\dim W}{n}\le \frac{d(n-d)}n.                 \tag{15.4}
$$
Indeed the left side is bounded by $\min(d,w)-dw/n$, maximized at $w=d$. This cost is attained by $W=X$. All these charges measure dimensions and word multiplicities in the original arrangement.

## 3. The field of the maximizer and specialization

**Candidate-D.** For a finite list of subspaces $J_u\le F$ over a number field $k$ or a finite field, consider any functional
$$
 H(W)=\sum_u c_u\dim(J_u\cap W)-a\dim W,\qquad c_u\ge0.
$$
It has the same maximum over $k$, its algebraic closure and every extension field. The canonical largest maximizing subspace over the algebraic closure descends to $k$.

For fixed $\dim W$ and integers $s_u$, the conditions $\dim(J_u\cap W)\ge s_u$ are determinantal on the Grassmannian. Indeed they bound the ranks of the quotient maps $W\to F/J_u$. On a matrix chart these are vanishing minors with coefficients in $k$. If the conditions hold over an extension, the corresponding affine chart equations have a solution over an algebraic closure of $k$, by the weak Nullstellensatz. Take the $s_u$ from a maximizing witness. Nonnegative weights then give at least its value at the algebraic point.

Over the algebraic closure, $H$ has a unique largest maximizer. Its values lie in a finite set, and the intersection-dimension formula gives $H(V)+H(W)\le H(V+W)+H(V\cap W)$. The sum of two maximizers is again a maximizer. A maximizer of largest dimension therefore contains them all. Galois conjugation preserves the rational data and fixes this largest subspace. Its unique reduced row echelon basis is consequently fixed, entry by entry. Both classes of fields are perfect, with fixed field $k$ in their algebraic closure, hence this basis is defined over $k$. This proves the claim. It also proves the geometric assertion of (15.1) and all weighted versions above, despite the splitting of the quartic after base extension.

An invertible group acting on a finite-dimensional $k$-target and permuting a weighted image list with its weights fixes the canonical maximizing subspace. If the representation is irreducible **over $k$** and the list is $k$-defined, choosing $a=\sum_u c_u\dim J_u/\dim F$ forces $H(W)\le0$ geometrically. Both endpoints have value zero. If the representation has multiplicity, a proper invariant subspace can remain. For example, on $K^2$, take every image to be $K\oplus0$. The exact order-five symmetry holds, yet an injective family of inclusions of that subspace has defect $1/2$. The four-translate assertion on a single copy uses the extra cyclotomic incidence calculation, so it also covers the incomplete orbit.

For integral matrices $A_u:\mathbb Z^{r_u}\to\mathbb Z^D$ put $R=\sum r_u>0$, $D>0$ and define
$$
 \epsilon(A)=\max_{W\le F}\left(\frac{1}{R}\sum_u\dim A_u^{-1}(W)-\frac{\dim W}{D}\right).
$$
Then at **every** prime $q$,
$$
 \epsilon_{\mathbb C}(A)\le \epsilon_{\mathbb F_q}(A\bmod q)
                         = \epsilon_{\overline{\mathbb F}_q}(A\bmod q). \tag{15.5}
$$
The defect is the preceding functional with $c_u=1/R,a=1/D$, plus the normalized kernel sum. Choose its rational maximizing $W$ by descent. The lattice $W\cap\mathbb Z^D$ is saturated and spans $W$ over $\mathbb Q$. Its reduction $\bar W$ has dimension $\dim W$ because a saturated sublattice is a direct summand. For each $u$ the saturated lattice $A_u^{-1}(W)\cap\mathbb Z^{r_u}$ reduces with its full rank into $(\bar A_u)^{-1}(\bar W)$. This gives (15.5) even at primes where a word loses rank.

A sharper version uses the saturated image lattices $L_u=(\operatorname{im} A_{u,\mathbb Q})\cap\mathbb Z^D$. Write $\tilde J_u=L_u\bmod q$ as a subspace of $\mathbb F_q^D$ and $\kappa=\sum_u(r_u-\operatorname{rank}_{\mathbb Q}A_u)/R$. Then
$$
 \epsilon_{\mathbb C}(A)\le
 \kappa+\max_{W\le\mathbb F_q^D}
       \left[\frac1R\sum_u\dim(\tilde J_u\cap W)-\frac{\dim W}{D}\right]. \tag{15.6}
$$
Use the same rational maximizer. Each saturated lattice $L_u\cap(W\cap\mathbb Z^D)$ reduces with unchanged dimension inside $\tilde J_u\cap\bar W$. The generic kernel term stays fixed. The saturated image dimension equals the rational rank, including when the literal reduced matrix loses rank. The right side of (15.6) is at most the right side of (15.5): enlarging the literal image by $s$ dimensions raises any intersection by at most $s$ and lowers the associated kernel term by $s/R$ after normalization. The same proofs apply over a number field at any nonzero prime ideal: localize its ring of integers at that ideal, take a common free target lattice and use saturated intersections there. Over this discrete valuation ring every saturated submodule of a finite free module is a direct summand. Equation (15.5) uses maps integral between the chosen free source and target lattices. For (15.6), saturated intersections with the target lattice suffice. The residue field replaces $\mathbb F_q$ and its size can exceed the rational prime $q$. More generally the argument needs only a common rational model of the image arrangement with the given source dimensions, up to a common target isomorphism. Integral entries of an unrelated matrix family give no such model.

**Candidate-D, fixed-instance equality.** For a fixed number-field tuple of matrices, after clearing the finitely many denominators, the inequalities in (15.5) and (15.6) are equalities at all but finitely many prime ideals. Here is a proof for the literal maps. For $0\le w\le D$ and $0\le s_u\le r_u$, impose $\dim A_u^{-1}(W)\ge s_u$ and $\dim W=w$. The first conditions are rank bounds $\operatorname{rank}(E_u\to F/W)\le r_u-s_u$. They cut out a closed locus on the relative Grassmannian of $w$-planes by minors. If $\sum s_u/R-w/D$ exceeds the geometric generic defect, this locus has empty geometric generic fibre. Cover the Grassmannian by its finitely many standard affine matrix charts. On each chart the minor equations generate the unit ideal over the fraction field, by the weak Nullstellensatz. Clearing the finitely many denominators of one polynomial identity for the unit yields a nonzero constant in the integral ideal of minors on that chart. Away from the prime divisors of these constants the locus has empty fibre. There are only finitely many $w$ and lists $(s_u)$, hence outside a finite set no larger value can occur. Combine with (15.5) and the intermediate bound (15.6). The exceptional set depends on the entire tuple; there is no family-uniform choice of prime or upper bound on its size in this argument.

**Candidate-D, restriction of scalars.** If $l/k$ is a finite extension of degree $f$, viewing the whole $l$-linear arrangement over $k$ preserves its normalized defect. Each $l$-subspace remains a test space and the source and target dimensions all scale by $f$. Conversely the largest $k$-maximizer exists by the sum argument above over $k$ itself. Every $c\in l^\times$ preserves all word images, so multiplication by $c$ fixes the largest maximizer. This makes it an $l$-subspace and its two normalized values coincide. For the finite or number fields in use, the descent argument already equates each base-field maximum with its geometric value. The same argument applies to the saturated image formula using the given source dimensions and kernel fraction.

For a prime $q\equiv2,3\pmod5$ and residue field $l=\mathbb F_{q^f}$, the quartic is irreducible over $l$ exactly when $\gcd(f,4)=1$, since the order of $q^f$ modulo five is $4/\gcd(f,4)$. In every residue degree, restriction to $\mathbb F_q$ allows the quartic certificate on flags in the **$fD$-dimensional** target with total source dimension $fR$. This changes the field and the dimensions together. It still requires the actual graded images to have the stated translates and masses. In particular multiplication by a coefficient-field scalar preserves each $l$-linear image and in general supplies no orbit of distinct word images.

## 4. A certificate on successive quotients

**Candidate-D.** Work over either base field above. On a $D$-dimensional target fix any flag $0=F_0<F_1<\cdots<F_m=F$. Write $G_a=F_a/F_{a-1}$ and $D_a=\dim G_a$. For a subspace $S$ let $S_a$ be the image of $S\cap F_a$ in $G_a$. Use for $J_u$ the actual image in the chosen field or, in (15.6), its saturated reduction. Put
$$
 X_{u,a}=(J_u)_a,\qquad N_a=\sum_u\dim X_{u,a}.
$$
Suppose for each layer there is a number $E_a\ge0$ such that for every $L\le G_a$,
$$
 \sum_u \dim(X_{u,a}\cap L)\le (N_a/D_a)\dim L+E_a.
$$
Then the normalized concentration defect satisfies
$$
 \boxed{\displaystyle
 \epsilon\le\kappa+\sum_a\left(\frac{N_a}{R}-\frac{D_a}{D}\right)_+
                         +\frac1R\sum_a E_a .}                          \tag{15.7}
$$
On each layer $(J_u\cap W)_a$ injects into $X_{u,a}\cap W_a$. The dimensions of the graded pieces of a subspace sum to its dimension. Summing the layer inequalities and using $0\le\dim W_a\le D_a$ proves (15.7). In (15.6) the same right side bounds the complex defect of the original family. The proof only uses the flag and induced subspaces. The images may be nonsplit extensions across the layers.

For each layer of dimension four identify $G_a$ with $K$ by one $k$-linear isomorphism. Divide its nonzero word pieces into disjoint lists matched to quartic templates of fixed dimensions within each list, and unmatched pieces. For a template list $b$, record its multiplicity $N_b$, seed dimension $d_b$, and proportions $p_b$ on the five translates. Equations (15.2)–(15.4) supply the following explicit choice:
$$
 E_a=\sum_b N_b\min(d_b,4-d_b)h(p_b)
   +\sum_{\rm matched}\big(\dim X-\dim(X\cap Y)\big)
   +\sum_{\rm unmatched}\frac{\dim X\,(D_a-\dim X)}{D_a}.              \tag{15.8}
$$
Zero and full pieces are balanced by themselves. Layers of any other dimension may use an independently established bound or only the last sum, treating all their pieces as unmatched. Thus a residue dimension outside multiples of four has an explicit cost. With exact capped matches, the whole orbit term and all replacement charges vanish. In particular if $N_a/R\le D_a/D$ on each layer and $E_a=0$, (15.7) yields $\epsilon=\kappa$ since $W=0$ attains $\kappa$. The counts $N_a$ are actual graded-image dimensions. A decomposition of the target as an abstract vector space into four-dimensional pieces imposes no balance on them.

### Computing a layer bound without an orbit

**Candidate-D.** For an arbitrary list of $m$ word pieces in a four-dimensional layer, the least permissible $E_a$ is determined by matrix ranks and tests of a single quadratic form. This applies when no cyclotomic matching has been proved. For example, four lines are balanced exactly when their four generators are independent. Dually the same holds for the annihilator lines of four hyperplanes. Four planes $U_1,\dots,U_4$ are balanced exactly when every triple has zero intersection, every triple spans the layer, and $\sum_i\dim(U_i\cap U_j)\le4$ for each $j$. A line test gives the first condition, and a hyperplane test gives the second because every plane meets a hyperplane in at least a line. A plane distinct from every $U_i$ contributes at most four in total, and the other plane tests give the third condition. These tests allow arbitrary repeated words.

The appendix gives the exact finite test for an arbitrary list of mixed-dimensional pieces.

## 5. A two-sided bound for a source and target cut

**Candidate-D.** Let $A_u:E_u\to F$ be a full family with total source dimension $R_0>0$ and target dimension $D>0$. Choose subspaces $E'_u\le E_u$ with total dimension $R>0$ and a common quotient $\pi:F\to F'$ with $n=\dim F'>0$. Set $B_u=\pi A_u|_{E'_u}$, $\alpha=R/R_0$, $\beta=n/D$, and $a=\max(1-\alpha,1-\beta)$. Then
$$
 \boxed{\big|\epsilon(A)-\alpha\epsilon(B)\big|\le a.}                \tag{15.9}
$$
For $W\le F$ of dimension $w$, $A_u^{-1}(W)\cap E'_u\subseteq B_u^{-1}(\pi W)$. Restriction loses at most $\dim E_u-\dim E'_u$ source dimensions. Writing $\Phi_A$ for the full normalized defect at a test space gives
$$
 \Phi_A(W)\le(1-\alpha)+\alpha\epsilon(B)+\alpha\min(w/n,1)-w/D .
$$
The last two dimension terms after $\alpha\epsilon(B)$ attain their maximum $(\alpha-\beta)_+$ at $w=n$ or $w=0$. Hence $\epsilon(A)\le a+\alpha\epsilon(B)$. Conversely for $L\le F'$ one has $B_u^{-1}(L)\subseteq A_u^{-1}(\pi^{-1}L)$, with $\dim\pi^{-1}L=D-n+\dim L$. Therefore
$$
 \alpha\Phi_B(L)\le\epsilon(A)+(1-\beta)+(\beta-\alpha)\dim L/n
                 \le\epsilon(A)+a.
$$
This proves (15.9), including nonzero kernels in either family. In particular a certified upper bound $U$ on the defect of the arithmetic cut gives $a+\alpha U$ on the full complex family whenever the stated common quotient, per-word source inclusions and cut identification hold. Separate right isomorphisms, one common left isomorphism, nonzero word scalars and simultaneous coefficient conjugation preserve the defect. A separate left transformation for each word need not do so.

## 6. Arithmetic scope

**Candidate-D, comparison only.** In the supplied Jacobian example the odd inert prime $q$ is the characteristic of the special fibre. The Frobenius isogeny $\pi_q$ satisfies $\pi_q j=j^q\pi_q$ and $\pi_q^4=[-q^2]$ there. Galbraith and Pujolàs compute the rational geometric endomorphism algebra of the Jacobian, of dimension sixteen. In a representation by matrices over a field of characteristic $q$ with the same scalar relation, the fourth power would be zero, so this relation cannot furnish an invertible four-cycle there. The coefficient-field automorphism $x\mapsto x^q$ on $\mathbb F_{q^4}$ has fourth power the identity. Its fixed line $\mathbb F_q\,1$ alone can support a Frobenius-invariant family of defect $3/4$. The operator in (15.1) is **multiplication by $t$**, of order five. The finite-field Frobenius guarantees the quartic degree at inert primes and permutes the four roots. It is not the Jacobian isogeny acting on the word images. [Galbraith and Pujolàs, Section 3, especially Corollary 3.6](https://www.math.auckland.ac.nz/~sgal018/jordi-paper.pdf#page=5)

**Candidate-D for the genuine arithmetic cut.** Under the source's lattice, rationality and Bessel identification hypotheses, the number-field map $B_k$ and the good-row block of $B_f V_r$ have the same complex defect. The target change is common to all words. The column changes and nonzero factors may depend on the word. With the common local target lattice and a coefficient prime $w$, write $U_w$ for either the literal residual defect from (15.5), or the sharper saturated right side of (15.6) retaining the cut's generic kernel fraction. The full complex period map consequently satisfies
$$
 \epsilon(P)\le \max(1-R/R_0,1-n/D)+(R/R_0)U_w .
$$
Only the arithmetic cut needs the number-field model for this argument. In particular a prime-power word factor can erase a literal reduced image without erasing its saturated reduction. The source's own inert valuations concern its named local data, and the source does not guarantee that every reduced word vanishes. [Pinned arithmetic cut and its lattice hypotheses](SOURCE.md) · [Full-space period witness](../PROOF.md#1-scope-notation-and-the-exact-source-bridge)

**O for the actual concentration estimate.** No bound of the required size on $U_w$ is proved here. The word images on the cut have not been shown to furnish the quartic matches or the alternative incidence counts of Section 4. A direct test on the uncut $B_f$ or $P_u$ would require either a common arithmetic model or control of the actual complex images, for example by proving the layer bounds over $\mathbb C$. The earlier complex diagonal estimate bounds the full generic kernel term under its hypotheses. It gives no modular orbit identities. A bound on the Möbius sum does not follow from the Jacobian Frobenius comparison. [Actual kernel estimate](../round9/PROOF.md) · [Unaveraged periods and ranks](../round12/PROOF.md#7-exact-consequence-for-concentration) · [Previous mixed-subspace bound](../round14/PROOF.md#4-the-error-from-testing-split-subspaces)

## Appendix. Arbitrary incidences on a four-dimensional layer

**Candidate-D.** Here is an exact procedure for mixed dimensions and multiplicities. It computes the geometric maximum of $\sum_u\dim(X_u\cap L)-(N_a/4)\dim L$, which equals its base-field maximum by Section 3. Fix first $\dim L=2$. In a chosen basis put $p=[v\wedge w]\in\mathbb P^5$ for $L=\langle v,w\rangle$. The possible $p$ are exactly the zeros of
$$
 p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0.
$$
Indeed on a chart with $p_{12}\ne0$, normalize $p_{12}=1$. The first two columns of a two-row basis matrix may be taken as the identity, the next four minors determine its remaining entries, and the last minor is precisely the displayed relation. Relabeling coordinates covers all charts. This proof also works in characteristic two.

For a threshold $\dim(X\cap L)\ge s$, remove any automatic or impossible conditions. The remaining predicates are systems of homogeneous **linear** equations in the six coordinates of $p$.

| Word piece $X$ | Threshold | Linear condition |
|---|---|---|
| Line spanned by $x$ | $s=1$ | $x\wedge p=0$ |
| Plane with two-vector $z$ | $s=1$ | $z\wedge p=0$ |
| Same plane | $s=2$ | $p$ and $z$ are proportional |
| Hyperplane $\ker \lambda$ | $s=2$ | Contraction $\iota_\lambda p=0$ |

For instance $\iota_\lambda(v\wedge w)=\lambda(v)w-\lambda(w)v$, which vanishes exactly when both vectors are in the hyperplane. The thresholds for a zero or full word piece are constant. Dimension is the sum of the indicators of its positive integer thresholds.

Collect the scalar linear forms occurring in the table for all words. Examine the common kernels $H\subset k^6$ obtained by choosing at most five independent forms, including the empty choice. In the projectivization of $H$ a geometric two-plane exists whenever $\dim H\ge2$: a quadratic form on any two-dimensional subspace has a projective zero over an algebraically closed field, including when the restriction vanishes identically. If $\dim H=1$, substitute its generator into the displayed quadratic. For each feasible kernel count the automatic thresholds and the thresholds whose entire linear system vanishes identically on $H$. Every geometric witness in this kernel attains at least that count. Conversely, for a maximizing point $p$, the span of **all** table forms vanishing at $p$ has dimension at most five. A basis of such forms produces an enumerated kernel, and every true threshold at $p$ is counted there. Taking the maximum gives exactly the true intersection sum.

For $\dim L=1$ in $\mathbb P^3$ the positive threshold is membership of its generator in $X$, a linear system. Use the same construction with at most three independent forms and all nonzero kernels feasible. For $\dim L=3$, apply the line test to $L^\circ$ against the annihilators $X^\circ$ and use $\dim(X\cap L)=\dim X-1+\dim(X^\circ\cap L^\circ)$. The endpoints are immediate. Subtraction of $(N_a/4)\dim L$ and maximization over the five dimensions now gives the exact layer error. There are $O(m^5+1)$ candidate kernels in the middle dimension since each word contributes a bounded number of forms. This counts kernels to test; scoring one kernel may read the entire word list. Feasibility here is geometric. Directly requiring each feasible kernel to contain a rational quadric point could discard valid incidence patterns prior to maximizing. No implementation or numerical application is part of this round.
