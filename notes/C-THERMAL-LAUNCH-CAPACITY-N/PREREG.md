# Prospective exact-audit contract

**NON-CANONICAL L1, design-exposed analytical candidate; not a formal P-probe.**
Claim #1760. Source authority is main/canon-v105 at
892a0b11089d34e241e1eb76d2c03247022d18e6. Parent candidate #1758 is fixed at
243379459e3c7493368473cbae1a17eb99ee8316 and is not independently accepted here.
The owner is A. M. Thorn / ChatGPT-finite-cycle-analysis-20261024.

Scope and code will be committed, pushed and read back BEFORE the first audit.
Before that pin only static syntax and file-custody checks are permitted.
No scientific executable has been run while writing this contract. The proposed
q1=4/15, q2=7/15, ten swaps, guard and energy moments were derived analytically
and are design-exposed; their audit is not a blind confirmation.

## Frozen carrier, equations and assertions

Use exactly PROOF.md sections 1-7 and verify.py as frozen together. Integer and
Fraction arithmetic only. The launch target is two charged registers |11> from
initial |00>, without extra changed workspace in the optimization class.
The general capacity uses bath dimensions from (1+x)^N(1+x^3)^N and sorted
individual weights 2^(3N-a-2b)/15^N. The fixed table is N=1,...,32; exhaustive
configuration comparison is N=1,...,6. No desired large-N threshold is stipulated
and no asymptotic or local-large-N conclusion may be inferred from this table.

The two-pair partial isometry has exactly the ten rows in PROOF. Its autonomous
replacement includes the existing last-loader guard on hopping, its positive
diagonal edge and the initial vertex potential. Check all 128 seven-qubit raw
basis inputs, inverse/energy/Hermitian/positive-polynomial identities. The
wrong-hot-gap and unguarded-relaunch controls must FAIL the corresponding
scientific property and be recorded as expected negative examples.

Audit all reached paths and all six inactive initialized bath words for loader
lengths 2,3,5, including every forward/reverse edge and vertex potential.
These finite examples do not substitute for the arbitrary-L proof. The audit
of logical matrix units is explicitly a small tensor-spectator algebra check,
not simulation of the inherited full accepted instrument.

Check the exact bath moments, covariance, transferred energy and source/read
rational margins stated in the proof. Preparation/read-output claims remain
conditional on the parent clock and inherited source/filter proofs. No state
weight is relabeled as empirical occurrence. No new reading-layer lift.

## Systematics and failures

Fixed basis order: h1,c1,h2,c2,s,t0,ell for the seven-site check. Bath lexicographic
order and the displayed chosen tied E=4 input are frozen. The six failure bath
words and every rejected/cursor history remain present. Units use epsilon and
g symbolically; the program checks their rational coefficients, not decimals.

A failed exact assertion gives nonzero exit and preserved stdout/stderr plus
an explicit disposition; it is never overwritten into PASS. No retry with
changed scientific input, threshold, mapping or guard under this same pin.
An infrastructure failure is distinguished from an exact counterexample. Any
successor code would need a new pre-execution pin and retained predecessors.

## Run and output contract

From a clean tree on Linux with Python 3.12 use the repository deterministic
settings LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC,
then run python3 reproduce/C-THERMAL-LAUNCH-CAPACITY-N/verify.py, timeout 120 s.
Record the actual first stdout as EXPECTED.txt and the command, platform,
architecture, exit, byte counts, hashes and public pin in RUN.md. Zero exit and
empty stderr are required. Subsequent same-code runs are reproductions only.
Use tools/check_reproduce.py for repository replay and the unchanged required
x86_64/aarch64 workflow; same bytes do not imply independent implementation or
mathematical acceptance. No new workflow or Canon files are authorized.

Only a new notes directory and its minimal reproduce directory are in scope.
Deliver a draft PR and PROMO scope to separate review. Native compilation,
physical preparation, repeated operation, reset and occurrence stay open.
