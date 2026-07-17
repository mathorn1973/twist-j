# Cross-branch transfer audit

```text
STATUS:          NON-CANONICAL INCUBATION RECORD
PUBLIC CLAIMS:   none created by this file
BASE:            6bb013bafb2d1c06fcb295fdbfce0f86198fd685
LOCAL PARENT:    913d1ea6ab6493af29b404a963c399ab580115fc
DATE:            2026-07-16
```

This record audits the owner-supplied transfer archive
`J_LI_CROSS_BRANCH_PACKET_rev1.tar.gz` and states exactly what can and cannot
be consolidated from it. It does not modify the public Canon, registry, or
probe ledger.

## 1. Archive identity and safety

```text
archive sha256   33a55eebb50c43b6c47db5dbe1d7f6df87e707a0e2393b637b9cab97ef7bbcdd
archive bytes    15303
members          16 (2 directories, 14 regular files)
manifest         13/13 payload pins PASS
```

The tar has one top-level directory. It contains no absolute path, `..`
component, duplicate path, symbolic or hard link, device, FIFO, PAX override,
or opaque binary payload. All regular payloads are UTF-8 text. Controlled
extraction is therefore safe.

The bundled reproduction wrapper uses a predictable `/tmp` filename derived
from `$$`. It was safe in the isolated audit runner, but it is not imported as
a public runner because a hostile shared `/tmp` would permit a symlink race.
A future public wrapper must use a securely created temporary file.

## 2. Byte-level crosswalk

| Transfer payload | SHA-256 | Consolidated destination or disposition |
| --- | --- | --- |
| `verify_j_li_schoenberg_2_rev2.py` | `170cb04a33a717e9f637b1948b81f01fba0414b86e0c082a2034bb398061bb8f` | byte-identical to `verify.py` |
| `EXPECTED.stdout` | `1dff821424280361ec15ebbb2e405d7e6b4d452d820aeefcd2e8d966cb8992e3` | byte-identical to `EXPECTED.txt` |
| `C_J_LI_SCHOENBERG_2_RESULT_rev3.md` | `b9e6da5ca28480da7a4ec0467e00e6ada8687d8e02591bf1176b1979bbc13a53` | mathematical content normalized into `README.md` |
| `J_LI_CND_COCYCLE_CANDIDATE.md` | `c6891a35e06f2161dadbb25fd1b6af138e77d63617ebbb82ca0a856f1df9277c` | theorem/open-gate content normalized into `README.md` |

The normalized README retains the corrected two-modulus complex CND identity,
the exact Toeplitz congruence, the unitary cocycle normal form, the finite
Schoenberg gate, the Artin determinant/Fock carrier, and the separation of the
full Artin packet from the Riemann target. It also distinguishes the trivial
Artin character \(\mathbf1_G\), whose Artin L-function is \(\zeta\), from the
principal Dirichlet character \(\chi_0^{(5)}\), whose L-function omits the
Euler factor at 5.

The transfer pinset uses two historical filenames that differ from the archive
member names, and it mentions a superseded result that the archive does not
contain. Those are provenance irregularities, not byte mismatches in the
payloads that are present. Its AArch64 result is an attestation; no native
AArch64 transcript is included in the tar.

## 3. Subsequent format-patch audit

After the original archive audit, the following format patch arrived as a
separate attachment:

```text
file             incubation-c-li-cocycle-1.patch
sha256           4e3f43c67d2cc29c3abfc4e8200bdc009c5e769270b8a6cb887755d4a2fdefa8
bytes            194361
lines            4016
reported commit  aee7a3762d6fffb1936ae54121dd77d74078b25b
stable patch-id  5a7dc9151e1304d3e2566a530d5ce5eed4009e13
```

It adds 22 ordinary text files and 3819 lines under `notes/incubation/`, with
no deletion, binary delta, symbolic link, submodule, path escape, or normative
file change. It applies without whitespace error to the exact public base
`6bb013bafb2d1c06fcb295fdbfce0f86198fd685`. The resulting tree is
`d78156ecba0782d61bdc46771ceb2c96d15fb82d`.

All three embedded `SHA256SUMS` manifests pass. A fresh execution in this
audit environment reproduced the six pinned stdout files byte for byte:

| verifier | reproduced stdout SHA-256 | disposition |
| --- | --- | --- |
| pentagon-Weil | `e0b6f4f86c12ef06c5ff5be05d5904db63f27e61b5b0402840bb971c474e6cef` | match |
| Weil realization | `fcd03da7ff8240aab49281ad3abf823ae641fa3dc8373788491c85a53b1ed812` | match |
| realization amendment 1 | `94237d8051f3aabe2b48b017cc3f728027a1aba8fb9b8237af62638ecd0f40a3` | match |
| realization amendment 2 | `2c5d81710f36c61f37d497932e27b4a609783167812389c64a65a72c7b9de540` | match |
| cocycle main | `eeb424205400af53fe62de5187ca4eebafa56367f23689d2f9cb300295fd5b71` | match; preserved CO6 failure, exit 0 |
| cocycle amendment 1 | `43ab5fbff93786506e87adefd4bacf27440f2b8bb3d59530a353adf605693d9a` | match |

The patch is therefore a verified content carrier. It is not an exact git
history carrier. A standard format patch records the author identity and
author date, but this one contains neither the parent object nor the committer
identity and committer timestamp. A control reconstruction under natural
committer defaults produced commit
`5fe4ce58d70a4a13bef35dca1dc7c3ea2f934a0f`, not the reported commit.

Consequently, the content of `aee7a376...` has been independently audited,
but that commit object still cannot be imported or merged byte-exactly without
the actual bundle. The reported bundle with prefix `373fde1e...9169` was not
present in the attachment surface available to this audit.

## 4. Exact merge gate

When the missing bundle arrives, consolidation must proceed in this order:

1. verify the complete bundle SHA-256 and run `git bundle verify`;
2. import it into a new non-public ref without rewriting any object;
3. require the imported tip to equal the full expected commit SHA and its
   parent to equal `6bb013bafb2d1c06fcb295fdbfce0f86198fd685`;
4. compare both trees and resolve any overlap explicitly;
5. create a no-fast-forward merge whose first parent is the then-current
   cross-branch staging tip (currently
   `a62b04090608049e946daf237281cd251ea26fbf`) and whose second parent is the
   full imported `aee7a376...` commit.

Cherry-pick, rebase, squash, or reconstruction from prose is forbidden for
this merge because each would destroy the requested two-parent provenance.

Until that gate can run, this branch is a staging consolidation of all
verifiable bytes, not the claimed two-parent history.

## 5. Status after content consolidation

```text
J-LI-CND-EQUIVALENCE          mathematical T candidate; public unregistered
J-LI-TOEPLITZ-EQUIVALENCE     mathematical T candidate; public unregistered
J-LI-COCYCLE-NORMAL-FORM      T as an equivalence; public unregistered
J-LI-SCHOENBERG-2             finite certificate candidate-T-ready
J-LI-COCYCLE-REALIZATION      O
RH                            O
exact aee7a376 history merge  BLOCKED: git bundle object still absent
```

No finite gate or transfer record is evidence for the uniform all-\(n\)
cocycle construction.
