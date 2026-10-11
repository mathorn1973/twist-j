# Fixed-pulse numerical error closure with normwise arithmetic bounds

PUBLIC NON-CANONICAL. Conditional L1 mathematics and computational evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-11.

```text
probe_id: P-U-CA40-BALL-CLOSURE-1
branch: probe/P-U-CA40-BALL-CLOSURE-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1460
authority_base: c2459261aa15552e6560753dd8e1753f5164972d
owner: A. M. Thorn, coordinated numerical-error session
```

The predecessor P-U-CA40-ERROR-CLOSURE-1, sealed in PR #1459 at result head
2f290525279849484b7f3ba5be01871c3e18c2ea, completed its exact supporting gate
but was stopped manually for resource reasons before its first numerical
configuration completed. Its source pin, incomplete result and original
receipts remain unchanged. This is a new implementation and identifier,
not a resumed or repaired predecessor. Earlier finite numerical centers
and the resource-stop observations are exposed design inputs; this work
is not a blinded prediction.

All scientific sources, unchanged input, mathematical proof, exact verifier,
defaults and source manifest must be committed, pushed and publicly read
back before any new scientific execution or import. Static inspection, AST
parsing, dependency capability checks and compilation are preparation only.
No numerical pilot, unrecorded retry or post-pin scientific repair is allowed.

## 1. Equation and fixed question

Keep the compensated sine parent, full two-frequency linear model and
full-linear moving frame, in the units and definitions of DERIVATION.md:

```text
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i,
R_z = 2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                    -cos(chi_i)(m_i+X_i)],
i dot(W_z)=R_z W_z, U_S,z=U_L,z W_z.
```

The original input.json bytes have SHA256
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Each decimal token denotes an exact rational model parameter. Derived pi,
k, kappa and eta=kappa*exp(i*k*x) are coherently enclosed. The independently
rounded legacy eta table supplies a mismatch diagnostic, not a second
force definition. No waveform, geometry or phase is fitted to new outputs.
Supplied constants are not certified measurements of an apparatus.

Retain five 100-us loops, sixteen constant 6.25-us amplitude segments per
loop, the absolute clock and full-linear prefix, ideal instantaneous X5
on the two active registers after every loop including the last, and no
bus reset. Evaluate (4,3), (4,4), (1,1) for +4*pi/5 and then -4*pi/5.
This six-case panel is not a worst-case guarantee over all 25 active labels.

The question is whether a rigorous full-space error bound resolves the
fixed-pulse nonlinear coherence difference for both angle envelopes with
all six pair total radii at most exactly 1/1000.

## 2. Code and numerical contract

The accepted standard-library verify.py audits the exact supporting
identities, finite fixtures and bookkeeping in EXACT-DESIGN.md. Its first
run has a 600-second ceiling and must produce deterministic ASCII/LF,
exit zero and empty stderr. It does not execute or certify a trajectory.

The scalar model preparation retains 192-bit directed MPFR4.2.2 arithmetic,
exact full-linear prefixes, rigorously isolated sixteen-point Gauss nodes,
positive enclosing weights, thermal weights, guard-tail factors and
complex-time tube constants. No rotating-wave reset or inconsistent legacy
force coefficient is substituted.

The candidate remains RK4 with quintic Hermite reconstruction from stored
dyadic coefficients, endpoint slopes and centered directional differences
with delta=h/128. This reconstruction is an arbitrary candidate; no
unproved accuracy of its integrator or second derivatives is assumed.

The new hot checker uses floating vector centers with proved normwise
error balls. Small coefficient tables and scalar bounds use outward
arithmetic. Every center operation is charged according to DERIVATION.md,
including coefficient uncertainty, node uncertainty, complex products and
sums, norm reduction, gradual underflow, and polynomial endpoint jumps.
No guessed epsilon or measured small difference replaces an error bound.
All accumulated roundoff allowances are part of the reported total.

Seven commuting one-mode triangular exponentials implement the exact
normal-order projected displacement. Their finite projections discard no
path that can return. Keep cancellation in the finite guard defect before
taking its norm; bound the remaining infinite creation tail analytically.
At sixteen Gauss nodes per occupied cell, degree N=15 and Bernstein ellipse
rho=6, retain the same analytic full-Hilbert continuum remainder. Node-only
time/projection subdivisions are diagnostics, not separate continuous-time
certificates. Duhamel unitarity, all endpoint jumps and initial thermal
omission give the final norm account without a Gronwall multiplier.

Compile with GNU C++14.2, -O3 -std=c++20 -fopenmp -ffp-contract=off
-fno-fast-math -fno-tree-vectorize, using explicit AVX-512 target attributes.
Require nearest rounding, gradual underflow, no FTZ/DAZ, finite values and
the frozen runtime fixtures. NaN, overflow, invalid scalar intervals,
failed coefficient/root/fixture checks or missing arithmetic accounting
prevent a certificate. Record all versions, command, source and binary hashes.

## 3. Carrier and fixed workload

All seven harmonic axial modes remain present, each initially thermal with
nbar=1/20 and independent of the electronic registers and external reference.
Retain all 120 Fock occupations with total number at most K=3, using the
original unequal weights (20/21)^7(1/21)^N without renormalization. The
omitted mass is exactly 680046581/794280046581.

Execute this fixed ladder in order, each configuration at most once:

| Dynamic cutoff L | Guard G | RK4 substeps per segment |
|---:|---:|---:|
| 8 | 10 | 512 |
| 10 | 12 | 512 |
| 10 | 12 | 1024 |
| 12 | 14 | 1024 |

Use 80 explicitly bound OpenMP workers and eight thermal SIMD lanes per
case/batch. Check two packages, 40 physical cores, all 80 logical CPUs and
both SMT siblings, then retain the final worker CPU/place mapping. This is
not a new 40-versus-80 or AVX2-versus-AVX512 benchmark.

The total runner budget is 14400 seconds from entry, including preparation
and all child launch/run time. Each child receives only the remaining
budget. Final validation, hashing and archival may extend reported wall
time. Preserve every attempted launch, interruption, timeout, nonzero exit
and partial output. An explicit documented coordinator resource abort is
permitted only as an incomplete NOT_CERTIFIED outcome, never as a precision
success. It does not authorize resumption or a replacement under this identifier.

## 4. Observables, errors and decisions

Restore the exact full-linear frames, including Weyl phases, before taking
electronic overlaps. Report the complex retained-sine and full-thermal
linear coherence intervals for three pairs per sign. Do not fit branch
phases or normalize approximate endpoint vectors or retained thermal mass.

Use the unnormalized Gram bound in DERIVATION.md. For every pair report
numerical, thermal, center-evaluation halfwidth and total radii, and a final
trace-distance interval clipped to [0,1]. The total radius includes the
center interval halfwidth; the final interval expands the already interval
center by numerical plus thermal error, avoiding double-counted arithmetic.
Retain per-column guard, outside-guard tail, analytic continuum and jump
accounts, with any further roundoff diagnostic explicitly scoped.

The precision goal is met only if all six total radii are at most exactly
1/1000. Stop at the first completed configuration satisfying that condition.
Separately, a lower interval endpoint strictly above 1/1000 for at least
one registered pair per sign certifies a nonlinear discrepancy for both
angle envelopes in this conditional model. A valid wider interval can
resolve a discrepancy while missing the separate precision goal.

Compare exact Fraction(binary64 bound) values with 1/1000. Valid wide bounds
mean precision UNRESOLVED. Missing/invalid arithmetic, output or custody
means NOT_CERTIFIED. Budget or ladder exhaustion never changes a threshold
and an upper bound is not the actual state error. No all-input channel or
hardware conclusion follows from this selected panel.

## 5. Evidence, layer and disposition

Action layer L1 only. Candidate and checker share a process; this arithmetic
proof and same-session static review are not independent numerical replication.
Preserve source/input/binary hashes, first exact stdout, every numerical
stdout/stderr and receipt, progress, basis, final endpoint vectors and
per-column component totals. Full intermediate quintic arrays are streamed,
not retained; independent offline re-audit of every intermediate node needs
deterministic replay. Do not invent a complete trajectory archive.

The five protected electronic registers and their external-reference
marginal remain unchanged only under the exact-zero-response premise. The
obstruction for an unknown complete source plus a retained informative
receiver record remains. This study includes no ion experiment, finite
control, heating/scattering, radial motion or complete work-reservoir account.

After a completed exact first gate, preserve its actual stdout as EXPECTED.txt
and record RUN.md. Preserve positive, negative, incomplete and inconclusive
numerical outcomes in RESULT.md/NUMERICAL.md at conservative status C.
If the exact first gate never completes, dispose the pin as ABANDONED under
policy; never invent stdout or resume a spent identifier. This probe changes
no Canon, registry, policy, workflow or predecessor file.
