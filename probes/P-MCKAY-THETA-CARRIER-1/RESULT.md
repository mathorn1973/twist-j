# P-MCKAY-THETA-CARRIER-1 result

Status: FORMAL PROBE RESULT; PUBLIC CLAIM UNREGISTERED

## Decision at the recorded leg

```text
verdict: ALL PASS (9 gates)
exit:    0
stderr:  empty
```

No preregistered falsifier fired on the first formal execution (see EXPECTED.txt
for the per-gate witnesses), and two immediate repeats reproduced that stdout
byte-identically. The conclusion is proof-first: `verify.py` audits the finite
witnesses only; the theorem rests on the proof frozen in PREREG.md.
This record supplies the local aarch64 leg. The strict two-architecture gate completes only if the required GitHub x86_64 check reproduces EXPECTED.txt byte-identically under the same verifier hash.
This probe changes no normative Canon file; registration is a separate sealed
fold (see notes/canon/PATCH-2026-07-17-rh-lane.md). RH remains O.
