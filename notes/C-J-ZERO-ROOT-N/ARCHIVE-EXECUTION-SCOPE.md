# Selector correction before the first archive replay

**NON-CANONICAL / no authority / prospective correction.**

Static review of aba3d1a311cbacc6ef48ecb034903a96dec7eae9 caught a
transcription error in ARCHIVE-PREREG.md before any archive program was
compiled, imported or run. Its sentence giving the selector omitted
reduction of popcount modulo2. The correct frozen native selector is

```text
theta(n) = popcount(n) modulo 2
letter(n,state) = (sum(state) + 2*theta(n)) modulo 5.
```

The earlier literal expression with twice the unreduced popcount is
incorrect, already at n=3. This correction, not that expression, defines
the intended equation for execution. The archived implementations and
the new wrapper already use the correct parity rule. The wrapper, manifest,
all received source bytes, tested domains, horizons, limits and expected
outputs remain unchanged. The earlier pin is retained verbatim rather
than amended or erased. The first run must wait until this additional
file is committed, pushed and read back; its descendant commit is the
execution pin for the complete protocol.

The caller must explicitly choose an output directory outside Git and
retain the outer process's exit code, stdout and stderr, including any
failure before the wrapper creates its own report. Isolated Python ignores
PYTHON environment options; the source uses deterministic output order and
the byte comparisons remain the acceptance conditions.

The static reviewers were same-session Astra and Sol helpers, not an
independent external review. No scientific outcome had been observed in
this session when this correction was made.
