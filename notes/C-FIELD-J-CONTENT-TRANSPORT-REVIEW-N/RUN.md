# Independent whole-state transport audit

PUBLIC, NON-CANONICAL. Independent finite audit on one architecture.

Independent source pin: `593ab81acdefb563ace6e29f7da0f5197a007a38`.
All three public source blobs matched before execution and author exposure.
The execution checkout had this exact HEAD and was clean. The harness uses
alternating path coordinates; it imports no author implementation.

```text
python3 notes/C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N/break.py
```

Date (UTC): 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Timeout: 600 seconds. Elapsed subprocess: 2.602 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 7717 | `8ed8c472e109d5575e912f9dc0535f10a120e5dd1206bced5a1a14e37c7e1bca` |
| DERIVATION.md | 9849 | `cee7a4e66f5de2106d24e76c5da5214092fb7e006b90fbb52dc241e59a7010ea` |
| break.py | 17332 | `d2aa61efa74bb26b323d9a940ac9269a8c7d1a561419869cf157abd14716467a` |
| EXPECTED.txt, exact stdout | 382 | `08bb207503943772e5c6e62b8f35fff1050d52decf654a280d30bc77feaeb000` |

PASS includes 49224 local cases, 840 dirty states, 8904 locality
interventions, 73332 clean macrosteps, 40740 cut macrosteps, 13968
underfunded macrosteps, 11046 complete-period macrosteps, all 1226 record
values and 356766 modular additions. Exact stdout includes the other frozen
control counts. These finite checks supplement the independent universal
derivation. No dynamic author adapter was run or added after the pin.
The separately pinned author implementation was compared statically only,
as preregistered; its own audit is separately recorded.

No two-architecture scientific result follows. Ordinary notes-only CI does
not execute this harness automatically. The scope is the separately selected
classical integer law, not a coherent or physical implementation.
