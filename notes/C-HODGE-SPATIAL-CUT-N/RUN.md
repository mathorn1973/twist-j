# Original first-execution record

**NON-CANONICAL. L1. C-HODGE-SPATIAL-CUT-N.**

Accepted public pre-execution commit: [9fb5ce827d71812e957995713385d955c949d6f9](https://github.com/mathorn1973/twist-j/commit/9fb5ce827d71812e957995713385d955c949d6f9).
Accepted tree: `17634bac0a5f1c5c291112e439a6b9fdeda1f069`.

All eight frozen contract files were fetched back from this immutable public commit and compared byte for byte before either mathematical program was executed or imported. The local worktree was then fetched and checked out at exactly this commit, with an empty `git status --porcelain`. All eight local SHA-256 values and byte counts were checked again before execution.

Each program was executed once, sequentially, on the clean accepted tree. These are the original first outputs, preserved without rewriting. No failed attempt, post-pin scientific repair, rerun or substituted expected output occurred. Result files are additions after this pin; the eight-file contract remains unchanged.

## Neutral environment

- Platform: Ubuntu 24.04.3 LTS.
- Architecture: `x86_64`.
- Python: `3.12.14`.
- Environment: `LC_ALL=C.UTF-8`, `TZ=UTC`, `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`.
- Working directory: repository root.

## Exact original outputs

| Program | Started UTC | Completed UTC | Exit | stdout bytes | stderr bytes |
|---|---|---|---:|---:|---:|
| `verify.py` | 2026-10-23T09:09:46.390059+00:00 | 2026-10-23T09:09:47.728824+00:00 | 0 | 510 | 0 |
| `break_certificate.py` | 2026-10-23T09:09:47.729328+00:00 | 2026-10-23T09:09:48.799858+00:00 | 0 | 610 | 0 |

| Output | SHA-256 |
|---|---|
| [EXPECTED.txt](EXPECTED.txt) | `51ca551e504c437fe9922c8dc7e2eddee4902ed21482065c0f4e185e62e46a49` |
| [BREAK_EXPECTED.txt](BREAK_EXPECTED.txt) | `48fabf881023d7da135e33c9476078937fc052a3fc8feae375c0dc4b09380363` |

Both empty stderr streams have SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. The byte counts and digests refer to the actual subprocess streams, including final newlines.

## Accepted contract custody

| File | Bytes | SHA-256 |
|---|---:|---|
| [README.md](README.md) | 11359 | `12a1e7d07911c03dfc0f8994d8ec36fcae669bb0901b4fd6273ddf2a362f18d3` |
| [PREREG.md](PREREG.md) | 9041 | `43ff5c46539b5506d2778383dc801603991e236febeaa3e1aa46974a9061e7dd` |
| [SOURCES.md](SOURCES.md) | 9945 | `cead240de6b231d0f80c3696258cb5d317f31d0d3e5a525b47d46a5fed67cf58` |
| [PROOF_CURRENT.md](PROOF_CURRENT.md) | 17448 | `b6b36f8b940fdad68c00f6272ee0ec13f466eef80cad283fb4aa59c7f8595d12` |
| [PROOF_RELATION.md](PROOF_RELATION.md) | 18296 | `498f73c5e99292c34223a904b86b5719d47992818e21648add6ccec480ad6206` |
| [PROOF_NATIVE.md](PROOF_NATIVE.md) | 17897 | `b9141d218beec2ce0fc85a8e53d407174d940d1c8b8958394736ccdd75e25d1a` |
| [verify.py](verify.py) | 12267 | `b58173a2853b9880e6ff5374a34b8d891c7bf8176c9f81802c4be2beaa0bd9c2` |
| [break_certificate.py](break_certificate.py) | 24976 | `aef1d60f585d4a6a656e2d9617dc9af4ad16e898101e360b087c8c1f658fdde9` |

## Reproduction commands

```sh
LC_ALL=C.UTF-8 TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python notes/C-HODGE-SPATIAL-CUT-N/verify.py
LC_ALL=C.UTF-8 TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python notes/C-HODGE-SPATIAL-CUT-N/break_certificate.py
```

Compare each stdout byte for byte with its corresponding committed output; require exit 0 and empty stderr. The programs use only the Python standard library and perform no network or source-file reads.

This record is one x86_64 scientific execution. The ordinary repository workflow does not run the mathematical programs under `notes/`; its x86_64/aarch64 jobs are not a two-architecture scientific gate for this note. Universal conclusions rest on the explicit proofs; the finite audit has only its declared finite scope.

## Repository checks

The accepted tree also passed the repository policy check, all 210 unit
tests, the Canon v104 check, the evidence/dependency ledger check and the
explicit gate-contract check. The changed-public-probe and
changed-minimal-reproduction selectors both reported not applicable for
this notes-only change. These repository checks are separate from the two
original scientific executions recorded above.
