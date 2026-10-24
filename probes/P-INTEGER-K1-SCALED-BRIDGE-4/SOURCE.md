# Source Manifest for P-INTEGER-K1-SCALED-BRIDGE-4

```text
probe_id:               P-INTEGER-K1-SCALED-BRIDGE-4
status:                 NON-CANONICAL
claim_level:            L1
external_datasets:      NONE
raw_transcripts:        NONE
canonical_authority:    mathorn1973/twist-j main (Public Canon v1, tag canon-v1)
base_commit:            dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
canon_sha256:           31d2fbce3effe7fbca29ab7e65dc0cfbf3fb4aa9fc2ebdeaa4f33ca4739a6d6e
canon_bytes:            99872
predecessor_probe:      P-INTEGER-SOURCE-HOLONOMY-1
predecessor_pr:         https://github.com/mathorn1973/twist-j/pull/1633
predecessor_pin_commit: b3de2d7886a00bc7d6b2f5fe470516424be8b046
predecessor_head:       1ffe24aab9f4bbe070dfbb23b914244c9b68aa02
abandoned_pin_1:        P-INTEGER-K1-SCALED-BRIDGE-1
abandoned_pin_1_commit: 632f59e97c169abe937e00a6d92642f32378d767
abandoned_pin_1_close:  1d7085545f26563ea4ebfd5faf0ea9fad10a9cd7
abandoned_pin_1_pr:     https://github.com/mathorn1973/twist-j/pull/1636
abandoned_pin_2:        P-INTEGER-K1-SCALED-BRIDGE-2
abandoned_pin_2_commit: fd4e5a2734fd99d94480b6bef30d2c657f6debc3
abandoned_pin_2_close:  0847cf6cc8fe0af0d0fde9e580184a8d40acff2d
abandoned_pin_2_pr:     https://github.com/mathorn1973/twist-j/pull/1637
abandoned_pin_3:        P-INTEGER-K1-SCALED-BRIDGE-3
abandoned_pin_3_commit: 989c4ba195d1e6a5ecce9baed437ae2fa1372543
abandoned_pin_3_close:  497e809b8d06fc8d6dc0dc9d9543739f6ff85b57
abandoned_pin_3_pr:     https://github.com/mathorn1973/twist-j/pull/1638
```

## Normative and Predecessor Inputs Referenced

1. `canon/CANON.md` (`DEF-K1-LINEAR-METRIC`, `K1-LINEAR-METRIC-COMPLETION [T]`,
   `O-G-EINSTEIN-SOURCE-LAW-1 [O]`, `GATE-L1-L2-MANIFOLD`).
2. `probes/P-INTEGER-SOURCE-HOLONOMY-1/` (`PR #1633`, pin
   `b3de2d7886a00bc7d6b2f5fe470516424be8b046`):
   - 6-phase Hermitian source-holonomy apparatus over `O = Z[j]`,
   - exact K1 3-adic denominator valuation theorem `v_3(d_n) = 4(n - 1)`,
   - no-4D-invariant-lattice and no-fixed-form `GL_4(Q(sqrt(5)))` pullback
     boundaries.
3. All computational checks in `verify.py` and `breaker.py` are self-contained
   using only the Python standard library (`fractions`, `hashlib`, `math`,
   `pathlib`, `subprocess`, `sys`). No external files outside
   `probes/P-INTEGER-K1-SCALED-BRIDGE-4/` are read at runtime.
