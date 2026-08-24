# C-TM-HANKEL-K4-SUBSTRATE-1: first freeze, run, and break

```text
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
DATE:         2026-08-11 (UTC)
PUBLIC BASIS: Public Canon v43, main 981aa1b9c8bc7ecd084346e099f014f3fc78847c
              tag canon-v43, CONTENT_COMMIT 320324f0def8ac9af89d0f128dbd7ab6548df55b
              canon/SHA256SUMS 5 of 5 OK on a fresh clone at freeze time
CONSUMED:     TM-HANKEL-K2-TRANSFER [T], TM-HANKEL-K3-UNIVERSAL-TRANSFER [F],
              TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION [C], and the three other
              v43 Hankel rows
LAYER:        L1 only
INHERITED:    nothing. No k = 3 law was assumed, and the k = 3 mechanism was
              never evaluated at k = 4.
```

The frozen question was the minimal invariant information deciding the
`k = 4` transfer. It was attacked from below: derive what the decision
cannot depend on, then raise the lower bound with exact witnesses.

## Pins

```text
PREREG   PREREG-C-TM-HANKEL-K4-SUBSTRATE-1.md
         sha256 130bd7649ccdeacd382c06080514782f85a59c9c46404a2c8ade7d736bb81b19
         10153 bytes, frozen before any computation
VERIFIER verify_tm_hankel_k4_substrate_1.py
         sha256 6cb0c5596ffb3b85f73cc31dff076188028a05a250f2e61ced9bd00e3bd6d8dd
         22929 bytes
STDOUT   sha256 785cc7ad90aed473b4dbd8fe3624f12155575b0687282952c62efa99b8f4b8f7
         2135 bytes, 44 lines, exit 0, empty stderr, 12 of 12 gates PASS
LEG 1    Ubuntu 24.04 x86_64, Python 3.11.15
LEG 2    Debian 13 aarch64, Python 3.13.5, run twice, byte-identical
```

Two architectures, byte-identical stdout. The transfer to the second
platform was chunked base64 with per-chunk SHA-256 verification; the decoded
file hash equals the leg 1 hash.

## What the frozen gates established

### A. The substrate split (candidate-T, written derivation plus exhaustion)

`W` is subset-monotone, so the `(S,T)` entry of `W^T M W` depends only on
cells `(S',T')` with `S'` a subset of `S` and `T'` a subset of `T`. Hence a
cell `m` can reach the weight-at-most-`w` block only if `sum(m) <= 2w`, at
every `k`. At `w = 2` the criterion is `sum(m) <= 4`, and it is exact in
both directions, verified cell by cell:

```text
k = 3   19 cells, 15 present, absent types (1,2,2) and (2,2,2)
k = 4   65 cells, 34 present, 31 absent, weight-2 block has 11 directions
k = 5   211 cells, 65 present
k = 6   665 cells, 111 present
count   sum over a >= 1, 2a + b <= 4 of C(k,a) C(k-a,b)
```

The k = 3 line reproduces the sealed k = 3 substrate exactly. The empty
direction carries no free cell at any k, generalizing the k = 3 fact that
the empty direction splits off for the whole pencil.

### B. Orbit-type relevance (exact witnesses, information lower bound)

Six of the ten orbit types carry an exact single-cell relevance witness:
`0002, 0012, 0022, 0112, 0122, 1112`. Each is a pair of tables differing in
one cell whose `K` inertia differs, confirmed by two independent exact
paths. The decision therefore may not discard any of these six.

The four types with no witness in the declared domain are
`0222, 1122, 1222, 2222`. **No irrelevance is claimed for them.** The
pattern that the six witnessed types are exactly those with `sum(m) <= 5`
is an observation about the search, not a result.

Note that `0122` and `1112` have `sum(m) = 5` and are therefore ABSENT from
the weight-at-most-2 block, yet are relevant to the full block. Presence in
the small block and relevance to the decision are different properties.

### C. The linear layer is insufficient at k = 4 (exact witness)

Two tables differing by a sum-preserving two-cell swap inside type `0002`:

```text
0x02e639472cd318ed2   inertia NEG 9 ZERO 0 POS 7
0x02e639472cd318ad3   inertia NEG 8 ZERO 0 POS 8
common ten orbit sums (0, 2, 0, -2, -2, 2, 0, 2, 0, 1)
```

Identical linear invariants, different transfer class. The ten `S_4` orbit
sums do not decide the `k = 4` transfer.

### Q. Quadratic layer: no claim

The canonical 109-entry quadratic invariant map was built and machine
checked to be `S_4` invariant with exactly 109 entries. No collision was
found in the declared domain. Per the freeze this proves nothing about
sufficiency and no sufficiency statement is made, at any search size.

### E. Real quadruples to 10^8

152 extremal quadruples with `n <= 10^8`, smallest `3.23.71.1523 =
7461177`, every one balanced `NEG 8 ZERO 0 POS 8` by two exact paths. 15
extremal quadruples extend the k = 3 canonical falsifier `{5,101,293}` with
`s <= 20000`, all balanced.

## The break attempt

Two independent code paths were written to falsify the above. They found
two defects, both in the breakers, and one real correction to my reading.

```text
B1  the abstract cell table reproduces the real integer block of a real
    extremal quadruple entry by entry, on six quadruples. SURVIVED. This
    is the load-bearing bridge: without it the abstract gates are void.
B2  the nonbalanced abstract witness survives a third inertia path, exact
    rational symmetric congruence, independent of both Bareiss leading
    minors and the characteristic polynomial. SURVIVED.
B2b the linear collision is a genuine two-cell same-type swap of opposite
    signs, Hamming distance exactly 2. SURVIVED.
R1  the criterion of gate A holds at k = 3, 4, 5, 6 under the stated
    conjugation. SURVIVED. Round one reported this BROKEN at k = 5, but
    round one computed W M W instead of W^T M W; the defect was in the
    breaker, not in the claim.
```

**Defect 1, mine, in the round-one breaker.** It conjugated by `W` on both
sides instead of `W^T` and `W`, and reported a false break at `k = 5`.
Corrected and re-run: the criterion holds at `k = 3, 4, 5, 6`.

**Defect 2, mine, in the round-two breaker.** Its inertia routine returned
`None` on a zero pivot with no fallback, and `None` compares unequal to the
balanced triple, so every zero-pivot case was counted as a failure. It
reported 326 failures below `4.10^9` including `n = 7461177`, which is in
fact balanced. Corrected: every inertia is now decided by two paths that
both return a value, and 309 of the 6559 quadruples in that range do hit a
zero pivot and are routed to the characteristic polynomial.

**Real correction, not a defect.** The frozen gate E bound of `10^8` was
set below the first real failure and therefore saw none. That is a true
statement about the frozen domain, and it stands. But my informal reading
of it, that real `k = 4` failures might be absent or that the k = 3
falsifier does not extend upward, was wrong, and my own breaker refuted it.

## Recon beyond the frozen gates

Declared as recon, outside the frozen domain, with every inertia decided by
two paths. Extremal quadruples with `n <= 4.10^9`: 6559, of which 17 are
nonbalanced.

```text
SMALLEST REAL k = 4 FAILURE
n = 377931745 = 5 . 23 . 839 . 3917     inertia NEG 7 ZERO 0 POS 9
its four sub-triples, all BALANCED NEG 4 ZERO 0 POS 4:
  (23, 839, 3917) n = 75586349
  (5, 839, 3917)  n = 16431815
  (5, 23, 3917)   n = 450455
  (5, 23, 839)    n = 96485
```

Two consequences, both exact:

**1. The k = 4 failure is not inherited.** Every 3-subset of the smallest
failing quadruple is balanced. The failure is a genuinely four-prime
phenomenon, not a lift of a k = 3 failure. Separately, the k = 3 canonical
falsifier `{5,101,293}` does extend to failing quadruples, the smallest
found being `5.101.293.23741 = 3513053065`, so both directions occur.

**2. The sign of det K no longer determines the inertia.** At k = 3 the
three profiles matched the three signs of `det K` one to one. At k = 4 the
17 failures split into two profiles:

```text
NEG 7 ZERO 0 POS 9   12 cases, smallest 377931745 = 5.23.839.3917
NEG 9 ZERO 0 POS 7    5 cases, smallest 689952085 = 5.71.317.6131
```

Both have `det K < 0`, since 7 and 9 are both odd. Two distinct inertia
profiles share one determinant sign, so no single determinant sign can
recover the profile at `k = 4`. The k = 3 correspondence is a low-`k`
accident. Note also that a POS-heavy failure has no k = 3 analogue at all:
at k = 3 every failure was NEG-heavy.

## Falsifiers for anything above

Gate A fires on one cell violating `sum(m) <= 4` in either direction. Every
witness fires on a recomputation disagreement between its two exact paths.
Every count fires on an independent rerun returning a different number.

## Explicit non-claims

No census, sufficiency, or universal statement over the `k = 4` substrate.
No irrelevance of any orbit type. No claim that the quadratic layer decides
or fails to decide. No inheritance of the k = 3 two-scalar law. Nothing
about zeta zeros, the Riemann hypothesis, Weil positivity or explicit
formulae; nothing about the infinite operator beyond finite compressions;
no `J` coupling, no `p = 5` selection, no physical reading, no L2-L6 lift.
This candidate creates no registry row and moves no status.

## Next cut, not started

The two exact facts above are the natural spine of a second freeze: the
decision at `k = 4` is not a function of `sign(det K)`, and failure is not
inherited from sub-triples. A second freeze should ask what the two
profiles `NEG 7 POS 9` and `NEG 9 POS 7` are separated by, with the same
discipline: preregister, then compute, then try to break it.
