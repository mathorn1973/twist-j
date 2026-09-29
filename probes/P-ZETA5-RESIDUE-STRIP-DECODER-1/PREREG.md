# P-ZETA5-RESIDUE-STRIP-DECODER-1

Status: preregistered public probe candidate, RESULT-EXPOSED.
Action layer: L1 only.
Owner: A. M. Thorn / current ChatGPT session.
Public lock: #1271.
Branch: probe/P-ZETA5-RESIDUE-STRIP-DECODER-1.
Source: public main 3813e4142e96d9233b246681e39bbd381e8780b4.
Authority: Public Canon v92 ACTIVE.

This probe is proof-first and confirmatory. The predecessor incubation #1269
and notes PR #1270 exposed the strip construction, counts and capacity endpoint
before this pin. The later residue/QDD observations were also exposed before
this pin. No blind-discovery status is claimed and no frozen threshold may move.

## 1. Equations and targets

Let K=Q(zeta_5), k=Q(sqrt(5)), O_K=Z[zeta_5],
phi=(1+sqrt(5))/2, J=1+zeta_5^2=zeta_5/phi. For nonzero alpha in O_K set

    A = |sigma_1(alpha)|^2,
    B = |sigma_2(alpha)|^2.

G1 RESIDUE.
Using the registered exact invariants

    K: r1=0, r2=2, h=1, w=10, d=125, R=2 log(phi),
    k: r1=2, r2=0, h=1, w=2,  d=5,   R=log(phi),

and the standard analytic class number formula, derive

    Res zeta_K(s) = 4 pi^2 log(phi)/(25 sqrt(5))
                  = (2 log(phi)/sqrt(5)) (2 pi^2/25).

For the primitive quartic character modulo five with kappa(2)=i, use the
standard primitive odd-character formula and verify

    S = sum_(a=1)^4 conjugate(kappa(a)) a = -3+i,
    |S|^2 = 10,
    |L(1,kappa)|^2 = 2 pi^2/25.

The ratio bookkeeping must use sqrt(125/5)=5 and 10/2=5.

G2 J-STRIP.
Prove that

    1 <= A/B < phi^4

is a half-open fundamental domain for multiplication by J^Z, because one
J-step multiplies A/B by phi^-4. The counter is

    n = -floor(log_(phi^4)(A/B))

and must admit an integer-only implementation by comparisons in Q(sqrt(5)).
For alpha*bar(alpha)=u+v phi the frozen equivalent test is

    alpha is in the strip iff v >= 0 and u-v > 0.

G3 ORBIT COUNT.
Using registered h_K=1 and O_K^x=mu_10 x <phi>, prove for every X>=1

    #{alpha != 0 : 1<=A/B<phi^4, N(alpha)<=X}
      = 10 * #{nonzero integral ideals I : N(I)<=X}.

The verifier must use the proved coefficient box and compare the two exact
counts norm-by-norm through X=2500. Frozen cumulative witnesses:

    X=940:  3110
    X=941:  3150
    X=1000: 3410
    X=2500: 8440

Negative control, frozen before execution:

    1 <= A/B < phi^2, X=2500  ->  4300.

Independent ideal-count witness:

    A_K(10^6) = 339775.

No decimal ratio is a gate.

G4 NATIVE SCALAR CAPACITY.
Import U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T], not its verifier. In the
frozen class of nonzero integral scalar readers that are exact U-to-J
equivariant, globally injective across all reachable sheets n>=3, and have
one uniform algebraic-norm bound X, prove

    X_min = min { X : |B_X| >= 3125 } = 941.

The lexicographic injection of the 3125 conserved labels into the first 3125
strip representatives ordered by (norm, coefficient tuple) is an existence
witness only, not a selected physical decoder.

G5 QDD GALOIS SUM-RATIO.
Use the registered Route A cyclotomic map iota_B0(v)=sum_(j=0)^3 v_j zeta^j
for the balanced piston v. With Q=sum v_j^2 and s=sum v_j, prove

    5Q - s^2 = Tr_(K/Q)(alpha bar(alpha)) = 2(A+B),

and hence, on supported sources,

    s^2/[4(5Q-s^2)] = s^2/[8(A+B)].

The strip reads A/B while this registered QDD incidence ratio reads A+B.

G6 LANDAU SPECIALIZATION.
Import Landau's standard ideal-counting theorem

    A_K(X) = kappa_K X + O_K(X^(1-2/(n+1)))

for degree n. At n=4 and kappa_K=Res_(s=1) zeta_K(s), record

    A_K(X) = C_K X + O_K(X^(3/5)),
    C_K = 4 pi^2 log(phi)/(25 sqrt(5)).

The verifier does not purport to prove the analytic asymptotic theorem.

## 2. Code

Before the first formal execution freeze PREREG.md, PROOF.md and verify.py in
one commit and push it. verify.py is Python-standard-library only and uses
integers and Fraction. It contains no float, randomness, external input,
network access or tolerance.

Formal command from repository root:

    python3 probes/P-ZETA5-RESIDUE-STRIP-DECODER-1/verify.py

The accepted first-run stdout becomes EXPECTED.txt. Required public replay is
the repository x86_64 and aarch64 pull-request workflow plus aggregate check.

## 3. Carrier and data

Arithmetic carrier: O_K in basis (1,zeta,zeta^2,zeta^3), its real relative
norm in Z[phi], and exact ideal Euler factors of Q(zeta_5).

QDD carrier: exactly the 625 balanced four-coordinate piston inputs
{-2,-1,0,1,2}^4 under the already registered iota_B0 map.

Native-reader input: only the published theorem
U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]. The native dynamics is not rerun in
this probe.

There is no external dataset.

## 4. Systematics and exact finite domains

The verifier:

1. checks the residue coefficient bookkeeping and quartic Gauss numerator;
2. audits the oriented strip and exact J round trip on five strip seeds and
   n=-12..12, exactly 125 pairs;
3. enumerates the complete proved coefficient box for norm <=2500;
4. compares every norm 1..2500 against ten times a separately implemented
   Euler-factor ideal count;
5. evaluates the frozen half-width negative control;
6. independently extends the ideal recurrence to 10^6;
7. evaluates the capacity threshold from the exact cumulative strip counts;
8. exhausts all 625 balanced QDD pistons for the trace/sum identity and ratio.

Universal conclusions rest on PROOF.md, not finite extrapolation.

## 5. Failure threshold

Any failed exact assertion fires its named target. In particular:

- a residue coefficient or Gauss numerator mismatch fires G1;
- a strip duplicate, gap or round-trip failure fires G2;
- one normwise discrepancy through 2500, any frozen cumulative mismatch,
  the wrong-strip count differing from 4300, or A_K(10^6) differing from
  339775 fires G3;
- capacity minimum other than 941 fires G4;
- one balanced QDD source violating the exact trace/sum identity or supported
  ratio equality fires G5;
- a dispute about the imported Landau theorem is dependency STOP for G6,
  not permission to alter a finite threshold.

A source, pin, custody, workflow or environment defect is integrity STOP and is
not converted into a mathematical falsifier. A completed fired falsifier is
merged, not hidden.

## 6. Action layer and exclusions

L1 only. No L2-L6 lift.

Explicitly excluded: physical clock, physical decoder uniqueness, preferred
codebook, Born law, apparatus, event, occurrence, measure, SI scale, or any
identification of the regulator width with a different rapidity convention.

Also excluded is the possible future 25-element carrier factorization

    (mu_10/{+/-1}) x O_K/(1-zeta_5) ~= C5 x F5.

Cardinality 25 alone is not evidence. A later probe must freeze one concrete
25-element carrier, its actions, equality and an equivariance contract.

## 7. Status discipline

Written proof targets may earn T only after review accepts the derivation.
Finite computation requires the formal two-architecture byte-identity gate.
No Canon or Registry change occurs in this probe. Canonization is a separate
public fold.
