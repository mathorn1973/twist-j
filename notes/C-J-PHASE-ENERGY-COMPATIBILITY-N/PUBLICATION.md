# Public transport and source custody

PUBLIC / NON-CANONICAL / L1. Author: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

The owner explicitly approved use of the connector account's GitHub noreply
address in the current conversation on 2026-10-18 Europe/Prague
(2026-10-17 UTC). This resolves the email-only publication blocker recorded
in CHECKS.md. No repository policy file is changed.

The connector creates new commit metadata; it cannot upload the original
locally authored commit object verbatim. The following transport preserves
each COMPLETE file tree and the complete parent topology, including the
independent-review branch and its merge. Every tree SHA was compared exactly
before creating its public commit. Local commits and the local Git bundle
remain unchanged. This is an explicitly mapped transport before the first
public execution pin, not an assertion that local SHAs are publicly fetchable
or that current upload dates establish earlier independent-review timing.

| Original local commit | Public transport commit | Identical tree |
|---|---|---|
| 81b10ebb36a7b80482d500ce96e9e51c92a1ec55 | b3563f556a05aa06da2475fbdc9bc13ef00c1f24 | 961988d9c3395bb75df96dd2101e6c32b8f9cc77 |
| e690cda29eda557ddde8b3f7f486a42cd15858e4 | f2956bc3127c06a128785c8412b38b5d695ea1c5 | e13a45289dd3c7ac712d31a60e29875f1f9464ac |
| 8787b25550631a26954055b15c1ca7da5d7ba29a | f01f223edfe0008ede529d3119a394966b558256 | 7f8cd91ce52897b400702103e31b01e1febc87c9 |
| e2135244e0995135ad399567120f9e279beec24b | e76220fa04cad3eb36031efb62179b0b159f7950 | 1bae504162fb224d315ed5af2b736fb6582db411 |
| f398cbe9e72b9dae2744feaeff0832100a30bd00 | 8e3cd9b6f319ab0704a6d4edc16c71aa25d3ca1f | e3ffbbedad92313cb922e2d73d6f7e0cc586128b |
| e3e7a58c8b98ce3982886aec93b2bd0348302923 | 2adeed4ad79aeb6c4dcdd13e197038a93827ae6e | e85b27ceabbc17203ccdaaf81a4e3648bb202b42 |
| 63aa60edb78aaf1e557de94777ede273b05566d1 | 1dfa62f69895c188bf0efce6b0ab22a6c14e129f | 93d35ab8c811b090d7a99ffccb2f97dc0cc1eed6 |
| c196a88ba093b89d4fc052a02c6e3dc3a7366a42 | ba9c3d4569e22afacee36f63f4d7fb495e07a5d3 | 58794e6e7deb5a4f84a0ec7d740edc19f597dc1e |
| bf9ff6eacfd52a4b771dad2fdfd96e7982f19092 | 56f5bc2fcef34ba83fc961ed2eabb437d859ca4c | d9ff14a2a4fe5947b8e6f38d96ab45e1cd59129e |
| 81d0cbe160a3e39357285e958807b34f4cb5c897 | 4547db9660e70e91db02da7e034f12aae36f9403 | 821d20c9a2f2a1522d7d9a89571cef44f4604715 |

The preregistration-only preview b3563f556a05aa06da2475fbdc9bc13ef00c1f24
is now adopted for transport under the explicit email approval. The complete
transported dossier head is 4547db9660e70e91db02da7e034f12aae36f9403.
Its whole repository tree equals local head
81d0cbe160a3e39357285e958807b34f4cb5c897 exactly.

ATTACK.md, DERIVATION.md and REVIEW.md retain their original text and local
pins. Use the mapping above to read the identical public file trees. They
describe the earlier local analytical review; statements that no audit had
run are true of that review stage. They are not claims that the analytical
work was publicly committed before exposure. The source pin for the FIRST
scientific execution is the new public commit containing this custody note,
recorded separately in RUN.md after execution.

## Frozen scientific files

These bytes are unchanged by transport and must remain unchanged after
the complete public pin:

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 7229 | 4a053c54ac58f822c38556248a5f051247211819ca532a04226206a3f38c86a7 |
| PROOF.md | 8716 | 2c2c0c8b8232e48ee366b3183609cc12eda36458cea907519c45897930b7813c |
| audit.py | 3807 | 5964f71f6a5d835cfe8093e545893bc66fc96afb82b82199d3a1337169b66df6 |

No scientific code has run as of this transport record. The complete
public pin must be read back and checked before executing the one
preregistered integer audit. Later RUN.md, updated RESULT.md and CHECKS.md
will distinguish the actual execution result from this pre-run state.
Neither notes CI nor this transport creates scientific acceptance,
a two-architecture reproduction, physical admission or Canon promotion.
