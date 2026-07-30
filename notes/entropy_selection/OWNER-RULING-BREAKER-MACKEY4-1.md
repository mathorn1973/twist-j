# OWNER RULING: retirement of PREREG-BREAKER-MACKEY4-1

```text
STATUS:      NON-CANONICAL OWNER RULING, INCUBATION LANE
AUTHORITY:   none. This is a protocol decision about evidence bookkeeping in
             the incubation lane. It is not a scientific claim and changes no
             public status.
DATE:        2026-07-30
OWNER:       A. M. Thorn / mathorn1973
PUBLIC BASIS: Public Canon v28, tag canon-v28,
             content 86a046007f89a64a696d013112a44f02e624dd2e
SUBJECT:     PREREG-BREAKER-MACKEY4-1
             sha256 d02badef96706f4c1e3f88edf1430e4641e2276245873b875e56f399fafc8a51
INSTRUMENT:  mackey4_break.py
             sha256 2bcb6ce2f009395e81f5904aef45475e8f165983003b6c4ca2d6aead86be6faa
SUCCESSOR:   PREREG-BREAKER-MACKEY4-2
             sha256 45192f7fcbe3b1699f69ccd35351c8a8ddc756e488a2f01ee0d0491e197f03e6
PUBLIC BRIDGE: unchanged. ENTROPY-LAYER-BRIDGE remains O / STOP.
```

## The ruling

```text
OWNER RULING: PREREG-BREAKER-MACKEY4-1 is retired in full.

The frozen preregistration states that a defect discovered after first
execution retires the breaker id. E9 was discovered after first execution
to be non-falsifiable by construction. No severability clause for individual
gates was frozen.

Therefore E1-E8 and E10-E13 retain discovery-history and diagnostic value
only and earn zero breaker credit. Their mathematical outputs are not
declared false, but any result required by the successor decision must be
re-established by PREREG-BREAKER-MACKEY4-2.

PREREG-BREAKER-MACKEY4-2 is the sole live successor instrument.
```

## Basis

The frozen clause reads "a defect in this preregistration discovered after
first execution retires this breaker id". It does not read "retires the
defective gate", and no severability clause for individual gates was frozen.
The retirement condition occurred exactly as written.

A retirement confined to `E9` would introduce severability after the result
was known. That is threshold movement after the preregistration pin, which
`POLICY.md` forbids.

## Effect on breaker 1

```text
PREREG-BREAKER-MACKEY4-1       RETIRED IN FULL

E1-E8, E10-E13
  mathematical value           preserved
  diagnostic value             preserved
  status                       discovery history
  breaker credit               0

E9
  instrument defect
  could not discharge its intended falsification role
```

The artifacts stay committed and unedited: `PREREG-BREAKER-MACKEY4-1.md`,
`mackey4_break.py`, `mackey4_break.stdout.txt`, and
`RESULT-BREAKER-MACKEY4-1.md`. Retirement withdraws evidential credit; it does
not delete or rewrite a record, and it does not declare any computed value
false. The adjudication in `MACKEY4-BREAKER-RESULT.md` is likewise preserved,
with its section 3 now reading as discovery history rather than as
corroboration.

## PREREG-BREAKER-MACKEY4-2 is not amended

The successor preregistration is frozen at
`45192f7fcbe3b1699f69ccd35351c8a8ddc756e488a2f01ee0d0491e197f03e6`. It records
the retirement question as open and requires the Mackey menu as secondary
output `G5` precisely so that a total-retirement ruling costs no third
instrument. That requirement is unchanged by this ruling, so the file needs no
amendment and must not receive one. Editing it would break its freeze pin and
would be threshold movement after the pin.

This ruling supersedes the "open owner ruling" wording of that file's
introductory section. The frozen expected values, thresholds, controls, and
scope of `PREREG-BREAKER-MACKEY4-2` are untouched.

## What the successor does and does not re-establish

Full retirement makes this mapping load bearing, because everything not
re-established by a live instrument now rests on the primary route alone.

```text
Re-established by PREREG-BREAKER-MACKEY4-2 when it runs:

E4    recurrent core and halves          C1, checked against the frozen spec
E6    313 components, 312 x 20 + 1 x 10  implied by C3 and G2
E7    312 generic halves regular D_5     C3, G2, both sides
E8    singlet D_5/C_2                    C3, G2
E9    common cocycle                     C2-C6, G1, G3, G4  (the decision surface)
E10   Mackey menu, all eight subgroups   G5
E11   629 not in the menu                G5
E12   mixed control (2,5)                G5

NOT re-established by PREREG-BREAKER-MACKEY4-2:

E1    SNF invariant factors (5,5,5,25), additive type Z/25 + (Z/5)^3
E2    J cycle type 1^1 4^1 20^156, unique fixed class, order 20
E3    dyadic component law and c_src = 158, 315, then 629 for r >= 2
E5    mirror law
E13   embedding arithmetic, translation transitivity, and the kernel
      relation gates: five involutions, (bc)^5 = id, and the M_J step identity
```

### Residual gap, stated plainly

`PREREG-BREAKER-MACKEY4-2` is scoped to the target side. The entire source
side is outside it. After this ruling, and after that successor runs
successfully, the obstruction stands as follows:

```text
629, the source component count at r >= 2   primary route only, no live breaker
the target menu {313,625,1563,3125}         primary plus the live successor
```

The obstruction is the statement that 629 is not in the menu. Half of that
statement will still rest on one implementation, one platform, one run. The
successor closes the premise that carried the most weight, not the whole
decision surface.

This is a consequence of the ruling, not an objection to it. It is recorded so
that no successor summary reads the eventual `PREREG-BREAKER-MACKEY4-2` result
as restoring the full two-route position.

Closing it requires a companion preregistration under its own new identifier,
scoped to `E1`, `E2`, `E3`, `E5` and `E13`, with a source presentation
distinct from the primary's lambda-digit arithmetic. It is disjoint from the
successor and may run in parallel. It is not opened by this ruling.

## Operating instructions

```text
1  Do not open a pull request yet. The bundle opens as one draft pull request
   against notes/entropy-selection-recon only after the successor instrument
   has been frozen and run. It carries: this ruling, the live prereg 2, the
   frozen mackey4_cocycle.py, its run record, its result record, and the
   updated RECON-V28-STATUS.md.
2  The implementing session must be clean. It must not receive the
   adjudicating conversation, a project summary, a handoff digest, or any
   paraphrase of the forbidden files. A "do not read these files" instruction
   is not sufficient if the content reaches the session by another route.
   Its permitted input package is exactly the one listed in
   PREREG-BREAKER-MACKEY4-2, independence declaration.
3  The session that wrote PREREG-BREAKER-MACKEY4-2 has read mackey4_verify.py
   and mackey4_break.py and is disqualified from implementing it.
4  Freeze mackey4_cocycle.py and record its SHA-256 before any comparison
   against the frozen expected values.
5  No public issue, formal probe, registry row, frontier change, Canon patch,
   or status change is authorized by this ruling or by the successor run.
   Every statement mentioning 629 keeps the r >= 2 scope.
```
