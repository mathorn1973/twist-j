# P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3

Exact Maurer-Cartan off-shell lapse gauge closure through degree 4 and forced
`a in {-1, 0, 1}` affine scalar-lapse completion with a non-trivial vacuum
cold-start free-lapse shell. `NON-CANONICAL`, `NEW_DECLARED L1`; conditional
`candidate-T`.

The local first formal run passed (`RESULT=PASS`). Independently implemented
primary (`verify.py`) and breaker (`breaker.py`) produced identical raw
certificate bytes and detected all 8 preregistered negative controls.

From the repository root, with Python 3 and its standard library:

```sh
python3 probes/P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3/verify.py
```

The primary invokes the standalone breaker in an isolated subprocess (`-I`);
stdout must match `EXPECTED.txt` byte for byte (`499` bytes, `17` lines,
SHA-256 `3215cd17cfd2db24744de14bfbfd5b4065ab293e9a2a7a8df03750a90664ffbc`).
`PREREG.md` defines the frozen contract, `PROOF.md` gives the universal
derivations, `SOURCE.md` records authority and provenance, and `FROZEN.sha256`
binds the five scientific files. `RUN.md` records the first execution,
`RESULT.md` states the outcome and scope limits, and `REVIEW.md` records the
post-pin source and proof review.

Prospective pin: `04e21ecf4a866cd861d875706050006e0d0fbd59`.
Ownership and pre-execution receipt:
https://github.com/mathorn1973/twist-j/issues/1669#issuecomment-6286325093

No Canon promotion is requested by this result package.
