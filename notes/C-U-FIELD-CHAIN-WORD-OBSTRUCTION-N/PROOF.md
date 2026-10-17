# Two exact obstructions in the inherited integer-chain alphabet

NON-CANONICAL / candidate-T / L1. No authority or public status change.
Author: A. M. Thorn.
Reservation: #1590. Frozen question: CONTRACT.md at
`dfbe4ef237e9fbf07f5e1886a5af9721a7b869a9`.

This is an authored proof with a finite self-audit, not an independent
review. Its universal quantifiers are proved below, not inferred from the
finite computation. The separate finite execution is recorded in RUN.md.

## 1. Inherited objects and exact scope

Write A=A_f and retain the literal matrices L,B_f,P,S and the complete
chain carrier of DEF-FIELD-WORK-RECORD-CHAIN in Public Canon v103.
Its integer active field is y=(a,b,c,d), with

```text
A = [[ 1, 0, 1, 0],
     [ 0, 1, 0, 1],
     [-2, 1,-1, 1],
     [ 1,-3, 1,-2]],

L = [[ 1,-3,-1,-2],
     [-3, 4,-2, 1],
     [ 0, 5, 1, 2],
     [ 5,-5, 2,-1]],

H(y)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd.
```

The inherited identities used are

```text
A^5=I,  A L=L A,  L^2=5 A^3,
H(Ay)=H(y),  H(Ly)=5H(y),
H(y) is a positive definite integer-valued form on Z^4.
```

Consequently A is unimodular, L is invertible over Q, and

```text
L^2 Z^4 = 5 Z^4.
```

These are hypotheses from the existing Canon proof, not new discoveries.
The exact image criterion is

```text
L Z^4 = {y : y0+2y1 = y2+2y3 = 0 (mod 5)}.
```

Its image modulo five is the marked plane

```text
G_L = {rho(s,t)=(3s,s,3t,t) : s,t in F5}.
```

For the unchanged zero-origin native U, the two fixed comparison residues
at native boundaries three and four are

```text
rho3 = (0,0,3,1) = rho(0,1),
rho4 = (2,4,0,0) = rho(4,0).
```

The native counter and the integer-chain step are not identified. Q1 asks
whether some finite intervening word in the already declared chain
primitives can realize these two marked endpoints at one and the same
cell. A negative answer for arbitrary word length also excludes a single
macrostep and any finite prescribed waiting interval.

### 1.1 What each permitted primitive really does to this cell

Suppose its raw field has the integral split P y+S sigma. All other stored
coordinates remain part of the state even when not written in a formula.
The complete primitive list has the following active-field restrictions:

| Actual primitive at the fixed cell | Active field | Static component |
| --- | --- | --- |
| F or F inverse | A y or A inverse y | fixed |
| Accepted G, literal R to AM | L inverse y, only when integral and funded | fixed |
| Accepted G, literal AM to R | L y, only when funded | fixed |
| Rejected G or identity | y | fixed |
| True Ghat inverse or forward Ghat | the same active-field G branch | fixed |
| Neutral resource swaps A_j,B_j, or their inverses | y | fixed |
| Primitive at another cell | y | fixed |

In particular, A_j and B_j do not swap field vectors. The shared letter A
in the field matrix and the indexed resource contact A_j denotes different
operations. The C5 pointer writer changes the pointer and not the field
formula. Its inverse is the actual recovered-input inverse, not an assumed
involution of Ghat.

All listed field operations preserve the integral split when accepted.
The guarded L inverse has an integer output by its admission condition.
Thus every prefix of an allowed execution remains in the split carrier
at this fixed cell. Rejections retain the entire input. Nothing here
replaces the guard with clipping, erasure, or an externally paid deficit.

## 2. Field-word and depth lemmas

### Lemma 1: a necessary normal form for every actual field word

For every finite actual word of the frozen primitives, the active field
at the fixed cell has the form

```text
y' = A^k L^m y,       k,m in Z,
```

as an equality over Q. Every actual intermediate field is integral.

**Proof.** By the table, each step multiplies y by A, A inverse, L,
an admitted L inverse, or I. These matrices commute over Q, so collecting
factors proves the formula. State-dependent guards and arbitrary adaptive
choices of the next permitted primitive affect k and m but not the
formula for the realized path. A zero field remains zero. This normal
form is a necessary condition; not every pair (k,m) is a legal word under
the matter labels and funding guards. Using the larger normal-form class
for a nonexistence proof is therefore conservative. QED.

### Lemma 2: the L-depth is finite and exactly covariant

For a nonzero integer field y define

```text
nu_L(y) = max {j>=0 : y in L^j Z^4}.
```

This maximum exists. For every such y,

```text
nu_L(Ay)=nu_L(y),
nu_L(Ly)=nu_L(y)+1,
nu_L(L inverse y)=nu_L(y)-1 whenever the inverse is integral.
```

**Proof.** The nested sublattices L^j Z^4 contain y only for bounded j.
Indeed y=L^j v implies v is nonzero and
H(y)=5^j H(v)>=5^j, since H(v) is a positive integer. The allowed j
include zero, so there is a finite maximum. The same conclusion follows
from L^(2j) Z^4=5^j Z^4.

Because A is unimodular and commutes with L, A maps each L^j Z^4
bijectively onto itself. For j>=1, injectivity of L over Q gives
Ly in L^j Z^4 iff y in L^(j-1) Z^4. This proves the raising formula;
applying it to an admitted L inverse y proves the lowering formula. QED.

### Lemma 3: every nonzero gate residue has depth exactly one

If y mod5 is a nonzero element of G_L, then nu_L(y)=1.

**Proof.** The image criterion gives y in L Z^4. Its nonzero residue
excludes y in 5Z^4=L^2 Z^4. QED.

### Corollary: a residue invariant at gate-to-gate endpoints

For every permitted execution with both endpoint residues nonzero in
G_L, the two residues lie in the same A orbit.

**Proof.** Along the actual integral path, Lemma 2 changes depth by +1
for each L and -1 for each admitted inverse. Both endpoints have depth
one by Lemma 3. The total exponent m in Lemma 1 is therefore zero,
so y'=A^k y. This includes paths which temporarily leave the nonzero
G_L residues, pass through depth zero or larger depths, or wait for
resource transport. The endpoint conclusion is unchanged. QED.

## 3. Q1: native boundary three cannot continue to four in this alphabet

Direct multiplication gives

```text
A rho(s,t) = rho(s+t,t) mod 5.
```

For completeness its four coordinates are
(3s+3t,s+t,-5s-2t,5s+t), which have the displayed residues.
Iteration gives rho(s+kt,t). For t nonzero its orbit has five elements;
for t=0 the orbit is a singleton. These are the four five-point orbits
and the five fixed points of the complete 25-point gate plane.

The orbit of rho3=rho(0,1) is precisely

```text
{(3k mod 5,k,3,1) : k in F5}.
```

It contains no rho4=rho(4,0). The preceding corollary thus proves:

> **Q1, candidate-T.** For every N>=2, every fixed marked cell, every
> integer active-field representative of rho3, every integer static
> component, every legal complete assignment of the other chain states
> and nonnegative resources, and every finite actual word of the frozen
> primitives and their true inverses, the active field at that same cell
> cannot end with residue rho4.

No energy-one assumption is used. No finite energy ceiling, finite word
search, common scheduling restriction or field-only energy-conservation
assumption is used. Each initial state has finite integer coordinates,
but the theorem quantifies over all such states and all finite words.
The original fixed four-layer chain is a subclass of the allowed words.
All of its complete energy, charge and inverse guarantees remain intact;
they cannot supply a missing operation outside the primitive alphabet.

The result strengthens the old unit-lift obstruction in a different,
explicitly dynamic direction: the old theorem excludes an energy-one
preimage of rho4 even with arbitrary choices. This theorem admits all
energies but restricts the transition to the inherited chain alphabet.
It does not exclude arbitrary higher-energy lifts as arithmetic objects.

### 3.1 An explicit outside-alphabet control

The minimal boundary-three representative is y3=(0,0,-2,1), H(y3)=5.
An allowed free field step has

```text
A y3=(-2,1,3,-4),   A y3 mod5=(3,1,3,1).
```

Consider instead the signed block exchange

```text
B_star(a,b,c,d)=(-c,-d,-a,-b).
```

It gives

```text
B_star y3=(2,-1,0,0),
B_star y3 mod5=rho4,
H(B_star y3)=15.
```

This is an explicit integer representative of the target residue, not a
claim of its minimum. B_star is an integral involution preserving the
gate plane, but it is not a word in the admitted field alphabet on this
input: it changes the gate-orbit invariant t. Its field energy increase
of ten also precludes calling it an H-isometry. Writing B_star as a new
operation, or adding a compensating store by hand, is not a derivation of
its native or physical admission. No such complete added contact is
constructed or asserted here.

## 4. Q2: a complete equal-energy source noninterference theorem

Fix a source cell i and integer vectors u,v with H(u)=H(v)=h. Prepare
two copies of the complete chain with source matter R and source fields

```text
P L u+S sigma,       P L v+S sigma.
```

All other complete coordinates are identical, including static sigma,
source spectators and resource, every other occupied cell, every neutral
channel and the pointer, when present. For h=0 positivity forces u=v=0;
nontrivial messages require h>0. The theorem does not assume other cells
are cold, neutral, on the Gauss subset, or successful reaction inputs.

At every common primitive prefix the following joint invariant holds:

1. Every state coordinate outside the source active field is equal.
2. The two source active fields are
   A^k L^epsilon u and A^k L^epsilon v, with common k in Z.
3. Their common source matter is R when epsilon=1 and AM when epsilon=0.

**Proof by induction.** Initially k=0 and epsilon=1.

A source F or F inverse adds +1 or -1 to the common k. It leaves every
other source coordinate unchanged. A source G on matter R has an
integral inverse field automatically because

```text
L inverse A^k L u = A^k u.
```

Its inverse-field energy is h. Both copies therefore test the identical
condition r+4h-2>=0. If rejected, neither changes. If accepted, both
change to AM, epsilon=0, and the same resource r+4h-2. On matter AM,
the field energy is h, so both test r+2-4h>=0. Acceptance multiplies
both fields by L, restores R and epsilon=1, and gives the same resource
r+2-4h. Rejection fixes both complete inputs.

The source static part is unchanged. The spectator, reacting-vector sum,
node charge and divergence accounts remain exactly those of the inherited
G proof. The pointer's forward event predicate and the recovered-input
predicate of its true inverse depend here on the same common accepted
matter transition, so their increments or decrements coincide.

A neutral contact reads and swaps only equal resources/channels. At any
other cell every complete input is identical, so its deterministic
primitive, including any split/image/funding rejection or occupied-pointer
inverse, gives identical complete outputs. These cases exhaust the frozen
alphabet and prove the induction. QED.

It follows that every receiver other than the source has the same full
history in both copies, not merely the same energy or one output. Any
fixed reading of that complete history is equal. Equality holds at every
finite prefix and hence at every index of an infinite common execution.

A controller using only equal receiver history or the other already-equal
state coordinates chooses the same next primitive in the two copies;
the induction therefore also covers that declared common adaptation.
A controller reading the differing source active field is an extra
message-access route and is explicitly not part of Q2. The Q1 obstruction
above, in contrast, already allows arbitrary scheduling for each path.

> **Q2, candidate-T.** Within the displayed R/PLu preparation class and
> common permitted protocol, all source-field distinctions on one fixed
> energy shell are invisible to every other complete cell and record,
> for arbitrary continuing occupation and funding. The source fields
> themselves need not coincide and their differences are not erased.

Equivalently, the receiver-history map factors through the scalar H(u)
when the rest of the complete preparation and protocol are held fixed.
This concerns the selected integer resource-chain port. It is distinct
from the Canon's U-CONTACT-SOURCE-NONINTERFERENCE theorem for the separate
rational (q,r)-fed wave/tape contact. Neither theorem can be silently
applied to the other's carrier or admitted controls.

### 4.1 The channel is not constant when source energy changes

For w=(0,0,1,0), H(w)=1 and H(2w)=4. At a two-cell source initially
(R,0,PLw,0) or (R,0,PL(2w),0), with a common blank R receiver and
zero channel, the first local accepted source branch deposits respectively

```text
4H(w)-2=2,             4H(2w)-2=14.
```

The existing resource swaps deliver these different amounts to the
receiver at the first boundary. This is an inherited-law control of the
scope: norm changes can be visible, while distinctions within a fixed
norm shell cannot. This does not provide a native preparation mechanism
for choosing w or 2w from a source message.

## 5. Consequences and limits

Q1 is a complete negative answer for the fixed original-chain alphabet
and fixed W comparison, even after removing the unit-energy restriction.
Q2 explains why equal-energy field codes cannot repair that interface
merely by attaching an otherwise common occupied receiver or more fuel.

A positive successor must identify an independently admitted action outside
the Q1 orbit-preserving alphabet and actual message access not factored
only through the Q2 scalar norm. A proposed new action must retain its
complete state, inverse, occupied-state guards and full energy account.
These are necessary demands, not a proof that any proposed new action is
sufficient or physically allowed. The existing primitive set is not
changed, and neither failed condition is reinterpreted as success.

No claim is made about all integer field models, altered preparations,
other native comparison maps, moving frames or addresses, direct field
exchange, new additive sources, source-sensitive controllers, rational
H_B implementations, physical energy, apparatus realization or any L2-L6
bridge. QDD-INSTRUMENT-APPARATUS and every other public owner remain
unchanged. The two negative mathematical conclusions have candidate-T
status, not public F and not a newly registered O.
