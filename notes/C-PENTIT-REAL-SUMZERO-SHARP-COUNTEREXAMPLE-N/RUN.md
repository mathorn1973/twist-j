# Exact confirmation audit and custody

**NON-CANONICAL / L1. One local x86_64 confirmation of exposed targets.**
Date: 2026-10-02. This is notes incubation, not a formal public-probe gate.

## Public pin and execution order

Input main: `01821412879dba442e1c864c61855fb4a4dfea99`.
Object lock: #1344.
Public preregistration/verifier/proof pin:
`fd41b1cb5662983a34742829807d9c510014242c`.
Pinned Git tree: `ef61af43d499c5b4150d91716c4c088747f04390`.

The four files below were committed and pushed, then fetched again through
the public GitHub file API at the exact commit. Returned Git blobs and full
UTF-8 content matched the proposed bytes exactly, 4/4. Only after that
readback did the first new scientific execution occur. No verifier import or
execution preceded the public pin; earlier AST parsing and file hashing were
static checks. Analytical targets were already exposed, as PREREG records.

| Frozen file | Bytes | Git blob | SHA-256 |
| --- | ---: | --- | --- |
| PREREG.md | 5802 | `510b2a36310b2bc1bf9dae55c4b9070a9580189b` | `8045eeae7d8f36be688df1b301c0749c7da64a1082cd45d6e4f1514973f09954` |
| verify.py | 9849 | `2bfa12c1e7cdaa35f9775da1c5103feb96fb8abf` | `40c09412631014aae23eb18715b49c9556ee2211d3f7bda10675f1669fc855e1` |
| PROOF.md | 4426 | `9b46aaa6b3d3ecf2bfc8ba78974da2734d0c45f0` | `3e7c3907b461e461d6f3b08c05fd39d7b1cb918c77f6cc3c4c6e6db3f59781c3` |
| LOWER-BOUND.md | 6211 | `3916cc24d0e108593524f7d066b8cb8d23215a6a` | `c1f26feee3ca960c6ac678877aed943c878b74d8a80322ee04c8804543db7762` |

## Environment and command

Platform: Linux. Architecture: x86_64. Interpreter: CPython 3.12.14.
No third-party runtime dependency. Public-pin files were materialized at
their canonical repository-relative paths in an isolated working root.
This was a byte-verified source materialization, not a full Git checkout or
a local replay of the repository policy/Canon test suite. The verifier reads
no runtime files, authority context or datasets.

From that working root:

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PENTIT-REAL-SUMZERO-SHARP-COUNTEREXAMPLE-N/verify.py \
  > notes/C-PENTIT-REAL-SUMZERO-SHARP-COUNTEREXAMPLE-N/EXPECTED.txt
```

Exit code: **0**. Exact scientific assertions: **148/148 PASS**.
The execution tool returned no error text. All four frozen files were
rehashed after the run and retained their exact pinned bytes.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| EXPECTED.txt | 361 | `a5df30dac7256d9894ec99268faca3885fa2bf4091292c4bf98e1d7ac5e1f64f` |

Stdout Git blob: `dc29b8ac772adbf0405971b4616271b72d3edc9d`.
The exact stdout is the committed `EXPECTED.txt`; no reconstruction from a
summary was used.

## Limits of this receipt

There was one scientific run, on one local architecture. There is no
second-architecture execution or independent second implementation here.
Notes-only GitHub architecture/check jobs validate repository policy and
their normal selected checks; they do not automatically execute this note's
verifier. Their success must not be reported as a scientific replay of these
148 assertions.

The software confirms the exposed witness and exact identities. The
universal lower bound is established by the separate analytical proof and
its same-session independent reasoning review, not by this finite run.
Neither result changes public Canon authority or supplies a native
occurrence/renewal/preparation mechanism.
