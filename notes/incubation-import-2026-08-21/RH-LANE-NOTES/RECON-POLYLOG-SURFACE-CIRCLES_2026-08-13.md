# RECON: the polylog surface F(s,z) = Li_s(z), three circles, and a lane proposal

```text
Status     NON-CANONICAL recon. No lane opened, no prereg, no authority.
           Verifies the owner's polylog-circle statement of 2026-08-13
           evening, extends it with what canon already carries, names the
           two classical bridges that make the question exact, and drafts
           the claim scope for a future candidate.
Date       2026-08-13, late. Basis: Public Canon v46, main 6545c1d0 (gate
           run earlier this session, 5/5 OK).
Witnesses  mpmath dps 30 readouts, labeled; not evidence, reading checks.
Collision  no polylog-surface lane exists in project docs, repo notes/,
           probes/, branches (surveyed this session), or REGISTRY.tsv.
           Siblings, not collisions: project C-LI2-PENTAGON-BALANCE-1 and
           C-LI2-RELATIVE-BLOCH-SEAM-2 (s = 2 layer), PROMO-J-LI-* (Li
           coefficient layer), and the three RH branches of the parallel
           recon (screw / capacity / half-angle carriers).
```

## 1. The owner's statements, verified [T, classical; witnesses recorded]

```text
V1  1 - J = -j^2 = e^(-i pi/5), |J| = 1/phi < 1, |1 - J| = 1  EXACT.
    Li_1(J) = -Log(1 - J) = i pi/5, so i pi = 5 Li_1(J).
    Witness: |Li_1(J) - i pi/5| < 3e-31; Re Li_1(J) = 0 because |1-J| = 1
    exactly (that is the geometric content). Matches registry row
    PI-FROM-J [T] at v46.
V2  zeta(s) = Li_s(1) for Re s > 1  EXACT, classical.
V3  PENTAGON-NORMALIZATION [T]: c(n) = 5[5|n] - 1 and
    sum c(n) n^-s = (5^(1-s) - 1) zeta(s)  as registered.
V4  Cayley: rho = 1/2 + i gamma implies |1 - 1/rho| = 1 and
    arg(1 - 1/rho) = 2 arctan(1/(2 gamma)).
    Witness at gamma_1: both readouts agree to 12 digits. Matches the
    FRONTIER text of LAMBDA-COCYCLE-ANGLES [H] and
    LAMBDA-COCYCLE-GRID-EQUIVALENCE [T].
```

No correction needed to the owner's message; all four legs check out at
source and at witness grade.

## 2. Canon already carries MORE slices of the surface than cited

Beyond PI-FROM-J and PENTAGON-NORMALIZATION, the v46 registry holds:

```text
J-HARMONIC-SEAM [T] (row 7): with psi = 1 - phi and u_n = F_n phi - F_(n+1)
    = -psi^n, the golden-weighted log series H(x) = sum u_n x^n / n =
    Log(1 - psi x). This IS the s = 1 golden-ray slice of the surface:
    the J-ray radial structure at s = 1 is already a public theorem.
WALL-LI2-RUNG [T] (row 186): the SS98 dilogarithm bridge,
    Re Li_2(sigma_a(J)) = pi^2/100 and 9 pi^2/100. The s = 2 slice at the
    four Galois points. (Real-part statement, as the contract insists.)
WALL-CIRCLE-LEMMA [T] (row 214): for every N >= 3 and 1 <= a <= N-1, the
    point z = 1 + zeta_N^a ... (the general 1 + root-of-unity circle
    geometry). V1 is its N = 5 instance family.
```

So the surface view unifies FIVE existing public [T] rows plus the
NON-CANONICAL seam fiber of notes/C-J-DEDEKIND-WEIL-ROAD-N.md section 2
(Delta(w,x) = log|1 - wx|, which is Re Li_1 geometry). That is a stronger
statement than "nice similarity": the program has been working on slices
of one two-parameter function without naming the ambient.

## 3. The two classical bridges that make the owner's question exact

The proposed target ("convert the Cayley transform in the s-plane to a
natural action on the z-circle") has a precise unconditional core in two
classical theorems. Both must be pinned at any freeze; both are checked at
witness grade this session.

```text
B1  EDGE EXPANSION (Lindelof; DLMF 25.12(ii) family). For s not a positive
    integer and small mu:
      Li_s(e^mu) = Gamma(1-s) (-mu)^(s-1) + sum_(k>=0) zeta(s-k) mu^k / k!.
    The z = 1 edge of the surface carries the ENTIRE zeta ladder as its
    Taylor data, plus the branch point (-mu)^(s-1). This is the exact
    control of the fact that z -> 1 and s-continuation do not commute
    naively; V2 alone understates the edge.
B2  HURWITZ FORMULA (Jonquiere/Hurwitz). With F(x,s) = Li_s(e^(2 pi i x)),
      zeta(1-s, x) = Gamma(s)/(2 pi)^s
                     [ e^(-i pi s/2) F(x,s) + e^(+i pi s/2) F(-x,s) ].
    Witness: |lhs - rhs| < 1e-32 at s = 2.3 + 0.4i, x = 1/5.
    READING: the s -> 1-s reflection, whose fixed line IS the critical
    line, is implemented exactly as an operation on the z-circle
    (x and -x, with the s-dependent phases). The action the owner asks
    for exists; it is the Lerch functional equation.
B3  TORSION FIBER = THE DEDEKIND PACKET. Exact rearrangement, witness
    2e-31 at complex s:
      Li_s(j^a) = 5^(-s) sum_(r=1..5) j^(ar) zeta(s, r/5),
    and via Gauss sums the five-torsion fiber {z = j^a} of the surface is
    exactly the mod-5 L-packet, i.e. the factor system of
    zeta_K = zeta . L(chi_5) . L(chi) . L(chi-bar) from
    C-J-DEDEKIND-WEIL-ROAD-N section 5. The place where "J meets zeta" is
    canonical: the boundary radial limit of the J-ray is z = j, and the
    torsion fiber there carries GRH_K's object.
```

## 4. Sharpened candidate scope (draft, NOT opened)

Proposed id C-LERCH-SURFACE-CIRCLES-1 (owner may rename). Three statements,
ordered so that everything gated is UNCONDITIONAL and the [H] stays fenced:

```text
Q1  FIVE-FIBER FUNCTIONAL OPERATOR [target candidate-T, classical
    repackaging with exact 5-structure]. Write B2 restricted to
    x in (1/5)Z as one exact linear operator on the five-dimensional
    torsion fiber; diagonalize by Gauss sums; record the root-number
    geometry as points on the z-circle. Everything exact, everything
    classical; the value is the canonical 5-shape, stated once.
Q2  J-RAY AT GENERAL s [the genuinely new computation]. The radial
    increment from the interior J-point to the boundary torsion point:
      Li_s(j) - Li_s(J) = sum_(n>=1) j^n (1 - phi^(-n)) n^(-s),
    with 1 - phi^(-n) = 1 - (-psi)^n: a golden-weighted twist of the
    fiber series. Its s = 1 shadow is J-HARMONIC-SEAM [T]; general s is
    open and exactly computable termwise. Target: exact identities
    connecting the J-ray data to the Hurwitz data of B3, with explicit
    remainder control from B1.
Q3  THE SEAM STAYS [H]. Any identification of the Cayley angle set
    {2 arctan(1/(2 gamma))} with the z-side five-torsion grid
    2 pi (1/4) Z[1/5] is exactly LAMBDA-COCYCLE-ANGLES [H] and is NOT
    assumed anywhere in Q1-Q2. The lane must deliver unconditional
    content even if the grid dies. No positive gate may consume the grid.
```

Falsifier shapes: exact identity failure in Q1/Q2 gates (Fraction and
ball-certified, same machinery as C-SUZUKI-LOCAL-CAPACITY-NOGO-1);
scope-creep firing if any gate is found to import RH, the grid, or zero
data. Layer L1, no lift, no physical reading; the pentagon/zeta_8 fences
of the half-angle lane apply verbatim.

## 5. Hard brakes, stated before anyone falls in love

```text
BR1  There is no seam theorem. The road note's boundary ("a common
     logarithmic geometry, not an inference") imports verbatim.
BR2  Mainstream expectation is that zero ordinates are not algebraically
     special. The grid condition of the [H] row may well be false; the
     lane is designed so its results survive that outcome.
BR3  Prior art: the two-variable surface is a professionally occupied
     home: Lagarias and Li, "The Lerch zeta function" series (II Analytic
     continuation, arXiv:1005.4967, Forum Math.; III Polylogarithms and
     special values; plus I and IV). Any freeze pins these and draws the
     novelty boundary: what is new here is only the exact five-torsion
     and golden-ray packaging aligned with the house registry, not the
     surface analysis itself.
BR4  Priority of attention: three RH incubation branches await merge and
     one candidate awaits push. This lane should open AFTER that wave
     lands, unless the owner explicitly reorders.
```

## 6. Verdict

[candidate-H assessment, NON-CANONICAL] The owner's picture is verified
with no corrections; canon already holds five [T] slices of the surface;
the requested s-to-z-circle conversion exists unconditionally as the
Hurwitz/Lerch functional equation; the five-torsion fiber is exactly the
Dedekind packet. A lane is warranted with the Q1-Q3 scope and the BR1-BR4
brakes. RH remains O; nothing here moves it.
