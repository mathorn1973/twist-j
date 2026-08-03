# RETYPE-COIN-MINIMAL-READ

**STATUS: NON-CANONICAL OWNER DISPOSITION. NO PROBE RUN. NO CANON CHANGE.**
This note has no normative authority and changes no claim, gate, frontier,
count, hash, tag, release, or status. It records one owner-approved input for
a later, separately sealed Public Canon v35 fold. It does not approve or seal
that fold and does not authorize a standalone Canon edit.

```text
candidate queue       Public Canon v35 composed-fold queue;
                      no public probe issue required
public base           Public Canon v34 ACTIVE
base main             76d3c3b70f7720a44a8c9ad30ef0c5fb550f4d38
tag                   canon-v34
content commit        b15bde93045a6650955ce6cca17e7f755a71d4b9
Canon SHA-256         1a26e8054a8d5ac1025917370fbbe0f4df583e52fe90186a69ec19a9982d9fcc
Canon bytes           172167
claim                 COIN-MINIMAL-READ
current status        H
owner decision        STATUS_CHANGE H -> D at byte-identical scope and
                      byte-identical falsifier
owner decision date   2026-08-03
supersedes            all operative H-typing instructions for
                      COIN-MINIMAL-READ in the v27 disposition
public evidence       unchanged, EV-COIN-MINIMAL-READ
formal execution      no new formal probe execution or evidence record;
                      mandatory CI replays remain required
fold intake           approved owner input; not yet applied
provisional release   Public Canon v35, composed with other approved inputs
```

The eventual fold must start from the then-current public `main`. The tuple
above is the currency stamp for this disposition, not permission to reuse stale
release fields. All counts, hashes, and path deltas must be recomputed when
the owner seals the v35 manifest.

This disposition is ready for v35 fold intake. The builder may apply it only
inside the complete composed content commit `C`, after revalidating the public
base and every field below. It must enter before `C` is sealed. If the v35
content commit is already pinned without this input, the disposition rolls
forward to the next unsealed positive-integer release; it is never injected
into a pinned or activated v35 tree.

## 1. Owner decision

In the next sealed fold that applies this disposition, reclassify the
registered claim `COIN-MINIMAL-READ` from `H` to `D` with byte-identical scope
and byte-identical falsifier. No other registry field moves.

This supersedes the v27 owner disposition
`notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md` only where it types
`COIN-MINIMAL-READ` as `H` or instructs later text or folds to do so. That
includes the metadata field and the operative H-typing language in sections
1, 3, 5, 6, and 9. In particular, it supersedes:

- section 1: "The future dictionary choice is `beta_1 [H]`, not `T` or `D`.";
- section 9: "It remains H until MINIMAL-READ-DERIVATION closes."

All non-status content in that disposition stands, in particular the adopted
name MINIMAL-READ, its two exact selection criteria, the named unadopted
counter-selector MAXIMAL-REACH, the separation of the derivation debt into
`MINIMAL-READ-DERIVATION [O]`, and the naming firewall of its section 9. The
current registered scope and falsifier remain byte-identical under this
disposition. The v27 note remains the historical record of the original
adoption.

## 2. Why the type moves

The registered scope sentence already is a dictionary adoption, not a
hypothesis about the world or the architecture:

> among the publicly proved complete pair {beta_1,beta_3}, the Canon
> dictionary adopts beta_1 by MINIMAL-READ ... no claim that the decoder
> architecture forces MINIMAL-READ is included

The Canon narrative itself calls the row "the adopted L1 dictionary premise"
(`canon/CANON.md`, status-separation narrative). Canon practice carries every
comparable adopted reading as `D`: `BOOST-COUNT-LADDER [D]`,
`PENTIT-ROOT-READING [D]`, `AXIOM-PROJECTION-DICTIONARY [D]`,
`COSMOLOGY-READING-DICTIONARY [D]`, and thirty-six further `DICTIONARY` rows
in `canon/NORMATIVE.tsv`. Among the four current `H` rows, the other three
(`NS-TILT`, `OBSERVER-WRITE-PORT`, `LAMBDA-COCYCLE-ANGLES`) assert falsifiable
content beyond an adopted reading; `COIN-MINIMAL-READ` alone does not.

The hypothesis content that the v27 disposition wanted kept at risk, namely
whether the architecture forces the selector, is exactly owned by
`MINIMAL-READ-DERIVATION [O]` and its gate `GATE-L5-L1-MINIMAL-READ`
(OPEN_SELECTION). That row stays `O` and `STOP`, unchanged, live, and ROOT in
`DECODER_CORE`. The retype closes nothing and derives nothing.

Analogous public precedent: `CANON12-POL-READ` moved `POL-READ` `O -> D` at
canon-v12 with the rationale "the physical naming remains a decoder
dictionary and no independent propagation law is introduced". That event
also changed the registered scope and falsifier after an exact derivation, so
it is not a byte-identical retype precedent. The stronger mechanical basis
here is the enforced `D`/`DICTIONARY` correspondence and the already public
theorem support for the adopted sentence. Precedent that a `D` row may carry
a live falsifier: `TIME-CUT-READING [D]`.

The rigid public order places `D` above `H`, so this is formally an upward
status reclassification. Guard against promotion by rewriting: the scope and
falsifier bytes do not change, so the registered sentence gains no content or
scope strength; only its type label moves to match what the sentence already
says. The falsifier stays armed: an exact public derivation uniquely forcing
`beta_3` still fires the row, now as `D -> F`. It also closes
`MINIMAL-READ-DERIVATION` negatively only when the O row's additional
condition is met that the complete admissible decoder class is proved
nonempty.

## 3. What does not change

- `MINIMAL-READ-DERIVATION [O]`: untouched, stays O and STOP.
- `GATE-L5-L1-MINIMAL-READ`: untouched.
- `COIN-SELECTION-CONDITIONAL [T]` and `READ-REDUNDANCY-PRIME-SUPPORT [T]`:
  untouched.
- `EV-COIN-MINIMAL-READ`, bundle
  `0e2c9daaee5a7c189615f1941894015be2b9e59a71a1183cfc6ed207c9c8d083`:
  unchanged evidence, with no new formal probe execution or evidence record;
  the mandatory architecture CI replays still run.
- MAXIMAL-REACH remains named and not adopted; no new selector, premise,
  theorem, or lift appears.
- `OBSERVER-WRITE-PORT [H]` and every dependency edge and topology of the v27
  split: unchanged; only the status-stale COIN edge rationale wording listed
  below moves.

## 4. Required v35 fold surface for this input

The composed content fold must update, at minimum:

```text
canon/REGISTRY.tsv          status H -> D, all other bytes identical
canon/NORMATIVE.tsv         item_type HYPOTHESIS -> DICTIONARY, status H -> D
canon/FRONTIER_PROGRAMS.tsv remove the COIN-MINIMAL-READ row; required,
                            check_ledger LIVE_STATUSES is {H,O}
canon/FRONTIER.md           regenerate; the row leaves; live 28 -> 27
canon/DEPENDENCIES.tsv      reword the edge rationale "the adopted H-level
                            choice rests on" to name the dictionary choice;
                            the edge itself is unchanged
canon/HISTORY.tsv           append the STATUS_CHANGE event of section 5
canon/CANON.md              update all five status-dependent claim surfaces:
                            the section 10 adoption paragraph; the later
                            READ-REDUNDANCY paragraph; the status-separation
                            narrative, including "hypothesis"; the registry
                            mirror and its H/O wording; and removal of the
                            COIN row from the OBSERVER frontier digest;
                            update current release identity and v35 ledger text
canon/CORE.md               update the release identity to v35; the selected
                            stable-orientation claim list is otherwise unchanged
canon/STATUS_COUNTS.tsv     status_D 40 -> 41, status_H 4 -> 3,
                            live_H_O 28 -> 27; total stays 220 and status_T 118
canon/CHANGELOG.md          v35 entry
canon/SHA256SUMS            recompute
reproduce/status-separation/verify.py
                            BOOST check: has_status H -> D, item_type
                            HYPOTHESIS -> DICTIONARY, title becomes
                            "MINIMAL-READ is D with derivation O", and the
                            COIN row must be absent from program metadata;
                            partition constants {"T":118,"D":41,"C":24,
                            "F":10,"H":3,"O":24}, total 220; 21 checks
reproduce/status-separation/EXPECTED.txt
                            regenerate byte-exact; RESULT remains 21/21
reproduce/status-separation/README.md
                            "the MINIMAL-READ H/O rows" -> D/O wording
tools/test_architecture_map_report.py
                            anchored status counts D 40 -> 41 and H 4 -> 3;
                            total and evidence counts remain unchanged
```

`canon/GATES.tsv` and `canon/EVIDENCE.tsv` are expected untouched. Per
policy, the content-fold pull request changes `canon/`, so both architecture
jobs widen to every public probe and minimal reproduction; the
status-separation triple must therefore move in the same content commit, not
in a follow-up.

## 5. HISTORY event for the sealed fold

The fold must append a `STATUS_CHANGE` event following the
`CANON12-POL-READ` pattern. Sequence, date, and release are reconfirmed at seal
time. With no intervening event for this claim, its next event sequence is 2:

```text
event_id          CANON35-COIN-MINIMAL-READ
event_sequence    2, reconfirmed at seal time
event_date        fixed at seal time
release           canon-v35
claim_id          COIN-MINIMAL-READ
event_type        STATUS_CHANGE
previous_status   H
new_status        D
scope_sha256      unchanged scope bytes; expected to equal the v27 DECLARE
                  value 47811ef80aafa07e1682084bbc2d9cc268287dea254997f83704b6fc38df415a,
                  recomputed at fold time
evidence_id       EV-COIN-MINIMAL-READ
evidence_location probes/P-BOOST-COHERENCE-1
evidence_sha256   0e2c9daaee5a7c189615f1941894015be2b9e59a71a1183cfc6ed207c9c8d083
rationale         the registered sentence is a dictionary adoption of the
                  proved conditional ranking, not a hypothesis; the scope and
                  falsifier bytes are unchanged, the architectural question
                  remains owned by MINIMAL-READ-DERIVATION [O] and its
                  OPEN_SELECTION gate, and no derivation, closure, or
                  promotion of content is claimed
```

## 6. Release topology and pipeline handoff

The v35 release preserves the queue topology `B <- C <- R`: `B` the
then-current public base, `C` one complete composed content commit, `R` the
release-form commit changing exactly `STATUS.md`, `README.md`, and
`CITATION.cff`.

This approval is notes-only and changes exactly this Markdown file. It creates
no Canon authority, claim, status, tag, or release. The note must first merge
through a reviewed notes-only pull request and be read back byte-for-byte from
public `main`. Only after that readback may a fresh v35 fold branch and
worktree be created from the then-current public `main`. This notes branch is
not the release branch.

## 7. Scope and safety firewall

This note:

- contains no executable artifact and runs no verifier;
- changes no public Canon byte;
- creates no theorem, dictionary, obligation, gate, dependency, or evidence;
- claims no derivation of MINIMAL-READ and no decoder completion;
- does not close, reopen, or reword `MINIMAL-READ-DERIVATION`;
- does not adopt MAXIMAL-REACH and names no new selector;
- does not retire the v27 disposition note, which remains the record of the
  original adoption;
- records no secret, credential, private hostname, machine nickname, binary,
  or personal datum.

Public Canon v34 remains fully authoritative. This disposition approves only
the retyping input and changes no public Canon byte. The Markdown note becomes
public only through its reviewed notes-only merge and must then pass
byte-for-byte readback before any fold branch is created. Inclusion in Public
Canon v35 remains provisional until the owner separately seals the complete
manifest and the complete v35 content and release-form pipeline is reviewed,
merged, tagged, and validated. If v35 content is pinned first, this input rolls
forward as stated above.
