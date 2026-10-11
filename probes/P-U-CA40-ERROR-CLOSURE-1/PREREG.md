# Enlarged motional space and complete numerical error account

PUBLIC NON-CANONICAL. Conditional L1 mathematics and validated numerical
enclosures. Original work Apache-2.0, A. M. Thorn, 2026-10-11.

```text
probe_id: P-U-CA40-ERROR-CLOSURE-1
branch: probe/P-U-CA40-ERROR-CLOSURE-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1458
authority_base: 287494a553963c8fa254d085a9a8358b1a3fe83a
owner: A. M. Thorn, coordinated numerical-error session
```

The sealed predecessor is `P-U-CA40-SINUS-COMPARISON-1`, result head
944a487533c2faa85deb81ca8ceca82c51e30f36. Its failed convergence screens and
UNRESOLVED conclusion remain unchanged. Its observed centers were exposed
before this successor was designed; this is not a blinded prediction.

The complete sources, input, exact verifier, numerical defaults, proof,
decision rules and manifest must be committed, pushed and publicly read
back before the first new scientific execution or import. Static inspection,
syntax parsing, dependency capability checks and compilation are preparation
only. There is no unrecorded numerical pilot or post-pin source repair.

## 1. Equation and fixed question

Keep the compensated sine parent and coherent full two-frequency linear
model, in the notation and precise units of DERIVATION.md:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z)=R_z W_z,  U_S,z=U_L,z W_z.
```

All original input JSON bytes are retained, SHA256
ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53.
Every decimal token denotes an exact rational parameter for this comparison
model. Derived pi, k, kappa and eta are consistently enclosed, with
eta=kappa*exp(i*k*x). The independently rounded stored eta values are only
a legacy interface audit. Their maximum discrepancy is reported; they are
not used as an inconsistent second definition of the sine/linear force.
No pulse amplitude, position, mode vector, mode frequency or phase is fitted
to the new output. Supplied mode/geometry values are not claimed to be exact
properties of a laboratory trap.

Retain five 100-us loops, sixteen constant 6.25-us amplitude segments in each,
the absolute optical/motional clock, ideal instantaneous active X5 after
each loop including the last, and no bus reset. Evaluate all three active
labels (4,3), (4,4), (1,1), in that order, for +4*pi/5 and then -4*pi/5.
The selected six cases are not a worst-case guarantee over all 25 labels.

The question is whether controlled intervals can resolve the nonlinear
change in the selected electronic coherences for both original envelopes,
while explicitly controlling the total numerical error.

## 2. Code and numerical contract

`verify.py` is the accepted standard-library exact algebra/bookkeeping gate,
scoped by EXACT-DESIGN.md. Its first invocation has a 600-second limit and
must produce deterministic ASCII with LF, exit zero and empty stderr. It
does not execute or certify the large interval calculation.

`prepare_input.py` serializes decimal tokens without a binary64 model
conversion. `validated_model.cpp` uses MPFR4.2.2, 192-bit precision and
directed rounding for the coherent model, absolute-time linear prefixes,
Gauss roots/weights, analytic tube constants, thermal weights and guard-tail
coefficients. Gauss roots are isolated by opposite endpoint signs and 100
bisections in 16 disjoint brackets. Every endpoint sign must be decisive,
nodes must lie in (0,1), weights must be positive and their sum must enclose
one. Elementary-function enclosures use directed MPFR operations, including
a global Lipschitz enclosure for sin/cos of a real interval.

`kernel.cpp` generates candidate states using RK4 and forms a quintic
Hermite curve from endpoint values, first derivatives and centered finite
differences of the first derivative, with delta=h/128. The latter evaluate
the analytic continuation of the same constant-amplitude segment, including
at its endpoints. Every stored polynomial coefficient is an exact dyadic
number for certification. Their construction is not assumed exact or
accurate. All mismatches between adjoining polynomial endpoints and stored
candidate endpoints are enclosed and accumulated as jumps.

For every occupied step and all 120 thermal columns, the online checker
uses sixteen Gauss nodes, analytic degree N=15 and Bernstein ellipse rho=6.
It encloses the full finite guard defect, preserves sine/linear cancellation
before the vector norm, and adds an analytic creation tail beyond the guard.
The analytic full-Hilbert-space ellipse majorant controls the entire time
cell between nodes. A branch error is the weighted purification norm of
per-column defect integrals plus jumps. No step-doubling or cutoff agreement
is promoted into an error bound.

Both candidate and interval displacement actions use normal ordering and
seven commuting one-mode triangular exponentials. Intermediate annihilation
projections cannot remove a contributing path; creation is monotone in total
occupation, so intermediate guard projections are also exact. Thus the
projected true displacement is used, not an exponential or sine of a
truncated position matrix. Small independent dense and collective-ladder
fixtures check these interfaces after the public pin.

Compile with GNU C++14.2, -O3 -std=c++20 -fopenmp -ffp-contract=off
-fno-fast-math -fno-tree-vectorize and explicit AVX-512 target attributes.
Record the compiler, MPFR/GMP packages, full command and binary hash.
Use explicit per-operation directed SIMD rounding for the checker, with
nearest rounding and gradual underflow verified for every candidate worker.
Overflow, nonfinite data, invalid interval orientation or a failed fixture
stops the numerical campaign. There is no arbitrary epsilon replacing a
missing arithmetic enclosure.

## 3. Carrier, initialization and fixed resource ladder

The seven harmonic axial modes all remain present. Initially each has
nbar=1/20, independently of the electronic registers and external reference.
Retain all 120 initial occupations with total number at most K=3 and their
original unequal weights (20/21)^7(1/21)^N, without renormalization. The
exact omitted mass is 680046581/794280046581. This initial thermal omission
is distinct from dynamical projection.

Use the following configurations in order, each at most once:

| Dynamic cutoff L | Guard G | RK4 substeps per segment |
|---:|---:|---:|
| 8 | 10 | 512 |
| 10 | 12 | 512 |
| 10 | 12 | 1024 |
| 12 | 14 | 1024 |

The first two already exceed the predecessor's maximum L=6. A total-number
basis has binomial(L+7,7) states; the guard is not a second propagated
thermal bath. There are 90 case/batch tasks with eight thermal SIMD lanes
each and 80 explicitly bound OpenMP workers. Verify all 80 logical CPUs,
40 physical cores, two packages, both SMT siblings and the final CPU/place
map. No performance comparison to 40 threads is made here.

`numerical_run.py` has one 28800-second budget from entry, including setup,
coefficient preparation and all child launches/runs. Each child receives
only the remaining budget. Final validation, hashing and archival may extend
reported wall time. This is a maximum workload, not a promise of accuracy or
a timing prediction. Preserve timeout/nonzero-exit receipts and partial
progress. No replacement run, new cutoff, new quadrature order, new thermal
cutoff or unplanned refinement is permitted. A fresh successor would need
a new identifier and source pin.

## 4. Observables, systematics and decisions

Restore the exact model's branch-dependent linear frames before taking
electronic overlaps. Report complex sine and full-thermal linear coherence
intervals for all three pairs per sign, including all Weyl phases. No
branchwise phase fit or state renormalization is allowed.

Use the non-unit endpoint Gram bound in DERIVATION.md. For every pair report
separately the propagated numerical radius, exact thermal-tail radius,
interval-evaluation radius, their outward total and the final trace-distance
interval clipped to [0,1]. The total radius includes the width of the
computed center interval; a wide arithmetic enclosure cannot pass by being
omitted from the target. Guard-node, outside-guard, analytic continuum and
jump contributions are retained per thermal column. Diagnostic subdivisions
at quadrature nodes are not standalone continuous-time error bounds.

Two different questions have two explicit decisions:

1. The numerical precision goal is met if every one of the six pair total
   radii is at most exactly 1/1000. Stop the ladder at the first completed
   configuration that meets this condition for all six pairs.
2. The fixed-pulse nonlinear discrepancy target remains D_pair<=1/1000.
   A lower endpoint strictly above 1/1000 for at least one selected pair of
   each sign certifies a discrepancy for both angles within the declared
   model. A valid but wider interval can decide this second question while
   missing the separate precision goal. Otherwise report what each interval
   actually decides, without inventing a full-channel conclusion.

The runner compares the exact rational value of a binary64 bound with
1/1000 using Fraction, not a rounded threshold. The interval implementation
and proof must pass review as well as all runtime integrity checks before
calling an output certified. Invalid arithmetic, missing output or failed
custody means NOT_CERTIFIED. A valid wide enclosure means a valid bound with
the precision goal UNRESOLVED; it is not relabeled as an implementation
failure. Exhausting the ladder or budget never moves a threshold.

## 5. Evidence, layer and disposition

Action layer L1 only. The online interval checker is a different arithmetic
path in the same process as the candidate. Preserve source/input/binary
hashes, exact first stdout, every child stdout/stderr and receipt, progress,
basis, all endpoint vectors and per-column component totals. Full quintic
arrays are streamed and not retained; independent offline re-audit of all
intermediate curves is unavailable without deterministic pinned replay.
Same-session assistant review is not blinded numerical replication.

All five protected electronic registers, including the full source and its
external-reference marginal, are unchanged only under the inherited exact
zero-response premise. The separate obstruction for an unknown complete
source plus a retained informative receiver record remains in force.
Classical controls, harmonic axial motion and instantaneous carrier pulses
remain selected premises. No heating, scattering, radial motion, finite
control or complete work-reservoir account is supplied.

After a completed exact first gate, copy its actual stdout to EXPECTED.txt
and record RUN.md. Preserve successful, negative, incomplete and inconclusive
numerical results in RESULT.md/NUMERICAL.md at conservative status C. If the
exact first gate never completes, dispose the pin as ABANDONED under policy;
never invent EXPECTED.txt or resume a spent identifier. No Canon, registry,
workflow, policy or predecessor file changes belong to this probe.
