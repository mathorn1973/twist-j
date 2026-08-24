# PREREG-AUDIT-QDD-TERMINALITY-1

```text
KIND:      independent audit of the owner-forwarded bifurcation report on
           P-QDD-J-CENTRALIZER-TERMINALITY-1 (PR #462, merge 4ed6cb72).
           One named session, this audit only: AUDIT-QDD-CENTRALIZER-TERMINALITY.
AUTHORITY: none. Project-side audit. No repo edit, no registry motion, no
           canon change, no probe, no fold. NON-CANONICAL.
BASIS:     Public Canon v56 ACTIVE (gate passed earlier this session, clone
           HEAD 4ed6cb72 = the PR #462 merge commit; origin/main has since
           advanced to d525da09 by an unrelated probe merge; the probe
           directory and canon/ are byte-identical between the two, checked).
LAYER:     L4 apparatus/support only, matching the probe. No lift. O1, O2,
           sampling, L5, L6 untouched.
DATE:      2026-08-20
```

## Falsifiers first, each a first class outcome if fired

```text
QF1  pin or reproduction failure: any of PREREG.md (3274806f.., 17331 B),
     verify.py (992f1bcc.., 12450 B), exact_matrix.py (12b87e67.., 4216 B),
     EXPECTED.txt (sha equal to recorded stdout fc40a456.., 848 B, 23 lines)
     disagrees with the sealed RUN.md values in the clone; or the pinned
     verifier, run once from repository root under the frozen environment,
     exits nonzero, writes stderr, or produces stdout not byte-identical to
     EXPECTED.txt.
QF2  independent recomputation disagrees with any sealed identity: the phase
     motor D = M_J - I with M_J built from the axiom step; D^5 = I and
     D^T G D = G for G = I - (1/5) one one^T; simplex sum zero, Gram 4/5 and
     -1/5, u_2 = -one; the twenty affine maps, group law, G-orthogonality,
     rho(1,1) = D; stabilizer averages P_k rank 1 with image Q u_k, Q_k rank
     3; g_k order 4 with characteristic polynomial (x-1)(x+1)(x^2+1); the
     R, C, J multiplication table including J^2 = -C and J^sharp = -J;
     centralizer nullity exactly 3 at every token with {R, C, J} a basis;
     affine transport of R, C, J; the effect equation reduction
     T^sharp T = e^2 R + (r^2+s^2) C; Kraus completeness P + T^sharp T = I
     and cross term zero; the rational circle injection on the declared t
     list; repeatability Q_k T = T for every member; ray terminality passing
     exactly at +-Q with a mixed-line witness failing every sampled
     non +-Q member; strict idempotence solving to (1, 1, 0) exactly;
     target comparison last with P_2 = E_low and Q_2 = E_high.
QF3  the audit's added reduction fails: inside the frozen class,
     T^2 = +T or T^2 = -T must hold exactly for T in {+Q, -Q} and fail for
     every other sampled member; and R - C must satisfy T^2 = Q with
     Q != +-(R - C), the explicit non-terminal involution witness.
QF4  internal route disagreement: the simplex built from D powers disagrees
     with the affine representation route, or the coordinate algebra from
     the multiplication table disagrees with direct matrix computation.
```

## Field 1, audited claims and grades

The sealed probe carries its own two-architecture evidence; nothing here can
raise or lower it. This audit earns candidate labels only:

```text
QA1  reconstruction of the frozen class by fresh code, no import of the
     probe's helper                                        [candidate-T]
QA2  the negative route: infinite physical nonselection, repeatability
     nonselection, the four-member self-adjoint involutive subclass with two
     physical classes                                      [candidate-T]
QA3  the positive route: ray terminality gives +-Q only; strict idempotence
     gives +Q only; both by exact witnesses plus the written scalar lemma
                                                           [candidate-T]
QA4  target comparison last: P_2 = E_low, Q_2 = E_high     [candidate-T]
QA5  reproduction of the sealed verifier                   [reproduction]
QA6  added reduction: class-level idempotence T^2 = +-T is equivalent to
     T in {+Q, -Q}; hence the missing O2 premise can be stated as ONE
     post-state-class equation, weaker than strict idempotence and not
     quantifying over vectors                              [candidate-T]
```

## Field 2, code

One program, audit_qdd_centralizer_1.py: Python standard library, integers
and Fraction only, no float anywhere, fresh implementation (own Fraction
matrix kernel, no import from the probe directory), deterministic output,
exit nonzero on any FAIL. Reproduction of the sealed verifier by subprocess
from repository root under LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0 TZ=UTC.

## Field 3, carrier

(Q^4, G) and Fraction only. Frozen lists: tokens k = 0..4; t list for the
injection audit: 0, 1, -1, 1/2, -2, 3, 1/3, -1/5, 7/2; mixed-line witness
w = w_R + w_C with w_R a nonzero column of R_k and w_C a nonzero column of
C_k chosen by first nonzero column index, deterministic.

## Field 4, systematics

No tolerance, no retry. Sign conventions fixed by the prereg of the probe.
The scalar lemma (a linear map preserving every rational line of a space of
dimension at least two is scalar) is quoted as standard; the audit certifies
its use by exact witnesses on every sampled member rather than re-proving the
quantifier.

## Field 5, failure threshold

Any FAIL fires the corresponding QF and is archived; disagreement between
this audit and the sealed probe is diagnosed before being voiced as a
finding against the probe. Single platform: candidate labels only; no
summary may exceed the sealed probe's own scope (the frozen L4 class), and
nothing here closes or moves O2.

## Field 6, layer

L4 only. SAMPLING NOT PROVIDED is the only sampling statement.

## Order of operations

This file is frozen and hashed before the program is executed. Static
compile check only before the freeze. One formal run, stdout captured and
hashed, findings recorded as they fall.
