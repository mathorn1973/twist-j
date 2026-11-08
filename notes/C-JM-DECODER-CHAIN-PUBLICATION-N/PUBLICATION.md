# Publication record

NON-CANONICAL. Documentation/custody task #1696, not new scientific execution.
Public basis: `b8bb9ed3ca1403df71c5192959e64cc9a9fb5018` on main.
ACTIVE Public Canon v103; content `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`;
Canon SHA-256 `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`,
1052518 bytes. The declared tag/content ancestry, all five normative hashes,
policy/Canon/ledger/gate checks and required main checks passed. Authority
files are byte-identical to the previous fully read construction basis.

## Completed source packets

| Archive | SHA-256 |
|---|---|
| PROMO-C-PROJECTIVE-BORN-READING-N.zip | c4bff6a2ca59df327ed17e24c2c440847c35706dc83f19977e566d4438ce3bc7 |
| PROMO-C-JM-ORIENTED-QUADRATIC-READING-N.zip | c9987855b3cb4c1bc7470dfa826be62213fc13f6d7231f52e382d1d561283553 |
| PROMO-C-JM-SEAM-READOUT-COST-N.zip | adfa7f3ed69ae6547a4938d720631288b3180f60b6b286f6525ac2c79b3b9a39 |

Every member named by the original archive manifests matched its SHA-256.
Each individual PUBLICATION.md lists every byte-identical imported file and
any zero-byte omission. Scientific reports, preregistrations, source code,
stdout and historical run records were not corrected or reconciled with new
outside knowledge. Only README publication prefaces and new custody/scope
files were added; the local source manifests are preserved separately.

## Actual publication reproduction

Platform Linux, architecture x86_64, Python3.13.5. The oriented-quadratic
verifier used SymPy1.14.0; the remaining programs use only the standard library.
Commands ran with PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, TZ=UTC,
LC_ALL=C.UTF-8. Every exit code was0, stderr was empty, and stdout matched
its source file byte for byte:

| Program | Bytes | Stdout SHA-256 |
|---|---:|---|
| C-PROJECTIVE-BORN-READING-N/verify.py | 717 | def33b36b0915391157321aa844f17ff566d8610a26e87e052b7e15dd2c7587f |
| C-JM-ORIENTED-QUADRATIC-READING-N/verify.py | 1011 | f87b21e161ec65e26652a98b6e82b9864c64659219b3b6f5370da95a051e1d46 |
| C-JM-ORIENTED-QUADRATIC-READING-N/breaker.py | 387 | 0b60e2b2048b1785a96a34e107384cf7bc40620c69bdf3627613c619d6b1ba40 |
| C-JM-SEAM-READOUT-COST-N/verify.py | 524 | f257aaefb68461f91617fd0870bb98697ec602c4cf962d5ba816ba5f6af71492 |

Per-program JSON records bind the unchanged script hashes and outputs.
These were reproductions of already exposed evidence, not a new probe,
preregistration, architecture gate, independent confirmation or empirical test.
No failure was hidden and no threshold was altered. No newly written
scientific verifier was run for this publication.

## Integration boundary

The merged seam packet and open preparation/source packets remain at their
own commits and review surfaces. This PR only fills missing publication links
and archives the completed source packets; it neither cherry-picks nor copies
unmerged research into main. Exact commit links in README work before the
other PRs are merged. The author's scope clarification applies prospectively
to this chain without rewriting their frozen proof bodies or run records.

Current scope excludes edits to canon/, tools/, workflows, formal probes,
registered owner dispositions or public activation. Existing publications may
be reviewed independently. Original status is preserved even if repository
integrity checks pass. No review or merge is asserted by the source archive.
