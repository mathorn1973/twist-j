# VERDICT on the pair: the prime-2 sharpness read, and the Boolean meta-layer

```text
STATUS:      INTERNAL, NON-CANONICAL. Candidate-lane verdict. No authority.
             Promotes nothing. Changes no public row.
BASIS:       Public Canon v58. Gate run this session against a fresh clone
             of mathorn1973/twist-j main:
               STATE ACTIVE, AUTHORITY mathorn1973/twist-j main,
               TAG canon-v58, CONTENT_COMMIT 05a0749e,
               CANON_SHA256 647822f5...6acc1, CANON_BYTES 304010,
               canon/SHA256SUMS 5 of 5 OK,
               tag and content commit both ancestors of main (HEAD 317d731).
DISCLOSURE:  RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND for
             half one. Preregistered and computation-blind for half two.
LEGS:        one, Linux x86_64 CPython 3.11.15. Not a two-architecture gate.
             Every computation-grade row here is at most candidate-C.
VERDICT:     half one  PASS-ARITHMETIC / RENAMED, NOT CLOSED
             half two  SELECTOR FALSIFIED / ONE CANDIDATE SURVIVES
```

## 0. The two headlines, before anything else

```text
half one   Every equation in the PASS-BRIDGE verdict is correct. 20 of 20
           independent gates hold. But the sharpness step does not close
           the gap the 2026-08-21 audit named. On the class where the
           verdict works, sharpness and the equal-norm condition are the
           SAME equation, by one line of Cayley-Hamilton. The verdict
           translates the open obligation into measurement vocabulary. It
           does not discharge it. STOP is right, and for a stronger reason
           than the verdict gives.

half two   {1, XOR, AND} is functionally complete, and that is exactly why
           it selects nothing. Preregistered as a defeat, and it lost.
           What survives is different and sharper: among ALL number fields
           carrying a unit of infinite order, Q(sqrt5) is the unique
           minimizer of |disc|, at 5. Among all cyclotomic fields carrying
           one, Q(zeta_5) is the unique minimizer, at 125. Both exact.
           Neither selects J. That last point is now settled negatively
           and should stop being carried as open.
```

---

# HALF ONE: the prime-2 Clifford read

## 1. What was independently checked

`audit_bell_sharpness_closure_1.py`, written from the verdict text alone,
importing no probe code and no prior-audit code. Q(i) is hand-rolled as
ordered pairs of Fractions; the built-in complex type is never used, and
no float appears anywhere. Sections 1 to 6 are re-proved symbolically over
`Z[a,b,c,d]` rather than sampled.

```text
A1   invariants of the single quarter-turn are exactly diag(a,b,a)   HOLDS
A2   hermiticity iff c purely imaginary; G_r = diag(1,r^2,1)         HOLDS
A3   (cK)^2 = I iff c = +-i;  E^2 - E = ((r^2-1)/4) I                HOLDS
A4   Clifford triple, Gram = I_3, <C_y,C_z> of order exactly 24,
     unique invariant symmetric form up to scale                     HOLDS
A5   eta hermitian, (1/2)Tr(eta eta') = xx'+yy'+zz', -det = |v|^2    HOLDS
A6   C = T except C_22 = -T_22; C^T C = T^T T; Spec = {Q^2,R^2,R^2}  HOLDS
A8   break attempt on the zero pattern: no counterexample            HOLDS
```

Two of these are stronger than the verdict states, and the strengthening is
free:

```text
A4b  the group is order 24 with every element of determinant +1 and every
     element a signed permutation. Verified by closure, not asserted.
A8b  the four vanishing off-block entries of T are not a fact about real
     M. M^T S M is symmetric whenever S is, and Tr(sym . antisym) = 0 in
     any commutative ring of characteristic not two. The zero pattern is a
     transpose identity. It holds over Z[a,b,c,d], over Q(i), and over any
     such ring. Section 6 is therefore true for far more than "real M".
```

## 2. The one finding that matters

The 2026-08-21 audit named the open obligation exactly:

```text
||S_1||_F^2 = ||S_2||_F^2 = ||S_3||_F^2 = 2
```

The new verdict claims the sharpness of the local measurement supplies it.
Test A7 asks whether that is a second condition or the same one.

```text
For any traceless 2x2 H over any commutative ring, Cayley-Hamilton gives

    H^2 = -det(H) . I           and       Tr(H^2) = -2 det(H).

On the hermitian slice ||H||_F^2 = Tr(H^dagger H) = Tr(H^2). Hence

    H^2 = I    <=>    det(H) = -1    <=>    Tr(H^2) = 2    <=>  ||H||_F^2 = 2.

Verified symbolically: H^2 = (x^2+y^2+z^2) I  and
||H||_F^2 - 2 = 2(x^2 + y^2 + z^2 - 1). One equation, written twice.
```

```text
[candidate-T]  On the traceless hermitian 2x2 class, "the measured
               generator is sharp" and "the three generators carry one
               common Frobenius norm equal to 2" are the SAME equation.
```

So the verdict does not close the audit's gap. It renames it. That is not
nothing: naming an unnamed normalization convention as a physical premise
is real work, because a premise can be attacked and a convention cannot.
But the label must be honest. The correct labels are

```text
[T]   the equivalence sharpness <=> equal norm, as algebra
[D]   the reading of that equation as "the local read is projective"
[O]   the derivation of either side from the architecture
```

and the third one has not moved. The verdict's own `[STOP]` is therefore
correct. Its section 3 headline, "the decisive condition is sharpness of
measurement", should read "the open condition, restated in measurement
vocabulary". Sections 1, 2, 4, 5, 6 and 7 stand as written.

## 3. Three collisions with v58 the verdict does not name

Read against the actual head, not against a recollection of it.

**3.1 The premise is already imported by the public row.**
`PURE-QUBIT-RELATIONAL-CHSH [T]` in v58 optimizes "over Hermitian local
observables with spectrum {+1,-1}", on an "externally supplied normalized
pure two-qubit scope in standard quantum mechanics". Sharpness is the
public row's own scope condition, supplied from outside. A derivation
cannot take its conclusion from a row that imports that conclusion as a
premise. This is a structural reason for STOP, not a contingent one.

**3.2 The next gate as phrased collides with two [T] non-selection rows.**
The proposed `C-BELL-V2-SHARP-APPARATUS-SELECTION-4C-N` asks whether QDD
projectors, Born halving and piston locality force the sharp phase gate.
v58 says:

```text
DEF-QDD-PROJECTOR-LOW    "ALGEBRAIC_READOUT, not a physical apparatus
                          selection, not a realized outcome, not a
                          post-state instrument, and not claimed to be
                          forced by J"
QDD-PROJECTOR-PAIR-TR4 [T]  "Linear algebra only; no apparatus, no
                          physical reading, and no uniqueness-from-J"
QDD-INSTRUMENT-NONSELECTION [T]  "...not an instrument-selection
                          principle. A coupling already controlled by the
                          target projectors is circular as
                          independent-selection evidence... No physical
                          selector, L5 realized-event stream, L6 measure,
                          decoder completion or SI statement"
```

The gate must therefore either work at a scope other than the L4
apparatus/support scope over `V = Q^4` where the non-selection theorem
lives, and NAME that lift, or it must target the scope boundary of
`QDD-INSTRUMENT-NONSELECTION` itself. As currently phrased it walks into
a standing `[T]` and a standing circularity warning. Pinned in that form
it is dead before first execution.

**3.3 beta = 4 is already public, and already labelled non-derived.**
`DQRC-INTEGER-CENSUS-ARITHMETIC [T]`, `DQRC-HORODECKI-REENCODING [T]` and
`DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]` already carry
`S_inf^2 = 4 + 16 Delta/Q^2`, `spec(T^T T) = {1, C^2, C^2}` in Schmidt
gauge, and `S_inf = 2 sqrt2` on the maximal locus, each with the explicit
caveat "not an intrinsic derivation from J". The bridge in section 6 of
the verdict is a re-derivation of a public row, not a new one. The verdict
says correctly that it is not a new Horodecki result. It is also not a new
TWIST-J result. The only genuinely new content in half one is the
translation in section 3, and section 2 is worth keeping precisely because
it shows how large the untranslated family still is.

## 4. What the next gate should be

Not "do the projectors force sharpness". That question is already answered
in the direction of no, at L4, by a `[T]` row. The live questions are:

```text
G1  name the layer at which the sharp local generator is supposed to be
    forced, and show it is NOT the L4 scope of QDD-INSTRUMENT-NONSELECTION.
    A layer lift that is not named is a stop condition, not a gate.
G2  find and state the exact scope boundary of QDD-INSTRUMENT-NONSELECTION:
    what does it NOT quantify over. If nothing, beta = 4 is not derivable
    on this route and the row should say so.
G3  only then: does anything in the architecture force det(Gamma_2) = -1
    rather than det(Gamma_2) = -t^2 . Everything else in the chain is exact
    and already checked twice.
```

---

# HALF TWO: the Boolean meta-layer

## 5. The mathematics, confirmed, and then dismissed as a selector

Preregistered as a NEGATIVE before computing, then computed.

```text
[T]  {1, XOR, AND} is functionally complete. Every f:{0,1}^n -> {0,1} has a
     unique algebraic normal form. Verified exhaustively for n = 1,2,3:
     4, 16 and 256 distinct truth tables, all attained, none twice.
[T]  a + b = (a XOR b) + 2(a AND b). The half adder. Verified.
[T]  Integer addition is the ripple of those two operations. Verified
     exhaustively on all 4096 pairs of six-bit integers.
[T]  Boolean completeness alone creates no time and no dynamics. It is a
     language for F in x_(n+1) = F(x_n), never the ordering. That part of
     the note is correct and correctly caveated.

[F]  "anchor + distinction + join" selects p = 5.  FALSIFIED, as
     preregistered. Every finite structure has a bit encoding. Universal
     representability has exactly zero selection power. The right response
     to "everything is Boolean" is "yes, and that is the problem".
```

So the answer to the framing question is: the Boolean layer is not a
deeper axiom under TWIST-J and cannot become one. It supplies the arrow
`1 -> (XOR, AND) -> N -> integer algebra` and stops. All the selective
work is in the last arrow, and that arrow is not Boolean.

## 6. What survives, and it is worth having

Name the closure requirement precisely and the last arrow becomes a
theorem. The requirement that carries the program's own vocabulary is not
"closed" in the abstract. It is: **the structure must admit a scale**, that
is, a unit of infinite order. Modulus to gravity and scale is the program's
own reading of the J-projection; a ring whose only units are roots of unity
has phase and no scale, and cannot carry it.

```text
C-SCALE-MINIMAL-FIELD-1, frozen and computed this session.

[candidate-T]  S1. Among ALL number fields with a unit of infinite order
               (unit rank r_1 + r_2 - 1 >= 1), Q(sqrt5) is the UNIQUE
               minimizer of |disc|, with |disc| = 5.

[candidate-T]  S2. Among ALL cyclotomic fields with a unit of infinite
               order, Q(zeta_5) is the UNIQUE minimizer of |disc|, with
               |disc| = 125. (n = 5 and n = 10 present the same field.)
```

Proof shape, all exact, no float and no table lookup:

```text
degree 1        Q has unit rank 0.
degree 2        imaginary quadratic has rank 0; real quadratic has rank 1;
                the least positive fundamental discriminant is 5, at
                Q(sqrt5), uniquely. Checked over all squarefree |d| <= 200
                and independently over all form discriminants |D| <= 400.
degree >= 3     Minkowski with a rational under-approximation of pi gives
                |disc| >= 13 at degree 3, >= 44 at 4, >= 986 at 6, and the
                bound is strictly increasing: the step ratio is
                (1 + 1/m)^m sqrt(pi/4) > 2 . 88/100 = 1.76 > 1, exactly.
                Independent corroboration: the least |disc| over all
                irreducible monic cubics in [-6,6]^3 is 23, at
                x^3 - 5x^2 + 4x - 1.
cyclotomic      rank >= 1 iff phi(n) >= 4; phi(n) = 4 holds for exactly
                n in {5,8,10,12} with |disc| 125, 256, 125, 144; degree >= 6
                is excluded by the same bound at 986 > 125. The
                discriminants are computed twice, once from the
                conductor-discriminant formula and once as the determinant
                of the trace form on the power basis, agreeing for
                n = 3..24.
```

This is a THIRD answer to "why five", in the same genre as the two v58
already carries in `canon/CORE.md`, and in a much less engineered class:

```text
v58 ramification answer   total-ramification locus of full quartic
                          cyclotomic fields is {(K_5,5),(K_8,2)}
v58 minimum answer        minimal absolute discriminant in the abelian
                          Galois CM unique-even-bit class, at 125
this candidate            minimal absolute discriminant among fields that
                          admit a scale at all, at 5 for the real field
                          and 125 for the cyclotomic one
```

It carries the same defect the other two carry, and the defect is stated in
the preregistration rather than discovered afterwards:

```text
[BREAK SUCCEEDS, intended]  The selection power is in the REQUIREMENT, not
in the minimization. Demand extra torsion instead of a scale and the same
minimization returns |disc| = 3 and the number three. Demand a square root
of minus one and it returns four. The class is chosen, not derived. This
is exactly the caveat v58 already attaches to both existing answers, and it
must travel with this one.
```

## 7. The element, settled negatively

The verdict-relevant part. S1 and S2 select the FIELD. They do not select
`J`. That has been carried as open. It should not be: it is closed, and
closed against us.

```text
[candidate-T, negative]  The four elements 1 + zeta_5^a, a = 1,2,3,4, are
Galois conjugates. They share one minimal polynomial over Q,

        x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1),

hence identical norm 1, identical trace 3, and identical Tr(u^k) for every
k. Verified for k = 1..12 and by the characteristic polynomial itself.

Therefore NO rational invariant of the ring can distinguish 1 + zeta_5^2
from 1 + zeta_5. The choice of J is a choice of archimedean embedding
together with a choice of contraction over expansion: |1 + zeta^2| = phi^-1
and |1 + zeta| = phi. It is an ORIENTATION, not an arithmetic fact, and no
future probe will derive it from Z[zeta_5] alone.
```

That is a real result and it is a limit, not a defeat. It says the axiom
`J = 1 + zeta_5^2` carries exactly one irreducible convention beyond the
field, and names it: which way time contracts. The program already reads
that as the arrow of scale. Saying so explicitly is stronger than leaving
the row open and hoping.

Witness, exact and pleasant:

```text
J^10 = 89 + 55(zeta^2 + zeta^3) = 89 - 55 phi = F_11 - F_10 phi = phi^-10.
```

---

## 8. Pins

```text
PREREG-AUDIT-BELL-SHARPNESS-CLOSURE-1.md
    83dde6936a5264cc22c42cca886be67119f211143abde32820d589c5d239affc
audit_bell_sharpness_closure_1.py
    8a4b9a7dec58452b3b369ea0b48ceb55feb15bd8db2fc3f649cfd6110ba3948f
  stdout (20 of 20 PASS, 0 findings, exit 0)
    d5c0441638184a6e6021106aeb5e80607b15d2fb5ab419bf44f5fbac16168fe1

PREREG-C-SCALE-MINIMAL-FIELD-1.md
    bc1ce96f63dd9086d3b090ffcda1ea881687a4508fcec13467fb64a51a570d77
verify_scale_minimal_field_1.py
    30f72a22d0974efcd4a6dbfc2dbd0878f74c7e35e23ffa5129922c393c755496
  stdout (20 of 20 PASS, 0 findings, exit 0)
    6d16ac8aa31ee056b4fbc9fa499bce19a16b7ea7c5ff8af25e231a564a44ef23
breaker_scale_minimal_field_1b.py
    b943625fbd300e018a07c5f2183cb475b349316d42eed2918848afcec0e27670
  stdout (5 of 7 survive, 2 intended framing breaks)
    2948277523f7c4673ac34441b4eb2dfd995e56f9c18e7f1af793a35c85a93188

Archived, not deleted: the first breaker run. Its leg BR4 used an
irreducibility test that never tested the root zero and so reported a
spurious cubic of |disc| = 3. Corrected in 1b, which reports 23. The
defective file is kept.
ARCHIVE_breaker_scale_minimal_field_1_BR4-DEFECTIVE.py
    3cda84fe287e34795a2ebaf64dec63788a3c45a86ba925b699c37df37247b79d

Environment: Linux x86_64, CPython 3.11.15,
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Every script run twice with byte-identical stdout and empty stderr.
Single architecture, so computation-grade rows stay at most candidate-C.
```

## 9. What this does NOT do

```text
No public row moves. No promotion. Nothing here belongs in release 59:
one leg, no public preregistration, no two-architecture gate. If
C-SCALE-MINIMAL-FIELD-1 is wanted publicly it goes through a normal probe
after 59, as PROMO-C-SCALE-MINIMAL-FIELD-1, targeting the "Why five"
section of canon/CORE.md with S4 attached as its own non-selection caveat.

BELL-CAUSAL-ACCOUNTING stays [O]/STOP. Nothing in half one supplies a
source, settings, outcomes, a kernel, the factorization test, measurement
independence, the no-signalling pair, the separate signalling test, the
three gated bridges, or the dimensional audit. Half one does not touch
that obligation and does not claim to.

No layer lift is performed anywhere in this document. Half one is L1
algebra on the piston factor. Half two is L1 arithmetic on the field.
```
