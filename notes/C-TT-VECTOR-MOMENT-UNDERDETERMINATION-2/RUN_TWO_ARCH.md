# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2 two-architecture run record

NON-CANONICAL. Incubation record. No public claim is established by this file.

## Legs

```text
leg 1   platform Ubuntu 24.04 container, Linux 6.18.5
        architecture x86_64
        CPython 3.12.3
        verify 14 s, executed 3 times, byte-identical stdout each time
        breaker 13 s

leg 2   platform macOS 26.5.2
        architecture arm64
        CPython 3.9.6, Clang 21.0.0
        verify 18 s
        breaker 16 s
```

Both legs run from the candidate directory with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`. The
prereg and the verifier were hashed before the first execution on leg 1; the
leg 2 copies were verified byte-identical against those pins before running.

## Byte identity

```text
artifact       sha256                                                             bytes  leg1  leg2
verify.py      a0b86d78e414825c386e3f08c654ec73e0d174c73f097cb311fa5244a07f4b67   13802  same  same
breaker.py     1ea4b98e174c5271f17310f76c60dad1051faa512fe2393a58d5297cfb899738    9809  same  same
EXPECTED.txt   711bb0e825029c2f77a84f74934c8af32224d53da934bf5c8e484ff801edd59c    3013  same  same
BREAK.txt      cf6902200fa6bf9a8896dc95099fb5aa3900ce2f1c1eb6ca75d6e8b210e9a642     986  same  same
```

The two legs differ in architecture, in operating system, and in CPython
minor version. Byte-identical stdout across that spread is stronger than the
two-architecture requirement asks for.

Verifier on both legs: 40 of 40 gates PASS, exit 0, empty stderr.
Breaker on both legs: 11 of 11 gates PASS, zero breaks, exit 0, empty stderr.

## What this does and does not buy

It buys the local two-architecture leg pair that a public probe needs. It
does not buy the GitHub x86_64 required check at pull-request time, which can
only be produced by the public probe under `probes/`, and it does not by
itself raise any status: the labels in `RESULT.md` are carried by the written
proofs, and the verifier audits them at complete finite scope.

Nothing here promotes anything. The parent `TT-VECTOR-STATE-NORMALIZATION`
remains `[O]` / STOP.
