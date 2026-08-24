# RESULT P-RH-WEYL-CANONICAL-1

```text
STATUS:      NON-CANONICAL INCUBATION RESULT, no authority
DATE:        2026-08-20 (UTC)
VERDICT:     6 of 7 checks PASS; FW3 (detection of the frozen bulk defect
             D1 within 8 nodes) FIRED. Per the frozen stop-gate the T2
             lane OPENS with the finite-node detection claim dropped and
             re-derived as a successor obligation. All other instruments
             are exact-verified. [candidate-C at the frozen model and
             ranges]
FIREWALL:    no RH claim. Model statements are never statements about
             zeta. J7 SOURCE [O]. RH [O]. Public Canon v55 untouched.
PIN:         commit d1aee4883ea6a5b046655285d634a95859e933b7, prereg and
             verifier committed before first execution, author A. M. Thorn
PREREG:      PREREG-P-RH-WEYL-CANONICAL-1.md
             sha256 3530477a1c841795b9ab44b971d9d1e6324585ae4c7512f863e56d28f53e48fb
VERIFIER:    verify_rh_weyl_canonical_1.py
             sha256 0b78aaf882fe32a1780162c9e356833596f966106582b94365c137150f99e5f1
STDOUT:      verify_rh_weyl_canonical_1.stdout.txt, 3967 bytes
             sha256 1f154a417b94cbb38f42a09eacff1c608df6b0a3009ffad39b6115daa266320a
             BYTE-IDENTICAL on macOS arm64 CPython 3.9.6 and Linux x86_64
             CPython 3.11.15, env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC; exit 1 by the frozen rule (a failed
             gated check), the failure itself being the recorded outcome
BREAKER:     breaker_rh_weyl_canonical_1.py
             sha256 b0d1439016d65f5f9e7a3c8d020eea5dac18f00574a6d5ce1e3b8ca4abe0301e
             stdout cbe3f0da90148aa1b9cec5e761d4bdb8d8e2d56c94fe13dbbeb84d05b12a65a2
             single leg Linux x86_64, FINDINGS: 0
```

## 1. What passed, exactly

```text
CHECK 0  sqrt enclosures certified (width < 1e-39).                 PASS
CHECK 1  S1 dictionary: chi^(1)/chi = resolvent Q, exact equality
         at 9 (R, z) pairs.                                         PASS
CHECK 2  S3 normalization.                                          PASS
CHECK 3  S2/S4: Im Q > 0 at all 40 (R, node) pairs; the full 8x8
         Pick matrix at R = 64 has exact positive pivot ladder
         2.36e-1, 2.08e-3, 6.44e-6, 9.89e-9, 9.02e-12, 5.43e-15,
         2.32e-18, 7.40e-22.                                        PASS
CHECK 4  S5 node convergence, certified enclosure bounds, strictly
         decreasing along R, < 1e-40 (squared) at R = 64.           PASS
CHECK 5  moment convergence at c = 2, exact Q(sqrt 3) series sqrt,
         < 1e-30 at R = 64 for k <= 6.                              PASS
CHECK 6  detection of frozen defect D1 within 8 nodes.              FAIL
```

The exact pivot ladder is the C10 doctrine made visible: float pivots of
the same matrix (breaker B2) are garbage from pivot 6 onward (1e-15 noise
floor against exact 2.3e-18 and 7.4e-22). Only exact or interval
arithmetic can gate anything on these nodes; the lane's instruments obey
that by construction.

Convergence law confirmed exactly: the certified distances give a
per-step factor 0.0556 at node 1 (a = 2; predicted q(a)^2/4 = 0.0557)
and 0.1446 at node 8 (a = 9/8; predicted 0.1446). The prereg prediction
holds at both checked nodes to three digits. The breaker's own float
check of this rate (B6) bottoms out at the double-precision floor and is
uninformative, as expected; the exact table is the record.
[candidate-C, MODEL CONVERGENCE LAW]

## 2. The fired falsifier, first-class

```text
DETECT D1  mu = 1/3 + i/10,  w = 1/10:  NOT detected at 8 nodes.
DETECT D2  mu = 9/10 + i/10, w = 1/10:  detected at N* = 6, exact
           negative pivot -2.422e-15.
DETECT D3  mu = 1/3 + i/100, w = 1/100: NOT detected at 8 nodes.
```

Reading. The instrument does fire (D2 proves the exact machinery
produces true negative pivots at finite node count), but detection at 8
clustered nodes is defect-position-dependent: a defect over the spectral
bulk (x0 = 1/3), where the background measure is dense, stays masked; a
defect near the band edge (x0 = 9/10), where the semicircle weight
vanishes, is caught. This is the model-scale appearance of the same
background-competition wall that the Hankel lane meets at step 3, and it
is consistent with consolidation C11 (the negative vector generally lies
outside any finite span; no effective bound on the first negative
dimension) and with the R2 height-cost reading. The prereg prediction
(N* = 2 to 4 for D1) was WRONG; the record stands corrected by the
machine.

The breaker's float defect landscape (B5) reports N* = 7..8 with pivots
near -1e-15 almost everywhere; those entries are float noise at exactly
the scale B2 identifies, so the landscape is unusable below pivot depth
5 and is recorded only as a demonstration of why C10 bans float gating.
An exact landscape is successor work.

## 3. Lane verdict and obligations

```text
T2 LANE OPEN (with the detection claim dropped per the frozen stop-gate).
Instruments exact-verified on the canonical model: S1 dictionary, S2/S4
Herglotz and Pick LDL* over Q(i), S5 node convergence with certified
enclosures, one-point moment gate in Q(sqrt 3).

O1  canonical-system construction of finite Q_R^(xi) from the screw
    function route of arXiv:2606.09096 v1, satisfying S1-S4.
O2  the dictionary from e^phi(R,z) W(R,theta;z) to Q-functions on the
    zeta side (gate S1 there).
O3  gate S5 for zeta: node convergence Q_R(i a_n) -> Q_xi(i a_n) or
    one-point resolvent-moment convergence; with A9 + A10 + A11 this is
    the full RH content of the lane.
O4  certified instruments only (C10): exact or interval LDL, never float
    signs on the 1+1/n chain.
O5  NEW, from the fired FW3: an exact detection landscape and a node
    design theory. The frozen 1+1/n chain is detection-weak at 8 nodes
    for bulk defects; consolidation R3 already prefers spread nodes or
    one-point derivative instruments. Successor probe: same model, the
    three instruments of the consolidation (chain, spread, J_N(c)) at
    N up to 24, exact arithmetic, mapping N*(x0, delta, w) and testing
    whether the bulk masking is a node-design artifact or a real
    finite-span obstruction.
```

Nothing here moves J7 SOURCE or RH; both stay [O]. The zeta-side
construction (O1-O3) is the lane's actual mathematics and remains
untouched by this opener.

End of result.
