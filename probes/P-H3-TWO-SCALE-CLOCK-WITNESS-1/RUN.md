# First public-pin replay of the two-scale clock witness

The preregistration and verifier were committed together. Remote branch readback identified the pin before execution. The working-tree SHA-256 digests of both files and the imported kernel were checked against the fixed values before the local process started.

```text
pin_commit: 8f282098a1aeaa621b953beff0fed13b18f55814
public_base: 93c36089db57032a6cbca482ff62c95884567d0f
prereg_sha256: 11d8b76fdccc28542ee313fb302ee2e036f751acd9a580f54c7c5fc73383f006
verifier_sha256: 7791add970d86c41968ca6f2d6756dc86865b9b5b26e3a09a32a0154b190d8f6
kernel_sha256: 4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd
command: python3 -B probes/P-H3-TWO-SCALE-CLOCK-WITNESS-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 99d815806ca10fb06ac692a55a4b4fcf5d82991e72ffeb4288d7c83b1cb78625
stdout_bytes: 203
stdout_lines: 4
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The process ran from the repository root with LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. EXPECTED.txt contains the original stdout bytes. The finite roster was public at the pin. This run documents an openly repeatable reconstruction.
