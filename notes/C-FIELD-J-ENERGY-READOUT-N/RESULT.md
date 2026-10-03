# Field/J interface: accepted mathematics and rejected Python contract

PUBLIC, NON-CANONICAL. Overall original implementation contract: REJECT.
The separate mathematical statements below have accepted scoped proofs.

Basis: Public Canon v96, `44423153eee6259c7277eec5f5adbed9679f9146`.
Author freeze: `49dfad177c6ab698b5751de3e56629508982b05f`.
Reservation [#1323](https://github.com/mathorn1973/twist-j/issues/1323).

The independent reviewer froze its derivation and breaker at
`c404c1c53a9af3ce1b2523de8a56a270e082e7c9` before opening the author proof,
code or outputs. Its final [review](https://github.com/mathorn1973/twist-j/blob/155dd04446564df7fddbb78996a3ad82231b595d/notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/REVIEW.md)
preserves the implementation failure and distinguishes it from the mathematics.
Known historical counts and ratios were disclosed; review was implementation-blind,
not result-blind. Both originals remain unchanged.

| Frozen claim | Disposition |
|---|---|
| A: all-integral chart, J, energy and trace identities; conservative Af versus virtual Jf | ACCEPT, scoped candidate-T proof |
| B: containing box, norm bound, mathematical unique inverse and complete census | ACCEPT, scoped proof plus candidate-C finite census |
| B: positive Python tuple-input contract as implemented | REJECT: exact valid tuple-subclass inputs falsely reject |
| C: equal-energy source pair with fixed-context LOW ratios 0 and 5/16 | ACCEPT, mathematical comparison only |
| D: unchanged positive chain receiver blindness at every time and actual substep | ACCEPT, induction for every N>=2 and all H(w)=1 seeds |

The concrete contract counterexamples are:

```python
class T(tuple):
    pass
outer = T((0, 0, (0, 0, 0, 0)))
inner = (0, 0, T((0, 0, 0, 0)))
```

Both satisfy the frozen positive syntax and represent stored zero. The
author's exact-type guards return None. This source-level counterexample was
found after review freeze; it was not included in either original finite
audit. Passing those audits therefore does not discharge the failed contract.
No after-the-fact interpretation excluding subclasses repairs this pin.
The separately reserved C-FIELD-J-TUPLE-READER-N successor must earn its own
verdict before the full interface is accepted for downstream work.

Actual runs: author `python3 notes/C-FIELD-J-ENERGY-READOUT-N/verify.py`,
independent `python3 notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/break.py`.
Both ran from clean exact public pins on Ubuntu 22.04.5 LTS, x86_64,
Python 3.10.12, timeout 600 seconds; exit 0 and empty stderr. Their RUN.md
and EXPECTED.txt preserve exact hashes and outputs. The author checked
52500 ordinary typed keys; the reviewer checked 143125 and 76920 raw-chain
boundaries. The universal proofs are not inferred from finite trajectories.
No second-architecture scientific execution is claimed; ordinary notes CI
does not execute these verifiers.

The accepted source distinction remains classical algebra. The complete
receiver tuple and pointer are blind only on the specified unchanged v96
positive preparation family. Arbitrary preparations and all alternative
apparatuses are outside that negative theorem. The norm-941/3125-label
codebook retains its separate modulo-25 interface.

FIELD-CONSERVATIVE-CHAIN-LAW, FIELD-CHAIN-FIRST-WORK,
FIELD-LOCAL-WORK-RECORD, J-TWO-TRACE-RESIDUE-INVERSE,
J-OBSERVED-SCALAR-CODE-CAPACITY, U-NORMALIZED-SCALAR-READBACK,
QDD-GALOIS-SUM-RATIO and U-COUNTER-REACHABLE-AMPLITUDE-CLASS retain their
existing status. No physical dictionary, coherent instrument, native-U
selection, occurrence law or L2-L6 lift is obtained. No Canon promotion,
registry, policy, workflow or release change is made.
