# C-H3-MATERIAL-READ-CONTROL-N: material-controlled native reading

NON-CANONICAL / NO AUTHORITY. Action layer L1.

Status: candidate-T for the conditional algebraic statements proved below.
No trajectory, successful endpoint, duration, finite census or resource
number is established by this file. Such findings are separate candidate-C
computations under `PREREG.md`, frozen at
`0fabe9ffdb8b387614344aa484589e3898bdb784`, and claim
[#2139](https://github.com/mathorn1973/twist-j/issues/2139).

The native law is the unchanged
`reproduce/h3-referenced-record/verify.py` at public main
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, SHA-256
`4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd`.
The particular retained material preparation is a computational premise
from `notes/C-H3-CLOCK-CONTACT-N/RESULT.md` at
`524dd4622cf23d04ef78ecc2564f649ab2a832e2`. That candidate source is not
Canon authority. The lemmas below do not extend its certified time window
or infer a successful new reader from its retained sum alone.

## 1. Ring and the information used by a local contact

Let `O=Z[j]`, with `1+j+j^2+j^3+j^4=0`, let `K=Q(j)`, and put

```text
rho=j^2,       J=1+rho,       J^-1=-j-j^2,
h(z)=z*conjugate(z),         gamma=h(J),
q(z)=Tr_K/Q(h(z))/2.
```

Both `J` and `rho` are units of `O`. The real element
`gamma=2+j^2+j^3` satisfies `gamma^2-3*gamma+1=0` and is strictly
positive under every real embedding of the real subfield. In particular
`gamma!=1`, `gamma^2!=1` and `gamma^4!=1`. For example positivity
would make `gamma^4=1` imply `gamma=1`, contradicting its displayed
quadratic equation. Also `J!=1` and `J^2!=1`.

A local cell has rails `(a,b,g,r)=(r0,r2,CLK,CORR)`. If either
`a-b` or `g-r` is outside `2O`, B leaves it unchanged. Otherwise define

```text
d=(a-b)/2,       f=(g-r)/2,
m=(a+b)/2,       c=(g+r)/2.
```

The centers `m,c` are retained. B1 applies when `d!=0` and
`h(f)=gamma*h(d)`, sending `(d,f)` to `(J*d,J^-1*f)`. B2 applies
when `f!=0` and `h(d)=gamma*h(f)`, sending `(d,f)` to
`(J^-1*d,J*f)`. All other cells are idle. These nonzero branches are
mutually exclusive because their simultaneous conditions would give
`gamma^2=1`. Each is the inverse of the other.

The radiation output depends on material only through the branch tag:

| Tag | Outgoing half-difference | Outgoing `(CLK,CORR)` |
|---|---|---|
| Idle | `f` | `(c+f,c-f)` |
| B1 | `J^-1*f` | `(c+J^-1*f,c-J^-1*f)` |
| B2 | `J*f` | `(c+J*f,c-J*f)` |

Whenever any nonzero branch occurs, `f!=0`. The three displayed outputs
are then pairwise different. This follows from `J!=1`, `J^2!=1`, and
the absence of zero divisors in `O`.

## 2. Exact local discrimination criterion

Define the material key of a pair by

```text
kappa(a,b) = BOTTOM,                  if a-b is outside 2O or a=b;
             h((a-b)/2),             otherwise.
```

`BOTTOM` is a distinct symbol, not a ring value. A pair with that key
is idle for every radiation input. For an admitted pair with `d=0`,
B1 is excluded by its nonzero condition, and B2 would require
`0=gamma*h(f)` with `f!=0`, which is impossible.

**Local discrimination theorem, candidate-T.** Two material pairs can be
distinguished by the B tag and radiation output of some common integral
radiation input if and only if their keys are different. The material
centers are unrestricted and need not agree. This is an instantaneous
local statement, not an assertion that the key classifies future material
trajectories under C.

**Necessity.** If both keys are `BOTTOM`, both contacts are always idle.
Otherwise equal non-bottom keys give the same parity admission and the
same two norm equalities for every common radiation input. They therefore
give the same tag and the same radiation output. An odd radiation
difference leaves both contacts idle as well.

**Sufficiency.** Choose a pair with a non-bottom key, write its nonzero
integral half-difference as `d_a`, and use the common balanced radiation
input `(g,r)=(f,-f)` with `f=J*d_a`. Its tag is B1. The other pair,
whose key is different, cannot also have tag B1: that equality would
force its key to equal `h(d_a)`. It is either idle or B2. The radiation
outputs are different by Section 1. Every supplied slot is integral.

For a prescribed positive class, a sharper statement is useful.

**Strict positive-reader theorem, candidate-T.** A common radiation input
making the positive material pair active and the negative pair idle
exists if and only if

```text
kappa_positive != BOTTOM
and
kappa_positive != kappa_negative.
```

When these conditions hold, at least one of the two canonical probes

```text
f1=J*d_positive,       f2=J^-1*d_positive
```

has the required property. The first gives positive B1 and the second
positive B2.

**Proof.** The necessity follows from the local discrimination theorem
and the inactivity of `BOTTOM`. If the negative key is `BOTTOM`, both
choices work. Otherwise write `k_plus=h(d_positive)` and
`k_minus=h(d_negative)`, with `k_plus!=k_minus`. For `f1`, negative B1
is impossible, and negative B2 occurs exactly when
`k_minus=gamma^2*k_plus`. For `f2`, negative B2 is impossible, and
negative B1 occurs exactly when `k_minus=gamma^-2*k_plus`.
Both obstructing equalities would imply `gamma^4=1`, since `k_plus`
is nonzero. Thus at least one probe leaves the negative pair idle.

No claim about other cells or later retention follows from the local
theorems. The experimental family uses exactly its two canonical choices,
with no extra phase variants.

## 3. A balanced probe before an actual C/B tick

The material pairs in Section 2 must be those actually reaching the
post-C read cut. In general they are not the pairs at the preceding full
cut. The preparation below respects that distinction.

Fix a supplied full state at cut `s`, its matching bit, and a read cell
`(x,y)`. Let `y'` be that cell's vertical partner in the next C matching
and `x'` its horizontal partner. The four selected radiation slots are

```text
CLK(x,y),       CLK(x,y'),
CORR(x,y),      CORR(x',y).
```

Load the same fixed probe into every member of the declared input family:
both CLK slots receive `+f`, and both CORR slots receive `-f`. These
are four distinct slots even though their sites may overlap. All
material is retained. The probe choice, slot set, start cut and matching
bit are common to the compared histories, not selected separately after
observing an individual input's predicate.

The actual C contact preserves each equal radiation pair, so the target
arrives at B with common radiation `(f,-f)`. Vertical material transport
is independent of radiation. Its target pair is exactly the post-C pair
computed from the supplied material state under the actual integral C,
including refusals. Consequently the local theorems apply to these
post-C keys and half-differences without an intervening external change.

For a strict reader, the negative radiation output is `(f,-f)`. The
positive output is `(J^-1*f,-J^-1*f)` for B1 or `(J*f,-J*f)` for B2.
These fixed two-slot outputs are different. If the two material donor
states and the probe are common across all other contexts, the first
output depends only on the material donor class, independently of those
contexts. Both donor classes must occur to assert exactly two output
classes; otherwise only the occurring class can be asserted.

Other cells can have their own B events. Their updates are simultaneous
and local, so they cannot influence the target's first B output in this
same tick. They must nevertheless be included in full-field conservation,
inverse and later-continuation checks. No silence of other cells or
duration of the target output is inferred from this construction.

For the particular column-4 experiments, an odd relative start cut has
next matching bit one, since the previous input boundary was at even
absolute time 114. Thus the target CORR partner is in column 3 rather
than the old archive in column 5. If column-3 material is still zero,
its B is necessarily idle regardless of the probe. More generally, any
claim about old-archive preservation requires the relevant actual
background and slot-locality premises; it is not granted by a probe's
zero linear sum.

## 4. Explicit closed accounts for material-by-background controls

A preparation may be reversible and fully funded without being a native
H3 preparation mechanism. The distinction is explicit here.

Let `F_h` be complete active-torus background states at one common full
cut and bit, where `h` includes every declared source, old-record and
radiation context. Retain each background's already supplied source
reserve `R_h` as well. Assume the complete accounts of `F_h plus R_h`
are common across `h`; equality of reserve contents is not assumed.
Let `D0,D1` be two fixed material
donor blocks, each containing all material slots of the read column at
that same cut. Include both donors in every experiment, whether or not
one has the same account as the other. Their complete contents and
origin are supplied premises.

Also include the fixed four-slot radiation probe

```text
P=(f,f,-f,-f).
```

Keep source, donor and probe slots as explicit reserves outside the active
torus. Their material or radiation types are fixed. During native
continuation they are retained unchanged and do not feed the torus.
The initial combined state is

```text
F_h plus R_h plus D0 plus D1 plus P.
```

Its complete accounts are independent of `h` and of the later choice of
donor `a in {0,1}`. For control `a`, first swap the entire active read
column's material block with the corresponding fixed slots of `Da`.
The displaced active material remains in that reserve; the other donor
remains untouched. Next swap the four probe slots with the four active
radiation slots of Section 3. Every outgoing radiation value remains
in its paired probe-reserve slot.

These are permutations of same-type slots. They preserve the complete
material sum, complete radiation sum and complete Hermitian account
exactly, and are reversible by the same swaps in reverse order. The
probe's own added accounts are

```text
S_material(P)=0,
S_radiation(P)=f+f-f-f=0,
H(P)=4*h(f),
Q(P)=4*q(f).
```

The source reserve and both donors' costs are also included; the probe
formula is not the cost of the whole controlled experiment. The same
donor-account argument applies without `P` to the separately declared
material-by-background continuation controls. After loading, the active torus
alone need not have equal accounts across controls. The equality belongs
to the complete torus-plus-reserves state. Omitting outgoing values or
the unused donor would invalidate that account argument.

The selection of `a` is an explicitly declared control-preparation
choice, not an internally computed measurement. For each selected
protocol, the probe and slot choices are the same for all `a,h`. The
subsequent native tick contains no such selection. Its target material
comes from `Da`, and its target radiation is the common probe. This is
why a verified output depending only on `a` isolates a material-controlled
contact from pre-existing source or radiation differences among `F_h`.

For natural, unswapped record histories the material may already equal
the donor associated with its predicate. The crossed controls still
matter: covariance of a natural output with that predicate alone does
not isolate the material from other correlated coordinates.

Equal evolving fields with the same bit may be replayed once only if
reserve independence is proved: native evolution and the declared active
readers never inspect the inert reserves, so induction gives the same
future field trajectory regardless of their retained values. The
original ordered reserve states and input multiplicities still remain
distinct parts of the complete preparation. In particular equal field
representatives after the source swap do not identify the different
outgoing source values in `R_h`. Equal accounts alone never justify
deduplicating fields or complete states.

All external preparations leave the matching bit and native schedule
unchanged. Subsequent native evolution acts on the active torus and as
the identity on the retained reserves. Each C preserves its pair sum and
Hermitian account because `h(rho)=1`; refused pairs are fixed. Each B
preserves material and radiation centers separately and preserves the
combined Hermitian account by its balance equality. Its two branches
are inverse. Reversing C on each preserved admission domain, applying B
again and retaining the matching bit therefore gives the exact inverse
of each native tick. The external swaps remain separately declared
boundaries, not extra native gates hidden inside that tick.

If any further external action is admitted, its dependence must also be
specified. Merely writing outside the read column is insufficient to
preserve a causal comparison: a map could read its material and encode
it elsewhere. For the isolation argument, common future actions must
leave the relevant differing material alone and preserve equality of
all other active coordinates whenever those coordinates and their
supplied inputs agree. In particular retained control reserves may not
secretly drive later active inputs. An experiment with no further
external action satisfies this requirement directly.

## 5. No export of material differences before a tag difference

**Finite-prefix isolation lemma, candidate-T.** Compare two active H3
states with the same matching bit that differ only in the material rails
of one fixed column `x`. All radiation, including CLK inside that column,
is initially equal. Give them the same subsequent native evolution and
any external boundaries satisfying the equality-preservation condition
of Section 4. If their B tags agree at every row of column `x` through
a finite prefix, all radiation and all coordinates outside its material
rails agree at every full and post-C cut of that prefix.
This is a statement about active coordinates; any different inert
reserves remain separately retained and are not identified by the lemma.

**Proof.** Vertical C transports the possibly different material only
inside column `x`. Every radiation C has equal input pairs in the two
histories, including equal parity decisions, so its outputs agree.
Every material C outside that column likewise agrees. Consequently every
other column has an identical pre-B state and makes an identical B update.
Inside column `x`, common radiation and common tags produce identical
radiation outputs by the table in Section 1. Only its material may remain
different. This closes the induction. The stated boundary condition
preserves its induction hypothesis at any allowed boundary.

At the first native tick with different column-`x` tags, the pre-B
radiation is still common. A nonzero branch has `f!=0`; different tags
therefore produce different radiation outputs at at least one of those
cells, by Section 1. The outside-column state is still equal at that
full cut, since B is local and simultaneous. Later horizontal transport
can carry a CORR difference outward, but need not do so immediately if
its contacts refuse. Thus a tag difference is necessary for export from
material into radiation, and is not by itself a proof of a retained or
already distant output.

The lemma permits equal nonzero tags; it does not assume B is idle.
It establishes the stronger fact that equal tags cannot export a
material-only difference into common radiation. Conversely, actual
histories that already have different radiation at the comparison cut
do not satisfy its premise. A downstream event in such histories may
read an earlier emitted pulse or source difference. The funded crossed
controls give a way to separate that possibility from a later use of
the retained material.

## 6. Why the column sum is not a universal single-cell input

Define the material column sum

```text
S0=sum_y r0(x,y).
```

**Local limitation, candidate-T.** On the unrestricted supplied H3
carrier of height six, a single local B, or the target B of one full
C/B tick with a fixed common radiation probe, cannot universally read
`S0` from that column.

Choose a row `z` outside the target's two-row vertical matching pair.
Choose distinct integral values `a,b`. Let two fields agree everywhere
except that one has `(r0(x,z),r2(x,z))=(a,b)` and the other `(b,a)`.
They have equal complete material and radiation sums, equal Hermitian
accounts and equal `Q`: the only change is a same-type slot swap.
Nevertheless their `S0` values differ by the nonzero element `b-a`.

Their target local material is identical. After one C it is still
identical because the altered row is outside the target matching pair.
A common probe supplies identical target radiation. Their target B tags
and radiation outputs are consequently identical. Thus no universal
single-cell decoder of the stated kind can distinguish these different
column sums. Equal complete accounts do not remove this counterexample.

This is not a no-go for a multi-step native circuit, a larger prepared
reader, or a restricted finite successor-state family. On a specified
family, two different `S0` classes may also have different local keys at
a declared phase and row. Sections 2 through 4 can then read that family.
It is the proven family and its local key distinction that supply the
interface, not a general identification of `S0` with a cell input.

## 7. Scope, falsifiers and successor states

The strict-reader test fails at a selected local cut if the positive key
is `BOTTOM` or equals the negative key. This is an exact local negative
over every common radiation input, not merely the two canonical probes.
Failure of every selected cut in a frozen finite family remains bounded
by that family. A mismatch with the proved canonical-probe implication,
the actual C partner slots, native-law pin, account conservation or
two-sided inverse is an error or missing premise, not grounds to alter a
scientific threshold.

An active contact generally changes both material and radiation. The
reader can therefore consume or transfer the original material encoding
while preserving information in the complete reversible state. A fixed
radiation output at its first read cut does not imply that this output
persists, that the original material sum survives, that other old records
survive, or that the apparatus returns to its original ready field.
Each later observation and the complete successor-state family require
their own actual finite verification under the frozen contract.

A prepared endpoint is an explicit stock-and-swap construction followed
by genuine native evolution. It does not supply a preinstalled common
probe from the first apparatus time, an autonomous source loader, or a
mechanism making those boundary swaps occur. A success in that experiment
does not repair a failure of unchanged continuation. No physical readout,
occurrence law, native-U equivalence, L1-to-L6 lift, permanent finite
archive, unlimited renewal or Canon promotion is asserted.
