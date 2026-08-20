# Widder angle sweep, corrected depth, and the finite-prefix horizon

```text
STATUS:        candidate-T / NON-CANONICAL INCUBATION
PUBLIC BASIS:  Public Canon v57
SOURCE ISSUE:  #477
PARENTS:       #471 and #374
AUDITED INPUT: handoff/audit-euler-widder-depth-20260820
RH:            unchanged and open
```

## 0. Result and correction boundary

The pole calculus in #471 and in the handoff audit is correct. For one
conjugate squared-pole pair `z=-A+iB`, `A>0`, its contribution to the Widder
level is

```text
P_k(A,B;u)
 =2(2k-1)! Re[(A-iB)^k/(u+A-iB)^(2k)],       k>=1, u>0.
```

The handoff audit then made two stronger auxiliary claims:

```text
H1  P_k is negative for some u iff Re[(A-iB)^k]<0;
H2  the first failing level is ceil(pi/(2 arctan(B/A))).
```

Both need correction at their boundaries. The correct statements are:

```text
P_k is negative for some u
iff k arctan(B/A)>pi/2
iff some j<=k has Re[(A-iB)^j]<0;

k_min
 =floor(pi/(2 arctan(B/A)))+1
 =min{k>=1:Re[(A-iB)^k]<0}.
```

Thus the integer-power test survives exactly for first failure. It does not
decide an arbitrary later level from the endpoint power alone.

The main strategic conclusion of the audit survives and becomes stronger:
for every finite prefix length `N`, an explicit off-critical symmetric pole
configuration passes every level through `N` for every real `u>0`. No finite
Widder prefix can characterize RH in the symmetric pole class.

## 1. Pair formula and phase

Let

```text
a=A-iB,
b(u)=u+A-iB.
```

For `B>0`, define

```text
theta=arctan(B/A),
phi(u)=arctan(B/(u+A)).
```

Then

```text
a=|a| exp(-i theta),
b(u)=|b(u)| exp(-i phi(u)).
```

Therefore

```text
a^k/b(u)^(2k)
 = [|a|/|b(u)|^2]^k exp(i k(2phi(u)-theta)).
```

Taking the real part gives

```text
P_k(A,B;u)
 =2(2k-1)!
  [(A^2+B^2)^(1/2)/((u+A)^2+B^2)]^k
  cos(k(2phi(u)-theta)).                         (1.1)
```

The prefactor outside the cosine is strictly positive.

For `B=0`, equation (1.1) reduces to

```text
P_k(A,0;u)=2(2k-1)! A^k/(u+A)^(2k)>0.
```

Only `B>0` needs further analysis.

## 2. The angle-sweep theorem

Differentiate:

```text
phi'(u)=-B/((u+A)^2+B^2)<0.
```

The endpoint limits are

```text
lim_(u->0+) phi(u)=theta,
lim_(u->infinity) phi(u)=0.
```

Hence

```text
delta(u):=2phi(u)-theta
```

is continuous and strictly decreasing, with

```text
lim_(u->0+) delta(u)=theta,
lim_(u->infinity) delta(u)=-theta.
```

Thus `delta` maps `(0,infinity)` bijectively onto the open interval
`(-theta,theta)`.

### Theorem 2.1

For every integer `k>=1`:

```text
P_k(A,B;u)>0 for every u>0  iff k theta<=pi/2,
P_k(A,B;u)<0 for some u>0   iff k theta>pi/2.       (2.1)
```

### Proof

If `k theta<=pi/2`, then for every finite `u>0`,

```text
|k delta(u)|<k theta<=pi/2.
```

Therefore `cos(k delta(u))>0`, and (1.1) is strictly positive.

If `k theta>pi/2`, choose a real number `d` satisfying

```text
pi/(2k)<d<min(theta,pi/k).
```

Such a `d` exists because `theta>pi/(2k)` and `pi/k>pi/(2k)`. The sweep gives
one `u>0` with `delta(u)=d`. Then

```text
pi/2<k d<pi,
```

so the cosine and the pair contribution are negative. This proves (2.1).

At the equality `k theta=pi/2`, the cosine approaches zero only at the open
endpoints of the sweep. It remains strictly positive at every finite `u>0`.
This endpoint fact is load-bearing for the first-failure formula.

## 3. Corrected first-failure depth

Define

```text
k_min=min{k>=1:P_k(A,B;u)<0 for some u>0}.
```

By Theorem 2.1,

```text
k_min=min{k>=1:k theta>pi/2}
     =floor(pi/(2theta))+1.                         (3.1)
```

The ceiling expression is equal to (3.1) only when the quotient is not an
integer.

### Theorem 3.1, exact integer first-failure test

```text
k_min=min{k>=1:Re[(A-iB)^k]<0}.                    (3.2)
```

### Proof

For every `j<k_min`, `j theta<=pi/2`, so

```text
Re[(A-iB)^j]=|A-iB|^j cos(j theta)>=0.
```

For `j=k_min`, minimality gives

```text
(k_min-1)theta<=pi/2<k_min theta.
```

Also

```text
k_min theta<=pi/2+theta<pi.
```

Therefore `cos(k_min theta)<0`, proving (3.2).

### Corollary 3.2, corrected arbitrary-level integer criterion

For any fixed integer `k>=1`:

```text
P_k(A,B;u)<0 for some u>0
iff k>=k_min
iff there exists j<=k with Re[(A-iB)^j]<0.          (3.3)
```

This is the exact no-pi form. The endpoint sign at the same level `k` is not
enough after the phase has rotated past further cosine periods.

## 4. Polynomial coefficient form

The same correction can be seen without dividing complex numbers. Multiply by
the positive denominator:

```text
Re[a^k/b(u)^(2k)]
 =Re[(A-iB)^k(u+A+iB)^(2k)]
  /[((u+A)^2+B^2)^(2k)].                            (4.1)
```

Expand the numerator:

```text
N_k(u)
 =sum_(j=0)^(2k) C(2k,j) u^j
   Re[(A-iB)^k(A+iB)^(2k-j)].                       (4.2)
```

Writing `R=sqrt(A^2+B^2)`, the coefficient of `u^j` is

```text
C(2k,j) R^(3k-j) cos((k-j)theta).                   (4.3)
```

If `k theta<=pi/2`, then `|(k-j)theta|<=k theta<=pi/2` for every
`0<=j<=2k`. Every coefficient in (4.2) is nonnegative and at least the middle
coefficient is positive. Hence `N_k(u)>0` for every `u>0`.

At the first failing level, the constant coefficient is negative because
`cos(k_min theta)<0`, so the polynomial is negative for sufficiently small
positive `u`. At later levels that constant coefficient can return positive,
while an interior interval remains negative. This is exactly why the handoff
endpoint criterion fails only after first failure.

## 5. Two exact counterexamples to the handoff wording

### 5.1 Arbitrary-level endpoint return

Take

```text
A=B=1, k=8, u=1/2.
```

The endpoint power is

```text
Re[(1-i)^8]=16>0.
```

Direct exact rational arithmetic gives

```text
P_8(1,1;1/2)
 =-172056926056081143103488000/51185893014090757<0.   (5.1)
```

Here `theta=pi/4` and `k theta=2pi`. The endpoint cosine has returned to `+1`,
but the swept interval contains many negative arcs. This falsifies H1 at its
arbitrary-level scope.

### 5.2 Resonance of the ceiling formula

Again take `A=B=1`, so `theta=pi/4`. At `k=2`,

```text
k theta=pi/2.
```

By Theorem 2.1, `P_2(1,1;u)>0` for every finite `u>0`; zero is only an
unattained endpoint infimum. The first negative level is

```text
k_min=floor(2)+1=3.
```

The expression `ceil(2)=2` is therefore false at exact resonance. This
falsifies H2 only at the integer-quotient boundary.

## 6. The owner depths survive

For the two controls in #471 and the handoff audit:

```text
rho=9/10+i/2:
A=17/50, B=2/5,
min{k:Re[(A-iB)^k]<0}=2.

rho=3/4+10i:
A=1603/16, B=5,
min{k:Re[(A-iB)^k]<0}=32.
```

These are exact integer-power calculations after clearing denominators. The
correction changes neither depth.

The large-height asymptotic also survives. For fixed `beta>1/2` and
`gamma->infinity`,

```text
B/A
 =gamma(2beta-1)/(gamma^2+beta(1-beta))
 =(2beta-1)/gamma+O(gamma^-3),

theta=arctan(B/A)
 =(2beta-1)/gamma+O(gamma^-3).
```

Thus

```text
k_min~pi gamma/(2(2beta-1)).                       (6.1)
```

Only the exact floor convention changes.

## 7. Intrinsic finite-prefix horizon

### Theorem 7.1

For every integer `N>=1`, there is an explicit off-critical symmetric
synthetic zero orbit whose contributions to

```text
f,W_1,...,W_N
```

are strictly positive for every `u>0`.

### Construction

Take

```text
rho_N=3/4+iN.
```

Its functional and conjugation closure is

```text
{rho_N,1-rho_N,conj(rho_N),1-conj(rho_N)}.
```

This set violates RH because `Re rho_N=3/4`. In the squared-pole coordinate,
its conjugate pair is

```text
z_N=-A_N+iB_N,
A_N=N^2+3/16,
B_N=N/2.
```

Exactly,

```text
B_N/A_N
 =(N/2)/(N^2+3/16)
 =8N/(16N^2+3)
 <1/(2N).                                           (7.1)
```

For `theta_N=arctan(B_N/A_N)`, the elementary inequality
`arctan x<x` gives

```text
theta_N<1/(2N).
```

For every `1<=k<=N`,

```text
k theta_N<k/(2N)<=1/2<pi/2.
```

Theorem 2.1 gives

```text
P_k(A_N,B_N;u)>0
```

for every `u>0`. The `f` contribution is positive by the unconditional pair
formula

```text
2(u+A_N)/((u+A_N)^2+B_N^2)>0.
```

This proves the theorem.

### Corollary 7.2

No finite prefix of the Widder hierarchy, even if each level is known as a
complete function on all `u>0`, characterizes RH in the class of finite pole
multisets with the functional and conjugation symmetries of xi.

Any positive critical-line background can be added to the construction and
preserves every inequality in the prefix. Exponential masking is therefore
not needed for this no-go. The handoff masking calculation remains a valid
bounded mechanism witness, but the intrinsic finite-prefix horizon is already
a theorem before background competition is considered.

This is a no-go about a criterion class. It supplies no information about the
actual zeta zero set.

## 8. Conditional safe depth for the actual zeta function

Let an off-critical nontrivial zero be

```text
rho=beta+i gamma,       0<beta<1,
```

and put

```text
A=gamma^2+beta(1-beta),
B=|gamma(2beta-1)|.
```

For `|gamma|>=H>=1`,

```text
B<|gamma|,
A>gamma^2,
B/A<1/|gamma|<=1/H.                              (8.1)
```

Hence

```text
theta<arctan(1/H).
```

Assume every zero with `|gamma|<H` lies on the critical line. Such lower
zeros have `B=0` and contribute positively at every level. Every possible
off-line zero lies above `H`. Therefore all levels

```text
1<=k<=floor(pi/(2 arctan(1/H)))                    (8.2)
```

are strictly positive for every `u>0`.

Since `arctan(1/H)<1/H`, the simpler conservative range

```text
1<=k<=floor(pi H/2)                                (8.3)
```

also follows.

Taking only a rigorous zero-free height above one in (8.2) gives

```text
W_2(u)>0 for every u>0.
```

Any numerical value of `H` is an imported witness and needs its own source and
certificate before public use. This note does not freeze one.

## 9. Boundary on level-to-level induction

The low synthetic control

```text
rho=9/10+i/2
```

has `W_1` positive for every `u>0` and `W_2` negative for some `u>0`.
Therefore no universal term-by-term rule

```text
one pole pair positive at level k
implies the same pair positive at level k+1
```

exists, already at `k=1`.

This does not exclude a theorem using the complete Euler plus archimedean sum.
It does exclude treating the proposed `W_k -> W_(k+1)` step as a local
positive induction on individual prime or pole atoms.

The surviving source task is global from the start:

```text
construct the Stieltjes measure directly,
or produce all Widder levels simultaneously from one positive global
Euler-archimedean object.
```

An adjacent-level scalar induction is not yet ruled out for the specific full
xi function, but it would have to use cancellations and structure absent from
every termwise formulation.

## 10. Corrected status ledger

```text
[candidate-T] angle-sweep theorem, equation (2.1).
[candidate-T] corrected first-failure and integer-power criteria.
[bounded F]   arbitrary-level endpoint criterion from the handoff audit.
[bounded F]   exact-resonance use of ceil in the handoff audit.
[candidate-T] intrinsic finite-prefix horizon, Theorem 7.1.
[candidate-T] conditional actual-zeta safe-depth theorem.
[candidate-T] termwise adjacent-level positive induction no-go.
[candidate-C] exact rational controls and owner-depth reproductions.
```

The handoff audit's main redirection survives after correction:

- do not attack `W_2`;
- do not expect a finite hierarchy prefix to decide support;
- do not use the same-level endpoint power after first failure;
- do not attempt a termwise positive induction in `k`.

The right positive target is a global Stieltjes representation or an
equivalent all-level Euler construction. RH remains open. No public claim or
status moves by this note.
