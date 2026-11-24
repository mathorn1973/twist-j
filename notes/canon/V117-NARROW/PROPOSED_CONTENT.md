# Content for review

**NON-CANONICAL.** The following entry is proposed for the first sealed
fold after v116, subject to the source merge and release gates described
in the [proposal](README.md).

## Canon section 2

Insert after the rank-43 relay continuation, before section 3.

> ### C-H3-ROW0-PULSE-RETURN [C]
>
> Use the registered periodic 288 by 2 H3 station with the fixed
> scattering receivers at x12 and x13 and common reference at x23.
> Observe at the x13 to x14 port both transfer words on even ticks 98
> through 256, reducing each word by the positive gcd of its integer
> coefficients and preserving its sign and zero. Keep the predecessor
> and its exact-control veto. For an abstention that passes the veto,
> add a positive decision at tick 256 if the row-0 activity on even
> ticks 98 through 120 spells `000111110001`.
>
> In the two fresh blind panels the predecessor correctly signs
> 1597 of 1600 intact packets and abstains on three positives.
> The new rule recovers all three, each directed 0 to 1 at mask phase 2,
> at signed gains -1216, +1088 and +1216. All prior signs survive,
> including the 34 intact row-1 onset corrections. Each of the 20
> directed intact groups scores 80 of 80. The 1600 exchanged tails
> score 1600 correct donor signs. The 3200 isolated presentations and
> 20 quiet controls yield zero writes.
>
> Each recovered packet repeats the complete raw late row-0 sequence
> of an opened rescue. The three full two-row primitive projections
> differ from one another and fall outside the 735 distinct projections
> from the two opened panels. All eleven registered predicates pass.
> This is finite L1 orientation decoding for the registered station and
> rosters. Q9 remains open.

## Registry and evidence

- **Claim** `C-H3-ROW0-PULSE-RETURN` with status `C` in
  `2. Time, space, and the decoder`.
- **Scope** At L1 on the registered 288 by 2 periodic H3 station,
  a row-0 pulse-return rule at the x13 to x14 port recovers all three
  previously silent positives in the 1600 fresh intact blind
  presentations and preserves every prior sign, including 34 intact
  row-1 onset corrections. All 1600 exchanged tails score their donor
  sign and all 3220 isolated or quiet controls stay silent. The three
  rescues repeat the same opened raw late row-0 sequence and have
  distinct complete two-row projections outside the 735-projection
  opened comparator.
- **Falsifier** An exact replay of the frozen station and rosters that
  contradicts a declared recovery, sign, preservation, control,
  matched raw trace, relative projection count or registered
  predicate rejects the affected finite claim. A custody, runtime or
  stdout-byte failure without such a contradiction is STOP.
- **Normative row** `COMPUTATION` with status `C`, layer `L1` and
  anchor `canon/CANON.md::C-H3-ROW0-PULSE-RETURN`.
- **Evidence** `EV-C-H3-ROW0-PULSE-RETURN`, kind `PUBLIC_PROBE`, at
  `probes/P-H3-ROW0-PULSE-RETURN-1`. Use
  `bundle-manifest-sha256-v1` and `two-architecture`, confirming
  bundle and both jobs again at the merged source. The evidence uses
  the public H3 kernel in `reproduce/h3-referenced-record/verify.py`
  at SHA-256
  `4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd`.
  The six fixed histories supported by that reproduction's Canon
  claim are separate from the fresh station panels.
- **History** Add one `DECLARE` event with previous status `-`,
  new status `C`, the finalized scope hash, merged evidence manifest
  digest and the actual fold date. Rationale: register finite
  orientation at the outgoing H3 port on the frozen rosters.

## Build from the integrated source

Apply the section and append the four ledger rows. Add a v117
changelog entry for the finite packet computation. Regenerate the
Canon views and normative checksums. Keep the current core selection,
frontier, dependency edges, gate rows and reproduction directory count.
Update the inventory assertions in
`tools/test_architecture_map_report.py` to 635 total claims, 50 C and
394 two-architecture claims.

The existing status-separation reproduction pins changed v116 files
by byte. Extend its reverse-delta chain to reconstruct exact v116
inputs from the final v117 files, preserving its existing verification
lines. Audit the new claim's unique L1 C registration, evidence
manifest and declared status transition against the frozen source.
Check the named counts and predicates from the exact probe transcript.
Refresh the status-separation README and expected stdout for the
resulting exact check. Then run policy, units, Canon, ledger,
gate-contract and static activation checks before freezing and running
the release candidate. The release-form commit carries the
new `STATUS.md`, `README.md` and `CITATION.cff` only.
