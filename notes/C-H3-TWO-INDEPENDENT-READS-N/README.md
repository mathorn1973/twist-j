# PROMO-C-H3-TWO-INDEPENDENT-READS-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2125](https://github.com/mathorn1973/twist-j/issues/2125)
and result-exposed D/E addendum.
Public Canon v117 main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

The exact #2124 relative archive is tested with a second
independently supplied raw root at complete source/worker
return cuts 114,198,244. Only the neutral source pair is
exchanged, at equal complete accounts, with an external
reserve retaining the old input. No native loader claimed.

Each of the three all-25-input families gives 24/25
correct second CLK writes at relative6, but 11 is missed
by the actual parity guard. At relative114 each has four
distinct current archive states, with only 16/25 complete
source/worker resets. A single actual CORR gives a joint
four-symbol read at that cut; no independently separated
bit reads or column factors. No common even complete
source/worker reset occurs through4096. All 600 admitted
alternative compensated receiver preparations fail the
same 11 second-write screen.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and EXPECTED.txt: primary A/C census.
- diagnostic.py and D_E.txt: primary D/E diagnostics and search.
- break.py: alternate audit reproducing both transcripts.
- predecessor.py and alternate_predecessor.py: immutable
  reused engine inputs from the earlier #2122/#2124 package,
  not presented as new evidence.

From repository root, let N=notes/C-H3-TWO-INDEPENDENT-READS-N:

```sh
python3 "$N/verify.py" > /tmp/two-reads-a.txt
cmp /tmp/two-reads-a.txt "$N/EXPECTED.txt"
python3 "$N/diagnostic.py" > /tmp/two-reads-de.txt
cmp /tmp/two-reads-de.txt "$N/D_E.txt"
python3 "$N/break.py" A > /tmp/two-reads-a-alt.txt
cmp /tmp/two-reads-a-alt.txt "$N/EXPECTED.txt"
python3 "$N/break.py" DE > /tmp/two-reads-de-alt.txt
cmp /tmp/two-reads-de-alt.txt "$N/D_E.txt"
```

All sources are standard-library-only. The primary imports
the immutable public H3 via predecessor.py. The alternate
uses its own pinned five-coefficient ring and update engine.
No formal repository runner invoked. The two-bit code is
not a fully renewed measurement device. Review required;
do not merge or fold automatically.
