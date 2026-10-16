# First run

PUBLIC / NON-CANONICAL / L1.

```text
pin_commit: 20c19576bba5382a45cb7acdfa9a76d3bf41ca67
verifier_sha256: afc7cc7f25dfd477f81b31e5edabd6404e5e420f844089f4d2f82a69a21f9a90
command: python3 probes/P-U-AFFINE-SEMANTIC-TWO-MESSAGE-1/verify.py
platform: Linux-6.18.44-x86_64-with-glibc2.39
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: a0e8da00a6294f82d227de144c92b429e7f237519337c0c5e6c093ae13b10b70
stdout_bytes: 578
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All eight initial files were publicly fetched and compared byte for byte
before this first scientific execution. INPUTS.sha256 was also read back
through the GitHub connector. The worktree was clean at the pin.
Both newly authored implementations passed in one recorded default run.
No frozen input changed and no old audit was run.

Required public x86_64/aarch64 replay is pending at this first-run record.
