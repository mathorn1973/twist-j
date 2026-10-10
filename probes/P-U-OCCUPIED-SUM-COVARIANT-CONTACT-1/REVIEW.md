# Separate symbolic review of the occupied-SUM contact class

**PUBLIC, NON-CANONICAL. Conditional L1 mathematical review.**
Review date: 2026-10-10, Europe/Prague.

Disposition: **ACCEPT at the explicitly restricted mathematical scope below.**
The class count requires the stated access restriction `f=f(x,y)`.
The complete enlarged evolution is not globally invertible. Neither physical
admission nor global minimality is established.

## 1. Review method, exposure and source identity

This is a separately derived symbolic review within one coordinated assistant
session. The reviewer was told the prospective class, proposed counts, unit
condition and continuation claim before deriving the arguments. This is
result-exposed review, not blind review or external experimental confirmation.
The reviewer had already inspected the predecessor definitions and proofs.
No newly written verifier was read, imported or executed. No scientific
program or formal gate was run for this review. No computational result is
reported here.

The mathematical sources read directly are:

- Public Canon v101 at
  `08ec6f93b5f70ad662bb447cd6cc41ccc62fa5f3`,
  [U-STABLE-PAIRED-PORT-TRANSPORT][canon-port], and
  [P-QDD-UNINTERRUPTED-RECORD-1/PROOF.md, equations (43)-(44)][port-proof].
  These supply the complete `T_delta` and `V_delta` maps, their relation
  to the literal generator `c`, and the stable native transport boundary.
- [P-U-NATIVE-FIXED-READ-1/PROOF.md][sum-proof] at
  `ec4995176d36005ba924e0b381c3cc72b97420fc`, especially sections 2-6.
  This open non-canonical candidate supplies the exact occupied SUM
  preparation, complete first output, fixed reader and later retention.

The source-dependent contacts and their placement in the enlarged law are
explicit new architectural premises. Reading an existing parameterized map
does not establish an available device that applies it under source control.

## 2. Exact class under review

All scalar arithmetic in this review is in F5. Center the piston coordinates
as

```text
x = p1-1,  u = p4-3,  y = p1p-4,  v = p4p-2,
c = x+y,   h = y-x,
M = 2(xu+yv),
S = p1+p4+p1p+p4p.
```

The source map is exactly

```text
V_delta(x,u,y,v,q,r) = (x,u+delta,y,v-delta,q,r).
```

Freeze the restricted family

```text
C_s^f = V_(-f(x,y)s),       f: F5^2 -> F5.
```

The supplied source pentit `s` is unchanged by this contact and is passive
under the receiver generators used in the covariance comparison. Dependence
only on `(x,y)` is part of the class definition, not a conclusion from the
other structural requirements. The statements below do not classify arbitrary
state-dependent source-additive contacts.

Since `V_delta` leaves `x,y,q,r` and `S` unchanged, it also preserves the
receiver trace `z=S+q+r`. Its complete effect in this family is

```text
u' = u-f(x,y)s,      v' = v+f(x,y)s,
M'-M = 2(y-x)f(x,y)s = 2h f(x,y)s.
```

The coefficient is unchanged by every application. Therefore, on the complete
declared carrier,

```text
C_s^f C_t^f = C_(s+t)^f,        (C_s^f)^(-1) = C_(-s)^f.
```

For the controlled map `(s,psi)->(s,C_s^f psi)`, the inverse retains the same
stored source and applies the negative control argument. It neither erases nor
replaces the source.

## 3. Necessary and sufficient covariance conditions

The complete centered piston actions of the three stable generators are

```text
b:   (x,u,y,v) -> (-y,-v,-x,-u),
d,e: (x,u,y,v) -> (-x,-u,-y,-v).
```

Their actions on `q,r` do not depend on the piston changes made by `C_s^f`;
the contact leaves `q,r` fixed. Comparing the complete `u,v` outputs yields

```text
b C_s^f = C_s^f b  iff  f(-y,-x) = f(x,y),
d C_s^f = C_s^f d  iff  f(-x,-y) = -f(x,y),
e C_s^f = C_s^f e  iff  f(-x,-y) = -f(x,y).
```

Necessity follows already by taking `s=1`; sufficiency follows by substitution
for every source value and every complete receiver state.

The coordinate change `(x,y)<->(c,h)` is invertible because 2 is nonzero in F5.
Writing `F(c,h)=f(x,y)`, generator `b` sends `(c,h)` to `(-c,h)`, while `d,e`
send it to `(-c,-h)`. The preceding equations are therefore equivalent to

```text
F(-c,h) = F(c,h),       F(c,-h) = -F(c,h).
```

In particular, `F(c,0)=0`. The first argument has three sign classes
`{0}`, `{1,-1}`, `{2,-2}`; the nonzero second argument has two sign classes
`{1,-1}`, `{2,-2}`. Assigning one value in F5 to each of the six pairs
determines and is determined by one covariant function. Thus the exact count
in the frozen class is `5^6`.

These are all-state identities for the named generator maps. On the stable
native union, trace preservation ensures that the actual state-selected step
uses the same generator before and after the contact. The identities then
apply to actual native continuation there. No claim is made that every literal
generator is selected by the original U on this union.

## 4. Unit gain on the actual SUM continuation

The inherited complete first output is

```text
psi3(s1,t) = (0,-t-s1,1,t+s1+3,1-s1,1+s1).
```

It has `S=4`, stable trace `z=1`, and centered coordinates

```text
x=-1, y=-3, c=1, h=-2.
```

Every later actual native step is one of `b,d,e`. Hence its centered pair
stays within

```text
c in {1,-1},       h in {2,-2}.
```

The same is true after every contact under review, since the contact leaves
`x,y` unchanged. On this set the requirement that the contact add its full
source value to M is

```text
2h F(c,h) = 1.
```

The covariance equations make this equivalent to the single condition

```text
F(1,2) = 4.
```

It fixes one of the six independent values. Thus exactly `5^5` members of the
frozen class have unit gain on the supporting SUM orbit. The representative
`f=2h` belongs to this class: on `h=+/-2`, `2h f=4h^2=1` in F5.

All unit members agree in the value of `f(x,y)` at every point of this orbit.
Consequently they agree in the complete contact map there, not merely in the
value of M. They leave `q,r` and the stored second source identical and apply
the same displacement to `u,v`. Deterministic native continuation from their
equal complete outputs is equal at all later times.

This is equality of complete trajectories on the specified supported family.
It is not equality of the contact maps on arbitrary raw states, and it says
nothing about intermediate states of a future physical implementation of an
atomic contact.

## 5. Actual-time continuation with one initially present second source

For a fixed integer `N>=4`, take the complete enlarged carrier

```text
Omega_ext = N0 x F5^6 x F5,
omega = (n,psi,s2).
```

At `n=N`, apply `C_s2^f` to the actual receiver state and then apply the
ordinary native step selected from that post-contact state. At every other
counter value, apply the ordinary native step alone. Retain `s2`, and advance
`n` by one on every step. This is the precise order reviewed as `W_N`.

Prepare the three independent symbols at time zero as

```text
(0,E_SUM(s1,t),s2),
E_SUM(s1,t) = (t,0,-t,0,-s1,s1).
```

The passive law of the additional source is an explicit part of the enlarged
model; it is not inferred from the one-cell U. Before the scheduled contact,
the receiver follows exactly the inherited native trajectory. The fixed
receiver reader is

```text
R = (1-S^2)(p1+p4p) + S^2 M.
```

The predecessor proves `R=t+s1` on every boundary `n>=3` of that free
trajectory. Therefore the first value is held on the actual boundaries
`3<=n<=N`.

At the contact, the unit condition gives `M'=M+s2`. The contact preserves
`S,z,q,r`, so the next selected native generator is unchanged. It is one of
`b,d,e`, preserves M and remains in the stable union. All later native steps
also preserve M and `S^2=1`. Thus the same reader satisfies

```text
R(omega_n) = t+s1       for 3<=n<=N,
R(omega_n) = t+s1+s2    for every n>=N+1.
```

This is an all-time symbolic argument. It does not extrapolate a finite
trajectory audit. No reset to `S=0`, new receiver, new source insertion or
counter restart occurs. The convention `N>=4` supplies the stated interval;
this review does not assert a minimum waiting time or a globally minimal
carrier.

## 6. Exact invertibility boundary and a complete-state collision

Each contact is a global permutation. The complete enlarged evolution on
`Omega_ext` is not globally injective. Fix any source value `s2` and compare

```text
omega  = (0,(0,0,0,0,0,0),s2),
omega' = (0,(2,1,2,1,1,0),s2).
```

At counter zero the contact has not occurred because `N>=4`. The first
checkpoint has trace 0 and selects `a`; the second has trace 2 and selects
`c`. Their exact outputs coincide:

```text
W_N(omega) = W_N(omega') = (1,(0,0,0,0,0,0),s2).
```

This is a falsifier of any global-inverse claim on the entire declared
carrier, independent of f. The monotone one-sided counter also gives no
predecessor within this carrier for a state at `n=0`.

There is nevertheless an exact restricted backward reconstruction. All
supported preparations have the same trace at each fixed time: initially
0, then 0, 2, 1, followed by the common stable trace history. The contact
preserves this trace. At each fixed time, the selected native letter is
therefore known and is a bijection between the corresponding trace sheets.
The contact is a bijection within such a sheet. Each supported time-layer
maps bijectively onto the following reached layer.

From a reached boundary at `n+1>0`, undo that known native generator and,
if the predecessor counter was `N`, then apply `C_(-s2)^f`. This recovers
the unique preceding supported complete state. The initial encoding of all
three symbols is injective, and these layer maps preserve its distinctions.
The argument establishes reconstruction on the actual reachable layers,
not a global permutation of `Omega_ext` or a predecessor for time zero.

## 7. Falsifier of an overbroad completeness claim

The dependence restriction `f=f(x,y)` must remain explicit. It cannot be
deduced merely from source additivity, preservation of `x,y,q,r,S`, and
commutation with `b,d,e`.

For a counterexample to that broader assertion, set

```text
w = u+v,        f_hat(x,u,y,v) = h*w^2,
C_hat_s = V_(-f_hat*s).
```

This contact fixes `w` as well as `x,y,q,r,S`. Its coefficient consequently
does not change during the contact, so it is source-additive and has inverse
`C_hat_(-s)`. Under `b`, `h` is fixed and `w` changes sign; under `d,e`,
both `h` and `w` change sign. Thus the coefficient has exactly the required
covariance: unchanged under `b`, negated under `d,e`.

For fixed `x,y` with nonzero h, varying w changes the coefficient. Hence it
is generally not a function of `(x,y)` alone. It satisfies the broader listed
structural properties but is outside the frozen class. The `5^6` and `5^5`
counts must therefore never be advertised as counts for that broader class.

## 8. Review disposition and unprovided admission

The restricted function classification, unit-gain count, complete supported
trajectory equality and actual-time continuation pass this symbolic review.
The full-state collision and the broader-access counterexample delimit two
stronger statements that fail; they are not failures of the restricted claims.

The correct description is a conditional L1 construction and classification
using an existing piston-displacement direction. It does not derive:

- physical availability of the controlled contact or of its signed inverse;
- physical access to `(x,y)` or to the independent source;
- the passive source law or the scheduled interaction from the original U;
- a nonzero-duration implementation compatible with every native tick;
- physical preparation, energy, measurement or event admission;
- a global inverse, a globally minimal carrier, or completeness beyond the
  explicitly restricted control interface.

The old letter identity involving `c` remains useful mathematical provenance.
It does not turn the silent letter into a selected stable native step, nor
does it certify an implementation of the new contact. Any later formal
execution, public acceptance or Canon promotion has its own required evidence
and cannot be claimed from this unexecuted review.

## 9. Subsequent static code review before the public pin

After the separate symbolic review above was written, its reviewer read
PROOF.md and primary.py against that argument, without reading independent.py
or executing scientific code. No mathematical defect was found. Separately,
the primary implementation's author statically reviewed the already completed
independent.py, including its centered generator offsets, modular nullspace,
table hashing, trajectory boundaries and inverse order. The implementation
methods had already been written before this cross-reading. Their shared
analytical targets and JSON contract were known throughout.

The independent implementation's off-support witness was strengthened before
pinning to lie on stable H1. A further static wrapper/preregistration review
found that malformed child outputs could be discarded on failure; before the
pin, every controlled failure path was changed to retain every started child's
exact streams and exit code, including an earlier successful child. A final
static reread confirmed that correction. All six preregistration fields,
scope boundaries, deterministic success output and public-safety limits passed
that review. The input hashes and public authority/issue receipt are filled
only after the final preflight, before the pin.

These are same-session static reviews, not executed tests or external human
approval. No newly written scientific code was run or imported during them.

[canon-port]: https://github.com/mathorn1973/twist-j/blob/08ec6f93b5f70ad662bb447cd6cc41ccc62fa5f3/canon/CANON.md#L6658
[port-proof]: https://github.com/mathorn1973/twist-j/blob/08ec6f93b5f70ad662bb447cd6cc41ccc62fa5f3/probes/P-QDD-UNINTERRUPTED-RECORD-1/PROOF.md#L588
[sum-proof]: https://github.com/mathorn1973/twist-j/blob/ec4995176d36005ba924e0b381c3cc72b97420fc/probes/P-U-NATIVE-FIXED-READ-1/PROOF.md
