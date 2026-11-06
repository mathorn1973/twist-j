# Parity and occupation geometry at interaction diameter two

**NON-CANONICAL. L1. Status: INCONCLUSIVE for both original settings.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1788](https://github.com/mathorn1973/twist-j/issues/1788).

The original source has both object constituents on odd physical sites.
An opposite-parity target requires changes at every old and new object
site, plus any changed carrier sites. This test selects targets whose
mandatory changes cannot fit into diameter two for any source component.
It then bounds the original logarithmic energy on that forbidden output.

The exact first calculation passed all integrity checks but its full
remainder bound was too large. Both preregistered comparisons are LT.
Diameter two remains open: no local realization or new obstruction is
established. The fixed sources, energy, projection and thresholds were
not changed after the public pin.

| File | Purpose |
|---|---|
| [PREREG.md](PREREG.md) | Fixed inputs, code hash, 29-line schema and dispositions. |
| [PROOF.md](PROOF.md) | Geometric zero, parity energy identity, finite certificate and 12 review obligations. |
| [verify.py](verify.py) | Exact standard-library cyclotomic computation. |
| [EXPECTED.txt](EXPECTED.txt) | Unchanged first stdout, including both settings. |
| [RUN.md](RUN.md) | Public pin and first-run metadata and hashes. |
| [RESULT.md](RESULT.md) | Scientific interpretation and remaining question. |
| [SHA256SUMS](SHA256SUMS) | Content manifest, excluding itself. |

Prospective pin: `55b6472d8b3081dd22f26439f09eb31d2e8dba69`.
Replay from the repository root:

```sh
python3 probes/P-SOURCE-PARITY-RANGE2-1/verify.py
```

Required GitHub x86_64/aarch64 exact replay evidence is reported in the
pull request after the actual logs are read. Reproduction does not confer
independent mathematical acceptance or promote this work into Canon.
