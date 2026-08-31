# P-C8-MARKING-RIGIDITY-1, preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**

Issue lock: #729

## Authority pin

At preregistration review:

- authority: Public Canon v72, `mathorn1973/twist-j main`
- public main base: `64055c8a2879668c5bf79eea8cdef067f0ac95a2`
- Canon content commit: `aac8a3a4aff027beb2b08edbde1ae8e59224914c`
- Canon SHA-256: `39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70`

The exact public inputs are the already carried L1 algebra around
`RAMIFIED-TM-LIFT`, `CARRY-PENTAD`, `PENTIT-ROOT-FACTS` and `QUBIT-FROM-F5`,
together with the three merged probes `P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1`
(#716), `P-C8-PHASE-SELECTION-1` (#721) and `P-C8-PAULI-QUOTIENT-TRANSPORT-1`
(#724). The probe does not reopen or strengthen any of them.

## Question

Given the marked datum, is the eighth order of `tau` a choice or a consequence,
and can the remaining orientation debt `J_lambda -> S` versus `J_lambda -> S^-1`
be settled by any observable with rational entries?

## Prior knowledge admitted

The rigidity statement of G2 was found during reconnaissance held in the
private handoff exchange point, not by this probe, and is already believed
true by the reviewing side. What is gated here is the registered exact audit
under the firewalls below, not the discovery. G1 and G4 restate carried facts
as anchors. G6 continues the two use construction of `P-C8-PAULI-QUOTIENT-
TRANSPORT-1` and gates a statement that probe did not make.

## Frozen scope

Six exact gates. All scopes are finite and exhausted exactly.

### G1, the marked datum

In `F_25 = F_5[t]/(t^2 - 2)` with `tau = t`, verify `tau^2 = 2 = J_lambda`,
`tau^4 = -1`, `ord(tau) = 8`, `ord_5(2) = 4`, and that the nonsquares of `F_5`
are exactly `{2, 3}`.

### G2, rigidity of the prime

Claim: let `p` be an odd prime and let `tau` lie in `F_{p^2}` with `tau^2 = 2`
and `ord(tau) = 8`. Then `p = 5`.

The argument is exact and finite. `ord(tau) = 8` gives `ord(tau^2) = 4`, so `2`
has order `4` in `F_p^*`, hence `p` divides `2^4 - 1 = 15` and does not divide
`2^2 - 1 = 3`. The prime divisors of `15` are `{3, 5}` and `ord_3(2) = 2`, so
only `p = 5` survives. Characteristic two is excluded because `F_{2^k}^*` has
odd order and carries no element of order eight.

The gate verifies the divisor argument on its exact finite data and, as a
check on the proof rather than as the proof, confirms by exhaustion that `5`
is the only prime below `20000` with `ord_p(2) = 4`.

### G3, the converse over the pentad

For every `m` in `F_5^*`, collect all square roots of `m` in `F_25` and their
orders. Verify that each `m` has exactly two roots, that both roots of each
nonsquare marking have order exactly `8`, and that no root of a square marking
has order `8`. Hence over `F_5` the C8 level is delivered by a nonsquare
marking and by nothing else; it is not selected among the levels of the
Clifford hierarchy.

### G4, the source side orientation

Verify `2 * 3 = 1` in `F_5`, that the nonsquares are exactly `2` and
`2^-1 = 3`, that `(tau^3)^2 = (tau^7)^2 = 3`, and that `(tau^5)^2 = 2`. So the
orientation reversing maps carry the marked multiplier to its inverse while
the sign branch preserves it, and on the source the orientation choice is
exactly the choice between an element and its inverse.

### G5, the `(Z/8)*` arithmetic

With Frobenius acting on the eighth roots by the exponent `p mod 8 = 5` and
complex conjugation by the exponent `7`, verify that the two exponents are
distinct, that together they generate `(Z/8)*`, and that the resulting group
acts freely and transitively on `{1, 3, 5, 7}`. Record as arithmetic, not as
an available alternative datum, that the exponent `7` is the only unit equal
to conjugation and the exponent `1` the only trivial one.

### G6, the target side orientation no-go

Prepare the pair of `P-C8-PAULI-QUOTIENT-TRANSPORT-1`, apply `T^k` to both
uses for `k = 1` and `k = 7`, and verify:

- the two orientation states are entrywise complex conjugates of each other;
- every expectation value below is rational;
- over all sixteen two use Pauli observables, no observable with rational
  entries takes different values on the two states;
- `XY` and `YX` do separate them, with `+1` at `k = 1` and `-1` at `k = 7`.

By linearity over the real span of the Pauli basis this extends to every
Hermitian observable with rational entries. The underlying reason is stated
here in advance: the expectation of a Hermitian operator is real, and
conjugating the state conjugates the expectation whenever the operator has
real entries, so a real number would have to differ from itself.

The claim is therefore a RELATIVE no-go. Separating the two orientations
requires an observable that already carries an orientation of the target. The
probe does not claim that the orientation is physically empty, and does not
claim that no oriented datum elsewhere can transport one.

## Firewalls

The probe MUST NOT claim any of the following:

- TWIST/J derives quantum mechanics;
- `tau`, `J_lambda`, the carry pentad or any Canon carrier is a physical
  qubit, state, phase, gate or apparatus;
- a Born rule, measurement law, state preparation, decoherence law,
  Hamiltonian or L2 to L6 lift;
- that the marking `J_lambda = 2` is derived; it stays a dictionary input and
  the rigidity is conditional on it;
- that `p = 5` is derived from nothing, or that the pentad is thereby
  explained;
- quantum computational advantage, universality, or any speedup;
- selection of a unique C8 generator orientation;
- that the orientation debt is physically empty, or that it is unpayable by
  transport from an independently oriented object.

Each firewall carries the same frozen action: if the run would support the
excluded reading, the probe is recorded as fired and the reading is not
adopted.

## Method

`verify.py` uses exact residue arithmetic in `F_p` and `F_25`, and exact
rational arithmetic in `Q[z]/(z^4 + 1)`. It contains no floating point,
numerical approximation, network, files, subprocesses, random choice or
external package. The finite scopes are: four residues of `F_5^*` with both
square roots each, the prime divisors of `15`, every prime below `20000`, the
four units of `(Z/8)*` under both involutions, and all sixteen two use Pauli
observables.

## Falsifiers

The probe fires if any exact identity of G1, G3, G4 or G5 fails; if the
divisor argument of G2 admits a prime other than `5`, or the exhaustion below
`20000` returns anything other than `[5]`; if a square marking yields a root of
order eight, or a nonsquare marking yields a root of any other order; if the
two orientation states are not conjugate; if any observable with rational
entries separates them; if `XY` or `YX` fails to separate them with the stated
signs; or if a proof would require a physical premise excluded above.

Failure to derive physical quantum mechanics, and failure to pay the
orientation debt, are outside scope and are not falsifiers.
