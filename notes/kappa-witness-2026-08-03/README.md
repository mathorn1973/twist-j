# Kappa witness candidate archive

**STATUS: NON-CANONICAL. NON-FORMAL REVIEW ONLY. NO PROBE RUN. NO PUBLIC
EVIDENCE. NO FORMAL PIN OR RESULT.**

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

The separately reviewed candidate for the future accepted probe verifier is:

```text
python3 -B verify_probe_candidate.py
```

It accepts no arguments, reads the adjacent pinned JSON, and implements the
canonical-byte, C1-C7, and S1-S5 contract of
`notes/canon/P-PHOTON-KAPPA-LEMMA-1-DEFINITION-PACKAGE.md`.  Executing it here
is expressly **non-formal review**.  Its stdout is not `EXPECTED.txt`, its
exit status is not a gate record, and a passing review earns no evidence,
status, closure, or outcome.

The reserved branch `probe/P-PHOTON-KAPPA-LEMMA-1` and path
`probes/P-PHOTON-KAPPA-LEMMA-1/` remain forbidden until all of the following
occur separately: the definition package is merged and publicly read back;
the owner records the required carrier, singleton-family, repeated-vertex,
`Fill(j) != empty`, subset-inclusion, and lane/probe outcome rulings in issue
#200; this candidate's exact public bytes and SHA-256 are reviewed and
owner-accepted there; current authority and collisions are rechecked; and the
owner explicitly authorizes the formal branch and preregistration pin.  Only
then may these accepted verifier bytes be copied byte-identically beside the
pinned witness and `PREREG.md`.  Formal execution remains forbidden until
remote pin hashes, byte counts, and line endings are read back exactly.

This notes directory must not receive `EXPECTED.txt`, `RUN.md`, `RESULT.md`,
architecture records, or any file presented as a formal probe artifact.

The remaining Python files are exploratory builders and diagnostics.  Some
builders optionally import PuLP and invoke HiGHS or CBC; those dependencies
are not vendored or pinned here and their output cannot support a formal
claim.  See `SOLVER-NOTES.md` for the deliberately limited solver provenance.
Root Apache-2.0 licensing applies to the authored files in this directory;
third-party solver code and raw solver transcripts are not included.
