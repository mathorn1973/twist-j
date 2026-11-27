# PROMO-C-H3-ARCHIVE-INTERFACE-N

NON-CANONICAL / NO AUTHORITY. L1.
[Issue #2127](https://github.com/mathorn1973/twist-j/issues/2127)
and result-exposed C/D addenda. Public Canon v117 main
6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

A: locate exact residual CORR and old-bit-dependent interface.
B/D: separately supplied passive phase memory; seven of ten
small stock choices pass160 and a distinct large common CLK
stock has an all-time no-B proof. No native writer into it.
C: combine two inverse-synthesized column5 B contacts and
a height6 vertical clock on column7. At t114 all five source
and worker columns and all48 CORR are literally initial,
with a two-class compensated archive, Q=80436. After the
declared external equal-account new-input exchange, all25
second writes are correct, including 11. Current archive
has four classes at all256 even cuts through512 and first-bit
separation persists at every cut. No common complete second
source/worker return through512. This is not yet a fully
renewed instrument. The actual archive can later react back.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py and EXPECTED.txt: primary A/B.
- synthesis.py and C.txt: primary C, corrected one name.
- synthesis_original.py and C_FIRST_PARTIAL.txt: original
  source and scientific partial stdout before that repair.
- diagnostic.py and D.txt: primary D.
- break.py and BREAK.txt: alternate exact A/B/C and core D.
- predecessor.py and alternate_predecessor.py: pinned engine
  inputs reused from #2126, not new independent evidence.

From repository root, let N=notes/C-H3-ARCHIVE-INTERFACE-N:

```sh
python3 "$N/verify.py" > /tmp/ab.txt
cmp /tmp/ab.txt "$N/EXPECTED.txt"
python3 "$N/synthesis.py" > /tmp/c.txt
cmp /tmp/c.txt "$N/C.txt"
python3 "$N/diagnostic.py" > /tmp/d.txt
cmp /tmp/d.txt "$N/D.txt"
python3 "$N/break.py" > /tmp/alt.txt
cmp /tmp/alt.txt "$N/BREAK.txt"
```

All sources are standard-library-only. The primary uses the
exact pinned public H3 source via predecessor.py. The alternate
uses its own pinned five-coefficient ring and update engine.
No formal repository runner invoked. Review required; do not
merge or fold automatically.
