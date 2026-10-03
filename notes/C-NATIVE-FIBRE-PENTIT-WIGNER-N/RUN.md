# Consolidated run record

**NON-CANONICAL. Status: PASS within the recorded scope. Action layer L1.**

## Basis and environment

[VERIFIED] Public Canon v97, tag `canon-v97`, main at
`738e0421bd15aaea5bb6ef2a56f1cab752d44de5`.
The publication currency check on 2026-10-02 found the same main, all five
Canon manifest entries valid, and no competing candidate claim.

[PIN] `reproduce/census/verify.py` SHA-256:
`1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c`.

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

## W1: four frozen programs

| Leg | Status | Platform | Architecture | Interpreter | Record |
| --- | --- | --- | --- | --- | --- |
| Original incubation | PASS, reported in frozen results | Ubuntu 24.04 | x86_64 | CPython 3.12.3 | RESULT.md and RESULT-ADDENDUM-1.md |
| Supplementary local run | PASS, same-architecture reproduction | Ubuntu 22.04.5 LTS | x86_64 | CPython 3.10.12 | W1/x86_64/RUN.md and run.json |
| Native second architecture | PASS, byte identity | Ubuntu 24.04.4 LTS | aarch64 | CPython 3.12.3 | W1/aarch64/RUN.md and run.json |

[PASS] All four stdout files in both W1 legs equal the original package's
recorded bytes. Every program exited zero with empty stderr. No differing
byte or frozen-claim falsifier was observed.

| Landed program | Status | Checks | Stdout bytes | Stdout SHA-256 |
| --- | --- | --- | --- | --- |
| verify.py | PASS | 38 of 38 | 4476 | `3b2bdc432e1bfebcd453b83a6766a2863b6a1d54243180cbc20e0b1ce4ea39ad` |
| verify_addendum1.py | PASS | 12 of 12 | 2436 | `fc5432d288f340038d64edb5ceab9aeec71c3b400cc378c8556878089b549bed` |
| break_check.py | PASS | 21 of 21 | 2660 | `f1044cc3c1371342ca3bfc5b921460332fa7c07a17999874e556dc1891cf6f0f` |
| break_check_addendum1.py | PASS | 11 of 11 | 1403 | `6e3aa7f8eac8d2df31f6c60f4e2b5cfa78c11a4092501b4a5defa1a12a733bd6` |

[CUSTODY] The native aarch64 execution started at `2026-10-02T19:15:25Z`
and finished at `2026-10-02T19:15:31Z`. The completed records were retrieved
after a conversation interruption; the programs were not rerun to reconstruct
them. Start, finish and wrapper outcome files are retained in `W1/aarch64/`.
The unchanged capture wrapper used for both W1 legs had SHA-256
`33a38114852e6a70c173867959a103ca21e1e2f809c978ba92d41b37fded166c`.
The wrapper is not needed for the direct replay described in README.md.

[LIMIT] These are exposed incubation reproductions. Byte identity provides
the requested second-architecture evidence but creates no public-probe pin
and promotes no claim to a Canon status.

[PASS: PUBLICATION REPLAY] On 2026-10-02 the four landed programs were replayed
from the repository root on Linux x86_64, CPython 3.10.12, in the same declared
environment. Each exited zero with empty stderr and matched the recorded
stdout byte for byte. All 54 imported source hashes remained unchanged before
and after this replay. This is additional exposed validation of the landed
filenames, not a new scientific pin.

## W2: independently authored breaker

[PASS: INDEPENDENT LOCAL AUDIT] Ten groups passed on Windows 11, AMD64
(x86_64), CPython 3.12.10. The first execution and one repeat both exited zero
with empty stderr and identical stdout: 1335 bytes, SHA-256
`187016c69990aaa276e7f3a49281c6deff9efe20b6b012659471f5275e5a9ff1`.
The raw stdout uses native CRLF. No Linux byte-identity claim is made for W2.

[PINNED LOCALLY] The three W2 files were pinned before first execution and
remain unchanged. See [W2/RUN.md](W2/RUN.md), [W2/PIN-W2.sha256](W2/PIN-W2.sha256),
and the exact FIRST/REPEAT records. This local pin preceded public publication.

[PASS: BOUNDED AUDIT] The audit includes the shear derivation of the four S3
form families, Weyl phase and primitive-root conventions, all 120 placements
and source permutations, 2175 rational vectors in dimensions 3, 5, 7, 9 and 15,
and the line-reading update laws. The independently serialized census has
9544 ASCII/LF bytes and SHA-256
`a2f76d45a0d42ae42906238833f90231ab55546ec4a9a3290bf2d6ed60c11491`.
That is a separate specified serialization, not a claimed match to the original
census table hash.

[QUALIFIED] W2's S8 resource conclusion requires the universal,
preparation-independent point/current-direction kernel and readiness for
arbitrary future line readings. A terminal two-outcome marginal does not
require its unused final refresh. See [W2/RESULT.md](W2/RESULT.md) for this
qualification, positive-count conditioning, the dimension-one exclusion,
finite-search limits and the full proof-review scope.

[UNCHANGED] `C-OCCURRENCE-CYCLE-COUNT-N` remains
`STOP_APPLICABILITY / H_NOT_TESTED`. The QDD reading remains conditional.
No native event contract, sharp-infimum theorem or Canon promotion follows.
