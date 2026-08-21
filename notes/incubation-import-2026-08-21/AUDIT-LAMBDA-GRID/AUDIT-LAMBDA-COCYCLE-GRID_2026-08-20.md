# AUDIT: the angular clause of LAMBDA-COCYCLE-ANGLES, the grid 2 pi (1/4) Z[1/5]

```text
Status     NON-CANONICAL independent audit. No authority, no repo edit, no
           registry motion, no probe, no fold. RH remains O and is not treated
           here, per the owner's direction: the grid placement only.
Session    AUDIT-LAMBDA-COCYCLE-GRID, 2026-08-20.
Basis      Public Canon v56 ACTIVE, mathorn1973/twist-j main, clone HEAD
           4ed6cb72, TAG canon-v56, CONTENT_COMMIT b36c93ed, CANON_SHA256
           b284ed6e..b6645, SHA256SUMS 5 of 5 OK, tag and content commit
           verified ancestors of main. Internal line not touched.
Prereg     PREREG-AUDIT-LAMBDA-GRID-1.md, sha256 39a3ef65576e14f41d1b408f5d
           662d85375f4dfb025c46a63e5dfec94230c215, frozen 2026-08-20T17:05:34Z
           before any formal run.
Layer      L6 measure and spectral only. No lift.
Verdict    the angular clause survives the audit intact; the grid itself is
           re-derived as forced, by three independent routes plus one new one;
           two local falsifiers of this audit fired on the audit's own
           material and are archived below; zero findings against the public
           rows; both sealed probes reproduce byte-identically.
```

## 1. The row as pinned, and what is audited

`LAMBDA-COCYCLE-ANGLES [H]` (registry, canon section 18): a cocycle vector
v in L^2(O_lambda, Haar) with ||sum_(k<n) U_J^k v||^2 = lambda_n for all n
exists if and only if RH holds and every Cayley angle
alpha_gamma = 2 arctan(1/(2 gamma)) lies in 2 pi (1/4) Z[1/5]; equivalently
every nontrivial zero is rho = 1/(1 - xi) with xi != 1 and xi^(4 . 5^a) = 1.
Falsifier: RH disproved, or one zero exactly proved off the grid.

Companions audited with it: `LAMBDA-COCYCLE-BRANCH-COLLAPSE [T]` (the exact
Cayley identities and the residual form) and
`LAMBDA-COCYCLE-GRID-EQUIVALENCE [T]` (the orbit theorem, the point spectrum,
the equivalence), sealed evidence probes/P-LAMBDA-COCYCLE-ANGLES-1 and -2.

The owner's question: the placement of the angles into the lattice. Is the
lattice right, is it forced, and what is the honest weight of the clause.

## 2. Falsification first

What would kill the angular clause: one ordinate gamma with
1/(2 gamma) = tan(pi r) exactly excluded for every grid rational r. The grid
ordinates (1/2) cot(pi m/(4 . 5^a)) are dense in the reals, so no finite
enclosure can do this; only a transcendence or irrationality result of a
strength that does not exist for zeta ordinates could. The audit therefore
attacked what is attackable: the exact skeleton that identifies the lattice.
Local falsifiers AF1 to AF8 were frozen in the prereg; two fired, on the
audit's own material, and are archived in section 6. None fired against the
public rows.

## 3. What was verified, by independent paths

The primary verifier avoids the sealed probes' basis (circulant 5-vectors in
Z[x]/(x^5 - 1) rather than the 4-tuple basis); the breaker adds a fresh
4-tuple implementation, a lambda-division valuation with a precision ledger
(no norms), the M_J matrix route built from the axiom step map, and direct
enumeration at level 2. No float exists in any assertion; the ordinate g is a
free polynomial variable throughout; no zeta data was opened.

```text
V1  [T re-verified]  The radial/angular split is exact. On the line the
    Cayley factor is the unit (V^2 - U^2, 2UV, V^2 + U^2)/D at U/V = 1/(2g);
    off the line it is not a unit. So the conjunction "RH and grid" is one
    statement: every w_rho is a torsion point of order 4 . 5^a. Modulus half
    RH, argument half the grid. Checks A5-01..A5-04.

V2  [T companions re-verified; one route added]  The grid is forced, four ways:
    (a) point spectrum of U_J: orbit lengths {1} u {4 . 5^a}, recomputed
        independently: ladder v_lambda(J^4 - 1) = 1, v(J^20 - 1) = 6,
        v(J^(4 . 5^m) - 1) = 4m + 2 for m = 2..6, by the norm route and the
        division route in agreement (AF8 silent), and the matrix route
        ord(M_J in GL_4(Z/5^m)) = 4 . 5^m for m = 1..6, where M_J is taken
        verbatim from the axiom step (a,b,c,d) -> (a-c+d, b-c, a, b-c+d),
        machine-checked equal to multiplication by J. Level-2 unit group
        enumerated directly: 20 units, exponent 20, J of order exactly 20.
    (b) the arithmetic set: reduced fractions with denominator 2^e 5^f,
        e <= 2. Equal to (a) on all denominators to 500.
    (c) NEW ROUTE of this audit: the lambda-adic torsion. The roots of unity
        of the tower Q_5(mu_(5^infinity)) are exactly mu_4 x mu_(5^infinity):
        mu_4 exists (Hensel lift of i from 2 mod 5 to 5^60, and independently
        the Teichmueller construction 2^(5^11) mod 5^12); mu_3 and mu_8 are
        blocked at the residue field (x^2 + x + 1 and x^4 + 1 rootless mod 5;
        the tower is totally ramified by the Eisenstein certificates for
        Phi_5, Phi_25, Phi_125 at x + 1, so the residue field stays F_5 and
        prime-to-5 torsion injects into F_5^x of order 4). In angle terms
        that torsion group is exactly (1/4) Z[1/5] mod 1.
        Consequence: the grid is maximal for EVERY lambda-adic torsion
        transport, not only for the U_J carrier. It cannot be enlarged: a
        1/8-turn or 1/3-turn angle has no lambda-adic home at any level.
    (d) the annihilation reading: dist(4 . 5^A x, Z) -> 0 iff x in
        (1/4) Z[1/5] mod Z, finite rational shadow checked at every declared
        fraction and index; the multiply-by-5 escape argument proves the
        general real case and is elementary.
    Checks A2-*, A3-*, A4-*, BR-01..BR-12.

V3  [candidate-T]  The 1/4 is earned at the base, not decorative. The
    uniformizer itself: (1 - zeta^4)(-zeta) = 1 - zeta exactly, so
    e^(2 i theta) = -zeta for theta = arg(lambda), giving turn 17/20 (fourth
    quadrant certificate): on the grid, NOT in (1/2) Z[1/5]. Any lattice of
    the shape 2 pi (1/2^s) Z[1/5] with s <= 1 already fails at lambda; s >= 3
    is impossible by V2c. The factor is exactly 1/4 and it is
    ord(J mod lambda) = ord(2 in F_5^x) = 4: the residue of the axiom object
    is the doubling map, and its period is the 4 of the grid. (Commentary,
    no layer claim: this is the binary shadow at the ramified place.)
    The same 4 forces the anomalous first ladder step: with w = J^4 - 1,
    res((w/lambda)^4 . u) = -1 mod lambda because fourth powers of units are
    1 in F_5 and u = lambda^4/5 has residue -1, so 5 + w^4 always cancels one
    extra lambda power; the +5 jump at the boundary case is not an accident
    of J but a consequence of the Teichmueller order. Machine-checked, BR-03.

V4  [candidate-T]  The axiom sits on its own grid. The Cayley triangle map
    z -> 1/(1 - z) sends J to -zeta^3 = e^(i pi/5): order 10, turn 1/10, a
    grid point of level 1. Its zero-side image rho_T = 1/(1 - (-zeta^3))
    satisfies, as exact ring identities: rho_T = phi zeta;
    rho_T + conj(rho_T) = 1, so Re(rho_T) = 1/2 exactly; |rho_T|^2 = phi^2;
    cot^2(pi/10) = 4 phi^2 - 1 = 4 phi + 3 in Z[phi]. The point
    1/2 + i (1/2) cot(pi/10) is the level-1 template of the hypothesis: the
    place a zero sits if its Cayley angle is the J-triangle angle. No claim
    that any actual zero is there. Checks A1-09..A1-16.

V5  [T re-verified]  The mechanism of BRANCH-COLLAPSE, symbolically over
    Q[g] and Z[phi], ordinate never instantiated: the second-difference
    identity X^(n+1) + X^(n-1) - 2 X^n = X^(n-1)(X - 1)^2; the reciprocal
    square collapse -rho^2 (A + iB) = (1/4 + g^2) D; the Fejer second
    difference D_(n+1) + D_(n-1) - 2 D_n = 2 cos(n theta) at exact-cosine
    angles including the mu_4 point pi/2; the two-initial-value induction
    rebuild of the ladder from t_n. Checks A5-05..A5-07.

V6  [candidate-T]  The tail test does what the rows say. A grid-supported
    synthetic measure has residual M - t_(n_A) exactly 0 from its level on;
    off-grid atoms at turns 1/3, 1/8, 5/12 keep residual exactly 3m, 4m, 3m
    at every index (period certificates), so a single off-grid atom is seen
    by the n_A subsequence forever and the mu_8 case confirms denominator 8
    is never absorbed. Shared-angle mass bookkeeping of the converse
    construction behaves as sealed. Checks A6-01..A6-04.

V7  [reproduction]  Both sealed public verifiers, at their sealed file
    hashes, reproduce on this platform with byte-identical stdout and exit 0
    (probe 1: 31/31, probe 2: 33/33). Same architecture class as their local
    legs; this is reproduction, not a new architecture leg. BR-13.
```

## 4. Proof reading of the sealed chains

R1 to R7 and S1 to S7 were read in full and re-derived where load-bearing.
The chains are sound. Points checked with extra care: the orthogonality and
mass bookkeeping in S6 (distinct angles give orthogonal eigenvectors, shared
angles merge masses first, total mass lambda_1 finite); the absolute
convergence that permits termwise application of Bombieri-Lagarias in R3; the
uniqueness step that identifies the spectral measure with the Cayley measure
(pure point spectrum forces grid support, symmetrized Fourier uniqueness does
the rest); the branch bookkeeping of arctan in R1. The one historically weak
point, the general finite-profile nonfalsifiability sentence, was withdrawn
in the v39 corrections and the v56 text states the necessary-only status of
the pointwise bounds plainly. The current public text is honest as written.

## 5. What the angular clause actually says, and its weight

Assessment, no status change proposed.

```text
1  The lattice is not a hypothesis. It is the unique angle set available to
   a lambda-adic torsion carrier: point spectrum of U_J, arithmetic set,
   tower torsion, and annihilation reading all coincide, the maximality is
   proved by the mu_3/mu_8 obstructions, the 1/4 is the residue order of J
   and is already required by the uniformizer, the Z[1/5] is the ramified
   tower. Beauty here is necessity. If a lambda-adic cocycle route exists at
   all, this and no other is its angle lattice.
2  The hypothesis is exactly the transfer of that lattice to zeta: every
   ordinate is gamma = (1/2) cot(pi m/(4 . 5^a)), an explicit algebraic
   number of Q(zeta_(4 . 5^a)), abelian over Q. Counting makes the strength
   visible: fewer than 2 . 5^a distinct grid ordinates of level <= a exist
   in total, at all heights, while N(T) grows without bound; so the level
   function on zeros is forced to be unbounded, and the maximal level up to
   height T grows at least like log base 5 of the distinct-ordinate count.
   The quantitative version of this pressure (capacity threshold, forced
   degree growth against the Bui and Heath-Brown conductor tail) is already
   carried by the hash-pinned package C-LAMBDA-COCYCLE-CONDUCTOR-CAPACITY-1-N
   and its sealed review on branch
   agent/review-lambda-cocycle-conductor-capacity-2026-08-14. This audit
   adds no duplicate lane and defers to that one.
3  No finite computation decides the clause: the grid ordinates are dense
   (probe 2's own closing statement), the pointwise Li bounds
   0 <= M - t_n <= 2M are necessary only, and the strict-positive
   finite-profile no-go of notes/C-LAMBDA-COCYCLE-Z5-FOURIER-NORMAL-FORM-1-N
   closes the finite shortcut. The surviving honest attack surfaces are the
   global tail targets delta_A -> 0, the grid-constrained moment feasibility
   gate proposed in RECON-CAYLEY-POLYLOG-SEAM C3 (home: the
   j-li-schoenberg-2 complex), and the conductor-capacity closure route.
   This audit endorses the CLOSING-SLATE reading: the pointwise first clause
   is not provable with current mathematics and the row's practical attack
   surface is the tail clause family.
4  Nothing known contradicts the clause; nothing known supports it beyond
   the internal coherence of the frame. The status H with the registered
   falsifier is exactly right. The row should be quoted only through the V1
   split: radial condition equals RH, angular condition is strictly extra.
```

## 6. Findings of this audit, both archived, neither against a public row

```text
F1  CONJ-FIRED. The audit's frozen closed form ord_(lambda^k)(J) =
    4 . 5^ceil((k-1)/4) is wrong at k in {6, 10, 14}; predicted before the
    run from the registered ladder, confirmed by the run. The measured table
    is 4, then 20 for k = 2..6, 100 for k = 7..10, 500 for k = 11..14, that
    is ord = 4 . 5^max(1, ceil((k-2)/4)) for k >= 2. The registered public
    statements (values at k = 1 and k = 4m) are all confirmed; the fired
    line was the audit's own extrapolation. Archived in the run record.
F2  Check A3-07 of the pinned verifier fired on an audit-code defect: the
    Horner shift kept a spurious trailing zero, so the leading coefficient
    was read from the wrong slot. The computed coefficients were correct,
    Phi_5(x+1) = x^4 + 5x^3 + 10x^2 + 10x + 5. The pinned run stands as
    recorded (51/52); the correction leg verify_lambda_grid_audit_1b.py
    reruns the certificate with the representation fixed and an independent
    congruence certificate Phi(x+1) = x^deg mod 5, 12/12 PASS. Pinned
    artifacts unchanged; both stdouts kept.
```

## 7. Run record

```text
order        prereg frozen and hashed 2026-08-20T17:05:34Z; static compile
             only before the freeze; then single formal run of each program;
             then the 1b correction leg; no threshold moved.
environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC; Linux x86_64; CPython 3.11.15. Single platform:
             candidate labels only.
prereg       PREREG-AUDIT-LAMBDA-GRID-1.md
             sha256 39a3ef65576e14f41d1b408f5d662d85375f4dfb025c46a63e5dfec94230c215  (10671 B)
verifier     verify_lambda_grid_audit_1.py
             sha256 fcb222393e7bf57c30018b54a12a3fc39094982f32c9812f198773885ab0b132  (21140 B)
stdout       verify_lambda_grid_audit_1.stdout.txt, 51/52 PASS + CONJ-FIRED,
             exit 1 by the F2 defect, stderr empty
             sha256 24ce684ad69cda9e38eff107bf8614af5d0ded85535ebf34c6abf026b710c7c5  (3029 B, 56 lines)
correction   verify_lambda_grid_audit_1b.py
             sha256 c31f702adb39f00eef49853845a9cc736cddc83c9851c1f04396de23e8bd5d6a  (1848 B)
stdout       verify_lambda_grid_audit_1b.stdout.txt, 12/12 PASS, exit 0
             sha256 b7bb08dbd05cda11042abb312c61c31a4087df6d3ac4b34f453ec958ae677e77  (672 B, 13 lines)
breaker      breaker_lambda_grid_audit_1.py
             sha256 5a21cbdf2e8c06fde9fa4fda45daebc86a6a99af0db09f00bf147d4833062885  (10261 B)
stdout       breaker_lambda_grid_audit_1.stdout.txt, FINDINGS 0 of 15, exit 0
             sha256 5fca4696670eb5e89d89ec9e39d3cf50de7ef17539ca7c9e23c45cc30ca080af  (1127 B, 16 lines)
ladder       v_lambda(J^(4 . 5^m) - 1), m = 0..6: 1 6 10 14 18 22 26
orders       ord_(lambda^k)(J), k = 1..14: 4 20 20 20 20 20 100 100 100 100
             500 500 500 500
reproduction probe 1 verify.py sealed 3263191d.., stdout 9e46f7f5.. matched;
             probe 2 verify.py sealed 37347d20.., stdout 7c5b6614.. matched;
             both exit 0, stderr empty, run from repository root.
```

## 8. Scope firewall

Single platform, candidate grades only; nothing here earns a public T and no
summary of this audit may exceed the sealed rows' own status or scope. No
statement about RH, about the emptiness or nonemptiness of the cocycle class,
or about any actual zeta ordinate is made anywhere above. L6 only. The
commentary sentences in V3 carry no layer lift. This document, the prereg,
the three programs and the three stdouts live in the project under claude/
and claim nothing by living there.
