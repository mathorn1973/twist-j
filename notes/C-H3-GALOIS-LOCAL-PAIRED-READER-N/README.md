# PROMO-C-H3-GALOIS-LOCAL-PAIRED-READER-N

NON-CANONICAL / NO AUTHORITY. L1 only.
Frozen [issue #2111](https://github.com/mathorn1973/twist-j/issues/2111)
and result-exposed preregistration addenda D,E.
Base Public Canon v117, main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

Two independently prepared four-state address tracks coexist on the same
8 by 8 field, with 224/224 complete four-stroke returns across fourteen
layouts. The faster adjacent-column family is exactly radiation-blind,
including B tags; the material C masks distinguish all sixteen inputs.
Fixed two-cut material readers recover the two independent phase
weights. A new algebraic seed choice yields two unimodular cyclic bases
whose coefficient pairing is the identity. All 80 paired read windows
and actual positional coincidence counts agree, with q=1024.

The actual K/W target values are mathematical read outputs, not native
arithmetic writes. The radiative reader fails; no active native
readout circuit, outside-code validity test, general coefficient
permutation, physical reading or cross-layer claim is made.

- PREREG.md, PROOF.md, RUN.md: scope, proof and custody.
- verify.py: A-C primary audit of the frozen fields.
- local_material.py: D, corrected missing helper alias.
- dual_basis.py: E, corrected shift-name shadowing.
- local_material_original.py, dual_basis_original.py and four
  FIRST_PARTIAL/FIRST_ERROR text files: original failed executions,
  retained without changing their scientific contracts.
- break.py: alternate exact five-power ring and native-update audit.
- EXPECTED.txt, D.txt, E.txt, BREAK.txt: exact final transcripts.

From repository root, let N=notes/C-H3-GALOIS-LOCAL-PAIRED-READER-N:

```sh
python3 "$N/verify.py" > /tmp/abc.txt
cmp /tmp/abc.txt "$N/EXPECTED.txt"
python3 "$N/local_material.py" > /tmp/d.txt
cmp /tmp/d.txt "$N/D.txt"
python3 "$N/dual_basis.py" > /tmp/e.txt
cmp /tmp/e.txt "$N/E.txt"
python3 "$N/break.py" > /tmp/alt.txt
cmp /tmp/alt.txt "$N/BREAK.txt"
sed -n '/^E1 X/,$p' /tmp/alt.txt > /tmp/ealt.txt
cmp /tmp/ealt.txt "$N/E.txt"
```

All sources are standard-library-only. The primary source checks the
immutable public H3 Git blob before import. The alternate checks core
A-D results and independently computes the full E transcript.
No formal public scientific runner was invoked. Review and a separate
later formal treatment are required; do not automatically fold.
