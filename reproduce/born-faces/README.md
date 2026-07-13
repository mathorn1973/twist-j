# Abelian face weights witness

The five abelian face weights w(k) = |1 + zeta_5^k|^2, exact in
Q(sqrt5) inside Z[zeta_5]: w(0) = 4, 2 w(1) = 3 + sqrt5,
2 w(2) = 3 - sqrt5, conjugate symmetry, total mass 10, the sigma_2
Galois pairing w(1) to w(2), and the tilt
w(1) + w(4) - w(2) - w(3) = 2 sqrt5 (normalized tilt sqrt5 / 5).
Integer arithmetic only, with sqrt5 = 1 + 2 (zeta_5 + zeta_5^4).

Evidence for registry claim BORN-FACE-WEIGHTS.

Run from the repository root:

```
python3 reproduce/born-faces/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 8/8 ALL PASS,
exit 0, no stderr.
