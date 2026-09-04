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
  names a stable three-file bundle under `reproduce/`; `PUBLIC_PROBE` requires
  the five-file preregistration, verifier, expected-output, run, and result core
  under `probes/`, while additional pinned breaker files may be included.
  A `PUBLIC_PROBE` location may also name the existing file
  `probes/<single-probe>/RESULT.md` with exactly those three POSIX path
  components. This entrypoint resolves to its parent probe directory for the
  same complete bundle hash and required-file and architecture checks. It
  never hashes only `RESULT.md`. Other filenames, nested paths, and
  `REPRODUCTION` file entrypoints are not aliases; directory locations retain
  their existing meaning. The literal entrypoint must agree in `REGISTRY.tsv`,
  `EVIDENCE.tsv`, and the latest `HISTORY.tsv` event.
  Reproduction hashes deliberately exclude `RUNS/`: immutable candidate
  content is pinned before formal run records arrive. The final activation
  gate checks every declared reproduction architecture requirement; public
  probe architecture evidence is recorded in its `RUN.md` and `RESULT.md`.
  Bundle manifests sort relative POSIX paths case-sensitively so case-mixed
  evidence filenames produce the same digest on every supported host.
- `HISTORY.tsv` starts at Public Canon v1 Genesis. It orders each claim's
  events explicitly and preserves the evidence identifier, location, and hash
  at every event. Later status, scope, and actual evidence changes append events;
  unrelated edits elsewhere in the Canon do not;
  retirement ends a chain and permits the claim to leave the current registry.
  It does not fabricate a detailed pre-public transition history; the legacy
  cutover audit is only a reconciliation record.
- `GATES.tsv` gives every declared layer gate a stable gate ID, an owning
  normative item, a closed `gate_kind`, and a public decision condition.
  Cross-layer gate kinds have distinct concrete L1--L6 endpoints. The sole
  same-layer kind is `OPEN_DECISION`; it has equal concrete endpoints and an
  open-obligation owner on that same concrete layer, and it represents a
  decision rather than a lift. `tools/check_gate_contract.py` validates every
  gate row directly: the gate kind fixes the required owner semantic type and
  public status, and a concrete cross-layer owner must land at `to_layer`.
  `MULTI` and `NOT_APPLICABLE` do not disable that cross-layer owner contract
  and may not own `OPEN_DECISION`. Separately, every declared dependency that
  actually crosses two distinct protocol layers must still name a matching
  cross-layer gate with the correct endpoints.
- `CORE_SELECTION.tsv` is the explicit, reviewable selection of closed claims
  used to generate the short core claim badges. Selection is policy, while
  statuses and scopes always come from `REGISTRY.tsv`.
- `FRONTIER_PROGRAMS.tsv` assigns every current live H/O claim to exactly one
  validated scheduling program with a queue role, work state, and work mode.
  `ROOT` and `FOLLOWUP` are queue positions, not scientific dependencies;
  `READY` permits scope or preregistration work but does not authorize a
  verifier; `BLOCKED` is scheduling metadata, not a dependency edge; and
  `STOP` requires definition work before computation. `FORMAL`, `EMPIRICAL`,
  and `ENRICHMENT` select work queues only. The table duplicates no status,
  scope, blocker, layer, gate, or evidence field. Those facts remain in
  `REGISTRY.tsv`, `DEPENDENCIES.tsv`, `NORMATIVE.tsv`, `GATES.tsv`, and
  `EVIDENCE.tsv`.

`tools/check_ledger.py` delegates ledger validation to
`tools/check_ledger_core.py`, requires the explicit gate contract, and then
applies the existing acyclic dependency, registry agreement, evidence hash,
continuous history and status-firewall checks. The historical cross-layer
rule remains unchanged: every dependency crossing two concrete protocol
layers requires a matching cross-layer gate. Same-layer `OPEN_DECISION` rows
are removed only from that cross-layer pass after the explicit gate-contract
checker has validated them; they remain counted public ledger objects.

These files are the machine-auditable companion-ledger surface of the current
Public Canon series.
Authority and activation state follow `STATUS.md`; their presence on another
ref neither promotes a claim nor creates a second authority.
