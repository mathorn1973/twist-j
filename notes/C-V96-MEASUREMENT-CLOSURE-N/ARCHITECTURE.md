# Reproduction of the existing B/C author and review programs

NON-CANONICAL. Completed 2 October 2026. **All four unchanged scientific
programs passed on x86_64 and aarch64 against their original exact outputs.**

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

## Actual two-architecture receipt

Public PR [#1337](https://github.com/mathorn1973/twist-j/pull/1337), workflow
[37019597956](https://github.com/mathorn1973/twist-j/actions/runs/37019597956),
completed successfully on 2 October 2026. Both job logs contain all four
`REPRODUCE PASS` lines with exactly the code and stdout hashes above.

- Head: `8ad9a1dca98900feb696bc9dfe4efa8e8c054118`.
- Base: `62db6065988ed1fbbd15a46fa3c2902339e6e700`.
- Actual checkout (PR merge): `31b688203fcb0c581d9dc2cd094ce6b220e95048`.
- [x86_64 job 110878952421](https://github.com/mathorn1973/twist-j/actions/runs/37019597956/job/110878952421).
- [aarch64 job 110878952501](https://github.com/mathorn1973/twist-j/actions/runs/37019597956/job/110878952501).
- CPython 3.12.14 on both standard GitHub-hosted Ubuntu architectures.
- Stock runner: `python tools/check_reproduce.py --base BASE_SHA`.
- Exit zero, empty stderr and byte-identical stdout are required by that
  runner for every PASS. Author and independent outputs each matched their
  own immutable original EXPECTED. The aggregate `check` also succeeded.

The source and expected-output bytes were unchanged for this run. This
closes the missing architecture audit for the B and C programs. It does not
transfer a theorem between machines, derive an occurrence law or itself
promote the scope/status of any claim.
