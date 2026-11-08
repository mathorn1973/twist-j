# Module A. Integral relative norms and polarization reachability

**Status: NON-CANONICAL.** This is a proof-only specialization to the fixed
geometric benchmark below. The underlying integral relative-norm criterion
is already registered as **SCALAR-HERMITIAN-NORM-IMAGE [T]** in the public
Canon. This module gives the polarization interpretation, exact witnesses,
and the consequences for the specified pullback operation; it does not
claim to discover or register the scalar-norm theorem anew.

## A.0. Inputs, meanings, and provenance

Fix

$$
B=\operatorname{Jac}(y^2=x^5-1),\qquad
K=\mathbb Q(\zeta_5),\qquad
F=\mathbb Q(\sqrt5),\qquad
\phi=\frac{1+\sqrt5}{2}.
$$

The root $\zeta=\zeta_5$ is chosen so that
$\zeta+\zeta^{-1}=\phi-1$. The rings of integers are
$\mathcal O_K=\mathbb Z[\zeta]$ and
$\mathcal O_F=\mathbb Z[\phi]$. Complex conjugation on $K$ is
written $z\mapsto\bar z$, and it fixes $F$. The two embeddings of
$F$ send $\phi$ to $\phi$ and
$\phi'=1-\phi=-\phi^{-1}$.

Take the canonical principal polarization
$\lambda_0:B\longrightarrow B^\vee$. The geometric inputs are

$$
\operatorname{End}_{\mathbb C}(B)=\mathcal O_K,\qquad
\beta^\dagger=\lambda_0^{-1}\beta^\vee\lambda_0=\bar\beta,
$$

and the integral identification

$$
\operatorname{NS}(B)\simeq\mathcal O_F,\qquad
D_\eta\longleftrightarrow
\eta=\lambda_0^{-1}\lambda_{D_\eta}.
\tag{A.1}
$$

Here $D_\eta$ is an ample Neron--Severi class exactly when
$\eta\gg0$, meaning positive at both real embeddings. These inputs,
including (A.1) and its ampleness criterion, are proved in
[the public fixed-model geometric dictionary](https://github.com/mathorn1973/twist-j/blob/655e022d0ef95ee94681464d3325d2aa589df1d6/notes/C-RH-CM5-HECKE-DICTIONARY-N/CM5_POLARIZATIONS.md).
They are retained as the benchmark's geometric assumptions here.

The inherited arithmetic theorem and its dependencies are pinned to
[the public Canon at 8e1f6538a09c8ef012a0a9971d501119f13d52ee, SCALAR-HERMITIAN-NORM-IMAGE](https://github.com/mathorn1973/twist-j/blob/8e1f6538a09c8ef012a0a9971d501119f13d52ee/canon/CANON.md#scalar-hermitian-norm-image-t).
The proof below spells out the integral argument rather than replacing it
with a criterion for $N_{K/F}(K^\times)$.

We count ample Neron--Severi classes modulo pullback by
$\operatorname{Aut}(B,0)=\mathcal O_K^\times$. We do not count individual
line bundles in a fixed Neron--Severi class, generators of an ideal, or
endomorphisms realizing a pullback. In particular, the group defining
equivalence is the full origin-preserving automorphism group of $B$;
it is not the smaller group preserving $\lambda_0$.

For $\eta=x+y\phi$, with $x,y\in\mathbb Z$, set

$$
n(\eta)=N_{F/\mathbb Q}(\eta)=x^2+xy-y^2.
$$

When $\eta\gg0$, the geometric normalizations are

$$
q(D_\eta)=\frac{D_\eta^2}{2}=n(\eta),\qquad
\deg\lambda_\eta=n(\eta)^2,\qquad
\lambda_\eta=\lambda_0\circ m_\eta.
\tag{A.2}
$$

Here $m_\eta$ denotes the integral endomorphism represented by $\eta$.
Primitivity means that $D_\eta$ is primitive in the integral group
$\operatorname{NS}(B)$; equivalently $\gcd(|x|,|y|)=1$.

## A.1. The exact operation

An allowed step is pullback by an arbitrary
$\beta\in\mathcal O_K\setminus\{0\}$, regarded as an integral
endomorphism of $B$. Every such endomorphism is an isogeny: multiplication
by $\beta$ is invertible on the rational homology module, so it has
finite kernel and is surjective. Functoriality of the polarization map
and the Rosati identity give

$$
\begin{aligned}
\lambda_{\beta^*D_\eta}
  &=\beta^\vee\lambda_0m_\eta\beta\\
  &=\lambda_0m_{\bar\beta\eta\beta}
   =\lambda_0m_{\beta\bar\beta\eta}.
\end{aligned}
$$

Thus the operation is exactly

$$
\boxed{\ \beta^*D_\eta=D_{\beta\bar\beta\eta}\ }.
\tag{A.3}
$$

The parameter remains integral and totally positive. The identity
$\beta=1$ is allowed. An orbit $[D_\eta]$ is **reachable from the
principal class** if

$$
[D_\eta]=[\beta^*D_1]
\quad\text{for some }\beta\in\mathcal O_K\setminus\{0\}.
\tag{A.4}
$$

Finitely many allowed steps have the same effect as one step, since their
parameters multiply and
$N_{K/F}(\beta_1\cdots\beta_k)=\prod_jN_{K/F}(\beta_j)$.
The empty sequence is the identity step.

## A.2. Unit norms and ideal classes

### Lemma A.1. Positive units and the norm on units

One has

$$
\mathcal O_F^\times=\{\pm\phi^j:j\in\mathbb Z\},\qquad
\mathcal O_F^{\times,+}=\{\phi^{2j}:j\in\mathbb Z\},
$$

and

$$
N_{K/F}(\mathcal O_K^\times)=\mathcal O_F^{\times,+}.
\tag{A.5}
$$

**Proof.** The identity $\phi^2-\phi-1=0$ shows that $\phi$ is
an integral unit of norm $-1$. There is no unit $u$ with first
real value in the open interval $1<u<\phi$. Indeed, if its norm is
$+1$, its integral trace would satisfy

$$
2<u+u^{-1}<\phi+\phi^{-1}=\sqrt5<3.
$$

If its norm is $-1$, the integral trace would satisfy

$$
0<u-u^{-1}<\phi-\phi^{-1}=1.
$$

Both alternatives are impossible. For any unit, first multiply by
$-1$, if necessary, to make its first real value positive, and then
by a power of $\phi$ to put that value in $[1,\phi)$.
The resulting unit equals $1$. This proves the full unit formula.
The signs of $\phi$ at the two embeddings are $(+,-)$, so
total positivity picks out precisely the even powers with positive sign.

For $u\in\mathcal O_K^\times$, each real embedding of
$u\bar u$ is the squared complex absolute value of an embedding of
$u$; hence $u\bar u$ is a totally positive unit. Conversely,
$\phi^j$ is itself a unit of $\mathcal O_K$, fixed by conjugation,
and

$$
N_{K/F}(\phi^j)=\phi^{2j}.
$$

This proves surjectivity onto the entire positive unit group. $\square$

### Lemma A.2. The two class numbers needed in the argument

One has $h_K=h_F=1$, and $h_F^+=1$.

**Proof.** The discriminants are $d_F=5$ and $d_K=5^3$.
For the latter, the derivative identity for
$\Phi_5(X)=(X^5-1)/(X-1)$, evaluated at its four roots, gives
$$
\prod_{a=1}^4\Phi_5'(\zeta^a)
 =\frac{5^4\prod_{a=1}^4\zeta^{4a}}
        {\prod_{a=1}^4(\zeta^a-1)}
 =5^3.
$$
The discriminant has positive sign in degree four, and
$\mathbb Z[\zeta]$ is the full ring of integers.

Minkowski's ideal-class bound says that every ideal class in a number
field of degree $d$, with $r_2$ complex places and discriminant
$\Delta$, contains an integral ideal of norm at most
$(4/\pi)^{r_2}(d!/d^d)\sqrt{|\Delta|}$.
For $K$ this is

$$
\left(\frac4\pi\right)^2\frac{4!}{4^4}\sqrt{125}
 =\frac{15\sqrt5}{2\pi^2}<2.
\tag{A.6}
$$

Thus every class contains an integral ideal of norm $1$, and $h_K=1$.
For $F$, the corresponding bound is $\sqrt5/2<2$, so $h_F=1$.
For the stated form of Minkowski's bound, see
[A. Sutherland, MIT 18.785, Lecture 14, Theorems 14.13 and 14.15](https://math.mit.edu/classes/18.785/2016fa/LectureNotes14.pdf).

Finally, $1,-1,\phi,-\phi$ realize all four sign pairs at the two
real places of $F$. Multiplying an integral ideal generator by one
of these units makes it totally positive. Hence the ordinary and narrow
class-number-one assertions both hold. $\square$

### Lemma A.3. Polarization orbits correspond to integral ideals

The map

$$
[D_\eta]\longmapsto(\eta)
\tag{A.7}
$$

is a norm-preserving bijection from ample Neron--Severi classes modulo
$\operatorname{Aut}(B,0)$ to nonzero integral ideals of $\mathcal O_F$.

**Proof.** By (A.3), an automorphism multiplies $\eta$ by the
positive unit $u\bar u$, so (A.7) is well defined. If two totally
positive elements generate the same ideal, their ratio is a totally
positive unit. Lemma A.1 expresses that ratio as $u\bar u$, so
they lie in the same orbit. Conversely, Lemma A.2 gives a totally positive
integral generator for every nonzero integral ideal. Its ideal norm is its
positive field norm. $\square$

In particular, $D_1$ is the unique principal polarization class in this
equivalence relation, and it is reachable by $\beta=1$.

## A.3. Integral relative-norm criterion

For a prime ideal $\mathfrak p$ of $\mathcal O_F$, normalize
$v_{\mathfrak p}$ so that it is the exponent in an $F$-ideal
factorization. These are valuations in $F$, not rational-prime
valuations of $n(\eta)$.

### Theorem A.4. Exact integral reachability

For every $\eta\in\mathcal O_F$ with $\eta\gg0$, the following
three statements are equivalent:

1. $[D_\eta]$ is reachable from $[D_1]$ by the operation (A.3).
2. $\eta=\beta\bar\beta$ for some
   $\beta\in\mathcal O_K\setminus\{0\}$.
3. $v_{\mathfrak p}(\eta)$ is even for every prime
   $\mathfrak p$ of $F$ inert in $K/F$.

**Proof.** First, an equality of classes in statement 1 means that
$\eta$ differs from a relative norm by the relative norm of a unit.
The unit can be absorbed into $\beta$, or its inverse can be absorbed,
according to the direction of the orbit equality. Both are integral
units. Hence statements 1 and 2 are equivalent, including exact
equality of the displayed representative rather than just its ideal.

For statement 2 implying statement 3, let $\mathfrak P$ be the unique
prime above an inert $\mathfrak p$. Here the extension is unramified
of residue degree two, and conjugation fixes $\mathfrak P$. Therefore

$$
v_{\mathfrak p}(\beta\bar\beta)
  =2v_{\mathfrak P}(\beta).
\tag{A.8}
$$

These valuations are nonnegative because $\beta$ is integral.

For sufficiency, factor the integral ideal
$(\eta)=\prod_{\mathfrak p}\mathfrak p^{m_{\mathfrak p}}$.
Construct an ideal $\mathfrak A$ of $\mathcal O_K$ prime by prime:

| Behavior of $\mathfrak p$ in $K/F$ | Factorization in $K$ | Exponents chosen in $\mathfrak A$ |
|---|---|---|
| Split | $\mathfrak p\mathcal O_K=\mathfrak P\bar{\mathfrak P}$, $\mathfrak P\ne\bar{\mathfrak P}$ | $m_{\mathfrak p}$ at one of the two primes, $0$ at the other |
| Inert | $\mathfrak p\mathcal O_K=\mathfrak P=\bar{\mathfrak P}$ | $m_{\mathfrak p}/2$ at $\mathfrak P$ |
| Ramified, the unique prime over $5$ | $\mathfrak p_5\mathcal O_K=\mathfrak P_5^2$ | $m_{\mathfrak p_5}$ at $\mathfrak P_5$ |

The inert exponents are integers by statement 3. All chosen exponents
are nonnegative, so $\mathfrak A$ is an **integral** ideal. The table
gives simultaneously

$$
N_{K/F}(\mathfrak A)=(\eta),\qquad
\mathfrak A\bar{\mathfrak A}=(\eta)\mathcal O_K.
\tag{A.9}
$$

In the ramified row the residue degree is one, so the ideal norm of
$\mathfrak P_5^{m}$ is $\mathfrak p_5^{m}$; its product with
its conjugate is $\mathfrak P_5^{2m}$, exactly the extension of
$\mathfrak p_5^m$.

By $h_K=1$, write $\mathfrak A=(\alpha)$. Its generator is
integral because $\alpha\in\mathfrak A\subseteq\mathcal O_K$, and it
is nonzero. Equation (A.9) implies

$$
(\alpha\bar\alpha)=(\eta)\quad\text{as ideals of }\mathcal O_F.
$$

Consequently
$\epsilon=(\alpha\bar\alpha)/\eta$ lies in
$\mathcal O_F^\times$. Both numerator and denominator are totally
positive, so $\epsilon\in\mathcal O_F^{\times,+}$.
Lemma A.1 yields $\epsilon=\phi^{2k}$ for some integer $k$.
Set

$$
\beta=\alpha\phi^{-k}.
\tag{A.10}
$$

Since $\phi^{-k}$ is an integral unit, $\beta$ is still a nonzero
element of $\mathcal O_K$, and

$$
\beta\bar\beta
 =\alpha\bar\alpha\,\phi^{-2k}
 =\eta.
$$

This proves integral sufficiency. $\square$

Theorem A.4 reproduces the inherited scalar-norm criterion in exactly the
domain needed for polarization pullbacks. Its proof constructs an integral
endomorphism and removes the positive unit factor; no local-global norm
principle is an additional premise.

### The ramified place over $5$

The only ramified finite prime of $K/F$ is
$$
\mathfrak p_5=(\sqrt5)\subset\mathcal O_F,\qquad
\mathfrak P_5=(1-\zeta)\subset\mathcal O_K.
$$
One has $\mathfrak p_5\mathcal O_K=\mathfrak P_5^2$,
$\bar{\mathfrak P}_5=\mathfrak P_5$, and residue degree one.
For integral $\beta$, the corresponding valuation identity is
$$
v_{\mathfrak p_5}(\beta\bar\beta)=v_{\mathfrak P_5}(\beta),
\tag{A.11}
$$
so odd valuations are possible.

There is nevertheless a local unit restriction at this ramified place:
conjugation acts trivially on the common residue field $\mathbb F_5$.
If $\beta$ is a unit at $\mathfrak P_5$, the residue of
$\beta\bar\beta$ is a nonzero square. Thus absence of a valuation
parity condition at $5$ is not a claim that every local unit is a local
norm. The global ideal construction and the proved positive-unit
surjectivity establish all the required compatibility for a totally
positive $\eta$ satisfying the other prime conditions.

An exact positive generator of the ramified ideal is supplied by
$$
(1-\zeta)(1-\zeta^{-1})=3-\phi,\qquad N_F(3-\phi)=5.
\tag{A.12}
$$
Multiplication of $1-\zeta$ by the real unit $\phi$ gives
$$
N_{K/F}\bigl(\phi(1-\zeta)\bigr)
 =\phi^2(3-\phi)=2+\phi.
\tag{A.13}
$$
This is the same ideal and the same polarization orbit. In particular,
the unique class of norm $5$ is reachable.

## A.4. Splitting and the exact examples $11$ and $19$

For $p\ne5$, the Galois group of $K/\mathbb Q$ is
$(\mathbb Z/5\mathbb Z)^\times$, Frobenius is the element $p$,
and complex conjugation is $-1$. The resulting splitting is:

| Rational prime | Prime ideals in $F$ above $p$ | Their behavior in $K/F$ |
|---|---|---|
| $p\equiv1\pmod5$ | Two, each of norm $p$ | Both split |
| $p\equiv4\pmod5$ | Two, each of norm $p$ | Both inert |
| $p\equiv2,3\pmod5$ | One, namely $(p)$, of norm $p^2$ | Inert |
| $p=5$ | One, $\mathfrak p_5$, of norm $5$ | Ramified with residue degree one |

For $p\equiv2,3$, Frobenius has order four in $K/\mathbb Q$;
its square is conjugation, explaining the relative inertness over the
degree-two prime of $F$.

### Example A.5. An existing primitive class of norm $19$ is unreachable

Take
$$
\eta_{19}=4+\phi.
$$
Its two real values are $(9+\sqrt5)/2$ and
$(9-\sqrt5)/2$, both positive, and
$$
N_F(4+\phi)=4^2+4-1=19,\qquad \gcd(4,1)=1.
\tag{A.14}
$$
Thus $D_{\eta_{19}}$ is an existing primitive polarization of type
$(1,19)$. Its principal ideal has norm $19$, hence is a prime
ideal $\mathfrak p$ of $F$, with
$v_{\mathfrak p}(\eta_{19})=1$. Since $19\equiv4\pmod5$,
this prime is inert in $K/F$. Theorem A.4 excludes reachability.

For a direct exact check of that inertness, the residue map
$\mathcal O_F\longrightarrow\mathbb F_{19}$ with
$\phi\mapsto-4=15$ has kernel $(4+\phi)$.
Using $\zeta+\zeta^{-1}=\phi-1$, the quadratic for $\zeta$
over this residue field is
$$
T^2-(\phi-1)T+1
 \equiv T^2+5T+1\pmod{19}.
\tag{A.15}
$$
Its discriminant is $2$ modulo $19$. The complete set of nonzero
squares modulo $19$ is
$$
\{1,4,5,6,7,9,11,16,17\},
$$
which excludes $2$. Thus the quadratic is irreducible. This is a
local prime-ideal obstruction to an integral relative norm, rather than
a search that failed to find a generator.

### Example A.6. A reachable primitive class of norm $11$

Take
$$
\beta_{11}=2+\zeta\in\mathcal O_K.
$$
Exact multiplication gives
$$
\begin{aligned}
\beta_{11}\bar\beta_{11}
 &=(2+\zeta)(2+\zeta^{-1})\\
 &=5+2(\zeta+\zeta^{-1})
  =3+2\phi.
\end{aligned}
\tag{A.16}
$$
The real values of $3+2\phi$ are $4+\sqrt5$ and
$4-\sqrt5$, both positive. Furthermore
$$
N_F(3+2\phi)=3^2+3\cdot2-2^2=11,\qquad \gcd(3,2)=1.
\tag{A.17}
$$
Hence $D_{3+2\phi}=\beta_{11}^*D_1$ is primitive, has type
$(1,11)$, and is reachable. Here $\deg\beta_{11}=11$ and
$\deg\lambda_{3+2\phi}=121$.

### Existence of $\lambda_\eta$ versus its norm factorization

For every totally positive integral $\eta$, the map
$\lambda_\eta=\lambda_0m_\eta:B\to B^\vee$ exists as an integral
polarization isogeny, with degree $N_F(\eta)^2$ by (A.2).
The stronger factorization
$$
\lambda_\eta=\beta^\vee\lambda_0\beta,\qquad
\beta\in\mathcal O_K\setminus\{0\},
\tag{A.18}
$$
is equivalent to $\eta=\beta\bar\beta$, because $\lambda_0$
is an isomorphism and (A.1) is injective.

In particular, $\lambda_{\eta_{19}}$ exists and has degree $361$,
while (A.18) is impossible for it. For the norm-$11$ example,
(A.18) holds with the explicit $\beta_{11}$ in (A.16).
The obstruction distinguishes these two assertions about maps on the
fixed abelian surface.

### Corollary A.7. Complete table at prime norm

Let the entries count polarization classes in the equivalence relation
of Section A.0, with $q(D)=p$.

| Rational prime $p$ | Existing primitive classes | Reachable primitive classes |
|---|---:|---:|
| $p\equiv1\pmod5$ | $2$ | $2$ |
| $p\equiv4\pmod5$ | $2$ | $0$ |
| $p=5$ | $1$ | $1$ |
| $p\equiv2,3\pmod5$ | $0$ | $0$ |

**Proof.** By Lemma A.3, existing classes of norm $p$ correspond
exactly to $F$-ideals of norm $p$. Such an ideal must be a
degree-one prime. The splitting table gives the existence counts.
These classes are automatically primitive because a rational content
greater than $1$ would have its square dividing $p$.

For $p\equiv1$, each of the two ideals has its sole nonzero
valuation at a relatively split prime, so Theorem A.4 makes both classes
reachable. For $p\equiv4$, that valuation is $1$ at a relatively
inert prime, so neither is reachable. Equations (A.12)--(A.13) treat
$5$. Finally, the only ideal above a rational prime $p\equiv2,3$
has norm $p^2$, so none has norm $p$. The two split ideals are
distinct and therefore define distinct orbits; no Galois identification
is included in our equivalence relation. $\square$

## A.5. Parity invariants and finite sets of starting classes

### Theorem A.8. The invariant for every finite sequence of allowed steps

For each relatively inert prime $\mathfrak p$ of $F$, define
$$
\epsilon_{\mathfrak p}([D_\eta])
 =v_{\mathfrak p}(\eta)\bmod2.
\tag{A.19}
$$
This is well defined on polarization orbits, and every finite sequence
of operations (A.3) preserves it, with automorphism equivalences allowed
at every stage.

**Proof.** An automorphism changes the parameter by a unit and so changes
no finite valuation. At an allowed step, (A.8) gives
$$
v_{\mathfrak p}(\beta\bar\beta\eta)
 =v_{\mathfrak p}(\eta)+2v_{\mathfrak P}(\beta).
\tag{A.20}
$$
The parity is unchanged. Applying this identity to each step proves the
finite-sequence assertion, including the identity sequence. $\square$

### Theorem A.9. No finite set of starting classes covers all classes

For any finite set of ample classes on this fixed $B$, at least one
primitive ample class is unreachable from every member of the set by
finite sequences of (A.3).

**Proof.** Choose positive integral representatives
$\eta_1,\ldots,\eta_k$ for the starting classes. Let $S$ be the
finite set of rational primes $p\equiv4\pmod5$ dividing at least
one $N_F(\eta_j)$, and put
$M=\prod_{p\in S}p$, with empty product $1$.
Since $5\nmid M$, the Chinese remainder theorem gives an integer
$x>0$ such that
$$
x\equiv0\pmod M,\qquad x\equiv4\pmod5.
\tag{A.21}
$$
It may be taken arbitrarily large. Put $\eta=x+\phi$.
For $x\ge1$ both real values are positive, and its coordinate
content is $1$, so it defines a primitive ample class.
Its positive norm is
$$
N=x^2+x-1\equiv4\pmod5.
\tag{A.22}
$$

No rational prime $p\equiv2,3\pmod5$ can divide $N$.
Indeed, such a $p$ is inert in $F/\mathbb Q$; if it divided
$N_F(\eta)$, its unique prime $(p)$ would divide $(\eta)$.
Then $\eta$ would belong to $p\mathcal O_F$, forcing both
coordinates $x,1$ to be divisible by $p$, a contradiction.
Also $5\nmid N$. Every prime factor of $N$ therefore has
residue $1$ or $4$ modulo $5$. Since $N\equiv4\pmod5$,
some prime $p\equiv4\pmod5$ occurs in $N$ to an odd exponent.

For each $p\in S$, (A.21) gives $N\equiv-1\pmod p$.
Thus the prime just found lies outside $S$. Write
$(p)=\mathfrak p\mathfrak p'$ in $F$.
Primitivity of $x+\phi$ implies that $(\eta)$ is not divisible
by both $\mathfrak p$ and $\mathfrak p'$, because their product
is $(p)$. Hence the odd exponent of $p$ in $N$ occurs
as an odd valuation at exactly one of these two $F$-primes.
Call it $\mathfrak p$. It is inert in $K/F$.

Every starting representative has
$v_{\mathfrak p}(\eta_j)=0$, because $p\notin S$, whereas
$v_{\mathfrak p}(\eta)$ is odd. The invariant (A.19) excludes a
sequence from any starting class to $[D_\eta]$. This construction
uses the Chinese remainder theorem and the stated splitting law; it
needs no theorem on primes in arithmetic progressions. $\square$

### Boundary of the operation: division by rational content

Theorems A.8 and A.9 concern the integral pullbacks (A.3) and
automorphism equivalence. After a step we do not replace
$\eta=x+y\phi$ by
$\eta/\gcd(|x|,|y|)$. Such division is an additional operation
on polarization parameters.

It can change the parity data: the rational parameter $19$ has
valuation $1$ at both primes of $F$ above $19$, whereas its
primitive part $19/19=1$ has valuation $0$ at both.
Thus the parity-invariance proof does not apply to a procedure in which
rational-content division is added as an allowed step.

## A.6. Exact finite audit domain for the single norm-$19$ witness

The impossibility in Example A.5 has already been proved by its prime-ideal
valuation. An auxiliary direct multiplication audit of this one fixed
target can nevertheless be made complete, rather than using an arbitrary
coefficient cutoff.

Write
$$
\beta=x_0+x_1\zeta+x_2\zeta^2+x_3\zeta^3,\qquad
x=(x_0,x_1,x_2,x_3)^{\mathsf T}\in\mathbb Z^4.
$$
Since $\operatorname{Tr}_{K/\mathbb Q}(1)=4$ and
$\operatorname{Tr}_{K/\mathbb Q}(\zeta^j)=-1$ for
$j\not\equiv0\pmod5$, exact expansion gives
$$
2\operatorname{Tr}_{F/\mathbb Q}(\beta\bar\beta)
 =x^{\mathsf T}Gx,\qquad
G=5I-\mathbf1\mathbf1^{\mathsf T},\qquad
\mathbf1=(1,1,1,1)^{\mathsf T}.
\tag{A.23}
$$
The matrix is positive definite: its eigenvalue on the span of
$\mathbf1$ is $1$, and on the perpendicular subspace it is
$5$. Its inverse is
$$
G^{-1}=\frac{I+\mathbf1\mathbf1^{\mathsf T}}5.
\tag{A.24}
$$
Cauchy--Schwarz for the $G$-inner product gives, for each coordinate,
$$
x_i^2
 \le (G^{-1})_{ii}\,x^{\mathsf T}Gx
 =\frac25\,x^{\mathsf T}Gx.
$$
The target $\eta_{19}=4+\phi$ has
$\operatorname{Tr}_{F/\mathbb Q}(\eta_{19})=9$.
Thus any integral solution of $\beta\bar\beta=\eta_{19}$ would
satisfy
$$
x_i^2\le\frac25\cdot18=\frac{36}5<9,
$$
and consequently $x_i\in\{-2,-1,0,1,2\}$ for every $i$.
The box $[-2,2]^4\cap\mathbb Z^4$, containing exactly $5^4=625$
vectors, therefore contains every possible integral preimage of this
specific target.

The auxiliary audit may check all 625 vectors using exact multiplication
in $\mathbb Z[T]/(T^4+T^3+T^2+T+1)$. This appendix specifies and
proves the complete audit domain; it makes no assertion about execution.
Historical auxiliary execution records are outside this mathematical admission.

The conclusions of this module are confined to the fixed complex abelian
surface, its stated automorphism equivalence, and the specified integral
pullback operation. Module B counts the primitive classes reachable from
the principal class under precisely these definitions.
