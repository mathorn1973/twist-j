# Reporting errata: preserved phase-chain review

**PUBLIC / NON-CANONICAL / L1. Reporting correction, 2026-10-18.**
Author: A. M. Thorn. License: Apache-2.0.

This records discrepancies in the review delivered by [PR #1607](https://github.com/mathorn1973/twist-j/pull/1607)
at `ab2d10a563d46799e6e595e23777bc156b284e85`, against its frozen pin
`80d6814a6b7c871b2b46d8e52f764c78c26810b4`. It supersedes that delivery's
unqualified claims that every preregistered identity and obligation passed.

**Disposition: completed computation retained; contract PARTIAL /
CHANGES_REQUIRED.** The recorded pass concerns the assertions actually
implemented by the pinned `break.py`. It does not establish satisfaction of
the conflicting or omitted prose obligations below. This completed run is
**not ABANDONED**. `PREREG.md`, `PROOF.md`, `SOURCES.tsv`, `break.py`,
`EXPECTED.txt`, and `RUN.md` remain unchanged; this correction neither
reruns nor retroactively repairs them.

This is an exposed reporting correction by the correction session, not an
additional independent scientific review. Source formulas inspected after
the original run are cited below to explain the discrepancies; they are
not retroactive evidence of an independent pre-exposure derivation. No
new scientific result, source-PR acceptance, merge or Canon promotion is
earned by this errata.

## E1. Frozen response identity differs from the executed assertion

[PREREG.md:66](https://github.com/mathorn1973/twist-j/blob/80d6814a6b7c871b2b46d8e52f764c78c26810b4/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/PREREG.md#L66)
requires `R0 = I4 - (1/2) P^T H S`. The pinned
[breaker:959–962](https://github.com/mathorn1973/twist-j/blob/80d6814a6b7c871b2b46d8e52f764c78c26810b4/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/break.py#L959-L962)
instead checks `R0 = -(1/4) P^T H S`, also used in `PROOF.md:127,140`.

The latter is the formula derived in the already authored
[#1581 source proof:423–451](https://github.com/mathorn1973/twist-j/blob/694e5839f50dc9ef19f28792c8c6b9d64307389d/probes/P-J-PHASE-THREE-REFERENCE-1/PROOF.md#L423-L451).
For example, that source gives `(P^T H S)[0,0] = 1421/1620`: the executed
formula gives `R0[0,0] = -1421/6480`, whereas the frozen prose formula
would give `1819/3240`. They are not equivalent expressions. A pass of
the implemented assertion does not pass the frozen textual target. The
incorrect target and its discrepancy remain recorded, not relabelled as
an executed successful check.

## E2. Frozen exact control vectors were not checked

[PREREG.md:37](https://github.com/mathorn1973/twist-j/blob/80d6814a6b7c871b2b46d8e52f764c78c26810b4/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/PREREG.md#L37)
specifies the old-port control's decoded pair as
`((0,-1/2,0,0), (1/2,0,0,0))`. The source-consistent pair reported later
in the [original REVIEW.md:86](https://github.com/mathorn1973/twist-j/blob/ab2d10a563d46799e6e595e23777bc156b284e85/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/REVIEW.md#L86)
is `((1/2,0,0,0), (1/2,1/2,0,0))`.

The distinction follows from the existing source specification: the
ready root selects `g2` and reaches `(q,r)=(1,4)`; the control piston
`(2,0,0,0)` selects `g3` and reaches `(1,0)`. The existing lift
`eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0)` gives the latter pair; see
[#1577 proof:54–59](https://github.com/mathorn1973/twist-j/blob/9c6a2471b72252d13eb45d4e58c77620ed8dfb92/probes/P-J-PHASE-PORT-SEPARATION-1/PROOF.md#L54-L59)
and the canonical apparatus lift cited in `SOURCES.tsv`.

The pinned `break.py:1199–1207` checks only that the decoded first source
is unchanged and the second differs. It does not assert the incorrect
exact pair frozen in the prose. That weaker check's pass is retained;
the incorrect exact numerical target was not satisfied by that pass and
is not an independently successful prediction.

## E3. Unfulfilled inverse and response-relation obligations

`PREREG.md:66` also requires independent construction of `F^{-1}` and
verification of `D2 = R1 K_{P^T H P}`. The breaker implements forward
`F_step` (`870–894`) and derives response matrices by forward basis
evolution (`925–963`). It supplies no independent wave/tape inverse or
inverse-composition audit, and does not define or check the displayed
`K_{P^T H P}` relation. Its Gaussian elimination for `R0^{-1}` is a
different operation, used by the reader.

The canonical dependency's `F_inverse` does not fulfill the promised
independent implementation. These obligations are **not delivered**;
this correction does not execute them or declare the undefined response
relation proved or disproved.

## E4. Written proof and evidence attribution require qualification

The assertion in `PROOF.md:140` that a nonzero upper-left `2 x 2`
determinant proves nonsingularity on `Q^4` is insufficient. The code
does perform full `4 x 4` elimination (`896–915`), but the claimed
determinant `14992667/13060694016` is not derived in the review's written
proof or explicitly computed by its breaker. The complete determinant
argument is in the cited #1581 source proof, inspected in the exposed
comparison phase. It must not be attributed to this review as a completed
independent written derivation.

`PROOF.md:145` also incorrectly calls `F` an “involution conjugate.” The
existing update is energy preserving but is not an involution: from
`u=v=0`, `A0=e0`, and other tapes zero, the first update has `v=2Pe0`
and the second has `u=2Pe0`, unlike the initial state. This is an
explanation from the printed update equations, not a newly executed
breaker. The source's conservation argument, rather than involutivity,
is the premise relevant to the two-kick energy bound.

## E5. Report actual resources and preserve the admission boundary

The [original REVIEW.md:143–146](https://github.com/mathorn1973/twist-j/blob/ab2d10a563d46799e6e595e23777bc156b284e85/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/REVIEW.md#L143-L146) offers shared-reference or shared-bit
alternatives alongside #1579's implemented resource count. The actual
[#1579 frozen carrier:85–103](https://github.com/mathorn1973/twist-j/blob/f48e0ce8ca86d707a5b2db458affb065419445df/probes/P-J-PHASE-DECLARED-CONTACT-1/PREREG.md#L85-L103)
has **four cells and two supplied bits**: two source cells and two
receiving/reference cells that are the downstream heads themselves.
There is no additional shared reference or collector transfer in that
prefix. Two sources, a separate shared reference and two separate heads
would already count five cells and would require a separately specified
transfer mechanism. Such alternatives are not results of this delivery.

The #1581 construction has seven cells: two sources, three restored shared
references and two collectors identified with the old heads. It also has
one restored work bit.
Its lower bound concerns three **binary outputs**, not a general minimum
of physical cells. Restoring source/reference/bit state does not restore
the complete funded apparatus. `B=5` covers the classical wave/tape
kicks; prefix and preparation energy remain unsupplied. Both inputs are
preloaded, and the second is captured early. The record-only reader omits
`d`; its five-phase dictionary does not detect absence, since the
outside-family zero piston aliases `j^4`. None of these statements grants
native/physical admission, independent late arrival or indefinite renewal.

## Continuation rule

The original completed computation, exact output and frozen materials
remain evidence of their actual scope. These discrepancies do not by
themselves falsify the original #1577/#1579/#1581 source conclusions, but
this review cannot supply an unqualified independent acceptance of all
its preregistered obligations. Any new scientific executable, corrected
formal contract or execution to fill the missing obligations requires a
**distinct successor scope and fresh pin**. It must disclose the existing
source exposure and may not resume, rewrite or reuse this completed pin.
