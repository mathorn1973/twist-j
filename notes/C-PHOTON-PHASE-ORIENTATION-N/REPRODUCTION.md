# Reproduction evidence and completion path

Status: NON-CANONICAL, candidate-C engineering record. Issue #1146.
This is a custody and procedure assessment, not a new simulation result or
a formal public pin. The corrected scope is in [README.md](README.md).

## Completion on 23 September 2026

The missing replacement x86_64 drift run has been recovered and checked.
The [dated record](drift/REPRODUCTION-X86_64-20260923.md) records exact source
identity, all 20 raw-log hashes, job parameters, measurement counts, END
states and a fresh unchanged analysis replay. Its disposition is
`REPRODUCTION_BITWISE`, against the published aarch64 records.
The sections below preserve the initial publication assessment and the
completion procedure. Their PENDING and missing-x86 statements describe
that earlier assessment, not the current drift disposition. B3 and earlier
calibration raw-data replays remain separately unperformed.

## Available and missing evidence

| Item | Supplied evidence | Limit |
| --- | --- | --- |
| B3 | `v3/RESULT-B3.md`, analysis, 16-log manifest and cross-check summaries | The result reports two-architecture identity; raw logs are absent here, so that comparison was not replayed by the publication review. |
| Drift aarch64 | `drift/RESULT.md`, analysis, 20-log manifest and 20 END records | One completed leg is recorded; the manifest does not contain the raw data. |
| Drift x86_64 | Historical restart account in `drift/ADDENDUM-2.md` and PENDING in the result | No completed log manifest, END list, analysis or reproduction disposition is supplied. Current remote process state is unknown. |
| Drift source pin | Five complete source hashes in the README and `drift/RESULT.md` | The named `PIN-DRIFT.sha256` file is not supplied. These are non-public incubation hashes, not evidence of a public pin. |
| v2/A3 calibration | Frozen source, preregistrations and result summaries | The custody account states that raw logs were lost; regeneration is required for a new raw-data replay. |

The corrected note can be reviewed with `REPRODUCTION PENDING`; it must not
be presented as a completed drift reproduction. Repository CI checks policy
and the changed registered probes/reproductions. These simulations live in
`notes/`, so a green CI result supplies no missing long-chain replay.

## First recover a completed run if available

Obtain the completed replacement x86_64 record through a reviewed, traceable
handoff. It must identify the source commit and five source hashes, OS,
architecture, compiler/version/flags, Python version, commands, per-chain
completion and stderr checks, raw-log SHA-256 manifest, END list, analysis
bytes and the comparison disposition. Check those records against the
supplied aarch64 manifest and END list. A timestamp or an old statement
that a job was running does not supply completion.

If a raw transcript is to be published, use a policy-compliant custody path
or an approved external manifest. Renaming a `.log` file to another suffix
does not make it admissible. The current note makes no raw-log policy
exception and changes no workflow.

## Fresh x86_64 replay if no completed record is recovered

Freeze the exact published note commit and confirm its five original source
hashes before execution. This is a non-formal replay of known results, not
a blinded new probe. Keep the frozen sources unchanged and use a new empty
run directory outside the repository.

The scripts have an intentional assembly dependency: `drift/jobs_drift.py`
imports `code/jobs_v3.py`, and `drift/analyze_drift.py` imports
`code/analyze_v3.py`. Use `PYTHONPATH` as below or assemble the five unchanged
files in one directory. The runner invokes `./zlgt2`, so the built executable
must be in the working directory.

With `NOTE` set to the absolute published note directory and `WORKERS` set
to a suitable positive CPU worker count, run from that empty directory:

```bash
gcc -O2 -ffp-contract=off -o zlgt2 "$NOTE/code/zlgt2.c" -lm
PYTHONPATH="$NOTE/code" python3 -B "$NOTE/drift/jobs_drift.py" list
PYTHONPATH="$NOTE/code" python3 -B "$NOTE/drift/jobs_drift.py" run logs_DR_x86_64 "$WORKERS" --owner-authorized
PYTHONPATH="$NOTE/code" python3 -B "$NOTE/drift/analyze_drift.py" logs_DR_x86_64 > ANALYSIS_X86_64.txt
```

Capture the runner output, build diagnostics and exit statuses as part of
the local custody record. The worker count can change scheduling, but not
jobs, seeds, sweeps, sampling, classifier or thresholds. These commands have
not been run for publication.

| Size | Cold replicas | Thermalization | Measurement sweeps | Measurements |
| --- | --- | ---: | ---: | ---: |
| L24 | 3 through 14, 12 chains | 18,000 per chain | 8,000 per chain | 4,000 per chain |
| L32 | 1 through 8, 8 chains | 32,000 per chain | 8,000 per chain | 4,000 per chain |

The frozen workload is 1,756,233,728,000 link updates, excluding measurement
work. This count is obtained from `4 L^4` updates per sweep and the table
above. It is not a short verifier. The archived aarch64 record reports about
80 minutes. The replacement x86_64 record anticipated about 3 hours and
12 minutes. Neither is a validated runtime estimate for a new machine.

## Completion checks outside the frozen runner

The frozen runner prints `FAIL` for a child error but does not propagate an
overall failing exit code. Its reuse check accepts a file containing
`END sweeps=` near the end. The analysis requires 4000 measurement rows and
RUN/END presence, but does not independently authenticate every parameter
or seed. Therefore a zero runner exit or an analysis terminal is not enough.

1. Use an empty output directory and require exactly the 20 prescribed
   filenames. Inspect the runner output for child failures and require
   successful child completion with empty stderr.
2. Check each RUN record against the frozen job list, including group,
   size, start, seed, thermalization, sampling count and cadence. Check the
   4000 measurement rows and total sweep count in every log.
3. Compare all 20 END state hashes with `drift/ENDS_AARCH64.txt`. Independently
   compare the complete raw-log hashes with `drift/LOGS_AARCH64.sha256`.
   Whole-log identity is stronger than matching final state hashes.
4. Run the unchanged analysis, require empty stderr and exit zero, and
   compare its exact bytes with `drift/ANALYSIS_AARCH64.txt`. Record any
   Python-version-dependent last-digit differences separately from terminal
   agreement; do not edit expected output to conceal them.
5. Apply the frozen reproduction rule. Equal END state hashes earn its
   `REPRODUCTION_BITWISE` label. Otherwise compare the completed analyses:
   matching terminals give only `REPRODUCTION_STATISTICAL`; differing
   terminals give overriding `STOP_REPRODUCTION`. Record separately whether
   whole logs and analysis bytes also match.
6. Append a new dated reproduction record with exact pins and comparisons.
   Preserve the original PENDING result and preregistrations unchanged;
   update the active README only after the new evidence is checked.

The archived terminal `NO_DRIFT` is known in advance. Even completed
reproduction remains candidate-C engineering orientation. It supplies no
unconditioned P1 coefficient bound, phase theorem, spectral mass bound,
public computation-grade T, or Canon promotion.
