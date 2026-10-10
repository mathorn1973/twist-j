# Finite reversible control over a recurrent clock: the one-shot boundary

**PUBLIC, NON-CANONICAL. Issue-reserved, unexecuted symbolic draft. L1 only.**
Draft date: 2026-10-10. Original text: Apache-2.0.
Incubation reservation: [issue #1440][reservation].
Branch: `codex/v101-controller-admission`.
Public source base: `c17fe88ddd3b95ab8ff76ac7923a37f582c97571`.

This note supplies a proposed proof and an applicability contract. It is not
a formal probe preregistration, immutable execution pin, physical admission,
or Canon promotion. Its public issue reserves notes-only incubation. The
proposed conclusion was derived before any new verifier. No scientific
program was run or imported for this note.

The question is whether the occupied-SUM construction's one-time trigger can
be replaced by a finite reversible controller which reads only a fixed legal
Thue-Morse window, without access to the absolute counter. The answer in the
class defined below is negative once that recurrent interface is active:
every complete state lies in a minimal subsystem, every observed finite
event recurs, and a fixed readout cannot become permanently different from
an earlier readout in that regime. Arbitrary finite persistent memory and
feedback are allowed, provided the assembled step is a permutation of one
common finite carrier for every admitted clock context.

This is an application of standard finite group-extension mathematics, not
a claim of a new general theorem in topological dynamics. A related general
distal-extension fact is used in M. G. Nerurkar, *Ergodic continuous skew
product actions of amenable groups*, Pacific Journal of Mathematics 119(2)
(1985), 343-363, p. 361, proof of Corollary 2.4. The finite argument required
here is proved directly in section 3 and does not depend on that paper's
genericity or measure-theoretic hypotheses. [Nerurkar source][nerurkar]

## 1. Existing results and the exact additional question

The repository references in this section use public source commit
`c17fe88ddd3b95ab8ff76ac7923a37f582c97571`. Line numbers identify that tree.

1. The complete native state includes `n in N0`; the checkpoint alone is not
   autonomous. See `canon/CANON.md:453-468`. A finite autonomous replacement
   cannot reproduce the complete native checkpoint trajectory even if its
   transition is not reversible: its output would be eventually periodic,
   whereas the actual trace encodes the non-eventually-periodic clock.
   This is already `KERNEL-Z6-SYNCHRONIZATION`,
   `canon/CANON.md:10768-10792`, registry row 298. [Native clock][native-clock]
   [Finite-realization obstruction][finite-realization]
2. A closed finite permutation and any fixed event label give a periodic
   accepted stream. This is already part of
   `RECORD-OCCURRENCE-SELECTION-CRITERIA`, `canon/CANON.md:6084-6095`.
   It immediately excludes a unique event followed by silence forever in
   that closed finite class. It does not make native U a finite machine.
   [Finite permutation cycles][finite-cycles]
3. A fixed finite native/clock window has bounded-gap recurrence and cannot
   change permanently from one synchronized readout to another. These are
   `U-FINITE-HISTORY-CLOCK-PHASE`, `canon/CANON.md:1146-1181`, and
   `probes/P-U-FINITE-HISTORY-EVENT-1/MEMORY-PROOF.md:76-124`.
   `probes/P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md:98-120` explicitly
   excludes a finite nonzero number of accepted synchronized events.
   [Window boundary][window-boundary] [Event recurrence][event-recurrence]
4. That earlier class explicitly excludes separate persistent memory and
   feedback: `P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md:22-41` and
   `P-U-FINITE-HISTORY-EVENT-1/MEMORY-PROOF.md:117-124`. It therefore cannot
   simply be cited as a theorem about every added finite reversible
   controller. That is the additional class treated here.
   [Earlier class restriction][reader-restriction]
5. A small decoding summary is not automatically an autonomous clock.
   The already recorded collision
   `T_4^read=T_6^read=(-1,4,0)` has different successors `T_5^read` and
   `T_7^read`; see `canon/CANON.md:5365-5389`. Reusing that summary does
   not supply the missing trigger. [Summary collision][summary-collision]
6. The finite internally controlled device in
   `notes/C-FIELD-J-INTERNAL-CONTROL-N/PROOF.md:359-382` explicitly gives
   a finite read window followed by an inverse program and return. It does
   not claim an absorbing halt or permanent changed record under its whole
   continued dynamics. The present conclusion does not contradict that
   non-canonical construction. [Finite read window][finite-read-window]

This local source review found no existing Canon statement proving the
finite persistent reversible-controller extension below. The separate
reservation receipt records the public issue/remote-branch collision audit;
the source comparison here identifies the mathematical overlaps. Section 7
also records a known public transient-contact result which must not be
erased by an overbroad version of the proposed obstruction.

## 2. Frozen mathematical class

Let `K` be a nonempty compact subshift on a finite alphabet, with the
two-sided shift `S`, and assume `K` is minimal: every orbit is dense in K.
The intended base is the two-sided Thue-Morse subshift `K_TM`.

Fix a finite length `L>=1` and the causal legal-window map

```text
a(kappa) = (kappa_(-L+1), ..., kappa_0).
```

Let `A` be its finite image. A shorter selector interface is allowed as a
fixed function of this window and of the finite apparatus state below.
The length, interface and update law are fixed for the entire run.

Let `B` be one nonempty finite set containing the **whole** non-clock state:
receiver, source registers, controller, counters, phases, work registers,
stored flags and any retained finite history. Each legal clock context
`a in A` specifies one map

```text
P_a : B -> B,             P_a in Sym(B).                 (1)
```

This is all-state bijectivity on the same B, not merely an inverse on the
prepared orbit or a succession of time-indexed reachable subsets. The full
mathematical evolution is the skew product

```text
F(kappa,b) = (S kappa, P_(a(kappa))(b)).                  (2)
```

The base is not changed by the apparatus. Equation (2) describes a finite
apparatus driven by a supplied clock stream; the complete carrier K x B is
infinite. It is not a construction of the physical clock or a closed finite
realization of Thue-Morse.

Feedback is included in (1). For example, the selected command may depend
on every component of b, including receiver and source. Once this selection
and the controller update have been composed, their complete map at context
a must be the single permutation P_a. There is no requirement that the
controller move independently of the receiver. There is also no restriction
to affine maps or to the previously classified contact coefficients.

Individual command permutations do not imply (1). On B={0,1}, choosing the
identity at input 0 and the transposition at input 1 maps both inputs to 0.
All-state bijectivity of the assembled feedback map is a substantive premise.

A permitted readout is a fixed finite-valued locally constant function

```text
r : K x B -> Y,                 |Y| finite.             (3)
```

In particular r may inspect b and any other fixed finite causal clock
window. An event flag `e:K x B->{0,1}` has the same restriction. A label on
a transition is covered whenever it is a fixed function of finite current
clock context, b and its successor: composing with (2) makes it locally
constant on the current complete state. No absolute time, changing window,
external first-hit operation or time-dependent decoding convention is
included. A permanent message already in the initial state is allowed.

## 3. Every point of a finite permutation extension is recurrent

### Lemma 1: every point lies in a minimal subsystem

Let K, B and F satisfy section 2. Then every point of K x B belongs to a
compact F-invariant minimal subset. The entire product need not be minimal;
distinct invariant components and distinct source values may remain apart.

**Proof.** Write `G=Sym(B)`, acting on B on the left, and abbreviate
`P(kappa)=P_(a(kappa))`. It is continuous because a is a finite-window
function and G is finite. Consider the auxiliary system

```text
F_tilde(kappa,g) = (S kappa, P(kappa) g),    on K x G.   (4)
```

This auxiliary group is a proof device, not additional apparatus storage.
Both (2) and (4) are homeomorphisms. For example,

```text
F_tilde^(-1)(kappa,g)
    = (S^(-1) kappa, P(S^(-1) kappa)^(-1) g).           (5)
```

Compactness supplies a nonempty compact minimal invariant subset M of
K x G. One may obtain it by taking a minimal member of the nonempty compact
forward-invariant subsets: every descending chain has a nonempty compact
intersection, and minimality then gives `F_tilde(M)=M`.

The projection of M to K is a nonempty compact S-invariant subset. Base
minimality makes this projection all of K. Thus, for every kappa and every
desired g, there is h in G with `(kappa,h) in M`.

For fixed u in G the right translation

```text
R_u(kappa,h) = (kappa,h u)
```

commutes with (4), because `P(kappa)(h u)=(P(kappa)h)u`. Consequently
`R_u M` is again a compact minimal invariant subset. Taking `u=h^(-1)g`
puts `(kappa,g)` in `R_u M`. Every point of K x G therefore lies in a
minimal subsystem. No commutativity of G is assumed.

Fix `b_* in B`. The map

```text
pi(kappa,g) = (kappa,g(b_*))                            (6)
```

is continuous, onto, and intertwines (4) with (2). The image of a compact
minimal system under such a factor map is minimal: the dense orbit of any
preimage maps to a dense orbit in the image. Every `(kappa,b)` has a
preimage under (6), so it belongs to the image of a minimal subsystem.
This proves the lemma. QED.

### Lemma 2: return times have bounded gaps within each such orbit

If y belongs to a compact minimal system M and U is a nonempty relatively
open subset of M, there is a finite J such that every forward interval
`[m,m+J]`, m>=0, contains a visit of the orbit of y to U.

**Proof.** Every forward orbit in a compact minimal homeomorphism is dense.
For completeness, the omega-limit set of any point is nonempty, compact
and invariant and hence is all of M; its forward orbit is therefore dense.
The open sets `F^(-j)U`, j>=0, cover M. A finite subcover has maximum
index J. Apply this cover to `F^m y`: some j<=J satisfies
`F^(m+j)y in U`. QED.

The bound may depend on the specified maps, component, event and window.
No numerical bound uniform over all finite controller sizes or all
interfaces is claimed, and no quantitative optimization follows here.

### Theorem: no isolated event and no newly permanent finite readout

For every initial `(kappa,b)` in the class (1)-(3):

1. Every finite-valued readout value which occurs once occurs infinitely
   often, with bounded gaps along that orbit.
2. A fixed event flag is either always zero or is one infinitely often
   with bounded gaps. In particular it cannot mark exactly one step, or
   any finite nonzero number of steps, in this regime.
3. If `r(F^n(kappa,b))=v` for every n>=n0, then the same equality holds
   for every n>=0 in this regime.

**Proof.** By Lemma 1 the point lies in some minimal M. If value w occurs,
the set `M intersect r^(-1)({w})` is nonempty and relatively open, because
r is locally constant with finite range. Apply Lemma 2. Statement 2 is
the case of an event flag. If an earlier value w differed from an eventual
constant v, its arbitrarily late recurrence would contradict that eventual
constancy. This gives statement 3. QED.

These are individual-orbit assertions for every initial finite state, not
almost-everywhere statements. No initial ensemble, stationary measure,
frequency, ergodicity, mixing or independence assumption is used.

## 4. Why the legal Thue-Morse base is minimal

This section supplies the elementary property of the intended base rather
than treating a finite sample as evidence for it. Let

```text
mu(0)=01,  mu(1)=10,
theta = lim_(j->infinity) mu^j(0).
```

Every legal finite word w occurs in some prefix `mu^r(0)`. Both `mu(0)`
and `mu(1)` contain 0. Therefore each `mu^(r+1)(a)`, a in {0,1}, contains
that prefix and hence w. The one-sided word theta is partitioned into
aligned blocks of length `2^(r+1)` of this form. Every sufficiently long
factor contains a complete such block and therefore contains w.

Define K_TM to be the two-sided sequences whose every finite factor occurs
in theta. It is closed, shift-invariant and nonempty. Nonemptiness follows
by taking a convergent subsequence of longer and longer windows centered
far from theta's left boundary, in the compact finite-alphabet product.
The preceding bounded-gap word-containment property passes to all elements
of K_TM: a sufficiently long legal block contains w. Hence the orbit of
every element meets every nonempty cylinder, and is dense. This proves
minimality of K_TM and allows section 3 to be applied.

The origin-zero one-sided theta also has a two-sided legal extension.
Indeed its length-m prefixes occur arbitrarily far to the right; center
successive larger legal windows at such occurrences and take a diagonal
subsequence. The limit has the prescribed whole nonnegative half. Using
this extension is a mathematical way to describe an already available
finite clock context, not a grant of physical prehistory or future bits.

## 5. The native stable sheets and the common finite carrier

The raw selected native maps are not permutations on the whole union of
trace sheets. The Canon gives, for the synchronized origin-zero tail,

```text
H_z = {v in F5^6 : sum(v)=z},
z_n = 4+2 theta_(n-1) mod 5,              n>=3.         (7)
```

For `alpha=theta_(n-1)`, `beta=theta_n`, the selected letters and trace
arrows are

| alpha | beta | input trace | selected letter | output trace |
|---|---|---|---|---|
| 0 | 0 | 4 | e | 4 |
| 0 | 1 | 4 | b | 1 |
| 1 | 0 | 1 | b | 4 |
| 1 | 1 | 1 | d | 1 |

Each individual arrow is a bijection between its indicated sheets.
`canon/CANON.md:10711-10722,10752-10765` proves precisely this distinction.
For example at beta=0 both H1 and H4 map onto H4, so treating the whole
H1 union H4 as one permutation carrier would be wrong. [Sheet maps][sheet-maps]

Identify each indicated sheet with the same finite set `D=F5^5` by

```text
J_alpha(p1,p4,p1p,p4p,q)
 = (p1,p4,p1p,p4p,q,4+2 alpha-p1-p4-p1p-p4p-q).        (8)
```

Every expression after the equality is in F5. If `g_(alpha,beta)` denotes
the table's selected generator, its common-carrier form is the permutation

```text
A_(alpha,beta) = J_beta^(-1) g_(alpha,beta) J_alpha
                  : D -> D.                          (9)
```

For the occupied-SUM application include the independently stored second
source and any proposed finite controller Kc:

```text
B = D x F5 x Kc.                                      (10)
```

All source values, dirty receiver coordinates and controller states belong
to this carrier. The stored source is not an omitted input. The class under
test consists of joint context maps on (10) that satisfy (1); preservation
of the source, if required by the intended realization, is an additional
restriction and causes no problem for the theorem.

This covers a balanced contact which preserves trace and a controller
acting within each appropriate input/output sheet. It also covers arbitrary
feedback assembled into a bijection of (10). It does not infer all-state
bijectivity from correctness on the 125 prepared symbol triples. A proposal
which changes the sheet contract or is invertible only on those prepared
paths needs its own applicability proof and is not silently included.

The actual native selector is a fixed function of the trace and current
bit. On these sheets it is the finite pair-table above. Giving a controller
only the selected letter or current bit supplies no more information than
the legal finite-window class. This statement concerns information available
to the controller; it does not derive the physical observation of that bit
or letter.

## 6. Application to the occupied-SUM one-shot construction

The existing conditional construction freezes N>=4, retains one source
`s2 in F5`, applies `C_(s2)^f` at counter N and otherwise follows native U.
Its complete preparation is

```text
(0,(t,0,-t,0,-s1,s1),s2),       (t,s1,s2) in F5^3.
```

With one fixed receiver function it requires

```text
R(v_n) = t+s1       for 3<=n<=N,
R(v_n) = t+s1+s2    for every n>=N+1.                  (11)
```

The complete-state specification is stronger than (11); see
`probes/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1/PROOF.md:263-306`.
The new question does not dispute that construction with explicit n.
It asks whether a controller in (1) can reproduce its all-time behavior
while removing that counter access. [Occupied-SUM specification][sum-spec]

Assume the legal recurrent interface and the joint permutation law are
already active at some native boundary j with `3<=j<=N`, and remain active
for every subsequent step. This assumption includes availability of every
required finite clock window at j. The initial finite state at j is
arbitrary; it may contain any prepared controller value and memory.

The reader in common coordinates is

```text
r(kappa,(d,s2,k)) = R(J_(kappa_-1)(d)).                 (12)
```

It is a fixed locally constant finite-valued function. Choose any admitted
nonzero s2. Equation (11) gives the earlier value `t+s1` at j and the
different eventual constant `t+s1+s2`. Section 3 excludes this. Therefore
no such finite reversible controller can realize the all-time occupied-SUM
specification within that continuously active recurrent regime. This is
already a contradiction for one nonzero-source preparation; a realization
promised on all 125 preparations necessarily includes it.

If the implementation exposes a fixed firing flag, the event conclusion
also independently forbids its firing at exactly N. The readout argument
does not require an exposed flag and continues to apply if the proposed
joint step hides its control decision internally.

For an interface using only current Thue-Morse bits, previous/current bits,
or the synchronized selector, the required legal context is available by
the first occupied-SUM boundary n=3. Subject to (1) and the sheet contract,
this gives the obstruction for every fixed N>=4.

For an arbitrary length-L acquisition interface, **N>=4 alone is not
sufficient** to invoke the result: the legal interface might not yet have
been acquired by N. The exact hypothesis is the existence of an earlier
first-record boundary j as above at which the recurrent class is already
active. No claim is made about a contact completed entirely during a
nonrecurrent acquisition transient.

## 7. Sharp exclusions and already known counterexamples to overclaims

### 7.1 The native synchronization transient is outside the class

Public incubation [C-U-NATIVE-CONTACT-TRANSIENT-N, issue #992][transient]
already reports a one-shot native commit on the first actual consecutive
11, starting from an unsynchronized state

```text
I_s=(0,0,0,0,-s,s),
C_s=(2,1+s,2,1-s,1+s,-s),
O_s=(0,-s,1,3+s,1-s,1+s),

T_0 I_s=I_s,  T_1 I_s=C_s,
T_0 C_s=I_s,  T_1 C_s=O_s.
```

Here T_beta is the complete state-selected native map, not one uniformly
chosen generator. Entry into the absorbing stable union supplies the unique
commit edge, and the record is permanent after entry. The public completed
incubation describes this result and its nonrenewability; it is not assigned
Canonical status by this note. [Recorded result and proof custody][transient-result]

There is an explicit failure of (1): I_s and C_s have different traces 0
and 2, but both map to I_s under T_0. Thus the full transient state-selected
map is not injective. The fact that each of its five constituent letters is
an involution does not repair that merger. This result is a counterexample
to any claim excluding all native one-shot writes, and is fully compatible
with the present theorem about recurrent, jointly bijective operation.

### 7.2 Acquisition and external origin markers must be charged

An empty buffer returning UNAVAILABLE is not a legal Thue-Morse word.
Switching once from that tag to legal windows supplies a nonrecurrent
interface transition. It cannot be included in K_TM merely by calling it
a clock read. The Canon explicitly distinguishes filling from fully
synchronized reading (`canon/CANON.md:1152-1154,1175-1181`).

A finite internally stored ready flag is included if the complete update
is bijective; section 3 then applies. A shift register that drops its oldest
symbol at each externally supplied bit is not automatically a permutation
on its complete finite raw state. Discarded history, an external once-only
start signal, erasure, or initialization of an additional later input must
not disappear from the full state/interface contract.

One must also distinguish the recurrent regime from a supplied finite
prefix containing special symbols. The theorem is applicable from the
start of that recurrent regime onward. It does not exclude a unique event
which happens earlier in the special prefix.

### 7.3 Time-layer inverses do not imply a global permutation

The finite rule `h -> min(h+1,N+1)` on {0,...,N+1}, initialized at h=0,
visits h=N exactly once and then remains at h=N+1. A flag `[h=N]` is a
one-shot scheduler. It violates (1): h=N and h=N+1 have the same image.
Each reached singleton layer nonetheless maps bijectively to its next
singleton layer. Thus an inverse defined separately with the actual time
label is insufficient for the present all-state premise.

Coupling the trigger to an invertible receiver contact does not repair
this raw collision. At one fixed context, if H is the native bijection and
C_s is the contact, inputs `(v,N)` and `(C_s v,N+1)` both produce
`(H C_s v,N+1)` with the same stored source. This argument concerns the
assembled map and retains the receiver coordinates.

### 7.4 Finite horizons and repeated operations remain possible

For the actual occupied-SUM state at native n=3, initialize a controller
`k in Z/P` at zero, with `P>N-3`. On the corresponding stable sheets use
one fixed previously declared unit-gain contact `C_s=C_s^f` and write
`G_(alpha,beta)=g_(alpha,beta)` for section 5's actual native arrow:

```text
(v,k,s) -> (G_(alpha,beta) C_s^[k=N-3](v), k+1 mod P, s).
```

After the sheet identification (8), this is a permutation on the common
finite carrier. Its inverse first recovers k, then undoes the known native
arrow and the indicated contact, retaining s. The contact occurs exactly
at native steps `N+jP`, j>=0. Covariance with the native stable arrows and
source additivity give the complete receiver and readout formulas

```text
w_n = #{j>=0 : N+jP<n},
v_n = C_(w_n*s2)^f(v_n^free),
R(v_n) = t+s1+w_n*s2,                  n>=3,           (13)
```

where the scalar argument is reduced modulo five. Thus for any prescribed
finite horizon H>=N+1, choosing `P>H-3` retains the second sum at every
boundary N+1 through H. After wraparound the contact repeats. No minimal
controller size is asserted, and the contact and clock interface remain
adopted premises. This is not an all-time one-shot implementation. It shows
why this theorem gives neither a universal finite experimental deadline on
recurrence nor a no-go for arbitrarily long finite retention with additional
finite resources.

Repeated refresh, cyclic contacts, finite read windows and invariant records
already encoded at preparation are not ruled out. Whether any such protocol
is physically available is a separate question.

## 8. Conservative disposition

The proposed mathematical result closes the following restricted question:
once the supplied legal recurrent clock interface is active, arbitrary
finite persistent memory with all-state reversible feedback cannot give an
isolated contact pulse or a newly permanent different fixed readout. For the
occupied-SUM target it excludes replacing the fixed-N scheduler by such a
controller when a first-record boundary remains inside that recurrent
regime before the contact.

The proof does not select a physical controller class. It does not imply
that absolute n is the uniquely necessary resource, that a new fundamental
axiom is necessary, or that every clockless implementation is impossible.
Nonbijective synchronization, a nonrecurrent input prefix, unbounded state,
fresh inputs, a modified clock law, discontinuous/infinite-history access,
or finite-horizon specifications change the mathematical premises.

Even in the admitted mathematical class, the Thue-Morse drive and the
ability to read its finite context remain supplied resources. Source
preparation and retention, source/receiver coupling, physical tick duration,
energy/work, spatial contact, event occurrence and physical readout are not
derived. No statistical or L2-L6 conclusion follows from this recurrence
argument. The issue reservation does not constitute a formal execution pin
or public Canon intake. Review and custody records are separate from this
proof; no scientific execution or normative promotion is represented as
completed by this unexecuted draft.

[reservation]: https://github.com/mathorn1973/twist-j/issues/1440
[nerurkar]: https://msp.org/pjm/1985/119-2/pjm-v119-n2-p07-s.pdf#page=20
[native-clock]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L453
[finite-realization]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L10768
[finite-cycles]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L6084
[window-boundary]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L1146
[event-recurrence]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/probes/P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md#L98
[reader-restriction]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/probes/P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md#L22
[summary-collision]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L5365
[finite-read-window]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/notes/C-FIELD-J-INTERNAL-CONTROL-N/PROOF.md#L359
[sheet-maps]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/canon/CANON.md#L10752
[sum-spec]: https://github.com/mathorn1973/twist-j/blob/c17fe88ddd3b95ab8ff76ac7923a37f582c97571/probes/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1/PROOF.md#L263
[transient]: https://github.com/mathorn1973/twist-j/issues/992
[transient-result]: https://github.com/mathorn1973/twist-j/issues/992#issuecomment-5655270719
