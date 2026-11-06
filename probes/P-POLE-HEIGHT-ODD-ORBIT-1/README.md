# Odd-input obstruction and complete six-slot orbit audit

NON-CANONICAL / L1. Reservation: https://github.com/mathorn1973/twist-j/issues/1897.

The odd inputs (tB,-tB,u,u,0,2), t=-1,+1, cannot reach first four slots
(u+tB,u-tB,0,0) under the integral contact C. Here u=1-j, p=j^2 and B=1-p.
PROOF.md gives a closed-alphabet argument: neutral slots remain zero or a
difference of fifth roots, with Q=0 or 5. The target needs a Q=15 slot.
The same obstruction covers any finite number of additional helpers in
that neutral alphabet, including blanks. Arbitrary neutral stock is not
covered; neither is sufficiency or global minimality of a second charged
helper. "Charged" here denotes arithmetic residue, not electric charge.

This result does not rely on a census count. A prospective exact verifier
separately audits complete six-slot orbits for t=-1,+1, with t=0 as a
positive control. Two arithmetic representations and different traversal
orders must produce the same full sets. Reported review sizes/radii were
known before source authoring and are explicitly exposed, not blind tests.

PREREG.md fixes the audit before execution. PROVENANCE.md and SOURCES.tsv
bind its inputs. The first completed execution will append only
EXPECTED.txt, RUN.md and RESULT.md. Reproducibility and an analytical
candidate do not themselves change Canon status. Sealed PR #1896 remains
its historical bounded non-finding and is not resumed or modified.

The review's switched-action proposal is a separate analytical question.
This probe neither constructs a Hamiltonian gate nor establishes physical
energy exchange, a clock quantum, electron identification or alpha.
