# Reproduction

## Input

Obtain the sole external source exactly as described in `SOURCE.md`.  The
verifiers reject any source whose SHA-256 is not

```text
55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae.
```

## Primary census

Replay the exact source, 2-unitarity, and field gate first:

```bash
python3 verify_source_field.py AME46_ORIGINAL.m > SOURCE_FIELD.txt
cmp EXPECTED_SOURCE_FIELD.txt SOURCE_FIELD.txt
```

Then run the covariant census:

```bash
python3 verify_a5lu_covariants.py AME46_ORIGINAL.m > OUTPUT.txt
cmp EXPECTED.txt OUTPUT.txt
```

Recorded environment:

```text
CPython 3.12.13
NumPy 2.3.5
Linux 6.18.35 x86_64
elapsed about 1.8 s
```

The program uses signed integer arrays only.  It checks before contraction
that the uniform unreduced bound

```text
40^6 * 6^11 = 1486016741376000000 < 2^63-1
```

holds, so no floating-point arithmetic or signed overflow is involved.
Two runs, including one with `PYTHONHASHSEED=193`, were byte-identical.

## Exact class representatives

```bash
python3 exact_scalar_reps.py AME46_ORIGINAL.m verify_source_field.py \
  > EXACT_REPS.txt
cmp EXPECTED_EXACT_REPS.txt EXACT_REPS.txt
```

This reuses only the exact `Q[z]/Phi_40(z)` arithmetic and parser from
`verify_source_field.py`; the contractions and descriptors are supplied by
the primary census.  It verifies one representative of every scalar class on
each leg in the exact cyclotomic field.

## Independent census

```bash
python3 crosscheck_f41.py AME46_ORIGINAL.m --output CROSSCHECK.json \
  > CROSSCHECK.stdout.txt
cmp EXPECTED_CROSSCHECK.txt CROSSCHECK.stdout.txt
sha256sum CROSSCHECK.json
```

The expected uncompressed JSON SHA-256 is

```text
37c81c9337656551ce0973b6012203ce58b74fba2ad57e6b7e81a42896712c9a.
```

`CROSSCHECK.json.gz` is the same complete output compressed with
`gzip -n -9`.  Two runs under different hash seeds were byte-identical.

## Integrity

```bash
sha256sum -c SHA256SUMS.txt
python3 tools/check_policy.py
python3 tools/check_canon.py
python3 tools/check_ledger.py
```
