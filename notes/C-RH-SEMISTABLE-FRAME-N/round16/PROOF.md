# Repairing a saturated reduction at a prescribed coefficient prime

**NON-CANONICAL. No authority. All deductions below are candidate-D. The quantitative bound for the actual periods remains O.**

Round 15 gave an upper bound for a complex period cut by reducing its saturated images in one common target lattice. A collision modulo the coefficient prime can make that bound too large. The theorem below decides by one linear system on the next digit of the primitive image coordinates whether a specified change of target lattice strictly improves the bound. Repetition attains the characteristic-zero defect at every prescribed coefficient prime. The number of changes can be arbitrarily large, even for two primitive lines in a target of dimension two.

Elementary modification along a destabilizing subspace belongs to the tradition of Langton's semistable reduction. Belmans, Damiolini, Franzen, Hoskins, Makarova and Tajakka prove semistable extension for quiver representations over the original discrete valuation ring when the generic representation is semistable. General semistable reduction for stacks and algorithms for quiver semistability and extremal subrepresentations are also established subjects. The proof here concerns the original normalized defect, arbitrary kernels, one common target lattice and a first-order test for a strict decrease. We give an elementary proof for this setting and make no historical priority claim. [Belmans et al., Proposition 5.6.2 in the author preprint](https://www.math.ru.nl/~vhoskins/GMS_quivers.pdf#page=31), [published version, 2026](https://doi.org/10.2140/ant.2026.20.747) · [Alper, Halpern-Leistner and Heinloth, §5.1](https://pi.math.cornell.edu/~danielhl/Existence_of_good_moduli_spaces_2018_07_19.pdf#page=25) · [Iwamasa, Oki and Soma, §§1–3](https://doi.org/10.4230/LIPIcs.ICALP.2025.99)

## 1. One change of lattice

**Candidate-D.** Let $B_u:E_u\to F$ be a finite family over a number field $L$. Put $D=\dim F>0$, $R=\sum_u\dim E_u>0$, $J_u=\operatorname{im} B_u$, and $\kappa=\sum_u\dim\ker B_u/R$. Fix any coefficient prime, write $K$ for the completion of $L$, $O$ for its valuation ring, $\pi$ for a uniformizer and $k$ for its finite residue field. Extend the images to $K$. For a common target lattice $\Lambda$, put $M_u=J_u\cap\Lambda$, $S=\Lambda/\pi\Lambda$ and $S_u=M_u/\pi M_u\subseteq S$. The inclusion uses saturation. Define
$$
 h(T)=\frac1R\sum_u\dim(S_u\cap T)-\frac{\dim T}{D},\qquad
 H(\Lambda)=\max_{T\le S}h(T),\qquad U(\Lambda)=\kappa+H(\Lambda).
$$
The complex defect satisfies $\epsilon(B)\le U(\Lambda)$ by saturated specialization. This also holds for a lattice in the completion: a generic maximizing subspace over $L$ extends to $K$, and its intersections with the common lattice reduce with their full ranks. Field extension preserves the geometric maximum as in round 15, §3. The denominator is the original $R$, including all word kernels. In particular $h(S)=-\kappa$.

The function $h$ is supermodular, by applying the dimension formula to $S_u\cap T$ for each word. Its maximizers are closed under sum and intersection. Write $V$ for their smallest and $W$ for their largest member. Both are defined over $k$, and the maximum equals its geometric value by round 15. Replace the common target lattice by
$$
 \Lambda'=\{x\in\Lambda:x\bmod\pi\Lambda\in W\}.
$$
Compute every new word lattice by saturation in this *same* target. Set $Q=S/W$, $X_u=S_u\cap W$, $Y_u=(S_u+W)/W$, $S'=\Lambda'/\pi\Lambda'$ and $S'_u=(J_u\cap\Lambda')\bmod\pi\Lambda'$. There is an exact sequence
$$
 0\longrightarrow Q\longrightarrow S'\xrightarrow{p} W\longrightarrow0,
 \qquad p(S'_u)=X_u,\qquad S'_u\cap Q=Y_u.                  \tag{16.1}
$$
The kernel of reduction to $W$ is $\pi\Lambda/\pi\Lambda'$, identified with $Q$ by division by $\pi$. Every element of $X_u$ lifts to $M_u\cap\Lambda'$. The elements of this last module in $\pi\Lambda$ are precisely $\pi M_u$, whose images in the kernel identify with $Y_u$.

For $A\le W$ and $C\le Q$, let $h_X(A)$ and $h_Y(C)$ denote the same expression with images $X_u$ and $Y_u$ respectively, **using the same $R,D$**. Then $h_X(A)=h(A)$ and
$$
 h_Y(C)=h(\operatorname{pr}^{-1}C)-h(W)\le0
$$
for $\operatorname{pr}:S\to Q$. Indeed the image of $S_u\cap\operatorname{pr}^{-1} C$ in $Q$ is $Y_u\cap C$. The inequality is strict when $C\ne0$ since $W$ is the largest maximizer. For $T'\le S'$, apply (16.1) to each $T'\cap S'_u$. With $A=pT'$ and $C=T'\cap Q$ this gives
$$
 h'(T')\le h_X(A)+h_Y(C)\le H(\Lambda).                    \tag{16.2}
$$
Thus $U(\Lambda')\le U(\Lambda)$. An equality witness must have $C=0$, $h(A)=H(\Lambda)$, and $p(T'\cap S'_u)=A\cap X_u$ for every word. Conversely these three conditions suffice. In particular, when the maximum is unchanged the largest new maximizer maps injectively into the old one.

## 2. A strict drop from the first-order period coordinates

**Candidate-D.** Choose a $k$-linear splitting $S'=W\oplus Q$ of (16.1). Each new word subspace determines a linear map $f_u:X_u\to Q/Y_u$: for $x\in X_u$, choose $(x,y)\in S'_u$ and put $f_u(x)=y\bmod Y_u$. Write $q_u:Q\to Q/Y_u$ for the quotient. For $A\le W$ form the linear system in $s\in\operatorname{Hom}_k(A,Q)$
$$
 q_u s|_{A\cap X_u}= f_u|_{A\cap X_u}\quad\text{for every }u.      \tag{16.3}
$$
Changing the splitting adds restrictions of a single common linear map to the right hand sides and leaves consistency invariant. Equation (16.3) asks whether the graph over $A$ lifts all its old word intersections.

* The new bound **strictly decreases if and only if** (16.3) is inconsistent for $A=V$, the smallest old maximizer.
* The bound and the dimension of the largest maximizer **both persist if and only if** (16.3) is consistent for $A=W$, the largest old maximizer.
* Each strict decrease is at least $1/\operatorname{lcm}(R,D)$. In particular, after an inconsistency certificate at $V$, $U(\Lambda)-1/\operatorname{lcm}(R,D)$ is a valid upper bound for the original complex cut.

For the first assertion, every equality witness in (16.2) is a graph over an old maximizing $A$, and its graph map solves (16.3). Its restriction to $V\subseteq A$ solves the system at $V$. Conversely a solution at $V$ produces a graph attaining $H(\Lambda)$. The same argument at $W$ proves the second assertion, since equality of dimensions for an injective projection into $W$ makes it onto. The spacing in the third assertion follows from the original two dimension denominators.

The cokernel in (16.3) at $V$ has a standard interpretation. On the star quiver with arrows $u\to 0$, take the representations $\mathcal A=(A_u\hookrightarrow V)$ with $A_u=X_u\cap V$, and $\mathcal B=(Y_u\hookrightarrow Q)$. The usual Hom–Ext sequence identifies $\operatorname{Ext}^1(\mathcal A,\mathcal B)$ with the cokernel of $(s,(z_u))\mapsto(s|_{A_u}-\iota_u z_u)_u$ in $\bigoplus_u\operatorname{Hom}(A_u,Q)$, where $s:V\to Q$, $z_u:A_u\to Y_u$ and $\iota_u:Y_u\hookrightarrow Q$. Quotienting first by the word maps $\iota_u z_u$ gives precisely the cokernel of the left side of (16.3). Restriction of (16.1) to $p^{-1}V$ and its word subspaces $S'_u\cap p^{-1}V$ gives an extension of $\mathcal A$ by $\mathcal B$ whose class is represented by $(f_u|_{A_u})_u$ in these coordinates. The bound drops exactly when this particular extension does not split. A nonzero Ext space alone also permits the zero class. [Belmans et al., §2.2, equation (3)](https://www.math.ru.nl/~vhoskins/GMS_quivers.pdf#page=5)

The inputs for this test are concrete. In an integral target basis adapted modulo $\pi$ to $W$, forming $S'$ divides the coordinates transverse to $W$ by $\pi$ on vectors whose old reductions lie in $W$. Bases for the **primitive** modules $M_u$ modulo $\pi^2\Lambda$ therefore suffice: lift generators of $X_u$ by combinations of those bases, take their divided transverse coordinates and use their classes modulo $Y_u$. Two such lifts differ by $\pi M_u$, contributing only $Y_u$. This gives $f_u$ after the common splitting is fixed. To certify inconsistency it suffices to give a row combination of the linear equations with zero left side and nonzero right side. These are coordinates of the actual pairings in a common row model. A truncation of the raw matrices may fail to determine a primitive frame if elementary divisors have high valuation.

## 3. Attainment at every prime

**Candidate-D.** Start from any common lattice, repeat the change of §1 using the largest maximizer, and stop if $H=0$. If continued whenever $H>0$, the resulting upper bounds equal $\epsilon(B)$ after finitely many changes and thereafter. Consequently
$$
 \epsilon(B)=\min_{\Lambda\text{ a common target lattice in }F_K} U(\Lambda).
                                                                    \tag{16.4}
$$
There is no residue-degree restriction or extension of local fields in this statement.

If $H=0$, equality follows from the lower witness $T=0$ in the original problem. Otherwise the bounded finite pair $(H,\dim W)$ is nonincreasing lexicographically by (16.2). Consider an infinite tail on which both entries are constant, and restart the indexing there with lattices $\Lambda_i$ and largest maximizers $W_i$. The reductions $W_{i+1}\to W_i$ are isomorphisms. They induce isomorphisms
$$
 W_{i+1}\cap S_{u,i+1}\longrightarrow W_i\cap S_{u,i}
$$
by the wordwise equality condition in (16.2). Denote their common dimensions by $t_u$ and put $w=\dim W_0$.

Choose a splitting $\Lambda_0=P\oplus Z$ with $P\bmod\pi=W_0$. For $i\ge1$, the image of $\Lambda_i$ in $\Lambda_0/\pi\Lambda_0$ equals $W_0$: the map through the previous reductions maps onto $W_{i-1}$ and along the isomorphisms onto $W_0$. Thus $\Lambda_i\to P$ is onto by Nakayama. Also $\pi^i\Lambda_0\subseteq\Lambda_i$ and the index length of $\Lambda_i$ in $\Lambda_0$ is $i(D-w)$. Surjectivity onto $P$ identifies this index with the length of $Z/(Z\cap\Lambda_i)$. Hence $Z\cap\Lambda_i=\pi^iZ$. The nested lattices now describe compatible graphs of maps $P\to Z/\pi^i Z$. Completeness identifies their intersection with the graph of a map $P\to Z$, of rank $w$. Denote its $K$-span by $T$.

For every $i\ge1$, $M_{u,i}=J_u\cap\Lambda_i$ reduces onto $W_0\cap S_{u,0}$ in the original residue space: its map onto $W_{i-1}\cap S_{u,i-1}$ is onto by (16.1), followed by the preceding wordwise isomorphisms. For each member of a residue basis of this $t_u$-dimensional space, the sets of lifts in $M_{u,i}$ are nested nonempty closed subsets of the compact lattice $\Lambda_0$. Their intersection is nonempty. The resulting lifts belong to $J_u\cap T$ and are $K$-linearly independent by reduction after primitive normalization of any proposed relation. Thus $\dim(J_u\cap T)\ge t_u$. The generic functional at $T$ is at least the residual maximum on the tail. By field-extension invariance it is bounded by the complex maximum. Saturated specialization gives the reverse bound. This proves (16.4) and eventual attainment.

A finite plateau alone cannot certify attainment. When given *exact* number-field matrices, one can combine this procedure with enumeration of number-field subspaces as lower witnesses, testing their exact intersection ranks. Round 15 proves existence of a number-field maximizer, so interleaving both searches eventually yields equal upper and lower witnesses. This is a termination argument, with no efficiency or family-uniform depth assertion. If only a prescribed upper threshold is needed, the first lattice meeting it gives a certificate on its own.

## 4. A conditional depth bound and a sharp precision obstruction

**Candidate-D.** A single nonzero minor bounds how many changes are needed to reach its upper certificate, including when words have kernels. Let $g=\gcd(R,D)$, $a=R/g$, $b=D/g$, $n=\ell\operatorname{lcm}(R,D)$, with $\ell\ge1$. Identify each generic word map with
$$
 J_u\oplus K^{\dim\ker B_u}\longrightarrow F_K,\qquad (x,z)\longmapsto x.
$$
This uses a separate generic source isomorphism for each word. Use $M_u\oplus O^{\dim\ker B_u}$ as its local lattice at every step. For fixed auxiliary integral matrices $X^{\mathrm{aux}}_u$ of size $a\ell\times b\ell$, form the square map $M=[B_u\otimes X^{\mathrm{aux}}_u]_u$ of size $n$ as in the parent proof, §5. If an initial $s$ by $s$ minor, $1\le s\le n$, has finite valuation $t$, put $\eta=1-s/n$. **After at most $t$ modifications the saturated upper bound is at most $\eta$.** A single exhibited minor suffices even when the exact rank exceeds $s$.

Let $k_s$ be the minimum valuation among the nonzero $s$ by $s$ minors of the map in integral bases of its current source and target. It is nonnegative, basis independent and initially at most $t$. In one modification, with $w=\dim W$ and $t_u=\dim X_u$, the source and target lattices of this square map decrease by lengths
$$
 L_{\rm in}=b\ell\big(\sum_u\dim J_u-\sum_u t_u\big),\qquad
 L_{\rm out}=a\ell(D-w).
$$
Both contain $\pi$ times their preceding lattices. The kernel coordinates in the word model do not change.

In Smith bases, take the primitive source summand $C$ on the first $s$ nonzero invariant factors, in nondecreasing valuation order. Its image has index length $k_s$ in the saturated target lattice of its $s$-dimensional generic image $Y$. Intersect $C$ with the new source. Its index in $C$ is at most $L_{\rm in}$, and the new intersection is primitive in the new source. The saturated lattice of $Y$ loses at least $L_{\rm out}-(n-s)$ in index length. Indeed reduction gives an $s$-dimensional subspace, and the old target modulo the new target has dimension $L_{\rm out}$; the image of that subspace has codimension at most $n-s$ in the quotient. Consequently the image of the new $C$ in the new saturation of $Y$ has index length at most $k_s+L_{\rm in}-L_{\rm out}+(n-s)$. Since both new summands are primitive in their respective lattices, extending their bases makes the determinant of this restricted map a minor. The minimum valuation in the new lattices is therefore bounded by
$$
 k'_s\le k_s+L_{\rm in}-L_{\rm out}+(n-s)
       =k_s-n\big(U(\Lambda)-\eta\big).                         \tag{16.5}
$$
Here $\sum_u\dim J_u=R(1-\kappa)$. The quantity $nU(\Lambda)$ is an integer. Whenever $U(\Lambda)>\eta$, (16.5) decreases $k_s$ by at least one. This proves the depth bound. More precisely, the sum of the positive excesses $U(\Lambda_i)-\eta$ before the first crossing is at most $t/n$. For a full determinant, each positive-defect step decreases the valuation by at least $\ell$, giving the depth bound $\lfloor t/\ell\rfloor$. This last assertion follows from (16.5) with $s=n$, since $nU$ is a multiple of $\ell$.

One can keep the auxiliary matrices symbolic. Put independent variables $x$ in their entries and work over $O[x]_{(\pi)}$, a discrete valuation ring with uniformizer $\pi$ and residue field $k(x)$. The valuation of a polynomial is the minimum valuation of its coefficients. Extend the original lattice chain to this ring. The ranks, saturation of the primitive inclusions, indices and chosen obstruction values in a prescribed chain are unchanged by this scalar extension, as is seen in bases adapted to each inclusion. The index proof of (16.5) applies to that chain and needs no finiteness of the new residue field. Consequently, for every initial segment with $U(\Lambda_i)>\eta$, **every coefficient of every symbolic $s$ by $s$ minor** in the initial integral bases is divisible by
$$
 \pi^{\sum_i n(U(\Lambda_i)-\eta)}.
$$
The assertion is automatic if all the minors vanish identically. Conversely a single coefficient of valuation $t$ gives the same depth bound without evaluating auxiliary variables in the finite residue field. Monotonicity and the sum bound give $U(\Lambda_j)\le \eta+t/[n(j+1)]$ at step $j\ge0$, taking the sequence to be constant after it stops. In the absence of a coefficient witness these are divisibility consequences of observed persistence, not a numerical small-defect estimate for the periods.

For any $m\ge1$ use two maps of one-dimensional spaces into $K^2$ with primitive generators $e_1$ and $e_1+\pi^m e_2$. In the standard lattice the reduction has defect $1/2$ at its unique maximizing line. After $i\le m$ changes the target basis is $e_1,\pi^i e_2$ and the second vector has transverse coordinate $\pi^{m-i}$. Thus the first $m-1$ changes keep the same bound, while change $m$ gives two distinct lines and defect zero. The generic lines are independent. Taking $a=b=\ell=1$ and $X^{\mathrm{aux}}_1=X^{\mathrm{aux}}_2=1$ gives $t=m$, attaining the depth bound. Replacing the second generator by $e_1$ gives the identical matrix data modulo $\pi^m$ and generic defect $1/2$. No fixed precision in primitive frames decides generic small defect uniformly. These are examples of arrangements, not period computations.

## 5. What the period data supply

**Candidate-D under the source hypotheses.** The arithmetic word lattices and their full-rank fractional-ideal modifications span the same coefficient spaces. Changing such a source lattice under a fixed field-linear $B_k(u)$ leaves $J_u$ and hence $J_u\cap\Lambda$ unchanged for every fixed common target lattice. Integral length estimates for those source changes alone therefore do not give the classes $f_u$ of (16.3). A common complex isomorphism in the cut comparison need not come with a common integral frame. The prescribed-prime test uses the coefficient model $B_k$ itself. [Round 15, arithmetic cut and comparison](../round15/SOURCE.md) · [Pinned source, full span and ideal twist](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1579-L1646)

The source also retains exact coefficient-sensitive identities. Under its local hypotheses, `KerEnt.kform` describes adjacent chain blocks through projections and theta differential evaluation, and the endpoint result returns a coefficient-field period value together with a valuation bound. These identities give a possible source for pairing entries. Applying (16.3) still requires joint coordinates at the same place for the fixed target and primitive images of the words in the equations. The local identities and source lengths alone have supplied no evaluated nonzero obstruction for those images. [Round 16 source audit](SOURCE.md)

For the actual transported full maps, let $\alpha$ be the retained source fraction and $\beta$ the retained target fraction. Under the block comparison of round 15, each individual successful bound $U_*$ for the cut yields
$$
 \epsilon(P)\le \max(1-\alpha,1-\beta)+\alpha U_* .
$$
In particular an inconsistency in (16.3) at the smallest maximizer allows $U_*=U(\Lambda)-1/\operatorname{lcm}(R,D)$. Attainment in (16.4) says some lattice eliminates all *excess created by reduction*. It gives no upper bound on the generic defect itself. No primitive first-order period coordinates, favorable numerical rank, or family-uniform depth for the actual $B_k$ are established here. The required small defect of the period family remains **O**.
