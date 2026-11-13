# Closed light-shift model: actual second-contact boundary

PUBLIC; NON-CANONICAL; L1. Reservation [#1360](https://github.com/mathorn1973/twist-j/issues/1360).

This probe examines one concrete restricted effective calcium-ion model for
the second trace contact. It directly encodes the original coordinates,
derives completed-loop operations from a documented light-shift Hamiltonian,
and tests whether the resulting common-control class can execute the ordered
port transition (s,0)->(4,s+1) for every original history.

The analytical candidate is negative: identical port dictionaries and
swap-symmetric completed control cannot send |00> to |41> with unconditional
success above 1/2. Arbitrary inherited auxiliary states do not remove this
bound. This is not an exclusion of individually addressed ions, unequal
fixed dictionaries, unclosed pulse control or a combined native/contact step.

- [MODEL.md](MODEL.md): physical levels, Hamiltonian, control class and limits.
- [PROOF.md](PROOF.md): continuous-time closed-loop derivation and exact bound.
- [SOURCES.md](SOURCES.md): primary physical and accepted mathematical sources.
- [PREREG.md](PREREG.md): frozen target, tests, error metric and execution rules.
- [REVIEW-PREREG.md](REVIEW-PREREG.md): independent pre-execution review.

The verifier is an exact finite audit of the proof and stored source interface;
it is not a fourteen-ion simulation or hardware experiment. It also audits the
history capacity and symbolic endpoint energies needed to avoid hidden resets
or reusing an incompatible energy ledger. See RESULT.md and RUN.md only once
an actual accepted execution has produced them.

The public basis is main `2973a432303e046aacb2cee3cea97254ea3ab8eb`, Canon v97.
The separate open #1359 audit remains at
`8f43a051e3dba8cc4ed17d379ad8e11b57101591`; its HOLD and missing complete
physical certificate are not discharged. Existing ion writer #1091 and
contact/history owners #987/#993/#994/#996/#998/#1003/#1333/#1349/#1353/#1356/#1358
retain their scopes.

Administrative preflight inspected 196 live remote heads and 1230 selected
changed-document occurrences, reused historical issue/comment snapshots only
as historical evidence, and read a fresh paginated delta. It found no exact
new-identifier collision. Both architecture jobs and main check were green.
This bounded scan does not claim to inspect inaccessible laboratory records
or every code/binary byte. Original text and code: Apache-2.0.
