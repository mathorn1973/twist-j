# P-DE-W-ARMING-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / ARMING / RULES AND CARRIER FROZEN`

This probe arms one empirical hypothesis: the dark-energy equation of state
read from the committed register form of `COSMOLOGY-REGISTER [D]`,

```text
w_DE(a) = -14/15 = -1 + 1/(d p),  d = 3,  p = 5,  exactly and constant,
equivalently rho_DE proportional to a^(-1/5),
```

in the standard flat FRW fluid convention. The probe freezes the falsifier
rules and the data carrier for a proposed registry row `DE-W-CONSTANT [H]`,
and evaluates those rules on the current published record. The registry,
frontier, and Canon are not touched by this probe; the row itself can enter
only through a later sealed fold that consumes this probe as evidence.

The result is exposed before execution: on the current record the row is

```text
ARMED, HOLDS (fires nothing today; four witnesses at or above 3 sigma)
```

The probe is an arming record and an exact audit, not a discovery engine.

## Public identity, authority, and action layer

```text
probe:               P-DE-W-ARMING-1
public claim lock:   issue #442
probe owner:         A. M. Thorn / delegated session de-w-arming-2026-08-19
branch:              probe/P-DE-W-ARMING-1
basis:               Public Canon v54, main 483591d, tag canon-v54,
                     CONTENT_COMMIT 0bfd67b4, SHA256SUMS 5 of 5 OK
action layer:        L6, reading only; no layer lift is performed and no
                     gate is consumed
authority:           none until folded; a fired falsifier sends the H row
                     to F and moves nothing else
```

## Falsifier, first

The proposed row `DE-W-CONSTANT [H]` fires, and folds as F, exactly when a
carrier release meets one of the frozen rules R1 or R2 below. Nothing else
fires it, and the thresholds never move.

```text
R1 CONSTANT-FIT EXCLUSION. In a HEADLINE flat constant-w (wCDM) fit of a
   carrier release, w = -14/15 is excluded at or above the 99 percent
   two-sided credible level. Gaussian witness convention: the exact ratio
   |z| = |w_mean + 14/15| / sigma at or above 322/125; a credible-interval
   or exclusion statement printed by the source paper overrides the
   Gaussian witness in both directions.
R2 CONFIRMED EVOLUTION. One carrier collaboration reports evolving dark
   energy (w_a != 0, or an equivalent rejection of constant w) at or above
   5 sigma in its HEADLINE combination; or two carrier collaborations each
   report it at or above 3 sigma from combinations sharing NO primary
   dataset (the disjointness clause; any published combination qualifies
   for this leg). Comparisons are at-or-above, not strictly-above.
R3 WITNESS BAND. Tension at or above 2 sigma in a constant-w fit, or an
   evolution preference at or above 3 sigma that R2 does not fire, is
   recorded as a labeled witness, fires nothing, and must never be used to
   soften or postpone R1 or R2.
```

## The six fields

```text
EQUATION     w_DE(a) = -14/15 exactly, constant in a, standard flat FRW
             fluid convention; equivalently rho_DE ~ a^(-1/5); equivalently
             Delta_DE = 1/5 for d rho_DE/d chi = -Delta_DE rho_DE with
             chi = log a. Source of the number: COSMOLOGY-REGISTER [D].
CODE         probes/P-DE-W-ARMING-1/verify.py. Python standard library
             only, exact Fraction arithmetic, no float in any assertion or
             printed value, deterministic stdout, well under 120 seconds,
             run from the repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
CARRIER      the cosmology releases of four named collaborations: DESI
             (DR2 and later), DES (Y6 and later), Euclid, CMB-S4, each
             evaluated as published (quoted posterior summaries and stated
             significances; no re-fit, no raw data). HEADLINE means the
             combination the collaboration's own abstract or summary
             designates. Current record frozen in verify.py: DESI DR2
             (arXiv:2503.14738) and DES Y6 (arXiv:2605.27221).
SYSTEMATICS  (a) supernova-sample dependence: all published SN combinations
             are recorded; only a HEADLINE combination can fire R1 or the
             R2 single leg. (b) shared data: the DES Y6 headline reuses
             DESI BAO and CMB, so collaboration independence is not
             evidence independence; the R2 double leg therefore requires
             disjoint primary datasets, and the primary-dataset labels are
             frozen in verify.py. (c) Gaussian witness versus the paper's
             own statement: the paper overrides. (d) prior-volume effects
             in (w0, wa) fits: R2 keys on collaboration-stated
             significances only. (e) lineage disclosure below.
THRESHOLD    rules R1, R2, R3 verbatim above. Immutable.
LAYER        L6, reading only. Firing sends the proposed H row to F;
             no T, D, or C row moves. DE-CONFORMAL-WEIGHT [O] is untouched
             in both outcomes, and per its CIRCULAR clause this row is
             never a selection premise for it.
```

## Lineage and disclosure

This probe carries a promotion in from an incubation lane, candidate
`C-DE-W-ARMING-1`. The lane's preregistration was frozen BEFORE any
publication was opened in that session (prereg SHA-256
`2ef041268f3f2c4849341919b8060de9ef9d6fc1706fa29665e365e5085c3cab`, with an
analyst-knowledge disclosure inside), the data were opened afterward, and
the lane's rules were applied without amendment. The DES Y6 release was
unknown at that freeze and outside the lane's carrier; the owner decision of
2026-08-19 (recorded in issue #442) widens the carrier to include DES and
adds the disjointness clause, before this public pin. Because the record was
already evaluated in the lane, this probe is RESULT-EXPOSED: its decision on
the current record, `ARMED, HOLDS`, is declared above, and the candidate
verifier file was smoke-executed once before this pin, outside the
repository, revealing nothing not declared here. The single accepted formal
execution happens only after this preregistration and the verifier are
pinned; its stdout becomes `EXPECTED.txt`.

Sealed invocation:

```text
python3 probes/P-DE-W-ARMING-1/verify.py
```

## What the current record contains, frozen

Six quoted w0waCDM preference significances, entered as exact rationals with
frozen primary-dataset labels: DESI DR2 at 31/10 (BAO+CMB, headline), 28/10,
38/10, 42/10 (adding Pantheon+, Union3, DESY5); DES Y6 at 22/10 (DES alone)
and 30/10 (DES+DESI-BAO+CMB, headline). No in-carrier collaboration
constant-w (wCDM) posterior summary is on this frozen record, so R1 is
recorded PENDING exact table readback of the DESI DR2 constant-w fit; a
future evaluation of R1 on that table belongs to a fresh probe, not to an
amendment of this one. Decimals behind these rationals are measured survey
witnesses, never conclusions.

## Proposed fold edits (a later sealed fold, not this probe)

Registry, one new row (tab-separated fields):

```text
DE-W-CONSTANT	H	the dark-energy equation of state read from the committed register form w = -14/15 = -1 + 1/(d p), d = 3, p = 5: exactly -14/15 and constant in a, equivalently rho_DE proportional to a^(-1/5), in the standard flat FRW fluid convention; a reading of COSMOLOGY-REGISTER; no derivation from J, no dictionary source, and no selection premise for DE-CONFORMAL-WEIGHT is claimed or supplied	18. The frontier	probes/P-DE-W-ARMING-1	live: fires if a carrier release (DESI, DES, Euclid, CMB-S4) excludes w = -14/15 at or above the 99 percent credible level in its headline constant-w fit, or reports evolving dark energy at or above 5 sigma in one headline combination, or two carrier collaborations each report it at or above 3 sigma from combinations sharing no primary dataset; witnesses as of 2026-08: DESI DR2 31/10 sigma (BAO+CMB) with 19/5 and 21/5 sigma adding Union3 and DESY5, DES Y6 30/10 sigma on shared data and 11/5 sigma alone; witnesses fire nothing
```

Frontier: one new entry in the Geometry and cosmology group, queue FOLLOWUP,
state BLOCKED between carrier releases, mode EMPIRICAL, in the NS-TILT
pattern. Program table: `DE-W-CONSTANT COSMOLOGY FOLLOWUP BLOCKED
EMPIRICAL`. Canon: one paragraph after the COSMOLOGY-REGISTER passage,
neutral wording, stating the arming and the untouched status of
DE-CONFORMAL-WEIGHT. Ledger delta: claims +1, H 2 to 3, live 26 to 27,
nothing else moves.

## Non-claims

No derivation of w from J is claimed. No dictionary source is selected.
COSMOLOGY-REGISTER [D] is unchanged as the source of the committed form.
DE-CONFORMAL-WEIGHT [O] is unchanged, and this row must never be used as a
selection premise there. The witnesses recorded here confirm nothing; a
consistent witness is not evidence of derivation, and the row's only public
life is the exposure of one exact rational to named future measurements.

## Threshold immutability

A defect found in this probe after the pin means a fresh probe with a new
identity. No amendment, no rebase, no force-push, no threshold movement, no
reinterpretation of the carrier or the disjointness clause after data.
