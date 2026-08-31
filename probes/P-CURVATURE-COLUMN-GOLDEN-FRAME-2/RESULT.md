# P-CURVATURE-COLUMN-GOLDEN-FRAME-2 result

## Status

```text
scientific route:  ABSENT
owner formal leg:  C, exact exhaustive computation on x86_64
public ceiling:    T at the frozen finite L2 scope only after the required
                   GitHub x86_64 and aarch64 jobs reproduce EXPECTED.txt
```

All eight frozen integrity gates passed at the immutable pin
`af90ed4b49504907501fd8f77db6dae2e7d82422`. The verifier exited zero,
wrote 997 bytes of deterministic stdout, and wrote no stderr.

No falsifier fired. The result is negative and terminal for this extraction:
there is no distinct pair of historical column rays with squared projective
cosine `1/5`. Therefore no six-ray clique and no `GOLDEN6` frame can occur.

## Exact result

For the frozen historical tuple

```text
X = F_5^6,
H = <b,d>,
V = (Q^X)^H intersect 1_X^perp,
K_hist = P[T_a,T_c]P |_V,
```

the complete exact census is:

```text
H order:                            20
H orbits:                           819
orbit census:                       5:1, 10:74, 20:744
active incidence entries:           26034
Tr_V(K_hist^2):                     -881/8
rank K_hist:                        292
nullity on V:                       526
nonzero orbit columns:              819
distinct rational projective rays:  567
ray source multiplicities:          315 rays from one column
                                    252 rays from two columns
ray pairs:                          160461
exact squared-cosine bins:          338
orthogonal ray pairs:               140841
pairs with c2=1/5:                  0
six-cliques in the c2=1/5 graph:    0
GOLDEN6 frames:                     0
```

The complete cosine-histogram digest is

```text
c24e129bb4b1399a4eb451925080e29005d8269682bb1d5b6ddc24becf830633
```

Both independent clique enumerators returned the empty ordered stream, whose
SHA-256 is the empty digest

```text
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
```

## Scientific conclusion

The exact historical commutator does **not** force the public golden
six-line geometry through the preregistered orbit-column extraction. The
route

```text
K_hist
  -> centered H-orbit columns
  -> rational projective rays
  -> c2=1/5 golden adjacency
  -> GOLDEN6 frame
```

fails at its first golden gate: the adjacency graph has no edges.

This is stronger than merely finding no six-frame. Even the pairwise golden
angle is absent from the complete frozen ray family.

## Scope firewall

This result closes only the historical **column-ray extraction**. It does not:

- select `K_hist` as the canonical spatial-curvature operator;
- close or partially close `CURVATURE-OPERATOR-CANONICAL [O]`;
- classify eigenlines, singular directions, image lines, row rays, mixed
  column constructions, or every admissible geometric extraction;
- falsify `GOLDEN-SIX-LINE-SYM2-FRAME [T]`, whose six lines live on a separate
  exact carrier;
- identify or exclude physical space, hyperbolic length, pseudoconvolution,
  a decoder output, or an L5/L6 measure;
- alter `CURVATURE-HISTORICAL-TRACE [T]`,
  `CURVATURE-HISTORICAL-GAUSS-SPLIT [T]`, `KERNEL-MACRO-READING [D]`, or
  `TIME-CUT-READING [D]`;
- add a parameter or authorize a Canon, Registry, Frontier, or release change.

The correct interpretation is narrow and decisive:

```text
The historical commutator's canonical orbit columns do not contain the
1/sqrt(5) projective-angle seam.
```

Any further attack must choose and preregister a different extraction or wait
for a complete public classification of admissible curvature operators. This
probe supplies no authority for changing the operator or extraction after
seeing `ABSENT`.

## Reproducibility

The committed `EXPECTED.txt` is the complete accepted stdout. The owner run is
recorded in `RUN.md`. Required pull-request jobs must use the unchanged verifier
and dependency, exit zero, write empty stderr, and match `EXPECTED.txt` byte for
byte on x86_64 and aarch64. A transcript mismatch is integrity STOP, not a new
scientific route.
