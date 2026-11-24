# Exact scalar colorings and their Euclidean boundary

Status: NON-CANONICAL, candidate-T for the written mathematical arguments.
Candidate: C-J-EUCLIDEAN-COLOR-BOUNDARY-N. Action layer: L1 scalar arithmetic.
Author: A. M. Thorn / session J-COLOR-20261009.

No theorem below identifies an arithmetic color with physical charge, a
particle, or a native checkpoint coordinate. The two classes in Section 4
are complete as explicitly defined mathematical classes, not as physical
decoder classes. No novelty or independent-agent review is claimed.

## 1. Objects

Put

\[
 O=\mathbb Z[j],\quad K=\mathbb Q(j),\quad
 j=e^{2\pi i/5},\quad J=1+j^2,\quad
 \varphi=-j^2-j^3,\quad \lambda=1-j.
\]

In the specified embedding, phi is positive and satisfies phi^2=phi+1,
phi>1, J phi=j and phi^(-1)=phi-1. These are algebraic identities; the
complex embedding specifies which real root is positive.

For S=O or K and A a subset of Z, let G_A(S) have vertices S and an edge
between distinct x,y exactly when |x-y|=phi^n for some n in A. In particular,
G_{0}(S) denotes A={0}, not A empty. This is the complex scalar embedding of
K, not the Cartesian plane (K intersect R)^2 and not the native state Omega.

A separate graph H_epsilon(S), for 0<epsilon<1, has an edge exactly when

\[
 1-\epsilon<|x-y|<1+\epsilon.
\]

Its adjacency is a different definition. No statement here identifies a
physical measurement uncertainty with this graph.

The external hypothesis E6, used only in Section 6.2, is that the full
Euclidean plane has no proper unit-distance coloring with five labels.
The OpenAI manuscript and Lean source for E6 are identified in SOURCES.md.
The Lean development is not rebuilt here. Sections 2 through 6.1 do not
use E6 or any claimed finite six-chromatic example from that manuscript.

## 2. A local congruence controlling every exact edge

### Lemma 2.1. The local residue

The map

\[
 \rho:O\longrightarrow\mathbb F_5,\qquad
 \rho(a_0+a_1j+a_2j^2+a_3j^3)=a_0+a_1+a_2+a_3\pmod5
\]

is a surjective ring homomorphism with kernel lambda O. Indeed, setting
j=1 in Phi_5(j)=0 gives 5=0, so O/(1-j)O is exactly F5. In particular,
lambda is a prime element. Conjugation satisfies

\[
 \overline\lambda=-j^{-1}\lambda,
\]

so it preserves divisibility by every power of lambda.

For a nonzero integral element a, there is a largest integer k such that
lambda^k divides a. To see finiteness without a factorization assumption,
use the field norm: N(lambda)=Phi_5(1)=5, and N(a) is a nonzero integer.
Divisibility by lambda^k implies divisibility of N(a) by 5^k. Primality
of lambda makes this order additive under multiplication. It therefore
extends to an integer valuation v_lambda on K by subtracting numerator
and denominator orders. It has

\[
 v_\lambda(\bar x)=v_\lambda(x),\qquad
 v_\lambda(\varphi)=0.
\]

The latter follows because phi and phi-1 are inverse elements of O.

Let R be the local ring of elements of K with v_lambda>=0. Equivalently,

\[
 R=\{a/b:a,b\in O,\ \rho(b)\ne0\}.
\]

Cancellation of the numerator and denominator powers of lambda proves the
equivalence. The residue map extends to R by rho(a/b)=rho(a)/rho(b).
Conjugation induces the identity on its residue field.

### Lemma 2.2. Parity of the length exponent

If delta in K has |delta|=phi^n, then

\[
 \delta\bar\delta=\varphi^{2n},\qquad
 v_\lambda(\delta)=0,\qquad
 \rho(\delta)^2=(-1)^n\quad\hbox{in }\mathbb F_5.
\]

The first equality is an equality in K: its selected complex embedding is
injective, so the displayed Euclidean equality implies the algebraic one.
Taking v_lambda gives 2v_lambda(delta)=0. Reduction is now legitimate.
Since rho(phi)=3 and conjugation acts trivially on residues,
rho(delta)^2=3^(2n)=(-1)^n, for positive or negative n alike.
Consequently,

\[
 \rho(\delta)\in
 \begin{cases}
 \{1,4\}=\{+1,-1\},&n\text{ even},\\
 \{2,3\}=\{+2,-2\},&n\text{ odd}.
 \end{cases}
\]

This argument applies to all K directions of the specified length, not only
to roots of unity or integral units.

### Remark 2.3. The field and ring must not be conflated

The exact witness

\[
 u=\frac{2+j}{2+j^4}
   =\frac{12+10j+3j^2+6j^3}{11}
\]

has u bar(u)=1 and rho(u)=1 but does not belong to O. Thus enumerating only
the integral directions would not establish the upper bound for K.
The local argument in Lemma 2.2 is what covers this larger domain.

## 3. Exact chromatic numbers

### Theorem 3.1. The five frozen scale families

For both S=O and S=K,

| Exponents A | Chromatic number of G_A(S) |
| --- | --- |
| {0} | 3 |
| 2Z | 3 |
| 2Z+1 | 3 |
| {0,1} | 5 |
| Z | 5 |

Proof of the upper bounds for O. For even exponents, rho maps every edge
to an edge of the five-cycle with steps +/-1. The palette

\[
 (f(0),f(1),f(2),f(3),f(4))=(0,1,0,1,2)
\]

colors that cycle properly. Hence f composed with rho is a three-coloring.
For odd exponents use f(3 rho(x)); multiplication by 3 changes steps +/-2
to steps +/-1. For arbitrary exponents, rho itself is a proper five-coloring,
since no edge difference has zero residue.

For K, every edge difference is in R, by Lemma 2.2. Thus no edge joins
different additive cosets of R. Choose one representative t for each
coset of K/R, choosing t=0 for R itself, and replace rho(x) by rho(x-t)
on that coset. This is legitimate even at points with negative valuation.
Since K is countable the representatives can, for example, be selected by
the first element of any fixed enumeration. The same palettes prove all
three upper bounds. A globally defined ring residue on all K is not being
asserted.

For the lower bounds, set

\[
 z_k=\sum_{a=0}^{k-1}j^a=\frac{j^k-1}{j-1},\qquad 0\le k\le4.
\]

The five adjacent differences, including the closing edge, are roots of
unity, so their lengths are one. The five diagonal differences have length
phi: for example

\[
 |1+j|^2=2+j+j^{-1}=1+\varphi=\varphi^2.
\]

Differences of three consecutive powers have the same length by
1+j+j^2+j^3+j^4=0. Thus these five points form an odd unit cycle, proving
the lower bound three for {0} and 2Z. The scaled points phi z_k form an odd
cycle of length phi and give the lower bound three for 2Z+1.

Every pair among the original five points is at distance 1 or phi. They
therefore form a complete graph on five vertices for A={0,1}, and also
for A=Z. Five distinct colors are necessary by the pigeonhole principle.
Together with the upper bounds, this proves the table. The construction
lies already in O, hence proves the lower bounds for K as well. QED.

The same scaling argument gives chi(G_{n}(S))=3 for any single n in Z.
The proof does not classify every arbitrary subset A. In particular, it
does not extrapolate from opposite exponent parity to a lower bound five
for every pair of distant scales.

The selected all-scale graph has a proper five-coloring. It has no forced
monochromatic edge. Its need for five colors is a two-length obstruction
to FOUR colors, not an obstruction to five colors at one length.

## 4. Complete classifications in two explicit additive classes

### Theorem 4.1. Scalar charts

Suppose F:O->C is additive and nonzero, and there is one w in C such that

\[
 F(Jx)=wF(x)\qquad\text{for every }x\in O.
\]

Then, and only then,

\[
 F(x)=\kappa\sigma_a(x),\quad \kappa\in\mathbb C^*,\quad
 \sigma_a(j)=j^a,\quad a\in\{1,2,3,4\},\quad
 w=\sigma_a(J).
\]

Proof. The relation j=(J-1)^3 proves O=Z[J]. The minimal polynomial of J is

\[
 P(T)=\Phi_5(T-1)=T^4-3T^3+4T^2-2T+1.
\]

Additivity and covariance give F(p(J)x)=p(w)F(x) for every p in Z[T].
Choose x with F(x)!=0 and apply P to obtain P(w)=0. Its four distinct
roots are sigma_a(J). Moreover F(1) cannot vanish, since O=Z[J] would
then force F=0. For x=p(J), covariance now gives
F(x)=p(w)F(1)=sigma_a(x)F(1). This proves necessity, and direct substitution
proves sufficiency. QED.

With literal equality there are four families indexed by nonzero kappa.
Normalizing F(1)=1 leaves exactly the four embeddings. Further identifying
Galois-related charts is an additional equivalence, not literal equality.
No continuity premise is needed.

After removing the factor |kappa| from lengths, sigma_1 and sigma_4
preserve the exponent n, while sigma_2 and sigma_3 replace it by -n, since
sigma_2(phi)=sigma_3(phi)=-phi^(-1). Conjugation commutes with all four
embeddings. Applying an embedding to delta bar(delta)=phi^(2n) proves
exact equivalence of the corresponding distance relations. These are graph
isomorphisms onto the respective embedded carriers, not merely one-way
edge-preserving maps. Thus this complete chart class cannot turn the
unit graph into a six-chromatic graph or the all-scale graph into one.

### Theorem 4.2. Five-valued additive readers

Suppose h:O->F5 is additive and nonzero and one t in F5 satisfies

\[
 h(Jx)=t h(x)\qquad\text{for every }x\in O.
\]

Then, and only then,

\[
 t=2,\qquad h(x)=b\rho(x),\qquad b\in\mathbb F_5^*.
\]

Proof. As before, O=Z[J] and h(p(J))=p(t)h(1). The value h(1) is nonzero
or h vanishes everywhere. Reducing the polynomial gives

\[
 P(T)=(T-2)^4\pmod5.
\]

Hence t=2. Since rho(J)=2, h(p(J))=h(1)rho(p(J)) for every polynomial.
The converse follows from the ring homomorphism property of rho. QED.

There are exactly four maps in the literal class; h(1)=1 picks rho.
Multiplication by b is an additive output relabeling. Arbitrary permutations
of five labels need not preserve additivity. This is not uniqueness among
all readouts, nonlinear maps, multi-register interfaces, or native machines.

In particular,

\[
 h(jx)=h(x),\qquad h(Jx)=2h(x).
\]

This label is NOT the absolute j-phase. On its values, J fixes zero and
cycles the four nonzero residues. A five-valued alphabet and a five-cycle
of phases are different structures. Nor is h automatically a function on
projective rays: rescaling a representative can change its value.

## 5. Density and a joint arithmetic read

### Lemma 5.1. All five residue fibers are dense

The single complex image of O is dense in C. For a direct proof, write any
z in C uniquely as a+bj with a,b real. For eta=phi^(-N), round a/eta and
b/eta to integers A,B. The point eta(A+Bj) belongs to O and is within eta
of z, because |j|=1. As N increases, eta tends to zero.

Multiplication by nonzero lambda is a homeomorphism of C, so lambda O is
dense too. Each residue fiber r+lambda O is therefore dense in C. This
statement concerns ONE complex embedding, not the full Minkowski lattice
in two complex embeddings.

### Corollary 5.2. The residue cannot be a locally stable position label

At every x in O and in every Euclidean neighborhood of x there are points
of all five residues. Thus rho, considered as a map from the embedded O
with its Euclidean subspace topology to the discrete F5, is discontinuous
at every point. It has no extension that is continuous at even one point
of C. The same holds for b rho and for every nonconstant function of rho.

This does not make rho nonmeasurable on the countable domain O, and does
not say that an internally stored residue cannot be read. It only excludes
recovering it as a locally stable function of this scalar position alone.

### Corollary 5.3. A total joint scalar read and its completion

A fully specified mathematical read on O is

\[
 \mathcal R(x)=(x,\rho(x))\in\mathbb C\times\mathbb F_5.
\]

It is injective, additive, and obeys the exact law

\[
 \mathcal R(Jx)=(Jx,2\rho(x)).
\]

The product construction uses the induced metric

\[
 d_{\mathcal R}(x,y)=|x-y|+\mathbf 1_{\rho(x)\ne\rho(y)},
\]

not the scalar Euclidean metric alone. This additional topology is an
explicit mathematical choice. The closure of its image in the product of
the usual complex topology and the discrete topology of F5 is exactly

\[
 \overline{\mathcal R(O)}=\mathbb C\times\mathbb F_5.
\]

Indeed, Lemma 5.1 approximates every z separately inside each prescribed
residue fiber. The extended update (z,r)->(Jz,2r) is a homeomorphism of
this product. The four scalar-chart families yield the analogous law
(z,r)->(sigma_a(J)z,2r).

On the original exact image, x determines its residue algebraically. In
the product completion, every position occurs with all five labels.
Thus completion destroys recovery of the label from position alone; it
need not destroy an explicitly retained second output. This completion is
a constructed comparison object, not a native physical carrier, topology
of matter, extra spatial dimension, or selected apparatus.

Metric completion followed by recomputation of all unit-distance edges
must also be distinguished from taking the closure of an existing edge
set. The two operations are not assumed to commute.

## 6. What changes when exact length is replaced by an interval

### Theorem 6.1. A prescribed-reader obstruction at every positive tolerance

For n>=1 define

\[
 d_n=1-\varphi^{-4n}\in O.
\]

Then

\[
 0<d_n<1,\qquad d_n\longrightarrow1,\qquad
 \rho(d_n)=1-3^{-4n}=0.
\]

For every epsilon>0, choose n with phi^(-4n)<epsilon. The pair 0,d_n has
the same residue and has distance strictly between 1-epsilon and 1.
It is consequently a monochromatic edge in H_epsilon(O), both for rho
and for every reader factoring through rho. This disproves every positive
uniform distance margin for this reader without leaving O and without E6.

The finite audit includes n=1,...,32. It also certifies the exact rational
windows epsilon=10^(-r), n=2r, r=1,...,12. Their all-r validity is elementary:
phi^4=3phi+2>5, so phi^8>25>10 and phi^(-8r)<10^(-r).
These finite instances are witnesses, not the proof of the all-epsilon
statement.

### Theorem 6.2. Transfer of an arbitrary-coloring obstruction

Let S be any dense subset of C. If the unit-distance graph of C has no
proper q-coloring, for a fixed finite q, then H_epsilon(S) has no proper
q-coloring for every 0<epsilon<1.

Proof. Graph-coloring compactness supplies a finite non-q-colorable
unit-distance graph with distinct vertices p_1,...,p_m in C. For
completeness, this compactness assertion follows by giving the set of all
q-labelings the product topology of finite discrete sets. Each edge
constraint is closed; colorability of every finite subgraph supplies the
finite intersection property. Compactness would then supply a global
coloring. Its contrapositive supplies the required finite graph. This is
a ZFC argument and makes no regularity assumption about colors.

Choose delta>0 smaller than epsilon/3 and than one third of the minimum
pairwise distance among the p_i. Density gives distinct s_i in S with
|s_i-p_i|<delta. For every original unit edge,

\[
 \bigl||s_i-s_k|-1\bigr|
 \le |s_i-p_i|+|s_k-p_k|<2\delta<\epsilon.
\]

Thus all original edges are present in H_epsilon(S); extra edges are
irrelevant. Any q-coloring of the latter would restrict to a q-coloring
of the forbidden finite graph, a contradiction. QED.

Under the explicitly named external hypothesis E6 this yields

\[
 \chi(H_\epsilon(O))\ge6,\qquad
 \chi(H_\epsilon(K))\ge6\qquad(0<\epsilon<1).
\]

This is not an exact computation of either annular chromatic number, not
a claim that six suffice, and not a numerical finite witness extracted
from the external paper. It is a conditional theorem, separate from the
unconditional failure of the selected residue reader in Theorem 6.1.

## 7. Boundary of the result

The all-scale arithmetic graph admits a proper five-coloring and has
chromatic number exactly five. There is no monochromatic defect to name
as a proton. Neither finite color counts nor the product completion imply
a topological charge, an energy cost, localization, conservation, or
persistent physical matter.

The assumptions of the scalar-chart and residue-reader classifications
are substantive. Additivity and one scalar response to J are not derived
as a complete physical interface contract. No map from native Omega to O
is supplied, and the multiplication x->Jx studied here is not silently
identified with the native update U.

A source-to-target graph homomorphism only implies chi(source)<=chi(target).
It cannot transfer a target lower bound to the source. Sections 3 and 4
use explicit colorings, subgraphs, and actual isomorphisms. Section 6.2
uses a finite graph embedding with all required edges present. No stronger
transfer is inferred from pictorial similarity.

A later physical proposal would need its own admitted source map, metric
read, interaction relation, record semantics and named cross-layer gates.
The present note closes none of the registered physical owners.
