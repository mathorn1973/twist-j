# Source review for the proposed v116 H3 fold

**NON-CANONICAL.** The active baseline is Public Canon v115 at
annotated tag canon-v115, activation 5b09d042dacd8a48d812264f117afe796645a95e
and content commit 6cd898bc6d35f339b471ea684486af8c0ac54f84.
The tagged CANON.md has the verified SHA-256
38afba3f5c815aa1c623f8cec9992f0e5f89659e493e85dc61054e8fdfa253cf.
The two proposed additions have finite computation status C at L1. The
v115 result C-H3-DOUBLE-RENEWED-TRANSFER-N establishes a matched local
B1/B2 pair at receiver 2 after two recurrent B2 writes on the unchanged
rank-43 trajectory. The present sources ask whether its held outputs, or
another qualifying pair of outputs on that trajectory, also reach cell 3.
Q9 remains open. [Public Canon v115](https://github.com/mathorn1973/twist-j/tree/canon-v115/canon)

## #2053. Fixed controls and prospective search

The primary fixed examples are retrospective controls. Their full post-B
fields were retained in a local replay of the sealed #2049 witnesses
before the #2052 pin. Both #2049 outputs meet their only target contact
on the next tick. Both material rails refuse, and the word is overwritten
by a local B at 2 before another target contact. The search for another
qualifying pair through tick 67,108,864 was prospective at that pin.
[Registration](https://github.com/mathorn1973/twist-j/blob/07e2f2ac4a6cbe2f5f862d711fb0ea1c75cfdd7a/probes/P-H3-RECEIVER-OUTPUT-RELAY-1/PREREG.md)

| Output at 2 | First rail in the j power basis | Contact with 3 | Next local overwrite at 2 |
| --- | --- | --- | --- |
| 7,390,475 B1 | (1,-1,0,1) | 7,390,476, both rails refuse | B2, first rail (0,0,1,2) |
| 9,915,383 B2 | (1,0,1,2) | 9,915,384, both rails refuse | B1, first rail (2,-1,1,1) |

The uninterrupted rank-43 run covered ticks 1 through $2^{26}$ inclusive
and counted 153,059 recurrent B2 writer episodes. The final disposition
of each read is counted under the originating B branch at cell 2.
The continuation verifier supplies the prefix breakdown of returns and
local overwrites.

| Site-2 branch | Eligible reads | Changed 3 at C | Ended at C with 1 | Overwritten by B at 2 | Held at ceiling |
| --- | ---: | ---: | ---: | ---: | ---: |
| B1 | 554 | 102 | 144 | 308 | 0 |
| B2 | 159 | 13 | 2 | 144 | 0 |

Zero pairs satisfy all registered conditions. Individual deliveries in
both branches are positive finite observations. The separate readiness
diagnostic grouped 44 B1 and 48 B2 readiness states among all eligible
reads, with three in common. Among deliveries the corresponding sets
have sizes 17 and 9 and an empty intersection. This identifies the
readiness mismatch before applying the distinct source, arrival and
output predicates. The set sizes and the separately replayed individual
examples are supplementary observations. The hosted verifier replays
the frozen default transcript. [Result](https://github.com/mathorn1973/twist-j/blob/519766f6215bc613423c69666ccc1730201fe56b/probes/P-H3-RECEIVER-OUTPUT-RELAY-1/RESULT.md), [Execution and supplementary checks](https://github.com/mathorn1973/twist-j/blob/519766f6215bc613423c69666ccc1730201fe56b/probes/P-H3-RECEIVER-OUTPUT-RELAY-1/RUN.md)

The #2053 readiness diagnostic also furnishes the later probe's
successful B2 reference. The earlier B2 at 8,176,761 and recurrence
at 36,442,231 lead to the read at 36,442,233. Its output
$\pm(1,0,1,2)$ changes cell 3 at 36,442,234 C from $\pm(-1,0,-1,0)$ to
$\pm(0,1,0,2)$, followed by B0. The two original #2049 encounters therefore
do not relay as a pair, even though the B2 local readiness and arrival
occur again in this successful individual delivery.
[Reference evidence in #2053](https://github.com/mathorn1973/twist-j/blob/519766f6215bc613423c69666ccc1730201fe56b/probes/P-H3-RECEIVER-OUTPUT-RELAY-1/RESULT.md)

## #2055. Retrospective confirmation through the longer ceiling

Issue #2054 disclosed the continuation counts, zero comparisons and
frozen reference before the verifier's public execution. This is a
retrospective confirmation of known exploration. The program starts from
the original launch and runs through $2^{30}$. Its new-read window is
$2^{26}<t\le 2^{30}$, an additional 1,006,632,960 ticks. Recurrent source
history crosses the prefix boundary. A read and its terminal
disposition are assigned by the read tick $t$ at 2, including a word
that is still held at the ceiling. The published prefix is an interior
control. [Claim #2054](https://github.com/mathorn1973/twist-j/issues/2054),
[Preregistration](https://github.com/mathorn1973/twist-j/blob/050a9be48757348fd57021bcc68ab3b9f9fcaf3c/probes/P-H3-RELAY-CONTINUATION-1/PREREG.md)

| Site-2 branch | Eligible new reads | Changed 3 at C | Ended at C with 1 | Overwritten by B at 2 | Held at ceiling |
| --- | ---: | ---: | ---: | ---: | ---: |
| B1 | 6,940 | 702 | 885 | 5,353 | 0 |
| B2 | 2,852 | 188 | 32 | 2,632 | 0 |

There are 503,316,480 post-prefix directed bit-1 contacts from 1 to 2
before filtering by source, branch or material motion. Exactly zero
return to the reference's four pre-C rails at 2, and zero match its
full readiness. Readiness comprises those four rails and both post-C
radiation rails. The code evaluates it at site 2, and allows different
site-3 resident values. On this window the 702 successful new B1 reads
give zero compatible pairs in each B2 comparison below.

| B2 pool | Successful reads | Pairs with a new B1 |
| --- | ---: | ---: |
| Fixed #2053 reference | 1 | 0 |
| Read ticks t <= 2^26 | 13 | 0 |
| Read ticks t <= 2^30, either read first | 201 | 0 |

Compatibility further requires distinct ordered source words, arrivals
and outputs at the first hop, and both held outputs must change site 3
at C. The comparison across the entire B2 pool still requires a new
B1. The finite result gives no claim about a pair of historical B1
and new B2, other launches, later ticks or a universal obstruction.
The fixed source and both contact projections agree with #2053. The
final 512-coefficient field matches the predeclared SHA-256
b05fee6196a0be63a6ab150a2db111114633a66a8c74dc76c8945964c1c7acfa
under the specified decimal coefficient encoding, and the endpoint
account equals the launch account. The frozen driver emits the
confirmation Boolean separately from its exit status. The recorded
last line is explicitly true.
[Result](https://github.com/mathorn1973/twist-j/blob/1ef0a6e0df49efcf06a8f32545c6ff1bd1f15119/probes/P-H3-RELAY-CONTINUATION-1/RESULT.md),
[Exact transcript](https://github.com/mathorn1973/twist-j/blob/1ef0a6e0df49efcf06a8f32545c6ff1bd1f15119/probes/P-H3-RELAY-CONTINUATION-1/EXPECTED.txt)

The frozen #2055 PREREG.md adds one trailing e to its textual main
reference. The actual direct parent of pin 050a9be48757348fd57021bcc68ab3b9f9fcaf3c
is 68812464c5566613b1000110e556968c9775fa95, the #2053 merge.
RUN.md records the discrepancy and the calculation checks the original
launch, inherited code and #2053 prefix by their literal pins.
[Recorded correction](https://github.com/mathorn1973/twist-j/blob/1ef0a6e0df49efcf06a8f32545c6ff1bd1f15119/probes/P-H3-RELAY-CONTINUATION-1/RUN.md)

## Public replay and custody

The final PR and merge commits match the GitHub workflow records for
both architectures and the aggregate. All four policy workflows completed successfully on attempt
1. Each architecture's log contains the explicit VERIFY PASS record
with the corresponding verifier and stdout hashes below. Each aggregate
log contains TWO-ARCHITECTURE CHECK PASS. The pinned verifier and
preregistration bytes match at pin, PR head and merge, and the expected
stdout bytes match between PR head and merge. This review reads hosted
replays and source artifacts.

| Probe | Pin | Reviewed PR head | Public merge |
| --- | --- | --- | --- |
| [#2053](https://github.com/mathorn1973/twist-j/pull/2053) | 07e2f2ac4a6cbe2f5f862d711fb0ea1c75cfdd7a | 519766f6215bc613423c69666ccc1730201fe56b | 68812464c5566613b1000110e556968c9775fa95 |
| [#2055](https://github.com/mathorn1973/twist-j/pull/2055) | 050a9be48757348fd57021bcc68ab3b9f9fcaf3c | 1ef0a6e0df49efcf06a8f32545c6ff1bd1f15119 | f3e27393bc2e329ac84232ab1a1a07dd81ea77d7 |

| Event | x86_64 | aarch64 | Aggregate |
| --- | --- | --- | --- |
| #2053 PR, run 44914221896 | [136876282088](https://github.com/mathorn1973/twist-j/actions/runs/44914221896/job/136876282088) | [136876281830](https://github.com/mathorn1973/twist-j/actions/runs/44914221896/job/136876281830) | [136877008365](https://github.com/mathorn1973/twist-j/actions/runs/44914221896/job/136877008365) |
| #2053 main push, run 44914552248 | [136877248283](https://github.com/mathorn1973/twist-j/actions/runs/44914552248/job/136877248283) | [136877248206](https://github.com/mathorn1973/twist-j/actions/runs/44914552248/job/136877248206) | [136877820506](https://github.com/mathorn1973/twist-j/actions/runs/44914552248/job/136877820506) |
| #2055 PR, run 44919751276 | [136892990051](https://github.com/mathorn1973/twist-j/actions/runs/44919751276/job/136892990051) | [136892990472](https://github.com/mathorn1973/twist-j/actions/runs/44919751276/job/136892990472) | [136895930184](https://github.com/mathorn1973/twist-j/actions/runs/44919751276/job/136895930184) |
| #2055 main push, run 44920791276 | [136896161179](https://github.com/mathorn1973/twist-j/actions/runs/44920791276/job/136896161179) | [136896160920](https://github.com/mathorn1973/twist-j/actions/runs/44920791276/job/136896160920) | [136899100058](https://github.com/mathorn1973/twist-j/actions/runs/44920791276/job/136899100058) |

The two verification records contain the probe name followed by the
SHA-256 digests of its verifier and exact stdout.

    VERIFY PASS P-H3-RECEIVER-OUTPUT-RELAY-1 096e8ef26f4fe90e6330fa4bcc6b3ab1f980870ead240e745870b8c6f740d8a5 a9e8dc1a09797b72970064b7a558544c1a2cf4d06fbcbb8d80119c14f94d4910
    VERIFY PASS P-H3-RELAY-CONTINUATION-1 af031b96bc46851d19eb2ae907e02f77f68d063ccf204068690a10872532b018 198ed32b967d202c0b729bc1c03e4de6e6ecbc3810b2709ec7880dfdd49cc1f3

The transcripts are 3,019 and 1,539 bytes respectively. #2053 also
documents a five-coordinate full history replay of the two fixed records.
#2055's frozen Python component independently checks the fixed local
operations and the endpoint account. Its exhaustive coverage and
pair counts come from the native scan. Both sources support a narrow C
fold and preserve the difference between native individual delivery and
paired delivery at matched site-2 readiness.
