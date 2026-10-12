# Local-window comparison of N256 and N512

PUBLIC NON-CANONICAL conditional L1 engineering mathematics.
P-U-CA40-GRID-COMPARISON-1.
Reservation: https://github.com/mathorn1973/twist-j/issues/1464.
Authority base: `37529581a5e0e111668f5f6501d633dbcbb3d2bc`.
This is mutable source preparation, with no execution or import authorized
before the complete public source pin.

## 1. Identical local problems and their restricted meaning

Keep the unchanged optimized PERF kernel, pulse/input bytes, seven modes,
dynamic cutoff L=8, guard G=10, full-linear moving frame and error account.
For each of the six fixed sign/label cases, let R_z(t) be the already defined
full-Hilbert residual generator. Its coefficients retain the original
absolute clock and full analytic linear history, including alpha, phase and
the branch's electronic schedule. Changing the subdivision count must not
change that mathematical generator or its linear-history initial condition.

At each registered window [a,b] define a NEW local comparison problem

    i dY_z(t,a)/dt = R_z(t) Y_z(t,a),   Y_z(a,a)=I.

For every retained occupation n, the common exact target is

    psi_(z,a,n) = Y_z(b,a)|n>.

Both numerical grids start from exactly the same unit vector |n>. This is
a computational reinitialization for a local test. It is not a physical bus
reset and not the actual nonlinear state at time a. The physical-frame local
input would be U_L,z(a)|n>; retaining U_L history does not manufacture the
missing earlier nonlinear W_z evolution. The full pulse's endpoint is not
computed by these disconnected windows.

There are 120 initial basis vectors with total occupation at most three.
They are evaluated separately, without renormalizing computed vectors or
combining them into a thermal pair-coherence claim. The test is not uniform
over all 6435 states of P_8, all 25 active labels, arbitrary initial bus
states, or nonlinear states that could have reached a window.

## 2. Exact matching of the windows

One amplitude segment has duration Delta=6.25 us=1/160000 second. A case
has S occupied segments in its full 80-segment sequence: S=32 for (4,3),
and S=16 for (4,4) or (1,1). Let s_j be the actual original segment index
at these occupied-sequence ordinals:

    0, floor((S-1)/3), floor(2(S-1)/3), S-1.

The coarse within-segment start indices are (0,128,128,254) at N=256.
The fine indices are (0,256,256,508) at N=512. Each coarse window uses two
cells; each fine window uses four. Thus for every j,

    a_j = Delta (s_j + q256_j/256)
        = Delta (s_j + q512_j/512),
    b_j-a_j = 2 Delta/256 = 4 Delta/512
            = 1/20480000 second = 48.828125 ns.

Every coarse boundary equals an even-indexed fine boundary. The last window
ends exactly at its amplitude-segment boundary, and no open window contains
a switch. All window clocks are original absolute times, not local zero.
The same four selection rules apply to both pulse signs. They are fixed
before outcomes, not selected where either grid looks favorable.

## 3. What the reused certificate bounds

For grid N in {256,512}, let p_N(t) be its actual dyadic polynomial candidate
on the window, with saved endpoint y_N and all local endpoint jumps retained.
The existing full-space residual proof, guard-tail bound, continuum allowance
and normwise arithmetic account apply to this new local initial value problem.
Their reported nonnegative total epsilon_N therefore has the conditional
meaning

    ||y_N - psi_(z,a,n)|| <= epsilon_N.

The exact initial basis vector and the reset local account are prerequisites.
The proof still requires all earlier floating/interval implementation
conditions. It is not replaced by grid agreement. No term may be removed
because both variants share it, and the arithmetic diagnostic already inside
guard is not added twice. The sampled time/projection/arithmetic components
remain diagnostic subdivisions, not standalone continuous-time certificates.

Different cells mean the two accumulated enclosures need not have identical
values. Local total growth can reflect time residual, projection, tail,
continuum, endpoint jumps or arithmetic; it is not by itself a measured
integrator order. A projection-dominated ratio near one does not demonstrate
time convergence, and a wider valid enclosure does not prove a larger actual
state error.

## 4. Independent endpoint discrepancy and three-way consistency

Triangle inequality through the SAME exact local target gives

    d = ||y_256-y_512|| <= epsilon_256+epsilon_512.

Treat every stored endpoint component and every reported error bound as its
exact binary64 dyadic value. The comparator independently encloses the norm
of their difference, without normalizing either endpoint or fitting phases.
For each real/imaginary component, subtract with directed rounding to obtain
[l,u]. Square safely:

    square([l,u]) = [0,max(l*l,u*u)] if l<=0<=u,
                   [min(l*l,u*u),max(l*l,u*u)] otherwise,

with outward products and sums. Directed square roots give [d_lo,d_hi].
All 6435 complex components contribute. The statement covers complex state
vectors through their ordinary realification; no extra sqrt(2) is appended.
Set S_up=add_up(epsilon_256,epsilon_512), including its final rounding.

Use exactly these classifications after finite/domain checks:

| Condition | Outcome |
| --- | --- |
| d_lo > S_up | INCONSISTENT |
| d_hi <= S_up | COMPATIBLE |
| Otherwise | UNRESOLVED |

An INCONSISTENT result contradicts the joint claimed certificates or the
matching-target/data contract; it is not a physical-model falsifier.
COMPATIBLE establishes compatibility with this outward sum, not a new proof
that the individual certificates are valid. UNRESOLVED is an interval that
straddles the comparison boundary. Merely having d_hi>S_up is not a proven
contradiction. Equality at the lower endpoint is not INCONSISTENT.

The fixed panel contains 4*6*120=2880 comparisons. All must be reported.
These are deterministic simultaneous checks; no statistical multiple-testing
interpretation or confidence level is attached to them.

Repeated runs at the SAME N must have identical endpoint/component bytes;
a same-grid mismatch is fatal. Each registered cross-grid comparison stores
all 2880 records in its output JSON and emits only a compact stdout summary.
INCONSISTENT is fatal. UNRESOLVED does not stop the remaining short trials,
but prevents a compatible-panel PASS. Comparator pairs are run ordinals
(1,2), (4,3), (5,6), after runs 2,4,6 respectively. Each comparator receives
at most 90 seconds within the campaign's total 1800-second budget.

## 5. Separate engineering growth budget

Independently of discrepancy classification, require for every registered
window/case/column

    epsilon_256 <= 2 epsilon_512.

Use exact rational values of the stored binary64 bounds for this decision.
Do not divide by a possibly zero fine bound: zero versus zero passes, and
positive coarse versus zero fine fails. Per-case/window summaries and
component ratios are informative but cannot hide a failing column.

The factor two is a predeclared engineering budget for local enclosure
growth, not a mathematical necessity, physical accuracy criterion, guarantee
of fourth-order scaling, or complete-trajectory tolerance. A missed budget
means the coarser grid failed this chosen local screen; a passed budget does
not adopt N256 globally. Wide common bounds may make both compatibility and
growth easy to pass while conveying little precision.
An error-growth miss is retained as a negative screen and does not cancel
the remaining six-run design. Speed is reported without a fixed speed target.

The existing twelve component fields and endpoint norm enclosures permit
reporting whether time, projection or other terms dominate. Timings and any
speed ratio remain separate measurements with the runner's frozen limits.
No comparison here closes full pulse pair coherences, demonstrates the
required nonlinear discrepancy for both signs, or authorizes a long run.

## 6. Proof and execution boundaries

The unitary local propagator and residual-domain contract are inherited from
the frozen sine/full-linear model. Reuse of its certificate is conditional
on correct source, coefficient, floating environment and data custody.
The small exact verifier checks only rational window/triangle/interval
supporting identities. It does not execute a propagator or emulate the
directed AVX implementation. The actual comparator needs source review and
pinned runtime checks; its outcomes must be preserved without retries.
