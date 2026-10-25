# Exact arithmetic storage for a fixed macrostep horizon

**NON-CANONICAL, L1. Conditional analytical candidate-T; no independent
acceptance.** Author: A. M. Thorn. License: Apache-2.0.

This appendix gives a finite-horizon storage upper bound for the exact
coefficient law of the complete v105 apparatus. It is an analytical
compatibility observation between that law and this finite-prefix note.
It is not a native gate construction or a precision certificate for the
spectral decoder and thermal couplings.

The arithmetic input is the public [#1771 dossier, comment
6396916409](https://github.com/mathorn1973/twist-j/issues/1771#issuecomment-6396916409),
specifically `PROOF.md`, **Exact scale and active memory for the complete
arithmetic step**, with SHA-256

    f7946237e6498cd7ff99ccee3253c10bc8645fe8bc8cbaf41fd6022cc235a8e9

Its Sections 1-2 supply the coefficient ring, gate order, complete integer
numerator and propagation radius. Its Sections 3-5 already establish the
primitive-scale law, local coefficient registers and sharp all-time
denominator growth. Those results are credited inputs, not new claims
here. The added statement is the explicit upper budget below for a
declared finite horizon and bounded arithmetic input. No scientific
program, stencil enumeration or expanded circuit was run for this proof.

## 1. Input type and the quantity being stored

Use the source's fixed power basis

    O=Z[t],   t=exp(i pi/10),
    t^8-t^6+t^4-t^2+1=0,   basis (1,t,...,t^7).

The configuration coordinate is q=(R,r,c) in Z^3, where c is the token
position y or pulse position x. At each q retain all

    d_internal=4(1+2)26^2=8112                         (A1)

internal coefficients: four object coins, one token arrangement or two
pulse banks, all 26 carrier labels and all 26 occupied-receiver labels.
This is the original configuration basis, not the spectral code basis of
[FINITE_PREFIX.md](FINITE_PREFIX.md).

Fix before evolution an integer N>=0, a finite set S0 of configurations,
an integer height bound H>=1, and an initial common denominator exponent
e0>=0. The admitted arithmetic inputs are

    b0=5^(-e0) a0,
    a0 in direct_sum_(q,internal) O,
    supp_q(a0) subset S0,    ||hat(a0)||_infinity<=H.   (A2)

Here hat replaces each O coefficient by its eight signed integer
coordinates, and the norm is the largest absolute integer coordinate.
Every fixed finite-support input over O[1/5] admits such a description by
clearing its finitely many denominators once. This does not give a finite
integer description for every complex input admitted by the separate
finite-prefix theorem. The zero arithmetic input is harmless; a normalized
Hilbert preparation requires b0 nonzero.

Put A=25 U_rec as in the cited proof, and retain the unprimitive integers

    a_n=A^n a0,    b_n=5^(-e0-2n) a_n,
    b_n=U_rec^n b0,                    0<=n<=N.        (A3)

There is no intermediate greatest-common-divisor operation or removal of
a common factor five. The representation in (A3) is sufficient for the
claimed horizon. If a normalized Hilbert vector is wanted, the one common
factor 1/||iota(b0)|| accompanies the entire preparation. It is independent
of n and is never chosen separately for a branch. Its value need not lie
in O[1/5]; the integer budget below is for a_n and its common exponent.

## 2. A uniform bound for the eight-coordinate stencil

For an O-linear operator B with finite rows, hat(B) is its real integer
coordinate matrix, with an 8-by-8 multiplication block for each O entry.
The infinity operator norm is the supremum of the absolute row sums of
this matrix. It is a coefficient-height norm, not the complex Hilbert
operator norm. Products and rational scalar factors respect this coordinate
representation, so the usual submultiplicative row-sum inequality applies.

First consider multiplication by any root t^k. In this field t^10=-1.
After reducing the exponent modulo 20, the only powers above the chosen
basis that must be expanded are

    t^8=t^6-t^4+t^2-1,
    t^9=t^7-t^5+t^3-t.

The remaining powers are basis powers, these two expansions, or their
negatives. Consequently every entry of the eight-coordinate multiplication
matrix of t^k belongs to {-1,0,1}. Each row has eight columns, giving

    ||hat(multiplication by t^k)||_infinity<=8.       (A4)

The following bounds use the exact factors of #1771, with their actual
order preserved. Identities on memory are implicit.

**Contact.** Outside contact ports, 5C is 5I. In a contact block its
active coordinate rows have one scalar diagonal entry 4, one scalar
entry of absolute value 1 in the same arrangement, and two entries of
the form +2i or -2i in the other arrangement. This follows by expanding
the source's normalized alpha and gamma vectors in

    5C=5I-2(P_alpha+P_gamma)
          +4(|gamma><alpha|-|alpha><gamma|).

The factors 1/2 in these outer products have canceled. Since i=t^5,
the triangle inequality and (A4) give, including the unaffected rows,

    ||hat(5C)||_infinity<=max(5,4+1+2*2*8)=37.        (A5)

**Object walk.** The integral coin numerator is

    (I+2iX) tensor (I+2iX)
       =I+2i(X tensor I+I tensor X)-4X tensor X.

Its coordinate norm is at most 1+2*8+2*8+4=37. Streaming is a coordinate
permutation. The output collision phase is either 1 or a root of unity,
and therefore has norm at most 8 by (A4). For the walk on both carrier
arrangements this yields

    ||hat(5 W_all)||_infinity<=8*37=296.              (A6)

**Carrier propagation.** Let R_all=I_token direct-sum V_pulse. On tokens,
5 R_all has norm 5. The source's pulse matrix is

    5V(k)=[[1-4 exp(ik), -2-2 exp(ik)],
           [2+2 exp(-ik), 1-4 exp(-ik)]].

These Fourier monomials are configuration shifts, not additional field
coefficients. Each spatial row has scalar absolute sum at most
1+4+2+2=9. Hence

    ||hat(5 R_all)||_infinity<=9.                    (A7)

The receiver calibration T is a coordinate permutation, including its
exchange of arbitrary carrier and old-memory labels. Its coordinate norm
and that of its inverse are one. The common phase exp(-i beta) is a root
of unity and contributes at most 8. The exact factorization is

    A=(1/5) T [exp(-i beta) (5 R_all)(5 W_all)(5C)] T*.

The cited complete-step cancellation proves that A itself has integral
O entries, despite the displayed factor 1/5. Using that identity only
for a norm estimate gives the explicit uniform bound

    kappa=max(1,||hat(A)||_infinity)
       <=(8*9*296*37)/5
       =788544/5 < 160000 < 2^18.                   (A8)

These estimates deliberately allow cancellations to be lost. They hold
for every row, including contacts, receiver crossings and both carrier
arrangements; no finite sample of rows is being used as a universal
certificate. Nor does this factorization declare its factors to be
permitted native arithmetic gates.

## 3. Height, support and exact current-state storage

Induction with (A8) proves at every declared macrostep boundary

    ||hat(a_n)||_infinity<=kappa^n H<=2^(18N)H,
                                      0<=n<=N.     (A9)

The source gives configuration propagation radius at most two in the
ell^1 metric. Therefore

    supp_q(a_n) subset S0+B_(ell^1)(2n),
    V_N=|S0+B_(ell^1)(2N)|<infinity.                (A10)

Here the plus sign is a Minkowski sum and B_(ell^1)(r) is the integer
ell^1 ball of radius r. No boundary condition, periodic wrap or spatial
truncation of the infinite operator is used in this inclusion.

Use signed-magnitude storage with one sign bit and sufficiently many
magnitude bits. The integer budget

    b_N=1+ceil(log2(H+1))+18N                        (A11)

suffices for every one of the eight coordinates, since

    ceil(log2(2^(18N)H+1))
       <=18N+ceil(log2(H+1)).

Fixing zero to have sign zero removes its redundant encoding if desired.
Allocating all internal slots throughout the cone in (A10) gives the
following conservative current-numerator storage bound:

    8*d_internal*V_N*b_N=64896 V_N b_N bits.         (A12)

For a simpler rectangular allocation, suppose S0 lies in a coordinate
box with integer side lengths L_R,L_r,L_c. Radius two alone permits the
safe allocation volume

    (L_R+4N)(L_r+4N)(L_c+4N).

The specified source factors give the sharper coordinate-wise inclusion
with volume

    (L_R+2N)(L_r+2N)(L_c+2N),                       (A13)

because one macrostep changes each individual coordinate by at most one.
Contact and calibration do not move coordinates. Formula (A13) can replace
V_N in a rectangular version of (A12); it is a separate support bound,
not a bound on the larger cone-set cardinality V_N as defined in (A10).

The common scale in (A3) can be stored as the integer exponent e0+2n,
using, for example,

    max(1,ceil(log2(e0+2N+1))) bits.                 (A14)

Storing the full decimal or binary expansion of 25^n is unnecessary.
When e0 and the schedule are hard-coded, the step counter determines
the same exponent. This is one common, unreduced scale; it does not
perform the nonlocal primitive normalization excluded in #1771.
Coordinate/address metadata, the allocation description and any program
or clock are additional resources to (A12)-(A14).

## 4. Macrostep and arithmetic implementation boundaries

The storage statement concerns the completed numerators a_0,...,a_N.
It does not assert that every intermediate factor C, W or V has the
same denominator, or that a partial microtick has the same register
budget. An implementation can use the integral full-step stencil A,
but its actual additions, constant multiplications, polynomial reductions,
carries and scratch still need a specified algorithm and inventory.

In particular, (A12) is not a bound for retaining all N+1 states at once,
and it contains no reversible arithmetic workspace, carry tracks, scratch
cleanup, input/output buffering or garbage history. The map a->Aa is
injective, but is not a permutation of a fixed bounded box of integer
strings. A finite reversible implementation must specify its time/scale
register, admitted ranges, overflow behavior, full raw completion and
inverse. A semantic bound on its intended trajectory does not supply
those operations on the remaining binary strings.

The coefficient stencil is local in the configuration q=(R,r,c). Its
8112 internal entries describe configurations of an object pair, carrier
and receiver; they have not been identified with independent material
registers at physical lattice sites. Increasing the digit length cannot
be assigned zero propagation time or one bounded physical tick. No
gate count, circuit depth, physical latency, energy cost, cooling cost,
reset cost or detector model follows from (A12).

All 26 occupied-memory labels are included in the bound. Operator
identities can still be tensored with identity on an arbitrary passive
reference. That does not describe the reference's unknown complex
amplitudes by finitely many integers. If one explicitly stores a finite
arithmetic reference basis as well, its coefficient multiplicity must
be counted separately; an arbitrary reference receives no such finite
classical-storage claim.

## 5. Relation to the finite quantum code and the next gate contract

The following quantities have different meanings:

- b_N bounds exact integer words for the restricted arithmetic family
  (A2) in the original configuration basis and only up to N.
- D in [FINITE_PREFIX.md](FINITE_PREFIX.md) is a Hilbert-space dimension.
  Its vectors may have infinite coordinate support, and its matrices
  depend on spectral projectors and Cayley compressions.
- d bounds an original-energy comparison and intrabin energy drift.
  It is not a bit precision for those projectors or matrix entries.
- The parameter k in [THERMAL_REALIZATION.md](THERMAL_REALIZATION.md)
  controls preparation defects and conditional output error for a device
  whose spectra and couplings are still specified exactly.

Neither a finite D nor a finite number of qubits supplies finite classical
descriptions of every state or coupling. In particular (A8)-(A14) do not
give an effective algorithm or certified accuracy for the spectral basis,
h_N, the load/decode matrices, thermal spectra or elementary rotation
angles. Their computability and robustness remain outside the supplied
coupling contract. The bit upper bound therefore does not turn the
thermal note's energy resolution into implementation precision.

A next native implementation must freeze the material digit carrier and
layout, its independently admitted gate alphabet, allowed carries and
controls, time/clock convention, input range, inverse and raw completion,
and one fixed reading that intertwines the entire active law. It must
also count preparation, workspace, occupied output storage and renewal.
Allowing gates merely because they calculate the desired answer does not
derive them from the original six-pentit update.

This corollary is compatible with #1771's exact denominator lower witness:
unbounded growth as N increases does not prevent a finite upper allocation
for a previously fixed N. It gives no approximation lower bound at fixed
nonzero tolerance and identifies no rational precision with thermodynamic
work. It neither duplicates the source's Borel-logarithm locality result
nor repairs the separate physical preparation and gate-admission gaps.

Falsifiers for this appendix are an incorrect factor order or row bound
in (A4)-(A8), a macrostep leaving (A9)-(A10), an omitted internal factor
in (A12), or an implementation/native claim exceeding the stated storage
contract. The derivation is authoring-session analysis, not independent
scientific acceptance of this appendix or of #1771.
