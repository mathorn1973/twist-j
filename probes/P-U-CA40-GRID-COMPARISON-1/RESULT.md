# Result: faster local propagation; bound-growth budget missed

Status: C

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

The frozen six-child N512,N256,N256,N512,N512,N256 panel completed in
636.4802846238017 seconds. All same-grid endpoint and component comparisons
were byte-identical. All three matched comparisons classified all 2880
columns COMPATIBLE, with no INCONSISTENT or UNRESOLVED case. Runtime
fixtures, eighty-worker placement and source/input/executable custody passed.
The separate exact supporting verifier passed; RUN.md and EXPECTED.txt
preserve its first actual output.

The propagation-window median fell from 69.82082353718579 seconds at N512
to 35.47577432915568 seconds at N256: observed speedup 1.9681268374684553.
The program end-to-end median fell from 116.65041020512581 to
61.60147115588188 seconds: observed speedup 1.8936302659062014. These
timings cover the joint panel containing both signs, not separately timed
angle campaigns. No speed threshold or universal performance claim applies.

The independent engineering condition eps256 <= 2*eps512 failed for all
2880 columns in each matched comparison: **LOCAL_BOUND_GROWTH_BUDGET_MISSED**.
These are bounds on local vector-norm error, not measured gate infidelities
or true-error ratios. Maxima below are taken independently over each sign's
1440 local columns; ratio ranges compare matching columns.

| Angle | Maximum local bound N512 | Maximum local bound N256 | Paired bound ratio range |
|---|---:|---:|---:|
| +4*pi/5 | 2.599540871089461e-7 | 3.868678895880346e-6 | 9.531582873158316 to 15.898152470508364 |
| -4*pi/5 | 1.975169639385187e-7 | 2.984426821755486e-6 | 10.56081818971268 to 15.87515143885409 |

The sampled temporal-defect diagnostic grew about 15.7 to 15.9 times,
whereas sampled projection and arithmetic diagnostics changed much less.
These sampled terms have no separate continuous-time certificate and are
not added again to guard or total. Two grids do not establish a convergence
order. COMPARISON.md gives all timings, all 24 window/case groups, component
breakdowns and the retained evidence account.

The immutable source pin is
`ea8bff874876c1b6f902409888e4e98fb7716066`.
All fourteen source files were publicly read back before execution. Original
pulses and input bytes, the seven modes, L8/G10 and all 120 retained thermal
columns were unchanged. Each window independently starts from a moving-frame
basis vector with the original full analytic linear history. It does not
start from the nonlinear state reached by an earlier complete evolution.

The local comparison supports a speed/upper-bound tradeoff and fails the
chosen growth budget. It does not adopt N256 for a complete calculation,
close either angle's full error account, compute final coherences, establish
physical contact admission or prove full-source preservation. No full
trajectory or longer follow-up was started. The exact-darkness and unknown-
source no-imprinting boundaries remain unchanged.

All first outcomes were retained without retry, source repair or discarded
warmup. This identifier is sealed; further numerical changes require a new
preregistration and public source pin.
