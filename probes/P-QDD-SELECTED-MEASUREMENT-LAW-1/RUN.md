# First completed run: selected measurement law

PUBLIC; NON-CANONICAL; P-QDD-SELECTED-MEASUREMENT-LAW-1.

This is the first completed scientific execution, from the clean public pin.
The seven frozen files were fetched from the public commit and compared byte
for byte before local checkout and execution. No scientific gate was run
before pinning. Static syntax checks and written review preceded the pin.

## Run fields

```text
pin_commit: f1a25f6a51cf167094eb95b8a37a5cb7e8dcc368
verifier_sha256: cf6b9ca76a9d0914ce9af181e3d173e1b6f55adab2319673c55608c20ace31e2
command: python3 probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_bytes: 702
stdout_lines: 9
stdout_sha256: 92c8c4e8f8e0dcf463c2e274a746fd2e279b829df8b0c86818466165c99cc641
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Public lock: [#1093](https://github.com/mathorn1973/twist-j/issues/1093).
Base: `822ae98c63545d9e800b4d145c0eec8c7bca29a6`.
Pin tree: `c93f9761557924c9d95dab07e0a4b53a18ba35ee`.
Worktree at invocation: clean; HEAD exactly the pin.
Working directory: repository root. Date: 2026-09-20.
Environment: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`. Exact stdout is committed unchanged as
`EXPECTED.txt`.

## Frozen input custody

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/PREREG.md` | 8066 | `f56cfc18350a4de61d945c3db5d005052928e0605bed4e0c462d65bcb6f777da` |
| `probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/MODEL.md` | 14602 | `98c36cbeb98f11c74ea3a23c53dc4c67d54e04bf9d49377947dc6cd017bdc0c0` |
| `probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/PROOF.md` | 21629 | `77337130debc01d231d7bf121a064f5245ca0c29c3fd3199ab9fef1c14635efc` |
| `probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/REVIEW.md` | 11050 | `42fb446019b1f6d7a29f432e3e6ade85b56e965a60c0271122e239c5fe8eb1a4` |
| `probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/verify.py` | 18973 | `cf6b9ca76a9d0914ce9af181e3d173e1b6f55adab2319673c55608c20ace31e2` |
| `notes/canon/SELECTED-THEORY-PROGRAM-2026-09-20.md` | 13942 | `9f048bac0e74663b1c9d6d6016431cf2111384d6a5a0ec8ded9e06fbe6629d20` |
| `notes/canon/SELECTED-MEASUREMENT-FOLD-PROPOSAL.md` | 11723 | `942a3352413197fa8e92acdc26811413c9a3f1058a0c22e36f57ef2a2053358b` |

The verifier uses only standard-library exact rational arithmetic and reads
no external files at runtime. Its finite checks audit the general written
proof; they do not establish physical validity of the selected inputs.

This record documents one local architecture. Subsequent public x86_64 and
aarch64 replay, review and acceptance are recorded separately in
`ACCEPTANCE.md` and the linked pull-request jobs. No hardware experiment,
random trial, empirical Born-law test or Canon activation occurred here.
