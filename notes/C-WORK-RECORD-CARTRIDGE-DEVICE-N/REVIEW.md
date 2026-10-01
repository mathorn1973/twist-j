# Design review disposition

NON-CANONICAL / OPEN engineering proposal. Review date: 2026-10-01.
This is static mathematical/engineering review, not laboratory evidence.

Three delegated reviews examined the full-state mathematics, electrical
energy provenance and metrology. Sources were the pinned #1316 proof and
physical contract, current public repository policy and primary manufacturer
and NIST documentation cited in DESIGN.md and TEST_PLAN.md. No physical data,
new scientific simulation, original-ZIP rerun or independent discovery of the
known work-to-record theorem occurred.

## Resolved specification defects

| Concern | Disposition in the proposal |
| --- | --- |
| Lossy capacitor charge sharing is not the exact contact swap | Move the entire insulated resource cartridge between fixed neighbouring docks. |
| Registers alone can conceal an independently powered reaction | Eleven physical banks, measured donor/recipient ports, net target bank work and whole-path provenance limits accompany the 96-coordinate readback. |
| Gate/sensor power or previously charged converter parts can finance apparent received work | Donor-fed LT8365/8 V supply sits behind the donor meter; all other possible contribution and residual storage is bounded over source-to-target interval. |
| A forward/reverse analog loop can accumulate errors before equalization | Table states ideal account changes; feedback starts from actual measured input energy, with fixed target counts, without compulsory nominal withdrawals. |
| Equalization can borrow the receiver's pre-existing energy and report a misleading gross pulse | Count net signed work over the entire local gate and all corrective routes, including baseline restoration. |
| Zero-count accounts make ratio division undefined | Handle restoration/drain to reference separately; ratio comparisons use positive target counts only. |
| Independent bank tolerance intervals are not a robust invariant physical domain | Separate Dec, tight Prepare and unearned Enc_oper reserve certificates; include an explicit9.560 J versus9.780 J counterexample. |
| Model-zero need not remain exactly5 V under passive leakage | Separate no-commanded-baseline-use from bounded passive droop, add4.7 V physical floor and idle-loss limits. |
| Measurement itself can consume the resource | Disconnect idle/moving probes, qualify loading; continuous INA228 VBUS sensing is expressly excluded at the proposed budget. |
| Exchanged capacitor identity and calibration can become hidden state | Track identity-to-dock permutation as auxiliary state; define a calibrated physical equivalence class. |
| Source and offimage only match in software | Require measured initial source-energy equality with uncertainty, common target preparation and both physical cuts. |
| Layer readouts, inverse timing and holdout use can be chosen afterward | Fixed operation/settling/read windows, separate inverse expected tables, and excluded end-to-end holdout tuning. |
| A full record reveals source preparation and cut configuration to the target evaluator | Fixed target-only packets, separate custody, sealed assignments/calibration mappings and a complete locked target verdict before any full-data disclosure; source attribution is assessed afterward. |

The local mathematical bounds, eleven-account decomposition, unchanged
Ghat;A;B;F law, C5 inverse and whole S42 logical encoding are internally
consistent. This is not a proof that the proposed analog controller converges
or that the chosen component population meets the work/retention requirements.

## Remaining physical obligations

The selected capacitor's published leakage limit is far above the required
idle-loss budget. Its actual population may fail qualification. The advertised
converter peak efficiency is not a short-pulse guarantee. Repeated isolated
source reactions under cut0, auxiliary startup/discharge, servo convergence,
mechanical timing, energy-map hysteresis, pointer degeneracy and metrology
loading all require actual qualification. None has passed in this work.
The first two hardware stages are explicitly one cartridge with its actual
switched sensing path (20 mJ also over 200 s), followed by one isolated cut0
source cell under repeated conversions without external recharging. The
0.100 mW and approximately 2.1 microampere equivalents of the first requirement
are design limits, not estimates of actual leakage. A user review identified
the need to lock target assessment before exposing the revealing full records;
section 5a specifies that separation without changing acceptance thresholds.

Detailed circuit/layout and fixture drawings, exact peripheral ordering codes,
controller implementation, calibration certificates, acquisition/reduction
code, finite-horizon reserve certificates and a named physical gate remain
absent. The documents therefore cannot be used as an execution-ready
preregistration or fabrication release. The acceptance numbers specify what
must be demonstrated and what will reject this proposal; they do not fill
these gaps with assumed performance.

If qualification succeeds, the proposed 400-run campaign tests the four
declared preparation families at a chosen clock, with complete decoded state
and actual source-funded work. It still does not certify every physical point
in S42, autonomous closure, microscopic reversal, natural selection of the
law, permanent memory or repeated reset. The mathematical candidate-T/L1
milestone remains intact independently of these hardware questions.

## Public provenance and repository scope

Authority was checked against public main and canon-v95 at
b8ba1a07ad776cdd8d878fe0a407e07312c0e263, declared content
5a1dd8ba6c339640940b5a013d3c412025a1f8fc, all five normative file hashes,
successful main architecture/aggregate run 36766242516 and publication runs
36769404870/36773377591. The Canon file remains 848893 bytes with SHA-256
b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f.

Before ownership issue #1317, the scan included182 remote heads, 157 open issues,
63 open PRs and an empty quoted all-state search for this candidate identifier.
The existing mathematical owner is #1315/#1316; general apparatus/data
definition owners #539 and#834 are not replaced. The branch begins exactly at
#1316 head 312d0a90b24d5f9e743096f0ee2a477cda719a10, retaining its dependencies
#1312 and#1310. The different law#1314 is not imported.

Only these four notes are new. No Canon, verifier, workflow or old candidate
source changes; no merge, promotion, tag, release or physical claim. Repository
CI for this documentation checks repository integrity, not physical feasibility.
