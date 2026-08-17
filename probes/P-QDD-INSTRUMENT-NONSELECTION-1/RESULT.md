# P-QDD-INSTRUMENT-NONSELECTION-1 result

Date: 2026-08-16

## Decision

```text
NONSELECTION-PASS
```

**Probe evidence gate: COMPLETE. Canon status: unchanged.** The frozen written
proof is theorem-grade at the declared L4 apparatus/support scope, the exact
local audit passed, and the repository-required GitHub x86_64 and aarch64 jobs
reproduced the committed `EXPECTED.txt` under the unchanged pin. The aggregate
`check` passed. This result is therefore eligible for a later reviewed `T`
fold, but this probe PR itself creates no Registry or Canon claim.

## Frozen scope decided

The exact audit returned 10/10 PASS with no tolerance and empty stderr.
Within the preregistered scope:

```text
S1a  For every nonzero G-self-adjoint idempotent E,
       {K : K^sharp K = E} = {W E : W in O(G,Q)}.

S1b  The frozen ordered two-branch raw fibre is one branchwise
       O(G,Q) x O(G,Q) orbit, not one diagonal orbit.

S1c  Gamma_ab = K_a^sharp K_b completely classifies diagonal O(G,Q)
       orbits. For the frozen two-branch pair, C = K_low^sharp K_high
       is complete. The attainable set is {E_low O E_high : O in O(G,Q)}.

S1d  With the frozen density-operator post-state definition, physical
       branch equivalence inside one nonzero effect fibre is exactly K ~ +/-K.

S1e  The rational family K_high(t)=R_t E_high gives an injection
       Q -> physical post-state instrument classes at fixed effects,
       fixed branch weights and C=0. Every two distinct rational t are
       physically inequivalent.

S2a  Every rational isometry between subspaces of a positive-definite
       rational bilinear space extends to a rational orthogonal map by
       an explicit finite product of rational reflections.

S2b  Every complete rational two-branch family
       sum_a K_a^sharp K_a = I
       has a rational orthogonal dilation on the frozen system/pointer type.

S3   Existence of an unrestricted rational orthogonal dilation is not
       an instrument-selection principle.

S3b  A target-controlled coupling U=sum_a E_a tensor X_a reduces to
       K_a=E_a with an adapted pointer because the target projectors are
       already present in U. It is circular as independent selection evidence.

S4   G-self-adjointness plus G-positivity plus K^sharp K=E uniquely gives
       K=E. This is a mathematical positive-square-root section only.

S5   K^sharp K=E implies globally on Q^4
       <Kv,Kv>_G = Tr(E v v^T G).
       The 625-point census is not needed as evidence for this identity.

S6   The displayed four-dimensional rational pointer apparatus is an exact
       orthogonal witness and reduces to the frozen Lueder pair, but S3b
       prevents reading that construction as independent selection.
```

## Strongest negative conclusion

The result is stronger than mere apparatus nonuniqueness:

```text
fixed effects + fixed branch weights + C=0
```

still contain an injective rational family of physically distinct post-state
dynamics. Geometric diagonal-orbit accounting therefore does not quotient the
physical instrument ambiguity.

Also,

```text
complete rational instrument family
  => rational orthogonal dilation
```

so existence of such a dilation cannot select one physical family.

## Remaining blockers

`QDD-INSTRUMENT-APPARATUS [O]` remains open. Two independent blockers survive:

```text
O2  independent physical instrument selection
O1  realized event generation / sampling
```

The only sampling statement earned here is `SAMPLING NOT PROVIDED`. No
impossibility theorem for sampling is claimed.

Any future independent selection probe must freeze its coupling before
comparison with `E_low,E_high`. A coupling controlled by those target effects
is forbidden as independent selection evidence unless the control projectors
are themselves derived from a separate registered input.

## What this result does not mean

No L5 stream or L6 measure was created. The probe does not close the apparatus
row, does not select the Lueder family physically, does not adopt positivity or
minimal disturbance as a physical law, does not rederive the effect pair or the
Born dictionary from J, and fills no decoder-completion-contract field.

The prior NON-CANONICAL incubation remains provenance only and contributes no
formal evidence to this result.

## Reproducibility state

```text
pin:             063a62b36a3aa9f9e90ffdc085c61d977d62ea16
PREREG sha256:   9575f297db404ceb7c10d7843351812d59ed1f8f655dc48130463b45a73c8d80
verifier sha256: 0ed1cea59d049ca13ee34de082c2b625a6c0bed289bbed0e02e3202d2a41134c
stdout sha256:   dc5ea636450ccb68f1c244654da8b48115342ee7b48012ca9ec34f280695a454
local x86_64:    PASS, empty stderr
GitHub x86_64:   PASS, workflow run 31943346739
GitHub aarch64:  PASS, workflow run 31943346739
aggregate check: PASS, workflow run 31943346739
Canon fold:      not started
```

Both architecture jobs passed policy, repository unit tests, Canon check,
ledger check, changed-probe reproduction and changed-minimal-reproduction
checks before the aggregate gate passed.

The next boundary is review and merge of this one-probe PR without squash or
rebase. Any Registry/Canon promotion is a later separate reviewed action.
