# CI audit for PR #1884

Status: NON-CANONICAL / L1. This is a read-only audit of public CI evidence
that already exists. It makes no Canon promotion and no owner decision.

## Identity

- Repository: `mathorn1973/twist-j`.
- PR: [#1884](https://github.com/mathorn1973/twist-j/pull/1884), open when
  checked.
- PR head: `c9bd0bc5ac97ad034be399e6619695c7fc2c4a61`.
- Base: `17de90b58f814238e151aac77badde6654b52627`, the v108 activation.
- Scientific source pin: `aaf3ec7e925c2c0261604179ee4166d542233e14`. Its
  only parent is the base, and it is the head's parent.
- [Actions run 41705245141](https://github.com/mathorn1973/twist-j/actions/runs/41705245141):
  attempt 1, event `pull_request`, conclusion `success`. Its head SHA is the
  PR head above.

`git diff --name-status aaf3ec7 c9bd0bc` lists only three added files:
EXPECTED.txt, RESULT.md and RUN.md. At the pin, the seven source files have
the SHA-256 values that RUN.md records:

| File | SHA-256 |
| --- | --- |
| PREREG.md | 6a2b90f07b4967d0e4eaf09c28a9628b0eae247b6acdf986c26d74f5c2b65a08 |
| PROOF.md | 13998852f685c474e0ec775ac2e4cd41f102c2c93412ee2ef0a77beeece28fd5 |
| PROVENANCE.md | 6882788bc1c108dfa8fe90f55fc6b93a91cc098a1d4f09153cb0d676a999c71f |
| RUNTIME_SOURCES.json | 8238c256e9ef089ea79d9349cfa413facbf3d751cd74982dc95f53406bf40ea8 |
| arithmetic_compiler.py | 0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027 |
| compiled_audit.py | 1b32ea0f8b38518495e59028ad8d5867ac5a36a87da78b5924726278c56926fd |
| verify.py | d9968f83bf2827f0849e65b65cb00876571d4ea3f262214c65a5362dab5d8fa5 |

This audit cannot check the claim that the files were publicly fetched
before execution. That claim is the author's custody statement.

## Actual checkout

Both architecture logs print `HEAD is now at f8ce10b3 Merge c9bd0bc5… into
17de90b5…`, the merge GitHub generated for testing. That merge commit is
`f8ce10b3bd40fa352cceb27782ea37a17ed38874`, with parents base and head. The
base is an ancestor of the head. The merge's tree,
`de25501883ab7ceb3370be975013624aa3f9503f`, equals the head's tree, so the
tested tree is byte-identical to the target head.

## Scientific replay on two architectures

| Architecture | Job | Python | Scientific log lines |
| --- | --- | --- | --- |
| x86_64 | [126158698747](https://github.com/mathorn1973/twist-j/actions/runs/41705245141/job/126158698747) | CPython 3.12.16 | `VERIFY ARCHITECTURE … x86_64`, then the PASS line below |
| aarch64 | [126158698894](https://github.com/mathorn1973/twist-j/actions/runs/41705245141/job/126158698894) | CPython 3.12.15 | `VERIFY ARCHITECTURE … aarch64`, then the PASS line below |

Both logs contain this identical line, produced by the unchanged
`tools/check_verifier.py --base "$BASE_SHA"`:

```text
VERIFY PASS P-NATIVE-RECEIVER-CARRY-MIRROR-1 d9968f83bf2827f0849e65b65cb00876571d4ea3f262214c65a5362dab5d8fa5 085d8c3dd70a9443e560440f9a4b1d70c9e66bec50b57dfdc7724ae120f8ad50
```

The two fields are the pinned verifier's SHA-256 and the SHA-256 of the
actual scientific stdout. The second equals the SHA-256 of the committed
2479-byte EXPECTED.txt. The runner prints PASS only when exit is zero,
stderr is empty and stdout matches byte for byte. Together these satisfy
the policy's two-architecture computation gate for this probe. The logs
show the replay took 4.133 s on x86_64 and 4.646 s on aarch64. That is
operational metadata only.

Each architecture job also ran `check_policy.py` (`POLICY PASS`), the 218
`tools/` unit tests (`Ran 218 tests … OK`), and the Canon, ledger,
gate-contract and changed-path reproduction checks. The 218 unit tests
check repository tooling. They are not independent implementations of this
probe.

The aggregate
[check job 126159445957](https://github.com/mathorn1973/twist-j/actions/runs/41705245141/job/126159445957)
succeeded. Its step "Require every architecture job to have succeeded" is
guarded by `if: needs.architecture.result != 'success'`. That step was
skipped, which means the architecture matrix succeeded.

## Local replay by the reviewer

The reviewer also ran the target verifier once, unchanged, from a clean
checkout of the head, on Linux x86_64 with CPython 3.13.18 and the
preregistered environment. Exit was 0, stderr was empty, and stdout was
byte-identical to EXPECTED.txt (2479 bytes, SHA-256 085d8c3d…).

This is a reproduction on the same architecture, not a gate. It is also not
independent of the target code. RESULT.md records the code-independent
check separately.
