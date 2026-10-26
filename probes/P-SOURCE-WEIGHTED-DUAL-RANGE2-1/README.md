# Original source energy excludes physical diameter two

**NON-CANONICAL. L1. Conditional CERTIFIED_OBSTRUCTION for both sources.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1790](https://github.com/mathorn1973/twist-j/issues/1790).

For each original source psi_+ and psi_-, every Hamiltonian in the declared
bare-occupation class with term-support diameter at most two has original
energy-action error strictly greater than E0/1200. Arbitrary interactions
inside three consecutive sites are included. The conclusion retains all
26 old-memory labels, passive references and fixed data-independent ancillas.

The first exact execution completed all 66 predetermined comparisons:
31 pass, 35 are inconclusive. The common member m=1,a=4 passes for both
sources. The two predecessor tests remain preserved as inconclusive.
The source, energy, physical encoding and target tolerance were unchanged.

| File | Purpose |
|---|---|
| [PREREG.md](PREREG.md) | Frozen inputs, full family, code hash and 381-line output contract. |
| [PROOF.md](PROOF.md) | Weighted-dual estimate, Taylor envelopes, physical scope and 14 review obligations. |
| [verify.py](verify.py) | Exact standard-library integer/cyclotomic computation. |
| [EXPECTED.txt](EXPECTED.txt) | Entire unchanged first stdout, including every failed comparison. |
| [RUN.md](RUN.md) | Public pin, first execution and output custody. |
| [RESULT.md](RESULT.md) | All dispositions, the physical conclusion and its limits. |
| [SHA256SUMS](SHA256SUMS) | Content manifest, excluding itself. |

Prospective pin: `b5ebcd6276d538710d3ff19534b67e46a04bda18`.
Replay from the repository root:

```sh
python3 probes/P-SOURCE-WEIGHTED-DUAL-RANGE2-1/verify.py
```

Required GitHub x86_64/aarch64 scientific replay evidence is reported in
the pull request after the actual logs are read. Reproduction does not
replace external mathematical acceptance or promote the result into Canon.
Larger interaction diameters, dressed encodings, another energy and the
separate compact apparatus remain outside this obstruction.
