# P-DE-W-ARMING-2 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / R1 EVALUATION / RULES INHERITED`

This probe evaluates exactly one frozen rule on exactly one new record. The
rule is R1 of `probes/P-DE-W-ARMING-1/PREREG.md`, inherited verbatim and
unamended. The record is the DESI DR2 flat constant-w (wCDM) posterior
readback that `P-DE-W-ARMING-1` declared PENDING, with the mandate that its
evaluation "belongs to a fresh probe, not to an amendment of this one". This
is that fresh probe. The registry, frontier, and Canon are not touched; the
consequence of a fired rule is taken by a later sealed fold, not here.

The result is exposed before execution: on the frozen readback,

```text
R1 FIRES (Gaussian witness 365/108, at or above the frozen bar 322/125)
```

and the fold consequence is `DE-W-CONSTANT [H] -> F`. A fired falsifier is
first-class progress; the reading dies and nothing else moves.

## Public identity, authority, and action layer

```text
probe:               P-DE-W-ARMING-2
public claim lock:   issue #576
probe owner:         A. M. Thorn / delegated session de-w-r1-2026-08-26
branch:              probe/P-DE-W-ARMING-2
basis:               Public Canon v66, main 687c781, tag canon-v66,
                     CONTENT_COMMIT 8f11ec18, SHA256SUMS 5 of 5 OK
action layer:        L6, reading only; no layer lift is performed and no
                     gate is consumed
authority:           none until folded; the fired rule sends the H row to F
                     at the next sealed fold and moves nothing else
```

## Falsifier, first

Rule R1 is inherited from `P-DE-W-ARMING-1` verbatim. This probe cannot
amend it, and restates it here for self-containment only:

```text
R1 CONSTANT-FIT EXCLUSION. In a HEADLINE flat constant-w (wCDM) fit of a
   carrier release, w = -14/15 is excluded at or above the 99 percent
   two-sided credible level. Gaussian witness convention: the exact ratio
   |z| = |w_mean + 14/15| / sigma at or above 322/125; a credible-interval
   or exclusion statement printed by the source paper overrides the
   Gaussian witness in both directions.
```

HEADLINE is inherited with its `P-DE-W-ARMING-1` meaning: the combination
the collaboration's own abstract or summary designates. Rules R2 and R3
remain on `P-DE-W-ARMING-1`'s record; nothing here re-evaluates, restates,
or reopens them, and the four R3 witnesses recorded there are unchanged.

## The six fields

```text
EQUATION     w_DE(a) = -14/15 exactly, constant in a, standard flat FRW
             fluid convention; equivalently rho_DE ~ a^(-1/5); equivalently
             Delta_DE = 1/5. Source of the number: COSMOLOGY-REGISTER [D],
             unchanged. Identical to P-DE-W-ARMING-1.
CODE         probes/P-DE-W-ARMING-2/verify.py. Python standard library
             only, exact Fraction arithmetic, no float in any assertion,
             comparison, or printed value, deterministic stdout, well under
             120 seconds, run from the repository root with LC_ALL=C
             LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
CARRIER      this probe's record is one quoted posterior summary from one
             carrier release already inside the P-DE-W-ARMING-1 carrier:
             DESI DR2 Results II (arXiv:2503.14738v3; Phys. Rev. D 112,
             083515), table 5, flat wCDM, combination DESI+CMB:
             w = -1.055 +/- 0.036, entered as the exact rationals
             w_mean = -211/200 and sigma = 9/250. HEADLINE: True, on the
             abstract's own designation of the DESI+CMB combination among
             the release's principal reported results. Quoted summary only;
             no re-fit, no raw data.
SYSTEMATICS  (a) readback provenance: the drafting environment's network
             egress policy blocks arxiv.org and every science host, so the
             analyst could not re-read the table independently; the quoted
             values enter on the owner's public readback of 2026-08-26
             (recorded in issue #576 before this pin) and are auditable by
             any reader against the public paper. A demonstrated misquote
             of the source is a defect: fresh probe, new identity.
             (b) override clause: per the same readback the source paper
             prints no credible-interval or exclusion statement about
             w = -14/15 in the wCDM model, so the Gaussian witness governs;
             if such a printed statement exists it overrides in both
             directions, and one found after the pin that reverses the
             decision is a defect: fresh probe, new identity.
             (c) single-row record: the source table carries further wCDM
             combinations that are not on this frozen record. R1 is
             existential over HEADLINE wCDM fits, so absent rows cannot
             manufacture this firing and cannot undo it; the recorded
             decision rests on the quoted row alone.
             (d) decimal-to-rational entry is checked inside the verifier:
             Fraction("-1.055") = -211/200 and Fraction("0.036") = 9/250
             are asserted, so the freeze cannot silently drift from the
             printed decimals.
THRESHOLD    rule R1 verbatim above, inherited. Immutable. The bar 322/125
             is asserted equal to the P-DE-W-ARMING-1 constant.
LAYER        L6, reading only. The fired rule sends DE-W-CONSTANT [H] to F
             at the next sealed fold; no T, D, or C row moves;
             COSMOLOGY-REGISTER [D] is unchanged as the source of the
             committed form; DE-CONFORMAL-WEIGHT [O] is untouched in both
             outcomes and per its CIRCULAR clause this row is never a
             selection premise there, fired or not.
```

## Lineage and disclosure

The rule engine and thresholds descend from `P-DE-W-ARMING-1` (public claim
lock issue #442, pin commit `516538cd73b35e3e2877acd5382e0e188638a706`);
this probe adds no rule and moves no threshold. The probe is RESULT-EXPOSED:
the exact arithmetic below was computed publicly in the owner's review of
2026-08-26 and again in issue #576, both before this pin. The candidate
verifier was smoke-executed in the drafting worktree before the pin; the
first smoke run exposed a malformed cross-product guard inside gate G7
(wrong arithmetic in the check itself, not in the witness), which was fixed
before the pin, and the rerun revealed nothing not declared here. Smoke
runs are not evidence. The
single accepted formal execution happens only after this preregistration
and the verifier are pinned and pushed; its stdout becomes `EXPECTED.txt`.

Sealed invocation:

```text
python3 probes/P-DE-W-ARMING-2/verify.py
```

## The frozen record and the exposed arithmetic

```text
entry:      DESI DR2, fit wCDM, combination DESI+CMB, HEADLINE
            w_mean = -211/200, sigma = 9/250, source arXiv:2503.14738v3
witness:    |z| = |w_mean + 14/15| / sigma
            = |(-633 + 560)/600| / (9/250)
            = (73/600) * (250/9)
            = 365/108
bar:        322/125
decision:   365/108 >= 322/125 because 365 * 125 = 45625 > 34776 = 322 * 108;
            margin 365/108 - 322/125 = 10849/13500. R1 FIRES.
```

Decimals behind the rationals are the survey's printed values; the
conclusion is the exact rational comparison, nothing else.

## Proposed fold edits (a later sealed fold, not this probe)

`DE-W-CONSTANT` moves `H -> F` with evidence `probes/P-DE-W-ARMING-2`
alongside the arming record `probes/P-DE-W-ARMING-1`; one FIRE lifecycle
event enters `canon/HISTORY.tsv`; the row leaves the live frontier and its
program-table row is retired. Ledger delta: H 3 to 2, F 16 to 17, live H/O
30 to 29, program rows 30 to 29; claims, T, D, C, O counts, gates,
dependencies, evidence grades of other rows: unchanged. The fold wording
records the fired witness exactly as frozen here.

## Non-claims

No derivation of w from J is claimed and none is refuted: the fired object
is the committed register reading, not COSMOLOGY-REGISTER [D] itself, which
remains a dictionary row. No statement is made about the w0waCDM evolution
preferences on `P-DE-W-ARMING-1`'s record. No cosmological conclusion is
asserted beyond the exact rational comparison of one quoted posterior
summary against one frozen threshold.

## Threshold immutability

A defect found in this probe after the pin means a fresh probe with a new
identity. No amendment, no rebase, no force-push, no threshold movement, no
reinterpretation of HEADLINE, the override clause, or the readback after
data.
