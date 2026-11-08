# Ten-input variable-arrival apparatus: confirmation result

Status: PASS / NON-CANONICAL / L1 / candidate-C.

The exact public replay confirms the complete contract on all ten declared
inputs and their occupied continuations through ten steps and three events.
The construction was already exposed during incubation. This result is a
confirmation of a frozen public protocol, not a blind discovery.

## Frozen scope and execution

Pin: `77575d506ab28c1d3024b5212ede7b1bb87220da`.
All six scientific files were pushed and read back byte for byte before
the first formal execution. Their hashes and the local execution record
are in `RUN.md`. No pinned file changed after that execution.

| Obligation | Exact result |
|---|---:|
| Declared input preparations | 10 / 10 |
| Common auxiliary sites | 26 |
| Complete macrostep states | 100 / 100 |
| Complete read-end states | 200 / 200 |
| Designated events | 30 |
| Complete trajectory inverses | 10 / 10 |
| Forward/inverse contacts checked in both arithmetic representations | 267500 |
| Distinct ordered record pairs | 10 |
| Values of either individual record | 5 |
| Second-record alternatives for each first record | 2 |
| Initial and final labelled residue-vector classes | 1 |

The accepted verifier exited zero with empty stderr. Its exact scientific
stdout is the 7940-byte `EXPECTED.txt`, SHA-256
`4a03a48056bc18e724627eef17dd79ac518ee7bdb3e00a014e1b7da05e705dc0`.
The endpoint SHA-256 is
`a10212635f9c3a5079952aa7a46a24352f62c6506fcb43cc4c10295ea4d347e4`,
equal to the exposed incubation prediction. All full macrostep states hash
to `f93a5460597ad2a02fc91fdd693e75cb99270dee6ddb631ddb9d7ff6f70b8ae5`;
all full read-end states hash to
`5bf8b7777e46eab10acd850d373efaa4078913bad1c82d74a9f15517dc2b118b`.
The serializations are fixed by the pinned verifier.

The local run is x86_64. The repository's required workflow independently
replays the same pinned code against this same stdout on x86_64 and aarch64;
its two architecture jobs and aggregate `check` are the authoritative CI
record for the PR head. Two arithmetic representations inside this one
executable are a crosscheck, not two independently authored experiments.

## What the records establish

The first record is `pA=-k mod5`. The second is
`pB=-(k+Delta_n) mod5`, where `Delta_0=1` and `Delta_1=8`.
Thus their difference distinguishes the two admitted gaps, and their ordered
pair identifies the full input `(n,k)`. In particular, first record zero
has second record four or two. The second acquisition contributes a source
distinction absent from the first.

The source and receiver clock are separately prepared input registers of
the same complete carrier. No input-dependent operation word or later
external injection is used. The two initially fresh sets fund two retained
acquisitions. A third event takes the bypass. The complete final state
contains both archives, the advanced source and clock, and the restored
controls with selection A. Account remains 82 and the labelled residues
remain unchanged. The record distinctions occupy phases within that fibre.

The gaps are one or eight free clock increments, but 804 or 4011 primitive
contacts between the designated onsets, and likewise between completions.
No conversion to 535 or 4280 elapsed contacts is valid. The reading resolves
exactly the declared interval family; gaps one and six would alias.

## Falsifiers and limits

No prediction frozen in this public protocol fired. No input was removed,
threshold moved, or executable repaired after the pin.

The earlier reviewer's stronger single-site prediction about `g` was reported
false during incubation. It remains false and is explicitly recorded in
`PROVENANCE.md`; it was never a premise of the designated-onset contract.
The joint control state must be retained in the interpretation.

Retention is certified at every declared read and macrostep boundary,
not after every primitive contact. The positive horizon remains exactly
ten steps and three events. This replay does not test or promote the
exploratory claim of maximality beyond that horizon, permanent shutdown,
unbounded reuse, arbitrary arrival intervals, or post-start loading.

Together with the conditional composition argument in `PROOF.md`, the exact
finite result supplies a positive candidate witness for the existence clause
of `RELATIVE-CONTACT-COMMON-APPARATUS-OPEN` under the stated contract. This
probe does not itself edit or close the Canon registry row. Native-U
compilation, physical energy, physical realization and cross-layer claims
remain outside its scope. A Canon decision requires its separate review.
