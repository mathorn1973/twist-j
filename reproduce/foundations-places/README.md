# Foundations and places witness

The foundations of the decoder section and the two arithmetic places,
in exact arithmetic: integers, rationals, Q(sqrt5) pairs, the
cyclotomic rings Z[zeta_5] and Z[zeta_8], Gaussian integers, and F_25
as pairs over F_5. No floats anywhere.

Verified: the internalized counter (the drive bit is the parity of a
2-adic odometer register, with the exact recursions t_2n = t_n and
t_2n+1 = 1 - t_n and the carry parity law, checked exhaustively below
2^13 and matched over a long window by the local carry rule alone:
one autonomous closed map); the self similar time quantum tower on
Z/5^k for k = 1 to 4 (T^(5^k) = i_5 I, the scalar of exact order 4
with i_5 = 2 mod 5, period exactly 4 x 5^k by direct order search);
the degree split by prime ((2 phi - 1)^2 = 5 in Z[zeta_5],
(m + m^-1)^2 = 2 and m^2 = i in Z[zeta_8], and neither sqrt2 nor i in
Q(sqrt5), the unique quadratic subfield of Q(zeta_5)); the Z2 family
split (exactly one involution in the cyclic Galois group at zeta_5,
the complete Klein four at zeta_8, and 5 = (2 + i)(2 - i) in Z[i]
with conjugation swapping the two Gaussian primes); the bilocation of
i (the order 4 element 2 of F_5* and zeta_8^2); and the silver
sibling (m = sqrt(i), the silver unit 1 + sqrt2 of norm -1, and
inside F_25 = F_5(sqrt 2) the element tau with tau^2 = 2, the image
of J at the ramified place, tau^4 = -1, ord(tau) = 8, F_25* cyclic of
order 24 by full order census).

Evidence for registry claims ODOMETER-INTERNALIZED,
TIME-QUANTUM-TOWER, DEGREES-BY-PRIME, Z2-PLACES-SPLIT, I-BILOCATED,
SILVER-SIBLING. READING-SPLIT is carried inline in the Canon (each
leg separately registered and witnessed elsewhere);
CURVATURE-TRACE-VALUE stays a live open row and nothing here claims
it; the all k time quantum statement stands at the sealed internal
scope, this witness computes k = 1 to 4 only. Check map: 01
ODOMETER-INTERNALIZED; 02 TIME-QUANTUM-TOWER; 03 DEGREES-BY-PRIME; 04
and 05 and 06 Z2-PLACES-SPLIT (04 also carries the unique quadratic
subfield clause of DEGREES-BY-PRIME); 07 I-BILOCATED; 08
SILVER-SIBLING.

Run from the repository root:

```
python3 reproduce/foundations-places/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 8/8 ALL PASS,
exit 0, no stderr.
