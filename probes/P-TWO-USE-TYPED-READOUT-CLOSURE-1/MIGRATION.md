# Source-derived migration and pre-pin review

NON-CANONICAL / L1. A. M. Thorn. Owner has read both I2/V2 code and results.
No independent authorship or blind confirmation is asserted.

I2 source pin06d63ae94f609cc54989e410e3c778ce147d22c5 and result
dac92207c11abb061c10fa4ab729e3789d9cbf85 remain unchanged. apparatus.py and verify.py are reused from that
result; DOMAIN.tsv is copied exactly. V2 PROOF at
6bde80a542df28dd8872173e2fea2460f2a816a2 is copied unchanged as SOURCE_PROOF.md.
SOURCES.tsv gives exact original paths, hashes and byte counts. REUSE.diff
is the complete code migration, including documentation and output changes.

Only two old top-level engine nodes change: DirectPortReadout defaults become
unknown, and direct_source_reader is replaced with a typed wrapper. Its exact
numeric body is moved to the separately named decode_port_vectors, with no
source dependence. All70 other old top-level functions/classes have identical
ASTs, including every dynamical primitive, state, inverse, preparation,
extractor and serialization. New tests make no physical-provenance claim.

Tests T01-T10,T12-T15,T17-T18 have identical ASTs. T11 checks the new single
record argument, preserving every forbidden specimen and its read/chronology
coverage. T16 explicitly implements its formerly only advertised five-run
rank-one subclass check, retaining the seven-run targets. NewT19 covers
unknown context, valid integer Q4, malformed tags and450 readout cases.
Default verifier now enforces dependency custody before import, reports a
controlled scientific failure, includesT19 and the exposedv2 digest. Witness
and test science use their original formulas, source families and thresholds.

Pre-pin algebra review finds no further inconsistency in the previously
unexecutedT12-T18 against the specified source equations. This is a static
review, NOT a scientific run or predeclared PASS. All arithmetic execution
waits for pin/readback. Standard-library imports only, no network/subprocess,
private files or copied user paths in science. Fixed loop bounds remain within
the existing600-second verifier limit subject to actual run. Negative results
will be preserved; no unpinned trial or performance adjustment is allowed.

Unsupported I2 PROMO statements (alternate geometry name/path, port partitions,
G1-G12,60x60/50x50/100x100/symplectic claims) are excluded. The I2 raw private
traceback and its administrative descriptions are not copied as new evidence.
Independent V2 PASS/reference digest and the I2 stopped default run remain
separate statuses. New software type conformance is not native contact admission.
