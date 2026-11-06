# One native law, three different memory obligations

2026-10-29. NON-CANONICAL, analytical L1 note. All register arithmetic is
in F5. Integer counters, counts, and inequalities retain their ordinary
meaning. No numerical extrapolation or new scientific run is used.

## 1. Fixed law and source identity

The primary public sources at
[`a193e389fb1ddb0bdc89165b015c95a17eb1e425`](https://github.com/mathorn1973/twist-j/tree/a193e389fb1ddb0bdc89165b015c95a17eb1e425)
are [CORE](https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/canon/CORE.md),
the native conventions preceding `U-NATIVE-SOURCE-RECEIVER-RECORD`,
`U-NATIVE-RECORD-CONTINUATION-BOUNDARY`, and
`U-NATIVE-INVARIANT-AND-NOWRITE` in
[CANON](https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/canon/CANON.md).

Write x=(a,b,c,d,q,r), z=sum x, theta_n=popcount(n) mod2. To distinguish
generator names from coordinates, use G_0,...,G_4:

```text
U(n,x)=(n+1,G_(z(x)+2 theta_n mod5)(x)),
G_0(x)=(b,a,d,c,q,r),
G_1(x)=(-c,-d,-a,-b,-q,-r),
G_2(x)=(2-c,1-d+r,2-a,1-b-r,1-q,-r),
G_3(x)=(2-a,1-b,3-c,4-d,1-q,1-r),
G_4(x)=(2-a,1-b,3-c,4-d,2-q,1-r).
```

These are the original a,b,c,d,e generators in that order. The complete
state includes n. A checkpoint is x alone. A reader does not change U.

The full public `reproduce/census/verify.py` is byte-identical between
v94 `af8dc5956e26917b265fd0070f500c841c326512` and the v106 main above:
8127 bytes, Git blob `f96615344421ea80b8dcfc31f8d905e9fd30fa8c`.
The autonomous-state/update block in CORE also agrees. This compares the
particular definitions; the complete CORE files and historical statuses
are not asserted identical.

## 2. Permanent one-shot record: the existing native witness

Fix source S=(a,c), data memory M=(b,d), reference C=(q,r), receiver
R=(b,d,q,r). For lambda in F5 prepare, at common counter zero,

```text
x_lambda(0)=(lambda,0,-lambda,0,0,0).
```

Only S varies. The actual first three selected generators are G_0,G_2,G_4,
giving

| n | Complete checkpoint |
| --- | --- |
| 0 | (lambda,0,-lambda,0,0,0) |
| 1 | (0,lambda,0,-lambda,0,0) |
| 2 | (2,1+lambda,2,1-lambda,1,0) |
| 3 | (0,-lambda,1,3+lambda,1,1) |

For receiver variables (u,v,q,r), put B=u+v, D=u-v-1,
zhat=3B+q+r. Define one total, counter-independent reader:

```text
BLANK,                    unless B in {2,3} and zhat in {1,4};
PRESENT(3-B*zhat*D),       otherwise.
```

The four displayed boundaries have (B,zhat)=(0,0),(0,0),(2,2),(3,1).
At n=3 the output is PRESENT(lambda). Let A=a+c. There A=2B, and
all subsequently selected G_1,G_3,G_4 negate A and B. Hence A=2B
persists and z=zhat on these trajectories. Their transformations are

| Selected generator | B' | D' | z' |
| --- | --- | --- | --- |
| G_1 | -B | D | -z |
| G_3 on z=1 or G_4 on z=4 | -B | -D | z |

Thus B*z*D and the readiness condition persist. The fixed reader is
BLANK for n<3 and PRESENT(lambda) for every n>=3. The distinct absence
preparation (0,0,1,0,0,0) keeps B=0 and is BLANK forever; occupied zero
is not absence. The supplied preparation is a premise.

The reference C is part of this interface. Bare M alone cannot give the
same stationary reading: M for lambda=0 at n=3 equals M for lambda=1 at
n=7. No claim of a two-coordinate stationary reader follows.

For every n>=1, the pairwise payload differences are

```text
x_lambda(n)-x_mu(n)=epsilon_n (lambda-mu) (0,1,0,-1,0,0),
epsilon_n in {1,-1}, common to all messages.
```

This follows at n=1 from the table, through the next two substitutions,
and thereafter from the displayed generators. Consequently every fixed
raw-coordinate target either contains b or d and already distinguishes
all messages at every n>=1, or contains neither and never distinguishes
them. The same dichotomy holds for a fixed affine observation Lx+c:
its payload coefficient is epsilon_n L(0,1,0,-1,0,0).

This family-specific continuation boundary starts at n=1. It is not
correct to call that time synchronized; synchronization begins at n=3.
Nor does the boundary cover arbitrary nonlinear readers or other initial
families. A nonlinear readout can hide and expose information already
present in its input without creating a new raw-coordinate receiver.

## 3. Newly created memory changes a distinct target

Use a different fixed partition: source S={r}, memory M={c,d}, target
A={a,b}, and reference q. For s in {0,1}, prepare

```text
y_s(0)=(0,0,0,0,2,s).
```

Exact application of the original selectors gives:

| n | Message 0 | Message 1 |
| --- | --- | --- |
| 0 | (0,0,0,0,2,0) | (0,0,0,0,2,1) |
| 1 | X=(2,1,2,1,4,0) | Y=(2,1,3,4,4,0) |
| 2 | (0,0,0,0,2,0) | (2,1,3,4,1,0) |

The generator sequences are G_2,G_2 and G_3,G_1. At n=1 the complete
environment outside M is identical: r=0, A=(2,1), q=4, and the counter
is common. Swapping the entire memory block exchanges X and Y exactly;
both are reachable, with explicit preimages in the table. The next target
is (0,0) or (2,1). Thus the only differing input at that comparison is
the created memory. Both the selector and direct coordinate formulas
depend on it; this example does not isolate either route.

The fixed M-only reader mapping (2,1) to PRESENT(0), (3,4) to PRESENT(1),
and every other value to BLANK is initially BLANK and correctly written
at n=1. At n=2 it gives BLANK and PRESENT(1). In fact y_0(2)=y_0(0)
as complete checkpoints. No fixed function of the checkpoint can label
these two occurrences respectively BLANK and permanently WRITTEN.
Their full autonomous states differ because their counters differ.

The memory difference at n=1 is (0,0,1,3,0,0), with nonzero sum. This
changes the selected generator. It is outside the zero-sum difference
line of Section 2 and occurs before synchronization. There is no conflict
with the earlier continuation boundary. There is also no permanent
record in both branches under this interface.

## 4. Reachable layers and exact relative evolution

Let I_n be the checkpoints reachable at counter n from all origin-zero
heads. Each G_i is an affine bijection of F5^6. Its output sum, as a
function of the input sum z, is respectively

```text
z, -z, 2-z, 2-z, 3-z.
```

On any fixed input hyperplane z=s, the selected affine map is a
bijection onto its indicated output hyperplane. The actual first bits
are 0,1,1. Their successive sets of sums are

```text
{0,1,2,3,4} -> {0,4} -> {1,2} -> {1}.
```

Every indicated hyperplane is full, so the image sizes are exactly
15625,6250,6250,3125. On z in {1,4}, the next sum is 4 when theta=0
and 1 when theta=1. Induction gives, for every n>=3,

```text
I_n={x:sum x=4-3 theta_(n-1)},     |I_n|=5^5.
```

The selected letter is therefore common to all states in I_n. Its table
is (theta_(n-1),theta_n): 00->G_4, 01->G_1, 10->G_1, 11->G_3.

Let P exchange a with c and b with d, fixing q,r. The linear part of
G_1 is -P; those of G_3 and G_4 are -I. For any two actual trajectories
compared at common counters m,n with n>=m>=3, write Delta_j=x_j-y_j.
The affine offsets cancel at each step. Since P^2=I,

```text
Delta_n = (-1)^(n-m) P^k Delta_m,
k = theta_(n-1) xor theta_(m-1).
```

Indeed G_1 occurs exactly when successive theta bits differ, so the
parity of its number of occurrences telescopes to the displayed xor.
This is an all-future identity, not an extrapolation from finite clocks.

Several distinct consequences follow.

1. The four fixed blocks {a,c}, {b,d}, {q}, {r} are invariant under P.
   If one complete block is payload-independent at m, it remains so.
   A union of these blocks cannot newly acquire a payload from another.
2. A smaller raw target can acquire an old difference from its paired
   coordinates. Equal a at m says nothing about c; a later G_1 can move
   a difference from c into a. Thus equality of an arbitrary target at
   one time is not a universal no-acquisition theorem.
3. The number of nonzero coordinates of every pairwise difference is
   preserved. More generally, over any prepared message family, the
   equality partition of messages seen by each coordinate is merely
   permuted by P. Signs and common affine offsets do not change that
   partition. The update cannot generate additional informative raw
   coordinates in this tail, though it can move existing ones.
4. Redundant initial encoding must be counted honestly. If a memory
   already contains two copies of a distinction, one can be transported
   while the other remains. The preceding invariant is not a universal
   no-copy theorem for arbitrary encoded subsystems or nonlinear readers.

The layers I_n are constrained hyperplanes, not Cartesian products of
the four blocks. None of these conclusions replaces the reachable set
by a product or permits an off-layer single-coordinate intervention.
The comparison concerns two actual reachable states at the same counter.

### 4.1 A positive tail witness with pre-existing redundancy

Retention and later transport can occur together. For lambda in {0,1},
the origin-zero preparations

```text
h_lambda(0)=(3,4,4-lambda,lambda,0,4)
```

follow the common actual G_0,G_2,G_4 prefix:

```text
h_lambda(1)=(4,3,lambda,4-lambda,0,4),
h_lambda(2)=(2-lambda,1+lambda,3,4,1,1),
h_lambda(3)=(lambda,-lambda,0,0,1,0).
```

Their sums are 0,0,2,1. At n=3 the actual next generator is G_1, giving

```text
h_lambda(4)=(0,0,-lambda,lambda,4,0).
```

Take the fixed memory M={a,b,c}, the disjoint target T={d}, and the
fixed memory-only reader D_M=(a+c)^2 in F5. At n=3, D_M=lambda and
the complete target is the common value zero. Every selected tail
generator negates a+c, so D_M=lambda for every n>=3. At n=4 the target
is lambda while the same memory reader still returns lambda.

This is an exact common-family witness for retention plus later target
distinguishability. It rules out an overbroad claim that these two
properties cannot coexist in the synchronized carrier. The interface
does not include a BLANK mark: the payload was already encoded in M at
preparation, and d itself carried lambda at n=0. Two informative raw
coordinates at n=3 become two informative raw coordinates at n=4;
one moves and one remains. No extra copy is created. The target can
later lose the distinction again, while the memory reading persists.

It is therefore not source-to-independent-blank-memory acquisition, not
a permanently updated target archive, and not arrival of another
independently selectable message. These qualifications are part of the
positive result, not consequences omitted from its statement.

## 5. Permanent completion after synchronization: the exact obstruction

The already accepted `U-NATIVE-INVARIANT-AND-NOWRITE` supplies a stronger
premise than the relative identity. On X14 define

```text
V(x)=(a+c,b+d,chi(z)(a-c-2),chi(z)(b-d-1)),
chi(1)=1, chi(4)=-1;       R(x)={V(x),-V(x)}.
```

That theorem proves the invariant R and proves that every actual
synchronized trajectory visits every checkpoint of its R fibre
arbitrarily late. A nonzero fibre has 20 checkpoints; the zero fibre
has 10. The recurrence premise is taken from its pinned mathematical
proof, not inferred from a finite visit count here.

Let D(x) be any fixed total checkpoint reader, possibly nonlinear or a
reader of only some coordinates. Suppose D(x_n)=v for every n>=T on
one origin-zero trajectory. Every earlier synchronized x_m, m>=3, is
visited again at an index beyond T. Therefore D(x_m)=v as well.

**Consequently, a new permanent completion value cannot first appear
after counter 3 under a fixed checkpoint reader of this single native
trajectory.** The same statement applies separately to each member of
a prepared family. It is impossible for an already synchronized BLANK
or old record to change later to a distinct permanent WRITTEN value.

The permanent witness in Section 2 completes at the synchronization
boundary and is consistent with this statement. The event in Section 3
does not give permanent completion in both branches. Repeated readback
of an existing record and finite retention intervals remain possible.

For a reusable archival receiver, requiring a second newly acquired
record after synchronization and then permanently retaining the final
archive under one fixed checkpoint reader is therefore an excluded
contract for this one unchanged native carrier. This is a precise
contractual boundary, not a prohibition of every possible memory or
self-relation. Counter-dependent reading, a history buffer, a larger
coupled carrier, a new input port, and altered dynamics are different
architectures. They must be stated and justified separately.

## 6. A separate capacity bound for arbitrary retained histories

Fix one common counter n>=3. Suppose every word w of length K over an
alphabet of size s has an admitted origin-zero preparation whose current
checkpoint x_w(n) is read back as that complete word. Correct readback
forces w->x_w(n) to be injective. Section 4 gives

```text
s^K <= |I_n| = 3125.
```

Thus K<=5 for five-letter words and K<=11 for binary words. Access to
the same known counter does not increase the number of checkpoints
available at that fixed reading boundary. This is a necessary bound,
not a construction achieving it. It does not infer any probability law.

The claim does not concern long correlated sequences, repeated outputs
of one retained message, an external record of past outputs, extra
cells, or message-dependent timing used as another code. In particular,
five initially selectable messages cannot become twenty-five independently
selectable message pairs merely by waiting. A source of new independent
messages must be part of the carrier and update, or an explicit input
resource. Deterministic continuation of a fixed preparation does not
itself supply that resource.

## 7. What is joined and what is still not constructed

Sections 2 and 3 prove compatible existence statements about the same U.
They do not furnish a shared device: the preparations, raw partitions,
payload alphabets, phase references, selector histories and readers differ.
There is no demonstrated native handoff between their interfaces.
Section 4.1 does join retention and later target distinguishability on
one family, using explicit pre-existing redundancy. It does not add the
missing blank-memory acquisition or repeated independent arrival.

Sections 4--6 give the common boundary. A tail difference can move inside
a paired block, but no new distinction spreads between the four invariant
blocks. A fixed checkpoint reader cannot first acquire a permanent value
in the synchronized tail. Arbitrary complete histories also face a
finite current-state capacity bound.

The worthwhile next construction must therefore state which obligation
it changes: finite rather than permanent retention, a declared larger
coupled carrier, a history-bearing record, or a counter-aware interface.
Merely relabeling a new target decoder is not a physical write operation.
The fixed common interface is specified in CONTRACT.md. None of these
mathematical statements defines selfhood or shows consciousness.

Copyright 2026 A. M. Thorn. Apache-2.0, under the repository license.
