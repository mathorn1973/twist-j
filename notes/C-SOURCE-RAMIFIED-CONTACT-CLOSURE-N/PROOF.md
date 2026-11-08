# Native free phase and the exact precision of a continuing work contact

PUBLIC / NON-CANONICAL / L1. Authored conditional candidate-T.
Author: A. M. Thorn. Apache-2.0. No scientific execution.

This proof follows the analytical contract pinned at
[`c47f97f0a35d4cffce412ac48150ae6ef80d3963`][pin]. The direct inputs are
the actual native architecture and integer field of [Public Canon v103][canon]
and the explicitly selected complete work law of [#1612][work].
The contract discloses the prior manual exposure of the arguments.

The result has two positive parts. A fixed reading of actual native
pistons and the existing counter realizes the five free source phases.
Separately, six ramified digits give an exact representation of the entire
specified energy-34 work machine, including occupied resources and all
future contacts. Five digits do not suffice on that whole machine.
Neither part admits the selected work law as an original-native operation.

## 1. Fixed algebra and the direction of the field identification

Write

\[
O=\mathbb Z[j],\qquad 1+j+j^2+j^3+j^4=0,\qquad
\lambda=1-j,\quad J=1+j^2.
\]

The direction of the identification is

\[
\iota:O\longrightarrow\mathbb Z^4,\qquad
\iota(\alpha)=J_{\rm cyc}\,\operatorname{coeff}_{1,j,j^2,j^3}(\alpha),
\]

where the literal matrices are

```text
Jcyc=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]],
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
Bf=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
L=(I-A)(I-A^2),
Bstar(a,b,c,d)=(-c,-d,-a,-b).
```

Here A is the field matrix A_f, not the resource-swap layer used below.
Since det Jcyc=-1 and A Jcyc=Jcyc Zcyc, where Zcyc is multiplication by
j in this basis, iota is an integral isomorphism and

\[
A\iota(\alpha)=\iota(j\alpha),\qquad A^5=I,\qquad
L\iota(\alpha)=\iota\bigl(\lambda^2(1+j)\alpha\bigr).
\tag{1}
\]

We will use the exact unit identities

\[
(1+j)^{-1}=-j-j^3,\qquad J^{-1}=-j-j^2,\qquad
\lambda^4=5J^2,\qquad J(1+j)=-j^4.
\tag{2}
\]

For example, the difference between the expansions of lambda^4 and 5J^2
is -4(1+j+j^2+j^3+j^4), hence zero. In particular

\[
(5)=(\lambda^4),\qquad O/(\lambda)\cong\mathbb F_5,
\qquad \rho(j)=1,
\tag{3}
\]

where rho denotes reduction modulo lambda, not a Hermitian norm. Each
successive ideal quotient has five elements. For nonzero alpha the
integer nu_lambda(alpha) is its finite order of divisibility by lambda.

Define I_s=iota(lambda^s O), also allowing I_0=Z^4. Because 1+j is a
unit, (1) gives

\[
I_{2r}=L^r\mathbb Z^4,\qquad
I_{4k}=5^k\mathbb Z^4,\qquad I_{4k+2}=5^k L\mathbb Z^4.
\tag{4}
\]

The canonical integer-image calculation is

\[
\Lambda:=L\mathbb Z^4
=\{(a,b,c,d):a+2b\equiv c+2d\equiv0\pmod5\}.
\tag{5}
\]

### Positive energy and its exact similarity

The energy is

\[
H(a,b,c,d)=\tfrac12 y^T B_f y
=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd.
\tag{6}
\]

It is integer on Z^4 and positive definite. An explicit check is useful:
with x=(a,b)^T, w=(c,d)^T and Q=[[2,-1],[-1,3]],

\[
H=\left\|w+\tfrac12 Qx\right\|^2
 +\tfrac14 x^T(5I-Q)x,\qquad
5I-Q=\begin{pmatrix}3&1\\1&2\end{pmatrix}>0.
\tag{7}
\]

Here Q^2=5Q-5I. Thus H(z)>=1 for every nonzero integer z. Substitution
of the displayed A gives A^T Bf A=Bf. Its energy adjoint is A^*=A^-1.
Equations (1)--(2) give L^2=5A^3, while
L^*=(I-A^-2)(I-A^-1)=A^-3 L. Consequently

\[
H(Ay)=H(y),\qquad H(L^r y)=5^r H(y),\quad r\ge0.
\tag{8}
\]

This is the declared field energy. No physical normalization is inferred.

## 2. The fifth digit is exactly the free phase and the waiting datum

Let

\[
v_0=(2,-1,0,0),\qquad v_a=A^a v_0,
\qquad \alpha_a=\iota^{-1}(v_a),\quad a\in\mathbb F_5.
\]

Expansion and the displayed basis give

\[
\alpha_0=6+2j+3j^2+4j^3=j^3\lambda^3,
\qquad \alpha_a=j^{a+3}\lambda^3.
\tag{9}
\]

For distinct a,b modulo five,

\[
\alpha_a-\alpha_b=j^{b+3}\lambda^3(j^{a-b}-1).
\]

Choosing a-b in {1,2,3,4}, the last factor is
-lambda(1+j+...+j^(a-b-1)); its second factor reduces to a-b, which is
nonzero in F5. It therefore has exactly one lambda factor. This proves

\[
\boxed{\nu_\lambda(\alpha_a-\alpha_b)=4\quad(a\ne b).}
\tag{10}
\]

All five phases coincide modulo the ideal (lambda^4)=(5) and are different
modulo lambda^5. Precision five is the minimum within this sequence of quotient
readings that distinguishes the prepared family.

On the entire coset C=alpha0+lambda^4 O define

\[
\ell(\alpha)=\rho\left(\frac{\alpha-\alpha_0}{\lambda^4}\right).
\]

Multiplication by j preserves C and

\[
\ell(j\alpha)=\ell(\alpha)-1,\qquad
\boxed{\ell(\alpha_a)=-a\pmod5.}
\tag{11}
\]

Indeed (j-1)alpha0/lambda^4=-j^3 reduces to -1. Equivalently,

\[
\boxed{\alpha_a\equiv\alpha_0+5a\pmod{\lambda^5}.}
\tag{12}
\]

To check the sign, j^a=(1-lambda)^a is 1-a lambda modulo lambda^2,
so alpha_a-alpha0 is -a lambda^4 modulo lambda^5. Equation (2) and
rho(J^2)=4 turn this into 5a modulo lambda^5. The digit relative to
lambda^4 is -a, whereas the coefficient relative to 5 is a.

The literal field/contact values from (6) and
Delta=f(c,d)-f(a,b), f(a,b)=(a-b)^2+b^2, are

| a | v_a | H | Delta |
|---:|---|---:|---:|
| 0 | (2,-1,0,0) | 15 | -10 |
| 1 | (2,-1,-5,5) | 15 | 115 |
| 2 | (-3,4,5,-10) | 15 | 260 |
| 3 | (2,-6,-5,10) | 15 | 225 |
| 4 | (-3,4,5,-5) | 15 | 60 |

At resource r=0, exactly phase zero accepts. Thus, on these five
preparations, the least nonnegative value d_a=[-a]_5 of ell is the number
of free waiting steps before the emitting phase. Section 9 proves this
as a statement about the complete chain and its actual receiver.

This is not a guard formula on every lift of the same fifth-digit value.
For example, iota(lambda)=(-1,0,2,-1), and

\[
v_0+5\iota(\lambda)=(-3,-1,10,-5)
\]

has the same residue modulo I_5 as v0 but Delta=245. It refuses at r=0.
The preparation restriction in the digit/guard identification is essential.

## 3. A literal native source for the free family

Use the actual six-coordinate checkpoint
psi=(p1,p4,p1',p4',q,r), with all its coordinates in F5. The generators
needed for an entirely explicit calculation are

```text
a(psi)=(p4,p1,p4',p1',q,r),
b(psi)=(-p1',-p4',-p1,-p4,-q,-r),
c(psi)=(-p1'+2,-p4'+1+r,-p1+2,-p4+1-r,1-q,-r),
d(psi)=((2,1,3,4)-p,1-q,1-r),
e(psi)=((2,1,3,4)-p,2-q,1-r).
```

In the last two lines p denotes the ordered four-piston vector. The
autonomous law remains

\[
U(n,\psi)=(n+1,g_{z(\psi)+2\theta_n}(\psi)),\quad
\theta_n=s_2(n)\bmod2,\quad z=\sum\psi\pmod5.
\tag{13}
\]

### Five source-only preparations and their retained payload

Prepare at the common counter zero

\[
\xi_a=(a,-a,0,0,0,0),\qquad a\in\mathbb F_5.
\tag{14}
\]

The common drive values at steps 0,1,2 are 0,1,1. The actual selected
letters are a,c,e, and direct substitution gives

| Native cut n | Actual checkpoint psi_n(xi_a) | z |
|---:|---|---:|
| 0 | (a,-a,0,0,0,0) | 0 |
| 1 | (-a,a,0,0,0,0) | 0 |
| 2 | (2,1,2+a,1-a,1,0) | 2 |
| 3 | (0,0,1-a,3+a,1,1) | 1 |

The set z in {1,4} is invariant for both possible drive bits. On it only
b,d,e can be selected. All three negate p1+p1': for d and e the constant
is 2+3=0 in F5. Therefore on these native histories, for every n>=3,

\[
(-1)^{n-3}(p_1+p'_1)=1-a.
\]

The fixed current-state function

\[
\widehat a(n,\psi)=1-(-1)^{n-3}(p_1+p'_1)\in\mathbb F_5
\tag{15}
\]

recovers the original a and is invariant under each subsequent actual U.
No saved history or newly stored counter is used.

The entire (z,q,r) history is common to all five preparations. This
follows by induction from their common initial (0,0,0) and the exact
closed factor

| Letter | (z,q,r) after the letter |
|---|---|
| a | (z,q,r) |
| b | (-z,-q,-r) |
| c | (2-z,1-q,-r) |
| d | (2-z,1-q,1-r) |
| e | (3-z,2-q,1-r) |

The selector uses only z and the common counter. The distinct payload is
actually present in the pistons, rather than recoverable from that common
factor. At cut three the difference is
(0,0,-(a-b),a-b,0,0).

### Exact free-phase factor and clocked embedding

On the declared native histories at n>=3 set

\[
Y(n,\psi)=A^{[\widehat a(n,\psi)+n-3]_5}v_0.
\tag{16}
\]

Invariance of the payload and A^5=I prove

\[
\boxed{Y(U\omega)=AY(\omega),\qquad
Y(3,\psi_3(\xi_a))=v_a.}
\tag{17}
\]

Under iota^-1 its exact O-valued reading is
j^(widehat a+n) lambda^3. Its reduction modulo lambda^5 is, equivalently,

\[
[\alpha_0+5(\widehat a+n-3)]_{\lambda^5}.
\tag{18}
\]

Thus the extra ramified datum has a concrete native provenance: the
pistons retain its initial offset, and the existing counter supplies its
advance. The phase reference at n=3 and this output family are selected
parts of the reading contract.

There is also an actual initialized embedding of the clocked phase
space. Write psi_n(xi) for the actual checkpoint after n native steps and
define, for m>=0 and b in F5,

\[
\mathcal E(m,b)=\bigl(m+3,\psi_{m+3}(\xi_{b-m})\bigr).
\tag{19}
\]

Different m have different native counters. At the same m the recovered
payload b-m distinguishes b, so E is injective. Both sides of

\[
\boxed{U\mathcal E(m,b)=\mathcal E(m+1,b+1)}
\tag{20}
\]

are the next checkpoint of the same initial head xi_(b-m). Also
Y(E(m,b))=v_b. The five m=0 starts are reached after the three actual
steps in the table.

This embeds N_0 x F5 with its advancing counter. A finite five-cycle
cannot embed as an invariant cycle in the whole native Omega: applying
U^5 would have to return its entire state, while its counter increases
by five. A finite phase factor such as (17) is compatible with that fact.

### Sharp checkpoint-only obstruction, including the nonzero exception

For every origin-zero head, not just (14), the sum after the first step
is in {0,4}, after the second in {1,2}, and after the third is 1. This
follows from the five trace laws in the preceding table and drive 0,1,1.
Drive values at steps 3,4,5 are 0,1,0. Hence the actual next three
letters are b,b,b and

\[
\psi_4=\psi_6.
\tag{21}
\]

Suppose one fixed checkpoint-only function X, on any nonempty family
of these origin-zero trajectories, takes values in O/lambda^s O and
satisfies X(psi_(n+1))=j X(psi_n) for every n>=3. Equations (21) and the
two updates at steps four and five imply

\[
(j^2-1)X(\psi_4)=0.
\]

Since j^2-1=-lambda(1+j) and 1+j is a unit, this is exactly

\[
X(\psi_4)\in\lambda^{s-1}O/\lambda^sO.
\tag{22}
\]

On this last ideal layer, sometimes called the socle, multiplication by
j=1-lambda is the identity. Invertibility of j propagates the same
stationary value to every cut n>=3 of that trajectory. If the recurrence
also holds before cut three, it propagates back to the head.

At s=4 the common phase image has valuation three, belongs to (22), and
is stationary. At s>=5 the nonzero alpha_a have valuation three and do
not belong to (22). Consequently the first precision that distinguishes
the five phases is also the first that a fixed checkpoint-only rotating
reading cannot realize. Over O itself the same argument forces zero.

Nonzero stationary modular values are genuinely allowed; the analogous
canonical obstruction for multiplication by J must not be substituted
for this j statement. The proof covers a law imposed from n=3 and does
not assert a result for arbitrary later starting cuts excluding (21).

## 4. The signed swap preserves precisely the even ideal levels

The map Bstar is an integral involution. From (5), it interchanges the
two congruences defining Lambda and changes their signs. Thus
Bstar Lambda=Lambda. It also commutes with integer multiplication by 5.
Equation (4) proves

\[
\boxed{B_\star I_{2r}=I_{2r}\quad(r\ge0).}
\tag{23}
\]

Two witnesses disprove every odd level. With e0=(1,0,0,0),

\[
\iota^{-1}(e_0)=1-j^4=-j^4\lambda,\qquad
\iota^{-1}(B_\star e_0)=-1.
\tag{24}
\]

This drops valuation one to zero. The source witness gives

\[
B_\star v_0=(0,0,-2,1)=:y_0,\qquad
\iota^{-1}(y_0)=-3-j^2-j^3=j^4\lambda^2.
\tag{25}
\]

This drops valuation three to two. Multiplying (24) and (25) by 5^k
gives a drop from s to s-1 for s=4k+1 and s=4k+3, respectively. Therefore

\[
\boxed{B_\star\text{ descends to }\mathbb Z^4/I_s
\ \Longleftrightarrow\ s\text{ is even}.}
\tag{26}
\]

The minimum input precision determining Bstar y modulo I_s is
M(s)=2 ceil(s/2). An even input precision equal to s or s+1 suffices by
(23). The odd same-level witnesses exclude s when s is odd. A smaller
input level t<s cannot suffice: Bstar I_t would have to lie in I_s,
but their indices in Z^4 are 5^t and 5^s, and Bstar is unimodular.

Since A preserves every I_s, level six is the smallest common invariant
quotient for the unguarded A and Bstar strictly refining level four.
This is a global statement about the linear maps, not yet about funding.
Bstar also preserves floor(nu_lambda/2), equivalently L-depth; changing
the parity of a valuation need not change that depth.

## 5. Bounded energy supplies exact reconstruction

Let E>=0, and suppose H(y),H(y')<=E and y-y' belongs to I_(2r).
By (4), y-y'=L^r z for some integer z. If the difference is nonzero,
(8) and the integer positivity of H give

\[
H(y-y')=5^r H(z)\ge5^r.
\]

The parallelogram identity for the positive quadratic form gives

\[
H(y-y')=2H(y)+2H(y')-H(y+y')\le4E.
\]

We have proved the exact, nonasymptotic criterion

\[
\boxed{5^r>4E\ \Longrightarrow\quad
y\longmapsto[\iota^{-1}(y)]_{\lambda^{2r}}
\text{ is injective on }\{y\in\mathbb Z^4:H(y)\le E\}.}
\tag{27}
\]

The inverse on the image is the unique energy-admitted representative.
It is not an arbitrary selection among lifts. Its existence is constructive:
the positive form (7) bounds all four coordinates, so finite enumeration
and exact congruence testing terminates. No enumeration was run here.
Equation (27) is a sufficient bound at general E, not an optimal formula
for every energy.

At E=15 the strict inequality is 5^3=125>60. Thus precision six determines
every integer source field in this energy ball exactly.

## 6. A complete invariant energy-34 machine, with occupied continuation

Fix any N>=2. Work on the literal complete chain of #1612: N cells,
their original resources r_0,...,r_(N-1), the N-1 channel resources
q_0,...,q_(N-2), and the original pointer p in C5. Each original cell
retains all its matter, spectator, raw-field and resource coordinates.

Define Sigma_N as in the frozen contract. The source and intermediate
matter are ZM. The receiver matter is R or AM; write e=0 or1 for those
two literal tuples, without adding a new register. All spectators and
static fields vanish. The source raw field is Py for arbitrary y in Z^4,
and all other raw fields vanish. Every r_i,q_j is nonnegative, p is
arbitrary, and

\[
H(y)+\sum_i r_i+\sum_j q_j+2e=15.
\tag{28}
\]

This is exactly total energy 34: receiver matter contributes 18+2e and
the inherited pointer energy is 1. Source and intermediate matter contribute
zero. This whole carrier contains states outside Lambda. It is larger
than the union of trajectories of the five original preparations.

### Every primitive and inverse stays inside this carrier

The source gate is

\[
K(y,r_0)=
\begin{cases}
(B_\star y,r_0-\Delta(y)),&r_0\ge\Delta(y),\\
(y,r_0),&r_0<\Delta(y),
\end{cases}
\quad \Delta(y)=H(B_\star y)-H(y).
\tag{29}
\]

Expansion of (6) gives Delta=f(c,d)-f(a,b). Since Bstar^2=I,
Delta(Bstar y)=-Delta(y). Every accepted image can afford its reverse,
which returns r0 exactly. Refused states cannot be accepted images.
Thus K is a total involution on the admitted source state, preserves
H(y)+r0, and retains all other coordinates.

The original G fixes every ZM cell. At the zero-field receiver, its
pointer version has the following exact restriction:

\[
(e,r,p)\longmapsto
\begin{cases}
(1,r-2,p+1),&e=0,\ r\ge2,\\
(0,r+2,p),&e=1,\\
(0,r,p),&e=0,\ r<2.
\end{cases}
\tag{30}
\]

Pointer arithmetic is modulo five. The true inverse sends
(1,r,p) to (0,r+2,p-1), sends (0,r,p) with r>=2 to (1,r-2,p), and fixes
(0,r,p) with r<2. It preserves 2e+r, and zero receiver field remains zero.
This retains occupied pointers; it does not promise fresh archival on them.

Resource layer A_res swaps r_j with q_j for each j=0,...,N-2. Layer
B_res swaps q_j with r_(j+1). The swaps within each layer are disjoint,
are their own inverses, and preserve nonnegativity and the sum in (28).
The free layer sends y to Ay and leaves all other fields zero. Its inverse
uses A^-1=A^4 and preserves H. All these facts hold at every primitive
cut. The fixed matter and zero fields retain zero charge and Gauss defect.

It follows that Sigma_N is invariant in both directions under all these
primitives, hence under

\[
T=F B_{\rm res} A_{\rm res}\widehat G K,
\qquad
T^{-1}=K\widehat G^{-1}A_{\rm res}B_{\rm res}F^{-1}.
\tag{31}
\]

Omitting the two swaps of any fixed cut also preserves this carrier.
In particular (28) gives H(y)+r0<=15 throughout every occupied
continuation, including returned pulses.

### Exact conjugacy on the image, not a formal product of residues

Define Pi_s by replacing only the source field y with its residue
modulo I_s and retaining every other original coordinate. By (27),
Pi_6 is injective on Sigma_N. Let

\[
\overline\Sigma_N=\Pi_6(\Sigma_N).
\]

For each primitive V and its actual inverse define

\[
\overline V=\Pi_6 V\Pi_6^{-1},\qquad
\overline V^{-1}=\Pi_6 V^{-1}\Pi_6^{-1}
\quad\text{on }\overline\Sigma_N.
\tag{32}
\]

The preceding invariance proves that these are total mutually inverse
maps on exactly this image. In particular

\[
\boxed{\overline T^{\,k}\Pi_6(s)=\Pi_6(T^k s)
\quad(s\in\Sigma_N,\ k\in\mathbb Z).}
\tag{33}
\]

Every exact resource account, receiver state, pointer value and next
contact is preserved. This is a complete continuing-state representation,
not a fit to five trajectories or only the first output.

Bstar already has an unguarded modular map at this even precision by
(26). What the energy bound additionally supplies is the exact integer
representative, guard and payment. We do not define an arbitrary funded
map on every element of (O/lambda^6) times unconstrained formal resources;
the image and the budget are essential to (32).

Sigma_N is finite, by positivity of H, the finite budget and the finite
pointer. T is a permutation of it, so every complete state is periodic.
There is no assertion of a common short period or permanent event record.

## 7. Six is the sharp precision for the whole funded machine

Put

\[
u=(-3,0,1,0),\qquad v=(2,0,1,0).
\tag{34}
\]

Both have H=13. Their difference is -5e0, so (24) gives

\[
\iota^{-1}(u-v)=5j^4\lambda,
\qquad \nu_\lambda(\iota^{-1}(u-v))=5.
\tag{35}
\]

Choose in both complete states r0=2, receiver R, p=0 and every other
resource zero. They are legal members of Sigma_N for every N>=2, since
13+2+18+1=34. Their Pi_s inputs agree for every s<=5, even with exact
H added to the reading. Direct application of the frozen contact gives

| Source y | H(y) | Delta(y) | Bstar y | H(Bstar y) | New r0 |
|---|---:|---:|---|---:|---:|
| (-3,0,1,0) | 13 | -8 | (-1,0,3,0) | 5 | 10 |
| (2,0,1,0) | 13 | -3 | (-1,0,-2,0) | 10 | 5 |

Both gates accept. The different integer resources prove that no function
of their common Pi_s input can give both Pi_s outputs. This also obstructs
the full macrostep, not merely its internal cut: G is still unfunded at
the initially empty receiver, and the resource layers move the respective
10 and 5 to r1. F does not change that difference, including for N=2.

Combining this witness with (33) proves

\[
\boxed{s=6\text{ is the minimum lambda precision carrying the full}
\ K\text{ and }T\text{ on all of }\Sigma_N.}
\tag{36}
\]

The retained coordinates are exactly those prescribed in Pi_s, optionally
including redundant H. This is not minimality among all encodings, for a
Boolean accept/refuse reader, or on the smaller actual orbit of the five
s_a. In fact u and v are outside Lambda, while the five prepared source
orbits remain in Lambda because both A and Bstar preserve it. Their
reachability from s_a is neither assumed nor claimed.

## 8. No fixed precision works across all energies, even with exact H

Fix s>=1. Choose k>=0 with 4k+4>=s and c=5^k. Compare the complete
zero-resource source preparations

\[
y=cv_0,\qquad y'=cAv_0.
\]

Their difference in O is

\[
\iota^{-1}(y'-y)=c(j-1)\alpha_0=-cj^3\lambda^4,
\]

of valuation exactly 4k+4. The Pi_s inputs agree and their exact source
energies are both 15c^2. Every other complete coordinate, the initial
resources, and the total energy 15c^2+19 are also equal. Nevertheless

\[
\Delta(y)=-10c^2,\qquad \Delta(y')=115c^2.
\]

At r0=0 the first source emits 10c^2 and the second refuses. The difference
persists after the complete macrostep as r1=10c^2 versus 0. Hence

\[
\boxed{\text{No single finite }s\text{ gives the complete funded law}
\text{ across unbounded energies, even with exact }H.}
\tag{37}
\]

Both fields even have the same exact lambda valuation 4k+3. Adding that
integer would not distinguish this witness. For each s the witness has
finite energy; the energy grows with the precision requested. Equation
(37) therefore coexists with the fixed-energy positive result (27).

The same scaling preserves the five-phase waiting costs up to c^2.
The early first write stays N and the delayed one N+4; the receiver still
costs 2 and retains the remainder 10c^2-2 in the channel. Thus the failure
also matters to later actual records, rather than only an inaccessible
source calculation.

## 9. Five phases, actual work, and the common receiver code

Let s_a be the complete zero-resource preparations in Sigma_N with
source v_a, receiver R and blank pointer. While the source phase is not
zero, its positive Delta in the table makes K refuse. Source/intermediate
G fix ZM, the receiver G is unfunded, all swaps exchange zeros, and F
advances only the source. Therefore, for d_a=[-a]_5,

\[
\boxed{T^{d_a}s_a=s_0}
\tag{38}
\]

as literal equality of the whole machine. Autonomy gives the same time
translation for every subsequent complete state; (33) preserves it too.

From s0, K changes v0 to y0 in (25) and releases 10. In the first resource
layers the pulse goes to r1. It then advances by one cell per macrostep
until reaching r_(N-1) at boundary N-1. Before this arrival no resource
has returned to the source. The five free phases of y0 have costs
10,55,75,40,0; the last is an actual Bstar fixed point. They produce no
second emission while the source resource is zero. This supplies the
induction for every N>=2, including the direct source/receiver case N=2.

At step N the receiver's actual R-to-AM reaction consumes 2 and increments
p from 0 to 1. The remaining 8 move to q_(N-2). The complete accounts are

\[
15+18+0+1=5+18+10+1=5+20+8+1=34.
\tag{39}
\]

It follows from (38) that s_a first emits at 1+d_a, first arrives at
N-1+d_a, and first writes at N+d_a. All five inputs have the same eventual
first payment amounts; their first-event times differ.

Another receiver increment requires an intervening AM-to-R step, so
increments are separated by at least two macrosteps. Starting from p=0,
at most four increments occur from the first event j through j+7.
Hence p remains nonzero on those eight boundaries. The fixed current
reader O(p), BLANK at zero and HIT otherwise, therefore gives at the five
common cuts N,...,N+4:

| Input a | d_a | First write | Ordered HIT/BLANK code |
|---:|---:|---:|---|
| 0 | 0 | N | 11111 |
| 1 | 4 | N+4 | 00001 |
| 2 | 3 | N+3 | 00011 |
| 3 | 2 | N+2 | 00111 |
| 4 | 1 | N+1 | 01111 |

Here 1 means HIT and 0 means BLANK. This is an ordered temporal code with
a common preparation and observation cuts, not a five-valued single
instantaneous record or a permanent archive. The pointer reader itself
does not consume a clock. Arbitrary occupied pointers have the exact
continuation (30), not the same fresh-read guarantee.

Source absence leaves all resources zero and the receiver permanently
unfunded. This absence preparation has total energy 19 and is outside
Sigma_N. Disabling K on s_a instead keeps the matched initial energy 34
and also leaves the receiver blank.
Any fixed channel cut isolates an initially zero downstream component,
which remains blank by primitive induction. These inherited controls
retain their exact preparation restrictions. On arbitrary occupied states,
a HIT alone is not a certificate of which source caused it.

## 10. What has and has not been connected

The complete statements now distinguish three information requirements:

| Required operation or observation | Exact result |
|---|---|
| Distinguish the five waiting preparations | Level5 is necessary and sufficient within lambda-power readings. |
| Follow unguarded A and Bstar on every integer field | Exactly the even levels are invariant; level6 first refines level4. |
| Follow the entire funded energy-34 Sigma_N, with occupied continuation | Level6 is necessary and sufficient for the prescribed Pi_s family. |
| Follow the funded machine over all finite energies with one fixed level | Impossible, even with exact H and all remaining input coordinates. |
| Obtain the five free phases from actual original-native histories | The selected piston/counter factor (16) and clocked embedding (19) do so. |
| Obtain them by a fixed checkpoint-only rotating reader from cut 3 | Only stationary last-ideal-layer values survive; the distinguishable family is excluded. |

The finite source quotient has 5^6 elements, but its additive group is

\[
O/\lambda^6O\cong(\mathbb Z/25\mathbb Z)^2
\times(\mathbb Z/5\mathbb Z)^2.
\tag{40}
\]

Indeed it is killed by 25, has order 5^6, and its image under multiplication
by 5 is lambda^4 O/lambda^6 O of order 5^2. The classification of finite
abelian groups gives exactly two order-25 factors and two order-5 factors.
It is not additively F5^6, whose exponent is 5. Equal cardinality with the
native checkpoint therefore supplies no additive identification or native
intertwining. This does not deny the existence of noninvertible additive maps.
The rest of the complete work machine is also still present.

Most directly, the native free reading in (16) has H(Y)=15 at every
native cut. The first accepted K branch instead requires H=5 and r0=10.
That branch is outside this free image. Nor can a loader using only the
common coarse field residue and common counter manufacture five distinct
native heads. The construction reads a real piston difference and uses
an explicitly selected dictionary; it does not recover erased data.

The next native-contact obligation is consequently concrete: extend the
common state/readout and its actual allowed transition to include both
energy sectors, the conserved funding coordinates and occupied continuation,
with a selection rule independent of the desired output. Identity still
shares the elementary conservation/inverse requirements and produces no
work on these initial states. The existence of (32) does not select K.

This respects [#1592][oldword]'s original-alphabet boundary and
[#1596][common]'s missing common native type. The positive definite finite
integer machine here is also a different carrier from [#1613][rational]'s
exact rational apparatus. Its proven contact-history restrictions may not
be discarded in any future translation; no such translation is supplied
or claimed in this note.

Finally, the integer 10 in (39) is the actual difference 15-5 in this
selected H account. Nothing here denominates it as the phase/energy
difference 2 sqrt(1+m^2)-2m, proves a work/frequency law, or measures
entropy. The separate [phase-energy analysis][phase] and exact finite
m/arctan(m)>1 for m>0 keep their scopes. Native admission, physical
selection and Canon promotion are not consequences of this proof.

[pin]: https://github.com/mathorn1973/twist-j/commit/c47f97f0a35d4cffce412ac48150ae6ef80d3963
[canon]: https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md
[work]: https://github.com/mathorn1973/twist-j/blob/2c305c0ed36d5f99b47bd9316256d2b10bb05f3a/probes/P-FIELD-SOURCE-WORK-RECORD-1/PROOF.md
[oldword]: https://github.com/mathorn1973/twist-j/blob/fbf3c402d5c56f3fb3e95cda8a853a40c3608819/notes/C-U-FIELD-CHAIN-WORD-OBSTRUCTION-N/PROOF.md
[common]: https://github.com/mathorn1973/twist-j/blob/a6d2b0d30b9d6703fffb15b187c58fa6ad71e229/notes/C-J-AREA-COMMON-CARRIER-JUNCTION-N/PROOF.md
[rational]: https://github.com/mathorn1973/twist-j/blob/3edeb861945cfeb0203d7699cc8085df2ff7a705/probes/P-EVEN-CONTACT-3ADIC-TEST-1/PROOF.md
[phase]: https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/ENERGY.md
