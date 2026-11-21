# First-run custody

Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.

The first captured scientific disposition is **CERTIFIED**. This file
records that existing execution; preparing it does not rerun the code.

```text
pin_commit: c4eee088d88f2da8dfab9e1f0c12249ad97c0b97
verifier_sha256: 13934b6e27d91b9f74f426970e42fa3f093df32c18f870ffdbe34bc3c9b32c47
command: python3 probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 988edf0ef07e5e638217301b53dac7da1fb7a605954048022519dc4c0c687bf5
stdout_bytes: 1171
stdout_lines: 28
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Public pin and execution order

- Public input commit: `c4eee088d88f2da8dfab9e1f0c12249ad97c0b97`.
- Public input tree: `b94b56914da77a50b4baaacdf58e82303dfba190`.
- Sole parent: `a193e389fb1ddb0bdc89165b015c95a17eb1e425`.
- All five files fetched at the public pin and compared byte for byte:
  **2026-10-28 12:17:39 UTC**.
- First scientific process started: **2026-10-28T12:17:59.246486+00:00**.
- First scientific process completed: **2026-10-28T12:17:59.353991+00:00**.
- Observed wall duration: 0.107728408 seconds.

The public branch ref, commit, parent, tree and approved author identity
were read back before execution. A fresh repository-root-shaped directory
was materialized from those publicly returned UTF-8 bytes. Its five file
lengths, SHA-256 and Git blob hashes were checked before the subprocess.
No local unpinned scientific code was substituted.

The process used Python 3.12 with `PYTHONHASHSEED=0`,
`PYTHONIOENCODING=utf-8`, `LC_ALL=C.UTF-8`, `LANG=C.UTF-8`, and `TZ=UTC`.
The subprocess had a 600-second timeout. It completed normally. The
exact captured stdout was copied unchanged to EXPECTED.txt; stderr
was empty. No scientific trial, import, numerical search or predecessor
replay preceded this first audit run. Pre-pin compilation and static
source review did not execute scientific code.

## Complete pinned input custody

| Public input | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/verify.py` | 18600 | `13934b6e27d91b9f74f426970e42fa3f093df32c18f870ffdbe34bc3c9b32c47` | `7ac5d3141e0f9ecfd03ab27af8391142726b187a` |
| `probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/PREREG.md` | 13333 | `31c3aa5ee25012f6af82a486cfae67cbbcd92d10585c8f166f8fadf9b098396c` | `3bbc71431bb228b91cdf89ef962fd232bac39bc4` |
| `notes/C-BOUND-PAIR-RESOLVENT-AUDIT-N/PROOF.md` | 28369 | `d8d74050b13902bd9aaa8be7f24feb399f5e997743a794a0cc7ecc179930254f` | `b65484c00235d5caa58e04106c7e47f93fc58d08` |
| `notes/C-BOUND-PAIR-RESOLVENT-AUDIT-N/SOURCES.md` | 8053 | `8e80ef466fcb4384919ad2f1e3edfdd34b0f58c670e64ac87936f74f99792cb9` | `58cb998392cfffd7f12e4608794e7aa127f9a98a` |
| `notes/C-BOUND-PAIR-RESOLVENT-AUDIT-N/FINITE_PROTOCOL.md` | 26374 | `715e0c5e4ec2e13757bc37855f757ad08044198cd0ad9e1681a60ac9b5663eb3` | `813f37601bc0fb1a1d963b44f37e4561351df098` |

Only `verify.py` is an executable input. The other four documents are
in the same pin and remain unchanged. The analytical finite-protocol
note has no numerical scattering-time result and is not a hidden
runtime input.

## Contributor and reproduction scope

The connected-account identity is A. M. Thorn
<221838986+mathorn1973@users.noreply.github.com>, explicitly approved by
the user for this continuing session and recorded in #1816. Source
headers retain the project correspondence address.

This is the first local x86_64 run. Independent GitHub x86_64 and
aarch64 byte replays are required by the PR workflow and are reported
by their actual job records, not inferred by this file. Same-session
static review is not external independent theorem acceptance.
