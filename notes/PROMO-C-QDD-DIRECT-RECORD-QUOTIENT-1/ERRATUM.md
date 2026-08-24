# ERRATUM: QDD_DIRECT_RECORD_PROMO_SHA256SUMS

Status: **NON-CANONICAL. DISCLOSURE RECORD.**

This erratum records a defect in the integrity manifest of this package. It
changes no scientific content, no status, no scope, and no Canon row. It does
not repair the manifest: an integrity record is not rewritten after
publication, because a silent rewrite destroys exactly the evidence a reader
needs to judge the defect.

```text
recorded      2026-08-24
basis         Public Canon v62, mathorn1973/twist-j main
              ec810acad66ab73631fdfa7e582043e7363eb435
              tag canon-v62, CONTENT_COMMIT
              72d7fdaf131f999763bb0904e50e8841245027ff
package       notes/PROMO-C-QDD-DIRECT-RECORD-QUOTIENT-1/
manifest      QDD_DIRECT_RECORD_PROMO_SHA256SUMS
owner lane    issue #107
```

## 1. The defect

The package README requires that, from the package directory,

```text
sha256sum -c QDD_DIRECT_RECORD_PROMO_SHA256SUMS
```

must pass. It does not. It reports 23 of 24 entries `OK` and one `FAILED`:

```text
C-QDD-DIRECT-RECORD-QUOTIENT-1-N/verify.py: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

The two values are:

```text
manifest asserts   3416f1b1a9176f308d93eac388c083713216988fba3ba713e236249e5bc07a6d
file actually is   e3dee4357e821fcfe62af8c282c97ad3e8ee06c928dca7c0369394ed6bcb6a04
file size          4714 bytes
git blob           80623a58b9098319553f4994b1bbc18e48cec3c2
```

## 2. What was ruled out

The asserted hash is not a stale record of any earlier state of this file, and
not a mis-transcription of a neighbouring entry.

```text
file history        one commit only, 0e4c64f "Publish noncanonical QDD
                    direct-record promotion package". The file has never been
                    modified since it entered the repository.
object store scan   every blob reachable from every ref in the full
                    (unshallowed) history was hashed. The asserted value
                    3416f1b1 matches NO blob anywhere in the repository,
                    at any commit, on any branch.
line endings        the file contains no CR byte and ends in exactly one
                    newline. CRLF conversion, stripping the final newline,
                    adding a newline, and CR-only conversion each produce a
                    different hash, and none of them is 3416f1b1.
sibling swap        the two sibling verifiers hash to f23aa3ed and ae0d6743.
                    Neither is 3416f1b1, so the entry is not a copied
                    neighbour line.
```

The remaining explanation consistent with all four observations is that the
asserted value was already wrong when the manifest was authored, upstream of
publication, in the source archive. The published bytes are not in question;
the record of them is.

## 3. Why the scientific content is unaffected

The affected file is the verifier of `C-QDD-DIRECT-RECORD-QUOTIENT-1-N`. As
published, it reproduces its own pinned output byte for byte:

```text
command        python3 verify.py
exit code      0
stderr         0 bytes
stdout         byte-identical to the committed VERIFY.out (568 bytes)
platform       Linux, one lane
```

The verifier therefore still audits the candidate it was published to audit,
and every other entry in the manifest verifies. This is reproduction on one
lane only. It is not a public formal run, not a two-architecture gate, and not
independent confirmation, and it does not raise the candidate above the
`candidate-T / NON-CANONICAL` status recorded in `RESULT.md`.

## 4. Disposition

```text
DONE      this disclosure record
NOT DONE  no edit to QDD_DIRECT_RECORD_PROMO_SHA256SUMS
NOT DONE  no edit to verify.py, VERIFY.out, RESULT.md or any inner file
NOT DONE  no status, scope, registry, frontier, gate or Canon change
```

A reader checking this package should expect the one `FAILED` line above,
compare it against section 1, and treat the remaining 23 entries as the
integrity surface of the package. Any future republication of this material
must regenerate the manifest from the published bytes rather than carry the
archive value forward.

The owner of issue #107 may adopt, amend, or supersede this record. Its
existence does not itself close the defect.
