# Exact finite-horizon reading capacity of periodic cyclotomic quotients

**Proposed analytical candidate-T; NON-CANONICAL; L1.**

This is a proof-first draft, not a frozen public preregistration. The user-supplied finite reconnaissance is result-exposed. No scientific program has been executed in preparing this proof.

## 1. Carrier and the preparation restriction

Let O=Z[zeta_5], phi=(1+sqrt(5))/2, and u=epsilon*zeta_5^a*phi^k with epsilon in {1,-1}, a integral and k nonzero. For n>=1 put a_n=u^n-1 and R_n=O/a_n O. Since no complex embedding of u has modulus one, a_n is nonzero. Thus R_n is a finite additive group of cardinality

    F_n = |N(a_n)|.

Multiplication by the unit u is a permutation T_n of R_n and T_n^n=I.

The reader contract chooses a nonempty T_n-invariant subset S of R_n and a free labeling f:S->{0,...,m-1}. The initial point is uniform on S, not necessarily on R_n. The requested n-word is (f(x),f(T_n x),...,f(T_n^(n-1)x)). Its law is uniform on all m^n words. The reader and the selected support may depend on n. No compatibility across horizons and no infinite independent process on one fixed finite carrier is asserted.

The distinction between S and R_n is material: using all of R_n additionally requires m^n to divide F_n and may fail even when a suitable smaller invariant S exists.

## 2. Fixed points and exact periods

For d dividing n, a_n=a_d b with b in O. The kernel of multiplication by a_d on O/a_n O is bO/a_n O. The map y mod a_d O -> b y mod a_n O is an isomorphism, since O is an integral domain. Consequently

    #Fix(T_n^d) = F_d.

This proof uses ideal divisibility, not an inference from cardinality alone and not a principal-ideal-domain assumption. Mobius inversion gives the number of states of exact period d:

    P_d = sum_(e|d) mu(d/e) F_e,

independent of the ambient n as long as d divides n. The number of source cycles of length d is C_d=P_d/d. The number of words of exact period d over an m-letter alphabet is

    W_d(m)=sum_(e|d) mu(d/e) m^e,

and their rotation-necklace count is B_d=W_d(m)/d.

## 3. Complete finite feasibility criterion

Uniformity means every word has the same positive integer number c of preimages, with |S|=c*m^n and 1<=c<=floor(F_n/m^n).

A source cycle of length e can label a target necklace of period d exactly when d divides e. It then contributes e/d preimages to each of the d words in that necklace. Therefore existence is equivalent to the following finite integer assignment problem. For every target necklace eta of period d and every e dividing n with d dividing e, choose y_(eta,e)>=0 integral, subject to

    sum_(e:d|e|n) (e/d)*y_(eta,e)=c,
    sum_eta y_(eta,e)<=C_e  for every e|n.

Necessity follows by decomposing S into source cycles. For sufficiency, allocate distinct actual source cycles according to the assignment and repeat the corresponding necklace along each allocated cycle; their union is S and its labeling has exactly c preimages per word. Thus no relaxation or fractional allocation is admitted.

In particular aperiodic words require exact-period-n states, giving

    c*W_n(m)<=P_n,

and hence the user's weaker necessary condition W_n(m)<=P_n. Neither this weaker condition nor m^n<=F_n is sufficient in general.

For a useful exact control, suppose n is prime, F_1=1, and m>=2. A constant output word can receive states only from fixed points and n-cycles. Thus for each of the m constant words, the number of allocated fixed points is congruent to c modulo n. There is only one fixed point altogether. Consequently c must be divisible by n. The user-exposed reconnaissance values F_5(J)=121 and F_1(J)=1 therefore predict no binary reader at n=5: c<=floor(121/32)=3, whereas positive c would have to be at least five. This finite prediction must be checked by the frozen independent census; no numerical execution established it here.

## 4. A uniform sufficient construction

Suppose P_n>=n*m^n. Set c=n and use only source cycles of length n. For each target necklace of least period d, allocate exactly d such source cycles. Each cycle contributes n/d preimages per word, so d cycles contribute n. The total number of n-cycles used is

    sum_(d|n) d*B_d = sum_(d|n) W_d(m)=m^n.

There are P_n/n>=m^n available. This constructs the desired support of exactly n*m^n states without any fixed-point requirement for constant words. The constant words are written as constant labels on full n-cycles.

## 5. Eventual alphabet threshold

Put r=phi^|k|>1 and rho=r^2. The embedding moduli of u are r,r,r^-1,r^-1. The phase and sign affect finite counts but triangle inequalities give the phase-uniform bounds

    rho^n*(1-r^-n)^4 <= F_n <= rho^n*(1+r^-n)^4.

For n>=2, r^n>=phi^2>2, and therefore F_n>=rho^n/16. For every d>=1, F_d<=16*rho^d. Since every proper divisor d of n obeys d<=n/2,

    P_n >= F_n - sum_(d|n,d<n) F_d
        >= rho^n/16 - 16*n*rho^(n/2).

If m<rho, the right side eventually exceeds n*m^n. Section 4 gives readers for every sufficiently large n. If m>rho, F_n/m^n tends to zero, so eventually even the cardinality condition fails. Equality cannot occur for integral m because rho=phi^(2|k|) is irrational.

Let L=L_(2|k|), where L_0=2,L_1=1 and L_(j+2)=L_(j+1)+L_j. The identity rho+rho^-1=L gives

    L-1 < rho < L.

Thus, for integral m>=2, readers exist for every sufficiently large n if and only if m<=L-1. For m>=L they exist for at most finitely many n. The latter phrase permits zero exceptions. This is a family of finite-horizon existence statements with n-dependent S and f, not an infinite Bernoulli factor theorem.

## 6. An explicit all-integer sufficient onset

The following conservative onset is computable without algebraic real comparisons. Let L=L_(2|k|)>=3 and Q=2L-1. Since rho=L-rho^-1 and rho>2, q=Q/2=L-1/2 is strictly smaller than rho. Also q^2>L.

For 2<=m<=L-1 define

    n0=max(2,ceil(2m/(Q-2m)),ceil(12L/(Q^2-4L))).

Define n_*(k,m) as the first integer n>=n0 for which both exact integer inequalities hold:

    Q^n >= 32*n*(2m)^n,
    Q^(2n) >= 512^2*n^2*(4L)^n.

This search terminates because Q/(2m)>1 and Q^2/(4L)>1. It is an explicit definition, not a claim that the first sufficient n is minimal. The first ratio (Q/(2m))^n/n is nondecreasing for n>=ceil(2m/(Q-2m)). The second ratio (Q^2/(4L))^n/n^2 is nondecreasing for n>=ceil(12L/(Q^2-4L)), since (1+1/n)^2<=1+3/n. Both inequalities therefore hold for every n>=n_*.

Using F_n>=q^n/16 and F_d<=16*L^d yields

    P_n >= q^n/16 - 16*n*L^(n/2).

The second integer inequality implies q^n>=512*n*L^(n/2), so the negative term is at most q^n/32. The first then implies

    P_n >= q^n/32 >= n*m^n.

Thus n_* is a phase-uniform all-n sufficient onset. A smaller phase-specific onset may be obtained by exact finite checks plus this tail proof, provided the finite domain is frozen before computation.

For an explicit eventual exclusion onset when m>=L, use rho<L-1/L. Every n satisfying

    16*(L^2-1)^n < (L*m)^n

has F_n<m^n, and the inequality remains true for larger n. This integer search also terminates.

## 7. Exact rational probabilities and their restricted meaning

Let p_i=a_i/b be a finite probability vector in least common denominator form: a_i nonnegative integers, sum a_i=b, and gcd(b,a_1,...,a_s)=1. Independent n-tuples have probabilities product a_i/b^n. Their least common denominator is b^n: for each prime divisor of b there is some a_i not divisible by that prime, and its constant n-word forces the full prime power in the denominator. Hence every uniform finite preparation support realizing this exact product law has cardinality divisible by b^n.

The cardinality argument excludes eventual existence when b>rho. Conversely a fair b-letter reader can be lumped into s outcomes in blocks of sizes a_i, proving eventual existence when b<rho. Thus the minimal positive stride k for eventual exact readings under step J^k is

    min{k>=1: b<L_(2k)}.

This is an exact preparation-support capacity under freely selected f and S. It is not a native physical sampling law, not a finite-horizon optimum, not a device latency, and not a cost derived for all interpretations of Born probabilities. It uses the denominator because exact uniform counting is required; it is not the Shannon entropy of the biased output law.

## 8. Torsion and rotation controls

If k=0, u is torsion of order q dividing 10. When q divides n, u^n-1=0 and R_n=O is infinite. The finite-quotient experiment is undefined there and must be marked INFINITE, never enumerated as a finite zero-determinant quotient. When q does not divide n the quotient is finite, but T_n^q=T_n^n=I, so its order divides gcd(q,n). In particular if n does not divide q, every output word has period strictly smaller than n, excluding a fair m-letter n-word for m>=2.

In the specific zeta_5 control, if 5 does not divide n then zeta_5^n-1 generates the same ideal as zeta_5-1. The quotient is F_5, with identity tick. At n=1 this admits every fair m-letter one-tick reader for 2<=m<=5 by choosing m fixed points. At n>=2 it admits no full-period fair m-letter reader for m>=2. At multiples of five the quotient is infinite. A blanket failure condition saying only that a rotation reader exists would therefore be false.

On an independently declared finite rotation system of order q, an m-letter window longer than q cannot be independent: the repeated positions agree identically. A single cycle of length n also cannot supply all m^n length-n words because it has only n states. These controls do not imply that rotations never supply finite-window independence: a cycle with m^h states carrying a de Bruijn labeling can supply all length-h words once, for h shorter than its orbit length. Zero asymptotic entropy of one fixed finite system must not be confused with impossibility of all finite windows across growing rotation carriers.

## 9. Scope boundaries

The phase contributes no exponential growth rate but may change finite state counts, exact periods, and the first feasible horizon. The principal embedding of J contracts by phi^-1; the conjugate expanding pair explains the growth rho=phi^2. No physical selection of S, f, uniform ensemble, self-location, apparatus, event, native U, or L1-to-L5 lift is supplied. No previous failed entropy bridge is reopened. Existing bank and native-reader theorems retain their own domains and cannot be identified with this class by a shared word such as capacity.
