# Breaker record: P-COUNTER-BELL-PRICE-1

`break.py` is an independent audit path and not a formal gate. It was
pinned with the verifier in commit
`46c717afa5067b8f0c8818c47dbc3c7017bcc9e7` (SHA-256
`9ee229fdafb3e1b86d0de74aaf46fdd8f151e04a5f36e98310efa66285f9f300`).

```text
command: python3 probes/P-COUNTER-BELL-PRICE-1/break.py
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: a1a76f8c4c358069aefdb894a94eebd1a91c0b4608e07d169ec9b58e3da2d9e7
stdout_bytes: 662
stdout_lines: 10
stderr_bytes: 0
started_utc: 2026-09-24T07:11:51Z
```

The same breaker bytes produced the same stdout on x86_64 in the incubation
lane, so BREAKER-EXPECTED.txt is byte-identical on two architectures.

```text
BR1 HOLDS  full exact simplex, Bland rule, all 1024 deterministic types, no
           symmetry and no hand certificate: w* = 15/16, minimal overlap
           1/16, 1067 pivots; the optimal support is exactly the A = B
           singletons and pairs, the structure of the hand primal, found
           independently
BR2 HOLDS  adversarial exact hill climbs: CHSH touches the bound (slack 0)
           and never exceeds it; the QDD climb stays far below the bound,
           so this part is a weak attack and is recorded as such
BR3 HOLDS  latent merges: merging latent points with identical responses
           can lower the overlap of a model, so overlap is a model property
           and not a property of the behaviour; the full merge and 200
           random partial merges of the (C5) model all keep 1/16
BR4 HOLDS  the table rebuilt only from LOW marginals 1/4 and correlator
           E = 1/16 + (15/16) delta equals the transcribed table; B = 35/16
BREAKER RESULT NO BREAK
```

BR3 fixes the wording of (C5): the behaviour-level invariant is the minimum
over all counter models reproducing the table, which is what (C5) states.
