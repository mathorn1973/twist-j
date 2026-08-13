# Frozen external source

Status: **NON-CANONICAL input manifest**

Incubation: `C-GOLDEN-AME-TWOPLACE-1-N`

## Authoritative matrix input

| Field | Frozen value |
|---|---|
| Repository | [`matrix-toolbox/AME_4_6`](https://github.com/matrix-toolbox/AME_4_6) |
| Commit | [`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`](https://github.com/matrix-toolbox/AME_4_6/commit/1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8) |
| Path | `AME46_ORIGINAL.m` |
| Raw bytes | `8515` |
| Git blob SHA-1 | `e0d0e171d58b3360c39595d677ffc401a466112d` |
| SHA-256 | `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae` |
| License | [MIT](https://github.com/matrix-toolbox/AME_4_6/blob/1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8/LICENSE) |

The third-party source is not vendored here. The exact raw input used for the
recorded runs can be recovered with:

```sh
curl -L --fail \
  https://raw.githubusercontent.com/matrix-toolbox/AME_4_6/1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8/AME46_ORIGINAL.m \
  -o AME46_ORIGINAL.m
sha256sum AME46_ORIGINAL.m
```

The verifiers reject any byte, SHA-256, or Git-blob mismatch. They parse the
two source `36 x 36` literals directly and do not use MATLAB floating-point
output.

## Publication provenance

- S. A. Rather et al.,
  [*Thirty-six entangled officers of Euler: Quantum solution to a classically
  impossible problem*](https://arxiv.org/abs/2104.05122v2),
  arXiv:2104.05122v2; Phys. Rev. Lett. 128, 080507 (2022).
- W. Bruzda et al.,
  [*Multi-Unitary Complex Hadamard Matrices*](https://arxiv.org/abs/2204.06800v2),
  arXiv:2204.06800v2. Appendix B is a human-readable cross-check, not the
  machine authority.
- S. Ball and R. Simoens,
  [*Thirty-six quantum officers are entangled*](https://arxiv.org/abs/2603.02334v1),
  arXiv:2603.02334v1 (2026). This supplies only the imported entanglement
  necessity theorem; it supplies neither the matrix nor a TWIST-J bridge.

The Appendix-B representative and the matrix called `U_36` in the original
construction are related by a partial transpose. This incubation uses only
the pinned MATLAB representative and the index conventions frozen in
`PREREG.md`.
