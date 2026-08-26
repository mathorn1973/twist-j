# P-DE-W-ARMING-2 result

Status: `R1 FIRED / RESULT-EXPOSED CONFIRMED / CANON UNCHANGED`

## Disposition

```text
decision:   R1 FIRED. On the frozen DESI DR2 readback, the HEADLINE flat
            constant-w (wCDM) fit DESI+CMB excludes w = -14/15 at or above
            the inherited 99 percent two-sided witness bar: exact Gaussian
            witness 365/108 against the immutable bar 322/125, margin
            10849/13500.
consequence: DE-W-CONSTANT [H] -> F, taken by a later sealed fold that
            consumes this probe as evidence; this probe moves nothing.
integrity:  no STOP. One formal execution from a fresh clone at the pin
            commit, exit zero, empty stderr, 9 of 9 gates PASS, stdout
            equal to EXPECTED.txt.
```

The single formal execution reproduced the exposed result exactly. The
frozen record is one quoted posterior summary — DESI DR2 Results II
(arXiv:2503.14738v3; Phys. Rev. D 112, 083515), table 5, flat wCDM,
DESI+CMB: `w = -1.055 +/- 0.036`, HEADLINE on the abstract's own
designation — entered as the exact rationals `-211/200` and `9/250`, with
the decimal-to-rational identities asserted inside the verifier.

## What the gates decided

Rule R1 (inherited verbatim from `P-DE-W-ARMING-1`, bar `322/125`
immutable): FIRES. The witness `|z| = |-211/200 + 14/15| / (9/250) =
365/108` sits above the bar by the exact margin `10849/13500`; the cross
products `45625 > 34776` decide it in integers. The HEADLINE designation
and the absence of a printed override statement are frozen record data
(gates G4, G5), with their readback provenance and misquote defect clause
in `PREREG.md`. Rules R2 and R3 are out of scope here and remain exactly as
recorded on `P-DE-W-ARMING-1` (gate G8).

## Provenance boundary

The drafting environment could not reach the source paper (network egress
blocked); the quoted values entered on the owner's public readback of
2026-08-26, recorded in issue #576 before the pin, and are auditable by any
reader against the public paper. A demonstrated misquote of the source is a
defect and voids this probe in favor of a fresh one; the thresholds
themselves can never move.

## Scope boundary

This probe changes no Canon, Registry, Frontier, workflow, gate, or
existing probe file. The move `DE-W-CONSTANT [H] -> F` does not exist until
a later sealed fold performs it; the proposed ledger delta is frozen in
`PREREG.md` (H 3 to 2, F 16 to 17, live 30 to 29, program rows 30 to 29,
nothing else). COSMOLOGY-REGISTER [D] is unchanged as the source of the
committed form: the fired object is the register *reading*, not the
register dictionary. DE-CONFORMAL-WEIGHT [O] is untouched and never takes
this row as a selection premise, fired or not. No statement is made about
the w0waCDM evolution preferences on `P-DE-W-ARMING-1`'s record. A fired
falsifier is first-class progress; the reading dies and nothing else moves.

## Evidence boundary

The local formal leg is x86_64 (Ubuntu 24.04.4 LTS, CPython 3.11.15). The
pull-request workflow reruns the pinned verifier on GitHub x86_64 and
native aarch64 and requires byte-identical stdout against `EXPECTED.txt`;
those runs complete the repository two-architecture computation gate for
this arithmetic. The computation is exact rational bookkeeping over one
quoted published summary; the two-architecture replay audits the
bookkeeping, and the readback provenance bounds what it can mean.
