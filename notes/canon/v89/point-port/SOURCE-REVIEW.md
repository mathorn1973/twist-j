# Point-port intake: custody and static scientific review

**NON-CANONICAL preparation review, 2026-09-19. No formal run or promotion.**

## Accepted source and checks actually performed

Read public [issue #1036](https://github.com/mathorn1973/twist-j/issues/1036)
and its two comments: source freeze
[`5732706048`](https://github.com/mathorn1973/twist-j/issues/1036#issuecomment-5732706048)
and accepted result/custody
[`5732811087`](https://github.com/mathorn1973/twist-j/issues/1036#issuecomment-5732811087).
Recovered the accepted Git tree and all eight blobs through read-only GitHub
Git object API calls. The object tree is complete (`truncated=false`).
The local byte count and Git blob SHA-1 matched for each file. Every one of
the seven manifest entries also matched its SHA-256. Reconstructed the
binary Git tree encoding `100644 path NUL raw_blob_sha1` in Git order and
hashed the tree header plus payload: exactly
`462e9721ad4b9f60f2df6c98715b0bfcc1976425`.

| Source file | Bytes | Git blob |
| --- | ---: | --- |
| MANIFEST.json | 2441 | `b87ed19cf41aac52966ebf1913299dc190ee0b38` |
| PREREG_REFERENCE.md | 1305 | `431723bd0cd7f8dc0cb0c85c682ab336e35c42d7` |
| PROOF.md | 15646 | `ab03fc5ab37ec787ea3794862a1a9b69048f0749` |
| README.md | 2293 | `9b969d1fca2edbe77fac7de75ed9fb522c9e9f7e` |
| RUN.json | 243 | `fd526c473b3fd6f55080ee7ee3bf3f6257f1f4bf` |
| audit.py | 10097 | `3e48205d4649118006377f559b9423950a6d97d7` |
| stderr.txt | 0 | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| stdout.json | 7194 | `e7aa626f20c5ac81f4b812c3cbc20126978a4ac0` |

| Source file | SHA-256 |
| --- | --- |
| MANIFEST.json | `994017c82c5e43c6b6105b4bc27d4df72cde62f51ec8d271ba90c3cc4156d69d` |
| PREREG_REFERENCE.md | `2f275f2b6448e7b5dbdd1d84ea543568eeb6a701a5e8b0fb2cae5e4221734511` |
| PROOF.md | `3f55fa7b5c60b1debf213b0b77293eeb7bfe617718f877ad94c3e7148b784dd8` |
| README.md | `1594283aad6199377e9b16cf0ce905e7d6f8676df4403142b74423ae7918f1de` |
| RUN.json | `dacd876444392200395754dc443b9c31c46494f49be8dcb844a2aaf07bdde683` |
| audit.py | `e68af62c225570fa49758d8cec63cc8dbe54a85710d7571e022617a641fc2b39` |
| stderr.txt | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| stdout.json | `6292d29565f5df4608ae7443e4e927c69bab062332d3010880264fddd565c5e2` |

The inherited public native proof was read and its Git blob locally checked
as `f848b6fa08163bcef2c51a0a7fdfad4b299163a6`. Original source licensing is
Apache-2.0. Source author attribution is retained; this preparation makes
no commit under that author's identity. The attached intake proposal is
editorial input, not repository authority or authorization to execute the
incubation issue's historical run instructions.

Source proof and code were read. The source `RUN.json`/`stdout.json` bytes
are preserved as incubation custody only, outside the tracked preparation;
no claim is made to have independently reproduced them. No original or
draft scientific verifier was imported or executed. The only executed
Python helper read bytes, checked hashes/tree identity, transformed draft
text, and used `ast.parse`; it never imported the audit module or called
its scientific functions.

## Static scientific findings

**Five response classes.** The pathwise argument is valid for fixed f
independent of the auxiliary variable. Equal encoded sums give equal Q
histories for each ready/seed, hence equal processor transcripts; integration
and positive-probability conditional ratios preserve the equality. The
draft makes measurability, common initial processor state, fixed event rule,
common launch clock, and absence of externally source-selected postselection
explicit. There is no need to limit processor memory or assume finite
completion time. A finite-history regression cannot substitute for this
induction.

**Exact six-source obstruction.** The six displayed target substitutions
are distinct and suffice for the impossibility result independently of
the census. They compare original beta(p), not the encoded beta(f(p)).
The five/four inherited history classification is not a new registration.

**Census and sharp upper certificates.** The source provides a table of
22 rational values and multiplicities but labels their finite evaluation
candidate-C. The new draft supplies the complete 69-pattern multinomial
certificate and freezes all 22 values/counts. This supports a small
independently checkable finite proof route. No new computation is claimed.
The table, all block boundary evaluations and the proposed attaining
permutation remain subject to independent review and a newly pinned audit.
Without those, publish the proved obstruction/lower bounds at their earned
scope rather than silently promote the full sharp finite conclusions.

**9/128 lower bound.** The six attainable packing values are separated by
at least 9/64. Pigeonhole plus the triangle inequality proves the bound
without encoder linearity, continuity or any averaging assumption. The
five displayed block radii furnish the matching upper bound once the
complete target table is accepted. This is worst-source absolute LOW
response error, not a measured discrepancy or total transcript distance.

**27/64 lower bound.** The source's analytic mixed-sign estimate is sound
after global sign reversal and removal of all but one negative entry. The
ratio is bounded by `3(t-1)^2/(t^2+3)` for `1<=t<=6`, whose monotonicity is
made explicit in the draft. Exactly 120 common-sign sources exceed 5/32.
Every faithful message group has at least 124 supported sources, yielding
the bound from a group containing beta=1. Sorted-block uncrossing preserves
capacities, and the explicitly described permutation attains the bound
conditional on the finite boundary table. Injection on all 625 labels is
essential to the stated capacity argument.

**Null and physical boundary.** The null has no beta value. Under faithful
encoding it shares its message with 124 supported labels, so equal laws
obstruct exact support tagging separately. Neither attaining comparison
construction supplies an occurrence law from U. Source-dependent stochastic
loading, seed-dependent f, coherent multipoint sources, a different port,
new source-sensitive input or native intervention are outside this class.
The physical QDD owner rows remain O, and no physical or cross-layer gate
is closed.

No mathematical counterexample was found in this static source review.
This review has seen the source and is not a blind breaker or independent
formal acceptance. The exposed candidate constants are explicitly frozen
as intake checks, not relabelled as new predictions.

## Draft verifier changes and preparation validation

The original audit would report a changed count or optimum without directly
asserting the exposed numerical values: it required only at least six
distinct targets and agreement between internal optimization algorithms.
That was appropriate for its original discovery question but insufficient
for this fixed acceptance statement. The new `verify.py` draft adds:

- The full 22-entry count table and an independent 69-pattern multinomial
  enumeration, compared with direct source enumeration.
- Exact assertions for `9/128`, `27/64`, all five faithful cases, the 120
  strict high-weight count, packing witnesses, all free covering inequalities,
  faithful block extremes/centers and five distinct ready `(0,1)` outputs.
- Explicit draft/provenance language and neutral audit-only output status.

It retains exact integer/Fraction arithmetic, the independent interval
recurrence, exhaustive cuts, full bijection, source-dependent-loading
counter-control, and inherited identity regressions. These are prospective
checks; none has run in this preparation.

Static AST parsing succeeded with Python 3.12.10; the AST contains no
floating-point constants. No `__pycache__` was created in this directory.
Draft verifier: **12919 bytes**, SHA-256
`db672316a35cd95d693677c1ca906bf7c40c359120196819c6acc56c836256dd`.
This is a preparation identity, not a preregistration pin.

Remaining formal work: actual owner/issue reservation and collision check;
review/acceptance of the final exact statement and code; public pin;
preserved formal execution and required architecture checks; independent
proof decision; sealed result; then any separate reviewed Canon fold.
No `EXPECTED.txt`, `RUN.md`, formal result, canonical file edit, public
write, probe reservation or release action is included here.
