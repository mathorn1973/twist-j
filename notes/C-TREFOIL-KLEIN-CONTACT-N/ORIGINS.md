# Origin and custody of the two recovered investigations

**NON-CANONICAL / provenance only.** Git contains the scientific text and source checkers, not the original archive binaries or the historical machine output. The first historical investigation is Package A; the second is Package B. Both were recovered verbatim before this note was assembled.

| Original package | SHA-256 (original .zip bytes) | Role | Original text files |
|---|---|---|---|
| A | `2a11f8019860499f64c457f997c4f7171e0d3bad0e8f8b74d3e7787e69c975ff` | Marked Klein coordinates and one-cell fixed-word obstruction | 21 |
| B | `42c93cf6d83382af6282a927577fd1fba35153e0df25b287745e03c340ea13ff` | Declared contact actions, marked positive meridians and independent analysis | 25 |

## Explicit retention rule

This note preserves original scientifically relevant proofs, preregistered targets, contact contract and checker **source code** unchanged under `source-A/` and `source-B/`. `CUSTODY.tsv` is the exact content manifest for these committed texts.

The full original archives, historical stdout/stderr, machine-specific run metadata, temporary materializations, reconstructed output tables and redundant JSON reports are intentionally **not committed** because `POLICY.md` excludes raw transcripts, logs, duplicate historical outputs and backups. In particular, the original on-disk checkers' absolute `/tmp` paths, when present, are historical, not a working repo runtime contract. An archival re-run is not a public status promotion.

The two original archives exist in the author's Library under the respective names `TWIST-J_trojlistek_souradnice_a_nativni_mez.zip` and `TWIST-J_trojlistek_kontakt_a_kladne_meridiany.zip`; these are provenance references only, not a shared Git handoff surface. All scientific claims to be continued must be supported by the text committed here or by the authoritative public repo and its cited external sources.

## Reproduction boundary

The original B checkers were recorded as first-run local PASS, with replays matching the captured first stdout byte-for-byte. Original A author and reviewer checks had 59 and 94 checks respectively, matching scientifically on replay; one A checker's stdout includes an environment/version field and therefore is not byte-identical across Python versions. The two original A and three original B scripts live here as historical scientific source, **not** pinned public verifiers. The scoped public CI gate must be separately satisfied before any computation-based public `T`.

## References

- Public status and policy: `STATUS.md`, `POLICY.md`, `AGENTS.md`.
- Public scientific basis: `canon/CORE.md`, `canon/CANON.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`.
- Related open proposals: public PRs #1577, #1579, #1581, retained as separate lanes.
