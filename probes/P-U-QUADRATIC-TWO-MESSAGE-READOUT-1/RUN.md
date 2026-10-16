# First run

PUBLIC / NON-CANONICAL / L1.

```text
pin_commit: ea25c5b7819b10b7a615d19150ee2c503a277293
verifier_sha256: 61b5c8b43076e86adb4a50a0cfcd1ced01c0e62085f0bf7507d87ee10ad8098b
command: python3 probes/P-U-QUADRATIC-TWO-MESSAGE-READOUT-1/verify.py
exit_code: 0
platform: Linux-6.18.44-x86_64-with-glibc2.39
architecture: x86_64
python: 3.12.14
stdout_sha256: d272c3a229f4dccce71d08bcfd85a4e173baeb072c0ae1cde70f45d83831da0c
stdout_bytes: 421
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All eight initial files were fetched and compared byte for byte before this
first execution; INPUTS.sha256 was independently read back through GitHub.
The two newly authored implementations passed in one recorded default run.
The closed native-U audits were not run. No frozen input changed.

Required public x86_64/aarch64 replay is pending at this first-run record.
