# Execution record

The [public input readback](https://github.com/mathorn1973/twist-j/issues/2023#issuecomment-6973454043) records all six input lengths and SHA-256 digests before the formal launch. The native verifier was compiled with g++ 11.4 using C++20 and -O3.

```text
pin_commit: fa63dd83a8bf5993cc0511a2b942435eb178be03
command: python3 probes/P-H3-WIRED-WORD-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: c66b2a1f4beea1c7b556c97c110a4836a99301f244b7d16583b3fc85af2f1cd1
started_utc: 2026-11-18T08:40:55.491498+00:00
ended_utc: 2026-11-18T08:41:01.138087+00:00
exit_code: 0
stdout_bytes: 11653
stdout_lines: 5
stdout_sha256: 50439131187f5c0ae4c5ab75657b6fc65d56ae2fdcab0a2a93809e25cac81dd9
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

[EXPECTED.txt](EXPECTED.txt) contains the clock/ledger record, two detailed witnesses and two tables of 85 rows. The independent four- and five-coefficient kernels share their launch fields. All 16 integer entries of every row match. Each plain forward loop takes the field and native bit for 164 steps. Its inverse recovers the full start. On rank 43 the three worker cuts obtained from that loop agree with the scored worker. The second wiring was first run after the public pin. Both preparations were designed using the known anchor.
