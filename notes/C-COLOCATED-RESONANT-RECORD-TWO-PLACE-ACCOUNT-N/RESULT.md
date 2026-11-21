<!-- SPDX-License-Identifier: Apache-2.0 -->

# Result and finite scope

**NON-CANONICAL / L1.** Proposed analytical status: candidate-T.
Finite evidence: candidate-C on one x86_64 architecture.
Read PROOF.md together with ERRATA.md.

Both unchanged scripts complete their mathematical checks with exit zero and
empty stderr. They produce identical raw Windows stdout. The stored LF
outputs match after explicit CRLF-to-LF normalization; direct byte comparison
fails in this environment. RUN.md records that distinction.

| Block | Conditional result | Finite audit scope | Reported checks |
| --- | --- | --- | ---: |
| A1 | Conjugate trace formulas and their sum; the two terms are equal iff B=0 | 625 seeds; 49 have B=0 | 6258 |
| A2 | Second-contact admission together with signal/field return iff a=Jc; exact helper-to-record partition | 6480 pairs, 38 resonant; 624 additional nonzero resonant seeds; 64800 forward/inverse cuts | 418503 |
| A3 | Five-channel bank works for all five resonant inputs iff c is outside 2O | 225 nonzero coset products; 81 odd seeds and their 81 doubles; 40500 forward/inverse cuts | 245088 |
| A4 | Correct seed (-1,-2,-2,0), helper drop 55 to 20 and record quantum 35 | Five phases and the two-selector port on its two declared inputs | 9 |
| A5 | Constant-quantum record shares equal count shares | 81 odd seeds, 12 count profiles, 4860 channel comparisons | 5346 |
| A6 | Dead-time lock, occupied-record backreaction and free-mode denominator obstruction | 405 blank-repeat cases; 405 occupied-repeat cases; two modes through n=25 with four primitive polarization fixtures | 1260 |

Total reported checks: 676464. Total audited primitive cuts: 105300.
The odd-seed inventory is the 80 nonzero elements of {-1,0,1}^4 plus
(-1,-2,-2,0). The even witnesses show disturbance of the first off-target
helper at input phase m=1, channel k=0; no claim that failure occurs only
at that phase is made.

The A4 calculation tests the selector port, not the complete predecessor
paths. The A5 count profiles are algebraic aggregates of separately prepared
single arrivals, not a simulated autonomous recharging detector.

## Boundaries

For each fixed odd seed, the deposited record quantum is
$w_0=5(A_c+B_c)$. Its source is the prepared helper:
$Q(h_0)=17A_c+B_c$ and $Q(h_1)=12A_c-4B_c$.
Repeat operation requires record isolation and helper recharge or replacement
of the prepared apparatus. Signal return does not provide a free energy
source.

The all-n denominator assertion belongs to the analytical argument;
the executable denominator audit is bounded by n=25. The two modes are
declared inputs, not a derived physical selection.

No Born occurrence law, autonomous native-U realization, action-scale
selection or ALPHA-FORM derivation is established. Public preparation,
repository checks and model consultation do not promote this note.
