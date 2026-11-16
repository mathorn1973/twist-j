# Run P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1

The public preregistration and verifier were pushed, freshly fetched and
[read back before execution](https://github.com/mathorn1973/twist-j/issues/1992#issuecomment-6916177153).
Both file digests matched again in the clean Linux checkout at the pin
immediately before the first formal invocation.

```text
pin_commit: c62b9faac89d59513043f8e8e1265becf94fb55c
prereg_sha256: 8cbab7d2977d84ea3999aaf3eaee633b97b9c4b649f633049543c43ca79d4bf8
prereg_bytes: 17869
verifier_sha256: d2e8f78bf9c3ff62e6fd5dfa27cf1990c7d60cab4320721c7037c8bbd918258e
verifier_bytes: 16032
command: python3 probes/P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1/verify.py
platform: Ubuntu 22.04, Linux-compatible WSL2
architecture: x86_64
python: 3.10.12
started_utc: 2026-11-16T12:17:22Z
exit_code: 0
stdout_sha256: a3e00cfd46cdfa8099d3f29cba10bbe4c1da0df202b0d9196620e1cb3c615589
stdout_bytes: 435
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The environment fixed LC_ALL=C, LANG=C, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1 and TZ=UTC. Python optimization was disabled and
the 600-second guard did not fire. The checkout remained clean after
execution. EXPECTED.txt contains the recorded stdout bytes from this run.

This is the local Linux run. The required hosted x86_64 and aarch64
architecture receipts belong to the pull request workflow.
