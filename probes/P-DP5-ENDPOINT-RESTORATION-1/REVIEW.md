# Pre-execution source review

**NON-CANONICAL / conditional L1 / static review, not a numerical result.**
Date: 2026-10-13. Same-session review by a separate reviewing agent.

No unresolved source-review blocker was found for the declared public pin,
exact controls and one bounded production invocation. This decision is
conditional on committing and publicly reading back these exact sources,
forming their complete `SOURCE_SHA256SUMS`, and observing `PREREG.md`.
It does not assert that the controls pass or that production finishes.
Neither the reviewer nor this review imported or executed the implementation,
its controls, endpoint restoration or historical numerical programs.

## Reviewed bytes

All paths below are relative to this probe directory. The source manifest
must additionally bind this review; it need not and must not hash itself.

| File | Bytes | SHA-256 |
|---|---:|---|
| restore.py | 38413 | a3c1afc635dbde338fc7462f71dd8b999700ee5a2af62945c5c53b22a0118cc5 |
| verify.py | 1098 | 49d2000bbb6ed2dc1e2c2c0a6f68c6bd4463b42ddf8bcf411d5415101a6e0820 |
| INPUT_BINDING.json | 2041 | d01109396b54296d15535bf8625c800153071f666350fa1e4287ba1e436b15fc |
| PREREG.md | 8574 | 334bbab9ed6c91b4d9aba0d59d29e99dfafd5f2c314ba3a8198247994ca2ab38 |
| README.md | 2491 | e95738d157677d5a959d39a1fa662325e819eae71488d66bf8769cbdf054863a |
| DERIVATION.md | 6836 | 368691338a50bca1497b8aeef850c4fa0688f5c841c35cfde6a4f588968d325a |
| SECURITY.md | 2083 | 5e767e090a8f40734902056d8728093da04fd8a9e2eeda73a4b100e4e925a5b9 |

## Mathematical assessment

The directed integer-grid operations enclose addition, subtraction,
multiplication, rational scaling, squaring and positive square roots.
Signed operands, exact zeros and binary64 subnormals are handled without
tolerance-based removal. Complex multiplication uses real interval extrema;
the inner product conjugates its bra. Shared-parameter dependence may widen
the result but does not invalidate containment.

The lowering polynomial acts first. Lowering cannot leave total degree
eight; later raising cannot return after leaving it. Consequently the two
degree-eight polynomials, with their stated Gaussian factor, give the exact
projected displacement matrix element for arbitrary stored vectors. There
is no omitted displacement Taylor tail. The independent factorial-basis
coefficient specification has the correct downward coefficient n and upward
coefficient one, including its n! coefficient prefactor.

The scalar polynomial remainders and the argument-radius additions are
valid on the frozen real-path domains. Intersections with the analytic
ranges [-1,1] or [0,1] preserve enclosure. The finite 32768-digit conversion
limit covers the guarded rational remainder records; a near-unit operand
with denominator 2^192 exercises this otherwise nontrivial conversion path.

The parameter construction uses delta=alpha_a-alpha_b and the relative
phase Phi_a-Phi_b+Im(conjugate(alpha_b)*alpha_a). The synthetic nonzero Weyl
phase control exercises this construction itself, including the branch
swap. The exact unequal, unnormalized thermal weights and the 11/20 linear
exponent match the declared target. The shared weight validator has both
positive and negative controls.

Whole-new-rectangle containment is compared against exact original
binary64 endpoints, without first widening the old box. Disjointness and
undecided overlap are separate outcomes. The witness-center interval is
expanded only by the inherited numerical and thermal radii; its arithmetic
halfwidth appears once in the reported total radius. Precision and
discrepancy use distinct exact rational decisions.

## Execution and custody assessment

The complete payload hashes bind the case/column/basis layout, while the
independently generated basis, six cases, 120 columns, common final time,
weights and metadata receive explicit validation. The serialized input is
checked against its actual final-custody receipt and internally pinned
source-binding object. This review checked the validation code and declared
receipts; it does not replace the runtime rehash of the preserved campaign.

Success requires all 720 distinct overlap slots, all six pair results,
successful controls, normal worker exits and final source/input rehash.
An exception explicitly resets all overall success fields. Partial pair
records cannot imply complete restoration. No precision adaptation,
column subsampling, propagation, normalization or phase fitting is present.

The parent and six fork workers each have a 256-MiB address-space limit,
including inherited limits during startup: 1792 MiB in total for this
process set. Fork and registration block the relevant signals together,
and children restore termination handling before computation. The internal
600-second deadline and documented process-group supervisor have distinct
roles; at most 15 additional seconds are reserved for cleanup and neutral
receipt writing. Completion inside the cap remains unmeasured.

The only subprocess operations in the implementation are fixed read-only
Git checks. Inputs are not executable code. The accepted command isolates
imports and disables bytecode writes. The output directory must be new and
outside both input campaign and checkout; result files use exclusive
creation. General OS exception text is excluded from public scientific
failure records to avoid exposing transport paths. The source contains no
network access, historical numerical import or source/input mutation.

## Limits of this review and any later result

The reviewer saw the public mathematical target, candidate implementation,
metadata contract and custody hashes and exchanged findings with its author.
This is exposed same-session review, not blind implementation or independent
laboratory replication. Mathematical source inspection is not an executed
control or a proof of implementation correctness for every possible input.

The supplied branch alpha/Phi intervals and inherited propagated-vector
error account remain premises. `components.bin` is hash-bound, not independently
reintegrated. A successful restoration would establish new conditional
enclosures at this exact endpoint scope; it would not validate the original
parameter preparation or complete trajectory. The repository verifier and
architecture jobs execute mathematical controls only, not the external-data
production restoration. No native source/contact realization, physical
apparatus, experiment or Canon promotion follows from this review.
