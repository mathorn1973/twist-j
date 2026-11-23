# C-RH-SEMISTABLE-FRAME-N, rounds 8 through 10

**NON-CANONICAL. No authority. No Canon status changes.**

Claim: [issue 2070](https://github.com/mathorn1973/twist-j/issues/2070).
Alias used in the earlier discussion: C-RH-BK-CONCENTRATION-N.

## Round 10 outcome

Candidate-D: the actual split word-prime compact orbit has only two Gram
eigenoperators. For r_S>0, after the complete Fourier coefficient, its
rank is exactly (q^k-1) times the visible input dimension, with the product
formula over split places. This is a statement about the full Fourier
function, before selected restrictions and period integrals.

Candidate-D: a spherical ambient local type with Satake height-interval
count below 2*r_S+1 at one suitable split place has zero Bessel Jacquet
module for every word. A
concrete noncharacter unitary spherical local example is therefore blind
despite full compact orbit rank. Its occurrence in the global target is
not inferred.

Candidate-D: coarse-level counting bounds the all-old source fraction by
(k/(T_u^k-1))^f and gives an explicit deletion budget. The actual character
normalization and distinct evaluation orbits prevent two false reductions.

Candidate-C: both blind, separately authored programs passed every fixed
first-run test: 920 orbit pairs, 21,614 lattice-neighbor pairs, 35 Gram
cases, four complete finite groups and 647 target subspaces. One x86_64
architecture only. The actual selected global period-rank bound remains open.

- [Round 10 proof and scope](round10/PROOF.md)
- [Round 10 source map and primary references](round10/SOURCE_MAP.md)
- [Round 10 first-run results](round10/RESULTS.md)
- [Round 10 development and opposition review](round10/REVIEW.md)
- [Round 10 preregistration](round10/PREREG.md) and [custody](round10/CUSTODY.md)
- [Round 10 verifier](round10/verify_r10.py) and [blind opponent](round10/break_r10.py)

Round 10 execution pin: e4b7ee04b10e227fa7362b6578c9046dd1613b22.
All prior frozen scientific evidence is unchanged.

## Round 9 outcome

Candidate-D: in the concrete primitive split Hida realization, the actual
word-prime level is conjugate to K_1 of exponent one. Every irreducible
local constituent has zero fixed space for conductor at least two, dimension
one for conductor one, and an exact Satake-interval count between one and k
for conductor zero. This does not require genericity.

Candidate-D: a family with exact pairwise Gram bounds, exact Hecke balance,
literal finite-group averaging, independent raw seeds and injective Fourier
projections in the active orbit still has defect (1-rho)*sqrt(sigma)/2.
These properties alone cannot give a uniform o(sqrt(sigma)) estimate.
The actual source's diagonal bound already gives kappa<=e0 exponentially.

Candidate-C: both separately authored, prospectively frozen programs passed
all round 9 checks on one x86_64 architecture. The actual exponential
intrinsic period-rank improvement remains open.

- [Round 9 proof and precise scope](round9/PROOF.md)
- [Round 9 source map and primary references](round9/SOURCE_MAP.md)
- [Round 9 first-run results](round9/RESULTS.md)
- [Round 9 opposition and dispositions](round9/REVIEW.md)
- [Round 9 preregistration](round9/PREREG.md) and [custody](round9/CUSTODY.md)
- [Round 9 development program](round9/verify_r9.py) and [blind opponent](round9/break_r9.py)

Round 9 execution pin: b83250a7db82d2a27de932617fb39f61cf6af823.
The round 8 frozen programs, contract and first-run evidence below are unchanged.

## Round 8 outcome

Candidate-D, conditional on the explicit geometric and counting premises:
the one-prime Hecke decomposition has exactly balanced source dimensions
and exponentially controlled target dimension imbalance. The source's
chosen full PMat witness and a fixed SIso transport this conclusion to the
actual full Poincare-map completion, rather than merely its good rows.

Candidate-D: raw seeds are jointly independent in the stated positive-rank
flag setting, although their unipotent characters belong to one rational
conjugacy class. The remaining concentration is exactly a question about
relations created by periodization on products of source subspaces.

Candidate-D: a finite high-rank Kronecker matrix certifies an upper bound
for a positive concentration defect. A genuine finite-group averaging
example has exact defect 1/6 despite raw independence, individual
injectivity and full target span.

Candidate-C: both prospectively frozen, separately authored programs pass
the finite audit on one x86_64 machine. A misleading stdout label is
retained and explicitly corrected in RESULTS.md.

The actual intrinsic period-rank bound remains open. No RH conclusion,
joint two-prime balance, Lean verification or Canon promotion is claimed.

## Round 8 package

- [Proof and exact assumptions](PROOF.md)
- [Source map and literature](SOURCE_MAP.md)
- [Prospective finite audit contract](PREREG.md)
- [Results, hashes and output-label erratum](RESULTS.md)
- [Same-session opposition and dispositions](REVIEW.md)
- [Development verifier](verify.py) and [blind opposition program](break.py)
- [Development stdout](verify.stdout.txt) and [opposition stdout](break.stdout.txt)
- [Promotion handoff](PROMO-C-RH-SEMISTABLE-FRAME-N.md)

The frozen execution commit is
72ff97914a1b56ad616d8e603d9776364ae90968.
Any later rerun is reproduction, not another first run or independent
confirmation. The accompanying JSON files preserve the actual first runs.
