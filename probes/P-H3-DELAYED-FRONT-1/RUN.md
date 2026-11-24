# Execution record

Public [readback of all seven frozen inputs](https://github.com/mathorn1973/twist-j/issues/2017#issuecomment-6963885719) preceded the run. The Linux runner rechecked their SHA-256 immediately before execution. From the probe directory:

```sh
python3 verify.py > observed.jsonl
g++ -std=c++20 -O3 audit.cpp -o audit
./audit > observed.tsv
python3 crosscheck.py observed.jsonl observed.tsv
```

```text
pin_commit: 5f332b3627b6d5c078b7266af777c0604956b56e
command: python3 probes/P-H3-DELAYED-FRONT-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 819205fbfcfaea20465f11e93498717e05a26beb96a6838fde9020b8e0e674a2
started_utc: 2026-11-17T23:19:20.782462+00:00
ended_utc: 2026-11-17T23:19:25.052489+00:00
exit_code: 0
stdout_bytes: 157607
stdout_lines: 766
stdout_sha256: 56e9d9574e0914d0cc4eab82d05094c7b05118aded774eba6d7573b482b0c982
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

[EXPECTED.txt](EXPECTED.txt) gives one summary, all 85 rank records and 680 event-distance records. The emission cohort and the earliest front counts matched the preceding run. In addition to the 622 bare steps, the Python verifier audited 85×193 live ticks and 170×65 comparison ticks, totaling 27,455 native ticks. The full ring-valued ledgers, scalar Q and local inverses passed at all recorded stages.

[ARRIVALS.txt](ARRIVALS.txt) is the separate four-coefficient C++ projection. The Ubuntu GCC 11.4 and macOS arm64 Apple Clang 21 runs produced the same 61,310 bytes on 681 lines, SHA-256 064c75f7dbc1b90ad774de047fffc44d9449e31ee5edce861ce477cd9c219f52. Both executables exited 0 with empty stderr. Compiling on macOS with -Wall -Wextra produced two warnings for unused constants inherited from the upstream core.

crosscheck.py matched the complete emission/length key domain and all 43 columns of every row, including nulls. It exited 0 with empty stderr and emitted one line of 49 bytes, SHA-256 62b021d2e5718bf5e55e092422aa0f42c947b7abf1666c074ee886a71a9291b5. This covers 29,240 table entries.
