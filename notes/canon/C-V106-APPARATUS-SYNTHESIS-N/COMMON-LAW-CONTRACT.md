# Draft common-law research contract

**NON-CANONICAL / L1 / UNFILLED RESEARCH CONTRACT.**
Author: A. M. Thorn <thorn@twistj.com>. Apache-2.0.

This is a specific continuation target for the v106 synthesis, not a claim
that the target has been constructed. It does not freeze a scientific
experiment, select new numerical parameters or authorize a formal run.
A successor must reserve its own identifier, complete the missing model
data and pin its verifier before any formal computation.

## 1. First target and carrier

Start with the original-port active-source and occupied-memory family of
#1777. Retain both phase choices, every allowed unknown old memory and
passive reference, and both successful and unsuccessful output branches.
The preparation and the three spatial steps already have a common supplied
apparatus; do not replace that result by an unrelated abstract circuit.

The successor must publish one full carrier

```text
H_carrier = H_data tensor H_memory tensor H_store tensor H_clock tensor H_aux,
```

or an explicit constrained subspace with a full-space extension. It must
give a physical graph, local factor dimensions, all ready states and a
single linear isometric embedding J on a stated logical carrier K. This
carrier must contain every tested source vector psi, every Q psi used in
the energy comparison, and every W^n psi used up to the chosen horizon;
passive references are handled by tensoring J with their identity. If a
finite compression replaces K, its leakage outside the retained subspace
must be explicitly bounded and included in the error, not silently dropped.
The source cannot
encode a precomputed answer, and the ready auxiliary state must be the same
for both source choices except for the explicitly named setting register.
The arbitrary old memory may be entangled with a passive reference.

The target word W is the complete preparation-and-record transformation,
including failure sectors. It is not the conditional normalized successful
branch alone. Exact reset of a working register may export its information
to named stores; it may not erase that information from the full carrier.

## 2. One law and two separately named energy requirements

Supply one time-independent self-adjoint generator

```text
H_tot >= 0,       H_tot = sum_X h_X,
```

with a declared bound on support size, physical diameter, strength and
incidence. These are four different locality/resource requirements.
The law includes the clock and contacts. Externally timed gates are not
part of the solution unless a separate controller and its energy are
included in this same carrier and generator.

Specify a second operator A for any proposed additive system/store account.
Prove [H_tot,A]=0 on the full admitted domain if exact conservation of A is
claimed. Also state H_tot itself and its preparation energy. Calling A
energy does not identify it with H_tot, and a constant A on the active
shell cannot by itself generate W.

If the original spectral energy Q=E0 f(U_rec) is retained as a physical
target, freeze its branch f and the exact comparison map. A possible
source-restricted requirement is

```text
sup_psi || H_eff J psi - J Q psi || <= E0/1200,
```

over normalized vectors in the complete declared source/memory/reference
family, with H_eff explicitly derived from the same apparatus terms and
energy-reading operation, and with its domain stated.
The existing tolerance is a comparison target, not a newly run test.
H_eff cannot simply be renamed from the old occupation charge. If the
successor chooses a different energy, it must say so and cannot claim
to have discharged this original-Q requirement.

The bare occupation class with physical term diameter at most two already
has the scoped obstruction in #1791. The successor must either use a
different precisely stated class or give a genuine correction to that
result. Diameter three is not known to suffice. Introducing a dressed
encoding requires its physical preparation, locality and readout maps too.

## 3. State-level motion and recording target

For each fixed finite N and error epsilon>0, publish the resource choices
before assessing the construction. A useful strong motion requirement is

```text
sup_(psi,R) || exp(-i n tau H_tot/hbar) J psi
               - J_n (W^n tensor I_R) psi || <= epsilon,
                    0 <= n <= N,
```

where psi is normalized, the norm is the joint-vector norm for pure dilated
inputs, R is an arbitrary passive reference, and each J_n contains the
explicitly accounted clock, store and archive state. The linear isometries
J_n and their record/readout meaning must be specified from the declared
resources before comparing with the actual evolution; defining J_n by
conjugating the desired output with that evolution would make the test
empty. If mixed inputs or channels are primary,
replace this by a fully specified trace-distance/channel criterion.
Neither J_n nor discarded auxiliaries may hide a second unaccounted
preparation, a chosen measurement outcome or an erased old record.

The successor may first solve N=1 with the occupied-memory interface, but
must label that as the one-attempt result. To claim reuse, prescribe N=2
on the same carrier with the same generator, retain the first archive,
and account for the fresh stores needed by the second attempt.

Publish local pointer effects, the time/readiness rule, and the full
unconditioned outcome probabilities. The phase-dependent record contrast
should survive the combined preparation, clock and pointer errors with
a strictly positive explicit lower bound, preferably the existing 1/100
comparison when the same source family and convention are retained.
If a Lüders operation is assumed, leave its physical occurrence and
implementation outside the theorem rather than claiming they are derived.

## 4. A concrete conditional construction route

The immediate mathematical bridge is to find local bounded generators
G_j for the funded complete word W on the chosen carrier, satisfying

```text
W = product_j exp(-i G_j),        [A,G_j]=0.
```

This is missing model data, not an established factorization. The
finite-rotor technique then suggests a candidate with clock-only quadratic
kinetic term and bounded local program G(phi). A valid continuation must
prove its own finite-compression error and confirm that compression
preserves [A,H_tot]=0 because A acts on the non-clock factors. Positivity,
locality, uniformity over references and all clock preparation costs must
be checked on this carrier, not inherited from matching notation.

Even a successful construction on this route proves only that A is
conserved while H_tot generates the motion. Equality with the selected
original Q remains the separate requirement in Section 2. The single-walk
rotor model #1795 and the two-walk sharp-store model #1793 are not already
such a factorization on a common carrier.

The concurrent #1804 candidate, pinned in SOURCE-ACCEPTANCE.tsv, now gives
a finite coherent conserving lift on the same contact sector as #1793,
with an explicit approximation bound and a positive static controller for
one nominated time. It remains pending public acceptance. Its spectral
couplings and coherent preparation are supplied; no local repeated
realization on the original-port carrier follows. Its strict
coincidence-support obstruction is a concrete constraint on that narrow
interaction class, not an exclusion of every finite-range construction.
Thus it advances the contact-source interface without filling the local
G_j or shared-carrier requirements above.

## 5. Decisive failure witnesses

The proposed common-law claim fails at its frozen scope if any admitted
input yields a wrong full output, an uncounted source/clock phase, a
violated energy identity, support outside the declared graph bounds, an
error beyond the chosen horizon budget, loss of the first archive during
reuse, or a nonphysical identification of a supplied read operation with
an occurrence law. A failed route narrows that route; it does not exclude
every possible local apparatus or every admissible reading of TWIST-J.

What must be delivered next is therefore explicit: the carrier and J,
the complete W, local G_j, H_tot and A, one common prepared family, local
pointer effects, a full energy/resource account, and uniform error bounds.
Until those objects are fixed there is no executable experiment to run.
