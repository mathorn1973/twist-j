# Full rooted-current tail: exact contract and the certified-floor deficit

**PUBLIC, NON-CANONICAL local draft. No authority.**
**Status:** pending review; no earned claim, formal run, or candidate pin.
**Action layer:** L6 mathematics of the explicitly selected finite measure.
**Date:** 2026-10-01. **Author:** A. M. Thorn, assisted by a scoped agent.

The uniform upper bound on the full rooted third moment is **not proved**
here. This draft reconstructs its exact measure, states one sufficient
conditional tail inequality with evaluated consequences, and supplies a
written derivation of a quantitative limitation of combining the inherited
moment majorant with the published local transverse floor. That limitation
is about the stated certificate, not the sign of the true infrared contrast.
No physical photon claim or P1 closure follows.

## 1. Authority, sources, and exposure

Execution basis supplied and checked by the coordinator: Public Canon v96,
public main and tag target
`44423153eee6259c7277eec5f5adbed9679f9146`; declared content commit
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`. Canon has 873495 bytes and SHA-256
`eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
The source files below were read at that main commit, and their SHA-256
values were checked locally. These are input pins, not a pin of this draft.

| Input path relative to repository root | SHA-256 |
|---|---|
| `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md` | `7ce7bdf7501e0e4b56de806a59b47ea53efc333cb141753c9d253576c211f0fe` |
| `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/SIGNED-SLICES.md` | `2b592a32912b4e02320b3a98946ba4ba02f50df221a85f3a40b49c907ca700f2` |
| `notes/C-CURRENT-PRIME-GATE-N/PROOF.md` | `ad34c7e6c3247a13fc32bbe125540929ffe97ec1885d40a442e08e27649cdc09` |
| `notes/C-PHOTON-CONTACT-TURN-SKELETON-N/PROOF.md` | `fc3dc556524cd9e9a125e209168f0531ee15dbe8a540e4cb8b7e5b19ed582dc7` |
| `notes/C-PHOTON-WHOLE-CURRENT-MOMENT-N/PREREG.md` | `9be196de72260a4682582b938ddbc6b5381ba94dc41079c86dc1d897884bde59` |
| `notes/C-PHOTON-WHOLE-CURRENT-MOMENT-N/PROOF.md` | `82029583a8f27acfeec0461edf1c10d01613a2966aecc772a1264770b3a5054b` |

The whole-current input's own preregistration pin is
`769a55d44ff71b7cacc4bebbeedf300b3982ec8b`; it remains NON-CANONICAL.
Its closed item #1198 proves the deterministic reduction, not its missing
probability premise. The broader owners
[#1122](https://github.com/mathorn1973/twist-j/issues/1122) and
[#1143](https://github.com/mathorn1973/twist-j/issues/1143) remain open.
Their public issue bodies were read. The #1122 proof was additionally read
from immutable Git blob `b828f5906e1102c1bb550998f60dbca3a9f79cdc`.
Their source-Hessian, joint-profile and bounded-surface subtraction contracts
are retained; this draft does not take ownership of those larger tasks.

Canonical input: PHOTON-CONDITIONAL-VARIANCE-FLOOR [T], including its
full-measure empty-set lemma and 21-face insertion. All other named notes
retain their source status. The existing neutral-joining proofs,
partial-current marginal bounds, #1202 STOP_EXECUTION record and restricted
reachability result were read. No sampler, diagnostic or scientific audit
was executed for this draft. No independent review is claimed.

## 2. Complete finite measure and equality

Let L>=4 be even, V=L^4, and use the labeled periodic cubical complex
(Z/LZ)^4. Canonical cells have increasing direction indices, with the usual
alternating upper-minus-lower boundary. There are 6V canonical plaquettes P
and 4V canonical positive edges E. Set

```
Omega_L = {n in {-1,0,1}^P : partial n = 0 modulo 5},
w(n) = 2^(-|supp n|),   Z_L = sum_(n in Omega_L) w(n),
mu_L(n) = w(n)/Z_L,    j(n) = partial n/5.
```

All exterior configurations, current sectors and torus sectors are summed.
The zero field makes Z_L positive. Equality of signed configurations is
literal coordinate equality on this labeled complex, with no quotient by
translation, gauge, support, sign reversal or cycle decomposition.

Write S=supp n and epsilon(e,p) for incidence. Six faces meet each edge.
Because partial n is divisible by five, the only local possibilities are:

* degree d_e=0,2,4,6, balanced positive and negative incidences, j_e=0;
* degree d_e=5, all five incidences aligned, j_e=+1 or -1.

In particular j_e is unit-capacity. Degrees one and three are impossible.

The augmentation is conditional on the **entire** n. At every neutral edge
of degree 2r, choose uniformly one bijection between its r positive and r
negative incidences, independently across edges conditional on n. There are
r! choices, including one at degree zero. Link the corresponding face pairs.
At every degree-five edge join all five occupied incident faces into a single
block. The connected components of these links on S are K. Degree-four and
degree-six neutral links must not be replaced by a single fixed pairing.

Equivalently forget the component signs and retain the unsigned structure
(S,M), with M the actual set of neutral pairs at each labeled edge. For each
matched pair p,q the sign relation is
eta(q)=-epsilon(e,p)epsilon(e,q)eta(p); at a degree-five block it is
eta(q)=epsilon(e,p)epsilon(e,q)eta(p). A structure is consistent exactly when
these relations have product +1 around every graph cycle. Its unnormalized
weight, with k connected components, is

```
W_L(S,M) = 1_consistent 2^(k-|S|)
           product_(e:d_e even) 1/(d_e/2)!.
```

Sum this over all allowed supports and pairings, including neutral-only and
winding structures. The sum is exactly Z_L: each n has product_e r_e!
compatible matchings, whose reciprocal factors cancel, and every consistent
(S,M) has exactly 2^k signings. Thus P_aug(S,M)=W_L(S,M)/Z_L. Equality here
is literal equality of the labeled S and all local pairs M. Reference signs
eta_K are a computational choice; their simultaneous reversal on one K
does not change M_K or any tail event below.

Every neutral pair cancels inside its K, and every charged block lies in
one K. Hence J_K=partial eta_K/5 is an integer conserved unit current.
Its homology is zero because 5[J_K]=0 in the torsion-free group
H_1(T^4,Z)=Z^4. Conditional component signs are independent uniform signs,
so Cov_mu(j)=E_aug sum_K J_K tensor J_K. This sign statement holds for
paired **face components**, not independently for connected pieces of
the current support.

For charged e, K(e) is the unique paired face component owning its five-face
block, and M_K counts all nonzero current edges of J_K, including distant
ones joined through neutral faces. Put the rooted variable to zero when
e is uncharged. Neutral components remain in the measure. Nonunique cycle
decompositions and mutually compensating winding cycles remain admitted.

## 3. Exact target, finite cutoff, and tail constants

For the fixed axis pair 01, let

```
B_K(r) = sum_(x:x_1=r) J_K(e_0(x)),
H_K(r)-H_K(r-1) = B_K(r),
ell_K = min_(h in Z) sum_(r in Z/LZ) |H_K(r)-h|,
Xi_L = V^-1 E_aug sum_K ell_K^2.
```

The zero homology ensures sum B_K=0, so a cyclic integer primitive exists.
The inherited NON-CANONICAL reduction gives, for every allowed nonzero
t=2pi k/L,

```
chi_L(t) <= Xi_L <= R3(L)/16,
R3(L) = (4V)^-1 sum_(e in E) E_aug[1_(e charged) M_K(e)^3].
```

The factor 1/16 follows from ell_K<=M_K^2/8 and the exact rooting identity
sum_e 1_(e charged)M_K(e)^3=sum_K M_K^4. The stronger nonwinding constant
cannot replace 1/8 for all components: a chosen cycle decomposition may
wind, even though its total homology vanishes. No rotational equality is
needed for the root average.

Let N=4V and define T_(L,e)(r)=P_aug(e charged,M_K(e)>=r). Then T(r)=0 for
r>N, and, with d_r=3r^2-3r+1,

```
R3(L) = (4V)^-1 sum_e sum_(r=1)^N d_r T_(L,e)(r).
```

This is exact finite telescoping of M^3. Translation invariance optionally
replaces (4V)^-1 sum_e by one quarter of the four orientation-root sums.

If one proves T_(L,e)(r)<=A q^(r-1), uniformly in all L,e,r with
0<q<1, then

```
R3(L) <= A F_N(q) <= A (1+4q+q^2)/(1-q)^3,
F_N(q) = sum_(r=1)^N d_r q^(r-1).
```

The exact discarded finite-size remainder is

```
F_infinity(q)-F_N(q)
 = q^N [(3N^2+3N+1)/(1-q)
        +(6N+3)q/(1-q)^2 + 3q(1+q)/(1-q)^3].
```

This follows by writing r=N+1+j and summing 1,j,j^2. For the convention
T(r)<=A exp(-a r), use q=exp(-a) and multiply these constants by q.

Alternatively, if T_(L,e)(r)<=C0 r^(-3-epsilon) uniformly with epsilon>0,
the exact finite majorant is

```
C0 [3 H_N(1+epsilon)-3 H_N(2+epsilon)+H_N(3+epsilon)],
H_N(s) = sum_(r=1)^N r^(-s).
```

The infinite constant is
C0[3 zeta(1+epsilon)-3 zeta(2+epsilon)+zeta(3+epsilon)], at most
C0(1+3/epsilon). The omitted positive tail is at most
3C0 N^(-epsilon)/epsilon, by integral comparison. Neither a tail exponent
nor any constants A,q,C0,epsilon for this full measure have been proved here.

## 4. One precise missing conditional inequality

The even torus is bipartite. A conserved nonzero unit current decomposes
into edge-disjoint directed simple cycles; each has even length at least
four. Thus every charged component has M_K in {4,6,...,N}.

A sufficient prospective theorem is the following **unproved** block-tail
contraction, for one explicit theta<1, uniformly in all L,e,k>=0 for which
the denominator event has positive probability:

```
P_aug(M_K(e)>=6+2k | e charged, M_K(e)>=4+2k) <= theta.   (H)
```

These are ordinary full-measure tail events, with every exterior and matching
summed. They are not conditioning on fixed exterior faces or on an arbitrary
exploration history. If the denominator is zero, subsequent tails are zero
and the corresponding undivided inequality is automatic.

For complete precision define the unnormalized restricted partition sum

```
Z_(L,e,r) = sum_(S,M) W_L(S,M) 1_(d_e=5, M_K(e)>=r).
```

Then (H) is exactly Z_(L,e,6+2k)<=theta Z_(L,e,4+2k). This is a concrete
remaining partition-sum comparison, not a proved property or an independent
loop-gas assumption. Writing p_(L,e)=P_mu(j_e!=0), (H) implies
T_(L,e)(4+2k)<=p_(L,e)theta^k. If p_(L,e)<=p_* uniformly, with p_*=1 always
admissible, exact even-size telescoping gives

```
R3(L) <= p_* [64 + sum_(k=1)^(2V-2)
                        (24k^2+72k+56) theta^k]
       <= p_* (64-40theta+32theta^2-8theta^3)/(1-theta)^3.
```

The finite expression retains the exact upper endpoint. For K=2V-2 the
infinite-minus-finite remainder is

```
theta^(K+1) [a_(K+1)/(1-theta)
             +(48(K+1)+72)theta/(1-theta)^2
             +24theta(1+theta)/(1-theta)^3],
a_k = 24k^2+72k+56.
```

This stronger sufficient route is not necessary for a finite third moment.
Failure to establish (H), or a counterexample to a particular theta, would
not prove R3 unbounded. The direct summable-tail target remains admissible.

The available partial-current inequalities concern specified local patterns
with all other currents summed, or conditioning on a disjoint **zero**
current set. They provide no such ratio after conditioning on a nonzero
rooted component. Arbitrarily long current loops need not contain a fully
charged elementary plaquette. Neutral tubes also join two separated small
current loops into one K while its current size stays eight. Therefore
neither selected elementary-loop probabilities, neutral-area entropy nor
component-diameter tails can be substituted for (H). Qualitative finite-state
reachability supplies no mixing rate or ensemble tail estimate. These are
identified gaps in those approaches, not a universal obstruction theorem.

## 5. A full-measure lower bound and the exact certificate deficit

Here is a self-contained derivation of a lower bound for the same R3,
using the canonical insertion argument. It uses no isolated-component
restriction, no empty halo and no approximate sampling.

First global reversal n -> -n is a weight-preserving bijection of Omega_L;
j_e changes sign. Hence E_mu j_e=0. Since each j_e is in {-1,0,1},

```
Var_mu(j_e) = E_mu j_e^2 = P_mu(j_e!=0) = p_(L,e).
```

For any face set B, the character expansion with independent uniform
A_e in Z5 gives

```
Z_L = E_A product_p [1+cos(2pi (dA)_p/5)],
Z_emptyB = E_A product_(p not in B) [1+cos(2pi (dA)_p/5)].
```

Every factor lies in [0,2]. Thus Z_L<=2^|B| Z_emptyB and
P_mu(n|B=0)>=2^(-|B|). This is unconditional and keeps the full exterior.

Use the 21-face defect

```
U(z) = -c_012(z)+c_012(z-e_2)-c_013(z)+c_013(z-e_3),
a(z) = partial U(z)-5 p_01(z),
partial a(z) = -5 partial p_01(z).
```

The four cubes give +4 on their common central face and twenty distinct
other faces of coefficient +/-1. Subtracting 5 at the center leaves a
ternary 21-face field. These faces are distinct for every admitted L>=4.
Choose a coordinate permutation and translation so the specified root e
lies on the central plaquette boundary. Then j_e(a)=+1 or -1. Put S=supp a,
so |S|=21 and partial a=0 modulo 5.

Condition on every face outside S. If the zero S-filling is allowed, both
+a and -a fillings are allowed, since adding either changes each edge
boundary by a multiple of five. Their conditional probabilities satisfy

```
p_+ = p_- = 2^-21 p_0.
```

This is exact: exterior weights cancel and each nonzero filling occupies
exactly 21 faces. The observable j_e is linear on all faces. Its values on
these three fillings are c,c+A,c-A, where c is the exterior contribution
and A=j_e(a) has |A|=1. For z=E[j_e | exterior]-c, their contribution to
the conditional variance is

```
p_0 |z|^2 + 2^-21 p_0 (|A-z|^2+|-A-z|^2)
 = (1+2^-20)p_0 |z|^2 + 2^-20 p_0 |A|^2
 >= 2^-20 p_0.
```

All omitted variance terms are nonnegative. If zero filling is not allowed,
p_0=0 and this inequality is trivial. By total variance and the exact
identity E_exterior p_0=P_mu(n|S=0),

```
p_(L,e) = Var_mu(j_e)
 >= E_exterior Var(j_e | exterior)
 >= 2^-20 P_mu(n|S=0)
 >= 2^-20 2^-21 = 2^-41.                               (1)
```

The augmentation preserves the n marginal, so (1) is also its charged-root
probability. No independence of distinct roots has been used.

For completeness, the minimum-four statement used in Section 4 requires
no probabilistic assumption. Orient each nonzero edge of J_K according to
its sign. Conservation makes indegree equal outdegree. Following unused
edges and splitting closed trails produces directed simple cycles, and
removing a cycle preserves balance. The underlying graph has no self-loop
or parallel-edge two-cycle for L>=4; a unit current cannot use one edge in
both directions. Its bipartite parity is sum_i x_i modulo two, well-defined
because L is even. Each nonempty directed cycle therefore has length at
least four. Hence M_K>=4 whenever K is charged, with every neutral join and
winding sector still included.

Pointwise 1_(e charged)M_K(e)^3>=64 1_(e charged). Averaging over all roots
and using (1) gives the proposed exact finite-volume consequence

```
R3(L) >= 64*2^-41 = 2^-35,       every even L>=4.         (2)
```

Now suppose a future proof obtains R3(L)<=C uniformly on this same family.
It must have C>=2^-35. The particular inherited majorant supplies the
certificate chi_upper=C/16, and therefore

```
chi_upper >= 2^-39 = 144 rho,
rho = 1/(36*2^41).
```

PHOTON-CONDITIONAL-VARIANCE-FLOOR certifies b_lower=25rho and, independently,
chi>=rho on every defined ordered profile. Pairing exactly this b_lower
with exactly the whole-moment upper certificate yields

```
margin_certificate = 25rho - 25C/16
                   = -D(C),
D(C) = 25(C/16-rho) >= 25(144-1)rho = 3575rho > 0.       (3)
```

Thus this certificate combination cannot establish a strict positive
margin, even if the uniform R3 theorem is later obtained. A different
transverse lower certificate paired with C/16 would have to exceed
25C/16, requiring an improvement over 25rho strictly greater than D(C).
At its theoretical smallest C, that improvement exceeds 3575rho.

Equation (3) is not a lower bound on the actual chi, nor an upper bound on
the actual b-25chi: C/16 can be a loose upper bound, and b can exceed its
local floor. It does not falsify a bounded R3, a positive true contrast, P1,
a massless phase, or a different direct signed-covariance estimate.

The finite Canon floor is c_L=2^-41 floor(L/3)^2/(4L^2). Its boundary terms
remain rho-2^-41/(6L)<=c_L<=rho and
S_n,02,02^L(t e_1)>=25rho-25*2^-41/(6L)-10rho t^2. An upper R3 constant
would control all nonzero allowed momenta. Passing to a specified nonempty
joint profile family still means thermodynamic limit first at fixed
nonzero limiting t, then infrared limit. No profile existence, local-to-
Fourier identification, interchange, or lowest-momentum substitution is
provided here.

## 6. Narrow prospective preregistration and disposition

The full tail theorem remains pending. The substantive written consequence
available for separate review is only (1)-(3) and the conditional tail
summation formulas, on the complete measure of Section 2.

Before any new computation, the owner must reserve the scoped successor,
freeze an immutable public input list and preregistration, and state whether
the candidate is this certificate limitation or an actual upper-tail theorem.
For the latter, freeze either explicit A,q or C0,epsilon, or one explicit
theta in (H); the complete pairing law, all even L>=4 and root orientations;
the exact unnormalized partition comparison; every exterior conditioning;
and the success/failure rule. A finitely audited list of volumes cannot earn
the all-volume tail theorem. A failure at one proposed theta is a failure of
that proposed contraction, not of every possible tail estimate.

For the written consequence (1)-(3), a fresh reviewer should reconstruct
the insertion, conditional probability ratios, current minimum size and
arithmetic from these allowed source statements before consulting any future
builder audit code. An admitted counterexample to one of those statements
rejects that statement. Absence of a counterexample is not a tail proof.
Any optional finite audit must first freeze its finite domains and exact
verifier under the repository procedure; this draft authorizes none.

No source files, Canon, registry, gates, policies, releases or larger-owner
scope are changed. The dependent whole-current reduction stays
NON-CANONICAL. PHOTON-CONDITIONAL-VARIANCE-FLOOR stays T;
PHOTON-MASSLESS-PHASE and PHOTON-CONE-CONVERGENCE stay O; P1 and the
uniform R3 upper bound remain unresolved. This file is not PREREG.md,
RESULT.md, PROMO, an independent review, or a formal execution record.
