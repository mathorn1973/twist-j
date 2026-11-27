# PROMO-C-H3-SOURCE-ECHO-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2117](https://github.com/mathorn1973/twist-j/issues/2117)
and result-exposed successor C.
Public Canon v117 main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

A: a new 8x2 affine-reference source is restored exactly on all
five roots after four forward ticks with a fixed native CLK
record retained in a separate reader column. Its complete
reader history has two classes through tick160. Initial
accounts vary across the inputs.

B: a new raw-root source with a fixed vertical reference has
equal initial ring H and Q for all five input roots. Of 220
fixed stocks, 212 pass the frozen filter and 143 have at least
one exact source-column return and distinct remote CORR record
with the two-class complete reader history. First selected
witness: t24, Q=1982, output held through full25.

C: all 17160 specified late capture candidates fail their
earlier-idle pretest. No late native CLK memory in B is claimed.

These are smaller supplied source preparations, not recovery of
the original running paired Galois motor or a proof of permanent
storage or renewed measurement.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and A.txt: primary four-tick echo.
- raw_echo.py and B.txt: primary raw equal-account census.
- capture.py and C_SUMMARY.txt: bounded late capture exclusion.
- break.py: alternate five-coefficient ring and native-update audit.
- Full redundant C stdout hash retained in RUN.md.

From repository root, let N=notes/C-H3-SOURCE-ECHO-N:

```sh
python3 "$N/verify.py" > /tmp/a.txt
cmp /tmp/a.txt "$N/A.txt"
python3 "$N/raw_echo.py" > /tmp/b.txt
cmp /tmp/b.txt "$N/B.txt"
python3 "$N/capture.py" > /tmp/c.txt
sha256sum /tmp/c.txt
grep -E '^(C STOCK|C CENSUS|C NO|DONE)' /tmp/c.txt > /tmp/c_summary.txt
cmp /tmp/c_summary.txt "$N/C_SUMMARY.txt"
python3 "$N/break.py" A > /tmp/a_alt.txt
cmp /tmp/a_alt.txt "$N/A.txt"
python3 "$N/break.py" B > /tmp/b_alt.txt
cmp /tmp/b_alt.txt "$N/B.txt"
python3 "$N/break.py" C > /tmp/c_alt.txt
cmp /tmp/c_alt.txt /tmp/c.txt
```

All sources are standard-library-only. The primary source checks
the exact immutable public H3 Git blob; the alternate does not
import it or any primary code. No formal repository runner was
invoked. Review and separate formal treatment are required; do not
promote or fold automatically.
