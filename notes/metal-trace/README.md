# notes/metal-trace

NON-CANONICAL. Exploration and audit material for the metallic-trace
lane. Nothing here is evidence for a public claim; the formal probe is
`probes/P-METAL-TRACE-1/` (public lock: issue 70, pull request 71).

```
verify_metal_trace.py          independent exploration witness (19 checks)
                               sha256 6e742fb01b23d1209fe1369c297530257df024190028fd258a46923f71d4ebdd
C-METAL-TRACE-1_break.py       independent break path of the candidate:
                               companion matrices + squarefree kernels,
                               locates the t = 1 / t = 4 scope boundary
                               sha256 f7feb2798eda1337f2e4b7da275bc29d1c1feb33f51a57c74219e132d6e55fb1
EXPECTED_break.txt             break path stdout (CORE SURVIVES, 31
                               assertions, 0 failures)
                               sha256 2c8065bf1a94a82ac9eb4a799e2bf1b3fee9ffcded94c1040de0bb31d307ab91
```

The hashes above are the ones pinned in issue 70 and in the probe's
PREREG.md. The synthesis note is
`notes/METAL-TRACE-SYNTHESIS_2026-07-19.md`; the fold proposal is
`notes/canon/PROMO-C-METAL-TRACE-1.md` and changes nothing until a
separate sealed public fold.
