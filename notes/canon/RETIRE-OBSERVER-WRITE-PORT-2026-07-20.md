# RETIRE-OBSERVER-WRITE-PORT. Architecture category audit

**STATUS: NON-CANONICAL.** This file has no authority and changes no claim
status. It proposes one later, separately reviewed and versioned Canon fold.

```text
public issue        #84
base                Public Canon v11 ACTIVE
tag                 canon-v11
activation commit   3d8c6307f20d01ad50fc90ae1c5777926b884881
content commit      3dc0d4255ae47f0512e5dd656d92ceb308ab026a
Canon SHA-256       d20b064c8564af4e4a22ec3d0a84a9847a3705af84fd6fee2faa6b2710d7c7e8
claim               OBSERVER-WRITE-PORT
current status      H
proposed action     RETIRE
formal probe        none
```

The eventual fold must start from the then-current public `main`. The base
above is the currency stamp for this proposal only.

## 1. Falsifier first

Reject retirement if the pinned public architecture contains any of:

1. a typed public class of admissible decoder extensions beyond the declared
   partial decoder `D`;
2. a current public decoder-output edge into the autonomous update `U`;
3. a registered consumer that uses `OBSERVER-WRITE-PORT` independently of
   `DEF-ARCHITECTURE`.

The v11 audit finds none:

- `canon/CANON.md` lines 232 to 254 define `D` as a typed partial interface;
- `D_clock` is terminal, no output of `D` feeds `U`, and the declared graph is
  acyclic;
- totality, uniqueness, and completeness are explicitly not claimed;
- `canon/DEPENDENCIES.tsv` contains only the edge from
  `OBSERVER-WRITE-PORT` to `DEF-ARCHITECTURE`;
- no current item depends on `OBSERVER-WRITE-PORT`;
- `canon/GATES.tsv` and `canon/CORE_SELECTION.tsv` contain no row for it.

The retirement gate therefore survives.

## 2. Category finding

Public Canon already declares the current decoder topology:

```text
D_matter : dom(D_matter) subset K -> MatterData
D_geom   : dom(D_geom) subset K x MatterData -> GeometryData
D_clock  : dom(D_clock) subset K x MatterData x GeometryData
           -> ObservableHistory
```

Its functional order is matter, geometry, clock. `D_clock` is terminal. None
of the outputs feeds `U`. These are architecture clauses, not a theorem
awaiting proof.

The live H row says that no admissible observer output writes into `U`, fires
when a typed write channel is supplied, and asks a completed dependency graph
to prove that every output is terminal. This mixes two scopes:

1. on the declared v11 decoder, terminality is already definitional;
2. for future extensions, the class called admissible is not typed and the
   decoder is explicitly not complete.

Positive closure would only repeat the declared graph. A firing write channel
would change the graph and define a new architecture. The row is therefore a
category error at fixed architecture, not a scientific hypothesis with a
frozen carrier.

The correct disposition is `RETIRE`, not `F`, `T`, or `D`.

## 3. Existing definitions are sufficient

`canon/NORMATIVE.tsv` already contains:

```text
DEF-DECODER-CLOCK   DEFINITION
DEF-ARCHITECTURE    DEFINITION
```

The read-only topology is present in their Canon source. Adding
`DEF-DECODER-READONLY` would duplicate the architecture and create no new
information. The later fold must preserve both existing definition rows and
must not register a replacement claim.

## 4. Current ledger pin

The row being retired has scope SHA-256

```text
2514a441ac07d4532412dad08f6b8cdece22779c2dec7e811b5e8c8e7beeb6c0
```

Its current evidence tuple is

```text
EV-OBSERVER-WRITE-PORT
INLINE_CANON
inline
d20b064c8564af4e4a22ec3d0a84a9847a3705af84fd6fee2faa6b2710d7c7e8
architecture requirement: none
```

The latest history event is sequence 11 and preserves status `H`. The next
event must therefore be sequence 12 if this proposal is consumed directly
from v11.

## 5. Exact retirement event template

For an immediate v11 to v12 fold, append:

```tsv
CANON12-RETIRE-OBSERVER-WRITE-PORT	12	YYYY-MM-DD	canon-v12	OBSERVER-WRITE-PORT	RETIRE	H	RETIRED	2514a441ac07d4532412dad08f6b8cdece22779c2dec7e811b5e8c8e7beeb6c0	EV-OBSERVER-WRITE-PORT	inline	<CANON_V12_SHA256>	Retired as a category error: read-only behavior is already part of DEF-ARCHITECTURE, while no typed class of admissible future write-bearing decoder extensions is registered.
```

The release label, event identifier, sequences, and hashes must be re-keyed if
Canon advances before the fold. `RETIRE` ends the history chain. The validator
then permits the claim to leave the current registry and companion tables.

## 6. Exact later-fold operations

Append the final `RETIRE` event to `canon/HISTORY.tsv`, then remove the current
claim rows from:

```text
canon/REGISTRY.tsv
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
```

Remove the duplicate live H and queue references from section 18 of
`canon/CANON.md`. Preserve the typed partial-decoder definition in section 2,
including the terminal `D_clock`, the absence of output-to-`U` edges, the
acyclic graph, and the explicit non-claims of totality, uniqueness, and
completeness.

Do not change:

```text
DEF-DECODER-CLOCK
DEF-ARCHITECTURE
QUADRATIC-ENVELOPE-DECODER
QUADRATIC-DECODER-DATA
canon/GATES.tsv
canon/CORE_SELECTION.tsv
```

Because the fold edits `canon/CANON.md`, re-pin every remaining
`INLINE_CANON` evidence row to the new Canon SHA-256 and append its next
contiguous `EVIDENCE_CHANGE` history event. Starting directly from v11, 39
inline claims remain after retirement. Their usual next sequence is 12, with
these exceptions:

```text
CURVATURE-OPERATOR-CANONICAL   11
O-R2-K-JUNCTION-PIN             4
CARRY-J-CHECKPOINT              2
```

## 7. Observer-only v11 to v12 deltas

Before batching any other work, the expected machine-ledger changes are:

```text
REGISTRY claims       190 -> 189
T                      93 -> 93
D                      38 -> 38
C                      21 -> 21
H                       6 -> 5
O                      23 -> 23
F                       9 -> 9
live H/O               29 -> 28

NORMATIVE items       205 -> 204
DEPENDENCIES          251 -> 250
EVIDENCE rows         190 -> 189
INLINE_CANON rows      40 -> 39
architecture none      40 -> 39
HISTORY events        588 -> 628
GATES                    7 -> 7
CORE_SELECTION          30 -> 30
```

The history delta is one `RETIRE` plus 39 `EVIDENCE_CHANGE` events. Update the
expected partition, total, and count description in
`reproduce/status-separation/verify.py`; update
`reproduce/status-separation/EXPECTED.txt` to the resulting exact stdout.

Recompute every count and sequence if another proposal is folded first or if
multiple reviewed changes are deliberately composed in a later version.

## 8. Scope firewall

Retirement covers only the redundant `OBSERVER-WRITE-PORT` registry row. It
does not:

- prove read-only behavior for undefined future extensions;
- forbid a future write-bearing architecture;
- claim decoder totality, uniqueness, or completeness;
- alter `QUADRATIC-ENVELOPE-DECODER` or `QUADRATIC-DECODER-DATA`;
- promote an observer reading or any physical observer claim;
- cross action layers L1 to L6.

A future write port requires a newly typed architecture and a separately
preregistered claim. It does not retroactively falsify the v11 architecture
definition.

## 9. Version and activation boundary

Public Canon v11 remains authoritative while this proposal is reviewed. This
proposal branch must add only this note and must not edit Canon or ledger
files.

The later content fold is expected to touch:

```text
canon/CANON.md
canon/REGISTRY.tsv
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/HISTORY.tsv
canon/FRONTIER.md
canon/CORE.md
canon/CHANGELOG.md
canon/STATUS_COUNTS.tsv
canon/SHA256SUMS
reproduce/status-separation/verify.py
reproduce/status-separation/EXPECTED.txt
```

The separate release-form commit changes only:

```text
STATUS.md
README.md
CITATION.cff
```

The v11 activation tuple remains authoritative until the new release-form
commit is merged, tagged with the next integer Canon version, and passes
public readback. No frontier decrement is counted before activation.

## 10. Validation checklist for the later fold

The later fold must run and pass, at minimum:

```text
python tools/generate_canon_views.py --apply
python tools/generate_canon_views.py --check-dir canon
python tools/check_policy.py
python -m unittest discover -s tools -p "test_*.py"
python tools/check_canon.py
python tools/check_ledger.py
python tools/check_verifier.py --base <ACTUAL_FOLD_BASE_COMMIT>
python tools/check_reproduce.py --base <ACTUAL_FOLD_BASE_COMMIT>
python tools/check_activation.py --full --content-commit <NEXT_CONTENT_COMMIT>
git diff --check
```

No scientific verifier is required for this procedural retirement. The later
fold must still perform a named-file security review.
