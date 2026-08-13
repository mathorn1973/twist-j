# Result

All values below are in `F_241`, with the frozen locator `xi -> 3`.

| target | `(D0,D1,D2,D3)` | `F8=(v0,e1,e2,e3)` |
|---|---|---|
| golden | `(209,17,88,148)` | `(209,12,166,170)` |
| sym | `(171,108,108,108)` | `(171,83,47,5)` |
| sparse | `(171,108,108,108)` | `(171,83,47,5)` |

For both comparisons, the first coordinate in the frozen order is `v0`.
The locator difference is `209-171 = 38 mod 241`.

The exact replay in `Q(zeta_120)` reconstructs a nonzero `golden-target`
difference whose 32 coefficients are published in `result.json` and
`AUDIT.md`; its locator reduction is 38.  Therefore:

```text
EXACT_NO_SYM
EXACT_NO_SPARSE
EXACT_NO_GG_ARTISANAL_9PLUS27
```

Within the preregistered scope, neither direct Gross--Goedicke artisanal
`9+27` orbit representative is equivalent to the pinned golden AME(4,6)
tensor under arbitrary four local unitaries, global phase, and any party
permutation.  By the frozen Theorem-1 orbit reduction, this excludes all 48
function tables in the two named orbits.  It is not a classification of all
AME(4,6) tensors.

