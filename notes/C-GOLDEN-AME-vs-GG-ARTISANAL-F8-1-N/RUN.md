# Reproduction

Requirements: CPython 3.10 or newer and only the Python standard library.
The three external inputs are deliberately not vendored.  Recover them at
the exact URLs in `SOURCE_PINS.json`, place them as follows, and verify their
listed byte counts and SHA-256 values:

```text
source/AME46_ORIGINAL.m
source/2504.15401v2.pdf
source/2504.15401v2.tar
```

Then run from this directory:

```sh
python3 verify_manifest.py
python3 run_primary.py
```

The full run takes about 75--80 seconds on the reference container.  It
validates G0--G2, computes all twelve modular contractions twice, computes
all twelve exact contractions twice, exactifies the first frozen mismatch,
and rewrites the six deterministic result files.  Successful stdout ends in

```text
UNION_VERDICT=EXACT_NO_GG_ARTISANAL_9PLUS27
STATUS=PASS
```

To reproduce the independently written F8 cross-check (it is not imported by
the primary evaluator):

```sh
python3 independent_f8_crosscheck/crosscheck_f8.py \
  --source source/AME46_ORIGINAL.m \
  --output /tmp/cross-result.json --progress
```

See `independent_f8_crosscheck/RUN.md` for all modes.  The independently
written G0/G1 auditor is preserved with its certificates in
`independent_gate_audit/`; its source-location CLI is documented by
`python3 independent_gate_audit/gate_audit.py --help`.

`verify_manifest.py` verifies the frozen delivered package.  Because
`run_primary.py` deliberately regenerates result files, rerun the manifest
check after a computation only when testing byte determinism against the
delivered certificate.
