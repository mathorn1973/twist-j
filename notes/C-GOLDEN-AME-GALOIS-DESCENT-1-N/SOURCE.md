# Frozen source

Status: **NON-CANONICAL input manifest**

The sole external matrix input is:

| Field | Frozen value |
|---|---|
| Repository | [`matrix-toolbox/AME_4_6`](https://github.com/matrix-toolbox/AME_4_6) |
| Commit | `1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8` |
| Path | `AME46_ORIGINAL.m` |
| Raw bytes | `8515` |
| Git blob SHA-1 | `e0d0e171d58b3360c39595d677ffc401a466112d` |
| SHA-256 | `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae` |
| License | MIT |

Recover and verify it with:

```sh
curl -L --fail \
  https://raw.githubusercontent.com/matrix-toolbox/AME_4_6/1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8/AME46_ORIGINAL.m \
  -o AME46_ORIGINAL.m
sha256sum AME46_ORIGINAL.m
```

The source is not vendored. Both verifiers reject a byte or hash mismatch.

Primary construction source: S. A. Rather et al., [*Thirty-six entangled
officers of Euler*](https://arxiv.org/abs/2104.05122v2), arXiv:2104.05122v2.

