# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2

Fresh formal `L=6,8` Ward/covariance cross-check for issue #756 and
production-firewall clause #757/F3.

The package runs the publicly qualified exact sector-umbrella wrapper through
an independent fail-closed reader.  Eight full engine streams remain
pipe-only.  The committed record consists of four deterministic primal replay
logs and eight filtered dual JSONL logs.  Each dual log retains all 2,048
sufficient-statistic records and exactly 128 canonical packed-state audit
frames.

The four terminals are

```text
DUAL_CROSSCHECK_PASS
STOP_DUAL_MIXING
STOP_DUAL_INTEGRITY
BREAK_DUAL_DICTIONARY
```

Only the first, after merge and public readback, can satisfy F3.  None is a
phase or physical-photon claim.

Before the public pin, the only executable check is the L3/L4 combined
fixture from repository root:

```sh
python3 probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2/run_crosscheck2.py --fixture
```

No formal seed or L6/L8 state may be opened before the complete source commit,
manifests and exact issue-#756 receipt have been pushed and read back.  After
that readback, the one and only formal command is

```sh
export LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
python3 probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2/run_crosscheck2.py \
  --formal --pin-commit FULL_SHA \
  --pin-receipt https://github.com/mathorn1973/twist-j/issues/756#issuecomment-N
```

The runner claims local and public attempt refs before compiling, validates
the combined fixture, regenerates the four byte-identical primal replays, and
runs exactly eight engine-to-reader pipelines with four workers.  One 48-hour
deadline starts immediately after both attempt refs have been claimed and read
back and covers toolchain checks through formal capture.  It never writes an
unfiltered engine transcript.  On a complete modeled record it exclusively
generates byte-exact `RUN.md` and `RESULT.md` before formal capture; the
verifier recomputes their hashes, terminal and F3 disposition, and only then
does the runner write `EXPECTED.txt`.

The formal command must run from a fresh full clone created by Linux, with a
real nonsymlink `.git` directory.  A Windows linked worktree whose `.git` file
names a host path is not admissible; a WSL-created full clone under
`/mnt/<drive>` is admissible.  The literal origin must remain
`https://github.com/mathorn1973/twist-j.git`.
The formal host is exactly Ubuntu 22.04.5 LTS x86_64 with CPython 3.10.12,
`g++` 11.4.0, Boost 1.74 (`BOOST_VERSION=107400`), Git 2.34.1 and GitHub CLI
2.4.0+dfsg1 authenticated as `mathorn1973`.

CI and later public replay use only

```sh
python3 probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2/verify.py
```

The verifier reads committed raw transcripts, redecodes retained states and
reruns the frozen analysis.  It never invokes or resamples a Monte Carlo
engine.  Production issue #742 remains forbidden until a merged public PASS.
