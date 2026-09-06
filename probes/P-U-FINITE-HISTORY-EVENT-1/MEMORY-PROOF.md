# P-U-FINITE-HISTORY-EVENT-1: causal history and the write boundary

**Prospective, proof-first, result-exposed, L1 only.** Issue #864.
This proof is part of the fresh formal pin named in PREREG.md. Its algebra
may be reviewed before that pin; it reports no new formal execution. The
native clock, synchronized chart and merger below are inherited public
mathematics, not new claims of physical realization. Mathematical capacity
of a reader does not identify a physical occurrence or apparatus law.

## 1. Two reader classes with distinct roles

Let theta_n=popcount(n) mod 2. For a fixed positive integer L, a full causal
clock window ending at n is

    B_L(n)=(theta_(n-L+1),...,theta_n),        n>=L-1.

A clock-window reader is one fixed function of this word. It does not
receive n, the original head, a source-dependent probability, a changing
context, or any state other than its explicitly retained window. The
clock-capacity classification in CLOCK-PROOF.md concerns this class.

For the write boundary, consider the larger class of fixed readers of

    H_L(n)=((x_(n-L+1),theta_(n-L+1)),...,(x_n,theta_n)).

Here x_n is the unchanged native checkpoint on one origin-zero trajectory.
The window is fully synchronized when n-L+1>=3, or equivalently n>=L+2.
Its alphabet is the finite set X14 x {0,1}, with X14={x:sum(x) in {1,4}}.
A reader may have any finite output alphabet and may be nonlinear. The
same one function must be used at every reading time. These larger windows
are used for the recurrence/no-write and merger theorems below, not for
silently enlarging the clock-only frequency-spectrum claim.

Each finite reader has one fixed L. Taking the union over finite L does
not authorize a reader whose window grows with time, a permanent saved
label outside the window, or an accumulated count supplied as an input.

## 2. Inherited primitive clock and the decorated checkpoint word

The source is
[P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md](../P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md),
sections 1-2 and 5. With the inherited S recurrence, write

    c_m=(m mod 5,S(m) mod 5,theta_m,theta_(m+1)),
    C=F5^2 x {0,1}^2,
    T0(r,s,u,v)=(2r,2r-s,u,1-u),
    T1(r,s,u,v)=(2r+1,2r+1-s,1-u,v),
    sigma(c)=T0(c) T1(c),           c_0=(0,0,0,1).

The first two coordinates are reduced modulo five. The infinite fixed word
of sigma starting at c_0 is c_0 c_1 c_2 ..., and its aligned block of
length 2^j starting at a*2^j is sigma^j(c_a). The inherited explicit
integer proof gives M^77>0, where M is the substitution incidence matrix
on all 100 letters. In particular, sigma^77(a) contains c_0 for every
letter a. Neither stationarity nor a finite observed prefix substitutes
for this exact word-containment assertion.

Fix one five-label chart l=(alpha,beta,gamma,delta,epsilon). Its inherited
odd/even formulas define a length-two morphism psi_l from C to decorated
checkpoints:

    psi_l(c_m)=((x_(2m+1),theta_(2m+1)),
                (x_(2m+2),theta_(2m+2))).

The right side is evaluated by the fixed chart formulas from c_m and l.
For m>=1 it is exactly the actual native trajectory at n>=3. The m=0
pair is only a formal chart extension and is not identified with the
unsynchronized actual source checkpoints. Define the formal word

    d_1 d_2 d_3 ... = psi_l(c_0 c_1 c_2 ...).

Thus d_n=(x_n,theta_n) for every n>=3. Deleting its first two letters
gives precisely the fully synchronized decorated trajectory. The morphism
may identify different clock letters; injectivity is not needed below.

## 3. Every legal finite synchronized history recurs with bounded gaps

Call W legal for l if it is a finite contiguous factor of d_3 d_4 ... .
Since it occurs at a finite position, there is an integer j>=0 such that
the finite prefix psi_l(sigma^j(c_0)) contains W. Every letter a satisfies

    sigma^(j+77)(a) contains sigma^j(c_0),

because sigma^77(a) contains c_0 and applying sigma^j preserves that
occurrence. Applying psi_l proves that every word

    psi_l(sigma^(j+77)(a))

contains W. Its native-word length is B=2^(j+78).

The actual infinite d word partitions, from index 1, into aligned blocks
of this length B, each of the displayed form. Any interval of 2B consecutive
native letters contains a complete aligned B-block. Consequently every
interval of 2^(j+79) consecutive letters lying wholly at n>=3 contains W.
This is an explicit finite recurrence bound; it need not be optimal. It
implies that W occurs arbitrarily late, with bounded gaps between starts.

This proof covers every legal finite W and every fixed chart label. It
does not infer word recurrence from positive single-checkpoint frequency:
the required extra step is primitivity and containment under the complete
length-two morphism. It also makes no claim that arbitrary free-control
paths or arbitrary words over X14 x {0,1} occur in the native trajectory.

## 4. Eventual constancy cannot be a permanent write after synchronization

Let f be any fixed reader on length-L decorated windows. Suppose there
exist n_0 and a symbol a such that

    f(H_L(n))=a for every n>=n_0.

Take any earlier fully synchronized window H_L(t), with t>=L+2. Section 3
shows that this same finite word recurs with its right endpoint beyond
n_0. Since f is fixed and its input words are equal, f(H_L(t))=a as well.
Therefore eventual constancy implies constancy on every fully synchronized
window of that trajectory, including all earlier such windows.

In particular, no such reader can be BLANK at a fully synchronized window
and later become a distinct WRITTEN value permanently under unchanged U.
The conclusion holds for every finite L and includes clock-only readers
as a subclass. It does not exclude transient or periodic outputs, finite
retention, an invariant message already encoded by preparation, or writes
in an apparatus with additional persistent state. It does not apply to a
window still containing an unsynchronized checkpoint. UNAVAILABLE during
buffer filling is an administrative tag, not a physical BLANK record.

## 5. Finite late history does not undo an original-head merger

Suppose two origin-zero native trajectories satisfy x_T=y_T at the same
time T. Determinism gives x_n=y_n for every n>=T; the driver theta_n is
also the same for both. Hence

    H_L^x(n)=H_L^y(n) for every n>=T+L-1.

Any fixed finite-history reader therefore has identical output tails on
the two preparations. It cannot recover distinct required original-head
records at late times. If a limiting output frequency or a limiting
accepted ratio with positive limiting acceptance density exists, it is
also the same on the two tails: their counts differ by at most a fixed
finite prefix. If only finitely many events are accepted, no positive
density accepted-event law is asserted here.

The inherited exact witness is

    x0=(4,1,0,0,0,0),       y0=(2,1,1,2,1,0),
    x1=y1=(1,4,0,0,0,0).

Its original QDD LOW weights are respectively 0 and 9/14, as proved in
[P-QDD-U-NATIVE-READBACK-1/PROOF.md](../P-QDD-U-NATIVE-READBACK-1/PROOF.md),
section 4. For every fixed L the two complete histories above are equal
at all n>=L. No single reader in this class can produce both different
original-head laws on these inputs. Access to the pointed full orbit
including its head, or a separately saved original record, is a different
input carrier; neither is prohibited by this theorem or supplied by the
finite clock buffer.

## 6. Explicit causal clock-buffer contract

The following is a mathematical stream implementation of the clock-window
class. It identifies the resource consumed by the positive construction;
it is not a physical realization certificate or a modification of U.

* **Fixed context:** one positive length L, one fixed output function f,
  and any fixed rational construction parameters specified before use.
  Context equality is literal equality of these finite data and the
  algorithm. The source counter is not an additional read input.
* **State:** an ordered binary word b of length at most L, initially empty.
  Equality is literal chronological word equality, including length.
  This carrier has exactly 2^(L+1)-1 states; an implementation may store
  at most L bits plus a fill-length indicator. No minimal-memory or
  physical-bit claim is made.
* **Update:** upon the next supplied native bit theta_n, replace b by
  the last min(L,|b|+1) symbols of b concatenated with theta_n. When the
  buffer is full, exactly its oldest bit is dropped. The update consumes
  one actual bit in order and creates no second clock or feedback to U.
* **Warm-up/read:** after receiving theta_n, return UNAVAILABLE if |b|<L.
  For origin-zero capture the first full window ends at n=L-1. Once full,
  validate the word and apply f(b). UNAVAILABLE is distinct from LOW,
  HIGH, SILENT, a physical zero-support disposition, and a written record.
* **Validation:** a nonbinary input or a full word outside the legal
  Thue-Morse length-L language returns ERROR with the rejected bounded
  word/input retained as evidence. ERROR is administrative, never SILENT
  or a completed event; an invalid capture cannot be repaired by deleting
  ticks and renormalizing an event ratio. On the stipulated native source
  no such error occurs. The theorem does not certify missing or reordered
  acquisitions as genuine native histories.
* **Causal ownership:** a reader sees only the filled word ending at the
  current tick. An output field is a function of that word and the fixed
  context. Updating the finite buffer overwrites its oldest entry; keeping
  a permanent saved output or an append-only output history would be a
  separately declared memory surface, not a hidden part of f.
* **No feedback:** feeds_U=false. Buffer update and output alter no native
  generator, selector, checkpoint, counter, source preparation or future
  native bit. Reinitializing capture is an administrative fresh capture,
  not a physical apparatus reset and not a native time reset.

Legality is a finite exact decision, without a search through an unbounded
observed prefix. Choose k with 2^k>=L. Every length-L factor lies within
two adjacent length-2^k substitution blocks of the binary morphism
mu(0)=01, mu(1)=10. All four binary pairs ab occur already in the prefix
01101001 of Thue-Morse. Therefore
the language is exactly the union, over these four pairs and
0<=r<2^k, of the length-L slices starting at r in mu^k(ab). Conversely,
each such slice is legal because mu^k(ab) itself occurs at an aligned
position of the infinite word. This gives a finite validation procedure;
no construction of a future source bit is required for streaming readout.

The exact stream theorem assumes the ordered native input. A wrapper that
handles nonbinary input returns ERROR without a successful buffer update;
the mathematical update is defined on binary input only. A captured binary
word may still be illegal, in which case the bounded word remains the
buffer evidence and no event reading is assigned to it.

## 7. Rational capacity is a supplied-parameter construction

CLOCK-PROOF.md gives a causal finite-window function recovering the native
right-end residue n mod 2^k, for each fixed k>=1, after the stated warm-up.
Choose integers 0<=a<=b<=2^k, with b>0, before the reading. The reader is

    LOW     if 0<=n mod 2^k<a,
    HIGH    if a<=n mod 2^k<b,
    SILENT  if b<=n mod 2^k<2^k,

where the residue is computed from the window, not supplied as an absolute
counter input. It has LOW density a/2^k, HIGH density (b-a)/2^k, and positive
acceptance density b/2^k. Its accepted LOW ratio is a/b. For any rational
in [0,1], some finite k and finite buffer suffice. This construction has
an exact periodic mathematical output tail; it does not claim independent
trials, randomness, one outcome per source preparation, or a permanent write.

Here a/b is a supplied parameter in a family of mathematical readers. The
construction does not derive a source-dependent a/b from native coupling,
does not read an unknown original QDD head through the clock, and does not
select its parameters from an event target while calling that a derivation.
For a fixed clock-only reader, every native preparation sees the same clock
and therefore the same output law. A physical rule connecting preparation
to an independently selected member of the family remains absent.

## 8. Precise contract and public-owner boundary

The applicable proposal is
[DEF-TYPED-APPARATUS-RECORD-CONTRACT](../../notes/canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md),
issue #539. Its sections 1, 5 and 9 require feeds_U=false, a functional
realized-event step with context and ready state selected independently of
targets, and disclosure of every clock, phase, memory and normalization
input. Section 6 above discloses a mathematical history buffer; it neither
fills that contract's physical carrier identifiers nor supplies its full
post-state, persistence/reset and L4-to-L5 obligations.

The separately proposed
[realization/occurrence contract](../../notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md),
issue #840, explicitly imports an ensemble in section 5. The current
clock construction imports no ensemble, but also issues none of that
contract's physical certificates. In its
[JSON inventory](../../notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.json),
TRC1-CERT-CLOCK, TRC1-CERT-REALIZATION, TRC1-CERT-READOUT,
TRC1-CERT-POSTSTATE and TRC1-CERT-RESET still require independent evidence;
TRC1-CERT-ENSEMBLE is not silently replaced by a proof of reader capacity.

The public owners QDD-INSTRUMENT-APPARATUS,
QDD-INSTRUMENT-CLASS-COMPLETENESS and QDD-TERMINAL-EVENT-SEMANTICS remain
open at their existing scope. No physical event, Born occurrence law,
selected complete apparatus family, L1-to-L5/L6 bridge or whole physical
decoder is obtained. The positive result is new causal finite-history
capacity; the accompanying recurrence and merger results delimit exactly
what that resource does not do.
