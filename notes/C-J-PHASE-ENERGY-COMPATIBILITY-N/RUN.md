# First exact finite audit run

PUBLIC / NON-CANONICAL / L1. Finite audit ceiling: candidate-C.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

Source pin: 5389b000a6e5178ba99f45a611ebeb07e31051f8
The complete public source was fetched and read back before execution.
The checkout was clean. No earlier scientific run or dry run occurred.

## Execution record

| Field | Recorded value |
|---|---|
| execution_count | 1 |
| start_utc | 2026-10-17T22:07:17.499969+00:00 |
| end_utc | 2026-10-17T22:07:17.610961+00:00 |
| duration_seconds | 0.11099303499941016 |
| os | Ubuntu 24.04.3 LTS |
| architecture | x86_64 |
| python | 3.12.14 |
| timeout_seconds | 60 |
| exit_code | 0 |
| timed_out | False |
| stdout_bytes | 474 |
| stdout_sha256 | b1b28d1517a84019626cbaf48c13cbbd42fdcdd23a1aa98e17166e4b4b162f15 |
| stderr_bytes | 0 |
| stderr_sha256 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

Command from the repository root:

```text
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/audit.py
```

The process was captured with Python subprocess.run and timeout=60; stdout
and stderr were kept separately outside the repository. The elapsed duration
is a monotonic-clock measurement. No raw transcript file is tracked.

## Frozen source custody

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 7229 | 4a053c54ac58f822c38556248a5f051247211819ca532a04226206a3f38c86a7 |
| PROOF.md | 8716 | 2c2c0c8b8232e48ee366b3183609cc12eda36458cea907519c45897930b7813c |
| audit.py | 3807 | 5964f71f6a5d835cfe8093e545893bc66fc96afb82b82199d3a1337169b66df6 |

The audit source hash was identical before and after the run. No source,
scope or threshold changed. PREREG.md and PROOF.md also match the public pin.

## Exact stdout

The following block contains all 474 stdout bytes, including the final
newline. Its hash is recorded above. Stderr is the empty byte string.

```text
NON-CANONICAL L1 exact finite audit; E<=6
states 9072 cycles 252
whole_inventory_allowed [(0, 0)]
zero period_energy_area (4, 0, 0)
one period_energy_area (4, 1, 0)
cold_B0 period_energy_area (4, 2, 0)
cold_B4 period_energy_area (124, 6, 0)
cold_orbits_allowed [(0, 0)]
energy PASS
inverse PASS
coboundary PASS
cycles PASS
zero_cycle_sum PASS
whole_inventory_pairs PASS
witness_zero PASS
witness_one PASS
witness_cold_B0 PASS
witness_cold_B4 PASS
cold_pairs PASS
AUDIT PASS
```

## Scope of the result

Every preregistered finite check passed. The 9072-state inventory exhausts
the complete E<=6 carrier; its 252 cycles have zero integer area sum and
admit only (kappa,beta)=(0,0). The separately checked cold orbits have periods
4 and 124, agreeing with the independent earlier handwritten derivation.
The universal statements rely on PROOF.md, not extrapolation from this
inventory. The normalized Dirac comparison remains an analytical result
and was not numerically tested by this program.

This is one local x86_64 execution of the author's frozen code. It is not
an independent implementation or a two-architecture scientific reproduction.
Notes CI does not execute this audit. No Canon or physical admission follows.
