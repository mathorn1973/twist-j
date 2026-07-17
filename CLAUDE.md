# CLAUDE.md

Guidance for Claude (Claude Code, Cowork, and similar agent environments)
working in this repository.

## Read first, in this order

1. `STATUS.md` — the authority gate. Confirm `STATE` and the declared Canon
   tag/commit/SHA-256 before any scientific work.
2. `AGENTS.md` — the binding agent manual and daily operating procedure.
3. `POLICY.md` — binding policy for probes, evidence, and releases.

Never infer authority from file age, internal version numbers, mirrors, or
attached copies. The public `main` branch at the declared Canon tag is the
only normative source.

## Repository map

- `canon/` — the normative Public Canon text, claim registry, ledger tables.
- `probes/` — preregistered probes (one directory per probe ID).
- `tools/` — exact verifiers (`check_*.py`) and ledger build scripts.
- `reproduce/` — independent reproduction instructions and manifests.
- `data/` — data manifests.
- `notes/`, `legacy/` — non-normative material.

## Verification

Run the relevant checkers from the repository root before proposing changes:

```sh
python3 tools/check_canon.py
python3 tools/check_ledger.py
python3 tools/check_policy.py
```

Do not edit `canon/` files to make a checker pass; a failing check means the
proposed change is wrong or requires the procedure in `AGENTS.md`.

## Working rules

- Do not commit directly to `main`; use a branch and open a pull request.
- Canon content changes follow the release procedure in `POLICY.md`; ordinary
  documentation fixes must not claim a new Canon version.
- Keep commits small and single-purpose; reference claim IDs
  (see `canon/REGISTRY.tsv`) where applicable.
