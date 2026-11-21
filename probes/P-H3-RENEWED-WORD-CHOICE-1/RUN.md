# Execution record

The five preregistered files were pushed to the [frozen commit](https://github.com/mathorn1973/twist-j/commit/b888eb0644e3f2133d29363c16da8c40343b63ce) before execution. The public Git blob of each file was read back and compared with the local file. The [claim](https://github.com/mathorn1973/twist-j/issues/2046) identifies the scientific lane. The live checkout contained the frozen files and no local changes.

```text
pin_commit: b888eb0644e3f2133d29363c16da8c40343b63ce
command: python3 probes/P-H3-RENEWED-WORD-CHOICE-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: a8b7acd92be8b3f168882f5188b515b3020b6ea6ebeae2a640daefcb44471ca3
started_utc: 2026-11-21T10:52:34Z
ended_utc: 2026-11-21T10:52:41Z
exit_code: 0
stdout_sha256: cd60930de63cc0f00a8af80e5f0c107f653f6429c48c1f571bd65ea996e3f8fe
stdout_bytes: 15102
stdout_lines: 94
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

| Frozen file | SHA-256 |
| --- | --- |
| PREREG.md | `b7ab6893ac851150fb146b504045c0955b3a7cffe7676e90ed0fc8cd62fee0c8` |
| verify.py | `a8b7acd92be8b3f168882f5188b515b3020b6ea6ebeae2a640daefcb44471ca3` |
| scan.cpp | `1b7f50a32d3e8d8aec55dae63e332e99628bdc81ce55b870efadadf575defafe` |
| matches.hpp | `2c146cffe7d7c1479f864ebb2ff0c2f82f199cdecf8eed62eb0e6b748472c827` |
| witness.py | `2c0542ce8c983e2cda452e5d7d243fd3dec4a89af5f4b7660fc55fa60cee5d9d` |

The driver ran the verifier with Python bytecode caching disabled and preserved its stdout byte for byte as EXPECTED.txt. The native scan checked every C and B account and inverse at each step and rewound each of the 85 histories. The four distinct certificate encounters all fall past the preregistered 4,096-tick Python replay ceiling. Inside the frozen run the Python implementation verified their local projections and receiver operations.

## Supplementary replay of the four reported encounters

After the frozen census, the complete rank-43 trajectory was replayed from launch through tick 735779 using the inherited five-coordinate Python arithmetic. The script selects exactly the four distinct certificate events already identified in EXPECTED.txt, checks that file's digest, and runs the frozen witness checks along their complete histories. Memoization is bounded during this longer run. All four events passed, including every earlier recurring-source tick specified by the certificates and the uninterrupted holds to the reads.

From the probe directory the command was `LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC python3 -B -u replay_witnesses.py`. On Linux x86_64 it exited zero with empty stderr and produced 1,209 stdout bytes with SHA-256 `4e33e2ca66a181859080b5da4c61f1081a312e94f009723908b0eaaed9d8481a`. The supplementary script has SHA-256 `2275b37aecdbf1270636821b87f13de63bfc11744e616b319801f0a309a6d0dc`.
