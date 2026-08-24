# FOLD RECORD. Public Canon v55, arm DE-W-CONSTANT [H]

Status: `LANDED / TAGGED / RELEASED / ALL GATES PASS`. Public line only. This
document is a record, not an authority. `STATUS.md` on
`mathorn1973/twist-j main` is the only statement of what the Canon is.

Session: canon-v55-fold-2026-08-20. Lane: public validation, not incubation.

## What landed

One new registry row, `DE-W-CONSTANT [H]`, exactly as frozen in the pinned
public preregistration of probe `P-DE-W-ARMING-1`. The committed dark-energy
form `w = -14/15 = -1 + 1/(d p)`, `d = 3`, `p = 5`, exactly and constant in
`a`, equivalently `rho_DE` proportional to `a^(-1/5)`, in the standard flat
FRW fluid convention, is now a live empirical exposure with an immutable
falsifier on named survey releases.

Second empirical frontier row in the public series, beside `NS-TILT [H]`.
First fold since the cutover to put two armed empirical rows on the frontier
at once.

## The chain, in order

```text
probe merge     PR #443 merged without squash at e61af13f7789430d7fea262d19135f0399dc74de
                probe branch probe/P-DE-W-ARMING-1 retained, not deleted
                independent replay outside the workflow (Ubuntu 24.04 x86_64,
                CPython 3.11, fresh clone) reproduced stdout
                cb55279b43f82504fddb0ca35a0ec28e35b0cb5bdf6514b96c061f84966b66f1,
                2061 B, exit 0, empty stderr, byte-identical to EXPECTED.txt
claim readback  issue #442 carries the merge and the fold pointer
fold branch     release/canon-v55, exactly two frozen commits
  content       6236c10cd89e0a3a53fca730f50c50c237d4add0
                canon: fold DE-W-CONSTANT arming into Public Canon v55
  release form  fc9105b599eefefdbb65d381a3a90833136cbb42
                release: activate Public Canon v55
fold PR         #444, CI green on the widened canon/ sweep:
                architecture-aarch64 PASS 13m09s, architecture-x86_64 PASS 15m21s,
                aggregate check PASS
merge           70e1c480b3ee8890fbcd97c21dd586f5713f0ffe, no squash, no rebase
readback        fresh clone of main: STATUS fields, SHA256SUMS 5 of 5 OK,
                CONTENT_COMMIT ancestor of HEAD, both frozen commits present
tag             canon-v55 on the merge commit, publication job success
release         Public Canon v55, immutable, Latest; assets validated by download
                before publication and revalidated by the release-event job
```

## Release form

```text
STATE:          ACTIVE
CANON:          Public Canon v55
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v55
CONTENT_COMMIT: 6236c10cd89e0a3a53fca730f50c50c237d4add0
CANON_SHA256:   e22ebb5648611780743122da67ec965394c3f97ed18b99079be028ca6ebb47a9
CANON_BYTES:    282461
```

## Ledger delta, signed term by term

```text
claims:    279 + 1 empirical row = 280
H:         2 + 1 = 3
live H/O:  26 + 1 = 27
T: 165, D: 43, C: 30, O: 24, F: 15, all unchanged
normative items: 324 + 1 = 325
dependencies:    486 + 3 = 489
evidence rows:   279 + 1 = 280
history rows:    797 + 1 = 798
two-architecture evidence: 197 + 1 = 198
reproductions: 23, gates: 10, programs: 7, unchanged
```

Exactly the delta the frozen preregistration declared. Nothing else moved.

## Evidence pins

```text
probe bundle   probes/P-DE-W-ARMING-1
               539cd6ab4ba7bda6c921b7e947b705b031f92373f4761836383f5fd5dc8f5727
               bundle-manifest-sha256-v1, two-architecture
registry scope 5939c19b49fbf9e80e8dba4188fae2c127580b457bed1816af4aa2eb248240ff
registry row   da0f321548f3f5feaed49fc5f5ec8fe2ce2b46095d4ccb08d0a3eee356cedebc
history event  CANON55-DECLARE-DE-W-CONSTANT, 2026-08-20, canon-v55-candidate
normative      DE-W-CONSTANT HYPOTHESIS H NOT_APPLICABLE, no gate
program row    DE-W-CONSTANT COSMOLOGY FOLLOWUP BLOCKED EMPIRICAL
dependencies   COSMOLOGY-REGISTER -> DE-W-CONSTANT   BOUNDED_BY
               DE-CONFORMAL-WEIGHT -> DE-W-CONSTANT  BOUNDED_BY
               DE-W-CONSTANT -> DEF-ARCHITECTURE     REQUIRES
```

The committed registry row was verified byte for byte against the row frozen
inside the pinned public `PREREG.md`. Nothing was reworded after the pin.

## Two-platform authoring

Every changed file was authored and checked on Ubuntu 24.04 x86_64 with
CPython 3.11 and reproduced independently on macOS aarch64 with CPython 3.13
before the push. All sixteen content-fold files and all three release-form
files carry identical SHA-256 on both platforms, including the regenerated
`reproduce/status-separation/EXPECTED.txt`
(`4a516f17b3c17f4c6b195ee7fb57b25f272df365c21b4464b89a97065998cabb`, 5986 B).
GitHub then reran the whole widened sweep on x86_64 and aarch64.

## Audit witness

`reproduce/status-separation` gained one check at position 46 of 47. It pins
the new row at `H` on the public-probe two-architecture bundle, the
`NOT_APPLICABLE` layer with no gate, the
`COSMOLOGY/FOLLOWUP/BLOCKED/EMPIRICAL` program tuple, exactly the three
declared dependency edges, and the unchanged statuses of
`COSMOLOGY-REGISTER [D]`, `DE-CONFORMAL-WEIGHT [O]` and `NS-TILT [H]`. Its
count check reads the folded tree. `RESULT 47/47 ALL PASS`.

## What is exposed now, and what fires it

```text
R1 CONSTANT-FIT EXCLUSION   a headline flat constant-w fit of a carrier
                            release excludes w = -14/15 at or above the
                            99 percent two-sided credible level
R2 CONFIRMED EVOLUTION      one carrier collaboration reports evolving dark
                            energy at or above 5 sigma in its headline
                            combination; or two carrier collaborations each
                            report it at or above 3 sigma from combinations
                            sharing no primary dataset
R3 WITNESS BAND             at or above 2 sigma tension, or an at or above
                            3 sigma evolution preference that R2 does not
                            reach, is recorded, fires nothing, and never
                            softens or postpones R1 or R2
carrier                     DESI, DES, Euclid, CMB-S4
```

On the record frozen by the probe the row holds. Four witnesses sit at or
above 3 sigma and every cross-collaboration pair among them shares DESI BAO
and CMB; the only disjoint cross-collaboration candidate, DES alone, carries
11/5 sigma. The next genuinely independent leg at or above 3 sigma fires the
row. DESI DR3, Euclid, a DES continuation and CMB-S4 are all pointed at it.

A fired falsifier here is first-class progress: the row goes to F, the
reading dies, and nothing else moves.

## Open, carried forward

```text
R1 readback   no in-carrier collaboration constant-w posterior summary is on
              the frozen record. The exact DESI DR2 wCDM table readback is a
              FRESH probe with a new identity, never an amendment of
              P-DE-W-ARMING-1. Not blocking; the row is live either way.
STATUS drift  STATUS.md carries CUTOVER: 2026-08-19. It read 2026-07-13
              through v52 and changed at the v53 activation. The project
              contract states the cutover as 2026-07-13. Left untouched by
              this fold because it is outside the frozen edits and a
              normative field is not corrected in passing. Owner decision.
```

## Non-claims, restated

No derivation of `w` from `J` is claimed. No dictionary source is selected.
`COSMOLOGY-REGISTER [D]` is unchanged as the source of the committed form,
with its comparisons fenced. `DE-CONFORMAL-WEIGHT [O]` is unchanged and open
and never takes this row as a selection premise; the CIRCULAR clause of that
obligation governs. No gate was created and no layer lift was performed. A
consistent witness is not evidence of a derivation.
