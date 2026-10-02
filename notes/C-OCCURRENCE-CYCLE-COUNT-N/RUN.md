# Completed Gate 0 custody audit

**NON-CANONICAL. One completed artifact-custody run; no occurrence-counting
experiment.** Reservation [#1336](https://github.com/mathorn1973/twist-j/issues/1336),
PR [#1338](https://github.com/mathorn1973/twist-j/pull/1338).

The preregistration, manifest and checker were committed and pushed at
[`f3b59cc08efce600957676fbce6d17b31ab9aa11`](https://github.com/mathorn1973/twist-j/commit/f3b59cc08efce600957676fbce6d17b31ab9aa11).
Before execution, all three files were retrieved from that public commit
through the GitHub contents API and verified byte for byte against the
following freeze. No frozen file was repaired or edited after that pin.

| Frozen file | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 10519 | `524fca08604268cbada9210c0ae8e399532db8a9d48d1aa443f4b24cb548c15b` |
| SOURCES.json | 1878 | `30aa7f1f8b27fc0cee45e27df394df31749ef6d39d07730857eb9ea84cbf2c1c` |
| verify_contract.py | 3833 | `3dea68eed9204d768a2f9f2506e205a902e3f005e0db1bd9b4a2e744d052d296` |

Run metadata:

```text
recorded_at_utc: 2026-10-02T14:24:48.879368+00:00
platform: Windows 11 (10.0.26300)
architecture: AMD64
python: 3.12.10
source_pin: f3b59cc08efce600957676fbce6d17b31ab9aa11
command: python notes/C-OCCURRENCE-CYCLE-COUNT-N/verify_contract.py .
exit_code: 0
stdout_bytes: 342
stdout_sha256: 4d11c1b7e7147597daac9c669ef8fc937849a03040c8ac16571c6382af552c26
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The actual stdout is retained unchanged as [EXPECTED.txt](EXPECTED.txt).
The checker ran once after public readback and returned all four immutable
source blobs with the required lengths/hashes. The program launches only
read-only `git show` operations; none of those sources' scientific verifiers
was run. The paper interpretation was independently accepted in [REVIEW.md](REVIEW.md).

Exit zero confirms custody and the declared contract. The emitted scientific
applicability disposition is **STOP / H_NOT_TESTED**. The program explicitly
does not automate semantic paper review. Zero occurrence runs, cycle counts,
history counts and cycle/trace comparisons mean that no such experiment
was executed, not that an admissible cycle was found to have zero events.
No two-architecture occurrence result, Born derivation or physical F is
claimed. An additional architecture replay of this checker would audit
only the same custody operation.
