# Result: residue, J-strip, scalar capacity and QDD Galois bridge

Status: candidate-T proof layer with candidate-C finite computation pending the
required public two-architecture gate.

Probe: P-ZETA5-RESIDUE-STRIP-DECODER-2.
Action layer: L1 only.
Outcome: PASS on the first completed pinned local run.
Fired mathematical falsifiers: none.

## G1. Dedekind residue

[candidate-T, proof-first]

For K=Q(zeta_5),

    Res_(s=1) zeta_K(s)
      = 4 pi^2 log(phi)/(25 sqrt(5))
      = (2 log(phi)/sqrt(5)) (2 pi^2/25).

For the primitive quartic character normalized by kappa(2)=i,

    S = -3+i,
    |S|^2 = 10,
    |L(1,kappa)|^2 = 2 pi^2/25.

The two denominator fives in the relative class-number-formula bookkeeping are
separate exact factors:

    sqrt(125/5)=5,
    10/2=5.

The Gaussian factorization -3+i=(1+i)(-1+2i) is retained only as an exact
witness and is not promoted to a derivation of w_K.

## G2. Exact oriented J-strip

[candidate-T, proof-first]

For nonzero alpha, with A=|sigma_1(alpha)|^2 and
B=|sigma_2(alpha)|^2,

    1 <= A/B < phi^4

is a half-open fundamental domain for J^Z, because one J-step multiplies A/B
by phi^-4. The exact counter is

    n = -floor(log_(phi^4)(A/B)),

with no logarithm needed in the implementation.

If alpha bar(alpha)=u+v phi, the same strip is exactly

    v >= 0 and u-v > 0.

The pinned integer-only round trip passed on all 125 frozen pairs
from five strip representatives and n=-12..12.

## G3. Exact orbit count

[candidate-T universal identity; candidate-C finite audit until PR replay]

Using public h_K=1 and O_K^x=mu_10 x <phi>,

    |B_X| = 10 A_K(X)

for every X>=1, where B_X is the oriented strip with norm at most X.

The complete coefficient bound is proved in PROOF.md. The pinned finite audit
agreed norm-by-norm for every n=1..2500 with an independent Euler-factor ideal
count and gave

    |B_940|  = 3110,
    |B_941|  = 3150,
    |B_1000| = 3410,
    |B_2500| = 8440.

The frozen wrong-width control

    1 <= A/B < phi^2

gave 4300 representatives at X=2500, so the width test discriminates.

The independent ideal recurrence also gave exactly

    A_K(10^6)=339775.

## G4. Native scalar capacity

[candidate-T reduction; candidate-C endpoint until PR replay]

Importing the already public complete reachable-reader classification, global
injectivity across all reachable sheets forces the 3125 conserved labels into
3125 distinct J-orbits. Therefore

    X_min = min{X: |B_X|>=3125}.

The exact frozen counts give

    X_min = 941.

This is a capacity theorem for the declared integral scalar-reader class, not a
physical constant. The lexicographic codebook is an existence witness only.

## G5. QDD Galois sum-ratio bridge

[candidate-T, proof-first]

For the registered Route A cyclotomic map on the balanced piston source,

    5Q-s^2
      = Tr_(K/Q)(alpha bar(alpha))
      = 2(A+B).

Hence on every supported source,

    s^2/[4(5Q-s^2)]
      = s^2/[8(A+B)].

The verifier exhausted all 625 balanced pistons for the trace identity and all
624 supported pistons for the ratio equality.

Thus the existing QDD arithmetic reads the symmetric sum A+B while the
J-strip reads the positive ratio A/B. This is an L1 arithmetic relation only.

## G6. Landau specialization

[candidate-T, conditional on the standard imported Landau theorem]

For a degree-four number field the standard Landau exponent specializes to

    1 - 2/(4+1) = 3/5,

so with the exact residue above,

    A_K(X)
      = [4 pi^2 log(phi)/(25 sqrt(5))] X + O_K(X^(3/5)).

The finite verifier audits the specialization and exact counts; it does not
prove the analytic Landau theorem.

## Boundary

The possible 25-element factorization

    (mu_10/{+/-1}) x O_K/(1-zeta_5) ~= C5 x F5

remains outside this probe. No carrier has been selected by cardinality alone.

No physical clock, decoder uniqueness, preferred codebook, Born law,
apparatus, event, occurrence, measure, SI scale or L2-L6 lift is established.

## Evidence ceiling before pull-request replay

The written derivations are candidate-T pending review. The finite computation
is one pinned local x86_64 execution and is therefore at most candidate-C until
the required x86_64 and aarch64 workflow jobs reproduce EXPECTED.txt byte for
byte. Canon and Registry remain unchanged.
