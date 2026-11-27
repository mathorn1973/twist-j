# PROMO-C-H3-READER-ARCHIVE-RESET-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2121](https://github.com/mathorn1973/twist-j/issues/2121)
and result-exposed successor D.
Public Canon v117 main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

A: existing static reader has exact joint period 928. At t114
the entire source and the six material/CLK worker slots return
with an actual remote CORR record. Complete worker+source
reset occurs only with full field return in this preparation.
Rotating variant has no simultaneous even source/store reset
through4096.

B: all 976 guard-admitted early archive candidates out of
4140 tried fail the held-reset screen through256.
D: a separately prepared delayed archive at (5,0) writes
j+j^2 relative to its common reference at t114, Q=2952,
with complete source and six-slot working-store restoration
for all five equal-account inputs. Its fixed record changes
at full115; worker CORR remains input-dependent. No complete
worker reset, fresh-input operation or autonomous renewal claimed.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and A.txt: primary existing-field census.
- capture.py and B.txt: frozen early archive search.
- delayed.py and D.txt: common context and delayed archive.
- break.py and BREAK.txt: alternate five-coefficient A/D1
  and selected D2 audit (not an independent B search).

From repository root, let N=notes/C-H3-READER-ARCHIVE-RESET-N:

```sh
python3 "$N/verify.py" > /tmp/a.txt
cmp /tmp/a.txt "$N/A.txt"
python3 "$N/capture.py" > /tmp/b.txt
cmp /tmp/b.txt "$N/B.txt"
python3 "$N/delayed.py" > /tmp/d.txt
cmp /tmp/d.txt "$N/D.txt"
python3 "$N/break.py" > /tmp/alt.txt
cmp /tmp/alt.txt "$N/BREAK.txt"
```

All sources are standard-library-only. The primary source checks
the pinned public H3 Git blob; the alternate uses its own exact
ring and local updates, and directly asserts the core primary
census results and selected witness. No formal repository
scientific runner invoked. Review and separate formal treatment
required; do not promote or fold automatically.
