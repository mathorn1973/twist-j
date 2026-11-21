# Result: full generator scan, verified three-input prefix, bounded miss

Status: NON-CANONICAL / L1. Exact finite audits passed on the first author
x86_64 run. Construction outcome: INCONCLUSIVE_COMPLETED_DECLARED_SEARCH.
No common-five word, full-stabilizer impossibility or minimum is established.

## Complete zero orbit and full generator family

The zero orbit under the frozen 64-direction K0 bank is complete:
1556 states and 99584 directed edges. Its maximum weighted tree distance
is 65, and the post-W38 zero residual belongs to the orbit. The complete
zero tree/edge certificate hash is
`3e427d2a5562b6036b79fc3f023fe420a026bbefadb29d860f50de7253537c7b`.

All 99584 Schreier descriptors were retained. They contain 3110 identity
descriptors and 96475 distinct structural programs including identity.
The complete direct pass started and completed the 96474 nonidentity
structural programs. No 4096-short-word pool, 256-contact cutoff or endpoint
fingerprint selection was applied. The largest generator expression has
180 expanded contacts. The complete family generates the zero stabilizer;
its one-generator root images are not the complete stabilizer orbits.

## Explicit three-input certificate

The DAG represents the zero bridge by 95 literal contacts. The expanded
W38 followed by that bridge has 133 contacts and was replayed separately
for t=-1,0,+1. Each exact six-slot target, including helpers X and 2,
passed both arithmetic routes and full invariants. Each literal inverse
used 532 contacts and recovered its original preparation. EXPECTED.txt
prints the complete program in ZERO_PREFIX_CERTIFICATE. This is a direct
three-input certificate, not a completed five-input witness audit.

The difference from the predecessor's 65-contact bridge is a representation
difference, not evidence of a worse minimum. The DAG retains adjacent
contact blocks across concatenation boundaries. Inspection of the printed
word gives the following exact C^5 reductions inside the bridge:

- C56^8 becomes C56^3;
- C26^8 becomes C26^3;
- C12^5 becomes the identity;
- C16^8 becomes C16^3;
- C56^12 becomes C56^2.

These remove 30 contacts and recover the predecessor's 65-contact bridge,
so the corresponding common three-input word has 103 contacts. Because
C^5 is the identity on admitted and refused branches, the compressed word
has the same complete endpoints and is reversible. This is a post-run
analytical compression of the printed certificate, not another program
execution. Neither 133 nor 103 is asserted shortest.

## Completed direct pass and preserved search miss

The full direct family produced 252 distinct minus-source images and
356 distinct minus-target images, including the initialized roots. Their
intersection was empty: no minus bridge was found. This completes the
declared direct test s.F=h.G for the single-generator family and identity.
It does not exclude meetings involving unrestricted longer products.

The direct target scan retained 192218 directed collision programs.
These are structural words; their count is not a count of distinct group
elements. The direct pass used 20936505 logical elementary contacts.

Both minus fallback sides then completed 32768 steps with restart depth
eight. Their accumulated image maps contained 705 source states and
1212 target states, still with no meeting. The collision bank grew to
249242 directed programs. These image counts are sampled path coverage,
not complete K1 orbit sizes. The finite target-collision family is not
claimed to generate the complete next stabilizer.

Total logical search contacts were 27761026 of 300000000. No work cap
fired, no bridge-root limit was reached and no overlong meeting was
reported. With zero minus bridges, the plus search did not start: its
maps contained only the initialized target identity, and no collision
image on a plus root or target was evaluated. The final five-input
forward/inverse witness audit was therefore not run. No omitted phase
is represented as passed.

Removing the predecessor's short-family selections did not produce a
bridge within this declared direct pass and bounded fallback. This does
not identify the cause of either non-finding. It excludes neither the
full zero stabilizer, K0, nor the full odd stabilizer. No complete K1
orbit was enumerated. Every source, ordering and limit remains frozen;
any successor requires a new prospective identifier.

## Custody and scope

Source pin: `82bb5e56f1559a9db12260745c0eb4c9ea445d89`.
Verifier SHA-256:
`30767524ea1e0b942d2351c320deef7ddc2a649ec66081ed2bc80207456daf68`.
All seven source files remain unchanged. The first clean pinned run
exited zero with empty stderr. Exact stdout has 3108 bytes and eight LF
lines, with SHA-256
`4a855bef5a2954edae41f1b41e509cdeea1cd94bce23105b674079dc3c873fec`.
Public source readback preceded execution. RUN.md records the actual
command and environment; repository checks and architecture CI remain
separate gates until their completion is recorded externally.

The predecessor's seven-stock exclusions remain separate and unchanged.
This probe does not reproduce the external even-orbit census, minimum38
claim or complete stock census. Its conditional orbit-size lemma is not
used to accept this run. No physical preparation bridge, funded schedule,
autonomous controller, action normalization, alpha prediction or Canon
promotion follows from this result.
