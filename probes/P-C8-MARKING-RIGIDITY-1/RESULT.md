# P-C8-MARKING-RIGIDITY-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED.

## Recorded decision

    verdict: 6/6 ALL PASS
    exit: 0
    stderr: empty
    stdout: 709 bytes, 7 lines; identical to EXPECTED.txt

Both required architecture legs replayed the frozen verifier from a clean
checkout in workflow run 33388842864 and both reproduced EXPECTED.txt exactly:
architecture-x86_64 SUCCESS, architecture-aarch64 SUCCESS, the aggregate check
SUCCESS, publication correctly skipped. The local leg is aarch64, so the run
record carries two distinct architectures.

No frozen falsifier fired. The negative statement in G6 is a proved boundary,
not a failure of the probe. The universal arguments live in the immutable
PREREG.md; the verifier audits their finite field, order, exponent and
operator-basis ingredients.

## Earned mathematical scope

**Rigidity of the prime.** Conditional on the marking J_lambda = 2 and on the
eighth order of tau, the residue prime is not a choice. Order eight forces
ord_p(2) = 4, hence p divides 15 and does not divide 3, hence p = 5. The
exhaustion below 20000 returned exactly one prime and is a check on that
argument, not the argument.

**The layer is delivered, not selected.** Over F_5 each nonzero residue has
exactly two square roots in F_25. Both roots of each nonsquare have order
exactly 8, and no root of a square has order 8. The C8 level of the phase
tower therefore follows from a nonsquare marking, and under that marking no
other level is available. Order eight is a consequence of the pentad plus the
marking, not a selection among the levels of the Clifford hierarchy.

**The orientation read on the source.** The nonsquares of F_5 are exactly 2
and its inverse 3. The orientation reversing maps carry the marked multiplier
to its inverse while the sign branch preserves it, since (tau^3)^2 and
(tau^7)^2 are 3 while (tau^5)^2 is 2. The open orientation debt is therefore
the choice between an element and its inverse, stated on the source side.

**Relative no-go on the target side.** The two orientation states of the two
use construction are entrywise complex conjugates. Across all sixteen two use
Pauli observables, no observable with rational entries takes different values
on them, while XY and YX separate them with plus one at k = 1 and minus one at
k = 7. Both separating observables carry i. By linearity over the real span of
the Pauli basis the statement extends to every Hermitian observable with
rational entries. Separating the two orientations requires an observable that
already carries an orientation of the target.

## Boundaries

The marking J_lambda = 2 is not derived and remains a dictionary input; the
rigidity is conditional on it, and nothing here explains the pentad. No
derivation of quantum mechanics, no identification of any carrier as a
physical qubit, state, phase, gate or apparatus, no Born rule or measurement
law, no transport of a Born norm, no advantage and no universality. The G6
no-go is relative to observables with rational entries. It does not claim that
the orientation is physically empty, and it does not exclude paying the debt
by transport from an independently oriented object.

## Prior knowledge

The rigidity statement was found during reconnaissance held in the private
handoff exchange point and was recorded there before this probe was
preregistered. What this record adds is the registered exact audit under the
frozen firewalls, not the discovery. One authoring defect, a set compared
against a list in the G5 orbit check, was found and corrected before the pin
and before any execution; it is recorded in the public lock.
