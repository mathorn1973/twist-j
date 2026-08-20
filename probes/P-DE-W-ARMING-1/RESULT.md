# P-DE-W-ARMING-1 result

Status: `ARMED, HOLDS / RESULT-EXPOSED CONFIRMED / CANON UNCHANGED`

## Disposition

```text
arming record:   COMPLETE. The falsifier rules and carrier for the proposed
                 row DE-W-CONSTANT [H] are frozen and publicly pinned.
current record:  HOLDS. Nothing fires on the frozen 2026-08 record.
integrity:       no STOP. One formal execution, exit zero, empty stderr,
                 10 of 10 gates PASS, stdout equal to EXPECTED.txt.
```

The single formal execution reproduced the exposed result exactly. The
frozen record carries six quoted w0waCDM preference significances from the
two carrier releases published to date (DESI DR2, arXiv:2503.14738; DES Y6,
arXiv:2605.27221), entered as exact rationals with frozen primary-dataset
labels.

## What the gates decided

Rule R1 (headline constant-w exclusion of `-14/15` at or above the 99
percent level): PENDING. No in-carrier collaboration constant-w posterior
summary is on the frozen record; its future evaluation on the DESI DR2
constant-w table, or on any later carrier release, belongs to a fresh probe.

Rule R2 single leg (one headline at or above 5 sigma): does not fire. The
headline maxima are 31/10 sigma (DESI DR2, BAO+CMB) and 3 sigma (DES Y6,
DES+DESI-BAO+CMB).

Rule R2 double leg (two carrier collaborations, each at or above 3 sigma,
from combinations sharing no primary dataset): does not fire. Four entries
sit at or above 3 sigma, but every cross-collaboration pair among them
shares DESI BAO and CMB. The counterfactual is recorded by gate G7: with
the disjointness clause removed, the leg would fire today on shared data,
so the clause is decision-bearing now, not hypothetically. The only
disjoint cross-collaboration candidate, DES alone, carries 11/5 sigma,
below the bar; and the DES headline sits exactly on the 3 sigma bar, so
the frozen at-or-above semantics is decision-relevant and is recorded.

Rule R3 witnesses: four, recorded and firing nothing: DESI DR2 at 31/10
(BAO+CMB), 19/5 (Union3), 21/5 (DESY5), and DES Y6 at 3 (shared-data
headline).

## Scope boundary

This probe changes no Canon, Registry, Frontier, workflow, gate, or
existing probe file. The row DE-W-CONSTANT [H] does not exist until a
later sealed fold creates it; the exact proposed edits are frozen in
`PREREG.md`. No derivation of `w = -14/15` from `J` is claimed, no
dictionary source is selected, `COSMOLOGY-REGISTER [D]` is unchanged as
the source of the committed form, and `DE-CONFORMAL-WEIGHT [O]` is
untouched and never takes this row as a selection premise. A future firing
of R1 or R2 on a new carrier release is evaluated by a fresh probe against
the rules frozen here and sends the folded row to F; the reading dies and
nothing else moves. A fired falsifier is first-class progress.

## Evidence boundary

The local formal leg is x86_64 (Ubuntu 24.04.4 LTS, CPython 3.11.15). The
pull-request workflow reruns the pinned verifier on GitHub x86_64 and
native aarch64 and requires byte-identical stdout against `EXPECTED.txt`;
those runs complete the repository two-architecture computation gate for
this arithmetic. The scientific content of the probe is an arming: the
computation it pins is exact rational bookkeeping over quoted published
summaries, and the two-architecture replay audits that bookkeeping. It
cannot add physical meaning; the physical exposure begins when the fold
puts DE-W-CONSTANT [H] on the live frontier.
