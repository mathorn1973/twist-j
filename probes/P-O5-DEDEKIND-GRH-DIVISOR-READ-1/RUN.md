# P-O5-DEDEKIND-GRH-DIVISOR-READ-1 formal run

Status: accepted local formal record. Public two-architecture replay pending.

```text
pin_commit: 6238d100506a5ebc37724faf3ad2bbab54295849
verifier_sha256: 240194b3cf6dc72284734f06ca549fe4236a2a8bf768e2d93ad4b2466f841deb
command: python3 probes/P-O5-DEDEKIND-GRH-DIVISOR-READ-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 1136f7a6abe6688a3ea2b6980a4fc6966cbd4fe5241f2d29cb4c9ca953ebf6c7
stdout_bytes: 451
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin readback

```text
basis main:      bb2172c69c0448ff3eeffc3960db362bf419a75e
pin tree:        625dd463e8e82e1661fefc5cf0025e2181944e18
PREREG SHA256:   90af26b1a2d7d42b20fa7571e93d3d0a073cfa9454e0b02e8dfca544ec52a7b9
PREREG bytes:    10650
PREREG blob:     583740a044fffb2bea45256daf9e72b2c5090628
verify bytes:    10614
verify blob:     d0ef9da19a584d9545a4d56999855a6e1b1af8cf
```

The pin had exactly one parent and exactly two added files under the fresh
successor probe directory. The local execution surface matched the public
pin by SHA-256 and Git blob identity before execution.

## Frozen startup preflight

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

Result: exit 0, stdout exactly `PYTHON_STARTUP_CLEAN` plus LF, stderr empty.

The verifier was then invoked exactly once under the same clean environment.
No threshold or pinned byte changed after the pin.
