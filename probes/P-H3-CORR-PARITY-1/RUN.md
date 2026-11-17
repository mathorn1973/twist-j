# Run record

The five [published source blobs](https://github.com/mathorn1973/twist-j/issues/2011#issuecomment-6961316433) were compared byte for byte with the preregistration commit before the Linux runs. The primary ran from a clean detached checkout. [EXPECTED.txt](EXPECTED.txt) is its exact stdout.

```text
pin_commit: 7fc0baf3c585bc4016536e1abdb943257a10a811
command: python3 probes/P-H3-CORR-PARITY-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: a8287d25282ca7555c01a31238fb1c46f2c9df7b788fbd9e995ecda1179b8896
started_utc: 2026-11-17T21:20:01.990276+00:00
ended_utc: 2026-11-17T21:20:09.569433+00:00
exit_code: 0
stdout_bytes: 171481
stdout_lines: 1
stdout_sha256: 6783b947fbdef2a6dc36f0dfe82d0535299e4ed06b494b898344905ac8529b54
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The trace digest inside the output is 34b2e01bb622a49d693ee73c500702941ecc6fe7101694802e5d1aa5f61483f0. It covers the bare trajectory, fresh inputs and decorated substeps. The primary covers 622 bare ticks, 1360 fresh ticks and 37320 uninterrupted decorated ticks.

## Separate C++ implementation

Built on Linux x86_64 with GCC 11.4.0. To reproduce the registered supplement, run the following in the probe directory. The sweep covers the 85 predecessors at 3110 ticks and three starting cuts at 1000000 ticks for each preparation. Each invocation terminates early on first complete return. The executable audits local maps and periodically verifies every rail of the whole inverse. Each digest in the sweep binds the underlying per-invocation stdout with LF endings.

```sh
g++ -std=c++20 -O3 period.cpp -o period
python3 sweep.py ./period
```

All 352 invocations succeeded, with 7341600 ticks executed. The sweep stdout is 45665 bytes and 353 lines, SHA-256 c62a15e485fd63e10bc61d4c43937eb05ef3e233da1431b39907375295f8aa77, with no stderr. [SWEEP.txt](SWEEP.txt).

For example, `./period material_support raw4 1000000` returns after 264800 ticks. Its three phase-4 writes complete at ticks 2, 35602 and 153430. For `./period material_support raw44 1000000`, the first unsolicited upper transport is at 12482 C, from (−3,2,−5,1) to (3,4,3,5). Both complete per-run hashes are in the corresponding rows.

## Additional input coverage

After the registered results, the [coverage follow-up](https://github.com/mathorn1973/twist-j/issues/2011#issuecomment-6961374200) fixed the full list of 85 Q725 predecessors and kept the existing 1000000 bound. It used the same pinned executable and the same row encoder. To reproduce the 85 headerless rows from the probe directory with the executable built above:

```sh
python3 - <<'PY'
from pathlib import Path
from sweep import run
for rank in range(85):
    print(*run((str(Path("period").resolve()), "material_support", f"raw{rank}", 1000000)))
PY
```

This run covers 27263392 ticks. All invocations succeeded with empty stderr. Output size is 11920 bytes and SHA-256 is 5934c73efdf8075f389d4fa4842a57270a14926e81fd78c90f65bb1a455bfe3e. The column names are those of the registered sweep. [COVERAGE.txt](COVERAGE.txt).

## Cross-architecture replay

The GitHub Linux x86_64 and aarch64 jobs both executed the pinned primary verifier and reproduced all 171481 bytes of EXPECTED.txt. [Two-architecture check](https://github.com/mathorn1973/twist-j/actions/runs/44181408481).

A separate Darwin 25.4.0 arm64 run used Apple Clang 21.0.0 and Python 3.9.6 for the supplemental driver. It downloaded period.cpp and sweep.py from the public pin and checked their SHA-256 before compiling. The registered 352 invocations and the additional 85 Q725 invocations reproduced SWEEP.txt (45665 bytes) and COVERAGE.txt (11920 bytes) exactly, with the same SHA-256 values given above and no stderr from the executable.
