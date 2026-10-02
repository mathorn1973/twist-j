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

The checker has not run. Publish the unchanged preregistration, manifest
and code, record/read back their public pin, then execute the documented
command once and retain its real output. No RUN or EXPECTED is fabricated
before execution. No further apparatus is introduced to avoid this stop.
