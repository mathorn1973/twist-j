# C-QDD-INSTRUMENT-DILATION-1-N

```text
STATUS      NON-CANONICAL incubation. No authority. Promotes nothing.
TARGET      QDD-INSTRUMENT-APPARATUS [O], Public Canon v48.
BASIS       tag canon-v48
            CONTENT_COMMIT d1d0df6d08dcb6b610719bc17151aabb97cc9d96
            activation main 88f376aa4df3d55449d152e024dfe399557890b3
            CANON_SHA256 65dfa8509abfdf44fdd1198c93d476d01f1c93ca3066c1f573aab6bbc70879bb
            CANON_BYTES 234810
ISSUE       #389
LAYER       L1 algebra to L4 apparatus witness only.
            No L5 outcome stream. No L6 measure.
EVIDENCE    Historical local exact checks predate a public preregistration pin.
            They are audit witnesses only, not formal public probe evidence.
VERDICT     Negative closeout. Orthogonal dilation does not select a physical
            instrument. QDD-INSTRUMENT-APPARATUS stays [O].
```

## 1. Scope and final decision

This note closes the incubation analysis of a rational apparatus for the frozen QDD effect pair. It does not close the public obligation and it does not retroactively turn pre-pin computation into a public probe.

The exact apparatus can be exhibited. It reproduces the frozen ordered effects and the frozen Born trace pairing. The stronger result, however, is negative:

```text
Existence of a rational orthogonal dilation is not an instrument-selection principle.
```

Two independent blockers remain for `QDD-INSTRUMENT-APPARATUS [O]`:

1. an independently justified physical selection of one instrument family inside the fixed effect fibre;
2. event generation or sampling, meaning a typed transition from branch weights to a realized outcome stream.

The first blocker is not reducible to the second. The nonselection theorem below shows that unrestricted apparatus dilation supplies no selector.

A later attack on instrument selection must start as a new preregistered candidate or public probe. Its coupling must be frozen before comparison with `E_low,E_high`. A coupling controlled by the target effects is forbidden as an independent selection input.

## 2. Frozen algebra

Let

```text
V = Q^4,
1 = (1,1,1,1)^T,
G = I_4 - (1/5) 1 1^T,
G^-1 = I_4 + 1 1^T,
A^# = G^-1 A^T G.
```

The frozen ordered effect pair is

```text
E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low.
```

Then

```text
E_a^2 = E_a,
E_a^# = E_a,
E_low E_high = 0,
E_low + E_high = I_4.
```

The form `G` is positive definite over `Q`. It has eigenvalue `1/5` on `span(1)` and eigenvalue `1` on `ker Tr_4`. Thus

```text
im(E_low)  = span(1),
im(E_high) = ker Tr_4.
```

No physical selection claim follows from these identities. They are the frozen algebraic input already separated from the public instrument obligation.

## 3. Exact four-dimensional pointer apparatus

Take the apparatus carrier to be a second copy

```text
P = (Q^4,G).
```

Choose

```text
r = (1/2,  1/2, -1/2, -1/2)^T,
f = (1/2, -1/2,  1/2, -1/2)^T.
```

Both are in `ker Tr_4` and satisfy exactly

```text
<r,r>_G = 1,
<f,f>_G = 1,
<r,f>_G = 0.
```

For rational vectors `x,y` define the rank-one operator

```text
R_(x,y) = x y^T G.
```

Define

```text
X = I - R_(r,r) - R_(f,f) + R_(r,f) + R_(f,r).
```

Then

```text
X r = f,
X f = r,
X^2 = I,
X^# X = I.
```

The complete two-outcome pointer PVM on the four-dimensional pointer is

```text
Pi_low  = R_(r,r),
Pi_high = I - Pi_low.
```

The high pointer space has rank three. The actual high branch produced below lands on the single vector `f` inside it, so there is no leakage into the other two high-pointer directions.

On `H = V tensor P` with form `G tensor G`, define the controlled coupling

```text
U = E_low tensor I_P + E_high tensor X.
```

Because the two effects are orthogonal complementary projectors and `X` is orthogonal,

```text
U^# U = I,
U^2 = I.
```

On the prepared subspace,

```text
U(v tensor r)
  = E_low v tensor r + E_high v tensor f.
```

Reduction by the pointer therefore gives

```text
K_low  = E_low,
K_high = E_high,
K_a^# K_a = E_a.
```

This is an exact rational controlled-dilation witness. Its scientific status here is only an exhibited non-canonical construction. The coupling was designed with knowledge of the target effects.

## 4. Occurrence identity is global, not a 625-point census

For any rational `K` satisfying

```text
K^# K = E,
```

we have

```text
K^T G K = G E.
```

Therefore for every `v in Q^4`, not merely for the 625 frozen piston vectors,

```text
<Kv,Kv>_G
  = v^T K^T G K v
  = v^T G E v
  = Tr(E v v^T G).
```

Hence the apparatus branch norm reproduces the frozen trace pairing identically on the whole rational carrier.

This proves an exact algebraic equality between two formulas. It does not derive the physical Born reading from nothing. Calling the common scalar an occurrence weight still uses the owner-frozen branch-weight dictionary. The earlier 625 of 625 census is therefore only a finite regression witness, not the evidential basis of the identity.

## 5. S1a. Raw single-branch fibre

**Status in this note: candidate-T, non-canonical.**

For a fixed nonzero `G`-self-adjoint projector `E`, define

```text
F_E = {K in End_Q(V) : K^# K = E}.
```

Then

```text
F_E = {W E : W in O(G,Q)}.
```

### Proof

If `x in ker E`, then

```text
||Kx||_G^2 = <x,Ex>_G = 0.
```

Positive definiteness gives `Kx=0`.

If `x,y in im E`, then

```text
<Kx,Ky>_G = <x,Ey>_G = <x,y>_G.
```

Thus `K` vanishes on `ker E` and is an isometric embedding of `im E` into `(V,G)`.

No external Witt citation is needed in this positive-definite rational case. For nonzero rational `z`, the reflection

```text
H_z(x) = x - 2 <x,z>_G / <z,z>_G z
```

lies in `O(G,Q)`. If two rational vectors have the same nonzero norm, a reflection in their difference maps one to the other. Induct on a rational orthogonal basis of the source subspace, choosing each new reflection in the orthogonal complement of the already fixed part. This extends any rational subspace isometry to an element of `O(G,Q)`.

Therefore `K = W E` for some `W in O(G,Q)`. The converse is immediate.

## 6. S1b. Raw ordered-family fibre

**Status in this note: candidate-T, non-canonical.**

For the fixed ordered pair `(E_low,E_high)`, the raw family fibre is

```text
{(K_low,K_high) : K_a^# K_a = E_a}
  = { (W_low E_low, W_high E_high)
      : W_low,W_high in O(G,Q) }.
```

It is one orbit under the product action

```text
O(G,Q) x O(G,Q),
```

with independent left actions on the two branches.

It is not generally one orbit under a single diagonal copy of `O(G,Q)`.

The earlier wording `one left O(G,Q) orbit` for the whole ordered family is withdrawn. The earlier name `GAUGE-ORBIT` is also withdrawn. Left orthogonal action generally changes the state update and is not merely a redundancy of description.

## 7. S1c. Complete classification of diagonal orbits

**Status in this note: candidate-T, non-canonical.**

For an admissible ordered family `K=(K_a)`, define the cross-Gram matrix of operators

```text
Gamma(K)_(ab) = K_a^# K_b.
```

Then:

1. `Gamma(K)_(aa) = E_a` for every branch.
2. Two admissible families `K,K'` lie in the same diagonal left `O(G,Q)` orbit if and only if `Gamma(K)=Gamma(K')`.
3. For two outcomes, the fixed diagonal blocks mean that the single cross term

   ```text
   C(K) = K_low^# K_high
   ```

   is a complete diagonal-orbit invariant. The opposite cross term is `C(K)^#`.
4. The reachable cross terms are exactly

   ```text
   { E_low O E_high : O in O(G,Q) }.
   ```

   Every reachable `C` has rank at most one, has image in `span(1)`, and annihilates `span(1)` on the right. In ordinary matrix form it is therefore of the form `1 u^T` with `u^T 1 = 0`, subject to the additional orthogonality constraint implicit in `C = E_low O E_high`.

### Proof of completeness

The forward implication is immediate: if `K'_a = O K_a` for one `O in O(G,Q)`, then

```text
K'_a^# K'_b = K_a^# O^# O K_b = K_a^# K_b.
```

For the converse, assume `Gamma(K)=Gamma(K')`. On the sum of the branch images define

```text
phi( sum_a K_a v_a ) = sum_a K'_a v_a.
```

If the source sum is zero, then the squared norm of the target sum is

```text
sum_(a,b) <v_a, K'_a^# K'_b v_b>_G
 = sum_(a,b) <v_a, K_a^# K_b v_b>_G
 = 0.
```

Positive definiteness makes the target sum zero, so `phi` is well defined. The same identity with two independent families of vectors shows that `phi` preserves the inner product. Rational reflection induction extends `phi` to a global `O in O(G,Q)`, giving `K'_a=O K_a` for every branch.

For two branches the diagonal blocks are frozen to `E_low,E_high`, so equality of `Gamma` is equivalent to equality of `C`.

Writing `K_low=W_low E_low` and `K_high=W_high E_high` gives

```text
C = E_low W_low^# W_high E_high
  = E_low O E_high,
```

and every `O in O(G,Q)` is obtained from a suitable pair `(W_low,W_high)`.

### Important boundary

This classifies diagonal orthogonal orbits. It does not classify physical instruments. Diagonal orthogonal action is not a physical gauge transformation in general.

The previously checked Householder example with `C != 0` is a direct witness that more than one diagonal orbit exists. Conversely, the permutation witness `P_12 E_high` has `C=0` and is diagonally equivalent to the Lueders pair, yet it changes post-state rays. Thus even the complete diagonal invariant `C` is not an operational equivalence invariant.

## 8. Physical post-state equivalence is strictly finer

**Status in this note: candidate-T at the declared pure-state/rank-one post-state scope.**

For a branch operator `K`, define the unnormalized rank-one post-state map

```text
R_K(v) = (K v)(K v)^T G.
```

Where the branch weight is nonzero, the normalized post-state is

```text
Post_K(v) = R_K(v) / <Kv,Kv>_G.
```

Within a fixed nonzero effect fibre `K^#K=E`, branchwise sign is invisible:

```text
R_(-K)(v) = R_K(v).
```

Conversely, if two operators in the same nonzero effect fibre induce the same rank-one post-state for every input on which the branch is supported, then they induce the same projective map on `im E`. Linearity forces one rational scalar on that image, and equality of the effect forces its square to be one. Thus

```text
K ~_post L  iff  L = +K or L = -K
```

at this declared rank-one post-state scope.

This corrects the earlier use of a sign-flipped branch as a witness of physical nonuniqueness. Sign changes alter the raw Kraus matrix but not the ray or density-operator update.

## 9. Strong nonselection: an infinite physically distinct family at fixed effects and weights

**Status in this note: candidate-T, non-canonical.**

The nonselection is stronger than the existence of two raw representatives.

The rational vectors `r,f` from section 3 form a `G`-orthonormal pair inside `im(E_high)=ker Tr_4`. For any rational parameter `t`, with `1+t^2 != 0`, set

```text
c_t = (1-t^2)/(1+t^2),
s_t = 2t/(1+t^2).
```

Define `R_t in O(G,Q)` by

```text
R_t r = c_t r + s_t f,
R_t f = -s_t r + c_t f,
```

and let `R_t` be the identity on the `G`-orthogonal complement of `span(r,f)`.

Then

```text
K_low(t)  = E_low,
K_high(t) = R_t E_high
```

satisfies for every rational `t`

```text
K_low(t)^# K_low(t)   = E_low,
K_high(t)^# K_high(t) = E_high,
C(K(t))               = 0.
```

Thus every member has the same effects, the same branch weights, and lies in the same diagonal `C=0` orbit as the Lueders pair.

For infinitely many rational parameters `t`, the restrictions `R_t|im(E_high)` are not equal up to sign. By section 8, these give infinitely many physically distinct post-state dynamics.

Therefore:

```text
The frozen effects and frozen branch weights are constant on an infinite
family of physically inequivalent post-state instruments.
```

Equivalently, diagonal `O(G,Q)` classification is geometric bookkeeping, not physical gauge reduction.

## 10. S2. Orthogonal-dilation surjectivity

**Status in this note: candidate-T, non-canonical.**

Let `(K_low,K_high)` be any rational two-branch family satisfying

```text
K_low^# K_low + K_high^# K_high = I.
```

Choose any two rational `G`-orthonormal pointer states `e_low,e_high` in `P`, for example `r,f`. Define

```text
J_K(v) = K_low v tensor e_low + K_high v tensor e_high.
```

Then

```text
<J_K(v),J_K(w)>_(G tensor G)
 = <v,(K_low^# K_low + K_high^# K_high)w>_G
 = <v,w>_G.
```

Hence `J_K` is a rational isometric embedding of the prepared four-dimensional subspace `V tensor r` into `V tensor P`. By the rational reflection extension argument of section 5, it extends to some

```text
U_K in O(G tensor G,Q).
```

Pointer reduction of `U_K` on the prepared subspace returns the original family `(K_low,K_high)`.

Therefore every complete rational two-branch family has a rational orthogonal dilation on the registered carrier type.

This theorem asserts existence of some orthogonal coupling. The extension need not be involutive and need not have the controlled form of section 3.

## 11. S3. Unrestricted orthogonal apparatus is nonselective

**Status in this note: candidate-T, non-canonical.**

At the scope where the admissible apparatus class contains all rational `G tensor G` orthogonal couplings with the frozen carrier type, one prepared rational unit state, and a complete two-outcome pointer type, section 10 gives

```text
complete instrument family
    iff
some rational orthogonal dilation exists.
```

Thus the existence of such an apparatus imposes no restriction beyond the completeness relation

```text
sum_a K_a^# K_a = I.
```

In particular, apparatus existence cannot select the Lueders representative out of the infinite post-state family in section 9.

This is the main negative result of the incubation.

## 12. S3b. Controlled-by-target couplings are circular selectors

**Status in this note: candidate-T plus methodological consequence.**

Let `(E_a)` be a complete pair of orthogonal `G`-self-adjoint projectors and consider the restricted coupling class

```text
U = sum_a E_a tensor X_a.
```

Because `E_a E_b=0` for `a != b`,

```text
U^# U = I
```

if and only if every `X_a` is `G`-orthogonal on the pointer carrier.

Now choose an adapted ready state and pointer states satisfying

```text
X_a r = e_a,
```

with the `e_a` belonging to the declared pointer outcomes. Then

```text
U(v tensor r) = sum_a E_a v tensor e_a,
```

so pointer reduction returns

```text
K_a = E_a
```

identically.

Hence restricting the admissible apparatus class to couplings controlled by the frozen target effects selects the Lueders family only because the target effects were inserted as the controls of the coupling.

This is not an independent apparatus-selection mechanism. It is the target answer encoded in the admissible coupling class.

A future independent-selection preregistration must therefore forbid the target-controlled form, or derive its control projectors from an independently frozen dynamical input that does not name, depend on, or compare against `E_low,E_high`.

## 13. S4. Positive square-root section

**Status in this note: candidate-T, mathematical only.**

Suppose

```text
K^# = K,
K >=_G 0,
K^# K = E,
```

where `E` is a `G`-self-adjoint projector. Then

```text
K^2 = E.
```

On `ker E`, positivity and self-adjointness force `K=0`. On `im E`, the equation is `K^2=I`. The spectrum there is contained in `{+1,-1}`, and `G`-positivity excludes `-1`. Therefore

```text
K = E.
```

So `G`-positivity selects the positive square root uniquely.

This corrects the rejected claim that `G`-self-adjointness alone selects the Lueders representative. It does not: `-E` is also self-adjoint. Positivity is the extra condition.

The physics selection does not follow. Adopting `G`-positivity after seeing the target would be a new qualitative dictionary input, even though it introduces no new dimensionless number. Zero new numbers is not zero new physical information.

Therefore this note rejects post-hoc `G`-positivity as a closure of `QDD-INSTRUMENT-APPARATUS`.

## 14. D1. What the controlled apparatus witness actually earns

**Status in this note: candidate-D, non-canonical.**

The displayed four-dimensional apparatus of section 3:

- uses only rational entries and a second copy of `(Q^4,G)`;
- has an exact complete PVM pointer;
- has an exact orthogonal involutive coupling;
- reduces to the frozen ordered algebraic pair;
- reproduces the frozen branch-weight pairing by the global identity of section 4.

It does not independently select its own control projectors, does not select a physical instrument out of the full effect fibre, and does not produce an outcome stream.

The preferred descriptive name is therefore

```text
QDD-CONTROLLED-DILATION-WITNESS
```

not `QDD-INSTRUMENT-EXHIBITED`.

## 15. F1. The route that is actually falsified

**Status in this note: candidate-F route, non-canonical.**

The proposition

```text
Existence of an orthogonal apparatus dilation selects a unique physical
instrument for the frozen effect pair.
```

is false at the unrestricted rational orthogonal-dilation scope.

Section 10 realizes every complete family. Section 9 exhibits infinitely many physically distinct post-state families with the same effects and branch weights. Therefore apparatus existence cannot perform the required selection.

This is a productive negative result. It removes a whole proposed route without changing the public Canon.

## 16. O1 and O2. The two independent blockers

### O1. Event generation and sampling

The apparatus signature `(P,r,U,Pi_a)` determines branch states and branch weights. It contains no map from those weights to one realized outcome indexed in an L5 stream.

The exact statement is

```text
SAMPLING NOT PROVIDED.
```

This note does not claim the stronger universal statement `SAMPLING IMPOSSIBLE`. Such a no-go theorem would require a separately frozen admissible class of sampling maps and a proof that the class is empty.

### O2. Independent instrument selection

The controlled witness was built from the target projectors. The unrestricted apparatus class is nonselective. The positive-root section is a mathematical section, not a derived physical law.

Thus the missing physical selector remains independent and open.

A future attack must derive a source-to-instrument restriction from an independently registered input, or else state a new physical dictionary rule openly and pay its dependency cost.

## 17. Corrected status ledger for this incubation

No line below is a public registry promotion. These are only proposed names and candidate statuses inside this non-canonical note.

```text
QDD-CONTROLLED-DILATION-WITNESS
    candidate-D
    exact rational witness reproducing the frozen effect pair and pairing

QDD-INSTRUMENT-RAW-SINGLE-FIBRE
    candidate-T
    {K : K^#K=E} = O(G,Q) E

QDD-INSTRUMENT-RAW-FAMILY-FIBRE
    candidate-T
    ordered pair is one O(G,Q)^2 orbit, branchwise

QDD-INSTRUMENT-DIAGONAL-CROSSGRAM-CLASSIFICATION
    candidate-T
    Gamma, and for two branches C=K_low^#K_high, completely classifies
    diagonal O(G,Q) orbits; diagonal action is not physical gauge

QDD-INSTRUMENT-POSTSTATE-SIGN-EQUIVALENCE
    candidate-T at the declared rank-one post-state scope
    physical equality inside one nonzero effect fibre identifies only +/-K

QDD-INSTRUMENT-INFINITE-POSTSTATE-NONSELECTION
    candidate-T
    fixed effects and fixed branch weights admit infinitely many physically
    inequivalent post-state dynamics, already inside C=0

QDD-ORTHOGONAL-DILATION-SURJECTIVITY
    candidate-T
    every rational complete two-branch family admits some rational orthogonal
    dilation

QDD-DILATION-NONSELECTION
    candidate-T
    unrestricted orthogonal apparatus existence adds no condition beyond
    completeness

QDD-TARGET-CONTROLLED-CIRCULARITY
    candidate-T plus methodological boundary
    a coupling controlled by the target effects returns K_a=E_a by construction

QDD-POSITIVE-SQUARE-ROOT-SECTION
    candidate-T
    G-positive self-adjoint square root of E is uniquely E; no physical
    selection rule is inferred

QDD-INSTRUMENT-APPARATUS
    remains public [O]
```

The earlier names `QDD-INSTRUMENT-GAUGE-ORBIT` and `PARTIAL-ISOMETRY-TORSOR` are retired for this candidate. The former falsely suggests physical gauge redundancy. The latter obscures the nontrivial diagonal-orbit structure.

## 18. Historical audit corrections preserved

The incubation caught four material errors before any public pin:

1. **Pointer mismatch.** An earlier text described a four-dimensional pointer while its verifier tested a two-dimensional pointer. The final construction above uses and types the four-dimensional pointer consistently.
2. **False post-state witness.** A sign-flipped Kraus operator changes the raw vector but not the ray or density-operator update. Sign is not a valid witness of physical nonuniqueness.
3. **Type error involving the balanced piston table.** The five-entry balanced map `ell` and the four-dimensional ready state `r` are different types. The comparison is removed.
4. **Overstated layer.** A static apparatus witness is L4. Without a realized outcome stream there is no L5 claim and no L6 measure claim.

A fifth correction came from the diagonal-orbit audit:

5. **Orbit versus physics.** `C=0` characterizes the diagonal Lueders orbit, but that orbit contains physically different post-state maps. Diagonal `O(G,Q)` action is not a physical gauge.

These are not editorial trivia. Each would have altered the scientific meaning of a public fold.

## 19. What must be frozen before the next round

A new instrument-selection candidate must be a new name. It must preregister before computation at least:

```text
1. source carrier and source dynamics used to construct the coupling;
2. apparatus carrier and form;
3. ready-state class and its equivalence;
4. allowed coupling class, frozen independently of E_low,E_high;
5. explicit prohibition on target-controlled couplings
   U = sum_a E_a tensor X_a unless the controls are independently derived;
6. pointer type and complete PVM/POVM semantics;
7. reduction map to K_a;
8. K-level physical equivalence, including post-state equality;
9. E-level equivalence;
10. occurrence/weight dictionary dependencies;
11. sampling/outcome-stream signature if that blocker is attacked;
12. complete acyclic dependency graph;
13. action layer and every named lift gate;
14. falsifiers that can return a genuine negative result without moving a
    threshold or changing the admissible class after computation.
```

The coupling must be frozen before any comparison with the target effect pair. Otherwise a positive result is circular.

## 20. Final closeout

The constructive part survives:

```text
A completely rational four-dimensional orthogonal apparatus can reproduce the
frozen ordered QDD effects and their frozen branch-weight pairing exactly.
```

The deeper result is negative:

```text
Orthogonal dilation existence does not select the physical instrument.
```

More sharply:

```text
The same effects and the same branch weights persist across an infinite family
of physically different post-state dynamics, even inside the single diagonal
cross-Gram layer C=0.
```

The only restriction that trivially returns the Lueders family is the controlled form whose controls are already the target effects. That is circular as an independent selection mechanism. `G`-positivity uniquely picks the positive square root mathematically, but adopting it as physics here would be a new dictionary choice.

Therefore `QDD-INSTRUMENT-APPARATUS [O]` remains open with two named blockers:

```text
O2  independent physical instrument selection
O1  event generation / sampling
```

No public status changes, no decoder-completion field is filled, and no L5 or L6 lift is claimed.