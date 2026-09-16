# PREREG. P-FRW-INHOM-K1-BACKREACTION-3

**Formal public probe. Frozen before first scientific execution.**

```text
ISSUE:           #923
AUTHORITY:       Public Canon v82, mathorn1973/twist-j main
BASE MAIN:       c596bfebd12bde3b15a3c3d378ca6b0f9c94608f
TAG:             canon-v82
CONTENT_COMMIT:  4e65adf0b483311d2a031cf2a23a65f2caf5af8a
CANON_SHA256:    5dcbf2abac151af1e6019ea4c009c7631cb773824a850bc5f5ff61bb324f9146
CANON_BYTES:     580724
OWNER:           FRW-INHOM [O]
CONNECTED:       TT-SOURCE [O], TT-VECTOR-STATE-NORMALIZATION [O]
SOURCE NOTE:     notes/canon/C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N.md
PREDECESSORS:    -1 ABANDONED PR #920; -2 ABANDONED PR #922
BRANCH:          probe/P-FRW-INHOM-K1-BACKREACTION-3
PATH:            probes/P-FRW-INHOM-K1-BACKREACTION-3/
```

Neither predecessor produced a scientific result. `-1` had an invalid
nonzero-exit transport for scientific FAIL. `-2` repaired that transport but
was abandoned before execution because its declared accepted SHA-256 did not
match the bytes pinned through the text contents transport.

This successor changes no scientific datum from `-2`. It reuses the exact
public verifier Git blob from `-2` without rewriting its bytes:

```text
accepted verifier Git blob: 34a26da1a7ae50622258ab26b081350de5297961
accepted verifier bytes:    16525
accepted verifier SHA-256:  12da283759b30ed9a1a388f4e022a0230e2362bd3ed2e420dacb31cc1d1c6596
```

The blob identity and SHA-256 were reconstructed from the exact public `-2`
bytes before this preregistration. The successor pin must contain this same
Git blob at its own `verify.py` path. Any other blob is STOP before execution.

## 1. Layer and selected class

```text
COMPUTATION LAYER: L1 exact finite rational arrays and polynomial identities.
PHYSICAL READING:  selected L2/FRW dictionary construction under test.
CROSS-LAYER CLAIM: none is earned by computation alone; any later D fold is separate.
```

The class is exactly the definition merged by #918. It is one positive
construction class, not an exhaustive class of all discrete gravities.

## 2. Frozen carrier and operator

```text
X=(Z/5)^3, |X|=125.
E={(x,a,k): x in X, a in {1,2,3}, k in {1,2}}, |E|=750.
(Bf)(x,a,k)=f(x+k e_a)-f(x).
w_1=29/324, w_2=65/324, L3=B^T W B.
<f,g>_V=(1/25)sum_X fg, <u,v>_E=(1/25)sum_E uv.
(iota f)(x1,x2,x3)=f(x3).
L3 iota=iota L_public.
L_public=[188I-29(S+S^-1)-65(S^2+S^-2)]/324.
```

No square root of `L3`, same-carrier Leibniz derivative, alternative product,
or alternative normalization is admitted.

## 3. Frozen K1 data

```text
W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101}.
nu(0110)=nu(1001)=1/6; every other word has weight 1/12.
u_t=w_(t+2)-w_t.
h_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/2, t=0,1.
h_(n+1)=(2I-L_public)h_n-h_(n-1).
H=diag(h,-h,0), cross component zero in this selected class.
```

No word, weight, amplitude, marked position, order, or recurrence may move.

## 4. Frozen TT action, source and off-shell identity

```text
d_n=h_(n+1)-h_n,
g_n=B h_n,
q_n=h_(n+1)-h_(n-1),
R_n=h_(n+1)-2h_n+h_(n-1)+L3 h_n,
A2_TT=(1/2)sum_n[<d_n,d_n>_V-<h_n,L3 h_n>_V].
```

```text
e_(n+1/2)(x)
 =(1/2)d_n(x)^2
 +(1/4)sum_(e incident to x) w_e g_(n+1)(e)g_n(e),

j_n(e)
 =(1/4)w_e g_n(e)[q_n(tail(e))+q_n(head(e))].
```

Exact target identity:

```text
e_(n+1/2)-e_(n-1/2)+B^T j_n=(1/2)q_n R_n.
```

No same-slice substitute, stochastic source, Gaussian closure, Cesaro
replacement, or manually inserted stress is admitted.

## 5. Frozen time placement and cubic constraint system

```text
h_n                  vertex, integer n
e_(n+1/2)            vertex, half n+1/2
j_n                  edge, integer n
tau_(n+1/2)          mean-zero vertex, half n+1/2
ell_perp_(n+1/2)     mean-zero lapse, half n+1/2
ell_0_(n+1/2)        homogeneous FRW lapse variation slot, half n+1/2
p_perp_n             edge in ker(B^T), integer n
P_n,N_n              edge, integer n
xi_n                 mean-zero gauge parameter, integer n
```

The link-lapse placement is a frozen new reading choice. No coefficient may
compensate for it.

```text
ell_total=ell_0*1+ell_perp,
P_n=WB[tau_(n+1/2)-tau_(n-1/2)]+p_perp_n,
p_perp_n in ker(B^T),
V0=<1,1>_V=5,
bar_e=<1,e>_V/V0.
```

Before the common public factor `1/(2 lambda)`, `lambda=216 pi`:

```text
A2_constraint=sum_n[2<ell_perp,L3 tau>_V+2<N,P>_E],
A3_source=sum_n[-V0 ell_0 bar_e-<ell_perp,e>_V+<N,j>_E].
```

The lapse pair is exactly `-<ell_total,e>_V`.

Local gauge family:

```text
delta_0 ell_perp_(n+1/2)=xi_(n+1)-xi_n,
delta_0 N_n=B xi_n,
delta_0 tau=delta_0 p_perp=delta_0 h=0,
delta_1 h_n=(1/2)xi_n q_n.
```

General coefficient control
`-alpha<ell_perp,e>+beta<N,j>`, `delta_1h=gamma xi q` has the frozen unique
solve

```text
alpha=beta, gamma=alpha/2, alpha=1,
(alpha,beta,gamma)=(1,1,1/2).
```

## 6. Frozen constraints and homogeneous complement

```text
L3 tau_(n+1/2)=(1/2)Pi_0 e_(n+1/2),
2P_n+j_n=0,
p_perp_n=-j_n/2-WB[tau_(n+1/2)-tau_(n-1/2)],
B^T p_perp_n=0.
```

```text
bar_rho_TT=bar_e/(2 lambda),
3H^2=lambda[rho_matter+bar_rho_TT]
    =lambda rho_matter+bar_e/2.
```

At `h=0`, `e=j=0` and the complete homogeneous restriction must be the public
FRW input unchanged:

```text
3H^2=lambda rho_matter,
lambda=216 pi,
H^2=72 pi rho_matter,
```

including its registered continuity, second Friedmann, Hamiltonian and fiber
clauses.

## 7. Frozen gates and thresholds

All thresholds are literal exact equality. Floating point is forbidden in the
scientific decision.

```text
G1  L3=B^T W B; rank 124; kernel constants; exact planar operator and norm.
G2  ten K1 inputs, weights and recurrence unchanged.
G3  pointwise off-shell balance identity exact as a polynomial identity.
G4  localized global energy equals the staggered invariant and is conserved.
G5  cubic Noether cancellation delta_0 A3+delta_1 A2=0.
G6  unique coefficient solve (1,1,1/2).
G7  unique mean-zero tau solution for every admitted K1 source record.
G8  exact Hodge split and full typed momentum completion.
G9  exact total-lapse split; no zero mode lost; h=0 returns FRW unchanged.
G10 no new free dimensionless coefficient.
G11 Public Canon v82 bytes/hash and frozen K1/predefinition inputs match.
G12 deterministic execution, policy/security, and byte-identical x86_64/aarch64 replay.
```

Outcome transport is frozen:

```text
PASS-CONSTRUCT: all G1-G11 scientific gates pass; completed exit 0.
FAIL-CONSTRUCT: one or more G1-G11 fail; failed gates printed; completed exit 0.
STOP: authority/hash/source/threshold/equality/layer mismatch before science.
Unexpected verifier/infrastructure fault: nonzero exit, not a scientific result.
```

## 8. Execution discipline

The accepted verifier is the public Git blob named at the top. Before first
scientific execution, the successor branch must pin this `PREREG.md` and that
exact blob, read both back publicly, and record the pin commit plus file
SHA-256 values. No result-bearing invocation is permitted before that record.

A completed local run produces exact `EXPECTED.txt`, `RUN.md`, and `RESULT.md`.
Only then may one probe PR open for the public two-architecture replay. A later
Canon fold, not the probe itself, decides whether the earned selected scope
literally satisfies the current positive clause of `FRW-INHOM [O]`.