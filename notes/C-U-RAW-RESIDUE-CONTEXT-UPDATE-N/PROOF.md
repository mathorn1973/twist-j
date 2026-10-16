# Proofs: autonomous obstruction and driven update

**NON-CANONICAL. Candidate-T by analytical derivation, L1 only.**
Author: A. M. Thorn. Date: 2026-10-12, Europe/Prague.
Reservation: [#1474](https://github.com/mathorn1973/twist-j/issues/1474).
The complete scope and source pins are in [CONTRACT.md](CONTRACT.md).
These arguments were exposed before public pinning. No scientific program
has been authored or executed for this package.

## 1. Definitions and inherited native formulas

Write F5 for the field of five elements, with exact modular arithmetic.
For a nonnegative integer x define

```text
theta(x) = popcount(x) mod2,
S(x) = x-floor(x/2)+floor(x/4)-floor(x/8)+...,
S(0) = 0.
```

The sum is finite. This S is the exact alternating-floor sum in the
canonical raw-residue theorem; it is not a stochastic count or a chosen
ensemble. Native inputs are all P in F5^4 with common C_0=(0,1), origin
zero, and the unchanged driver theta_n=theta(n). The label is
`kappa(P)=sum(P) mod5`.

The inherited first-three-step table is:

| kappa | C_1 | C_2 | C_3=(a_k+1,b_k) | c_k=a_k+b_k |
|---|---|---|---|---|
| 0 | (0,4) | (0,1) | (1,0) | 0 |
| 1 | (1,4) | (0,1) | (2,0) | 1 |
| 2 | (1,0) | (4,0) | (2,1) | 2 |
| 3 | (2,0) | (3,0) | (3,1) | 3 |
| 4 | (0,1) | (1,4) | (1,2) | 2 |

Every row represents the 125 raw inputs with that sum. For n>=3 put

```text
sigma_n = (-1)^(n-3),
z_n = 4+2 theta(n-1) mod5,
N_n = S(floor((n-1)/2))-1 mod5.
```

The canonical inverse says

```text
q_3 = 1+sigma_n*(q_n-z_n)+N_n,
r_3 = sigma_n*r_n-N_n.
```

Since sigma_n^2=1, the equivalent forward formulas are

```text
q_n = z_n+sigma_n*(a_k-N_n),
r_n = sigma_n*(b_k+N_n).                         (1)
```

In particular, for odd n=2m+1 with m>=1,

```text
sigma_n=1, z_n=4+2 theta(m) mod5, N_n=S(m)-1 mod5,
q_n=z_n+a_k-N_n, r_n=b_k+N_n.                    (2)
```

No new trajectory assumption is made in (1)-(2); these are algebraic
rearrangements of the inherited all-time native inverse.

## 2. Digital lemma for the alternating-floor sum

Let x have binary digits b_j in {0,1}, only finitely many nonzero. Then

```text
S(x) = sum_j b_j w_j,
w_j = 2^j-2^(j-1)+...+(-1)^j
    = (2^(j+1)+(-1)^j)/3.                       (3)
```

To prove the first equality, substitute
`floor(x/2^k)=sum_(j>=k) b_j 2^(j-k)` into S and interchange the two
finite sums. The second is the finite geometric sum. Each w_j is an
integer, so no rounding or modular division is involved.

Moreover

```text
w_(j+4)-w_j = 5*2^(j+1),
(w_0,w_1,w_2,w_3) mod5 = (1,1,3,0).             (4)
```

Thus the weights repeat modulo five with period four. For integers whose
binary supports are disjoint, both S modulo five and theta add, in F5 and
F2 respectively. Shifting by a multiple of four preserves S modulo five
and preserves theta. These statements concern binary supports, not ordinary
addition with carries.

## 3. Explicit all-period, arbitrarily late realization lemma

**Lemma.** For every positive integer p, every nonnegative m_0, every
target t in {0,1}, every target s in F5 and every bound B, there exists
m>B such that

```text
m = m_0 mod p, theta(m)=t, S(m)=s mod5.          (5)
```

**Proof.** Factor p=2^a r with a>=0 and odd r>=1. Choose L>=4 divisible
by four and satisfying `2^L=1 mod r`. For r>1 such an L exists because
2 is a unit modulo r; one can take four times its multiplicative order.
For r=1 take L=4. No order or bound is computed here.

Define two finite positive integers by their indexed binary supports:

```text
E_r = sum_(j=0)^11 2^(jL)
      + sum_(j=0)^(10r-7) 2^(jL+1),
O_r = sum_(j=0)^(r-1) 2^(jL).                   (6)
```

The second sum in E_r has 10r-6 terms, at least four. Since L>=4,
all exponents within each displayed support and between its two columns
are distinct. In particular these sums create no binary carries.

Reduction modulo r and equations (3)-(4) give

```text
E_r = 12+2(10r-6)=20r=0 mod r,
theta(E_r)=(10r+6) mod2=0,
S(E_r)=(10r+6) mod5=1;

O_r = r=0 mod r,
theta(O_r)=r mod2=1,
S(O_r)=r mod5.                                 (7)
```

The modular evaluations of S follow because all E_r exponents are 0 or
1 modulo four and all O_r exponents are 0 modulo four, so every involved
weight is 1 modulo five. The statements modulo r also hold for r=1.

Put `epsilon=t-theta(m_0) mod2`, represented by 0 or 1, and choose
`j_* in {1,2,3,4,5}` with

```text
j_* = s-S(m_0)-epsilon*r mod5.                  (8)
```

Using 5 for residue zero makes j_* positive. Choose a positive H divisible
by L and larger than every binary exponent occurring in E_r or O_r.
Set

```text
Q = epsilon*O_r + sum_(j=1)^(j_*) 2^(jH) E_r.  (9)
```

The unshifted O_r occupies only positions below H. The j-th E_r copy
occupies positions from jH through a number strictly below (j+1)H.
Consequently every summand in (9) has disjoint binary support from the
others. The multiples of H preserve the weight classes modulo four.
Equations (7)-(9) therefore imply

```text
Q>0, Q=0 mod r,
theta(Q)=epsilon,
S(Q)=epsilon*r+j_* = s-S(m_0) mod5.             (10)
```

Finally choose K divisible by L, with K>=a, strictly above every binary
position occupied by m_0, and large enough that `m_0+2^K Q>B`.
There are arbitrarily large such K. Define

```text
m = m_0+2^K Q.                                 (11)
```

The two terms have disjoint binary supports. Since K is divisible by four,
(3)-(4) and (10) give theta(m)=t and S(m)=s modulo five.
Since Q is divisible by r and K>=a, the difference `2^K Q` is divisible
by p=2^a r. Positivity and the choice of K give m>B. This proves every
clause of (5). The construction is finite for every p, with no bound on
p, period, transient or B. It also proves arbitrarily late realization
by taking B arbitrarily large. QED.

## 4. The whole finite-autonomous-context obstruction

**Theorem A.** In class A of CONTRACT.md, every eventually permanent
original-residue readout F is constant. Conversely every constant F has
a one-state realization.

**Proof.** An orbit of a self-map of a finite nonempty set is ultimately
periodic. Thus there are integers N_A>=0 and p>=1 such that

```text
a_(n+p)=a_n for every n>=N_A.                   (12)
```

This requires neither injectivity nor any restriction on the transient.
There are finitely many raw inputs P. If the eventual readout property
holds with source-dependent thresholds N_P, let N_* be their maximum
together with N_A and 3. Choose any odd `n_0=2m_0+1>=N_*` and put
`a_*=a_(n_0)`.

By the lemma, for every pair `(t,s) in F2 x F5` there are arbitrarily
late m with m=m_0 modulo p, theta(m)=t and S(m)=s modulo five. At the
corresponding odd n=2m+1,

```text
n-n_0=2(m-m_0)=0 mod p,
n>=N_*, hence a_n=a_*.                         (13)
```

The first congruence works for every p, including even periods; no division
by two modulo p is used. Both ticks are odd by construction. Equations
(2) and (5) show that, at these times with the same context a_*, each
original label k visits every point of the following exact receiver set:

```text
R_k = L_(1+c_k) union L_(4+c_k),
L_u = {(q,r) in F5^2 : q+r=u}.                 (14)
```

Indeed t takes both values, so z takes 1 and 4; s takes every value,
so N=s-1 takes all five values. For fixed z, the coordinate r=b_k+N
therefore takes all five values and q is then uniquely determined by
q+r=z+c_k. Conversely (2) always lies in (14). Each actual late point
is reached for every raw input with that same k; no independently
controlled generator trajectory has been substituted for native U.

The five sets are

| k | Allowed values of q+r in R_k |
|---|---|
| 0 | {1,4} |
| 1 | {2,0} |
| 2 | {3,1} |
| 3 | {4,2} |
| 4 | {3,1} |

The eventual hypothesis forces `d(a_*,q,r)=F(k)` on all of R_k. Their
overlap graph is connected: R_0 and R_2 share L_1; R_0 and R_3 share
L_4; R_3 and R_1 share L_2; R_2=R_4. A fixed function on an intersection
cannot take two unequal values. Hence

```text
F(0)=F(2)=F(4), F(0)=F(3)=F(1),
```

and F is constant. A one-state context and a constant d supply the
converse. This decides the entire frozen class A. QED.

### An explicit conflicting pair for full five-label recovery

The overlap proof already excludes every nonconstant F. For a concrete
two-label collision, keep the same context-period p and take an odd
`n=2m+1` after its transient. Apply the lemma with target theta(m')=theta(m)
and S(m')=S(m)+1 modulo five, with m'=m modulo p and m' arbitrarily late.
Put n'=2m'+1. Then a_n=a_(n'), sigma_n=sigma_(n')=1, z_n=z_(n') and
N_(n')=N_n+1 modulo five. Formula (2) gives

```text
C_(n')(k=2)
 = (z+1-(N+1), 1+(N+1))
 = (z-N, N+2)
 = C_n(k=4).                                  (15)
```

The two sources are admitted, for example P=(2,0,0,0) and P=(4,0,0,0).
A faithful residue reader would have to return PRESENT(2) and PRESENT(4)
on the same pair (a_*,q,r). This is an actual arbitrarily late native
collision, not only a finite ambiguity of the inherited twenty-context
summary. No claim is made that the full integer counter is necessary:
class B below is an explicit different supplied interface.

## 5. The explicitly driven update

**Theorem B.** The 23-state bit-driven construction in CONTRACT.md,
initialized once at I0 and supplied with b_n=theta(n) at transition
n->n+1, returns BLANK at n=0,1,2 and PRESENT(kappa(P)) for every P
and every n>=3. It uses only 20 possible ready contexts. Minimality and
physical or native-register implementation are not asserted.

**Proof.** The three total startup rules place the context at

```text
tau_3=(1,1,0)
```

after the first three transitions. This is precisely
`(sigma_3,z_3,N_3)`, since theta(2)=1 and S(1)=1. The raw family has
the inherited distinct C_3 values in the table of section 1. The reader
at I0,I1,I2 returns BLANK by definition, so the readiness convention
has an explicit finite implementation in this abstract observer.

Suppose at an admitted time n>=3 the context is
`tau_n=(sigma_n,z_n,N_n)`. Its z coordinate determines the previous
bit exactly:

```text
t(z_n)=theta(n-1),
delta_n=[b_n=t(z_n)]=[theta(n)=theta(n-1)].      (16)
```

The canonical increment identity is

```text
N_(n+1)-N_n=delta_n mod5.                      (17)
```

Also sigma_(n+1)=-sigma_n and
z_(n+1)=4+2 theta(n) modulo five. Therefore the complete primitive
update h_(b_n) gives exactly tau_(n+1). Induction from tau_3 proves
that the maintained finite context agrees with the canonical evaluation
summary at every admitted time.

For completeness, (17) follows directly from the same finite sum: if
M>=1, then `S(M)-S(M-1)` is the alternating sum of `nu_2(M)+1` ones,
hence is 1 for even nu_2(M) and 0 for odd nu_2(M). For odd n=2m+1,
the floor argument of S does not change at n->n+1, while
theta(2m+1)=1-theta(m) differs from theta(2m)=theta(m), so both sides
of (17) vanish. For even n=2m, its S argument advances m-1->m.
The binary identity

```text
theta(m)-theta(m-1)=1-nu_2(m) mod2
```

shows that theta(2m)=theta(m) equals
theta(2m-1)=1-theta(m-1) exactly when nu_2(m) is even. Thus (17)
holds also at every even step. This derivation uses the actual native
Thue-Morse driver, not arbitrary bit sequences.

With the maintained tau_n, the reader's restored (qhat,rhat) is the
inherited C_3 for that input, by the inverse in section 1. Its fixed
five-point table consequently returns PRESENT(kappa(P)) for every P
and every n>=3. No input-specific initial context, receiver feed into
the updater, source-side sum, saved receiver history, new preparation
between steps or integer-counter evaluation is used. QED.

## 6. Resource and scope accounting

- Class A covers all finite autonomous source-independent contexts, with
  arbitrary finite transients and arbitrary nonlinear readers. Its exact
  negative conclusion is scoped to the common-ready raw-input receiver
  port and an eventually permanent original-sum function. It is not a
  no-go for all native readings, full-checkpoint factors or physics.
- Class B has three initial-readiness states and at most twenty ready
  contexts. The bound counts the previous-bit information stored in z,
  the sign phase sigma and N modulo five. All are source-independent.
  No claim is made that every listed state occurs, that all are needed,
  or that 23 is the least possible total cardinality. Class A implies
  that simply dropping the exposed bit and retaining some other finite
  independent autonomous clock cannot reproduce the claimed readout.
- The B updater is a mathematical transducer. Its exposed exact bit,
  timing and startup are supplied; an implementation of that input port
  or of a reversible complete context mechanism is not derived. U is
  unchanged and receives no feedback from this observer. The primitive
  context update need not be injective. No discarded information is
  claimed to disappear from a closed physical apparatus for free.
- Observing the scalar native trace after synchronization is another
  possible driving interface because z_(n+1)=4+2 theta(n). Such access
  is not assumed by A or silently added to B. In particular the native
  six-coordinate sum is not the bare receiver sum q+r. No separate
  trace-driven minimum or trace sensor is constructed here.
- A receiver-driven observer can store the payload after C_1, whose
  five values are distinct. That observation writes source-dependent
  memory and changes the resource class. It does not contradict A and
  is not the source-independent context of B.
- BLANK through tick two is a readiness convention. No sixth semantic
  source/absence distinction is introduced. Equal-sum raw inputs still
  have identical receiver histories, so the canonical presence boundary
  remains intact.
- No source erasure, repeated input/loading rule, durable physical
  archive, reset, occurrence law, sampling law, physical clock, energy
  selection, apparatus completeness or L2-L6 bridge follows.

The all-period and all-time conclusions rest on these written arguments.
A future bounded exact audit can check their identities and examples but
cannot replace their quantifiers. No such audit has been executed here.
