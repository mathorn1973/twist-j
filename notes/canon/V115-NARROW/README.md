# Proposed Public Canon v115

**NON-CANONICAL.** This proposal adds two finite computations at L1 to Public Canon v114. Both compare two encounters on a single unmodified H3 trajectory. At the receiving site the four rails before contact C, the incoming radiation after C and the matching bit agree. Different arriving material then leads to different active B operations. The two statements distinguish which writer events produced those words. Q9, the selection of the physical electromagnetic coupling, stays open.

## Review of #2047

**Proposed C for `C-H3-RENEWED-WORD-CHOICE-N`.** On rank 43, writer 1 repeats its tick-330940 B2 episode at 598058. Its material word reaches receiver 0 at 598060 and selects B1. At 720019 the same writer emits a second word by B1, which reaches that receiver at 720028 and selects B2. Each contact changes the receiver's material. The source and receiver operations are different parts of this comparison. [Exact certificate and census](https://github.com/mathorn1973/twist-j/blob/c550395cb5e7b21d26289058a588df6f9986ebe7/probes/P-H3-RENEWED-WORD-CHOICE-1/RESULT.md)

Across the 85 launches and 1,851,392 ticks, 60 opposite-branch pairs have at least one repeated B2 source. Eight transfer material on a repeated-source arm, and one transfers material on both arms. Four pairs have two repeated B2 sources. Each of those four transfers material on exactly one arm. The original functional renewals at writer 28 supply a separate finite negative result. Their 14,606 writes give 14,613 contacts while the word is still held, with zero changes to receiver material at C or B. The three tick-181 outputs face refusal at tick 182 and the receiver executes B0. [Frozen output](https://github.com/mathorn1973/twist-j/blob/c550395cb5e7b21d26289058a588df6f9986ebe7/probes/P-H3-RENEWED-WORD-CHOICE-1/EXPECTED.txt)

## Review of #2049

**Proposed C for `C-H3-DOUBLE-RENEWED-TRANSFER-N`.** On the same original rank-43 trajectory, writer 1 produces two different ordered pairs $(a,-a)$ through repeated native B2 events. Each repeat has a named earlier occurrence with the same writer and matching, four pre-contact writer rails, ordered material input, incoming radiation and ordered output. The native contact changes material at both ends of the upstream edge. The writer retains each emitted pair through the intervening C and B cuts. At receiver 2, with bit one and identical readiness, each contact changes both material rails. [Exact certificate and Hermitian branch equalities](https://github.com/mathorn1973/twist-j/blob/e245183f625f097bfb3126367b27f78a3dc89a15/probes/P-H3-DOUBLE-RENEWED-TRANSFER-1/RESULT.md)

| Prior B2 | Repeated B2 | First rail $a$ | Read at site 2 | Operation |
| ---: | ---: | --- | ---: | --- |
| 7,316,785 | 7,390,473 | $2j^3$ | 7,390,475 | B1 |
| 8,176,761 | 9,915,381 | $-2(j+j^3)$ | 9,915,383 | B2 |

The first qualifying pair ends the search on its first launch. Through this stop the native scan records 784,474 locally repeated B2 writes and 3,222 encounters with material change at both C and B. The other 84 launches contribute only to the earlier census. Both reads lie beyond the earlier rank-43 limit of 1,048,576. The witness establishes existence within one trajectory at matched local inputs, without exchanging words or modifying the evolution. [Search order and stopping condition](https://github.com/mathorn1973/twist-j/blob/d1552a78a09689a5ae3f8ff433203ba52854f01a/probes/P-H3-DOUBLE-RENEWED-TRANSFER-1/PREREG.md)

## Source and patch verification

| Source | Preregistration | Reviewed head | Default stdout | Hosted x86_64 and aarch64 |
| --- | --- | --- | ---: | --- |
| [#2047](https://github.com/mathorn1973/twist-j/pull/2047) | `b888eb0644e3f2133d29363c16da8c40343b63ce` | `c550395cb5e7b21d26289058a588df6f9986ebe7` | 15,102 bytes | [PR checks](https://github.com/mathorn1973/twist-j/actions/runs/44896661141) |
| [#2049](https://github.com/mathorn1973/twist-j/pull/2049) | `d1552a78a09689a5ae3f8ff433203ba52854f01a` | `e245183f625f097bfb3126367b27f78a3dc89a15` | 1,620 bytes | [PR checks](https://github.com/mathorn1973/twist-j/actions/runs/44899739073) |

The [content patch](CONTENT.patch) applies to the merged base `f1771c187bb49161194d6ce2236270d9784c34f3`. Its SHA-256 is `fd81c0f77997249430bb698221aa6f2a0454f0994631a91f403f7904fe651d39`. Applying it to a fresh index of that base reproduced the exact 13-file change and content tree `1b691d4b9e1e15e02c04759365a98d04adaf5b5a`. The proposed CANON.md has 1,565,061 bytes and SHA-256 `38afba3f5c815aa1c623f8cec9992f0e5f89659e493e85dc61054e8fdfa253cf`. [Merged source base](https://github.com/mathorn1973/twist-j/commit/f1771c187bb49161194d6ce2236270d9784c34f3)

The proposed ledger contains 632 claims with 479 T, 62 D, 47 C, 2 H, 23 O and 19 F. The 630 earlier registry rows retain their exact bytes. The frontier, all 25 open H/O items, the dependency and gate ledgers, and the 43-reproduction inventory are preserved. The two new entries bind the complete public probe bundles by SHA-256.

The working-session review replayed both frozen default verifiers on Linux x86_64. Their stdout matched the published files byte for byte, with empty stderr. The default Python checks cover the local states at four distinct encounters in #2047 and two in #2049. Separate full Python runs from launch through ticks 735,779 and 9,915,383 reproduced the published supplementary digests, including the earlier writes and uninterrupted holds. [#2047 execution record](https://github.com/mathorn1973/twist-j/blob/c550395cb5e7b21d26289058a588df6f9986ebe7/probes/P-H3-RENEWED-WORD-CHOICE-1/RUN.md) · [#2049 execution record](https://github.com/mathorn1973/twist-j/blob/e245183f625f097bfb3126367b27f78a3dc89a15/probes/P-H3-DOUBLE-RENEWED-TRANSFER-1/RUN.md)

In a clean Linux checkout of the local release-form preview, all 248 unit tests passed, along with policy, Canon, ledger, gate-contract, generated-view and static activation checks. The status-separation verifier reproduced its 40,673-byte expected output with 256 passing checks. Its first 250 numbered results are byte-identical to v114. The hosted two-architecture runs in the table verified the two source probes.

To apply the reviewed content on the stated base, use `git apply --index --whitespace=error-all <path-to-CONTENT.patch>`. An eventual release binds the resulting content commit in its separate release form and verifies the final candidate under the public release procedure. [Release procedure](https://github.com/mathorn1973/twist-j/blob/f1771c187bb49161194d6ce2236270d9784c34f3/AGENTS.md#6-formal-work-after-cutover)
