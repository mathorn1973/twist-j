# Conditional finite-duration control model for the affine routing

**PUBLIC; candidate-T, L1; NON-CANONICAL.** This document supplies an exact
Hamiltonian construction under explicitly added quantum-control assumptions.
It does not identify a native physical carrier, derive an interaction from
`J` or `U`, report a device experiment, or close QDD-INSTRUMENT-APPARATUS.
The mathematical construction is separate from the conservation boundary in
this probe. In particular, an externally prescribed control Hamiltonian is
not a clean autonomous implementation with a fully accounted controller.

## 1. A control family specified independently of the QDD response

Take six distinguishable five-level systems, with Hilbert space

```math
\mathcal H_S=(\mathbb C^5)^{\otimes6},\qquad
|x\rangle=|a,b,c,d,q,r\rangle.
```

The labels are the representatives `0,1,2,3,4` of `F5`. For each system define
the dimensionless, integer-valued operator

```math
N=\sum_{j=0}^4 j|j\rangle\langle j|.
```

This notation does not identify `N` with a physical particle number or a
free-energy observable. An actual carrier and its free Hamiltonian would
have to be specified separately.

The following ideal control family is admitted on the whole tensor product,
independently of the four QDD inputs, the response `f`, and LOW/HIGH:

1. On each five-level system, exact local Fourier transforms, their inverses,
   cyclic label shifts, and nonzero field-label scalings, up to known global
   phases independent of the input. A sufficient Hamiltonian implementation
   of this local assumption is described in Section 4.
2. On each chosen ordered pair of distinct systems, a calibrated interaction
   `H_ij=-hbar g N_i N_j`, with `g>0`, can be applied for a prescribed positive
   duration. The interaction itself is symmetric in the two systems; the
   local Fourier operations determine which one is the target of an addition.
3. A calibrated local term `-hbar g N_j` is available when a simultaneous
   local phase is used below. Alternatively, use the separately admitted
   local label shift.
4. These Hamiltonians act exactly on the declared five-level systems, with
   all unlisted systems as spectators. Residual free drift is absent in this
   model or its complete evolution is known and compensated. Switching,
   pulse areas and local phases are supplied by external controls.

Thus this is a specified family of one-system and two-system Hamiltonians,
not the logarithm of the desired entrance matrix. It is broad enough to
implement affine field permutations on any input, rather than only an
interpolated response at four points. Its physical availability is an added
premise. Neither the pair interaction nor the control infrastructure is
asserted to belong to the native TWIST-J architecture.

## 2. Exact controlled addition from a pair pulse

Set `omega=exp(2 pi i/5)` and fix the Fourier convention

```math
F|y\rangle=\frac1{\sqrt5}\sum_{j=0}^4\omega^{jy}|j\rangle.
```

For a coefficient `k` in `{1,2,3,4}`, apply `H_ij` for

```math
\tau_k=\frac{2\pi k}{5g}>0.
```

The Schrödinger sign and the sign of the Hamiltonian give exactly

```math
D_{ij}^{(k)}
=\exp(-iH_{ij}\tau_k/\hbar)
=\exp(2\pi i kN_iN_j/5),
\qquad
D_{ij}^{(k)}|x,y\rangle=\omega^{kxy}|x,y\rangle.
```

For `k=0`, no interaction pulse is used. Conjugating on the target gives

```math
S_{i\to j}^{(k)}
=(I\otimes F^\dagger)D_{ij}^{(k)}(I\otimes F).
```

Indeed, its coefficient at `|x,z>` is

```math
\frac15\sum_{m=0}^4\omega^{m(y+kx-z)}
=\begin{cases}1,&z=y+kx\pmod5,\\0,&\text{otherwise.}\end{cases}
```

Therefore

```math
\boxed{S_{i\to j}^{(k)}|x,y\rangle=|x,y+kx\pmod5\rangle.}
```

There is no input-dependent phase in this identity. All arithmetic reduction
modulo five comes from the finite Fourier sum; the Hamiltonian eigenvalues
and its time parameter are ordinary real physical-model quantities. Exact
equality holds on the whole 25-dimensional pair space, hence on arbitrary
amplitudes and all pair matrix units, and remains true after tensoring an
untouched reference system.

The durations of the two local Fourier operations must be added to
`tau_k`. They are not zero-duration basis changes in a physical execution.
Using the actual inverse of the implemented Fourier unitary cancels its
global phase in this sandwich. If a separate implementation differs from
that inverse by a global phase, the resulting overall phase is independent
of both input labels and must be retained in the control account.

## 3. The actual routing map A and the affine construction

The entrance routing from P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1 is

```math
A(a,b,c,d,q,r)=(a,b,c,d,q+a+b+c+d+2,r).
```

It is the product of the four additions `a,b,c,d -> q` and the local shift
`X_q^2`, where `X|q>=|q+1 mod5>`. These additions commute with each other
and with the final shift. In the Fourier convention above, one may therefore
combine their diagonal stages:

```math
\boxed{
U_A=F_q^\dagger
\exp\!\left[\frac{2\pi i}{5}
N_q(N_a+N_b+N_c+N_d+2)\right]F_q.
}
```

Identities on all other factors are suppressed. If the four pair couplings
and the local term can be applied simultaneously, the middle stage is one
positive-duration pulse (including the twice-strength local term
`-2 hbar g N_q` as part of this additional simultaneous-control option)

```math
H_A=-\hbar gN_q(N_a+N_b+N_c+N_d+2),
\qquad \tau_A=\frac{2\pi}{5g}.
```

This simultaneous availability is an extra control option, not needed for
existence. With sequential access, use the four commuting pair pulses and
the separately implemented local shift. The full duration includes local
operations and switching in either case. There is no claim of a minimum
physical duration or optimal pulse count.

The other routing map `B` is implemented by the elementary affine operations
listed in [NETLIST.md](NETLIST.md). The present construction supplies the
controlled-addition part of that list; the local shifts and nonzero scalings
are covered by the local-control premise. An exchange of two complete
registers in that list is not a local five-level permutation. It is supplied
by the following four operations in chronological order, using the current
values at each step:

```text
y <- y+x;  x <- x-y;  y <- y+x;  x <- -x.
```

The successive pairs are `(x,x+y)`, `(-y,x+y)`, `(-y,x)`, and `(y,x)`.
Thus an exchange requires three admitted controlled additions, with
coefficients `1,4,1`, and one local negation. No additional two-system
exchange interaction is assumed. These physical control decompositions do
not change the abstract operation counts in NETLIST.md; their constituent
pulse durations must be included in a physical schedule.

The affine equalities of that netlist concern all `5^6` basis states. With
the phase conventions fixed,
their unitary extensions agree on every amplitude, up to at most one known
global phase for the fixed control schedule. No intermediate label is
measured or transferred to an unlisted work register in this ideal
system-only model.

On the four QDD input amplitudes this implies the required sixteen
matrix-unit equalities for these affine gates, not merely agreement of
four populations. It does not assert that a real controller, laser field,
mediator, or environment finishes in an input-independent state. Such
systems have not been included in the model's Hilbert space.

## 4. Explicit scope of the local controls and a primary-source comparison

A sufficient target-independent local family has a connected graph on the
five levels, with the two Hamiltonians

```math
H^x_{jk}=\hbar\Omega(|j\rangle\langle k|+|k\rangle\langle j|),
\qquad
H^y_{jk}=\hbar\Omega(-i|j\rangle\langle k|+i|k\rangle\langle j|)
```

available on each graph edge, with `Omega>0`. Their rotations generate the local special
unitary group. Pairwise rotations eliminate the entries below the diagonal
of any desired local unitary, and relative diagonal phases finish the
construction. The remaining determinant phase is a common global phase.
Hence these controls supply `F`, `F^dagger`, cyclic shifts and nonzero field
scalings up to explicitly accounted global phases. The prescribed pulse
durations are finite when `Omega` is nonzero. This is an admitted control
model, not evidence that the connected graph or its fields exist natively.

Brennen, O'Leary and Bullock give this connected-transition construction and
an exact universality result with an additional selective two-system
interaction. They discuss an eight-level rubidium example, not a verified
five-level implementation of TWIST-J:
[Criteria for Exact Qudit Universality, arXiv:quant-ph/0407223v1](https://arxiv.org/pdf/quant-ph/0407223).
The local control family here has this established mathematical precedent;
its adoption for the present carriers remains conditional.

The selective interaction in that paper also gives a route to the diagonal
pair pulse without independently postulating its full number-product
Hamiltonian. If `-hbar Omega |4,4><4,4|`, with `Omega>0`, and the required local permutations
are available, conjugation supplies each `-hbar Omega |a,b><a,b|`. For each
`a,b` in `{1,2,3,4}`, choose the positive duration

```math
t_{ab}=\frac{2\pi\,[kab]_5}{5\Omega},
```

where `[kab]_5` is the representative in `{1,2,3,4}` for `k!=0`. The sixteen
diagonal pulses commute, and their product is exactly
`D_ij^(k)`. Terms with a zero label require no pulse. Local conjugations
must be executed and included in the duration and phase account. Thus the
pair phase can be assembled from a fixed selective interaction and local
controls, rather than assumed to be an already available QDD operation.

No Hamiltonian approximation, leakage estimate, coherence lifetime,
experimental fidelity, or calibrated numerical time is inferred from the
reference. Those would require a specified device and a separate evidence
record. This probe does not copy the paper's hardware assumptions into the
native architecture.

## 5. A calibration consequence outside the target

The added pair interaction has a testable consequence independent of the
QDD response. For coefficient one, the same controlled addition obeys

```math
S_{i\to j}^{(1)}
\left(\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes|0\rangle\right)
=\frac{|0,0\rangle+|1,1\rangle}{\sqrt2}.
```

This target checks a relative coherence as well as two basis transitions.
It is a possible independent calibration of the admitted pair coupling;
it uses neither the four QDD points nor the fitted LOW/HIGH response. A
physical test would also need independently specified preparation and
measurement operations. No such calibration or experiment has been
performed in this probe. The stated equality is a consequence of the ideal
Hamiltonian model.

## 6. What this supplies and what it leaves open

The construction supplies a finite-duration, source-sensitive interaction
law sufficient for the affine routing, conditional on the declared quantum
carriers, local controls and pair coupling. It explains explicitly how a
field addition can arise from a phase interaction and local interference.
It does not adopt that law as TWIST-J physics.

In particular, none of the following follows from the pulse formulas:

- that the six native checkpoint coordinates are these six physical
  five-level systems, with this tensor product and these available controls;
- that prescribed classical pulse envelopes are produced autonomously by
  the native counter, or that all controlling and mediating systems have
  clean input-independent final states;
- that compensated drift can be assumed for a particular material carrier,
  or that the field-label operator `N` is its physical energy;
- that these nonzero gate durations fit before and between the two native
  ticks at counters three and four, or that native evolution may be paused,
  slowed, inverted or omitted during their implementation;
- that the globally noninvertible native checkpoint map has been given a
  clean unitary realization. The earlier routing theorem only used its
  injective action on particular intermediate code supports;
- that a physical archive, one realized event, an occurrence law, reset or
  repeated preparation has been supplied.

If the controls are included in a closed energy-conserving model, the
conservation result in this probe must be respected. Declaring a classical
drive does not defeat that result; it changes the admitted implementation
class and leaves the drive's full physical accounting to be supplied.
Degenerate encodings or different carrier Hamiltonians are separate
explicit choices, not conclusions from the finite-field notation.

These remaining carrier, time, interaction and environmental obligations
belong to QDD-INSTRUMENT-APPARATUS and the physical-definition lane
[#539](https://github.com/mathorn1973/twist-j/issues/539). No field of that
physical profile is silently marked resolved here. The construction gives
one precisely stated conditional implementation, not a classification of
all apparatuses or a new physical origin theorem.
