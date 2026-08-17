# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 two-architecture run record

NON-CANONICAL. Incubation record. No public claim is established by this file.

This record supersedes the paragraph headed ONE LEG ONLY in `RESULT.md`.
`RESULT.md` is left byte-exact at its recorded pin and is not edited, so the
sequence stays auditable: the first leg was run and written up alone, then a
second architecture was added. Read `RESULT.md` for the proofs and this file
for the run evidence.

## Legs

```text
leg 1   platform Ubuntu 24.04 container, Linux 6.18.5
        architecture x86_64
        python 3.9 not used; CPython 3.12.3
        verify 5 s, executed 3 times, byte-identical stdout each time
        breaker 4 s

leg 2   platform macOS 26.5.2
        architecture arm64
        CPython 3.9.6, Clang 21.0.0
        verify 4 s
        breaker 4 s
```

Both legs run from the candidate directory with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

## Byte identity

```text
artifact       sha256                                                             bytes  leg1  leg2
verify.py      68238c8609a6e651a11f760d493045e015839bd3810ed05466823e21c2a3fc7c   13398  same  same
breaker.py     6fc905cec73a5bc3607b384723ea0d25eaf6c91a17828b64b64075c891bcff43    9112  same  same
EXPECTED.txt   d547022e0aad57f2fa7ab36fa1a2c575f345c8169572130a7d6bb1e0a0acefe6    4313  same  same
BREAK.txt      0ac5a53d4046a123d666410004e6bc9545c942ec38e98ed88c950d866301064d    1064  same  same
```

The two legs differ in architecture, in operating system, and in CPython minor
version. Byte-identical stdout across that spread is stronger than the
two-architecture requirement asks for, because a version-dependent formatting
or ordering effect would have shown up as a diff and did not.

Verifier on both legs: 63 of 63 gates PASS, exit 0, empty stderr.
Breaker on both legs: 13 of 13 gates PASS, zero breaks, exit 0, empty stderr.

## What this does and does not buy

It buys the local two-architecture leg pair that a public probe needs. It does
not buy the GitHub x86_64 required check at pull-request time, which can only
be produced by the public probe under `probes/`, and it does not by itself
raise any status: the labels in `RESULT.md` are carried by the written proofs,
and the verifier audits them at complete finite scope.

Nothing here promotes anything. The parent `TT-VECTOR-STATE-NORMALIZATION`
remains `[O]` / STOP.
