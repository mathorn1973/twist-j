# Proof/dependency audit disposition

NON-CANONICAL / STATIC review with replay evidence / L1. Date: 2026-10-01.
This record is for the proposed mathematical fold, not a physical gate.
The consolidation author read the old proofs and both implementation lines.
That exposure is intentional and forbids describing this pass as independent
discovery or clean-room implementation. Separate independent review of this
new consolidated text remains required before a READY FOR FOLD decision.

## Authority and dependency custody

The coordinator freshly checked public main and the v95 authority gate.
Main and the peeled canon-v95 target are
`b8ba1a07ad776cdd8d878fe0a407e07312c0e263`; the declared content commit is
`5a1dd8ba6c339640940b5a013d3c412025a1f8fc`. The annotated tag object is
`7810207b27539ee35e30ffb0ed81cec32fa322c7`. Ancestry, current Canon
848893 bytes/SHA-256
`b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f`,
main checks and publication checks were verified; authority is still v95.
STATUS, POLICY, AGENTS, CORE, FRONTIER and relevant existing registry rows
were read for this audit. Remote collision/owner review belongs to the
coordinator's current authority record; this editorial note reserves no
new scientific probe and displaces none of #1303-#1318.

Fresh read-only GitHub PR metadata obtained by the coordinator, then read
by this audit, confirms the following exact heads are still OPEN. All three
required checks (architecture-x86_64, architecture-aarch64, check) are SUCCESS:

| PR | Current head | Current required-check run |
| --- | --- | --- |
| #1304 | dcfde46760bdfd4551686be1e99b5433fa6e9adf | 36784630463 |
| #1306 | 869998eb8c1c68f7a884fafbf683bf20db0eb7f1 | 36793890508 |
| #1308 | 23d57d1a0397a775f7b8ae3aaa7e2ca5dc93cf5f | 36833230091 |
| #1310 | dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2 | 36836950256 |
| #1312 | 04fa72ca2506398bf47a64fe33aa024625bd4f9b | 36842589477 |

The direct source #1316 is pinned at
`312d0a90b24d5f9e743096f0ee2a477cda719a10`, and design #1318 at
`4756a3df650b91fb1d30806b0fb2aaac00e50cc2`. Their pinned records are read
as noncanonical evidence, with no promotion from stack ancestry.

DEPENDENCIES.tsv was produced from actual `git show COMMIT:PATH` bytes,
not copied hash strings. It binds 55 authority/proof/evidence/runtime/design
files by exact commit, SHA-256 and byte count. Every file present in the
integration checkout matched those bytes. All six relevant proofs and the
fourteen listed bridge/runtime/expected inputs also matched their original
public scientific pins byte for byte. In particular #1304/#1306/#1308
were read directly at their own commits; their presence in historical
metadata was not used as a substitute for source inspection.

## Mathematical audit

The consolidation re-establishes the consumed selected-cell certificates,
funded gate and swap identities explicitly. The broader #1304 spectral
classification, #1306 isolated-cell period and #1308 different macrostep
are excluded. PROOF.md contains all matrices, rational split numerators,
divisibility/image tests, all rejection paths, complete ordered matter
recognition, and both writer inverse identities. Its proofs distinguish:

* 32N-1 original versus 32N extended coordinates;
* true electric rho and DE-rho versus the separate neutral contact graph;
* retained static/spectator energy versus active energy;
* occupied resource swaps versus destructive send/copy formulas;
* forward reverse-matter branch versus Ghat inverse, which subtracts
  e(Gc');
* all forward and inverse layer projections versus witness-only equality;
* all-N first arrival N-1, work N and original receiver return N+1;
* eight HIT boundaries versus seven elapsed steps, with no exact first
  reset assertion at N+8;
* all individual cuts and the specified y_minus=(0,0,1,-2) control;
* finite-energy recurrence versus permanent memory;
* mathematical definitions versus physical calibration or native selection.

No mathematical counterexample or missing algebraic premise was found in
this consolidation pass. The full proofs are conditional on the displayed
architecture, not on the truth of an unproved external field theorem.
The retained inherited claims and excluded generalizations are mapped in
CLAIM_MAP.tsv. No parent FRONTIER condition is partially claimed satisfied.

## Actual existing-verifier replays

The coordinator actually reran the unchanged three-bridge suite in a
Linux-compatible checkout after the old protocols were read, using Ubuntu
22.04 / WSL2, x86_64, CPython 3.10.12, assertions enabled:

```text
python3 -B tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

The runner exited 0. Its three exact success receipts were:

```text
REPRODUCE PASS FIELD-THREE-CELL-DELAYED-TRANSFER-N c1bcd8ade32c78d829a42b75f97e22842cebe5595a44bb52991d558ee1beefea 9d22bd31bbafd95b057e2ea230707db3947e6675d6bbaba25e854a141c20bf23
REPRODUCE PASS field-finite-chain-first-delivery-n bfbd1cec8e7b3bec1d3d41d703656e5d28b617d63fe8f1843f248a9f40c9324c c77b74b795dfe030c8b3dde34a8ff3755e9659d0e03da8f14b5245600640a394
REPRODUCE PASS field-work-record-unit-n b1b231508fca99a3d26474c46a75918774924cc9263a6688e38db5d185da57f9 ead14e75ea593819e24be8e9bdb178a7733b01ba6df87dfe853b453095208b80
```

Each receipt records actual execution under the existing runner's exit,
empty-scientific-stderr, timeout and exact-byte rules, not merely a hash
test. The #1310 bridge invokes both frozen main programs. The #1312
bridge invokes both generic adapters. The #1316 bridge invokes the two
extended adapters and original projection checks; it reuses the exposed
local arithmetic and does not execute predecessor main programs in their
place. No verifier, expected output, old proof, threshold or workflow was
changed. These are replays of previously pinned, known results, not a new
prospective scientific run or a new independent implementation.

Historical source evidence is separately recorded in each pinned RUN.md.
#1310 run 36836750687, #1312 run 36842242086 and #1316 run 36854724602
contain their respective reported actual x86_64/aarch64 scientific receipts
at CPython 3.12.14. Reading those source records is not a new CI execution.
The current local replay is one architecture. The earlier distinct source
reviews and two-architecture checks support their original scopes; neither
is silently promoted into independent review of this new editorial text.

## Disposition before separate review

At the end of the author's pass, **MATHEMATICAL CONSOLIDATION was
REVIEWABLE; separate review was pending.** The
concrete remaining gate is an independent reader checking PROOF.md and
the three scopes in CLAIM_MAP.tsv against the pinned sources, especially
the actual ordered-reaction recognition, inverse writer, all-N induction
and retention wording. Any review finding must identify a precise formula
or missing premise and be resolved before READY FOR FOLD. The following
independently authored section records completion of that review and
supersedes this initial pending status.

**PHYSICAL RESULT: NONE.** Stage A, Stage B, complete device and blinded
campaign have no measured evidence in this mathematical package. Their
absence does not falsify the conditional theorem. No formal new scientific
ID, status award, Canon edit, merge, activation, tag, release, purchase or
energization has been performed here.

## Independent review of the consolidated proof (C96-02 reviewer)

Date: 2026-10-01. Reviewer role: reserve-certifier implementer, separate from
the C96-01 consolidation author. This is an independent review of the new
editorial proof and claim scopes, not independent discovery, a clean-room
implementation, a new scientific run, or independent hardware qualification.
The reviewer had already read the exposed #1316/#1318 sources while preparing
the separate reserve work; that exposure is explicitly retained.

The reviewed bytes are:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PROOF.md | 21867 | 5b1b32cc541bb69217801b8b48e95c5bcd44a3c418a9f09dc85edb9efc0a7532 |
| CLAIM_MAP.tsv | 6841 | 33ce490cc2228a0a42c62ce0e0ed1852d67e620fbce0a750ac7f0fb4e0cc6ac6 |
| DELTA.md | 11376 | 2f547ecb39204b6630c289d99db015496efd46337df0737e67c7d603359e6c84 |
| DEPENDENCIES.tsv | 18959 | c2d05a4cf5531b085db89eab20eec9d39c38d798f4344e04a7de16a96b08db7e |

Final integration subsequently replaced seven empty `excluded_scope` cells
in the authority-context rows with `Not applicable (authority context)` to
avoid trailing tab whitespace. All 55 source commit/path/hash/length tuples
were independently rechecked by the coordinator and are unchanged. The final
table is 19,197 bytes, SHA-256
`c4e5b38416e1690f6c1841392b3bb1d97ca15947388cf64f9a6f021dea8e2958`.
The other three reviewed artifacts retain the exact bytes listed above.

**Disposition: no mathematical or scope defect found in those reviewed
bytes.** The separate-reader requirement for this editorial proof has been
performed. This does not award public T or decide the separate release gate.

The reviewer checked the complete 30N unrestricted plus 2N-1 nonnegative
original coordinates, the extra C5 coordinate, literal ordered reactions,
nonintegral split/image/funding rejection, arbitrary spectators and static
fields, and all actual charge/divergence/defect accounts. In particular,
individual reacting-register charge need not be preserved; their common-node
sum is what the proof preserves. The accepted gate pairs are disjoint and
both reverse funding guards follow from the original nonnegative resource.

The full-domain writer inverse uses the recovered input e(Gc'), with both
composition identities valid for every p. Forward AM-to-R leaves p unchanged;
it is not substituted for that inverse. Layer projection holds for both
chronologies, occupied swaps retain all old values, and cuts keep the old qj.
The N=2 empty ranges are handled in the contact permutation, arrival induction,
receiver return and fixed downstream control argument. The all-N first times
N-1/N/N+1 follow by induction rather than finite enumeration. The designated
offimage control is kept outside the image by the integer field automorphism.
The event-spacing inequality guarantees eight boundaries and seven elapsed
steps, with no permanent-memory or exact N+8 reset assertion. Positive
definiteness plus the displayed square identity makes each shell finite;
the bijection gives periodicity from the initial state, including each cut.

As auxiliary STATIC arithmetic checks, a separate short Python standard-library
calculation, importing none of the source verifiers, multiplied the displayed
matrices and computed determinants by the permutation formula. It confirmed
the cyclotomic conjugacy, L factorization/commutation/square, Vinv products,
energy-adjoint identities, triangular integer-image certificate, DC=0,
DP_E=0, C^t S_E=0 and the static divergence. The reviewer also read every
DEPENDENCIES.tsv row via `git show COMMIT:PATH` and independently recomputed
all 55 byte counts and SHA-256 values; all matched. These are static proof and
custody checks, not new formal scientific evidence or another architecture
run. The previously reported three-bridge replays were not rerun in this pass.

The three proposed claims stay inside the proved selected L1 architecture.
The broader #1304 classification, #1306 isolated-cell period, different #1308
chronology and #1314 law are not silently imported. Existing registry statuses
remain at their original scopes, and the copied FRONTIER clauses match the
current text. The device's SI scaling, C5 implementation, clock, metrology,
source provenance, apparatus-family completeness and native U/J selection
remain explicit open physical/selection debts. No extra Canon claim is needed
for a matrix identity, coordinate count, chosen energy offset or charged
three-cell illustration.
