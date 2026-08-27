# P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1 formal run record

Date: 2026-08-27

Status: local accepted formal record. The public two-architecture gate is
pending the pull-request workflow, which must rerun the unchanged pinned
verifier on x86_64 and aarch64 and compare stdout byte for byte with the one
committed EXPECTED.txt.

The flat fields below are the machine-readable execution record.

```text
pin_commit: 0c216fad6cf1a758153e893799403730c24c0028
verifier_sha256: 70e1d3b4e44657ad218a93bb1b067bfc171b0078bc0ceda75c21c6e8839af5fd
command: python3 probes/P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 222a9bf7e84b819138b164adf7773fb2319dfe127bde1f0413950b68e7249992
stdout_bytes: 496
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin readback before execution

```text
basis_main:       b66ea7eda80e0028c74c7b71b70205db9566c37b
pin_tree:         1b59ae1f62ed01feef6840e3ad86daad66efa813
prereg_blob:      5ce14fde507fa04bc5f65d781831ada48ac40171
prereg_sha256:    538ce295c04b2bc2cf962b04d98d252695fed4712b307c7a685c449644e6f32a
prereg_bytes:     6023
verifier_blob:    ba6587b780b05d68034ae26d789c706444639de3
verifier_bytes:   4821
```

The pin has exactly one parent, the declared basis, and exactly two added
files. Before the pin, both unattached server blobs matched the local
`git hash-object` identities. Public post-pin readback then matched both blob
identities and byte counts again. Neither pinned file changed after the pin.

The accepted runtime surface was reconstructed from those byte-identical
pinned files. The verifier is self-contained and reads only its own source.
Before the pin it was read and AST-parsed only; it was not imported or run.

## Clean startup preflight

```text
preflight_command: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
preflight_exit_code: 0
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0
```

The preflight passed immediately before the single accepted scientific
execution. `EXPECTED.txt` is its complete LF stdout. No threshold, witness,
pinned byte, or mechanism moved after the pin.
