# P-SNAP-OCCURRENCE-IDENTITY-1 preregistration

**Do not execute before immutable commit, push and accepted-byte readback.**

Mode: PROOF-FIRST / RESULT-EXPOSED / NON-CANONICAL MATHEMATICS.
Owner: A. M. Thorn. Public lock: [#893](https://github.com/mathorn1973/twist-j/issues/893).
Base: `94cab0e0941c6aca51d5ef580d21002e4b4105b9`.
Authority: ACTIVE Public Canon v80, tag `canon-v80`, content commit
`b00171ef21ecb0d905593224f66f5e8a0f6c28e5`, Canon SHA-256
`8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c`,
541516 bytes. No formal execution has occurred during preparation.

## 1. Equations and mathematical targets

The question is which premises distinguish equal payloads as different
occurrences. No physical definition of Snap is presumed.

1. Classify all equivalences E on N_0 with
   `n E m => (n+1) E (m+1)`: equality, or the unique index-period quotient
   `n E m iff n=m or (n,m>=mu and p divides n-m)`, mu>=0, p>=1.
   Adding successor cancellation leaves equality and the mu=0 quotients.
   The kernel of an address map h has this property exactly when its image
   admits an autonomous update `T(h(n))=h(n+1)`. Arbitrary deterministic
   observation of a richer state is not the same premise.
2. A right congruence on payload words is exactly a deterministic history
   reader kernel. Weak append compatibility, including cancellation of a
   common appended symbol, need not preserve order or fresh identities.
   Separating the empty word and recovering both the last symbol and the
   predecessor class forces exact word equality. SILENT erasure preserves
   accepted multiplicity while forgetting native timing.
3. On each synchronized origin-zero native U trajectory, any fixed map
   from decorated length-L windows to IDs or NO_EVENT has at most 20,000 L
   distinct IDs, and every emitted ID recurs infinitely often. This follows
   from the already public full native language and recurrence proofs, even
   if the declared ID codomain is infinite. Finite additional apparatus
   state A gives the cardinality bound |A|20,000 L; recurrence is not claimed
   for arbitrary added state dynamics. Counter access supplies a different
   address class. None of these bounds denies distinct physical events
   whose identity is supplied outside the emitted symbol.
4. For a fixed positive integer c, an initially empty log appending at most
   c atomic entries per tick can
   materialize at most cT entries in T ticks. Injectively materializing
   `W_R = disjoint union_(r=0)^R B_r`, where
   `B_r={(x,y) in Z^2: max(|x|,|y|,|x-y|)<=r}`, needs at least
   `ceil((R+1)^3/c)` ticks. This is sharp: lexicographically serialize the
   tags of layer r at slots `r^3,...,(r+1)^3-1`, then group at most c slots
   per tick. A counter reader can describe this sequence; physical writes,
   fresh storage and the timing interpretation do not follow from it.

The geometric obstruction concerns atomic entries under the stated budget.
It does not bound the cardinality of a set described by one entry, or the
number of relations reconstructed between previously recorded entries.

## 2. Accepted code

`verify.py` is a standalone Python >=3.10 standard-library exact audit. It
reads no repository files, external data or network, uses no randomness or
floating-point assertions, and emits one deterministic JSON record. The
all-domain arguments are in the accepted `PROOF.md`; enumeration is an audit,
not an extrapolation from finite tests.

An exact mismatch is retained as FALSIFIED with exit 0 and explicit failure
data. An unexpected exception or incomplete process is integrity STOP, not
scientific falsification. An uncompleted pin is consumed under POLICY.md;
neither code nor thresholds may be repaired or reused after freezing. Only
static review and syntax parsing are allowed before public pin and readback.

## 3. Carriers and finite audit ranges

There is no experimental payload. The finite fixtures are defined before use:

- Every equivalence partition of `{0,...,N}` for N=0..8, testing local
  successor preservation and cancellation. Compare the full admitted set
  to restricted index-period kernels; counts are `1+N(N+1)/2` and `N+1`.
- Every deterministic map on a labeled set of size 1..5, from every initial
  state, using trajectory endpoints 0..2m+2 for carrier size m and comparing
  the orbit's first repetition with its index-period kernel.
  Injective maps must have no transient on any starting orbit.
- Binary payload words of length at most four and the exact, length-modulo
  two/three, Parikh-count and set-accumulation controls. Check append
  compatibility, empty separation and final-symbol/predecessor recovery,
  with explicit counterexamples and parents of length at most three. Audit
  chronological SILENT erasure on words of length at most four and on
  concatenations whose total raw length is at most four.
- Independently enumerate hexagonal balls by six-generator breadth-first
  expansion and by the norm inequality for radii 0..20. Audit lexicographic
  rank/unrank, layer and prefix cardinalities and the cube slot boundaries.
  This includes all 9261 tagged points and slots 0..9260 through radius 20.
  Audit budgets c=1..5, minimal completion counts and distinct same-tick
  batch addresses.

Detailed finite loop bounds and witnesses are part of the accepted source.
The inherited native recurrence and complexity theorem is used as a written
dependency, not silently rerun or purportedly re-proved by these fixtures.

## 4. Systematics, inherited inputs and prior exposure

Run in Linux or Linux-compatible WSL with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. Record actual Python version,
platform and architecture; CI uses Python 3.12. Require deterministic UTF-8
stdout, empty stderr, exit 0 and a 600-second process ceiling.

The expected structural conclusions are exposed before freezing. This is
not blind prediction, a claim of historical novelty for cyclic quotients
or free words, or an independent rediscovery of inherited native dynamics.

Dependencies: `P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md` sections 2-4 for the
actual decorated native language and bounded-gap recurrence;
`P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md` for the adopted integer hexagonal
lift and its relation to the finite native quotient. The lift remains an
explicit extra carrier. Existing fresh-record, record-monoid descent and
reservoir-accounting results remain unchanged. Any external mathematical
reference in the proof is background, not runtime data or a missing proof.

The index includes n in the full native state `(n,x_n)`, so that state never
repeats along one orbit. Repetition of a checkpoint or reader output must
not be substituted for repetition of the full autonomous state. An address
may require a run/context and a batch ordinal as well as a tick. Accepted
event rank is distinct from native tick when some ticks are silent.

## 5. Threshold and disposition

Threshold: zero exact mathematical mismatches. Preserve any admitted
counterexample to a frozen target; never adjust the class to save it.
Proof defects without an exact negation leave the affected claim unresolved.
Source-integrity, process or architecture failures are integrity STOP.

Complete proofs and byte-identical x86_64/aarch64 replays support only the
stated NON-CANONICAL mathematical conclusions. They cannot decide which
equivalence, emission granularity or physical persistence law Nature uses.
The physical event owner stays STOP-DEFINITION until an independent admitted
apparatus profile supplies those definitions. A later Canon fold is separate.

## 6. Action layer and immutable procedure

Action layer: L1 mathematical addresses, words and counting protocols.
No L4 apparatus selection, admitted L5 material stream, L6 probability,
physical dimension, Born derivation or universal physical no-go is claimed.

Commit and push PREREG.md, PROOF.md and verify.py before execution; read back
their hashes at the full pin. Execute the accepted verifier once locally and
append byte-identical EXPECTED.txt, RUN.md and RESULT.md. Require both CI
architectures and merge without squash or rebase. No existing probe, Canon,
Registry, Frontier, authority, gates, workflows or release is changed.
The companion note is an adapter to the existing definition-only issue #539;
this independent mathematical probe neither occupies nor completes that lane.
