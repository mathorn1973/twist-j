# Proposed Public Canon v117, wider form

**NON-CANONICAL.** This proposal builds on the narrow proposal of
[#2062](https://github.com/mathorn1973/twist-j/pull/2062). It keeps that
proposal's one finite computation, with corrected wording, and adds four
theorem entries. The 634 entries of v116 stay. The proposed registry has
639 entries with 483 T, 62 D, 50 C, 2 H, 23 O and 19 F. The 25 live H and
O claims are unchanged, and two reproductions are added to the 43. [Proposed text and ledger edits](PROPOSED_CONTENT.md)

## What the edition would change

| Entry | Status | Source | What it adds |
| --- | --- | --- | --- |
| `C-H3-ROW0-PULSE-RETURN-N` | C | [#2059](https://github.com/mathorn1973/twist-j/pull/2059) | One finite L1 orientation computation on a station frozen in its probe |
| `QDD-PAIR-INTERVENTION-LOCALIZATION` | T | [#2061](https://github.com/mathorn1973/twist-j/pull/2061) | A channel-level certificate that an encoded five-level state sits on the logical levels at one cut, exactly when the addressed pairs form a connected graph |
| `QUADRATIC-L5-SOURCE-SYMMETRY` | T | [#2063](https://github.com/mathorn1973/twist-j/pull/2063) | A source reflection every successful contact must break, and a minimal lift that keeps the common scalar symmetry |
| `QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT` | T | [#2063](https://github.com/mathorn1973/twist-j/pull/2063) and [#2068](https://github.com/mathorn1973/twist-j/pull/2068) | Five affine alternatives never cover the common-ready layer; six cover it in the class of the registered $C=K\oplus0_2$, with data fibres of size at most two |
| `QUADRATIC-L5-NATIVE-WORD-COUNT` | T | [#2072](https://github.com/mathorn1973/twist-j/pull/2072) | At least 25 native alternatives are needed to satisfy the Gram identity on all ready inputs at any fixed value of the radical coordinates. The same bound applies to a fixed residual-alphabet word that succeeds on those inputs. |

The existing theorem QUADRATIC-L5-NATIVE-OBSTRUCTIONS excludes one affine
map and any selection between two, and says that it does not cover programs
with more than two distinct data branches. The affine-alternative entry excludes up to five branches in ranks three
through six and shows that six suffice for the registered $C$ at rank four.

No open owner closes. QUADRATIC-MEMORY-NATIVE-CONTACT gains two necessary
conditions and stays open: a successful contact must break the source
reflection at a named ready state, and its ready data projection is not a
selection among at most five affine maps. Six are enough for everything
the Canon asks of the data projection: with suitable output isometries the
six maps give fibres of size at most two, and the data map extends to a
complete permutation that satisfies the readout equation on its whole
reachable set. It selects among six linear maps on the ready layer and
15 on reachable occupied states, with a fallback on unreachable occupied
states. Its selection and bit
rules are tables derived from the target and none of its maps is shown to
be native, so it is no realization. For words in the registered
generators, a selector that satisfies the Gram identity throughout a ready
slice needs at least 25 alternatives. A ready slice consists of all ready
inputs at one fixed value of the radical coordinates. The registered
controls act at each input as such words. The fixed composition of
RESIDUAL-STEP-RECORD satisfies the initialized readout on every ready
slice, so its data projection selects among at least 25 native maps on
each slice. The live total stays 25.

## Review state of the sources

The baseline is annotated tag `canon-v116` at activation
`93c36089db57032a6cbca482ff62c95884567d0f` and content
`0b6ae8e23d7086715b908cce6e1755d2898f55fc`.

| Source | Head | Review result |
| --- | --- | --- |
| #2059 | `47e02915bf34608d270ed598a7275c05224bf287` | The outside review confirmed the computation, frozen files, custody chain and two-architecture run at the parent. This head addresses the review in RESULT.md. The [corrected-head run](https://github.com/mathorn1973/twist-j/actions/runs/45261428008) replayed the frozen verifier on both architectures with byte-identical scientific output. |
| #2061 | `d91453e6d6256320a8e51e0a164b0cbf9f4910a3` | Exact theorem, quantitative bound, real rotations and minimality hold. The review adds that the exact conclusion holds for every connected pair graph. |
| #2063 | `5c47b58bd1fcd5702625b12f5766cfb150fc5414` | All three results hold; wording repairs only. |
| #2068 | `0ff48f747195a38e08c57ee5bf94a33315e4f112` | The [outside review](https://github.com/mathorn1973/twist-j/pull/2068#issuecomment-7112960069) supported merge after requiring both coefficients after Lemma 4 to be nonzero. This head adds that hypothesis. Its [repository checks](https://github.com/mathorn1973/twist-j/actions/runs/45261354870) passed. Separate x86_64 and aarch64 replays passed all 47 checks and matched the 6,176 expected bytes. |
| #2072 | `16bfe6eeda21622e3b309a076b9369b8e970fe2f` | The [outside review](https://github.com/mathorn1973/twist-j/pull/2072#issuecomment-7112964009) supports merging this head as a non-canonical note and records exact verifier replays on both architectures. |

The sources for all five entries have outside review comments. Their
individual merges are required before the fold.

## Fold entry conditions

1. Each source merges under its own record first: #2059 with the reviewed
   wording in RESULT.md, and #2061, #2063, #2068 and #2072 as notes.
2. Two theorem entries carry `INLINE_CANON` evidence, so the fold places
   their complete proofs in the Canon, as written in
   [the proposed text](PROPOSED_CONTENT.md) and in the merged source notes.
   The two counts include exhaustive finite checks; the fold places their
   proofs in the Canon and promotes the exact verifiers of #2068 and #2072
   to reproductions.
3. The release then follows the standing order described in #2062:
   content commit with regenerated views, release-form commit, one complete
   frozen pair of architecture checks with the aggregate, activation, tag
   and release readback.
   [Release procedure](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/AGENTS.md#6-formal-work-after-cutover)

No rule limits a fold to one claim. v111 declared nine, v112 five and v114
three.

## Not included

[#2064](https://github.com/mathorn1973/twist-j/pull/2064) is a sound finite
computation and can merge as a probe record after the changes its review
lists. Its number is an attained donor-bank stock. As a Canon entry it would
need a stated optimisation class and a lower bound, so it is left out here.
