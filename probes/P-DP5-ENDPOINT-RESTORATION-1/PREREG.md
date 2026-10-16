# P-DP5-ENDPOINT-RESTORATION-1

**NON-CANONICAL / conditional numerical restoration / action layer L1.**
Owner: A. M. Thorn. Date: 2026-10-13.
Reservation [#1488](https://github.com/mathorn1973/twist-j/issues/1488).
Implementation design reservation: [#1487](https://github.com/mathorn1973/twist-j/issues/1487).

No scientific execution precedes the complete accepted source commit,
public push and exact readback. Compilation and static review are allowed.
This is a new probe. It does not resume or rename the original full campaign.

## 1. Equation

For pairs (0,1),(0,2),(1,2),(3,4),(3,5),(4,5), evaluate

    delta_j = alpha_a,j-alpha_b,j
    theta = Phi_a-Phi_b+Im sum conjugate(alpha_b,j)*alpha_a,j
    Gamma_ret = exp(i theta) sum_r p_r <y_b,r|D(delta)|y_a,r>
    Gamma_linear = exp(i theta) exp(-(11/20) sum_j |delta_j|^2)
    p_r = (20/21)^7 (1/21)^|nu_r|, r=0,...,119.

The finite normal-ordering theorem B1 and coefficient identity B2 in
the predecessor B design are the mathematical source. The retained weights
are unequal and unnormalized. The bra is conjugated. Both coherences use
the same relative Weyl phase. The cutoff is total occupation <=8 on seven
modes, with independently generated graded/recursive-lexicographic basis.

## 2. Code

`restore.py`, `verify.py`, `INPUT_BINDING.json`, `DERIVATION.md`,
`README.md`, `SECURITY.md`, `REVIEW.md` and this preregistration are the complete accepted
source inventory, bound by `SOURCE_SHA256SUMS` and the public commit.
The verifier imports only the adjacent accepted implementation and runs
exact mathematical positive/negative controls; it prints deterministic JSON.
The production entry point is separate and requires the exact clean Git
candidate checkout and a newly created output directory outside both the
source and preserved campaign. Source bytes are rehashed before and after.

Arithmetic is standard-library Python >=3.11, fixed 192-bit directed dyadic
integer intervals. Scalar exponentials use degree 256 exact rational
polynomials and proved remainders. The finite integer-text limit is 32768
digits, not an unlimited conversion. Positive square roots use `isqrt`.
The lowering polynomial precedes the raising polynomial; both are degree 8.
Arrays are fresh at every ladder action. Only exact zero coefficients may
be skipped. No numerical tolerance, nonzero pruning or normalization exists.

## 3. Carrier and data

Original campaign source: `bca348445715c03f4cdc3af6079207024dd40332`.
Preserved first outcome: `6f378a1ba9b39fa1c29188b61a2e6507a92eb9d5`.
Audit source: `9a5c07e140d5781934e026414aa7f7b306b15952`.
Closed campaign final time: exactly 1/2000 seconds.

`INPUT_BINDING.json` binds serialized input, the actual final-custody
receipt and all 16 original source/binary receipt entries. Its frozen
SHA-256 is `d01109396b54296d15535bf8625c800153071f666350fa1e4287ba1e436b15fc`.
The actual preserved serialized input has 3918 bytes, SHA-256
`720f167680bbb51549165a10ba04ce9688de43cc67bb4087cd4ce5be20ebb471`.
This also equals independent decimal-token reconstruction of the original
pinned JSON. The receipt association was read back from the same closed
offline campaign without executing or importing its numerical program.

The five payloads are immutable external inputs, not committed binaries:

| File under full-state | Bytes | SHA-256 |
|---|---:|---|
| basis.json | 103064 | ec66eca09652f6d5d5ee80f7beb592e72bfd31cd71d5a92ba52093d6d7970f61 |
| components.bin | 69120 | 581e371bce1fd72b1abab5f837b4e33786bada00a6e2de14d750542877928c41 |
| endpoints.bin | 74131200 | 7d67034f594bdc923794b61e019c3566b860d6bfe942143ff5c6a06d2b66066f |
| metadata.json | 6773 | 7c2edd7701efad8a2db8af997d97c704a6460b1aeb3487d5503ac0083800fff2 |
| result.json | 312313 | 49940669a1954abaa52a230d1e40d76bc9bc7cef0b6eb395b1c57f10176f3e31 |

The inventory has 2424474 bytes/hash
`b540e5135c5d0b81f7c4e7b5ee8bf0a0ac9f08bf6812b1931b113666a40700c8`;
final-custody 1575 bytes/hash
`ae81c8e940ae2beead4eca379c78b8d07380a573c4a04350e0316f366eed56a6`;
summary 17670 bytes/hash
`ac9348f39112dfb00de47988f79f483b492600f4bfbbc4d8871babec4ded1def`.
These are read-only public mathematical data created under the original
Apache-2.0 source. Remote transport/location is operational context, not
part of the mathematical or public machine identity.

Final endpoints are little-endian interleaved binary64 real/imaginary,
case-major then column-major then basis-major. Every finite bit pattern
is decoded as an exact dyadic before outward rounding, including subnormals.
Nonfinite values, changed hashes, truncation, trailing bytes, changed basis,
boolean/numeric schema impersonation, duplicate JSON keys, wrong case/time
labels, missing columns or invalid thermal enclosures are rejected.

## 4. Systematics and source exposure

The operator identity and old metadata/schema were read. The implementation
is separately authored, not blind to the old mathematical target. No old
module, MPFR routine, displacement code, compiled solver, checkpoint state
or propagation node is imported or executed. Static review in the same
working session is not an independent laboratory reproduction.

Validity of the supplied branch alpha/Phi rectangles remains an explicit
premise. The inherited propagation-error radii and thermal omission remain
separate premises. Components are hash-bound; this probe does not reproduce
their original integration or per-node certification. All binary64 JSON
numeric endpoints denote their exact binary64 values. Parameter dependencies
can widen enclosures and are not phase-fitted away.

The center magnitude is half the magnitude of Gamma_ret-Gamma_linear.
Its exact interval contributes an arithmetic halfwidth once to total radius.
Final distance endpoints expand the center only by numerical+thermal radii.
No second addition of center uncertainty is permitted.

## 5. Failure threshold and bounded outcomes

One production invocation; 600 seconds from source/input hashing through
controls, all 720 overlaps, all 6 pair decisions and final rehash. Six fixed
pair workers, no adaptive precision, retry, resume, subsampling, cutoff
ladder, source repair or propagation. The parent and each worker have a
256-MiB address-space ceiling; seven processes total <=1792MiB, below 2 GiB.
Linux fork adds no resource-tracker helper. SIGALRM/TERM/INT are blocked
only around each fork and registration, then restored; every registered
child is terminated/killed during cleanup. Cleanup and neutral receipt
writing are not scientific computation and may use at most15 additional
seconds under the external invocation supervisor.

The analytic argument domain is |theta.midpoint|+theta.radius<=64 radians
and 0<=x<=64 for the Gaussian and thermal real exponential arguments.
Exceeding the domain is `SCALAR_DOMAIN`, not a phase reduction or retry.
Deadline, memory, worker, input/source custody, schema or control failure
gives `NOT_CERTIFIED`. Partial completed-slot and pair evidence is retained.
The first output and receipts are immutable evidence even on failure.

`CONDITIONAL_RESTORATION_COMPLETE` requires exactly720 distinct pair/column
slots, all 6 pairs, all controls and both custody checks. It means a new
conditional sound enclosure, not a physical PASS. The comparison to each
old rectangle is separately `COVERED` only for whole-new containment,
`CONFLICT` for coordinate disjointness, otherwise `NOT_DECIDED`.

The precision goal is total radius<=1/1000. Discrepancy is `EXCEEDS_TARGET`
if the final lower distance endpoint>1/1000, `WITHIN_TARGET` if its upper
endpoint<=1/1000, otherwise `UNRESOLVED`. All decisions are exact rational
comparisons, and all six outcomes are retained without threshold changes.

Controls freeze: B1/B2 all81 one-mode coefficients in factorial basis;
zero displacement; vacuum/one-excitation matrix elements; nonunit endpoint;
adjoint and branch swap; actual pair-parameter Weyl sign; scalar zero and
understated remainder rejection; a long exact-rational serializer operand;
retained mass, wrong/normalized weights; basis reordering; nonfinite,
subnormal, truncated/trailing binary data; booleans and duplicate JSON keys;
and center-width double-count rejection.

## 6. Action layer and nonclaims

L1 conditional numerical check only. No Canon or registry promotion is
requested. This does not prove preparation of branch parameters, repeat the
old propagation, certify a physical apparatus, or provide the native-to-
classical source/contact bridge. Seven-mode Hilbert endpoints, a rational
wave and the native F5 state remain distinct objects.
