# First synthetic execution record

**PUBLIC / NON-CANONICAL. Auditor fixtures only; no campaign result.**
Original work Apache-2.0, A. M. Thorn, 2026-10-12.

The complete eight-file source package was committed and pushed at
`9a5c07e140d5781934e026414aa7f7b306b15952` before this first execution.
Public immutable-ref readback matched the full text of `audit_saved.py`,
`verify.py` and `CONTRACT.md` byte for byte; all eight public Git blob IDs and
byte counts matched the committed tree. The two executable source SHA-256
values were checked again immediately before execution:

```text
2f92288c339ed17370d1bd8d22bbbf7929c793dfdf504a25c1bf4bf281480340  audit_saved.py
83b848f1d78b288eeabe69a4321f26156dfc9eaedf5089b83b3fbc5c4d0641b9  verify.py
```

Command from the repository root:

```sh
python3 -B notes/C-U-CA40-FULL-PULSE-INDEPENDENT-AUDIT-N/verify.py
```

Neutral environment: WSL2; Linux kernel
`6.6.87.2-microsoft-standard-WSL2`; x86_64; little endian; CPython 3.10.12.

First invocation: 2026-10-12T16:28:57.185634+00:00 to
2026-10-12T16:28:57.250361+00:00. Measured elapsed time 0.064720 seconds.
Exit code **0**. Stdout was captured without text or newline conversion and
is reproduced exactly in [EXPECTED.txt](EXPECTED.txt):

```text
stdout bytes: 2593
stdout SHA-256: 62f5b1cc1827b77d2fe441de30dc3b25d48c045d9165d05c11ea2b0d76e657a5
stderr bytes: 0
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The first stdout, stderr and execution metadata were preserved before this
public transcription. There was no failed invocation, replacement or retry.
The executable sources remain byte-identical to the source pin.

This is one local architecture. Repository policy CI is not configured to
execute this notes-only fixture suite; passing policy jobs on two architectures
does not constitute a second execution of these fixtures. This record neither
claims a two-architecture scientific computation gate nor promotes a claim.
No candidate module was imported, no campaign data were read, and no solver
was executed. The live full-pulse campaign was not modified.
