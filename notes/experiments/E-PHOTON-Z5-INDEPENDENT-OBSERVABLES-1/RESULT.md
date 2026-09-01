# Result - independent Z5 saved-state reader

> **NON-CANONICAL / ZERO-EVIDENCE.** Maximum result in this lane is engineering
> integrity. This document does not classify a phase or authorize production.

## Verdict

The immutable candidate pin returned

```text
INDEPENDENT_READER_FIXTURE_PASS
EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY
```

The formal command exited `0`, wrote exactly 72 ASCII/LF bytes to stdout, wrote
empty stderr and was not rerun. Its exact transcript is `EXPECTED.txt`; full
chronology and custody are in `RUN.md`.

## What passed

- The recursive candidate inventory contained exactly the pinned documents,
  sources, verifier, nine fixture states and `SOURCE_SHA256SUMS`, with no extra
  file, symlink or bytecode cache.
- All 15 manifest-owned rows matched their exact byte counts and SHA-256 values.
- The oracle was executed directly from the verified `fixture_oracle.py` source
  bytes, never from an import-path candidate or `.pyc` file.
- The strict seven-line state parser accepted canonical `uint64` boundaries and
  rejected all 19 malformed controls in both Python and C++, plus absent,
  uppercase, empty and mismatched digest controls.
- Nine analytic periodic fixtures fixed oriented plaquette signs, all four
  Polyakov directions, charge conjugation, local current closure, contractible
  and charged-wrapping monopole components, charged vortex homology, cancelling
  wrapped components and the support-winding/charged-zero negative control.
- A two-record same-chain fixture proved exactly in `Q(zeta_5)` that block
  histogram aggregation differs from forbidden configuration-centering.
- The independent Python oracle and C++ reader produced byte-identical complete
  canonical JSON for every accepted fixture, including all frozen full-record,
  correlator and fingerprint digests.

## Authority boundary

This result is the local one-shot reader result required by issue `#748`. It
satisfies production-firewall condition `F2` only after this record is merged,
all required repository checks pass and the merge is publicly read back.

It does not satisfy or waive condition `F3`: the separate `L=6,8` execution
under issue `#756` must still return `DUAL_CROSSCHECK_PASS`. Production issue
`#742` therefore remains forbidden. No Canon, Registry, Gate, Frontier,
release, theorem or program status changes here.
