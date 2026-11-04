# Provenance and exposed predecessor outcome

NON-CANONICAL / L1. P-POLE-HEIGHT-FULL-SCHREIER-1 is a new prospective
construction attempt, reserved in issue1905. It does not resume or change
a sealed verifier. Current public Canon authority and exact source bindings
are recorded separately in SOURCES.tsv.

## Sealed predecessor

The immediate predecessor is [PR1904](https://github.com/mathorn1973/twist-j/pull/1904),
P-POLE-HEIGHT-STABILIZER-CHAIN-1:

- source pin: `38450ba5a54f0aa80c681092f3fbb5fc36161733`;
- result head: `7151f512fa203ca5aeb1c729a06422afcae21ea5`;
- verifier SHA-256: `c8a37c2db5c5731d1df5a985e695576b39293397c45d91e70d60c48b8a5c8317`;
- exact stdout: 10576 bytes, 15 LF lines, SHA-256
  `efc4392c5d719fdb15edb5d4553b26bcbb578a2189e4c336487784b5f536093e`.

The first author run passed its finite audits and returned
INCONCLUSIVE_MINUS_TRANSPORT. It established a complete zero orbit of
1556 states and 99584 directed bank edges, with an explicit 65-contact
zero bridge. Its complete tree and edge family represents the full zero
stabilizer. The construction then retained a 4096-word short pool and
selected 95 undirected generators, or 190 directions. Its two 32768-step
walks visited 765 and 805 states, with no meeting. These are sampled-state
counts, not complete subgroup orbit sizes. It retained 2048 collision
words but no minus bridge, so the plus stage did not run. The search used
2316921 logical elementary contacts.

Those outcomes were all known before this new source pin. They motivate
the changed construction and are not blind predictions. The predecessor
miss does not diagnose whether the short-word pool, action-diversity
filter, restart depth or another restriction was responsible. It excludes
neither its selected subgroup nor the full zero stabilizer.

The predecessor also certified seven small-stock exclusions and the
compositional W38-plus-zero-bridge result for inputs -1,0,+1, at 103
contacts before cross-boundary reduction. That was not an all-five final
word audit or a shortest-word claim. Those certificates are preserved;
this successor does not rerun the small-stock census.

Before this source pin, the coordinator read back successful x86_64,
aarch64 and aggregate checks for the predecessor in
[CI run41883960120](https://github.com/mathorn1973/twist-j/actions/runs/41883960120),
including the matching scientific output and 219 repository tests.
That acceptance applies to the predecessor's actual scope. It does not
pre-approve the new construction.

## Fixed data and reused arithmetic

BANK.json is unchanged: 7943 bytes, SHA-256
`d4270e03f851f0d2327e2eac7f23cc796b9bbffb1e54b2943f52a0c89fb83f07`.
It contains the one EXTENSION_ROOTS record and 64 MACRO records extracted
from the public P-POLE-HEIGHT-COMMON-ODD-1 output in
[PR1902](https://github.com/mathorn1973/twist-j/pull/1902).
That source output has 18997 bytes and SHA-256
`966de8e350775121ab6d2b38379a82f6206205d919661976415249da0189fcaf`.
The fixture supplies the same W38 residuals, exact targets and inverse-paired
odd-returning bank. It is a fixed data input, not a new archive discovery.

The new verifier copies the predecessor's scalar arithmetic into its own
source: the four-coefficient power basis and the normalized five-coefficient
quotient route, with exact invariant and inverse checks. These remain two
arithmetic representations. Copying them creates neither a third independent
implementation nor an independent-session reproduction. The old verifier
and supplied review scripts are not executed or imported to supply the new
search. Every copied line is covered by the new source pin and static review.

## External pre-exposure

The prior review archive `review-scripts-round4-20261104.zip`, SHA-256
`71e340b1fc174a4ca01261913db0825d9be2a30879f119f59e7a350806d1e960`, was
received before the predecessor. Its complete entry manifest and static
review limits are bound in that predecessor's PROVENANCE.md. No supplied
scientific script was executed or imported by this authoring session.

Its reported individual even orbits and common-odd minimum remain exposed
information unless separately audited. In particular, a reported individual
target in each bank orbit is not a common-word certificate. The external
stock census tested the first four cells; successes there do not alone
certify helper restoration. The previously missing round-three archive was
not retroactively received by inspecting round four.

## New construction and outcome boundary

The new program represents the complete zero-Schreier family by shared
expression paths, examines its root images and constructs target-returning
collision words for the next component. It removes the predecessor's
4096-short-word selection from that family. This does not make a root-image
scan a complete orbit search, nor prove that the subsequently constructed
collision family is the full next stabilizer. The exact caps, ordering,
walk fallbacks and acceptance conditions are frozen in PREREG.md and code.

Any reported common-five witness requires one explicit chronological
contact word, complete helper endpoints, both arithmetic routes and all
five inverse recoveries. A bounded miss remains inconclusive at its stated
scope. All scientific execution of this new verifier follows its new public
pin and readback. Static reviews are authoring checks. No physical action,
autonomous preparation, alpha normalization or Canon promotion is implied.
