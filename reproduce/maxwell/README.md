# Maxwell closure witness

The classical Maxwell closure of the decoder, chain exact and weight
free, in exact integer arithmetic: integer chains on finite
complexes, an integer Smith normal form, and F_5 elimination. No
floats anywhere. Symbolic identities are carried as exact linear
algebra: each edge or face symbol is a basis vector of an integer
coordinate space, so an identity in 32 or 96 symbols is a vanishing
integer vector.

Verified: on the 3+1 tesseract (16 vertices, 32 edges, 24 faces, 8
cubes) the Bianchi identity dF = d(dA) = 0 holds identically in the
32 edge symbols and gauge invariance F[A + d Lambda] = F[A] is an
identity in 16 more vertex symbols; on the closed 2 x 2 x 2 spatial
torus, Gauss is the boundary equation with all seven Smith divisors
equal to 1, a constructive two edge dipole, the integrated law on
every one of the 256 vertex regions, and the Z_5 obstruction counted
in p (solvable iff the total charge vanishes mod 5, with a
constructive solution and an exhibited obstruction); on the 2^4
spacetime torus (16, 64, 96), conservation bd1 bd2 = 0 is an exact
integer identity in the 96 face symbols, the Smith form of the face
boundary has all 45 divisors equal to 1 so H_1 is free of rank 4,
the four winding certificates annihilate the face boundary and pair
with the elementary winding currents as the identity, the single
winding current is Z_5 obstructed while five parallel windings are
solved, and the exact rank identity 45 = 64 - 19 closes the iff: the
current pair is solvable in the Z_5 theory iff the current is
conserved and all four winding numbers vanish mod 5.

Evidence for registry claims MAXWELL-BIANCHI, MAXWELL-GAUSS-CHAIN,
MAXWELL-AMPERE-CHAIN, MAXWELL-OBSTRUCTION-P, MAXWELL-CLOSED. Check
map: 01 and 02 MAXWELL-BIANCHI; 03 and 04 MAXWELL-GAUSS-CHAIN; 05,
09, 10 MAXWELL-OBSTRUCTION-P; 06 to 08 MAXWELL-AMPERE-CHAIN; 01 to
10 together witness the MAXWELL-CLOSED dictionary reading.

Run from the repository root:

```
python3 reproduce/maxwell/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 10/10 ALL PASS,
exit 0, no stderr.
