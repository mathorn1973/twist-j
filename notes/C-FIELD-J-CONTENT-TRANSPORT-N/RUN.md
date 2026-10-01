# Author finite audit of the whole-content law

PUBLIC, NON-CANONICAL. One x86_64 execution, not independent review.

Specification pin: `0167766b8b89839daca9951186000063abb0adce`.
Complete source pin: `d47754854f4796cbff4a985fae52b497ea72a8ce`.
Public source blobs matched before execution; exact clean checkout.

```text
python3 notes/C-FIELD-J-CONTENT-TRANSPORT-N/verify.py
```

Date (UTC): 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Timeout: 600 seconds. Elapsed subprocess: 3.474 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 18488 | `8e910ff4b9edb95af7ef8c420c839ac2dc7c7ef299af29d62f668373232bcf7f` |
| PROOF.md | 15601 | `b9f54e881182aa12daa913270a7904d60cab6f8f39130a7dd5455d31d50fd6ad` |
| verify.py | 17681 | `cc67d1fa3e2203cfc47498e10488ce02fdde5761b817509c2523fad5896ac883` |
| EXPECTED.txt, exact stdout | 632 | `386d9b9a1c801cc38b22aa04305ddf10dbe66a1cf38243e4f28e8686e0ed875f` |

PASS: 29300 local gate cases; 640 occupied states; 1455 clean trials with
122220 layer comparisons; 1746 cut trials with 59364 layer accounts;
75 no-event and 105 dirty trials; all 1226 record values; 356766 modular
additions over all 291 supported codes. The frozen exact stdout supplies
the detailed counters. Universal all-state/all-N/all-time statements rely
on PROOF.md and independent review, not finite trajectory extrapolation.

No second-architecture scientific run is claimed. Ordinary notes-only CI
does not execute this candidate verifier. The model is a selected classical
integer law; no coherent instrument, occurrence or physical lift is tested.
