# Independent executable Stage-A review

**NON-CANONICAL / SOFTWARE + SYNTHETIC / 2026-10-01.** Reviewer: C96-02
reserve implementer, separate from the cartridge hardware author. This pass
reviewed and corrected `stage_a.py`, `keysight_acquire.py` and their tests.
It did not edit the design, BOM, wiring, enclosure or physical acceptance
limits, connect an instrument, energize a cartridge or perform qualification.

## Findings and implemented corrections

The following defects had concrete pre-fix software witnesses. They were
development defects, not observed laboratory failures.

| Witness | Pre-fix behavior | Corrected behavior |
| --- | --- | --- |
| `read_windows=81.0` | Numerically satisfied the 81-window check | Noninteger count rejected |
| 81 windows with `probe_on_s="0"` | Satisfied numerical hold because only an upper exposure bound was checked | Frozen 100 ms settling plus 100 ms read exposure required |
| Capture with both-pole feedback false and no probe intervals | Returned a RAW_DMM_CAPTURE | Invalid capture; armed admission consumed |
| Transport origin changed SYNTHETIC to MEASURED after arm | Returned MEASURED | Origin frozen at construction; changes rejected before reading |
| Re-arm after a previous successful arm then an identity failure | Left `armed=True` | Duplicate/reconfiguration failure consumes capture eligibility |
| Configured sample/trigger/autozero/delay state ignored by transport | Insufficient readback could still arm | Counts, pretrigger, range/autozero, delay and original settings must read back exactly |
| 10 NPLC selected for the frozen 100 ms read | Allowed despite 167/200 ms integration at 60/50 Hz | Only the selected 1 NPLC mode admitted |
| FAILED or INDETERMINATE hold through the CLI | Printed the failure but exited zero | Exit 2 or 3 respectively; numerical satisfaction remains exit 0 |
| Voltage extrema exactly on 4.7 or 50 V with nonzero uncertainty | No voltage uncertainty field existed | Required `voltage_U_V` expands the extrema before range acceptance |

The adapter now also requires independently observed measurement-complete
timestamps. Trigger and completion intervals, widened by their uncertainty,
must fit inside a declared probe interval's final 100 ms, following the first
100 ms settling period. Overlapping captures, empty/unobserved intervals,
wrong pole-feedback types and excessive timestamp uncertainty are rejected.
Returned metadata is copied so later changes to the caller's metadata object
cannot silently rewrite a previously returned observation.

The SCPI path checks initiation and acquisition errors as well as pre-existing
and configuration errors. Missing/extra samples, overload/nonfinite responses,
bad numeric readbacks, ignored settings and transport exceptions cannot return
a successful capture. These paths were exercised through a visibly SYNTHETIC
transport; none was tested against an actual 34465A. Command/readback semantics
were checked against the manufacturer's
[Truevolt Operating and Service Guide](https://www.keysight.com/zz/en/assets/9018-03876/service-manuals/9018-03876.pdf),
particularly trigger/sample count, integration, range/autozero and trigger
delay. Independent VM-complete observations are still the required timing
evidence; programming a mode does not prove its actual measurement latency.

## Metrology and unchanged limits

The covariance expression is correct for supplied endpoint standard
uncertainties: `k*sqrt(u0^2+u1^2-2*cov)+unresolved_U`. The code checks the
two-variable positive-semidefinite condition `abs(cov)<=u0*u1`, requires
nonnegative uncertainty and positive degrees of freedom, and rounds the
rational square-root enclosure outward. Missing or nonfinite uncertainty is
never substituted by zero. A justification hash is syntactic custody input;
it is not proof that a model is complete or independently authenticated.

Empirical-map interpolation is confined to measured-map knots, the exact
specimen/dock/temperature/history/protocol context, and an explicit qualified
interpolation-error bound. The convex weighted endpoint U values plus that
bound form a conservative interval enclosure without assuming independent
knot errors. This is distinct from the covariance model used for a difference.
The implementation never substitutes nominal CV-squared energy or extrapolates
outside the map. Authenticating the map and linking the difference covariance
to the actual map/calibration sources remains an external prerequisite.

For measured energy centers the hold upper bound is
`initial-final + U_difference + injection_upper`. The entire possible positive
injection is added, so it cannot conceal dissipation. Both 100 s and 200 s
retain exactly the 20 mJ limit. The measured-center formula adds U once; unlike
the true-energy enclosure in C96-02, there is no second estimate-error U to
add here. Tests accept exactly 20 mJ and reject 20.001 mJ at either horizon.

`voltage_U_V` must cover the calibrated voltage error and unresolved extrema
between observations for the supplied envelope. Treating it as only a DMM
catalogue accuracy would not meet that contract. A missing bound produces
INDETERMINATE. A covariance or voltage bound supplied as zero still requires
external justification; a numerical helper cannot authenticate such a claim.

The current executable protocol is deliberately narrow: it requires exactly
200 ms per declared probe interval and total exposure `windows/5` seconds,
with every retained capture inside the settled final 100 ms. This prevents a
measurement-free or shortened-exposure hold from satisfying the intended
assembled-sensing-path test. If a future qualified hardware protocol uses
strictly shorter actual on-time, it needs an explicit settling/read-coverage
contract and a new reviewed adapter/input revision. This helper does not
silently infer such coverage from a total-time upper bound.

## Actual checks and remaining limits

Executed on Python 3.12.10, without connected hardware:

```
python -B -m unittest discover -s notes/v96-cartridge -p test_stage_a.py -v
python -B notes/v96-cartridge/stage_a.py
```

All **24 SOFTWARE/SYNTHETIC tests passed**. The second command produced only
the conditional divider-load calculations, `41/172900 J` for 100 s and
`81/172900 J` for 200 s. It was not a physical hold. A development CLI test
initially encountered a temporary-directory permission failure; it was changed
to exercise the same actual subprocess/exit path through stdin, without local
fixture files. No scientific result was obtained or replaced by that repair.

The numerical helper never returns whole-Stage-A qualification. Synthetic
results retain their origin and NOT_CONFIRMATORY status; measured-labeled
summaries remain PENDING_AUTHENTICATED_FULL_STAGE_A. A real SCPI transport,
trusted calibration/receipt verification, an independent observation system,
all-read decoding and continuous-time envelopes, complete condition roster,
and preservation of every initiated/faulted attempt remain external duties.
The surrounding acquisition runner must retain raw responses and faults even
when this adapter raises an exception. These obligations cannot be replaced
by supplying favorable summary fields or a locally generated hash.

The coordinator separately read the repaired acquisition state, fixed-origin
handling, read-window checks and numerical predicates, then replayed all 24
tests on CPython 3.12.10 / Windows x86_64 (exit 0, 0.131 seconds). No further
blocking defect was found in that executable scope. This integration check
does not verify an instrument transport, authenticate a summary or establish
the as-built sensing circuit's settling and isolation.

## Separate circuit review of D1

The C96-01 reviewer, separate from the hardware author, inspected BUILD.md,
NETLIST.tsv and BOM.tsv against the cited manufacturer pin diagrams. The
LMP7721 special pinout and guard, HCT221 positive Q/reset/timing network,
HCT08 gates, ULN2003 coil connections, 91 Mohm divider and 10 kohm service
chains were consistent. The discharge power and ideal discharge-time
calculations were checked as design arithmetic, not access permission.

The reviewer found one concrete defect in the initial interface: a direct
powered DAQ REQUEST could back-power unpowered HCT logic through its input
diodes. The hardware author replaced it with a VO617A-4 optical link and
separately supplied SN74LVC1G17 Schmitt buffers. The reviewer then reread the
corrected pin/net connections and manufacturer diagrams. DAQ supply and
return remain on the LED side; opto collector and receiver use only the coil
rail. Logic polarity, pulldowns and bypasses match the intended operation.
The identified conductive backfeed path is removed. No further pin/net or
polarity defect was found in this correction.

This is a static circuit review. It does not establish as-built relay
pickup/release, powered-off leakage, component faults, protection, aperture
timing or thermal behavior. A1 is still incomplete because the independent
actual-contact observation topology and its bounded energy coupling are
absent, alongside the final vendor temperature configuration. Neither this
review nor the software suite qualifies a manufactured cartridge.
