# RESULT P-CENTRAL-LIFT-PHASE-1

## Decision

**FORMAL RESULT PASS; TWO-ARCHITECTURE GATE SATISFIED.**

The pinned verifier at commit
`0c8adc4ea22b88c5fb65f78ea567cd4e04f9aa26` was executed exactly once
after the public pin. It exited 0 with empty stderr and produced 10 of
10 PASS gates. Its exact stdout is the committed `EXPECTED.txt`,
SHA-256
`0609c48f3df68d79c0cea9fd38cbccaab14ad908590f00767a51322944a994cc`,
826 bytes and 11 lines.

The required GitHub x86_64 and aarch64 jobs independently reran the
same pinned verifier. Both exited successfully, enforced empty stderr,
and produced stdout byte-identical to the same committed
`EXPECTED.txt`. The local x86_64 leg and the recorded GitHub aarch64
leg differ in architecture, satisfying the POLICY section 4
two-architecture computation gate.

### Chronology and post-CI ratification

The first version of this `RESULT.md` was committed in
`59a55ecef8bb64e87f9eee97459ca0f9bc3cda89` after the local formal
execution and before the required GitHub jobs had completed. It was
therefore provisional only as to the two-architecture conclusion.
Workflow run `30750743452` subsequently passed on that exact PR head:
aarch64 job `91504236573` and x86_64 job `91504236569` both reported
`VERIFY PASS` for verifier SHA-256
`d062a009a98db0e1c26f1c95b2e3df04f04f14a79f68df4ec7784a9d8d40e163`
and stdout SHA-256
`0609c48f3df68d79c0cea9fd38cbccaab14ad908590f00767a51322944a994cc`;
aggregate job `91504252562` passed.

Commit `160af09af09dd0b16b207b88914171cdb4e664c6` then recorded the
required aarch64 leg in `RUN.md`. Workflow run `30751810897` passed on
that structured-record head: aarch64 job `91507054033` and x86_64 job
`91507053994` both reported
`RUN RECORD P-CENTRAL-LIFT-PHASE-1 TWO-ARCHITECTURE` and repeated the
same `VERIFY PASS` hashes; aggregate job `91507074426` reported
`TWO-ARCHITECTURE CHECK PASS`. This paragraph ratifies the
two-architecture conclusion after the evidence and validated record
existed. It changes no frozen equation, proof, verifier, expected
output, threshold, falsifier, scope, or action layer.

The frozen decisions are audited positively:

```text
E1  projective fifth and central spinor sign       E1          PASS
E2  normalized Herm/Sym scalar laws, J action,
    fifth power, and central zeta^2 factor         E2A-E2D     PASS
E3  finite terminal certificate supporting the
    universal unit-phase proof, and primitive
    tenth-root obstruction                         E3A-E3B     PASS
R   inherited public cyclotomic inputs             R1-R3       PASS
```

## Falsification

No scientific falsifier fired. F-CLP-1 through F-CLP-3 were frozen
before execution and remain armed. No threshold, equation, scope, or
action layer moved after the pin.

## Status and scope

- The finite verifier evidence satisfies the two-architecture
  computation gate and earns at most `C` on computation alone.
- The owner explicitly accepted `PREREG.md` section 7 as an independent
  theorem-grade proof before the pin. That proof makes `T` available at
  exactly the frozen E1-E3 scope; the verifier audits the exact
  certificates supporting it.
- The probe is RESULT-EXPOSED and confirmatory: its incubation output
  was public before the pin.
- The result is L4 quadratic support only. It owns no Herm2
  positive/Born/causal cone or boundary, split-unit projectors, boost
  rigidity, icosian order, ramified glue, diagonal integrality, integral
  or twisted tick or tick ladder, physical time, bit, U(1),
  electromagnetism, decoder data, `QCarrier`, `MatterData`, L5 stream,
  L6 measure, or cross-layer lift.
- `QUADRATIC-DECODER-DATA` and every other live row remain unchanged.
  No registry, frontier, or Canon file is modified by this probe.

This record is ratified against workflow run `30751810897` after its
structured `TWO-ARCHITECTURE` classification and aggregate pass. A
failed exact gate or byte mismatch is retained; an infrastructure-only
failure is an integrity STOP, not a scientific negative result.
