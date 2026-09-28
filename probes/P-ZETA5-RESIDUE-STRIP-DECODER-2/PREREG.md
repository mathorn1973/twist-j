# P-ZETA5-RESIDUE-STRIP-DECODER-2

Status: preregistered public probe candidate, RESULT-EXPOSED.
Action layer: L1 only.
Owner: A. M. Thorn / current ChatGPT session.
Public lock: #1273.
Branch: probe/P-ZETA5-RESIDUE-STRIP-DECODER-2.
Source: public main 41c3c01dc25d6426fe4085048f95527bda9486f7.
Authority: Public Canon v92 ACTIVE.

## Predecessor

P-ZETA5-RESIDUE-STRIP-DECODER-1 is ABANDONED in merged PR #1272.
Its formal gate never ran. Public readback before execution found byte-transport
corruption in the pinned verifier. The predecessor identifier is consumed.

This successor changes no scientific equation, domain, threshold or falsifier
from issue #1271. It changes only the probe identifier and the source-transport
procedure. The residue, strip, capacity and QDD results were exposed before
this pin, so the probe is confirmatory and proof-first, not blind discovery.

## 1. Frozen equations and targets

Let K=Q(zeta_5), k=Q(sqrt(5)), O_K=Z[zeta_5],
phi=(1+sqrt(5))/2 and J=1+zeta_5^2=zeta_5/phi.
For nonzero alpha in O_K put

    A = |sigma_1(alpha)|^2,
    B = |sigma_2(alpha)|^2.

G1 RESIDUE.
Using the already public exact invariants

    K: r1=0, r2=2, h=1, w=10, d=125, R=2 log(phi),
    k: r1=2, r2=0, h=1, w=2,  d=5,   R=log(phi),

and the standard analytic class number formula, derive

    Res_(s=1) zeta_K(s)
      = 4 pi^2 log(phi)/(25 sqrt(5))
      = (2 log(phi)/sqrt(5)) (2 pi^2/25).

For the primitive quartic character modulo five normalized by kappa(2)=i,
verify

    S = sum_(a=1)^4 conjugate(kappa(a)) a = -3+i,
    |S|^2 = 10,
    |L(1,kappa)|^2 = 2 pi^2/25,

using the standard primitive odd-character formula. The relative bookkeeping
must use sqrt(125/5)=5 and 10/2=5.

G2 J-STRIP.
Prove that

    1 <= A/B < phi^4

is a half-open fundamental domain for multiplication by J^Z. One J-step
multiplies A/B by phi^-4. The counter is

    n = -floor(log_(phi^4)(A/B)),

but the implementation must use exact comparisons in Q(sqrt(5)), no floating
point. If alpha bar(alpha)=u+v phi, the same strip is exactly

    v >= 0 and u-v > 0.

G3 ORBIT COUNT.
Using public h_K=1 and O_K^x=mu_10 x <phi>, prove for every X>=1

    #{alpha != 0 : 1<=A/B<phi^4, N(alpha)<=X}
      = 10 * #{nonzero integral ideals I : N(I)<=X}.

The complete coefficient box must be proved. Formal finite thresholds are

    X=940:   3110
    X=941:   3150
    X=1000:  3410
    X=2500:  8440

and the norm-by-norm equality with ten times an independently implemented
Euler-factor ideal count is required for every n=1..2500.

Frozen negative control:

    1 <= A/B < phi^2, X=2500  -> 4300 representatives.

Frozen independent ideal-count witness:

    A_K(10^6) = 339775.

No decimal ratio is a gate.

G4 NATIVE SCALAR CAPACITY.
Import U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T], not its verifier. In the
frozen class of nonzero integral scalar readers that are exact U-to-J
equivariant, globally injective across all reachable sheets n>=3 and uniformly
bounded by algebraic norm X, prove

    X_min = min{X : |B_X| >= 3125} = 941.

The lexicographic codebook is an existence witness only, not a selected
physical decoder.

G5 QDD GALOIS SUM-RATIO.
Use exactly the registered Route A map

    alpha = iota_B0(v) = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3

on the balanced four-coordinate QDD source. With

    Q = sum_j v_j^2,
    s = sum_j v_j,

prove

    5Q-s^2 = Tr_(K/Q)(alpha bar(alpha)) = 2(A+B),

and on supported sources

    s^2/[4(5Q-s^2)] = s^2/[8(A+B)].

The strip reads A/B while this registered QDD arithmetic reads A+B.

G6 LANDAU SPECIALIZATION.
Import the standard Landau ideal-counting theorem

    A_F(X)=kappa_F X + O_F(X^(1-2/(n+1)))

for a fixed degree-n number field. At n=4 and
kappa_K=Res_(s=1) zeta_K(s), record

    A_K(X)
      = [4 pi^2 log(phi)/(25 sqrt(5))] X + O_K(X^(3/5)).

The verifier audits only the exact exponent specialization and finite counts;
it does not numerically prove the asymptotic theorem.

## 2. Code

Freeze PREREG.md, PROOF.md and verify.py in one public commit before the first
formal execution. verify.py uses only the Python standard library, integers
and Fraction. It has no floating point, randomness, input files, network,
tolerance or generated codebook file.

Formal command from repository root:

    python3 probes/P-ZETA5-RESIDUE-STRIP-DECODER-2/verify.py

The first completed formal stdout becomes EXPECTED.txt. Required public replay
is the repository x86_64 and aarch64 pull-request workflow plus aggregate
check.

## 3. Carrier and data

Arithmetic carrier: O_K in basis (1,zeta,zeta^2,zeta^3), its real relative
norm in Z[phi], and exact ideal Euler factors of Q(zeta_5).

QDD carrier: exactly the 625 balanced four-coordinate piston inputs
{-2,-1,0,1,2}^4 under the registered iota_B0 map.

Native-reader input: only the public theorem
U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]. Native dynamics is not re-run.

There is no external dataset.

## 4. Systematics

The verifier:
1. audits residue coefficient bookkeeping and the quartic Gauss numerator;
2. checks exact J inverse and norm;
3. enumerates the complete proved coefficient box through norm 2500;
4. compares every norm 1..2500 with ten times the independent Euler recurrence;
5. checks all frozen cumulative counts and the wrong-width negative control;
6. checks 125 exact J strip round trips on five frozen representatives and
   n=-12..12;
7. decides the 3125-orbit capacity endpoint from the exact cumulative counts;
8. independently evaluates A_K(10^6);
9. exhausts all 625 balanced QDD pistons for the trace/sum identity and all
   624 supported pistons for the incidence rewrite;
10. audits the Landau exponent arithmetic 1-2/5=3/5.

Universal statements rest on PROOF.md, never finite extrapolation.

## 5. Failure threshold

Any failed exact assertion fires its named target. In particular:
- residue/Gauss mismatch fires G1;
- strip or round-trip failure fires G2;
- one normwise mismatch, frozen count mismatch, wrong negative-control count
  or wrong A_K(10^6) fires G3;
- capacity endpoint other than 941 fires G4;
- one balanced QDD source violating the exact trace identity or supported
  ratio equality fires G5;
- a dispute about the imported Landau theorem is dependency STOP for G6, not
  permission to change a finite threshold.

A source, pin, custody, workflow or environment defect is integrity STOP and
is not converted into a mathematical falsifier. A completed fired falsifier is
merged, not hidden.

## 6. Action layer and exclusions

L1 only. No L2-L6 lift.

Explicitly excluded: physical clock, decoder uniqueness, preferred codebook,
Born law, apparatus, event, occurrence, measure, SI scale, and any
identification of regulator width with another rapidity convention.

Also excluded is a possible future 25-element factorization

    (mu_10/{+/-1}) x O_K/(1-zeta_5) ~= C5 x F5.

Cardinality 25 alone is not evidence. A later probe must freeze one concrete
25-element carrier, its actions, equality and an equivariance contract.

## 7. Status discipline

Written proof targets may earn T only after review accepts the derivation.
Finite computation requires the formal two-architecture byte-identity gate.
No Canon or Registry move occurs in this probe. Canonization is a separate
public fold.
