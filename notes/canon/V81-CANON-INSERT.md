# Public Canon v81 exact Canon insertion

**NON-CANONICAL / FOLD INPUT.** Insert the body below immediately before
`## 3. The kernel and the census` in the Public Canon v80 `canon/CANON.md`
byte source at content commit `b00171ef21ecb0d905593224f66f5e8a0f6c28e5`.
The eight entries condense the written proofs of the merged public probes
named in `V81-DECODER-INTAKE.md`; the proofs, not this condensation, carry
the universal quantifiers.

The delimiter lines `BEGIN` and `END` are not part of Canon.

<!-- BEGIN V81 CANON INSERT -->

### BINARY-RECORD-VALUATION-NONSELECTION [T]

Let X be a finite set with d elements carrying only equality, let X^k be
its ordered k-tuples for a fixed k>=1, and let simultaneous relabeling act
on every coordinate by one bijection of X. An atomic valuation assigns each
tuple a nonnegative integer weight and is injection-stable when

```text
v_Y(f(t_1),...,f(t_k)) = v_X(t_1,...,t_k)
```

for every injection f:X->Y. Write pi(t) for the equality partition of the
positions, b(pi) for its number of blocks and (d)_r for the falling factorial,
with (d)_0=1 and (d)_r=0 when d<r.

The simultaneous S_d orbits on X^k are exactly the equality partitions with
at most d blocks; the orbit of a partition with r blocks has (d)_r tuples;
every invariant support is a union of orbits. Injection-stable valuations
correspond bijectively to assignments c_pi in N_0, with full-carrier count

```text
W_k(d) = sum_pi c_pi (d)_(b(pi)).
```

The degree of a nonzero valuation is its largest occupied block count. Full
Cartesian counting has every c_pi=1, giving d^k=sum_pi (d)_(b(pi)) without
a power-law assumption. On triples the supports all-equal, first-two-equal
and unconstrained have counts d, d^2 and d^3.

For k=2 the two orbits are the diagonal and its complement, so

```text
W_2(d) = a d + b d(d-1),        a,b in N_0,
W_2(d) = c d^2 for every d  iff  a=b=c.
```

Positivity, additivity over disjoint edge sets, simultaneous relabeling
covariance and injection stability permit every a,b>=0; strict positivity
permits a=1, b=2 with W=d(2d-1). For two unmarked carriers S,T the product
action Sym(S) x Sym(T) is transitive on S x T, so an invariant relation is
empty or complete and unit normalization gives |S||T|. If a bijection f:S->T
is part of the data, relabeling both carriers independently while
transporting f to tau f sigma^(-1) keeps the graph of f and its complement
as two orbits and does not force a=b.

For every nonempty finite symbol set S let B={blank} disjoint-union S, let
tau_s transpose blank and s on B, and put

```text
T(s,r) = (s, tau_s(r)).
```

T is a total involutive bijection of S x B; it preserves the source, sends
(s,blank) to (s,s), is covariant under every relabeling of S, has active
source-to-record graph {(s,s)} of size |S|, and extends to any finite
collection of cells by acting on one addressed cell, so that consecutive
writes to fresh cells preserve every older record and the whole sequence
is invertible. At d=2 the active graph has 2 edges while full Cartesian
incidence on the two active carriers has 4. Binary representation, source
retention, reversibility, covariance and preservation of older records
therefore do not force the full Cartesian count.

On the adopted four-coordinate integer source z with s=sum_i z_i, for every
integer p>=1 put

```text
A_p = |s|^p,     B_p = 5 sum_(i<j) |z_i-z_j|^p,     D_p = A_p+B_p,
```

with normalized pair (A_p/D_p, B_p/D_p) when D_p>0 and no normalized ratio
at z=0. Every member has nonnegative integer branch weights, total zero iff
z=0, LOW zero iff s=0, HIGH zero iff all coordinates are equal, invariance
under coordinate permutations and global sign reversal, degree-p homogeneity
under integer scaling and a scale-invariant normalized pair. Distinct p give
distinct readings: at z=(1,1,0,0), A_p=2^p, B_p=20 and LOW=2^p/(2^p+20) is
strictly increasing in p, equal to 1/11 at p=1 and 1/6 at p=2. The member
p=2 is exactly the adopted A=s^2 and B=5(4 sum_i z_i^2 - s^2).

If B:G x H -> R_(>=0) is additive in each argument on abelian groups then
B=0: additivity gives B(0,h)=2B(0,h) and 0=B(g,h)+B(-g,h) with both terms
nonnegative. Unsigned nonzero pair counting on a positive monoid is therefore
not a nonnegative bilinear law on its signed completion; for raw arrivals
(+1,-1) the unsigned pair count is 4 while the reduced residual count is 0.

The implications "binary arity forces a square" and "reversible faithful
covariant record writing forces complete incidence" are refuted by these
exact examples; at the classified binary scope quadratic selection is
exactly the additional equality a=b. This is an L1 theorem about
equality-only relations, symbolic writers and the listed scalar laws. It
does not classify native relations carrying additional algebraic structure,
does not assert that any member of the power family satisfies complete
rational-frame additivity, the QDD record contract or physical admission,
and supplies no physical apparatus, complete-incidence law, occurrence law,
sampling law or L6 measure. Born's empirical rule, QDD-SIMPLEX-PAIR-INCIDENCE
and every physical QDD owner retain their scopes.

### RECORD-OCCURRENCE-SELECTION-CRITERIA [T]

Let a finite group G act on a finite set R of ready states and a nonempty
finite set E of fine outcomes, with G_r the stabilizer of r and E^(G_r) its
fixed set. An equivariant selector F:R->E, F(gr)=gF(r), exists if and only
if E^(G_r) is nonempty for one representative r of every G-orbit of R; the
complete class is obtained by choosing e_r in E^(G_r) per representative and
setting F(gr)=g e_r, so the number of selectors is the product of |E^(G_r)|
over ready orbits. If E is transitive with |E|>1, no fully symmetric ready
state admits a deterministic equivariant selection of one outcome, and a
deterministic equivariant update cannot lower a stabilizer. The invariant
probability laws on R are exactly the laws constant on each orbit; an
equivariant F pushes an invariant law to an invariant law on E, uniform when
E is transitive, so a declared coarse partition E=disjoint-union E_j then
has P(j)=|E_j|/|E|. Invariance of the input law is an additional premise,
not a consequence of covariance; with several outcome orbits their total
masses remain free.

Let Omega be a nonempty finite set, T a permutation of Omega and
e:Omega->{1,...,r} disjoint-union {SILENT}, observed along e(T^t x) with no
reset, new input or external rule. For a cycle C put l_C=|C|,
m_(C,j)=|{x in C: e(x)=j}| and d_C=sum_j m_(C,j). A start on a cycle with
d_C=0 gives NO_EVENT forever; otherwise the accepted stream is periodic with
period d_C, its accepted frequency is q_(C,j)=m_(C,j)/d_C, and its prefix
count satisfies |K_j(n)-n q_(C,j)|<d_C. Every start has limiting accepted
frequencies q if and only if

```text
d_C>0 and m_(C,j)=q_j d_C for every cycle C and every j.
```

Every stationary law has the form mu(x)=gamma_C/l_C on C with gamma_C>=0
summing to one; the stationary single-tick law conditioned on acceptance is
the mixture of the q_C with weights proportional to gamma_C d_C/l_C, every
such mixture is attained, and uniform mu gives the global counting ratio
without implying cycle balance. For d>=2 the identity dynamics on E with
e(x)=x is reversible and fully equivariant with a uniform invariant law, yet
every realized stream is constant and P(e_t=e_s)=1 for t!=s. Cycling once
through a supplied incidence carrier with branch fibres of sizes d_j gives
d_j^2/sum_i d_i^2 from every start when |E_j|=d_j^2; the cyclic update is
adopted, not derived. The four-state cycle with coarse word 0011 has every
start at frequency 1/2 and, under uniform phase, each adjacent pair at
probability 1/4, while 000 never occurs.

For a closed deterministic autonomous model with N initial states and one
binary output per step: if the first k>=1 outputs have exactly the
independent Bernoulli(p) law with 0<p<1 then the support of the initial law
has at least 2^k states, so no fixed finite model has that law at all
horizons; if the initial law is uniform and p=a/b in lowest terms then b^k
divides N; and for each a,b,k a reversible single cycle on exactly b^k
states, built from an Euler circuit of the b-ary de Bruijn graph, attains
that law through k under uniform phase with every-start frequency a/b and
fails it at k+1. For the adopted source (1,0,0,0) with p=1/16, twenty exact
independent outputs under a uniform finite ready ensemble require N
divisible by 2^80.

This is an L1 theorem about finite selectors, cycles and initial ensembles.
It refutes the implication from reversibility, relabeling covariance and a
uniform stationary ensemble to every-start counting frequencies, and from
correct one- and two-output laws to independence. The finite obstruction
does not apply to native U, whose complete state has an unbounded counter,
nor to an open apparatus with fresh input. It supplies no physical ready
selection, symmetry action, update, event map, realized trial, occurrence
law, sampling law or L6 measure, and it adds no independence requirement to
any physical owner.

### RELATIONAL-GROWTH-SATURATION-BOUNDARY [T]

Pascal's identity gives the exact antidifference
sum_(k=0)^(n-1) binom(k,r)=binom(n,r+1), hence
sum_(k=1)^n (k)_r=r! binom(n+1,r+1) for r>=1. For a fixed arity and the
injection-stable equality-pattern weights c_pi of
BINARY-RECORD-VALUATION-NONSELECTION, the layer count on k labels is
S_k=sum_pi c_pi (k)_(r_pi) and its tagged disjoint accumulation is exactly

```text
V_n = sum_pi c_pi r_pi! binom(n+1, r_pi+1),
```

of degree R+1 with R the largest occupied block count. For binary weights
a,b this is V_n=a n(n+1)/2+b n(n+1)(n-1)/3: every b>0 gives cubic growth,
so cubic accumulation does not select complete incidence, and a=b=1 is the
sum of squares n(n+1)(2n+1)/6. The carrier is the disjoint union with the
layer index retained; forgetting tags leaves the largest layer.

The statement "V_n ~ c n^d implies n(V_n-V_(n-1))/V_n -> d" is false: the
strictly increasing integer sequence V_n=n^3+(-1)^n n^2+n is asymptotic to
n^3, yet its shell ratio is exactly 1 on odd n and tends to 5 on even n.
Sufficient repairs are a polynomial V with positive leading coefficient, an
error e_n=V_n-c n^d with e_n-e_(n-1)=o(n^(d-1)), or eventually monotone
shells, each proved by direct squeezing. Without shell regularity the valid
macroscopic consequences are log(V_n)/log(n)->d and
V_floor(lambda n)/V_n -> lambda^d for each fixed lambda>1. Replacing the
radius by floor(m^alpha) changes the inferred exponent to alpha d.

For a finite group acting on a finite set with a fixed finite generating
set and exact semantic equality, word balls are nested and constant from
radius M-1 on an M-element reachable carrier; their growth exponent is zero
and their tagged accumulation is Mn+constant, of exponent one. This applies
to the registered finite native word group and its finite commutator images;
it is not applied to the complete autonomous U state with its unbounded
counter.

With the displayed fired translations a0=(3,0), b0=(3,3), c0=a0+b0 of
FIRED-COMMUTATOR-NOGO as unit steps, the torsion-free carrier Z^2 has exact
word norm rho(x,y)=max(|x|,|y|,|x-y|) and ball count

```text
H_r = 3r(r+1)+1 = (r+1)^3 - r^3,     sum_(r=0)^n H_r = (n+1)^3,
```

with shells of 6r members and growth exponent two. The native quotient has
ball sizes 1,7,19,25,25,... and tagged accumulation 25n-23 for n>=2, so the
cubes 1,8,27 are followed by 52 rather than 64 at radius three. Interpreting
the same signed affine formulas of b,d,e over Z^6 gives involutions whose
derived group is the free rank-two lattice L=Z t1+Z t2 with

```text
t1=[d,e]=(0,0,0,0,-2,0),   t2=[b,d]=(-5,-5,-5,-5,-2,-2),   [b,e]=t1+t2,
```

acting freely, with reduction modulo five onto the 25 fired translations
and kernel exactly 5L; its nonzero piston translations vanish natively, and
the lift is a declared additional choice. The silent group commutator
[a,c](x)=x+v(r) with v(r)=(-1-r,1+r,-1+r,1-r,0,0) has a five-point native
orbit and an infinite cyclic lifted orbit with balls 2n+1 and tagged
accumulation (n+1)^2; it is a group commutator of state maps, not the
additive Koopman curvature.

This is an L1 theorem about exact counts and their limits. It proves cubic
accumulation in its explicit counting class, falsifies the general inference
from cubic volume asymptotics to the local shell ratio, and excludes the
literal finite native-word route to an asymptotic exponent three. It
supplies no geometric carrier, intrinsic radius, nonduplicating measure,
limit regime, spatial dimension, metric, physical length or decoder bridge,
and the same-carrier curvature bridge remains open.

### U-FINITE-READER-INDEPENDENCE-OBSTRUCTION [T]

For the unchanged origin-zero native U on every one of the 15,625 heads
(0,x_0), with unbounded counter and decorated letters d_n=(x_n,theta_n),
fix a length L>=1 and one function f from legal length-L decorated windows
to {0,1,SILENT}, applied at every tick n>=L+2 with no absolute counter,
growing window, separate memory, changed context, feedback or added input.
Deleting SILENT outputs chronologically yields the accepted word.

The registered chart coding writes each synchronized trajectory as a
length-two morphic image of the primitive length-two substitution on the
100-letter clock alphabet, every letter of which occurs in every depth-77
substituted letter. Consequently the number of distinct length-t native
factors on one chart is at most

```text
p_d(t) <= 20,000 t,
```

and at most 62,500,000 t across all charts. If the reader accepts one legal
window on a chart, that window occurs in every aligned superblock of some
length B=2^(j+78), so acceptance is infinite and consecutive accepted
endpoints differ by at most G=2^(j+79); otherwise the disposition is
NO_EVENT with no accepted ratio, and there is no third case. A block of k
accepted symbols is determined by a native factor of length L+G(k-1), so

```text
p_accepted(k) <= 20,000 [L+G(k-1)].
```

Once 2^k exceeds this linear bound some binary k-word never occurs in the
synchronized accepted tail, while every nondegenerate Bernoulli product
gives it positive weight; the accepted stream therefore cannot have those
block frequencies at all orders, finitely many unsynchronized outputs do not
change this, and for one fixed global reader the finite union over heads is
excluded once 2^k>62,500,000[L+G(k-1)].

No single finite horizon defeats every finite-window reader. For any h>=1
the binary de Bruijn cycle D_h of length 2^h contains every h-word once, so
its all-prefix block frequencies equal the fair product values through h and
fail at h+1; composing the registered phase reader of length 5 2^(h-1) with
D_h gives one fixed finite-window reader that emits D_h[n mod 2^h] on every
origin-zero trajectory after synchronization, with no SILENT output.
Arbitrary explicit counter dependence admits the reader F(n,x)=b_n for any
prescribed sequence, so the bound concerns the fixed finite-window class and
not every reading of the complete carrier.

This is an L1 theorem about the actual native trajectory and a declared
reader class; it is not a finite periodic surrogate and it is distinct from
the driver-only entropy statement. It selects no physical event reader,
resources, preparation, accepted-trial semantics or comparison horizon,
asserts no minimal window or approximate-independence bound, does not
presume that any experiment requires all-order independence, and does not
falsify Born's marginal rule.

### OCCURRENCE-ADDRESS-AND-LOG-EQUALITY [T]

An equivalence relation E on N_0 with n E m implying (n+1) E (m+1) is
equality or has unique mu>=0 and p>=1 with n E m iff n=m or both n,m>=mu
and p divides n-m, giving mu+p classes; adding the cancellation
(n+1) E (m+1) implies n E m leaves exactly equality and reduction modulo p.
The kernel of a deterministic address read h:N_0->A has the successor
property if and only if an autonomous map T on h(N_0) satisfies
h(n+1)=T(h(n)); an arbitrary repeated address need not qualify. On a finite
prefix {0,...,N} there are 1+N(N+1)/2 such relations and N+1 cancellative
ones. Constant addresses, phase tags n mod p and fresh tags n all satisfy
both laws, so homogeneity and cancellation do not select freshness.

Right congruences on finite words are exactly the kernels of pointed
deterministic history readers; two-sided monoid congruences include exact
words, total identification, length modulo p, Parikh counts and occurring
letter sets, and even cancellation of an appended known symbol holds for
length residues and Parikh counts without recovering the history. The
contract that the class of the empty word is a singleton and that
ua E vb implies a=b and u E v forces exact word equality, so repeated equal
payloads occupy distinct positions; the morphism erasing SILENT keeps
accepted multiplicity while losing tick timing.

For a fixed length-L decorated-window reader emitting identity labels or
SILENT on the origin-zero native trajectory, the chart coding and bounded-gap
recurrence of U-FINITE-READER-INDEPENDENCE-OBSTRUCTION give at most 20,000 L
distinct labels per trajectory, each recurring infinitely often with bounded
gaps, at most 62,500,000 L across charts, and at most |A| 20,000 L labels
when a fixed finite apparatus state is also read; a nonempty reader of this
class cannot issue a fresh literal identity at every accepted occurrence,
even with an infinite label codomain. The counter tag (n,id_n) and
accepted-rank tagging are fresh within their enlarged read domains.

An append-only log with at most c atomic entries per tick holds at most
L_0+cN entries after N ticks, sharply, so V fresh entries need at least
ceil(V/c) ticks. On the lifted hexagonal balls B_r of
RELATIONAL-GROWTH-SATURATION-BOUNDARY, with rows of length
ell_r(x)=2r+1-|x| and lexicographic rank k_r(x,y), the map
(r,x,y) -> n=r^3+k_r(x,y) bijects the tagged disjoint union onto N_0 with
the intervals [r^3,(r+1)^3) as layers and an explicit integer inverse, so
one entry per tick completes radius R after exactly (R+1)^3 ticks and c
entries per tick attain ceil((R+1)^3/c); the count is cubic in the chosen
radius and linear in elapsed ticks.

This is an L1 theorem about address quotients, log congruences, a native
reader class and emission budgets. Repeated labels do not prove one physical
event, distinct events identified by external history positions are not
excluded, and the serialization is a chosen enumeration. It selects no
physical Snap, event equality, emission law, persistent record or spatial
radius, and closes no physical owner.

### RECORD-LOADER-RETENTION-CLASS [T]

In the registered reservoir account, a READ leaves the complete state
unchanged while a valid DEPOSIT of zero input energy and zero channel
vectors appends one zero batch; under the projection retaining only the
zero-port amplitudes before and after and their energies, the two
transitions coincide as the tuple (0,0;0,0), so the completed-batch
increment, 0 versus 1, is not a function of that projection: for pi:X->Y
and d:X->D a factorization d=e pi exists iff d is constant on every
pi-fibre. Both transitions emit zero threshold marks.

Let source and record each be Q^m with the same rational positive definite
Gram matrix G. An orthogonal rational W with W(s,0)=(0,s) for all s has
exactly the block form

```text
W = [[0,B],[I,0]],       B^T G B = G,
```

hence W(0,r)=(Br,0): reapplying the same perfect loader exports a stored
nonzero record into the source port. For V=S orthogonal-sum R
finite-dimensional, an orthogonal W with W(R) contained in R satisfies
W(S) contained in S, and the passive condition P_R W(0,r)=r already forces
W(0,r)=(0,r); a rational shear (s,r)->(s,r+s) and the infinite
shift W e_j=e_(j+1) on finitely supported sequences delimit these premises.
With a pointwise protected old bank O and fresh capacity F, an orthogonal W
with W(s,o,0)=(0,o,Js) exists iff a rational isometric embedding J:S->F
exists, realized by the involution

```text
W(s,o,f) = (J^* f, o, J s + (I_F - J J^*) f);
```

dim F>=dim S is necessary but not sufficient over Q, since the form <1> has
no rational isometry into <2>, while (s/2,s/2) embeds <1> into <2,2>.

A cell carrier C={BLANK} disjoint-union {occupied(v): v in Q^m}, with
occupied(0) distinct from BLANK, a head j in Z/N and two length-N arrays
S,R has the single update FLOW swapping S_j with R_j and advancing the head,
a bijection with FLOW^N(j,S,R)=(j,R,S) and FLOW^(2N)=identity, conserving
total occupancy and energy. Its emitter returns (j,v) exactly when the
record cell changes from BLANK to occupied(v). From an all-BLANK record
bank, the first lap records every preloaded arrival once at a distinct
address, including zero payloads, leaves earlier records unchanged, and
emits nothing for BLANK sources or stipulated passive queries; the second
lap empties the records and the third reissues the same addresses. Erasing
the occupancy tag makes a zero arrival and an idle slot indistinguishable,
and the record-energy change s^T G s - r^T G r detects nonzero cold loading
but not a zero arrival or the warm swap (1,-1)->(-1,1).

This is an L1 theorem about the displayed linear couplings, symbolic
carriers and transition classes. It is not a physical bit bound, an energy
cost per event, a nondisturbance certificate or a no-go for larger
controllers, nonlinear storage or additional ports. Which interactions are
records, which queries are passive, how occupancy is realized and how
records persist remain with the physical apparatus owner.

### REGISTRATION-PAIR-RECOVERY-INVERSE [T]

In a discrete renewal model with rational hazard h_k in [0,1] at age k since
the last registration, no further state and independent identically
distributed gaps, put S_0=1, w_k=h_k S_(k-1), S_k=S_(k-1)(1-h_k), u_0=1 and
u_n=sum_(j=1)^n w_j u_(n-j). Then S_k is the weight of no registration
through age k, w_k the first-gap weight and u_n the anchored all-pairs weight
of any registration at lag n; every binary word has weight equal to the
product of its age-path factors, and the three sequences are different
objects. Given rational u_1..u_N with u_0=1, the unique candidate first-gap
prefix is

```text
w_n = u_n - sum_(j=1)^(n-1) w_j u_(n-j),
```

admissible as a renewal prefix iff every w_n>=0 and sum_n w_n<=1; where
S_(n-1)>0 the only compatible hazard is h_n=w_n/S_(n-1), and an age with
S_(n-1)=0 is UNREACHABLE rather than of zero hazard. Finite prefixes do not
identify the stationary intensity, and an arbitrarily normalized or
early-truncated curve does not satisfy the inverse's input contract.

For d dead steps followed by constant hazard a in (0,1], the gaps are
w_n=a(1-a)^(n-d-1) for n>=d+1, the mean gap is d+1/a, the intensity is
lambda=a/(1+da), and the j-th subsequent registration at lag n has weight
binom(n-jd-1,j-1) a^j (1-a)^(n-j(d+1)). For d=1 and a=1/2, lambda=1/3,
u_2,u_3,u_4=1/2,1/4,3/8, the normalized pair values are 3/2, 3/4, 9/8 while
the normalized hazard is already 1, and u_n=1/3+(2/3)(-1/2)^n; the exact
substitution of normalized all-pairs counts for normalized recovery is
false. If h_j=a eta_j with 0<=eta_j<=1 and 0<a<=1 then

```text
|u_k - h_k| <= a(1-S_(k-1)) <= a^2 (k-1),    |u_k/a - eta_k| <= a(k-1),
```

attained at k=2, in units of the admitted opportunity rate rather than the
registration intensity or a finite-lag normalization. For a finite nonzero
hazard prefix with maximum m, every a in [m,1] with eta_j=h_j/a gives the
same registration tree, so opportunity rate and efficiency are not
separately identified by registrations. The period-12 patterns {0,1,4,6}
and {0,1,3,7} under uniform phase have identical absolute pair weights at
every lag, with numerator 4 at lag 0, 2 at lag 6 and 1 otherwise, and the
same intensity 1/3, yet cyclic gaps (1,3,2,6) and (1,2,4,5) with age-3
hazards 1/2 and 0; complete pair data do not certify the renewal premise.

This is an L1 theorem of exact rational coefficient calculus and finite
weighted event trees. It supplies no observation map, absolute scale,
binning, physical opportunity model, detector calibration, admitted
measurement payload or empirical result, asserts no published experiment
wrong, and provides no native source, coupling, record map or physical
registration semantics.

### TRC1-CALIBRATION-IDENTIFIABILITY [T]

For a head h in N_0 x F_5^6, read its first four checkpoint coordinates once
with the balanced lift (0,1,2,-2,-1) to z in {-2,...,2}^4, and fix a context
(Gamma,q,N) with Gamma a finite nonnegative rational field on the even
sublattice of Z^3 with support R, q>0 rational and horizon N>=0. With
s=sum z_i and the five sites y_0..y_4, prepare S(z)=sum_j((z,0)_j-s/5)
delta_(y_j), so that m(z)=z^T G z=||S(z)||^2 with G=I_4-ee^T/5 positive
definite. The fixed stencil with shell weights (6,1,15,1,1)/324 summing to
8/9 defines L, and the cold transition on P=(u,v) is

```text
w_x = [2v_x - (Lv)_x - (1-Gamma_x/2)u_x] / (1+Gamma_x/2),
b_x = -(w_x-u_x)/2  (x in R),      D_x = Gamma_x b_x^2,
P' = (v,w),   heat' = heat + D,   tape' = tape appended with b,
```

with finite rational support at every cut and the exact balance
E(P_t)+sum_R H_x(t)=m(z)/2. Counts C_x=floor(H_x/q) are nondecreasing, every
newly crossed ordinal is emitted once, and one accounting record is emitted
per coupled transition, including zero-crossing batches; rereading a record
appends nothing and administrative END adds no interaction. Induction defines
exactly one complete history through N for every admitted head and context;
z=0 gives N zero-crossing records. Visible packets retain context, relative
cut, crossing category, site multiplicities and ordinal ranges and discard
head identity, signed fields and tape; since deposits are even in z, at
most 313 distinct visible histories occur per context and horizon. A
preparation ensemble p on finitely many heads, drawn once, pushes forward to
Pr(prefix=y)=sum_i p_i 1[v_i=y], normalized and prefix-consistent.

For rational calibration rows A and validation rows B on the same finite
head list, with C the matrix A extended by the all-ones row, the following
are equivalent: Ap=Aq implies Bp=Bq for all probability vectors p,q; ker C
is contained in ker B; every row of B lies in the row space of C; B=KC for
a rational K. When the inclusion fails, a rational d with Cd=0 and Bd!=0
yields two strictly positive interior mixtures with equal calibration and
predictions differing by 2 epsilon Bd. For the heads e0=(1,0,0,0) and
e1=(0,1,0,0), both have total 4/5, LOW weight 1/20, HIGH weight 3/4 and
normalized weights (1/16,15/16); at origin conductance 1, horizon 1 and
q=1/16 the first-origin row (1421,-349,-349,-349)/1620 gives deposits
1421^2/4860^2 and 349^2/4860^2, hence counts 1 and 0, and the mixtures
(1/3,2/3) and (2/3,1/3) share the scalar calibration while predicting
crossing probabilities 1/3 and 2/3. For e0 against 2e0 at q=1/8 the counts
are 0 and 2 although normalized weights agree. Appending the calibration row
(1,0) restores full rank and determines every prediction on that pair. The
inherited obstruction survives: on z_H=(1,-1,0,0) and z_L=(1,1,1,1) the
first origin form is strictly positive while the LOW and HIGH targets vanish
respectively, so no state-independent complete nonnegative two-output
processing recovers both targets, and ensemble averaging does not repair
this pointwise contradiction.

This is a conditional L1 theorem about the composed mathematical record
chain and its finite-ensemble identifiability. The source design, lift,
context, one update per counter label, fresh cold slots and the preparation
ensemble are choices. It supplies no physical preparation law, port, clock
or observable identification, realization certificate, reset satisfying the
apparatus contract, independent occurrence law, frequency convergence, Born
derivation or admitted measurement payload.

<!-- END V81 CANON INSERT -->
