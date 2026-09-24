# Recovered x86_64 drift reproduction, 23 September 2026

PUBLIC; NON-CANONICAL; candidate-C engineering orientation. Issue #1146.
Continuation owner: A. M. Thorn / Codex-drift-custody-20260923.

```text
TERMINAL       NO_DRIFT
REPRODUCTION   REPRODUCTION_BITWISE
raw-log hashes 20 / 20 match the published aarch64 manifest
END states     20 / 20 match the published aarch64 list
analysis       1056 bytes, byte-identical to the published aarch64 output
```

## Provenance and authority

The completed replacement x86_64 run described in ADDENDUM-2 was recovered
from persistent storage. This review did not launch another simulation.
The recovered sources were compared byte for byte with the five files in
public note commit `94b27e84e06e9e5f7ab6c07242857f109a5fe0cc`.
This is a retrospective source-identity check, not a claim that the
incubation run was started from that later public commit or public pin.

Public basis checked for this continuation: main
`a00d3635979e4618fb8175f91c37dbbd41ddc914`; Public Canon v91, tag
`11b66d4755a697031157f0e10dc1898a7d5b6379`, and content commit
`b89b0c80bb5cebddade567f31a979aaf42f1d9dd` are ancestors.
The five normative hashes match and required main architecture checks pass.
No Canon, registry, workflow, formal probe or scientific threshold changes.

## Recovered evidence and checks

The raw directory contains exactly the prescribed 20 filenames: L24 cold
replicas 3 through 14 and L32 cold replicas 1 through 8. For every file,
the RUN header was checked against the unchanged `jobs_drift.jobs()` list:
engine, N, L, seed, cold start, thermalization, measurement count, cadence
and disabled correlator cadence. Each file has exactly one RUN line, 4000
measurement lines and one END line. Every measurement sweep number was
checked, not just the final row. Final sweep counts are 26000 and 40000.

All complete raw files were rehashed on the host. The sorted manifest
matches `LOGS_AARCH64.sha256` byte for byte. The freshly extracted sorted
END list matches `ENDS_AARCH64.txt` byte for byte. These comparisons use
the reference bytes at the public note commit above, not an attachment.

The recovered runner transcript has exactly one `done` line per prescribed
job in the frozen job order, with no `FAIL` or `skip`. In the unchanged
runner, `done` is emitted only for child exit 0 and empty captured stderr.
Individual historical stderr files and numeric exit records were not
separately retained; completion is supported by that runner transcript and
the complete raw-log checks, not by a new observation of those old exits.

## Analysis replay and environment

- OS: Debian GNU/Linux 13 (trixie).
- Architecture: x86_64.
- Python used for this analysis replay: 3.13.5.
- Installed GCC and recovered executable `.comment`: GCC 14.2.0-19.
- Historical build flags reported by the run account: `-O2 -ffp-contract=off`.
  No original build transcript was recovered to independently establish flags.
- Command, from the assembled unchanged five-source directory:
  `python3 -B analyze_drift.py runs_DR`.
- Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
- Replay exit: 0; stderr: 0 bytes; stdout: 1056 bytes.

The newly executed analysis matches both the recovered historical x86_64
analysis and the published `ANALYSIS_AARCH64.txt` byte for byte.

| Checked object | SHA-256 |
| --- | --- |
| Source zlgt2.c | `62be81dc972596f10ff29636888b8b923c56c1c5c393627a24fba8cc1ab6d27c` |
| Source jobs_v3.py | `3a9b280b3b1f0fb4e46a0baeaac7d5b096645791a0ff328b88b94c8b6f485f04` |
| Source analyze_v3.py | `8460818640313e30e3b3fde985222dc7f6ecc9f1abe0a870df39fc35e9dae377` |
| Source jobs_drift.py | `7708c43e36d00e4daad2171b192d34adb5a8782c33fd27cb10495535f5e144b4` |
| Source analyze_drift.py | `e5a022a5bef7624936216d86a9460471df70dd23d7eb2a84bd84ff7a321acfae` |
| Sorted 20-log manifest | `8fd4807378a65043266459fc56af8a6f4faba5f9ef52602a84ceeed71721bb96` |
| Sorted 20-END list | `780bb01732e670a21b452f3e69dfc6d71be7c869636221a41a8fcf68abb87e62` |
| Analysis stdout | `0ede6cdce7a37703ac0952759e9055376de4fe633d2cb6b05bfaae984f69e936` |
| Historical runner completion transcript | `f95565986344e71d362951a831c2d3f4e7fda05df75c3214adaa655ad9bef785` |

## Disposition and limits

Equal END states satisfy the frozen `REPRODUCTION_BITWISE` rule. The
matching whole-log SHA-256 values and byte-identical analysis supply
additional agreement with the archived aarch64 record. The aarch64 raw
files were not newly inspected and no fresh aarch64 simulation was run.
This is checked recovery and reanalysis of a known-result reproduction,
not blind confirmation or a formal two-architecture computation-grade T.

The earlier execution-environment failures reported in PR #1150 remain
failed separate replay attempts. Recovery of this completed run resolves
the publication evidence gap; it does not relabel those failed attempts.
The historical `drift/RESULT.md` with PENDING and all 35 archived source
and transcript files remain unchanged. This dated record supplies the
current reproduction disposition.

B3's full 16-chain raw-data comparison and earlier calibration comparisons
were not replayed in this continuation. Their status remains attributed
to the archived reports. The use of B3 constants in `analyze_drift.py`
does not newly validate their provenance.

`NO_DRIFT` means failure to detect the specified drift at the frozen
resolution. It is not zero drift, a full-measure P1 bound, a massless-phase
theorem or a spectral mass bound. The same sector-conditioned finite-volume
scope and known-result disclosure for any prospective #1116 pin remain.
Raw logs remain outside the public repository under the existing policy.

