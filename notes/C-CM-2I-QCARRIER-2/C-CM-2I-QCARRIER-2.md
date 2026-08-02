# C-CM-2I-QCARRIER-2: the order-eight quarter-turn (rev 1)

NON-CANONICAL. Incubation-lane candidate against Public Canon v30. No
authority, no Canon change, no canon/ file touched. Second slice of the
audit-proposed probe P-CM-2I-QCARRIER-1, completing the constructive
step left open by notes/C-CM-2I-QCARRIER-1: the EXPLICIT semilinear
quarter-turn on the branch pair, with its cocycle decided. All gates
exact and deterministic (verify_cm_2i_qcarrier_2.py, 11 gates).

## Candidate claims

Setting: K = Q(zeta5), Gal(K/Q) = <tau>, tau(zeta) = zeta^2,
tau^2 = sigma; G = <S, T> the registered integral 2I lift
(COLOR-INTEGRAL-LIFT); pair carrier V = K^2 (+) K^2 with
Pi(g) = diag(g, tau(g)). Any G-equivariant tau-semilinear map is
necessarily nu(x, y) = (C tau(y), d tau(x)) with C the
sigma-intertwiner and d a scalar (the diagonal Hom-blocks vanish
because the two branches are inequivalent; Schur).

1. The intertwiner (N1-N3). The space of C with C sigma(g) = g C is
   exactly one K-line; the primitive integral representative is
   computed, invertible, and intertwines all 120 elements.
2. The cocycle (N4-N5). C sigma(C) = mu I with mu = -phi^2 EXACTLY:
   totally negative at both real places. CM norms are totally positive,
   so the norm equation N(d) = tau^3(mu^-1) is unsolvable in principle
   (and verified unsolvable over the exhaustive box): nu^4 = 1 is
   UNREACHABLE for every scaling of C and every d. The obstruction
   class is [-1] in F^x / N_{K/F}(K^x).
3. The order-eight closure (N6-N8). With N(d) = phi^2 (solvable;
   deterministic smallest d) the explicit nu satisfies: nu is
   G-equivariant, nu^2 is the block-diagonal sigma-descent (the pair's
   global conjugation), nu^4 = -1, nu^8 = 1. THE ARITHMETIC
   QUARTER-TURN ON THE EQUIVARIANT PAIR CLOSES AT ORDER EIGHT, NEVER
   FOUR.
4. The bit for the third time (N9). The central sign -1 forced here is
   the same sign as: the order-8 antiunitary spinor lift of the
   rotoreflection S (C-HERM2-BORN-CONE-1 gate C5), the mu_5-escaping
   tenth-root glue phase 1 - J with (1-J)^5 = -1
   (C-CENTRAL-LIFT-PHASE-1 gate CP12), and the half-tick obstruction
   sigma(phi^-1) = -phi < 0 (C-COMMON-CARRIER-ICOSIAN-1 gate T6).
   Vector level C4, spinor level C8, on both the geometric and the
   arithmetic side. The finding-A operator phi_g has order 4 on the
   bare CM spinor; 2I-equivariance is what forces the central sign.
5. Branch bookkeeping and Gram (N10-N11). nu swaps the two branch
   summands while nu^2 preserves them: ker chi5 within branches, the
   nontrivial coset across -- the explicit operator completing the
   descent dichotomy of C-CM-2I-QCARRIER-1. And nu transports the pair
   Gram diag(H0, tau H0) exactly onto diag(N(d) tau H0, kappa sigma H0)
   with totally positive multipliers: a semilinear similitude
   respecting the unique invariant form up to positive scale.

## Status separation

candidate-T: all eleven gates; the impossibility argument in N5 is
theorem-grade (total positivity of CM norms) with the box search as an
independent audit. [T, literature]: Schur's lemma and total positivity
of CM norms. [D]: reading "the bit is the cohomology class [-1]" as the
lane's ontological bit; reading nu as the carrier realization of the
finding-A quarter-turn. [H]: none new; the U(1) dictionary and decoder
shape remain deferred as before. [O]: the formal probe registration
(see the PREREG draft in this directory), the checkpoint
orbit-to-amplitude bridge, and MatterData writing -- untouched, and
QUADRATIC-DECODER-DATA / COLOR-MEASURE-SELECTION remain open rows.

## Falsifiers

- F-QC2-1: any FAIL gate of verify_cm_2i_qcarrier_2.py.
- F-QC2-2: an exact G-equivariant tau-semilinear nu with nu^4 = 1
  (would contradict the total-negativity of the cocycle).
- F-QC2-3: a G-equivariant tau-semilinear map outside the ansatz
  (would contradict the Schur block decomposition).

No falsifier fired. No threshold moved. PROMO deferred.
