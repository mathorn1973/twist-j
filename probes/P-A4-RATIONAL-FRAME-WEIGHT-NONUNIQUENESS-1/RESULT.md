# P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1 result

**Scientific result: CONFIRMED.**
**Proposed public status: T.**
Scope: L4 rational A4 rays, complete rational orthogonal frames and scalar
frame weights only.
Public lock: #875.

## Theorem

Let

```text
V = {v in Q^5 : sum_i v_i = 0},
q(v) = sum_i v_i^2.
```

For nonzero rational `a=3^k u`, with `u` a 3-adic unit, define

```text
h(a)=0  if k is even;
h(a)=-1 if k is odd and u=1 mod 3;
h(a)=+1 if k is odd and u=2 mod 3.
```

Then `H([v])=h(q(v))` is well-defined on rational rays and every complete
rational orthogonal four-frame satisfies

```text
sum_i H([v_i]) = 0.
```

Therefore, for every rational `|t|<=1/4`,

```text
w_t([v]) = 1/4 + t H([v])
```

is a nonnegative normalized rational frame weight on all rational A4 rays.
For `|t|<1/4` it is uniformly strictly positive.

On the 30 inner Cl(4) rays, `H=0`, hence every member has the same value `1/4`.
Nevertheless the frozen equal-projector cover in `U_012` satisfies

```text
D(w_t) = 3t.
```

Every nonzero-t member is therefore nonquadratic: it cannot have the form
`tr(W P_v)` for one symmetric W, even without a positivity requirement on W.

## Decided implication

The following implication is false:

```text
rational A4 rays
+ all complete rational orthogonal records
+ noncontextual complete-frame additivity
+ positivity, even uniform strict positivity
=> quadratic reading.
```

This is a global theorem, not a finite-truncation counterexample.

## Evidence

`PROOF.md` is self-contained. Its universal argument is proof-first:

1. projective square invariance of the ternary residue;
2. a binary diagonal-change identity modulo four;
3. orthogonal-basis invariance modulo four;
4. the A4 discriminant `det G=5`, which excludes H-sum `+/-4` and forces exact
   frame sum zero;
5. an explicit equal-projector six-ray cover with defect `D=3t`.

The pinned standard-library verifier completed with:

```text
85517 exact assertions
exit 0
stderr 0 bytes
stdout 318 bytes
```

The required GitHub x86_64 and aarch64 jobs remain the public computation
readback gate for this pull request.

## Meaning for the decoder programme

The result closes one attempted **uniqueness derivation**. It does not reject
the quadratic decoder.

Public reading-family discipline does not require global decoder uniqueness.
Accordingly, the correct conclusion is:

> The quadratic registration may be an explicitly chosen algebraic reading.
> Positivity and complete rational frame additivity alone do not prove it is
> the only possible reading.

Once that reading is frozen, its mathematical consequences remain exact and
falsifiable. A physical claim using it must still provide the independently
required mapping from physical preparation/context to that reading and must
not select the reading after inspecting the target result.

## Explicit nonclaims

This probe does not establish or falsify:

- a physical effect, apparatus, pointer or ready state;
- a realized event or occurrence/sampling law;
- a post-state instrument;
- an L6 probability measure;
- physical realization of the nonquadratic family;
- completeness of the decoder family;
- any contradiction with real Gleason theorems, quantum mechanics, or J.

No current physical O row is discharged by this theorem.