# Registration-pair and recovery-law result

PROOF-SURVIVES, NON-CANONICAL. First pinned exact audit: PROOF_AUDIT_PASS.
No new empirical result, detector identification, native physical lift or
canonical status promotion.

Source pin: `d71a413ede89cfedec7ad58cd4ff47e73f993f6c`.
See [PREREG](PREREG.md), [PROOF](PROOF.md), [RUN](RUN.md) and the unchanged
raw [EXPECTED](EXPECTED.txt). The verifier reports 20,531 exact checks with
zero failures. No accepted source was repaired after its public pin.

## Surviving conclusions

1. Under the stipulated renewal rule, all-pairs registration weights have an
   exact causal transform and inverse. A finite inverse is admissible exactly
   when its first-gap weights are nonnegative and sum to at most one.
   Reachable hazards are unique; zero-survival ages are UNREACHABLE.
2. Direct normalized pair-to-recovery substitution is false in general.
   One dead step followed by hazard 1/2 gives stationary intensity 1/3 and
   normalized pairs 3/2,3/4,9/8 at lags 2,3,4, while normalized recovery is
   already 1 at each lag. The general proof supplies the all-length formula.
3. A finite dilute-input error bound survives, using the admitted opportunity
   rate rather than a measured far-lag normalization. It is not uniform in
   an unlimited time horizon or a calibration of continuous-time data.
4. Registrations alone do not separate opportunity rate from efficiency in
   the stated product model. Finite prefixes likewise do not fix their
   tail or stationary intensity.
5. The uniform-phase period-12 patterns {0,1,4,6} and {0,1,3,7} have identical
   absolute pair laws at every lag and the same intensity 1/3, but different
   next-gap distributions. Complete pair data do not establish the renewal
   premise or identify the larger class of correlated histories.

These are intended mathematical boundaries. They do not assert that the
published detector experiment, its finite-rate approximation or its reported
physical fit is wrong.

## Finite audit

| Category | Exact checks |
|---|---:|
| Hazard-prefix census | 11724 |
| Proposed-marginal census | 767 |
| Finite-prefix extensions | 319 |
| Hard-dead-time models | 600 |
| Dilute bound | 6569 |
| Input/efficiency ambiguity | 398 |
| Nonrenewal parity control | 20 |
| Stationary period12 pair-equivalent controls | 105 |
| Typed and empty boundaries | 29 |
| Total | 20531 |

The independent event-word oracle enumerated 56,326 words across 1,122 hazard
prefixes. Of 363 proposed pair prefixes, 40 admitted a renewal inverse and 323
failed its exact constraints. These are synthetic rational candidates, not
experimental samples or an estimated physical failure fraction. The audit
also covered 156 positive-survival tail extensions, 20 positive dead-time/rate
parameter pairs through lag 24, 1,452 dilute-efficiency prefixes and 24 phases
of the two periodic patterns through lag 48.

The all-length results rest on the proofs. Finite enumeration is an audit,
not an extrapolation to a physical detector.

## Physical disposition

The [successor note](../../notes/C-REGISTRATION-PAIR-RECOVERY-N.md) relates
the result to a documented all-pairs acquisition. No new experimental payload
was opened or fitted. Absolute scale, early-lag coverage, source statistics,
electronics and a justified reset/state law remain requirements for a physical
comparison. Independent arrival information is needed for efficiency claims.

The L1 source/coupling/record realization from native U remains
STOP-DEFINITION. Owners #539/#830/#832/#834 remain open. Public Canon v80 and
every earlier probe are unchanged. Required two-architecture CI must reproduce
the preserved stdout before the reviewed merge.
