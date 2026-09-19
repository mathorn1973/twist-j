# PREREG: P-U-J-HODGE-CHECKPOINT-NOGO-1

**FORMAL PUBLIC PROBE / NO CANON PROMOTION.**

Owner: A. M. Thorn / ChatGPT-B1-finite-reader-20260919.
Action layer: L1.
Issue lock: #1057.
Branch: `probe/P-U-J-HODGE-CHECKPOINT-NOGO-1`.
Authority: Public Canon v89; base main
`9351b130c3e31645257db31ca1a6bbadaa51a7fb`.
The author explicitly authorized use of the connected GitHub commit identity.

## Equation and complete comparison class

Use `V=A4 tensor Q` in the ordered root basis `a_i=e_i-e_0`, i=1..4,
with Gram `H=I_4+11^T`. The marked coordinate cycle is

```text
C=((-1,-1,-1,-1),(1,0,0,0),(0,1,0,0),(0,0,1,0)).
M=I+C^2; W=Lambda^2 V; L=Lambda^2 M; A=Lambda^2 C.
```

The ordered wedge basis is `01,02,03,12,13,23`. Let B be its symmetric
wedge-pairing matrix, G=Lambda^2 H, K=BG, and
`P_+=(I+K/sqrt(5))/2`, `P_-=(I-K/sqrt(5))/2` over R.
The fixed-plus predictive carrier is
`E_J=im P_+ + im(P_- L P_+)`, as in the accepted A1/A2 probes.
Their definitions are retained, not replaced by a physical carrier.
Set

```text
T=(I+A+A^2+A^3+A^4)/5; R=I-T;
p(X)=X^2-3X+1; q(X)=X^4-X^3+X^2-X+1.
```

The primary targets are:

1. T and R are complementary rational projectors of ranks 2 and 4,
   commuting with L; K commutes with R and K^2=5I.
2. p(L)T=0, q(L)R=0 and L^5 R=-R.
3. The complete periodic-vector locus of L over R or C is
   `im R=ker(L^10-I)`. Every nonzero vector there has exact period ten.
4. `E_J intersect im R=R(im P_+)` has real dimension two.
5. For every finite nonempty set Y, every sequence y_n in Y, and every
   fixed function r:Y->W_R (not assumed linear), an exact identity
   `r(y_n)=L^n v` for all n>=0 implies Tv=0. No source periodicity or
   autonomous update on Y is assumed. If Tv!=0, exact agreement on
   n=0..N requires at least N+1 distinguishable reader configurations.
6. Let X be a finite nonempty address set, F_n:X->X arbitrary maps,
   `N_n e_x=e_(F_n(x))`, B_src:S->F^X and D:F^X->W_F fixed linear maps,
   where F is R or C and S is a finite-dimensional F-vector space.
   If `D N_n B_src=L^n D B_src` for every n>=0, then `T D B_src=0`.
   Its image has dimension at most four, or at most two if it is contained
   in E_J or its explicit complexification. The fixed encoding and fixed
   output map are essential assumptions; no time-dependent amplitudes,
   extra address states, time-dependent output basis or channels are added.

Native scope: a checkpoint-only reader of unchanged U, or a fixed-length
finite-alphabet window with a fixed finite auxiliary register, has finite
configuration set Y and is covered only if it satisfies the displayed exact
all-time target identity. The full Omega=N_0 x F_5^6 is not finite and is
not excluded. The fixed free-linear-code clause applies to the free
pushforwards of actual deterministic native checkpoint maps, not arbitrary
physical quantum dynamics. No nonzero periodic native reader is constructed.

## Code and proof

`PROOF.md` gives the universal finite-orbit and fixed-code arguments.
`verify.py` reconstructs the rational operators using Python standard-library
Fraction arithmetic. It audits these finite certificates:

```text
G1 marked C^5=I, C^T H C=H, invertibility of L;
G2 integrality of K and K^2=5I;
G3 complementary projectors, ranks, commutation;
G4 exact p and q factor identities;
G5 order-ten operator identities, rank(L^10-I)=2,
   rank((L^d-I)R)=4 for d=1,2,5;
G6 tr(KR)=0 and R(KL-LK)=0;
G7 a nonzero ten-state periodic target control;
G8 a nonzero hyperbolic target control.
```

The all-time quantifiers in targets 3 through 6 are proved, not inferred from
G7/G8 or any native-time sampling. Neither the finite-orbit principle nor
standard cyclotomic identities are claimed novel.
No additional scientific verifier, native trajectory sweep or independent
reviewer is part of this preregistration.

## Carrier, input custody and systematics

All matrices are generated from the displayed basis, metric and cycle.
No runtime input is taken from a moving Canon or another probe's program.
The completed A1 (#1049), A3 (#1050), A2 (#1052) and separately owned A4
(#1053/#1056) are not changed or resumed. In particular the closed duplicate
A1/A3 attempts are not predecessors for a new suffix of either probe.

Real scalar extension is explicit; the fixed-code clause also permits the
explicit complexification, with dimensions then taken over C. Orientation
and the plus output are fixed. The projectors T,R are algebraic and carry
no probability interpretation. Literal equality is required at every
integer step, including zero outputs. There is no tolerance, rescaling of
time, projective-output quotient, discarded subsequence or approximation.

## Failure threshold and execution

Any exact counterexample to targets 1 through 6 rejects the corresponding
claim. Every evaluated G1-G8 condition is printed as PASS or FIRED_NEGATIVE;
a completed scientific decision exits zero, including a negative decision.
Uncaught implementation errors remain nonzero failures without a completed
scientific run. The repository's current runners and POLICY.md control the
pin, execution, record and two-architecture procedures.

PREREG.md, PROOF.md and verify.py are published together and read back before
the first scientific execution. Only syntax inspection precedes that pin.
Expected output is recorded from the actual run, never generated by hand.

## Explicit nonclaims

This is exact L1 algebra and a restricted reading obstruction. It does not
show that actual checkpoints are periodic, identify physical time, select
an observer or spatial dimension, refute the full native architecture,
supply a positive native-U bridge, or close any physical O row. It makes
no approximate-simulation, energy-cost, probability, measure, SI or L2-L6
claim. Unbounded read-time information is necessary for the specified
nonzero hyperbolic target, not sufficient and not uniquely a counter.
The existing coherent code's source-information/isometry result is untouched.
