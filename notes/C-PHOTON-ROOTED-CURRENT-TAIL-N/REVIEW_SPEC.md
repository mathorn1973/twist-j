# Fresh-review input: rooted-current certificate and conditional tails

**PUBLIC, NON-CANONICAL specification; no proof verdict.**
Candidate C-PHOTON-ROOTED-CURRENT-TAIL-N, issue
[#1324](https://github.com/mathorn1973/twist-j/issues/1324).

This document gives definitions, admitted source statements and advertised
targets. It intentionally contains no author's new lower-bound derivation.
The reviewer may know the target constants and is not result-blind. Do not
read CONTRACT.md, the author's detailed diff or future builder audit code
before freezing your own written derivation on the coordinator-assigned
review ref. Disclose any earlier exposure. No computational implementation
is required, and none is represented as independent here.

## 1. Pin and admitted inputs

The coordinator supplies the candidate commit containing PREREG.md and this
file. Scientific source base:
`44423153eee6259c7277eec5f5adbed9679f9146`, Public Canon v96. Read repository
authority and procedural rules, then these exact scientific inputs only:

| Path at the source base | Permitted scope | SHA-256 |
|---|---|---|
| `canon/CANON.md` | PHOTON-CONDITIONAL-VARIANCE-FLOOR | `eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2` |
| `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md` | Exact auxiliary measure, normalization and component-current definitions | `7ce7bdf7501e0e4b56de806a59b47ea53efc333cb141753c9d253576c211f0fe` |
| `notes/C-PHOTON-WHOLE-CURRENT-MOMENT-N/PROOF.md` | Inherited deterministic current-moment reduction | `82029583a8f27acfeec0461edf1c10d01613a2966aecc772a1264770b3a5054b` |

The first source is canonical T at its stated finite-model scope. The other
two remain NON-CANONICAL dependencies. No earlier simulation, finite
diagnostic, builder verification output or review verdict is an input.
PREREG.md fixes the claim and failure rules and is also allowed.

## 2. Complete carrier and equality

For every even integer L>=4 let V=L^4 and take the periodic cubical complex
(Z/LZ)^4. Canonical cells have increasing coordinate indices and the usual
alternating upper-minus-lower boundary. There are 6V plaquettes P and 4V
canonical positively oriented edges E. The full measure is

```
Omega_L={n in {-1,0,1}^P : partial n=0 modulo 5},
w(n)=2^(-|supp n|),  Z_L=sum_(n in Omega_L) w(n),
mu_L(n)=w(n)/Z_L,    j=partial n/5.
```

Every exterior, current and winding sector is included. Equality of signed
states is literal equality of all labeled coordinates. The zero field has
positive weight. Each edge meets six plaquettes with oriented incidence
epsilon(e,p). Neutral edges have degrees 0,2,4,6 with balanced incidence;
charged edges have degree five with all five incidences aligned.

Conditional on the entire signed n, independently at each neutral degree-2r
edge draw a uniformly chosen bijection between its r positive and r negative
occupied incidences, and link the resulting pairs of faces. There are r!
choices. Join all five faces at each charged edge. Components K are the
connected components of these face links, not components of supp j.

The equivalent unsigned structure is the labeled support S and all selected
neutral pairings M. Matching pairs obey the relative sign equation
eta(q)=-epsilon(e,p)epsilon(e,q)eta(p); degree-five junctions obey the same
equation with a plus sign. Consistency means that the relative signs agree
around every graph cycle. With k components its exact probability is

```
P_aug(S,M)=Z_L^-1 1_consistent 2^(k-|S|)
                       product_(e:d_e even) 1/(d_e/2)!.
```

Equality is literal equality of S and M, without quotienting by translations,
gauge transformations or choices of a cycle decomposition. Each consistent
component has two reference signings. Choose either eta_K; the source
augmentation defines its integer conserved unit current J_K=partial eta_K/5.
Its total integral homology vanishes. Conditional component signs are
independent uniform signs. These are statements of the admitted source law;
the reviewer should check their precise use and status rather than assuming
an independent law for individual current loops.

A charged edge has one owner K(e). Define M_K as the count of all nonzero
edges of J_K. For uncharged e, every rooted variable below is defined as
zero. Neutral components remain in the probability space, and neutral paths
may join distant charged currents. Winding cycles and nonunique cycle
decompositions are included.

## 3. Allowed variance and susceptibility inputs

The canonical source supplies, for any plaquette set B,

```
P_mu(n|B=0)>=2^(-|B|).
```

It also supplies the following linear-observable theorem. If ternary fields
a_i are supported exactly on nonempty face sets S_i of size m_i, satisfy
partial a_i=0 modulo five, and no edge is incident to two different sets
S_i, then every complex linear observable F(n)=sum_p n_p g_p obeys

```
Var_mu F >= sum_i 2^(1-2m_i) |F(a_i)|^2.
```

Variance is Hermitian. The source's explicit defect is

```
U(z)=-c_012(z)+c_012(z-e_2)-c_013(z)+c_013(z-e_3),
a_01(z)=partial U(z)-5p_01(z),
partial a_01(z)=-5 partial p_01(z).
```

It is ternary with 21 occupied faces, distinct for L>=4. Its coordinate
permutations and translations are available. The reviewer may use the
canonical geometric statement, or reconstruct it from the cell boundary.

For the fixed axis pair 01 the inherited current reduction uses

```
B_K(r)=sum_(x:x_1=r) J_K(e_0(x)),
H_K(r)-H_K(r-1)=B_K(r),
ell_K=min_(h in Z) sum_(r in Z/LZ)|H_K(r)-h|,
Xi_L=V^-1 E_aug sum_K ell_K^2,
R3(L)=(4V)^-1 sum_e E_aug[1_(e charged)M_K(e)^3].
```

At every allowed nonzero t=2pi k/L, with lambda(t)=4sin^2(t/2) and
chi_L(t)=S_j,00^L(t e_1)/lambda(t), the admitted NON-CANONICAL input is
chi_L(t)<=Xi_L<=R3(L)/16. It includes compensating winding cycles.
The canonical ordered-profile floor is b_lower=25rho with
rho=1/(36*2^41), and independently chi>=rho. These statements apply to each
defined thermodynamic-first, infrared-second joint profile, not an asserted
profile existence theorem. The finite floor and boundary terms are

```
c_L=2^-41 floor(L/3)^2/(4L^2),
rho-2^-41/(6L)<=c_L<=rho,
S_n,02,02^L(t e_1)>=25rho-25*2^-41/(6L)-10rho t^2.
```

## 4. Advertised new targets, without their derivation

For all admitted L and all e, the candidate claims

```
G1: P_mu(j_e!=0)>=2^-41.
G2: M_K in {4,6,...,4V} for every charged K; R3(L)>=2^-35.
```

If a future uniform theorem R3(L)<=C holds and one uses exactly the inherited
upper certificate C/16 and exactly the published transverse floor 25rho,
the candidate claims

```
G3: C>=2^-35; C/16>=144rho;
    25rho-25C/16=-D(C),  D(C)=25(C/16-rho)>=3575rho.
```

This rejects that certificate combination as a way to establish a positive
margin. It does not assert that the true b-25chi is nonpositive.

Set N=4V, d_r=3r^2-3r+1 and
T_(L,e)(r)=P_aug(e charged,M_K(e)>=r), with T(r)=0 for r>N.

```
G4: R3(L)=(4V)^-1 sum_e sum_(r=1)^N d_r T_(L,e)(r).
```

If T_(L,e)(r)<=Aq^(r-1) uniformly for A>=0 and 0<q<1, the advertised upper
constant is A F_N(q), with

```
F_N(q)=sum_(r=1)^N d_r q^(r-1),
F_infinity(q)=(1+4q+q^2)/(1-q)^3,
F_infinity-F_N=q^N[(3N^2+3N+1)/(1-q)
                  +(6N+3)q/(1-q)^2+3q(1+q)/(1-q)^3].
```

For an Aq^r convention multiply the bound by q.

G5: Under a uniform tail T_(L,e)(r)<=C0 r^(-3-epsilon), C0>=0,
epsilon>0, the advertised finite majorant is
C0[3H_N(1+epsilon)-3H_N(2+epsilon)+H_N(3+epsilon)], with
H_N(s)=sum_(r=1)^N r^(-s). Its infinite form uses zeta, is at most
C0(1+3/epsilon), and its positive remainder beyond N is at most
3C0 N^(-epsilon)/epsilon.

G6: The additional unproved premise (H) is

```
T_(L,e)(6+2k)<=theta T_(L,e)(4+2k),
one theta in [0,1), all L,e,k>=0.
```

It is a full normalized-measure tail comparison; zero denominator events
are handled by the undivided form. If p_(L,e)=P_mu(j_e!=0)<=p_* uniformly,
the advertised consequence is, with Kmax=2V-2,

```
R3(L)<=p_* G_Kmax(theta),
G_K(theta)=64+sum_(k=1)^K a_k theta^k,
a_k=24k^2+72k+56,
G_infinity(theta)=(64-40theta+32theta^2-8theta^3)/(1-theta)^3,
G_infinity-G_K=theta^(K+1)[a_(K+1)/(1-theta)
                         +(48(K+1)+72)theta/(1-theta)^2
                         +24theta(1+theta)/(1-theta)^3].
```

No antecedent in G4-G6 is claimed for the actual measure. No uniform upper
bound on R3 is claimed. Proving these implications cannot establish their
missing probability hypotheses.

## 5. Required independent disposition

Write your own derivation before comparison with CONTRACT.md. Check the
complete measure and normalization, the charged-root probability and its
conditioning domain, minimum current size including winding, all root and
volume factors, the certificate's logical direction, all three series
constants and finite remainders, and the order-of-limits boundary. Classify
any defect as an admitted counterexample, a proof gap, an equivalent
convention, or an outside-scope example.

Freeze the independent written artifact with its commit and hash before
opening the author's construction. Then compare, preserving both originals,
and report accept/reject/blocked at the exact target scope with exposure
disclosure. An exact counterexample must obey the hypothesis of the target
it refutes. Do not repair a failed frozen target by changing its constants
or carrier. Do not call finite agreement an all-volume theorem, two-architecture
replay an independent proof, or a failed sufficient contraction a universal
obstruction to bounded R3. No fresh scientific computation is requested.
