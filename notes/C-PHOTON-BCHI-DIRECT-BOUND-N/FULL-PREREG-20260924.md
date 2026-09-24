# Prospective full-measure extension audit, 24 September 2026

PUBLIC, NON-CANONICAL. C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Apache-2.0. Public Canon v91.
Base main: `af6afcc732ef2daa89e2a0a2a2bb4e02644de8e3`, after #1158.

The analytical attempt extends the two-copy argument to its complete sum
law and derives evaluated full-measure bounds. It also constructs an
unsaturated conditional obstruction, a complete sector with zero transverse
response, and a summable specified class of current loops. It does not
claim a uniform bound on the complete signed covariance or a positive P1
margin. This is a notes audit, not a formal P-probe.

## Prospective public pin

Before the first scientific execution, publicly commit and read back this
file, FULL-MEASURE.md and the complete verify_full_measure.py. Record the
immutable commit and their SHA-256 hashes. The sole imported local helper
is the unchanged verify_connected_current.py from #1156, SHA-256
`ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403`.
Read it back and check its hash from that same commit. Its main audit is
guarded and does not run on import.

No scientific execution may precede the pin. Static source review and AST
syntax parsing are allowed. The seven loop fixtures are specified below;
they were constructed analytically, not selected after running the source.

Environment: Linux x86_64, Python 3, standard library only, integers and
Fraction throughout the scientific calculation. From the note directory:

```
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_full_measure.py
```

Budget: 60 seconds, including a subprocess timeout of 55 seconds.
Require exit zero, empty stderr and the final line

```
RESULT PASS; full signed covariance and positive P1 margin remain unproved
```

Preserve the first execution, exact stdout, environment, hashes and byte
counts in FULL-RUN-20260924.md. Recheck all inputs afterward. Wall-clock
duration is environment metadata, not a scientific floating-point output.

## Frozen finite targets

1. For D=5,7,9 and L=2D+4, construct the actual aligned S and connected
   neutral background B from cubical boundaries. Require |S|=4D+40,
   |B|=12D-14, partial B=0, ternary coefficients, disjoint face supports,
   and common edges exactly the interior cap boundaries. B has degree two
   at every occupied edge.
2. Remove the designated caps, derive every necessary equality from the
   remaining degree-two and degree-five edges, and require exactly D+3
   color components: the D+2 original segments and one connected B part.
   At each cap test all local triples (left,right,Y) and every permitted
   ternary value against all four actual modulo-five edge equations.
   Require exactly the value left-right+beta*Y when it is permitted.
3. Enumerate all binary segment colors and both background colors for
   D=5,7,9, retaining precisely the allowed cap assignments. Build both
   actual fields; check ternarity, sum, full boundary, current and support
   weight. Require no saturated designated cap, zero mean difference
   currents, and exactly 8 F_(D+2) local pairs. With N=16D+26,
   require Z_local=25 F_(D+2)/2^(N+3),
   signed numerator=9 F_(D-4)/2^(N+3), and their ratio
   (9/25) F_(D-4)/F_(D+2).
   The counts are 104,272,712 and ratios 9/325,9/425,9/445.
4. For D=3,5,9, form the alternating signed C_i pair with every cap
   saturated. Derive its connected orientation graph from the actual
   incidences, require exactly two local pairs, verify both fields and
   their weights, and require difference-current moment exactly one.
5. Exhaust the 3^6 ternary incidence tuples at one charged edge and require
   precisely six patterns per sign: five equal incidences and one zero.
   For L=4,6,8 construct the specified alternating current j*, derive the
   forced zero 01 faces by conflicting sign demands, and force all five
   remaining incidences at each charged edge. Require 9V/2 fixed occupied
   faces. Derive the residual 23 equality graph and require L^2 components
   of L^2 faces each, exactly the independently assignable planes.
   For plane assignments zero, plus, minus and checkerboard, check actual
   boundaries, ternarity, occupied-face count and every 02 axial slice
   sum equal to zero.
6. For those L, check the complete sector partition factor
   2^(-9V/2)(1+2^(1-L^2))^(L^2), its stated upper bound, the eight
   plaquette-independent edge colors of size V/2, and the exact density
   constant (12/11)^4/(3/2)=13824/14641<1. Check
   6^12/11^11<1/121 without floating-point square roots.
7. Derive the loop constants from cosh(k log3)=(3^k+3^(-k))/2. Require
   a=15625/177147, r=41/25, q=a(1+6r)=169375/177147<1 and
   2ra/(1-q)=25625/3886. Check the elementary cosh inequality for
   multiplicities 0,1,2,3,4.
   Also check (73/70)^12>14173/8575>41/25 using the stated truncated
   binomial sum, q_contact=q*(73/70)=2472875/2480058<1, and
   2ra*(73/70)/(1-q_contact)=748250/7183. These certify the written
   extension from the earlier length/24 contact budget to length/12.
8. Build seven simple closed walks from their stated step lists, then
   independently compute every incident plaquette's four edge incidences,
   multiplicity m, curl, corners c and opposite-edge pairs O. Require
   sum m=6 ell, sum binomial(m,2)=c+O, the direct rational source weight
   at most a^ell r^(c+O), and the sign-sensitive refinement stated in the
   proof. The fixtures are: 1x1 square, 2x2 rectangle, 2x3 rectangle,
   1x3 rectangle, the eight-step bent 3D cycle, the length-six straight
   winding cycle, and the sixteen-step parallel-contact 3D cycle.
   The complete step lists are frozen in the source. The last cycle must
   contain a pair of opposite signed incidences whose curl cancels.

## Scope and failure handling

The universal prescribed-face probability bound, factorial-moment
expansion, full-measure loop probability and loop-counting tail, arbitrary
volume sector classification, dense-sector removal, and all-distance
Fibonacci obstruction are written analytical proofs. This execution
checks their stated finite inputs and incidence structure. It does not
enumerate the complete lattice measure, measure chi or b, select a
favorable limit profile, or prove P1 by finite testing.

Any failed assertion, unexpected stderr, nonzero exit, timeout or hash
mismatch remains attached to this unchanged pin. Do not silently repair
the frozen source or change the targets. A correction requires a new
public pin and an explicit disposition of the first attempt.

Separate agents have reviewed the derivations using shared sources; this
is not blind external review. The written results remain candidate-T;
the finite one-architecture audit is candidate-C. Ordinary repository CI
does not run this notes audit on a second architecture. Canon, Registry,
workflows, formal probes and all earlier pins stay unchanged. P1 is OPEN.
