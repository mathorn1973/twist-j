# Finite context for the native raw-residue reader

**NON-CANONICAL. Proof-first, result-exposed, L1 only. Candidate-T.**
Author: A. M. Thorn. Date: 2026-10-12, Europe/Prague.
Reservation: [#1474](https://github.com/mathorn1973/twist-j/issues/1474).
Public basis: Public Canon v101 at
`5f54015ed8361e3a64cb10894397020ddfadd104`.

The unchanged native U and all 625 raw piston inputs, with common receiver
(q,r)=(0,1), are retained. The Canon already reads the original sum modulo
five from the actual counter and current receiver for every n>=3. Its
twenty-valued evaluation summary is not itself an autonomous clock.

This proof-only continuation makes two precisely separated decisions:

| Contract | Analytical result |
|---|---|
| Any finite source-independent context with no input and a fixed current-(q,r) reader | Every eventually permanent function of the original residue is constant. Arbitrary context size, transient, period and nonlinear reader are covered. |
| A finite source-independent context supplied with the exact current Thue-Morse bit at every transition | One explicit total update reads all five residues at every n>=3, with 20 ready contexts and three startup states. |

The negative result uses an explicit binary construction: in any prescribed
time congruence class, arbitrarily late times realize all ten pairs of
Thue-Morse parity and the alternating-floor sum modulo five. The resulting
receiver-support overlap graph is connected. It proves the full class-A
statement, rather than repeating the known ambiguity of one summary.

The positive result replaces repeated evaluation from n by one bit-driven
register update. The exposed driving bit and its timing remain supplied
resources. The context update is an abstract observer and is not asserted
to be invertible or physically implemented. Its 23-state count is an upper
bound; minimality is not proved. A receiver-driven processor that stores
the payload is a third, distinct resource class.

- [CONTRACT.md](CONTRACT.md): complete classes, equality, source bindings,
  resources, adjacent ownership and failure conditions.
- [PROOF.md](PROOF.md): digital lemma, all-finite-context no-go, explicit
  receiver collision and driven construction with startup.

The conclusions were exposed in the authoring discussion before any public
pin. No scientific program, run, finite audit or computational evidence is
part of this package. The written proofs remain candidates pending separate
review and public disposition. Existing scientific verifiers were read only.

No physical instrument, autonomous native clock, material archive, source
erasure, reset, repeated input law, presence/absence mechanism, event,
occurrence measure or higher-layer bridge is supplied. The Canon and all
its open owners remain unchanged.
