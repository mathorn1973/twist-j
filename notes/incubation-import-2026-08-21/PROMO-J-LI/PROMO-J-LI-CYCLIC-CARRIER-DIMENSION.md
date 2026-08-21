# PROMO-J-LI-CYCLIC-CARRIER-DIMENSION. Fold hand-off (Lane B2)

```
CANDIDATE:     notes/j-li-schoenberg-2/CYCLIC_CARRIER_DIMENSION.md (proof) plus
               the finalized skeleton verifier below
TARGET:        public mathorn1973/twist-j, sealed fold v6 -> v7
PROPOSED ROW:  J-LI-CYCLIC-CARRIER-DIMENSION [T, unconditional]
SCOPE:         L6 measure. Excludes every finite-dimensional cyclic carrier for
               the Li ladder.
AUTHORITY:     none (incubation). Public two-architecture validation required.
RH:            O.
```

## 1. Claim (exact, unconditional)

Every unitary triple (U, v) whose cyclic subspace is finite-dimensional obeys

```
q_n := || sum_{k=0}^{n-1} U^k v ||^2 = a_* n^2 + R_n,
a_* = || P_{z=1} v ||^2,   0 <= R_n <= C < infinity.
```

If q_n = lambda_n(xi) for all n >= 1, the norm identity forces lambda_n >= 0, so
Li's criterion gives RH, and then the Lagarias asymptotic
lambda_n = (n/2) log n + ((gamma - 1 - log 2pi)/2) n + O(sqrt n log n) makes
lambda_n unbounded and o(n^2). The first limit forces a_* = 0, which makes q_n
bounded, contradicting unboundedness; a_* > 0 makes q_n ~ a_* n^2, contradicting
o(n^2). The contradiction closes on every branch, so the exclusion is
unconditional. Every exact all-n unitary Li realization has infinite cyclic
dimension: infinite support, 1 in supp(mu_v), no atom at 1.

## 2. Falsifier

A finite-dimensional cyclic (U, v) with q_n = lambda_n for all n. Excluded by the
theorem; no finite numerical cutoff can establish it, and none is used.

## 3. Verifier and pins (non-formal incubation run, single architecture)

```
file            verify_carrier_nogo.py  (project: claude/verify_carrier_nogo.py)
file sha256     d1f0f866352e45fd1ca5692bedba5b9bbfb84b0808ba380e7b32778330244542  (5125 bytes)
stdout sha256   ed0db62d39cc9354d21de31b4de1a848a4e4a037764b8a7a9a417dab45d38925  (808 bytes, 8 lines)
environment     LC_ALL=C LANG=C ... TZ=UTC; Linux x86_64, Python 3.11.15; 6/6 PASS
gates           KC1 primitive-10 exemplar ladder (0,4,10,14,20,24,...) bounded,
                10-periodic, a_* = 0 (reproduces the owner CC1 exemplar exactly)
                KC2 a_* = 0 for the primitive carrier
                KC3 z=1 carrier ladder is n^2 + bounded, a_* = 1
                KC4 dichotomy q_n = a_* n^2 + R_n on both exemplars
                KC5 no branch is both unbounded and o(n^2) (contradiction closes)
                KC6 Ramanujan c_10(n) exact, c_10(0) = phi(10) = 4
```

Import (frozen in the public PREREG): Lagarias's Li-coefficient asymptotic; Li's
criterion; the spectral theorem. The verifier pins only the exact finite
skeleton; it does not reprove the imports.

## 4. Dependency edges

```
parents   J-LI-COCYCLE-NORMAL-FORM; the exemplar J-PHI10-SCHOENBERG-EXEMPLAR
          (the primitive 10th-root carrier is the plenum 2-form torsion sector).
upgrades  the guard COCYCLE-BY-FINITE-FIT from a caution to a theorem-backed row.
```

## 5. Exact fold edits

REGISTRY.tsv, add (tab-separated):

```
J-LI-CYCLIC-CARRIER-DIMENSION   T   every unitary (U,v) with finite-dimensional cyclic subspace has ||sum_{k<n}U^k v||^2 = a_* n^2 + O(1); the Li ladder is unbounded and o(n^2) (Lagarias), so no finite carrier realizes it: the realization has infinite support, 1 in supp, no atom at 1   <RH/Li lane>   probes/P-J-LI-CARRIER-NOGO-1
```

CANON.md: add the theorem under the RH/Li lane heading. CHANGELOG.md,
HISTORY.tsv: one sealed entry. STATUS_COUNTS.tsv: T +1. SHA256SUMS: recomputed.
FRONTIER.md: no live row (a T no-go).

## 6. Non-claims

The theorem narrows the realization space; it does not enter it and does not
advance RH. RH [O].
