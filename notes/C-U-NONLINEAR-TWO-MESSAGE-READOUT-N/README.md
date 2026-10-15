# Origin-zero nonlinear two-message readout and the reader-complexity boundary

NON-CANONICAL / L1 / no scientific authority.
Owner issue: [#1535](https://github.com/mathorn1973/twist-j/issues/1535).

[PROOF.md](PROOF.md) gives the construction and the boundary results.
[PREREG.md](PREREG.md) discloses prior exposure and freezes the audit.
[RESULT.md](RESULT.md) states the exact outcome scope; [RUN.md](RUN.md)
records the first lane execution and [EXPECTED.txt](EXPECTED.txt) is
that stdout.

In one paragraph: on unchanged native `U`, 25 preparations at `n=0`
carrying two pre-loaded messages give, under one fixed clock-free
nonlinear global readout, `BLANK -> PRESENT(lam) -> BLANK ->
PRESENT(mu) -> ...`. The readout can be taken as the single cubic
polynomial pair `(z, C(1-z^2) + A*z*D)`. On this family no affine
two-coordinate receiver with any decoder can do this (three affine
coordinates are necessary and sufficient), and no reader using only
four coordinates — in particular not the canonical receiver block
`(b,d,q,r)` — can do it at all. This is an existence result for a
native reading, not a funded contact, insertion, or energy result.

Run from the repository root:

    PYTHONHASHSEED=0 PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 \
    python3 notes/C-U-NONLINEAR-TWO-MESSAGE-READOUT-N/verify.py

Compare stdout byte for byte with EXPECTED.txt. Notes-only CI does not
perform this scientific replay. Independent review and any public
promotion are separate steps; this branch changes no Canon file.

Promotion dossier: [PROMO.md](PROMO.md).
