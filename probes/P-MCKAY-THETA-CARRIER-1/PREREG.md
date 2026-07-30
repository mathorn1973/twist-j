# P-MCKAY-THETA-CARRIER-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN PENDING REMOTE PIN READBACK

This document freezes one proof-first public no-go probe. It contains no
formal gate output and earns no scientific status. Formal execution is
forbidden until this exact revision and `verify.py` are committed, pushed,
and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          J-LI
probe:            P-MCKAY-THETA-CARRIER-1
public lock:      issue 57
owner:            A. M. Thorn
branch:           probe/P-MCKAY-THETA-CARRIER-1
path:             probes/P-MCKAY-THETA-CARRIER-1/
action layer:     L6 spectral multiplicity; E8 functional-calculus carrier class; no further lift
scientific state: candidate proof-first no-go; RH and every replacement
                  carrier remain open
```

Authority base is Public Canon v8, tag `canon-v8`, content commit
`208124ac19dbdc65c6f1cc80616ce55dbbceac51`, Canon SHA-256
`eabf29bc8058fa42104b53b44b0e6db3f02540f48fa79b54d5873c4f4fb09d0b`,
Canon byte count 65077. The probe earns at most public status `T` by the
proof frozen below; `verify.py` is an exact audit of the finite witnesses,
not the source of the theorem. The two-architecture gate is the local
`aarch64` record plus the required GitHub `x86_64` check; no prior
run is carried in as the public pin.

## Frozen preregistration body


```
CANDIDATE:  P-MCKAY-THETA-CARRIER-1
SESSION:    r4-execution-2026-07-17 (one session, one owner, this doc claims it)
DIRECTIVE:  owner "Ok. Tak jdi na to." on the mining note extraction list
            (the plenum mining note, item E2).
TARGET:     public line on promotion. This probe carries no authority until public validation.
LAYER:      L6 (measure and spectral multiplicity). Any lift is a separate gate.
STATUS:     candidate. Expected honest outcome, stated up front: the route
            FIRES as candidate-F and the paired no-go lands as candidate-T.
```

## 0. Currency (verified this session, before this freeze)

```
public head   STATUS.md: STATE ACTIVE, Public Canon v8, tag canon-v8,
              CONTENT_COMMIT 208124ac19dbdc65c6f1cc80616ce55dbbceac51,
              CANON_SHA256 eabf29bc...fb09d0b, 65077 bytes.
verified      canon/CANON.md fetched and hashed this session:
              eabf29bc8058fa42104b53b44b0e6db3f02540f48fa79b54d5873c4f4fb09d0b,
              65077 bytes. Match.
RH lane rows  public: J-LI-TORAL-HAAR-NOGO [T], PENTAGON-NORMALIZATION [T].
              Not yet public: S2 normal form, cyclic carrier no-go,
              pentagon-only dilations (packaged 2026-07-17, pending owner).
E8 edge       public: COLOR-CORE-2I [T] (2I = SL_2(F_5)), COLOR-MCKAY-E8 [T]
              (affine E8 via the spin row). The J-to-E8 derivation edge the
              route relies on is already public theorem-grade.
```

## 1. Scope check (pre-freeze recon, the mining note's mandatory first move)

The frozen analytic-nuclear line (Q-MOMENT, prior lane) reads "exponential
singular-value carriers excluded". The heat semigroup exp(-t Delta) on
R^8 / E8 has singular values decaying stretched-exponentially,
exp(-c n^(1/4)) (Weyl counting in dimension 8). The frozen wording does not
unambiguously cover alpha = 1/4. Conclusion of the check: the free F is not
free; the kill must be PROVED, not cited. This candidate proves a stronger
kill (multiplicity mechanism) that covers the whole functional-calculus
class at once, heat included.

## 2. Claim under test (the route R4 carrier form)

There exists a function f from the Laplace spectrum of the McKay torus to
[0, infinity) such that A = f(Delta_{E8}) is a positive trace-class operator
on L^2(R^8 / E8) and

    det_1(I - t^2 A) = Xi(t) / Xi(0)     as entire functions,

with Xi(t) = xi(1/2 + i t) the completed Riemann xi. This is the G8 target
of the S2 candidate, specialized to the shell-constant carrier class.
Special cases inside the class: f(q) = exp(-t q) (heat, any t > 0),
f(q) = q^(-kappa) off the kernel (kappa > 4 in dimension 8), and
Laplace-transform weights f(q) = integral w(t) exp(-t q) dt whenever the
resulting f(Delta_{E8}) is trace class.

## 3. Frozen equations and imports

```
E1  Spectral model. Characters chi_v, v in E8 (self-dual, D8+ model);
    Laplacian eigenvalue kappa0 |v|^2 for a fixed positive normalization
    kappa0 (irrelevant: f absorbs it). Shells |v|^2 = 2n, size r(2n);
    the zero shell is the constant mode, dimension 1.
E2  Import THETA-E8 [classical]. Theta_{E8} = E4, hence r(2n) = 240 sigma_3(n)
    for every n >= 1; every shell occupied; shell floor 240.
    Witness in the verifier: exact enumeration n = 1, 2, 3.
E3  Import W-RVM [classical, weakened frozen form]. For T >= 3,
        | N(T) - M(T) - 7/8 | <= E(T),
        M(T) = (T / 2 pi)(log(T / 2 pi) - 1),
        E(T) = (1/2) log T + (1/2) log log T + 5,
    N(T) counting zeros of zeta with 0 < Im rho <= T WITH multiplicity.
    Dominated by Rosser 1941 (0.137, 0.443, 1.588) and by Trudgian 2014
    (0.112, 0.278, 2.510) on T >= 3; the verifier consumes only this
    deliberately weakened form, so constant-version variance is absorbed.
E4  Import PI-ENCLOSURE [classical].
        3141592653589793 / 10^15 < pi < 3141592653589794 / 10^15.
E5  Import DET1-HADAMARD [classical]. For A positive trace class the ordinary
    trace-class Fredholm determinant, in the public J-LI convention,
        det_1(I - t^2 A) = prod_j (1 - t^2 a_j),
    over the nonzero eigenvalues a_j > 0 with multiplicity, is an even entire
    function of order <= 2 whose zero set is { +- a_j^{-1/2} } with the
    eigenvalue multiplicities. No det_2 exponential regularization is used.
```

Forced-spectrum lemma (proved here, self-contained modulo E5; no external
document needed). Assume the claim of section 2 holds with A >= 0 trace
class, so det_1(I - t^2 A) = Xi(t)/Xi(0) with Xi(t) = xi(1/2 + i t).

- By E5 the left side is even with real zeros { +- a_j^{-1/2} }, of the
  eigenvalue multiplicities; positivity a_j > 0 makes them real.
- The right side vanishes exactly where 1/2 + i t = rho for a nontrivial
  zero rho = beta + i gamma, that is at t = (rho - 1/2)/i = gamma + i(1/2 - beta),
  with the zero's multiplicity. Xi is even, so these come in +- pairs.
- Matching the two zero multisets forces every such t real, hence beta = 1/2
  for every zero (all zeros on the critical line) and t = gamma. Equating
  magnitudes, a_j^{-1/2} = |gamma|, so a_j = gamma^{-2}.

Therefore the nonzero spectrum of A is exactly { gamma^{-2} } over ordinates
gamma > 0, the multiplicity of gamma^{-2} equals the zero multiplicity
m_gamma, and the eigenvalue count with multiplicity up to ordinate T is the
standard zero-counting N(T). The lemma assumes the determinant identity (the
object under refutation) and derives its forced spectrum; it neither assumes
nor proves RH.

## 4. Carrier and dataset

The E8 lattice in the D8+ model. Nothing else. The zeta side enters only
through the unconditional counting import E3. No zero locations, no primes,
no Li coefficients, no Xi values are inputs.

## 5. Code and environment (frozen before the code exists)

```
verifier    verify.py
            Python stdlib only; exact rational arithmetic (Fraction);
            rigorous log enclosures by atanh series with dyadic argument
            reduction and exact geometric tail bounds; interval endpoint
            products for signed multiplication; no float in any assertion;
            decimal prints are labeled witnesses only.
run         first formal local leg must be aarch64/arm64 after remote pin
            readback and must repeat byte-identically three times. The required
            GitHub x86_64 leg is the later public gate; neither is claimed
            here. File sha256 is recorded before the first run.
env         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

## 6. Failure threshold (the no-go FAILS to establish if any gate fails)

```
G1  N(200) lower bound: M_lo(200) - 7/8 - E_hi(200) >= 68.
G2  N(5) upper bound:   M_hi(5) + 7/8 + E_hi(5) < 6      (so N(5) <= 5).
G3  uniform multiplicity on 5 <= gamma <= 200:
        m_gamma <= N(gamma + 1) - N(gamma - 1)
                <= (1/pi) log(201 / 2 pi) + 2 E(201) =: D,  gate D < 19,
    hence m_gamma <= 18 there; with G2, m_gamma <= 18 for ALL gamma <= 200.
G4  18 < 240 (max forced multiplicity below the shell floor).
G5  distinct forced eigenvalues >= ceil(68 / 18) = 4 > 1 = the carrier's
    small-multiplicity slots (the single constant mode f(0)).
G6  E8 shells by exhaustive enumeration: r(2) = 240 = 240 sigma_3(1),
    r(4) = 2160 = 240 sigma_3(2), r(6) = 6720 = 240 sigma_3(3).
G7  log-enclosure sanity: 6931/10000 < log 2 < 6932/10000.
```

## 7. Falsifiers

```
Of the no-go     any gate G1..G7 fails; or anyone exhibits an explicit f
                 with a valid determinant identity (which would also prove
                 RH and win a larger prize than this candidate).
Of the route     the expected outcome: the theorem stands, the route fires
                 as candidate-F, Lane A stays R1, R2, R3, and Theta_{E8}
                 survives only as a positivity source on the moment side,
                 folded into the generic moment lane, not as a carrier.
```

## 8. Not covered (frozen honesty)

Non-shell-constant translation-invariant operators (per-character weights);
operators not commuting with translations; orbifold quotients of the torus;
the Mellin or positivity-source use of Theta on the moment side; any bearing
on RH itself. RH [O] before, during, and after this candidate.

## 9. Break-it-yourself plan (to be executed and recorded in the PROMO)

```
a  per-character weights            escape? outside the frozen class: note.
b  Laplace-weight integrals of heat covered: they are f(Delta).
c  merging f values across shells   covered: merging only raises multiplicity.
d  f(0) placement                   covered: at most one small slot, merged
                                    or not; kernel placement only removes it.
```
