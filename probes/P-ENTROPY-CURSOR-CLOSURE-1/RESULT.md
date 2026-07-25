# P-ENTROPY-CURSOR-CLOSURE-1 result

Status: FORMAL AARCH64 PASS; X86_64 PENDING

The immutable preregistration pin
`916eed58a37f0a4ce56ff093fc0dcb7e1d42d5ff` was executed once on native
aarch64 after remote readback. The verifier exited zero, wrote no stderr, and
produced the exact 1,474-byte output recorded in `EXPECTED.txt` with SHA-256
`21ca2301ffa17634eb868c154e7b683c0d2ca0bc54661962029b12a7a0e65ca7`.

At the preregistered finite surface, all 522 distinct window/cursor pairs for
driver windows `L = 4..32` and all 27 distinct depth-grid triples were zero:
549 distinct candidate parameter triples, 0 nonzero. The E05 structural
certificate proves that the labelled zero-residue restriction projects to the
same pure-word obstruction, transporting this finite-cylindrical no-go to
every lambda-depth.

This is candidate-T evidence only for the typed `F_5^6` finite-cylindrical L5
ansatz. It makes no measurable-selection, entropy, or measure-lift claim and
does not close `ENTROPY-LAYER-BRIDGE [O]`.

Public lock: https://github.com/mathorn1973/twist-j/issues/151

Disposition: await the required GitHub-hosted x86_64 byte-identical
reproduction before merge or Canon registration.
