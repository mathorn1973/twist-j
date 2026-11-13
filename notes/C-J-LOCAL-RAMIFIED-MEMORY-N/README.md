# Local ramified memory: encoding, circuits and latency

**NON-CANONICAL / candidate-T / L1 / proof-first / result-exposed.**
Author: A. M. Thorn <thorn@twistj.com>. Owner: [#1294](https://github.com/mathorn1973/twist-j/issues/1294).

The literal finite varpi-digit chain fails before a locality question arises:
with varpi=1-j and digits 0,...,4, even J times the one-digit value 1 has no
finite expansion. A different common finite alphabet nevertheless supports
exact ramified writing, J holding and finite-phase reading by explicit
reversible nearest-neighbour circuits. Their depth grows with the word length.

| Question | Written result |
| --- | --- |
| Do ordinary finite varpi words cover O=Z[j]? | No. Every nonredundant complete digit set containing zero has a nonzero fixed division cycle. |
| Are the 0,...,4 words closed under J? | No. The quotient orbit of J has an explicit six-cycle. |
| Can one finite alphabet represent all of O? | Yes. Four balanced base-five coefficient tracks, with digits -2,...,2. |
| Can ramified append be reversible and local? | Yes, on O squared: explicit unimodular charts reduce it to moving one balanced digit between two registers. Finite circuits retain the endpoint. |
| Can the same carrier hold by J? | Yes. Five integer shears, each compiled into local reversible carry gates with clean workspace. |
| Can the gate schedule be internal? | Yes. An explicit single moving head supplies an autonomous local reversible rule on the consistently marked one-head carrier. |
| Can a J macrostep take a fixed number of local ticks? | Not in this canonical coefficient encoding. An exact carry witness gives an unbounded causal lower bound. |
| How much clock is needed for reading? | Latest single ramified digit: phase modulo four. Full residue modulo five: phase modulo twenty. Both statements freeze their observation class. |

The positive result is an explicit scalable **family of finite circuits**
and a **uniform autonomous controller with one moving head**, for a selected
finite program, declared reserve width and ready workspace. The graph,
endpoint and side marks are inputs. Neither the selected rule nor those
marks are derived from native U. At each fixed width the complete machine
remains a finite permutation; it is not an unlimited permanent archive.

In particular, finite current phase does not recover an arbitrary history of
interleaved writes and holds. Occupancy, packet boundaries, write-relative
phase and instruction history are different resources. None is discarded
under the name of a zero digit or a completed arithmetic operation.

Read [PROOF.md](PROOF.md) for the constructions and inverses,
[PREREG.md](PREREG.md) for the exact comparison contract,
[REVIEW.md](REVIEW.md) for exposed proof review, and
[PROMO-C-J-LOCAL-RAMIFIED-MEMORY-N.md](PROMO-C-J-LOCAL-RAMIFIED-MEMORY-N.md)
for the limited promotion boundary.

This follows [PR #1293](https://github.com/mathorn1973/twist-j/pull/1293)
without depending on its unmerged files. The proofs here are self-contained
apart from the named v94 unit/residue facts, also derived at the used scope.
No scientific program was run. Administrative repository checks are not
computational evidence for these new propositions. Canon and all live
physical obligations remain unchanged.
