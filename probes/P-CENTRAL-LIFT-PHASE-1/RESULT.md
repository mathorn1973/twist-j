# RESULT P-CENTRAL-LIFT-PHASE-1

## Decision

**LOCAL FORMAL LEG PASS; REQUIRED GITHUB LEGS PENDING.**

The pinned verifier at commit
`0c8adc4ea22b88c5fb65f78ea567cd4e04f9aa26` was executed exactly once
after the public pin. It exited 0 with empty stderr and produced 10 of
10 PASS gates. Its exact stdout is the committed `EXPECTED.txt`,
SHA-256
`0609c48f3df68d79c0cea9fd38cbccaab14ad908590f00767a51322944a994cc`,
826 bytes and 11 lines.

The local leg audits the frozen decisions positively:

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

No scientific falsifier fired on the local formal leg. F-CLP-1 through
F-CLP-3 were frozen before execution and remain armed. No threshold,
equation, scope, or action layer moved after the pin.

## Status and scope

- The owner explicitly accepted `PREREG.md` section 7 as an independent
  theorem-grade proof before the pin. That proof makes T available at
  exactly the frozen E1-E3 scope; the verifier is its audit.
- The required pull-request workflow has not yet rerun the pinned
  verifier on GitHub x86_64 and aarch64. This result therefore does not
  claim the two-architecture computation gate or final PR closure.
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

This record must be ratified only after the required GitHub x86_64 and
aarch64 jobs and their aggregate `check` pass byte-identically. A failed
exact gate or byte mismatch is retained; an infrastructure-only failure
is an integrity STOP, not a scientific negative result.
