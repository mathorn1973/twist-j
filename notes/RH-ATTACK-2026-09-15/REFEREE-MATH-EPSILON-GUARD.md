# REFEREE (mathematics lens): ATTACK-EPSILON-GUARD.md, lane B-epsilon-guard

```text
STATUS      NON-CANONICAL referee report. No status motion, no registry row,
            no probe. Adversarial lens: mathematics.
DATE        2026-09-15
BASIS       Public Canon v86, unchanged
RH          unchanged: open program-level obligation
REVIEWED    ATTACK-EPSILON-GUARD.md, verify_epsilon_guard.py,
            verify_epsilon_guard.stdout.txt (all read in full)
CONTEXT     C-RH-MOBIUS-MEAN-CHANNEL-N.md (+_VERIFY.py, _EXPECTED.txt),
            RH-ONE-WALL-CROSSREF_2026-08-17.md, ZETA-RH-STATUS-2026-09-08.md,
            RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md, REVIEW-CZ.md 3.7 and 4
TESTS       referee_math_tests.py (int and Fraction only; DIAGNOSTIC floats
            for printing only), plus two clean-shell runs of the lane verifier
```

## Falsifiers first

- Verdict on C1: killed if a function $g$ with $tg\in L^1(0,1)$ and
  $\sup_N S_N<\infty$ but $g\notin L^2(0,1)$ exists (it cannot: Riesz-Fischer
  plus moment uniqueness), or if the closed-form Jacobi coefficient used in
  my tests disagrees with the direct sum (it agrees for $n\le30$).
- Verdict on C6 (exponent correction): killed if
  $(2n+3)a_n^2\,n^{1+2\varepsilon}$ for $g=t^{-1/2+\varepsilon/2}$ fails to
  stabilise; it stabilises at $2.03$ ($\varepsilon=1/4$) and $2.00$
  ($\varepsilon=1/16$) for $n\le800$, while the lane's $n^{1+\varepsilon}$
  scaling drifts to zero.
- Every other verdict is a re-derivation; killed by a gap I missed.

## Verdict table

| ID | Verdict | Reason (short) |
|----|---------|----------------|
| C1 | CONFIRMED | Every step re-derived; Parseval tested exactly on $t^{-1/4}\notin V_N$ |
| C2 | CONFIRMED | Cauchy-Schwarz, parameter-integral holomorphy, identity theorem, boundary-line growth: all correct; mechanism is the Nyman-Beurling bounded-functional argument in quotient form, as the lane says |
| C3 | WEAKENED | Theorem 5.1 and Corollary 5.2 correct; Remark 5.3(b) asserts "does not imply RH" flatly (unprovable as stated); Corollary 5.2 proof says "all zeros" where it means nontrivial zeros |
| C4 | CONFIRMED | Lemma 6.2 geometry and constants, Steps 1-3 re-derived; imports (I1)-(I6) are the standard statements, not re-proved here |
| C5 | CONFIRMED | Corollary 7.2 is a correct theorem; Corollary 7.1's "equivalent modulo" is a gloss, the content is three implications |
| C6 | WEAKENED | Table reproduced; HEURISTIC exponent wrong ($n^{-1-2\varepsilon}$, tail $N^{-2\varepsilon}$, not $n^{-1-\varepsilon}$, $N^{-\varepsilon}$); "independent re-implementation" is a verbatim port |
| C7 | CONFIRMED | Placement accurate; one-wall counting honoured; add Burnol (note's external input 3) to the prior-record list |
| O1 | CONFIRMED | |

## Derivations behind the verdicts

### C1

Substitution $x=1/t$: $x^{\varepsilon-2}|F|^2dx=t^{-\varepsilon}|F(1/t)|^2dt$ and
$t^{k+1}g\,dt=F(x)x^{-(k+2-\delta)-1}dx$; (35) is (B.2) at $s=k+2-\delta$.
Rodrigues form and $\int_0^1t^2R_n^2=1/(2n+3)$ re-derived. Completeness of
$\{t^{k+1}\}$ in $L^2(0,1)$ and the converse of Proposition 3.6 (bounded
$S_N$ implies $g\in L^2$) are correct: $\chi=g-G$ has $t\chi\in L^1$ and all
moments zero, hence $\chi=0$ a.e. Exact test: for $g=t^{-1/4}$,
$a_n=\prod_{j=1}^n(\alpha-j)/\prod_{j=0}^n(\alpha+2+j)$ (closed form, agrees
with $\sum_kb_{n,k}/(k+2+\alpha)$ for $n\le30$), and $2-S_N\to0$ with
$(2-S_N)N\to2.05$. The constant in (36) is correctly identified.

### C2, C3, C4, C5

Re-derived line by line; no gap found in the theorems. Two wording defects
in Section 5: (a) Remark 5.3(b) must read "RH implies $H_\varepsilon$;
$H_\varepsilon$ is not known to imply RH, and as a constraint on abstract
zero configurations it admits configurations violating RH"; (b) the
($\Leftarrow$) proof of Corollary 5.2 must say "all nontrivial zeros lie in
the open strip" and add the one-line trivial-zero case ($w=-2k$,
$w-\varepsilon$ is not a zero); it does not use (41). C4: the three-circle
constants are $M(r')\le\max(1,C_2)C_1^a(\log t)^a$, a constant exists as
claimed. C5: "Theorem 6.3 with $\theta=1/2$" is $\theta=1/2+\delta/2$ in the
proof; cosmetic.

### C6

Single-term endpoint behaviour $g\sim t^{\alpha}$, $\alpha=-1/2+\delta+i\gamma$:
$|a_n|\asymp n^{-2\operatorname{Re}\alpha-2}$, so
$(2n+3)|a_n|^2\asymp n^{-4\operatorname{Re}\alpha-3}=n^{-1-4\delta}=n^{-1-2\varepsilon}$
and the tail is $N^{-2\varepsilon}$ ($N^{-1/8}$ at $\varepsilon=1/16$). The
lane prints $n^{-1-\varepsilon}$ and $N^{-\varepsilon}$. Verified exactly
(referee_math_tests.py). The qualitative point of the remark survives.
The interval machinery in verify_epsilon_guard.py is a verbatim port of the
note's (same class, same $N=128$, $p=24$); G8a is a port self-consistency
check, not an independent verification, and should be worded so.

## What this does not do

It does not prove or disprove (41) at any $\varepsilon$, says nothing about
RH, moves no status, and re-proves none of the classical imports.
