# P-COUNTER-BELL-PRICE-1 preregistration

Status: FORMAL PREREGISTRATION / PROOF-FIRST / RESULT-EXPOSED / L6 ONLY.
Owner: A. M. Thorn, Claude session counter-bell-price-20260923. Date: 2026-09-23.
Public claim: [issue #1153](https://github.com/mathorn1973/twist-j/issues/1153).
Branch: `probe/P-COUNTER-BELL-PRICE-1`.
Directory: `probes/P-COUNTER-BELL-PRICE-1/`.
Carried candidate: `C-COUNTER-BELL-PRICE-N` from the incubation lane.

## Authority, exposure and custody

Authority is ACTIVE Public Canon v91, fetched public main
`f8a77855288b5f94ea554504b3c636624ca1318a`, content commit
`b89b0c80bb5cebddade567f31a979aaf42f1d9dd`, tag `canon-v91` peeling to
`11b66d4755a697031157f0e10dc1898a7d5b6379`. `canon/CANON.md` has 772678
bytes and SHA-256
`6d49a9dfce95f2146490ccc9ae76066bca01d1614291549562b599d35b2218e1`.
Tag and content ancestry and `canon/SHA256SUMS` (5 of 5) were confirmed.
Open issues, `probes/`, the registry and explicit remote heads were scanned:
no measurement-dependence price, overlap measure, counter Bell row, probe or
branch exists. Related rows read and unchanged: BELL-MAGIC-BOUNDARY,
QDD-FIVE-CONTEXT-BELL-SEPARATION, BELL-CAUSAL-ACCOUNTING,
QDD-SELECTED-PAIR-LAW.

Exposure, disclosed in full. Every statement below was derived by hand
before any code, then frozen in the incubation preregistration carried here
verbatim as `INCUBATION-PREREG.md` (7446 bytes, SHA-256
`c412e70327439d687edcab82acfb54b4ceb185378b7c02feef4db37383bf3ad8`). The
accepted `verify.py` (17845 bytes, SHA-256
`26a6b8faaae92f9b533700f1a3bcd87d73364f4a2b59f1461cfd460e37e6e27b`) and
the independent `break.py` (SHA-256
`9ee229fdafb3e1b86d0de74aaf46fdd8f151e04a5f36e98310efa66285f9f300`) are
byte-identical to the incubation files. The verifier was executed in
incubation on x86_64 and aarch64 with byte-identical stdout (1482 bytes,
SHA-256 `083e31cacdc6324cb54d72f73bbb910de99bf7ef178926477a3f33c2274f3c0d`,
all pass); the breaker once on x86_64 (stdout SHA-256
`a1a76f8c4c358069aefdb894a94eebd1a91c0b4608e07d169ec9b58e3da2d9e7`, no
break). The verifier prints the incubation preregistration hash, which is
why that file is carried.

This probe is therefore NOT a blind prediction. The proposed status rests on
the exact proofs in `PROOF.md`; the verifier is an audit of them and of the
explicit constructions and certificates. Freeze PREREG.md, PROOF.md,
INCUBATION-PREREG.md, verify.py and break.py in one fresh commit whose sole
parent is the main above; push and read back the exact bytes before the
formal run. Never amend, rebase, squash or force-push this pin.

## Field 1: equation

Bipartite scenario, settings x, y in a finite set X, two outcome letters. A
counter model is a finite latent set Lambda, rational setting-conditional
latent laws mu_xy, and rational local response kernels alpha(a|x,lambda),
beta(b|y,lambda), alpha blind to y and beta blind to x:

    p(a,b|x,y) = sum_lambda mu_xy(lambda) alpha(a|x,lambda) beta(b|y,lambda)
    eps        = 1 - sum_lambda min_(x,y) mu_xy(lambda)

eps is the overlap dependence of the model; eps = 0 exactly when the latent
law is setting independent. Claims:

    (C1) nu = min_xy mu_xy and r_xy = mu_xy - nu satisfy nu >= 0, r_xy >= 0
         and mass(r_xy) = eps for every setting pair.
    (C2) moving the response randomness into the latent variable reproduces
         p and preserves eps.
    (C3) CHSH, X = {0,1}, outcomes +1/-1, S = E00 + E01 + E10 - E11:
         |S| <= 2 + 2 eps for every counter model; for every rational eps in
         [0,1] an explicit model with overlap exactly eps has S = 2 + 2 eps;
         S = 2 sqrt 2 needs eps >= sqrt 2 - 1 and is attained there, exactly
         in Q(sqrt 2).
    (C4) X = Z/5, outcomes L/H, B = 2 sum_k p(LL|k,k) - sum_(k!=l) p(LL|k,l):
         B <= 2 + 8 eps for every counter model, attained for every rational
         eps in [0,1]; 35/16 needs eps >= 3/128 and is attained there.
    (C5) for the complete ETH-QDD-2 table P, the minimal overlap dependence
         of a counter model reproducing P exactly is 1/16. Lemma: this
         minimum equals 1 - w*, with w* the largest weight w in
         P = w L + (1 - w) Q, L local and setting independent, Q arbitrary.
    (C6) |p_A(a|x,y) - p_A(a|x,y')| <= eps and the same for Bob, for every
         counter model; attained for every rational eps in [0,1].

Proposed status on a later separate fold: T by the proofs in PROOF.md, with
the verifier as audit. This probe changes no registry, frontier or Canon row.

## Field 2: code

`verify.py`, Python 3 standard library only, Fraction arithmetic and Q(sqrt 2)
pairs with sign decided by exact squaring, no float, pinned integer seed,
final digest line. Command from the repository root:

    python3 probes/P-COUNTER-BELL-PRICE-1/verify.py

with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
The verifier reads no file. `break.py` is an independent audit path, not a
formal gate: full exact simplex over all 1024 types without symmetry or hand
certificate (BR1), adversarial exact hill climbs against (C3) and (C4) (BR2),
a latent merge attack on (C5) (BR3), and a second reading of the table from
marginals and correlator only (BR4).

## Field 3: carrier

No external data. CHSH scenario with 16 deterministic types; five-context
scenario with 1024 deterministic types (A, B), A and B the LOW sets. The
table P, transcribed from `probes/P-QDD-SELECTED-BIPARTITE-LAW-1/RESULT.md`
at the main above:

    x = y       LL 1/4    LH 0      HL 0      HH 3/4
    x != y      LL 1/64   LH 15/64  HL 15/64  HH 33/64

The verifier re-derives normalization, both LOW marginals 1/4, the
correlator E = 1/16 + (15/16) delta_xy and B(P) = 35/16 before use. Random
families: 400 seeded rational counter models per scenario, latent sizes 1
to 6, denominators up to 12. Explicit families: eps in
{0, 1/16, 3/128, 1/7, 1/3, 1/2, 2/3, 1}.

## Field 4: systematics

    wrong table          normalization, marginals, correlator and 35/16
                         asserted before use; BR4 rebuilds P independently
    wrong functional     local bound 2 recomputed on all 1024 types as
                         3c - ab, matching the registered proof
    symmetry shortcut    the dual certificate is checked on every type; the
                         primal point is expanded to explicit types; BR1
                         solves the full LP with no symmetry
    lemma direction      both directions constructed explicitly
    model versus law     eps is a property of a model and can fall when
                         latents with identical responses merge; (C5) is a
                         minimum over all models; BR3 attacks it by merges
    irrational target    2 sqrt 2 handled only in Q(sqrt 2)
    float                none
    architecture         the required workflow compares x86_64 and aarch64
                         stdout byte for byte with EXPECTED.txt

## Field 5: failure threshold

One failed exact assertion fires the falsifier: a counter model with
|S| > 2 + 2 eps, B > 2 + 8 eps or signalling above eps; an explicit
construction missing its exact value or its exact eps; the dual certificate
violated on any type; a primal point that is not nonnegative or does not
reproduce P; any model reproducing P with eps below 1/16. The verifier then
exits nonzero and prints `FALSIFIER FIRED`. A formal stdout that differs
from the incubation stdout named above is a reproducibility STOP, recorded
and not repaired. A crash is UNRESOLVED, not PASS and not F. No tolerance,
no exception list, no threshold movement after this pin.

## Field 6: action layer

L6, measure: the objects are occurrence tables p(a,b|x,y). Pure finite
theorem on the stated comparison classes. No lift to L1 through L5.

Explicitly not claimed: that any TWIST-J latent state, including the global
counter, is or is not setting dependent; any choice among latent-variable,
nonlocal, superdeterminist or retrocausal explanations; any empirical
statement; any change to BELL-CAUSAL-ACCOUNTING, QDD-SELECTED-PAIR-LAW or
QDD-FIVE-CONTEXT-BELL-SEPARATION. A reading of Lambda as a TWIST-J plenum
state needs its own named gate.
