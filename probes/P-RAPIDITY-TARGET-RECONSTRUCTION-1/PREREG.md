# P-RAPIDITY-TARGET-RECONSTRUCTION-1 preregistration

Status: FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED.

Date: 2026-09-05. Owner: A. M. Thorn / delegated session.
Public claim: https://github.com/mathorn1973/twist-j/issues/817.
Branch and path: `probe/P-RAPIDITY-TARGET-RECONSTRUCTION-1` and
`probes/P-RAPIDITY-TARGET-RECONSTRUCTION-1/`.

## Authority and ownership

The basis is public main `935aaad0827aa6bc99cebd28acc97c271985ae80`,
Public Canon v76, after the reviewed merge of PR #792. STATUS declares
content commit `07910adb8418742bf52a0d204577b84b38009b18`, tag `canon-v76`,
Canon SHA-256 `c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112`,
and 420539 bytes. Tag target
`d83bacde1355ecfd1ca0b38678e6a43744e786d8` and content are ancestors of main;
the five normative checksums and public main checks were verified. The
required main workflow at this basis is run 33926293885, successful.

The collision scan covered remote heads, open and closed issues and PRs,
the registry, probes and current rapidity notes. PR #792 owns the golden
diagonal evaluation ladder, its integrality selection and finite layer
inversion; it does not own target-only interpolation cost. This probe
defines its polynomial problem and proves its identities independently.
It makes no claim of priority over classical polynomial interpolation or
q-product algebra. No external analytic theorem is imported.

Classical background: Lagrange interpolation is recorded in
https://dlmf.nist.gov/3.3 and the q-Pochhammer notation in
https://dlmf.nist.gov/17.2. The proofs needed here are self-contained.

The action layer is NOT_APPLICABLE: exact arithmetic and polynomial
analysis only. No physical or L1-L6 bridge is proposed. No claim is added
to Canon by this probe. TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O] stays open.

## Falsifiers and frozen scope

Let phi=(1+sqrt(5))/2, q=phi^(-2)=(3-sqrt(5))/2, and
L_(2k)=q^(-k)+q^k. Write m=d+1, with integers m>=1 and d>=0.
The source nodes are x_k=1-L_(2k), k=1,...,m; the target is -1.
The target rung k=0 is not admitted as a source.

The proposed candidate theorem has the following exact clauses.

```text
A  For every real polynomial Q of degree <= m-1, Q(-1) is the unique
   linear combination sum_k w_(m,k) Q(x_k) reproducing that polynomial
   space. The rational weights are the Lagrange products and equal
   (-1)^(k-1) q^(k(k-1)/2) (1+q^k) P_m^2/(P_(m-k) P_(m+k)),
   where P_j=product_(l=1)^j (1-q^l), P_0=1.
B  Their signs are (-1)^(k-1). Lambda_m=sum_k |w_(m,k)| increases
   strictly to C(q)=1+2 sum_(j>=1) q^(j(j+1)/2), and
   1 <= Lambda_m < C(q) < 3-sqrt(5)/2 < 19/10.
C  Extending w_(m,k)=0 for k>m, for each integer K>=0,
   sum_(k>K)|w_(m,k)| <= q^(K(K+1)/2)
           * (1+2 q^(K+1)/(1-q^(K+2))).
   In particular the weight tail beyond k=1 is strictly less than 1/2.
D  For independent real input errors |e_k|<=epsilon_k, epsilon_k>=0,
   sup |sum_k w_(m,k)e_k| = sum_k |w_(m,k)| epsilon_k.
   Uniform absolute errors are amplified by exactly Lambda_m, hence
   by at most 19/10. A truncated reconstruction has error bounded by
   sum_(k<=K)|w|epsilon_k + sum_(k>K)|w| |Q(x_k)|.
E  For d>=1, a_k=-x_k=L_(2k)-1 and S=d(d+1)/2, the relative-error
   amplification of the explicit witness Q(z)=z^d is
   kappa_d=sum_(k=1)^(d+1)|w_(d+1,k)|a_k^d, with
   q^(2-S) < kappa_d < 6 q^(-S).
   The independent error box |e_k|<=eta |Q(x_k)|, eta>=0, has exact
   worst target error eta*kappa_d and target magnitude |Q(-1)|=1.
```

An exact counterexample to any clause within these domains fires its
mathematical falsifier. The finite audit covers the frozen ranges below;
the written proofs, not extrapolation from those ranges, carry the
universal statements. A pin/byte mismatch, nonzero exit, nonempty stderr,
changed threshold, pre-pin execution or architecture disagreement is an
integrity STOP, not automatically a mathematical counterexample.

The theorem does not assert a relative condition number for the actual
arithmetic coefficient family B_a(N), whose coefficients or source errors
may be correlated. It proves no estimates for the source values Q(x_k),
no cancellation in M(N), no RH/GRH or zero statement, no Fourier/Hecke
identification, and no general impossibility of reconstruction. The
supremum in B is a limit; no finite m attains C(q).

## Six frozen fields

```text
EQUATION:  clauses A-E and the definitions above, proved below.
CODE:      verify.py in this probe directory; Python stdlib only,
           exact integers, Fraction and exact Q(sqrt5) pairs; no floats,
           numerical transcendental library, random input or network.
CARRIER:   real polynomials of degree <=d, the m=d+1 prescribed integer
           nodes, rational evaluation weights, independent real error
           boxes; exact Q(sqrt5) is used to audit the product identities.
SYSTEMATICS: target k=0 excluded; signs retained; absolute and relative
           error domains distinguished; full polynomial space versus
           arithmetic subfamily distinguished; no source data fitting.
THRESHOLD: G1-G8 exact PASS at m=1,...,16; rational linear-system
           crosscheck at m=1,...,6; B1-B5 fire at the named controls;
           exit zero, empty stderr, identical stdout on both architectures.
LAYER:     NOT_APPLICABLE; no L1-L6 lift.
```

## 1. Nodes and interpolation

The number q satisfies q^2-3q+1=0 and 0<q<1. The even Lucas integers
are defined by L_0=2, L_2=3, L_(2(k+1))=3L_(2k)-L_(2(k-1)).
The sequence q^(-k)+q^k has the same initial values and recurrence.
It follows that all x_k are integers. Since q^(-k)+q^k strictly increases
for k>=1, x_k strictly decreases from x_1=-2. Thus the source nodes
are pairwise distinct and none equals the target -1.

For distinct source nodes define

```text
w_(m,k)=product_(j!=k) (-1-x_j)/(x_k-x_j).
```

The Lagrange basis polynomials take the value one at their own node and
zero at the others. Subtracting their reconstruction from a polynomial
Q of degree <=m-1 yields a polynomial of that degree with m distinct
roots, hence zero. Evaluation at -1 proves reconstruction. The invertible
Vandermonde matrix, or evaluation on each Lagrange basis polynomial,
proves uniqueness of the linear evaluation functional. Integer nodes
give rational weights. No analytic continuation or infinite interpolation
is used.

## 2. Exact product formula

Put y_k=L_(2k)-2=q^(-k)(1-q^k)^2, so x_k=-1-y_k. For j!=k,

```text
y_j-y_k=q^(-j)(1-q^(j-k))(1-q^(j+k)),
w_(m,k)=product_(j!=k) y_j/(y_j-y_k).
```

The k-1 factors with j<k are negative. Extracting them contributes
(-1)^(k-1) q^(k(k-1)/2). The remaining products give

```text
w_(m,k)=(-1)^(k-1) q^(k(k-1)/2)(1+q^k)
         * P_m^2/(P_(m-k)P_(m+k)).
```

For completeness, the factors with |j-k| supply P_(k-1)P_(m-k),
and the factors with j+k supply P_(m+k)/(P_k(1-q^(2k))).
The numerator is P_m^2/(1-q^k)^2. Their quotient leaves
(1-q^k)(1-q^(2k))/(1-q^k)^2=1+q^k, as displayed.

## 3. Sharp limiting absolute norm

Write c_k=q^(k(k-1)/2)(1+q^k). The remaining factor is

```text
R_(m,k)=P_m^2/(P_(m-k)P_(m+k))
       =product_(j=0)^(k-1) (1-q^(m-j))/(1-q^(m+j+1)).
```

Every factor lies strictly between zero and one. For fixed k each factor
increases strictly with m and tends to one: for constants A>B>0,
(1-At)/(1-Bt) decreases with t, and here t=q^m decreases.
Therefore |w_(m,k)|=c_k R_(m,k)<c_k, and each existing term increases
when m increases. Adding the new positive term proves strict monotonicity
of Lambda_m; Lambda_1=1.

The summable majorant has sum

```text
C(q)=sum_(k>=1)c_k=1+2 sum_(j>=1)q^(j(j+1)/2).
```

For any fixed finite number of terms R_(m,k) tends to one. Taking first
that finite limit and then its length to infinity, with the displayed
summable majorant bounding the remainder, proves Lambda_m tends to C(q).
No unproved interchange of an infinite sum and a limit is needed.

For j>=2, j(j+1)/2>=3(j-1), strictly for j>=4. Consequently

```text
C(q)<1+2q+2q^3/(1-q^3)=3-sqrt(5)/2<19/10.
```

The equality follows by q^2-3q+1=0. The last inequality is equivalent
to sqrt(5)>11/5, whose square is 5>121/25. This proves B, including
strictness, rational uniform bound, and the exact supremum.

## 4. Weight tails and absolute errors

Summing the two triangular-exponent contributions in c_k gives

```text
sum_(k>K)c_k=q^(K(K+1)/2)
              +2 sum_(j>=K+1)q^(j(j+1)/2).
```

The first exponent in the second sum is (K+1)(K+2)/2 and successive
exponent gaps are at least K+2. A geometric sum proves C. At K=1 its
right side is q(1+2q^2/(1-q^3))=1/2. Every finite weight tail is
strictly smaller than that positive infinite majorant.

The triangle inequality yields D. It is exact for each independent
error box: choosing e_k=epsilon_k sign(w_(m,k)) attains its upper bound.
Thus the absolute input l-infinity to target norm is precisely Lambda_m.
For zero errors the reconstructed error is zero; the strict bound by
(19/10) times the maximum error is asserted only when that maximum is
positive. Splitting the full identity at K gives the truncated bound.
Small weights by themselves do not bound large omitted polynomial values.

## 5. Relative-error boundary

Set d=m-1>=1, S=d(d+1)/2, and a_k=L_(2k)-1. Then 1<a_k<q^(-k).
The last term of kappa_d alone gives

```text
|w_(d+1,d+1)| a_(d+1)^d
 =product_(j=1)^d (a_j-1)/(1-a_j/a_(d+1))
 >product_(j=1)^d (L_(2j)-2)
 =q^(-S) product_(j=1)^d (1-q^j)^2.
```

The elementary finite-product bound product(1-u_j)>=1-sum u_j for
u_j in [0,1] and the strict finite geometric sum imply

```text
product_(j=1)^d(1-q^j)>1-q/(1-q)=q.
```

The last equality again uses q^2-3q+1=0. Hence kappa_d>q^(2-S).
For the upper bound, |w_(m,k)|<2q^(k(k-1)/2) and a_k<q^(-k).
Writing r=d+1-k transforms the exponent into

```text
k(k-1)/2-kd=-S+r(r-1)/2.
```

Thus

```text
kappa_d<2q^(-S) sum_(r=0)^d q^(r(r-1)/2)
       <=2q^(-S)(2+q/(1-q))
       =2q^(-S-1)<6q^(-S),
```

since r(r-1)/2>=r-1 for r>=2 and q^(-1)=3-q<3. This proves E.
For Q(z)=z^d the target magnitude is one and source magnitudes are a_k^d.
The same error-sign extremizer as in D proves the exact worst error
eta*kappa_d. Equivalently log kappa_d=S log(phi^2)+O(1), with absolute
constants supplied by the two displayed bounds.

These are independent componentwise relative errors, not an assertion
about the correlated errors of an arithmetic method. In particular the
positive absolute result and the relative lower bound are compatible.

## 6. Arithmetic interpretation without an analytic promotion

For squarefree integers, the registered integral lift has factors
1-X_p-X_p^(-1) at split primes and -1 at non-split primes, including 5.
After X_p=t and tau=t+t^(-1), define B_a(N) as the sum of (-1)^b over
squarefree n<=N having a split and b non-split factors. Then directly

```text
Q_N(z)=sum_a B_a(N)z^a,
Q_N(1-tau)=sum_(n<=N)mu(n)^2 m_tau(n),
Q_N(-1)=M(N).
```

This is the finite source interpretation already recorded by PR #792.
For any integer d covering the support degree, the theorem reconstructs
the target from the d+1 positive golden rungs k=1,...,d+1. One may use
d=floor(log N/log 11) for N>=1, or any proved smaller degree bound.
The n=1 case has degree zero and one source value. The theorem is
independent of choosing an optimal degree bound.

The reconstruction supplies no estimates for these source sums. It also
does not replace the full integral shell by its squarefree restriction in
a Fourier contract: that is a different carrier question. No target
estimate enters the proof or verifier. All RH-strength obligations remain.

## 7. Accepted verifier, ranges, and negative controls

The fixed finite range is m=1,...,16, with d=m-1 and k=1,...,m.
Exact arithmetic audits the q-product formula in Q(sqrt5), its sign
via rational comparisons and squaring, and its rational equality to
the integer-node Lagrange construction. No approximate roots or logs
enter a decision. A rational Gaussian system is a second weight
construction at m<=6. The finite gates are:

```text
G1 nodes, rational Lagrange weights, and exact small reference weights;
G2 independent Q(sqrt5) product formula equals the rational weights;
G3 all monomials of degree 0,...,m-1 reconstruct, with Gaussian
   crosscheck for m<=6;
G4 alternating signs, sum one, positive product factors and envelopes;
G5 Lambda_m increases strictly and remains below 19/10;
G6 tail bound for K=0,...,m and strict tail beyond one below 1/2;
G7 relative monomial amplification, both E bounds, small references;
G8 exact absolute and relative independent-error extremizers.
```

Hand-derived reference values, frozen before execution:

```text
m=1: weights (1), Lambda_1=1.
m=2: weights (5/4,-1/4), Lambda_2=3/2, kappa_1=4.
m=3: weights (4/3,-4/11,1/33), Lambda_3=19/11, kappa_2=299/11.
```

Breakers must use the same production constructors or audit assertions:

```text
B1 wrong target 0 on m=2 weights fails Q(z)=z at actual target -1;
B2 removing weight signs on m=2 fails reconstruction of Q(z)=1;
B3 repeated nodes (-2,-2) are rejected;
B4 admitting target -1 as a source is rejected by the node contract;
B5 the assertion kappa_1<=19/10 fails at exact kappa_1=4.
```

G1-G8 and B1-B5 must all pass their intended decisions before the final
line `VERIFY RESULT 8/8 ALL PASS`. stdout is deterministic ASCII with LF.
No guessed decimal constant or finite observation is promoted to a
universal theorem. The independent mathematical review is result-exposed;
it is not described as blind.

## 8. Pin, execution and evidence discipline

Before the first accepted verifier execution, commit and push exactly
PREREG.md and verify.py, read back the complete commit, parent, file
blobs, raw SHA-256 and byte counts, and record the public pin in issue
#817. No development copy or scientific function of this verifier may
be executed before this pin. Static reading and in-memory parsing are
permitted. The theorem was derived symbolically and independently reviewed
before pinning; it is disclosed as proof-first and result-exposed.

Run from a clean Linux checkout at the pinned commit. First check a clean
interpreter with the same empty deterministic environment; it must emit
exactly PYTHON_STARTUP_CLEAN plus LF and no stderr. Then execute

```text
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-RAPIDITY-TARGET-RECONSTRUCTION-1/verify.py
```

under an external timeout of 600 seconds. Save exact stdout in EXPECTED.txt;
RUN.md records pin and byte custody, neutral environment fields, exit,
stdout/stderr hashes and sizes. RESULT.md states only the earned scope.
Require byte-identical replay on x86_64 and aarch64 through the existing
read-only workflow. No new workflow, package, dataset or copied handoff
material is required. Preserve every fired falsifier. Never amend, rebase,
force-push, repair or reuse an executed immutable pin.
