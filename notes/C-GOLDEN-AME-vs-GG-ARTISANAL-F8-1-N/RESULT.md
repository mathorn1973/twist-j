# C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N — post-lock result

## Verdict

`EXACT_NO_GG_ARTISANAL_9PLUS27`

The frozen complete lowest non-universal closed fingerprint differs already
at `v0`.  Therefore the pinned golden AME(4,6) tensor is not related to
either Gross–Goedicke artisanal 9+27 orbit by arbitrary local `U(6)^4`, a
global phase and any of the 24 party permutations.

This conclusion is scoped to the two Gross–Goedicke Theorem-1 artisanal
orbits.  It is not a classification of all AME(4,6) tensors.

## Frozen modular scan

Over `F_241`, with `xi -> 3`:

| target | `(v0,v1,v2,v3)` | `F8=(v0,e1,e2,e3)` |
|---|---|---|
| golden | `(209, 17, 88, 148)` | `(209, 12, 166, 170)` |
| sym | `(171, 108, 108, 108)` | `(171, 83, 47, 5)` |
| sparse | `(171, 108, 108, 108)` | `(171, 83, 47, 5)` |

Both independent factor orders agree for every one of the 12 scalars.
The first frozen comparison coordinate is `v0`: `209-171=38 mod 241`.

## Exact witness

Both artisanal representatives have exact `v0=171`.  In the frozen power
basis of `Q(xi)`, `xi=zeta_120`, the exact difference
`v0(golden)-v0(artisanal)` is

```text
(-57/4)*xi^0 + (3/1)*xi^6 + (3/2)*xi^8 + (3/2)*xi^12 + (-3/1)*xi^18 + (-3/2)*xi^28 + (3/2)*xi^30
```

Its nonzero coefficient indices are
`[0, 6, 8, 12, 18, 28, 30]`, and its reduction is
`38 mod 241`, replaying the locator.

## Gates

- Public prereg commit `62c1e877c3817923dca6b922ebd4562f83d2bbea`, tree `9a8bf350f0f255bd74c0e7dabca665d0a46477c3`, issue #368.
- All public prereg and source byte/hash pins: PASS.
- Golden exact three-way two-unitarity: PASS.
- Direct sym/sparse construction, 48 -> 24+24 disjoint GL census: PASS.
- Standard and twisted autocorrelations for all 24+24 tables: PASS.
- Direct sym/sparse exact three-way two-unitarity: PASS.
- Exact Pi9/Pi27 ranks 9/27 and commutators: PASS.
- Pure diagram census and party action: PASS.
- Primary/alternate modular and exact replay: PASS.
- Independent G0/G1 audit certificate SHA-256:
  `67c9493c92129eba274345e5042d6c38738cc53e08172ff95e6d879865384834`.

This result is published only on the notes branch.  No Canon or Registry file
is modified, and no `PROMO.md` is created.
