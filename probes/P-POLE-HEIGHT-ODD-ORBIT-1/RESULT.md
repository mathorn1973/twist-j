# Odd-input loader obstruction: proof and completed orbit audit

NON-CANONICAL / L1 analytical candidate with a completed exact audit.
Each known odd input in the declared six-slot preparation cannot reach
the target. Therefore one common word loading all five inputs is also
impossible in that contract. This is a new result; sealed PR #1896 remains
its correctly scoped historical bounded non-finding.

## Analytical mechanism

PROOF.md establishes a closed alphabet independently of any census count:
neutral slots stay in N={0} union {j^a-j^b}, with Q=0 or 5, while the sole
charged slot stays in R={j^a+j^b}, with Q=3 or 8. The odd target needs a
Q=15 slot. No allowed contact can create it. The argument covers inverse
contacts, input-dependent or adaptive schedules, permutations and any
finite number of extra N-valued neutral helpers, including blanks.
It does not cover arbitrary neutral stock such as 2u, two charged helpers
and their mutual contacts, or a different operation alphabet.

For the six-slot odd input, total Q=28 forces at least five nonzero slots.
Reference positions 3 and 4 consequently cannot both become zero. This
occupancy statement is six-slot-specific; the Q=15 obstruction has the
broader N-helper scope above. Finiteness follows from positive Q and the
integer carrier, not from the order-five property of each generator alone.

## Actual complete finite audit

Source pin: 4c3a5aae1237c66e40798b18eb8bfb09dfc0e77a.
The first clean Linux run completed with exit 0 and empty stderr.
Stdout is 2941 bytes / 11 lines, SHA-256
dca5a40b9b68712f9ebe80ed35b54ac6a70a6dfb1ffafecdb3558a9fa058099c.

| Input t | Complete states | Forward radius | Targets | Shortest target lengths by helper phase k=0,...,4 |
| --- | ---: | ---: | ---: | --- |
| -1 | 1480 | 25 | 0 | none |
| +1 | 1480 | 25 | 0 | none |
| 0 | 110 | 14 | 5 | 10,11,12,13,14 |

For every input, the power-basis elementary BFS and the separately
implemented quotient-arithmetic macro DFS produced equal complete state
sets. Every reached state's conservation and alphabet membership passed;
every elementary edge was checked for closure and inverse recovery.
Predecessor paths and all-edge inequalities certify the reported shortest
forward-contact distances. Both traversals exhausted their frontiers;
no state or runtime cap was reached.

The local audit checked 1071 ordered pairs through all five powers in both
representations. The complete orbit audit checked 46050 elementary edges
and the secondary traversal visited 184200 macro transitions. All five
neutral slots in each odd orbit had precisely Q values {0,5}; the last
slot had {3,8}. The count with reference positions 3 and 4 simultaneously
zero was 0 for each odd orbit and 13 for t=0.

A shortest t=0 word restoring both helpers is

    C_16^3 C_36^2 C_26^3 C_46^2.

The expression is written in chronological order, left to right. Appending
C_56^k gives the other four recorded shortest targets. EXPECTED.txt contains
the exact elementary words, full distance histograms and sorted-state
hashes. Each word was replayed in both representations and reversed with
four forward contacts per inverse. Only k=0 restores the helpers exactly.

All exposed review comparisons matched. Their numbers were never used as
stopping counts. No reviewer script was executed or imported. The supplied
even-input million-state census, enlarged-helper counts, 17/20-contact
paths and second-charge sufficiency/minimality were not verified by this
probe. The new alphabet proof does independently cover arbitrary extra
blank helpers, rather than only the two finite examples in the review.

## Status and remaining boundary

An independent acceptance or Canon promotion is not asserted. Two code
routes within this session are arithmetic crosschecks; architecture replay
is separately reported after its actual completion. The six pinned source
files are unchanged; only EXPECTED.txt, RUN.md and RESULT.md were appended.
No prior probe, Canon file, policy, workflow, registry, tag or release changed.

To escape this proven obstruction, a new construction must leave the
one-R/all-other-N contract. A second charged cell is one proposed route,
not the only resource change excluded from the theorem's premises. A
common seven-slot loader remains open. Physical charge, calibrated action,
electron identification and alpha are not consequences of this L1 result.
