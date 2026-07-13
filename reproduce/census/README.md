# Kernel census witness

The full attractor census of the Thue-Morse driven kernel on Z_5^6,
by complete enumeration of all 15625 seeds (warmup 400 ticks, window
300): exactly 313 attractors, 312 of size 20 with basins of 50 and one
singlet of size 10 with a basin of 25; disjoint attractor support of
6250 states; full basin coverage; 313 = 13^2 + 12^2. Every recurrent
state lies on the z5 sheet {1, 4} and the selection law fires only the
mirror generators b, d, e there. The piston pairing (b4 d4 on pistons,
identity on the fiber) is an involution on the 313 attractors with 144
transpositions and 25 fixed points (24 of size 20 plus the singlet),
so classes modulo the pairing number 169 = 13^2. The return group
`H_1 = <d, b e b>` has order 10, d(b e b) is the line translation
T_0 = (0, 0, 0, 0, 3, 2), and for every attractor A there is a chosen
representative x_A in A with exact two-coset formula
`A = H_1 x_A union b H_1 x_A`. Two closure properties back the word
attractor: every signature is closed under both one step transitions
(drive bit 0 and drive bit 1), and the next independent 300 tick
window reproduces every signature exactly. Integer arithmetic only;
the generator
relations a^2 = b^2 = c^2 = d^2 = e^2 = id and (bc)^5 = id are checked
on all states.

Evidence for registry claims CENSUS-313, CENSUS-Z5-SHEET,
CENSUS-PAIRING, CENSUS-HOSTING.

Run from the repository root:

```
python3 reproduce/census/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 11/11 ALL PASS,
exit 0, no stderr.
