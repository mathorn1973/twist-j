# Quadratic polynomial readers and initialized memory for fixed L5

This is a supplemental exact audit of the independently proved inline L1
statements QUADRATIC-COUPLED-POLYNOMIAL-CLASS,
FINITE-READOUT-INITIALIZED-MEMORY,
QUADRATIC-L5-FULL-DOMAIN-OBSTRUCTION, and
QUADRATIC-L5-INITIALIZED-CAPACITY in canon/CANON.md, under
DEF-QUADRATIC-MEMORY-L5. The mathematical proofs are the theorem evidence.

The calculation originated as exploratory candidate-C work. This directory
does not constitute a formal probe, preregistration, retrospective
preregistration, or independent native realization. EXPECTED.txt records the
deterministic successful audit output; it is not a preregistered prediction.

Run from the repository root:

~~~text
python reproduce/quadratic-memory-l5/verify.py
~~~

Use Python 3.8 or later without -O; assertions are part of the verifier.
Only the Python standard library is used. The script reads no input files,
writes no files, makes no network calls, and emits deterministic UTF-8 stdout
with LF newlines on every platform. Exit status must be zero, stderr empty,
and stdout byte-for-byte identical to EXPECTED.txt; no newline normalization
is admitted in this comparison.

The named inputs are:

~~~text
L5_W = ((3,3,2), (3,4,2), (3,2,0))
B_W_FROM_GRAM = ((1,4,2), (4,0,1), (3,4,4))
M_GRAM = ((0,3,0), (4,4,4), (0,3,3))
~~~

The fixed L5 is a declared mathematical target, not a derived physical or
native Hodge step. The script checks the marked conjugacy, all 234 quadratic
polynomial coefficients under the two slot transvections (equation rank 213,
explicit solution dimension 21), the scalar quadratic-rank certificate,
all 15 target orbits, all 1500 Gram-fiber counts by both coordinate
convolution and independent closed formulas, exact one-step and indefinite
memory capacities, and minimum reachable-domain sizes.

The complete data domain is F5^6 x F5^6. A symmetric source matrix C is fixed
independently; its rank and nondegenerate determinant square class index the
12 rows. Initialized memory means that the readout equation is required
along every trajectory starting in X x {a0}. Requiring it on all X x A is a
different contract and remains obstructed for every nonzero C.

The exact two-state capacity at ranks four through six concerns arbitrary
global permutations. It neither selects C nor supplies a native contact,
controller, gate compilation, preparation mechanism, or physical time.
