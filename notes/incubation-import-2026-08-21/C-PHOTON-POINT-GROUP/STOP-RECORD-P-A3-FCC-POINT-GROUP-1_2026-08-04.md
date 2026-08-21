# STOP RECORD: P-A3-FCC-POINT-GROUP-1

```text
DATE       2026-08-04, evening
STATUS     STOP, owner-accepted. Issue #275 closed NOT_PLANNED. The sealed
           probe may not be amended, renamed or resumed; any new attempt
           needs a fresh identity and a new explicit owner decision.
PROBE      probes/P-A3-FCC-POINT-GROUP-1, branch probe/P-A3-FCC-POINT-GROUP-1
PIN        commit 5ebf5f0d93424ededf849f747f65aac25da287fe,
           "probe: pin A3 FCC point group preregistration",
           PREREG.md (548 lines, sha256 prefix 465bbb8a) and verify.py
           (881 lines, sha256 prefix e435849b). Remote readback of both
           SHA-256 and git blobs confirmed by the owner.
BREAK      fresh blind breaker, BREAK FOUND, report sha256
           33793e98ba17faa48334aa67e2ec2ab29fef7d8cdfd9c6ff9fc15378b41c95c9
           (owner-reported; the report file is not on the probe branch).
EXECUTION  the accepted verifier was NEVER run. No EXPECTED.txt, RUN.md,
           RESULT.md, no PR, no status movement. Main, Canon v36, issue
           #193 and QDD untouched. The branch stays as an immutable
           public audit record. Verified by this session from a fresh
           fetch: the branch carries exactly the pin commit.
```

## The five blockers, mapped to the sealed PREREG

```text
1  Z3/Z4 type transition       A01d (line 178): the root set is typed in
                               Z^4 while downstream gates consume Z^3
                               objects; the per-gate ambient was not
                               frozen tightly enough for a blind breaker
                               to derive the gate without guessing.
2  missing frozen F^-1         D01d (194) asserts "the displayed rational
                               inverse is exact" without the inverse
                               being frozen as a displayed formula.
3  unfrozen D3 generators      D01e (195) tests integral preimages of
                               "D3 basis generators" that the frozen text
                               does not fix.
4  missing quarter-turn        Q02c/Q02d (229, 230) and K10 (441) consume
                               "the frozen generator" of order four; no
                               quarter-turn matrix is frozen.
5  undetermined K11a mutation  K11a (442) rejects "a wrong shell-size
                               table" without determining which mutation.
```

All five are definitional self-containment failures of the probe
preregistration, exactly the class the gate design rule of the working
agreement exists to catch, caught by a blind breaker BEFORE execution.
This is the first live case where the cross-seat break discipline
produced a clean disagreement before any compute; the working agreement's
falsifier 3 asked for precisely this evidence that the pairing buys
something.

## What the STOP does and does not touch

It does not touch the mathematics. The candidate-grade facts of
C-PHOTON-POINT-GROUP-1 (order 48, full octahedral, icosahedral non-lift
240/24, invariant quartics dimension 2, shell anisotropies and the cone)
stand at candidate grade with their two-architecture byte-identical
record; the candidate branch notes/c-photon-point-group-1 (commit
56674bb2) is unaffected and remains valid handoff material. What died is
the attempt to carry that content into a public probe with a
preregistration that was not self-contained.

Honesty requires the mapping both ways: the same five gaps exist in
latent form in the candidate package itself. Its prereg also moves
between Z^4 and Z^3; it froze the isometry columns but not the explicit
inverse; the second D3 basis, the fourfold rotation of demo D5, and the
wrong-table mutation of demo D6a live in code, not in the frozen prereg
text. At candidate grade that was acceptable; at probe grade it is not,
and the breaker proved it.

## Freeze list for any future fresh-identity attempt (owner decision first)

```text
1  one ambient per gate: state for every gate whether it lives in Z^4
   (A_3 model) or Z^3 (D_3 model); treat the isometry itself as a gated
   claim with BOTH matrices displayed, F and its exact inverse
   (2 F^-1 is integral; display it).
2  freeze the D_3 generators in the prereg text, with their Gram.
3  freeze the quarter-turn as an explicit matrix wherever a gate
   consumes it.
4  determine every mutation: an expected-fail demonstration names its
   exact mutated input in the frozen text, not in code.
5  the blind-breaker test before pinning: can a reader derive every
   gate's pass and fail condition from the PREREG alone, without the
   verifier? If not, it is not ready to pin.
```

No relaunch, no amendment, no rename from this side. The next move on
this lane, if any, is the owner's.
