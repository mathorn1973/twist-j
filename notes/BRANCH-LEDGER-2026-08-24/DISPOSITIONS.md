# Branch dispositions, 2026-08-24

Status: **NON-CANONICAL. PROPOSAL TO THE OWNER.**

A disposition for each of the 94 divergent and orphan refs in
`BRANCH-LEDGER.tsv`, so that every ref that holds unique content has a
recorded decision. This proposes; it closes nothing. No identifier is
consumed and no probe is sealed by this file.

```text
FOLD       28   finished work whose content should land
ARCHIVE    51   no pin, no obligation; superseded or historical. Keep the
                ref, record it, do no further work
ABANDON    13   pin frozen, gate never completed, closed by an ABANDONED
                record that spends the identifier
RETARGET    2   content belongs under a new identifier; the old identifier
                still owes its own ABANDONED record
```

## Abandoned pins: fifteen, not twenty-five

The naive filename filter (a path containing `PREREG`, none containing
`RESULT`) flags 25 refs. Opening them reduces that to **fourteen branch-level
pins, plus one sub-branch identifier, so fifteen records are owed.**

Eleven of the 25 are not abandoned. They carry a real result under a filename
the filter cannot see, or they never formed a pin at all:

```text
agent/c-jacobi-phase-cross-1        C-JACOBI-PHASE-CROSS-1.md, chi-square
                                    table, all NOT-REJECTED
codex/cm-2i-qcarrier-hardening      PREREG_DRAFT, never pinned; the gate ran
                                    on main at probes/P-CM-2I-QCARRIER-1
codex/entropy-mackey-consolidation  MANIFEST.tsv records source_state
                                    untracked: nothing was frozen in git
handoff/audit-euler-widder-depth-*  AUDIT-...md verdict block
handoff/audits-lambda-grid-*        AUDIT-LAMBDA-COCYCLE-GRID...md
C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N  BREAK-RESULT.md on a descendant ref,
                                    discharged on main
c-jacobi-...-canonical-h-review     REVIEW.md and REANALYSIS-STDOUT.txt
c-qdd-u-induced-null-anatomy-1-n    hit is a self-declared DRAFT prereg
c-rh-ray-finite-window-certificate-1-n
                                    EXPECTED.txt ends RESULT 10/10 ALL PASS
census-v2-and-photon-lane           hit is DRAFT, UNFROZEN, NOT FOR PIN
probe/P-QDD-INSTRUMENT-U-INDUCED-2  one PREREG_DRAFT.md, no verifier
```

The fifteenth record is not a branch. `notes/entropy-selection-recon-breaker-m2`
is itself finished, but carries
`notes/entropy_selection/PREREG-BREAKER-MACKEY4-2.md`, frozen on that ref
alone, with no `RESULT-BREAKER-MACKEY4-2` on any of the 203 refs. A per-branch
column cannot express it; it owes its own record.

## Two pins whose gate ran

Neither was simply never started, and both are why `POLICY.md` now defines an
abandoned pin by a gate that never **completed** rather than never executed:

```text
probe/P-QDD-FRESH-RECORD-NOFEEDBACK-1
    sole formal execution exited nonzero on a verifier fixture defect.
    Closed STOP / NO SCIENTIFIC CONCLUSION. The successor -2 already
    discloses this on main, before its own pin.
notes/c-rh-ray-finite-window-certificate-2-n
    the pinned wrapper failed during import before the engine ran; it was
    not repaired. The closing account is written in
    c-rh-ray-finite-window-certificate-3-n RESULT.md section 5.
```

Neither produced an exact stdout, so neither has an `EXPECTED.txt` or `RUN.md`
to commit, and neither can take the ordinary result route.

## Sequencing that the records depend on

```text
1  This cleanup lands first. POLICY.md on main contains no abandoned-pin
   rule today, so no ABANDONED record can honestly cite the policy it
   follows until this branch merges.
2  Fold c-rh-ray-finite-window-certificate-3-n before writing the record
   for -2-N, so the record can quote its integrity history instead of
   restating it.
3  Fold notes/c-jacobi-phase-cross-1-canonical-h-review only. The branch
   agent/c-jacobi-phase-cross-1 is its strict ancestor; folding both lands
   the same eight blobs twice.
4  notes/c-rh-weil-norm-junction-1-n is locked to issue #374, which is
   OPEN. It is the one candidate that must not be closed unilaterally.
5  probe/P-QDD-IDEMPOTENCE-DOMINATES-FORK-2 has no closure statement on any
   ref; its record has to be authored, not quoted.
```

## Three branches collide with this cleanup

Each modifies a file this cleanup also changes, so each needs a rebase and a
fresh reading before it can land:

```text
agent/incubation-contract       rewrites AGENTS.md
agent/incubation-checker        tools/check_policy.py, policy.yml
codex/lean-public-audit-policy  AGENTS.md, POLICY.md, tools/check_policy.py,
                                and a new root audits/, which also needs a
                                POLICY.md layout change to be admissible
```

## How far each row was checked

```text
adversarial  20   independently re-checked by a second reading whose brief
                  was to refute the first
direct       13   checked by hand against git for this file, including
                  every correction listed above
single-pass  61   one reading. All are FOLD or ARCHIVE, neither of which
                  consumes an identifier
```

Every one of the fifteen owed records was either adversarially re-checked or
verified by hand. No `ABANDON` rests on a single unreviewed reading.

The `has_prereg` and `has_result` columns in `DISPOSITIONS.tsv` are the
corrected values, not the filename-filter values; `BRANCH-LEDGER.tsv` keeps
the mechanical counts so the two can be compared.
