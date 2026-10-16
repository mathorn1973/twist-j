# P-PHOTON-AXIS-POS-PRIMAL-1

Status: preregistered finite-size probe of the #1116 axis coefficient,
unexecuted. Ceiling C. `PREREG.md` is the contract; this file only says what
each file does and which commands exist.

## Files

```text
PREREG.md             six fields, seeds, schedule, gates, terminals, disclosures
AXIS_PIN.md           pin declaration; its first commit is the immutable pin
SHA256SUMS            ordered nine-file inventory of the pin
axis_engine.cpp       pilot-2 engine included byte for byte, plus --axis and --axis-fixture
axis_core.py          exact S -> R -> Q reduction, record parsing, #757 gates,
                      block jackknife, M1/M2 fits, terminal precedence
axis_reader.py        independent numpy reader of the saved #748 link states
run_axis.py           one-shot supervisor (formal) and blind plumbing runs (dev)
verify.py             formal verifier, Python standard library only
FIXTURE_EXPECTED.txt  engine --axis-fixture 3, 4 and 6
```

After execution the probe gains `records/` (one thermal and one measurement
record per chain), `CHAINS.tsv`, `READER.txt`, `STATE_MANIFEST.tsv`,
`ANALYSIS.txt`, `EXPECTED.txt`, `RUN.md` and `RESULT.md`. Link states and
full transcripts stay on the formal host under the state root; their SHA-256
values are in `STATE_MANIFEST.tsv` and `CHAINS.tsv`.

## Verify

From the repository root:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 probes/P-PHOTON-AXIS-POS-PRIMAL-1/verify.py
```

Before execution it checks custody, the engine tables, the exact score
identities, the fixtures with the exact Fourier identity in
`Q(phi)[x]/Phi_2L(x)`, the deterministic readout, bitwise identity of the
statistics with pilot-2, the seeds and the terminal grammar. After execution
it also replays the complete analysis from the committed records and requires
byte equality with `ANALYSIS.txt`.

## Development (no formal seed, sizes outside the production set)

```sh
python3 run_axis.py dev --boost-deb <libboost1.83-dev_1.83.0-4.2_amd64.deb> --out <dir outside the repo>
```

Runs `L = 3, 4, 5, 6` with the DEVELOPMENT seed family and prints only the
integrity class.

## Formal (only after the public pin readback)

```sh
cd probes/P-PHOTON-AXIS-POS-PRIMAL-1
LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
    python3 run_axis.py formal --pin <pin commit> --boost-deb <path> \
    --state-root <empty local directory> --attempt 1
```

The supervisor refuses to start unless the probe directory equals the pin,
HEAD is the pin, the public branch head is the pin and no decision artifact
exists. It needs about 60 GiB free under the state root.
