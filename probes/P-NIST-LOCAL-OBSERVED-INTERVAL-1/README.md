# Causal local observation packets

NON-CANONICAL / PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED.

The [preregistration](PREREG.md) freezes the same four NIST source portions
already decoded by P-NIST-RAW-RECORD-QUALIFICATION-1. This successor turns raw
indexed rows into lossless local packets with explicit ownership and causal
closure. The [argument](PROOF.md) explains the partition and prefix invariants.
DEPENDENCIES.json binds every reused source and the new adapter implementation.

```text
python3 probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/verify.py
```

Use Python 3.12 standard library from the repository root on Linux. Cold replay
downloads 746,878,746 compressed bytes to temporary storage. Optional
`TWISTJ_NIST_CACHE_DIR` supplies `<id>.zip` cache files, each fully rehashed
before ZIP access. Preserve the inherited
[NIST notice](../../notes/NIST-RAW-CUSTODY-1.md) with all data copies.

The streaming adapter is also a reusable API: indexed raw rows go through
`feed` or `feed_many`; `snapshot` describes the pending fragment without
emitting an event or resetting the stream. Full packet payloads are transient;
the repository retains only bounded audit summaries and canonical digests.
Right sync references are nonowning. Metadata channel 64 is never an event clock.

A closed record packet does not certify a physical trial, no-click, complete
apparatus or a Born law. The NIST measurement proposal remains a distinct
physical interpretation contract under issue #839.
