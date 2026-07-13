# Kernel witness

Fifteen exact checks of the axiom facts in Z[zeta_5], integer
arithmetic only: J = 1 + zeta_5^2 is a unit (N(J) = 1, Tr(J) = 3), the
golden bridge J phi = j, the cube law (J - 1)^3 = j, the fifth power
J^5 phi^5 = 1, the integer step matrix, the modulus chord
J Jbar = 2 - phi = phi^-2, the tenth root 1 - J, and the ramified
chord N(1 - zeta_5) = 5.

Evidence for registry claims J-UNIT, J-GOLDEN-BRIDGE, J-STEP,
J-MODULUS-CHORD, J-TENTH-ROOT, J-RAMIFIED-CHORD.

Run from the repository root:

```
python3 reproduce/kernel/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 15/15 ALL PASS,
exit 0, no stderr.
