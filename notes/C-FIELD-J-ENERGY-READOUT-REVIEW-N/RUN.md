# Independent finite audit run

PUBLIC, NON-CANONICAL. One x86_64 audit; no two-architecture claim.

Frozen source: `c404c1c53a9af3ce1b2523de8a56a270e082e7c9`.
All three frozen Git blobs were publicly read back before execution.
The execution checkout had this exact HEAD and was clean.

```text
python3 notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/break.py
```

Date: 2026-10-01. Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Timeout: 600 seconds. Actual elapsed subprocess time: 4.609 seconds.
Exit: 0; stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 8709 | `19071a223723c9189d9463b2389707ebdcc1c84ed843bd1f9651426018e6d5d3` |
| DERIVATION.md | 10777 | `6b4f080e94a5c68ddddc4fd20282f8388b82a86b71938d4c08a40bec4c57963e6` |
| break.py | 15364 | `0aa1aa2eb2347490d38feb930f2a8bb3b0dabbf49d12e3e4fe774d0e3cd24f68` |
| EXPECTED.txt, exact stdout | 610 | `f12a35424245bbca754ac849d360877956393cd77f894b8f42f279c2e25713c5` |

Finite checks passed, including 143125 typed keys and 76920 chain boundaries.
The all-input and all-time claims rely on the written derivation. This PASS
does not override the original author's tuple-subclass false rejection found
in post-freeze comparison; see REVIEW.md for separate claim dispositions.

An earlier checkout preflight stopped before candidate execution because
the requested commit had not been fetched. The successful run used the
unchanged public pin. No scientific input, domain or threshold changed.
Ordinary notes-only CI does not execute this audit automatically.
