# PREREG. P-FRW-INHOM-K1-BACKREACTION-2

**Formal public probe. Frozen before first scientific execution.**

```text
ISSUE:           #921
AUTHORITY:       Public Canon v82, mathorn1973/twist-j main
BASE MAIN:       76e2e14a41d309da969d9ef330e973a3964a3841
TAG:             canon-v82
CONTENT_COMMIT:  4e65adf0b483311d2a031cf2a23a65f2caf5af8a
CANON_SHA256:    5dcbf2abac151af1e6019ea4c009c7631cb773824a850bc5f5ff61bb324f9146
CANON_BYTES:     580724
OWNER:           FRW-INHOM [O]
CONNECTED:       TT-SOURCE [O], TT-VECTOR-STATE-NORMALIZATION [O]
SOURCE NOTE:     notes/canon/C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N.md
SOURCE COMMIT:   890333f1dc1cd2fbceff41528259f4259b3e4dc2
PREDECESSOR:     P-FRW-INHOM-K1-BACKREACTION-1, ABANDONED, PR #920
BRANCH:          probe/P-FRW-INHOM-K1-BACKREACTION-2
PATH:            probes/P-FRW-INHOM-K1-BACKREACTION-2/
```

No scientific result existed when this preregistration and `verify.py` were
accepted. Before the public pin the accepted verifier was only parsed
statically and passed `python -m py_compile`. It was not scientifically
executed.

## 0. Predecessor and the only allowed repair

`P-FRW-INHOM-K1-BACKREACTION-1` was publicly pinned but never scientifically
executed. It was closed `ABANDONED` because its verifier represented an exact
scientific `FAIL-CONSTRUCT` by raising `AssertionError` and exiting nonzero.
Repository policy classifies such an invocation as an incomplete execution,
not as a completed scientific negative result.

This successor preserves every scientific equation, carrier, coefficient,
time placement, threshold, equality, source definition, and gate G1 through
G12 from the predecessor. The only change is verdict transport:

```text
scientific PASS-CONSTRUCT -> exact stdout, exit 0
scientific FAIL-CONSTRUCT -> exact stdout, exit 0
unexpected verifier/infrastructure fault -> nonzero exit
```

The successor may not use the change in verdict protocol to repair a failed
scientific gate.

## 1. Layer and scope

```text
COMPUTATION LAYER: L1 exact finite rational arrays and exact polynomial identities.
PHYSICAL READING:  the L2/FRW interpretation is the object under test, not an
                   earned computation-layer promotion.
CROSS-LAYER CLAIM: none is earned by the verifier itself. A later D dictionary
                   disposition, if any, is a separate reviewed Canon fold.
```

The probe tests exactly one selected positive class frozen in the merged
predefinition. It does not classify every discrete gravity theory and cannot
earn the universal negative side of `FRW-INHOM`.

## 2. Frozen carrier, incidence and planar restriction

```text
X = (Z/5)^3,                              |X| = 125,
E = {(x,a,k): x in X, a in {1,2,3}, k in {1,2}}, |E| = 750,
tail(x,a,k)=x,
head(x,a,k)=x+k e_a,
(B f)(e)=f(head(e))-f(tail(e)),
w_1=29/324,
w_2=65/324,
(Wu)(x,a,k)=w_k u(x,a,k),
L3=B^T W B.
```

Normalized products and planar embedding:

```text
<f,g>_V=(1/25) sum_X f g,
<u,v>_E=(1/25) sum_E u v,
(iota f)(x1,x2,x3)=f(x3).
```

Required exact identities:

```text
<iota f,iota g>_V=sum_(r in Z/5) f(r)g(r),
L3 iota=iota L_public,
L_public=[188I-29(S+S^-1)-65(S^2+S^-2)]/324.
```

No square root of `L3`, same-carrier Leibniz derivative, alternative product,
or alternative spatial normalization is admitted.

## 3. Frozen K1 input

Use Public Canon v82 literally:

```text
W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101},
nu(0110)=nu(1001)=1/6,
nu(w)=1/12 for every other word,
u_t=w_(t+2)-w_t,
h_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/2, t=0,1,
h_(n+1)=(2I-L_public)h_n-h_(n-1).
```

The 3D field is `iota h_n`. The selected TT representative is
`H=diag(h,-h,0)`. Cross polarization is zero in this selected class. No K1
word, weight, amplitude, local order, counter, or marked spatial point may be
changed after the pin.

## 4. Frozen quadratic action and TT Noether pair

Put

```text
d_n=h_(n+1)-h_n,
g_n=B h_n,
q_n=h_(n+1)-h_(n-1),
R_n=h_(n+1)-2h_n+h_(n-1)+L3 h_n.
```

Before the common public factor `1/(2 lambda)`, `lambda=216 pi`, freeze

```text
A2_TT=(1/2) sum_n [<d_n,d_n>_V-<h_n,L3 h_n>_V].
```

The half-slice vertex energy and integer-slice edge current are

```text
e_(n+1/2)(x)
 = (1/2)d_n(x)^2
   +(1/4) sum_(e incident to x) w_e g_(n+1)(e)g_n(e),

j_n(e)
 = (1/4)w_e g_n(e)
   [q_n(tail(e))+q_n(head(e))].
```

The exact off-shell target identity is

```text
e_(n+1/2)-e_(n-1/2)+B^T j_n=(1/2)q_n R_n.
```

No alternative same-slice energy, later average, Cesaro replacement, Gaussian
closure, stochastic source, or manually inserted stress is admitted.

## 5. Frozen time placement, lapse split and edge Hodge split

```text
h_n                    vertex, integer n
e_(n+1/2)              vertex, half n+1/2
j_n                    edge, integer n
tau_(n+1/2)            mean-zero vertex, half n+1/2
ell_perp_(n+1/2)       mean-zero local lapse, half n+1/2
ell_0_(n+1/2)          public homogeneous FRW lapse variation slot, half n+1/2
p_perp_n               edge in ker(B^T), integer n
P_n                    edge momentum, integer n
N_n                    edge shift multiplier, integer n
xi_n                   mean-zero local gauge parameter, integer n
```

The link-lapse placement is a selected physical-reading choice and is not
identified with the integer-slice auxiliary lapse placement of the v82
comparison action. No coefficient may compensate for this choice.

```text
ell_total=ell_0*1+ell_perp,
P_n=WB[tau_(n+1/2)-tau_(n-1/2)]+p_perp_n,
p_perp_n in ker(B^T).
```

Let `Pi_0` subtract the spatial mean, `V0=<1,1>_V=5`, and
`bar_e=<1,e>_V/V0`. Freeze

```text
A2_constraint=sum_n [
  2<ell_perp,L3 tau>_V + 2<N,P>_E
],

A3_source=sum_n [
  -V0 ell_0 bar_e - <ell_perp,e>_V + <N,j>_E
].
```

The two lapse terms are exactly `-<ell_total,e>_V`.

For any later physical dictionary fold only:

```text
rho_TT=e/(2 lambda),
J_TT=j/(2 lambda).
```

## 6. Frozen local gauge family and coefficient solve

```text
delta_0 ell_perp_(n+1/2)=xi_(n+1)-xi_n,
delta_0 N_n=B xi_n,
delta_0 tau=0,
delta_0 p_perp=0,
delta_0 h=0,
delta_1 h_n=(1/2)xi_n q_n.
```

`ell_0` is inert under this mean-zero local gauge family.

The general coefficient control is

```text
-alpha<ell_perp,e>+beta<N,j>,
delta_1 h=gamma xi q.
```

The exact target solve is

```text
alpha=beta,
gamma=alpha/2,
alpha=1 by the frozen public source convention,
therefore (alpha,beta,gamma)=(1,1,1/2).
```

## 7. Frozen constraints and homogeneous split

```text
L3 tau_(n+1/2)=(1/2)Pi_0 e_(n+1/2),
2P_n+j_n=0.
```

On `R_n=0` the momentum completion is

```text
p_perp_n=-j_n/2-WB[tau_(n+1/2)-tau_(n-1/2)],
B^T p_perp_n=0.
```

The exact complementary homogeneous source is

```text
bar_rho_TT=bar_e/(2 lambda),
3H^2=lambda[rho_matter+bar_rho_TT]
    =lambda rho_matter+bar_e/2.
```

At `h=0`, `e=j=0` and the required homogeneous restriction is exactly the
public `FRW-CANONICAL-FORM` input:

```text
3H^2=lambda rho_matter,
lambda=216 pi,
H^2=72 pi rho_matter,
```

with its registered continuity, second Friedmann, Hamiltonian and fiber clauses
unchanged.

## 8. Gate blocks and exact thresholds

Every threshold is exact equality. No tolerance and no floating point occur in
the decision path.

```text
G1  L3=B^T W B; rank(L3)=124; kernel(constants); exact planar L_public and norm.
G2  all ten K1 inputs, weights and v82 recurrence unchanged.
G3  off-shell pointwise local balance identity holds as a polynomial identity.
G4  global localized energy equals the staggered invariant; K1 histories conserve it.
G5  cubic Noether cancellation delta_0 A3 + delta_1 A2 = 0.
G6  unique coefficient solve (alpha,beta,gamma)=(1,1,1/2).
G7  unique mean-zero tau solution exists for every admitted K1 source record.
G8  divergence Hodge split and full typed momentum completion hold exactly.
G9  total-lapse split is exact; no zero mode is lost; h=0 returns public FRW unchanged.
G10 no new free dimensionless coefficient occurs.
G11 Public Canon v82 bytes/hash and K1/predefinition inputs match their frozen source.
G12 deterministic verifier, repository policy, security and both architecture replays pass.
```

Outcome routing:

```text
PASS-CONSTRUCT
  G1 through G11 pass locally and G12 passes in the public PR workflow on both
  required architectures with byte-identical stdout.

FAIL-CONSTRUCT
  one or more exact scientific gates G1 through G11 fail. The verifier prints
  every failed gate and exits zero so the negative is a completed scientific
  result. This rejects only the selected class.

STOP
  authority drift, source hash mismatch, changed threshold, changed K1 input,
  changed coefficient, changed link-lapse placement, changed equality, missing
  evidence, or an unnamed layer lift. Unexpected verifier/infrastructure faults
  are nonzero and are not scientific outcomes.
```

## 9. Verifier

`verify.py` is Python 3 standard library only. Scientific arithmetic uses
integers and `fractions.Fraction`; no random input, floating-point literal,
network access, subprocess, external data, tolerance, or environment-dependent
branch appears in the decision path. It reads only frozen repository source
guards.

Accepted verifier before pin:

```text
bytes:   16900
SHA-256: b8c418c76bb0a0e4dc909cb21204ef5003ca6815981c8a051d0de29e1461fd73
```

Relative to the abandoned predecessor verifier, the scientific calculations
are unchanged. `check()` records rather than raises a scientific failure, and
`main()` catches exact scientific `AssertionError` instances per gate and emits
`FAIL-CONSTRUCT` with exit zero. Other unexpected exceptions remain nonzero.

The first result-bearing execution is forbidden until this file and the
accepted verifier are committed and pushed on the named probe branch. The pin
commit and both public file hashes must be recorded before that execution.