# P-DQRC-ARITHMETIC-RECONSTRUCTION-1 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / PROOF-FIRST / NO FORMAL RUN`

This fresh probe freezes the exact arithmetic content and the exact failure
boundary of the proposed Deterministic Quadratic Relational Census (DQRC).
Earlier local files and outputs are disclosed lineage only. They motivated the
scope, but they are pre-pin and confer no public evidence, status, execution
credit, or fired-falsifier credit.

The probe has four purposes. It proves the universal integer identities of the
formal census; identifies the proposed asymptotic CHSH law exactly with the
already public standard-pure-two-qubit optimum; classifies the coefficient in
`H` under a frozen invariant-polynomial ansatz; and tests whether the finite
one-sided deficit survives an integer shift of the tick origin. The answers
are exposed in advance. The proposed `H` and both asymptotic correlators
re-encode the Horodecki pure-state formula exactly. Within the declared
invariant class, the coefficient `4` is selected only by matching that target,
not by the census identities. The one-sided deficit is destroyed by shifting
the otherwise unselected integer origin. The verifier is an exact audit of
the written proofs, not a discovery engine.

No physical Bell experiment, TWIST-J apparatus, realized event, probability
measure, causal account, or intrinsic carrier bridge is claimed or tested.

## Public identity, authority, and action layer

```text
probe:               P-DQRC-ARITHMETIC-RECONSTRUCTION-1
public claim lock:   issue #436
probe owner:         A. M. Thorn / delegated session
branch:              probe/P-DQRC-ARITHMETIC-RECONSTRUCTION-1
path:                probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1/
initial base:        278d253f2d72f5e0bce95b380792ea3912a6420a
Public Canon:        v53, tag canon-v53
content commit:      27b8d28c84eb7bb4c4844705839c7f96f9fe014a
Canon SHA-256:       74a7da6c72cbfe9c2e3da419f42c02fb531d72e1dfe97a48d65db72553aabc02
Canon bytes:         274311
action layer:        L1 exact arithmetic and formal combinatorics only
mode:                result-exposed, proof-first; verifier is an exact audit
formal runs:         none
static checks:       Python ast.parse and public text/hash readback only
```

Candidate objects and immutable ceilings for a later, separate Canon fold:

```text
DEF-DQRC-INTEGER-CENSUS                  DEFINITION, L1, no Registry status
DQRC-INTEGER-CENSUS-ARITHMETIC           ceiling T
DQRC-HORODECKI-REENCODING                ceiling T
DQRC-H-COEFFICIENT-NONSELECTION          ceiling T
DQRC-ORIGIN-NONSELECTION                 ceiling T
DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY       ceiling T
```

The field statements below use existing public cyclotomic structure but add a
new, narrowly named DQRC application: the maximal-sector slope and the exact
restrictions on the resulting `S_inf`. The proposed field-boundary row is not
a duplicate of `DEGREES-BY-PRIME`. The physical DQRC lane is not a theorem
candidate. Its maximum disposition remains open/STOP pending an
intrinsic-carrier, apparatus, event, measure, and intervention contract.

Proposed dependency edges for a later fold are:

```text
DQRC-INTEGER-CENSUS-ARITHMETIC
    REQUIRES DEF-DQRC-INTEGER-CENSUS
DQRC-INTEGER-CENSUS-ARITHMETIC
    REQUIRES DEF-ACTION-LAYERS
DQRC-INTEGER-CENSUS-ARITHMETIC
    BOUNDED_BY BELL-CAUSAL-ACCOUNTING
DQRC-HORODECKI-REENCODING
    REQUIRES DQRC-INTEGER-CENSUS-ARITHMETIC
DQRC-HORODECKI-REENCODING
    REQUIRES PURE-QUBIT-RELATIONAL-CHSH
DQRC-HORODECKI-REENCODING
    BOUNDED_BY BELL-CAUSAL-ACCOUNTING
DQRC-H-COEFFICIENT-NONSELECTION
    REQUIRES DQRC-INTEGER-CENSUS-ARITHMETIC
DQRC-H-COEFFICIENT-NONSELECTION
    REQUIRES DQRC-HORODECKI-REENCODING
DQRC-H-COEFFICIENT-NONSELECTION
    BOUNDED_BY BELL-CAUSAL-ACCOUNTING
DQRC-ORIGIN-NONSELECTION
    REQUIRES DQRC-INTEGER-CENSUS-ARITHMETIC
DQRC-ORIGIN-NONSELECTION
    BOUNDED_BY BELL-CAUSAL-ACCOUNTING
DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY
    REQUIRES DQRC-INTEGER-CENSUS-ARITHMETIC
DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY
    REQUIRES DEGREES-BY-PRIME
DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY
    BOUNDED_BY BELL-CAUSAL-ACCOUNTING
```

No edge to `BELL-MAGIC-BOUNDARY`, QDD, a Born measure, or a physical apparatus
is proposed. `BELL-CAUSAL-ACCOUNTING [O]`, `QDD-INSTRUMENT-APPARATUS [O]`,
and `QUADRATIC-DECODER-DATA [O]` remain unchanged.

## Result-exposed lineage and non-evidence

The following supplied local artifacts predate this public lock:

```text
verify_dqrc_1.py
    sha256 068bcd02b05469ce8ddc949b64bdf7e99aa90ad66c9f861a8b5e1126d5ffb0ba
breaker_dqrc_1.py
    sha256 1ed4292a7944442b3ce9a387b7dd09f6ed9717edf32e2314fcbfd80c7d1a6d14
RECONDQRCBELLCENSUS_20260819.md
    sha256 650ff88430742ed091fc5534c1f067770d8329bb35cfe339b44ee8de6f9c3a01
```

Their reported local outputs are not formal runs. The supplied floating-point
breaker is not accepted as evidence. Its useful conclusions are replaced here
by exact proofs. Its silver-word comparison also did not assert or prove its
own shifted equality: the program compared unshifted prefixes and printed
`12/40` without an assertion. No all-prefix silver-word theorem is frozen in
this probe.

## 1. Frozen carrier and equations

Let

```text
X = ((a,b),(c,d)) in Z^(2 x 2) \ {0},
Q = a^2+b^2+c^2+d^2,
Delta = (ad-bc)^2,
H = Q^2+4 Delta.
```

For `K >= 0`, define by integer inequalities

```text
M_0(K) = max {m >= 0 : H m^2 <= Q^2 K^2},
M_1(K) = max {m >= 0 : Q^2 H m^2 <= 16 Delta^2 K^2}.
```

Equivalently, only in the written proof,

```text
alpha_0 = Q/sqrt(H),
alpha_1 = 4 Delta/(Q sqrt(H)),
M_x(K) = floor(alpha_x K).
```

The implementation never evaluates either square root. Put

```text
u_x(k) = M_x(k+1)-M_x(k).
```

For formal bits `x,y,r,t in {0,1}` and `k >= 0`, write the formal tick address

```text
n = 16k + 4(2x+y) + 2r+t,
sigma_xy = (-1)^(xy),
A = (-1)^t,
B = A sigma_xy (-1)^(r(1-u_x(k))).
```

These are formal labels in an L1 combinatorial model. Calling `x,y` settings,
`A,B` outcomes, or `n` a trial does not make them an L4 apparatus or an L5
realized event.

For an integer tick-origin shift `j >= 0`, also define the shifted comparator
and log

```text
M_x^[j](K) = M_x(K+j)-M_x(j),
u_x^[j](k) = u_x(k+j).
```

Use `u_x^[j](k)` in the outcome formula and write the resulting formal signs
as `A_xy^[j](k,r,t)` and `B_xy^[j](k,r,t)`. Define the four-cell count, signed
census correlator, and CHSH census functional by

```text
N_xy^(epsilon,eta)(K;j)
  = #{(k,r,t): 0<=k<K, r,t in {0,1},
                 A_xy^[j](k,r,t)=epsilon,
                 B_xy^[j](k,r,t)=eta},
E_xy^[j](K)
  = (1/(4K)) sum_(0<=k<K; r,t in {0,1})
                  A_xy^[j](k,r,t) B_xy^[j](k,r,t),
S_K^[j] = E_00^[j](K)+E_01^[j](K)+E_10^[j](K)-E_11^[j](K)
          = 2(M_0^[j](K)+M_1^[j](K))/K.
```

These are rational signed-count statistics, not ontic probabilities or
expectations over a stochastic law.

The original proposal is exactly the special origin `j=0`.

## 2. R1: DQRC-INTEGER-CENSUS-ARITHMETIC

For every declared `X`, every `K >= 1`, and every origin shift `j >= 0`:

```text
A1  4 Delta <= Q^2.
A2  0 <= alpha_0,alpha_1 <= 1 and u_x^[j](k) is in {0,1}.
A3  for each fixed outcome pair (epsilon,eta),
       N_xy^(epsilon,eta)(K;j)
         = K+M_x^[j](K)  if epsilon eta = sigma_xy,
         = K-M_x^[j](K)  otherwise.
A4  each local sign occurs exactly 2K times in every context.
A6  X -> qX, q in Z\{0}, leaves M_x^[j], u_x^[j], and every census unchanged.
A7  for every fixed (k,r,t,j), product_(x,y) A_xy B_xy = -1,
    while every locally factorized deterministic table has product +1.
```

For the frozen origin `j=0` only,

```text
S_K = S_K^[0] = 2(M_0(K)+M_1(K))/K,
S_inf = 2 sqrt(H)/Q,
0 <= S_inf-S_K < 4/K.
```

### Proof

Let `v=(a,b)` and `w=(c,d)`. The exact Lagrange identity is

```text
Q^2-4 Delta
  = (a^2+b^2-c^2-d^2)^2 + 4(ac+bd)^2 >= 0.
```

Equivalently, Cauchy-Schwarz gives

```text
|det X| <= ||v|| ||w||,
4 ||v||^2 ||w||^2 <= (||v||^2+||w||^2)^2=Q^2,
```

which proves A1. The first slope is at most one because `Q^2 <= H`. For the
second, A1 gives

```text
16 Delta^2 <= 4 Delta Q^2 <= Q^4+4 Delta Q^2=Q^2 H.
```

Because `Q>0` and `H>0`, `m=0` is admissible and each inequality bounds `m`,
so each maximum exists independently of A1. The determinant bound then puts
both slopes in `[0,1]`, and consecutive lower-floor differences are zero or
one. Thus totality is a theorem of the definition, while A1 supplies the
binary-increment conclusion rather than an extra premise.

For fixed `k,x,y`, if `u_x=1`, both values of `r` have product `AB=sigma_xy`.
If `u_x=0`, one value of `r` has each product sign. The bit `t` maps every
pair `(A,B)` to `(-A,-B)`. Summing
`u_x(k+j)` over `0 <= k < K` telescopes to `M_x^[j](K)`, proving A3 and A4.
The exact margins are inserted solely by the `t` involution. They are a
finite-table balance identity, not a derived causal or intervention-level
no-signalling statement.

For each context the two cells with product `sigma_xy` contribute
`2(K+M_x^[j])` counts and the other two contribute `2(K-M_x^[j])`. Therefore

```text
E_xy^[j](K) = sigma_xy M_x^[j](K)/K.
```

Multiplication by the CHSH signs `sigma_xy` and summation over `x,y` gives the
displayed exact formula for `S_K^[j]`.

Under `X -> qX`, `Q -> q^2 Q`, `Delta -> q^4 Delta`, and `H -> q^4 H`; both
integer comparator inequalities are unchanged. This proves A6.

In A7 the `t` factor squares away, and the `r,u` factor occurs twice for each
fixed `x`. The only surviving product is

```text
product_(x,y) sigma_xy = -1.
```

Thus the parity is inserted by the frozen CHSH sign table. A local table has
product `A_0^2 A_1^2 B_0^2 B_1^2=+1`. Neither statement is an emergent fact
about the TWIST-J carrier.

For `j=0`, each lower floor has remainder in `[0,1)`. Adding the two
remainders and multiplying by `2/K` proves the one-sided error bound. Its sign
comes from choosing the lower floor.

## 3. R2: DQRC-HORODECKI-REENCODING

Supply externally a normalized real pure two-qubit state with coefficient
matrix

```text
X/sqrt(Q).
```

Its standard pure concurrence is

```text
C = 2 |det X|/Q,
C^2 = 4 Delta/Q^2.
```

The unnormalized formula `C=2|det X|` is false unless `Q=1` and is explicitly
excluded.

The public theorem `PURE-QUBIT-RELATIONAL-CHSH [T]` gives

```text
B_max = 2 sqrt(1+C^2).
```

But the proposed DQRC definition gives identically

```text
H = Q^2+4 Delta = Q^2(1+C^2),
S_inf = 2 sqrt(H)/Q = 2 sqrt(1+C^2)=B_max.
```

This is not merely equality of the maxima. After local real singular-value
rotations, write the normalized state in Schmidt gauge as

```text
|psi> = s_0 |00> + s_1 |11>,
s_0,s_1 >= 0,
s_0^2+s_1^2=1,
C=2s_0s_1.
```

Direct evaluation of the Pauli products gives, in `(x,y,z)` axes,

```text
T = diag(C,-C,1),
```

and hence

```text
spec(T^T T) = {1,C^2,C^2}.
```

Choose

```text
A_0=z,
A_1=x,
B_0=(z+C x)/sqrt(1+C^2),
B_1=(z-C x)/sqrt(1+C^2).
```

Equivalently the Bob directions are at angles `+delta,-delta` in the Schmidt
plane, with `tan(delta)=C`. Direct scalar products `E_xy=A_x^T T B_y` give
the four exact correlators

```text
(E_00,E_01,E_10,E_11)
  = (r_0,r_0,r_1,-r_1),
r_0 = 1/sqrt(1+C^2) = Q/sqrt(H),
r_1 = C^2/sqrt(1+C^2) = 4 Delta/(Q sqrt(H)).
```

For a general, non-Schmidt-gauge matrix `X`, the apparatus directions must be
rotated by its local singular-value transformations. The seven numerical
examples in the supplied breaker did not establish this apparatus map and are
not a 14,640-case correlator proof. The exact statement here includes the
required Schmidt-gauge qualifier.

Therefore `H` is exactly the known pure-two-qubit optimum written in integer
invariants. The equality is a valid reconstruction theorem. It is not
independent evidence that TWIST-J derives quantum CHSH, because `H` has not
been derived from `Omega`, `U`, an apparatus, or an event law without using
the external pure-qubit target.

## 4. R3: DQRC-H-COEFFICIENT-NONSELECTION

Freeze the full local action

```text
X -> U X V^T,  U,V in O(2).
```

For an unnormalized real `2 x 2` matrix, its orbit is classified by the
unordered squared singular values. Equivalently, the polynomial invariant
ring is generated by

```text
Q = tr(X X^T),
Delta = det(X)^2.
```

The sign of `det(X)` is erased by the full orthogonal action. Under the smaller
`SO(2) x SO(2)` action it would be extra data. After normalization of a pure
state only the ratio `4 Delta/Q^2=C^2` remains; `Q` and `Delta` are two orbit
invariants only for the unnormalized carrier.

Every homogeneous degree-four full-orthogonal invariant polynomial therefore
has the form

```text
A Q^2 + beta Delta.
```

Indeed, singular-value decomposition reduces an orbit to the unordered pair
`(lambda_1,lambda_2)` of eigenvalues of `X X^T`. An invariant polynomial is a
symmetric polynomial in that pair, hence a polynomial in
`lambda_1+lambda_2=Q` and `lambda_1 lambda_2=Delta`. At total degree four in
the entries of `X`, only `Q^2` and `Delta` occur.

Normalizing the rank-one locus by `H(Q,0)=Q^2` fixes `A=1` but leaves `beta`
free. In particular, for every integer `beta >= 0`, put

```text
H_beta = Q^2 + beta Delta.
```

Define `M_(0,beta)`, `M_(1,beta)`, and `u_(x,beta)` by the same integer
inequalities as in Section 1 with `H` replaced by `H_beta`:

```text
M_(0,beta)(K)=max {m>=0: H_beta m^2 <= Q^2 K^2},
M_(1,beta)(K)=max {m>=0: Q^2 H_beta m^2 <= 16 Delta^2 K^2},
u_(x,beta)(k)=M_(x,beta)(k+1)-M_(x,beta)(k).
```

The two comparator slopes

```text
alpha_0(beta) = Q/sqrt(H_beta),
alpha_1(beta) = 4 Delta/(Q sqrt(H_beta))
```

remain in `[0,1]`: the first because `H_beta >= Q^2`, the second because
`16 Delta^2 <= Q^4 <= Q^2 H_beta`. Hence comparator totality, binary
increments, the closed census, exact margin balance, integer rescaling, and
the inserted parity all survive for every such `beta`. Their actual census
limit is

```text
L_beta = 2(alpha_0(beta)+alpha_1(beta))
       = 2(Q^2+4 Delta)/(Q sqrt(H_beta)).
```

For `Delta>0`, comparison with the standard pure-state maximum gives

```text
L_beta^2 = B_max^2
iff H_beta = Q^2+4 Delta
iff beta=4.
```

Likewise the internally written equality

```text
L_beta = 2 sqrt(H_beta)/Q
```

is equivalent to `beta=4` away from the product locus. Thus the full
`O(2) x O(2)` orbit data, degree-four homogeneity, rank-one normalization,
integrality, comparator totality, binary increments, census closure, margins,
scaling, and parity do not select `4`. They admit the infinite integer family
`beta=0,1,2,...`. The value `4` is selected exactly when the already known
Horodecki target (or the equivalent internally named target equality) is
imposed.

This theorem falsifies uniqueness within the explicitly frozen ansatz. It
does not prove that no richer construction from `J`, `Omega`, or `U` could
derive `beta=4`; that wider intrinsic-origin question remains STOP until its
admissible construction class is defined.

## 5. R4: DQRC-ORIGIN-NONSELECTION

For every fixed origin shift `j`, all of A1-A4 and A6-A7 remain true, and

```text
M_x^[j](K)/K -> alpha_x,
S_K^[j] -> S_inf.
```

The finite sign in A5 is not origin invariant. At the maximal point

```text
(Q,Delta,H)=(2,1,8), K=1:
S_1^[0]=0,
S_1^[1]=4,
(S_inf)^2=8.
```

Thus the same integer comparator, asymptotic target, census formula,
margin balance, scaling invariance, and parity permit both a deficit and an
excess. The origin-zero one-sided `O(1/K)` deficit is a theorem of the chosen
origin, not a physical prediction until the origin/intercept is selected by a
separate intrinsic carrier and apparatus law.

Proof: `M_x^[j](K)` is a sum of `K` consecutive binary increments, so it lies
between zero and `K`, gives the same count proof, and differs from
`alpha_x K` by a bounded amount independent of `K`. The displayed witness is
an exact integer evaluation.

## 6. R5: DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY

On the maximal locus `4 Delta=Q^2`,

```text
H=2Q^2,
S_inf=2 sqrt(2),
alpha_0=alpha_1=1/sqrt(2).
```

Let `K_5=Q(zeta_5)`. Its Galois group is cyclic of order four and hence has a
unique index-two subgroup. Its unique quadratic subfield is its real
quadratic subfield

```text
Q(zeta_5+zeta_5^-1)=Q(sqrt(5)).
```

Consequently `sqrt(2)` is not in `K_5`. Also

```text
Q(zeta_5) intersection Q(zeta_8) = Q.
```

The latter follows, for example, because the first field is ramified only at
5, the second only at 2, and a nontrivial common number field cannot be
unramified at every finite prime.

The correct extension statement is:

```text
Q(zeta_5,sqrt(2)) has degree 8 over Q and is a proper subfield of Q(zeta_40);
Q(zeta_5,zeta_8)=Q(zeta_40) has degree 16 over Q.
```

Thus adjoining the scalar `sqrt(2)` does not by itself require the full
`Q(zeta_40)`. The full compositum is required only if the whole `zeta_8`
field is adjoined.

This field mismatch is not a no-go for a purely integer substitution or
automatic sequence. The silver substitution `A->AAB`, `B->A` has integer
incidence matrix

```text
M=((2,1),(1,0)).
```

Its Perron-Frobenius eigenvalue is `lambda=1+sqrt(2)`, with right eigenvector
`(lambda,1)`, and its normalized `A` frequency is

```text
lambda/(lambda+1)=1/sqrt(2).
```

Thus integer incidence matrices can produce this irrational limiting
frequency without making `sqrt(2)` an element of the coefficient field of
each finite state. The field mismatch obstructs only a claim that the slope is
an internal `K_5` scalar or follows by a `K_5`-linear construction.

Finally,

```text
S_inf^2 = 4+16 Delta/Q^2 is rational.
```

If `S_inf=a+b sqrt(5)` with rational nonzero `a,b`, its square has nonzero
irrational part `2ab sqrt(5)`, a contradiction. A pure `sqrt(5)` field sector
is possible: `X=((-3,-1),(-1,0))` has `(Q,Delta,H)=(11,1,125)` and
`S_inf=10 sqrt(5)/11`. No linear `phi` value with both rational and
`sqrt(5)` parts can occur in this DQRC family.

The exact value `S_inf=sqrt(5)` is nevertheless impossible for nonzero
integral `X`. It would imply `Q=4|det X|`. Hence `Q` is divisible by four. A
sum of four squares is divisible by four only when its four entries are all
even or all odd: every square is zero or one modulo four. If all entries are
odd, `Q/4` is odd while `det X` is even, a contradiction. If all are even,
divide `X` by two and obtain the same equation, producing an infinite descent.

## 7. Born, measure, and probability boundary

`Q` has polynomial degree two in the entries of `X`; `Delta=(det X)^2` has
degree four. `Delta` is quadratic only after `det X` has already been supplied
as a coordinate on the determinant/wedge line. Therefore the map
`X -> (Q,Delta)` is not literally quadratic in both original matrix slots.

The exact identity with a standard-QM Born/CHSH expression runs from the
externally supplied quantum structure to the DQRC formula. It does not prove
the reverse physical bridge from the TWIST-J quadratic carrier to an L5 event
stream or an L6 measure. No current Born, QDD, or decoder obligation is closed.

For any declared finite census one may define the normalized rational
abbreviation

```text
P_K(epsilon,eta|x,y)=N_xy^(epsilon,eta)(K)/(4K).
```

This introduces no randomness into the formal dynamics. But a physical Bell
claim still owes the full normalized source and conditional kernels required
by `BELL-CAUSAL-ACCOUNTING`, as well as positive-denominator handling and the
named L1-to-L4, L4-to-L5, and L5-to-L6 gates.

Deleting ontic randomness does not evade Bell's premise structure. If one
temporarily writes `lambda=(k,r,t)`, the displayed `B` depends explicitly on
the remote formal label `x` through both `sigma_xy` and `u_x(k)`. The model is
therefore a deterministic contextual/relational table, not a locally
factorized hidden-variable model. Cancellation over `t` proves balanced
tables; it does not supply a spacetime causal mechanism or exclude
controllable signalling under interventions.

## 8. Frozen breakers and failure thresholds

The probe has the following scientific falsifiers:

```text
F1  any universal identity in R1 is false on its declared integer carrier;
F2  after the external real pure-two-qubit structure is supplied, the exact
    DQRC maximum or any of the four Schmidt-gauge correlators differs from R2;
F3  an admissible beta != 4 is excluded by one of the frozen beta-independent
    properties in R3, or beta=4 is not exactly equivalent to target matching;
F4  a shifted origin fails one of the origin-invariant identities in R4, or
    the exact origin witness is wrong;
F5  sqrt(2) lies in Q(zeta_5), the displayed compositum degrees are wrong, or
    the rational-square exclusion is false.
```

The following are integrity or scope STOP conditions, not scientific
falsifiers:

```text
S1  a physical setting, outcome, no-signalling, probability, or causal claim;
S2  treating the inserted t-balance or sigma parity as emergent;
S3  calling pre-pin local output formal evidence;
S4  promoting the origin-zero finite deficit before deriving its origin;
S5  calling the field mismatch a no-go for an integer limiting frequency;
S6  claiming that the direct standard-QM reconstruction is an intrinsic
    derivation from J, Omega, U, QDD, or a Born event law;
S7  moving BELL-CAUSAL-ACCOUNTING, QDD-INSTRUMENT-APPARATUS, or
    QUADRATIC-DECODER-DATA.
```

No threshold, origin, carrier, finite box, or status ceiling may change after
the public pin. A changed scientific statement requires a fresh probe.

## 9. Data-attack disposition

`P-DQRC-FINITE-DEFICIT-1` is not authorized by this preregistration and is not
run here. Published loophole-free Bell data cannot yet test the displayed
origin-zero law because no typed map identifies their trials, settings,
detections, losses, ordering, estimator, and apparatus interventions with the
formal DQRC ticks. In addition, R4 proves that the sign of the finite
discrepancy changes under an unselected integer origin while the asymptotic law
and all other formal census identities remain fixed.

There is also an unresolved address dichotomy. The formal address makes one
`k` enumerate all sixteen tuples `(x,y,r,t)`. A laboratory Bell trial realizes
one setting pair and one outcome pair. If `n` is asserted to be physical time,
the formula imposes a fixed sixteen-tick setting schedule and exact block
margins before it predicts a deficit; randomized-setting records attack that
schedule first. If `n` is only an accounting enumeration after regrouping the
record by context, then `K`, `j`, and the Sturmian fine structure are not yet
chronological observables. Equating one complete formal block with sixteen
realized trials is itself an unproved L4-to-L5 bridge.

Moreover an `O(1/K)` mean displacement is asymptotically smaller than an
`O(1/sqrt(K))` sampling width in an ordinary independent-trial comparison.
That scaling statement itself depends on a supplied sampling model; it is not
a bare prediction of unitary quantum mechanics. A viable empirical attack
would therefore have to freeze the full word-level trial law, not merely look
for a preferred sign in a noisy aggregate CHSH estimate.

A future data probe must first freeze and pass:

```text
D0  intrinsic selection of the tick origin/intercept;
D0a decision whether n is physical time or a nonchronological enumeration;
D1  exact external dataset identities, versions, licenses and SHA-256 hashes;
D2  immutable trial inclusion, loss, heralding, setting and outcome maps;
D3  exact estimator and block/window construction, with no reordering chosen
    after reading the data;
D4  preparation and apparatus bridge to the DQRC carrier;
D5  systematic-error and detector model without a fitted probability input;
D6  a deterministic falsifier stated without importing a quantum p-value as
    DQRC ontology.
```

Until D0-D6 exist in one public lock, the empirical lane is `HOLD / STOP`, not
a public probe and not evidence for or against DQRC physics.

## 10. Verifier and formal-run protocol

The accepted `verify.py` uses only Python integer arithmetic, `Fraction`, and
`isqrt`. It has no RNG, float, tolerance, NumPy, network access, external data,
or expected-output import. It requires CPython 3.12 exactly at major/minor
level, no command-line arguments, and `sys.flags.optimize=0`; an explicit
pre-assertion guard exits `1` if any integrity condition fails. A failed
scientific assertion exits `2`; a clean pass exits `0`. The written proofs
carry the universal statements; the frozen boxes are exact audit witnesses
only and never delimit the theorem scope.

Before the initial public pin only `ast.parse`, text inspection, hashing, Git
blob inspection, and policy checks that do not import or execute the verifier
are permitted. After the exact public bytes are pushed and read back, one
formal execution is authorized with

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1/verify.py
```

The expected successful stdout must end with

```text
SUMMARY PASS gates=15/15 physical-bridge=NOT-TESTED data-attack=STOP
```

Exit `1`, nonempty stderr on the accepted path, an unexpected exit code,
remote-byte mismatch, or architecture mismatch is integrity STOP. Exit `2`
with the frozen `SCIENTIFIC FALSIFIER FIRED gate=...` record fires the named
F1-F5 scientific falsifier. Exit `0` must reproduce the committed
`EXPECTED.txt` byte for byte. The required pull-request workflow must do so on
native x86_64 and aarch64 with Python 3.12 before any computational T
disposition.

## 11. Maximum dispositions

On a clean exact pass:

```text
DEF-DQRC-INTEGER-CENSUS                 definition candidate, L1;
DQRC-INTEGER-CENSUS-ARITHMETIC          T candidate, exact L1 theorem;
DQRC-HORODECKI-REENCODING               T candidate, external-QM comparison;
DQRC-H-COEFFICIENT-NONSELECTION         T candidate, exact L1 classification;
DQRC-ORIGIN-NONSELECTION                T candidate, exact L1 nonselection;
DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY      T candidate, exact L1 boundary;
physical DQRC reading                   O/STOP only;
BELL-CAUSAL-ACCOUNTING                  unchanged O/STOP.
```

A verifier pass does not itself alter the Canon. All dispositions remain
candidate results until a later, separate sealed Canon fold reviews their
scope, evidence, dependencies, and falsifiers.
