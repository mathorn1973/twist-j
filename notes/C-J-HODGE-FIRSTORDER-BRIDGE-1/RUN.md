# Local run record (not a public probe gate)

**NON-CANONICAL, L1, single architecture.** No formal frozen public preregistration and no independent blind breaker. Calculations and outputs were exposed before this verifier was authored.

```
Platform: Linux x86_64
Python: 3.13.5
Command: python3 verify.py
Exit: 0
Stderr: 0 bytes
Stdout: 830 bytes
Stdout SHA-256: dfdf503cb2f71163187583877ee088a6961198801b696133c4ee805212cacb08
Verifier SHA-256: b6fe0f23f2d7cc23e288bff85a97645c20c978bceb9652696d398eb9c91a4485
Comparison: expected stdout exact byte match
Repeat: a second same-architecture execution also matched exactly; reproduction only
```

The new verifier was first assembled in local development, before this recorded accepted run. Its initial typed quotient action mistakenly omitted the factor 2 from `Lambda^2 M_J` acting on `ell wedge Vbar`. The error was corrected and the full exterior-square induced action was reconstructed before this recorded successful local run. The failure was a local implementation defect, not a pinned scientific falsifier. No public formal gate or immutable preregistration was claimed.

The original author's six source file digests (plus source SHA256SUMS itself) and archive custody are separately listed in `SOURCE-MANIFEST.md`. The new `SHA256SUMS` covers the proposed note's own files, not the historical archive.

Public CI for this notes-only PR does not execute this verifier as a formal public probe. Nothing here gives theorem-status acceptance, native `U` causality or L2/L6 evidence.
