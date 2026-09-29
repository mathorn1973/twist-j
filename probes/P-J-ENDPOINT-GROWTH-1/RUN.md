# Run record: P-J-ENDPOINT-GROWTH-1

First completed formal local execution, after public pin and byte readback.
The finite replay is not a replacement for the all-n written proof.

```text
pin_commit: 645100c1fd6ec2b287e5087582991e7b4d38d84a
verifier_sha256: 3758ca321b5bdadc767bba10b3c35bece5f34e7cc2e5c74a2760954b7801026e
command: python3 probes/P-J-ENDPOINT-GROWTH-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 507d1995a5cba039e91c5054a248a00b3c726cd399d493446e5aecefcf4e953a
stdout_bytes: 459
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

The preregistration, proof and verifier match the immutable pin.
Their public readback receipt precedes execution in issue #1278.
No frozen source or threshold changed. The required pull-request x86_64 and
aarch64 jobs must reproduce EXPECTED.txt byte for byte.
