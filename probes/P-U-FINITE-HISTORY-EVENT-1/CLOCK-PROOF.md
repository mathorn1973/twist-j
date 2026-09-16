# P-U-FINITE-HISTORY-EVENT-1: causal clock windows and exact frequencies

**Prospective, result-exposed, proof-first, L1 only.** Issue #864.
The analytical predictions are disclosed before this probe's formal execution;
the new accepted verifier has not been executed or imported before its pin.
The preregistration and accepted verifier must be committed and publicly pushed
before that execution. A finite audit is not the proof of any all-time or
all-window claim below. Public authority remains the declared Canon; this
document proposes mathematical results for review and a possible later fold.

The carrier in Sections 1--7 is the fixed-origin Thue--Morse word alone.
Section 8 transports a clock reader to native phase history. Nothing here
classifies the complete frequency spectrum of readers that also inspect
other checkpoint coordinates. No physical event, apparatus, memory carrier,
context key, occurrence measure, or layer lift is adopted.

## 1. Objects and the complete clock-window reader class

For `n>=0` define

    theta_n = popcount(n) mod 2,
    mu(0) = 01,                  mu(1) = 10.

Thus

    theta_(2m) = theta_m,        theta_(2m+1) = 1-theta_m,

and `theta` is the one-sided fixed word of `mu` beginning with zero. A
length-`L` causal clock window at endpoint `n>=L-1` is

    w_L(n) = (theta_(n-L+1), ..., theta_n),

always ordered oldest to newest. Let `W_L` be the set of these legal length-`L`
words. A fixed clock-window reader is any function `f:W_L -> A`, where `L`
is any fixed positive finite integer and `A` is a finite alphabet. The
accepted interface rejects complete words outside `W_L`; it does not assign
them scientific outputs. The class contains every function on `W_L`, with
no linearity or circuit restriction. The endpoint `n`,
its residue, future bits, a growing window, and separately evolving reader
state are not input arguments.

For unconditional LOW density take `A={LOW,HIGH}`, or designate one output
symbol as LOW in a larger finite alphabet. For accepted-event ratios take
`A={LOW,HIGH,SILENT}` and normalize the LOW count by the LOW-plus-HIGH count.
Zero acceptance is tagged `UNDEFINED`. The union spectra below range over
all fixed finite window lengths; they are not assertions that every member
of the union is attainable at one fixed length.

## 2. Local parity is visible in five past bits

There is no `000` or `111` factor. Every interval of three consecutive
indices contains a pair `(2j,2j+1)`, and the two bits of such a pair are
complementary by the recurrence.

There is also no alternating factor of length five. Indeed any such interval
contains both odd-start pairs at `2j+1` and `2j+3` for an appropriate `j`.
The first pair is `(1-theta_j,theta_(j+1))`, and the second is
`(1-theta_(j+1),theta_(j+2))`. Alternation of these pairs would require

    theta_j = theta_(j+1) = theta_(j+2),

contradicting the preceding no-triple statement. Consequently every
five-letter factor contains an adjacent equal pair. Such a pair must begin
at an odd index, since every even-start pair is complementary.

Let the last five bits at endpoint `n` be indexed locally by `0,...,4`, and
let `i in {0,1,2,3}` be any start position of an equal pair. Its actual start
index is `n-4+i`, which is odd. Therefore

    n mod 2 = (1+i) mod 2.

Every equal pair in that five-letter window gives the same answer. Selecting
the first equal pair is a deterministic implementation convention and adds
no clock input.

## 3. Causal reconstruction of every fixed dyadic phase

Set `L_0=1`, with `R_0` the constant zero map, and for `k>=1` set

    L_k = 5*2^(k-1).

We define a fixed function `R_k` on occurring words of length `L_k` and prove

    R_k(w_(L_k)(n)) = n mod 2^k          for every n>=L_k-1.

For `k=1`, use Section 2. For `k>=2`, put `H=L_(k-1)`, so `L_k=2H`.
Given an occurring word `W` of length `L_k`, use its last five bits to obtain
the endpoint parity `e`. Form the length-`H` parent word in chronological
order by taking indices

    L_k-1-e-2j,             j=H-1,H-2,...,0,

and call it `P(W)`. All indices lie in the available word: the earliest is
`1-e>=0` and the latest is `L_k-1-e<=L_k-1`. These are precisely the bits
at actual indices

    n-e-2j = 2*(floor(n/2)-j).

By the Thue--Morse recurrence,

    P(W) = w_H(floor(n/2)).

The induction hypothesis applies because `n>=2H-1` implies
`floor(n/2)>=H-1`. Define

    R_k(W) = e + 2*R_(k-1)(P(W)).

This is `n mod 2^k`, completing the induction. A longer legal supplied history
can use its last `L_k` bits. Complete input words outside the legal domain
are rejected before scientific evaluation. The decimated internal words are
legal by the displayed parent-word identity, so no extension to illegal
words is a premise of the construction.

For `k=8`, the formula gives `L_8=640`. Thus 640 past and present driver bits
suffice to recover phase modulo 256. This is a proved sufficient length,
**not a minimality claim**. The history is an explicitly enlarged read
domain; this construction does not assert that a physical history buffer
already exists inside the instantaneous checkpoint.

## 4. Pair and triple frequencies along every prefix length

We first give a self-contained proof of the frequencies needed below. Let

    q_m = (theta_m,theta_(m+1)),
    A0(u,v) = (u,1-u),           A1(u,v) = (1-u,v).

Then `q_(2m)=A0(q_m)`, `q_(2m+1)=A1(q_m)`, and `q_0=01` is fixed by `A0`.
The four pair states have the following two successors:

| State | `A0` | `A1` |
| --- | --- | --- |
| `00` | `01` | `10` |
| `01` | `01` | `11` |
| `10` | `10` | `00` |
| `11` | `10` | `01` |

Let `B` be the integer adjacency matrix, counting both labelled transitions,
and `P=B/2`. From every state there is a path to `01` of length at most two;
from `01` every state is reached in at most three. The loop at `01` pads any
combined path to length five. Hence every entry of `B^5` is at least one.

In state order `00,01,10,11`, the row vector

    pi = (1,2,2,1)/6

satisfies `pi P=pi`, as direct incoming-weight addition in the table shows.
For all-length convergence, let `J` have every row equal to the uniform
probability vector on the four states. Since each entry of `P^5` is at least
`1/32`, there is a row-stochastic nonnegative matrix `Q` with

    P^5 = (1/8) J + (7/8) Q.

A zero-sum signed row vector is annihilated by `J`, and multiplication by a
stochastic matrix cannot increase its `l1` norm. It follows that, for every
state `a` and every `j>=0`,

    || e_a P^j - pi ||_1 <= 2*(7/8)^floor(j/5).

The pair substitution `a -> A0(a) A1(a)` produces exactly the pair word.
Its aligned block at indices `t*2^j,...,(t+1)*2^j-1` is the `j`th substituted
image of `q_t`. Thus the last inequality bounds its normalized pair-count
vector uniformly in the starting position.

Partition a prefix of length `N` into complete aligned blocks of length
`2^j` and one remainder of length less than `2^j`. If `F_N` is the normalized
pair-count vector, then

    || F_N-pi ||_1
      <= 2*(7/8)^floor(j/5) + 2^(j+1)/N.

For example `j=floor(log2(N)/2)` proves convergence along **every integer
prefix length**, not merely powers of two. Adding or deleting finitely many
initial terms has no effect. The same block argument with two partial
boundary blocks gives uniform interval convergence if needed.

The triples beginning at even and odd indices are respectively

    (theta_m,1-theta_m,theta_(m+1)),
    (1-theta_m,theta_(m+1),1-theta_(m+1)).

Their complete table is:

| Parent pair | Even-start triple | Odd-start triple | Parent pair frequency |
| --- | --- | --- | --- |
| `00` | `010` | `101` | `1/6` |
| `01` | `011` | `110` | `1/3` |
| `10` | `100` | `001` | `1/3` |
| `11` | `101` | `010` | `1/6` |

Each index parity has density one half. The table and the proved pair limits
therefore give exactly the six triples

    001, 010, 011, 100, 101, 110,

each with frequency `1/6`, along every prefix length. There are no other
triples, by the no-constant-triple result. The normalization by number of
eligible window endpoints rather than total ticks has the same limit,
because those counts differ by a fixed finite number.

## 5. Exact factor frequencies for every fixed length

Fix any positive length `L`. Choose `k>=0` with `M=2^k>=L`. The aligned
block of length `M` starting at `Mm` is `mu^k(theta_m)`. For a forward
length-`L` factor starting at `n=Mm+r`, `0<=r<M`, the factor is exactly

    mu^k(theta_m theta_(m+1))[r:r+L],

where slicing includes its left endpoint and excludes its right endpoint.
It fits inside those two substituted letters because `r+L<=2M`.

For each fixed residue `r`, parent indices `m` in a prefix form an ordinary
initial interval, whose pair counts have the all-length limits proved in
Section 4. The number of such indices divided by the original prefix length
tends to `1/M`. Summing over the finitely many residues proves that every
word `w` of length `L` has the exact limiting frequency

    freq_L(w) = 1/(6M) * sum_(r=0)^(M-1) sum_(ab in {00,01,10,11})
                            h(ab) * 1_[mu^k(ab)[r:r+L] = w],

where `h(00)=h(11)=1` and `h(01)=h(10)=2`. This is an all-prefix limit
formula, not a finite sample estimate. The same formula applies to causal
windows by translating their start index to their endpoint; the discarded
initial boundary is finite. Every occurring word has positive frequency,
since an actual occurrence supplies at least one positive summand. Conversely
a positive summand uses a parent pair of positive frequency and therefore
produces actual occurrences. Thus the formula also gives the complete
length-`L` language.

In particular every factor frequency is an integer multiple of `1/(6M)`.
Any fixed output frequency is a finite sum of such values. Every accepted
ratio with nonempty acceptance is rational, because both of its limiting
counts are sums of these rational atom weights and the denominator is
positive. There is no nonempty zero-density acceptance set in this class.

## 6. Uniform classes recognized from a causal window of length 3M

For any `k>=0`, put `M=2^k` and consider the available word `w_(3M)(n)` at
`n>=3M-1`. For `k=0` set `r=0`. For `k>=1`, Section 3 recovers
`r=n mod M` from its last `L_k=5M/2` bits, which fit because `5M/2<=3M`.
Write `n=Mm+r`.

At offsets `r+2M`, `r+M`, and `r` backwards from the endpoint, the observed
bits are

    theta_(M(m-2)), theta_(M(m-1)), theta_(Mm)
      = theta_(m-2), theta_(m-1), theta_m.

All three positions are available, since `r+2M<=3M-1`, and `m>=2` follows
from `n>=3M-1`. These bits form a permitted parent triple `t`. Therefore

    C_k(W) = (r,t)

is a fixed, causal, well-defined function of the length-`3M` word. With word
indices beginning at zero, its three selected indices are exactly

    3M-1-r-2M,   3M-1-r-M,   3M-1-r.

For each residue `r`, endpoints run through `Mm+r`; their parent indices
run through consecutive integers. Each parent triple has frequency `1/6`
by Section 4, while that endpoint residue contributes the factor `1/M`.
Consequently all `6M` values `(r,t)` occur and each has frequency

    1/(6M).

These are classes of possibly several length-`3M` factors, not an assertion
that there are exactly `6M` distinct raw binary factors. Distinct class
values are disjoint because `C_k` is a function of the observed window.
This distinction makes whole-class assignments to a reader legitimate.

## 7. Complete union spectra and constructive accepted ratios

Define

    D = ((1/3)*Z[1/2]) intersect [0,1]
      = {j/(3*2^k): k>=0, 0<=j<=3*2^k}.

The notation allows at most one factor of three in a reduced denominator;
it is not the larger localization allowing all powers of three. Section 5
shows that every unconditional clock-window output density belongs to `D`.
Conversely, Section 6 permits assigning LOW to any chosen number of the
`6M` equal classes and HIGH to all others. This realizes every `j/(6M)`.
Their union over `M=2^k` is exactly `D`, including the fractions with
denominator three. Hence `D` is the complete unconditional union spectrum.

Section 5 already proves that every defined accepted ratio belongs to
`Q intersect [0,1]`. For the converse, fix integers `0<=a<=b`, `b>=1`, and
choose any `k>=0` for which `M=2^k>=b`. Read the recovered phase
`r=R_k(W)` and apply the one fixed rule

    LOW     if 0<=r<a,
    HIGH    if a<=r<b,
    SILENT  if b<=r<M.

For `k=0`, the constant phase suffices. For `k>=1`, the rule uses only the
last `L_k` bits; it does not receive `n` as a separate argument. Each phase
has density `1/M`, so LOW, HIGH, and acceptance have densities respectively

    a/M,              (b-a)/M,              b/M>0.

The accepted LOW ratio is precisely `a/b`. For the ideal phase sequence at
indices `0,...,N-1`, writing `N=qM+s`, `0<=s<M`, gives the exact counts

    LOW(N)        = q*a + min(s,a),
    ACCEPTED(N)   = q*b + min(s,b),
    HIGH(N)       = ACCEPTED(N)-LOW(N).

Starting only when the finite causal history is available removes a fixed
initial segment, preserving all limits. Any other finite starting index
likewise changes the residue counts by bounded boundary terms. These
formulas supply a deterministic periodic output sequence after history
availability, with a possibly silent portion of each period. They do not
assert invocation-rank accuracy under externally selected gaps.

Thus the exact accepted union spectrum is `Q intersect [0,1]`, together
with the separate tag `UNDEFINED` for empty acceptance. All assignments are
functions of whole observable words; no fraction of an atom is allocated
separately. The constructor is specified for every rational before any
comparison with a selected list of target values. An algebraic constructor
does not select its parameters as a physical context.

For example, `1/256` can be realized unconditionally by selecting one phase
modulo 256; the sufficient window length is 640. The rational `9/14` is
absent from the unconditional union spectrum because of its factor seven,
but is present in the accepted spectrum by choosing `M>=14`, nine LOW
phases and five HIGH phases. These distinguish the expanded class from the
instantaneous class without changing the latter's proved boundary.

## 8. Native phase history and the one-tick offset

On the synchronized native trajectory, the inherited phase identity is

    z_n = 4-3*theta_(n-1)       in F5, for n>=3.

In particular `z=4` reads as bit zero and `z=1` as bit one. A chronological
window of `L` synchronized checkpoints ending at native time `n` therefore
supplies exactly the clock word

    theta_(n-L), ..., theta_(n-1).

Applying `R_k` to this word gives `(n-1) mod 2^k`. To read the current native
phase, use

    native_phase = (R_k(word)+1) mod 2^k.

The plus one is essential; omitting it gives a shifted phase, although it
would leave the marginal rate unchanged. For a length-640 checkpoint window
with every checkpoint synchronized, `n>=642` suffices and yields phase
`n mod 256`. This bound includes history availability, not just the
arithmetic sufficiency of 640 bits. It is not asserted to be sharp.

The resulting residue reader is a mathematical function of the declared
finite checkpoint history and uses only its phase sums. It supplies no
history storage mechanism, coupling, permanently writable record, physical
reader selection, external-context schedule invariance, or recovery of
original-head information lost before synchronization. The complete spectra
proved here remain the **clock-only** spectra; readers additionally using
the other checkpoint coordinates require their own classification.
