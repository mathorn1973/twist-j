# Local pre-execution freeze

Status: NON-CANONICAL, candidate-T proofs / candidate-C finite audits, L1.

Joint pin UTC: `2026-10-08T22:23:09.200354+00:00`.

The specification was frozen at 2026-10-08T22:11:34Z. T7 was added by hand before this joint pin, with the original specification unchanged. Both scientific sources, the proof, separate text review and custody wrapper were complete before this pin. No scientific program had been executed or imported. Only metadata hashing, source inspection and AST syntax parsing preceded this record.

This is a local research pin. It is not a public preregistration commit, formal probe pin or public computational gate. No GitHub write is part of this record.

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 13958 | `58b8e76488c0eda439407b8e52ee667dfb33ba7ffab6c88dada2a7f30c6470d1` |
| ADDENDUM-READOUT.md | 3979 | `d9ada337b321f16659ead0ee0dcc76ae25efdc229f18ad4d24ef23e4cdc23320` |
| PROOF.md | 19809 | `b6f389ed5b476fee7dc07aed939e599968b25e166fe3e350a854539cd86f6e34` |
| REVIEW.md | 12690 | `f2ff2455a00f84ea3307220bbe2e3e6acb5228275c29e2a7ec8b592e36fbdf21` |
| verify.py | 30302 | `309162881f0f66e124919b867f54b2f47b78c8d51ac35d652a29dcbea09a6340` |
| break_check.py | 34311 | `c02319e5a43a70daca464b73fa909a599ba7e0ff1c4f504b07c58163eb2498b6` |
| run_once.py | 3806 | `756faa724875907e894fde5dc15d2e4f47e44afd5248d2c5181e242b6f112f0e` |

`run_once.py` checks every pinned file before and after execution and refuses to overwrite first stdout, stderr or run metadata. The two audit programs use separate processes and output files. First failures or timeouts must be retained, not overwritten. The frozen budget is 300 seconds per program.
