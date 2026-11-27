# PROMO-C-H3-CAPTURE-CLOCK-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2119](https://github.com/mathorn1973/twist-j/issues/2119)
and result-exposed addenda D,E.
Public Canon v117 main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

A: a local free-C clock on height two repeats modulo five. All 143
earliest successful raw-source return cuts from #2118 have an earlier
identical incoming value at the same clock phase. Waiting with an
otherwise B-idle five-step clock cannot distinguish those events.

B: first successful early-capture preparation writes at tick6 and
retains a fixed CLK/reference record over seven exact common even
source returns at 16,30,44,58,72,86,100, with Q=2654 for every input.
The hold lasts through full110 and post-C111. All five raw roots have
equal complete initial accounts; the four negative reader histories
are identical through160.

C: frozen standalone t3 prediction fails (first B at t2).
D: changing the initial rotating clock phase changes or suppresses
the write; simpler static readiness also succeeds, Q=2630. Clock
necessity in the coupled device is not established.
E: independent new constant-radiation timing gate gives first writes
at 3,2,1,5,4 in its five initial clock phases, Q=360. It is not a
permanent or repeatedly reset clock, nor integrated into B.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and EXPECTED.txt: primary A-C, including bounded B search.
- controls.py and D.txt: D phase and static controls.
- phase_gate.py and E.txt: E standalone timing gate.
- break.py and BREAK.txt: independent five-coefficient arithmetic and
  exact A,C, selected B via D, D and E replay. No independent B search.
- B_PREV.txt: exact pinned #2118 B.txt, input roster for A; not new evidence.

From repository root, let N=notes/C-H3-CAPTURE-CLOCK-N:

```sh
python3 "$N/verify.py" > /tmp/abc.txt
cmp /tmp/abc.txt "$N/EXPECTED.txt"
python3 "$N/controls.py" > /tmp/d.txt
cmp /tmp/d.txt "$N/D.txt"
python3 "$N/phase_gate.py" > /tmp/e.txt
cmp /tmp/e.txt "$N/E.txt"
python3 "$N/break.py" > /tmp/alt.txt
cmp /tmp/alt.txt "$N/BREAK.txt"
grep -E '^A ' /tmp/abc.txt > /tmp/a.txt
grep -E '^A ' /tmp/alt.txt > /tmp/a_alt.txt
cmp /tmp/a.txt /tmp/a_alt.txt
grep -E '^C ' /tmp/abc.txt > /tmp/c.txt
grep -E '^C ' /tmp/alt.txt > /tmp/c_alt.txt
cmp /tmp/c.txt /tmp/c_alt.txt
sed -n '/^D CONTROL /,/^DONE exact clock phase controls/p' /tmp/alt.txt > /tmp/d_alt.txt
cmp /tmp/d.txt /tmp/d_alt.txt
sed -n '/^E NORMS/,$p' /tmp/alt.txt > /tmp/e_alt.txt
cmp /tmp/e.txt /tmp/e_alt.txt
```

All sources are standard-library-only. No formal repository runner,
general clock theorem for H3, original paired motor recovery, physical
interpretation or higher-layer result is claimed. Do not automatically
fold or promote.
