# Multi-architecture run record for the review

Status: **NON-CANONICAL**

Branch state exercised: commit
`01a99d71370952bccd042b6a2f99fe332b4257a3` (review artifacts) on top of
`177f2602dc406ea4ee89f24d4fd32bd39500a5ec` (primary result package).

On every leg the upstream source was freshly cloned and pin-checked:
commit `1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`, file
`AME46_ORIGINAL.m`, 8515 bytes, SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.

## Legs

| Leg | Platform | CPython | Primary scripts vs `EXPECTED_*` | Review certificates |
|---|---|---|---|---|
| A | Linux x86_64 | 3.11 | byte-identical (3 of 3) | reference run |
| B | Linux x86_64 | 3.12 | byte-identical (3 of 3) | byte-identical |
| C | Linux aarch64 | 3.11 | byte-identical (3 of 3) | byte-identical |

All ten script executions exited 0. The three primary scripts produced
empty stderr; the two review scripts write exactly one platform line to
stderr by design, and their stdout certificates carry no platform data.

Certificate hashes, identical on every leg:

```text
CERT-G0-G1-INDEPENDENT.txt  5afb8eb1c188536de7de175eec3fe1340ea47fa449471540d67f5f6a3c3c1f7d
CERT-G3-G4-REVIEW.txt       48f469f53ffc3803647b0708a590954f356f8f991dbfff4262343d1e533755f9
```

The primary `RUN.md` recorded a single x86_64 environment and explicitly
claimed no architecture gate. This record adds two-architecture
byte-identity for both the primary and the review scripts. Machine
nicknames and private addresses are intentionally not recorded.
