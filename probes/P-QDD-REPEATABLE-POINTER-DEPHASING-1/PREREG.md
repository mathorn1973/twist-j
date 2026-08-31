# P-QDD-REPEATABLE-POINTER-DEPHASING-1 preregistration

Date: 2026-08-29

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the accepted verifier are
both present at the immutable public pin and read back from the remote branch.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v71
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v71
CONTENT_COMMIT: a77d720433c19976f9ab663d023ec9364eac34eb
CANON_SHA256:   0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
BASE_COMMIT:    842b43e2f258469712aedf121f879767d1bd072c
CLAIM_ISSUE:    671
BRANCH:         probe/P-QDD-REPEATABLE-POINTER-DEPHASING-1
PATH:           probes/P-QDD-REPEATABLE-POINTER-DEPHASING-1/
```

The declared Canon tag and content commit are ancestors of `BASE_COMMIT`.
The normative Canon hash matches `canon/SHA256SUMS`. The most recent merged
pull request at the base passed the required x86_64, aarch64 and aggregate
`check` jobs.

## Mandatory result-exposure disclosure

A same-session NON-FORMAL incubation preceded this preregistration. It derived
the candidate block-dephasing identity, considered a rational pointer-overlap
example with overlap `3/5`, and considered an effect-preserving but
non-repeatable branch as a negative control. Those calculations and all chat
transcripts are discovery context only and are excluded from formal evidence.

The accepted `verify.py` in this directory has not been executed before the
public pin. Syntax parsing, byte hashing and other static checks are permitted
before the pin and carry no scientific evidence.

## Existing public inputs

This probe consumes only registered or already public exact mathematical
inputs at their existing scopes:

```text
QDD-PROJECTOR-PAIR-TR4               [T]
QDD-INSTRUMENT-NONSELECTION          [T]
QDD-FINITE-MEMORY-O2B-BOUNDARY       [T]
```

In particular, the finite-memory result supplies the frozen mathematical
pure/repeatable branch form at each apparatus phase,

```text
K_L,m = O_L,m P,
K_H,m = O_H,m Q,
```

with exact branch effects, support repeatability and a rational orthogonal
microscopic dilation into orthogonal LOW/HIGH pointer slots. This probe does
not adopt that apparatus class as physical, enlarge it, or close
`QDD-INSTRUMENT-APPARATUS [O]`.

No current cross-layer gate is consumed. The present decision remains entirely
at L4.

---

## Frozen preregistration fields

### 1. Equation

Work over

```text
V = Q^4,
one = (1,1,1,1)^T,
G = I_4 - (1/5) one one^T,
G^-1 = I_4 + one one^T,
A^sharp = G^-1 A^T G.
```

Freeze the complementary `G`-self-adjoint projectors

```text
P = E_low  = (1/4) one one^T,
Q = E_high = I_4 - P.
```

Thus

```text
P^2=P,  Q^2=Q,  P^sharp=P,  Q^sharp=Q,
PQ=QP=0,  P+Q=I.
```

Let `M` be any finite nonempty phase set. For each `m in M`, admit branch maps
in the frozen rational pure/repeatable class:

```text
K_L,m^sharp K_L,m = P,
K_H,m^sharp K_H,m = Q,

P K_L,m = K_L,m P = K_L,m,
Q K_H,m = K_H,m Q = K_H,m.
```

Let the two pointer records be orthonormal slots `e_L,e_H` of a rational
two-dimensional pointer carrier. Define the joint ready-subspace isometry

```text
J_m(v) = K_L,m v tensor e_L + K_H,m v tensor e_H.
```

For any rational operator `R in End_Q(V)`, define the exact pointer reduction
of `J_m R J_m^sharp` by contraction on the orthonormal pointer slots. Its
system operator is

```text
Phi_m(R)
 = K_L,m R K_L,m^sharp
 + K_H,m R K_H,m^sharp.
```

The target theorem is

```text
P Phi_m(R) Q = 0,
Q Phi_m(R) P = 0
```

for every finite phase set `M`, every `m in M`, every admitted branch pair and
every rational operator `R`.

The same map is trace preserving:

```text
Tr(Phi_m(R)) = Tr(R).
```

The word `dephasing` in the candidate name means exactly this vanishing of the
two complementary L4 operator blocks after the displayed mathematical pointer
reduction. It does not mean physical environmental decoherence or collapse.

### Written proof of the universal target

Because `P K_L,m = K_L,m`, taking `sharp` and using `P^sharp=P` gives

```text
K_L,m^sharp P = K_L,m^sharp.
```

Since `K_L,m P = K_L,m`, the LOW map is zero on `im(Q)`, and equivalently

```text
K_L,m Q = 0,
K_L,m^sharp Q = 0.
```

Similarly,

```text
P K_H,m = 0,
P K_H,m^sharp = 0.
```

Therefore each summand of the cross block vanishes:

```text
P K_L,m R K_L,m^sharp Q = 0,
P K_H,m R K_H,m^sharp Q = 0.
```

Hence `P Phi_m(R) Q=0`. Taking `sharp` after replacing `R` by `R^sharp`, or
repeating the same support argument on the opposite block, gives
`Q Phi_m(R) P=0`.

For the trace,

```text
Tr(Phi_m(R))
 = Tr((K_L,m^sharp K_L,m + K_H,m^sharp K_H,m) R)
 = Tr((P+Q)R)
 = Tr(R),
```

using only cyclicity of finite matrix trace.

The phase label never enters the proof. The conclusion therefore holds
pointwise for every member of every finite phase family in the frozen class.

### 2. Code

`verify.py` is the only accepted verifier.

It uses Python standard-library `Fraction` arithmetic only. It audits:

1. the exact `G`, `G^-1`, `P`, `Q` carrier identities;
2. representative rational phase maps from the already classified
   pure/repeatable fibre;
3. exact orthogonal-pointer reduction against direct block summation on the
   full 16-element matrix basis of `End_Q(V)`;
4. vanishing LOW/HIGH cross blocks and trace preservation;
5. the two frozen negative controls below.

The universal quantifier is owned by the written proof above. The verifier is
an audit, not the logical source of that quantifier.

No external package, network access, file input, random seed, clock or
floating-point arithmetic is admitted.

### 3. Carrier or data

There is no external dataset.

The complete frozen carrier is the rational data displayed above. The verifier
also uses the exact sum-zero orthonormal vectors

```text
r = ( 1, 1,-1,-1)/2,
f = ( 1,-1, 1,-1)/2,
g = ( 1,-1,-1, 1)/2,
```

to construct representative rational rotations inside `im(Q)`.

#### Negative control N1: pointer orthogonality removed

Keep the repeatable Lueder branch pair

```text
K_L=P,  K_H=Q,
```

but use unit pointer records

```text
u_L = (1,0),
u_H = (3/5,4/5),
<u_L,u_H> = gamma = 3/5.
```

Use the fixed rational source vector

```text
v = (4,3,2,1)^T
```

and its normalized pure record

```text
R_v = v v^T G / (v^T G v).
```

The pointer-reduced system operator is then

```text
Phi_gamma(R_v)
 = P R_v P + Q R_v Q
 + gamma (P R_v Q + Q R_v P).
```

The frozen negative decision is

```text
P R_v Q != 0
and
P Phi_gamma(R_v) Q = (3/5) P R_v Q != 0.
```

This control shows that orthogonal record slots are load-bearing for the
displayed one-event dephasing theorem.

#### Negative control N2: range repeatability removed

Keep orthogonal pointer slots and the exact effects, but set

```text
z = (1,0,0,0)^T,
W_z(x) = x - 2 z <z,x>_G / <z,z>_G,
K_L = P,
K_H = W_z Q.
```

`W_z` is a rational `G`-reflection, so

```text
K_L^sharp K_L=P,
K_H^sharp K_H=Q.
```

The right support remains `Q`, but the HIGH output is not required to remain
inside `im(Q)`. Use `R=I_4`. The frozen negative decision is

```text
Q K_H != K_H
and
P (K_L R K_L^sharp + K_H R K_H^sharp) Q != 0.
```

This control shows that exact effects alone do not imply the target theorem.

The controls establish only that each removed premise admits a counterexample.
They do not assert a complete necessity classification over all alternative
apparatus axioms.

### 4. Systematics

The probe must distinguish the following without conflation:

```text
S1  algebraic branch effects versus physical effects;
S2  support repeatability versus effect equality alone;
S3  orthogonal record slots versus a nonzero record overlap;
S4  pointer reduction at L4 versus an L5 realized-event stream;
S5  block dephasing versus instrument selection inside a branch;
S6  block dephasing versus Born occurrence frequencies;
S7  global rational orthogonal reversibility versus reduced information loss;
S8  this finite-memory rational class versus unbounded, nonlinear, mixed,
    irrational or differently typed apparatus classes.
```

No claim may use one side of a distinction as an alias for the other.

### 5. Failure threshold

The positive target fires if any exact algebraic counterexample within the
frozen pure/repeatable orthogonal-record class gives

```text
P Phi_m(R) Q != 0
or
Q Phi_m(R) P != 0,
```

or if the displayed trace-preservation identity is false.

The audit also fails if any frozen carrier identity or representative
pure/repeatable effect identity is false.

Negative control N1 must retain nonzero coherence with exact factor `3/5`.
Negative control N2 must preserve the two effects, fail HIGH range
repeatability, and exhibit a nonzero cross block. Failure of either control
does not move a threshold; it fires the corresponding preregistered audit gate.

Any attempt to interpret this L4 theorem as a physical apparatus, realized
event, environment, collapse, L5 stream, L6 measure, photon coupling, SI
decoherence time or unique instrument is outside scope and is not a positive
closure.

### 6. Action layer

```text
ACTION_LAYER: L4
FROM_LAYER:   L4
TO_LAYER:     L4
CROSS_LAYER:  NO
```

This is an exact support/operator theorem and an exact mathematical pointer
reduction on one L4 carrier. It creates no L1-L5 or L4-L6 lift and owns no
entry in `canon/GATES.tsv`.

---

## Candidate scientific ceiling

If the written proof survives review and the pinned exact audit passes, the
probe may support at most the following later Registry row:

```text
QDD-REPEATABLE-POINTER-DEPHASING [T]
```

with scope restricted to the exact rational L4 pure/repeatable finite-memory
class and the orthogonal mathematical pointer reduction frozen here.

The probe itself changes no Canon, Registry, Frontier, Evidence or Gate ledger.
Any promotion is a separate reviewed fold.

## Scope firewall

No physical decoherence claim. No environment model. No collapse. No physical
effect or instrument adoption. No apparatus selection. No realized event,
occurrence law, sampling, randomness or independence. No L5 stream. No L6
measure. No photon bridge or photon-window repair. No SI rate or time. No
decoder completion. No change to `QDD-INSTRUMENT-APPARATUS [O]`,
`QDD-INSTRUMENT-CLASS-COMPLETENESS [O]` or
`QDD-TERMINAL-EVENT-SEMANTICS [O]`.
