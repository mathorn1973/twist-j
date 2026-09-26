# PREREG-C-COUNTER-BELL-PRICE-N

Candidate. No authority. Frozen before the verifier is written and before any
code touches the claims. Target line on promotion: public,
mathorn1973/twist-j, as a probe P-COUNTER-BELL-PRICE-1. One named session owns
this candidate. Claimed 2026-09-23.

## 0. Currency

```
STATE            ACTIVE
AUTHORITY        mathorn1973/twist-j main
CANON            Public Canon v91, tag canon-v91 -> 11b66d47
CONTENT_COMMIT   b89b0c80bb5cebddade567f31a979aaf42f1d9dd (ancestor of main)
main read at     f8a77855288b5f94ea554504b3c636624ca1318a
CANON_SHA256     6d49a9dfce95f2146490ccc9ae76066bca01d1614291549562b599d35b2218e1
CANON_BYTES      772678
SHA256SUMS       5 of 5 OK
Internal line    not reachable this session; v184 not claimed
Collision check  registry, probes/, open issues and branches carry no
                 measurement-dependence price, overlap measure or counter Bell
                 row. Related rows read, unchanged: BELL-MAGIC-BOUNDARY [T],
                 QDD-FIVE-CONTEXT-BELL-SEPARATION [T], BELL-CAUSAL-ACCOUNTING
                 [D], QDD-SELECTED-PAIR-LAW [D].
```

PRIOR EXPOSURE, DISCLOSED. Every claim below was derived by hand in this
session before the freeze, including the value 1/16 in (C5), its primal
point and its dual certificate. No code has been executed on any claim. The
freeze fixes statements and thresholds; the verifier is the exact check of a
hand derivation, not a blind measurement.

## 1. Equation

Bipartite scenario, settings x, y in a finite set X, outcomes a, b in a
two-letter alphabet. A counter model is a finite latent set Lambda,
setting-conditional latent laws mu_xy on Lambda (rational, one per setting
pair), and local response kernels alpha(a|x,lambda), beta(b|y,lambda)
(rational, stochastic, alpha blind to y, beta blind to x):

```
p(a,b|x,y) = sum_lambda mu_xy(lambda) alpha(a|x,lambda) beta(b|y,lambda)
eps(mu)    = 1 - sum_lambda min_(x,y) mu_xy(lambda)      overlap dependence
```

eps = 0 exactly when the latent law is setting independent.

```
(C1) canonical split: nu = min_xy mu_xy, r_xy = mu_xy - nu >= 0, and every
     r_xy has mass eps.
(C2) determinization: moving the response randomness into the latent
     variable reproduces p and preserves eps.
(C3) CHSH, X = {0,1}, outcomes +1/-1, S = E00 + E01 + E10 - E11:
     |S| <= 2 + 2 eps for every counter model; for every rational eps in
     [0,1] an explicit model with overlap dependence exactly eps has
     S = 2 + 2 eps. Hence S = 2 sqrt(2) needs eps >= sqrt(2) - 1, exact in
     Q(sqrt 2), and is attained there.
(C4) five-context functional, X = Z/5, outcomes L/H,
     B = 2 sum_k p(LL|k,k) - sum_(k != l) p(LL|k,l):
     B <= 2 + 8 eps for every counter model, attained for every rational
     eps in [0,1]. The value 35/16 needs eps >= 3/128 and is attained there.
(C5) full ETH-QDD-2 table P, with p(.|k,k) = (LL 1/4, LH 0, HL 0, HH 3/4)
     and p(.|k,l) = (1/64, 15/64, 15/64, 33/64) for k != l: the minimal
     overlap dependence of a counter model reproducing P exactly is
     eps_T = 1/16. Upper certificate: local weight 15/16 on types A = B = S,
     total 50/64 on singletons and 10/64 on pairs, uniform in each size
     class, plus the free remainder. Lower certificate: dual weights
     z(off-diagonal LL) = 1/4, z(off-diagonal HH) = 1/12,
     z(diagonal LH) = z(diagonal HL) = 1, all others 0, checked on all
     1024 deterministic types. Lemma inside (C5): minimal eps equals one
     minus the maximal local weight w* in P = w L + (1 - w) Q, L local and
     setting independent, Q an arbitrary behaviour.
(C6) signalling: |p_A(a|x,y) - p_A(a|x,y')| <= eps for every counter
     model, and for every rational eps in [0,1] a model attains eps.
     No-signalling is forced by the class only at eps = 0.
```

Scope sentence, part of the claim: these are finite theorems about the
stated comparison classes. The reading of Lambda as the TWIST-J plenum
state with the global counter t_n, and of the settings as physical
controllers, is not claimed here and needs its own named gate.

## 2. Code

verify.py, Python 3 standard library only, Fraction arithmetic; Q(sqrt 2)
as an ordered pair of Fractions (a, b) = a + b sqrt 2 with sign decided by
exact squaring. No float anywhere. Deterministic output, a pinned integer
seed for the random rational model families, final line a SHA-256 digest of
the preceding stdout. Runtime target under 120 seconds. Run from its own
directory with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
TZ=UTC.

## 3. Carrier

No external data. The carrier is:

```
CHSH scenario         2 x 2 settings, 16 deterministic response types
five-context scenario 5 x 5 settings, 1024 deterministic response types
                      (A, B) with A, B subsets of Z/5 the LOW sets
table P               as displayed in (C5), transcribed from
                      probes/P-QDD-SELECTED-BIPARTITE-LAW-1/RESULT.md at
                      main f8a77855; the verifier re-derives B(P) = 35/16,
                      both LOW marginals 1/4 and E(x,y) = 1/16 + (15/16)
                      delta_xy before using it
random families       seeded rational counter models, |Lambda| from 1 to 6,
                      denominators up to 12, at least 400 models per
                      scenario, for (C1), (C2), (C3), (C4), (C6) bounds
explicit families     eps in {0, 1/16, 3/128, 1/7, 1/3, 1/2, 2/3, 1} for
                      the attaining constructions
```

## 4. Systematics

```
wrong table          guarded: normalization, marginals, correlator and
                     B(P) = 35/16 asserted before use
wrong functional     guarded: local bound 2 recomputed by exhaustion over
                     1024 types (3c - ab <= 2), matching the canon proof
symmetry shortcut    guarded: the dual certificate is checked on every one
                     of the 1024 types with no symmetry assumption; the
                     primal point is expanded to explicit types and
                     compared entrywise with P
lemma direction      guarded: both directions of the (C5) lemma are
                     constructed explicitly and their eps computed
irrational target    guarded: 2 sqrt 2 handled only in Q(sqrt 2)
float                none
architecture         byte-identical stdout on two architectures
```

## 5. Failure threshold

ONE failed exact assertion fires the falsifier. In particular: any counter
model with |S| > 2 + 2 eps, B > 2 + 8 eps, or signalling above eps; any
explicit construction missing its exact value or its exact eps; a dual
certificate violated on any of the 1024 types; a primal point that fails
nonnegativity or does not reproduce P exactly; any eps below 1/16 found to
reproduce P. The claims are additionally asserted as T by derivation; if
the verifier fires, the derivation dies with it. No tolerance, no exception
list, no threshold movement after execution. A verifier crash is
UNRESOLVED, not PASS and not F.

## 6. Action layer

L6, measure: the objects are occurrence tables p(a,b|x,y). Pure finite
theorem on the comparison classes. No lift to L1 through L5 and no
physical identification is claimed.

Explicitly NOT part of this candidate: any statement that the TWIST-J
counter is or is not setting dependent; any choice among latent-variable,
nonlocal, superdeterminist or retrocausal explanations; any empirical
claim; any change to BELL-CAUSAL-ACCOUNTING or QDD-SELECTED-PAIR-LAW.
