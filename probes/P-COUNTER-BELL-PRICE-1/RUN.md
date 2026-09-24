# Run record: P-COUNTER-BELL-PRICE-1

```text
pin_commit: 46c717afa5067b8f0c8818c47dbc3c7017bcc9e7
verifier_sha256: 26a6b8faaae92f9b533700f1a3bcd87d73364f4a2b59f1461cfd460e37e6e27b
command: python3 probes/P-COUNTER-BELL-PRICE-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 083e31cacdc6324cb54d72f73bbb910de99bf7ef178926477a3f33c2274f3c0d
stdout_bytes: 1482
stdout_lines: 28
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Prospective public custody

```text
pin_parent: f8a77855288b5f94ea554504b3c636624ca1318a
public_claim_lock: issue 1153
formal_date: 2026-09-24
started_utc: 2026-09-24T07:11:42Z
finished_utc: 2026-09-24T07:11:46Z
```

The five pinned files were committed in one commit whose sole parent is the
public main above, pushed to the named public branch and fetched back before
the first formal execution. HEAD and FETCH_HEAD equaled the pin, and every
fetched blob matched its frozen identity:

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 8145 | 8ef87f4ec8eac6d24aad57c84cf8a1fd1f66b6c13221d9cc3cf608d72f4da045 |
| PROOF.md | 5947 | 31fbc663afa7d37f40f69fe173e640c6511bdcbc655d045ee76db913ca471f3d |
| INCUBATION-PREREG.md | 7446 | c412e70327439d687edcab82acfb54b4ceb185378b7c02feef4db37383bf3ad8 |
| verify.py | 17845 | 26a6b8faaae92f9b533700f1a3bcd87d73364f4a2b59f1461cfd460e37e6e27b |
| break.py | 9389 | 9ee229fdafb3e1b86d0de74aaf46fdd8f151e04a5f36e98310efa66285f9f300 |

The formal run used a fresh clone of the branch at the pin, a clean worktree
before and after, the displayed command from the repository root, a cleared
environment with only the listed variables and PATH, and stdout and stderr
captured separately outside the worktree. The actual stdout was then saved
verbatim as EXPECTED.txt.

The formal stdout is byte-identical to the incubation stdout declared in
PREREG.md (1482 bytes, SHA-256 083e31ca...f4c0d), which had been produced
by the same verifier bytes on x86_64 and aarch64. The reproducibility STOP of
Field 5 did not fire. The required pull-request workflow reruns the pinned
verifier on GitHub x86_64 and aarch64 against this EXPECTED.txt.

Verdict line: `RESULT ALL PASS`, `failures 0`, 23 checks.
