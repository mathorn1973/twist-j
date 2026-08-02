# C-CENTRAL-LIFT-PHASE-1: the central phase of the lift (rev 1)

NON-CANONICAL. Incubation-lane candidate against Public Canon v30. No
authority, no Canon change, no canon/ file touched. This bundle promotes
the algebraic core of the accepted external audit of
notes/C-HERM2-BORN-CONE-1 (see AUDIT file there) from prose to exact
gates, and joins it to the integral glue of
notes/C-COMMON-CARRIER-ICOSIAN-1. It carries the theorem-grade content
the audit proposed for a probe P-CENTRAL-LIFT-PHASE-1, at candidate
level. All gates exact, deterministic, no randomness
(verify_central_lift_phase.py, 16 gates).

## Candidate claims

1. Branch pinning (CP1-CP2). The cosine data J + Jbar = J Jbar is
   branch-blind (Jbar satisfies it identically); the polarization
   J phi = zeta5 pins J = phi^-1 zeta5 and arg J = +2 pi/5. Audit
   correction 1, accepted and machine-checked.
2. Projective fifth power (CP3-CP4). zeta10 = -zeta5^3 has
   zeta10^5 = -1 exactly, so the principal spinor step s = zeta10/sqrt phi
   satisfies s^5 = -phi^-5/2: g_J^5 is a pure boost only in the
   projective Herm action; the spinor clears the central sign at ten.
   Audit correction 2, accepted.
3. Cone theorem (CP5-CP6). The characteristic polynomial of X is
   lambda^2 - 2t lambda + det X, proved by the 3^4 interpolation grid;
   with the 2x2 sum/product sign lemma, X >= 0 iff (t >= 0 and
   det X >= 0) is theorem-grade. Audit correction 3, accepted; the
   sampled M2/M3 gates of the Herm2 bundle are re-graded to audits.
4. One tick without square roots (CP7-CP8). The normalized Herm action
   of A_J = diag(J, 1) is exactly (u, v, w) ->
   (phi^-1 u, phi v, zeta5 w); its fifth power is the pure boost
   (phi^-5 u, phi^5 v, w). The loxodromic backbone tick needs no
   square root anywhere. Audit hidden finding, Herm part.
5. Central phase (CP9-CP10). A_J^2 = J diag(J, J^-1) exactly; the Sym
   slot gains the central phase zeta5^2 per two ticks while the Herm
   slots agree: the Herm slot is projective, the Sym slot sees the
   center. Audit hidden finding, Sym part.
6. mu_5 versus mu_10 (CP11-CP12). The unit-scalar central phase group
   {c^2/N(c)} over c = +-zeta5^a phi^b is EXACTLY mu_5; the glue phase
   1 - J = -zeta5^2 of the integral even tick (registered J-TENTH-ROOT)
   is a genuine tenth root outside mu_5: the central sign -- the bit --
   is available only through the glued integral step, never through a
   unit rescaling.
7. Tick ladder (CP13-CP14). res(J) = 2 (registered J_lambda,
   RAMIFIED-TM-LIFT), res(1) = 1: no unit multiple of diag(J, 1) meets
   the ramified glue criterion, so the ONE tick has no integral
   realization on the glued carrier; the det-1 four-tick
   diag(J^2, J^-2) is integral as the square of the twisted tick.
   The full ladder: half-tick over K(sqrt phi); one tick K-projective
   only; two ticks integral with the sign twist and tenth-root phase;
   four ticks integral untwisted; five double-ticks pure boost with the
   e-slot sign; ten pure.
8. Split-unit projectors and rigidity (CP15-CP16). (n.sigma)^2 = |n|^2 I
   grid-proved; P+- = (I +- n.sigma)/2 complementary determinant-zero
   idempotents, B = P+ - P- traceless with B^2 = I (audit ontological
   lemma). The rigidity lever off-diagonal cs(a+b) is a grid-proved
   polynomial identity; with cosh sinh = sqrt5/4 != 0 invariance forces
   b = -a, and the audit's common-carrier hypothesis is discharged at
   candidate level by C-COMMON-CARRIER-ICOSIAN-1.

## Status separation

candidate-T: all sixteen gates. [T, literature]: the 2x2 sum/product
sign lemma (finishes claim 3 in text). [D]: the tick-counter reading of
the ladder ("one physical tick realizes the Herm action of A_J" remains
candidate-D exactly as the audit graded it). [H]: identification of the
Sym central phase with a physical U(1) -- NOT claimed here; that is the
deferred dictionary probe (P-U1-DICTIONARY-1 territory), kept strictly
separate per the audit's instruction.

## Falsifiers

- F-CLP-1: any FAIL gate of verify_central_lift_phase.py.
- F-CLP-2: an exact unit scalar c with c^2/N(c) a primitive tenth root
  (would collapse the mu_5/mu_10 separation).
- F-CLP-3: an exact integral realization of a single tick on the glued
  carrier (would contradict the ladder; fires jointly with
  C-COMMON-CARRIER-ICOSIAN-1 gate T3).

No falsifier fired. No threshold moved. PROMO deferred.
