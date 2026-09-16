# Occurrence analysis: chronological first hits and ordered incidence words

**PROOF-FIRST / RESULT-EXPOSED.** Public claim lock: issue #871,
`P-QDD-V80-CLOSURE-BOUNDARIES-1`. This is the occurrence part of the frozen
joint closure-boundary proof against Public Canon v79. Its results were
derived analytically before the formal pin and are disclosed in full. No
scientific gate was executed in preparing this proof or its accepted audit.
The public v79 content and existing physical obligations are unchanged.

The primary statements concern exact finite maps, cardinalities and their
universal algebraic consequences. Arbitrary probability vectors below are
conditional mathematical parameters. No physical probability, sampled
ensemble, empirical observation, L6 measure or new layer gate is adopted.

The underlying source, Cartesian fibres, 1024-slot word, acquired native
phase and fresh-cell protocol are exactly those of
`QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD` and
`probes/P-U-PREPARATION-EVENT-RECORD-1/INCIDENCE-PROOF.md`. This proof addresses
the remaining difference between consecutive-tick occupancy ratios and the
law of the first and subsequent coarse labels. It does not identify two
complete records merely because their LOW/HIGH projections agree.

## 1. Complete chronological onset class

Fix a positive integer M and a word

    e: Z/M -> {LOW,HIGH,SILENT}.

After valid acquisition, observation starts at a chosen phase R and then
invokes e once at every consecutive tick forever. SILENT appends nothing;
each accepted tick appends its existing record. No reset, feedback, source
change, thinning or reordering occurs during this run. Phase equality and
ordered coarse-output equality are literal. If R is assigned a mathematical
probability law mu, it is the only variable input to the output sequence.
No claim is made that such a law is physically supplied.

Let the nonempty accepted-address set be

    S={t_0<...<t_(D-1)} subset {0,...,M-1},
    c_i=e(t_i),
    t_(-1)=t_(D-1)-M,
    J_i={t_(i-1)+1,...,t_i} modulo M,
    g_i=|J_i|=t_i-t_(i-1).

Indices of c and J are cyclic. Observation at an occupied onset accepts
that very tick; the half-open direction in J is therefore essential.

**Proposition 1: exact complete ordered law.** The J_i partition Z/M into
nonempty sets. On R in J_i the entire accepted coarse sequence is exactly

    c_i,c_(i+1),c_(i+2),... .

Consequently, for every k>=1 and every prescribed label word
w=(w_0,...,w_(k-1)),

    P_mu(first k accepted labels = w)
      = sum_i mu(J_i) product_(j=0)^(k-1) 1[c_(i+j)=w_j].       (1)

Conversely every probability vector nu on the D accepted starting indices
is realized by some onset law: put mu(t_i)=nu_i and zero elsewhere. Thus
the complete class of ordered laws induced by arbitrary onset distributions
is exactly the convex hull of the D cyclic deterministic accepted streams.
Different starting indices can yield the same stream; the statement does
not assume their distinctness. If S is empty, the disposition is NO_EVENT
at every valid tick and there is no first accepted label or accepted law.

**Proof.** Between the previous accepted address and t_i inclusive, t_i is
the first accepted address encountered while advancing chronologically.
These disjoint cyclic intervals cover the circle. Subsequent accepted
addresses occur in their cyclic order. Taking the probability of this
finite partition proves (1). Concentrating the chosen mass at each t_i
proves the converse. The empty case follows from the definition.

For uniform onset, nu_i=g_i/M. The first-label law is therefore weighted
by the preceding gaps, whereas selecting an accepted address uniformly
would give nu_i=1/D. These are different experiments even though both are
described informally as observing at an unspecified phase.

## 2. No common onset law can realize all v79 source weights

Retain the exact source domain V={-2,-1,0,1,2}^4. Write

    s=sum_i v_i, Q=sum_i v_i^2,
    A=s^2, B=5(4Q-s^2), D=A+B.

LOW addresses are 8a+b with 0<=a,b<|s|. HIGH addresses are

    64+16(5j+c)+4a+b,

where j indexes the ordered pairs
((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)), 0<=c<5, and
0<=a,b<|v_i-v_k| for the pair (i,k) at index j.

Suppose A>0 and B>0. Let m=|s|, let j_* be the largest pair index with a
nonzero difference, and put d_*=|v_i-v_k| at that pair. The largest occupied
LOW and HIGH addresses are respectively

    L_max=9(m-1),
    H_max=64+16(5j_*+4)+5(d_*-1)
         =123+80j_*+5d_* .                                    (2)

All occupied LOW addresses precede all occupied HIGH addresses. Therefore
the complete set of onset phases that yield first LOW is

    F_v={0,...,L_max} union {H_max+1,...,1023}.                  (3)

Indeed an onset at or below L_max encounters an occupied LOW before any
HIGH, including when the onset itself is an empty LOW slot. An onset
strictly between L_max and H_max encounters HIGH next. An onset beyond
H_max wraps to the occupied LOW address zero.

For an arbitrary onset law the first-LOW probability is exactly mu(F_v).
For uniform onset it is

    (1024-H_max+L_max)/1024.                                   (4)

If A=0 and B>0, every first label is HIGH. If B=0 and A>0, every first
label is LOW. At v=0 there is no first accepted label.

**Proposition 2: complete common-onset obstruction.** Let mu be any
probability law on Z/1024, required to be independent of the captured
source v. In the complete class of all such mu, none makes the first-LOW
probability equal to the QDD value A(v)/D(v) for every supported v in V.
The same impossibility holds for any distribution of absolute valid onset
times whose residue distribution is common across sources.

**Proof by two exact sources.** Choose

    v=(1,0,1,0),        w=(2,-1,1,0).

Both have s=2. For both, the final pair j_*=5 is (2,3) with d_*=1. Hence

    L_max(v)=L_max(w)=9,
    H_max(v)=H_max(w)=528,
    F_v=F_w={0,...,9} union {529,...,1023}.                      (5)

Their first LOW/HIGH outputs agree at every single onset phase. However,

    Q(v)=2, A(v)=4, B(v)=20, D(v)=24, A(v)/D(v)=1/6,
    Q(w)=6, A(w)=4, B(w)=100, D(w)=104, A(w)/D(w)=1/26.

Thus mu(F_v)=mu(F_w) cannot equal both required values. This exhausts all
common onset measures at once; no strict positivity, rationality, smoothness,
uniformity, computability, stationarity or finite-support restriction is
imposed on mu beyond its being a probability on the stated finite carrier.
Absolute times reduce to their residues because the word is periodic. QED.

This is coarse-outcome equality only. The sources, waiting times, signs,
fine slots and full records may differ. Their difference cannot repair
the failed necessary coarse marginal in this first-hit class.

For the earlier v79 source u=(1,0,0,0), A=1, B=15 and the final HIGH is
288. Equation (4) gives

    uniform-onset first LOW = 736/1024 = 23/32,
    accepted-stream LOW density = 1/16.

Thus the seemingly natural added assumption of uniform onset does not
even repair that individual witness. Proposition 2 is stronger: changing
to any other common phase measure cannot repair the whole supported domain.

The negative class is complete only for this fixed incidence word and
consecutive first-hit protocol with source-independent onset. It does not
exclude source-dependent coupling or onset, a changed slot order, a new
invocation/reset protocol, fresh trial randomness, other apparatus splits,
or any complete physical class that has not been independently specified.
It does not close `QDD-INSTRUMENT-APPARATUS` negatively.

## 3. The ordered law of one retained-source accepted stream

**Proposition 3: exact bunching and a finite ordered diagnostic.** For the
same fixed incidence construction with A>0 and B>0, deleting SILENT from
one full phase cycle gives precisely

    LOW^A HIGH^B.

At any onset the entire infinite accepted sequence is a cyclic shift of
the repetition of this word. In particular its all-prefix adjacent-pair
frequencies, measured per pair of consecutive accepted records, are

    LL: (A-1)/D,   LH: 1/D,   HL: 1/D,   HH: (B-1)/D.           (6)

These limits hold for every onset and hence for every probability law on
onsets. The stream cannot have a nondegenerate independent Bernoulli law
at its accepted indices, for any law on the initial onset.

**Proof.** Every LOW address lies below every HIGH address, so chronological
deletion of silent positions gives the displayed word. A cyclic word of
this form has A-1 adjacent LL pairs, one LH, one HL and B-1 HH per D
cyclic pairs. Every prefix differs from complete periods by a bounded
remainder, which proves (6). For the all-order assertion, no admitted
output sequence contains A+1 consecutive LOW symbols, whereas independent
Bernoulli(p), 0<p<1, assigns that word positive probability p^(A+1).
The empty/single-label cases are excluded explicitly by A>0 and B>0. QED.

For u=(1,0,0,0), the accepted word is LOW HIGH^15. Its LL pair never
occurs. Bernoulli(1/16) would give it probability 1/256. This is an exact
two-record distinction, not a statistical claim about any real apparatus.
Independence is not inserted as a requirement of the physical owner: (6)
instead supplies the correlations that would have to be adopted, tested
or changed if this mathematical stream were proposed as its ordered law.

## 4. Positive conditional alternatives and their remaining costs

**Proposition 4: source-independent permutation scan.** Consider all M!
permutations Pi of the M addresses, without choosing a physical law on
them. Inspect addresses in the given permutation order, at most once
each, and stop at the first accepted address. For every nonempty accepted
set S and every t in S, exactly M!/|S| permutations return t first. Under
the separately stated conditional uniform distribution on permutations,
common to every source and chosen before inspecting its occupied slots,
this finite count gives

    P(t is the first accepted address)=1/|S|.                   (7)

Consequently the first coarse LOW/HIGH probabilities are exactly A/D
and B/D for every nonzero source of the incidence construction. The zero
source has no accepted address and is assigned NO_EVENT after M visits.

**Proof.** The first accepted slot always exists when S is nonempty.
For any two t,u in S, transposing their names in every permutation is a
bijection on the M! permutations. It interchanges the sets of permutations
in which t and u appear first among S. All D such sets therefore have
equal cardinalities and partition the M! permutations. Each cardinality
is M!/D. Conditional uniform normalization gives (7); summing over LOW
addresses proves the conditional coarse claim. The empty case is
separate. This argument works for every subset S of Z/M, not only for
the known QDD occupancy sets, and uses neither A/D nor a QDD target as
an input to the permutation selection. QED.

For every k<=D, each exact ordered list of k distinct accepted slots is
the initial accepted list of precisely M!/(D)_k permutations. This follows
by extending a bijection of two such lists to a permutation of S and fixing
its complement; it bijects the corresponding classes of address orders.
The classes partition all M! orders and there are (D)_k of them. This is
again an exact count, including k=0.

Under conditional uniform normalization, if a whole scan is retained, the
accepted slots are a uniformly ordered list of S. For any k<=D and any
prescribed coarse word containing a LOW symbols and b HIGH symbols,
a+b=k, its probability is

    (A)_a (B)_b / (D)_k,                                     (8)

where (x)_j=x(x-1)...(x-j+1), (x)_0=1. Uniformity of the induced order on
S follows from the same permutation bijections. Each exact ordered
distinct-slot list has probability 1/(D)_k; there are (A)_a(B)_b lists
with the prescribed coarse labels. This proves (8), including zero when
too many slots of one kind are requested. A scan is sampling without
replacement and does not give independent records. Independently redrawing
Pi for each fresh first-hit trial would give independent coarse outcomes
for a fixed retained source. One shared permutation across trials does
not justify that conclusion.

This repair changes the complete observation class. It introduces the
permutation carrier, its source-independent uniform law, persistent scan
position and its fresh-trial resupply. It can be scheduled on the existing
periodic phase clock by continuing chronological bit acquisition while
waiting for each next listed residue before invoking the observation;
every residue recurs within M ticks. Those nonconsecutive selected
invocations are outside Proposition 2. Alternatively direct random access
would be another declared apparatus resource. Neither realization follows
from unchanged U, and the uniform permutation law is an additional
measure assumption requiring its own physical and layer justification.
The positive mathematical repair therefore does not close O1.

There is also an exact constructive answer for the narrower *different*
question of which source-specific onset laws preserve consecutive scans
and yield uniform accepted starting index. Precisely when

    mu_v(J_i(v))=1/D(v) for every accepted index i.              (9)

One explicit choice is uniform mass on occupied addresses:

    mu_v(t_i)=1/D(v), mu_v(r)=0 for unoccupied r.

Another spreads mass uniformly within each preceding gap:

    mu_v(r)=1/[D(v) g_i(v)] for r in J_i(v).

Both give first LOW A/D without entering a reduced rational target into
the selector; they use the already declared incidence set. Equation (9)
is necessary and sufficient for a uniform *fine accepted starting index*,
which is stronger than merely obtaining the correct coarse LOW marginal.
No uniqueness is asserted: masses can be distributed freely inside each
gap while preserving its prescribed total.

If an additional mechanism independently redraws such a phase for every
fresh fixed-source trial, the coarse labels are Bernoulli(A/D). If it draws
only once and then observes continuously, Proposition 3 still applies and
the labels are not independent. A source-specific onset kernel and repeated
independent draws are additional mathematical resources, not consequences
of the native phase reader, its density theorem, the archive or the
Cartesian identity. This route is a conditional construction and does not
supply its own physical occurrence, sampling or L6 certificate.

## 5. Novelty, dependencies and candidate review targets

The v79 proof already establishes the periodic word, exact prefix counts,
two deterministic first-onset alternatives and calendar sensitivity. Those
facts are not claimed anew. The new deductions here are the complete
gap-partition formula for all ordered labels, the two-source obstruction
to *every* source-independent onset law, and exact accepted adjacent-pair
frequencies/all-order independence obstruction. The underlying general
finite-word counting is proved here rather than imported from an external
probability theorem.

The dependencies are the v79 incidence definition and its slot bijection,
the acquired phase identity and unchanged consecutive observation contract,
and the existing QDD comparison A/D. No physical ownership, new source
capture, carrier equality, saturation or instrument theorem is assumed.
The already registered `TM-ENTROPY-ZERO` is not needed; periodic incidence
gives a more direct and narrower all-order obstruction.

The accepted `onset_audit.py` is inert on import. Its `audit()` function
checks the complete ternary-word inventory M=1,...,6, every inclusive onset
and the first three accepted labels, together with an exact nonuniform
mixture check. It checks all 625 source vectors and all 1024 slots by
independent Cartesian enumeration and inverse slot decoding, every
source's first-label map, the two explicit same-map witnesses, the uniform
23/32 discrepancy and the cyclic pair counts. It also checks every
nonempty subset and every permutation for M=1,...,6, including all fine
ordered accepted prefixes. These finite checks are audits of the written
proofs, not extrapolated proofs of their universal statements. The
coordinator must freeze and publish the complete preregistration and
accepted verifier before executing any of these checks.
Falsifiers are a wrong cyclic partition or first-hit map, an incorrect
extremal occupied slot, a discrepancy in the two sources' first-label
functions or rational targets, a wrong pair count, or an admitted
nondegenerate Bernoulli stream in the declared periodic class. An expanded
apparatus or observation class is not a counterexample to this scope.

These deductions delimit the current construction without opening another
physical owner. They establish a concrete failed route toward O1 and a
conditional alternative, not a decision replacing the missing physical law.
