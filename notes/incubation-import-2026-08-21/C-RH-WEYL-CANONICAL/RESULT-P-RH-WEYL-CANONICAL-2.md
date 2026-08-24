# RESULT P-RH-WEYL-CANONICAL-2

```text
STATUS:      NON-CANONICAL INCUBATION RESULT, no authority
DATE:        2026-08-20 (UTC)
VERDICT:     6 of 6 checks PASS, exit 0. MAP RECORDED. The exact
             rank-two threshold map w*(x, delta; design, m) to m = 24
             stands as the record [candidate-C at the frozen grid].
             The owner prediction window is hit exactly:
             N*(D1, ND1, w = 1/10) = 11.
FIREWALL:    no RH claim, no zeta claim. Model statements only.
             J7 SOURCE [O]. RH [O]. Public Canon v55 untouched.
PIN:         commit 51efd3d98f66a58d8a81154825f6d350180e1cd0 on branch
             agent/rh-weyl-canonical-2 (above the correction head
             a3509c9), prereg and verifier committed BEFORE first
             execution, author A. M. Thorn
PREREG:      PREREG-P-RH-WEYL-CANONICAL-2.md
             sha256 ba6a19c42fbf3929f3f400c609a5f601fbd00d3561afed8e3b4fb1e6a40ce74b
VERIFIER:    verify_rh_weyl_canonical_2.py
             sha256 1236eeaca7e7ba27986eb8735b4a3f91197d5d4da73211f13bf64b7c1467bd05
STDOUT:      verify_rh_weyl_canonical_2.stdout.txt, 8056 bytes
             sha256 20c1ae5757dcd0e3efe764e4dd9034cc4c973c62ff0fc7e09000b11f18d1c457
             BYTE-IDENTICAL on macOS arm64 CPython 3.9.6 and Linux
             x86_64 CPython 3.11.15, env LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC, exit 0
BREAKER:     breaker_rh_weyl_canonical_2.py
             sha256 1ed746cd46997b68653a4eafa98af32a99696d4fd1a9d97f729d30e018639c44
             stdout breaker_rh_weyl_canonical_2.stdout.txt
             sha256 97e9340a13d9e6ac368fde043adc002806f560917a876d89701f76fe74113507
             single leg Linux x86_64, FINDINGS: 0
```

## 1. What passed, exactly

```text
CHECK 0  foundations: 24 distinct upper half-plane nodes per Pick
         design; background pivots strictly positive to m = 24 on all
         four designs (ND1 bottoms at 6.8e-88, ND2 1.1e-47, ND3
         2.3e-19, ND4 2.4e-3).                                   PASS
CHECK 1  rank-two determinant identity, exact, against direct
         determinants at m = 12, 2 cells x 2 weights x 4 designs
         (16 comparisons, including the ND4 symmetric variant). PASS
CHECK 2  Cauchy-Schwarz D_m >= 0, all 24 blocks, all 10 cells, all
         4 designs (960 block quantities).                       PASS
CHECK 3  consistency with the pinned WEYL-1/1b record on ND1 at
         m <= 8: D1 undetected, D2 N* = 6, D3 undetected; all three
         w*_8 brackets inside the frozen anchors (D1 1.709752e-1,
         D2 1.800330e-2, D3 2.141727e+1).                        PASS
CHECK 4  owner prediction window: N*(D1, ND1, 1/10) = 11, inside
         the frozen [9, 13]. The owner-reported value was ~ 11;
         the exact computation lands on 11 exactly.              PASS
CHECK 5  depth stop-gate: D1 detected by m <= 24 at w = 1/10 on at
         least one design (in fact on all four).                 PASS
```

The background pivot ladders are the C10 doctrine at scale: ND1's
exact 24-node ladder descends to 6.8e-88, seventy orders below the
float noise floor. Nothing float can gate on these objects; the exact
LDL prefix-sum machinery is the only instrument that sees the map at
all.

## 2. The map, headline rows (full 40-row record in the pinned stdout)

Detection depths N* at the frozen weight w = 1/10, defect delta = 1/10:

```text
x       ND1 chain   ND2 spread   ND3 shifted   ND4 one-point c=5/4
1/10        11          11            9              20
1/3         11          11            9              14
3/5         10          10            9               8
4/5          7           8            7               4
9/10         6           6            7               3
```

Thresholds at full depth, w*_24 (dec6 of certified brackets),
delta = 1/10:

```text
x       ND1          ND2          ND3          ND4
1/10    1.118e-3     2.002e-3     7.649e-5     4.609e-2
1/3     1.507e-3     1.879e-3     6.078e-4     1.122e-2
3/5     1.038e-3     1.336e-3     2.216e-3     4.957e-4
4/5     3.477e-4     3.357e-4     1.287e-3     1.179e-6
9/10    7.313e-5     4.316e-5     5.014e-4     3.147e-10
```

Readings, all [candidate-C at the frozen grid]:

```text
R1  The owner-reported landscape is CONFIRMED on the frozen designs:
    D1 chain N* = 11 (owner ~ 11, gated, hit); spread N* = 11 (owner
    ~ 11, ungated context, hit); shifted window N* = 9 (owner 9 to 10,
    ungated context, hit). FW3 of WEYL-1 was insufficient depth at
    N = 8, exactly as the correction's E4 narrowed reading states: the
    bulk defect D1 becomes visible three nodes deeper.
R2  Node-design leverage at the bulk is real but modest: moving from
    the chain to the shifted window buys N* 11 -> 9 for D1 and lowers
    w*_24 by a factor ~ 2.5 (1.5e-3 -> 6.1e-4). Spreading alone (ND2)
    buys nothing over the chain at the bulk. Consolidation R3's
    preference for spread nodes is NOT supported at delta = 1/10 bulk
    positions; the shifted (closer to the axis) window is what helps.
R3  The one-point instrument ND4 is sharply position-selective: at the
    band edge it dominates every node design by orders of magnitude
    (x = 9/10: N* = 3, w*_24 = 3.1e-10, six orders below ND1), and at
    the far bulk it is the worst instrument (x = 1/10: N* = 20). Its
    power concentrates where its expansion point c = 5/4 sits, at the
    spectral edge. It is also the ONLY instrument that catches any
    delta = 1/100 defect within m = 24: x = 4/5 at N* = 20 and
    x = 9/10 at N* = 11 (w = 1/10).
R4  The weak-defect wall is now quantified, not guessed: at
    delta = 1/100 every node design has w*_24 in [0.10, 1.07] across
    the grid, two to three orders above the frozen w = 1/100. Depth
    24 is nowhere near these defects; the wall stands as data with
    exact heights attached.
R5  Monotonicity observed (not gated): w*_m decreases in m in every
    cell of every design; min24 is attained at m = 24 throughout the
    grid.
```

## 2b. The breaker record (FINDINGS: 0)

```text
B1  Full float recomputation of the N* map: agreement 3 of 30 on the
    Pick designs, 4 of 10 on ND4, and every agreeing row is shallow
    (N* <= 6 Pick, <= 11 on ND4 whose pivots bottom at 2.4e-3). The
    float map is garbage precisely where the map lives: the exact
    detections at m = 9..11 occur at pivot scales below 1e-30. This
    is the C10 doctrine measured on the whole grid: the map does not
    exist for float instruments.
B2  The real independent verification: direct exact-determinant
    bisection of w* (no LDL, no prefix sums) at three pinned spots,
    including the deep ND2 m = 24 threshold 4.3e-5; all three
    brackets overlap the verifier's dec6 windows.
B3  Inertia attack on the at-most-one-negative-direction statement:
    exact pivot signs of P(w) at w = 1/100, 1, 32, 1024, 2^20 on the
    detected cell; exactly ONE negative pivot at every w. The
    theorem's clause (v) survives a five-decade weight sweep.
B4  Roam over 40 random rational cells (N = 12): 7 float-flagged
    suspects all exact-rechecked; D >= 0 in every case, and the
    determinant law 1 + 2 w Re(gamma) - w^2 D fitted from two w
    values reproduces a third exactly (residual identically 0),
    verifying the quadratic law itself on random off-grid cells.
B5  ND4 symmetric law float witness at (3/5, 1/10), m = 10:
    negative float det ratios above the crossing, consistent with
    the exact bracket ordering w*_12 < 0.05 < w*_8.
```

## 3. Consequences for the lane

```text
1  Obligation O5 of WEYL-1 is DISCHARGED at the frozen scope: the
   detection landscape and node-design question posed by the fired
   FW3 now has an exact answer on four designs to m = 24, with the
   correction's E4 depth reading confirmed by gate.
2  The detection instrument for successor probes is settled: block
   quadratics from one LDL plus prefix sums, strict-negativity
   semantics, boundary = zero, per correction E6. Verified against
   direct determinants (CHECK 1) and the pinned lineage (CHECK 3).
3  Open and NOT claimed: any statement off the frozen grid; the
   delta -> 0 scaling law of w*(m) (the R4 wall heights invite a
   scaling probe but none is preregistered here); mixed or adaptive
   node designs; and the zeta-side obligations O1-O3, which remain
   the lane's actual mathematics and are untouched by this probe.
```

Nothing here moves J7 SOURCE or RH; both stay [O].

End of result.
