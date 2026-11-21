# Execution record

The [public claim #2052](https://github.com/mathorn1973/twist-j/issues/2052) and [immutable pin](https://github.com/mathorn1973/twist-j/commit/07e2f2ac4a6cbe2f5f862d711fb0ea1c75cfdd7a) precede formal execution. The four local Git blobs were compared against the public GitHub tree at that commit. The pinned driver validates inherited source digests and the original ordered 85-launch family before selecting rank 43.

```text
pin_commit: 07e2f2ac4a6cbe2f5f862d711fb0ea1c75cfdd7a
command: python3 probes/P-H3-RECEIVER-OUTPUT-RELAY-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 096e8ef26f4fe90e6330fa4bcc6b3ab1f980870ead240e745870b8c6f740d8a5
started_utc: 2026-11-21T14:16:29Z
ended_utc: 2026-11-21T14:17:23Z
exit_code: 0
stdout_sha256: a9e8dc1a09797b72970064b7a558544c1a2cf4d06fbcbb8d80119c14f94d4910
stdout_bytes: 3019
stdout_lines: 5
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

| Frozen file | SHA-256 |
| --- | --- |
| PREREG.md | `b935e19775d9d74c6f0c165b5b121ca532e90a6c407238617dff32b3e7f75fa6` |
| verify.py | `096e8ef26f4fe90e6330fa4bcc6b3ab1f980870ead240e745870b8c6f740d8a5` |
| relay.cpp | `8678fe7075ba6fbd84d294ad6c0db3b9f52e4f0bf4c9cfc786d7e02295272892` |
| confirm.py | `059228e6f05b2d36c13688ab88527c16aeac048468429a663d0dcb5406738e9d` |

Both native runs used the C locale, UTC, deterministic Python hashing and disabled bytecode output. The x86_64 stdout was preserved verbatim in EXPECTED.txt. The native code checked the full-field accounts and the stage inverses at selected cuts. Reversing the entire 67,108,864-tick search recovered the exact launch and matching bit.

## Complete history of the two fixed records

The registered supplementary command with `--full-witness` ran on Linux x86_64 from 14:18:02 to 14:22:30 UTC on 2026-11-21. Its five-coordinate Python kernel replayed the original field through tick 9,915,384. It checked both recurrent source histories, first-hop deliveries, the continuous hold of each site-2 output until its first overwrite, and the complete third-cell cuts and per-rail refusal counts. The one stdout line reported two events and two full replays, 373 bytes, SHA-256 `2eb14d939a117f21c8542bb88c5ad6de2fe978888267b9c3a1cfa70ae08f2feb`. Exit status was zero and stderr was empty. The exhaustive negative census through the ceiling comes from the two native scans.

## Native aarch64 reproduction

A clean detached checkout of the public pin on Debian GNU/Linux 12, aarch64, with Python 3.11.2 and g++ 12.2.0 ran the default command from 14:16:01 to 14:17:43 UTC on 2026-11-21. It started without EXPECTED.txt for the new probe and remained clean. The exit status was zero, stderr was empty, and all 3,019 stdout bytes matched the x86_64 output byte for byte.

## Supplementary readiness grouping

A separate diagnostic copy used the same native kernel and event detection, disabled the pair finder, and emitted each completed eligible read through the full ceiling. For each read it preserved the originating branch, readiness, terminal stage, mate and number of moved rails. Readiness was the ordered tuple of the four `reader_pre` rails followed by `reader_c[2:4]`. Ring-value IDs were shared across the entire scan. Each read tick occurred once. The instrumented output, including the original fixed records, had SHA-256 `f9af83cbb470946e8e6d9c69802316c7c280f21cc84b254f9120bb9bda2f38a6`.

For each branch, a set held all observed readiness tuples. A second set accepted a tuple only if the terminal stage was C at site 3 and the number of moved rails was positive. Separate Python aggregation of these observations recovered the registered branch totals and zero pending holds. The two all-read sets had sizes 44 and 48 and intersection size 3. The sets for successful deliveries had sizes 17 and 9 and intersection size 0. This diagnostic explains the registered count and shares its native dynamics. It was performed after the formal run.

A separate five-coordinate replay from launch through tick 1,137,486 checked the two illustrative individual deliveries at 715,458 and 1,137,486, the recurrent upstream emissions, the actual local readiness, and every intervening material hold. Both destination contacts changed the two material rails. The 4,342-byte supplemental output on Linux x86_64 had SHA-256 `419bc5c7bd47a35f1fe2461b741b1334bc076d544ecff1a844b61d83b5f85510`, exit status zero, and empty stderr.

A targeted extraction in the same native dynamics also retained complete certificates for the two B1 reads in the #2049 readiness state and its one successful B2 relay. The (earliest identical source episode, recurrent emission, site-2 read) triples were (7316785,7390473,7390475), (7316785,7390685,7390687) and (8176761,36442231,36442233). Five-coordinate local calculations verified the branch and contact arithmetic and compared each read against its corresponding #2049 arm. The native certificates had SHA-256 `25c262b683ef432061e46b4c7777726a6a69aa1efee8d19a89c39c47cb9138b1` and the local comparison had SHA-256 `80f7d6d1362f5646a3edac930f250ee3152963356c88e7b8993adf77d13cee45`. These later diagnostics were separate from the registered scan.
