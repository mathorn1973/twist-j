# Proposed Public Canon v117

**NON-CANONICAL.** Add one finite L1 computation at status C,
`C-H3-ROW0-PULSE-RETURN`. Keep the 634 v116 registry entries, the 25
live H/O claims, the 43 reproductions and Q9 as recorded in v116. The
proposed registry has 635 entries with 479 T, 62 D, 50 C, 2 H, 23 O and
19 F. [Proposed text and ledger edits](PROPOSED_CONTENT.md)

## Source and dependency

The reviewed baseline is annotated tag `canon-v116` at activation
`93c36089db57032a6cbca482ff62c95884567d0f` and content
`0b6ae8e23d7086715b908cce6e1755d2898f55fc`. The 1,568,802 Canon bytes
at that tag, content commit and current main agree, with SHA-256
`ea4f924dc02838fcfe47d9b983bc0be929da7378ee9278c48831f34a5c393695`.
[Public Canon v116](https://github.com/mathorn1973/twist-j/tree/canon-v116/canon)

The sole source is [#2059](https://github.com/mathorn1973/twist-j/pull/2059)
at head `5bd84c79b58ca21ea2bb39d2a5aaa3b67f0e09e5`. Its exact-head
pull-request run `44968423841`, attempt 1, succeeded. Both architecture
logs record `VERIFY PASS` with the following verifier and stdout digests,
and the aggregate records `TWO-ARCHITECTURE CHECK PASS`.
[x86_64](https://github.com/mathorn1973/twist-j/actions/runs/44968423841/job/137042589693)
[aarch64](https://github.com/mathorn1973/twist-j/actions/runs/44968423841/job/137042589518)
[Aggregate](https://github.com/mathorn1973/twist-j/actions/runs/44968423841/job/137044940623)

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| Frozen verifier | 12,797 | `4259f3c0209d97cd4c932f1f93f2796f27eb6a82873b8793b73fd9428f80c857` |
| Expected stdout | 62,143 | `6330720d5177e133c22c92796e5fd1094810b5a3be9fea35bed38b385a3465aa` |
| Source bundle manifest | | `0a3c4db9d29cf3f99e66612f9f7fb1d3e823124e0aa8af011fec77ba0374894a` |

The six frozen source files are identical at the preregistration pin and
the reviewed head. Before opening the anonymous ordering, the blind
commitment bound the anonymous input and the 6,420 answer records. The
published opening audit checked the individual answers. The prospective
panels use gains beyond the two opened replication panels. Their three
rescues repeat the opened raw row-0 trace. Their complete two-row
projections differ and are absent from the 735 distinct comparator
projections. The comparison is with that fixed public panel. The opened
panels calibrate the rule and supply its replication control. The fresh
panels supply the claimed prospective test.
[Preregistration](https://github.com/mathorn1973/twist-j/blob/1cb47b7ec72bc0c4556bde8e37f64347584739dd/probes/P-H3-ROW0-PULSE-RETURN-1/PREREG.md)
[Blind commitment](https://github.com/mathorn1973/twist-j/blob/dad53aa85bf7e003507525ac343ac69d273e6064/probes/P-H3-ROW0-PULSE-RETURN-1/BLIND.md)
[Run record](https://github.com/mathorn1973/twist-j/blob/5bd84c79b58ca21ea2bb39d2a5aaa3b67f0e09e5/probes/P-H3-ROW0-PULSE-RETURN-1/RUN.md)
[Result](https://github.com/mathorn1973/twist-j/blob/5bd84c79b58ca21ea2bb39d2a5aaa3b67f0e09e5/probes/P-H3-ROW0-PULSE-RETURN-1/RESULT.md)

## Fold entry condition

At review, #2059 is open. Merge the reviewed source into main under its
own probe record first. Read back the merge, the source bundle and the
required checks, and prepare the release from the then-current main.
Bind the folded content and generated views in the content commit.
Bind that exact content in the subsequent release-form commit. The
release candidate needs its own complete frozen x86_64 and aarch64
checks and aggregate before merge. Apply the subsequent public
activation, tag and release readback in the standing order.
[Release procedure](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/AGENTS.md#6-formal-work-after-cutover)
