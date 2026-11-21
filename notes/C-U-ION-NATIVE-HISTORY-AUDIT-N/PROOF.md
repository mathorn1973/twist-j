# Retained-selector dilation and the first native history loss

**NON-CANONICAL analytical audit.** Reservation
[#1366](https://github.com/mathorn1973/twist-j/issues/1366). Public authority
remains Canon v97. No scientific program is imported or executed here.
This is a conditional algebraic construction and a restriction on a stated
class of physical endpoints, not an available ion control sequence.

The original two-contact law and its complete-state collisions are already
documented in [CONTRACT.md](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/CONTRACT.md)
and [PROOF.md](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/PROOF.md), at public
main `2973a432303e046aacb2cee3cea97254ea3ab8eb`. Their stored
[HISTORY.csv](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary/HISTORY.csv)
is prior evidence, not a newly generated table. General native
irreversibility is not a new discovery of this note.

The fixed physical dictionary is exactly
[#1363 at its immutable note head](https://github.com/mathorn1973/twist-j/blob/8847b657c648b5c2b231eca13d9adfbef451cc60/notes/C-U-ION-OFFSET-GLOBAL-AUDIT-N/README.md).
The local exchange result is
[#1365 at its evidence head](https://github.com/mathorn1973/twist-j/blob/8cbdf106f6626698aabcc84c8d028bd12ff643c1/probes/P-U-ION-LS-LOCAL-EXCHANGE-1/RESULT.md),
with scientific candidate pin
`b1b2019f35fc2cc3bc5b3d364f9d6ad8c2051a11`. Its model factors the completed
ideal contact word from its included motional and spectator remainder. It
does not supply a physical native-step dilation or a finite quantum work
source. The derivations below do not rerun either predecessor.

## 1. The branch maps and the actual selectors

All coordinate arithmetic is in F5. In logical coordinates
`chi=(p1,p4,p1p,p4p,q,r)`, write `P=(p1,p4,p1p,p4p)`, `kappa=sum(P)` and
`z=kappa+q+r`. The canonical branches, in label order 0,...,4, are

```text
g0 = a: (p4,p1,p4p,p1p,q,r),
g1 = b: (-p1p,-p4p,-p1,-p4,-q,-r),
g2 = c: (2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
g3 = d: (2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
g4 = e: (2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

Each is an involution on the entire six-pentit space. For a, the two
coordinate swaps undo themselves. For b, the signed swaps and two sign
changes undo themselves. For d and e, each coordinate has the form
`x -> constant-x`. For c, applying the map twice gives, for example,

```text
p4'' = 1-(1-p4-r)+(-r) = p4,
p4p'' = 1-(1-p4p+r)-(-r) = p4p;
```

the other four coordinates similarly return. Thus `g_j^-1=g_j` for
every branch. This is also the canonical involution property; selection
by the current state does not inherit that invertibility automatically.

Let K1 be the identity and K2 replace q by its physical label `y=q-1`.
Write `G_(i,j)=Ki g_j Ki^-1`. These conjugated branches are again
involutions. For either receiver let v denote its physical fifth label
(q on R1, y on R2), and define

```text
delta_1=0, delta_2=1,
theta_n=popcount(n) mod2,
j_(i,n)(P,v,r)=kappa+v+r+delta_i+2 theta_n mod5,
F_(i,n)(chi)=G_(i,j_(i,n)(chi))(chi).
```

The selector acts on the actual post-contact coordinates. The additive
offset on R2 is mandatory. No original input label a1 or a2 is supplied
to this rule. These are the full six-coordinate native targets, not
operations only on the eventual archive reader.

## 2. An exact abstract permutation with a retained selector

Fix i and n and abbreviate its selector by j(chi) and its branches by G_k.
Adjoin one explicitly counted five-state register M. On the entire basis
of `H_data tensor H_M`, define

```text
k = m+j(chi) mod5,
Phi: |chi,m> -> |G_k(chi),k>.
```

This is a total permutation, not merely an unspecified extension of an
isometry. Its inverse, evaluated on arbitrary output `(chi',k)`, is

```text
chi = G_k(chi'),
m = k-j(G_k(chi')) mod5.
```

The involution property verifies both compositions directly. Equivalently,
Phi is the composition of a reversible selector addition
`(chi,m)->(chi,m+j(chi))` and a branch permutation controlled by the
resulting memory label. These are algebraic factors of the definition;
neither factor is declared to be an available physical gate.

On the specified ready sector this gives the desired isometry

```text
Phi |chi,0> = |F_(i,n)(chi),j_(i,n)(chi)>.
```

If two outputs agree, their retained selectors agree, so the common
invertible branch recovers the same chi. Hence the isometry is injective
on every input basis state and preserves all inner products by linearity.
We have chosen amplitude +1 for every basis transition. This coherent
phase convention is an explicit candidate target, stronger than the
predecessor's classical coordinate table; that table does not derive it.

For one simultaneous native step of two receivers, two blank registers
M1,M2 give a finite 25-dimensional selector bank. The two copies of Phi
commute because they act on disjoint data and memory factors. Both source
ports are retained unchanged during this native part, and the fixed
counter input n has output n+1. In particular, the complete target for
that one input-counter sector includes all fourteen data coordinates,
the two new selector labels and the new counter value. No realization of
an unbounded physical counter follows from this one-step construction.

This 25-state bank is a conditional one-step sufficient register for the
displayed algebra, not a minimum, a full-machine resource bound or a
reusable blank supply. If it is used again with nonzero m, the selected
branch is generally `m+j(chi)`, not the native j(chi). A further step
therefore needs an explicit treatment of its already occupied history.

An algebraic extension `Phi tensor I_B` also acts on an arbitrary
inherited ancillary system B, including states correlated with data or
with a reference, provided the newly specified M really is in the
declared blank sector. Identity on B is an optional future target for
identified spectator factors, not a claim that a finite physical laser,
controller or work source returns unchanged. Those sources must have
their own physical input and output account. In particular, nothing here
justifies placing a fresh M at counter six without preparing and carrying
that counted resource from the beginning or explicitly supplying it.

## 3. A collision in the actual first native step

The fixed dictionary gives the prepared family, in physical labels,

```text
(n; S1,S2; R1; R2)
  = (0; a1+1,a2+1; (0,0,0,0,1,0); (0,0,0,0,0,0)).
```

Fix any one `t=a2+1` and compare the two actual histories a1=2 and a1=3.
Their first source labels are s=3 and s=4. The first exchange family W1
has the exact basis-label action `(s,1)->(1,s)`. Thus the complete data
inputs to the native part are the two orthogonal codewords

```text
D_3 = (0; 1,t; (0,0,0,0,3,0); (0,0,0,0,0,0)),
D_4 = (0; 1,t; (0,0,0,0,4,0); (0,0,0,0,0,0)).
```

Since theta_0=0, R1 selects d on D3 and e on D4. Direct substitution
gives

```text
d(0,0,0,0,3,0) = (2,1,3,4,3,1),
e(0,0,0,0,4,0) = (2,1,3,4,3,1).
```

R2 selects its conjugated b on its all-zero physical state and becomes
`(0,0,0,0,3,0)`. S1 stays 1, S2 stays t, and the counter becomes 1.
Consequently both histories require the same full data-and-counter target

```text
Y_t = (1; 1,t; (2,1,3,4,3,1); (0,0,0,0,3,0)).
```

This is an actual two-history collision inside the required 25-history
family, not an off-family input selected from the full six-pentit space.
It agrees with the predecessor's stored rows for a1=2 and a1=3 at
boundary 1. The fixed change of R2.q moves the same old equality to the
new physical dictionary; it does not remove it.

The retained-selector construction instead has distinct outputs
`|Y_t> tensor |3,1>` and `|Y_t> tensor |4,1>`. It exposes precisely where
the distinction can go, if a physical interaction with the memory exists.

## 4. Why data-only unitary endpoints cannot implement this step

Allow an arbitrary, input-independent unitary V on all fourteen data
registers, with any data support or asymmetric data controls. The two
input codewords D3,D4 are orthogonal, so their images under V are
orthogonal. Suppress the common, fixed counter labels and let

```text
p_3 = |<Y_t|V|D_3>|^2,
p_4 = |<Y_t|V|D_4>|^2.
```

The projector onto their two-dimensional input span is bounded by the
identity. Therefore

```text
p_3+p_4 = <Y_t| V (|D_3><D_3|+|D_4><D_4|) V^dagger |Y_t> <= 1,
max(1-p_3,1-p_4) >= 1/2.
```

The success event is the exact rank-one codeword of the full fourteen
data coordinates at the prescribed counter, without postselection. This
is not a bound for the coarse archive reading W1 alone. The conclusion
also applies when the endpoint factors as `V tensor W_B`; arbitrary
inherited B states, even different between the two histories, do not
change these data probabilities. With the declared common initial
remainder and #1365's ideal factorized first exchange, the remainder is
in fact still common immediately before this first native step.

This obstruction does not use port-swap symmetry and persists if every
data-only unitary is admitted. It therefore cannot be repaired merely
by adding more data-only pair supports. Closed motional excursions may
entangle data and motion during a pulse, but if the complete endpoint
factors in this way, they retain no needed distinction outside the data.

A unitary that transfers this distinction into an explicit history
register, a work source, a controller or an environment is outside the
excluded class. It can evade the bound, subject to its own physical
availability and resource conditions. The original data collision alone
does not forbid such a dilation. Conversely, even if a separate post-C
physical instant is not required, the entire first enlarged update has
the same two orthogonal prepared inputs and common complete data target;
the data-only endpoint bound still applies to that combined update.

## 5. When the selector can and cannot be uncomputed

For a declared input domain A, erasing j while retaining F(chi) is
possible by a reversible computation from the data alone exactly when
j is a function of F(chi) on A. Necessity follows because a common data
output cannot select two different inverse erasures. Sufficiency follows
by reversibly subtracting that function from M. Since every branch is
injective, this condition is equivalent to injectivity of F restricted
to A.

The two actual inputs above violate it: their common output would have
to determine both j=3 and j=4. More generally, no unitary can map the
orthogonal outputs `|Y_t,3,1>` and `|Y_t,4,1>` to one identical full state.
Information may be moved to some other counted factor and the scratch
selector then reset, but it has not been erased from the whole machine.
Applying Phi inverse resets its memory by restoring the previous data;
it does not retain the required updated data at the same time.

This statement leaves room for restricted domains where uncomputation
does work. It also leaves room for existing history H that makes the
selector recoverable from `(F(chi),H)`. Such a construction must state
and evolve H, including its actual inherited state; it cannot assume
H is common or freshly blank after an earlier merger.

## 6. Full-space fibres are a separate, stronger-domain calculation

For clarity, the complete six-pentit map has a simple analytical fibre
classification. Summing the branch coordinates gives the logical trace
maps `z, -z, 2-z, 2-z, 3-z` for a,b,c,d,e. For fixed theta the selected
input trace is `z=j-2 theta`. Thus

| theta | output logical trace z' | possible retained labels j | fibre size |
| --- | --- | --- | ---: |
| 0 | 0 | 0,2 | 2 |
| 0 | 4 | 1,3,4 | 3 |
| 1 | 1 | 1,3,4 | 3 |
| 1 | 2 | 2 | 1 |
| 1 | 3 | 0 | 1 |

All other output traces have empty fibres. Every branch maps its selected
trace hyperplane bijectively onto the stated output trace hyperplane:
the affine involution and its trace formula prove this directly. Each
listed label therefore contributes exactly one predecessor to every
full output codeword in that hyperplane. On R2 the physical output trace
is `zbar'=z'-1`; cardinalities are unchanged by K2.

It follows that the full single-cell map has maximum fibre size three,
and the independent pair of full native cell maps at a fixed counter has
maximum fibre size nine. Passive source labels and a fixed counter do
not change this. Precomposing with the complete algebraic contact, which
is a permutation on its full domain, also preserves these fibre sizes.
This statement does not extend #1365's restricted local exchange word to
that complete contact domain.

Under orthogonal input encoding, common pure initial remainder and exact
pure full data outputs, these maximum fibres imply lower bounds three
and nine on remainder dimension for those respective full-domain tasks.
They are not lower bounds for the narrower 25-history preparation. The
actual first-step witness requires at least two distinguishable residual
states. The older fourfold complete merger at boundary nine requires at
least four under the same pure-code hypotheses, as already noted in
#1363. Equal coarse logical readings alone require distinguishable states
somewhere in the full physical decoding fibre; they do not by themselves
force all those distinctions into a separately designated remainder.

No claim that four, nine or twenty-five states suffice for the complete
physical machine follows. The finite-horizon history targets need their
specific preparations, fixed physical timing, source and energy outputs,
archive protection and actual native-control interactions. The selector
permutation proves an abstract way to retain the missing information;
the first actual collision proves why such an information destination is
needed. A sourced Hamiltonian and a finite implementation of that transfer
remain absent.
