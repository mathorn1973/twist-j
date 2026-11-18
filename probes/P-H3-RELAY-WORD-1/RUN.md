# Execution record

The [public readback](https://github.com/mathorn1973/twist-j/issues/2021#issuecomment-6972967700) binds all nine frozen input files to the public pin. The Linux runner used the committed inputs and compiled audit.cpp with g++ 11.4, C++20 and -O3.

```text
pin_commit: 617f0ea8ecc108e8e00c31f8b53de8c6a882cc4a
command: python3 probes/P-H3-RELAY-WORD-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 681abafeeadf3d0b72e32535455f1f691b957bf7317ce16b8ead737b08f0ecdc
started_utc: 2026-11-18T08:15:56.953924+00:00
ended_utc: 2026-11-18T08:16:36.645092+00:00
exit_code: 0
stdout_bytes: 329844
stdout_lines: 9
stdout_sha256: a4c7ccb1a929ba19c9bba789be3e5059235f7d4ec98e7ffa02a483e2147b7d7e
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

[EXPECTED.txt](EXPECTED.txt) is the exact stdout. The native C++ census and five-coefficient Python verifier share preparations. The latter separately evolves 343 eligible starts across five representative modes and checks all 16 native output fields, both cuts and inverse motion. A second in-session build of the pinned native program also matched all 5,257 rank-43 direct and auxiliary screening rows. Rebuilding the same program tests reproducibility. The distinct Python evolution tests the implementation of the dynamics and scoring.

The output has one protocol record, the full rank-43 auxiliary screen, a census with per-mode hashes over ordered input rows, five representative Python replays with local witnesses, and a separate intermediate-cut calibration. Missing eligible starts in the auxiliary census can be distinguished from scored zeroes by the per-mode denominators and replay rank lists.
