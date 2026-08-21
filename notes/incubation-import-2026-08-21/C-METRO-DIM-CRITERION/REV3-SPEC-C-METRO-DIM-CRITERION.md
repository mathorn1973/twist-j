# REV3 SPEC: C-METRO-DIM-CRITERION-1-REV3

Specification only. **Not preregistered, not run.** Whoever picks this up
preregisters it fresh on the target machine and pins the SHA-256 before opening
data or computing. Do not reuse the rev2 pin.

Revised 2026-07-25 after readback. Changes from the first draft are marked.

## 0. Why rev3 exists, and what it may not touch

rev2 fired `F-MDC2-SUBSUME` on gate N1. That fire falsifies **the gate**, not
clause (A) and not clause (A'). rev2's threshold does not authorize a repair for
it, so the disciplined move is a new preregistration with a new pin and a stated
reason.

```
DO NOT touch clauses (A'), (B), (C), (D).
DO NOT touch the allowed list R1, R3, R5 or the forbidden list R4, R6.
DO NOT touch any gate that passed: N2, N3, N4, N5, N6, N7.
DO NOT register rev1 or rev2 as public F rows. They are archived candidate-F
       fires. No public claim was refuted because none was made.
```

## 1. The defect: a quantifier-order conflation

rev1's clause was universal, rev2's is per vector:

```
A(P)   = for all w, C(P, w)     rev1
A'(P, w) = C(P, w)              rev2
```

rev2's N1 asserted that `A'(P, w_alldistinct)` equals `A(P)`. That conflates a
universal statement with one instance of it. Eight exact counterexamples.

## 2. The corrected gate (CHANGED after readback)

The first draft proposed enumerating `w` over `{0,1,2}^S`. That family is
separating but redundant. **State indicators suffice, and the reverse direction is
a theorem, so it needs no enumeration.**

```
THEOREM (indicator separation). Let R be a terminal class of period p >= 2, with
cyclic layers L_0,...,L_{p-1} and layer stationary vectors pi^(j) of mass 1. The
layer functionals a^(j)(w) = sum over s in L_j of pi^(j)_s w_s have pairwise
disjoint supports, because the layers partition R. Take s in L_i and w = e_s.
Then a^(i)(w) = pi^(i)_s > 0 while a^(j)(w) = 0 for every j != i. Since p >= 2
such a j exists, so the layer averages are not all equal and (A') is false.
Hence every indicator of a state in a periodic terminal class separates.
```

So N1 splits into a proved direction and a proved converse, each with an
enumeration that acts as a control on the code rather than as the evidence:

```
N1a FORWARD   every terminal period = 1  =>  (A') holds for every w.
              Already verified in rev2: 966 automata, 0 violations. Keep as is.

N1b REVERSE   some terminal period p >= 2  =>  (A') is false at w = e_s for
              EVERY s in that class. Proved by the theorem above. The
              enumeration is a code control, not the evidence.
              Readback check already run, exact: 306 (automaton, periodic-class
              state) pairs over (2,1,|S|<=3), (2,2,|S|<=2), (3,1,|S|<=3),
              0 failures; and 0 automata with a periodic terminal class
              separated by no indicator.

              Preregister the tested family as the |S| state indicators. Do NOT
              enumerate {0,1,2}^S; it is redundant and buys nothing.
```

## 3. New gate: w-transport through R3, standalone (NEW after readback)

R3 invariance must not fold the transport of `w` into the verdict comparison.
Split it, because the two failures have different dispositions: a transport
failure means the reduction was misapplied, an invariance failure means the
criterion is presentation-dependent.

```
N2a W-TRANSPORT   for every delta-stable partition refining the level sets of w:
                  assert that w is constant on every block, so that w_quot is
                  well defined, and assert the transport identity
                      (P^m w)(s) = (P_quot^m w_quot)(block(s))  for m = 0..M
                  on a declared finite M, exactly over Q. This is its own gate
                  and is checked BEFORE any verdict comparison.

N2b R3-INVARIANCE only after N2a passes: the verdict triple
                  (converges by (A'), constant, L) is unchanged by the quotient.
                  rev2 result to reproduce: 4702 cases, 0 violations.
```

## 4. New registrable gate: the separation fact, split by grade (CHANGED)

The first draft bundled two claims of different evidential grade. Separate them.

```
N8a INLINE-WITNESS   architecture-free, provable from the matrix alone.
    There exists an accessible (q,d)-DFAO with a period-2 terminal class whose
    all-distinct output vector converges while another output vector does not:
      q = 2, d = 1, |S| = 3, delta = (1,1,0,2,1,1)
      B = [[0,2,0],[1,0,1],[0,2,0]], row sums 2
      terminal class {0,1,2}, period 2, cyclic layers {0,2} and {1}
      w = (0,1,2): layer averages 1 and 1; P^m w = (1,1,1) for every m >= 1
      w = (0,0,1): layer averages 1/2 and 0; P^m w oscillates forever between
                   (0,1/2,0) and (1/2,0,1/2)
    Verifiable by hand. No enumeration, no platform, no second architecture.
    This is the part a fold can carry without the aarch64 leg.

N8b CENSUS           computational, second architecture REQUIRED.
    Exactly 8 of the 879874 automata of BOX-A have the N8a property. Pin the
    eight as a frozen regression list.
```

## 5. Runtime guidance, from measurement

rev2 ran in 24.9 s once the convergence-only path existed.

```
Name the convergence-only path IN THE PREREGISTRATION this time. rev2 added it
after its freeze and had to disclose it afterwards. It computes clause (A') and
skips the (B)/(C) stationary solves, returning immediately when every terminal
period is 1, which is about 99.9 percent of BOX-A.

Declare the coverage of any w-enumerating gate as an explicit sub-box and print
it. Silent narrowing is a failure; a declared cap is not.
```

## 6. What rev3 must not do

```
do not narrow the allowed reduction list a third time. If an allowed reduction
fires again, the honest conclusion is that no presentation-invariant criterion of
this shape exists for the class, and the disposition is a negative result on the
class, reported as such;
do not claim closure of METRO-ADMISSIBILITY;
do not claim any discrepancy bound, Folner statement, selector theorem, or
L5-to-L6 lift. The L5-to-L6 gate belongs to the child row, not here;
do not claim the factorwise witness as new. It already exists in the METRO fork
note with a two-architecture pin. Only its placement as the R6 prohibition inside
a complete calculus is new;
do not cite, name, quote, or lean on the development line as authority. The words
sealed, internal, private, hidden and unpublished are machine forbidden in the
five hashed files.
```

## 7. Break round for rev3

Carry rev1's and rev2's break rounds forward unchanged, and add:

```
B8  independent proof check of the indicator-separation theorem: verify by a
    second code path that the layer functionals have disjoint supports on every
    periodic terminal class in the boxes, which is the theorem's only hypothesis.
B9  push BOX-A to |S| = 4 at (q,d) = (2,1) and (2,2) as far as the budget allows,
    declaring the covered part exactly, and hunt for a case where N1b fails.
    A failure would refute the theorem, so this is a real adversarial test.
B10 control: confirm the tested family still contains, under (A'), all three
    verdict types and at least one automaton whose convergence depends on w.
    rev2 found 37 such automata; a rev3 that finds none has broken something.
B11 transport control for N2a: construct a partition that is delta-stable but
    does NOT refine the level sets of w, confirm w_quot is ill defined, and
    confirm the gate refuses it rather than silently averaging.
```

## 8. Second architecture

Everything computational above is owed a byte-identical aarch64 leg before any
fold. Run `RUNME.sh` at the bundle root and diff against the x86_64 stdout in
`runs/`. N8a is the sole exception: it is an inline hand-checkable witness and
carries no platform dependence.
