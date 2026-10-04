# Independent historical replay-context review

NON-CANONICAL. Administrative and static review, 2026-10-05.
Disposition: **PASS for the reviewed helper, registration and test sources.**
This is not a scientific run receipt or a claim that the release gate passed.

The independent reviewer read the post-v97 probe inventory, runtime source
reads, frozen manifests, preregistrations, policy and replay implementation.
Only source reads, Git metadata reads, hashing and byte comparisons were
executed. No scientific program was run or imported. The reviewer did not
author the replay helper or its tests and changed only this review note.

## Complete post-v97 inventory

The paths changed under `probes/` between `canon-v97` and the reviewed release
history identify exactly these four directories. Their original pins are
ancestors of the release base `1bf5b154a049f5b70ac199c3997aee8f0026ce52`.

| Probe | Original pin | Replay-context finding |
| --- | --- | --- |
| P-J-LAMBDA6-DECODER-INTERFACE-1 | `561679f65aa4b0a534cd94129fe243ac8fc9936b` | ABANDONED before scientific execution, with no RUN.md or EXPECTED.txt; no historical replay registration. |
| P-J-LAMBDA6-DECODER-INTERFACE-2 | `79c8cd3cdb7df40eedd59e12bf70832c8cbc4b2d` | Runtime hashes its 16 local INPUTS entries and imports its local decoder. SOURCE.json is provenance; external source files are not read at runtime. No context registration needed. |
| P-U-EARLY-SOURCE-FIBRE-CONTACT-1 | `9754d85622844d40212288d2204fc240e6cd8e31` | Runtime checks every local INPUTS entry and all 11 external SOURCE.json files. This is the sole eligible missing context. |
| P-U-TWO-TRACE-PORT-CONTACTS-1 | `5d122f0cab1fb20b368302cee4b4989d13ff16d2` | Runtime hashes its 20 local INPUTS entries. Standalone programs retype the native formulas; SOURCES.json is provenance. Its preregistration explicitly excludes a future whole-Canon runtime dependency. No context registration needed. |

All local INPUTS entries of the three completed probes, and their manifest
files themselves, were compared with their respective original Git pins.
Every byte matched. The later-alphabet two-contact probe was inspected
explicitly, so the conclusion does not rely on a gate that stops at its first
failure.

## Admissibility and complete custody

POLICY.md permits historical replay only for a sealed probe that explicitly
froze its complete runtime authority context. EARLY-SOURCE's PREREG.md,
section "Frozen programs, serialization and execution", binds its full local
dependency manifest and SOURCE.json. Its INTEGRATION.md expressly requires
an explicit replay-context decision when future Canon changes those source
bytes. This is a declared historical-input boundary, not a new exemption
inferred from a failed test.

The registration uses the original run pin
`9754d85622844d40212288d2204fc240e6cd8e31`, rather than the earlier scientific
source baseline `5e872c22a18043c8126945a982efad55472cea82`. Independent byte
comparison confirmed that all 11 external files have exactly the same bytes
at both commits, and match every SOURCE.json SHA-256 and byte count:

- STATUS.md, POLICY.md and AGENTS.md;
- canon/CORE.md, canon/FRONTIER.md, canon/REGISTRY.tsv and canon/CANON.md;
- reproduce/census/verify.py;
- probes/P-U-PREPARATION-EVENT-RECORD-1/RESULT.md;
- probes/P-KERNEL-Z6-SYNCHRONIZATION-1/RESULT.md;
- notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/PREREG.md.

All 25 registration specifications were independently reconstructed from
Git bytes and matched their declared Git blob, SHA-256 and byte count. The
complete isolated tree consists of these 11 external files and 14 local
files: the 13 INPUTS.sha256 entries plus INPUTS.sha256 itself. The helper
checks verifier and preregistration separately, and checks the remaining
12 `bundle_files` against both the immutable pin and their current bytes.
The 12 entries include both implementation companions, SOURCE.json,
INPUTS.sha256, .gitattributes and every declared local document. Nothing
consumed by the default wrapper is omitted. The external census script is
read for its hash; it is not imported or executed by this probe.

## Runtime and scientific boundary

The helper admits exact, code-reviewed path sets for each named probe.
Unknown names, additional fields or paths, omitted files, duplicate JSON
keys, invalid hash/size metadata and non-regular pinned Git entries fail
closed. The original pin must be a commit and ancestor of HEAD and must
equal RUN.md's pin. All current executable and local bundle bytes must
still match that pin. Only the admitted files are materialized in the
temporary tree, which is removed afterward; no current Canon file is
overwritten and no ambient directory is copied.

The current RUN.md and EXPECTED.txt are checked by check_verifier.py before
historical execution. The subprocess still runs the original wrapper and
both frozen scientific implementations under the existing timeout and
deterministic environment. Nonzero exit, stderr or any stdout difference
still fails. The original expected result remains 2377 bytes, SHA-256
`613ac47b49187ee1e7b89f7587ca393d8b82c71815d7d55a20605fbf7756925e`.
No predicate, threshold, scientific source, program, run record or expected
stdout changes. Current Canon, ledger and activation checks remain current.
The existing FRW replay registration is unchanged.

## Reviewed tests and remaining execution evidence

Static inspection confirms synthetic coverage for a nested wrapper and
companion with source hashes, exact temporary-tree contents, preservation
of current authority files, every changed or missing current bundle file,
missing or additional registered paths, altered Git/SHA/size metadata,
duplicate keys and unreviewed probe names. The retained tests cover old
context replay, verifier/preregistration tampering, ancestry, run-pin
agreement, current expected-output validation, forbidden Git modes,
temporary-tree cleanup and changed-path gate selection. These tests use
synthetic fixtures, not scientific probes.

Execution receipts remain the responsibility of the integration checks:
the synthetic test suite; historical replay of the registered EARLY-SOURCE
probe against its unchanged expected bytes; preservation of the existing
FRW replay; the complete final-tree probe and reproduction gates; and both
required public architectures on the final frozen release pair. This note
does not substitute static review for those receipts.

The actual reviewed SHA-256 values are:

| File | SHA-256 |
| --- | --- |
| tools/probe_replay_context.py | `0be8dc7f8a1edee8f028ef117bfd82e01e577ea93ab85ac123737c9eea505104` |
| tools/probe_replay_contexts.json | `81e27ad1c98dd359998b50832bcc94bf85b435b52296681073458bffa92ec7af` |
| tools/test_probe_replay_context.py | `32853a4042748f8d7353ac01eea08cd31ebced224c2730004201dafb59c51555` |
