# P-QDD-INSTRUMENT-CLASS-COMPLETENESS-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific result is earned by this file.

Public claim lock: issue 515. Parent split lock: issue 514.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    a25e2c640295962a7983f16d940347b2b7c1525e
```

Target: O2b `QDD-INSTRUMENT-CLASS-COMPLETENESS` only. O2a and O1 are separate.

Layer: L4 apparatus/support with a finite internal classical phase register. No L5 realized-event stream and no L6 measure.

## Result exposure

RESULT-EXPOSED / proof-first. Before this pin the session identified the pointwise fibre argument and the possibility that internal apparatus phase yields a family `m -> T_m` rather than one fixed branch map. These observations are discovery context only. No accepted verifier under this probe id has been executed.

The public predecessor results are lineage, not imported code: `QDD-INSTRUMENT-NONSELECTION [T]`, PR #510, and O1 boundary PR #513.

## Frozen target-independent carrier

Let

```text
V = Q^4,
one=(1,1,1,1)^T,
G=I_4-(1/5)one one^T,
M_J=[[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]],
D_J=M_J-I_4,
u_x=D_J^x e_0, x in F_5.
```

For token `k`, before target comparison, let `P_k` be the `G`-orthogonal projector onto `Q u_k`, `Q_k=I-P_k`.

The accepted audit checks all five tokens. Target comparison with `E_low,E_high` occurs only at the final gate, at `k=2`.

## Frozen finite-memory apparatus class

Let `M={0,...,L-1}` be finite and nonempty. Let `tau_L,tau_H` be permutations of `M`. At phase `m`, let rational linear maps

```text
K_L,m, K_H,m : V -> V
```

be the two pure branch maps.

The class is defined operationally, not by membership in `A_rep`.

### A. Exact effect norms

For all phases and all `v in V`,

```text
<K_L,m v,K_L,m v>_G=<v,Pv>_G,
<K_H,m v,K_H,m v>_G=<v,Qv>_G.
```

### B. Ordinary exact repeatability after the phase update

For every phase and every `v`, the opposite branch on the next fresh invocation vanishes:

```text
K_H,tau_L(m) K_L,m v = 0,
K_L,tau_H(m) K_H,m v = 0.
```

No projective terminality, record sufficiency, naturality, commutator saturation, phase gauge, or Lueder law is assumed.

### C. Ready-state apparatus type

The ready input has the typed image

```text
v tensor |ready> tensor |m>
 -> K_L,m v tensor |LOW>  tensor |tau_L(m)>
  + K_H,m v tensor |HIGH> tensor |tau_H(m)>.
```

The theorem decides whether A and permutation typing make this a rational isometry and whether it extends to a rational orthogonal microscopic map.

## Written theorem 1: pointwise fibre completeness

From equality of quadratic forms and polarization,

```text
K_L,m^sharp K_L,m=P,
K_H,m^sharp K_H,m=Q.
```

Positive definiteness then kills the opposite input support:

```text
K_L,m Q=0,
K_H,m P=0.
```

For repeatability, use the next-phase effect identity. For example

```text
0=||K_L,tau_H(m) K_H,m v||_G^2
 =<K_H,m v, P K_H,m v>_G
 =||P K_H,m v||_G^2,
```

so `P K_H,m=0`; similarly `Q K_L,m=0`. Thus

```text
P K_L,m=K_L,m P=K_L,m,
Q K_H,m=K_H,m Q=K_H,m.
```

On its support each branch restriction is an injective isometry from a finite-dimensional positive-definite rational space to itself, hence an orthogonal automorphism. Therefore phase by phase

```text
K_L,m=O_L,m P,
K_H,m=O_H,m Q.
```

Internal finite phase creates no branch outside the old one-effect `A_rep` fibre under the frozen operational premises.

## Written theorem 2: converse finite-memory realization

Conversely choose any finite `M`, permutations `tau_L,tau_H`, and any phase-indexed maps in the two repeatable branch fibres. On the ready subspace, different phases remain orthogonal because each `tau_a` is injective and the LOW/HIGH pointer states are orthogonal. For a fixed phase the norm is

```text
<K_L v,K_L w>+<K_H v,K_H w>
=<v,(P+Q)w>=<v,w>.
```

So the ready map is a rational isometry. The already public rational reflection-extension theorem from `QDD-INSTRUMENT-NONSELECTION [T]` extends it to a rational orthogonal map on the full finite system-pointer-memory carrier. Two-sided support gives ordinary repeatability automatically.

This proves completeness only for the named finite-memory rational pure/repeatable class. No theorem about unbounded history, nonlinear, mixed, irrational or differently typed apparatuses is claimed.

## Written theorem 3: phase nonselection

For every token choose

```text
w_k=u_(k+1)-u_(k+2).
```

The regular-simplex Gram makes `w_k` nonzero and `G`-orthogonal to `u_k`. Let

```text
O_* = I - 2 w_k (w_k^T G)/(w_k^T G w_k)
```

be the rational `G`-reflection. It fixes the `P_k` line, preserves `Q_k V`, is orthogonal, and is not `+/-I` on the three-dimensional moving support.

For `M={0,1}`, `tau_L=tau_H=(0 1)`, freeze

```text
K_L,0=K_L,1=P,
K_H,0=Q,
K_H,1=O_* Q.
```

This apparatus satisfies the complete finite-memory class but its two HIGH maps are not equivalent under the registered single-branch sign equality. Hence the frozen operational premises do not force phase-independent post-state dynamics.

The audit also checks `L=256`, cyclic phase update, with all HIGH phases equal to `Q` except one phase equal to `O_*Q`. This is only a control aligned with the public O1 finite-memory boundary. It imports no O1 count or sampler theorem.

## Architecture boundary

Public Canon v59 does not supply a complete apparatus-memory class and does not identify local apparatus phase as gauge or require the post-state law to be phase independent. PR #513 shows local phase can be load-bearing for event realization but explicitly leaves O2 untouched.

Therefore a successful finite-memory theorem does not close O2b globally. It narrows the residual question to completeness beyond the frozen finite-memory class and the physical treatment of phase dependence.

## Formal machine audit

Accepted file:

```text
probes/P-QDD-INSTRUMENT-CLASS-COMPLETENESS-1/verify.py
```

Python standard library only; integers and `Fraction`; no float, randomness, network, subprocess, external data, predecessor import, or filesystem read/write. Zero arguments, deterministic stdout, empty stderr on PASS.

It audits:

- the J simplex, Gram and five target-independent projectors;
- the rational reflection witness at every token;
- branch effect and two-sided support equations for identity and reflected branches;
- exact two-phase repeatability and phase inequivalence;
- exact `L=256` cyclic-family controls;
- ready-subspace isometry identities at the branch level;
- final target comparison only after all previous gates.

Universal polarization, finite-memory class completeness and rational extension are carried by the written proofs above.

## Frozen decision

```text
FINITE-MEMORY-FIBRE-BOUNDARY
  pointwise fibre completeness and converse finite-memory realization hold;
  finite internal phase does not escape the A_rep branch fibres but does allow
  a genuinely phase-indexed post-state apparatus law; current architecture
  neither selects nor gauges that dependence; O2b remains open outside the
  named finite-memory class.

PHASE-COLLAPSE
  the complete frozen operational premises themselves force all phase-indexed
  branch maps into one registered sign class independent of phase.

FIBRE-F | DILATION-F | PHASE-WITNESS-F | TARGET-F | ARCHITECTURE-F | STOP
```

A mathematical or finite-control failure is a scientific route. Authority, collision, stale basis, pre-pin execution, post-pin mutation, target leakage, incomplete class definition, unnamed lift, runtime, security, or nondeterministic output is STOP.

Maximum later rows after the full public gate:

```text
QDD-FINITE-MEMORY-BRANCH-FIBRE-COMPLETENESS [T]
QDD-FINITE-MEMORY-APPARATUS-REALIZATION      [T]
QDD-POSTSTATE-PHASE-NONSELECTION             [T]
QDD-FINITE-MEMORY-O2B-BOUNDARY               [T]
```

## Firewall

O2a untouched. O1 untouched. No realized event stream, L6 measure, randomness, sampling, Bell, SI, decoder completion, phase gauge, target-controlled selector, or new free dimensionless input. No Canon, Registry, Frontier, gate, workflow, release or existing-probe edit.

## Formal order

Commit and push `PREREG.md` and `verify.py` together, read both back from the public remote, then execute the accepted verifier exactly once. Add `EXPECTED.txt`, `RUN.md`, `RESULT.md` without changing the pinned files. One probe-only PR, required byte-identical x86_64/aarch64 replay, aggregate `check`, merge commit only.