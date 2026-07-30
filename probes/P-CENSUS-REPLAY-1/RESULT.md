# P-CENSUS-REPLAY-1 result record

Status: two-architecture reproduction complete. The post-pin aarch64 owner
leg and the GitHub x86_64 leg reproduce the frozen transcript from the same
pinned verifier hash.

## Pin

```text
public issue                         #72
preregistration + verifier pin       1633a26005b8b9316f4c84084646cca26854eb5d
verify.py sha256                     1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c
PREREG.md sha256                     f5979759843a05692b42350559675c706d984920cd84a50f9919cb1ff48065c6
```

The pin was public before this execution. The verifier remained byte-identical
to `reproduce/census/verify.py` at the frozen base commit.

## Formal legs

```text
leg      architecture   python   result           stdout sha256
-------  -------------  -------  ---------------  ----------------------------------------
owner    aarch64        3.12.3   11/11 ALL PASS   f0022dc...bbb0 (1125 bytes, 18 lines, empty stderr, exit 0)
GitHub   x86_64         3.12.13  11/11 ALL PASS   f0022dc...bbb0 (policy run 162, job 88192431671, VERIFY PASS)
```

The owner stdout is byte-for-byte identical to the pre-existing frozen public
reference `reproduce/census/EXPECTED.txt`. Its SHA-256 is
`f0022dc0c19314c88efae2974139b659d0748b3d039c9f9368de1be891a8bbb0`.
The clean checkout remained unchanged by the verifier.

## Gate

Owner aarch64 leg: **PASS**. All eleven preregistered gates pass, stderr is
empty, the exit code is zero, and the exact transcript matches the frozen
reference.

Two-architecture replay gate: **PASS**. GitHub PR #73 policy run 162 checked
the changed public probe on x86_64 and reported:

```text
VERIFY PASS P-CENSUS-REPLAY-1 1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c f0022dc0c19314c88efa2974139b659d0748b3d039c9f9368de1be891a8bbb0
```

The same job also passed policy, all 38 unit tests, Canon, and ledger checks.
No claim, evidence row, Canon file, dependency, or status changes in this
probe.

This replay does not establish protocol independence or an independent census
implementation. Any later evidence-ledger fold remains a separate reviewed
change.
