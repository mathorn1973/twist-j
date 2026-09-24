# Result: measurement-dependence price of counter models

Status: `T` proposed by the exact proofs in PROOF.md, with the verifier as
audit; non-canonical candidate until a separate public fold.
Outcome: `COUNTER-PRICE-PROVED; QDD-TABLE-PRICE-1/16; NO-CEILING`, subject to
required pull-request acceptance on both architectures.
Action layer: L6 only.

## What was proved

A counter model is a local response model whose latent state may depend on
the settings. Its overlap dependence eps is the latent mass not common to
all setting pairs; eps = 0 is setting independence.

| Object | Bound for every counter model | Attained | Price of the target |
| --- | --- | --- | --- |
| CHSH | `abs(S) <= 2 + 2 eps` | every rational eps | `2 sqrt 2` needs `eps >= sqrt 2 - 1` |
| five-context functional B | `B <= 2 + 8 eps` | every rational eps | `35/16` needs `eps >= 3/128` |
| complete ETH-QDD-2 table | minimal overlap `1/16` | yes | primal 15/16, dual 15/16 |
| signalling | at most `eps` | every rational eps | no-signalling forced only at `eps = 0` |

The complete table costs more than its Bell value alone: `1/16 = 8/128`
against `3/128`. The CHSH supremum over the class with overlap at most `e`
is `min(4, 2 + 2e)`. It rises linearly to the algebraic maximum and passes
`2 sqrt 2` at one tuned value without stopping there, so the class carries
no Tsirelson ceiling of its own.

## Evidence

The proofs are in PROOF.md. The pinned verifier (23 exact checks, Fraction
and Q(sqrt 2) arithmetic, no float) passed with stdout SHA-256
`083e31cacdc6324cb54d72f73bbb910de99bf7ef178926477a3f33c2274f3c0d`,
identical to the preregistered incubation stdout; see RUN.md. The
independent breaker found no break, including a full exact simplex over all
1024 types that recovers `w* = 15/16` without symmetry or hand certificate;
see BREAKER.md. This probe was RESULT-EXPOSED, as its preregistration
states, so the status rests on the proofs and not on a blind prediction.

## Relation to registered rows

QDD-FIVE-CONTEXT-BELL-SEPARATION is the eps = 0 case of the five-context
bound, and its setting-dependent separable construction is one member of the
class of (C5) with a larger overlap. BELL-CAUSAL-ACCOUNTING adopts
independent uniform controllers, that is eps = 0, and chooses no mechanism.
BELL-MAGIC-BOUNDARY and QDD-SELECTED-PAIR-LAW are untouched. This probe
adds the price and the absence of a ceiling.

Measurement-dependence relaxations of Bell inequalities are established
literature; the CHSH bound here is that genre in one exact form and no
priority is claimed for it. The exact values 3/128 and 1/16 for the
registered QDD table are the new content.

Measured witness, in no assertion: a reported photon-pair CHSH value of
2.82759 with standard error 0.00051 would require eps of about 0.414 in
this class. The decimals are a witness only.

## Scope and what is not claimed

Pure finite theorem at L6 on the stated comparison classes. It does not
state that any TWIST-J latent state, including the global counter, is or is
not setting dependent; it chooses no latent-variable, nonlocal,
superdeterminist or retrocausal explanation; it makes no empirical claim.
A reading of the latent variable as a TWIST-J plenum state needs its own
named gate.

Conditional consequence, recorded for that gate and not claimed here: a
counter reading of the registered QDD table is excluded under the adopted
independent controllers, needs at least one trial in sixteen with
setting-correlated latent state if independence is relaxed, and in either
case supplies neither the Tsirelson value nor no-signalling as a law.

## Fold proposal

For a later separate sealed fold, one registry row:

```text
claim_id       COUNTER-BELL-PRICE
status         T
scope          (C1) to (C6) of probes/P-COUNTER-BELL-PRICE-1/PREREG.md at L6
canon_section  8. The measure and Born
evidence       probes/P-COUNTER-BELL-PRICE-1/RESULT.md
falsifier      fires on a counter model with |S| > 2 + 2 eps, B > 2 + 8 eps
               or signalling above eps, on a counter model reproducing the
               ETH-QDD-2 table with overlap below 1/16, or on failure of
               an attaining construction or of the dual certificate
```

No change to any other registry, frontier or Canon row is proposed.
