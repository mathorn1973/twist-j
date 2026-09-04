# Full-shell reconstruction from nonzero Fourier modes

**NON-CANONICAL / PROOF-FIRST CONTRACT DRAFT / NO FORMAL PIN OR RUN.**

Date: 2026-09-05. Public basis: `main`
`1a58703ec17a4c031bb8c450f56162f5aa3e5e5a`, Public Canon v76.
This note proposes a finite mathematical contract. It creates no Registry
row, public status, preregistration, verifier, formal execution, or evidence
gate. No scientific code was executed in deriving or writing it. No claim
of novelty over classical finite Fourier frames or the existing Canon
separation and Fejer proofs is made. Any formal successor needs its own
collision scan, scope, public claim, accepted verifier, and pin.

Independent static review checked the support, frame, reconstruction,
error domains and the separately sourced arithmetic corollary. No
mathematical blocker remains in this candidate; no formal status is earned
by this review.

The extension investigated here is precise: replace the existing finite
split prime-power address set by the complete Laurent-monomial support of
the integral shell through N. Reconstruct augmentation on that whole finite
space using only positive Fourier modes, with a bound on the reconstruction
cost. This supplies no bound on the arithmetic source values and does not
close `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`.

## 1. Public inputs and exact domains

The inputs are the registered integral rapidity lift and the universal
separation theorem, not an analytic Hecke interpretation:

- [Integral lift and its prime-power coefficients](https://github.com/mathorn1973/twist-j/blob/07910adb8418742bf52a0d204577b84b38009b18/canon/CANON.md#L7268):
  `J-IDEAL-RAPIDITY-CHARACTER-LIFT [T]` and the accompanying ternary census.
- [Split-prime independence](https://github.com/mathorn1973/twist-j/blob/07910adb8418742bf52a0d204577b84b38009b18/canon/CANON.md#L6827):
  `SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T]`.
- [Universal effective-vector separation](https://github.com/mathorn1973/twist-j/blob/07910adb8418742bf52a0d204577b84b38009b18/canon/CANON.md#L6895):
  `SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION [T]`.
- [Existing finite address Fejer bound](https://github.com/mathorn1973/twist-j/blob/07910adb8418742bf52a0d204577b84b38009b18/canon/CANON.md#L7033):
  `SPLIT-RAPIDITY-FEJER-GRAM-BOUND [T]`, whose registered carrier is narrower
  than the carrier defined below.
- [The open evaluation obligation](https://github.com/mathorn1973/twist-j/blob/07910adb8418742bf52a0d204577b84b38009b18/canon/CANON.md#L9728).

Fix an integer N >= 1. Set F=Q(sqrt(5)), phi=(1+sqrt(5))/2, and L=log(phi).
Let S_N be the finite set of rational primes p <= N split in F. Choose an
oriented prime ideal above each such p and an allowed totally positive
generator of norm +p. Write eta_p for its rapidity and
theta_p=eta_p/L modulo Z. This is a labeling choice, not an orientation
selector. The constructions below are invariant under relabeling either
prime-ideal pair and under the allowed unit-gauge changes.

All vector spaces below are finite-dimensional complex vector spaces. The
action layer is NOT_APPLICABLE: exact arithmetic and finite function-space
analysis only. No physical, probabilistic, Hecke, automorphic, or L1-L6 lift
is supplied.

## 2. The complete shell carrier

For a finite exponent vector a=(a_p) over S_N define

```text
P(a) = product_p p^|a_p|,
Gamma_N = {a in {-1,0,1}^S_N : P(a) <= N},
X^a = product_p X_p^a_p,
V_N = span_C {X^a : a in Gamma_N},
D_N = |Gamma_N|,
theta_a = sum_p a_p theta_p modulo Z,
z_a = exp(2 pi i theta_a).
```

The zero vector belongs to Gamma_N and represents the constant monomial.
If S_N is empty then Gamma_N={0} and V_N is the constant space.

**Exact support assertion.** Gamma_N is precisely the union of the Laurent
supports of `bold_mu(n)` for 1 <= n <= N.

Proof. At a split prime, the local coefficients of the registered integral
lift are

```text
bold_mu(p)   = 1-X_p-X_p^(-1),
bold_mu(p^e) = 2-X_p-X_p^(-1) for e>=2.
```

At a non-split prime they are -1 for exponent one and zero thereafter.
Every surviving exponent at a split prime is therefore -1, 0, or 1. Its
nonzero support consists of distinct primes dividing n, so P(a) <= n <= N.
Conversely, for a in Gamma_N take n=P(a). If a is nonzero, this is a
squarefree pure-split integer and the expansion of
`product_(p|n)(1-X_p-X_p^(-1))` contains X^a with nonzero coefficient
`(-1)^omega(n)`. For a=0 use n=1. This proves both inclusions.

In particular,

```text
D_N = sum_(r<=N, r squarefree and pure-split) 2^omega(r).
```

This support statement does not permit replacing the arithmetic sum
`P_N = sum_(n<=N) bold_mu(n)` by a squarefree-restricted sum. The two sums
can have the same ambient space while having different coefficients. The
nonzero split-prime-power residues remain part of P_N.

For f=sum_(a in Gamma_N)c_a X^a define

```text
aug(f) = sum_a c_a,
ev_h(f) = sum_a c_a z_a^h,       h in Z,
||f||_coeff,1 = sum_a |c_a|,
||f||_coeff,2^2 = sum_a |c_a|^2.
```

Only h > 0 will be source data. Neither ev_0 nor the value M(N) is admitted
as an input to the reconstruction.

## 3. Separation of the full support and D_N <= N

For distinct a,b in Gamma_N put c=a-b. It is nonzero, and

```text
P(c) <= P(a)P(b) <= N^2.
```

The first inequality is prime-by-prime, from
`|a_p-b_p| <= |a_p|+|b_p|`. The registered universal separation theorem
therefore gives

```text
dist(sum_p (a_p-b_p) eta_p, L Z)
    >= asinh(1/(2 sqrt(P(c))))
    >= delta_N := asinh(1/(2N)).
```

This uses the general effective-vector theorem, including coordinates of
magnitude two. It does not assume that a or b is a prime-power address.
In particular all z_a are distinct.

The golden identity `L=asinh(1/2)` and concavity of asinh on [0,infinity)
give

```text
delta_N >= L/N.
```

For completeness, the derivative of asinh is `(1+t^2)^(-1/2)`, which
decreases for t>=0; concavity and asinh(0)=0 imply
`asinh(t/N) >= asinh(t)/N`. Apply this at t=1/2.

Thus distinct theta_a have circular distance at least 1/N. If D_N>=2,
list these points in circular order. Every successive circular gap is at
least 1/N, while the gaps sum to one. Hence D_N<=N. If D_N=1 the same
inequality holds directly because N>=1; no minimum pairwise gap is needed
or defined in that case.

This proves the finite counting consequence

```text
1 <= D_N <= N.
```

## 4. A positive-frequency frame with a fixed linear cutoff

Set

```text
H = 2N,
source modes h = 1,...,2H-1 = 1,...,4N-1,
w_h = (H-|h-H|)/H^2.
```

Every w_h is a positive rational number, and sum_h w_h=1. Define the
sampling matrix T, the diagonal weight matrix W, and the Gram matrix B by

```text
T_(h,a) = z_a^h,
W = diag(w_h),
B = T* W T,
```

where star denotes conjugate transpose. These are defined by the complete
node set and not by any coefficients c_a or source values ev_h(P_N).

Here is a direct finite-frame proof of invertibility and its norm bound.
For integer H>=1 put

```text
Phi_(H-1)(u)
 = (1/H) sum_(r=-(H-1))^(H-1) (1-|r|/H) exp(2 pi i r u)
 = (1/H^2) |sum_(j=0)^(H-1) exp(2 pi i j u)|^2.
```

The second identity follows by collecting the pairs of indices with each
difference r. Consequently the kernel is nonnegative, equals one at
integer u, and satisfies

```text
0 <= Phi_(H-1)(u) <= min(1, 1/(4H^2 ||u||^2))
```

for nonintegral u, where ||u|| is circular distance to Z. The geometric-sum
formula gives the sine quotient, and `sin(pi t)>=2t` for 0<=t<=1/2 gives
the displayed bound.

Let A_(a,b)=Phi_(H-1)(theta_b-theta_a). It has diagonal one. Around any
fixed theta_a, each half-open distance shell

```text
j/N <= dist(theta_b-theta_a,Z) < (j+1)/N,  j>=1,
```

contains at most one point on either side: two on the same side within an
interval of length 1/N would violate the established separation. Thus
the sum of off-diagonal absolute values in any row is at most

```text
2 sum_(j>=1) N^2/(4H^2 j^2) = pi^2 N^2/(12H^2) = pi^2/48.
```

This is the same packing proof and constant as in the registered Fejer
row. A self-contained coarser bound is also sufficient here: for j>=2,
`1/j^2 < 1/(j(j-1))`, so telescoping gives `sum_(j>=1)1/j^2 < 2`.
The row sum is therefore strictly below `N^2/H^2=1/4`, without needing
the Basel-sum evaluation. For a singleton A=[1] and the norm is zero.
For a Hermitian matrix, a uniform absolute row-sum bound bounds the
Euclidean operator norm; this follows, for example, by applying the
weighted Cauchy inequality to each row and then summing. We obtain

```text
||A-I||_(2->2) <= rho := pi^2/48 < 1/3.
```

The coarser argument alone gives `||A-I||<1/4<1/3` and proves every
subsequent bound that uses 1/3. The elementary inequality pi<4 also
implies rho<1/3.

The actual positive-frequency Gram satisfies

```text
B_(a,b) = (z_b/z_a)^H Phi_(H-1)(theta_b-theta_a),
B = U* A U,       U=diag(z_a^H).
```

U is unitary. Therefore `||B-I||=||A-I||`, and in particular

```text
(1-rho)||v||_2^2 <= v* B v <= (1+rho)||v||_2^2,
```

for every coefficient vector v. B is positive definite and invertible.
The weaker but elementary interval `(2/3,4/3)` for its eigenvalues is
enough for the explicit reconstruction cost below.

### Frequency shift is not phase dilation

The source modes above are all strictly positive. The unshifted offsets r,
including r=0, occur only in the proof of the Gram bound; no ev_0(f) is
sampled. The formula for B is obtained directly from its positive modes.

Nor does this proof reuse the base spacing after multiplying every phase
by h. For a single integer h>0 and c=a-b, the correct product budget is

```text
P(hc)=P(c)^h <= N^(2h).
```

An individual dilated node set h theta_a therefore has no right to the
undilated 1/N spacing bound. What preserves the Gram norm here is the
displayed diagonal-unitary conjugacy of a *translated consecutive frequency
window*. Replacing that translation by h -> nu h is a different operation
and is not covered by this proof.

## 5. Exact reconstruction kernel and error contract

Let v be the D_N-vector whose entries are all one. Define

```text
u = B^(-1) v,
lambda_h = w_h conjugate((T u)_h),       1<=h<=4N-1.
```

This finite kernel is defined for every N>=1. For any f in V_N with
coefficient vector c,

```text
sum_h lambda_h ev_h(f)
 = (T u)* W T c
 = u* B c
 = v* c
 = aug(f).
```

The reconstruction residual is identically zero on the *whole* V_N, not
merely on one observed polynomial P_N. The vector v specifies the desired
functional; it does not contain its unknown value on P_N. No kernel fitting
against M(N), augmentation sample, hidden ev_0 mass, or residual functional
equal to augmentation is present. Applying the identity to f=1 gives the
necessary normalization `sum_h lambda_h=1`.

Since the w_h sum to one, weighted Cauchy gives

```text
sum_h |lambda_h|
 <= sqrt(sum_h w_h |(T u)_h|^2)
 = sqrt(v* B^(-1) v)
 <= sqrt(D_N/(1-rho))
 < sqrt(3D_N/2)
 <= sqrt(3N/2).
```

Thus this contract has linear cutoff 4N-1, exact reconstruction, and a
guaranteed kernel coefficient-l1 cost below sqrt(3N/2). It does not claim
that this bound is sharp or that every admissible kernel has this cost.

For approximate source values `F_h+e_h`, where F_h=ev_h(f) and independent
complex error discs satisfy |e_h|<=epsilon_h with epsilon_h>=0,

```text
sup |sum_h lambda_h e_h| = sum_h |lambda_h| epsilon_h.
```

For lambda_h nonzero, choose
`e_h=epsilon_h conjugate(lambda_h)/|lambda_h|` to attain the bound; zero
kernel entries contribute zero. In particular a common absolute error
epsilon is amplified by at most `sqrt(3N/2) epsilon`. If epsilon=0 the
error is exactly zero; the strict inequality inherited from the kernel
bound is used only when epsilon>0. Correlated errors can only reduce the
supremum relative to the independent-disc domain, but their actual
structure has not been modeled here.

No phase convention selects a split orientation: independently reversing
one theta_p permutes the columns indexed by Gamma_N. This conjugates B
by the corresponding permutation, fixes v, and leaves T B^(-1)v and the
kernel unchanged. Allowed integer shifts of theta_p leave T unchanged.

## 6. What is still missing on the arithmetic source side

For the actual integral sum

```text
P_N = sum_(n<=N) bold_mu(n),
F_N(h) = ev_h(P_N),
M(N) = aug(P_N),
```

the proven finite identity would give

```text
M(N) = sum_(h=1)^(4N-1) lambda_h F_N(h).
```

For example, source estimates

```text
max_(1<=h<=4N-1) |F_N(h)| <= C_epsilon N^epsilon
```

would be sufficient for `|M(N)| <= sqrt(3/2) C_epsilon N^(1/2+epsilon)`.
To reach the registered RH-strength target this would have to hold for
every epsilon>0 and be proved without importing the target or an equivalent
zero statement. This is only a sufficient conditional implication. The
classical corollary below rules out these unsigned source estimates for
epsilon<1/2. Signed
correlations in the particular kernel sum could instead be useful even
when an unsigned uniform-source estimate fails.

The elementary bounds currently available from the carrier do not supply
that estimate. In particular let

```text
T_N = sum_(n<=N) ||bold_mu(n)||_coeff,1,
H_N = sum_(j=1)^N 1/j.
```

The local norms 3 at a split prime and 4 at a split prime power of exponent
at least two are bounded by the corresponding three-divisor coefficients
`binomial(e+2,2)`. Non-split local coefficients are bounded as well.
Consequently

```text
||P_N||_coeff,1 <= T_N
 <= sum_(n<=N) d_3(n)
 = #{(a,b,c) in positive integers: abc<=N}
 <= N H_N^2.
```

The last bound follows by replacing each `floor(N/(ab))` by N/(ab) and
enlarging to a,b<=N. Hence the immediate source bound is only
`|F_N(h)|<=N H_N^2`, which combined with the kernel norm does not approach
the requested cancellation.

There is also a useful exact feasibility check for any attempt to control
all source magnitudes or their unsigned energy. Let R_N be the number of
split primes in `(N/2,N]`. For each such prime p, the coefficients of X_p
and X_p^(-1) in P_N are exactly -1: n=p is the only integer <=N divisible
by p. Therefore

```text
||P_N||_coeff,2^2 >= 2 R_N,
sum_h w_h |F_N(h)|^2
 = coeff(P_N)* B coeff(P_N)
 >= (1-rho)||P_N||_coeff,2^2
 >= 2(1-rho) R_N.
```

Thus the proposed uniform source estimate would necessarily imply
`2(1-rho)R_N <= C_epsilon^2 N^(2epsilon)`. This is an exact finite check
requiring no prime-counting asymptotic.

**Classical corollary, with a separately named external input.** Split
primes here are the two reduced residue classes 1 and 4 modulo 5. The
unconditional prime number theorem for fixed arithmetic progressions,
as stated in [DLMF 27.12.8](https://dlmf.nist.gov/27.12#E8), implies

```text
R_N = (1+o(1)) N/(4 log N).
```

This follows by subtracting the count through N/2 from the count through
N in those two classes. Since sum_h w_h=1, the finite energy bound yields

```text
max_(1<=h<=4N-1)|F_N(h)|
 >= sqrt(2(1-rho)R_N)
 = (sqrt((1-rho)/2)+o(1)) sqrt(N/log N).
```

Consequently the displayed O(N^epsilon) bound cannot hold on this whole
source window for any fixed epsilon<1/2. This exclusion uses that
classical theorem, not RH or GRH; the preceding reconstruction and finite
energy results do not require it. It excludes the stated uniform-magnitude
route for this stable frame, not the exact signed kernel reconstruction
or all possible Fourier families. The reconstruction identity does not
remove source energy. A signed correlation estimate for
`sum lambda_h F_N(h)` remains a distinct task.

## 7. Candidate breakers for a future formal contract

These are proposed symbolic or exact structural controls, not executed
gates and not a preregistration:

1. At N=209, the monomial X_11 X_19 belongs to Gamma_N. An address class
   containing only signed prime powers omits it and fails the full-carrier
   specification.
2. At N=121 the polynomial `bold_mu(11^2)=2-X_11-X_11^(-1)` is nonzero.
   Dropping it changes the source polynomial even though its augmentation
   is zero. The source constructor must detect this, rather than checking
   augmentation alone.
3. A source kernel with lambda_0=1 is rejected by the strictly-positive-mode
   contract, even though it would reconstruct augmentation vacuously.
4. Omitting the constant monomial is rejected by the Gamma_N definition;
   the actual kernel must pass `sum_h lambda_h=1`.
5. Replacing the consecutive frequency translation by a dilation is outside
   this contract and requires a new budget and proof. The unchanged Gram
   argument cannot be presumed valid; this does not assert algebraic
   failure for every special case, such as a singleton carrier. The
   product-budget identity is
   `P(h(a-b))=P(a-b)^h`, never the undilated budget by default.
6. The identity `sum_h lambda_h z_a^h=1` must hold on every basis monomial,
   not just on P_N or a fitted scalar value.
7. An alleged reconstruction residual containing augmentation is rejected:
   this contract has identically zero residual on V_N. Approximation error
   must enter through explicitly bounded source errors instead.

Any future verifier must state honestly which symbolic identities and
finite exact carriers it audits. Approximate evaluations of the actual
transcendental phases are not silently exact assertions. The written
proof supplies the universal mathematics; no finite run can certify the
all-N signed source cancellation estimate left open in section 6.

## 8. Disposition

This is a complete candidate finite reconstruction contract. Its extra
content relative to the registered prime-power Fejer row is the proved
full-support identity, the product-budget extension, the D_N<=N packing
consequence, and an explicitly constructed positive-frequency augmentation
kernel on all V_N. It does not identify an analytic automorphic family,
prove a source cancellation estimate, select a physical reading, or change
any existing status. The useful next decision is whether a signed source
mechanism exists at this frozen carrier and norm, after the elementary
source-energy obstruction has been respected.
