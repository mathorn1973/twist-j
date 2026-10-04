# Analytical review: depth six is the first capacity for 3125 labels

NON-CANONICAL, L1. **Review outcome: ACCEPT; threshold claim candidate-T**
relative to the existing canonical strip cardinality 3150. This is a
post-run mathematical proof and review of exposed witnesses supplied by
the coordinator. It is not blind discovery, an independent census, or a
second-architecture execution. No scientific program was opened or run for
this review. The exact counts at the individual lower depths retain their
separate computation status.

## Reviewed scope and inherited input

Use exactly the domain in `PREREG.md`: O=Z[j], lambda=1-j,
J=1+j^2, phi=-j^2-j^3, with coefficient basis (1,j,j^2,j^3), and

    alpha bar(alpha)=u+v phi,
    u=a^2-ab+b^2-bc+c^2-cd+d^2,
    v=ab-ac-ad+bc-bd+cd,
    N=u^2+uv-v^2,  S0=2u+v,  S1=3u-v,
    B={alpha: 0<=v<u, 1<=N<=941}.

The registered J-OBSERVED-SCALAR-CODE-CAPACITY [T] supplies |B|=3150.
The current public source is main
`5e872c22a18043c8126945a982efad55472cea82`, Public Canon v97; the exact
source manifests are already recorded in `SOURCE.json`. In particular,
the inherited decoder proof has SHA-256
`491f568d1c03c20578af7858cccae40a97f0ff5b83af272e2ec49295a96a3fc0`.

Here D_k(alpha)=(S0,S1,alpha mod lambda^k O), and K_k=|D_k(B)|.
Thus D_5 here denotes depth lambda^5, not the older rational-modulus-5
notation. The reviewed targets are K_5<3125 and K_6=3150, hence minimum
depth six both for 3125 labels and for full injectivity. The proof below
does not claim a sharper exact value of K_5 or any smaller-depth count.

## Exact witness audit

The three proposed pairs are as follows. Substitution into the displayed
integer formulas gives the same u,v for both endpoints in each row.

| Pair | alpha | beta | (u,v) | N | (S0,S1) |
| --- | --- | --- | --- | --- | --- |
| A | (-3,-5,-3,-3) | (2,5,2,2) | (13,6) | 211 | (32,33) |
| B | (-2,1,1,3) | (3,1,1,-2) | (13,7) | 211 | (33,32) |
| C | (-6,-6,-5,-4) | (-1,-1,5,1) | (27,8) | 881 | (62,73) |

Indeed the norms are 169+78-36=211, 169+91-49=211, and
729+216-64=881. Each row has 0<v<u and norm at most 941, so all six
endpoints lie in the unchanged complete strip.

Reducing j^4=-1-j-j^2-j^3 gives

    lambda^4=5(-j+j^2-j^3),
    lambda^5=5(-1-2j+j^2-3j^3).

Direct ring multiplication then gives the following exact integral
quotients, not just residue coincidences:

| Pair | delta=beta-alpha | delta/lambda^5 |
| --- | --- | --- |
| A | (5,10,5,5) | (1,0,-2,-2) |
| B | (5,0,0,-5) | (-1,-3,-3,-1) |
| C | (5,5,10,5) | (2,2,0,-1) |

For an explicit multiplication check, write l=lambda^5/5. The three
products l times the final column are respectively (1,2,1,1),
(1,0,0,-1), and (1,1,2,1). Each quotient in that column has
(u,v)=(5,8), hence norm 25+40-64=1. Since N(lambda)=5, every displayed
nonzero delta has exact norm 5^5=3125 and exact lambda valuation five.
Every row therefore supplies a genuine D_5 collision, separated at depth
six.

The claimed construction of B from A is also exact. Under sigma_2:j->j^2,
the endpoints of A become (0,0,-2,3) and (0,0,3,-2). Using the public
J multiplication formula

    J(a,b,c,d)=(a-c+d,b-c,a,b-c+d),

these are respectively J times the two endpoints of B. Thus B is the
sigma_2 image followed by J^-1. The direct arithmetic above independently
checks its strip membership and collision; it does not rely only on this
construction. The unique prime (lambda) is Galois-stable and J is a unit,
so this construction also preserves the relevant ideal congruence.

## Thirty disjoint collisions

For any zeta in mu_10, zeta bar(zeta)=1. Multiplying both endpoints of a
row by zeta preserves u,v, hence the strip and both traces. It preserves
their congruence modulo lambda^5 because zeta is an integral unit.

For any nonzero alpha, the ten values zeta alpha are distinct. The alpha
and beta root-of-unity orbits in a given row cannot meet: such an
intersection would imply beta=zeta alpha for some zeta in mu_10. The
endpoints are distinct, so zeta!=1 and

    delta=alpha(zeta-1),
    N(delta)=N(alpha) N(zeta-1).

Here zeta-1 is a nonzero algebraic integer, so its norm is a positive
integer. This would force 211 or 881 to divide 3125, which is impossible
since 3125 is a power of five and both proposed divisors exceed one and
are coprime to five. Thus each row supplies ten disjoint unordered
colliding pairs, covering twenty distinct strip points.

The three twenty-point families are mutually disjoint, because their
values (u,v) are respectively (13,6), (13,7), and (27,8), and multiplication
by mu_10 preserves that ordered pair. There are consequently thirty
pairwise disjoint colliding pairs among the 3150 strip elements.

Identifying those thirty pairs already gives a quotient set of cardinality
3150-30=3120. The observation D_5 factors through that quotient, so

    K_5 <=3120<3125.

No assumption that these are the only collisions is used. Further merging
can only lower the capacity. Reduction from lambda^5 to lambda^k gives
K_k<=K_5 for every 1<=k<=5. Thus every such depth is insufficient for the
requested 3125 labels, regardless of the exact census counts.

## Depth-six injectivity

Suppose two nonzero integral elements alpha,beta of norm at most 941 have
equal D_6. Their two equal traces recover the same u,v, so they have equal
squared magnitudes A,B at the two complex places. For delta=alpha-beta,
the ordinary triangle inequality at each place gives

    N(delta)=|sigma_1(delta)|^2 |sigma_2(delta)|^2
            <= (4A)(4B)=16 N(alpha)<=16*941=15056.

If delta were nonzero, its membership in lambda^6 O would give
delta=lambda^6 gamma for a nonzero algebraic integer gamma, hence

    N(delta)=5^6 N(gamma)>=15625.

This contradicts 15056<15625. Therefore delta=0. This proves injectivity
on the entire norm-bounded integral domain, in particular on B, without
enumerating it. The inherited |B|=3150 now gives K_6=3150, and the same
holds at every larger depth.

## Disposition

The first partial ramified depth sufficient for 3125 labels is exactly
six, and it is also the first injective depth on the full strip. This
threshold has a complete analytical proof using finitely displayed,
independently checked witnesses and the previously canonical strip size.
The discovery of those witnesses followed the local census and is disclosed.
This review neither promotes the full lower-depth census nor reopens the
sealed rational-modulus decoder. No broader observation minimum, native
implementation, codebook selection, physical measurement or L2-L6 result
follows.
