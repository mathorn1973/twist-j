# Execution record

The [public readback](https://github.com/mathorn1973/twist-j/issues/2025#issuecomment-6973944963) binds all nine frozen files. The original H3 foundations and literal launch match [the predecessor](https://github.com/mathorn1973/twist-j/pull/2024). The native program was compiled with g++ 11.4, C++20 and -O3.

```text
pin_commit: 7d96658c40d7ac7debef67e4c9bd7e56faf3929e
command: python3 probes/P-H3-SECOND-WRITE-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 36aa229d197601ed75fb571fc092de7fee628526068a123f09215e16f8f4fe0c
started_utc: 2026-11-18T09:04:22.169371+00:00
ended_utc: 2026-11-18T09:04:30.029437+00:00
exit_code: 0
stdout_bytes: 77149
stdout_lines: 99
stdout_sha256: a02017a479b6a199a0aa5bbdac43c61f76dffe0c9331427cbf028bfdba72742a
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

[EXPECTED.txt](EXPECTED.txt) includes the protocol, 85 native rank records with terminal digests, ten rank-43 snapshot records and three Python comparisons. The four-coefficient native implementation audits the full windows. The five-coefficient Python implementation independently checks through 8,192 ticks on the three first writers, including their earliest later work and earlier omission histories. Local snapshot replay verifies that the supplied complete pre-C field gives the registered post-C and post-B fields. The source-undo and exchanged-word arms exist only in the measurement.

The follow-up [local_trace.py](local_trace.py) reconstructs the material and CLK half-gap rotations on the shorter interval from the same literal input. It was written after the primary run. From the repository root run:

```sh
python3 probes/P-H3-SECOND-WRITE-1/local_trace.py
```

The nine output lines have SHA-256 `5133b6de3ec67358bb33a8371a68ee772aedf111ee09e09e55951b4128080824`. Its assertions check native C on the two five-contact sequences on each bond and the repeated worker states at 160, 170, 171 and 181.
