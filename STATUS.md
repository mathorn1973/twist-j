# Status

```text
STATE:          ACTIVE
CANON:          Public Canon v30
AUTHORITY:      mathorn1973/twist-j main
CUTOVER:        2026-07-13
TAG:            canon-v30
CONTENT_COMMIT: 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
CANON_SHA256:   2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a
CANON_BYTES:    157167
```

Public Canon v30 is the normative public ledger of TWIST-J. Authority begins
only when this activation form is merged into public `main` and the merge
commit is published under the tag `canon-v30`; the same form on any other
branch is an activation candidate, not an activation.

## Independent archival

The Canon is archived at Software Heritage, a non-commercial archive backed by
UNESCO and Inria. This is a preservation copy and a citation surface, not a
competing authority: the fields above remain the only declaration of authority,
and the archive holds whatever `main` held when it was visited.

Archived 2026-07-30 from `https://github.com/mathorn1973/twist-j`. The
identifiers below are SWHIDs, intrinsic content-addressed identifiers
standardised as ISO/IEC 18670, and each pins bytes rather than a location:

- the content of `canon/CANON.md` at Public Canon v27 —
  `swh:1:cnt:99fbf396ad353267c1dae996e47c5562399cf29a`
- the revision named as the content commit of Public Canon v27 —
  `swh:1:rev:116b62edf505914d96fcd65318d97f3675c53f85`
- the snapshot of the origin at the archiving visit —
  `swh:1:snp:735c0fe3dbf7f8fbe3f8559411a5309d1305e9d3`

Software Heritage independently reports the archived `canon/CANON.md` as
150959 bytes with SHA-256
`c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6`. Both agree
with the byte count and checksum this file declared for Public Canon v27, so
the archive is a third-party witness to them and not merely a copy. The fields
above declare the current Canon, which is a later version and is not covered by
these identifiers.

To cite the Canon with the resolution context included:

    swh:1:cnt:99fbf396ad353267c1dae996e47c5562399cf29a;origin=https://github.com/mathorn1973/twist-j;visit=swh:1:snp:735c0fe3dbf7f8fbe3f8559411a5309d1305e9d3;anchor=swh:1:rev:116b62edf505914d96fcd65318d97f3675c53f85;path=/canon/CANON.md

A later Canon version requires a new visit and yields new identifiers; these
three are fixed to v27 for ever and are not updated in place.
