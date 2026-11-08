# Public source custody and admission ledger

Status: NON-CANONICAL. Evidence for the preregistered `L1` proposal
`P-INTEGER-K1-SCALED-BRIDGE-1` only.

## 1. Authority

The session read `STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/CORE.md`, and
`canon/FRONTIER.md` from public `main` at
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d` (peeled tag `canon-v103`, declared
content commit `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`, `canon/CANON.md`
1052518 bytes).

| File at checked `main` (`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`) | SHA-256 |
| --- | --- |
| `STATUS.md` | `6ff52d4fc3bdeb210fe2c8ae89d54d4e5f21dfccb63aa37ddad281710ef21375` |
| `POLICY.md` | `da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d` |
| `AGENTS.md` | `7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1` |
| `canon/CANON.md` | `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b` |
| `canon/CORE.md` | `9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728` |
| `canon/FRONTIER.md` | `8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0` |
| `canon/REGISTRY.tsv` | `5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d` |
| `canon/SHA256SUMS` | `0579c7174198fdea2af8357512c1d746584da9bd58ec3b584c8b8d54884d1fb4` |

## 2. Companion probe context (#1632 / #1633)

This probe directly continues the `L1` boundary established in
`P-INTEGER-SOURCE-HOLONOMY-1` (ownership issue #1632, draft PR #1633, immutable
pin `b3de2d7886a00bc7d6b2f5fe470516424be8b046`, result head
`1ffe24aab9f4bbe070dfbb23b914244c9b68aa02`), which was independently reviewed
by this session in
https://github.com/mathorn1973/twist-j/issues/1632#issuecomment-6262097998 .

| Companion file in #1633 (`1ffe24aab9f4bbe070dfbb23b914244c9b68aa02`) | Bytes | SHA-256 |
| --- | ---: | --- |
| `probes/P-INTEGER-SOURCE-HOLONOMY-1/PREREG.md` | `15054` | `75660464a3a8d437ab7a84f602da5b8bced2e2b1516e4567a4b7c451c57776de` |
| `probes/P-INTEGER-SOURCE-HOLONOMY-1/PROOF.md` | `21468` | `64edde47710199d76eff127276515551cbc6b7d06c69514199e4b8d03303a197` |
| `probes/P-INTEGER-SOURCE-HOLONOMY-1/RESULT.md` | `7328` | `4c995271a0ef82eb0a77e12bd29d0420ab2fb6713d6c1eb311d6b99f62f2617e` |
| `probes/P-INTEGER-SOURCE-HOLONOMY-1/EXPECTED.txt` | `930` | `c053b1840bf40ede47a7d03525d84ce3cd4a3a010190572a8f492bb2f3b3aaef` |

## 3. Admission and layer table

| Item | Custody / admission status |
| --- | --- |
| `O = Z[j]`, `J = 1 + j^2`, `phi = -j^2 - j^3`, cyclotomic conjugation | Existing `L1` algebra, used literally |
| `DEF-K1-LINEAR-METRIC` and `K1-LINEAR-METRIC-COMPLETION [T]` | Existing canonical `L1` definition and theorem, used literally |
| `v_3(d_n) = 4(n-1)` K1 denominator theorem | Proved in #1633 (`PROOF.md` §8) and independently verified here |
| Universal 3-adic quadratic precision bound `sum P_n^2 + D_n^2 >= (6/5) 3^(8(n-1))` | Unconditional `L1` theorem on `DEF-K1-LINEAR-METRIC` (Claim B3) |
| Scaled integer K1 carrier `X_K1 = Z^5 x Z^5 x Z_(>=1)` and `E_K1` | `NEW_DECLARED` integer precision state and arithmetic account |
| Domain-and-Bank Reflection Bijection `F_K1` and `F_bridge` | `NEW_DECLARED` total bijection rule with unconditional `L1` proof (Claim B1) |
| Additive transverse metric readout `g_r(U, k)` on `X_K1` | `NEW_DECLARED` current-state rational metric projection (Claim B4) |
| Coupled 7-phase, 40-integer apparatus `X_bridge` | `NEW_DECLARED` composite source-holonomy + scaled-K1 carrier (Claim B5) |
| Native original-`U` gate admission, physical clock, dynamical Einstein law | `UNSUPPLIED` |

All runtime computations are self-contained under `probes/P-INTEGER-K1-SCALED-BRIDGE-1/`
and use only Python's standard library.
