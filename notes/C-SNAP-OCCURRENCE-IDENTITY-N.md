# C-SNAP-OCCURRENCE-IDENTITY-N

**NON-CANONICAL / physical STOP-DEFINITION.**
Public lane: [#893](https://github.com/mathorn1973/twist-j/issues/893).
Authority remains Public Canon v80 under [STATUS.md](../STATUS.md).
This note connects [relational reading](C-RELATIONAL-READING-ARITY-N.md) and
[integer geometric accumulation](C-GEOMETRY-RELATIONAL-ACCUMULATION-N.md).
The separate [identity proof](../probes/P-SNAP-OCCURRENCE-IDENTITY-1/PROOF.md)
owns the mathematical arguments and their frozen scope; this note creates
no Canon claim, physical event definition, gate or competing apparatus schema.

## 1. Equal values and different occurrences

The immediate question is which equality the phrase "the same substrate
state" means. Along one native U trajectory, complete states `(n,x_n)` never
repeat because the counter increases. Checkpoints do repeat: for every
origin-zero head, `x_4=x_6`, although `theta_4=1` and `theta_6=0`. Different
initial histories may also merge into the same later complete current state.
Thus nonrepetition along one trajectory does not establish recovery of every
origin or history. These distinctions are already exact in
[the native chart](../probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md) and
[the checkpoint collision](../probes/P-CARRY-J-CHECKPOINT-1/PREREG.md).

An occurrence address, an event payload and a material record answer different
questions. Two positions in an ordered history may contain equal payloads
without being the same position. Reading one position twice may return the
same payload without creating another accepted interaction. Conversely,
requiring a globally unique printed identifier for every physical event is
an additional contract: distinct events may be identified by their relations
to apparatus, positions or other records without carrying unique symbols.

The existing counter supplies a mathematical address for a native transition.
It does not select which transitions are Snaps, what counts as one event,
or whether a record was physically written. If one transition emits a batch,
the tick alone does not identify its individual members. A proposed address
may need a context or run, a tick, and a channel or within-batch ordinal.
Which fields matter belongs to the chosen event equality.

## 2. What the mathematical classification settles

On the ordered count carrier `N_0`, require an equivalence relation compatible
with successor: `i~j` implies `i+1~j+1`. The companion proof classifies the
whole class. Either every index remains distinct, or there are `mu>=0` and
`p>=1` such that indices below mu are singleton classes and indices at or
above mu are identified exactly by their residues modulo p. Consequently,
compatibility with the next step permits both distinct occurrences and
eventually cyclic identification. It does not choose the physical equality.

There is also a precise native address boundary. A fixed deterministic
length-L reader of synchronized decorated checkpoints has only finitely many
possible inputs. Every legal input recurs with bounded gaps on its actual
origin-zero U trajectory. Therefore every identifier it emits from such an
input recurs, and its identifier image has at most `20,000 L` elements on
one chart. It cannot print a fresh unique identifier at every accepted
occurrence. This uses the inherited all-time recurrence and
[native language bound](../probes/P-U-FINITE-READER-INDEPENDENCE-1/PROOF.md),
not extrapolation from a finite experiment.

This is an obstruction to that address contract, not proof that the repeated
outputs represent one physical event. An added log position, explicit
counter read or further apparatus resource changes the contract. Similarly,
the linear accepted-word bound gives zero exponential complexity rate; it
does not say that the native sequence has zero complexity or is periodic.

## 3. Cubic tagged counts require an occurrence carrier

The preceding geometric result counts tagged incidences. For the stated
integer lift, balls satisfy `|B_k|=3k(k+1)+1`, and

```
|{(k,x):0<=k<=n, x in B_k}| = sum_(k=0)^n |B_k| = (n+1)^3.
```

Forgetting k leaves the largest ball, of quadratic size. In the literal
modulo-five quotient the balls instead saturate at 25. These are different
counted objects and equalities, as shown in
[the growth proof](../probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md).

If every retained tag is to become a separate event and a protocol allows
at most one event per tick, the cubic tagged set requires at least `(n+1)^3`
emission ticks. Enumerating its tags attains that counting bound. The sharp
serialization result in the companion identity probe makes this resource
explicit. A layer index is not automatically an emission tick: realizing all
of layer k in one tick would instead require a batch of `|B_k|` events.
Neither convention follows from the cardinality, and neither establishes a
spatial dimension or physically instantiates the tags.

Growth normalization also retains its precise hypotheses. A supplied shell
asymptotic `S_k~c*d*k^(d-1)` with `c,d>0` suffices for
`sum_(k<=n) S_k~c*n^d`. The converse local shell-ratio inference does not
follow merely from `V_n~c*n^d`. The valid macroscopic statement is
`V_floor(lambda*n)/V_n -> lambda^d` as `n -> infinity` for each fixed
`lambda>1`; replacing that limit by `lambda -> infinity` or silently using
an infinitesimal shell would change the claim.

In particular, for supplied nonnegative counts `|B_r|~c*r^d`, c>0 and d>=0,
the tagged sum has leading term `c*n^(d+1)/(d+1)`. The increment in growth
degree belongs to this explicitly tagged count. Calling it a world-volume
principle is a proposed interpretation until tags are identified with events.

## 4. A record mechanism exists conditionally, with disclosed choices

The registered reservoir account is a useful positive mathematical example.
Its chosen wave/port coupling transfers deposits into a persistent signed
tape. A fixed channel partition and threshold q divide the accumulated
energy into integer counts and remainders. Each newly crossed lifetime
ordinal is emitted once, including multiple crossings in one batch; with
zero initial heat and no added input energy, the total count is at most
`floor(E_initial/q)`. See
[the reservoir proof](../probes/P-DECODER-RESERVOIR-COUPLING-1/PROOF.md).

The separate NON-CANONICAL stabilizer apparatus composition additionally
distinguishes READ, END and RESET. READ is nonmutating; END administratively
closes the run; RESET
archives the old account and preserves its signed store, residuals and
lifetime ordinals. These are conditional laws of the
[published record account](../probes/P-QDD-STABILIZER-APPARATUS-1/RECORD-CONTRACT.md).
They show how multiplicity and passive rereading can be kept distinct.

The coupling, conductance, threshold, channel partition, fresh cold incoming
ports, retained tape and batch convention remain explicit premises. Changing
a threshold can change the mark count while leaving the energy transfer
unchanged. This model has not derived a universal Snap, a photon identity,
a QDD outcome or a physically selected detector.

Regenerating a log is weaker than this retained-record specification. The
[native archive corollary](../probes/P-QDD-V80-CLOSURE-BOUNDARIES-1/NATIVE-PROOF.md)
allows suitable stipulated histories to be recomputed from current state and
counter. Its limit of 3,125 alternative histories at common origin is not a
bound on their lengths or event counts. It supplies no material tape, fresh
independent inputs or evidence that a past write occurred.

## 5. The next attack belongs under the existing apparatus owner

Use the existing [#539 contract](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md)
as a specification surface, with the current physical owners in
[REGISTRY.tsv](../canon/REGISTRY.tsv) retaining authority. This note adds no
new schema. One proposed profile must fill the following existing obligations:

1. Freeze the complete source, context, apparatus state and transition emitter,
   including every consumed clock, memory, blank input and batch resource.
2. Freeze event granularity and equality before testing outcomes. State the
   relation between payload equality, occurrence identity, apparatus equality
   and ordered-history equality; publish any deliberate quotient.
3. Give the acceptance/completion rule and exact handling of NO_EVENT,
   passive rereading, fresh interaction, multiple emissions and invalid calls.
4. Supply the actual persistence/reset laws and independent realization
   evidence for any physical claim; retain the required layer gates.

The strongest next target is one fixed, independently motivated apparatus
transition and emitter. Compare two fresh interactions with equal source
payload against two passive reads of an existing record. The required result
is determined by the frozen event/history equality and resources, not by the
desired number of Snaps or a Born target. If the two situations are claimed
different but the admitted inputs cannot distinguish them, an exact
factorization counterexample can refute that proposed profile. If a profile
does distinguish them, prove that its transition, append and persistence laws
preserve the declared identities across continuation and reset.

This tests an explicit mechanism rather than selecting an equality after its
desired output is known. Until that profile is supplied, the physical Snap
question and the existing QDD apparatus and terminal-event obligations remain
STOP-DEFINITION. The mathematical identity and serialization results do not
falsify Born's marginal law or promote a new canonical physical reading.
