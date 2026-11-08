<!-- SPDX-License-Identifier: Apache-2.0 -->

# Validation record

NON-CANONICAL / L1. Reservation:
[#1922](https://github.com/mathorn1973/twist-j/issues/1922).

Content commit:
`33c87a7ea54bfac8a651ed9fa3f72cac7b33a88c`.

Base:
`650029c20408f1dd665983d72225d0d195fd030e`.

Everything below was run in a clean Linux clone of the content commit on
x86_64, Ubuntu 24.04. The clone remained clean afterward. This record was
appended after the checks and is not listed in `SHA256SUMS`.

## Replay of the scripts

Each script was run from the repository root as documented in README.md, with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` and
Python 3.13.18. The two contact scripts take the path of `WORD.txt` as their
argument. Every run exited 0 with empty stderr, and every output was
compared with `cmp` against the committed `.stdout` file: identical.

| Script | Script SHA-256 | Stdout bytes | Stdout SHA-256 |
| --- | --- | ---: | --- |
| `recon_native_u_2026-11-06.py` | `394fd7cc527b164316f6ae9ad0dfa77268e86bc1efdeeace6a5ba3d993dc2403` | 1508 | `5ddfeca81ccb863dc7aaf346991e967df285cfd9e80accf36e0e51b8de7aac3b` |
| `recon_contact_phase_2026-11-06.py` | `f506749c30d53420dd548e1d67a3863395a6e63fede26f523edea6d4cc18b0ab` | 3663 | `01fc8307cd3287e4feb77dab34bec1b5e5944122dfa147c170f0e311bcec9d1b` |
| `posthoc_contact_area_2026-11-06.py` | `5dc1fa98c1c2a1293561d2242e2e6990895e761828cf1ae57d35c1a1030ab729` | 1898 | `f70642f37b8160331169c12b6c5a1edfc553763b3aaf0876381b299e58238e83` |
| `check_log_coordinate_2026-11-06.py` | `3bafa1bff38436d43b24619c87f62c356bab4688958897d25875bb4a879fb5a1` | 238 | `9d7d52de14cfe87fa1c477049e3dfe0c9ced71b515002712bd5bcea7690f792b` |
| `explore_shortest_count_loop_2026-11-06.py` | `7384c9b81a2dd978d23d3669c9fa95fed978bd40c63ca130ff1329ef54939fab` | 2968 | `cdde106e8015f6bb2e2fd0ae2cf9199e5bfd216d1ee486e397219a73ea052360` |
| `witness_equal_area_pair_2026-11-06.py` | `c2ccc68c9e0fa3467f5339e14c06fbbf5b0cb4eb4ab0df5466fe7cc2eda10e4a` | 342 | `3b0b8ae395c9ab68dd93faef97ab02ca079826723a9aa63f606935188fb1bbbf` |
| `check_tick_law_2026-11-06.py` | `9fd275dca7d3f1916e983e6135516b67ab1620b9643cc6291e13643b9ed2a1a0` | 420 | `f432c563c749c513fcaaf2940ed2eef6829d1ced8e97b33a75525cca160bd310` |
| `break_recon_parts_u_k_2026-11-06.py` | `e710323a1a6309d86c7ee59197f6013fe4d8d88111405fd24cb41854db63e2d9` | 1220 | `852efd2d4c01533be637d6477ad8c30627392abda2ab4f7cf35ade610fc49434` |

The breaker takes about two minutes on this machine, each of the others at
most about fifteen seconds.

Three further replays of all eight scripts in the same clone gave the same
bytes:

- Python 3.13.18 started as `python3 -I -B`, which ignores `PYTHONHASHSEED`
  and therefore runs with randomized string hashing;
- Python 3.12.3 with the documented environment;
- Python 3.11.18 with the documented environment.

All four replays ran on x86_64. They show that the outputs do not depend on
the hash seed or on these three interpreter versions. They are not a second
architecture.

Relation to the session runs, as recorded in PROVENANCE.md: the six scripts
published unchanged reproduce the bytes of their session outputs. The breaker
extract reproduces the session output without its single B-D line.
`check_tick_law_2026-11-06.py` had its first run while the note was prepared.

`sha256sum -c SHA256SUMS` in this directory reported 23 of 23 files OK.

## Repository checks

The following commands passed in the same clone with Python 3.13.18.

| Command | Result |
| --- | --- |
| `python3 tools/check_policy.py` | POLICY PASS |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 219 tests, OK |
| `python3 tools/check_canon.py` | CANON PASS v109, 609 claims |
| `python3 tools/check_ledger.py` | LEDGER PASS |
| `python3 tools/check_gate_contract.py` | GATE CONTRACT PASS, 26 gates |
| `python3 tools/check_verifier.py --base 650029c20408f1dd665983d72225d0d195fd030e` | VERIFY NOT APPLICABLE |
| `python3 tools/check_reproduce.py --base 650029c20408f1dd665983d72225d0d195fd030e` | REPRODUCE NOT APPLICABLE |

The exact staged paths and the diff were reviewed. The content commit changes
24 files, all inside this notes directory. Normative files and predecessor
probes are untouched. No machine-specific path, credential or confidential
record is part of the committed package.

## Mathematical authoring checks

The proofs of the corollary in NATIVE.md, of Proposition K and of Theorem L
were reread line by line against the registered definitions while the note
was written. The read found no mathematical blocker. Three statements were
sharpened during it: the tick law of (C3) now covers windows of either
parity and no longer depends on #1915; the determinant remark names the
admitted count and the odd rescaling exactly; consequence (K3) is restricted
to banks whose unequal residues differ by one square.

These checks come from the authoring session. They are quality assurance,
not blind or independent mathematical acceptance.

## What the pull-request checks do and do not show

The required x86_64 and aarch64 pull-request checks validate repository
integrity under the existing rules. They do not run the scripts of this
note and do not test its proofs. A two-architecture execution of these
scripts has not taken place. Independent mathematical review and any future
Canon disposition remain separate.
