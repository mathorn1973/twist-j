# P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1 result

Status: ABANDONED.

The preregistration identifier is consumed and must not be reused, renamed,
resumed, amended or reinterpreted.

## Why the gate never ran

The immutable pin was pushed as commit
`dbe4fcf453d1164e227eb86b00e7dc58409de38f`. Before any import or execution,
the two pinned files were read back from the public remote.

The pinned `PREREG.md` declares

```text
verifier sha256: da26458e9ffd6a25eb4165e0860aa1eddc1ce885dedf25f6e40bb7559ed9d626
verifier bytes:  4755
```

but the actual pinned remote verifier is

```text
blob sha:        849dde29cdd02a6eca5e56074fe4c695c7427345
sha256:          e224e4d21d2f0aa3161b5fc9452246d6eb94ccf3b97c203477f79447e8dadaff
bytes:           4753
line endings:    LF
final LF:        yes
```

The local pre-pin scratch copy used to calculate the declared metadata
contained a leading backslash followed by LF, bytes `5c 0a`, which were not
part of the uploaded remote verifier. Removing exactly those two bytes from
the scratch copy gives both the remote Git blob SHA and the remote byte
content. Thus the frozen metadata identifies a different byte string from the
pinned verifier.

The mismatch was found by the required remote readback. The verifier was never
imported or executed. Formal execution count is zero.

## Required terminal record

No scientific gate completed. Therefore this abandoned-pin record contains no
`EXPECTED.txt` and no `RUN.md`. It earns no scientific conclusion and fires no
scientific falsifier.

The unchanged pinned files remain the audit record:

```text
PREREG.md blob: 94ff2cde17b45152fa956d3842432a65a32cde88
verify.py blob: 849dde29cdd02a6eca5e56074fe4c695c7427345
```

Any continuation requires a new identifier, a new issue, a new branch, a
fresh preregistration pin, and a fresh accepted verifier. The successor must
name this abandoned predecessor and the reason for retargeting before its own
pin.

Public Canon v68, the registry, frontier, dependencies, evidence, gates and all
scientific statuses are unchanged.
