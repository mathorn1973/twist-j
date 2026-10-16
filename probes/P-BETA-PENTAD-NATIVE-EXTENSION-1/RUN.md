# First formal revalidation run

PUBLIC NON-CANONICAL. Exact L1 supporting evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-13.

```text
pin_commit: 69b6c211dcf5414dc555cab3409baffcb802a00b
base_commit: 5f54015ed8361e3a64cb10894397020ddfadd104
command: python3 probes/P-BETA-PENTAD-NATIVE-EXTENSION-1/verify.py
working_directory: clean repository root at pin_commit
platform: Linux / WSL2
architecture: x86_64
python: 3.10.12
prereg_sha256: a6c22a1201d1a3b145ac886155e5ed1aac5e7e8e157da9945df4571b15eacc1d
verifier_sha256: a454e4ae06a03f6c90961efbfea28272eaa0e4de95fd0270183e7a2011a3badf
public_source_readback_utc: 2026-10-12T23:47:35+00:00
started_utc: 2026-10-12T23:48:22.248462+00:00
ended_utc: 2026-10-12T23:48:23.254137+00:00
wall_seconds: 1.005666815006407
deterministic_executions: 1
exit_code: 0
stdout_bytes: 6431
stdout_lines: 1
stdout_sha256: d2dab98c8441c196525dc73a3d687923501a20b68931453a6097a1599fec8320
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The complete thirteen-file source package was committed and pushed before
this first formal execution. Public immutable-ref readback matched the full
text of all four executable sources and PREREG.md byte for byte; all thirteen
public Git blob IDs and sizes matched the committed tree. The four source
hashes and preregistration hash were checked again immediately before running.

The three unchanged helper hashes are recorded in SOURCE_MANIFEST and in
the accepted stdout. Environment overrides were LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. The neutral kernel
descriptor was 6.6.87.2-microsoft-standard-WSL2, CPython, little endian.
The UTC date above precedes the Czech local date of this record.

The first stdout and empty stderr were preserved outside the repository
before exact transcription to EXPECTED.txt. There was no failed invocation,
replacement or retry. No source or target changed after the source pin.
Supplied output JSONs, live numerical data and predecessor verifiers were
not read or executed. The accepted program executes only its three reviewed,
hash-bound helpers in process; it runs no numerical solver.

This is the first local x86_64 leg. The required public CI is responsible
for replaying this same verifier and helper bytes on x86_64 and aarch64,
comparing stdout to this exact EXPECTED.txt. Its result is recorded by the
public workflow and the PR/issue; this initial local record does not predict
those outcomes. The proof candidates and their explicit scopes are unchanged.
