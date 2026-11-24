# Reading a quadratic character from squared moduli

**NON-CANONICAL. Status for each numbered result: candidate-D. Authority: none.**
This is an arithmetic derivation for the public candidate. The earlier
[C-SPLIT-UNIT-1, T1 and T5](../incubation-import-2026-08-21/C-SPLIT-UNIT/C-SPLIT-UNIT-1.md)
already gives the modulus character and the prime-five coincidence of its
kernel with the conjugation subgroup. The questions here concern extraction
from an integer coordinate, rigidity of a difference of two squared moduli,
and products along doubling cycles. No historical priority is claimed.

## 1. Integer extraction at five [candidate-D]

Let $j$ be a primitive fifth root, $J=1+j^2$, and $J_n=1+(J-1)^n$ for
$n\in\mathbb Z$. Thus $J_n=1+j^{2n}$. Put
$$
 A(n)=J_n\overline{J_n}=2+j^{2n}+j^{-2n},\qquad
 t=j+j^{-1}.
$$
Complex conjugation is taken in the cyclotomic field. The identity
$1+j+j^2+j^3+j^4=0$ gives $j^2+j^{-2}=-1-t$ and
$t^2=1-t$. The two embeddings of $\mathbb Q(t)$ exchange $t$ and $-1-t$.
Write $\sigma_s$ for the automorphism $j\mapsto j^s$ when $5\nmid s$.

Every $A(n)$ has a unique expression $u_n+v_nt$ with integer coefficients.
Indeed $A(n)$ equals $4$, $1-t$, or $2+t$ according as $n$ belongs to
$0$, $\{1,-1\}$, or $\{2,-2\}$ modulo five. These values follow from
the two displayed real periods. Uniqueness follows from the irreducibility of
$X^2+X-1$ over $\mathbb Q$. Define
$$
 D(n)=A(2n)-A(n),\qquad \delta=D(1)=1+2t.
$$
Since $A(2n)=\sigma_2(A(n))$ even at $5\mid n$, subtraction yields
$$
 D(n)=-v_n\delta,\qquad \delta^2=5,\qquad R(n)=D(n)/\delta=-v_n.
$$
Thus a single integer coordinate of the input $A(n)$ gives the sign, including
zero at every multiple of five. Radical extraction and an input character table
are both unnecessary.

To see the multiplication law directly, let $s$ be a unit modulo five.
Then $D(sn)=\sigma_s(D(n))$. Since $R(n)$ is rational,
$$
 D(sn)=R(n)\sigma_s(\delta)=R(n)D(s).
$$
Division by $\delta$ proves $R(sn)=R(s)R(n)$. If $5\mid s$, both sides
vanish, so the law holds for all integers. The kernel on units is
$\{1,-1\}$, exactly the squares modulo five. Consequently $R(n)$ is the
usual quadratic residue character $\chi_5(n)$ extended by zero. This
identification comes after extraction and the multiplication law.

The unnormalized gap depends on the specified embedding. If
$j=\exp(\pm2\pi i/5)$, then $t=2\cos(2\pi/5)>0$ and
$\delta=+\sqrt5$. With the other primitive pair $\delta=-\sqrt5$.
Thus $D(n)=\delta\chi_5(n)$ works in every embedding. Under either choice
the two nonzero-index squared moduli have sum $3$ and product $1$, by
$(1-t)(2+t)=1$.

## 2. The branches and their doubling cycles [candidate-D]

Let $q$ be an odd prime, $\zeta$ a primitive $q$th root, and write
$$
 G=\mathbb F_q^\times/\{\pm1\},\quad m=(q-1)/2,\quad
 K=\mathbb Q(\zeta+\zeta^{-1}),\quad e_s=\zeta^s+\zeta^{-s}.
$$
The polynomial $\Phi_q(X)=1+\cdots+X^{q-1}$ is irreducible over
$\mathbb Q$ by Eisenstein after translating $X$ by one. Hence the
cyclotomic field has degree $q-1$, and the maps $\zeta\mapsto\zeta^s$
for $s\ne0$ give all automorphisms. The extension over $K$ has degree
two since $\zeta$ is nonreal and satisfies $X^2-e_1X+1=0$.
The Galois group of $K/\mathbb Q$ is $G$, with its regular action by
index multiplication on the distinct $e_g$, $g\in G$. Indeed $e_s=e_t$
makes $\zeta^s$ a root of $(X-\zeta^t)(X-\zeta^{-t})$, hence
$s=\pm t$ modulo $q$.

Define $A_q(n)=|1+\zeta^{2n}|^2=2+e_{2n}$. There are exactly $m$
distinct squared moduli on nonzero indices. The additional value
$A_q(0)=4$ occurs only at zero modulo $q$, as $e_{2n}=2$ forces
$\zeta^{2n}=1$. Multiplication of indices by two acts on $G$ with
$$
 d=\operatorname{ord}_G([2])
   =\min\{k>0:2^k\equiv\pm1\pmod q\}
$$
as the length of every cycle. There are $m/d$ cycles. The action is the
identity precisely when $q=3$. A nonidentity involution requires
$4\equiv\pm1\pmod q$ and $2\not\equiv\pm1\pmod q$, which singles
out $q=5$. This uniqueness concerns the multiplier two. More generally
$G$ is cyclic, and has one element of order two whenever $m$ is even.

## 3. Rigidity of every difference of two branches [candidate-D]

Choose $a,b\in\mathbb F_q^\times$ with $b\ne\pm a$. Define
$$
 D_{b,a}(n)=A_q(bn)-A_q(an),\qquad
 U(n)=\frac{D_{b,a}(n)}{D_{b,a}(1)}.
$$
The denominator and all gaps at nonzero indices are nonzero by Section 2.
For units $s,n$ one always has
$$
 U(sn)=U(s)\sigma_s(U(n))
$$
by applying $\sigma_s$ to the numerator and denominator. This identity,
usually called the cocycle identity, retains the Galois action on the
second factor. We ask exactly when that action can be omitted for all pairs.

The element $D=D_{b,a}(1)$ has $m$ distinct conjugates. To prove this,
represent it as a polynomial in $\zeta$ with exponents reduced to
$0,\ldots,q-1$. The coefficients are $+1$ at $\{2b,-2b\}$,
$-1$ at $\{2a,-2a\}$, and zero elsewhere. All four displayed positions
are distinct. The difference of this representative and the representative
of $\sigma_s(D)$ has constant coefficient zero. If it vanishes at
$\zeta$, it is a rational multiple of $\Phi_q$ by its degree bound.
Its constant coefficient forces that multiple to vanish. Thus
$\sigma_s(D)=D$ requires $\{2bs,-2bs\}=\{2b,-2b\}$, which is
equivalent to $s=\pm1$. The stabilizer in $G$ is trivial and $D$ generates
$K$ over $\mathbb Q$.

If $U$ is multiplicative on $\mathbb F_q^\times$, its finite real
multiplicative image lies in $\{1,-1\}$. All $m$ conjugates of $D$
then lie in $\{D,-D\}$. The existence of two distinct branches forces
$m\ge2$. Hence $m=2$ and $q=5$. Conversely for $q=5$ the unique
nonidentity element of $G$ exchanges the two branches. It sends $D$ to
$-D$ for either ordering, giving the nontrivial sign character. Extending
by zero yields complete multiplicativity on $\mathbb Z$. This proves
rigidity for every nonzero-index pair.

A single sign reversal in a larger field does not suffice. The same
coefficient argument shows $\sigma_s(D)=-D$ exactly when $s$ exchanges
the two branch classes. Equivalently $[s]=[b/a]$ and $[b/a]$ has order
two in $G$. The remaining conjugates still prevent a multiplicative
normalization when $m>2$. If $a=\pm b$, the proposed denominator vanishes.
If exactly one endpoint is zero, all gaps on units have the same strict
sign, since $A_q(g)<4$. Multiplicativity would force their normalized
values all to be $1$, possible only for $q=3$, with one nonzero branch and
the trivial character on its unit group.

### Size of a nonzero gap [candidate-D]

The gap admits a factorization that also determines its absolute norm.
Set $S_c=\zeta^c-\zeta^{-c}$. Direct multiplication gives
$$
 D_{b,a}(1)=S_{b+a}S_{b-a}.
$$
For any nonzero $c$, the absolute norm of $S_c$ from
$L=\mathbb Q(\zeta)$ is $q$, since $S_c$ is a root of unity times
$1-\zeta^{2c}$ up to sign, and $\Phi_q(1)=q$. As $D\in K$ and
$[L:K]=2$, this yields $|N_{K/\mathbb Q}(D)|=q$.
Also each $1-\zeta^k$ for $k\ne0$ is $1-\zeta$ times an algebraic
integer of norm one, by the geometric series and equality of norms.
Therefore $U(n)$ on units is a quotient of products of such units and
roots of unity, hence itself an algebraic unit in $K$.

For the sign, use representatives $1\le i\le m$ of $G$. Reducing $ci$
to a signed representative introduces $r$ minus signs. Multiplication of
the congruences $ci\equiv\pm\pi(i)$ and cancellation of $m!$ gives
$c^m\equiv(-1)^r\pmod q$, where $\pi$ permutes the representatives.
Euler's criterion identifies $(-1)^r$ with the quadratic residue sign
$(c/q)$. Thus $\prod_i S_{ci}=(c/q)\prod_i S_i$. Now
$\prod_{i=1}^m S_i^2=(-1)^m q$: pair $S_i$ with $S_{-i}=-S_i$ in
$\prod_{k=1}^{q-1}S_k=q$, the latter identity also following from
$\Phi_q(1)=q$. Consequently
$$
 N_{K/\mathbb Q}(D_{b,a}(1))=q\left(\frac{a^2-b^2}{q}\right).
$$

## 4. Shortest product and reciprocal pairs [candidate-D]

Among multisets of nonzero branch indices, a product of exactly $r>0$
squared moduli can equal one if and only if $d\mid r$. To see necessity,
the evaluation $\zeta\mapsto1$ gives a ring map
$\mathbb Z[\zeta]\to\mathbb F_q$ since $\Phi_q(1)=q$.
Under this map every $A_q(g)$ becomes $4$. A product equal to one requires
$4^r\equiv1\pmod q$. As $\mathbb F_q$ is a field, this is equivalent
to $2^r\equiv\pm1\pmod q$, hence to $d\mid r$.

For sufficiency set $B(g)=|1-\zeta^{2g}|^2$. On $G$ these quantities
are positive and
$$
 A_q(g)=\frac{B(2g)}{B(g)}
$$
by $1-x^2=(1-x)(1+x)$. The product over one full doubling cycle is one
by cancellation. Repeating the cycle realizes every positive multiple of
$d$. In particular two distinct branches can be reciprocal only at
$q=5$. Indeed a product of length two forces $q\mid 4^2-1=15$.
At $q=3$ the only branch equals one. At five the doubling cycle consists
of both branches. This argument applies to any reciprocal pair.

## 5. All integer product relations [candidate-D, using Franz's lemma]

Write $z_g\in\mathbb Z$ for the exponent of branch $g\in G$. Then
$$
 \prod_{g\in G} A_q(g)^{z_g}=1
 \quad\Longleftrightarrow\quad z_{2g}=z_g\quad(g\in G).
$$
The reverse implication is cycle cancellation. For necessity regroup the
left side as $\prod_h B(h)^{c_h}$, where $c_h=z_{h/2}-z_h$ and $h/2$
denotes multiplication by $[2]^{-1}$ in $G$. Thus $\sum_h c_h=0$.
For $j\in\mathbb F_q^\times$ put $a_j=c_{[j/2]}$. These are integers,
$a_j=a_{-j}$ and $\sum_j a_j=2\sum_h c_h=0$. On expanding $B(h)$
the assumed equality becomes
$$
 \prod_{j=1}^{q-1}(\zeta^j-1)^{a_j}=1.
$$
The sign change from $1-\zeta^j$ to $\zeta^j-1$ cancels. Negative
exponents are legitimate since every factor is nonzero. Every nonidentity
$q$th root is $\zeta^s$ for a unit $s$. Applying the corresponding field
automorphism gives the same equality with $\zeta$ replaced by any such
root and the same integer exponents. These are precisely the symmetry,
zero-sum and all-roots hypotheses of Franz's independence lemma, which
forces $a_j=0$ for every $j$. Thus $c_h=0$ for every $h$.

The relation lattice consequently has a basis given by the indicator
vectors of the $m/d$ doubling cycles. The multiplicative group generated
by the squared moduli is free abelian of rank $m-m/d$: on each cycle the
all-ones vector is primitive and can replace one coordinate vector in
an integral basis. A multiset with product one contains equal
multiplicities at every position of a cycle, independently for each cycle.
Section 4 determines the possible lengths without using Franz's lemma.

The cited independence result is Wolfgang Franz, *Über die Torsion einer
Überdeckung*, J. reine angew. Math. **173** (1935), 245–254. Milnor states
it as Lemma 12.6 on printed p. 406 of *Whitehead Torsion*, with its
group-algebra convention on pp. 404–405. For prime $q$ his algebra is
$\mathbb Q[X]/(\Phi_q)$. Under that convention the two factors at
indices $j,-j$ differ by a signed group element. Lück, *A Basic
Introduction to Surgery Theory* (2004), Lemma 2.39 on printed p. 46,
gives the symmetric all-roots formulation used above.
[Franz](https://doi.org/10.1515/crll.1935.173.245) ·
[Milnor](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorwh.pdf) ·
[Lück](https://www.math.uni-bonn.de/people/lueck/data/ictp.pdf)

## 6. Which rational linear combinations give a sign? [candidate-D]

The obstruction for a two-term difference is sharp. For $q\equiv1\pmod4$
a sign can be read from a linear combination of all $m$ squared moduli.
Moreover, the normalized nontrivial sign determines that homogeneous
rational linear combination up to scalar. For $q\equiv3\pmod4$ no such
nontrivial sign occurs on $G$.

First $\{e_g:g\in G\}$ is a rational basis of $K$. In a putative
dependence the representative polynomial has zero constant term, so the
$\Phi_q$ argument of Section 3 gives zero at each coefficient. Also
$\sum_g e_g=-1$. Suppose $\sum_g c_g A_q(g)=0$, and let
$C=\sum_g c_g$. In the $e_g$ basis this equality says $c_g=2C$ for
every $g$ and hence $(2m-1)C=0$. Thus $\{A_q(g):g\in G\}$ also
forms a rational basis.

The group $G$ is cyclic. Choose a generator $h$. If $m$ is odd, every
homomorphism $G\to\{1,-1\}$ is trivial. If $m$ is even, put
$$
 T=\sum_{k=0}^{m-1}(-1)^k A_q(h^k).
$$
Then $T\ne0$ by the basis property and $\sigma_h(T)=-T$. The normalized
orbit $\sigma_s(T)/T$ is the unique nontrivial sign on $G$. Conversely
any nonzero $W=\sum_k c_k A_q(h^k)$ whose normalized orbit is nontrivial
and multiplicative must satisfy $\sigma_h(W)=-W$, so $c_{k-1}=-c_k$ at
each position. Therefore $W$ is a rational multiple of $T$ and necessarily
uses all $m$ basis elements. This support bound refers specifically to
homogeneous rational linear combinations of the displayed basis.

Finally $T^2=q$. The constant terms cancel in $T$, leaving the same
alternating sum of $e_{2h^k}$. For a nonzero class $i$ the trace
$\operatorname{Tr}_{K/\mathbb Q}(e_i)=-1$ follows by summing its
orbit. From $e_i e_j=e_{i+j}+e_{i-j}$ and $e_0=2$, the trace of this
product is $q-2$ on the diagonal of the basis and $-2$ off diagonal.
The coefficients of $T$ have sum zero and sum of squares $m$, giving
$\operatorname{Tr}_{K/\mathbb Q}(T^2)=qm$. Since $T^2$ is fixed by
$\sigma_h$, it is rational and the same trace is $mT^2$.
At five this alternating sum has exactly two terms and recovers the gap
in Section 1 up to sign.
