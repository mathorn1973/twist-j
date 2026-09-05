# Ownership and causal-prefix argument

NON-CANONICAL / CANDIDATE ARGUMENT / NO PHYSICAL EVENT CLAIM.

Let a finite indexed input have length N and channel-6 indices
`j_0<...<j_(K-1)`. Each raw row is identified by its index and its three
unsigned words. A right-boundary reference is distinct from row ownership.

If K=0, the sole unanchored snapshot owns `[0,N)`. If K>0, the disjoint
half-open intervals

```text
[0,j_0), [j_0,j_1), ..., [j_(K-2),j_(K-1)), [j_(K-1),N)
```

partition `[0,N)` in increasing order. Empty initial ownership can be omitted.
Thus concatenating owned rows reconstructs every original row once; the same
holds for their fixed-width `<QQQ` byte encodings. Nonowning right references
are not part of this concatenation. Their repetition as the next left owner
does not duplicate ownership.

Maintain the invariant: emitted packets own an initial input segment; pending
rows are exactly the remaining suffix; their concatenation equals the input
read so far. Before the first sync, all rows are pending and unanchored.
On the first sync, emit the old prefix if nonempty and retain the sync as
the pending left boundary. A nonsync row appends only to pending rows. On
the next sync, emit the pending left-boundary-plus-interior packet with the
incoming sync as nonowning right reference, then retain that incoming row as
the new pending left boundary. Each case preserves the invariant.

Emission therefore depends only on the prefix through the incoming boundary.
Its `emitted_at` is that row's index. Later input changes only pending rows or
appends a new packet. A snapshot is a value describing pending rows and leaves
the state unchanged, so ending an inspected prefix creates no new closed event.
The empty input, consecutive syncs, no sync, one sync and trailing nonsync rows
all satisfy the same invariant without special deletion rules.

An induction over individual input rows gives chunk independence: feeding a
concatenation and feeding its positive-sized chunks execute the same ordered
transitions. At every prefix length they therefore have the same emitted
packet sequence and pending snapshot. Immutable packet contents preserve
already emitted prefixes under extension.

Derived references select owned interior indices with explicitly named channel
predicates. Missing, repeated and simultaneous setting classes partition the
nonnegative count pairs `(n_2,n_4)`. Detector multiplicity is retained. For a
closed interval, a detector's left-sync difference uses exactly that raw left
boundary. A unique-setting difference exists only when `n_2+n_4=1`; no witness
or clock is selected when the reference is absent or ambiguous. Calendar and
unknown rows remain raw data, with no event-time interpretation imposed.

The implementation audit compares a streaming state machine with an independent
batch slicing construction, reconstructs the original bytes, and checks derived
views and prefix behavior. Digests compact the public transcript; the ownership
argument is about exact rows, not a mathematical claim that a cryptographic
digest is injective. A computed digest mismatch is a definite audit failure;
matching hashes provide reproducible integrity evidence for the finite data.

This argument concerns an explicitly chosen serialization and software
transducer. It supplies neither an apparatus realization nor a physical trial,
terminality, no-click, post-state or probability law. Its public scientific
status is not raised merely by placing it beside a verifier.
