# P-FIELD-ZERO-NONZERO-CUT-1 result

Date: 2026-08-18. Preregistration pinned at commit
`4c63a5ac23efb71d6c12bddbc79a7d2788937559` before every accepted formal run.

## Verdict

```text
universal written proof                              PASS
F_2,F_3,F_4,F_5,F_7,F_8,F_9,F_11 finite audits      PASS
F_5^x zero-deletion boundary control                 PASS
FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT                proposed [T]
QDD-INSTRUMENT-APPARATUS                             [O] / STOP, unchanged
```

For every field `F`, every nonempty proper `A subset F`, and every total
Boolean table `B`, the identity

```text
1_A(xy) = B(1_A(x),1_A(y)) for all x,y in F
```

holds exactly in the two oriented cases `A={0}, B=OR` and
`A=F^x, B=AND`. The field-independent proof in `PREREG.md` supplies the
universal theorem. The verifier exhaustively confirms it over eight finite
fields, including three nonprime fields, after checking their field axioms.
No falsifier fired.

## Evidence

```text
PREREG.md    sha256 23e307ecfc726cb9a387baefdf51b79e91273e09206c8df7b3c095ae5476a5a0  11374 B
verify.py    sha256 1a5e539c07e4f448eacb99f81e9f9e009efa947225d71ce12d143cd2ffccc2aa   8217 B
EXPECTED.txt sha256 f5dcf8c2f6115c6ece84303b736cce877e4fec67933c5ea8e37570667b90f6be    889 B
```

The accepted local leg ran twice from a fresh detached public worktree at the
pin on Ubuntu 24.04.3 LTS, x86_64, CPython 3.12.13, with deterministic
environment, exit 0, empty stderr, and byte-identical stdout. Pull-request CI
must independently reproduce the exact output on x86_64 and aarch64 before
this proposal can be consumed by a Canon fold.

## Boundary and non-inflation

Deleting zero changes the theorem. On `F_5^x`, the exhaustive control finds
the two quadratic-character orientations `QR/XNOR` and `NQR/XOR`. This does
not contradict the total-field classification; it exhibits why zero's
presence is the decisive hypothesis.

The result is field- and characteristic-independent. The appearance of
`F_5` in the audit does not create five-specific content. The theorem
classifies a two-cell multiplicative quotient; it does not select a field, a
cut, a QDD channel, a physical decoder, an L5 stream, or an L6 measure. It
therefore supplies only a structural cross-reference to the public
ZERO/SUPPORTED branch and moves no QDD parent or gate.
