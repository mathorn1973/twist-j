# Run record

Status: NON-CANONICAL candidate-C finite audit. Date: 2026-10-09.
Not a formal public probe or a two-architecture science gate.

Preregistration and both verifiers were committed and pushed BEFORE the
first execution of either verifier. Public remote readback confirmed:

```text
pin: 1981511b55f72dfdfff1009cf3b77f2978d58641
branch: notes/c-j-euclidean-color-boundary-n
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
```

Frozen SHA-256:

```text
6cb515ddf9e023b00f63c7d43f42666e3c11b981d58222ae2be20312d473a5c7  PREREG.md
df277a48ad7894686af8691627ff74d4bb13ecf9f18bc59fc89a89904e979395  verify.py
ead2132f50571505b822cd5aa7865c2753cf0c576f6f96100042b1f43a035ce9  break.py
```

## First exact executions

From the repository root, each command was executed separately with
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1:

```sh
python3 notes/C-J-EUCLIDEAN-COLOR-BOUNDARY-N/verify.py
python3 notes/C-J-EUCLIDEAN-COLOR-BOUNDARY-N/break.py
```

| Script | Exit | stdout bytes | stderr bytes |
| --- | --- | --- | --- |
| verify.py | 0 | 3741 | 0 |
| break.py | 0 | 3741 | 0 |

The two stdout byte strings were compared exactly and were identical.
Their common output was saved as EXPECTED.txt:

```text
sha256: 3fe724f2fc65c76eb796a229000743aadbaba2ff47901c4e00ef3753f70c9524
bytes: 3741
```

The proof of an infinite-graph upper bound is not replaced by these finite
checks. No E6 proof or Lean build was executed by these commands.

## Repository-runner replay

A subsequent call to the repository's existing reproduce function passed:

```sh
python3 -c 'from pathlib import Path; from tools.check_reproduce import reproduce; reproduce(Path("notes/C-J-EUCLIDEAN-COLOR-BOUNDARY-N").resolve())'
```

It reported REPRODUCE PASS with the pinned verify.py and EXPECTED.txt
hashes. An earlier invocation passed a relative Path to this function and
stopped before invoking verify.py because the runner requires an absolute
path. Only the invocation was corrected by adding resolve(); no scientific
code, preregistration, assertion or threshold changed. This invocation
error is not a scientific falsifier or a completed formal gate.

Both scientific scripts were frozen before comparison and were authored by
the same session. Their agreement is a representation cross-check, not
blind independent-agent confirmation. A replay is reproduction, not an
independent proof. No other execution architecture is claimed.
