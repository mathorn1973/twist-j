# Exact finite certificate and arithmetic representation

**NON-CANONICAL. L1. Conditional analytical and computational work.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1786](https://github.com/mathorn1973/twist-j/issues/1786).
This derivation fixes what the prospective verifier computes. No result
of its first execution is assumed here.

## 1. Original source and finite necessary test

Keep U=U_rec, Q=E0 f(U), E0>0, f(exp(-i theta))=theta for
0<=theta<2pi, f(1)=0. The source of PR1777 at
`191ab035be823bd9d6fdc9effba81528fa026e49` is

    chi=|R=97,r=0,iB;c=97,token label0> tensor Xi,
    B=(e2-e3)/sqrt(2),
    psi_sigma=[I+sigma(U²-U^-²)]chi/sqrt(Z),
    sigma in {+1,-1}, Z=(39521+154sqrt(5))/15625.       (A1)

All 26 old-memory labels and arbitrary passive references are retained.
The physical encoding is I=Emb Gamma^(-1)D2*. Each source carrier is
in [95,99]. A physical term of diameter rho cannot move the carrier
between positions separated by more than rho: the removed and created
carrier subbanks must both lie in its support. Object and memory
subbanks cannot supply a missing carrier change. Compression against
a fixed data-independent ancillary ready state preserves this zero.

Let P_a project onto carrier positions outside [95-a,99+a]. With the
source action and local matrix-element limits defined,

    ||H_tilde Vpsi_sigma-VQpsi_sigma||/E0
       >= ||P_rho f(U)psi_sigma||.                    (A2)

The positive contraction b_ell(U), with
b_ell(z)=[(2-z-z^-1)/4]^ell, obeys
b_ell(U)P_(rho+ell)=P_rho b_ell(U)P_(rho+ell). Taking adjoints bounds
(A2) below by ||P_(rho+ell)b_ell(U)f(U)psi_sigma||. This changes
only a mathematical dual test; no physical source is filtered.

The exact calculation in
[PR1785 FILTERED_TAIL.md](https://github.com/mathorn1973/twist-j/blob/19f1c74a27684a22bf038c1e6fc1133f638fb613/notes/C-SOURCE-LOCAL-ENERGY-N/FILTERED_TAIL.md)
gives coefficients, for |n|>ell,

    c_n=-i(-1)^ell(2ell)! /
         [4^ell(n-ell)(n-ell+1)...(n+ell)].

The uniform tail after |n|<=N+ell is

    r_(ell,N)=2^(1-2ell)(2ell-1)!/[(N+1)...(N+2ell)]. (A3)

The positive and negative tails telescope. Central terms, including
every pi coefficient, vanish after projection by finite propagation.
Fix rho=2, ell=2, N=8 and P=P_4=1_(c<=90 or c>=104). Then

    v_sigma=(-3i/2) sum_(n=5)^10
                P(U^n-U^-n)psi_sigma /
                [(n-2)(n-1)n(n+1)(n+2)],
    r=1/15840,
    ||H_tilde Vpsi_sigma-VQpsi_sigma||/E0
         >= ||v_sigma||-r.                           (A4)

A sufficient certificate is therefore

    ||v_sigma||² > tau²,
    tau=1/1200+1/15840=71/79200.                      (A5)

Both signs are fixed and reported separately. Failing (A5) is
inconclusive about physical existence. All squared quantities in (A5)
are nonnegative, so the strict squared comparison is equivalent.

## 2. Calibration and reference invariance

The receiver law is U_rec=T(U_uncal tensor I)T*. Its position-dependent
carrier/memory exchange T fixes chi and commutes with P_a. Thus (A4)'s
norm equals its uncalibrated fixed-label norm tensored with Xi. This
retains every memory/reference correlation; it does not assert that
arbitrary comparator errors are independent of memory. One fixed
carrier label is sufficient for the exact norm calculation.

## 3. Internal arithmetic coordinates

Conjugate the object coin by G=diag(1,i,i,1) for computation only;
arithmetic amplitudes are G* times the physical coordinate amplitudes.
This diagonal unitary preserves every position projection and norm.
It is not a changed physical encoding or a preparation resource.
It takes sqrt(2)chi to the integer seed e2-e3; the contact vectors
become B token and A pulse-bank1, A=(e1-e4)/sqrt(2). The real coin is

    5G* M2 G =
       [ 1 -2 -2 -4 ]
       [ 2  1 -4  2 ]
       [ 2 -4  1  2 ]
       [-4 -2 -2  1 ].                              (A6)

The contact C' keeps the real rotation with columns (3/5,4/5) and
(-4/5,3/5) on (B token,A pulse-bank1). The coin fixes both vectors,
so

    (G*M2G)C'=(G*M2G)+(C'-I).                        (A7)

The combined factor has integer numerator and denominator five.
The pulse step has numerator

    5V(z)=[[1-4z^-1,-2-2z^-1],[2+2z,1-4z]],         (A8)

where z means right translation; its token numerator is 5I. Object
streaming, phase zeta5^-1 at output r=0, and global phase zeta5^-2
complete the step. Thus A=25G*U_uncal G is integral over Z[zeta5].
Its adjoint reverses all stages, transposes real numerators, reverses
translations and conjugates phases. In particular the inverse phase
uses the input r, while inverse contact is tested after reverse
streaming and pulse propagation.

For k>=0 let w_k=A^k chi0, and for k<0 let w_k=(A*)^(-k)chi0,
where chi0=e2-e3 is at (97,0,97) in the token arrangement. Then, in
these arithmetic coordinates,

    U^k chi=w_k/[sqrt(2)25^|k|].                    (A9)

The largest required seed power is 12. Every forward and backward
source term is retained. Common integer denominators produce one
integer cyclotomic vector, whose squared norm is divided by that
denominator squared and 2Z. The common unit phase -i in (A4) may be
omitted from this norm only, not from a claimed energy matrix element.

## 4. Exact field reduction and ordering

Represent coefficients in the basis 1,zeta5,zeta5²,zeta5³, reduced with
1+zeta5+zeta5²+zeta5³+zeta5^4=0. Multiplication and conjugation are
exact. Each squared norm is a real element of Q(zeta5), hence lies
in Q(sqrt(5)). Reality of a0+a1zeta5+a2zeta5²+a3zeta5³ forces
a1=0 and a2=a3. Since zeta5²+zeta5³=-(1+sqrt(5))/2, its value is

    [(2a0-a2)-a2sqrt(5)]/2.                         (A10)

The verifier evaluates norms directly in this quadratic basis and
checks the reduction identity on fixed arithmetic test inputs.
Division by the positive Z stays in that quadratic field. The sign of a+b sqrt(5)
is decided by rational coefficient signs; if they oppose, compare
a² with 5b². Irrationality of sqrt(5) handles equality, with the zero
element treated separately. No floating point or numerical square
root is needed.

Integrity checks and immutable outputs are specified in
[PREREG.md](PREREG.md). Successful arithmetic execution need not
satisfy the scientific sufficient threshold and does not establish
independent acceptance of the inherited conditional premises.
