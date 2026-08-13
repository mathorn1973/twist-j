# READBACK C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS:        NON-CANONICAL INCUBATION READBACK
AUTHORITY:     none
ISSUE:         #357
PUBLIC BASIS:  Public Canon v46, main 6545c1d0
PUBLIC STATUS: no change
RH STATUS:     O (unchanged)
```

The frozen `PREREG.md` and corrected exact `break.py` are preserved verbatim.
There is no `RESULT.md`, no verifier claiming G3, and no promotion object in
this lane.

## Current gate state

The exact finite breaker checks only the displayed witnesses or discrete
models that it prints:

```text
G1  one delayed prime block has both signs
G2  one exact finite Schur witness has the required negative sign
G5  one exact discrete disjoint-shift analogue adds equal V-/V+ mass
    w_n ||v||^2
```

The general G2 Schur sign law and the general G5 disjoint-support identity are
separate elementary algebraic statements; the script is an audit witness, not
a universal proof by sampling.

For an actually disjoint translated support, the equal G5 increment cancels in
`||V_a^-v||^2-||V_a^+v||^2`. It does not by itself construct canonical
restriction maps, close the candidate form, or establish a nested Hilbert
system.

The terminal line remains decisive:

```text
G3 UNIVERSAL POSITIVITY UNDECIDED
```

Thus `q_A,a(v)>=0` has neither been proved nor refuted, and G4-G6 have not
opened. No per-cutoff or global contraction has been earned.

## Source and lane boundaries

This lane imports Suzuki arXiv:2606.09096 for the Weil functional and the
localized form `Q_W^a`. It is source-distinct from the scalar screw-function
work in #355 and #358, which uses Suzuki arXiv:2206.03682. The kernel theorem
source correction recorded in #355 must not be imported silently into this
frozen preregistration.

Three capacity-looking objects are not interchangeable:

- `q_A,a(v)` here is a quadratic-form candidate on the frozen test domain;
- `X_(+,a)` in #355 is the positive feature carrier in a windowed Krein-Gram
  factorization;
- scalar `A(t)` in #358 is the diagonal completion-capacity function attacked
  by ramp and screw falsifiers.

Before selecting between the first two as the carrier for a contraction, one
G0 classification must freeze their domains, gauges or neutral quotients,
cutoff maps, and equivalence criterion. Outcome-dependent selection is
forbidden.

The complete-prime-sector no-go recorded in #355 constrains any future
contraction built on those frozen source-side carriers: a surviving map cannot
be finite-prime-only and must have finite/archimedean coupling. It does not
prove G3 positivity or supply the missing cross-place map.

## Owner-reported G3a lead, not yet a result

During consolidation, the owner reported that a direct expansion of the
non-prime part appears to reduce `q_A,a` to one Fourier multiplier plus a
rank-two pole term. No exact formula, derivation, or repository commit was
available at this survey point. It is therefore recorded only as an open G3a
lead. It proves no lower bound, does not decide G3, and must be supplied and
audited under #357 before it can enter the scientific result state.

## Status boundary

This readback records exact finite algebra and an open gate. It carries no RH
evidence and moves no Canon, Registry, frontier, or evidence-ledger status.
