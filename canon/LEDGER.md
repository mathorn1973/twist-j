# Public Canon companion ledgers

`REGISTRY.tsv` remains the authoritative table of public claim identifiers,
statuses, scopes, Canon sections, evidence locations, and live decision
conditions.  Its six-column schema is unchanged.

The companion tables make the current Public Canon auditable without turning Git
history or the private development archive into scientific evidence:

- `NORMATIVE.tsv` inventories the public axiom, architectural definitions,
  empirical calibration anchor, and every registered claim by semantic kind.
- `DEPENDENCIES.tsv` contains declared logical dependencies and explicit open
  boundaries.  It does not infer dependencies from thematic proximity.
- `EVIDENCE.tsv` maps every registered claim to a SHA-256-pinned public
  evidence identity and records its architecture requirement. `INLINE_CANON`
  uses `registry-scope-sha256-v1`: the digest is the exact UTF-8 hash of that
  claim's current `REGISTRY.tsv` scope. The immutable release tag,
  `canon/SHA256SUMS`, and the published activation manifest separately pin the
  full Canon and repository bytes. This two-level pin keeps an unrelated Canon
  edit from manufacturing a claim-level evidence change. `REPRODUCTION`
  names a stable three-file bundle under `reproduce/`; `PUBLIC_PROBE` names
  the five-file preregistration, run, and result bundle under `probes/`.
  Reproduction hashes deliberately exclude `RUNS/`: immutable candidate
  content is pinned before formal run records arrive. The final activation
  gate checks every declared reproduction architecture requirement; public
  probe architecture evidence is recorded in its `RUN.md` and `RESULT.md`.
- `HISTORY.tsv` starts at Public Canon v1 Genesis. It orders each claim's
  events explicitly and preserves the evidence identifier, location, and hash
  at every event. Later status, scope, and actual evidence changes append events;
  unrelated edits elsewhere in the Canon do not;
  retirement ends a chain and permits the claim to leave the current registry.
  It does not fabricate a detailed pre-public transition history; the legacy
  cutover audit is only a reconciliation record.
- `GATES.tsv` gives every currently declared cross-layer lift a stable gate ID,
  an owning normative item, and a public decision condition. Items without an
  explicit L1--L6 role remain `NOT_APPLICABLE`; that value does not invent a
  protocol placement. Every declared dependency that actually crosses two
  distinct protocol layers must name a matching gate.
- `CORE_SELECTION.tsv` is the explicit, reviewable selection of closed claims
  used to generate the short core claim badges. Selection is policy, while
  statuses and scopes always come from `REGISTRY.tsv`.

`tools/check_ledger.py` requires an acyclic dependency graph, exact agreement
with `REGISTRY.tsv`, valid evidence hashes, continuous status history, and the
status firewall: theorem rows cannot require lower-status claims, and
dictionary rows cannot require open or falsified claims.

These files are the machine-auditable companion-ledger surface of the current
Public Canon series.
Authority and activation state follow `STATUS.md`; their presence on another
ref neither promotes a claim nor creates a second authority.
