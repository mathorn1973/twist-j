# Occurrence as counting: frozen applicability audit

NON-CANONICAL. Added hypothesis [H], not a derived occurrence law.

[PREREG.md](PREREG.md) freezes the intended experiment, source contract,
known target exposure, and the Gate 0 paper proof. [SOURCES.json](SOURCES.json)
binds four immutable source blobs; [verify_contract.py](verify_contract.py)
checks custody and a manually reviewed typed contract without counting
states, cycles or histories. [REVIEW.md](REVIEW.md) accepts that scope.

The paper conclusion is **STOP_APPLICABILITY / H_NOT_TESTED**: neither the
full forward-clock native U nor #1334's complex operator model supplies the
required finite actual event-counting contract. This is not F of the
hypothesis and does not rule out other actual-state models.

The checker was published and read back at
`f3b59cc08efce600957676fbce6d17b31ab9aa11`, then ran once with exit zero,
empty stderr and a 342-byte custody report. [RUN.md](RUN.md) records the
execution; [EXPECTED.txt](EXPECTED.txt) retains its actual output and
[RESULT.md](RESULT.md) gives the final disposition. No cycle counting or
trace-weight comparison ran. No further apparatus was introduced to avoid
this stop; the occurrence hypothesis remains untested.
