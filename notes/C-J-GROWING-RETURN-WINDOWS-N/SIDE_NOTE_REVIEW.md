# Paper review of the unit-relation note

**NON-CANONICAL. No authority. All deductions below are candidate-D, L1.**
This is a shared-context paper review for #2084. It provides neither blind
confirmation nor a computational rerun. The user-supplied reference is
`PROMO-C-J-UNIT-RELATION-DEPTH-1(1).md`, 8044 bytes, SHA-256
`5adb6941ee9c9e3caa88b4e793b775fe7bab0863e2055c39da451218409683de`.
Its reported finite checks are outside this review.

## Equality and normalized triples (sections 2 and 3)

Work modulo the whole rational ideal $(p)$, $p>5$. Put
$j=\zeta_5$, $\alpha=\phi^2$, $h=\operatorname{ord}(\alpha)$, and
$B=\mathbf F_p[\phi]$. Conjugation on $B$ exchanges $\phi$ and
$\psi=-\phi^{-1}$. Cyclotomic complex conjugation fixes $B$.
The norm-one group of $B$ is cyclic in both cases. In the split case
it consists of $(a,a^{-1})$ with $a\in\mathbf F_p^\times$.

The norm of $\phi$ is $-1$, so its order is even and equals $2h$.
For even $h$, $\alpha^{h/2}=-1$ by uniqueness of the norm-one
involution. For odd $h$, the only involution in
$\langle\phi\rangle$ is $\phi^h$, of norm $-1$, whereas $-1$
has norm $+1$. For $a\not\equiv0\pmod5$,
$S_a=j^a-j^{-a}$ is invertible since $1-j^{2a}$ has absolute norm
five. Thus no nontrivial fifth root $j^a$ is real after reduction.
These facts determine equality of all labels $\pm j^a\phi^b$ from
$h$. They do not determine arbitrary addition in the quotient.

Normalize a triple to $xj^a+yj^b=1$ with $x,y\in\langle-1,\phi\rangle$.
Exactly one nonzero phase is impossible by complex conjugation. Equal
nonzero phases would make $x+y=j^{-a}$ real. Distinct nonzero phases
give an invertible two-by-two system with determinant $S_{a-b}$ and
solution $x=-S_b/S_{a-b},\ y=S_a/S_{a-b}$. The ratios are real units
already over the integers, as $S_2/S_1=\phi^{-1}$, $S_3=-S_2$,
and $S_4=-S_1$. This gives twelve ordered pairs.

For zero phases write $e=N(x), f=N(1-x)$. Then
$\operatorname{Tr}(x)=1+e-f$. For $(e,f)=(+,-)$, the two values of
$x$ are $\phi^2,\phi^{-2}$. Exchanging summands treats $(-,+)$.
For $(-,-)$ they are $\phi,\psi$. Within each case the roots are
distinct since the discriminant is five. In the split algebra the two
coordinates must have the prescribed sum and product, so the only
choices are the two orderings of the roots. For $(+,+)$, $x$ has
order six and $1-x=x^{-1}$. Conversely, each norm-one element of
order six satisfies $x^2-x+1=0$, including in the split algebra where
both coordinates have order six. The norm-one part of the real unit
image is $\langle-1,\alpha\rangle$, of order
$\operatorname{lcm}(2,h)$. Thus the count is
$18+2\mathbf1_{3\mid h}$ **ordered normalized pairs of unit images**.
Different exponent strings for the same image count once. The kernels
also identify the solutions as labeled equalities at two primes with
the same $h$. In the order-six case the solutions are precisely the
two order-six elements in the norm-one subgroup of the real unit image.

## Signed divisibility flags (section 4)

Let $\chi=\chi_5(n)$ at an admitted odd index and
$r=(n-\chi)/2$. The flag $p\mid R(n)$ is equivalent to
$\alpha^r=\chi$. For $\chi=+1$ this means $n\equiv1\pmod{2h}$.
For $\chi=-1$ it requires even $h$ and $n\equiv h-1\pmod{2h}$.
On $n=1+10k$ the hits give the multiples of $h/\gcd(h,5)$ in
$k$. On $n=9+10k$ a hit exists exactly when $5k+4\equiv0\pmod h$
is solvable, equivalently $5\nmid h$. Together the two readings recover
$h$, also when the initial index one is excluded.

For two primes with equal $h$, any common choice of forward neighbors
therefore gives identical prime-divisibility flags for the lcm of the
pairwise gcds. For a growing or adaptive common window,
divisibility still requires a hit at the start and at some selected neighbor.
Higher prime-power valuations, the entire integer value, and procedures
that choose different neighbors for the two factors lie outside this
conclusion.

## Four-term witnesses and vertical gcd (sections 5 and 6)

Both stated order collisions admit a short paper check. The Fibonacci
identity $F_{19}=F_{10}^2+F_9^2=55^2+34^2=37\cdot113$ gives
$\alpha^{19}=-1$ at either prime by Binet's identity. The only possible
orders are two and 38, and $\alpha\ne-1$ since $\phi+2$ has norm
five. Likewise $L_5=11$ and
$L_{25}=11(11^4+5\cdot11^2+5)=11\cdot101\cdot151$.
For odd $s$, $1-\alpha^s=-\phi^s L_s$. Hence the second pair has
$\alpha^{25}=1$ and $\alpha^5\ne1$, giving order 25.
The four-unit expression $L_9-L_0=76-2=74$ vanishes modulo 37 and
survives modulo 113. The four-unit expression $L_{11}+L_2=199+3=202$
vanishes modulo 101 and survives modulo 151. These are separations
using four summands with multiplicity. A same-parity signed trace
comparison fixes the norm as well as the trace, hence gives equality
up to conjugation, also in the split case. The classification of labeled triples establishes
the four-term lower bound for a separator inside an equal-order class.
The two witnesses establish attainment for these two pairs only.
Universal attainment and efficient discovery remain open here.

Finally, in the geometric sum for $F_{st}/F_s$, each of the $t$
summands reduces to $F_{s-1}^{t-1}\pmod{F_s}$, since both
$\phi^s$ and $\psi^s$ reduce to $F_{s-1}$. Reduction of this
rational integer agrees with reduction in the integral basis
$1,\phi$. Coprimality of consecutive Fibonacci numbers gives
$\gcd(F_s,F_{st}/F_s)=\gcd(F_s,t)$ for $s,t\ge1$, with $F_s=1$
immediate. This resolves this particular increased-precision reading.
