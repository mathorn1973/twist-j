# RESULT: P-J-HODGE-SEMILINEAR-MEMORY-1

Status: ABANDONED.

The public three-file preregistration pin is
`747f189cc532c61d13e0fc097c7b5989e34f754a`.

The first formal execution started only after public readback of PREREG.md,
PROOF.md and verify.py. It exited nonzero before producing any exact scientific
stdout. The failure occurred in the G7 coordinate certificate: the frozen
deterministic rational primary vector gives a valid sigma-conjugate Hodge basis,
but its off-diagonal boost coefficients have product 5/4 without individually
having the additionally asserted normalization magnitude sqrt(5)/2. The
verifier therefore raised AssertionError before printing stdout.

This is a verifier/basis-normalization defect, not a scientific falsifier of
G1-G6 or of the intended semilinear-memory theorem. No EXPECTED.txt and no
RUN.md exist or may be added.

Under POLICY.md the identifier P-J-HODGE-SEMILINEAR-MEMORY-1 is consumed and
must not be reused, renamed or resumed. Any successor must use a new identifier,
cite this abandoned predecessor, and freeze its primary-basis normalization
before its own pin.
