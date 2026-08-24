# CORRECTION: owner review of AUDIT-QDD-CENTRALIZER-TERMINALITY

```text
Status      NON-CANONICAL correction by addendum. No pinned artifact of the
            first leg is altered. No threshold moved. O1 and O2 open.
            SAMPLING NOT PROVIDED.
Date        2026-08-20
Basis       Public Canon v57 ACTIVE, main 4ef54f0c, content commit 8e8b04ab,
            CANON_SHA256 c96a2ef5.., CANON_BYTES 295013.
Disclosure  RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
Decision    AUDIT-PASS on the correction leg, 8/8 chain gates and 5/5 proof
            inputs.
```

## 0. The order of events, stated first

The review is written as a PRE-RUN verdict: "audit jeste nespoustej". By the
time it arrived the audit had already been preregistered, frozen, executed
once, recorded and published to the project. The instruction could not be
followed as written, and pretending otherwise would be worse than saying so.

What that means for each item: the four corrections are accepted on their
merits and applied as an addendum, in the way POLICY treats a sealed object,
by adding a correction rather than editing a record. Two of them (the stale
basis, the loose QA6 wording) are defects in what was published and are
corrected below. Two of them (co-freezing the program, chain of custody) are
process gaps that the first leg cannot retroactively repair; they are
admitted, and the correction leg is run under the corrected procedure so the
repaired discipline exists in artifact form rather than only in prose.

## 1. Basis, corrected

Accepted. The public authority is Public Canon v57, not v56.

The published sentence

```text
the probe directory and canon/ are byte-identical between the two, checked
```

was true when written, for the pair 4ed6cb72 against d525da09, both of which
predate the v57 activation. It is false for the pair 4ed6cb72 against current
main 4ef54f0c. Carried forward without a timestamp it misleads, so it is
withdrawn and replaced by the pair statement, machine-checked as gate CH8:

```text
the audited probe directory is byte-identical between its sealed merge and
current main;
canon/ is NOT byte-identical, because Public Canon v57 has since activated;
QDD-INSTRUMENT-APPARATUS remains O, unchanged in selection and sampling
boundary.
```

Verified independently here: v57 adds five closed rows (`J-MAHLER-MEASURE`,
`REGULATOR-TWO-LOG-PHI`, `CYCLOTOMIC-CLASS-NUMBER-ONE` at T,
`J-TORAL-PERIODIC-POINTS`, `METRO-FORBIDDEN-WITNESSES` at C) and changes the
scope text of exactly one existing row, `METRO-REDUCTION-CALCULUS`, which
stays at O. No live row moves. The owner's reading is confirmed on all
points.

The audit's conclusions do not depend on Canon prose, and every sealed object
it checked is unchanged, so the corrected basis changes no result of the
first leg.

## 2. Co-freezing the program: gap admitted, procedure repaired

Accepted. The first leg's preregistration froze "this file" and named the
program only by description. What actually happened is narrower than a
freeze: the program was statically compiled and its SHA-256 computed in the
same shell invocation that then executed it, so the hash does pin the
executed bytes, but it was not published before execution and the
preregistration did not bind it. That is exactly the gap the review names.

Repaired for this leg. `PREREG-AUDIT-QDD-TERMINALITY-1-CORRECTION.md` and
`audit_qdd_chain_1.py` were frozen together, checked only by `ast.parse` with
no import and no execution, and pinned before the single run:

```text
prereg_sha256:   56e1d4701816f6dc3a8e46c9273786a0223b95b5f3c8308e93e479f724f85430
prereg_bytes:    6424    lf 147   cr 0   final_lf yes
code_sha256:     244b0b8846f26423d127b4f7bc0e9211ab24dd5497ff0d23e7d055cbefdaba24
code_bytes:      11892   lf 358   cr 0   final_lf yes
basis_commit:    4ef54f0c34f80897af0121a2d93b710e70a8377c
audited_merge:   4ed6cb72ab1110b68ed0574115e9dacbaf65e954
timeout_seconds: 120
formal_audit_executions at pin time: 0
stdout_sha256:   fee39189a805a45b43df00caa971c4193b25c88f690c5dbd379309b3e0b74de8
stdout_bytes:    1390    exit 0    stderr 0 bytes
```

The audit files live outside the audited worktree, which stays clean.

## 3. Chain of custody, added and passed

Accepted; the first leg checked file hashes only. Gates CH1 to CH8 now check
the history, and all pass:

```text
CH1  e1cf7394 is an ancestor of 936a396d, aef78f68 and 4ed6cb72
CH2  the three pinned blobs are identical at all four commits
     (PREREG 582a8383, verify 50a54fae, exact_matrix 245372ba)
CH3  EXPECTED.txt, RUN.md and RESULT.md do not exist at the pin
CH4  no pinned file changes in any commit after the pin up to the merge
CH5  current-main copies of all six sealed files equal the merge copies
CH6  the audit checkout worktree is clean
CH7  the audit checkout HEAD is exactly 4ed6cb72, the audited merge
CH8  the basis pair of section 1
```

CH7 answers the review's point 8 for the first leg as well: that leg ran from
a clone whose HEAD was exactly the audited merge, never from a moving main.
That was true but unrecorded; it is now recorded and checked.

## 4. QA2: the universal proof, adopted

Accepted. Nine sampled `t` are a regression check, not a proof of
infinitude. The proof, frozen:

For `e_t = 1`, `r_t = (1-t^2)/(1+t^2)`, `s_t = 2t/(1+t^2)` we have
`r_t^2 + s_t^2 = 1`, and for every finite rational `t`

```text
1 + r_t = 2/(1+t^2) != 0,
```

so the parameter is recoverable as `t = s_t/(1 + r_t)`. Hence
`T(t) = T(u)` forces `t = u` by uniqueness of the centralizer coordinates.
And `T(t) = -T(u)` is impossible, because comparing the `R_k` coefficient
gives `1 = -1`. Therefore `Q` injects into the post-state classes, which is
the infinitude claim.

Frozen with it, and machine-checked as PR1: `R` and `C` are self-sharp and
`J^sharp = -J`, so by linearity

```text
T(e,r,s)^sharp = e R + r C - s J.
```

Self-adjointness therefore forces `s = 0` with no sampling; with
`r^2 + s^2 = 1` this gives `r = +/-1` and `e = +/-1`, four algebraic members,
and modulo `T ~ -T` exactly two physical classes.

Label consequence, stated plainly: as executed, QA2 rested on samples plus an
unwritten argument, and on the review's standard that supports at most
`candidate-C`. With the two proofs above written and their matrix inputs
certified, QA2 stands at `candidate-T`. The first leg's label was ahead of
its written evidence; this addendum is what closes that gap.

## 5. QA3: the scalar lemma, written out

Accepted; there is no reason to cite it. If `T` preserves every rational
line, then for independent `u, v` there are scalars with `Tu = alpha u` and
`Tv = beta v`, while invariance of the line through `u + v` gives
`T(u+v) = alpha u + beta v = gamma (u+v)`; independence forces
`alpha = beta = gamma`, and running over a basis gives `T = lambda I`.

On `Q_k V`, which has dimension three, `T` is invertible by the effect
equation, so `v -> Tv` is onto and the ray condition
`T^2 v` parallel to `Tv` says exactly that every line is preserved. Hence
`T = lambda Q_k`, and `lambda^2 = 1` from the effect equation, so
`T = +/- Q_k`. The mixed vector `w_R + w_C` remains a good computational
breaker and is kept as one, not as a substitute for the quantifier.

## 6. QA6: restated as projective idempotence

Accepted, including the objection to the wording. The published phrase

```text
the missing O2 premise can be stated as ONE post-state-class equation
```

reads as though global O2 had been reduced to a single physical principle.
The audit does not show that. It is withdrawn and replaced:

```text
QA6  PROJECTIVE-TERMINALITY-REDUCTION.

Inside the frozen invertible orthogonal centralizer class at one moving
branch, the sign equivalence T ~ -T is a congruence for composition.
Therefore the post-state quotient is a group with identity [Q_k].

Fresh-pointer ray terminality is equivalent, inside this class, to the
single projective equation

    [T]^2 = [T].

Since every [T] is invertible, the only idempotent in this quotient group is
the identity [Q_k]. Equivalently,

    T^2 = +T or T^2 = -T   iff   T = +Q_k or T = -Q_k.

This is weaker than strict representative idempotence T^2 = T, but
physically equivalent to the unique Lueders post-state class under T ~ -T.

It compresses the terminality selector inside the frozen class. It does not
derive terminality, prove the class globally exhaustive, or close O2.
                                                          [candidate-T]
```

The universal proof in representatives, adopted, and better than the
parameter classification the first leg used: from `T^sharp T = Q_k`, `T` is
invertible on `Q_k V`; if `T^2 = eps T` with `eps` in `{+1, -1}`, then

```text
T^sharp T^2 = (T^sharp T) T = Q_k T = T,
T^sharp (eps T) = eps Q_k,
```

hence `T = eps Q_k`. The converse is immediate. No classification of
infinitely many parameters is needed. Machine-checked inputs: PR3 certifies
`Q_k T = T` and the associativity step, PR4 the congruence.

The breaker sharpens the same point, PR5: for `T = R_k - C_k` we get
`T^2 = Q_k` while `T` is not `+/- Q_k`, and on `w = w_R + w_C` it sends `w`
to `w_R - w_C` and back to `w`, off the line of `w`. Involutivity is not
terminality; repeatability of the outcome is not terminality of the
post-state.

QF3 is split as required into QF3a universal reduction, QF3b the `R - C`
witness, QF3c well-definedness of the quotient. None fired.

## 7. Output grammar and return codes

Adopted for this leg: gates collected in fixed order with no fail-fast, every
available exact witness printed, decision word and code at the end,
`0 AUDIT-PASS`, `1 AUDIT-INTEGRITY-STOP`, `2 AUDIT-DISAGREEMENT`. Stdout
carries no time, path, host, or other variable datum; environment and timing
live in this record instead.

## 8. What stands, and what is next

The first leg's verdict is unchanged: the forwarded bifurcation report is
faithful to the sealed record, the chain re-verifies independently, the
sealed verifier reproduces byte-identically, zero findings against the probe.
What changes is the standard of proof behind QA2, QA3 and QA6, the basis
statement, and the process discipline.

O2 is not moved by any of this. The public row still requires a physically
independent selector or apparatus dynamics, frozen before comparison with the
target effects, and O1 separately requires realized events and sampling. The
audit's contribution is to narrow the next scientific question to

```text
[T]^2 = [T]   in the post-state quotient of the moving branch,
```

and the next attack is not another instrument classification. It is to decide
whether projective idempotence follows from the typed composition of fresh
apparatus, irreversible record and the no-feedback rule. A positive result
derives terminality. A negative result must exhibit an architecturally
admissible non-terminal member, of the `[R - C]` kind, satisfying every other
frozen law. That is the real fork.
