# Result: DP5/N384 passes the short speed and local-bound screens

Status: C

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-12.

The frozen A,C,C,A panel completed in 494.19504443742335 seconds.
A is inherited RK4/N512; C is the unchanged two-DP5-halfstep method and
three-point Hermite quintic at N384 certificate cells per segment.
Both within-arm repetitions were byte-identical. Both matched comparisons
classified all 2880 columns COMPATIBLE, with no INCONSISTENT or UNRESOLVED
case. Source/input/executable custody, runtime fixtures, eighty-worker
placement and the exact supporting gate passed. RUN.md and EXPECTED.txt
retain the first actual exact output.

**LOCAL_SPEED_AND_BOUND_SCREEN_PASSED.** The exact epsilon_C <= epsilon_A
condition passed for every column in both observations, including both
previously exposed exceptions. The speed condition passed independently.
No threshold, tolerance, input or pulse was changed after the source pin.

| Two-observation median | RK4/N512 A | DP5/N384 C | Observed A/C factor |
|---|---:|---:|---:|
| Program end-to-end seconds | 116.64690829534084 | 97.07313533872366 | 1.2016394431715545 |
| Kernel seconds | 69.80748984403908 | 55.42723101377487 | 1.2594439333743805 |

Timings cover the joint panel containing both angles, not separately timed
angle campaigns. Each median is the arithmetic mean of two observations.
These are descriptive measured factors, without confidence intervals or a
universal speed guarantee. All four individual timings remain in COMPARISON.md.

| Angle | Maximum local bound A | Maximum local bound C | Paired C/A bound ratio range |
|---|---:|---:|---:|
| +4*pi/5 | 2.599540871089461e-07 | 1.4229342499442583e-07 | 0.10032998428888386 to 0.7771823885396543 |
| -4*pi/5 | 1.975169639385187e-07 | 9.020590573093261e-08 | 0.10015906557114494 to 0.7311718085344631 |

Maxima are independent over each angle's 1440 local columns; ratios compare
matching columns. These are certificate upper bounds on local vector-norm
error, not measured true errors or gate infidelities.

The two formerly failing targets are window zero, labels (4,3), thermal
column 36, occupation (0,0,0,0,0,0,3), once per angle:

| Angle | Fresh RK4/N512 bound | Fresh DP5/N384 bound | C/A ratio | Decision |
|---|---:|---:|---:|---|
| +4*pi/5 | 4.777055050900987e-08 | 9.755508459129317e-09 | 0.2042159521960995 | PASS in both observations |
| -4*pi/5 | 3.879535150480492e-08 | 7.059814728598311e-09 | 0.18197578974697345 | PASS in both observations |

Their previous DP5/N256 C/A ratios were 1.001164071473513 and
1.0012107880240055. Those exposed results motivated this new probe and
remain unchanged. The present conclusions use fresh N384 and N512 runs;
no new DP5/N256 campaign or post-hoc tolerance was introduced. Passing the
two targets alone was insufficient: the complete 2880-column screen passed.

The immutable source pin is
`99625cf6039a4a17334664b00630857bdfa772c3`.
All fifteen sources plus the manifest were publicly read back before any
scientific execution. The six inherited input/model/kernel/tableau/helper
files were byte-identical to their predecessor. The DP5 step and quintic
formulas remained unchanged. Each window uses 4 RK4 steps/36 RHS calls/64
Gauss nodes for A and 6 DP5 halfsteps/39 RHS calls/48 Gauss nodes for C.
A/C changes integration method, substep count and certificate grid together;
the measured speed difference cannot be attributed to method order alone.

The pulses, seven modes, L8/G10 and all 120 retained thermal columns remain
fixed. Each 48.828125 ns window independently starts from a moving-frame
basis state with complete analytic linear history. It is not the nonlinear
state reached partway through a complete pulse. These local certificates
cannot be chained or extrapolated into a complete-pulse error account.

This result supports DP5/N384 for further bounded numerical work at this
local scope. It does not close either angle's complete error account,
compute final coherences, establish physical feasibility or prove complete
source preservation. No full trajectory, long run or automatic successor
was started. Exact-darkness and unknown-source no-imprinting boundaries
remain unchanged. The exact gate and later CI replay audit algebraic support,
not an independent rerun of the floating numerical campaign.

All first outcomes were retained without retry, repair or discarded warmup.
This identifier is sealed. Any extension requires a new preregistration
and source pin; this positive local screen authorizes no additional run.
