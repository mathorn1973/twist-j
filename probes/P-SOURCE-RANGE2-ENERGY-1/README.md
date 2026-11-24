# Diameter-two source-energy certificate

**NON-CANONICAL. L1. Status: INCONCLUSIVE.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1786](https://github.com/mathorn1973/twist-j/issues/1786).

This fixed exact test asks whether a forbidden carrier tail of the original
energy Q=E0 f(U_rec), on either original source psi_+ or psi_-, excludes
bare physical interactions of diameter at most two at error E0/1200.
Both preregistered comparisons are **LT**, so neither supplies the proposed
obstruction. All arithmetic and propagation integrity checks passed.

This is a completed, reproducible inconclusive result. It establishes neither
a diameter-two realization nor a small true forbidden energy tail. The
nearest-neighbor obstruction in the pinned predecessor is unchanged.
An exact post-run bound also shows that increasing the Fourier cutoff alone
cannot rescue this same filtered test; RESULT.md gives the short derivation.

| File | Purpose |
|---|---|
| [PREREG.md](PREREG.md) | Prospective parameters, strict threshold, immutable outputs and failure rules. |
| [PROOF.md](PROOF.md) | Conditional physical inequality, calibration and exact arithmetic representation. |
| [verify.py](verify.py) | Frozen, standard-library integer/cyclotomic verifier. |
| [EXPECTED.txt](EXPECTED.txt) | The exact first completed stdout, preserved byte for byte. |
| [RUN.md](RUN.md) | First-execution custody, platform, exit and output hashes. |
| [RESULT.md](RESULT.md) | Both scientific dispositions and what remains open. |
| [SHA256SUMS](SHA256SUMS) | Content manifest, excluding itself. |

The executable and its two prospective documents were published at
`c4584bb481e369338c2f90d2c2e7fd4eed3aec54` and read back before execution.
No parameter or source was changed after that pin. From the repository root:

```sh
python3 probes/P-SOURCE-RANGE2-ENERGY-1/verify.py
```

The repository replay compares stdout exactly and requires empty stderr.
Required GitHub x86_64 and aarch64 results are reported in the pull request
after their actual replay logs are available. Reproduction and same-session
reviews do not constitute independent external scientific acceptance.
The sole authority remains ACTIVE Public Canon v105.
