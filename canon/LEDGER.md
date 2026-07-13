# Public Canon companion ledgers

`REGISTRY.tsv` remains the authoritative table of public claim identifiers,
statuses, scopes, Canon sections, evidence locations, and live decision
conditions.  Its six-column schema is unchanged.

The companion tables make the Public Canon v1 Genesis state auditable without
turning Git history or the private development archive into scientific
evidence:

- `NORMATIVE.tsv` inventories the public axiom, architectural definitions,
  empirical calibration anchor, and every registered claim by semantic kind.
- `DEPENDENCIES.tsv` contains declared logical dependencies and explicit open
  boundaries.  It does not infer dependencies from thematic proximity.
- `EVIDENCE.tsv` maps every registered claim to a SHA-256-pinned public
  evidence bundle and records its architecture requirement. A
  `two-architecture-pending` value is an explicit Genesis release debt; the
  final activation gate must reject it rather than treating an old informal
  run report as a formal record.
- `HISTORY.tsv` starts at Public Canon v1 Genesis.  It does not fabricate a
  detailed pre-public transition history; the legacy cutover audit is only a
  reconciliation record.
- `GATES.tsv` gives every currently declared cross-layer lift a stable gate ID
  and a public decision condition.
- `CORE_SELECTION.tsv` is the explicit, reviewable selection of closed claims
  used to generate the short core claim badges. Selection is policy, while
  statuses and scopes always come from `REGISTRY.tsv`.

`tools/check_ledger.py` requires an acyclic dependency graph, exact agreement
with `REGISTRY.tsv`, valid evidence hashes, continuous status history, and the
status firewall: theorem rows cannot require lower-status claims, and
dictionary rows cannot require open or falsified claims.

These files are a Genesis audit surface until the final reconciliation commit
and activation manifest pin them as part of the release bundle.  They create
no scientific promotion and no authority while `STATUS.md` says `GENESIS`.
