# Fixed-edge crossed current under independent source and phase codes

Use the unchanged native H3 rule on a 16 by 8 torus with initial matching bit zero. Set L = 1 - rho, h(w) = w times its conjugate, and theta = h(J) = 2 - phi. Use the real trace for scalar Q. Write nu for the coefficient of phi in a Hermitian account.

Measure both edges in column 2, with fixed coordinate directions 0 to 1 and 4 to 5. The two row bands start at y = 0 and y = 4. Install antipodal matter gaps (a, a, L, L) at (y - 1, y, y + 1, y + 2) in each band, modulo 8, with zero radiation. Let s = 1 in the first band and s = -1 in the second. Set n(1) = 1 and n(-1) = 3. The independently set probe phase code p = +/-1 chooses a = -p*s*n(s)*J^(s+1). The two phase codes have the same support, identical sitewise Hermitian accounts on each rail, and the same complete probe H = 72 - 4*phi, Q = 140, nu = -4. Their contrast reverses the resident gaps while retaining both receiver gaps.

For each band install a primary two-by-two emitter in rows y and y + 1. Its starting column is 0 when incident and 12 when distant. A complementary emitter in that band starts in column 6. At each emitter cell use words (d, -d, 4, -4), with d = 4*u for source code q = -1 and d = 4/u for q = 1, where u = j + 1/j. The primary tiles share q and the complementary tiles take the opposite code. These positions stay fixed across the four fully incident arms. All unspecified sites start at zero. The full paid ledger in each arm and control is M = U = 0, H = 1352 - 4*phi, Q = 2700.

In the target column, the 1C pairs (0,1), (2,3), (4,5), and (6,7) refuse. Each compares L to a resident of residue J^(s+1) modulo 2. These are distinct because L has residue J and J has odd order greater than one. At 2C the vertically matched pairs (7,0), (1,2), (3,4), and (5,6) compare equal launch gaps. The target has no CLK through 2C, and the CORR input at 2C is confined to rows 0, 1, 4, and 5. Accordingly rows 2, 3, 6, and 7 retain their launch gaps through 2B. At 3C the seam pairs (2,3) and (6,7) again refuse by the same residue comparisons.

Before 2B the two receivers keep gap L for either phase code. An incident tile delivers CORR = -2*L*J^(-q) and selects B1 if q = -1 or B2 if q = 1 at the receiver. The neighbor at y remains B0. Its field-to-material gap norm ratio has rational norm 5 in the first band and 5/81 in the second. Either active resonance requires rational norm 1. The distant tiles give zero CORR and B0 at this cut. At 3C a measured edge admits exactly when its band is incident and s = -q. The residues J^(-1), 1, and J are distinct, so the two B outputs and the no-signal receiver gap give distinct parity comparisons with the resident.

Score the increase in receiver material H from 2B to 3C, with the opposite change on the partner. Its trace is the oriented material Q current. On an admitted edge the before pair is (a,b), with b = J^s*L. The receiver becomes b' = (L*a + J*b)/2 = (1 - p*s*n(s))*J*b/2. The signed scalar read is 2*Tr(h(b') - h(b)). Preregister the individual currents and their fixed unit-weight sum for the fully incident geometry.

| Source q | Probe phase p | 0 to 1 | 4 to 5 | Sum |
| --- | --- | ---: | ---: | ---: |
| -1 | -1 | +10 | 0 | +10 |
| -1 | +1 | -10 | 0 | -10 |
| +1 | -1 | 0 | -10 | -10 |
| +1 | +1 | 0 | +20 | +20 |

The sum has sign q*p and the magnitudes shown in the table. A single edge gives a nonzero signed reversal when the phase code changes at its admitted source orientation. Changing the source sign selects the other edge. The fully distant control must give zero on both edges. The two partial controls each retain only one incident tile and must retain just its individual entry above. Score the exact incident words and B tags, parity, material words on both edge endpoints, and all scalar currents. Audit both native inverses, the full ledger at every cut, the composed terminal inverse, and Hermitian conservation on both measured edges.

A simultaneous global reversal of both matter rails at every site, or of both radiation rails at every site, commutes with the native step. At C any matched difference changes by a common sign or stays fixed. The parity guard is unchanged and the linear map commutes with the reversal. At B both norm guards are unchanged, and the sector's center and gap reverse together. The quadratic edge currents are invariant under either reversal. Check all intermediate cuts, branch tags, and signed currents under each global sign reversal in the four fully incident arms.

The crossed currents measure a finite two-edge comparison under a source code and a programmed probe phase. Both probe preparations have identical signed Hermitian accounts. The comparison differs from the independently crossed Hermitian sign test in [#2034](https://github.com/mathorn1973/twist-j/pull/2034), where the opposite probe sign code was silent. A mismatch of the table, the control outcomes, or the declared exact native words falsifies this prepared current fixture. A probe force under independent charge reversal and a conserved momentum exchange remain separate tests.
