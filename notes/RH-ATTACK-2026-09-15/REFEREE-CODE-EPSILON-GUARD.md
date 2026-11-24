# REFEREE (evidence and code lens): ATTACK-EPSILON-GUARD.md, lane B-epsilon-guard

```text
STATUS      NON-CANONICAL referee report. No status motion, no registry row,
            no probe. Adversarial lens: evidence and code.
DATE        2026-09-15
BASIS       Public Canon v86 (STATUS.md ACTIVE, tag canon-v86), unchanged
RH          unchanged: open program-level obligation
REVIEWED    ATTACK-EPSILON-GUARD.md (900 lines), verify_epsilon_guard.py
            (829 lines), verify_epsilon_guard.stdout.txt (57 lines), all in
            full; REFEREE-MATH-EPSILON-GUARD.md and referee_math_tests.py
            (the parallel mathematics-lens report) read for overlap only.
CONTEXT     C-RH-MOBIUS-MEAN-CHANNEL-N.md, _VERIFY.py, _EXPECTED.txt;
            ZETA-RH-STATUS-2026-09-08.md; RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md;
            RH-ONE-WALL-CROSSREF_2026-08-17.md; REVIEW-CZ.md 3.7 and 4;
            O-WEIL-REALIZATION_RECON_2026-07-15.md route 3;
            NOTE-RH-DECODER-CLASSIFICATION_2026-08-12.md section 2.
ARTIFACTS   rerun.stdout.txt (clean-shell rerun), referee_code_mutations.py
            (mutation harness, int/Fraction only, asserts nothing).
```

## Falsifiers first

- Rerun verdict: killed if a clean-shell run of the lane verifier exits
  nonzero or differs from the frozen stdout. It did neither (two runs).
- "G8a is a port, not independent": killed if the interval class, root
  enclosure and Euler-Maclaurin routine of the lane differ materially from
  the note's. They do not (see 2.3).
- "G3d/G3e are bookkeeping tautologies": killed if scrambling the
  stand-in Laurent coefficients of the model makes either check FAIL. It
  does not (mutation M5).
- "HEURISTIC exponent in Section 9 is wrong": killed if
  $(2n+3)a_n^2\,n^{1+\varepsilon}$ stabilises for the single-term model
  $g=t^{-1/2+\varepsilon/2}$. It drifts to zero; $n^{1+2\varepsilon}$
  stabilises at $2.0$ (closed form re-derived, exact values printed as
  DIAGNOSTIC by referee_math_tests.py).
- Every CONFIRMED analytic verdict: killed by a gap I missed in my own
  re-derivation of the cited lemma or theorem.

## 1. Rerun record

```text
command   env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_epsilon_guard.py
python    3.11.15 (/usr/bin/python3 -> python3.11)
exit      0 (both runs)
wall      3.68 s, 3.73 s (declared: about 4 s)
cmp       rerun stdout byte-identical to verify_epsilon_guard.stdout.txt; run 1 == run 2
sha256    verifier 57a5a982...6ba7ce1d (matches declaration)
          stdout   eff1b406...c0379 (matches declaration, both reruns)
checks    31 check() calls in source, 31 PASS lines, 0 FAIL, final line "CHECKS: 31 of 31 PASS"
```

## 2. Source audit

### 2.1 Imports, exactness, floats, determinism

- Imports (lines 39-45): `__future__.annotations`, `sys`, `dataclasses`,
  `fractions.Fraction`, `functools.lru_cache`, `math.comb/factorial/isqrt`.
  Standard library only. No numpy/mpmath/sympy, no `random`, no I/O.
- Every `check()` predicate is int/Fraction arithmetic. The only `float`
  calls are lines 804, 805, 810, inside `diagnostic()`, which prints the
  block headed "DIAGNOSTIC ... asserts nothing" and calls no `check()`.
- Determinism: stand-in arrays and test polynomials use a fixed-seed LCG
  (lines 181-186, 380-386); the one `set` (line 564) is used only for its
  cardinality; polynomial dictionaries are compared by equality, which is
  order-independent; no printed output depends on dict or set order. Two
  clean-shell runs agree byte for byte.
- Exit code: `sys.exit(0 if PASSED == TOTAL else 1)` (line 825).

### 2.2 Bare asserts outside the PASS/FAIL protocol

Lines 275, 484, 694, 741 use `assert` (Laurent-inverse leading coefficient,
rational exponent of the monomial model, integer root enclosure, zeta
enclosure width and positivity). A violation would abort with a traceback
and exit 1 instead of printing a FAIL line, and `python3 -O` would strip
them. Not a correctness defect, a protocol deviation. Minor.

### 2.3 G8a: "independent re-implementation" is a port

Whitespace-stripped character comparison of the lane's interval block
(lines 610-742) against the note's (C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py
lines 13-98) gives similarity 0.84; every difference is quote style,
semicolons, a docstring, or `check(...)` turned into `assert`. Same
`GRID_BITS=256`, `ROOT_BITS=288`, same `nthroot`, same Euler-Maclaurin
with `N=128`, `p=24`, same Bernoulli-polynomial supremum bound. The
PUBLISHED table (lines 767-779) is transcribed correctly from the
_EXPECTED.txt (10 of 10 rows, denominator $10^{12}$). So G8a is a
port self-consistency gate. It is non-vacuous (mutation M4: shifting one
published bound by $10^{-12}$ makes it FAIL), but the words "independent
re-implementation" (verifier line 25, check label line 792, stdout line
31) overstate it. The markdown's own wording, "re-implemented ... after"
(Section 9, line 799-801), is closer to the truth and should be the only
wording.

The Euler-Maclaurin remainder bound inherited from the note is correct as
written: `rising` holds the $2p-1$ factors $s(s+1)\cdots(s+2p-2)$, the tail
integral contributes $N^{-s-2p+1}/(s+2p-1)$ and the lane bounds
$1/(s+2p-1)$ by $1$, so the printed error is an over-estimate. The
enclosures are rigorous relative to the model; nothing in this report
depends on that, since C6 asserts nothing.

### 2.4 Which checks are non-vacuous (mutation harness, referee_code_mutations.py)

```text
M1  test polynomial with constant term (not in V_N)     G4c FAIL, G4d FAIL   (Parseval check is real)
M2  R_3 coefficient perturbed by 1                       G4a, G4e, G4g FAIL   (orthonormality/Rodrigues real)
M3  mu(6) := 0                                           G1a-d all FAIL       (Dirichlet identity real)
M4  one published bound shifted by 1e-12                 G8a FAIL             (gate real, see 2.3)
M5  z-model Laurent coefficients scrambled               G3a-e all PASS       (G3d/G3e are bookkeeping)
M6  theta > sigma_1 in the three-circle geometry         predicate False      (G7b real)
```

M5 detail: in `group_G3` (lines 333-346) the pole order of the stand-in
$\zeta(s+\varepsilon)$ series is an input (`ls(-1, ...)`), and `ls_inv`
sets `lo = -a[0]` (line 276), so the product $Q = z\cdot Y^{-1}$ has
leading index $+1$ by construction and `ls_coef(Q, 0) == 0`,
`ls_coef(Q, -1) == 0` hold for every choice of $z$ and $y$. G3d therefore
certifies "a simple pole in the denominator gives a simple zero of the
quotient in truncated Laurent arithmetic", and G3e certifies
$M(1-\varepsilon) = -c/\varepsilon$ given that. Neither certifies anything
about $\zeta$; Lemma 3.3(b) is carried entirely by the markdown's
$\eta$-function argument, which is correct. The labels "the quotient has a
simple zero at $s=1-\varepsilon$" overstate what the code tests.

Similarly G4f (lines 443-444) and the tuple comparison in G5a (line 466)
are Fraction identities that cannot fail for any $\varepsilon$; they are
bookkeeping, correctly described as such in the markdown, but they inflate
the "31 checks" count.

### 2.5 Scope promised by the verifier map versus code

All ranges match: $k\le400$ (G1), four stand-in arrays (G2), $n,m\le24$
(G4a), 36 test polynomials (G4b-d, counted: 11+12+13), $N\le40$ (G4e),
$n\le40$ (G4g), $k\le40$ and five $\varepsilon$ (G5a), four $\varepsilon$
and two $X$ and four $j$ (G5b), $k\le6$ (G5c), four $\varepsilon$ (G6a-b),
30 points (G6d), six pairs (G7b), ten rows (G8a). Cosmetic: G4g is printed
before G4f (stdout lines 19-20).

### 2.6 Claim-to-check mapping

Real for C2 (G3a-b, G5a, G7a), C3 (G6a-d), C4 (G7a-b), C5 (G6c-d), C6
(G8a). C1 lists G3a-e, which support Lemma 3.3 (used by C2), not the
identification of $g_\varepsilon$; harmless over-listing. No claim
represents a finite check as certifying an analytic statement; the
markdown says so at the head of Section 10 and again in Section 11.

## 3. Markdown audit

- Header block present (lines 4-8): STATUS NON-CANONICAL, DATE 2026-09-15,
  BASIS Public Canon v86, RH unchanged.
- "Falsifiers first" (line 51), verdict table (line 96), "What this does
  not do" (line 874): present.
- No absolute paths, no scratch paths, no machine nicknames, no secrets
  (grep over `/tmp`, `/home`, `/root`, `scratchpad`, the fleet host
  names, `token`, `password`, `@`: zero hits in all three files).
- No forbidden overclaim: no "proves RH", "evidence for RH", "promotes";
  every T is "candidate-T"; the one HEURISTIC step is labelled in capitals.
- Stray phrase: line 699 "(the task's open form '$>5/8$' is implied)"
  refers to the orchestrator's prompt, which a reader of the note cannot
  see. Not a path or nickname; should be deleted.
- Citations checked: note sections 8, 13 (items 4, 6, 7), 14 as cited;
  REVIEW-CZ.md 3.7 (Mellin-Plancherel into $H^2(\operatorname{Re}s>1/2)$)
  and 4 ("natural candidates converge exactly when $1/\zeta$ is controlled
  in $\operatorname{Re}s>1/2$") as cited; O-WEIL-REALIZATION_RECON route 3
  is "Nyman-Beurling / Baez-Duarte" as cited; DECODER-CLASSIFICATION
  section 2 contains "A criterion restates the target" verbatim.
- Compression in Section 8.3: "(24) makes $\mathscr A_Q$ nonvanishing
  there" holds only for $Q\ge4|s+1|$; the note's guard needs an unbounded
  set of dyadic $Q$ and is itself candidate-T. The paraphrase is a gloss.

## 4. Verdict table

| ID | Verdict | Reason |
|----|---------|--------|
| C1 | CONFIRMED | Re-derived Lemma 3.4 (substitution and exponents), Lemma 3.5 (Rodrigues coefficient $\binom{n}{j}\frac{(n+2+j)!}{n!(j+2)!}=\binom nj\binom{n+j+2}{j+2}$, orthogonality by $n$-fold parts, norm $1/(2n+3)$, completeness via $tf\in L^1$), Proposition 3.6 including the Riesz-Fischer converse; Remark 3.6 constant $\int_0^1x^{\varepsilon-2}(c x)^2dx=c^2/(1+\varepsilon)$ exact. Finite pieces non-vacuous (M1, M2). |
| C2 | CONFIRMED | Re-derived Theorem 4.1 (i)-(iv): Cauchy-Schwarz exponent, Plancherel, identity theorem on the connected half-plane, boundary-line contradiction $m\ge1>1/2$, shadow order inequality with $s_0\ne0,1$. G3a-b real; G3d-e bookkeeping only (M5), but Lemma 3.3(b) is proved in text. Mechanism is the note's own Section 8 guard and the REVIEW-CZ Section 4 reading; the lane says so (8.3). |
| C3 | WEAKENED | Theorem 5.1 and Corollary 5.2 are true, but the ($\Leftarrow$) proof of 5.2 (lines 483-487) says "all zeros lie in the open strip", false for trivial zeros; the missing line ($w=-2k$, $w-\varepsilon$ not a zero) is needed. Remark 5.3(b) (lines 497-500) asserts flatly that $\mathrm H_\varepsilon$ "does not imply RH", which is not a provable statement; must read "is not known to imply". G6a-d real. |
| C4 | CONFIRMED (modulo declared imports, as labelled) | Re-derived Lemma 6.2 (disc geometry, Borel-Caratheodory, three circles, $a<1$) and Theorem 6.3 Steps 1-3; exponent $2(-\tfrac34+\tfrac\delta2+\kappa)=-\tfrac54+\tfrac\delta2<-1$ verified; Paley-Wiener and $L^1$ uniqueness used as stated. Cosmetic: line 608 absorbs $\log\lvert t\rvert$ into $\kappa$ silently; line 578 constant should be $\max(1,C_2)C_1^a$. G7a-b real (M6). |
| C5 | CONFIRMED | Corollary 7.2 isolation argument re-derived (infinitely many $\varepsilon\in E$ in $(0,2\beta-1]$, distinct shadows on a compact segment). Cosmetic: "Theorem 6.3 with $\theta=1/2$" in the claim text is $\theta=\tfrac12+\tfrac\delta2$ in the proof (lines 673-676); "equivalent modulo" in 7.1 is a gloss on three implications. |
| C6 | WEAKENED | Table reproduced byte-identically, widths $\le1.4\cdot10^{-28}$ as stated, non-monotone increments as stated. Two defects: (a) HEURISTIC exponent (lines 843-849, repeated in the claim text) is $n^{-1-2\varepsilon}$ with tail $N^{-2\varepsilon}$, not $n^{-1-\varepsilon}$, $N^{-\varepsilon}$ (closed form $a_n=\prod_{j=1}^n(\alpha-j)/\prod_{j=0}^n(\alpha+2+j)$, so $(2n+3)a_n^2\asymp n^{-3-4\alpha}$ with $\alpha=-\tfrac12+\delta$); the qualitative point survives; (b) "independent re-implementation" (verifier lines 25, 792; stdout line 31) is a port (2.3). Status R is unaffected; the text is not. |
| C7 | CONFIRMED (R) | All cited notes exist and say what is attributed to them; one-wall counting honoured; ledger line offered, not folded. Gloss on (24) noted (Section 3 above); stray "the task's" at line 699. |
| O1 | CONFIRMED | Consistent with ZETA-RH-STATUS-2026-09-08.md sections 4-5 and the dependence patch's falsifier standard. |

## 5. Duplicates of the record

- C2's mechanism ($L^2$ membership forces the Mellin quotient into $H^2$,
  poles of $1/\zeta$ become obstructions) is the note's Section 8 guard and
  the Nyman-Beurling reading of REVIEW-CZ.md Section 4; acknowledged in
  Section 8.3 of the lane note. The $\varepsilon$-shifted quotient and the
  shadow-chain bookkeeping are the only parts not already in the record I
  read.
- C5's "RH iff (41) for all $\varepsilon$" is a Baez-Duarte-type family
  equivalence in new clothing; acknowledged as a one-wall reading.
- C7 is a reading by construction.

## 6. What this does not do

It does not prove or disprove (41) at any $\varepsilon$, establishes no
zero-free region, moves no status, and re-proves none of the imports
(I1)-(I7). It confirms only what was re-derived here or re-run here. RH is
unchanged.
