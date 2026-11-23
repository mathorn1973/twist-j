# Proposed Public Canon v117, wider form

**NON-CANONICAL.** This proposal builds on the narrow proposal of
[#2062](https://github.com/mathorn1973/twist-j/pull/2062). It keeps that
proposal's one finite computation, with corrected wording, and adds three
theorem entries whose sources have been reviewed. The 634 entries of v116
stay. The proposed registry has 638 entries with 482 T, 62 D, 50 C, 2 H,
23 O and 19 F. The 25 live H and O claims and the 43 reproductions are
unchanged. [Proposed text and ledger edits](PROPOSED_CONTENT.md)

## What the edition would change

| Entry | Status | Source | What it adds |
| --- | --- | --- | --- |
| `C-H3-ROW0-PULSE-RETURN-N` | C | [#2059](https://github.com/mathorn1973/twist-j/pull/2059) | One finite L1 orientation computation on a station frozen in its probe |
| `QDD-PAIR-INTERVENTION-LOCALIZATION` | T | [#2061](https://github.com/mathorn1973/twist-j/pull/2061) | A channel-level certificate that an encoded five-level state sits on the logical levels at one cut, exactly when the addressed pairs form a connected graph |
| `QUADRATIC-L5-SOURCE-SYMMETRY` | T | [#2063](https://github.com/mathorn1973/twist-j/pull/2063) | A source reflection every successful contact must break, and a minimal lift that keeps the common scalar symmetry |
| `QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT` | T | [#2063](https://github.com/mathorn1973/twist-j/pull/2063) and the alternative-count note | Five affine alternatives never cover the common-ready layer; six cover it in the class of the registered $C=K\oplus0_2$ |

The existing theorem QUADRATIC-L5-NATIVE-OBSTRUCTIONS excludes one affine
map and any selection between two, and says that it does not cover programs
with more than two distinct data branches. The last entry moves that limit
to five and shows that it is sharp in the class of the registered $C$.

No open owner closes. QUADRATIC-MEMORY-NATIVE-CONTACT gains two necessary
conditions and stays open: a successful contact must break the source
reflection at a named ready state, and its ready data projection is not a
selection among at most five affine maps. The six-map cover is not a binary
contact, because its selector has forced fibres of size four. The live
total stays 25.

## Review state of the sources

The baseline is annotated tag `canon-v116` at activation
`93c36089db57032a6cbca482ff62c95884567d0f` and content
`0b6ae8e23d7086715b908cce6e1755d2898f55fc`.

| Source | Head | Review result |
| --- | --- | --- |
| #2059 | `5bd84c79b58ca21ea2bb39d2a5aaa3b67f0e09e5` | The computation, the frozen files, the custody chain and the two-architecture run were confirmed. The review asks for narrower wording in RESULT.md; the entry here already uses it. |
| #2061 | `d91453e6d6256320a8e51e0a164b0cbf9f4910a3` | Exact theorem, quantitative bound, real rotations and minimality hold. The review adds that the exact conclusion holds for every connected pair graph. |
| #2063 | `5c47b58bd1fcd5702625b12f5766cfb150fc5414` | All three results hold; wording repairs only. |
| Alternative-count note | to be linked | Proofs and exact verifier by the session that wrote this proposal. It still needs a review by another party before a fold. |

The entry for the alternative count is conditional on that outside review.
The other three entries rest on sources written by one party and reviewed
by another.

## Fold entry conditions

1. Each source merges under its own record first: #2059 with the reviewed
   wording in RESULT.md, and #2061, #2063 and the alternative-count note as
   notes.
2. The three theorem entries carry `INLINE_CANON` evidence, so the fold
   places their complete proofs in the Canon, as written in
   [the proposed text](PROPOSED_CONTENT.md) and in the merged source notes.
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
