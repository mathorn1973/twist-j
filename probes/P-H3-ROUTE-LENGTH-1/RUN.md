# Execution record

The protocol and eight source files were frozen at commit `e2dece04113981691f4fa2d0659b3df364df39f3`. The [public readback](https://github.com/mathorn1973/twist-j/issues/2015#issuecomment-6963725595) records their byte lengths and SHA-256 digests. The Linux runner verified the pinned bytes in a clean checkout before executing the new preparations.

From the pinned probe directory:

```sh
python3 phase.py
python3 verify.py > primary.jsonl
g++ -std=c++20 -O3 audit.cpp -o audit
./audit > launch.tsv
python3 crosscheck.py primary.jsonl launch.tsv
```

## Python primary

```text
pin_commit: e2dece04113981691f4fa2d0659b3df364df39f3
command: python3 probes/P-H3-ROUTE-LENGTH-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 8b8c3553248df5427233a603d820b1109f99c606e241edc8449c0daae24db57c
started_utc: 2026-11-17T23:11:28.695864+00:00
ended_utc: 2026-11-17T23:11:34.658391+00:00
exit_code: 0
stdout_bytes: 1023160
stdout_lines: 428
stdout_sha256: 030be51ef86ab247c4a26aa96ec81f6b7ffe3fc8b95e5cbef38e73ceb32edfc1
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The JSON Lines output comprises the 622-tick bare reference summary, the pooled natural summary and 85 natural rank records, the prepared protocol summary, and 340 prepared rank-distance records. Natural trajectories and their local counterfactuals passed every C/B ledger and inverse check. The prepared audit passed those checks on 52,785 native steps, covering one zero-pulse trajectory and eight sign-distance preparations per rank. The phase module's synthetic tests passed.

## Independent C++ projection

The four-coefficient audit checked the three paired prepared comparisons per rank and distance. Its TSV includes each first arrival, the isolated-hit criteria, next-tick survival and retention, and the first direct conversion in the registered window. [LAUNCH.txt](LAUNCH.txt) contains its output.

| Platform | Compiler | Exit | Stdout bytes | Stdout lines | Stdout SHA-256 | Runtime stderr bytes |
| --- | --- | ---: | ---: | ---: | --- | ---: |
| Ubuntu 22.04.5 LTS x86_64 | GCC 11.4.0 | 0 | 53605 | 1021 | `e50d7457aa5fd1e7c109a314d26df8628649a36b63d322cefd7a7f4cc73f6ef8` | 0 |
| macOS arm64 | Apple Clang 21 | 0 | 53605 | 1021 | `e50d7457aa5fd1e7c109a314d26df8628649a36b63d322cefd7a7f4cc73f6ef8` | 0 |

The Ubuntu C++ run started at 2026-11-17T23:11:30.336335+00:00 and ended at 2026-11-17T23:11:30.637234+00:00. The macOS build with `-Wall -Wextra` emitted four warnings for unused constants inherited from the upstream core.

Python `crosscheck.py` matched all 1,020 keys and all 18,360 metric values. It exited 0 with empty stderr. Its stdout was one line, 42 bytes, SHA-256 `cc6fe1aec42a9f335f9bdfb6b7475a0ee5962d91402ebedd69d7da4cfc5763a9`. The C++ agreement covers the prepared comparison fields. The Python evidence supplies the exact chord phase and the natural-emission counterfactual.
