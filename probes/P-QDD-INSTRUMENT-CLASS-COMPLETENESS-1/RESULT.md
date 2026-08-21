# RESULT. P-QDD-INSTRUMENT-CLASS-COMPLETENESS-1

Status: `PROVED AND AUDITED IN THE FROZEN FINITE-MEMORY CLASS / PUBLIC REPLAY PENDING / CANON UNCHANGED`.

## Decision

```text
FINITE-MEMORY-FIBRE-BOUNDARY
```

One formal execution returned zero, wrote empty stderr and produced the exact committed 27-line output with 18/18 exact gates passing. The accepted verifier was not executed before its public pin and was not rerun.

## 1. Complete pointwise branch fibres from operational premises

Let `M` be any finite nonempty internal phase set, with outcome-dependent phase permutations `tau_L,tau_H`. At phase `m`, let rational pure branch maps `K_L,m,K_H,m` obey only the frozen exact branch-norm identities and ordinary exact repeatability after phase update.

Polarization of the branch-norm identities gives

```text
K_L,m^sharp K_L,m=P,
K_H,m^sharp K_H,m=Q.
```

Positive definiteness kills the opposite input support. Repeatability together with the next-phase effect identities kills the opposite range support. Hence, for every phase,

```text
P K_L,m=K_L,m P=K_L,m,
Q K_H,m=K_H,m Q=K_H,m.
```

The support restrictions are finite-dimensional rational isometries and therefore orthogonal automorphisms. Thus exactly

```text
K_L,m=O_L,m P,
K_H,m=O_H,m Q.
```

Internal finite phase does not create a branch outside the already classified one-effect rational `A_rep` fibres under these operational premises.

This is completeness of the named rational finite-memory pure/repeatable apparatus class only. It does not cover unbounded-history, nonlinear, mixed, irrational or differently typed apparatus architectures.

## 2. Converse finite-memory realization

Conversely, take arbitrary finite phase-indexed branch maps from the two `A_rep` fibres and arbitrary phase permutations. The ready-state map

```text
v |ready,m>
 -> K_L,m v |LOW,tau_L(m)>
  + K_H,m v |HIGH,tau_H(m)>
```

is a rational isometry on the entire ready subspace. Distinct phase inputs remain orthogonal because the phase updates are permutations and the LOW/HIGH pointer states are orthogonal. At one phase the two effect forms sum to `P+Q=I`.

The public rational reflection-extension theorem then gives a rational orthogonal microscopic dilation on the full finite system-pointer-memory carrier.

Therefore the frozen finite-memory class is exactly a phase-indexed product of the old branch fibres together with the two phase permutations. Finite memory enlarges the apparatus law, but not the pointwise branch fibre.

## 3. Phase is a real post-state ambiguity under the registered equality

At every target-independent token, the probe constructs a rational `G`-reflection `O_*` on the three-dimensional moving support. It is orthogonal and is not `+/-I` on that support.

The two-phase apparatus

```text
M={0,1},
tau_L=tau_H=(0 1),
K_L,0=K_L,1=P,
K_H,0=Q,
K_H,1=O_*Q
```

satisfies exact effects, microscopic finite-memory reversibility and ordinary repeatability. Yet its two HIGH branch maps are not equivalent under the registered branch equality `K ~ +/-K` and an explicit rational ray is changed differently.

The same phenomenon survives an exact 256-phase cyclic control: 255 HIGH phases use `Q` and one uses `O_*Q`. This control is aligned with the memory scale exposed independently by the O1 sampler probe, but it imports no O1 sampler or denominator theorem.

Thus

```text
exact effects + finite internal memory + microscopic reversibility
+ ordinary repeatability
-/-> one phase-independent post-state branch law.
```

No phase gauge is adopted.

## 4. Consequence for O2b

The result changes the shape of the class-completeness problem.

A future physical class cannot be specified only by one branch map `T`. If local apparatus memory is physically admissible, the post-state law is at least potentially a family

```text
m -> T_m.
```

Within every finite rational pure/repeatable memory class frozen here, each `T_m` lies in the old exact branch fibre. But the family itself is not selected by the branch effects or repeatability.

Therefore O2b is narrowed, not closed globally:

1. finite internal memory does not escape the old pointwise fibres;
2. finite internal memory creates a genuine phase-indexed post-state ambiguity;
3. Public Canon v59 supplies no phase equality, phase gauge, or phase-independence law;
4. unbounded-history and differently typed apparatus classes remain outside this theorem.

The O1 result in PR #513 is relevant only as boundary evidence that local phase/memory can be load-bearing for event realization. It does not imply that post-state dynamics must depend on phase, and this probe does not modify O1.

## 5. Target comparison last

Only after the class, realization and phase-nonselection results are established does token `k=2` give

```text
P_2=E_low,
Q_2=E_high.
```

No target effect is used to choose any branch map or phase law.

## Candidate theorem rows

After byte-identical public x86_64 and aarch64 replay, a later separate fold may register at most:

```text
QDD-FINITE-MEMORY-BRANCH-FIBRE-COMPLETENESS [T]
QDD-FINITE-MEMORY-APPARATUS-REALIZATION      [T]
QDD-POSTSTATE-PHASE-NONSELECTION             [T]
QDD-FINITE-MEMORY-O2B-BOUNDARY               [T]
```

## Scope firewall

O2a terminal-event semantics is untouched. O1 is untouched. No L5 realized-event stream, L6 measure, randomness, sampling, Bell, SI, decoder completion, phase gauge, target-controlled selector, or new free dimensionless input is supplied.

Global O2b remains open beyond this frozen finite-memory class. Global `QDD-INSTRUMENT-APPARATUS [O]` remains open.

```text
SAMPLING NOT PROVIDED
```
