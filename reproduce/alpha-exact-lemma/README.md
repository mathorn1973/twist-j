# Alpha exact lemma witness

The dimensionless trace target alpha* = 1/p, exactly: the cyclotomic
Galois-trace Gram G = p I - 1 1^T on dimension p - 1 has spectrum
{1 (once), p (p - 2 times)}, normalized {1/p, 1 x (p - 2)}, with the
all-ones trace direction the eigenvector of the small eigenvalue.
Eigenvector identities and the determinant p^(p - 2) verified exactly
for p in {3, 5, 7, 11, 13}. Integer arithmetic only (fraction-free
Bareiss elimination for the determinant).

Evidence for registry claim ALPHA-SEED.

Run from the repository root:

```
python3 reproduce/alpha-exact-lemma/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 5/5 ALL PASS,
exit 0, no stderr.
