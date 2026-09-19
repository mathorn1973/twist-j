# Public acceptance: P-U-COUNTER-AMPLITUDE-CLASS-1

Status: **TWO-ARCHITECTURE SCIENTIFIC REPLAY AND CHECK PASS**.
This is a head-pinned readback record, separate from the historical local
execution in RUN.md. The probe remains NON-CANONICAL until a Canon fold.

PR: [#1078](https://github.com/mathorn1973/twist-j/pull/1078).
Immutable four-file pin: `e38ee8049797a9ae60935753eb2c68e5a53f2492`.
Tested PR head: `9053491000dd22396a7824c7bc01c47267fd42ef`.
Base: `16e6bd3579527f522ca7e8c85411107f6873eea8`.

| Required job | Outcome and scientific evidence |
| --- | --- |
| [x86_64](https://github.com/mathorn1973/twist-j/actions/runs/35475498169/job/105983932619) | success; VERIFY ARCHITECTURE x86_64; VERIFY PASS with hashes below |
| [aarch64](https://github.com/mathorn1973/twist-j/actions/runs/35475498169/job/105983932750) | success; VERIFY ARCHITECTURE aarch64; VERIFY PASS with identical hashes |
| [check](https://github.com/mathorn1973/twist-j/actions/runs/35475498169/job/105983992521) | success; both required architecture jobs succeeded |

The workflow metadata names the exact tested head above. Actual logs from
both architecture jobs were inspected for this probe's architecture and
VERIFY PASS lines. These are scientific verifier replays, not inference
from a green documentation job.

```text
prereg_sha256: d69d98c58d417ca3f760394ab639096076863a3be1b3335d515539b570297de3
proof_sha256: e2e2e42dcb66d007d2f7eeb52178cff50eb4000c3a350e0368b54759bec32725
verifier_sha256: d811afdd74cc11891282d93bf4575e7fc087a2ee209d74729e4ba1e3feb0e703
stdout_sha256: f6495cdbf148175e762ab7d0fb628b303d93ecda3130c06c3f94bd3df0a8b2cb
stdout_bytes: 1155
stdout_lines: 18
```

This subsequent documentation commit adds this acceptance record and updates
RESULT.md only. All four scientific pin files and both exact output files
remain unchanged. The final PR head must also pass the repository gate
before merge. The independent breaker has one recorded local architecture;
the public two-architecture statement concerns verify.py.
