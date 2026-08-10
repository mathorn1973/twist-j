# Boolean orthogonal read: change, persistence, and growth

**Status:** NON-CANONICAL note. No authority. No Canon promotion. No public probe is opened by this file.

**Scope:** preserve one exact algebraic pattern and the physical hypothesis it suggests. The theorem layer is elementary Boolean and projection algebra. The proposed readings of light, matter, electromagnetism, and gravity are hypotheses only.

**Issue:** #323.

## 1. The point

The useful opposition is not XOR versus OR.

OR already contains two disjoint pieces:

```text
union = change + persistence
```

For bits `x,y in {0,1}`, as an equality of ordinary integers,

$$
\boxed{x\lor y=(x\oplus y)+(x\land y).}
$$

Moreover,

$$
(x\oplus y)(x\land y)=0.
$$

Thus XOR and AND are disjoint components of OR.

**[T, elementary]** This is the four-case Boolean truth table.

There is a second exact identity:

$$
\boxed{x+y=(x\oplus y)+2(x\land y).}
$$

XOR is addition without carry. AND marks the overlap that creates the carry.
This gives a precise arithmetic distinction between alternation and accumulation.

## 2. The projection lift

Let `P` and `Q` be commuting orthogonal projections on one finite-dimensional inner-product space. Commutativity is essential in this section.

Define

$$
C:=P-Q,
$$

$$
L:=C^2=P+Q-2PQ,
$$

$$
M:=PQ.
$$

Because `P` and `Q` commute, their join is

$$
R:=P\vee Q=P+Q-PQ.
$$

Then

$$
\boxed{R=L+M}
$$

and

$$
\boxed{LM=ML=0.}
$$

**[T, elementary]** `L` and `M` are orthogonal projections. `L` is the symmetric-difference subspace, the part present in exactly one of the two cuts. `M` is the intersection, the part present in both cuts. Their orthogonal sum is the join.

The signed operator `C=P-Q` retains orientation. Squaring removes the sign:

$$
C \longmapsto C^2=L.
$$

So the same construction naturally separates

```text
oriented change      C = P - Q
change intensity     L = C^2
persistence          M = P Q
total occupied part  R = L + M
```

This is the core observation worth preserving.

## 3. Alternation and growth

Two elementary laws distinguish the two directions:

$$
x\oplus x=0,
$$

$$
x\lor x=x.
$$

XOR cancels a repeated bit. OR retains it.

But OR alone does not generate unbounded growth. It is idempotent. Growth requires new independent support.

Let `R_n` be the projection onto everything accumulated through step `n`, and let `P_(n+1)` be a new projection. If

$$
R_nP_{n+1}=0,
$$

then

$$
\boxed{\operatorname{rank}(R_n\vee P_{n+1})
=\operatorname{rank}(R_n)+\operatorname{rank}(P_{n+1}).}
$$

**[T, elementary]** Orthogonal novelty makes the rank additive.

Therefore the sharper statement is

$$
\boxed{\text{growth}=\text{OR}+\text{orthogonal novelty}.}
$$

Without novelty, OR saturates. With orthogonal novelty, the occupied carrier grows.

## 4. Relation to the current public architecture

The public Canon already separates three registered reading modes:

- `READING-SPLIT [D]`: linear projection, binary Thue-Morse cut, quadratic registration.
- `J-PROJECTIONS [T]`: the exact modulus and argument of `J`.
- `AXIOM-PROJECTION-DICTIONARY [D]`: modulus read as gravity and scale, argument read as electromagnetism and phase, with no uniqueness claim.
- `QUADRATIC-DECODER-DATA [O]`: the typed quadratic `D_matter` bridge is still incomplete and remains a STOP obligation.

This note changes none of those statuses.

The Boolean driver is already parity. For the binary digits `b_k(n)` of `n`,

$$
\theta_n=s_2(n)\bmod2=\bigoplus_k b_k(n).
$$

So the Thue-Morse cut is literally an XOR fold of the counter bits. That is an exact statement about the registered driver, not a physical interpretation.

## 5. Candidate physical reading

The following is **[H, note-local]** only.

After two physical cuts have been transported to the same carrier, try the dictionary

$$
\boxed{\text{light} \sim L=(P-Q)^2}
$$

as transported change,

$$
\boxed{\text{matter} \sim M=PQ}
$$

as transported persistence,

$$
\boxed{\text{EM orientation} \sim C=P-Q\ \text{or its phase holonomy}}
$$

as the signed or oriented channel, and

$$
\boxed{\text{gravity source weight} \sim R=L+M}
$$

as a positive total occupied weight.

The last line is intentionally not `gravity ~ matter`. Radiation gravitates. If a useful Boolean/projection bridge exists, its positive gravitational read must be able to include both the persistent and changing sectors.

This proposed type split is compatible in spirit with the registered modulus/argument dictionary, but it does not derive that dictionary and does not identify `C`, `L`, `M`, or `R` with any existing Canon carrier.

## 6. Transport comes before comparison

A naive comparison of states at two ticks is wrong for physics. Moving matter would otherwise appear as pure change.

Let `T_n` be a candidate transport from the carrier at tick `n` to the carrier at tick `n+1`. Pull the later projection back first:

$$
\widetilde P_{n+1}=T_n^{-1}P_{n+1}T_n.
$$

Only then compare

$$
C_n=P_n-\widetilde P_{n+1},
$$

$$
L_n=C_n^2,
$$

$$
M_n=P_n\widetilde P_{n+1}.
$$

**[O, note-local]** A real bridge would require a Canon-typed carrier and transport for which this comparison is well-defined and invariant under the admitted equivalences. None is supplied here.

If transported projections do not commute, the simple decomposition

$$
P\vee Q=(P-Q)^2+PQ
$$

is not available. Noncommutativity is therefore a hard boundary of this note, not a detail to hide.

## 7. The 3/4 guard

For two independent uniform bits,

$$
P(XOR=1)=\frac12,
$$

$$
P(AND=1)=\frac14,
$$

$$
P(OR=1)=\frac34.
$$

and

$$
\frac34=\frac12+\frac14.
$$

**[T, elementary]** This is only a two-bit counting identity.

TWIST-J contains other exact occurrences of `3/4`. This note makes **no identification** between them and this Boolean count. Equal numbers on different carriers are not a bridge. Any future identification must exhibit an exact map that transports the relevant structure, not merely the fraction.

## 8. Falsification-first boundary

This idea is useful only if it becomes narrower under attack.

A future formalization should fail rather than move the goalposts if any of the following occurs:

1. No canonical or fully classified transport puts the two cuts on one carrier.
2. The transported projectors are necessarily noncommuting and no replacement theorem preserves the proposed split.
3. The matter/light assignment changes under an admitted gauge or carrier equivalence.
4. A transported persistent object is classified as change solely because it moved.
5. The registered gravity read requires an additional mixed term that cannot factor through `R=L+M` at the declared scope.
6. The proposed EM orientation cannot be typed through the registered argument/phase channel.
7. A `3/4` coincidence is the only surviving evidence for a claimed bridge.

No threshold is frozen by this note because no formal probe is opened.

## 9. What a real next step would have to freeze

Before any computation, a formal candidate would need at least:

```text
carrier
state-to-projection map
tick-to-tick transport
equality / gauge relation
commutativity domain
matter and light output types
positive source weight
phase or orientation output
layer L1 to L6 for every map
falsifiers before execution
```

Only after those objects are public could the question be asked whether the Boolean/projection split actually factors any registered decoder leg.

Until then the compact statement is:

$$
\boxed{\text{union}=\text{change}\ \perp\ \text{persistence}}
$$

for compatible projections, and

$$
\boxed{\text{growth}=\text{union}+\text{orthogonal novelty}.}
$$

The mathematics is exact. The physical reading is open.
