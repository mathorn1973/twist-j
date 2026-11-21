# Prospective zero-first common-loader construction

NON-CANONICAL / L1. Identifier P-POLE-HEIGHT-STABILIZER-CHAIN-1.
Public reservation #1903. This file and all scientific sources/fixtures
must be committed, pushed and read back before the first execution.

## Equation and full endpoint

O=Z[j], Phi_5(j)=0; p=j^2, u=1-j, B=1-p, X=1+j-2j^3.
On a labelled pair the contact refuses when x-y is not in 2O; otherwise

    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2).

The other slots are unchanged. All 15 unordered edges of six labelled
slots are allowed. One word acts unchanged on all five input states:

    I_t=(tB,-tB,u,u,X,2),
    G_t=(u+tB,u-tB,0,0,X,2),       t=-2,-1,0,1,2.

Admission is part of the fixed contact, not a choice made by the input
or an outside controller. A refused contact still occupies its position
in the program. Inverse C^(-1)=C^4 is four forward elementary contacts
when an expanded program length is reported.

## Carrier, inputs and prior information

All states are exact integer power-basis tuples. Q(z)=Tr(z*zbar)/2.
Preserved quantities include the whole complex sum, sum of z*zbar,
account sum and each marked residue modulo (1-j). The full helper
endpoint is mandatory, not merely the first four cells.

BANK.json freezes the 64 public directed macros and their inverse IDs,
with odd target states and even source/target states from PR1902.
Its SHA-256 is d4270e03f851f0d2327e2eac7f23cc796b9bbffb1e54b2943f52a0c89fb83f07.
The supplied W38 is audited from the original preparations before its
residuals are used. No old verifier or review script is imported.
PROVENANCE.md discloses all exposed counts and archive hashes. Reported
orbit sizes and targets are comparisons, not hard-coded search outcomes.

## Accepted code and frozen construction

The accepted sources are verify.py and smallstock.py. Both use only the
Python standard library. BANK.json is the only scientific read fixture.
The run prints deterministic JSON records, never elapsed times or host
identifiers. The complete algorithm and logical limits follow below and
are fixed at the source pin.

The construction order is zero, minus two, plus two. The zero graph uses
all 64 original directed macros, with a cap of 4096 vertices. When its
queue exhausts, all generator edges and rooted paths certify the complete
orbit. A native-contact-cost Dijkstra transversal rooted at G_0 supplies
the bridge a from r_0 to G_0. Its reduced expanded length is capped at
4096; exceeding this ZERO_PATH_CAP gives INCONCLUSIVE. Every graph edge (x,m,y) specifies the full
Schreier generator U_x m U_y^(-1), including self-loops. This family is
complete only when the zero orbit is complete. No kernel is factored out.

For the constructive continuation, select at most 256 undirected return
words of native length at most 256, plus inverse directions. Selection
and endpoint diversity choose a subgroup; they do not prove equality to
the full zero stabilizer. Formal adjacent C_e powers may be reduced
modulo five. Agreement on an input is never treated as global equality.

On t=-2, run deterministic bidirectional root-restarted walks for at most
32768 steps on each side, restarting after eight moves. The fixed integer
PRNG, seeds, immediate-inverse rule and all tie ordering are specified in
verify.py. Source and target walks store actual chronological words.
A meeting F,T yields b=F T^(-1). Retain at most eight short such bridges
with distinct resulting t=+2 states. Separately, target-side collisions
between U and V produce U V^(-1), which fixes G_-2 as well as G_0 and both
odd targets. Select at most 128 undirected collision words of native
length at most 4096, with their inverse directions.

For t=+2, repeat the same at-most-32768-steps-per-side walk scheme under
the collision bank, alternating source restart blocks among the retained
at-most-eight roots and sharing the target side. An actual meeting
supplies c and identifies its bridge b. The expanded candidate is W38 a b c.
Its maximum expanded elementary length is 100000. The complete five-input
forward/inverse audit is mandatory before a construction is reported.

The global search budget is 100000000 logical elementary contact
applications, counted independently of cache hits. The verifier checks
cost before an application; deterministic exhaustion is a completed
INCONCLUSIVE outcome. Mandatory final certificate audits are separate
from the search budget. A reduced bank, capped walk, absent collision or
unaffordable candidate cannot produce a full-bank no-go.

For selection, retain at most 4096 short zero-Schreier candidates in
increasing (expanded native length, chronological word lexicographic)
order, then at most 256 undirected loops with distinct observed actions
on the four remaining source/target states. This fingerprint is only a
heuristic diversity filter, never a claim that equal fingerprints mean
equal group elements. The complete Schreier family stays certified by
the whole zero tree and edge graph.

Keep at most 2048 short target-side collision candidates, selecting at
most 128 undirected loops by the same length/word ordering and observed
action on the first retained +2 source and its target. Keep at most 64
short stage-B bridge words before selecting up to eight distinct +2
roots. The exact finite ordering and canonical undirected representation
are implemented in verify.py and are part of the accepted code.

The zero Dijkstra queue is ordered by (distance, canonical 24-byte state,
state IDs). Equal distances keep the first predecessor, and original
macro IDs are traversed in fixture order. The undirected representative
is the lexicographically smaller reduced word or reduced inverse. Both
directions must satisfy the respective 256 or 4096 length bound.
Seen walk states retain the least (requested native path cost, source
root index, program-ID path). This makes all path and selection ties
explicit and independent of wall time.

The two xorshift64* seeds are 0xd1b54a32d192ed03 and
0x94d049bb133111eb; the multiplier is 2685821657736338717.
All arithmetic is integer with explicit 64-bit masking. An immediate
inverse proposal advances one bank index. Walk sides alternate and use
no wall-clock decision. Run-length contact programs combine only valid
adjacent powers of the same edge modulo five; their logical cost remains
the expanded number of forward elementary contacts.

The seven-stock audit has separate frozen caps: 256 states per small
orbit and 64 values in each alphabet category. Its six explicitly listed
Q15 stocks have exposed 13-state forecasts. It prints each actual positive
orbit, audits the swapped negative orbit, all 15 outgoing edges of every
state of both signs, both arithmetic routes and complete C^5 cycles.
The seventh stock is 2(j^2-j^4). Its exposed forecast is an alphabet of
15 neutral and five charged values; the actual lists are printed. All
375 ordered NN, NR and RN pairs are audited, with budget thresholds 45
and 48 respectively. Both signs require the excluded u+B. Distinctness
and nonmembership in the previous 124 exclusion classes are checked.
Failure of an exposed forecast is an explicit falsifier, not a reason
to alter the source. The supplied full census is not rerun or accepted.

## Systematics and exact checks

Different input-dependent admission histories are permitted. The program,
preparation and complete target contract are fixed. A direct scalar
arithmetic route checks an independently coded quotient representation;
all final forward and reverse word steps are audited. Summed Q alone is
not a substitute for full endpoint equality or full complex invariants.

The macro input is bound by hash; IDs, inverse map and words are checked.
All selected return words have explicit paths and are verified on every
state they promise to stabilize. Agreement on a root or a small sample is never treated as proof of
generator equality or preservation of the full stabilizer. Heuristic
omission during the declared selection is allowed only as selection of
a subgroup, with no full-stabilizer completeness claim.

The secondary small-stock audit prints explicit finite states and values
and audits every declared transition, so its exclusions can be checked
independently of a large census. This does not accept the entire external stock census.

## Failure thresholds and dispositions

Any mismatch in fixture custody, arithmetic routes, contact inverse,
invariant, claimed orbit closure or promised return is a fired verifier
failure. Preserve the run; never repair a pinned source or suppress it.
The declared search operation/state bounds are deterministic scientific
limits. Their exhaustion gives INCONCLUSIVE, not an impossibility or a
shortest-word claim. The separate small-stock caps belong to its exposed
finite forecasts; exceeding them fires that audit rather than reporting
a search miss. A complete no-target orbit decides only its explicitly generated
subgroup. It cannot exclude the full odd stabilizer without a separate
completeness proof.

Success requires one expanded chronological contact word from every I_t
to its exact G_t, including X and 2, with all five inverse recoveries.
Only actual completed certificates may be called complete. A found word
is not asserted shortest. Any mathematical no-go is conditional on the
fixed six-slot carrier and allowed contacts, not on arbitrary apparatus.

The external process timeout is 600 seconds, matching the existing
repository gate. It is operational and does not turn a timed-out process
into a completed negative result. The first author run uses a clean
Linux-compatible checkout of the public source pin with assertions on,
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and no bytecode writes.

## Custody, output and scope

Before execution record the full source commit and hashes, and verify
all source files through immutable public readback. Afterwards append
only EXPECTED.txt, RUN.md and RESULT.md. Preserve exact stdout, stderr,
exit code and neutral environment data. Both existing architecture jobs
must reproduce the same committed output bytes. No changes to source,
limits or fixtures are permitted after the pin.

This is L1 construction and finite verification. It provides no native
preparation bridge, bank-affordability schedule, autonomous controller,
physical time, Planck action, charge normalization or alpha prediction.
Same-session review is authoring review; promotion remains separate.
