# A finite dual certificate for the remaining carrier-tail question

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1784](https://github.com/mathorn1973/twist-j/issues/1784).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`a07b8909d2926e223549433528a189a80d14bc09`.
Independent scientific acceptance is not asserted.

The diameter-one question has a separate analytical answer in this
package. This appendix supplies a finite, explicitly bounded dual test
that could address the remaining diameter-two question. No value of the
test has been computed, and no passing diameter-two obstruction is
claimed. Its general lemma is valid for integer diameter rho>=1.
Execution would require a separately frozen executable and public
readback; the formulas here do not constitute an executed gate.

## 1. The fixed source and a coarse forbidden projection

Keep the Public Canon v105 occupation encoding at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, the positive logarithm of
PR1772 at `3abf054e435e31c51e6e50528b09fe3cf7cffe13`, and the actual
source of PR1777 at `191ab035be823bd9d6fdc9effba81528fa026e49`:

    U=U_rec, Q=E0 f(U), E0>0,
    f(exp(-i theta))=theta, 0<=theta<2pi, f(1)=0,
    psi_±=[I±(U²-U^-²)]chi/sqrt(Z),
    chi=|R=97,r=0,iB; c=97,token label 0> tensor Xi,
    Z=(39521+154 sqrt(5))/15625.                    (T1)

The frozen successor PR1783 is
`9e765fcef4c9e4917c25a49eebce8f052fc9a961`. Its cut-mass bound is
not required by the proof below. In particular this proof does not use
a fitted density or a new source with its near-cut part removed.

Let c denote the carrier position: y for a token and x for a pulse.
Both U and U* change c by at most one. The contact changes carrier
type only at the same site, tokens do not stream, pulse propagation
has displacement at most one, and receiver calibration changes labels
only. Consequently both sources in (T1) are supported in the interval

    I=[95,99].                                    (T2)

This is a sufficient common interval, not a claim that every carrier
position or every configuration in it has nonzero source amplitude.
For an integer a>=0, write I_a=[95-a,99+a], and let P_a be the
orthogonal projection in the original code onto c outside I_a, with
identity on the other coordinates, labels and references.

Consider any admitted sum of physical terms of diameter at most rho.
A coded matrix element between carrier positions c and c' vanishes
when |c-c'|>rho. Indeed the nonzero carrier code at c must replace
carrier vacuum, and the nonzero code at c' must become vacuum. A term
must include both sites. The carrier coordinates h5,...,h16 are
disjoint from the object and receiver coordinates, including when
their physical sites coincide. This argument permits either carrier
type and all labels. The occupation gauge is diagonal and receiver
calibration preserves c, so neither changes the support zero.

Thus P_rho is a valid coarse forbidden projection on this source. It
need not exhaust the configurations forbidden by physical geometry.
For the bare isometry V, including any fixed ancillary ready state
allowed by the contract, compression and the support zero give

    ||H_tilde V psi - V Q psi||
       >= E0 ||P_rho f(U) psi||.                  (T3)

Here psi is either actual source in (T1). For infinite sums this uses
the contract's domain and matrix-element convergence requirements.
Ancillary entanglement in a fixed ready state does not enlarge the data
support of a compressed term. Positivity and charge conservation are
not needed for this necessary bound.

## 2. A centered filter acts only on the dual test

For an integer ell>=1, define

    b_ell(z)=[(2-z-z^-1)/4]^ell,
    B_ell=b_ell(U),
    g_ell(z)=b_ell(z) f(z).                        (T4)

On the circle b_ell(exp(-i theta))=sin^(2ell)(theta/2), so B_ell is
a positive contraction. Its Laurent degree is ell, while its zero at
the cut has order 2ell. Finite carrier propagation implies

    B_ell P_(rho+ell)=P_rho B_ell P_(rho+ell).

Taking adjoints and using ||B_ell||<=1 proves

    ||P_rho f(U) psi||
       >= ||P_(rho+ell) B_ell f(U) psi||
       =  ||P_(rho+ell) g_ell(U) psi||.            (T5)

Equivalently, every vector B_ell eta with eta in the deeper projected
space is an admissible forbidden dual vector, of norm at most ||eta||.
Equation (T5) takes the strongest such dual test without selecting a
particular coordinate ket. It does not physically filter, reprepare or
replace psi, and the compared energy remains the original Q.

## 3. Exact coefficients and an operator-norm remainder

Write the finite filter coefficients as

    b_ell(z)=sum_(j=-ell)^ell b_j z^j,
    b_j=(-1)^j binom(2ell,ell+j)/4^ell.

The Fourier coefficients of the specified sawtooth are a_0=pi and
a_n=-i/n for n!=0, in the convention z=exp(-i theta). Therefore all
coefficients c_n of g_ell are specified by

    c_n=pi b_n - i sum_(j=-ell,...,ell; j!=n) b_j/(n-j),
    b_n=0 when |n|>ell.                           (T6)

This includes the central pi terms and all their signs. For |n|>ell,
the finite-difference identity

    sum_(j=0)^m (-1)^j binom(m,j)/(x+j)
       = m!/[x(x+1)...(x+m)]

gives the simpler formula

    c_n= -i (-1)^ell (2ell)! /
           [4^ell (n-ell)(n-ell+1)...(n+ell)].     (T7)

The identity follows by partial fractions and holds whenever none of
the denominators vanishes. In particular c_-n is the complex conjugate
of c_n. The coefficients in (T7) are absolutely summable. Their Fourier
series is g_ell everywhere: multiplication of the sawtooth by b_ell
gives the coefficients (T6), and g_ell is continuous at the cut with
g_ell(1)=0. The assigned value f(1)=0 is therefore preserved even if
the spectral measure has an atom there.

For N>=1, set

    g_(ell,N)(z)=sum_(n=-N-ell)^(N+ell) c_n z^n.

The paired tails of (T7) telescope, giving

    ||g_ell-g_(ell,N)||_infinity <= r_(ell,N),
    r_(ell,N)=2^(1-2ell) (2ell-1)! /
                       [(N+1)(N+2)...(N+2ell)].   (T8)

For example, the positive tail is proportional to
sum_(k=N+1)^infinity 1/[k(k+1)...(k+2ell)]. Subtracting the adjacent
products of length 2ell evaluates this sum as
1/[2ell (N+1)...(N+2ell)]. Doubling and inserting (T7) proves (T8).
This is a uniform scalar, hence operator-norm, bound. It requires
neither the large Fejer approximation degree nor any spectral estimate
near the cut.

## 4. A finite algebraic certificate

Define the finite vector

    v_(rho,ell,N;±)=P_(rho+ell) g_(ell,N)(U) psi_±.

Combining (T3), (T5) and (T8) yields

    ||H_tilde V psi_± - V Q psi_±|| / E0
       >= ||v_(rho,ell,N;±)|| - r_(ell,N).         (T9)

By (T2), P_(rho+ell) U^n psi_±=0 for |n|<=rho+ell. All the central
terms of (T6), including every pi term, vanish in the projected vector.
Thus when N>rho it can be computed directly as

    v_(rho,ell,N;±)
      =[-i (-1)^ell (2ell)!/4^ell]
         sum_(n=rho+ell+1)^(N+ell)
          P_(rho+ell)(U^n-U^-n)psi_± /
                   [(n-ell)(n-ell+1)...(n+ell)].  (T10)

When N<=rho the vector is zero and gives no passing certificate.
Formula (T10) has only rational coefficients multiplying i and the
fixed algebraic walk amplitudes. The source normalization sqrt(Z) is
retained. No numerical approximation to pi or arbitrary test-vector
selection is hidden in this expression.

The largest seed power needed in (T10) is

    K=N+ell+2,                                    (T11)

because each psi_± already contains powers 0,2,-2 of U applied to chi.
The signs are to be evaluated separately; equality of the complete
energy laws does not imply equality of these projected norms.

Receiver calibration is a position-preserving conjugation and is
identity on chi. Removing it leaves the fixed active walk tensored
with Xi. Since each P_a commutes with calibration, the projected target
norm in (T5) and the finite-certificate norm in (T10) are independent
of all 26 old-memory labels and arbitrary passive reference states.
This includes mixed inputs by purification; it does not assert that a
comparator's actual error is independent of its memory couplings.
With an orthogonal retained setting register, the squared norms add
with the setting weights. An arbitrary unmarked superposition of
psi_+ and psi_- is not substituted for that setting contract.

## 5. A fixed prospective diameter-two instance and its limits

One explicit instance for future consideration is

    rho=2, ell=2, N=8,
    degree(g_(2,8))=10, K=12,
    P_(rho+ell)=1_(c<=90 or c>=104),
    r_(2,8)=1/15840.                              (T12)

For either nominated sign, the sufficient passing condition is

    ||v_(2,2,8;±)|| > 1/1200 + 1/15840.           (T13)

If established, this would prove that sign's original energy-action
error exceeds E0/1200 for every comparator of diameter at most two.
Both signs of this displayed instance are nominated for separate
reporting. Success on one sign would refute a uniform realization of
the pair, without establishing failure on the other sign.
No value in (T13) has been evaluated. A failure of this sufficient test
would be inconclusive, and would not authorize a changed source,
threshold or unrecorded parameter search. Any computational use must
freeze the exact implementation, both algebraic comparisons, outputs
and dispositions before its first scientific run.

All seed iterates in (T12) lie in |R-97|,|r|,|c-97|<=12. A coarse
bound is therefore 12*25^3=187500 coordinate/coin basis positions,
from four object coins and one token plus two pulse banks. This is
an upper bound for one iterate, not a run-time or memory benchmark.
The position-dependent calibration permutes the fixed carrier/memory
labels; it does not require enumerating every memory or reference.
An exact verifier remains to be written and pinned.

There is also an analytical limit to this filter family. The deeper
projection kills all powers |n|<=rho+ell in the full series, so (T8)
with N=rho gives

    ||P_(rho+ell) g_ell(U) psi||
       <= r_(ell,rho).                            (T14)

For rho=1 this ceiling is
2^(1-2ell)/[2ell(2ell+1)]. Already ell=3 gives 1/1344<1/1200.
The ratio r_(ell+1,rho)/r_(ell,rho) equals
(2ell)(2ell+1)/[4(rho+2ell+1)(rho+2ell+2)]<1/4, so all larger ell
are also excluded for this contraction-based certificate. Increasing
rho lowers the ceiling further. Thus ell>=3 cannot cross the target
for any rho>=1 in this particular method. This restricts the dual
method, not the true forbidden energy tail. The options ell=1 or 2
remain only candidate tests; neither is asserted to pass for rho=2.
For the instance (T12), the ceiling is r_(2,2)=1/480; this upper bound
does not provide any positive lower bound on the actual test norm.

## 6. Separate review obligations

1. Check the unchanged source, energy branch and occupation pins;
   establish the common carrier interval (T2) for positive and negative
   source powers, without claiming a larger source family.
2. Check the carrier support zero for both types, the coarse forbidden
   projection, fixed ancillary states and the action bound (T3).
3. Check the centered filter's positivity, degree, support relation and
   adjoint argument in (T5), and that no physical source is filtered.
4. Check all coefficients including the central pi terms, the Fourier
   convention, the value at the cut and the telescoping remainder.
5. Check the projected cancellation, both signs in (T10), seed power
   bound and the separate memory/reference and setting statements.
6. Check the frozen example's geometry, degree, exact remainder and
   sufficient threshold; confirm that no test was executed or passed.
7. Check the ceiling (T14), its monotonicity and its restriction to this
   dual method, without promoting a failed test to physical existence.

This appendix supplies neither a diameter-two construction nor a
diameter-two impossibility theorem, and no new continuous-time,
preparation, funded readout, renewal or empirical admission. All these
claims remain separate from the finite necessary test.
