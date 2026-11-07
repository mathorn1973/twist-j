<!-- SPDX-License-Identifier: Apache-2.0 -->

# First prospective reduced-collision audit

Source pin: `70233c0ae554fece2a472b6fdc4dc0990f4f28e9`.
All nine source files were fetched from that exact public commit through the
GitHub connector BEFORE execution; every returned Git blob matched the
locally inspected pinned blob. SOURCE-SHA256SUMS was checked again before
launch. The verifier is byte-identical to the unexecuted precursor.

| Item | Actual value |
|---|---|
| Platform | Ubuntu 22.04.5 LTS |
| Architecture | x86_64 |
| Python | 3.10.12 |
| Command | `python3 -I -B notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/verify.py` |
| UTC start | 2026-11-07T08:09:47.258877+00:00 |
| Elapsed time | approximately 9.77136 seconds, execution metadata only |
| Exit | 0 |
| stderr | 0 bytes |
| stdout | 560 bytes |
| stdout SHA-256 | 7145286870c9e12d1962676f80cedf700eb205ecd502b1e9cb4c3c4f120c5385 |
| Verifier SHA-256 | 6db372a9c5b7d9ac634f10b8b6ba16b6dde712c659cf21e7d026c08c0c346dea |
| Limits | real subprocess timeout 300 seconds; RLIMIT_AS 1073741824 bytes |

This was the FIRST scientific execution of the unchanged pinned source.
No failure, timeout, source correction or threshold change occurred.
The complete deterministic stdout is EXPECTED.txt. The process limits were
enforced by an external standard-library wrapper; its metadata and original
stdout/stderr are retained separately. No private paths or machine names are
part of the public scientific record.

This run is a reduced mathematical notes audit, not a full spatial-field
reproduction or a formal P-probe CI gate. Universal results rely on the
written proof. Same-session review is not independent acceptance.

## Clean second-architecture reproduction

A fresh single-branch clone of the public source pin was checked clean, and
all SOURCE-SHA256SUMS entries were verified before launch. The same unchanged
verifier ran on Debian GNU/Linux 12, aarch64, Python 3.11.2, with the same
300-second timeout and 1-GiB RLIMIT_AS. UTC start 2026-11-07T08:11:28.134124+00:00;
measured duration approximately 25.84695 seconds. Exit 0, stderr 0 bytes,
stdout 560 bytes, SHA-256 7145286870c9e12d1962676f80cedf700eb205ecd502b1e9cb4c3c4f120c5385.
It matches the first x86_64 stdout exactly by size and SHA-256. Source SHA-256
also matches 6db372a9c5b7d9ac634f10b8b6ba16b6dde712c659cf21e7d026c08c0c346dea.

This is actual two-architecture reproduction of the reduced notes audit,
not independent authorship, physical validation or a claim that notes CI
executed the verifier. The two raw receipts are retained outside the public
repository; this record uses only neutral environment descriptors.
