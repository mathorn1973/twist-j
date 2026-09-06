# Result: exact finite-history event decoder and its write boundary

Status: `T` proposed by the separately reviewed exact proofs; non-canonical
candidate until a separate public fold.
Outcome: `FINITE-HISTORY-PHASE-AND-RATIONAL-CAPACITY-PROVED;
PERMANENT-WRITE-AND-MERGER-BOUNDARIES-RETAINED`, subject to required
pull-request acceptance on both architectures.
Action layer: L1 only.

## Positive construction

A fixed finite past-and-current Thue-Morse window reconstructs native clock
phase modulo every fixed power of two. For k>=1 a sufficient length is
`L_k=5*2^(k-1)`; therefore **640 bits suffice for phase modulo 256**. This
bound is proved for every eligible endpoint, not estimated from a sample,
and no claim of minimality is made.

The implemented mathematical interface is causal and explicit. Begin with
an empty finite observer buffer, append each supplied bit and discard the
oldest when full. Before a complete window, return UNAVAILABLE. Reject
illegal complete words and nonbinary inputs with ERROR. Once available,
the phase and event functions receive only the bounded word and fixed
parameters; they receive no counter or future bits. The buffer feeds no
data back to U. This is an additional observer history resource, not a
physical memory carrier already proved to exist inside a checkpoint.

Given any supplied rational a/b in [0,1], choose a power M=2^k>=b. Read
the phase r from the window and return LOW for r<a, HIGH for a<=r<b, and
SILENT otherwise. LOW has density a/M, acceptance has density b/M, and
the accepted LOW ratio is exactly a/b. Every M consecutive full-window
ticks contain a LOW, b-a HIGH and M-b SILENT outputs. The theorem and
constructor cover all rational parameters, independently of any QDD list.

For example a=1,b=M=256 gives LOW density 1/256 with no silent ticks and
at most 640 bits of history. On synchronized native checkpoint histories,
z_n=4-3*theta_(n-1) supplies the preceding driver bit. Decode that word and
add one modulo M to obtain the current phase. A 640-checkpoint window is
fully synchronized by n=642. A single current checkpoint is not enough
for this construction's declared history input.

## Complete spectrum of fixed finite clock-window readers

Let the class be all fixed maps from legal length-L clock words to the
event alphabet, with the same map on all overlapping occurrences. Take
the union over all positive finite lengths L, evaluating every natural tick
after warmup. Then the complete spectra are:

| Quantity | Exact union over finite clock-window lengths |
| --- | --- |
| Unconditional LOW density | `{j/(3*2^k): k>=0, 0<=j<=3*2^k}` |
| LOW ratio among positive-density accepted events | every rational in [0,1] |
| Empty acceptance | UNDEFINED |

Every legal factor's frequency follows from complete parent-pair expansion,
with all-prefix convergence proved by a primitive four-state pair automaton.
Conversely, a length-3M window recognizes 6M disjoint classes, each of mass
1/(6M), determined by phase and three causal parent bits. Arbitrary unions
of whole classes prove completeness of the unconditional spectrum. No raw
word or occurrence is fractionally assigned to different outcomes.

These spectra are clock-only. They are not claimed for all checkpoint-history
readers: the sealed instantaneous checkpoint class already attains 1/20,
which lies outside the unconditional clock-only set. Nor is the union
spectrum a claim that every value is available at each particular length.

After the whole rational family was constructed, the audit enumerated all
624 supported QDD piston tuples, corresponding to 15600 full heads. Their
22 distinct LOW weights all occur as family parameters. All eight values
excluded by the previous present-state accepted-event class are included
here. This removes that denominator obstruction by enlarging the read
domain to explicit finite history. It neither changes the earlier result
nor selects a physical source-dependent reader.

## Two boundaries that remain exact

Every finite legal decorated-checkpoint window on each synchronized native
chart recurs with bounded gaps. The proof uses the complete primitive
100-state clock substitution and its length-two image in checkpoints,
rather than inferring word recurrence from single-state frequencies.

Thus a fixed finite-history reader that eventually has one constant value
already had that value on every fully synchronized window of the same
trajectory. It cannot change permanently from a distinct BLANK value to
WRITTEN under unchanged U after its entire window is synchronized. Buffer
warmup UNAVAILABLE is not BLANK. Transient outputs, finite retention and
apparatus with additional persistent state are outside this exclusion.

The original-head merger also survives every finite extension of the window.
The exact heads `(4,1,0,0,0,0)` and `(2,1,1,2,1,0)` have original QDD LOW
weights 0 and 9/14 but the same first successor `(1,4,0,0,0,0)`. Once a
length-L window excludes their distinct heads, their inputs and outputs
are identical forever. No single reader of such late windows recovers both
original records or realizes both different original-head laws. The full
pointed-orbit decoder, whose input retains the head, is a different carrier
and remains unaffected.

## Formal audit

The preregistration, three proof files and exact verifier were publicly
pinned at `f5ba76c60a8aac1a5d3dec80634fcf040be23496`, fetched and compared
byte for byte before the first formal execution. The clean Linux x86_64 run
passed **446919 exact comparisons**, with zero mismatches, zero exit status,
empty stderr, no exception and all six groups completed. These comparisons
are not independent experiments.

Coverage includes every one of 8160 phase-factor generating contexts and
8176 uniform-partition contexts; all 33152 pairs 0<=a<=b<=256, b>=1,
with 7255772 residue allocations and 19949 distinct reduced ratios;
all 6250 synchronized checkpoints with both controls; the 100-state
primitive clock; both clock-child recurrences for every m=0,...,65535;
2298 causal buffer updates and all 32 length-five binary words; the full
supported QDD corpus and the merger witness.

The new run reproduces the inherited primitive certificate M^29 with
minimum entry 1778335 and row sum 536870912. Universal recurrence is
proved from the separately inherited exponent-77 certificate; these finite
checks are audits of the proofs, not a replacement for them.

The actual stdout is 11583 bytes with SHA-256
`a01866fc55b8b6a3d1bec522e650e1db2990eef3f3b90835a71b8ea1486953e7`.
RUN.md preserves custody and the identity of every pinned file. No file in
the pin changed after execution, and no mathematical falsifier fired.
Required GitHub x86_64 and aarch64 replays must match the same exact stdout.

## Physical decoder boundary

The complete mathematical event-reader family now has enough frequency
capacity for every supported QDD rational. For any fixed clock-only member,
every native head sees the same clock and the same output law. The family
does not derive which a/b belongs to a physical preparation. Choosing it
after observing a desired weight would not derive that weight's occurrence.

The history buffer still needs a physical carrier, preparation, readout and
post-state certificate. Source-to-reader coupling, independent context
selection, an exclusive realized outcome, physical occurrence, persistence
and reset remain separate obligations of QDD-INSTRUMENT-APPARATUS, issue
#539 and the proposed TRC1 contract. Natural-tick phase recovery does not
provide invocation-rank accuracy under arbitrary external schedules.

The whole physical decoder remains open. This probe closes its stated
finite-history mathematical construction and classification, and retains
the exact writing and information-loss boundaries. Public Canon v78, U,
all sealed probes and the existing owner contracts are unchanged.
