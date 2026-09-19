# Independent implementation contract: native point-port capacity

**PREREGISTERED, RESULT-EXPOSED, AUTHOR-CODE-BLIND CONSTRUCTION.**
Reviewer: A. M. Thorn / Codex-scope-review-20260919.
No scientific execution is reported in this pre-execution contract.

## Frozen input, code and exposure

The reviewer read the final formal PREREG.md mathematical statement,
SHA-256 `03525a9e8d833ef77ccbe414158188ee48d48cb36f006eb806183ea8734423d2`,
the earlier exposed editorial proposal and statement drafts, and the
inherited public native quotient proof and Canon definitions. Target
weights and constants were known. Neither incubation audit.py nor the
new author verify.py or new author PROOF.md was read before the following
independent code was locally frozen:

```text
file: BREAKER.py
sha256: 4f038471633689013c63fa477d28284247011528b3e789dca9b40c107de9e3b0
```

The implementation uses only Python standard-library exact integers and
Fractions. Its syntax was checked with ast.parse without importing or
executing it. No author code/output comparison occurred before this code
freeze. Result exposure forbids describing this as a blind prediction.

## Exact attack and acceptance targets

1. Check the native-to-quotient commuting identity for each of the five
   public generators on every six-coordinate checkpoint, and both selector
   bits. The complete finite identity supports the independent all-time
   induction; a bounded history is not substituted for that induction.
2. Independently compute the exact coefficient table of
   `(sum_(v=-2)^2 X^v Y^(v*v))^4` by four coefficient convolutions. Its
   `(s,N)` coefficients count every ordered balanced source. Remove only
   coefficient `(0,0)` and push the others through the original beta
   formula. Compare this with separate direct field-label enumeration and
   the full 22-value preregistered table. Require 624 supported sources,
   exactly 120 with beta>5/32, and no beta value at zero.
3. Check the six original-source obstruction values and six distinct
   sharp-packing values. Independently solve the complete one-dimensional
   five-interval partition by considering every cut of the sorted attained
   values. Require diameter 9/64, equivalent to minimax error 9/128.
4. Build the free encoder from the five frozen target-cover intervals,
   check every source assignment and exact error, and verify the common
   ready (0,1) separates all five sums at its first observation. Check
   rational thresholds can be represented by one supplied finite seed.
5. Construct and check all five sorted faithful assignments with the
   124-supported-member block at each possible position. Require full
   625-label bijections, exact error 27/64, the stated endpoint/center
   certificate for the selected first placement, and the null sharing its
   sum with exactly 124 supported originals.

The check has no tolerance, stochastic search, external input, execution
of author code, or physical randomness assumption. Any assertion failure,
exception, nonzero exit, stderr, timeout or later byte mismatch fails this
audit. Preserve the failure; do not modify the public pin to hide it.

## Independent reasoning beyond the finite check

For one fixed common seed, equal sums of f(p) have equal initial quotients.
The commuting identity and common driver imply equal quotient histories
at every tick. A common deterministic processor of equal inputs has equal
complete responses, including stopping and memory resets. Integrating
over the same source-independent seed law preserves this equality.
Conditioning on the same fixed completion event preserves it wherever
completion has positive probability. Thus there are at most five laws.
The six distinct original targets exclude complete exact response.

For free encoders the six packing values have adjacent separation at least
9/64, so radius below 9/128 cannot cover them with five centers. The five
frozen intervals have diameter at most 9/64; exact exhaustive target
membership and the realized sum assignment give the matching upper bound.
Alternatively nearest-center assignment makes any one-dimensional cover
contiguous, which justifies the independent dynamic program.

For a permutation every sum fibre has 125 labels. The fibre containing a
beta=1 source has at least 124 supported sources, while only 120 originals
have beta>5/32. That fibre therefore contains a beta<=5/32 original.
Its response error is at least half the spread 27/32, namely 27/64.
The checked full bijections supply attainment. Independently the null's
fibre also contains 124 supported originals, so its support tag cannot be
recovered through this port. Failure is limited to the frozen point-port
class; it creates no physical apparatus F verdict.

## Public pin and execution

Freeze this contract and the exact BREAKER.py above in the same public
pre-execution commit as PREREG.md and the author verifier. Read back the
public bytes before running either implementation. The lane owns the
commit, runner, result records and required architecture checks.

API: `check()` returns one deterministic string and prints nothing.
Standalone `python3 probes/P-QDD-NATIVE-POINT-PORT-CAPACITY-1/BREAKER.py`
prints that returned string and a newline. The author verifier includes
the return value in its fixed JSON output, so both required architecture
jobs execute the unchanged independent implementation. The successful
standalone line is fixed here, not asserted to have been observed:

```text
INDEPENDENT_BREAKER_A PASS sources=624 weights=22 high=120 free=9/128 faithful=27/64
```

Use the same Linux-compatible environment and existing 600-second process
limit as the formal probe. After the public pin, preserve the first
standalone stdout as BREAKER-EXPECTED.txt and record its command, exact
hashes, environment, exit and empty/nonempty stderr in the review record.
Combined required replay compares the complete author-plus-breaker stdout
against the one committed EXPECTED.txt. Independent construction and
independent mathematical reasoning are distinguished from reproduction.
