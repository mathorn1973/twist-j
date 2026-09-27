# Result: all-contact quarter-turn single-cycle contribution

**PUBLIC, NON-CANONICAL. No Canon promotion.**
Owner: #1192. Author: A. M. Thorn. Date: 27 September 2026.
License: Apache-2.0.

## Disposition

**candidate-T, pending separate mathematical review:** the written proof in
PROOF.md establishes an exact straight-contact ribbon decomposition and a
volume-uniform bound for the selected one-copy signed moment. The selection
requires a component current to be exactly one unit simple cycle, with m
edges and c turns satisfying 4c<=m. All opposite-edge contacts, of either
sign, are admitted. No product or prism representation is required.

**candidate-C:** the first frozen finite audit passed on one Linux x86_64
lane, using integer and Fraction arithmetic only. Pin:
`a5c5fc5045eeb0bf30c0de1821e8d03366324231`.
The exact output and custody hashes are in RUN.md.

## Evaluated bound

With

    A=4913/4096,
    q=741863/819200<1,
    T_R(q)=sum_(m>=R) m^3 q^(m-1),

PROOF.md gives, for every admitted even finite torus,

    Xi_quarter(L) <= C_quarter := (A/64) T_16(q) < 1194.

The reduced rational C_quarter is printed in RUN.md. The displayed integer
ceiling is a coarse evaluated consequence, not an optimized physical number.
The same argument gives the uniform long-cycle tail

    Xi_quarter,>=R(L) <= (A/64) T_R(q), R>=16,

which tends to zero independently of volume. No Fourier/volume limit exchange
is made.

The counting step is W_m(e)<=A q^(m-1), applied separately to each of all 4V
root edges. It does not equate orientation-specific slice expectations.
The deterministic estimate ell<=n0*n1/4<=m^2/16 explicitly periodizes a
closed lift, including when it spans more than one period.

## Contact skeleton and strict examples

Every simple zero-winding cycle has reinforcing opposite contacts partitioned
into maximal straight two-strand ribbons with

    O_+=sum_alpha d_alpha,    number_of_ribbons<=6c.

This is not a global prism-extraction or coverage theorem.
The L-strip family for every n>=5 has

    m=4n+4, c=6, O_+=2n, O_-=0, ell=2n+1,

and is inside the new class but outside the earlier signed-contact sufficient
class. Its nonrectangular two-axis support is outside the specific previously
declared fixed-displacement ribbon and complementary product-prism families.
No classification of every possible broader prism definition is asserted.

## What was audited

The frozen program checked 31 local sign patterns, 2145 quarter-turn integer
pairs, exact weighted direction transfer through length 10, 93 prescribed
cycles, 186 periodic embeddings, 2232 ordered observation-axis pairs, nine
synthetic multiple-period primitive profiles, and the generating-series and
tail identities at their preregistered finite ranges. The L-strip examples
covered n=2,...,20. These finite examples audit the proof; they are not an
exhaustive enumeration of the full measure or an independent proof.

## Open boundary

Full Xi_L and Xi_L^(2) remain open. This result controls a nonnegative part
of Xi_L; it is not a bound on the full susceptibility chi_L. High-turn cycles,
components with multiple current cycles, and non-simple current networks are
not disposed of by this result. P1 still needs its positive macroscopic
comparison. Public Canon v92, its registry, frontier, gates and release are
unchanged.
