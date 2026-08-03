# Kappa witness candidate archive

**STATUS: NON-CANONICAL. NO PROBE RUN. NO PUBLIC EVIDENCE.**

This directory accompanies
`notes/KAPPA-CHECKERBOARD-ATTACK-2026-08-03.md`.  The exact candidate
certificate is `witness_6_3_6_6.json`; its SHA-256 is
`9b664f16830d2b562949933e40b4f1460d9da5645a88beff7bca347b70320313`
and its byte count is 280106.

The two read-only certificate checks use only the Python standard library:

```text
python3 -B verify_witness.py witness_6_3_6_6.json
python3 -B adversarial_check_fresh.py
```

They are review tools, not a formal reproduction.  No `EXPECTED.txt`, run
record, architecture record, probe result, or public status is claimed here.
The reserved formal route remains `P-PHOTON-KAPPA-LEMMA-1` after issue #200
freezes the complete definition surface.

The remaining Python files are exploratory builders and diagnostics.  Some
builders optionally import PuLP and invoke HiGHS or CBC; those dependencies
are not vendored or pinned here and their output cannot support a formal
claim.  See `SOLVER-NOTES.md` for the deliberately limited solver provenance.
Root Apache-2.0 licensing applies to the authored files in this directory;
third-party solver code and raw solver transcripts are not included.
