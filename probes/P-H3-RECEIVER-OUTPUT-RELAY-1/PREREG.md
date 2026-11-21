# A third receiving cell for the two native H3 output words

The public base for [claim #2052](https://github.com/mathorn1973/twist-j/issues/2052)
is 5b09d042dacd8a48d812264f117afe796645a95e.
The authority is Public Canon v115, content commit
6cd898bc6d35f339b471ea684486af8c0ac54f84, normative Canon SHA-256
38afba3f5c815aa1c623f8cec9992f0e5f89659e493e85dc61054e8fdfa253cf.
The fixed starting observations come from
[P-H3-DOUBLE-RENEWED-TRANSFER-1](https://github.com/mathorn1973/twist-j/pull/2049).

The primary question is retrospective. Before public registration, a separate
local reproduction of the sealed #2049 Python witness retained the full
post-B fields at its two original reads. Its stdout matched the published
full-witness digest. Substitution into C and B from those fields showed that
both first contacts at 3 refuse both material rails. Cell 2 overwrites the
first word by B2 and the second by B1 in those same ticks. These two outcomes
are known controls. The secondary scan for other occurrences on rank 43
has its own fixed predicates and ceiling below. It has not been run.

## 1. Equation and decision

On the original rank-43 orbit, follow each exact ordered material pair
emitted by cell 2 at the two fixed B events in the table. Determine its
first material-changing substep while the pair is still held at cell 2.
A successful relay is a C contact from 2 to 3 that changes the ordered
material at 3 while the original ordered output is still present at 2
immediately before that C. The B tag at 3 is recorded at a successful
relay. The tag places no additional requirement on success. The two
relays must reach the same cell 3. Its pre-C material, radiation and
resulting B tag may differ between the two encounters.

| Arm | Earlier B2 at writer 1 | Repeated B2 at writer 1 | Matched read and material write at cell 2 | Output first rail at cell 2 |
| --- | ---: | ---: | --- | --- |
| 1 | 7316785 | 7390473 | 7390475 B1 | (1,-1,0,1) |
| 2 | 8176761 | 9915381 | 9915383 B2 | (1,0,1,2) |

The two outputs are ordered antipodal pairs (w,-w) in the power basis
(1,j,j^2,j^3). At a bit-0 contact, cell 2 is the first endpoint and
cell 3 the second. For an ordered rail value w at cell 2 and resident
rail r at cell 3, the new value at 3 is
((1+rho)r+(1-rho)w)/2 if r and w agree coefficientwise modulo 2, with
rho=j^2. Otherwise both endpoints retain their values on that rail.
An admitted equal-value contact is stationary. A moving contact changes
the corresponding rail at both endpoints.

The two known first rails have distinct residues (1,1,0,1) and
(1,0,1,0) modulo 2. All four cells in column 0 start with antipodal
material rails. C applies the same oriented matching to both rails and
respects simultaneous negation, including refusal. B preserves their
midpoint. Consequently each bit-0 encounter accepts or refuses both
material rails in this column. The two given words cannot both move the
same resident pair, while distinct residents at the same cell can have
the required respective parities. This fact concerns optional equal
third-cell material. The test observes the same third-cell index and its
actual resident values at the two times.

## 2. Accepted code and output

Run from the repository root with Python 3 and a C++20 compiler:

    python3 probes/P-H3-RECEIVER-OUTPUT-RELAY-1/verify.py

The driver, native scan in relay.cpp, and five-coordinate confirmation in
confirm.py are fixed before the first formal execution. The driver checks
the pinned predecessor and launch sources, compiles the scan, and
validates and serializes its exact output. The native ABI supplies one
SCAN record, two fixed CERT and RELAY records, and any required FIRST3
and STOP TRACE records for each reported arm. If the fixed pair fails
and a qualifying alternative is found, two more arms use the same ABI.
A relay record identifies the originating read, terminal tick and
substep, terminal site, target-contact count and refused-rail count,
first target attempt and its admission and movement counts, terminal
target movement and the target B tag. Each trace gives the two contact
endpoints before and after the reported cut in exact integer
coordinates. The scan record gives the ceiling, executed ticks, source
recurrences, eligible reads and target relays by branch, and the
remaining held count by branch.

## 3. Carrier and finite search

Use the original ordered 85-launch four-wire family with SHA-256
8e65f16a2f545c566c3b2fa915fd993f3fd0e78644a17b12567a42ccc434c4cd.
Execute only its rank-43 field, on the 8 by 4 periodic lattice with the
original matching bit one at tick 1. Apply native C then native B, and
toggle the bit once per tick. The complete field and current bit
determine each update. No word, relay state, or source data are inserted
into the evolving field.

The fixed input to each relay is the complete #2049 witness with the
prior, emission, and read ticks shown above. Continuity requires the
ordered pair to equal the actual output at cell 2 on every prior
intervening C and B cut and immediately before the terminal C. A change
followed by the return of its values ends the original hold. For a
secondary search, consider the same rank, writer 1, reader 2, bit-1
first hop and third cell 3. Each source is a material-changing native
B2 whose complete signature matches an earlier qualifying emission on
this orbit. The signature comprises writer, matching, all four pre-C
writer rails, ordered upstream donor material, incoming post-C
radiation and ordered output material. At both source occurrences C
changes material at the writer and its upstream donor. Between emission
and the first hop the ordered source word stays intact at the writer.

At both first-hop reads, C changes both material rails at cell 2 and B
changes its ordered material. The two candidate reads must share all
four pre-C rails and both post-C radiation rails, choose opposite B1
and B2 branches, and have distinct emitted source words, material
arrivals and B outputs. Both receiver output words must then reach
cell 3 by changing its material before either word loses provenance.
The requirement of equal readiness applies to the first-hop reader 2.

Use the ceiling 2^26 = 67108864. Track the secondary candidates from
the beginning of the same forward scan. For a common first-hop
readiness and branch, keep the earliest completed target relay of each
distinct triple of source word, cell-2 arrival and cell-2 output. At a
new completed target relay compare against earlier compatible
representatives of the opposite branch in insertion order and retain
the first qualifying pair by completion time. Report the fixed result
first. After both fixed outcomes are resolved, stop if the fixed
pair succeeds or a qualifying alternative is available. Otherwise
continue through the ceiling. A word held at the ceiling is reported
as right-censored. The finite negative outcome applies only to the
specified predicates and executed window.

## 4. Systematics and independent confirmation

The first change at C resolves the relay at that mating endpoint. A
bit-1 contact with site 1 can end the hold without a third-cell relay.
After a stationary C, the first B change at cell 2 resolves the relay
as a local overwrite. Record the exact cell-2 and target cut at the
first bit-0 attempt, including refusal, and the exact terminal cut at
the mate or at the horizon. The outcome of an earlier stationary
contact does not decide a later contact while the word is still held.

Use the conserved launch account M=(-9,2,-2,-3), U=(19,7,5,19),
H=(463,0,152,152), Q=774. The native scan checks complete accounts and
C/B inverses at the recurrent writers, eligible first-hop events, first
target attempts and terminal changes. Rewind the full scanned prefix
and recover the original launch and matching bit.

The independent five-coordinate Python check verifies the reported
source and receiver collisions, ordered C projections, per-rail
admission and movement, first-hop matching and terminal relay
predicates. After preserving the formal output, the full-witness mode
replays the original rank-43 field to the latest selected terminal
cut. It checks the earlier B2 signatures, every intervening cut of
both holds, the complete target-attempt and refusal counts, and the
first terminal change or exact horizon. Report local checking and a
completed full Python history replay separately.

## 5. Failure threshold and controls

One exact contradiction invalidates the affected certificate: a
changed fixed #2049 event, missing earlier recurrent signature,
nonmoving upstream endpoint, a break in a required hold, inconsistent
first-hop readiness or branch, material movement on a refused rail,
stationary target reported as moved, a prematurely or belatedly
terminated trail, mismatching counts at its actual prefix, ledger
disagreement, or failed inverse. A failed input pin, compile or runtime
failure, incomplete execution, or nonmatching architecture stdout
without a mathematical counterexample is STOP. A completed scan that
finds no qualifying alternative is a finite measured result.

## 6. Action layer and custody

This is an L1 finite native H3 probe. Commit and push these input
files, read back the public pin and hashes, then run the formal
verifier. Preserve stdout byte for byte in EXPECTED.txt and record
command, input hashes, exit status and output custody in RUN.md.
Record the fixed outcomes and the disposition of the secondary search
in RESULT.md. Q9 remains open.
