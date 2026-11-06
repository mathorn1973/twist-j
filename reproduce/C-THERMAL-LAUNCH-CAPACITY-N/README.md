# Exact audit: finite thermal launch capacity

NON-CANONICAL L1. Design-exposed audit of the self-contained note, not a formal
P-probe or independent confirmation. Read the public pre-execution contract at
notes/C-THERMAL-LAUNCH-CAPACITY-N/PREREG.md and the full analytical PROOF.md.

The standard-library program checks exact capacity allocation, small exhaustive
comparisons, complete seven-qubit reaction matrices, finite reached histories,
negative controls, moments and rational interface margins. The complete device
and the parent's spectral/capture theorems are not simulated by this program.

Run from repository root with Python 3.12 and deterministic settings described
in PREREG. The repository reproduction runner compares exact stdout with the
first committed EXPECTED.txt, requires exit zero and empty stderr, and rejects
changes of scientific bytes. Sources are hashed Git blobs from reachable pins.
