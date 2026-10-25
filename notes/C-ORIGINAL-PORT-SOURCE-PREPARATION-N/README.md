# Original-port source preparation and its native boundary

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Date: 2026-10-25.
License: Apache-2.0.

This successor gives an exact complete preparation circuit for the
contact-active source pair in [issue #1775](https://github.com/mathorn1973/twist-j/issues/1775),
a finite driven local realization on the actual occupation code, and
explicit thermal, energy and reset boundaries. It does not claim that
the original six-pentit transition synthesizes that circuit.

## Fixed target and result

The source is the same one-pair, one-carrier model, with receiver at 100
and U_rec unchanged during the subsequent three-step experiment. Put

```text
chi_s=alpha_(97,0), d_s=(U^2-U^(-2))chi_s,
Z=(39521+154 sqrt(5))/15625,
psi_s,±=(chi_s±d_s)/sqrt(Z).
```

The supplied predecessor proves that the two sources have the same
initial configuration populations and entire U_rec spectral measure,
but their three-step receiver contrast is

```text
Delta_p=65536(48533-10985 sqrt(5))
        /[5^9(39521+154 sqrt(5))] > 1/50.
```

These predecessor identities remain conditional inputs to this successor.
They do not become independently accepted by being used here.

[SOURCE_CIRCUIT.md](SOURCE_CIRCUIT.md) gives one full unitary from the
specified source basis port u2 and three ready auxiliary bits to psi_s,+.
It uses a linear combination of I,U_rec^2,-U_rec^(-2), one calibrated
attenuation and one exact amplitude-amplification iteration. The good
amplitude is fixed to 1/2 before that iteration. All helpers return to
zero, with no success postselection or discarded branch. The construction
uses 29 named operations, including six controlled forward steps and six
controlled inverse steps. These are not 29 elementary local gates.

The endpoint is uniform on the entire 26-state old memory and every
reference. Intermediate controlled steps may act on the memory and
subsequently restore it. One retained setting qubit, controlled-F and
an explicit setting Z phase give the coherent two-source isometry with
31 named operations. The three later forward steps are exactly the
original experiment, with no preparation gate inserted between them.

[LOCAL_REALIZATION.md](LOCAL_REALIZATION.md) supplies a deliberately
conservative local existence realization. It uses the actual occupation
intertwiner, including its coin gauge, 4414 qubits and 4414 finite ladder
sites of dimension 26469. Each funded interaction involves at most six
nearby qubits and one ladder site. With a fixed interaction cap g, the
serial duration is bounded by

```text
T_prep <= (pi hbar/g) 512 n^4 4^n,    n=2208.
```

The sharp reservoir funds the specified occupation charge H_N, not the
original spectral H_*. The construction is driven; ordered gate control,
timing, calibration precision and its reset remain supplied. The bound
establishes finiteness and locality in the added gate model, not feasible
hardware or a single autonomous thermal Hamiltonian.

The concrete helper-cooling option adds 220900 fresh thermal donor qubits
to prepare its 2209 zero-energy helpers within error 1/4000. Their complete
local routing costs at most 10934550 additional operations. The localized
source seed and sharp reservoir/rail states are still supplied resources;
this is not an all-thermal preparation of the full apparatus.

## Complete input, error and reset contract

The ideal input consists of the original localized basis source u2,
arbitrary admitted old memory/reference, ready core and synthesis scratch,
one sharp reservoir and ready rail sites, and a retained setting when
required. Each is an explicitly supplied resource. The readout contrast
requires the old receiver to lie in K=span(d1,...,d25). The preparation
itself works on all 26 labels. Unknown data are not used as workspace.

The desired endpoint includes the selected source, unchanged old memory
and its reference, returned computational helpers and returned sharp
charge reservoir. The spent thermal donors are retained separately and
are not assumed to have been regenerated. A returned computational
workspace is not a reset of the source seed, setting, timing controller
or donor bank.

[RESOURCES_RESET.md](RESOURCES_RESET.md) proves:

- Every U_rec-stationary state is more than 1/100 in trace distance from
  the active positive target. A covariant preparation with error at most
  1/1000 must use an input more than 9/1000 from every stationary input.
  This is an asymmetry bound, not a work or joule bound.
- M dirty zero-energy helper bits can be prepared within error epsilon
  using exactly 2Mr retained Gibbs donor qubits, where
  r=2 ceil(log2(2M/epsilon)), beta_h*d_h=ln2 and
  beta_c*d_h>=ln(4M/epsilon). All initial thermal defects remain in the
  channel. This does not prepare the original Q-asymmetric seed.
- The two source vectors have nonzero overlap (2-Z)/Z. Erasing N
  orthogonal settings while retaining the exact product sources requires
  at least 2^N distinguishable garbage states in the stated pure-ready
  unitary contract. Coherent settings also require retaining their known
  relative phase.

For two preparations with errors delta_+,delta_-, three common evolution
steps with half-diamond errors epsilon_j and a read effect with operator
error eta, the retained contrast obeys

```text
Delta_p_actual >= Delta_p-delta_+-delta_-
                 -2 sum_(j=1)^3 epsilon_j-2 eta.
```

The sufficient total loss budget 1/100 preserves contrast greater than
1/100. A possible allocation is delta_±<=1/1000, each epsilon_j<=1/1000
and eta<=1/1000. These are requirements on a realization, not achieved
material tolerances. Full joint helper/donor comparisons and reduced
reference comparisons are distinguished in RESOURCES_RESET.

## What the unchanged six-pentit rule actually contributes

[NATIVE_BOUNDARY.md](NATIVE_BOUNDARY.md) proves a positive native primitive:
at counter zero the actual selector swaps the zero-sum codes
E(lambda,mu)=(lambda,mu,-lambda,-mu,0,0). Its linear extension gives a
relative plus/minus eigenphase on already prepared symmetric and
antisymmetric vectors. It does not supply controlled-SWAP or coherent
preparation. A checkpoint-diagonal input remains at least 1/2 away from
the required antisymmetric eigenspace.

The full original map also merges some distinct first-step heads; its
unqualified delta lift is not a unitary. The previous residue
semiconjugacy is not invertible into full complex amplitude data. These
are scoped obstructions, not a universal impossibility theorem for all
extended native encodings. A new encoding needs a fixed reader, admitted
gates and readiness, not only a target-matching dimension count.

## Evidence, scope and next admissible step

This package is proof-first analytical work. Three parallel authoring
roles and the coordinating author checked the source circuit, native
boundary, resources and local synthesis. These are same-session checks.
No expanded scientific matrix, circuit program or simulation ran. The
precise external sources and independent review obligations are in
[VALIDATION.md](VALIDATION.md); SHA256SUMS covers the six content files.

The next bridge obligation is now explicit: supply the source seed and
the phase-correct local gates under one admitted preparation/control
law, with an inclusive physical energy and a finite timing/precision
budget. The local driven construction can be used as a specified target
for that work. It does not decide original six-pentit admission, incoming
unbound capture, physical energy selection, autonomous controller
renewal, permanent storage or individual-outcome occurrence.

No predecessor proof, Canon, registry, scientific threshold or workflow
is changed by this directory. No merge or scientific promotion is part
of this result.
