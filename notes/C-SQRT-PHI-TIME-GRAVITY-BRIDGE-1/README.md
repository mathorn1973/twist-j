# C-SQRT-PHI-TIME-GRAVITY-BRIDGE-1: frozen bridge contract, selector-free route

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-T clock leg, candidate-C finite check,
                        gravity leg constant by definition
ACTION LAYER:           L1 only
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        NONE (the verifier was run before any pin)
PUBLIC OBJECT LOCK:     issue #1493
TARGET ROW:             SQRT-PHI-TIME-GRAVITY [O], unchanged
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
PROMOTION:              NONE
```

The registry row SQRT-PHI-TIME-GRAVITY stays O; status and any fold are the
owner's decision.

Basis: Public Canon v101, tag `canon-v101`, content commit `421a4ec1`,
`CANON_SHA256 b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`,
`canon/SHA256SUMS` 5 of 5 OK, read at main `8b91a935` on 2026-10-14.
Layer L1 throughout. No lift is claimed.

Files in this directory:

```text
README.md                        this contract
verify.py                        exact verifier, Python standard library, no float
EXPECTED.txt                     its stdout
SqrtPhiTimeGravityBridge.lean    Lean 4 + Mathlib proof of the clock leg
```

Replay from the repository root:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-SQRT-PHI-TIME-GRAVITY-BRIDGE-1/verify.py
```

## Frozen list

```text
1 SOURCE DOMAIN     Omega_src = N_0 x {+,-}, total, no selector.
                    Y_n^eps = r_eps^s_2(n) in C8 = <eta> subset F_25^*,
                    F_25 = F_5[tau]/(tau^2 - 2), r_+ = eta = tau^3 = 2 tau = (0,2),
                    r_- = -eta = (0,3). Y is the frozen unique solution of
                    Y_0 = 1, Y_(2n) = Y_n, Y_(2n+1) = r_eps Y_n (SQRT-PHI-DIGIT-LIFT).
                    The image is all of C8 (s_2(n) mod 8 takes all eight values).

2 BRANCH EQUIV.     Y_n^- = (-1)^theta_n Y_n^+ (frozen; Lean branch_relation,
                    branch_sequence). No sign-branch selector is chosen. The contract
                    uses the row's sign-invariance alternative, not a selector.

3 READOUT           R = Theta = N(Y) = Y^6 in F_5^* = C4.
                    Not a choice among equals: on C8 every fibre of N is exactly
                    {y, -y}, so every branch-invariant function of Y factors
                    uniquely through Theta.

4 CONVENTION        PRE-UPDATE. The record of the step taken at the checkpoint
                    omega = (n, psi) is read at omega itself, from its counter n,
                    before U is applied. Forced, not a matter of taste: sigma(omega)
                    uses theta_n of the same omega. The post-update reading
                    theta_(n+1) differs from sigma's bit at 6668 of 10001 counters,
                    and native U driven by it leaves the canonical orbit at step 0.

5 Y-TO-D_CLOCK      Y_n -> Theta_n = N(Y_n) -> theta_n = q(Theta_n),
                    q : F_5^* -> C2, q = 0 on {1,4}, q = 1 on {2,3}
                    (square class, a surjective homomorphism).
                    Into the five-cycle counter only through the sigma law
                    sigma(n, psi) = z_6(psi) + 2 theta_n mod 5,
                    U(n, psi) = (n + 1, g_sigma(psi)).
                    t -> 2t mod 5 is a set map {0,1} -> {0,2}, not a homomorphism.
                    Hom(C8,C5) = Hom(C4,C5) = Hom(C2,C5) = 0 and (1/5)/(1/8) = 8/5,
                    so Y carries no phase into the tick: METRO-TICK is untouched,
                    one step of U is one counter step for either branch.
                    Read-only: D_clock is terminal and feeds nothing into U. The
                    bridge is an identity at the checkpoint, not a write into U.

6 CODOMAINS         clock:   C2, entering the five-cycle counter via sigma.
                    gravity: the constant g = 2^5 phi^2 sqrt(3 - phi), g > 0,
                             g^2 = 1024 phi^4 (3 - phi) = 5120 + 2048 sqrt5.

7 EQUALITY          For every n >= 0 and eps in {+,-}:
                      q(N(Y_n^eps)) = s_2(n) mod 2 = theta_n,
                      Grav(n, eps)  = g.
                    The complete readout B(n, eps) = (theta_n, g) is independent
                    of eps: sign invariance of the complete readout holds.

8 DEPENDENCIES      SQRT-PHI-DIGIT-LIFT [T]   source, branch law, Theta, q.
                    native U, section 2        theta_n, sigma law, U.
                    METRO-TICK [T]             only as: the bridge adds no phase.
                    GRAVITY-BRIDGE-LAW [D]     the constant g; the gravity leg
                                               inherits at most D from it.
                    decoder interface          D_clock typed partial, terminal.
                    ODOMETER-INTERNALIZED [D]  used only in the independent
                                               carry-law cross-check.
```

## Result

```text
candidate-T  q(N(Y_n^eps)) = s_2(n) mod 2 for all n >= 0, both branches.
             Proof: N(-1) = 1, so N(Y^-) = N(Y^+); N(Y_n) = N(r)^s_2(n) = 2^s_2(n);
             q(2) = 1 and q is a homomorphism, so q(2^k) = k mod 2.
             Lean 4 + Mathlib: SqrtPhiTimeGravityBridge.lean compiled in full,
             no errors, no sorry (one external compile by the second reader;
             toolchain version not recorded). Covers readout_parity,
             clock_bridge, sigma_pre_update, bridge_total_compatible,
             bridge_sign_invariant.
by definition  the gravity leg is constant in n and eps. In Lean,
             gravity_leg_constant is rfl because gravityRead is defined as a
             constant function: a definition, not a proof. The exact value
             g^2 = 5120 + 2048 sqrt5 and its positivity rest only on the Python
             verifier (gates 21 to 24). The bridge defines no n-dependent
             gravity modulation because it is built with none.
candidate-C  exact check n = 0..10^4, both branches, 27 of 27 gates PASS,
             including native U from origin zero driven by q(N(Y_n)) of either
             branch reproducing the canonical orbit for 10^4 steps.
```

Content of the positive answer, stated plainly. The frozen bridge class is
nonempty and the bridge is total, but it is structurally degenerate: the clock
leg returns only theta_n, which native U already has, and the gravity leg
carries no information about n. The bridge exists because it says almost
nothing.

## Excluded readouts and why

```text
Y itself                    odd: Y^+ != Y^- exactly when theta_n = 1
                            (5001 of 10001 counters).
bare successor multiplier   r^(1 - nu_2(n+1)) is branch dependent at 333 of
                            n = 1..499.
E(n) = s_2(n) + s_2(n+2) + nu_2(n+1) + nu_2(n+2)
                            branch invariant (always even) but not a function
                            of Y_n: witness n = 0 and n = 255, Y_0 = Y_255 = 1,
                            E(0) = 2, E(255) = 18. A readout of the bridge must
                            be a function of Y_n; E is not, so it is excluded.
```

## Readings, not derivations

`phi (3 - phi) = sqrt5` and therefore `g^2 = 2^10 phi^3 sqrt5`. Verified
exactly; a reading of the frozen g, nothing derived from it.
`3 - phi = (1 - j)(1 - j^4) = |1 - zeta_5|^2`, verified exactly in Z[zeta_5].

## Not claimed

No SI scale (any SI claim stays bounded by METRO-EDGE-SCALE), no physical
tick, no physical event, no interpretation of time, no selection of a branch
by nature, no derivation from the axiom, no status change.

## Falsifier

Fires if for some n >= 0 and some eps, q(N(Y_n^eps)) differs from
s_2(n) mod 2; if some branch-invariant function of Y fails to factor through
N on C8; if the gravity leg acquires an n or eps input; if native U driven by
the bridge bit leaves the canonical orbit; or if the Lean file fails to compile
without sorry.

## Pins

```text
SqrtPhiTimeGravityBridge.lean  3557d91266caa49359ba307880ee58bdf98346e438b4807f7a135cdeb1001bd8
verify.py                      799109cf931309429eb456cc6b1d22bf59c05d8435e914c2db88e150027251f8
EXPECTED.txt                   c5e1da68a617bb8741683526ac84d0f1bd8b8661dd21420ece90ed524ae67069
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC,
             Python 3.13, x86_64, one leg only (not a two-architecture result).
```

The first run of the verifier fired gate 21 (26 of 27 PASS) on an expected
literal written by hand before computing (`1280 + 768 sqrt5`; script
c935792ee925d6326a71240107736afa29d7eb11469e3c144c75c354f0f4c2b4, stdout
7c97522d4928bddbb14cd0ca7cad6a1b6fac1f7cfd21c9715b21754cb82fde1f). The
computed value `5120 + 2048 sqrt5` was confirmed by hand
(`phi^4 (3 - phi) = 5 + 2 sqrt5`) and independently by a second reader. It
was a script error, not a property of the bridge; only that literal and its
label changed. The verifier was not preregistered, so this is incubation
evidence, not a pinned probe.
