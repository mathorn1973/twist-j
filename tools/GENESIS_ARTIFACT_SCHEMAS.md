# Genesis artifact schemas

These schemas are the interface between the parallel x86_64 tooling lane and
the aarch64 reconstruction lane. All documents remain non-canonical while the
repository is in `GENESIS`.

Policy permits `notes/` and `data/`; it does not permit new generic root
directories named `genesis/` or `prereg/`. The required paths are therefore:

```text
notes/genesis/recon/RECONSTRUCTION.tsv
notes/genesis/recon/FRONTIER_SPLITS.tsv
notes/prereg/post-genesis/*.md
data/EXTERNAL_SOURCES.tsv
data/ENGINEERING_DISPOSITION.tsv
notes/ENGINEERING.md
```

`RECONSTRUCTION.tsv`:

```text
item_id current_claim_id action public_statement evidence_required post_genesis_probe blocker
```

`action` is one of `KEEP_PRECISE_O`, `KEEP_PRECISE_H`, `SPLIT`, `RETIRE`,
`REMOVE_PROSE`, or `PORT_PREREG`. Exactly the nine Genesis reconstruction
items named by the roadmap must appear once.

`FRONTIER_SPLITS.tsv`:

```text
parent_id child_id child_status layer decision_condition dependencies
```

Children remain `H` or `O`; Genesis splitting does not promote them. Multiple
dependencies use semicolons, and `-` means no declared dependency.

`EXTERNAL_SOURCES.tsv` uses the review schema verbatim:

```text
source_id observable source_title edition DOI_or_record value uncertainty units scheme access_date local_hash license
```

`local_hash` is a lowercase SHA-256 when a licensed local fixture exists and
`NOT-LOCAL` otherwise. A remote record identifier and license are still
required.

`ENGINEERING_DISPOSITION.tsv`:

```text
item_id canon_locator observable value source_id action evidence_path rationale
```

Allowed actions are `KEEP_MEASURED`, `KEEP_ENGINEERING`, `MOVE_TO_NOTES`,
`REMOVE`, and `PUBLIC_C_EVIDENCE`. Retained comparisons need valid
`source_id` entries; multiple sources are separated by semicolons. A public
computed claim needs an existing evidence path. Every `canon_locator` must
occur in `canon/CANON.md`, and every moved item must be named in
`notes/ENGINEERING.md`.

Each preregistration draft declares `NON-CANONICAL DRAFT` and contains these
bold fields:

```text
Claim
Action layer
Input object
Observable
PASS
FAIL
Budget
Stop rule
Post-pin changes
```

No draft may contain `RUN.md`, `RESULT.md`, `EXPECTED.txt`, an earned status,
or a formal result during Genesis.
