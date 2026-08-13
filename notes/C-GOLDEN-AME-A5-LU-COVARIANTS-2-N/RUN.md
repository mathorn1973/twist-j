# Reproduction

Requirements: Python 3.12 and NumPy.  Run from this directory.  Supply the
pinned `AME46_ORIGINAL.m` as the first argument to each verifier.

```bash
python verify_source_field.py /path/to/AME46_ORIGINAL.m \
  > SOURCE_FIELD_STDOUT.txt
cmp EXPECTED_SOURCE_FIELD.txt SOURCE_FIELD_STDOUT.txt

python run_n4.py /path/to/AME46_ORIGINAL.m \
  --prereg PREREG.md \
  --engine n4_locator_engine.py \
  --output MODULAR_RESULT.json \
  > MODULAR_STDOUT.txt

python exact_witness.py /path/to/AME46_ORIGINAL.m \
  --field-module verify_source_field.py \
  --output EXACT_WITNESS.json \
  > EXACT_STDOUT.txt

python independent_mod41.py /path/to/AME46_ORIGINAL.m --scan \
  --output INDEPENDENT_MOD41.json

python independent_exact.py /path/to/AME46_ORIGINAL.m \
  --output INDEPENDENT_EXACT.json

sha256sum -c SHA256SUMS.txt
```

Expected terminal decisions:

```text
G0 PASS
G1 PASS: 2345 orbits, four irreducible cores
G2 PASS: complete 16+16 census; first hard locator q=0,R1
G3 PASS: exact minor nonzero, residue 31, exact eigen split 2+2+2
G4 EXACT NO in the frozen arbitrary-local-unitary 1+5 scope
```

`run_n4.py` accepts explicit preregistration, engine, and output paths.
`exact_witness.py` accepts explicit field-module and output paths.  Neither
script depends on a `/tmp` path or an unpublished module.
