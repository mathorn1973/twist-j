# Confirming the extended search for a third H3 receiver

[Public claim #2054](https://github.com/mathorn1973/twist-j/issues/2054).
Public main at registration is 68812464c5566613b1000110e556968c9775fa95e.
The authority is Public Canon v115, content commit
6cd898bc6d35f339b471ea684486af8c0ac54f84, Canon SHA-256
38afba3f5c815aa1c623f8cec9992f0e5f89659e493e85dc61054e8fdfa253cf.

This is retrospective confirmation of the disclosed exploratory result.
The launch, window, comparison keys, reference and expected counts were
chosen and measured before this public pin. This registration fixes the
confirmation and its failure thresholds before public verifier execution.

## 1. Equation and decision

Follow the native directed material path 1 to 2 to 3. An eligible site-2
read receives a continuously held ordered word from a recurrent native B2
write at site 1. The earlier and repeated writer episodes have the same
writer, bit, four pre-C writer rails, ordered upstream donor material, two
incoming post-C radiation rails and ordered output material. Both upstream
C contacts change material at both endpoints, and both B2 operations change
the writer's material. At the read, bit 1 selects 1 to 2, both receiver
material rails change at C, and native B1 or B2 changes the material at 2.

Follow the resulting ordered pair at cell 2 through pre-C, post-C and
post-B cuts until its first material change or the ceiling. A first change
at bit-0 C on 2 to 3 is a delivery if it changes the recipient's material.
A first change at the bit-1 C contact with 1 or at B on 2 terminates this
hold without delivery. A word still held at the ceiling is right-censored.
A later restoration does not restore the earlier word's provenance. The
ensuing B at site 3 is recorded where relevant and can be B0.

Readiness is the ordered key (four pre-C rails, two post-C radiation rails)
at site 2. A compatible pair has equal readiness, opposite B1/B2 branches,
two deliveries to site 3, and distinct ordered source words, post-C
arrivals and post-B outputs at site 2. Site 3 is the same cell at both
contacts and may have different resident values. Only B1 reads in
67108864 < t <= 1073741824 enter any pairing decision. Compare them with
the fixed B2 reference, with all successful B2 reads in the published
prefix, and with all successful B2 reads through the ceiling. The wider
comparison permits either read to precede the other.

The fixed B2 has earlier source tick 8176761, repeated source tick
36442231, read 36442233 and delivery 36442234 C. Its readiness in the
basis (1,j,j^2,j^3) is

    (2,2,2,2), (-2,-2,-2,-2), (4,2,4,2), (3,2,0,4),
    (4,2,4,2), (6,2,2,4).

The ordered source, arrival and output matter on this arm are the pairs
with first rails (0,-2,0,-2), (2,-1,1,1) and (1,0,1,2), respectively.
Each second rail is its first rail's negative. At the first 2-to-3
contact both rails are admitted and change. The site-3 first rail goes
from (-1,0,-1,0) to (0,1,0,2), and site 3 selects B0.

## 2. Code and carrier

Run from the repository root with Python 3 and a C++20 compiler:

    python3 probes/P-H3-RELAY-CONTINUATION-1/verify.py

The driver compiles the exact integer native scan. Its implementation may
optimize the existing C and B maps. It keeps the original matching,
collision predicates and order of substeps. It validates source pins and
records the observed coverage and fixed-reference checks.

Use the original ordered 85 four-wire launches with SHA-256
8e65f16a2f545c566c3b2fa915fd993f3fd0e78644a17b12567a42ccc434c4cd.
Only the rank-43 field is evolved. Start from that field on the 8 by 4
periodic lattice with matching bit 1 at tick 1. Apply native C then B
and toggle the bit each tick. Compute from launch through tick
1073741824, including the published 67108864-tick prefix of
[#2053](https://github.com/mathorn1973/twist-j/pull/2053). The driver
follows the observed native evolution without any prepared substitutions.

## 3. Systematics and confirmation targets

The published prefix contains 153059 recurrent writer episodes,
554 eligible B1 and 159 eligible B2 reads, and 102 B1 and 13 B2 deliveries.
Its published fixed-pair and alternate-pair dispositions are negative.

In the continuation, the disclosed counts are 6940 eligible B1 and 2852
eligible B2 reads and 702 B1 and 188 B2 deliveries. The expected count of
still-held words at the ceiling is zero. The 13 historical B2 deliveries
and 188 new B2 deliveries provide the two chronological pools for the
broader comparisons. Assign a delivery to the interval of its originating
site-2 read, retaining the actual terminal cut and any ceiling censoring.
All three pair comparisons are expected to be empty.

Separately count bit-1 contacts 1 to 2 after the prefix where the site's
four pre-C rails, and where its full six-word readiness, equal the fixed
reference. Count these at the contact layer before imposing any recurrent
writer, material-change or B-branch filter. The expected pre-four and
six-word counts are both zero. This tests absence of the basic fixed
context separately from absence of a qualifying successful B1.

The conserved launch account is M=(-9,2,-2,-3), U=(19,7,5,19),
H=(463,0,152,152), Q=774. Match the final full field independently
obtained in the exploratory work. Serialize the 32 cells in site order,
each with its four rails in kernel order and each rail's four decimal
coefficients in the j power basis. Join the resulting 512 integers by
one ASCII space and append one LF. The expected SHA-256 is
b05fee6196a0be63a6ab150a2db111114633a66a8c74dc76c8945964c1c7acfa.
This pin checks the final field, while branch, readiness, provenance and
population checks address the intermediate history.

## 4. Failure threshold

Any exact disagreement in the launch, published prefix, fixed
certificate, branch or contact counts, full-field digest, or one of the
three pairing decisions rejects its corresponding confirmation target. A
candidate with an interrupted hold, unequal site-2 readiness, nonmoving
endpoint where motion is required, or an inconsistent C/B result fails
its certificate. A source-pin mismatch, compile or runtime error,
incomplete output, or architecture stdout mismatch without a verified
mathematical counterexample is STOP. A completed zero census concerns
only the specified finite rank, path, time window and predicates.

## 5. Action layer

This is a finite L1 computation. Q9 remains open.

## 6. Custody and reproduction

Freeze and publish the input files before formal execution and read back
the immutable commit and input hashes. Preserve the exact stdout as
EXPECTED.txt and record the command, hashes, exit status, stderr,
architecture and actual coverage in RUN.md. Record the confirmation
disposition in RESULT.md. Report the two architecture reproductions
with their actual hashes and status.
