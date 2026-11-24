# Round 18: the conductor-five pattern and the remaining period estimate

**NON-CANONICAL. No authority. No Canon status change.**
Candidate C-RH-SEMISTABLE-FRAME-N, also discussed as C-RH-BK-CONCENTRATION-N.
Session: ChatGPT-Astra-Sol-20261124-R18. Paper deductions are **candidate-D**
with the hypotheses stated below. Classical imported theorems retain their
scope. The fixed-character critical-line conjecture and the actual
all-subspace period estimate remain **O**.

## 1. Outcome

The owner's five-symbol note is mathematically substantive in its own
right. Its conductor-five character simultaneously describes a Gauss sum,
the exchange of the two real scaling values of J, a Fibonacci divisibility
law, and the root number of one Dirichlet L-function. These are compatible
readings of the same quadratic Galois data. The note does not need to
produce an operator on the RH period family to have that meaning.

This round proves the following scoped consequences and boundaries.

1. The character remains balanced to an explicit square-root bound after
   restriction to squarefree integers. The ordinary prime number theorem
   improves this to little-o of the square root.
2. The same factored polynomial gives a positive Mellin kernel, proving
   positivity of L(s,chi_5) on the positive real axis. It also recovers the
   already known exact value tied to log(phi).
3. For the project's existing split-factor polynomial Q_x(z), the balanced
   evaluation Q_x(1) is little-o of sqrt(x), whereas its first derivative is
   asymptotic to sqrt(5) log(phi) x/(pi^2 log(x)). This last assertion uses
   the classical prime number theorem in progressions of fixed modulus five.
   It gives a concrete limit on transferring a balanced evaluation to
   nearby weighted sums.
4. The actual period Gram expansion admits a source-linked cyclic trace
   formula. The closing rational element lies in the special unitary group
   at the actual two-prime level. Determinant characters disappear on these
   cycles; the additive level phase and archimedean cyclic overlaps remain.
   Their required quantitative cancellation is not proved.

Proofs and internal review are in [DEVELOPMENT](DEVELOPMENT.md),
[OPPOSITION](OPPOSITION.md), and [SOURCE](SOURCE.md). No new scientific
program, finite census, or Lean verification was run.

## 2. What is exact in the five-symbol note

Put j=exp(2 pi i/5), J=1+j^2 and phi=-j^2-j^3, with this embedding fixed.
For P(X)=(1-X)(1-X^2),

\[
 A=P(j)=1-j-j^2+j^3,\qquad
 jA=j+j^{-1}-j^2-j^{-2}=\sqrt5
 =\frac jJ+\frac Jj.
 \tag{18.1}
\]

Also

\[
 h=J\overline J=\phi^{-2}=\frac{3-\sqrt5}{2},
 \qquad h+h^{-1}=3.
 \tag{18.2}
\]

The five monomials are register coordinates with one relation after
evaluation at j; they are not a basis of the quartic number field.
On the full regular five-cell register, with shift g and N=11^T, set
G=gP(g) and M_J=I+g^2. Then

\[
 G^2=5I-N,\qquad G=3I-2M_J^TM_J+N.
 \tag{18.3}
\]

On the zero-sum space N vanishes, and G has both signs of sqrt(5), each
twice. The shorthand G=sqrt(5) is valid only after selecting its positive
sector or the corresponding field embedding. The registered mixer called
A is gG=g^2P(g); its difference from the owner's A is a cyclic shift.
The integral augmentation lattice also has index five in its evaluated
cyclotomic lattice, as detailed in OPPOSITION.

For an unramified rational prime p, arithmetic Frobenius acts by
j -> j^p, so

\[
 \sigma_p(h)=h^{\chi_5(p)},\qquad
 h^p=h^{\chi_5(p)}\ \text{after reduction}.
 \tag{18.4}
\]

| p modulo 5 | chi_5(p) | Action on h | Residue degree in Q(j) |
| --- | --- | --- | --- |
| 1 | +1 | fixes h | 1 |
| 2 | -1 | exchanges h and h^{-1} | 4 |
| 3 | -1 | exchanges h and h^{-1} | 4 |
| 4 | +1 | fixes h | 2 |
| 0, hence p=5 | 0 | ramified case | outside this unramified rule |

Thus the displayed sign is the quadratic quotient of the quartic
Frobenius information. In particular the prime class four fixes the
scaling values while acting nontrivially on j. The zero at five is the
Dirichlet-character convention; it does not say that J vanishes.
[Milne, Algebraic Number Theory, Examples 8.18-8.19](https://www.jmilne.org/math/CourseNotes/ANT.pdf)

There is a further exact distinction for Fibonacci numbers. In
R_p=F_p[T]/(T^2-T-1), the element giving the least positive index z(p)
with p dividing F_{z(p)} is t=-h, not h in general. For p not equal to five,

\[
 z(p)=\operatorname{ord}(-h)\mid p-\chi_5(p).
 \tag{18.5}
\]

For odd p different from five put N_p=p-chi_5(p). Then

\[
 h^{N_p/2}=\chi_5(p),\qquad
 (-h)^{N_p/2}=(-1)^{(p-1)/2}.
 \tag{18.6}
\]

Consequently z(p) divides N_p/2 exactly when p is 1 modulo four.
When p is 3 modulo four, z(p) contains the entire power of two in N_p.
This is a second character, of modulus four. At five the full quadratic
algebra is nonreduced: t=1-2 epsilon with epsilon^2=0, and t has order
five. Passing to its residue field would lose that order. These statements
concern the first zero index. The full Fibonacci pair period is a different
invariant; the two values can coincide.
[Cubre and Rouse, Divisibility properties of the Fibonacci entry point](https://arxiv.org/abs/1212.6221)

## 3. Squarefree cancellation: a completed elementary step

Let C(y)=sum_{n<=y} chi_5(n). Its values at floor(y) modulo five are
0,1,0,-1,0. Let

\[
 B(x)=\sum_{n\le x}\mu(n)^2\chi_5(n),\qquad
 D_x=\lfloor\sqrt{x}\rfloor .
\]

**Candidate-D, elementary.** The prime-local divisor identity
mu(n)^2=sum_{d^2|n} mu(d) gives

\[
 B(x)=\sum_{\substack{d\le D_x\\5\nmid d}}
       \mu(d)C(x/d^2),
 \qquad
 |B(x)|\le D_x-\lfloor D_x/5\rfloor .
 \tag{18.7}
\]

Every surviving term has magnitude at most one. This proves an explicit
bound at every cutoff, with no hypothesis about zeros and no finite
experiment. The argument applies to the squarefree restriction itself.

**Candidate-D with a classical analytic input.** In fact B(x)=o(sqrt(x)).
The ordinary prime number theorem says M(y)=sum_{n<=y}mu(n)=o(y).
After removing multiples of five,
M_5(y)=sum_{j>=0}M(y/5^j)=o(y), by geometric domination.
In (18.7), the terms d<=delta sqrt(x) cost at most delta sqrt(x).
On the remaining range, floor(x/d^2) takes finitely many values for
fixed delta. Each interval sum is a difference of M_5 at fixed positive
multiples of sqrt(x), hence little-o of sqrt(x). First let x grow, then
let delta decrease to zero.
[Soundararajan, Notes for Math 155, section 1](https://math.stanford.edu/~ksound/Math155W10/Notes1.pdf)

For squarefree n prime to five, let a(n) count its split prime divisors
and b(n) its inert prime divisors in Q(sqrt(5)). The exact distinction is

\[
 \mu(n)^2\chi_5(n)=(-1)^{b(n)},\qquad
 \mu(n)\chi_5(n)=(-1)^{a(n)}.
 \tag{18.8}
\]

Equation (18.7) controls the parity discrepancy of the inert-factor count
on this support. The desired twisted Mobius sum controls the split-factor
count on the same support. For Re(s)>1 their respective series are

\[
 \sum_n\frac{\mu(n)^2\chi_5(n)}{n^s}
 =\frac{L(s,\chi_5)}{(1-5^{-2s})\zeta(2s)},\qquad
 \sum_n\frac{\mu(n)\chi_5(n)}{n^s}=\frac1{L(s,\chi_5)}.
 \tag{18.9}
\]

The reciprocal in the second formula is the exact analytic difference.
The assertion that this second summatory function is
O_epsilon(x^(1/2+epsilon)) for every positive epsilon is equivalent to
the critical-line conjecture for this particular L-function. The easy
direction follows by partial summation of its reciprocal series; the
reverse direction uses reciprocal growth bounds and Perron inversion.
It is not a proof of the Riemann hypothesis for zeta, or of GRH for all
Dirichlet characters.
[Gao and Zhao, equation (1.2)](https://arxiv.org/html/2212.09241v2#S1.E2)

## 4. Positive kernel and a precise boundary for weighting

**Candidate-D.** At 0<z<1 the same polynomial has a positive generating
function:

\[
 K(z)=\sum_{n\ge1}\chi_5(n)z^n
     =\frac{z(1-z)(1-z^2)}{1-z^5}>0.
 \tag{18.10}
\]

Its Mellin integral is

\[
 \Gamma(s)L(s,\chi_5)
 =\int_0^\infty t^{s-1}K(e^{-t})\,dt .
 \tag{18.11}
\]

Near zero the kernel is asymptotic to 2t/5; at infinity it decays
exponentially. The integral therefore extends to Re(s)>-1. For real s>0
both it and Gamma(s) are positive, giving L(s,chi_5)>0, including at 1/2.
For nonreal s the factor exp(i Im(s) log(t)) oscillates, so this argument
does not exclude complex zeros. OPPOSITION gives the full proof.

The elementary integral at one also yields the already known special value

\[
 L(1,\chi_5)=-\frac{\log h}{\sqrt5}
            =\frac{2\log\phi}{\sqrt5},
 \qquad L'(0,\chi_5)=\log\phi.
 \tag{18.12}
\]

The second equality follows from the functional equation. This is an
exact relation between the logarithmic scale of J and the same
L-function, with no physical interpretation assigned.
[Primitive character functional equation](https://kskedlaya.org/ant/chap-funceq2.html)

Now retain the polynomial already defined in the registered
RAPIDITY-TARGET-RECONSTRUCTION statement:

\[
 Q_x(z)=\sum_{\substack{n\le x\\n\ {\rm squarefree}}}
           (-1)^{b_{\rm all}(n)}z^{a(n)} .
 \tag{18.13}
\]

Here b_all counts inert prime divisors and the ramified prime five.
Separating n=5m proves

\[
 Q_x(1)=B(x)-B(x/5)=o(\sqrt{x}),\qquad Q_x(-1)=M(x).
 \tag{18.14}
\]

**Candidate-D with the classical prime number theorem in progressions.**
The first split-count weighted sum has the exact leading behavior

\[
 Q'_x(1)\sim c_5\frac{x}{\log x},
 \qquad c_5=\frac{5L(1,\chi_5)}{12\zeta(2)}
           =\frac{\sqrt5\log\phi}{\pi^2}>0.
 \tag{18.15}
\]

For clarity, this is not inferred by differentiating an asymptotic in z.
Put f(n)=mu(n)^2(-1)^b_all(n). Its summatory function is Q_x(1)=O(sqrt(x))
already by (18.7). For Re(s)>1 the derivative of the exact Euler product is

\[
 \sum_n\frac{a(n)f(n)}{n^s}
 =\frac{L(s,\chi_5)}{(1+5^{-s})\zeta(2s)}
       \sum_{\chi_5(p)=1}\frac{p^{-s}}{1+p^{-s}} .
 \tag{18.16}
\]

Expand the last sum into coefficients supported on split prime powers,
with alternating signs in the exponent. Their summatory function is
asymptotic to x/(2 log(x)), and their absolute count is O(x/log(2x)).
In the convolution, keep the first index at most a fixed K. This part has
main coefficient one half of sum_{m<=K}f(m)/m. Swapping the two indices
on the remaining part and using the O(sqrt(x)) prefix bound gives an
error O(x/(sqrt(K) log(2x/K))). Let x tend to infinity before K.
The conditionally convergent sum of f(m)/m equals
5L(1,chi_5)/(6 zeta(2)), proving (18.15).
The complete estimates are in OPPOSITION.
[Kedlaya, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html)

There is also a shorter boundary argument needing only the Euler behavior
at s=1: (18.16) diverges logarithmically as s decreases to one. Thus
Q'_x(1)=O(x^theta) is impossible for every theta<1. DEVELOPMENT proves
the precise lower-excursion version by partial summation.
In particular a uniform O(x^theta) bound on any fixed complex
neighborhood of z=1 is impossible by Cauchy's derivative estimate.
This excludes that particular transfer of a balanced evaluation to a
uniform Taylor neighborhood. It does not exclude cancellation at another
isolated value, including z=-1, or a proof of RH by other means.

## 5. The source-level period work: what closes around a cycle

The actual-period branch remains separate. SOURCE uses the pinned RH
operator expansion, its absolute convergence premises and the same
positive source normalization as the full Gram maps of round 17.
For A_u:E_u->F, write G_uv=A_u^*A_v. An ordered cycle in a Gram trace
has finite support elements

\[
 k_i=x_i^{-1}\gamma_{i,f}x_{i+1}\in K_2,\qquad x_{\ell+1}=x_1.
\]

**Candidate-D under the actual full realization and unfolding premises.**
The finite parts and characters telescope:

\[
 k_\circ=x_1^{-1}(\gamma_1\cdots\gamma_\ell)_f x_1,
 \qquad
 \prod_i\chi_2(k_i)=\chi_2(k_\circ).
 \tag{18.17}
\]

The product of rational representatives preserves the starting lattice.
Its determinant is an integral norm-one unit, hence a root of unity.
The two distinct residue characteristics in the actual level force that
determinant to be one. The rational closing element therefore belongs to
SU. The determinant argument leaves its additive level phase undetermined.

For a supported tuple the contribution, apart from the explicit positive
normalizing scalars, is

\[
 \chi_2(k_\circ)\operatorname{tr}(O_1\cdots O_\ell),
\]

where each O_i is a Bochner integral of rank-one operators. Its cyclic trace
is the integral of the cyclic product of the corresponding inner products.
SOURCE proves the convergence needed for these operations and preserves
the antiunitary coordinate convention. It does not treat a chosen quotient
representative as a canonically defined rational conjugacy class.

Every determinant multiplier used in R17 cancels on a closed chain.
A formal average of powers of chi_2 filters the closing phase, but only
the original power is the actual period problem. The other powers have
not been realized as the same target or source family.

The exact moment identity is

\[
 \operatorname{tr}_F\left[\left(\sum_u A_uA_u^*\right)^\ell\right]
 =\sum_{u_1,\ldots,u_\ell}
   \operatorname{tr}_{E_{u_1}}
      (G_{u_1u_2}\cdots G_{u_\ell u_1}).
 \tag{18.18}
\]

It also localizes to the actual multiplicity spaces by inserting their
central projector once and dividing by the simple-factor dimension.
The normalization is stated in SOURCE. A general projector can mix column
classes; it cannot be silently inserted into the simpler phase telescope.

**O.** The source estimates reviewed so far control pairs. They do not
give the cancellation in the cyclic sums needed to improve the residual
all-subspace defect. Fixed centered moments merely on the usual
sigma^a scale would still permit the R9 square-root countermodel.
The R17 algebra/commutant distinction and the weighted intrinsic defect
E_mult remain unchanged. This round identifies more of the actual
operator data, without claiming the remaining rank inequality.

## 6. Custody and scope of review

The PUBLIC basis is main ed3b1878d95825ab9473c16416c8db76cc152079,
Public Canon v116, content 0b6ae8e23d7086715b908cce6e1755d2898f55fc.
The draft continued from 8217fff0cb08129bc12e8cc0cf6e5737ca0529b3.
Authority, normative hashes, tag/content ancestry and successful main
checks were verified before authoring. The R18 claim was read back in
issue 2070 before the new files were written.

The algebraic note overlaps existing canonical statements, including
J-PLENUM-POLAR-ORBIT-SEPARATION, J-IDEAL-COUNT-QUADRATIC-CHARACTER,
J-IDEAL-RATIONAL-MOBIUS-DESCENT, J-MERTENS-IDEAL-TWOSUM and the rapidity
polynomial results. These are credited, not rediscovered or promoted.
Existing Mobius approximation and topology owners remain separate.

Two Astra agents developed and opposed the arithmetic reasoning; a Sol
agent developed the actual-source cycle formula; the root read the decisive
source definitions and integrated the results. The agents cross-reviewed
the squarefree, Mellin, torus, derivative and cycle arguments. This is
internal paper review, not external independent confirmation.

All source claims use RH commit 40e56bab026552e089d7afcfeff08d2defb9c005.
No claim about the validity of the full current RH proof or a fresh Lean
build is made. No historical mathematical priority is asserted. Earlier
round files, frozen programs and their evidence remain unchanged.
