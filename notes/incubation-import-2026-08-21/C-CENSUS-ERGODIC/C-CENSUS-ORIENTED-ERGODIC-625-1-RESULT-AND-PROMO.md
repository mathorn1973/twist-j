# C-CENSUS-ORIENTED-ERGODIC-625-1: result and promotion proposal

```
STATUS   BRANCH ORIENTED-625. 10 of 10 gates PASS. candidate-C on the
         enumerations, candidate-T on the count. Incubation lane, no
         authority. Not canon. Supersedes the falsified BIJECTION-313.
DATE     2026-07-25
RESULT   |M_e(U_hat)| = 625 exactly. The invariant simplex is Delta^624.
         The 313 census supports are the affine mirror quotient of the 625
         oriented streams: F_5^4 / (p ~ (2,1,3,4) - p), (625+1)/2 = 313.
```

## Verdict on the counteraudit: confirmed, and its open end closed

The counteraudit is correct on every substantive point. I reproduced it from
a construction that shares nothing with either its code or the falsified
verifier: the decomposition is the strongly connected components of the
exact context-window product graph, computed by Tarjan, with no return words
involved at all. Return words enter only afterwards, to close the upper
bound.

```
counteraudit claim                                    my independent finding
generic components split in two, singlet does not     CONFIRMED
the first radius that sees it is a 4-symbol context   CONFIRMED at window
                                                      length 5 in my
                                                      alignment; lengths
                                                      2,3,4 still give 313
625 cells biject with F_5^4, one piston each          CONFIRMED, 5 states
                                                      per cell per window
census = F_5^4 / (p ~ c_d - p), c_d = (2,1,3,4)       CONFIRMED, unique
                                                      fixed point (1,3,4,2)
that fixed piston is the singlet                      CONFIRMED
Burnside (625+1)/2 = 313                              CONFIRMED
uniform seed ensemble gives 25 seeds per cell         CONFIRMED at 3, 4 and
                                                      8 ticks
old weights (2/625 x 312, 1/625) are the pushforward  CONFIRMED
of uniform 1/625
coarse D_5 survives as monodromy, C_5 is the real     CONFIRMED
return group
the maximum-entropy correction, 625 extreme points    CONFIRMED, and the
and the full simplex is their hull                    hull is Delta^624
```

The counteraudit closed its own breaker with "NEXT: prove or refute unique
ergodicity inside each of the 625 clopen components before claiming the
exact count 625." That is now closed here, and by a route independent of its
substitution argument:

```
at the fine cylinder 11001011 the first-return lengths are 16, 24, 32; every
cell fibre is exactly 5 states and is closed under all three returns; the
return group has order 5 and acts REGULARLY; and every group element is
realised by an actually occurring factor of the derived sequence.
A regular C_5 action means each cell is a MINIMAL PRINCIPAL C_5 EXTENSION of
the uniquely ergodic Thue-Morse base. A minimal compact group extension of a
uniquely ergodic system is uniquely ergodic. Hence exactly one measure per
cell, and the lower bound 625 from the clopen decomposition meets the upper
bound 625.
```

## Two corrections to the counteraudit

```
1  SCOPE. Its E4 folds "all four first-return words induce the SAME order-5
   cycle rho: q -> q+1". That is a property of its cylinder [0110], not a
   general fact. At the fine cylinder used here the three first-return words
   induce THREE DIFFERENT permutations, with q-shifts 0, 1 and 3, while the
   group is still exactly C_5 and still regular. The group is foldable; the
   common-generator form is not. This is gate G09.
2  BOUND HYGIENE. Its B3 correctly reports the clopen decomposition as a
   LOWER bound. The context-window graph over-approximates the non-sofic
   Thue-Morse language, so its component count can only rise with radius.
   Stability from length 5 to length 64 in three window alignments is
   strong, but the exact count is earned by the regular-action argument
   above, not by stabilisation. The distinction is kept explicit here.
```

## Pins

```
prereg    PREREG-C-CENSUS-ORIENTED-ERGODIC-625-1.md
          sha256 d8109d17452ee33016c67f4952b0ed46542a9a7b140226390cb6f45cf854ff83
          6273 bytes. CONFIRMATION freeze, not a blind freeze; the
          disclosure is in the prereg itself.
verifier  verify_oriented_ergodic_625.py
          sha256 cfd40026d0fc228bb515dfecf9e5bc627a45c3e4e65c1ff8c98ddb873f3b6854
          12615 bytes, runtime 22 s
stdout    sha256 bd6c3d7ce9eefc20a673c822c5e59810e097550a07ad6fdbd1e7e466fb5b51df
          2995 bytes, 23 lines, exit 0, stderr empty
falsifier F-CENSUS-ERGODIC-BIJECTION-313.md
          sha256 32e0caaf2d150f8c46656a8eb0ed3d7ff32244ef56d941d443f31a207116d9e9
platform  Ubuntu 24.04 x86_64, CPython 3.11.15, stdlib only, exact integer
          arithmetic over F_5, no floats in any assertion
inputs    counteraudit zip sha256
          a5893ffed32a9b0afd4ac09ae8540074e5bce529ce761df6e3b7badf8b00866a
          verified; its own SHA256SUMS verified; its claimed verifier hash
          ea9d1eb9... and stdout hash 65224231... both match the files.
MISSING   the aarch64 leg, still. Two architectures have not run.
```

## Exact edits a fold would make, after a public probe passes

```
REGISTRY.tsv
  RETIRE   nothing. CENSUS-ERGODIC-BIJECTION was never folded. It must NOT
           be folded now in the 313 form.
  NEW  CENSUS-CONTEXT-DECOMPOSITION            C
       the exact context-window decomposition of the living hull: 313
       components at context radius <= 4, 625 at radius >= 5, stable to
       length 64 in past-heavy, balanced and future-heavy alignments; each
       cell carries 5 states over every window, sharing one piston; the 625
       cells biject with F_5^4
       falsifier: any window length or alignment giving another count, or a
       cell whose fibre is not 5 states
  NEW  CENSUS-MIRROR-QUOTIENT                  T
       the 313 census supports are exactly F_5^4 / (p ~ c_d^piston - p) with
       c_d^piston = (2,1,3,4); the involution has the single fixed piston
       (1,3,4,2), which is the singlet; Burnside gives (5^4 + 1)/2 = 313.
       This DERIVES the census count 313 from the axiom-level mirror letter d
       rather than reporting it as an enumeration.
       falsifier: a second fixed piston, or a generic component whose two
       cells are not mirror partners
  NEW  CENSUS-ORIENTED-ERGODIC-COUNT           T
       U_hat has exactly 625 ergodic invariant probability measures, one per
       oriented cell; the invariant simplex is Delta^624; every vertex has
       entropy zero. Each cell is a minimal principal C_5 extension of the
       uniquely ergodic Thue-Morse base.
       falsifier: a second ergodic measure on any cell, or an ergodic
       measure charging no cell
  NEW  CENSUS-COARSE-RETURN-MONODROMY          C
       at context radius 1 the return group of each census component half is
       D_5 of order 10, transitive on the 10 state labels, with every element
       realised along the derived gap sequence; the hosting group H_1 =
       <d, b e b> stabilises one half of each component and b H_1 b the
       other. Scope note, mandatory: this is the monodromy of the coarse
       symbolic quotient and does NOT count ergodic components.
       falsifier: a return group of order other than 10 at radius 1
  NEW  CENSUS-SEED-MASS-UNIFORM                C
       the uniform ensemble of all 15625 seeds collapses after 3 ticks onto
       the 625 cells with exactly 25 seeds each, oriented weight 1/625; the
       registered window law (2/625 x 312, 1/625) is its mirror pushforward
       falsifier: a cell with seed mass other than 25
FRONTIER.md
  ENTROPY-LAYER-BRIDGE [O] keeps status, decision condition and falsifier.
  Extend scope by one clause: the target now has a complete invariant-measure
  census of 625 oriented cells, and any admissible P_5 must push mu forward
  into Delta^624.
  OPEN one new row, because the physical question has actually sharpened:
  ORIENTATION-SELECTION [O]  why a physical reading would quotient the
  oriented stream census by the affine piston mirror, or alternatively which
  point of Delta^624 it selects; the uniform barycentre is a distinguished
  point but no principle yet selects it, and maximum entropy does NOT select
  it because it fixes only the Haar torus factor
CANON.md
  section 3: replace any prose that reads the census count 313 as primitive
  with the mirror-quotient derivation. section 8: the hull, the radius
  dependence, and the 625 count with its dependency named.
CHANGELOG.md and SHA256SUMS: reseal.
```

## POLICY question, restated and sharpened

Both T rows above rest on one import each: Burnside for the quotient count
(elementary, self-contained, safely T) and the unique ergodicity of minimal
compact group extensions for the count (classical literature). The earlier
recommendation stands and is now easier: fold CENSUS-MIRROR-QUOTIENT at T
because Burnside can be written out in three lines inside the repository, and
fold CENSUS-ORIENTED-ERGODIC-COUNT at D unless the owner accepts a named
literature import at public T.

## What is still open, corrected

```
open  ORIENTATION-SELECTION. This is the real gap now, and it is sharper
      than the old BASIN-WEIGHT-LIMIT. The counting part of basin weights is
      essentially closed: the uniform ensemble is exactly uniform on 625
      oriented cells after three ticks, and membership is invariant
      afterwards. What is not decided is why physics would read the
      unoriented quotient, or pick any single point of Delta^624.
open  ATTRACTOR-OBSERVABLE-QUOTIENT. Now visibly related to the above: the
      mirror quotient IS one candidate observable quotient, and the question
      is whether the decoder realises it.
open  ENTROPY-LAYER-BRIDGE [O]. Untouched on the source side.
open  ARCHIMEDEAN-ENTROPY-CARRIER, composition, Bell. Untouched.
```

## Corrected maximum-entropy statement

The earlier claim that the maximum-entropy measures of U_hat x M_J are
exactly 313 products was wrong twice. Corrected:

```
ex M_max = { nu_p x m_Haar : p in F_5^4 },   |ex M_max| = 625
M_max    = conv of that set,  isomorphic to Delta^624
```

Maximum entropy fixes the Haar torus factor and forces the product structure
by K-disjointness. It does not select one of the 625 oriented streams, and it
does not select the barycentre. That is a separate principle and it is not
yet named.
