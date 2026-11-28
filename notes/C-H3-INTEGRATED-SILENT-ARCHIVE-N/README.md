# PROMO-C-H3-INTEGRATED-SILENT-ARCHIVE-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2131](https://github.com/mathorn1973/twist-j/issues/2131)
and its separately frozen D addendum. Public Canon v117,
main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

Adapt the #2130 absorption principle to actual
#2128 incoming radiation. All4420 frozen local
preparations are checked. The original combined
archive holds4 ticks; the taller selected device
holds126 subsequent ticks with every archive B idle.
At full114 all five source/worker columns and all48
CORR are literally initial, with distinct compensated
material records, Q=80316. After the declared external
equal-account input exchange, all25 second writes pass.
All source/worker and CORR histories agree with the
bare reference through relative126, independent of
the first bit. At relative114 the source returns
25/25, complete worker20/25. No common complete second
return through512. A separate second-bank target D
fails its incoming distinction prefilter; no stock
enumeration or changed target follows.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and EXPECTED.txt: primary A-C.
- second_bank.py and D.txt: separately frozen D.
- break.py and BREAK.txt: alternate independent ring
  and update implementation, exact A-D audit.

From repository root, let N=notes/C-H3-INTEGRATED-SILENT-ARCHIVE-N:

```sh
python3 "$N/verify.py" > /tmp/ab.txt
cmp /tmp/ab.txt "$N/EXPECTED.txt"
python3 "$N/second_bank.py" > /tmp/d.txt
cmp /tmp/d.txt "$N/D.txt"
python3 "$N/break.py" > /tmp/alt.txt
cmp /tmp/alt.txt "$N/BREAK.txt"
grep -E '^(CENSUS|BEST|COMBINED_|FIRST_RETURN|SECOND |SILENT_CONTRACT)' /tmp/ab.txt > /tmp/ab_extract.txt
grep -E '^(CENSUS|BEST|COMBINED_|FIRST_RETURN|SECOND |SILENT_CONTRACT)' /tmp/alt.txt > /tmp/alt_extract.txt
cmp /tmp/ab_extract.txt /tmp/alt_extract.txt
grep -E '^D ' /tmp/alt.txt > /tmp/d_alt.txt
cmp /tmp/d.txt /tmp/d_alt.txt
```

All sources are standard-library-only. The primary
checks the immutable public H3 source. Alternate
implements its own cyclic coefficients and contacts.
Result-exposed informal reproduction, not the formal
public gate. Review required; do not merge or fold
automatically.
