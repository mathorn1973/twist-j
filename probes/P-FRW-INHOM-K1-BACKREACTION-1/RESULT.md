# RESULT. P-FRW-INHOM-K1-BACKREACTION-1

```text
Status: ABANDONED
Scientific run: NONE
Exact stdout: NONE
RUN.md: ABSENT BY DESIGN
EXPECTED.txt: ABSENT BY DESIGN
Owner status move: NONE
```

The immutable preregistration and accepted verifier were publicly pinned at

```text
776668bfd6d87317cb7f3c5b2f6ce55b25a75e74
```

before any result-bearing execution.

After the pin, but before the first scientific invocation of `verify.py`, a
protocol audit found that the accepted verifier encoded a preregistered
scientific `FAIL-CONSTRUCT` by raising `AssertionError` and exiting nonzero.
Under repository policy a nonzero scientific invocation does not produce a
completed gate or an exact scientific stdout. It therefore cannot serve as the
frozen negative outcome promised by the preregistration. Running this verifier
would conflate a scientific falsifier with an execution failure.

No scientific invocation of the pinned verifier was made. One attempted local
repository checkout failed on DNS resolution before checkout completed and
before `verify.py` was invoked. It produced no scientific stdout and is not a
gate execution.

The verifier and preregistration remain unchanged. No threshold, equation,
coefficient, carrier, time placement, equality, or source definition was
altered after the pin.

This identifier is consumed and must not be reused, renamed, resumed, or
repaired. Any successor must use a new probe identifier and its own immutable
pin. The successor must name this abandoned predecessor and must preserve the
frozen scientific target while changing only the verdict protocol needed to
represent both `PASS-CONSTRUCT` and `FAIL-CONSTRUCT` as completed exit-zero
scientific outcomes.

This abandonment has no scientific conclusion. It neither supports nor rejects
the selected K1 backreaction construction and changes no Canon, Registry,
Frontier, gate, `FRW-INHOM`, `TT-SOURCE`, or
`TT-VECTOR-STATE-NORMALIZATION` status.