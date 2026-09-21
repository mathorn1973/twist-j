# Public acceptance: selected outgoing TT state

PUBLIC; NON-CANONICAL. P-TT-SELECTED-OUTGOING-STATE-1 / ETH-TT-1.
Accepted at the frozen conditional L1 scope. This is not a Canon release
or physical validation of the selected state.

## Immutable result-stage evidence

- Lock: [#1097](https://github.com/mathorn1973/twist-j/issues/1097).
- Pull request: [#1098](https://github.com/mathorn1973/twist-j/pull/1098).
- Base main: `1d3e70433f850d03aa210374d8cda16dd97a0c10`.
- Pre-execution pin: `6257dfaae9132ef2a2a49ec06300775287d595db`.
- Accepted result head: `521b088042219c6ed6d25d2947e5010406c83c4d`.
- Accepted result tree: `2206548b26289c43cf24d8e20f8547773336c2e7`.
- Public workflow: [35535272952](https://github.com/mathorn1973/twist-j/actions/runs/35535272952).
- [x86_64](https://github.com/mathorn1973/twist-j/actions/runs/35535272952/job/106143062899): success.
- [aarch64](https://github.com/mathorn1973/twist-j/actions/runs/35535272952/job/106143062874): success.
- [aggregate check](https://github.com/mathorn1973/twist-j/actions/runs/35535272952/job/106143136449): success.

Both architecture job logs were read. Each contains this exact replay line:

```text
VERIFY PASS P-TT-SELECTED-OUTGOING-STATE-1 8cc1b45f70c71037cdade0046e4ae3d485cd5053293cf907ef14a66d66ff2002 dc1e909f2934f7fe3095875d21b374fa79afde6aa6c104d263aa86b6e43c0fc4
```

The committed EXPECTED is the unchanged first completed local stdout:
1125 bytes, 11 lines, all ten gates PASS, exit 0 and empty stderr. The
six preregistered files remain byte identical to their public pin and
the hashes in RUN.md. The three result records were read back exactly
from this result head.

| Result record | Bytes | SHA-256 |
| --- | ---: | --- |
| `EXPECTED.txt` | 1125 | `dc1e909f2934f7fe3095875d21b374fa79afde6aa6c104d263aa86b6e43c0fc4` |
| `RUN.md` | 3648 | `ca495f6f62d737d65fa90d3d918cab3358f4aec5e7938924be161e642fa25c7d` |
| `RESULT.md` | 12290 | `fd218cfa520f1a775320d76fb9ec3704c2297e3f1d1cf0d4e74387bb5c02d174` |

## Preserved earlier metadata failure

The first result head `9a818bca959f7330c70c78249edcbfb98b576c05`
has a failed public workflow
[35535183741](https://github.com/mathorn1973/twist-j/actions/runs/35535183741).
Both architecture jobs stopped before scientific replay because the RUN
command field said `python` while the checker requires literal `python3`.
RUN.md documents the correction and the verified identity of both aliases
with the first local invocation's Python 3.12.14 executable.

Only neutral RUN/RESULT text was corrected. No preregistration, model,
proof, review, verifier, expected output or threshold was altered.
The first local scientific execution had already completed successfully;
this is neither an abandoned pin nor a changed scientific verdict. The
failed metadata check remains in immutable history. Fresh public checks
on the corrected head are the accepted evidence above.

## Review and limits

The independent reviewer derived the state, moments, all-counter
nonvanishing and positive-denominator results without reading the new
verifier, then checked MODEL, PROOF, PREREG and the fold proposal. A separate
post-run review checked result records, frozen hashes, the exact transcript
and the neutral metadata correction. Local policy, 172 tool tests, Canon
437-claim validation, ledger and gate checks passed.

The finite audit covers m=0,...,10; its 55x55 point-pair checks and exact
spectral certificates do not substitute for the all-counter written proof.
The selected state is complete at its stated L1 scope, with two supplied
persistent signs and a declared composite-intensity comparison. It does
not close the physical scalar comparison by renaming R_TI as cosmological
r_T. The full normalization owner and all proposed physical gates retain
their stated open scopes.

Canon v90, its entire canon/ tree, STATUS, workflows and tools are unchanged.
A future Canon fold is separate. This record accepts the immutable result
head above. The neutral descendant containing this acceptance record must
itself pass fresh required CI before merge. Its final-head and merged-main
readbacks belong to the linked pull-request body, avoiding self-reference
or a claim here that those later checks have already run.

