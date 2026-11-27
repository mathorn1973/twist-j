# PROMO-C-H3-NEUTRAL-COEFFICIENT-TRANSPORT-N

NON-CANONICAL / NO AUTHORITY. L1 only. Frozen reservation
[issue #2109](https://github.com/mathorn1973/twist-j/issues/2109),
with four result-exposed preregistration addenda D-G.
Base Public Canon v117, main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

Exact bounded negative results: arbitrary fixed-horizon affine
cyclic transport of four independent integer coefficients is
obstructed; all 1296 two-tick branch words in the stated relay
carrier exclude an active-C full return; no frozen horizontal
single-defect translation or direct height-8 single-marker
translation was found. All original failures are retained.

Positive finite results: five-input clean neutral phase relocation
on 8 by 4, with all other stock restored, after 40 or 120 ticks.
On 8 by 8, two independently supplied nonbaseline phases give
32/32 verified full-field translations over four strokes,
24 exact order-four orbits and eight order-two controls.
The faster unequal-phase full period is 160 ticks and Q=1024.
No raw Galois arithmetic or arbitrary coefficient permutation
is claimed. A fixed four-address Galois code is a conditional
mathematical interpretation of the actual transport.

Files: PREREG.md, PROOF.md, RUN.md; verify.py and search2d.py
(first exact A-C audit), break.py (alternate A-C); closed_audit.py
(literal replay of eight closed cases); phase_diagnostic.py,
phase_record.py, height8.py, four_stroke.py (D-G);
follow_break.py (alternate D-G). EXPECTED.txt, FOLLOW.txt and
CLOSED.txt are exact retained transcripts. All scripts are
standard-library only. The first implementation imports the
immutable public H3 source after verifying its Git blob identity;
the second implements the ring and contacts independently.

From repository root, let N=notes/C-H3-NEUTRAL-COEFFICIENT-TRANSPORT-N:

```sh
{ python3 "$N/verify.py"; python3 "$N/search2d.py"; } > /tmp/abc.txt
cmp /tmp/abc.txt "$N/EXPECTED.txt"
python3 "$N/break.py" > /tmp/abc_alt.txt
cmp /tmp/abc_alt.txt "$N/EXPECTED.txt"
python3 "$N/closed_audit.py" > /tmp/closed.txt
cmp /tmp/closed.txt "$N/CLOSED.txt"
{ python3 "$N/phase_diagnostic.py"; python3 "$N/phase_record.py";   python3 "$N/height8.py"; python3 "$N/four_stroke.py"; } > /tmp/follow.txt
cmp /tmp/follow.txt "$N/FOLLOW.txt"
python3 "$N/follow_break.py" > /tmp/follow_alt.txt
cmp /tmp/follow_alt.txt "$N/FOLLOW.txt"
```

No formal public probe runner was invoked. Review and any separate
future formal treatment remain necessary; do not promote or fold
automatically.
