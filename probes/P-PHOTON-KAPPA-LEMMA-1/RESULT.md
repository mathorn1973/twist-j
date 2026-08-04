# P-PHOTON-KAPPA-LEMMA-1 result

Status: `FORMAL LOCAL RESULT / BELOW-THRESHOLD / PUBLIC TWO-ARCHITECTURE
GATE PENDING / NO CANON CHANGE`

The single owner-authorized formal execution of the immutable verifier
completed with exit 0, empty stderr, and stdout byte-identical to
`EXPECTED.txt`.

## Frozen decision

```text
OUTCOME BELOW-THRESHOLD
RESULT 12/12 ALL PASS
```

All integrity and scientific gates passed:

```text
C1  canonical schema and exact fixture bytes                 PASS
C2  nonzero ternary closed current                           PASS
C3  connected support and oriented 3240-step Euler circuit   PASS
C4  ternary face chain with support 7993                     PASS
C5  two exact paths establish partial n=5j and partial^2=0   PASS
C6  declared counts, pinned counts, bytes, and SHA-256       PASS
C7  exact 2^7993<=7^3240, B=9095, slack=1102                PASS
S1  nine registered shape regressions, minimum 31/8          PASS
S2  periodic torus out-of-carrier control                    PASS
S3  five exact mutation controls at their named gates        PASS
S4  fresh evaluation and transcript determinism              PASS
S5  exactly one BELOW-THRESHOLD outcome line                 PASS
```

No STOP predicate fired.

## Exact certificate conclusion

The pinned JSON exhibits a pair `(j_*,n_*)` on the owner-frozen L4 carrier
with

```text
j_* != 0,
partial j_* = 0,
supp(j_*) connected,
L(j_*) = |supp(j_*)| = 3240,
partial n_* = 5j_*,
F = |supp(n_*)| = 7993,
2^7993 <= 7^3240.
```

Thus `j_*` is in `CertificateCurrent`, hence in `ParentWorldline`, and
`n_* in Fill(j_*)`. Therefore `F_occ(j_*)<=7993`.

For any coprime positive integers `(a,b)` satisfying frozen K2,

```text
2^(4a) > 2401^b = 7^(4b),
```

so `2^a>7^b`. If universal K1 held at `j_*`, then

```text
b*7993 >= b F_occ(j_*) >= a*3240.
```

It would follow that

```text
2^(b*7993) >= 2^(a*3240) > 7^(b*3240),
```

contradicting `(2^7993)^b <= (7^3240)^b`. Consequently the admitted
singleton family `{(j_*,n_*)}` excludes every positive rational
`kappa=a/b` satisfying K2 from satisfying universal K1 on
`ParentWorldline`.

This fires the frozen negative-certificate predicate `BELOW-THRESHOLD`. It is
not merely a refutation of one candidate coefficient or proof.

## Evidence and status disposition

The formal local result is exact and preserves the fired falsifier. The
required GitHub x86_64 and aarch64 reproductions are still pending. Until both
match the committed `EXPECTED.txt` and the aggregate `check` passes:

- no public Registry status is earned;
- `PHOTON-WINDOW-PROOF [O]` remains the current Canon row;
- no Canon, frontier, evidence, dependency, gate, program, release, or tag
  changes;
- no two-architecture completion is claimed by this file.

If both architecture jobs pass unchanged, this probe supplies public exact
evidence for the frozen Kappa counterexample route. A later separate owner
disposition and sealed Canon fold must decide registration of the Kappa child
and the compound parent. This probe itself makes no Canon edit.

## Scope firewall

The result does not compute or claim `F_occ(j_*)=7993`; it uses only the exact
upper bound supplied by the exhibited filling. It claims no optimal filling,
pump family, asymptotic sequence, second certificate, positive Kappa
coefficient, universal shape classification, or alternative carrier result.

It does not execute, prove, falsify, or close the electric-face roughening
certificate or issue #201. It establishes no Froehlich-Spencer import,
massless phase, Coulomb window, continuum limit, propagator, or physical
photon. It introduces no cross-layer lift, physical measure, time statement,
FCC carrier, displacement support, shell weight, polarization, holonomy, or
SI interpretation.

The existing `KAPPA-SHAPES [C]`, `MONOPOLE-COST [C]`, and all other public
rows remain at their current status. Any wider interpretation requires a
separate public ruling, proof, probe, or later sealed Canon fold.
