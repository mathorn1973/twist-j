# Independent derivation of the frozen rooted-current targets

**PUBLIC, NON-CANONICAL. Written before opening the author contract.**

Reviewer session: photon_breaker. Date: 2026-10-01.
The scope, exposure, source pins and comparison boundary are in
[PREREG.md](PREREG.md). This derivation uses candidate
`82b16f69418df669d0674d878afbf96eadfb3f4e` only through its PREREG.md and
REVIEW_SPEC.md. Scientific sources are the three admitted snapshots at
`44423153eee6259c7277eec5f5adbed9679f9146`.
No scientific computation was performed. All equalities and inequalities
below are written arguments, including the all-real-parameter statements.

## 1. The complete law, reversal and augmentation

Fix an even L>=4 and write V=L^4 and N=4V. Let P and E be the canonical
plaquettes and positive edges. On

```
Omega_L = {n in {-1,0,1}^P : partial n = 0 modulo 5},
mu_L(n) = Z_L^-1 2^(-|supp n|),
j = partial n/5,
```

the partition sum is finite and strictly positive because the zero field
is included. The boundary at an edge is a sum of six numbers in
{-1,0,1}. Its only multiples of five are -5,0,5. Thus j_e is always
-1,0 or 1. A sum of magnitude five has exactly five occupied terms, all
aligned: degree six has even sum and cannot produce five. A neutral edge
has even degree 2r, with r positive and r negative incidences. This uses
the complete law, without choosing a sector.

The map n -> -n is an involution of Omega_L, preserves the support weight
and Z_L, and sends j_e to -j_e. Pairing each state with its negative gives
E_mu j_e=0. Therefore

```
Var_mu(j_e) = E_mu j_e^2 = P_mu(j_e != 0) =: p_e.       (1)
```

This is unconditional reversal. A fixed nonzero exterior need not be
invariant under reversal, and no conditional symmetry of that sort is used.

For completeness, the prescribed paired augmentation keeps the same Z_L.
For each signed n, neutral edge e of degree 2r has r! compatible matchings.
The independent conditional choices give each complete matching weight
product_e 1/r!. Summing those choices is one for every n. Conversely,
given a consistent labeled (S,M), every link fixes the relative sign of
its two faces. A sign choice on one face in a connected component fixes
all others; cycle consistency makes this well-defined. Each of the k
components admits exactly two choices. Every signing has the same weight
2^(-|S|) product_e 1/(d_e/2)!. Hence its unsigned marginal is precisely

```
Z_L^-1 1_consistent 2^(k-|S|) product_(e:d_e even) 1/(d_e/2)!.
```

Summing it recovers the original Z_L. Conditional component signs are
independent uniform signs because all 2^k signings have identical weight.
This independence is on paired *face* components. It does not confer
independent signs on an arbitrary cycle decomposition or on disconnected
pieces of the current support.

Extend a reference component signing eta_K by zero outside K. Every neutral
pair cancels within its own K, even if several pairs at one neutral edge
belong to K. All five incidences at a charged edge lie in one K. Consequently
J_K=partial eta_K/5 is integer-valued, takes values in {-1,0,1}, and is
conserved because partial squared is zero. Each charged edge has exactly
one owner K, and all other components have zero current on that edge.
Neutral components and neutral joining paths remain in the probability
space. Also 5J_K is an integral boundary; since the integral H_1 of a torus
has no torsion, [J_K]=0. The minimum-size argument below does not require
individual cycles to have zero winding.

## 2. G1: one charged root from a linear observable

Fix any canonical edge e. Choose a plaquette p whose boundary contains e.
Translate and permute the canonical 21-face defect to obtain a ternary a
with support S of size 21 and

```
partial a = -5 partial p.
```

Induced orientation signs can change the overall sign but not its magnitude
at e. The defect's 21 faces remain distinct for every admitted L, including
L=4, by the canonical geometric input.

The observable

```
F_e(n) = (partial n)_e/5
       = sum_(p' incident to e) epsilon(e,p') n_p'/5
```

is a deterministic real linear observable on the full plaquette field.
It is exactly j_e on Omega_L, and |F_e(a)|=1. Apply the canonical
linear-observable variance lemma with this single S. The separation
condition for multiple sets is vacuous. It gives

```
Var_mu F_e >= 2^(1-2*21) |F_e(a)|^2 = 2^-41.           (2)
```

To expose the relevant conditioning step explicitly, condition on all
plaquettes outside S. If the zero filling is allowed and its conditional
probability is p_0, then +a and -a are also allowed and each has conditional
probability 2^-21 p_0. After subtracting the fixed exterior contribution,
their observable values are 0,+A,-A, where A=F_e(a). For any real or complex
conditional mean z, their variance contributions alone are

```
p_0 |z|^2 + 2^-21 p_0 (|A-z|^2 + |-A-z|^2)
  >= 2^-20 p_0 |A|^2.
```

All omitted contributions are nonnegative. If zero is forbidden, p_0=0
and the same lower bound is trivial. Total variance and averaging over
the entire exterior distribution give

```
Var_mu F_e >= 2^-20 |A|^2 E(p_0)
           = 2^-20 |A|^2 P_mu(n|S=0)
           >= 2^-20 * 2^-21 |A|^2.
```

The last estimate is the admitted *unconditional* empty-set estimate.
There is no assertion that every exterior permits zero or that the empty
probability is bounded below after fixing an arbitrary exterior. Using
(1) in (2) proves, at every root and volume,

```
p_e >= 2^-41.                                         (G1)
```

## 3. G2: minimum current support and the rooted moment

Orient each occupied edge in the direction of the sign of J_K. Conservation
means that indegree equals outdegree at every vertex. Any finite nonempty
balanced directed graph decomposes into edge-disjoint directed simple
cycles: follow outgoing edges until a vertex repeats, remove the resulting
simple cycle, and repeat. Removing a cycle preserves balance and strictly
decreases the finite edge set, so the procedure terminates. Unit capacity
ensures no current edge is counted more than once.

The underlying nearest-neighbor torus graph is simple for L>=4: it has no
loops and no parallel geometric edges. It is bipartite for even L, by the
parity of the sum of vertex coordinates. That parity is well-defined across
every periodic seam. A simple cycle is therefore even, and cannot have
length one, two or three. Every cycle has length at least four.

It follows that for each nonzero component current

```
M_K = |supp J_K| belongs to {4,6,...,N}.                (3)
```

This is an inclusion of possible sizes, not a claim that every listed size
is realized. Winding cycles satisfy the same graph argument. The proof does
not remove them, select a preferred cycle decomposition, or assume current
support is connected. Several disconnected cycles can belong to one K.

For each root, on its charged event M_K(e)^3>=4^3=64. The augmentation has
the original signed marginal, so its charged-root probability equals p_e.
Consequently

```
E_aug[1_(e charged) M_K(e)^3] >= 64 p_e >= 2^-35.
```

Averaging this inequality over exactly N=4V canonical roots gives

```
R3(L) >= 2^-35.                                       (G2)
```

There is no extra orientation factor. Uncharged roots contribute zero.
As a consistency check on normalization, the exact deterministic count is
sum_e 1_(e charged) M_K(e)^3 = sum_K M_K^4: each component is counted once
at each of its M_K charged edges. Neutral faces do not enter M_K.

## 4. G3: the specified certificate, with its logical direction

Assume a future theorem supplies R3(L)<=C for every admitted L. G2 forces
C>=2^-35. With rho=1/(36*2^41), direct arithmetic gives

```
C/16 >= 2^-39 = 144 rho.
```

The admitted NON-CANONICAL reduction chi_L(t)<=Xi_L<=R3(L)/16 then supplies
the particular upper certificate chi_upper=C/16, uniformly in allowed
nonzero lattice frequencies. On the originally specified nonempty family
of joint ordered profiles, it is compatible with the canonical lower
certificate b_lower=25rho. Their certified margin is

```
b_lower - 25 chi_upper = 25rho - 25C/16 = -D(C),
D(C) = 25(C/16-rho) >= 25*(144-1)rho = 3575rho > 0.   (G3)
```

These two certificates cannot prove a strict positive margin. A transverse
lower certificate used with this same C/16 must exceed 25C/16 for that
sufficient comparison to be positive. The actual b may exceed its lower
certificate and the actual chi may be below C/16; neither is equated with
its bound. The calculation therefore does not prove b-25chi<=0.

The canonical finite boundary terms remain

```
c_L = 2^-41 floor(L/3)^2/(4L^2),
rho - 2^-41/(6L) <= c_L <= rho,
S_n,02,02^L(t e_1) >= 25rho - 25*2^-41/(6L) - 10rho t^2.
```

For each admitted profile, take the thermodynamic limit with allowed
momenta tending to a fixed nonzero t, then the infrared limit t->0.
The displayed uniform upper bound passes through those limits wherever
the profile is defined. None of this constructs a profile, replaces a
Fourier limit by local weak convergence, interchanges limits, or substitutes
the smallest torus momentum. The dependency reduction's status is unchanged.

## 5. G4: finite telescoping and an exponential majorant

For a fixed root define X_e=M_K(e) on the charged event and X_e=0 otherwise.
It is a bounded nonnegative integer, X_e<=N, with
P(X_e>=r)=T_e(r) for r>=1. Set d_r=r^3-(r-1)^3=3r^2-3r+1>0. Pointwise,

```
X_e^3 = sum_(r=1)^N d_r 1_(X_e>=r).
```

Taking expectations and then the N-root average is a finite interchange,
giving exactly

```
R3(L) = N^-1 sum_e sum_(r=1)^N d_r T_e(r).             (4)
```

No independence assumption is involved. If, as an additional premise,
T_e(r)<=Aq^(r-1) uniformly in root and volume for A>=0 and 0<q<1, positivity
of d_r implies R3(L)<=A F_N(q), where

```
F_N(q) = sum_(r=1)^N d_r q^(r-1).
```

To evaluate the infinite sum and its exact remainder, for any real 0<=x<1
write

```
S0(x) = sum_(s>=0) x^s     = 1/(1-x),
S1(x) = sum_(s>=0) s x^s   = x/(1-x)^2,
S2(x) = sum_(s>=0) s^2 x^s = x(1+x)/(1-x)^3.           (5)
```

For example, termwise differentiation of the geometric series twice on
each compact subinterval of (-1,1) gives these identities; uniform absolute
convergence of the differentiated series there follows from domination by
a polynomial times a fixed geometric sequence. Thus the identities hold
for every real parameter in the stated range, not only sampled values.

Putting s=r-1 yields d_r=3s^2+3s+1, so

```
F_infinity(q) = 3S2(q)+3S1(q)+S0(q)
              = (1+4q+q^2)/(1-q)^3.                  (6)
```

For the omitted terms put r=N+1+s, s>=0. Then

```
d_(N+1+s) = (3N^2+3N+1)+(6N+3)s+3s^2.
```

Multiplying by q^(N+s) and using (5) proves the exact finite remainder

```
F_infinity-F_N
 = q^N [(3N^2+3N+1)/(1-q)
        +(6N+3)q/(1-q)^2 + 3q(1+q)/(1-q)^3].          (G4)
```

If the premise is instead T_e(r)<=Aq^r, each term has one further factor
q; both finite and infinite bounds are multiplied by q. This is a convention
change, not a change in the carrier or root normalization. If A=0 the
conditional implication still holds algebraically; G1 shows that such an
antecedent cannot describe this full measure. No q=1 claim is made.

## 6. G5: polynomial majorant and its uniform remainder

Assume T_e(r)<=C0 r^(-3-epsilon), with C0>=0 and epsilon>0, uniformly in
root and volume. Applying (4) gives the exact *majorant* sum

```
C0 sum_(r=1)^N d_r r^(-3-epsilon)
 = C0 [3H_N(1+epsilon)-3H_N(2+epsilon)+H_N(3+epsilon)]. (7)
```

This is equality for the deterministic majorant expression, not equality
between that expression and the actual moment. Each unsplit summand is
nonnegative. Since each zeta argument exceeds one, all three infinite
series converge absolutely, and their linear combination equals the same
unsplit positive sum with H replaced by zeta.

At r=1 the summand d_r r^(-3-epsilon) is exactly one. For r>=2,
d_r<=3r^2, hence it is at most 3r^(-1-epsilon). The decreasing positive
function x^(-1-epsilon) satisfies

```
sum_(r=2)^infinity r^(-1-epsilon)
 <= integral_1^infinity x^(-1-epsilon) dx = 1/epsilon.
```

This proves that the infinite majorant is at most C0(1+3/epsilon).
For the omitted tail beyond any positive integer N, the same comparison
starting at N gives

```
0 <= C0 sum_(r=N+1)^infinity d_r r^(-3-epsilon)
   <= 3C0 integral_N^infinity x^(-1-epsilon) dx
    = 3C0 N^(-epsilon)/epsilon.                        (G5)
```

The remainder is strictly positive if C0>0, and zero if C0=0. In the latter
case the algebraic implication remains valid but, again by G1, the premise
cannot hold for this full measure. No epsilon=0 extension is claimed.

## 7. G6: even-size contraction, endpoints and finite remainder

Let Kmax=(N-4)/2=2V-2. For k>=0 set

```
Q_k = T_e(4+2k).
```

By G2, Q_0=p_e, and Q_k=0 if 4+2k>N. The additional unproved premise (H)
is exactly Q_(k+1)<=theta Q_k for every root, volume and k>=0, with one
theta in [0,1). Induction gives

```
Q_k <= p_e theta^k <= p_* theta^k,       k>=1,
Q_0 = p_e <= p_*.
```

The k=0 case is stated separately to avoid an unnecessary 0^0 convention
when theta=0. If Q_k=0, nestedness already gives Q_(k+1)=0 and (H) needs
no division. If Q_k>0, Q_(k+1)/Q_k is precisely the conditional probability
of the nested larger-size event given the smaller charged-root event.
Thus the undivided version covers the complete domain of the premise.

For X_e in {0,4,6,...,N}, the even-size version of telescoping is

```
X_e^3 = 64 1_(e charged)
       + sum_(k=1)^Kmax [(4+2k)^3-(2+2k)^3]
                          1_(X_e>=4+2k).
```

The increment is

```
a_k = 8[(k+2)^3-(k+1)^3] = 24k^2+72k+56.
```

It follows root by root, and hence after averaging, that

```
R3(L) <= p_* G_Kmax(theta),
G_K(theta) = 64 + sum_(k=1)^K a_k theta^k.             (8)
```

The available unconditional choice p_*=1 uses only that p_e is a
probability; it does not supply (H). For every finite integer K>=0,
the same series identities (5) give

```
G_infinity(theta)
 = 64 + 24S2(theta)+72S1(theta)+56(S0(theta)-1)
 = (64-40theta+32theta^2-8theta^3)/(1-theta)^3.         (9)
```

For the tail, set m=K+1 and write

```
a_(m+s) = a_m+(48m+72)s+24s^2.
```

Using (5),

```
G_infinity-G_K
 = theta^(K+1) [a_(K+1)/(1-theta)
                +(48(K+1)+72)theta/(1-theta)^2
                +24theta(1+theta)/(1-theta)^3].        (G6)
```

At theta=0, (H) forces Q_1=0, all larger tails vanish and (8) gives the
correct bound 64p_*. Both G_K and G_infinity equal 64; the displayed
remainder is zero since K+1>=1. There is no singular denominator at this
endpoint. The formulas make no assertion at theta=1. For theta<1 they
hold for every real theta, by the exact power-series derivation above.

## 8. Attempts to break the statements and resulting boundary

The possible failure modes tested in writing have the following outcomes:

| Attack | Disposition within this derivation |
|---|---|
| Use reversal after fixing a nonzero exterior | Unnecessary and generally unjustified; G1 uses global reversal and then conditional variance averaged over the complete exterior. |
| Demand the defect fit beside every fixed exterior | Not required: forbidden zero fillings contribute p_0=0, and the unconditional empty-set bound controls the average. |
| Select one neutral matching or omit neutral components | Changes the measure; summing all compatible matchings proves the exact common Z_L. |
| Flip each current loop independently | Not an admitted law; only paired face-component signs are independent. |
| Reduce M_K to one cycle or exclude winding | Invalid for the carrier; the graph proof uses the entire unit-current support, including arbitrary cycle decompositions and winding. |
| Find an odd or two-edge current at an admitted volume | Excluded by the simple bipartite graph and unit-capacity conservation argument. Odd L or L=2 is outside the frozen domain. |
| Confuse sum_K M_K^4 with an unrooted third moment | The exact charged-edge count fixes the N=4V normalization; no factor is lost. |
| Infer an actual negative margin from negative certified margin | Not valid; G3 addresses only the specified certificate combination. |
| Treat a tail premise as a result | Not permitted; G4-G6 are conditional implications only. |
| Divide by a zero tail event or drop theta=0 | Avoided by the undivided recurrence and the explicit endpoint calculation. |
| Extrapolate sampled parameter checks or finite volumes | None used: geometric-series and integral arguments cover the full stated real-parameter and volume domains. |

The independent derivation establishes G1-G6 at their frozen analytical
scope, conditional on the named source statements where used. This is not
yet comparison with the author contract: that comparison is deferred until
the public freeze of this file and PREREG.md. No uniform upper bound on R3,
tail premise, existence or uniqueness of an ordered profile, physical
identification or open Canon-owner closure follows from this work.
