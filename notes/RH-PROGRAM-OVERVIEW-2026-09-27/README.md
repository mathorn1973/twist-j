# RH program overview at Public Canon v92: what was achieved, and what could move toward a proof

```text
STATUS         NON-CANONICAL OVERVIEW. No status motion, no probe, no lock,
               no Canon, Registry, Frontier, gate or evidence change.
DATE           2026-09-27
BASIS          Public Canon v92, tag canon-v92,
               content commit d7eb6de16c11f6a105996de02ffd7afa32683a93,
               canon/CANON.md sha256
               31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68,
               797365 bytes; public main 3bad0a50065418cde782ce9b3074bb691051d4f1
GATE           STATUS.md ACTIVE; check_canon PASS v92 claims=465; check_ledger
               PASS; check_policy PASS (this session, x86_64, read-only)
HANDOFF        mathorn1973/twistj-handoff at 1e358487f74a114d7128c6aa088f278031c4d8d3;
               its latest RH page is ZETA-RH-STATUS-2026-09-08.md (Public Canon v81)
COUNTING       notes/RH-ONE-WALL-CROSSREF_2026-08-17.md applies to every item here
AUTHORITY      none. Every status label below is copied from the file that
               carries it; nothing is promoted, lowered or reinterpreted.
COMPUTATION    none. No scientific code was run for this overview.
```

## 0. The answer in one page

**What the program achieved.** Between Public Canon v9 (July 2026) and v92
(26 September 2026) the RH line produced an exact, audited map of the problem
rather than a result about the zeros:

- 35 registered rows adjacent to RH, all at their stated scopes: 26 `T`,
  3 `C`, 4 `F`, 1 `H`, 1 `O` (section 3.1). They normalize the objects
  (`Z_J = zeta`, `1/zeta = C_0 O_5`, the exact Mertens two-sum, the golden
  ladder), fix the lambda-adic spectrum exactly, prove that the cocycle
  vector exists iff RH plus a grid condition, and close nine carrier or
  route classes by proof.
- A candidate layer, merged or on branches, carrying at least ten exact
  reformulations of RH (section 3.2), ten unconditional estimates each of
  which stops exactly at a classically known boundary (section 3.3), and a
  no-go ledger of about thirty closed proof routes (section 3.4).
- A review discipline that caught its own over-claims: the positive pole
  factorization (withdrawn), the "quasi-GRH" reading of (M37) (withdrawn),
  the "converge / do not converge" wording of finite diagnostics (narrowed),
  the Li-series radius (corrected), the pure-height certificate (F-bounded),
  the Widder depth audit's own sign criterion (recorded false and replaced
  by `k theta > pi/2` in its correction file).

**What it did not achieve.** No statement about the location of any
nontrivial zero beyond classical knowledge. Every unconditional bound in the
record reaches exactly the known line `Re s = 1` or a known exponent and no
further (section 3.3). The Canon at v92 carries no row named `RH`; the owner
declaration of 2026-09-08 that RH is a program-level requirement with a
falsifier is still a proposal on two unmerged branches (section 6).

**Could anything bring us toward a proof?** Nothing in the record reduces RH
to something easier. Every route met the same obstruction, which the record
counts once: a finite prefix of any positivity hierarchy is passed by some
off-critical configuration, so only a global positive object built from the
Euler side without zero data would decide, and every attempt to build one
was either circular (the map defined from the inequality it must prove),
indefinite (the pole term, the delayed prime legs, the per-prime Stieltjes
atom), or nonlocal (capacity contraction norm exactly one). The J-structure
of TWIST-J (`Q(zeta_5)`, `chi_5`, `phi`, the split-orientation channel) never
enters the analytic difficulty: it supplies bookkeeping and twists on top of
Moebius, and where it changes the target it makes it formally harder
(`GRH(zeta_F)` contains RH). Section 5 ranks the surviving routes. Two have a
payoff that is not RH in another dress: the unconditional nontriviality of
Suzuki's space `V(0)` (strictly weaker than RH, an open problem stated by
Suzuki himself), and the program-specific construction of the completed
Dedekind factor from J-native data (which tests TWIST-J, not the zeros). The
only direction decidable by finite means is the negative one: an exactly
enclosed off-critical zero, which by the owner declaration falsifies the
program; the 2026-09-15 watch found none.

## 1. Where the Canon stands at v92

| Item | Value at v92 |
|---|---|
| Registry rows named `RH` or `RH-PROGRAM-DEPENDENCE` | 0 |
| Live rows that mention RH | `LAMBDA-COCYCLE-ANGLES [H]`, `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` |
| Program label of both rows in `canon/FRONTIER_PROGRAMS.tsv` | `ENRICHMENT`; states `BLOCKED` and `STOP` |
| RH-lane registry motion in v82 to v92 (eleven activations) | none |
| Live H/O rows in the whole registry | 25 (2 H, 23 O) |
| Rows whose scope says "no RH statement" explicitly | the Suzuki triple, the Li and lambda no-go rows, the rapidity rows |
| Owner declaration of 2026-09-08 | recorded in the handoff repo and in two unmerged patch proposals; not in the Canon |

Decision condition of the bridge row, verbatim from the registry: STOP until
a non-circular transfer mechanism, its complete domain, approximation or
kernel, uniform norm and reconstruction errors are frozen; closes positively
at RH strength only by deriving the displayed all-epsilon estimate from the
refined shell; closes negatively only after a frozen complete admissible
transfer class containing both route families is proved empty or incapable;
failure of one candidate or every fixed-mode estimate is STOP, not negative
closure. No transfer class has been frozen. The row is byte-identical since
v67.

Falsifier of the lambda row: fires if RH is disproved, or if one nontrivial
zero is exactly proved not to be `1/(1 - xi)` with `xi^(4 . 5^a) = 1`. The
grid `2 pi (1/4) Z[1/5]` is dense, so no finite computation decides the row;
finite satisfaction of the residual bounds `0 <= M - t_n <= 2M` decides
nothing, an exact finite violation refutes membership.

## 2. Timeline of the RH line

| Period | Lane | Where it lives | Outcome |
|---|---|---|---|
| 2026-07-15 to 07-18 | Li cocycle, Weil realization, pentagon normalization (v9 fold) | `notes/C-LI-*`, `notes/C-WEIL-REALIZATION-1`, `notes/C-PENTAGON-WEIL-1`, `notes/j-li-schoenberg-2`, `notes/verdicts` | PENTAGON-NORMALIZATION `T`; four carrier no-gos `T`, three paired with `F` rows; realization stays `O` |
| 2026-08-06 to 08-07 | Lambda-cocycle angles (v38) | `probes/P-LAMBDA-COCYCLE-ANGLES-1,2` | grid equivalence `T`, branch collapse `T`, cocycle existence `H` |
| 2026-08-11 | Zeta simple-zero and Gram-defect incubation (fleet) | `twistj-handoff/zeta-rh-2026-08-11/` | ten candidates; scalar routes capped below the 0.675 target; strategic closure candidate-D |
| 2026-08-13 to 08-17 | Suzuki screw function: half-angle, capacity, Sonin (v50 fold of the local no-go) | `notes/C-RH-PYTHAGORAS-HALFANGLE-2-N`, `notes/C-RH-CAPACITY-CONTRACTION-1-N`, `notes/C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N`, `probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1` | signed Krein factorization candidate-T; capacity G3 UNDECIDED after correction; `V(0) ~= ker T_(conj Theta)` candidate-T; SUZUKI-LOCAL-CAPACITY-NOGO `T` |
| 2026-08-14 to 08-24 | Ray-Pick, Hadamard, Hausdorff, Stieltjes-Widder, finite-window certificates, Hankel hard edge, Widder depth audit | `notes/incubation-import-2026-08-21/*`, branches `notes/c-rh-*`, `handoff/*`, `twistj-handoff/RH-RAY-PICK-*` | RH iff Hausdorff moment sequence, RH iff Widder rungs `W_k >= 0`, both candidate-T; pure height certificate F-bounded; three lanes ABANDONED with consumed ids |
| 2026-08-11 to 09-05 | Arithmetic rapidity and the integral Moebius lift (v44, v45, v46, v50, v67, v77 folds) | `probes/P-ARITH-RAPIDITY-1`, `P-J-IDEAL-*`, `P-RAPIDITY-*`, `notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1`, `probes/P-O5-*` | 17 `T` and 3 `C` rows; bridge row `O`; O5 cluster nine candidate-T, three ABANDONED, none registered |
| 2026-09-05 | Proof-first notes (PR #819) | `notes/RH-EULER-HAUSDORFF-SOURCE-TAIL-2026-09-05.md`, `RH-FULL-SHELL-FOURIER-CONTRACT-2026-09-05.md`, `RH-HARD-EDGE-CEILING-BOUND-2026-09-05.md` | tail bound uniform in `r`; full-shell reconstruction from positive modes; matched-quartet ceiling `T_*^3/(delta c^2) -> 2` |
| 2026-09-06 to 09-16 | Signed prime correlations and the moment target (PR #856) | branch `codex/rh-correlation-moment-note-20260906` | whole-moment bound (M32) unconditional; target (M37) open; (M37) is implied by Lindeloef for `L(s, chi_5)`, no zero-location consequence |
| 2026-09-08 | Owner declaration and patch proposal | `twistj-handoff/ZETA-RH-STATUS-2026-09-08.md`, branch `notes/rh-program-dependence-2026-09-08` | "RH is required for TWIST-J. If RH falls, TWIST-J falls." Proposal only |
| 2026-09-10 to 09-16 | Nyman-Beurling binary routing review (PR #933) | branch `claude/dreamy-pascal-liep2q` | finite identities valid; the missing step is asymptotic admissibility at RH strength |
| 2026-09-12 to 09-16 | Moebius mean channel and fixed-epsilon target (41) (PR #979) | branch `notes/c-rh-mobius-mean-channel-n` | finite-`N` bound (38) candidate-T; (41) open; strength guard: (41) at one `eps` is a shadow condition, along `eps_j -> 0` it is RH |
| 2026-09-15 to 09-16 | Attack session, four refereed lanes (PR #1020); Jacobi growth ladder (PR #1031); refreshed declaration (PR #1021) | branches `claude/rh-program-status-ymq3np`, `claude/jacobi-coefficients-rh-bound-qi5pse`, `notes/rh-program-dependence-v87-2026-09-16` | zero new structure by the counting rule; a weaker sufficient family (21) for RH; exact K<=72 obstruction for certificate (29) |
| 2026-09-27 | Moebius divisor antiresonance note (issue #1193, lock only) | branch `notes/c-mobius-divisor-antiresonance-n` (not yet pushed at reading time) | first-order prime-power response `A_n'(0) = Lambda(n)`; the lock forbids any RH implication |

## 3. What was achieved

### 3.1 Registered rows adjacent to RH

Li, lambda and pentagon cluster, Canon section 16 (`p = 5 and the wall`)
and section 18:

| Row | Status | Content at its scope |
|---|---|---|
| PENTAGON-NORMALIZATION | T | `P_0(s) = (5^(1-s) - 1) zeta(s)`; after classical completion `Z_J = zeta`, `xi_J = xi`; a normalization identity, no Weil form or positivity |
| LAMBDA-COCYCLE-GRID-EQUIVALENCE | T | `U_J` on `L^2(O_lambda, Haar)` has pure point spectrum on the grid `2 pi (1/4) Z[1/5]`; a cocycle vector exists iff RH and every Cayley angle `2 arctan(1/(2 gamma))` lies on the grid |
| LAMBDA-COCYCLE-BRANCH-COLLAPSE | T | on the critical line `1 - 1/rho` is a unit; `0 <= M - t_n <= 2M` are necessary conditions only |
| LAMBDA-COCYCLE-ANGLES | H | the cocycle vector exists (RH plus grid); the only live positive-direction hypothesis of the line |
| J-LI-CYCLIC-CARRIER-DIMENSION | T | no finite-dimensional cyclic carrier realizes the Li ladder; every realization has infinite support, `1` in the support, no atom at `1` |
| J-LI-TORAL-HAAR-NOGO | T | no Haar-Koopman on `T^d` realizes the Li ladder |
| J-LI-LAMBDA-HAAR-HS-NOGO | T | `I - U_J^n` is never Hilbert-Schmidt; excludes HS-perturbation and S2 witness forms only |
| J-LI-LAMBDA-SHIFT-NOGO | T | the discrete lambda-scaling unitary is a bilateral shift; no all-`n` Li cocycle witness |
| J-LI-E8-SHELL-MULTIPLICITY-NOGO | T | no `f(Delta_E8)` gives `det_1(I - t^2 A) = Xi(t)/Xi(0)`; shells have multiplicity at least 240 |
| J-LI-PENTAGON-DILATION-DEFICIENCY | T | pentagon-tower dilations miss every `q` coprime to 5 by exactly `(1/12)(1 - 1/q^2)` |
| MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER | F | the shell-constant E8 carrier is falsified |
| LAMBDA-BOUNDARY-HS-KOOPMAN | F | the HS/S2 forms of the boundary Koopman carrier are falsified; the cocycle form stays `H` |
| LAMBDA-DISCRETE-SCALING-SINGLE-UNITARY-CARRIER | F | the discrete-time scaling single-unitary carrier and its tensor composites are falsified |
| PENTAGON-ONLY-DILATIONS | F | Nyman-Beurling restricted to `5^m` dilations is falsified |

Rapidity, Moebius lift and Suzuki cluster, Canon section 10 (`Relativity as
counting`) and section 18:

| Row | Status | Content at its scope |
|---|---|---|
| ARITHMETIC-RAPIDITY-DECOMPOSITION, SPLIT-PRIME-RAPIDITY-CLASS, SPLIT-PRIME-RAPIDITY-INDEPENDENCE, REDUCED-SPLIT-GENERATOR-HEIGHT, SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION, SPLIT-RAPIDITY-FEJER-GRAM-BOUND, J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL, J-RAPIDITY-TERNARY-SHELL-CENSUS | T | the rapidity class of split primes in `Q(sqrt5)`, its injectivity, separation `dist >= asinh(1/(2 sqrt P))`, and the finite Fejer Gram bound |
| SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT | C | two constructions agree for all 146 split primes below 2000 |
| J-IDEAL-COUNT-QUADRATIC-CHARACTER, J-IDEAL-RATIONAL-MOBIUS-DESCENT, J-MERTENS-IDEAL-TWOSUM | T | `a_F = 1 * chi_5`; `mu = b * chi_5`; the exact identity `M(N) = sum b(a) S_5(floor(N/a))`, an incidence identity and not an estimate |
| J-IDEAL-RAPIDITY-CHARACTER-LIFT, J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION | T | the integral lift `bold_mu` with local factor `((1 - X_p T)(1 - X_p^-1 T))/(1 - T)`; `1/zeta = C_0 O_5` at formal Euler scope with no continuation or zero claim |
| J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO | T | the termwise `l^1` triangle bound is `> N/4`, not `o(N)`; a narrow route no-go |
| RAPIDITY-GOLDEN-LADDER, RAPIDITY-TARGET-RECONSTRUCTION | T | integer evaluations exactly at `t = +-phi^(2k)`; `M(N)` reconstructible from positive rungs with weights of norm below `19/10`; the difficulty moves to higher rungs |
| SUZUKI-LOCAL-CAPACITY-NOGO | T | capacity contraction norm is exactly one; every Gram realization dominating the prime curve is nonlocal in `t`; twelve certified exact gates |
| SUZUKI-PRIME-FREE-WINDOW, SUZUKI-EVENT-COUNT | C | `A(t) > 0` on `[1/128, 45/64]` at scale `2^-192`; `N(10^6) = 78734` prime-power events |
| TRIVIAL-RAPIDITY-EVALUATION-BRIDGE | O | the evaluation obligation; the only registered positive-direction target of the rapidity line |

Counting by registry id pattern: 21 rows in this cluster (17 `T`, 3 `C`,
1 `O`); the 2026-09-08 handoff page grouped 22 under its own rule. Neither
count includes a row about zero location.

### 3.2 Exact reformulations of RH obtained (candidate layer, unregistered)

Each line is an equivalence or a sufficient condition with a written
derivation; each carries the label its file gives it, none is a public `T`.

| Reformulation | Label | Where |
|---|---|---|
| RH iff `{b_n(c)}`, `b_n(c) = c^(2n) A_(n+1)(c)`, is a Hausdorff moment sequence for one fixed `c > 1/2`; at `c = 1` every cell `H_(n,r)(1)` is an absolutely convergent von Mangoldt log-moment plus archimedean constants | candidate-T | branch `notes/c-rh-weil-norm-junction-1-n`; `twistj-handoff/RH-RAY-PRIME-MOMENT-HAUSDORFF-2026-08-20.md`; tail bound in `notes/RH-EULER-HAUSDORFF-SOURCE-TAIL-2026-09-05.md` |
| RH iff `f(u) = q^-1 xi'(s)/xi(s)`, `u = s(s-1)`, is a Stieltjes function; iff all Widder rungs `W_k(u) >= 0`; `f > 0` and `W_1 > 0` unconditionally, first possible obstruction at `W_2` | candidate-T | branch `notes/c-rh-stieltjes-widder-euler-1-n` |
| RH iff every finite Ray-Pick matrix `[K_ray(a_i, a_j)]` is PSD, iff all `D_N > 0` on the chain `a_n = 1 + 1/n`; diagonal `M(a) > 0` unconditionally, so all RH content is off-diagonal | candidate-T | `notes/incubation-import-2026-08-21/C-RAY-PICK-KERNEL-374/`, `twistj-handoff/RH-RAY-PICK-CONSOLIDATION-2026-08-20.md` |
| `S_2 - lambda_1 = ||P_- v_(1/2)||^2 >= 0` with equality iff RH: the Cayley defect is the negative projection energy of the Cauchy carrier | candidate-T | same |
| `Psi(t) = ||U_t||^2 - ||V_t||^2` on Suzuki's screw function; RH iff `||V_t|| <= ||U_t||` for all `t`; local prime-by-prime contraction is impossible | candidate-T identity, candidate-D reading | `notes/C-RH-PYTHAGORAS-HALFANGLE-2-N/` |
| `Q_W^a(v) = ||R_+(v)||^2 - ||R_-(v)||^2` with corrected indefinite pole part; Weil positivity iff the graph map `R_+ -> R_-` is contractive | candidate-T | `notes/C-RH-CAPACITY-CONTRACTION-1-N/` (with `CORRECTION.md`) |
| `V(0) ~= S(Theta_xi) ~= ker T_(conj Theta_xi)`; nontriviality of `V(0)` is strictly weaker than RH and open | candidate-T | `notes/C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N/` |
| `GRH(zeta_F)` iff the split-orientation channel `O_5` is pole-free on `Re s > 1/2` iff `T_5(N) = O_eps(N^(1/2+eps))`; unconditional floor `sigma_c(O_5) >= 1/2` | candidate-T (bridge-down candidate-T-lit) | `notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1/`, `probes/P-O5-DEDEKIND-GRH-DIVISOR-READ-1` |
| Fixed-epsilon membership (41) puts `M_eps(s) = c_eps/(s-1) - zeta(s)/(s zeta(s+eps))` in `H^2(Re s > 1/2 - eps/2)`; one `eps` gives a shadow condition `ord_(rho-eps) >= ord_rho`, an accumulating family `eps_j -> 0` gives RH; RH implies (41) for every `eps` | candidate-T | branches `notes/c-rh-mobius-mean-channel-n` (addendum), `claude/rh-program-status-ymq3np` (lane B) |
| Jacobi ladder: `A_N(eps) = O((N+2)^kappa)` implies holomorphy on `Re s > 1/2 - eps/2 + kappa/4`; bounds with `eps_j -> 0`, `kappa_j -> 0` imply RH; the present exponent `kappa = 2 - 2 eps` reaches exactly `Re rho = 1` | candidate-T, reviewed HOLDS | branch `claude/jacobi-coefficients-rh-bound-qi5pse` |
| Nyman-Beurling binary routing: membership of the constant sequence in the residue closure implies RH (elementary direction); the hard direction is Bagchi's, imported | review | branch `claude/dreamy-pascal-liep2q` |
| Li-lane forms of July: RH iff the Li sequence is conditionally negative definite iff `K_N >= 0` iff `T_N >= 0` with `K_N = (1/2) L_N T_(N-1) L_N^*`; RH iff an orthogonal `O` with `I - O` Hilbert-Schmidt has `lambda_n = (1/2)||I - O^n||^2_S2`, every witness carrying the zeros' eigenangles; RH iff double shifted-Hankel positivity of the `w = s(1-s)` moments; first rung closed with margin `M_1 = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log 4 pi`, about `3.7 . 10^-5 > 0` | candidate-T, unregistered | `notes/j-li-schoenberg-2/`, `notes/C-LI-S2-RELATIVE-DETERMINANT-1/`, `notes/C-LI-Q-MOMENT-1/`, `notes/C-LI-COCYCLE-1/` |
| Signed moment: `r_Y(T) << B T^eps` iff `||P||_(2,T)^2 << N^2 T^eps` (finite-reduction theorem); the uniform family (M37) suffices | candidate-T, unconditional | branch `codex/rh-correlation-moment-note-20260906` |

### 3.3 Unconditional estimates obtained, and where each stops

| Estimate | Proved | Target | Gap |
|---|---|---|---|
| Signed-moment analytic tail at `sigma = 0.255` | `Y^(0.7221...)` | `Y^(0.6175)` | excess `Y^(0.1046...)`; retuning Hoelder exponents cannot help (M38) |
| Whole Fejer moment `F_T(P)/N^2` | `T^(0.4184...)` | `T^eps` | same source |
| Mean-channel finite energy `L_N(eps)` (38) | `A^(2-2 eps)/eps^2 . min{25, 2^16 exp(-sqrt(2 log A)/20)}`, `A = N + 2` | uniform in `N` (41) | polynomial growth remains; through the Jacobi ladder this exponent reaches exactly `Re rho = 1`, nothing beyond the known boundary |
| Euler-Hausdorff prime tail at `c = 1` | `|T_(n,r)(X)| <= 6 kappa_n (9/5)^(n+1/2) X^(-1/6) (log X + 6)`, uniform in `r` | positivity `H_(n,r)(1) >= 0` | no positivity is established; finitely many cells cannot establish RH |
| Matched hard-edge ceiling | `|T_*^3/(2 delta c^2) - 1| < 3 c^(-1/3) + 3 c^(-2/3) + c^-1` | detection of an isolated quartet at all heights | one quartet, matched family; detection ceiling is real |
| Capacity strict-shell bound | `q_(A,a)/||v||^2 >= 2 Re[M_+ conj(M_-)]/||v||^2 + (9/20) x - 3/5 - (log x)/x - kappa`, `x = e^a >= 41` | `q_(A,a) > 0` (G3) | the pole term has lowest eigenvalue `2a - 2 sinh(a)`; the supplied large-cutoff proof was withdrawn |
| Exact H-norm obstruction for certificate (29) | `min over span{r_2..r_72}` of the first 144 terms lies in `(7601923, 7601924)/10^9` | `9/2^23` | more than 7000 times the threshold; prunes the support class through 72 only |
| Widder hierarchy below the verified height `H` | `W_2 >= 0` unconditionally; every level `k <= floor(pi H / 2)`, about `4.7 . 10^12` levels, is nonnegative | all `k` | the finite certificate is always unconditionally true and the RH content sits past the horizon; `rho_N = 3/4 + iN` passes the first `N` levels |
| Hankel hard-edge detection (HE-2) | ceiling law `T^3 < 2 delta c^2` on the frozen grid; detection margin of order `c^-4` | detection at every height | against a critical-line background of order `c log c`, so no single member detects anything by itself |
| Weil Gram tower | finite sections certified positive definite on two platforms; the Davenport-Heilbronn fake certified negative | a reference positive form | the rank equals the number of visible zeros; "PSD with a large kernel is a weak statement"; the archimedean part cannot serve as the reference form |

Simple-zero and Gram-defect incubation of 2026-08-11 (handoff repo,
`zeta-rh-2026-08-11/`): local Montgomery-Taylor stencils saturate near
`0.6730` against the frozen target `0.675`; a periodic point set of density
`337/500 = 0.674` caps every scalar-defect route; the degree-4 bandwidth-one
polynomial with value `0.6818` survives `N <= 12` and is killed exactly at
`N = 13`; the fourth-moment route needs `m_3 >= 1.9897` where positivity gives
at most `16/9`. Every item is candidate-C or candidate-D on one architecture,
and the handoff page records that its `RH shortcut` is `F` and its strategic
closure candidate-D: "the missing positivity is RH itself."

### 3.4 Closed routes (the no-go ledger, in one place)

Registered as `T` or `F`: finite cyclic carriers; toral Haar-Koopman; E8
shell-constant functional calculus; lambda-adic boundary Koopman in HS and
S2 forms; lambda-adic discrete scaling shift and its tensor composites;
pentagon-only dilations; the termwise `l^1` triangle bound; local capacity
contraction and every nonnegative per-place budget.

Recorded at candidate grade, on `main` or on branches: the positive pole
shortcut; the supplied large-cutoff capacity proof; independent positive
delayed prime legs (`det = -L^2/4`); the pure-archimedean positive Schur
shortcut; the automatic Hardy (Toeplitz) shortcut; the pointwise Euler
impedance limit; direct de Branges-space equality with Suzuki's `H(E_xi)`;
importing Suzuki's RH-dependent zero vectors into `V(0)`; direct
Makarov-Poltoratski on `Theta_xi` (imports innerness, which is RH); a
per-prime Stieltjes decomposition (the atom density changes sign); pure
height certification `f(N)` from finite rank alone (F-bounded on the
symmetric model class); a difference kernel in `rho - rho*` recovering the
Cayley defect pointwise; the finite Li/Cayley statistic for the subharmonic
defect `E`; absolute Moebius pair summation; degree-only Walsh control; one
common Walsh coefficient bound with absolute row sums; a scalar Mertens
envelope alone; finite Taylor truncation in `eps`; pointwise decay alone in
the moment supremum; discarding the negative quartet; a finite prefix of the
Euler-Widder hierarchy as an RH criterion (`rho_N = 3/4 + iN` passes every
level `k <= N`); a fixed polynomial detecting every height at the hard edge.

None of these is a statement against RH. Each closes one proof route at its
frozen class and says so.

## 4. The wall

The record counts one obstruction, read at several levels, and forbids
booking the readings as separate theorems
(`notes/RH-ONE-WALL-CROSSREF_2026-08-17.md`; handoff page 2026-09-08,
section 4). In the files' own words:

```text
capacity   contraction norm exactly one; the dominating Gram realization is
           nonlocal in t                          (SUZUKI-LOCAL-CAPACITY-NOGO)
Li         finite positive Toeplitz profiles cannot decide support on Z_5
                                                  (Z5 attack, issue #404)
Hankel     hard-edge detection has a height ceiling for an isolated quartet
                                                  (HE-1 STOP, HE-2 ARMED)
Widder     no finite prefix of the Euler-Widder hierarchy characterizes RH
                                                  (rho_N = 3/4 + iN)
Ray-Pick   the finite matrix stays positive while an off-line quartet
           already exists at height T             (T3, F-bounded)
Jacobi     the current exponent yields nothing beyond Re s = 1
                                                  (section 8 of the ladder note)
NB         rate, not membership, is the closure debt (O(1/log K))
                                                  (PR #933 addendum)
moment     the negative quartet must remain coupled; separate estimates
           overshoot the target by a fixed power   (M30, M38)
Gram       finite-cut positivity reports only the visible zeros
                                                  (C-WEIL-GRAM-TOWER)
Boole      "RH lives one floor higher, in completeness, not in one inner
           product"                               (C-PRIME-BOOLE)
```

The sharpest positive statement of the missing object is in the handoff
milestone of 2026-08-12 and the decoder classification note of the same
week: does the arithmetic-side Weil form admit an explicit factorization
`Q = A^* A` into arithmetic data, coherent across cuts, without passing
through the zeros? The record calls that the uniform arithmetic square root
and "the main prize"; nothing in the record constructs a candidate `A`. The
same milestone states the position in its own words: "Nothing here is
progress on the Riemann hypothesis"; on a finite cut "the positivity that
can be checked is exactly the positivity that classical results already
guarantee. Checking it is a consistency test, not evidence."

Common form, quoted from the 2026-09-08 page: a finite prefix of any
positivity hierarchy is passed by some off-critical configuration. What
survives is a global object that gives all levels at once: a positive
Stieltjes measure constructed directly, one Euler-plus-archimedean object,
or a frozen non-circular transfer class with its norm and reconstruction
error.

One sentence, in this overview's reading: every positive-direction object in
the record is either defined from the inequality it must prove, or is
indefinite once the omitted term is restored, or is a finite prefix that
classical theory already makes positive.

## 5. Could anything bring us toward a proof?

Ranked by what a success would actually establish. The verdict column is
this overview's reading of the files, not a status.

| Rank | Route | What a success would prove | Present state | Verdict |
|---|---|---|---|---|
| 1 | Unconditional `V(0) != {0}` through a Wiener-Hopf transport `Theta_xi D_F = N_F u_F~` from one finite Connes-Consani stage | an open structural problem stated by Suzuki; strictly weaker than RH | G5 and G6 OPEN; three exact no-gos fence the shortcuts | the only target in the record whose payoff is a new theorem that is not RH in another dress; it does not prove RH |
| 2 | `J-DEDEKIND-COMPLETION` and `J-WEIL-FORM-REALIZATION` (O1, O2a of `notes/C-J-DEDEKIND-WEIL-ROAD-N.md`): derive `125^(s/2) (2 pi)^(-2s) Gamma(s)^2` and the Weil form from J-native data without importing `Gamma` | that TWIST-J owns an archimedean construction; failure kills the J-native route with RH untouched | unattempted; no lock, no probe | the only place where the J-structure could contribute something classical analysis lacks; it tests TWIST-J, not the zeros; O2b (positivity for `zeta_K`) is GRH itself and must not be booked as progress |
| 3 | Euler-side global positivity: EHP1 (a sum-of-squares or integral representation for all `H_(n,r)(1)`), or all Widder rungs `W_k >= 0` | RH | the per-prime decomposition is impossible (sign-changing atom density); the pole term is indefinite; no candidate representation exists | this is RH; the reformulation is exact and clean but supplies no mechanism |
| 4 | Non-circular contraction `T_a` on the Krein carrier with `||T_a|| <= 1` proved without zero data, coherent in `a` | RH (via Suzuki's criterion) | local contraction impossible; any construction must mix prime and archimedean channels globally; G0 domain freeze still owed | RH in operator dress; the record's own rule: a pointwise map defined from the desired inequality is circular and forbidden |
| 5 | Jacobi energy ladder (21): `A_N(2^-j) <= C_j (N+2)^(2^(1-j))` | RH | proved exponent `2 - 2 eps` reaches only `Re s = 1`; a fixed power saving would already give a new zero-free half-plane | a weaker sufficient family than uniform boundedness, and an honest analytic target; but any fixed-`eps` proof "would be the first" zero-free half-plane inside the strip, so it is at least as hard as a major open problem |
| 6 | Signed-moment target (M37) | an analytic-tail bound on the `L(s, chi_5)` side | implied by Lindeloef for `L(s, chi_5)`; no zero-location consequence known; inputs outside the bridge fence | a well-posed classical estimate; not a bridge to RH by any implication presently proved |
| 7 | Bridge row: derive `M(N) = O_eps(N^(1/2+eps))` from the integral shell | RH (Mertens form) | no transfer class frozen; full-shell reconstruction exists but bounds no source value; O5 dictionary is conditional in both directions | STOP by the row's own condition; every conditional arrow is on the forbidden side of its fence |
| 8 | Lambda-cocycle vector (`LAMBDA-COCYCLE-ANGLES [H]`) | RH plus the grid condition, strictly stronger | grid dense; not decidable by finite means; owner decision 2026-08-20: leave standing | cannot be proved from inside; only external mathematics (an off-grid ordinate) can fire it |
| 9 | Finite certificates: Ray-Pick `(N, T, delta)` certificate, Nyman-Beurling census, certificate (29) | detection of a specific off-line configuration, never its absence | the pure-height version is F-bounded; K<=72 support class excluded for (29) | useful only in the `F` direction |
| 10 | F-watch | a program falsifier by the owner declaration | twelve items scanned on 2026-09-15, none is a record of an off-critical zero; last verified height unchanged (Platt-Trudgian `3 . 10^12`) | the one direction finite means can decide; STOP on a claim, `F` only on an exact enclosure |

Three observations that follow from the table and not from any single file:

- **The J-structure has not entered the analytic difficulty.** Every
  RH-relevant statement in the record factors through classical objects:
  `xi`, Suzuki's screw function and `V(0)`, Li coefficients, Nyman-Beurling
  residue sequences, Moebius mean values, `L(s, chi_5)`. Where the
  TWIST-J arithmetic appears (`chi_5`, `phi`, `Q(sqrt5)`, the
  `2^omega(n)` orientation fiber, the golden ladder) it is exact bookkeeping
  on top of Moebius, and where it changes the target it makes it formally
  harder (`GRH(zeta_F)` contains RH; the cocycle row is RH plus a grid).
  Route 2 is the only one where the program's own structure could supply
  something new, and it has not been tried. The owner's first verdict of
  2026-07-15 already fixed the target as the classical Weil form `W_xi`
  and refused a silent substitution by the Dedekind form for `Q(zeta_5)`;
  the record has respected that choice, which is also why the J-structure
  has stayed on the bookkeeping side.
- **The referee discipline is the program's strongest asset.** Six
  over-claims were caught by the lanes' own adversarial reviews and
  withdrawn in writing before any fold (section 0). The cost is visible in
  the branch sprawl of section 6; the benefit is that nothing false has
  reached the registry.
- **Progress and motion are different quantities.** From v67 to v92 the
  registry grew by 129 rows while the two RH-adjacent live rows did not
  move. The handoff map of 2026-09-08 already said this for v81; it remains
  true at v92 for the RH line.

## 6. Process state and debts

Open pull requests and locks carrying RH material at reading time:

| Item | Branch or lock | State | What it owes |
|---|---|---|---|
| PR #856 signed prime correlations and the moment target | `codex/rh-correlation-moment-note-20260906` | draft, open since 2026-09-06 | merge as NON-CANONICAL with the (M37) strength annotation |
| PR #933 review of the binary-routing note | `claude/dreamy-pascal-liep2q` | draft, open | merge as NON-CANONICAL; a `C` row would need an aarch64 replay under a new probe id |
| PR #979 Moebius mean channel | `notes/c-rh-mobius-mean-channel-n` | open, not draft | owner decision whether "continue from (41)" remains the handoff |
| PR #1020 attack session 2026-09-15 with review addendum | `claude/rh-program-status-ymq3np` | draft, open | merge as the record of the session |
| PR #1021 RH program-dependence proposal on v87 | `notes/rh-program-dependence-v87-2026-09-16` | draft, open | the fold that puts the owner declaration into the Canon as `RH-PROGRAM-DEPENDENCE [H]` under a new program id `RH_FOUNDATION` |
| PR #1031 Jacobi growth ladder | `claude/jacobi-coefficients-rh-bound-qi5pse` | draft, open; review record HOLDS | merge as NON-CANONICAL |
| issue #1193 Moebius divisor antiresonance | `notes/c-mobius-divisor-antiresonance-n` | lock opened 2026-09-27, no branch content at reading time | notes-only; its firewall forbids any RH implication |

Further debts, each already named in an earlier map and still open:

- The owner declaration of 2026-09-08 is not in the Canon; the F-watch
  actions name a row that does not exist. Two proposal branches exist
  (2026-09-08 and the v87 refresh); the refresh resolves the three owner
  decisions conservatively (ordinary RH for `zeta`, program id
  `RH_FOUNDATION`, no dependency edges).
- The O5 cluster: nine candidate-T probes with public two-architecture
  replay pending since 2026-08-28, three ABANDONED; no fold decision, no
  explicit non-registration; the `GRH(zeta_F)` versus `M(N)` target
  mismatch lives only in a note.
- The bridge row has no frozen transfer class. Without it neither closure
  is typed, and the 2026-09-08 page's rule stands: a new RH probe opened
  without that definition lands as candidate-T without a fold vehicle.
- Twelve unmerged `notes/c-rh-*`, `notes/c-suzuki-*`, `notes/rh-*` and
  `handoff/*` branches from August (Hadamard horizontal source, Hadamard
  Weil Cayley, Ray finite-window 1 to 3, Stieltjes-Widder, Widder angle
  sweep STOP, Weil-norm junction, local capacity no-go, Suzuki
  consolidation, Euler-Widder depth audit, lambda-grid audit). Three of their ids are consumed by
  `notes/V63-TERMINAL-RECORDS/`; the branch ledger dispositions of
  2026-08-24 are not executed.
- Handoff repo hygiene: `README.md` still says Public Canon v54 in its
  first paragraph; `INDEX.md` is the 2026-08-11 manifest; the Ray-Pick
  consolidation's SHA-256 is still "PENDING FLEET/STUDIO READBACK".
- Nothing in the September RH work has a two-architecture replay; all lane
  verifiers ran on x86_64 only, so none of their computations can be filed
  as `C`.

## 7. Smallest next steps

Ordered; each is a decision or a definition, not a theorem, because the
record shows that theorems in this lane have been arriving at the rate of
several per week without moving either live row.

1. Fold the owner declaration through PR #1021: adds one `H` row with the
   F-watch as its procedure, removes the gap between what the program means
   by RH and what the Canon says. Administrative; zero mathematical risk.
2. Merge the six open notes pull requests as NON-CANONICAL so that the
   corrections they carry (pole-subtracted Hardy object, shadow versus
   half-plane, (M37) strength, K<=72 obstruction) travel with the results
   they correct. Then execute the August branch dispositions.
3. Decide the O5 cluster: run the public two-architecture replay of the nine
   candidate-T probes and open a fold decision, or write the explicit
   non-registration as was done in v73. Record the target mismatch in the
   registry, not only in a note.
4. Open the definitional lane for the bridge row: freeze the admissible
   transfer class containing both route families (growing-mode diagonal
   `h = h(N)` and the non-diagonal kernel), its domain, norm and error terms,
   with no estimate. This is the standing prerequisite for typing any
   closure of the only registered positive-direction RH target.
5. If mathematical effort continues, point it at the two routes whose
   payoff is not RH in another dress: route 1 (`V(0) != {0}`; freeze one
   applicable Toeplitz-kernel criterion for a meromorphic unimodular symbol
   of bounded type and test its hypotheses on `conj(Theta_xi)` without
   assuming innerness) and route 2 (`J-DEDEKIND-COMPLETION`, with the
   completion convention frozen before any work). Each needs its own lock,
   collision scan and scope; neither may reuse an abandoned id.
6. Keep the F-watch as the one finite-decidable item, with the vocabulary of
   `F-WATCH-2026-09-15.md`: STOP on a claim, `F` only on an exact enclosure
   or machine-checked proof in an independent public record.
7. Do not open a new RH probe, a new finite positivity scan, or a new
   scalar inequality on this lane. Each such object is already refuted by
   the wall on sight (section 4) and would land as candidate-T without a
   fold vehicle.

## 8. Sources

Public repository, on `main` at the basis above: `canon/REGISTRY.tsv`,
`canon/FRONTIER.md`, `canon/FRONTIER_PROGRAMS.tsv`, `canon/CHANGELOG.md`
(v82 to v92 entries), `notes/RH-ONE-WALL-CROSSREF_2026-08-17.md`,
`notes/RH-EULER-HAUSDORFF-SOURCE-TAIL-2026-09-05.md`,
`notes/RH-FULL-SHELL-FOURIER-CONTRACT-2026-09-05.md`,
`notes/RH-HARD-EDGE-CEILING-BOUND-2026-09-05.md`,
`notes/C-RH-CAPACITY-CONTRACTION-1-N/`,
`notes/C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N/`,
`notes/C-RH-PYTHAGORAS-HALFANGLE-N/`, `notes/C-RH-PYTHAGORAS-HALFANGLE-2-N/`,
`notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1/`, `notes/C-J-DEDEKIND-WEIL-ROAD-N.md`,
`notes/incubation-import-2026-08-21/` (C-RH-HANKEL-HARD-EDGE,
C-RH-WEYL-CANONICAL, C-RH-OFFCRITICAL-WITNESS, AUDIT-WIDDER-DEPTH,
C-WEIL-GRAM-TOWER, C-RAY-PICK-KERNEL-374, RH-LANE-NOTES, SESSION-RECORDS,
PROMO-J-LI, AUDIT-LAMBDA-GRID, C-PRIME-BOOLE, C-PRIME-ORDER-READING),
`notes/V63-TERMINAL-RECORDS/`, `notes/C-LI-COCYCLE-1/`,
`notes/C-LI-Q-MOMENT-1/`, `notes/C-LI-S2-RELATIVE-DETERMINANT-1/`,
`notes/C-LI-TORAL-HAAR-1/`, `notes/C-WEIL-REALIZATION-1/`,
`notes/C-PENTAGON-WEIL-1/`, `notes/j-li-schoenberg-2/`,
`notes/LI-COCYCLE-LANE_CONSOLIDATION_2026-07-16.md`, `notes/verdicts/`,
`notes/C-LAMBDA-COCYCLE-Z5-FOURIER-NORMAL-FORM-1-N/`,
`notes/FRONTIER-ATTACK-MAP-2026-08-26/`, `probes/P-LAMBDA-COCYCLE-ANGLES-1,2`,
`probes/P-J-LI-*`, `probes/P-R2-LAMBDA-HAAR-1`,
`probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1`, `probes/P-ARITH-RAPIDITY-1`,
`probes/P-J-IDEAL-*`, `probes/P-RAPIDITY-*`, `probes/P-O5-*` (twelve
directories).

Public repository, unmerged branches read at their tips:
`codex/rh-correlation-moment-note-20260906` (bdcc66c),
`claude/dreamy-pascal-liep2q` (2787900),
`notes/c-rh-mobius-mean-channel-n` (3fbb912),
`claude/rh-program-status-ymq3np` (1c2612d),
`notes/rh-program-dependence-2026-09-08` (ffff345),
`notes/rh-program-dependence-v87-2026-09-16` (dd9d5d5),
`claude/jacobi-coefficients-rh-bound-qi5pse` (06113aa),
`notes/c-rh-weil-norm-junction-1-n` (bed965b),
`notes/c-rh-stieltjes-widder-euler-1-n` (f0a455a),
`notes/c-rh-ray-finite-window-certificate-3-n` (ce3c7b5),
`notes/c-rh-hadamard-horizontal-source-1-n` (ee0474f),
`notes/c-rh-hadamard-weil-cayley-1-n` (a815dda),
`notes/rh-suzuki-consolidation-20260813` (873f5f3),
`notes/c-j-artin-mazur-zeta-1-n` (424abb4),
`notes/j-weil-weight-carlitz-rank-2026-09-16` (4ee76fc; not an RH item, its
section 6 is "entirely negative" for the RH lanes).

GitHub: issues #354, #355, #357, #360, #363, #371, #374, #471, #1030,
#1193; pull requests #819, #856, #907, #933, #979, #1020, #1021, #1031.

Handoff repository `mathorn1973/twistj-handoff` at 1e358487: `README.md`,
`INDEX.md`, `ZETA-RH-STATUS.md`, `ZETA-RH-STATUS-2026-08-20.md`,
`ZETA-RH-STATUS-2026-09-08.md`, `RH-RAY-PICK-CONSOLIDATION-2026-08-20.md`
and its pointer, `RH-RAY-PRIME-MOMENT-HAUSDORFF-2026-08-20.md`,
`STATE-2026-08-12.md`, `MILESTONE-2026-08-12.md`, `RAPIDITY-STATUS.md`,
`PRACOVNI-MAPA-V81-2026-09-08.md` with its verification record,
`zeta-rh-2026-08-11/` (ten incubation directories with `SHA256SUMS.txt`).

Method: one reading session on 2026-09-27 over the Canon tables, the
September branches and the handoff status pages, with four delegated
read-only summaries of the July Li lane, the August incubation notes on
`main`, the August unmerged branches and the handoff repository's 2026-08-11
artifacts; every status label copied verbatim from its file. No external reference was re-verified; literature imports are named as
the files name them. This overview does not replace the 2026-09-08 handoff
page, which remains the last RH status page written from inside the lane.
