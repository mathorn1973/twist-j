# PREREG C-SUZUKI-LOCAL-CAPACITY-NOGO-1

```text
DATE       2026-08-13 (UTC). FROZEN BEFORE THE VERIFIER WAS WRITTEN.
CANDIDATE  C-SUZUKI-LOCAL-CAPACITY-NOGO-1. No authority. Incubation lane of
           the TWIST-J project. One named session, this candidate only:
           the 2026-08-13 prime-capacity session (owner directive "claimni
           prereg a zacni inkubaci").
TARGET     public mathorn1973/twist-j on promotion. Gated this session:
           STATE ACTIVE, Public Canon v46, TAG canon-v46, CONTENT_COMMIT
           62628ca4, both ancestors of main (HEAD 6545c1d0), SHA256SUMS
           5 of 5 OK.
COLLISION  scan clean this session: no Suzuki, screw, capacity or plastic
           lane in project docs, twist-j notes/, probes/, or REGISTRY.tsv.
           Nearest rows: the J-LI carrier no-go family (different carriers),
           LAMBDA-COCYCLE-ANGLES [H] (untouched).
LAYER      L1 (state; classical real analysis of one scalar function and
           finite Gram data). No lift to L2..L6 is claimed.
```

## Definitions (frozen)

Prime side and completion capacity of Suzuki's screw function for the
Riemann zeta function, in the normalization of Mittermeier eq. (9), termwise
equal to Suzuki's archimedean part (S-A below):

```text
P(t)  = sum_(p^k <= e^t) (log p) p^(-k/2) (t - k log p)         (t >= 0)
S(z)  = sum_(k >= 0) z^k / (4k+1)^2                              (0 < z < 1)
A(t)  = 8 (cosh(t/2) - 1) - alpha t + C - 4 e^(-t/2) S(e^(-2t))  (t > 0)
alpha = (log pi - psi(1/4)) / 2      [= (log(8 pi) + gamma_E + pi/2)/2]
C     = psi'(1/4) / 4                [= pi^2/4 + 2 G_Catalan]
Psi   = A - P.   A(0) = 0 by trigamma(1/4) = pi^2 + 8 G.
K_F(s,t) = F(s) + F(t) - F(|s-t|)    (screw combination of a function F)
```

## Prior art and attribution (frozen; no novelty is claimed over these)

```text
S-A  M. Suzuki, JLMS 108 (2023) 1448-1487, arXiv:2206.03682: Psi, the
     criteria RH iff Psi >= 0 (Thm 1.7), RH iff Psi = O(1) (Thm 1.6),
     screw kernel (Thm 1.2). NOTE: the recon cited volume 107; correct is
     108 per Mittermeier's reference list.
M-4  R. A. Mittermeier, "Prime-Power Checkpoints ... Plastic-Constant
     Convexity and a Restricted Legendre-Mangoldt Representation",
     Zenodo 10.5281/zenodo.21805557 (2026). OWNS the closed form
     A''(t) = e^(t/2) + e^(-t/2) - e^(-t/2)/(1 - e^(-2t)) and the
     plastic-constant transition at log rho, rho^3 = rho + 1, before
     log 2. This candidate's A2 gates are REPRODUCTION of M-4, by an
     independent implementation (different language, different interval
     method, separately developed prime stream), which is exactly the
     validation target M-5 names as its Route F.
M-5  R. A. Mittermeier, Zenodo 10.5281/zenodo.21838882, v5, 2026-08-08,
     verified this session from owner-supplied files:
     pdf sha256 37e8642bd7a15affffb12521392301276b5dbaa7973ef136b7f8150a764fffa9
     zip sha256 c86eb0770785371a8349d8d21c9a3fdd3ab4482b879a7ecb59fc06eebaa4ac89
     zip-internal SHA256SUMS 30 of 30 OK. Theorem 1.1: all 455,062,595
     event segments through q = 10^10 close positive; smallest certified
     bound 0.0214985598... at q = 34,186,367; flags rh_proved = false,
     infinite_tail_proved = false. Also: the trichotomy census C4, the
     barrier B(x) with (38)-(41), open obligations 7.4, 8.1, 9.1, 10.1.
     This candidate's A6 gate reproduces a corner of Theorem 1.1's domain
     by an independent code path; nothing beyond that corner is claimed.
S-C  Suzuki arXiv:2606.09096; K-9 Kim et al. arXiv:2607.24830; CCM-10
     Connes-Consani-Moscovici arXiv:2511.22755: operator stream, context.
```

## Field 1. EQUATION (frozen claims)

Novel claims (N) and reproduction gates (R). Every claim is about the frozen
A, P above. "Certified" means the stdlib verifier's outward-rounded
enclosures separate the stated sign at the frozen precision.

```text
N1  PRIME CURVE IS A CANONICAL ORTHOGONAL-INCREMENT PATH    candidate-T
    For ANY locally finite event family {(tau_q, omega_q)} with tau_q > 0,
    omega_q >= 0, the direct-sum curve Y_t = (+)_q omega_q 1_[tau_q, t]
    satisfies (i) ||Y_t||^2 = F(t) := sum omega_q^2 (t - tau_q)_+,
    (ii) <Y_s, Y_t> = F(min(s,t)), (iii) <Y_t - Y_u, Y_u> = 0 for u <= t,
    (iv) ||Y_t - Y_u||^2 = F(t) - F(u). Specialization to prime powers
    gives P. Proof: finite additivity of interval overlaps (4 lines,
    attached in the result doc). GATE V1: exact Fraction verification of
    (i)-(iv) on the frozen surrogate family
    tau = (1, 3/2, 2, 7/3), omega = (2, 1/2, 1, 3/4),
    times (1/2, 1, 5/4, 3/2, 2, 9/4, 3), computed componentwise from
    overlap integrals, NOT from the identity being tested; plus the frozen
    negative control (component 2 left endpoint moved to 5/4 in the
    difference vector only) must break (iii).
    FALSIFIER: any exact instance where (i)-(iv) fails.

R2  CURVATURE AND PLASTIC TRANSITION (reproduction of M-4)   candidate-T,
    attribution M-4; no novelty claimed.
    (a) A''(t) = e^(t/2) + e^(-t/2) - e^(-t/2)/(1 - e^(-2t)) for t > 0.
        GATE V2a: geometric-series consistency at t in {1/4, 1/2, 1}:
        the partial sum of sum_(n>=0) e^(-(2n+1/2)t) plus its rational
        tail enclosure must intersect e^(-t/2)/(1-e^(-2t)), both widths
        below 2^-100. GATE V2r: algebraic cross-check against M-5 eq. (12):
        A''(log 2) must enclose 5 sqrt(2)/6 and A''(log 3) must enclose
        23 sqrt(3)/24.
    (b) With h(y) = y^3 - y - 1: h is strictly increasing on y >= 1
        (h' = 3y^2 - 1 > 0 there), h(13/10) = -103/1000 < 0,
        h(4/3) = 1/27 > 0, so the unique real root rho (plastic) lies in
        (13/10, 4/3) and log rho < log 2. A'' < 0 on (0, log rho),
        A'' > 0 on (log rho, infinity).
        GATE V2b: the two exact Fraction sign evaluations of h, the exact
        h' positivity witness at the bracket endpoints, certified
        A''(1/4) < 0, certified A''(log 2) > 0.
    FALSIFIER: any certified sign contradicting (a) or (b).

N3  RAMP-CLASS EMPTY (the local Bessel decoder class is empty)
                                          candidate-T; the class carries F.
    No c0, c1 in R and locally finite Borel measure mu >= 0 on [0, inf)
    give A(t) = c0 + c1 t + integral (t-a)_+ dmu(a) on (0, inf). Reason:
    every member is convex; A is not convex on (0, 1/2). The completion
    capacity is NOT a positive superposition of the prime-type ramp atoms
    (P'' = sum w_q^2 delta >= 0 always; A'' < 0 before log rho by R2).
    GATE V3: certified three-point convexity violation at the frozen
    triple (1/20, 1/4, 1/2):
    (A(1/4) - A(1/20)) * (1/2 - 1/4)  >  (A(1/2) - A(1/4)) * (1/4 - 1/20),
    enclosures strictly separated.
    FALSIFIER: enclosures fail to separate at frozen precision (UNDECIDED,
    recorded) or separate with the opposite sign (fires N3 to F).
    Novelty scope: the inequality is an easy corollary of R2; what is
    claimed as new is the classification statement (this decoder class is
    EMPTY) in the sense of the RH-decoder gate frame.

N4  FILTRATION AND DOMINATION KILLS                          candidate-T
    (a) A is not nondecreasing on (0, log 2): certified A(1/4) > A(1/2).
        Hence no filtration model Z_t = 1_[0,t] in L^2(dA) exists there
        (dA is not a nonnegative measure).
    (b) Certified (log 2 / sqrt 2) * (4/5 - log 2) > A(4/5) - A(log 2).
        On (log 2, log 3) the prime side is the single ramp
        P(t) = (log 2/sqrt 2)(t - log 2) exactly, so increment domination
        dP <= dA fails on [log 2, 4/5]: the increment-diagonal contraction
        dies at the FIRST event. COROLLARY: no decomposition of dA into
        nonnegative per-place budgets dominates the prime ramps (the total
        already fails). Convergent operator-level statement in M-5 sec. 9
        ("a proof cannot assign an independent positive contribution to
        each prime power"), cited, not imported.
    GATES V4a, V4b: the two certified separations.
    FALSIFIER: per gate, as in N3.

N5  BOTH SCREW KERNELS ARE SEPARATELY INDEFINITE             candidate-T
    4A(3) - A(6) < 0 and A(6) > 0; 4P(3) - P(6) < 0 and P(6) > 0,
    certified. Hence det of the 2x2 section of K_A (and of K_P) at (3,6)
    is negative: neither the capacity alone nor the prime side alone is a
    screw geometry; only the difference kernel K_A - K_P = G_g can be
    (S-A Thm 1.2, iff RH). Fences off any "difference of two positive
    screw geometries" shortcut.
    GATE V5: the four certified signs. Event-boundary guards: certified
    e^3 in (20, 23) and e^6 in (401, 409) so the prime-power lists
    {q <= 20} and {q <= 403} are exact.
    FALSIFIER: per gate, as in N3.

R6  PRIME-FREE WINDOW POSITIVITY (independent corner of M-5 Thm 1.1)
                                          candidate-T; attribution M-5.
    A(t) > 0 for every t in [1/128, 45/64]. On (0, log 2), Psi = A, so
    this is the unconditional prime-free positivity window, reproduced by
    adaptive bisection with outward interval arithmetic (independent of
    MPFR, of C, and of M-5's event stream).
    GATE V6: every leaf of the adaptive cover certified positive; depth
    cap 24; a cap hit is UNDECIDED, recorded, fires nothing.
    The sliver (0, 1/128) is remark-grade here (log-divergence of the
    S-block lower bound), no gate.
    FALSIFIER: a certified negative leaf. That would contradict M-5
    Theorem 1.1 and, through S-A Thm 1.7, RH itself; per house rule any
    such firing is FIRST an integrity STOP pending independent audit.

R7  EVENT-COUNT CONSISTENCY (method of M-5 C3 at small X)    candidate-C
    N(10^6) computed two ways, direct prime-power enumeration versus
    sum_k pi(floor(10^(6/k))), exact integer equality. GATE V7.
    FALSIFIER: inequality of the two integers.

N8  NO STRICT CONTRACTION (norm one forced)      candidate-T by proof only
    Any T with T Z_t = Y_t, ||Z_t||^2 = A(t), ||T|| <= 1 - delta,
    delta > 0, forces Psi >= delta A, contradicting Psi(t) = o(e^(t/2)),
    which follows unconditionally from PNT (NAMED IMPORT, not proved
    here). Hence ||T|| = 1 exactly. NO MACHINE GATE (asymptotic claim);
    carried by the written proof in the result doc.
    FALSIFIER: a proof of a uniform strict contraction (would refute PNT).

SYNTHESIS (carried in scope, not a separate gate): N3 + N4 + N5 together
say every Gram realization of the capacity dominating the prime curve is
NONLOCAL in t; with the recon 11.2 diagonal-model lemma, bare existence of
a contraction pair is verbatim RH, so all remaining content in the
completion-Gram lane (future C-SUZUKI-COMPLETION-GRAM-N) is in the frozen
canonicity class, exactly the decoder-note G0 discipline.
```

## Field 2. CODE

```text
verifier   verify_suzuki_local_capacity_nogo_1.py
breaker    breaker_suzuki_local_capacity_nogo_1.py (independent path)
rules      verifier: Python 3 standard library only; integers and
           Fractions only; scaled-integer outward-rounded interval
           arithmetic at scale 2^-192; no float object anywhere in the
           verifier; no timestamps; deterministic stdout; under 120 s;
           env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
           TZ=UTC. Constants: pi by Machin with alternating-tail bounds;
           log of rationals by dyadic range reduction plus atanh series
           with geometric tail; exp of scaled rationals by Taylor with
           factorial tail; psi(1/4), psi(3/4), psi'(1/4), psi'(3/4) by
           exact downward recurrence from a = 100 + fraction plus the
           classical asymptotic expansions with remainder bounded by the
           first neglected term (NAMED IMPORT: DLMF 5.11(ii) error form
           for psi and the corresponding polygamma bounds; completely
           monotone integrands). Internal cross-gates: psi(3/4) - psi(1/4)
           must enclose pi; psi'(1/4) + psi'(3/4) must enclose 2 pi^2.
           sqrt of integers by integer bisection brackets.
breaker    may use mpmath (independent second path); recomputes every gate
           quantity at dps 50, scans for tighter counter-triples, and
           perturbs alpha by +-10^-6 to test robustness; reports
           discrepancies; asserts nothing the verifier depends on.
```

## Field 3. CARRIER OR DATA

Classical Riemann zeta over Q. The frozen A, P, constants above. Prime
powers from an inline sieve; the only external artifacts consumed are none
(M-5 files are context and attribution, not inputs to any gate). All gate
points and windows are the frozen rationals stated in Field 1.

## Field 4. SYSTEMATICS

All truncations carry explicit rational tail bounds (geometric, factorial,
first-neglected-term). Outward rounding everywhere; comparisons of scaled
integers are exact. Event-boundary decisions are guarded by V5's e^3, e^6
enclosures. The two psi reflection cross-gates guard the constant
machinery. Discretization is absent by design (no derivatives are gated;
only function values and exact algebra).

## Field 5. FAILURE THRESHOLD

Zero tolerance on exact gates. A non-separating enclosure at the frozen
precision or the V6 depth cap is UNDECIDED: recorded, fires nothing,
moves nothing. A certified opposite sign fires that claim to F and is
archived. A defect shown to be in the verifier is an integrity STOP,
recorded with both hashes; the corrected verifier is archived alongside,
never substituted silently. No threshold moves after this freeze. A V6
negative leaf is first an integrity STOP (see R6).

## Field 6. ACTION LAYER AND NON-CLAIMS

```text
Layer L1 throughout. No lift claimed.
NOT CLAIMED  any progress on RH or on zeta zeros; any statement about the
             infinite tail (M-5 obligations 7.4, 8.1 remain M-5's);
             novelty of Psi, of the criteria (S-A), of the curvature and
             plastic transition (M-4), of the 10^10 strip (M-5);
             any J-coupling, p = 5 structure, or physical reading;
             any evidential value of finite positivity scans beyond the
             named windows (rank-diagnosis discipline).
FENCED       the counter resonance (prime events as ticks, orthogonal
             increments) stays motivation only, per the owner's rule.
```

FROZEN 2026-08-13 before the verifier was written. The SHA-256 of this file
is recorded in the run record and the result doc.
