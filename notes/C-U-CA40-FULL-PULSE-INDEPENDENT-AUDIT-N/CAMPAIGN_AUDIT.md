# First saved-account audit of the closed full-pulse campaign

**PUBLIC / NON-CANONICAL. Conditional L1 numerical evidence.**
Original work Apache-2.0, A. M. Thorn, 2026-10-13.
Reservation: [#1473](https://github.com/mathorn1973/twist-j/issues/1473).

The first actual campaign audit returned **SAVED_FULL_ACCOUNT_AUDIT_PASS**:
the complete saved account passed its consistency and exact aggregation
checks. All six selected pairs met the `1/1000` precision-radius goal.
Four pair intervals resolve discrepancy above `1/1000`, including two at
each angle sign; one pair remains unresolved and one is within target.
These are separate conclusions. This is one Linux x86_64 audit execution,
not a numerical replay or a two-architecture scientific computation gate.
No normative claim, source, pulse or previous first outcome was changed.

## Source and execution record

| Field | Recorded value |
|---|---|
| Numerical probe | P-U-CA40-DP5-FULL-CLOSURE-1 |
| Reviewed numerical source pin | `bca348445715c03f4cdc3af6079207024dd40332` |
| Original closed outcome | `COMPLETE_PRECISION_GOAL_MET` |
| Original campaign end, normalized to UTC | `2026-10-12T22:42:17.332027Z` |
| Auditor source pin, published before its first execution | `9a5c07e140d5781934e026414aa7f7b306b15952` |
| Auditor record head before this campaign report | `7220b6d190d876baff27ff584a87976799406d20` |
| audit_saved.py bytes / SHA-256 | 43212 / `2f92288c339ed17370d1bd8d22bbbf7929c793dfdf504a25c1bf4bf281480340` |
| Actual audit environment | Linux; x86_64; CPython 3.13.5 |
| Actual audit start, normalized to UTC | `2026-10-13T10:04:18.364799Z` |
| Actual audit end, normalized to UTC | `2026-10-13T10:05:14.645621Z` |
| Measured wall seconds | 56.25480427965522 |
| Audit invocations / exit code | 1 / 0 |
| Audit stdout bytes / lines | 9897 / 1 |
| Audit stdout SHA-256 | `5f71cf4a6ee8e75aac46dc7382fb05dc2aa2da02eb8d75e702e8f275c654b333` |
| Audit stderr bytes / SHA-256 | 0 / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Copied source and executable independently rehashed | Both true |
| All-snapshot norm option | False: default terminal checks only |
| Solver executed by this audit | False |

The private receipts use explicit `+00:00` timestamps; the UTC values above
are their normalized instants. The original campaign end is therefore on
the preceding UTC date. The command's flags and order were:

```sh
python3 -I -B <hash-bound-audit_saved.py> \
  --campaign <absolute-closed-offline-campaign> \
  --binary <absolute-copied-binary> --source <absolute-copied-source>
```

Angle-bracket operands replace private absolute paths. The auditor source
is the pinned `audit_saved.py` named above. Neither `--allow-incomplete` nor
`--all-snapshot-norms` was used. The retained private run record carries the
actual command and receipts; this public document is a reviewed neutral
summary, not a raw stdout or private-log import.

## Copied evidence and completeness

The coordinator's separate copy receipt records a closed campaign, verified
closed processes, preserved original key receipts and no scientific program
or solver execution during copying. The audited inputs remained unchanged.
The auditor rehashed **all 14588 state artifacts** against a complete copied
inventory. It validated **90 complete tasks, 7290 committed snapshots and
5280 inactive byte-identical carries**, with no uncommitted checkpoint files.
Both logs were available and complete: 23040 cell-progress records, 7200
checkpoint-progress records and 90 task-completion records, with the six
required lifecycle phases and no truncated final log record.

Exact IEEE binary64 squared norms were recomputed for **720 terminal column
vectors only**. Initial basis bytes and final endpoint/component equality
with terminal snapshots were checked. Active intermediate endpoint norms
were not all recomputed; their payloads were hashed and their cumulative
component rows checked. The optional all-snapshot norm audit was not run.

| Preserved evidence | Bytes | SHA-256 |
|---|---:|---|
| Copied artifact inventory | 2424474 | `b540e5135c5d0b81f7c4e7b5ee8bf0a0ac9f08bf6812b1931b113666a40700c8` |
| Copied final custody receipt | 1575 | `ae81c8e940ae2beead4eca379c78b8d07380a573c4a04350e0316f366eed56a6` |
| Copied child receipt | 222 | `26e50adc009d7e723470cf55c9663af0bbb6c324474a7a75e03f46ed6816c1ba` |
| Original numerical stdout | 312313 | `49940669a1954abaa52a230d1e40d76bc9bc7cef0b6eb395b1c57f10176f3e31` |
| Original numerical stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Copied closed summary | 17670 | `ac9348f39112dfb00de47988f79f483b492600f4bfbbc4d8871babec4ded1def` |
| Copied executable, rehashed without executing | 376464 | `cb758140dc2387221c59bd8e5cc4bd9c8b0e0234c9f6bc36bf425e03b11849db` |
| Private first audit execution record | 2193 | `b767adab4b1be589a3c95f58f8855747f79a8254a9bd1e423513f8a0ea032d60` |
| Private offline-copy custody record | 1601 | `564f39fe92942478dd56d0873aa646ed3f90b8dd826f10fce613c4c08cf0ae25` |

The copied source manifest matched all fixed reviewed-source hashes, and
the copied source files and binary were additionally rehashed. These
receipts identify preserved bytes and mutually checked custody. The auditor
still reports `original_execution_independently_authenticated=false`;
matching receipts do not independently attest the original machine.

## Six exact pair accounts

Cases 0,1,2 are `(4,3),(4,4),(1,1)` at `+4pi/5`; cases 3,4,5 repeat those
labels at `-4pi/5`. All entries below are the **exact saved rational values**.
The saved thermal radius is an outward bound on half the exact omitted
thermal mass; it is not a renormalized retained-state error.

| Cases | Numerical radius | Thermal radius | Arithmetic radius | Total radius | Final distance interval | Precision | Discrepancy |
|---|---|---|---|---|---|---|---|
| 0,1 | 7584607333403175/18446744073709551616 | 1974216350377137/4611686018427387904 | 13773/72057594037927936 | 3870368184609403/4611686018427387904 | [6180320861745755/144115188075855872, 6422218873283843/144115188075855872] | PASS | EXCEEDS_TARGET |
| 0,2 | 948075916675333/2305843009213693952 | 1974216350377137/4611686018427387904 | 13747/72057594037927936 | 3870368184607611/4611686018427387904 | [3115375241708271/72057594037927936, 3236324247477259/72057594037927936] | PASS | EXCEEDS_TARGET |
| 1,2 | 1183696747253451/2305843009213693952 | 1974216350377137/4611686018427387904 | 97399/576460752303423488 | 4341609845663231/4611686018427387904 | [0, 7183517048513581/4611686018427387904] | PASS | UNRESOLVED |
| 3,4 | 1087604666264357/9223372036854775808 | 1974216350377137/4611686018427387904 | 110357/576460752303423488 | 5036037368784343/9223372036854775808 | [1745543596785147/72057594037927936, 7296926722689611/288230376151711744] | PASS | EXCEEDS_TARGET |
| 3,5 | 4350418665056665/36893488147419103232 | 1974216350377137/4611686018427387904 | 110359/576460752303423488 | 5036037368784185/9223372036854775808 | [109830130467365/4503599627370496, 7343880685460373/288230376151711744] | PASS | EXCEEDS_TARGET |
| 4,5 | 5187105761169209/36893488147419103232 | 1974216350377137/4611686018427387904 | 6573757/36893488147419103232 | 5245209142690017/9223372036854775808 | [0, 1132347373966847/1152921504606846976] | PASS | WITHIN_TARGET |

The following displays are **rounded approximations for orientation only**.
They are not new outward enclosures; all decisions use the exact table above.

| Cases | Numerical radius, approximately | Thermal radius, approximately | Arithmetic radius, approximately | Total radius, approximately | Distance interval, approximately |
|---|---:|---:|---:|---:|---|
| 0,1 | 4.1116239e-4 | 4.2808993e-4 | 1.9113877e-13 | 8.3925232e-4 | [0.04288459, 0.04456310] |
| 0,2 | 4.1116239e-4 | 4.2808993e-4 | 1.9077795e-13 | 8.3925232e-4 | [0.04323452, 0.04491302] |
| 1,2 | 5.1334663e-4 | 4.2808993e-4 | 1.6896033e-13 | 9.4143657e-4 | [0.00000000, 0.00155768] |
| 3,4 | 1.1791833e-4 | 4.2808993e-4 | 1.9143888e-13 | 5.4600827e-4 | [0.02422428, 0.02531630] |
| 3,5 | 1.1791833e-4 | 4.2808993e-4 | 1.9144235e-13 | 5.4600827e-4 | [0.02438719, 0.02547920] |
| 4,5 | 1.4059678e-4 | 4.2808993e-4 | 1.7818204e-13 | 5.6868671e-4 | [0.00000000, 0.00098215] |

Precision means every total radius is at most exactly `1/1000`; it does
not mean every model discrepancy is at most that threshold. Discrepancy
is above target only when the final lower endpoint is strictly greater
than `1/1000`, within target when the upper endpoint is at most `1/1000`,
and otherwise unresolved. Thus this account has both a precision PASS and
resolved selected nonlinear discrepancy for both angle signs. The two
remaining pair conclusions are retained rather than being absorbed into
that both-sign statement.

For the unresolved pair (1,2), the saved witness-center upper endpoint is
5683814407259083/9223372036854775808. Adding its thermal radius gives
exactly 9632247108013357/9223372036854775808, approximately 0.001044330324,
which exceeds 1/1000 before any numerical radius is added. Therefore these
unchanged K3 retained-center/tail intervals cannot certify WITHIN_TARGET
merely by reducing the numerical radius to zero. This is a direct
post-audit rational consequence of the saved bounds, not an additional
auditor check, a lower bound on the true discrepancy or a new solver run.

## Conditional scope and remaining limits

`K3` retains all 120 initial seven-mode thermal columns of total occupation
`N<=3`, with exact unrenormalized weights `(20/21)^7(1/21)^N`. Its omitted
mass is `680046581/794280046581`, charged once as half-distance allowance.
This is distinct from dynamic cutoff `L8`, guard `G10` and subsequent
occupation growth. The fixed full word covers 80 segments through 500 us,
with 384 cells per occupied segment, not a cutoff/grid convergence ladder.

The audit independently checked saved consistency and rational aggregation.
It did **not** independently rerun propagation, recover the cellwise quintics,
internal stages or Gauss-node enclosures, recompute MPFR force/model
preparation, rederive all inherited norm-ball/guard/infinite-tail/continuum
bounds, or recompute restored displacement, relative phases and coherence
rectangles from endpoint vectors. Valid local enclosures, the declared unitary
full-space propagator and correct restoration remain premises. Sampled
time/projection/arithmetic splits are diagnostics and are not extra radii;
the arithmetic center halfwidth is counted once in the precision account.

The distance intervals concern only the selected fixed compensated sine
parent versus its declared full-linear reference and the selected pair
witnesses. They do not establish an all-input channel bound, all 25 labels,
a complete motional-state/energy account, spectator protection, apparatus
accuracy, physical occurrence, a native contact or any L2-L6 bridge.
Review was assisted within the same coordinated session and is not blind
external confirmation. The earlier 27-positive/52-negative synthetic fixture
result and its RUN/EXPECTED files remain unchanged and separate from this
first actual saved-output audit.

The original numerical branch records its own first outcome. Prospective
bounded follow-up planning is separate from this audit result; this report
authorizes no solver rerun, altered pulse, extended deadline or ion experiment.
