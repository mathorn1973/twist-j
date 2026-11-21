# Can a new B1 output reach cell 3 at the readiness of a successful B2?

**Candidate C, finite L1 computation.** On the original rank-43 H3 trajectory, 702 new B1 outputs and 188 new B2 outputs each changed the material of cell 3. Zero pairs met all the registered conditions. The new interval covers site-2 reads at ticks $2^{26} < t \le 2^{30}$, or 1,006,632,960 additional ticks. The public execution confirmed the previously disclosed exploratory result. [Registration](PREREG.md) and [exact counts](EXPECTED.txt).

## Where the fixed B2 comparison fails

The successful reference B2 from [#2053](https://github.com/mathorn1973/twist-j/pull/2053) was read at cell 2 at tick 36,442,233. Its output changed both material rails of cell 3 at the following C contact, before B0 at cell 3. The replay recovered the earlier equivalent source write at tick 8,176,761 and the repeated write at tick 36,442,231. It checked the source, arrival, output and recipient material against the registered reference.

The continuation had **503,316,480** directed contacts from cell 1 to cell 2. Across all those contacts, the four rails at cell 2 before C matched the reference **zero times**. The full readiness, which also includes the two radiation rails after C, consequently matched zero times. These counts include every opportunity, before filtering by writer, branch or delivery.

## What happened to the new outputs

The replay carried the original recurrent-write history across the boundary at tick 67,108,864. It counted 3,657,170 more eligible repeated B2 writes at cell 1. A site-2 read enters the table at its own tick. Its output is followed until the first material change. Delivery requires that the held output change cell 3 at C. The other two completed dispositions locate the first material change at cell 2.

| Site-2 branch | Eligible reads | Changed cell 3 | Ended at C with cell 1 | Overwritten by local B at cell 2 | Still held at ceiling |
| --- | ---: | ---: | ---: | ---: | ---: |
| B1 | 6,940 | 702 | 885 | 5,353 | 0 |
| B2 | 2,852 | 188 | 32 | 2,632 | 0 |

The pairing test requires equal six-word readiness at cell 2, opposite branches, distinct source words, distinct arrivals, distinct outputs, and two deliveries to the same cell 3. Both outputs must arise on the uninterrupted trajectory from recurrent source writes. All contacts and branch choices followed the native dynamics without prepared substitutions.

| Successful B2 reads compared with the 702 successful new B1 reads | B2 reads | Compatible pairs |
| --- | ---: | ---: |
| Fixed reference | 1 | 0 |
| Published prefix through tick 67,108,864 | 13 | 0 |
| Entire trajectory through tick 1,073,741,824, allowing either read first | 201 | 0 |

The conserved account at the ceiling equalled the launch account. The final 512-coefficient field had the registered SHA-256 `b05fee6196a0be63a6ab150a2db111114633a66a8c74dc76c8945964c1c7acfa`. All registered confirmation targets passed. The conclusion covers this launch, directed path, time window and pairing rule. Later ticks and other launches remain open. Q9 remains open. [Execution record](RUN.md).
