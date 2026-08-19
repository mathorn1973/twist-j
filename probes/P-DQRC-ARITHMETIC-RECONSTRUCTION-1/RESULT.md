# P-DQRC-ARITHMETIC-RECONSTRUCTION-1 result

Status: `SCIENTIFIC RESULT / LOCAL X86_64 PASS / ARCHITECTURE GATE PENDING / CANON UNCHANGED`

## Verdict

The fresh public pin read back exactly and the single authorized formal run
passed all 15 exact audit groups with exit code zero, empty stderr, and stdout
byte-identical to `EXPECTED.txt`. The written proofs in `PREREG.md` carry the
universal statements; the verifier audits exact coordinate formulas and
frozen boundary witnesses.

No Canon row changes in this probe-only branch. The maximum dispositions after
a successful two-architecture replay remain:

```text
DEF-DQRC-INTEGER-CENSUS                  definition candidate, L1
DQRC-INTEGER-CENSUS-ARITHMETIC           T candidate
DQRC-HORODECKI-REENCODING                T candidate
DQRC-H-COEFFICIENT-NONSELECTION          T candidate
DQRC-ORIGIN-NONSELECTION                 T candidate
DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY       T candidate
physical DQRC reading                    NO ROW / O-STOP only
```

## Exact arithmetic result

For every nonzero integral `2 x 2` matrix `X`, the written proof establishes

```text
4 Delta <= Q^2,
M_x(K)=floor(alpha_x K),
u_x(k) in {0,1},
N_xy^(epsilon,eta)(K;j)=K +/- M_x^[j](K),
each formal local sign count=2K,
S_K^[0]=2(M_0(K)+M_1(K))/K,
0 <= S_inf-S_K^[0] < 4/K.
```

Integer scaling by every nonzero `q` leaves the census unchanged. The balanced
margins are inserted solely by `t`; the relational parity `-1` is inserted
solely by `product sigma_xy=-1`. Neither is an emergent causal theorem.

## Exact target reconstruction

After externally supplying the normalized real pure-two-qubit state
`X/sqrt(Q)`,

```text
C=2|det X|/Q,
C^2=4 Delta/Q^2,
H=Q^2(1+C^2),
S_inf=2 sqrt(1+C^2)=B_max.
```

In Schmidt gauge `T=diag(C,-C,1)` and the explicitly frozen optimal directions
give

```text
(E_00,E_01,E_10,E_11)=(r_0,r_0,r_1,-r_1),
r_0=Q/sqrt(H),
r_1=4 Delta/(Q sqrt(H)).
```

Thus the DQRC asymptotic expression is exactly a re-encoding of the public
pure-state Horodecki optimum. This is a valid external comparison, not an
intrinsic derivation from `J`, `Omega`, `U`, QDD, or an event law.

## Two exact nonselection results

Under the full local `O(2) x O(2)` action, homogeneous quartic invariant
polynomials with rank-one normalization form

```text
H_beta=Q^2+beta Delta.
```

Every integer `beta>=0` retains comparator totality, binary increments, census
closure, exact margins, scaling, and parity. For `Delta>0`, its census limit
matches the pure-qubit maximum if and only if `beta=4`. The existing invariant
and combinatorial premises therefore do not select `4`; the target does.

Likewise a shifted integer origin

```text
M_x^[j](K)=M_x(K+j)-M_x(j)
```

retains the same structural identities and asymptotic limit. At the maximal
point `(Q,Delta,H)=(2,1,8)` and `K=1`, origin `0` gives `S=0` while origin `1`
gives `S=4`. The one-sided finite deficit is not origin invariant.

## Field boundary

On `4 Delta=Q^2`, the slope is `1/sqrt(2)`. It is not an element of
`Q(zeta_5)`. Adjoining only `sqrt(2)` gives the degree-eight field
`Q(zeta_5,sqrt(2))`, a proper subfield of `Q(zeta_40)`; adjoining the full
`zeta_8` gives degree sixteen and the full `Q(zeta_40)`. This does not obstruct
an integer substitution from having `1/sqrt(2)` as a limiting frequency.

Also `S_inf^2` is rational, so `S_inf` cannot have both nonzero rational and
`sqrt(5)` parts. Integral carriers can occupy a pure `sqrt(5)` field sector,
but no nonzero integral matrix has the exact value `S_inf=sqrt(5)`.

## Physical and empirical STOP

Deleting ontic randomness does not evade Bell factorization. With
`lambda=(k,r,t)`, the displayed `B` depends on the remote formal label `x`;
this is a deterministic contextual/relational table, not a local hidden-
variable model. The construction supplies no spacetime causal mechanism.

`P-DQRC-FINITE-DEFICIT-1` is not authorized. One formal `k` enumerates all
sixteen tuples `(x,y,r,t)`, while one laboratory trial realizes one setting
pair and outcome pair. Until an intrinsic origin, trial map, apparatus, state,
loss rule, and complete `BELL-CAUSAL-ACCOUNTING` contract are frozen, `K` is
not a physical trial count and the finite deficit is not an identifiable
prediction. The correct next attack is the L4-to-L5 trial/address bridge, not
a retrospective fit to Bell data.

The required two-architecture workflow is still pending. All dispositions
remain non-canonical.
