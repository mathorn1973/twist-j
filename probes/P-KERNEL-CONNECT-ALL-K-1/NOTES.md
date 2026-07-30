# P-KERNEL-CONNECT-ALL-K-1 provenance notes

Non-normative. Records the incubation provenance of this probe. No
scientific status is claimed here; the decision surface is `PREREG.md` and
the verifier is `verify.py`.

## Source package

This probe was inserted from the sealed incubation package
`kernel-fold-package-2026-07-18`, verified byte for byte against its
`MANIFEST.sha256`. The public probe references the package by manifest
hash, not by any private path.

Provenance files in the package (manifest sha256):

```
verify.py source     verify_kernel_connect_all_k.py
                     b6fd3cb513987aae9b9c6d5a5c31e26c2c9a34b4610582e8c8072ffaa33cccbc
PREREG source        PREREG_DRAFT_P-KERNEL-CONNECT-ALL-K-1.md
                     a2685d5c3e11e6cb789d7b61e826b09e6beb2e4c622067c608466596ea6dd9b4
candidate record     C-KERNEL-CONNECT-ALL-K-1.md
                     8a83d5abbb81b0472575dc7abef4a06d4496930aa62c41cf75a6f35d986708df
run record           C-KERNEL-CONNECT-ALL-K-1_RUN_2026-07-18.md
                     528867c6023d54947f0f17954f804553a4e08d9e0b4e82a352e3084870c6e268
incubation stdout    stdout_kernel_connect.txt
                     15685afbb9a96ca4ba2cb3787b4ddd74b57cd9d89436350ca7b4ee9542ac9709
```

## Finalization from the draft

`PREREG.md` is the package draft `PREREG_DRAFT_P-KERNEL-CONNECT-ALL-K-1.md`
with the DRAFT status block removed and every frozen field kept verbatim.
`verify.py` is a byte-identical copy of the package verifier (sha256 above).
The pin (this `PREREG.md` and `verify.py`) is committed and pushed before
any public execution on this branch; nothing in the decision surface may be
weakened after the pin.

## Incubation witnesses (not part of verify.py)

The exhaustive C witness `break_bfs_k2.c` and the invariant breaker
`break_invariants.py` are incubation evidence that exceeds the 120 s public
budget and are not part of `verify.py`. They are retained privately in the
source package and are committed here only if the owner elects to publish
them as witness source.
