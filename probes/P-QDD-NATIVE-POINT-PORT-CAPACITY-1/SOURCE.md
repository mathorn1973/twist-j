# Accepted source custody: P-QDD-NATIVE-POINT-PORT-CAPACITY-1

Prospective, result-exposed public intake. Recorded 2026-09-19 before the
first formal execution. Source author: A. M. Thorn; original work licensed
Apache-2.0. This intake adapts source proof/code and preserves their original
custody; it does not relabel the incubation output as a new formal run.

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
draft scientific verifier was imported or executed. Pre-pin Python helpers read bytes, checked hashes/tree identity, transformed
text, and used `ast.parse`; they never imported the audit module or called
its scientific functions.


## Adaptation and independent review boundary

The accepted proof is self-contained at its frozen mathematical scope and
expressly inherits the public native quotient theorem. The source audit is
adapted to assert the complete exposed 22-entry census, both sharp errors,
the analytic high count, exact packing witnesses, complete upper covers,
five faithful cases and the attaining permutation. A separate 69-pattern
multinomial enumeration checks the pointwise census. These fixed acceptance
assertions replace the discovery source's weaker at-least-six-value
condition; the known target values are declared exposed, not predictions.

No source RUN or stdout is imported into this probe as formal evidence.
Fresh formal stdout must come from the publicly pinned accepted verifier.
The independent BREAKER.py is prepared from PREREG.md without author-code
access, and has its own frozen BREAKER-PREREG.md. It shares the exposed
problem statement and is neither result-blind nor a separate physical
experiment. Its exact check is invoked by verify.py, so both architectures
replay both implementations. Neither implementation ran before the pin.
