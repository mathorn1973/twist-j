# Reproduction of the existing B/C author and review programs

NON-CANONICAL. Prepared 2 October 2026. **New two-architecture execution is
pending publication approval; no new successful run is claimed here.**

The original #1328 and #1330 RUN records each report x86_64 scientific
execution. Their ordinary notes-only CI jobs were green on two platforms
but did not execute these scientific programs. The new reproduction
directories make the four unchanged programs visible to the existing
stock `tools/check_reproduce.py` runner. No workflow or timeout is changed.

| Program | Original immutable receiving pin | Original code SHA-256 | Original stdout SHA-256 |
|---|---|---|---|
| B author | `05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa` | `cc67d1fa3e2203cfc47498e10488ce02fdde5761b817509c2523fad5896ac883` | `386d9b9a1c801cc38b22aa04305ddf10dbe66a1cf38243e4f28e8686e0ed875f` |
| B independent | same B receiving pin | `d2aa61efa74bb26b323d9a940ac9269a8c7d1a561419869cf157abd14716467a` | `08bb207503943772e5c6e62b8f35fff1050d52decf654a280d30bc77feaeb000` |
| C author | `024936502544c2ec45acc8890a052c7b3aca26be` | `76f92f9b8fe0501f58d25bb16f3d066e3a0e5a39e01e80a1939657c88bd6bbcc` | `5ba56f3fa9036a0d5cc1fe13dba06250362850c3fbe38c6779c78fe106b694b1` |
| C independent | same C receiving pin | `da26e40b9bbfd2534d0bc3e530d88fa505d9143d0d0c9542bb0e4493aeea69fd` | `49bc7306bedebd523a7cfa7f886e4ab854c631cb7e7a31045f7bd4f4339b13b7` |

Each `reproduce/C-FIELD-J-.../verify.py` is byte-identical to its original
author `verify.py` or independent `break.py`. Each EXPECTED is the original
public stdout, not a new prediction produced from the replay. Static AST
and byte comparisons have passed; scientific code was not executed during
materialization. Author and independent stdout are distinct and are each
compared against their own EXPECTED.

After publication, the existing PR workflow must produce actual
REPRODUCE PASS lines for all four directories on x86_64 and aarch64,
with exit zero, empty stderr and exact stdout. The evidence receipt will
name the workflow run, both jobs, tested PR merge SHA, head/base pins,
source hashes and output hashes. A green aggregate without those lines
will not be credited as completion. No theorem changes status merely
because the same audit passes on a second architecture.
