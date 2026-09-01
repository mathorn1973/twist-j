# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1 result

Status: **STOP_DUAL_MIXING / ZERO_ENGINEERING_ONLY / zero phase evidence /
non-canonical**.

## Recorded decision

```text
source custody:          PASS
public input custody:    PASS
raw/output custody:      PASS
analysis replay:         PASS
primal mixing L=6:       PASS
primal mixing L=8:       PASS
dual mixing L=6:         FAIL (57 registered failures)
dual mixing L=8:         FAIL (60 registered failures)
terminal:                STOP_DUAL_MIXING
evidence weight:         ZERO_ENGINEERING_ONLY
production firewall F3: NOT SATISFIED
```

The sole authorized execution completed all four primal replays and all eight
independent dual chains. Every process exited zero with empty captured stderr,
and all source, input, raw-output, run-table and analysis-replay custody checks
passed. The authoritative line in `EXPECTED.txt` is exactly:

```text
TERMINAL STOP_DUAL_MIXING
```

## Why the gate stopped

The inherited primal sampler passed every frozen mixing gate at both volumes.
The independent dual sampler did not. Its local even observables had very low
effective sample sizes and excessive between-chain diagnostics. More
decisively, all four chains at both volumes had constant current observables:
zero within-chain variance in `j2_mean`, current nonzero density and every
registered lowest-momentum current power. The charge-conjugation-odd `n_mean`
mode was also constant in seven of eight chains.

The worst registered diagnostics included per-chain ESS `3.56722` versus the
required `64`, pooled bulk ESS `6.33387` versus `200`, split Rhat `1.66461`
versus `1.05`, and half-drift z `5.26172` versus `4`. This is a direct failure
of the prospectively frozen adequacy test for the dual schedule.

## Dictionary residuals are not interpretable

Five contact/off-contact residuals lie outside their four-SE intervals in the
raw analysis, while five pass. The preregistered precedence forbids treating
any of them as a character-dictionary test once mixing has failed. Therefore
this record is neither `STOP_DUAL_INTEGRITY` nor `BREAK_DUAL_DICTIONARY`, and it
is not evidence for or against a photon phase. The reported lowest-momentum
screening values likewise have no decision authority.

## Consequence

This immutable identifier is consumed and is never rerun. It does not satisfy
clause F3 of issue #757, so production issue #742 remains forbidden. Any future
attempt must use a fresh public identifier and a new preregistration aimed at
dual-sector mobility and current-mode mixing; it cannot tune this frozen run
after seeing the result.

No Canon, Registry, Frontier, program status, phase label, thermodynamic limit,
physical photon, pole, polarization, causal cone, SI quantity, Born selection,
matter/light split, contraction/expansion law or cosmological claim changes.
