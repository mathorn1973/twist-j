# P-QDD-REPEATABLE-POINTER-DEPHASING-1 result

Status: `PROVED AND TWO-ARCHITECTURE AUDITED IN THE FROZEN L4 CLASS / CANON UNCHANGED`.

## Decision

```text
REPEATABLE-POINTER-DEPHASING-PASS
```

The written proof in the frozen preregistration establishes the universal L4 statement. The accepted exact verifier ran only after the public pin and returned `9/9 ALL PASS`, exit code zero and empty stderr. Pull request #672 then reproduced the same pinned verifier and exact stdout on GitHub-hosted x86_64 and aarch64, and the aggregate `check` passed.

## 1. Exact theorem in the frozen class

On

```text
V = Q^4,
G = I_4 - (1/5)11^T,
P = E_low,
Q = E_high = I-P,
```

let a finite-memory phase `m` carry any branch pair in the already registered rational pure/repeatable class,

```text
K_L,m^sharp K_L,m=P,
K_H,m^sharp K_H,m=Q,
P K_L,m=K_L,m P=K_L,m,
Q K_H,m=K_H,m Q=K_H,m.
```

With exact orthogonal LOW/HIGH pointer records, the mathematical pointer reduction is

```text
Phi_m(R)=K_L,m R K_L,m^sharp + K_H,m R K_H,m^sharp.
```

For every rational operator `R`, every finite phase set and every phase in that set,

```text
P Phi_m(R) Q = 0,
Q Phi_m(R) P = 0,
Tr(Phi_m(R)) = Tr(R).
```

The proof is support algebra: `K_L,m Q=K_L,m^sharp Q=0` and `P K_H,m=P K_H,m^sharp=0`; trace preservation uses cyclicity and `K_L,m^sharp K_L,m + K_H,m^sharp K_H,m=P+Q=I`.

This result is independent of which allowed within-branch orthogonal post-state map is used at a phase. Therefore the already proved post-state instrument nonselection inside the finite-memory fibre does not obstruct this block-dephasing theorem.

## 2. Exact pointer-reduction audit

The verifier constructs five rational phase representatives in the registered fibre and audits the full sixteen-element basis of `End_Q(V)`. On all `5 x 16` cases it verifies:

```text
joint ready-map isometry,
orthogonal pointer contraction = Phi_m,
LOW/HIGH cross blocks = 0,
trace preservation.
```

This finite audit is not the source of the universal quantifier; the written algebraic proof is.

## 3. Frozen negative control N1

Removing pointer orthogonality while keeping the repeatable Lueder branch pair retains coherence exactly.

For

```text
u_L=(1,0),
u_H=(3/5,4/5),
gamma=<u_L,u_H>=3/5,
v=(4,3,2,1)^T,
v^T G v=10,
```

the frozen pure record has `P R_v Q != 0` and the pointer reduction gives

```text
P Phi_gamma(R_v) Q = (3/5) P R_v Q != 0.
```

The verifier exhibits the first nonzero output entry as

```text
(0,0) = 9/40.
```

Thus orthogonal record slots are load-bearing for the displayed one-event dephasing theorem.

## 4. Frozen negative control N2

Removing HIGH output repeatability while retaining exact effects and orthogonal pointer slots also breaks the target.

Let `W_z` be the frozen rational `G`-reflection at `z=(1,0,0,0)^T` and set

```text
K_L=P,
K_H=W_z Q.
```

Then

```text
K_L^sharp K_L=P,
K_H^sharp K_H=Q,
Q K_H != K_H.
```

At `R=I_4`, the reduced channel has

```text
P Phi(R) Q != 0,
```

with first nonzero verifier entry

```text
(0,0) = 105/256.
```

Hence exact occurrence effects alone do not force block dephasing.

The two negative controls show only that each removed premise admits a counterexample. They do not classify every alternative apparatus axiom.

## 5. Scientific meaning and ceiling

The earned mathematical statement is narrower than physical decoherence:

```text
orthogonal mathematical pointer record
+ exact branch support repeatability
=> exact LOW/HIGH block dephasing after L4 pointer reduction.
```

It does not say that the current public architecture physically realizes such an apparatus. It does not identify an environment, event, collapse process, occurrence law or decoherence time.

Because the universal statement has a self-contained exact proof, the scientific ceiling is theorem-grade at the frozen L4 scope. A later separate Canon fold may register at most:

```text
QDD-REPEATABLE-POINTER-DEPHASING [T]
```

No Registry or Canon change is made by this probe itself.

## 6. Remaining physical blocker

`QDD-INSTRUMENT-APPARATUS [O]` remains unchanged. The public theory still lacks physical ownership of the effects, apparatus carrier, ready phase, coupling, pointer, reduction, realized event and L1-to-L5 event bridge. This probe only shows that if a future physical apparatus lands inside the already classified pure/repeatable orthogonal-record class, block dephasing requires no additional within-branch instrument selector.

## 7. Public reproduction

Pull request #672 workflow run `33275989088` reproduced the pinned verifier and exact `EXPECTED.txt` on both required repository architectures:

```text
x86_64:   Ubuntu 24.04.4, CPython 3.12.14, VERIFY PASS
aarch64:  Ubuntu 24.04.4, CPython 3.12.14, VERIFY PASS
aggregate: TWO-ARCHITECTURE CHECK PASS
```

Both architecture legs reported verifier SHA-256
`c366b9e6bfcc2727fbcd2e49fde87d76f6867dfecea6f4e99bffaa7a572f77c5`
and stdout SHA-256
`d734fb338f315db08d69a6b8a80d555a45e57a7a531c492e037b502120f42240`, identical to the public pin/local record. Both also passed policy, 142 tool tests, Canon v71 with 342 claims, ledger and gate contract.

This is two-architecture reproduction, not independent mathematical confirmation.

## Scope firewall

No physical decoherence claim. No environment. No collapse. No physical apparatus adoption. No event generation or sampling. No randomness or independence. No L5 stream. No L6 measure. No photon bridge or photon-window repair. No SI rate or time. No decoder completion. No move of `QDD-INSTRUMENT-APPARATUS [O]`, `QDD-INSTRUMENT-CLASS-COMPLETENESS [O]` or `QDD-TERMINAL-EVENT-SEMANTICS [O]`.

## Formal record

```text
claim issue:       #671
pull request:      #672
base commit:       842b43e2f258469712aedf121f879767d1bd072c
pin commit:        254127da12f4570c16e80293244fd3770a604cd3
PREREG sha256:     2866bfa490257afccf32a2370dda6ade69a123f894353ca2726b0e598e41fe60
verifier sha256:   c366b9e6bfcc2727fbcd2e49fde87d76f6867dfecea6f4e99bffaa7a572f77c5
stdout sha256:     d734fb338f315db08d69a6b8a80d555a45e57a7a531c492e037b502120f42240
local architecture: x86_64
local result:      9/9 ALL PASS
workflow run:      33275989088
x86_64 replay:     PASS
aarch64 replay:    PASS
aggregate check:   PASS
Canon status:      unchanged
```
