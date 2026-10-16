# Result

NON-CANONICAL / L1 / candidate-T written proofs, candidate-C finite audit.
First lane execution at pin `d085d7ad63401619911bd26a2da09df06be5a047`
passed (exit 0, empty stderr, one PASS line; see RUN.md).

## Established in this lane, in the stated scopes

1. **Construction.** For all 25 ordered pairs `(lam,mu) in F5^2`, the
   preparation of PROOF section 1 on unchanged `U` at `n=0` gives the
   common word `c,c,e`, the full checkpoint reset `x2=x0`, and under
   each of two fixed clock-free readers the output
   `BLANK, PRESENT(lam), BLANK, PRESENT(mu)` at `n=0,1,2,3` with
   `PRESENT(mu)` permanent for all `n>=3`. Readers: the author's
   piecewise `(z,T)` and the single cubic polynomial pair
   `(z, C(1-z^2) + A*z*D)`. `(z,T)` extends to an explicit bijective
   coordinate change of `F5^6`.
2. **Affine boundary.** No affine map into `F5^1` or `F5^2` with an
   arbitrary decoder realizes this pattern on this family (written
   proof, PROOF section 4). The displayed affine map into `F5^3`
   separates all labels. Minimal affine receiver dimension: exactly 3.
3. **Quadratic boundary inside two codes.** No message polynomial of
   total degree at most 2 in either named exact-message code; degree 3
   works in both. General quadratic pair with arbitrary decoder: open.
4. **Access classification.** On the exact 550-point required set
   (equal to the set of points the actual orbits visit), a function of
   a coordinate subset realizes the pattern iff the subset contains
   `q,r` and at least three piston coordinates. No four-coordinate
   access works; the canonical receiver block `(b,d,q,r)` fails at
   `n=1` by the displayed witness pair.

## Explicitly not established

- Both messages are pre-loaded in the preparation (`C(x0)=lam`,
  `D(x0)=mu`). This is a scheduled reveal under a fixed global reading,
  not later insertion, not source clearing or depletion, and not a
  transfer into a disjoint receiver subsystem.
- Preparation is admitted as an initial condition; production by a
  preceding native trajectory is not asserted.
- No funded contact `H_B`, energy store/accounting, physical
  instrument, occurrence law, layer lift, or Canon status change.
- No uniqueness or forcing claim over admissible readings. The
  dimension-3 affine decoder of item 2 is an arbitrary table on 125
  image values; the admissibility comparison between it and the
  two-coordinate cubic reader is precisely the open physical question.
- Section 6 is for this preparation family. A two-message construction
  with a common literal receiver block at `n=0` remains undecided.
- This lane's finite audit is one x86_64 Windows run by the owner
  session (RUN.md records the CRLF/LF framing note). Independent review
  by a distinct owner, and a Linux replay, remain separate steps.
