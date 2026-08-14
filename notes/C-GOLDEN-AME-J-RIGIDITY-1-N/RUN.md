# Reproduction

## Inputs

Supply the two pinned upstream files as command-line arguments:

```text
55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae  AME46_ORIGINAL.m
af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649  block944.m
```

The verifiers reject any byte change.  They write no files and make no
network calls.

## Primary standard-library replay

From any working directory:

```bash
bundle=/path/to/this/directory
source_m=/path/to/AME46_ORIGINAL.m
block_m=/path/to/block944.m

"$bundle/run_standardlib.sh" "$source_m" "$block_m" > replay.txt
cmp replay.txt "$bundle/EXPECTED_STANDARDLIB.txt"
sha256sum replay.txt
```

Expected transcript: 4,122 bytes, SHA-256
`34319c86bd8efb3c4745be032af494f6af9214ec28660d5d3bfba57794cfd34e`.
The replay requires only CPython 3.11 or newer and the Python standard
library.  `PYTHON` may select a different interpreter.  Both run wrappers
unset `PYTHONOPTIMIZE` and refuse any interpreter with assertions disabled.

For a deterministic double replay:

```bash
"$bundle/run_standardlib.sh" "$source_m" "$block_m" > replay.1.txt
"$bundle/run_standardlib.sh" "$source_m" "$block_m" > replay.2.txt
cmp replay.1.txt replay.2.txt
cmp replay.1.txt "$bundle/EXPECTED_STANDARDLIB.txt"
```

Verify the package payloads with:

```bash
(cd "$bundle" && sha256sum -c SHA256SUMS.txt)
```

## Optional exact SymPy discovery replay

This lane is informative, not trusted by the primary verifier.  It requires
SymPy 1.14.0.  The reference source checkouts were SymPy commit
`16fa855354eb7bcabd3fe10993841e03b1382692` and mpmath commit
`b5c04506ef0cd4a1f1213f8389ee21c9c3551582`.

With SymPy available to the selected Python:

```bash
"$bundle/run_optional_sympy.sh" "$source_m" > sympy.txt
cmp sympy.txt "$bundle/INDEPENDENT_SYMPY_EXPECTED.txt"
sha256sum sympy.txt
```

Expected stdout SHA-256:
`5cb4c9c756e25c69bcbb7effe88fde744dbac15e79bd1d7244a5acdcb8405e60`.
The four `STAGE` lines make long exact computations visible without adding
timings or host-dependent text.

## G8 resource record

The integrated primary replay ran on CPython 3.12.13, Linux x86_64,
sequentially with one worker: wall 20.159 s, user 20.072 s, system 0.060 s,
and maximum RSS 28,296 KiB.  The largest committed certificate is 276,630
bytes, below the frozen 5-MiB artifact limit.  These measurements are also
well below the frozen limits of 24 hours, eight workers, and 16 GiB RAM.
Re-measure on another host with:

```bash
/usr/bin/time -v -o resource-use.txt \
  "$bundle/run_standardlib.sh" "$source_m" "$block_m" > replay.txt
```
