# Ramified depth: analytical consequences, separated from the census

Status: local **candidate-T analytical draft**, NON-CANONICAL, L1. Public source pin `5e872c22a18043c8126945a982efad55472cea82`, Public Canon v97. This text was written after the frozen run. The coordinator supplied the norm-bound idea before that run, and it was disclosed in PREREG.md. The norm-211 and norm-881 witnesses were selected from the resulting exact census. The coordinator supplied the subsequent thirty-pair capacity construction; the ramified-algebra reviewer checked it by hand and accepted it in [CAPACITY-REVIEW.md](CAPACITY-REVIEW.md). Neither author independence nor blinded discovery is claimed. The proofs below are direct algebra and inequalities; they do not require trusting the newly enumerated counts.

## 1. Domain, ideal, and inherited facts

Let `O=Z[zeta]` for a primitive fifth root, `lambda=1-zeta`, `J=1+zeta^2`, and `phi=-zeta^2-zeta^3`. For nonzero `alpha` write

`alpha*bar(alpha)=u+v*phi`, `A=|sigma1(alpha)|^2=u+v*phi`, `B=|sigma2(alpha)|^2=u+v-v*phi`.

Then `N(alpha)=AB=u^2+uv-v^2` is a positive integer. The registered two-trace inverse supplies `S0=2u+v`, `S1=3u-v` and their integer inverse. Thus equal ordered trace pairs imply equal ordered `(A,B)`. The original oriented strip is `B941={alpha:0<=v<u,1<=N(alpha)<=941}`. Its registered cardinality is 3150; the original public range proof places it in `[-8,8]^4`.

Define for each positive integer k

`D_k(alpha)=(S(alpha),S(J alpha),alpha mod lambda^k O)`.

The final component is an ideal class. Canonical ramification gives `N(lambda)=5` and `(5)=(lambda)^4`; the equality is between ideals. In particular this definition coincides in equivalence relation with the original mod-5 reader at k=4 and the mod-25 reader at k=8.

Inherited sources are `probes/P-J-TWO-TRACE-RESIDUE-DECODER-1/PROOF.md` sections 1-5 and 7, registered as J-TWO-TRACE-RESIDUE-INVERSE [T] and J-OBSERVED-SCALAR-CODE-CAPACITY [T], together with C20-TEICHMULLER-SPLIT [T]. The inherited cardinality 3150 appears explicitly in `canon/CANON.md` line 11897, under J-OBSERVED-SCALAR-CODE-CAPACITY beginning at line 11866; ramification is stated from line 393. Exact public byte hashes are recorded in SOURCE.json. The norm argument below is the original modulus argument applied to the actual ramified ideal; it is not presented as a newly discovered general separation method. The notation D_5 here means depth lambda^5, whereas D_5 in the original probe denotes the rational modulus 5.

## 2. Uniform injectivity criterion for the ramified depth

**Proposition.** For every integer `X>=1` and every integer `k>=1` such that `5^k>16X`, D_k is injective on the complete domain `{alpha in O:1<=N(alpha)<=X}`. This domain need not be restricted to an oriented strip.

**Proof.** Suppose two domain elements have equal readings and put `delta=beta-alpha`. The trace inverse gives identical positive A and B for alpha and beta. The triangle inequality at the two complex embeddings gives

`|sigma1(delta)|<=2sqrt(A)`, `|sigma2(delta)|<=2sqrt(B)`.

Therefore `N(delta)=|sigma1(delta)|^2 |sigma2(delta)|^2 <=16AB=16N(alpha)<=16X`. If delta is nonzero, equal ideal residues imply `delta=lambda^k eta` with a nonzero algebraic integer eta. Multiplicativity and positivity of its integer norm give `N(delta)=5^k N(eta)>=5^k`, contradicting the strict hypothesis. Hence delta=0. This covers every pair of domain elements. QED.

For `X=941`, `16X=15056<15625=5^6`. Therefore **every k>=6 is injective** on the full bounded-norm domain, and hence on B941. The unbounded two-trace entries remain part of the observation; this is not a finite-state storage theorem.

## 3. Direct depth-five collision and exact minimal injectivity

Use the coefficient basis `(1,zeta,zeta^2,zeta^3)` and take

`alpha=(-3,-5,-3,-3)`, `beta=(2,5,2,2)`.

Substitution into the public quadratic formulas gives `(u,v)=(13,6)` for both. Thus `N=13^2+13*6-6^2=211`, both lie in B941, and the common traces are `(32,33)`. The nonzero difference is `delta=(5,10,5,5)`.

For any vector x whose coefficient sum is divisible by 5, put `t=sum(x)/5`. Exact division by lambda is

`x/lambda=(x0-t,x0+x1-2t,x0+x1+x2-3t,t)`.

This follows by multiplying the right side by lambda, whose coefficient action is `(a,b,c,d) -> (a+d,b-a+d,c-b+d,2d-c)`. In particular the following chain is a direct certificate, with each arrow denoting division by lambda:

```text
(5,10,5,5)
 -> (0,5,5,5)
 -> (-3,-1,1,3)
 -> (-3,-4,-3,0)
 -> (-1,-3,-4,-2)
 -> (1,0,-2,-2).
```

Consequently `delta=lambda^5*(1,0,-2,-2)` lies in lambda^5 O. The last vector has coefficient sum -3, so it is not in lambda O: evaluation `zeta -> 1` modulo 5 identifies `O/lambda O` with F5. Thus the valuation is exactly 5. Its norm is 1, since its quadratic coordinates are `(5,8)` and `25+40-64=1`; consequently `N(delta)=3125` as well.

The distinct displayed scalars therefore collide for D_5 and, by ideal nesting, for every `1<=k<=5`. Combined with section 2, this proves **k=6 is the exact first injective depth** both on B941 and on the complete norm-at-most-941 domain. This conclusion uses a single exact witness and the general bound; it does not require the census's assertions that the witness has minimum norm or that K_5 is 2882.

## 4. Thirty disjoint collisions prove the 3125 threshold

Let `K_k=|D_k(B941)|`. In addition to the pair A in section 3, take the following pairs B and C:

| Pair | alpha | beta | Common (u,v) | Common N | Common (S0,S1) | delta=beta-alpha | delta/lambda^5 |
|---|---|---|---|---:|---|---|---|
| A | (-3,-5,-3,-3) | (2,5,2,2) | (13,6) | 211 | (32,33) | (5,10,5,5) | (1,0,-2,-2) |
| B | (-2,1,1,3) | (3,1,1,-2) | (13,7) | 211 | (33,32) | (5,0,0,-5) | (-1,-3,-3,-1) |
| C | (-6,-6,-5,-4) | (-1,-1,5,1) | (27,8) | 881 | (62,73) | (5,5,10,5) | (2,2,0,-1) |

All entries are exact integer identities: substitute the endpoint vectors into the quadratic u,v formulas; the three norms are `169+78-36=211`, `169+91-49=211`, and `729+216-64=881`. Hence all six endpoints belong to the unchanged strip. The cyclotomic relation gives

`lambda^4=5(-zeta+zeta^2-zeta^3)`,

`lambda^5=5(-1-2zeta+zeta^2-3zeta^3)`.

Writing `l=lambda^5/5`, direct ring multiplication of l by the three quotient vectors in the table gives, respectively, `(1,2,1,1)`, `(1,0,0,-1)`, and `(1,1,2,1)`. This proves every listed ideal membership. Each quotient has `(u,v)=(5,8)` and norm 1; therefore every difference has norm 3125. Thus all three rows are D_5 collisions. Pair B can also be obtained by applying `J^-1 sigma2` to pair A, but the displayed direct substitutions suffice and make that construction unnecessary as a proof premise.

Consider the ten explicitly given units `mu10={epsilon:epsilon=+/-zeta^j, 0<=j<5}`. Each has `epsilon*bar(epsilon)=1`, and therefore multiplication by epsilon preserves u,v, the strip and both traces. It also preserves congruence modulo lambda^5, since it is an integral unit. From a row `(alpha,beta)` obtain the ten colliding pairs `(epsilon*alpha,epsilon*beta)`.

For any nonzero alpha its ten multiples are distinct, since O is a domain. The two ten-point orbits in a row cannot meet. Indeed an intersection would give `beta=xi*alpha` with xi in mu10. Since alpha and beta are distinct, xi is not 1, and

`3125=N(beta-alpha)=N(alpha)*N(xi-1)`.

The second factor is a positive integer. This would require 211 (rows A and B) or 881 (row C) to divide 3125, which neither does. Thus each row gives ten disjoint unordered pairs on twenty distinct strip points. The three twenty-point families are mutually disjoint because their ordered u,v values `(13,6)`, `(13,7)`, `(27,8)` are different and preserved by mu10. There are **thirty pairwise disjoint colliding pairs**.

Identifying just those thirty pairs in the inherited 3150-element strip produces a quotient of size `3150-30=3120`. The map D_5 factors through this quotient, so

`K_5 <= 3120 < 3125`.

This argument does not assume that these are all collisions or that their keys are different from one another. Extra identifications only lower the image cardinality. Reduction modulo lambda^k for every `1<=k<=5` then gives `K_k<=K_5<3125`. Section 2 and the inherited strip cardinality give `K_6=3150`, and the same at all larger depths. It follows that **k=6 is the exact first depth with at least 3125 strip keys**, by an analytical proof that does not use the newly computed value `K_5=2882` or any exact lower-depth count.

For the inherited observed-reader capacity interpretation, J is a unit and multiplication by J or J^-1 preserves each ideal lambda^k O. Thus the original strip normalization and residue transport apply verbatim at each depth. Under the original reader class `R(n,x)=J^n G(label_n(x))`, nonzero integral generators of norm at most 941, every label available at every sheet `n>=3`, and no separately supplied sheet n, the same argument as public PROOF section 7 gives maximum usable labels `min(3125,K_k)`: select one strip representative per distinct key for attainment; for an upper bound, normalize two proposed generators sharing a key and choose accessible sheets that align their integer J offsets. These are the inherited exact hypotheses. Consequently the threshold just proved is also exactly six for that class. This establishes existence of a mathematical codebook, not its physical selection.

## 5. Relation to the frozen results and scope

The complete exact counts `(256,1170,1384,2603,2882,3150,3150,3150)`, witness minimality, fibre histograms and valuation frequencies in RESULT.md remain findings of the one-architecture frozen run, with candidate-C status. Sections 2-4 supply separate candidate-T proofs of the injectivity criterion, first injective depth six, the upper bound `K_5<=3120`, and first 3125-capacity depth six. The exact counts at depths 6 and above also follow from section 2 and the inherited cardinality, but the exact intermediate counts do not follow from the thirty-pair bound.

A single collision would not prove that fewer than 3125 keys remain among 3150 scalars; section 4 supplies the necessary stronger obstruction with thirty disjoint pairs. [CAPACITY-REVIEW.md](CAPACITY-REVIEW.md) records a separate mathematical review of this post-run argument. It is not a blind or second-architecture census. No assertion about the minimum over other observables, physical detector construction, acquisition resources, or a preferred codebook is made here.
