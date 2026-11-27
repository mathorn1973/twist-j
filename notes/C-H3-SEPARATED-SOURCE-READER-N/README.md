# PROMO-C-H3-SEPARATED-SOURCE-READER-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2115](https://github.com/mathorn1973/twist-j/issues/2115)
and its result-exposed preregistration addendum D.
Public Canon v117, main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

Strict preservation of the reference material trajectory in the two
complete source columns prevents any input-dependent radiation or
outside-source material record from a common reader preparation.
The explicit new 8x8 single-column source interrogation instead
keeps the initial source column unchanged up to one common integral
scale and sends common radiation pulses from separate reader columns.
At tick5 a fixed remote CORR distinguishes one phase from the other
three; all sixteen separately translated address-query preparations
pass. A further fixed common receiver stock writes the same bit
into one actual remote CLK, with a retained adjacent reference and
difference phi. The selected stock holds the binary record through
full tick12. Whole-reader histories have exactly two classes through
that cut, not four.

The source trajectory is disturbed and no material or complete
source-column recovery is found through tick160. There is no
nondestructive original two-track coupling, simultaneous equality
comparison, four-port reduction, native source/reader preparation
or physical/higher-layer claim.

- PREREG.md: original scope and separately frozen successor D.
- PROOF.md: conditional obstruction, exact construction and limits.
- verify.py and EXPECTED.txt: primary A-C audit.
- capture.py and D.txt: primary D capture search.
- break.py: separately implemented five-power arithmetic, local law
  and exact synthesis/replay for A-C and D.
- RUN.md: evidence custody.

From repository root, let N=notes/C-H3-SEPARATED-SOURCE-READER-N:

```sh
python3 "$N/verify.py" > /tmp/abc.txt
cmp /tmp/abc.txt "$N/EXPECTED.txt"
python3 "$N/capture.py" > /tmp/d.txt
cmp /tmp/d.txt "$N/D.txt"
python3 "$N/break.py" ABC > /tmp/abc_alt.txt
cmp /tmp/abc_alt.txt "$N/EXPECTED.txt"
python3 "$N/break.py" D > /tmp/d_alt.txt
cmp /tmp/d_alt.txt "$N/D.txt"
```

All sources are standard-library-only. The first checks the
immutable public H3 Git blob before import. Capture replays the
first transcript before its separate successor computation. The
alternate does not import either or the public H3 implementation.
No formal public scientific runner was invoked. Review and
separate formal treatment are required; do not promote or
fold automatically.
