# HANDOFF-2026-08-21-SHARPNESS-AND-SCALE

```text
STATUS:      NON-CANONICAL handoff bundle. No authority.
AUTHORITY:   none. This bundle creates no claim, no Registry row, no
             evidence entry, no probe permission and no status change. It
             edits no normative file. BELL-CAUSAL-ACCOUNTING remains O with
             STOP. QDD-INSTRUMENT-NONSELECTION is quoted, not moved. No live
             H or O row moves anywhere.
CONTENTS:    one independent audit and one preregistered candidate, carried
             out in a single Cowork session on 2026-08-21, each with its
             preregistration frozen and hashed before execution, its own
             exact verifier, its own recorded stdout, and its own findings;
             plus one promotion proposal and one archived defective leg.
LAYER:       L1 state throughout. The audit is L1 algebra on the piston
             factor; the candidate is L1 arithmetic on the field. Neither
             lifts, and no lift is named or attempted.
DISCLOSURE:  the audit is RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT /
             NOT BLIND: it was written after reading the verdict text and
             claude/AUDIT-C-BELL-BETA-4_2026-08-21.md, with independent code
             and no import from either. The candidate is preregistered and
             computation-blind: nothing was computed before its freeze.
LEGS:        one, Linux x86_64 CPython 3.11.15. This is NOT the
             two-architecture gate of the public probe protocol. Every
             computation-grade row in this bundle is at most candidate-C.
```

## 1. Authority, and the basis this bundle used

Currency gate run at the start of the session against a fresh clone of
`mathorn1973/twist-j` `main`, not against a rendered page, an attachment or
the project snapshot:

```text
STATE:          ACTIVE
CANON:          Public Canon v58
AUTHORITY:      mathorn1973/twist-j main
CUTOVER:        2026-08-21
TAG:            canon-v58
CONTENT_COMMIT: 05a0749e95c1a3603a4ee8e3016d92b066d8c5e9
CANON_SHA256:   647822f56c807b6a49b069010b6ce968998f5543f568f230f6cdf2588be6acc1
CANON_BYTES:    304010
MAIN_AT_WRITE:  317d731 (Merge PR #486: activate Public Canon v58)
```

Verified, not assumed: `canon/SHA256SUMS` five of five OK; the recomputed
`sha256` and byte count of `canon/CANON.md` equal the declared fields; the
tag `canon-v58` and the content commit are both ancestors of `main`.

v58 activated the same day this bundle was written. Release 59 was in
preparation at the time. **Nothing in this bundle belongs in 59** and none
of it was written against 59. A later reader must re-run the gate rather
than trust the block above; the head moves and STATUS.md is the only
statement of what it is.

### Reach of this seat

```text
mathorn1973/twist-j        public, cloned and verified this session
mathorn1973/twistj-handoff PRIVATE, NOT REACHABLE from this seat. No
                           credentials. Not probed beyond one unauthenticated
                           ls-remote, which failed as expected.
mathorn1973/twistj-jam     PRIVATE, NOT REACHABLE from this seat. The v184
                           pin carried by the project contract could NOT be
                           confirmed against the repository. Nothing in this
                           bundle rests on the internal ledger, so no result
                           is affected, but a later session must not read the
                           project snapshot as a confirmed pin.
```

Pushing this bundle to `mathorn1973/twistj-handoff` is therefore an owner or
other-seat act, not something this session performed or could perform.

## 2. `bell-sharpness/`, the audit of the PASS-BRIDGE verdict

Question asked: does the prime-2 sharpness argument close the gap that
`claude/AUDIT-C-BELL-BETA-4_2026-08-21.md` named, namely
`||S_1||_F^2 = ||S_2||_F^2 = ||S_3||_F^2 = 2`.

Answer: no. It renames it. Verdict `PASS-ARITHMETIC / RENAMED, NOT CLOSED`.

Twenty of twenty independent gates hold. `Q(i)` is hand-rolled as ordered
pairs of `Fraction`; the built-in complex type is never used; no float is
formed in any assertion; sections 1 to 6 of the audited verdict are proved
symbolically over `Z[a,b,c,d]` rather than sampled. Every equation in the
audited verdict is correct.

The load-bearing finding is one line of Cayley-Hamilton:

```text
For any traceless 2x2 H over any commutative ring,
    H^2 = -det(H) I        and        Tr(H^2) = -2 det(H).
On the hermitian slice ||H||_F^2 = Tr(H^dagger H) = Tr(H^2), hence

    H^2 = I   <=>   det H = -1   <=>   Tr(H^2) = 2   <=>   ||H||_F^2 = 2.

Verified symbolically: H^2 = (x^2+y^2+z^2) I and
||H||_F^2 - 2 = 2(x^2+y^2+z^2 - 1). One equation, written twice.
```

So "the measured generator is sharp" and "the three generators carry one
common Frobenius norm equal to two" are the SAME condition on the class
where the verdict works. Correct labels: `[T]` on the equivalence as
algebra, `[D]` on the reading of it as a projective local read, `[O]` on the
derivation of either side from the architecture. The third has not moved.
The audited verdict's own `[STOP]` is correct, and for a stronger reason
than it gives.

Two of the audited claims come out stronger than stated, at no cost:

```text
the group <C_y, C_z> is order 24 with every element a signed permutation of
determinant +1, established by closure rather than asserted;

the four vanishing off-block entries of T are not a fact about real M.
M^T S M is symmetric whenever S is, and Tr(sym . antisym) = 0 in any
commutative ring of characteristic not two. The zero pattern is a transpose
identity, so section 6 of the verdict holds far beyond "real M".
```

### Three collisions with v58 that the audited verdict does not name

```text
1  PURE-QUBIT-RELATIONAL-CHSH [T] already optimizes "over Hermitian local
   observables with spectrum {+1,-1}" on an "externally supplied" scope.
   Sharpness is that row's own imported premise. A derivation cannot take
   its conclusion from a row that imports the conclusion as a premise. This
   makes STOP structural rather than contingent.

2  the proposed next gate C-BELL-V2-SHARP-APPARATUS-SELECTION-4C-N asks
   whether QDD projectors force the sharp phase gate. v58 answers in the
   other direction at L4: DEF-QDD-PROJECTOR-LOW is labelled
   "ALGEBRAIC_READOUT ... not claimed to be forced by J";
   QDD-PROJECTOR-PAIR-TR4 [T] is "linear algebra only ... no
   uniqueness-from-J"; QDD-INSTRUMENT-NONSELECTION [T] states it is "not an
   instrument-selection principle" and warns that "a coupling already
   controlled by the target projectors is circular as independent-selection
   evidence". Pinned as phrased, that gate walks into a standing [T] and a
   standing circularity warning, and is dead before first execution.

3  beta = 4 is already public and already labelled non-derived:
   DQRC-INTEGER-CENSUS-ARITHMETIC [T], DQRC-HORODECKI-REENCODING [T] and
   DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T] carry S_inf^2 = 4 + 16 Delta/Q^2,
   spec(T^T T) = {1, C^2, C^2} in Schmidt gauge, and S_inf = 2 sqrt2 on the
   maximal locus, each with "not an intrinsic derivation from J". The
   bridge of section 6 re-derives a public row.
```

### The next gate, re-scoped

```text
G1  name the layer at which a sharp local generator is supposed to be
    forced, and show it is NOT the L4 apparatus/support scope over V = Q^4
    where QDD-INSTRUMENT-NONSELECTION lives. An unnamed layer lift is a stop
    condition, not a gate.
G2  state the exact scope boundary of QDD-INSTRUMENT-NONSELECTION: what does
    it not quantify over. If nothing, beta = 4 is not derivable on this
    route and the row should say so.
G3  only then: does anything in the architecture force det(Gamma_2) = -1
    rather than det(Gamma_2) = -t^2. Everything else in the chain is exact
    and has now been checked by three independent code paths.
```

## 3. `scale-minimal-field/`, the candidate C-SCALE-MINIMAL-FIELD-1

Origin: the Boolean meta-layer question, whether "anchor + distinction +
join + closure" selects `p = 5`. The Boolean half was preregistered as a
DEFEAT before any computation, and it lost as preregistered.

```text
[T]  {1, XOR, AND} is functionally complete; every f:{0,1}^n -> {0,1} has a
     unique algebraic normal form. Verified exhaustively for n = 1,2,3:
     4, 16 and 256 truth tables, all attained, none twice.
[T]  a + b = (a XOR b) + 2(a AND b), and integer addition is the ripple of
     those two operations. Verified on all 4096 pairs of six-bit integers.
[T]  Boolean completeness alone creates no time and no dynamics: it is a
     language for F in x_(n+1) = F(x_n), never the ordering.
[F]  "anchor + distinction + join" selects p = 5. FALSIFIED. Every finite
     structure has a bit encoding. Universal representability has exactly
     zero selection power.
```

What survives is the last arrow, once the closure requirement is named in
the program's own vocabulary: the structure must admit a SCALE, that is a
unit of infinite order. A ring whose only units are roots of unity carries
phase and no scale.

```text
[candidate-T]  S1. Among ALL number fields with a unit of infinite order
               (unit rank r_1 + r_2 - 1 >= 1), Q(sqrt5) is the UNIQUE
               minimizer of absolute discriminant, at 5, with fundamental
               unit phi.
[candidate-T]  S2. Among ALL cyclotomic fields with a unit of infinite
               order, Q(zeta_5) is the UNIQUE minimizer, at 125. The orders
               n = 5 and n = 10 present the same field.
```

All exact, no float, no discriminant table lookup: Minkowski with a rational
under-approximation of pi gives 13 at degree 3, 44 at 4 and 986 at 6, with
step ratio `(1 + 1/m)^m sqrt(pi/4) > 1.76 > 1`, so the bound is strictly
increasing and the tail is closed by argument rather than by sampling. The
cyclotomic discriminants are computed twice, once from the
conductor-discriminant formula and once as the determinant of the trace form
on the power basis, agreeing for `n = 3..24`. Independent corroboration of
the degree tail: the least absolute discriminant over all irreducible monic
cubics in `[-6,6]^3` is 23, at `x^3 - 5x^2 + 4x - 1`.

This is a THIRD answer to "why five", in the same genre as the two v58
already carries in `canon/CORE.md`, and in a much less engineered class:

```text
v58 ramification answer   total-ramification locus of full quartic
                          cyclotomic fields is {(K_5,5),(K_8,2)}
v58 minimum answer        minimal absolute discriminant in the abelian
                          Galois CM unique-even-bit class, at 125
this candidate            minimal absolute discriminant among fields that
                          admit a scale at all: 5 for the real field, 125
                          for the cyclotomic one
```

It carries the same defect as the other two, stated in the preregistration
rather than discovered afterwards:

```text
[BREAK SUCCEEDS, intended]  the selection power is in the REQUIREMENT, not
in the minimization. Demand extra torsion instead of a scale and the same
minimization returns absolute discriminant 3 and the number three. Demand a
square root of minus one and it returns four. The class is chosen. That
caveat must travel with the row exactly as it travels with the other two.
```

### The element, settled negatively

```text
[candidate-T, negative]  The four elements 1 + zeta_5^a, a = 1,2,3,4, are
Galois conjugates sharing one minimal polynomial over Q,
        x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1),
hence equal norm 1, equal trace 3 and equal Tr(u^k) for every k, verified for
k = 1..12 and by the characteristic polynomial itself. Therefore NO rational
invariant of Z[zeta_5] distinguishes J = 1 + zeta_5^2 from 1 + zeta_5. The
choice of J is a choice of archimedean embedding together with the choice of
the contracting representative, abs(1 + zeta_5^2) = phi^-1 against
abs(1 + zeta_5) = phi. It is an orientation, not an arithmetic fact.
```

This is the part worth carrying forward. It is a limit, not a defeat: the
axiom carries exactly one irreducible convention beyond the field, and the
convention now has a name. It also forbids a whole class of future work: no
probe will derive the element from the ring alone. A row that has been
treated as open should be closed negatively instead.

Witness, exact: `J^10 = 89 + 55(zeta^2 + zeta^3) = 89 - 55 phi = phi^-10`,
that is `F_11 - F_10 phi`.

## 4. The archived defective leg

The first breaker run is kept, not deleted. Its leg BR4 used an
irreducibility test for monic integer cubics that never tested the root
zero, and therefore accepted `x^3 - x^2 + x = x(x^2 - x + 1)` and reported a
spurious cubic of absolute discriminant 3, which would have broken the
degree tail. Corrected in `breaker_scale_minimal_field_1b.py`, which reports
the correct 23. Both files and both stdouts are in the bundle. The defect
was in the breaker, never in the claim, and the claim was not weakened to
accommodate it.

## 5. What a reader may and may not take from this bundle

```text
MAY      the exact identities, the symbolic proofs, the recorded stdout, the
         Cayley-Hamilton closure argument of section 2, the three v58
         collisions, the re-scoped gate G1 to G3, S1, S2, the negative
         element result, and the archived defect.
MAY NOT  any status change. Every earned label here is a candidate label.
         Nothing is public T, nothing is evidence for a Registry row, and no
         summary may exceed the status or scope of what it summarizes.
         BELL-CAUSAL-ACCOUNTING is untouched and stays O with STOP. Nothing
         here supplies a source, settings, outcomes, a kernel, the
         factorization test, measurement independence, the no-signalling
         pair, the separate signalling test, the three gated bridges, or the
         dimensional audit.
```

## 6. Order for the next session

```text
1  Owner call on whether the sharpness step is relabelled in the probe
   record as a translation. The arithmetic does not change either way; only
   the headline of its section 3 does.
2  Re-scope the next Bell gate to G1 and G2 before anything is pinned. As
   currently named it collides with a standing [T].
3  After release 59, open a public probe P-SCALE-MINIMAL-FIELD-1 under the
   normal protocol: public issue claim, PREREG.md with the six fields pinned
   before first execution, verify.py under 120 seconds from repository root,
   two architectures byte-identical, EXPECTED.txt, RUN.md, RESULT.md.
   PROMO-C-SCALE-MINIMAL-FIELD-1.md is written to be consumed without
   reading anything else in the lane and carries the exact registry, CORE.md
   and frontier edits.
4  Independence is the point: a second author should attempt the
   counterexample by their own code path rather than re-running these files.
```

Adjacent and NOT claimed by this session, flagged only so a reader does not
rediscover it: contract open decision 4 (the Czech exposition head carrying
`Tr(C^2) = -21/8`) is recorded as factually resolved in
`claude/NOTE-SESSION-PUSH_2026-08-05.md`, the live value being `-881/8`; the
project instructions have not been updated to match, and updating them is
the owner's act.

## 7. Reproduction

Every program is Python standard library only, exact integer and `Fraction`
arithmetic, with no floating-point value formed in any assertion and no
built-in complex type anywhere. No program reads a repository checkout, so
none carries a sandbox path and every file hash is reproducible as shipped.
Frozen command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <file>
```

Each program was run twice with byte-identical stdout and empty stderr, on
Linux x86_64, CPython 3.11.15. One architecture only. A second architecture
leg is owed before any computation-grade row leaves candidate-C.

`SHA256SUMS` covers every file in this bundle except itself.

## 8. Inventory

```text
README.md                                          this file
VERDICT-PAIR-SHARPNESS-AND-BOOLEAN_2026-08-21.md   the verdict on both lanes
bell-sharpness/PREREG-AUDIT-BELL-SHARPNESS-CLOSURE-1.md  frozen before execution
bell-sharpness/audit_bell_sharpness_closure_1.py         independent audit program
bell-sharpness/audit_bell_sharpness_closure_1.stdout.txt 20/20 PASS, 0 findings
scale-minimal-field/PREREG-C-SCALE-MINIMAL-FIELD-1.md    frozen before execution
scale-minimal-field/verify_scale_minimal_field_1.py      primary verifier
scale-minimal-field/verify_scale_minimal_field_1.stdout.txt 20/20 PASS, 0 findings
scale-minimal-field/breaker_scale_minimal_field_1b.py    corrected breaker
scale-minimal-field/breaker_scale_minimal_field_1b.stdout.txt 5/7 survive, 2 intended
scale-minimal-field/ARCHIVE_breaker_scale_minimal_field_1_BR4-DEFECTIVE.py    kept
scale-minimal-field/ARCHIVE_breaker_scale_minimal_field_1_BR4-DEFECTIVE.stdout.txt kept
scale-minimal-field/PROMO-C-SCALE-MINIMAL-FIELD-1.md     the fold-ready proposal
SHA256SUMS                                         covers every file but itself
```
