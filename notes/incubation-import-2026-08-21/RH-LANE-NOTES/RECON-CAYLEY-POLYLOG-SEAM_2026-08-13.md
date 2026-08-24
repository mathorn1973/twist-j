# RECON: the J-Cayley polylog seam view, verified, with three sharpenings

```text
Status     NON-CANONICAL recon of the owner-forwarded third view
           (J-Cayley path, Mellin bridge, renormalized edge, dilog
           closure, Li-energy chain, cocycle attack proposal). No lane
           opened, no authority, no public change. RH remains O.
Date       2026-08-13, night. Basis Public Canon v46, main 6545c1d0
           (unchanged through this session).
Witnesses  mpmath dps 30 readouts, labeled; algebra checked by hand where
           stated. One harness typo of THIS session in the circle
           parametrization check was found and fixed; the identity itself
           is correct (diff 1e-31 after the fix). Recorded for honesty.
```

## 1. Verified [T unless noted; witness grades in brackets]

```text
V1  Cayley = order-zero polylog: 1 + Li_0(z) = 1/(1-z) = exp(Li_1(z));
    at J: 1 + Li_0(J) = e^(i pi/5) = -j^3.                     [1e-31]
V2  Cayley triangle of order three: f(z) = 1/(1-z), f^3 = id;
    J -> e^(i pi/5) -> phi j -> J with radii 1/phi -> 1 -> phi.
    Six-point anharmonic orbit {J, Jbar, 1/J, 1/Jbar, e(+-i pi/5)}:
    verified elementwise (J/(J-1) = Jbar, (J-1)/J = 1/Jbar).    [1e-31]
V3  Time reversal is the functional equation: C_J(-t) = 1 - C_J(t)
    [1e-33], hence xi(C_J(t)) is EVEN in t. Critical line is exactly
    Re(t Log J) = 0; circle parametrization 1/(1-e^(i a)) =
    1/2 + (i/2) cot(a/2)                                        [1e-31]
    and a = 2 arctan(1/(2 gamma)) as in the public rows.
V4  Radial/angular split of the cocycle hypothesis:
    1 - |w_rho|^2 = (2 beta - 1)/|rho|^2, so beta = 1/2 iff
    |w_rho| = 1. LAMBDA-COCYCLE-ANGLES [H] therefore splits EXACTLY as
    (radial condition = RH) + (angular condition = five-torsion grid),
    and the angular part is strictly extra. This is the cleanest
    statement of that row's burden this session has seen; any future
    cocycle prereg should quote it.                             [algebra]
V5  Mellin bridge: int_0^inf u^(q-1) Li_s(J^u) du =
    Gamma(q)(-Log J)^(-q) zeta(s+q) (Re q > 0, Re(s+q) > 1,
    arg(-Log J) inside (-pi/2, pi/2) so principal powers are safe);
    s = 0 gives zeta(q) from the Cayley path C_J(u) - 1.
    Witness at q = 5/2: quad diff 1.3e-6 (truncation).        [derived]
V6  Renormalized edge: R_J(s,u) = Li_s(J^u) - Gamma(1-s)(-u Log J)^(s-1)
    satisfies d/du R = (Log J) R(s-1, u) [1e-16 numeric], R(s,0) =
    zeta(s) [3e-10 at u = 1e-9], all normal derivatives
    (Log J)^k zeta(s-k). The naive limit Li_s(J^u) -> zeta(s) FAILS on
    the strip; the subtraction is mandatory. Matches recon
    POLYLOG-SURFACE B1.
V7  Zero-motion readout: for a simple zero, rho_J'(0) =
    -(Log J) zeta(rho-1)/zeta'(rho). At rho_1 the readout is
    -0.9363810562 + 1.8562309270 i: REAL PART NONZERO, so the natural
    J-deformation does not preserve the critical line. The view's own
    falsifier expectation is confirmed by computation; any bridge must
    stand on renormalization plus global symmetry, not on zero
    transport.                                                  [readout]
V8  Dilog closure: D(J) = D(e^(i pi/5)) = Cl_2(pi/5) (Bloch-Wigner
    invariance under the order-three cycle), hence with the public
    Re Li_2(J) = pi^2/100:
    Li_2(J) = pi^2/100 + i (Cl_2(pi/5) - pi log(phi)/5).        [1e-31]
V9  Weight-2 circle energies: zeta(2) - Re Li_2(e^(i theta)) =
    theta(2 pi - theta)/4; at pi/5 and 2 pi/5 exactly 9 L2 and 16 L2
    with L2 = pi^2/100; closure Re Li_2(sigma_2(J)) +
    Re Li_2(e^(i pi/5)) = zeta(2).                       [1e-31, exact]
V10 Weight-q circle energy: sum n^(-q)(1 - cos n a) = zeta(q) -
    Re Li_q(e^(i a)) [3e-8 truncation]; under RH the Li-energy chain
    sum lambda_n n^(-q) = 2 sum_(gamma>0)[zeta(q) - Re Li_q(w_rho)]
    for q > 2 is a correct rearrangement with correct exponents
    (absolute convergence from alpha_gamma ~ 1/gamma).
V11 The unified Mellin formula of section 11 is consistent on its
    stated domain (q > 1; the u -> 0 blowup of log xi(C_J(u)) is
    exactly compensated).                                       [derived]
```

The three [F] guards of the view (no Euler product for J^n; e^(i pi/5)
is a control point, not a zero phase; no raw strip limit) are all
correct and should freeze with any lane.

## 2. Three sharpenings

```text
C1  The section-10 candidate criterion (RH iff sum lambda_n n^(-q)
    converges for at least one real q) has a SOUND skeleton: divergence
    from an off-line zero is exactly the radius-of-convergence argument,
    since beta > 1/2 puts w_rho strictly INSIDE the disk (V4). But the
    mechanism is the one in Li 1997, and growth-form equivalents live in
    Bombieri-Lagarias, "Complements to Li's criterion" (1999). VERDICT:
    probably classical; import audit against those two before any
    claim; at best a candidate-D repackaging, not a new criterion.
C2  The section-13 Toeplitz falsifier family ALREADY EXISTS IN-HOUSE:
    notes/j-li-schoenberg-2 carries RH iff T_N >= 0 for the second
    differences t_n (equivalence at mathematical-T grade), the congruence
    K_N = (1/2) L T L*, and two interval gates candidate-T-ready;
    LI-COCYCLE-LANE_CONSOLIDATION_2026-07-16.md is the cross-branch
    source of truth. The collision audit the view itself requests closes
    POSITIVE: extend that bundle, do not open a duplicate.
C3  The five-adic uniform continuity of m -> t_(4m) is a TRUE necessary
    consequence of the grid (atom of level a depends on m mod 5^a; the
    tail mass bounds the discrepancy), but it is NOT finitely
    falsifiable as stated: no convergence RATE is forced, so any finite
    discrepancy can hide in the tail. The workable finite falsifier is
    the GRID-CONSTRAINED MOMENT FEASIBILITY: given certified rational
    enclosures of t on a finite index set, decide by exact LP/SDP
    whether ANY positive measure supported on the 4.5^infinity torsion
    angles matches them; an infeasibility certificate fires the ANGULAR
    part of LAMBDA-COCYCLE-ANGLES without touching RH (V4 split). This
    strictly refines both plain Toeplitz positivity (full-circle
    measures) and the pointwise bounds of LAMBDA-COCYCLE-BRANCH-COLLAPSE.
    This is the genuinely new gate in the view, once restated this way.
```

## 3. Lane reconciliation (proposals, nothing opened)

```text
L1  C-J-CAYLEY-POLYLOG-SEAM-1-N: ADOPT this name and let it absorb the
    C-LERCH-SURFACE-CIRCLES-1 draft of RECON-POLYLOG-SURFACE (same
    territory; the third view goes deeper). Theorem layer at freeze:
    V1-V3, V5-V6, V8-V9 as exact verifier gates (all certifiable with
    the house interval machinery), V7 as a pinned readout, the three
    [F] guards frozen, plus the POLYLOG-SURFACE brakes BR1-BR4
    (Lagarias-Li prior art, grid independence, ordering).
L2  C-LI-GRID-MOMENT-FEASIBILITY-1-N: the C3 gate family as an
    EXTENSION of notes/j-li-schoenberg-2 (owner decision D-B of the
    decoder note already asks to consolidate the Li complex). Targets
    the angular [H] specifically; unconditional; finite; falsifiable.
L3  Ordering unchanged: merge wave (BR-2, BR-3), push of
    C-SUZUKI-LOCAL-CAPACITY-NOGO-1, G0 freeze for the capacity
    classification, THEN these two, on the owner's word.
```

No summary of this recon may exceed: identities verified, one criterion
flagged as probably classical, one falsifier family relocated to its
existing home, one genuinely new finite gate distilled. RH remains O.

## 4. ADDENDUM, 2026-08-13 later: both lanes landed publicly, and L2 is dead

Two audited branches were pushed by the parallel session and verified here
from a fresh fetch (tips match the reported commits, main unchanged at
6545c1d0; check_policy, check_canon, check_ledger PASS on main; the full
tools suite reruns on this platform: 99 tests, OK):

```text
A1  notes/c-j-polylog-renormalized-seam-1-n (issue #362, bbb25f64):
    typed J-Cayley coordinates, Mellin identity, Jonquiere renormalization,
    simple-zero velocity, Li polylog energy. Collision map correct and
    complete (including ELECTRON-G-RATIO owning the Li_(-1..1) ladder at J,
    which this recon had not flagged). SUPERSEDES the L1 proposal of
    section 3; nothing further to open there.
A2  notes/c-lambda-cocycle-z5-fourier-normal-form-1-n (issue #363,
    3514cef5): the exact Z_5 Fourier normal form (E1-E4), conductor-tail
    identities R_A = M - Cesaro limit and R_A <= delta_A <= 2 R_A with the
    sharp factor two, and the ATTACK theorem: for any STRICTLY positive
    finite Toeplitz profile there exist exact grid-carried representing
    measures with ANY tail mass in [0, M] and with arbitrarily slow
    R_A -> 0 (dense-grid truncated moment lemma: interior of the moment
    body via Fejer-Riesz, closure/relative-interior argument,
    Caratheodory; exact rational witness mu_100 vs zeta_500 mu_100 at
    N = 12). Under RH the Cayley measure has infinitely many atoms, so
    every finite Li block is strictly positive and the no-go applies to
    the real data. It also proves, with exact hypothesis, the
    finite-profile realization statement whose overclaimed ancestor was
    withdrawn in issue #293 / PR #294.
FIRED  the L2 proposal of section 3 (C-LI-GRID-MOMENT-FEASIBILITY-1-N) is
    DEAD, killed by A2's R1: for strictly positive profiles a grid-carried
    exact realization always exists, so grid-constrained feasibility never
    discriminates beyond plain Toeplitz positivity. First-class outcome;
    this recon's C3 caution (no finite falsifiability without a rate) was
    the right instinct, and the parallel session carried it to the full
    realization theorem, which is stronger. Surviving targets are exactly
    A2's section 6: delta_A -> 0, the all-moment Cesaro averages, or one
    exact ordinate.
QUEUE  the merge wave is now four branches (BR-2, BR-3, #362, #363) plus
    the BR-1 archive decision plus the push of
    C-SUZUKI-LOCAL-CAPACITY-NOGO-1. Cross-reference discipline of the
    parallel-branch recon applies to all four.
```
