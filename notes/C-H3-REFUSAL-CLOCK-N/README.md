# PROMO-C-H3-REFUSAL-CLOCK-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2135](https://github.com/mathorn1973/twist-j/issues/2135)
and its frozen D,F,G,H successors. Public Canon v117,
base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

A: all21844 mixed-tag CLK patterns at even heights2..14
fail the old repeated correction schedule even with actual
native refusals. B: a free refusal clock has period90, Q24.
D/F/G: neutral direct read fails; a fixed-reference clock
writes first at17, but single-rail exact114 test fails.
H: independent material wheels with disjoint earlier
target occurrences give a general conditional finite-delay
construction and native first writes at114,90,89. The
114 witness has Q1414 and constant radiation before
write. No literal mark holds another tick. This is a
new standalone timing gate, not a complete second
restoration or integrated apparatus.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and EXPECTED.txt: A/B.
- gate.py and D.txt: D.
- reference_gate.py and F.txt: F.
- target_gate.py and G.txt: G.
- coupled_gate.py and H.txt: H.
- break.py and BREAK.txt: result-exposed alternate audit.

From repository root, let N=notes/C-H3-REFUSAL-CLOCK-N:

```sh
python3 "$N/verify.py" > /tmp/clock-ab.txt
cmp /tmp/clock-ab.txt "$N/EXPECTED.txt"
python3 "$N/gate.py" > /tmp/clock-d.txt
cmp /tmp/clock-d.txt "$N/D.txt"
python3 "$N/reference_gate.py" > /tmp/clock-f.txt
cmp /tmp/clock-f.txt "$N/F.txt"
python3 "$N/target_gate.py" > /tmp/clock-g.txt
cmp /tmp/clock-g.txt "$N/G.txt"
python3 "$N/coupled_gate.py" > /tmp/clock-h.txt
cmp /tmp/clock-h.txt "$N/H.txt"
python3 "$N/break.py" > /tmp/clock-alt.txt
cmp /tmp/clock-alt.txt "$N/BREAK.txt"
```

All sources standard-library-only. Primary checks the immutable
public H3 source. Alternate implements its own cyclic arithmetic
and contacts. Review required; do not merge or fold automatically.
