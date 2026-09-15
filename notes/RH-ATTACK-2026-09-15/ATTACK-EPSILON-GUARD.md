# ATTACK-EPSILON-GUARD: strength guard for the fixed-epsilon target (41)

```text
STATUS      NON-CANONICAL incubation note, lane B of the 2026-09-15 RH attack session.
            No status motion. No registry row is touched. No probe is opened.
DATE        2026-09-15
BASIS       Public Canon v86 (tag canon-v86), unchanged by this note
RH          unchanged: an open program-level obligation
            (ZETA-RH-STATUS-2026-09-08.md sections 4-5;
             RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md)
TARGET      the fixed-epsilon target (41) of C-RH-MOBIUS-MEAN-CHANNEL-N.md,
            sections 10-14, with its verifier C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py
            and expected output C-RH-MOBIUS-MEAN-CHANNEL-N_EXPECTED.txt
VERIFIER    verify_epsilon_guard.py (Python 3 standard library, int and
            fractions.Fraction only; 31 checks, all PASS; deterministic under
            LC_ALL=C PYTHONHASHSEED=0; about 4 s); stdout frozen in
            verify_epsilon_guard.stdout.txt; SHA-256 pins in Section 12.  It
            certifies finite algebraic pieces only (four of the 31 checks are
            bookkeeping identities, see Section 10).  The analytic theorems
            are proved in this text.
REVIEW      Two adversarial referee reports (mathematics lens; evidence and
            code lens) of 2026-09-15 applied; every accepted correction is
            listed in Section 11 (Review record).  No status label was
            raised; C3 and C6 carry the referees' wording corrections.
COUNTING    RH-ONE-WALL-CROSSREF_2026-08-17.md applies: this note is a new
            reading of the known wall in Mellin-quotient / Nyman-Beurling
            clothing.  It is not a new theorem about RH.
```

## 0. One-paragraph summary

The note C-RH-MOBIUS-MEAN-CHANNEL-N.md sets as its next target, for one fixed
rational $0<\varepsilon\le 1/4$, the uniform bound (41)
$\sup_N\sum_{n\le N}(2n+3)|a_n(\varepsilon)|^2<\infty$ on its Jacobi moment
energies. Section 3 below identifies the object exactly: (41) is equivalent to
$\|F_\varepsilon\|_\varepsilon<\infty$, the weighted $L^2$ membership of
$F_\varepsilon(x)=c_\varepsilon x-H_\varepsilon(\lfloor x\rfloor)$, with the
exact value $\sum_n(2n+3)|a_n|^2=\|F_\varepsilon\|_\varepsilon^2$. Section 4
proves the guard: this membership forces the Mellin transform into the Hardy
space $H^2$ of the half-plane $\operatorname{Re}s>\tfrac12-\tfrac{\varepsilon}2$,
so the meromorphic quotient $\zeta(s)/(s\,\zeta(s+\varepsilon))$ has no pole
there or on its boundary line; hence every zero $\rho$ of $\zeta$ with
$\operatorname{Re}\rho\ge\tfrac12+\tfrac\varepsilon2$ has an
"$\varepsilon$-shadow" zero at $\rho-\varepsilon$ of at least the same
multiplicity, and iterating, an $\varepsilon$-chain of zeros ending in the strip
$|\operatorname{Re}s-\tfrac12|\le\tfrac\varepsilon2$. Section 6 proves the
converse with a margin: a zero-free half-plane
$\operatorname{Re}w\ge\tfrac12+\tfrac\varepsilon2-\eta$ implies (41). Section 7
draws the two-sided reading as three implications,
$\mathrm{ZF}(\tfrac12+\tfrac\varepsilon2-\eta)\Rightarrow(41)\Rightarrow
\mathrm{ZF}(\tfrac12+\tfrac\varepsilon2)$ or shadow chains (informally: (41)
at $\varepsilon$ sits, up to the shadow caveat and an $\eta$ of margin, at
the quasi-Riemann hypothesis with abscissa $\tfrac12+\tfrac\varepsilon2$;
that phrase is a gloss, not a theorem); (41) along any sequence
$\varepsilon_j\to0$ is RH outright, and RH implies (41) for every
$\varepsilon$. No zero-free
half-plane strictly inside the critical strip is known, so a direct
unconditional proof of (41) at any fixed $\varepsilon<1$ would be the first.
This is a reading of the strength of the note's target, not a result about RH.

## 1. Falsifiers first

Each claim below names what would kill it. A kill of any claim leaves RH
exactly where it is.

- **C1 (identification, candidate-T).** Killed by: a rational polynomial
  $p\in V_N$ with $\sum_n(2n+3)|a_n|^2\ne\|p\|_{L^2(0,1)}^2$ (check G4c); a
  monomial model on which the substitution $t=1/x$ with weight $t^{-\delta}$
  changes the norm or a moment (G5b, G5c); an $f\in L^2(0,1)$, $f\ne0$,
  orthogonal to every $t^{k+1}$, $k\ge0$ (this would break Lemma 3.4 and is
  excluded by Weierstrass); or a definition of $g_\varepsilon$ in the source
  note under which (36) holds with the additive constant on the $(0,1)$ side
  (Remark 3.6 shows there is none).
- **C2 (guard, candidate-T).** Killed by: an $F$ with
  $\|F\|_\varepsilon<\infty$ whose Mellin transform is not holomorphic on
  $\operatorname{Re}s>\tfrac12-\delta$ (excluded by Cauchy-Schwarz, Theorem
  4.1(i)); or a simultaneous exact record of a proof of (41) at some
  $\varepsilon$ and of a zero $\rho$ with
  $\operatorname{Re}\rho\ge\tfrac12+\tfrac\varepsilon2$ and
  $\operatorname{ord}_{\rho-\varepsilon}\zeta<\operatorname{ord}_\rho\zeta$.
  The finite pieces (residue cancellation, the zero at $1-\varepsilon$, the
  exponent at which Cauchy-Schwarz fails) are G3a-e, G5a, G7a.
- **C3 (chain and corollaries, candidate-T after referee wording fixes).**
  Killed by an arithmetic error in the chain bookkeeping (G6a-d) or by a
  flaw in Theorem 4.1. The corollary with hypothesis $\mathrm{H}_\varepsilon$
  is killed by exhibiting two zeros differing by exactly $\varepsilon$ (that
  is a kill of the hypothesis, not of the implication). The statement
  "$\mathrm{H}_\varepsilon$ is not known to imply RH" is killed by a
  published proof that it does.
- **C4 (converse, candidate-T with declared imports).** Killed by a false
  import (Section 6.1 lists each with its exact statement), by a
  counterexample to Lemma 6.2 (a zero-free half-plane with margin on which
  $\log\zeta$ is not $O((\log t)^a)$ with $a<1$), or by an error in the
  uniform $L^2$ bound of Theorem 6.3. The exponent bookkeeping and the
  three-circle geometry are G7a-b.
- **C5 (two-sided reading and ladder, candidate-T).** Killed by a kill of C2,
  C3 or C4, or by an error in the isolation argument of Corollary 7.2 (the
  finite model is G6d).
- **C6 (DIAGNOSTIC table, R).** Cannot be killed; it asserts nothing. The
  port of the note's interval machinery is gated by G8a (port
  self-consistency: exact reproduction of the note's ten published
  enclosures). The HEURISTIC decay exponent $n^{-1-2\varepsilon}$ stated
  there is killed if $(2n+3)a_n^2\,n^{1+2\varepsilon}$ fails to stabilise for
  the single-term model $g=t^{-1/2+\varepsilon/2}$ (it stabilises near $2$ for
  $n\le800$ in exact arithmetic; the lane's original $n^{-1-\varepsilon}$
  did not).
- **C7 (placement, R).** A record of a zero-free half-plane
  $\operatorname{Re}s>\theta$ with $\theta<1$ in the public literature would
  change Section 8.2; nothing else in this note would move.
- **Verifier.** Any FAIL line, any nondeterminism between two clean-shell
  runs, or any use of floating point outside the block labelled DIAGNOSTIC.

## 2. Verdict table

| ID | Statement | Status | Verifier checks |
|----|-----------|--------|-----------------|
| C1 | $g_\varepsilon(t)=t^{-\varepsilon/2}F_\varepsilon(1/t)$ on $(0,1]$; $m_k=\int_0^1 g_\varepsilon t^{k+1}dt=M_\varepsilon(k+2-\tfrac\varepsilon2)$; $\sum_n(2n+3)\lvert a_n\rvert^2=\|F_\varepsilon\|_\varepsilon^2$ exactly, $+\infty$ allowed; (36) is exact only when $g_\varepsilon$ is read on $(0,\infty)$ with the trivial tail $c_\varepsilon t^{-1-\varepsilon/2}$ on $(1,\infty)$; $\sup_N L_N<\infty\iff\|F_\varepsilon\|_\varepsilon<\infty$ | candidate-T | G1a-d, G2a-d, G4a-g, G5a-d (G3a-e support Lemma 3.3, used by C2) |
| C2 | If $\|F_\varepsilon\|_\varepsilon<\infty$ then $M_\varepsilon\in H^2(\operatorname{Re}s>\tfrac12-\tfrac\varepsilon2)$, $\zeta(s)/(s\zeta(s+\varepsilon))$ has no pole in $\operatorname{Re}s\ge\tfrac12-\tfrac\varepsilon2$ except $s=1$, and every zero $\rho$ with $\operatorname{Re}\rho\ge\tfrac12+\tfrac\varepsilon2$ has $\operatorname{ord}_{\rho-\varepsilon}\zeta\ge\operatorname{ord}_\rho\zeta$ | candidate-T | G3a-b, G3d-e, G5a, G7a (finite pieces only) |
| C3 | (41) at $\varepsilon$ forces $\varepsilon$-chains ending in $[\tfrac12-\tfrac\varepsilon2,\tfrac12+\tfrac\varepsilon2)$ with non-decreasing multiplicity; with $\mathrm{H}_\varepsilon$ (no two zeros differ by exactly $\varepsilon$) it gives $\zeta\ne0$ on $\operatorname{Re}s\ge\tfrac12+\tfrac\varepsilon2$, and conversely that zero-free half-plane gives $\mathrm{H}_\varepsilon$ unconditionally; RH implies $\mathrm{H}_\varepsilon$, $\mathrm{H}_\varepsilon$ is not known to imply RH; the hypothesis "no two zeros share an ordinate" is RH itself and yields nothing | candidate-T (wording corrected on referee review, Section 11) | G6a-d |
| C4 | If $\zeta(w)\ne0$ for $\operatorname{Re}w\ge\tfrac12+\tfrac\varepsilon2-\eta$, some $\eta>0$, then $\|F_\varepsilon\|_\varepsilon<\infty$, i.e. (41) holds | candidate-T (imports declared in 6.1) | G7a-b |
| C5 | Three implications: $\mathrm{ZF}(\tfrac12+\tfrac\varepsilon2-\eta)$ for some $\eta>0$ $\Rightarrow$ (41) at $\varepsilon$ $\Rightarrow$ $\mathrm{ZF}(\tfrac12+\tfrac\varepsilon2)$ or shadow chains (the phrase "quasi-RH modulo the shadow caveat and an $\eta$ of margin" is a gloss on these); (41) on a set of $\varepsilon$ accumulating at $0$ $\iff$ RH; RH $\Rightarrow$ (41) for every $\varepsilon\in(0,\tfrac14]$ (Theorem 6.3 with $\eta=\delta/2$, i.e. $\theta=\tfrac12+\tfrac\delta2$) | candidate-T | G6c-d |
| C6 | $L_N(\varepsilon)$ enclosures to $N=64$ for $\varepsilon=\tfrac14,\tfrac1{16}$, computed with a port of the note's interval machinery; increments do not decay visibly at this scope; finite partial sums decide nothing; HEURISTIC single-term decay $n^{-1-2\varepsilon}$, tail $N^{-2\varepsilon}$ | R (DIAGNOSTIC; exponent corrected on referee review) | G8a is a port self-consistency gate; the table asserts nothing |
| C7 | Placement: the target is a zero-free half-plane target (a quasi-RH rung); no such half-plane is known; the note's program becomes a ladder $\varepsilon\to0$; one wall, new reading | R | none |
| O  | (41) at any fixed $\varepsilon>0$; a zero-free half-plane strictly inside the critical strip; RH | O | none |

Throughout, $\delta:=\varepsilon/2$.

## 3. Objects and the identification of $g_\varepsilon$ (C1)

### 3.1 Standing notation

Fix a rational $\varepsilon$ with $0<\varepsilon\le\tfrac14$ and put
$\delta=\varepsilon/2\le\tfrac18$. As in the note, sections 9-11,

$$h_\varepsilon(k)=\sum_{d\mid k}\mu(d)d^{-\varepsilon}=\prod_{p\mid k}(1-p^{-\varepsilon}),\qquad
H_\varepsilon(n)=\sum_{k\le n}h_\varepsilon(k),\qquad
c_\varepsilon=\frac1{\zeta(1+\varepsilon)},$$

$$F_\varepsilon(x)=c_\varepsilon x-H_\varepsilon(\lfloor x\rfloor)\quad(x\ge1),\qquad
\|f\|_\varepsilon^2=\int_1^\infty x^{\varepsilon-2}|f(x)|^2dx .$$

Since every factor $1-p^{-\varepsilon}$ lies in $(0,1)$,
$0<h_\varepsilon(k)\le1$, hence $0\le H_\varepsilon(n)\le n$ and, with
$0<c_\varepsilon<1$,

$$|F_\varepsilon(x)|\le(1+c_\varepsilon)\,x\le 2x\qquad(x\ge1). \tag{B.1}$$

Write $Q_\varepsilon(s):=\zeta(s)/(s\,\zeta(s+\varepsilon))$, a meromorphic
function on $\mathbb C$, and $M_\varepsilon(s):=\int_1^\infty
F_\varepsilon(x)x^{-s-1}dx$ wherever the integral converges absolutely. The
note's moments (35), polynomials $R_n$, coefficients $b_{n,k}$ and
$a_n(\varepsilon)=\sum_{k\le n}b_{n,k}m_k(\varepsilon)$ are used unchanged;
$b_{n,k}=(-1)^{n-k}\binom nk\binom{n+k+2}{k+2}$ is the coefficient of $t^k$ in
$R_n(t)$.

### 3.2 Dirichlet series and the Mellin identity (34)

**Lemma 3.1.** For $\operatorname{Re}s>1$,
$\sum_{k\ge1}h_\varepsilon(k)k^{-s}=\zeta(s)/\zeta(s+\varepsilon)$, both sides
absolutely convergent.

*Proof.* $\sum_d\mu(d)d^{-\varepsilon}d^{-s}=1/\zeta(s+\varepsilon)$ converges
absolutely for $\operatorname{Re}(s+\varepsilon)>1$, in particular for
$\operatorname{Re}s>1$, and so does $\zeta(s)=\sum_m m^{-s}$. The Dirichlet
product of two absolutely convergent Dirichlet series is the Dirichlet series
of the convolution of their coefficients; the coefficient of $k^{-s}$ is
$\sum_{d\mid k}\mu(d)d^{-\varepsilon}=h_\varepsilon(k)$. The product formula
$h_\varepsilon(k)=\prod_{p\mid k}(1-p^{-\varepsilon})$ is the multiplicativity
of $d\mapsto\mu(d)d^{-\varepsilon}$. $\square$

The verifier checks the coefficient identity as an identity of polynomials
over $\mathbb Q$ in formal variables $u_p$ (standing for $p^{-\varepsilon}$):
$(1*\mu u)(k)=\prod_{p\mid k}(1-u_p)$ for all $k\le400$ (G1a), that
$\mu(d)u_d$ is the Dirichlet inverse of the completely multiplicative
$u_k=\prod_{p^e\|k}u_p^e$ (G1b), and the specialisations $u_p=0$, $u_p=1$,
$u_p=\tfrac12$ (G1c, G1d).

**Lemma 3.2 (identity (34)).** For $\operatorname{Re}s>1$ the integral
$M_\varepsilon(s)$ converges absolutely and

$$M_\varepsilon(s)=\frac{c_\varepsilon}{s-1}-\frac{\zeta(s)}{s\,\zeta(s+\varepsilon)}=\frac{c_\varepsilon}{s-1}-Q_\varepsilon(s). \tag{B.2}$$

*Proof.* Absolute convergence for $\sigma=\operatorname{Re}s>1$ follows from
(B.1). $\int_1^\infty c_\varepsilon x\cdot x^{-s-1}dx=c_\varepsilon/(s-1)$.
For the step part, $H_\varepsilon(\lfloor x\rfloor)=\sum_{n\le x}h_\varepsilon(n)$,
so by Tonelli (all terms positive for real $s$, and absolutely convergent in
general since $\sum_n h_\varepsilon(n)n^{-\sigma}<\infty$)

$$\int_1^\infty H_\varepsilon(\lfloor x\rfloor)x^{-s-1}dx=\sum_{n\ge1}h_\varepsilon(n)\int_n^\infty x^{-s-1}dx=\frac1s\sum_{n\ge1}h_\varepsilon(n)n^{-s}=\frac{\zeta(s)}{s\,\zeta(s+\varepsilon)}$$

by Lemma 3.1. $\square$

The step-function integration is checked exactly on truncated models: integer
$s$ with exact antiderivatives (G2a), rational $s=p/q$ with jump points at
$q$-th powers so that every value $x_j^{-s}$ is rational (G2b), the formal Abel
identity as linear forms in symbols $v_n$ (G2c), and the telescoping of the
linear term (G2d).

**Lemma 3.3 (local structure of $Q_\varepsilon$ at $s=1$, $1-\varepsilon$, $0$).**
(a) $Q_\varepsilon$ has a simple pole at $s=1$ with residue
$c_\varepsilon=1/\zeta(1+\varepsilon)$, so $M_\varepsilon$ as given by (B.2) is
regular at $s=1$. (b) $Q_\varepsilon(1-\varepsilon)=0$: the point
$s=1-\varepsilon$ is a simple zero of $Q_\varepsilon$ (not of $M_\varepsilon$)
and $M_\varepsilon(1-\varepsilon)=-c_\varepsilon/\varepsilon\ne0$. (c)
$Q_\varepsilon$ has a simple pole at $s=0$ with residue
$-1/(2\zeta(\varepsilon))\ne0$; it lies to the left of the line
$\operatorname{Re}s=\tfrac12-\delta\ge\tfrac38$.

*Proof.* (a) $\zeta(s)=(s-1)^{-1}+\gamma_0+O(s-1)$ and
$1/(s\zeta(s+\varepsilon))$ is holomorphic near $s=1$ with value
$1/\zeta(1+\varepsilon)=c_\varepsilon$; the product has residue $c_\varepsilon$
and the constant term of (B.2) is
$c_\varepsilon\bigl(1+\zeta'(1+\varepsilon)/\zeta(1+\varepsilon)-\gamma_0\bigr)$
(G3a-c check this Laurent bookkeeping exactly on stand-in models). (b)
$\zeta(s+\varepsilon)$ has a simple pole at $s=1-\varepsilon$, so
$1/\zeta(s+\varepsilon)$ has a simple zero there, while
$\zeta(1-\varepsilon)/(1-\varepsilon)$ is finite and nonzero because $\zeta$
has no zero on the real segment $(0,1)$: from
$\eta(\sigma)=(1-2^{1-\sigma})\zeta(\sigma)$ with the alternating series
$\eta(\sigma)=\sum(-1)^{n-1}n^{-\sigma}>0$ and $1-2^{1-\sigma}<0$ one gets
$\zeta(\sigma)<0$ on $(0,1)$. Hence $M_\varepsilon(1-\varepsilon)=
c_\varepsilon/(1-\varepsilon-1)=-c_\varepsilon/\varepsilon$ (G3d-e). (c)
$\zeta(0)=-\tfrac12$ and $\zeta(\varepsilon)<0$. $\square$

### 3.3 The reciprocal coordinate

**Lemma 3.4 (identification of $g_\varepsilon$).** Define
$g_\varepsilon(t):=t^{-\delta}F_\varepsilon(1/t)$ for $0<t\le1$. Then

(a) $\|F_\varepsilon\|_\varepsilon^2=\int_0^1|g_\varepsilon(t)|^2dt$, both sides in $[0,\infty]$;

(b) $|g_\varepsilon(t)|\le2t^{-1-\delta}$, so $t\,g_\varepsilon(t)\in L^1(0,1)$;

(c) for every integer $k\ge0$, $\int_0^1 g_\varepsilon(t)t^{k+1}dt$ converges
absolutely and equals $M_\varepsilon(k+2-\delta)=m_k(\varepsilon)$, the
note's moment (35).

*Proof.* Substitute $x=1/t$, $dx=-t^{-2}dt$. (a):
$x^{\varepsilon-2}|F(x)|^2dx=t^{2-\varepsilon}|F(1/t)|^2t^{-2}dt=|t^{-\delta}F(1/t)|^2dt$
since $2\delta=\varepsilon$. (b) is (B.1). (c):
$t^{k+1}g(t)\,dt=t^{k+1-\delta}F(1/t)\,dt=F(x)x^{-(k+1-\delta)}x^{-2}dx=F(x)x^{-(k+2-\delta)-1}dx$,
and $k+2-\delta>1$, so Lemma 3.2 applies; (B.2) at $s=k+2-\delta$ is
$c_\varepsilon/(k+1-\delta)-\zeta(k+2-\delta)/\bigl((k+2-\delta)\zeta(k+2+\delta)\bigr)$,
which is (35). $\square$

Check G5a records the formal identity "(35) is (34) at $s=k+2-\delta$" for
$k\le40$ and five values of $\varepsilon$, together with the exponent
bookkeeping of the substitution; G5b and G5c check the substitution itself
exactly on monomial models $F=x^j$ on $[1,X]$ with $X=r^{2q}$, so that every
power $X^{\delta}$ is rational, for both the norm and the moments; G5d
brackets the one power-rule integral used there between exact Riemann sums.

**Lemma 3.5 (the orthonormal basis).** Let $e_n(t):=\sqrt{2n+3}\,t\,R_n(t)$,
$n\ge0$. Then $\{e_n\}$ is an orthonormal basis of $L^2(0,1)$, and
$\operatorname{span}\{e_0,\dots,e_N\}=V_N=\operatorname{span}\{t,\dots,t^{N+1}\}$.

*Proof.* Rodrigues form: expanding $t^{n+2}(1-t)^n=\sum_j(-1)^j\binom nj t^{n+2+j}$
and differentiating $n$ times,

$$\frac{(-1)^n}{n!}\,t^{-2}\frac{d^n}{dt^n}\bigl[t^{n+2}(1-t)^n\bigr]=\sum_{j=0}^n(-1)^{n-j}\binom nj\frac{(n+2+j)!}{n!\,(j+2)!}t^j=\sum_{j=0}^n(-1)^{n-j}\binom nj\binom{n+j+2}{j+2}t^j=R_n(t)$$

(G4g checks this exactly for $n\le40$). For $m<n$, integrating by parts $n$
times, $\int_0^1t^2\,t^mR_n(t)\,dt=\frac{(-1)^n}{n!}\int_0^1 t^m\,D^n[t^{n+2}(1-t)^n]dt
=\frac1{n!}\int_0^1 D^n[t^m]\,t^{n+2}(1-t)^n\,dt=0$; the boundary terms vanish
because $D^j[t^{n+2}(1-t)^n]$ vanishes at $0$ and $1$ for $j<n$. For $m=n$ the
same computation gives $\int_0^1t^2t^nR_n\,dt=\frac1{n!}\,n!\,B(n+3,n+1)=
\frac{(n+2)!\,n!}{(2n+3)!}$, and the leading coefficient of $R_n$ is
$\binom{2n+2}{n+2}=\frac{(2n+2)!}{(n+2)!\,n!}$, so
$\int_0^1t^2R_n^2dt=\frac{(2n+2)!}{(n+2)!\,n!}\cdot\frac{(n+2)!\,n!}{(2n+3)!}=\frac1{2n+3}$.
Hence $\int_0^1e_ne_m\,dt=\delta_{nm}$ (G4a checks this exactly for
$n,m\le24$; the note's verifier checks it to 12). Since $tR_n$ has degree
exactly $n+1$, the span statement follows.

Completeness: let $f\in L^2(0,1)$ be orthogonal to every $e_n$, hence to every
$t^{k+1}$, $k\ge0$. Then $\lambda:=t f\in L^1(0,1)$ satisfies
$\int_0^1\lambda(t)t^jdt=0$ for all $j\ge0$. By Weierstrass, for every
$\varphi\in C[0,1]$ there are polynomials $p_m\to\varphi$ uniformly, so
$\int\lambda\varphi=\lim\int\lambda p_m=0$. A finite signed measure
$\lambda\,dt$ on $[0,1]$ annihilating $C[0,1]$ is zero (uniqueness in the
Riesz representation theorem), so $\lambda=0$ a.e., so $f=0$ a.e. $\square$

**Proposition 3.6 (exact equivalence).** For every $n\ge0$,
$a_n(\varepsilon)=\int_0^1g_\varepsilon(t)\,tR_n(t)\,dt=\langle g_\varepsilon,e_n\rangle/\sqrt{2n+3}$,
the integral converging absolutely. Put
$S_N(\varepsilon):=\sum_{n\le N}(2n+3)|a_n(\varepsilon)|^2$, so that
$L_N=c_\varepsilon^2/(1+\varepsilon)+S_N$ by (37). Then

$$\sup_N S_N(\varepsilon)<\infty\iff g_\varepsilon\in L^2(0,1)\iff\|F_\varepsilon\|_\varepsilon<\infty,$$

and in every case $\lim_{N}S_N(\varepsilon)=\sum_{n\ge0}(2n+3)|a_n(\varepsilon)|^2=\|F_\varepsilon\|_\varepsilon^2\in[0,\infty]$.

*Proof.* $a_n=\sum_kb_{n,k}m_k=\sum_kb_{n,k}\int_0^1g\,t^{k+1}dt=\int_0^1g\,tR_n\,dt$
by Lemma 3.4(c) (a finite sum of absolutely convergent integrals; G4b checks
the two definitions agree exactly on 36 rational test polynomials). If
$g\in L^2(0,1)$, Parseval for the orthonormal basis of Lemma 3.5 gives
$\sum_n|\langle g,e_n\rangle|^2=\|g\|_2^2$, i.e. $\sum_n(2n+3)|a_n|^2=\|g\|_2^2=\|F\|_\varepsilon^2$
by Lemma 3.4(a). Conversely suppose $\sup_NS_N=:S<\infty$. By Riesz-Fischer,
$G:=\sum_n\langle g,e_n\rangle e_n$ converges in $L^2(0,1)$ and
$\langle G,e_n\rangle=\langle g,e_n\rangle$ for all $n$. The function
$\chi:=g-G$ satisfies $\int_0^1\chi\,t^{k+1}dt=0$ for all $k\ge0$, and
$t\chi\in L^1(0,1)$ by Lemma 3.4(b) and $G\in L^2\subset L^1$. The argument
of Lemma 3.5 (Weierstrass and Riesz uniqueness applied to $\lambda=t\chi$)
gives $\chi=0$ a.e., so $g=G\in L^2(0,1)$ and $\|g\|_2^2=S$. If
$g\notin L^2$, then $S_N$ is unbounded by the first part, and
$\|F\|_\varepsilon=\infty$ by Lemma 3.4(a), so both sides are $+\infty$.
$\square$

G4c checks $\sum_n(2n+3)|a_n|^2=\|p\|_{L^2(0,1)}^2$ exactly, with no additive
constant, for 36 rational polynomials $p\in V_N$; G4d checks $a_n=0$ for
$n\ge\deg p$ and the Bessel monotonicity; G4e checks, for the constant
function $p=1\notin V_N$, the exact Muentz deficit
$1-S_N=1/(N+2)^2$ for $N\le40$, which exhibits both that the system exhausts
$L^2(0,1)$ and the endpoint concentration scale $(N+2)^{-2}$ named after
(39) in the note.

### 3.4 Remark 3.6: the constant in (36)

The note prints (36) as
$\|g_\varepsilon\|_2^2=c_\varepsilon^2/(1+\varepsilon)+\sum_n(2n+3)|a_n|^2$
without printing a definition of $g_\varepsilon$. By Proposition 3.6 the sum
equals $\|F_\varepsilon\|_\varepsilon^2=\int_0^1|t^{-\delta}F_\varepsilon(1/t)|^2dt$
with no additive constant. The constant is exactly

$$\frac{c_\varepsilon^2}{1+\varepsilon}=\int_0^1x^{\varepsilon-2}(c_\varepsilon x)^2dx=\int_1^\infty c_\varepsilon^2\,t^{-2-2\delta}dt ,$$

the energy of the trivial piece $F_\varepsilon(x)=c_\varepsilon x$ on
$0<x<1$, where $H_\varepsilon(\lfloor x\rfloor)=0$ (G4f records the exponent
bookkeeping). Hence (36) is exact precisely when $g_\varepsilon$ denotes the
reciprocal-coordinate function on the whole half-line,
$g_\varepsilon(t)=t^{-\delta}F_\varepsilon(1/t)$ for $0<t<\infty$ with
$F_\varepsilon(x)=c_\varepsilon x$ on $(0,1)$, so that
$g_\varepsilon(t)=c_\varepsilon t^{-1-\delta}$ for $t>1$ and
$\|g_\varepsilon\|_2$ is the $L^2(0,\infty)$ norm. The note's own words
"whole-domain moments" and "extended exact identity" fit this reading, and
(39) integrates over $(0,1)$ only, consistently. Under the alternative reading
"$g_\varepsilon$ on $(0,1)$ only", (36) is off by exactly
$c_\varepsilon^2/(1+\varepsilon)$. This does not affect the target:

$$\lim_{N\to\infty}L_N(\varepsilon)=\frac{c_\varepsilon^2}{1+\varepsilon}+\|F_\varepsilon\|_\varepsilon^2=\int_0^\infty x^{\varepsilon-2}|F_\varepsilon(x)|^2dx\in[0,\infty],$$

and **(41) holds at $\varepsilon$ if and only if $\|F_\varepsilon\|_\varepsilon<\infty$.**

## 4. The guard (C2)

### 4.1 Definitions

For $\sigma_0\in\mathbb R$, $H^2(\operatorname{Re}s>\sigma_0)$ denotes the
Hardy space of functions $f$ holomorphic on the open half-plane with
$\sup_{\sigma>\sigma_0}\int_{\mathbb R}|f(\sigma+it)|^2dt<\infty$. Fourier
convention: $\hat\varphi(y)=\int_{\mathbb R}\varphi(u)e^{-iyu}du$, Plancherel
$\int|\hat\varphi|^2=2\pi\int|\varphi|^2$. Put

$$\varphi(u):=F_\varepsilon(e^u)\,e^{-(\frac12-\delta)u}\qquad(u>0). \tag{B.3}$$

With $x=e^u$, $dx=x\,du$:
$\int_0^\infty|\varphi(u)|^2du=\int_1^\infty|F_\varepsilon(x)|^2x^{-(1-\varepsilon)}\frac{dx}x=\|F_\varepsilon\|_\varepsilon^2$,
and for $\operatorname{Re}s>1$,
$M_\varepsilon(s)=\int_0^\infty F_\varepsilon(e^u)e^{-su}du=\int_0^\infty\varphi(u)e^{-zu}du$
with $z:=s-(\tfrac12-\delta)$. So $M_\varepsilon(\tfrac12-\delta+z)$ is the
Laplace transform $(\mathcal L\varphi)(z)$ of $\varphi$, and
$\varphi\in L^2(0,\infty)$ if and only if $\|F_\varepsilon\|_\varepsilon<\infty$.

### 4.2 The theorem

**Theorem 4.1 (Hardy-space guard).** Assume $\|F_\varepsilon\|_\varepsilon<\infty$. Then:

(i) $M_\varepsilon(s)=\int_1^\infty F_\varepsilon(x)x^{-s-1}dx$ converges
absolutely for every $s$ with $\operatorname{Re}s>\tfrac12-\delta$, with

$$|M_\varepsilon(s)|\le\frac{\|F_\varepsilon\|_\varepsilon}{\sqrt{2\operatorname{Re}s+\varepsilon-1}}, \tag{B.4}$$

and $M_\varepsilon$ is holomorphic on $\operatorname{Re}s>\tfrac12-\delta$.

(ii) $M_\varepsilon\in H^2(\operatorname{Re}s>\tfrac12-\delta)$ with
$\sup_{\sigma>\frac12-\delta}\int|M_\varepsilon(\sigma+it)|^2dt=2\pi\|F_\varepsilon\|_\varepsilon^2$;
the boundary function $M_\varepsilon(\tfrac12-\delta+i\,\cdot)$ exists as the
$L^2(\mathbb R)$-limit of $M_\varepsilon(\sigma+i\,\cdot)$ as
$\sigma\downarrow\tfrac12-\delta$, equals $\hat\varphi$, and
$\int_{\mathbb R}|M_\varepsilon(\tfrac12-\delta+it)|^2dt=2\pi\|F_\varepsilon\|_\varepsilon^2$
(Mellin-Plancherel on the line $\operatorname{Re}s=\tfrac12-\delta$).

(iii) On $\operatorname{Re}s>\tfrac12-\delta$ the identity
$Q_\varepsilon(s)=c_\varepsilon/(s-1)-M_\varepsilon(s)$ holds as an identity
of meromorphic functions. Consequently $Q_\varepsilon$ has exactly one pole in
the open half-plane, the simple pole at $s=1$ with residue $c_\varepsilon$, and
no pole on the closed half-plane $\operatorname{Re}s\ge\tfrac12-\delta$ other
than $s=1$.

(iv) ($\varepsilon$-shadow) For every zero $w$ of $\zeta$ with
$\operatorname{Re}w\ge\tfrac12+\delta$,

$$\operatorname{ord}_{w-\varepsilon}(\zeta)\ \ge\ \operatorname{ord}_w(\zeta)\ \ge1 .$$

In particular every nontrivial zero $\rho$ with
$\operatorname{Re}\rho\ge\tfrac12+\tfrac\varepsilon2$ has a nontrivial zero
at $\rho-\varepsilon$ (same ordinate, real part smaller by $\varepsilon$) of
at least the same multiplicity.

*Proof.* (i) For $\sigma=\operatorname{Re}s$, by Cauchy-Schwarz,

$$\int_1^\infty|F_\varepsilon(x)|x^{-\sigma-1}dx=\int_1^\infty\bigl(|F_\varepsilon(x)|x^{\frac\varepsilon2-1}\bigr)\bigl(x^{-\sigma-\frac\varepsilon2}\bigr)dx\le\|F_\varepsilon\|_\varepsilon\Bigl(\int_1^\infty x^{-2\sigma-\varepsilon}dx\Bigr)^{1/2}=\frac{\|F_\varepsilon\|_\varepsilon}{\sqrt{2\sigma+\varepsilon-1}},$$

finite exactly when $2\sigma+\varepsilon-1>0$, i.e. $\sigma>\tfrac12-\delta$
(G7a checks that the exponent vanishes exactly at $\sigma=\tfrac12-\delta$).
Holomorphy: on a compact subset $K$ of the open half-plane with
$\sigma_K:=\min_K\operatorname{Re}s>\tfrac12-\delta$ the integrand is
dominated by $|F_\varepsilon(x)|x^{-\sigma_K-1}\in L^1(1,\infty)$, so the
parameter integral is holomorphic (Morera and Fubini, or differentiation
under the integral sign).

(ii) For $\sigma>\tfrac12-\delta$ put $x_\sigma:=\sigma-\tfrac12+\delta>0$ and
$\varphi_\sigma(u):=\varphi(u)e^{-x_\sigma u}$ for $u>0$, $0$ for $u\le0$.
Then $\varphi_\sigma\in L^1\cap L^2(\mathbb R)$ (Cauchy-Schwarz against
$e^{-x_\sigma u}$) and $M_\varepsilon(\sigma+it)=\hat\varphi_\sigma(t)$. By
Plancherel, $\int|M_\varepsilon(\sigma+it)|^2dt=2\pi\int_0^\infty|\varphi(u)|^2e^{-2x_\sigma u}du\le2\pi\|\varphi\|_2^2=2\pi\|F_\varepsilon\|_\varepsilon^2$,
with equality in the limit $\sigma\downarrow\tfrac12-\delta$ by monotone
convergence. As $\sigma\downarrow\tfrac12-\delta$, $\varphi_\sigma\to\varphi$
in $L^2(\mathbb R)$ (dominated convergence), hence
$\hat\varphi_\sigma\to\hat\varphi$ in $L^2(\mathbb R)$ by the Plancherel
isometry; this is the boundary function, and its norm identity is Plancherel
again. (These are the elementary halves of the Paley-Wiener theorem; the
converse half is used only in Section 6.)

(iii) By Lemma 3.2, $D(s):=M_\varepsilon(s)-c_\varepsilon/(s-1)+Q_\varepsilon(s)$
vanishes on $\operatorname{Re}s>1$. By (i) and the meromorphy of
$Q_\varepsilon$, $D$ is meromorphic on the connected open half-plane
$\operatorname{Re}s>\tfrac12-\delta$; a meromorphic function on a connected
domain vanishing on a nonempty open subset vanishes identically. So
$Q_\varepsilon=c_\varepsilon/(s-1)-M_\varepsilon$ there, and the poles of
$Q_\varepsilon$ in the open half-plane are those of $c_\varepsilon/(s-1)$:
the simple pole at $s=1$ (which lies in the half-plane since
$1>\tfrac12-\delta$) with residue $c_\varepsilon$, consistent with Lemma
3.3(a). Boundary line: suppose $Q_\varepsilon$ had a pole of order $m\ge1$
at a point $s_0$ with $\operatorname{Re}s_0=\tfrac12-\delta$ (so $s_0\ne1$).
Then $|Q_\varepsilon(s_0+x)|\ge C'x^{-m}$ for small $x>0$, while
$|c_\varepsilon/(s_0+x-1)|\le C''$, so
$|M_\varepsilon(s_0+x)|\ge C'x^{-m}-C''$; but (B.4) at $s=s_0+x$ reads
$|M_\varepsilon(s_0+x)|\le\|F_\varepsilon\|_\varepsilon(2x)^{-1/2}$, since
$2\operatorname{Re}(s_0+x)+\varepsilon-1=2x$. As $x\to0^+$ this is
contradictory because $m\ge1>\tfrac12$.

(iv) Let $\zeta(w)=0$ with $\operatorname{Re}w\ge\tfrac12+\delta$ and put
$s_0:=w-\varepsilon$, so $\operatorname{Re}s_0\ge\tfrac12-\delta>0$; in
particular $s_0\ne0$ and $s_0\ne1$ (the latter would need
$\zeta(1+\varepsilon)=0$). Near $s_0$, $1/\zeta(s+\varepsilon)$ has a pole of
order $m:=\operatorname{ord}_w\zeta\ge1$, $1/s$ is holomorphic and nonzero,
and $\zeta(s)$ has a zero of order $m':=\operatorname{ord}_{s_0}\zeta\ge0$. So
$Q_\varepsilon$ has a pole of order $m-m'$ at $s_0$ if $m>m'$. By (iii) this
cannot happen; hence $m'\ge m$. If $w=\rho$ is a nontrivial zero, then
$\operatorname{Im}\rho\ne0$ (no real zeros in $(0,1)$, Lemma 3.3(b)), so
$\rho-\varepsilon$ has nonzero imaginary part and cannot be a trivial zero
(the trivial zeros $-2,-4,\dots$ are real and negative); as
$0<\tfrac12-\delta\le\operatorname{Re}(\rho-\varepsilon)<1-\varepsilon<1$,
the forced zero is a nontrivial zero in the critical strip. $\square$

**Remarks.** (1) The pole of $\zeta(s)$ at $s=1$ is cancelled in (B.2) exactly
by $c_\varepsilon/(s-1)$ (Lemma 3.3(a), G3a-b); the point $s=1-\varepsilon$
is a zero of $Q_\varepsilon$ and no obstruction (Lemma 3.3(b), G3d-e); the
pole of $Q_\varepsilon$ at $s=0$ and the poles at $s=-2m-\varepsilon$ (trivial
zeros of $\zeta(s+\varepsilon)$) lie in $\operatorname{Re}s<0$, to the left of
the line (Lemma 3.3(c)). (2) The guard uses only Cauchy-Schwarz, holomorphy of
a parameter integral and the identity theorem; the $H^2$ statement (ii) is
recorded because it is what makes Section 6 an equivalence. (3) Everything in
this section holds verbatim for $0<\varepsilon<1$; the restriction to
$\varepsilon\le\tfrac14$ is the note's.

## 5. Shadow chains and corollaries (C3)

**Theorem 5.1 (chain structure).** Assume (41) at $\varepsilon$, i.e.
$\|F_\varepsilon\|_\varepsilon<\infty$. Let $\rho$ be a nontrivial zero with
$\beta:=\operatorname{Re}\rho\ge\tfrac12+\delta$ and put
$j^*:=\lfloor(\beta-\tfrac12-\delta)/\varepsilon\rfloor+1\ge1$. Then every
point $\rho_j:=\rho-j\varepsilon$, $0\le j\le j^*$, is a nontrivial zero of
$\zeta$, with

$$\operatorname{ord}_{\rho_0}\zeta\le\operatorname{ord}_{\rho_1}\zeta\le\cdots\le\operatorname{ord}_{\rho_{j^*}}\zeta,$$

all with the same ordinate $\operatorname{Im}\rho$, and the chain ends in the
strip: $\tfrac12-\delta\le\operatorname{Re}\rho_{j^*}<\tfrac12+\delta$.

*Proof.* Induction on $j$: for $j<j^*$, $\operatorname{Re}\rho_j=\beta-j\varepsilon\ge\tfrac12+\delta$
by the definition of $j^*$, so Theorem 4.1(iv) applied to $w=\rho_j$ gives
that $\rho_{j+1}$ is a zero with $\operatorname{ord}_{\rho_{j+1}}\ge\operatorname{ord}_{\rho_j}$.
By definition of $j^*$, $\operatorname{Re}\rho_{j^*}<\tfrac12+\delta$, and
$\operatorname{Re}\rho_{j^*}=\operatorname{Re}\rho_{j^*-1}-\varepsilon\ge\tfrac12+\delta-\varepsilon=\tfrac12-\delta$.
$\square$ (G6a-b check the chain arithmetic on a rational grid of $\beta$ for
four values of $\varepsilon$.)

**Definition.** $\mathrm{H}_\varepsilon$: no two zeros of $\zeta$ differ by
exactly the real number $\varepsilon$, i.e. $\zeta(w)=0\Rightarrow\zeta(w-\varepsilon)\ne0$.

**Corollary 5.2.** Assume (41) at $\varepsilon$. Then
$\mathrm{H}_\varepsilon$ holds if and only if $\zeta(w)\ne0$ for
$\operatorname{Re}w\ge\tfrac12+\delta$. The direction ($\Leftarrow$) does not
use (41) and is unconditional. In particular, (41) at $\varepsilon$
together with $\mathrm{H}_\varepsilon$ gives the zero-free closed half-plane
$\operatorname{Re}w\ge\tfrac12+\tfrac\varepsilon2$.

*Proof.* ($\Rightarrow$, uses (41)) A zero $w$ with
$\operatorname{Re}w\ge\tfrac12+\delta$ (necessarily nontrivial, since
$\operatorname{Re}w>0$) has the shadow $w-\varepsilon$ by Theorem 4.1(iv),
contradicting $\mathrm{H}_\varepsilon$. ($\Leftarrow$, unconditional) Suppose
there is no zero with $\operatorname{Re}w\ge\tfrac12+\delta$, and let
$\zeta(w)=0$. If $w$ is a trivial zero, $w=-2k$ with $k\ge1$, then
$w-\varepsilon=-2k-\varepsilon$ is real and negative but not an even integer
(as $0<\varepsilon<1$), so it is neither a trivial zero nor (having
$\operatorname{Re}<0$) a nontrivial one: $\zeta(w-\varepsilon)\ne0$. If $w$ is
nontrivial, then by the symmetry $\rho\mapsto1-\bar\rho$ of the nontrivial
zero set (functional equation and reality) there is no nontrivial zero with
$\operatorname{Re}\le\tfrac12-\delta$ either, so all nontrivial zeros lie in
the open strip $|\operatorname{Re}\,\cdot-\tfrac12|<\delta$, where two
points differ by a real number of absolute value $<2\delta=\varepsilon$; and
$w-\varepsilon$, having $\operatorname{Im}(w-\varepsilon)=\operatorname{Im}w\ne0$,
is not a trivial zero. Hence $\zeta(w-\varepsilon)\ne0$ in every case.
$\square$

**Remark 5.3 (what is and is not proved).** (a) The hypothesis "no two
nontrivial zeros share an ordinate" is not weaker than RH: if
$\operatorname{Re}\rho\ne\tfrac12$ then $1-\bar\rho$ is a zero with the same
ordinate and a different real part (G6c), so that hypothesis is RH itself and
the corollary under it is circular. It is stated here only to be discarded.
(b) RH implies $\mathrm{H}_\varepsilon$ (under RH all differences of
nontrivial zeros are purely imaginary, and trivial zeros are handled as in
the proof of Corollary 5.2). $\mathrm{H}_\varepsilon$ is not known to imply
RH: as a constraint on abstract zero configurations it admits configurations
violating RH (it excludes, among mirror pairs $\rho,1-\bar\rho$, only those
with $\operatorname{Re}\rho=\tfrac12+\delta$ exactly, G6c). Whether
$\mathrm{H}_\varepsilon$ implies RH for the actual zeros of $\zeta$ is not a
question this note can decide (if RH is true, every statement implies it),
so no stronger claim than "not known to imply" is made. (c) Without any such
hypothesis, (41) at $\varepsilon$ implies the chain structure of Theorem 5.1,
which is consistent with the functional equation (the mirror of a chain is a
chain) and with the isolation of zeros (each chain is finite). It is a
constraint that no known result implies and that is expected to be vacuous;
under RH the premise $\operatorname{Re}\rho\ge\tfrac12+\delta$ never occurs.
So (41) at one fixed $\varepsilon$ does not, by itself, prove the zero-free
half-plane; it proves "zero-free half-plane or shadow chains". The shadow
caveat is removed either by $\mathrm{H}_\varepsilon$ (Corollary 5.2) or by
the ladder (Corollary 7.2).

## 6. Converse: a zero-free half-plane with margin implies (41) (C4)

### 6.1 Imports, with the exact statements used

- **(I1) Convexity bound.** For $0\le\sigma\le1$ and $|t|\ge2$,
  $|\zeta(\sigma+it)|\le C\,|t|^{(1-\sigma)/2}\log|t|$; for $\sigma\ge1$,
  $|t|\ge2$, $|\zeta(\sigma+it)|\le C\log|t|$. (Titchmarsh, *The Theory of
  the Riemann Zeta-Function*, Chapter V, section 5.1; Phragmen-Lindelöf
  between the lines $\sigma=0$ and $\sigma=1$.)
- **(I2) Borel-Caratheodory.** If $f$ is holomorphic on $|z-z_0|\le R$ and
  $0<r<R$, then $\max_{|z-z_0|\le r}|f(z)|\le\frac{2r}{R-r}\max_{|z-z_0|=R}\operatorname{Re}f(z)+\frac{R+r}{R-r}|f(z_0)|$.
  (Titchmarsh, *The Theory of Functions*, section 5.5.)
- **(I3) Hadamard three circles.** If $f$ is holomorphic on
  $r_1\le|z-z_0|\le r_2$ and $M(r):=\max_{|z-z_0|=r}|f|$, then for
  $r_1<r<r_2$, $M(r)\le M(r_1)^{1-a}M(r_2)^{a}$ with
  $a=\log(r/r_1)/\log(r_2/r_1)$. (Titchmarsh, *The Theory of Functions*,
  section 5.3.)
- **(I4) Paley-Wiener, half-plane version.** If $G$ is holomorphic on
  $\operatorname{Re}z>0$ and $\sup_{x>0}\frac1{2\pi}\int|G(x+iy)|^2dy=C<\infty$,
  then there is $\psi\in L^2(0,\infty)$ with $G(z)=\int_0^\infty\psi(u)e^{-zu}du$
  for $\operatorname{Re}z>0$ and $\int_0^\infty|\psi|^2=C$. (Rudin, *Real and
  Complex Analysis*, Theorem 19.2.)
- **(I5) Plancherel** and **(I6) uniqueness for the Fourier transform on
  $L^1(\mathbb R)$** (if $k\in L^1$ and $\hat k\equiv0$ then $k=0$ a.e.).
  (Rudin, *Real and Complex Analysis*, Chapter 9.)
- **(I7) Template.** The argument of Lemma 6.2 is the argument of Titchmarsh,
  Chapter XIV, Theorem 14.2 (under RH: $\log\zeta(s)=O((\log t)^{2-2\sigma+\epsilon})$
  uniformly for $\sigma\ge\tfrac12+\delta$), with the zero-free half-plane
  $\operatorname{Re}w>\theta$ in place of RH; it is written out here so that
  the exponent and the geometry are explicit (G7b).

### 6.2 Growth of $\log\zeta$ in a zero-free half-plane with margin

**Lemma 6.2.** Let $\tfrac12\le\theta<1$ and suppose $\zeta(w)\ne0$ for
$\operatorname{Re}w>\theta$. Let $\theta<\sigma_1\le1$. Then there are
$a=a(\theta,\sigma_1)\in(0,1)$ and $C_3$ such that, for the branch of
$\log\zeta$ on $\{\operatorname{Re}w>\theta,\ \operatorname{Im}w\ne0\}$ that
agrees with $\sum_p\sum_{k\ge1}p^{-kw}/k$ on $\operatorname{Re}w>1$,

$$|\log\zeta(w)|\le C_3(\log|\operatorname{Im}w|)^{a}\qquad\text{for all }\operatorname{Re}w\ge\sigma_1,\ |\operatorname{Im}w|\ge3 .$$

Consequently $|1/\zeta(w)|\le\exp(C_3(\log|\operatorname{Im}w|)^a)=|\operatorname{Im}w|^{o(1)}$ there.

*Proof.* The region $\{\operatorname{Re}w>\theta,\operatorname{Im}w>0\}$ is
simply connected, and $\zeta$ is holomorphic and zero-free on it (the pole
$w=1$ is real), so the branch exists; the case $\operatorname{Im}w<0$ follows
by conjugation. Fix $t\ge3$ and set

$$\eta_1:=\tfrac12(\sigma_1-\theta),\quad w_0:=1+\eta_1+it,\quad R:=1-\theta,\quad r:=1+\eta_1-\sigma_1,\quad r_1:=\tfrac12\eta_1,\quad r_2:=\tfrac12(r+R).$$

Then $0<r_1<r<r_2<R\le\tfrac12$ (G7b checks these inequalities exactly for
six pairs $(\theta,\sigma_1)$). The closed disc $|w-w_0|\le R$ lies in
$\operatorname{Re}w\ge\theta+\eta_1>\theta$ and in $\operatorname{Im}w\ge t-R\ge\tfrac52$,
so $f:=\log\zeta$ is holomorphic on it. On that disc, by (I1) and
$\operatorname{Re}w>\tfrac12$, $|\zeta(w)|\le C(2t)^{1/4}\log(2t)$, hence
$\operatorname{Re}f=\log|\zeta|\le\log t$ for $t\ge t_0$. Also
$|f(w_0)|\le\sum_p\sum_kp^{-k(1+\eta_1)}/k=\log\zeta(1+\eta_1)$. By (I2) with
radii $r_2<R$,

$$M(r_2)\le\frac{2r_2}{R-r_2}\log t+\frac{R+r_2}{R-r_2}\log\zeta(1+\eta_1)\le C_1\log t\qquad(t\ge t_0).$$

On $|w-w_0|=r_1$ one has $\operatorname{Re}w\ge1+\tfrac12\eta_1>1$, so
$M(r_1)\le\log\zeta(1+\tfrac12\eta_1)=:C_2$. By (I3), for every
$r'\in(r_1,r]$, $M(r')\le C_2^{1-a'}(C_1\log t)^{a'}$ with
$a'=\log(r'/r_1)/\log(r_2/r_1)\le a:=\log(r/r_1)/\log(r_2/r_1)<1$. A point
$\sigma+it$ with $\sigma_1\le\sigma\le1+\eta_1-r_1$ lies on the circle of
radius $r'=1+\eta_1-\sigma\in[r_1,r]$; a point with $\sigma>1+\eta_1-r_1$
has $\operatorname{Re}w>1$ and $|f|\le C_2$ directly. Since $a'\le a<1$ and
$C_1\log t\ge1$ for $t\ge t_0$ (enlarging $t_0$ if necessary),
$C_2^{1-a'}(C_1\log t)^{a'}\le\max(1,C_2)\,C_1^{a}(\log t)^a$. Hence
$|\log\zeta(\sigma+it)|\le\max(1,C_2)\,C_1^a\,(\log t)^a$ for all
$\sigma\ge\sigma_1$, $t\ge t_0$. For $3\le t\le t_0$ the bound holds with a larger constant by
continuity of $f$ on the compact set $\sigma_1\le\sigma\le2$, $3\le t\le t_0$
and by $|f|\le\log\zeta(2)$ for $\sigma\ge2$. Finally
$C_3(\log t)^a\le\kappa\log t$ for every $\kappa>0$ once $t$ is large, since
$a<1$. $\square$

### 6.3 The theorem

**Theorem 6.3 (sufficiency).** Suppose there is $\eta>0$ such that
$\zeta(w)\ne0$ for all $w$ with $\operatorname{Re}w\ge\tfrac12+\delta-\eta$.
Then $\|F_\varepsilon\|_\varepsilon<\infty$, i.e. (41) holds at $\varepsilon$.

*Proof.* Shrinking $\eta$ preserves the hypothesis, so assume
$0<\eta\le\delta$ and put $\theta:=\tfrac12+\delta-\eta\in[\tfrac12,1)$,
$\sigma_0:=\tfrac12-\delta-\eta\ge\tfrac12-2\delta\ge\tfrac14>0$, and
$G(s):=c_\varepsilon/(s-1)-Q_\varepsilon(s)$.

*Step 1: $G$ is holomorphic on $\operatorname{Re}s>\sigma_0$.* The poles of
$Q_\varepsilon$ are at $s=0$ (excluded: $0<\sigma_0$), at $s=1$ (cancelled,
Lemma 3.3(a)), and at $s=w-\varepsilon$ for zeros $w$ of $\zeta$; such an $s$
has $\operatorname{Re}s>\sigma_0$ only if $\operatorname{Re}w>\sigma_0+\varepsilon=\theta$,
which the hypothesis excludes (for trivial zeros $\operatorname{Re}w<0$).

*Step 2: uniform $L^2$ bounds on vertical lines.* Let $\tfrac12-\delta\le\sigma\le\tfrac32$
and $|t|\ge3$. By (I1) (with $(1-\sigma)/2\le(\tfrac12+\delta)/2$ for
$\sigma\ge\tfrac12-\delta$, and $\log|t|$ for $\sigma\ge1$) and by Lemma 6.2
applied with $\sigma_1:=\tfrac12+\delta>\theta$ to $w=s+\varepsilon$
(so $\operatorname{Re}w=\sigma+\varepsilon\ge\tfrac12+\delta=\sigma_1$),

$$|Q_\varepsilon(\sigma+it)|=\frac{|\zeta(\sigma+it)|}{|\sigma+it|\,|\zeta(\sigma+\varepsilon+it)|}\le C|t|^{\frac14+\frac\delta2-1}\log|t|\;\exp\bigl(C_3(\log|t|)^a\bigr)\le C'|t|^{-\frac34+\frac\delta2+\kappa}$$

for any fixed $\kappa>0$, where the factors $\log|t|$ and
$\exp(C_3(\log|t|)^a)$, both $|t|^{o(1)}$ because $a<1$, have been absorbed
into $|t|^{\kappa}$ for $|t|\ge t_1(\kappa)$, and the range $3\le|t|\le t_1$
into the constant $C'$. Choose $\kappa:=\tfrac14(\tfrac12-\delta)$; then
$2(-\tfrac34+\tfrac\delta2+\kappa)=-1-\tfrac12(\tfrac12-\delta)<-1$ (G7a checks
$-\tfrac32+\delta<-1$ for all $\delta<\tfrac12$), so
$\int_{|t|\ge3}|Q_\varepsilon(\sigma+it)|^2dt\le C_4$ uniformly in
$\sigma\in[\tfrac12-\delta,\tfrac32]$; and $\int_{|t|\ge3}|c_\varepsilon/(\sigma+it-1)|^2dt\le c_\varepsilon^2\int_{|t|\ge3}t^{-2}dt$.
On the compact rectangle $\tfrac12-\delta\le\sigma\le\tfrac32$, $|t|\le3$, which
lies inside $\operatorname{Re}s>\sigma_0$, $G$ is continuous (Step 1), hence
bounded by some $C_5$. Therefore

$$\int_{\mathbb R}|G(\sigma+it)|^2dt\le 2C_4+\tfrac43c_\varepsilon^2+6C_5^2=:C_6\qquad\text{for all }\sigma\in[\tfrac12-\delta,\tfrac32],$$

using $|G|^2\le2|c_\varepsilon/(s-1)|^2+2|Q_\varepsilon|^2$ on $|t|\ge3$.

For $\sigma\ge\tfrac32$, $G=M_\varepsilon$ by Lemma 3.2, and
$M_\varepsilon(\sigma+it)=\hat\varphi_\sigma(t)$ as in the proof of Theorem
4.1(ii), where now $\varphi_\sigma(u)=F_\varepsilon(e^u)e^{-\sigma u}\mathbf 1_{u>0}$
is in $L^1\cap L^2$ by (B.1) since $\sigma>1$; by (I5),

$$\int_{\mathbb R}|M_\varepsilon(\sigma+it)|^2dt=2\pi\int_1^\infty|F_\varepsilon(x)|^2x^{-2\sigma-1}dx\le2\pi\int_1^\infty4x^{-2}dx=8\pi .$$

Hence $\sup_{\sigma>\frac12-\delta}\int|G(\sigma+it)|^2dt\le\max(C_6,8\pi)<\infty$.

*Step 3: Paley-Wiener and uniqueness.* By Step 1 and Step 2, $z\mapsto G(\tfrac12-\delta+z)$
is holomorphic on $\operatorname{Re}z>0$ with the uniform $L^2$ bound, so by
(I4) there is $\psi\in L^2(0,\infty)$ with $G(\tfrac12-\delta+z)=\int_0^\infty\psi(u)e^{-zu}du$
for $\operatorname{Re}z>0$. For $\operatorname{Re}z>\tfrac12+\delta$ (that is,
$\operatorname{Re}s>1$) Lemma 3.2 gives $G(\tfrac12-\delta+z)=M_\varepsilon(s)=\int_0^\infty\varphi(u)e^{-zu}du$
with $\varphi$ from (B.3), absolutely convergent by (B.1). Fix $x_0:=1+\delta$
and set $k(u):=(\varphi-\psi)(u)e^{-x_0u}\mathbf 1_{u>0}$; then $k\in L^1(\mathbb R)$
(the $\varphi$ part by (B.1), the $\psi$ part by Cauchy-Schwarz) and
$\hat k(y)=\int_0^\infty(\varphi-\psi)(u)e^{-(x_0+iy)u}du=0$ for every
$y\in\mathbb R$. By (I6), $k=0$ a.e., so $\varphi=\psi$ a.e., so
$\varphi\in L^2(0,\infty)$ and $\|F_\varepsilon\|_\varepsilon=\|\varphi\|_2<\infty$.
$\square$

**Remark 6.4 (why the margin).** Step 2 needs $1/\zeta$ controlled on the
closed line $\operatorname{Re}w=\tfrac12+\delta$ and $G$ continuous on a
neighbourhood of the boundary line $\operatorname{Re}s=\tfrac12-\delta$. A
zero-free open half-plane $\operatorname{Re}w>\tfrac12+\delta$ with zeros
accumulating towards its boundary would not give either. So the exact
converse of Theorem 4.1 is not claimed; the equivalence in Section 7 carries
"an $\eta$ of margin".

## 7. Two-sided reading and the ladder (C5)

**Corollary 7.1 (two-sided reading at fixed $\varepsilon$).** Let
$\mathrm{ZF}(\theta)$ denote "$\zeta(w)\ne0$ for $\operatorname{Re}w\ge\theta$"
(the quasi-Riemann hypothesis with abscissa $\theta$). Then

$$\mathrm{ZF}\bigl(\tfrac12+\tfrac\varepsilon2-\eta\bigr)\text{ for some }\eta>0\ \Longrightarrow\ (41)\text{ at }\varepsilon\ \Longrightarrow\ \mathrm{ZF}\bigl(\tfrac12+\tfrac\varepsilon2\bigr)\ \text{or shadow chains (Theorem 5.1)},$$

and, under $\mathrm{H}_\varepsilon$, the right-hand alternative is
$\mathrm{ZF}(\tfrac12+\tfrac\varepsilon2)$. The mathematical content of this
corollary is exactly the displayed implications together with the
$\mathrm{H}_\varepsilon$ variant. The sentence "(41) at $\varepsilon$ is
equivalent, modulo the shadow caveat and an $\eta$ of margin, to the
zero-free half-plane $\operatorname{Re}s>\tfrac12+\tfrac\varepsilon2$" is an
informal gloss on them and not a separate mathematical statement; the exact
converse without margin is not claimed (Remark 6.4).

*Proof.* Theorems 6.3, 4.1(iv), 5.1 and Corollary 5.2. $\square$

**Corollary 7.2 (the ladder removes the shadow caveat).** Let
$E\subset(0,\tfrac14]$ be a set of values of $\varepsilon$ at each of which
(41) holds, and let $\varepsilon_*\in[0,\tfrac14]$ be an accumulation point
of $E$. Then $\zeta(w)\ne0$ for $\operatorname{Re}w>\tfrac12+\tfrac{\varepsilon_*}2$,
with no shadow caveat. In particular: (41) along any sequence
$\varepsilon_j\to0$ implies RH; and conversely RH implies (41) at every
$\varepsilon\in(0,\tfrac14]$. Hence

$$\mathrm{RH}\iff(41)\text{ holds for every }\varepsilon\in(0,\tfrac14]\iff(41)\text{ holds on a set of }\varepsilon\text{ accumulating at }0 .$$

*Proof.* Suppose $\zeta(\rho)=0$ with $\beta:=\operatorname{Re}\rho>\tfrac12+\tfrac{\varepsilon_*}2$,
i.e. $2\beta-1>\varepsilon_*$. Infinitely many $\varepsilon\in E$ lie in
$(0,2\beta-1]$, and for each of them $\tfrac12+\tfrac\varepsilon2\le\beta$, so
Theorem 4.1(iv) gives a zero at $\rho-\varepsilon$. These are infinitely many
distinct zeros on the bounded segment $\{\sigma+i\operatorname{Im}\rho:1-\beta\le\sigma\le\beta\}$
(G6d models the finite version), contradicting the isolation of the zeros of
the meromorphic function $\zeta$. For the converse, RH gives
$\zeta(w)\ne0$ for $\operatorname{Re}w>\tfrac12$, hence for
$\operatorname{Re}w\ge\tfrac12+\delta-\eta$ with $\eta:=\tfrac12\delta$, and
Theorem 6.3 applies at every $\varepsilon$. $\square$

So the family of targets (41), indexed by $\varepsilon$, is RH-equivalent as
a family, while each single member is a quasi-RH rung, modulo shadows.
Duplicate-of-record attribution: the implication "RH implies finiteness of
the $\varepsilon$-damped norm" is already stated in the note's own section 9
for the discrete form (26) ("Under RH, the symmetrically shifted Mellin
calculation gives a joined norm of order $\varepsilon$"), retained there as
conditional structural evidence without proof. Theorem 6.3 supplies a proof
of the qualitative finiteness for the continuous norm
$\|F_\varepsilon\|_\varepsilon$ (and hence of (41) via Proposition 3.6) under
the weaker hypothesis of a zero-free half-plane with margin; it does not
supply the note's "order $\varepsilon$" quantitative statement.

## 8. Consequences and placement (C7)

### 8.1 Numerical readings

- $\varepsilon=\tfrac14$: (41) implies, modulo shadows, no zero with
  $\operatorname{Re}\rho\ge\tfrac58$ (a fortiori none with
  $\operatorname{Re}\rho>\tfrac58$).
- $\varepsilon=\tfrac1{16}$: no zero with $\operatorname{Re}\rho\ge\tfrac{17}{32}$.
- General $\varepsilon\in(0,1)$: no zero with $\operatorname{Re}\rho\ge\tfrac12+\tfrac\varepsilon2$,
  a half-plane strictly inside the critical strip.

### 8.2 What is known

No zero-free half-plane $\operatorname{Re}s>\theta$ with $\theta<1$ is known.
The widest known zero-free region is of Vinogradov-Korobov type,
$\sigma\ge1-c/\bigl((\log t)^{2/3}(\log\log t)^{1/3}\bigr)$, which shrinks to
the line $\operatorname{Re}s=1$ as $|t|\to\infty$ (Titchmarsh, Chapter VI and
the end-of-chapter notes of the second edition; Ivic, *The Riemann
Zeta-Function*, Chapter 6). Zero-density estimates bound the number of zeros
to the right of a line but exclude none. Therefore a direct unconditional
proof of (41) at any fixed $\varepsilon<1$ would be the first zero-free
half-plane strictly inside the strip (modulo the shadow structure, which no
known result excludes either). The classical companion statement is the
equivalence between $\mathrm{ZF}(\theta)$ and $M(x)=O(x^{\theta+o(1)})$ for
the Mertens function (Titchmarsh, Chapter XIV); the present target is of the
same type with the $\varepsilon$-damped Moebius weights and a two-sided
$L^2$ reading.

### 8.3 Relation to the note's own guards and no-go ledger

- **Section 8 of the note, (23)-(24).** The note already guards its original
  sharp family by the same mechanism: $L^2$ membership forces the Mellin
  quotient $\mathscr A_Q(s)/((s-1)\zeta(s))$ into a half-plane, and since the
  numerator $\mathscr A_Q$ is nonvanishing at $s$ by (24) whenever
  $Q\ge4|s+1|$ (which is why the note's guard needs an unbounded set of
  dyadic $Q$ and is itself only candidate-T), every zero of $\zeta$ in
  $\operatorname{Re}s>\tfrac12$ produces an uncancelled pole for large $Q$:
  hence RH and simple zeros. In the $\varepsilon$-family the numerator is
  $\zeta(s)$ itself, which can cancel poles of $1/\zeta(s+\varepsilon)$; that
  is exactly the shadow caveat, and the weight $x^{\varepsilon-2}$ moves the
  line to $\tfrac12-\delta$, which is why the conclusion is a half-plane of
  abscissa $\tfrac12+\delta$ rather than RH. The present note is the
  $\varepsilon$-family instance of the note's own guard method.
- **No-go item 7.** The note warns that the all-large-$J$ closure is
  stronger than a bare RH statement. The fixed-$\varepsilon$ target is
  implied by RH (Corollary 7.2) and is not known to imply RH (at a single
  $\varepsilon$ it yields only a half-plane modulo shadows, Corollary 7.1),
  but it is still a quasi-RH rung; the ledger should read it that way. A suggested wording for a new ledger line, offered and
  not folded: "8. Fixed-$\varepsilon$ finiteness (41) is, modulo
  $\varepsilon$-shadow chains and an $\eta$ of margin, the zero-free
  half-plane $\operatorname{Re}s\ge\tfrac12+\tfrac\varepsilon2$. Do not treat
  it as a soft regularized estimate; no proof route insensitive to the zeros
  of $\zeta$ in that half-plane can reach it."
- **No-go items 4 and 6 (envelopes).** The guard explains them: any argument
  that uses the arithmetic input only through majorants shared by inputs
  whose Mellin quotient has a pole in $\operatorname{Re}s\ge\tfrac12-\delta$
  cannot prove (41). This is a reading, not a new F-route beyond the note's
  ledger.
- **Section 5 of ZETA-RH-STATUS-2026-09-08.md.** "Any proposal that reduces
  RH to a finite check at a fixed level is already refuted by the wall." The
  quantities $L_N(\varepsilon)$ are finite checks at level $N$; the target
  (41) is the global object $\sup_N$. The DIAGNOSTIC of Section 9 illustrates
  it: partial sums to $N=64$ carry no information about the limit, and under
  RH (Corollary 7.2) they converge, but nothing at finite $N$ shows it.
- **Section 4 of the status page and RH-ONE-WALL-CROSSREF_2026-08-17.md.**
  The wall's common form is that a finite prefix of any positivity hierarchy
  is passed by some off-critical configuration; what survives is a global
  object. Here the global object is the $H^2$ membership of the Mellin
  transform, which encodes control of $1/\zeta(s+\varepsilon)$ on a closed
  half-plane. The record already contains this reading in the unshifted
  case: REVIEW-CZ.md, section 3.7 (the $H$-norm as an $L^2(0,1)$ norm and the
  Mellin-Plancherel isometry into $H^2(\operatorname{Re}s>\tfrac12)$) and
  section 4 ("natural candidates converge exactly when $1/\zeta$ is
  controlled in $\operatorname{Re}s>\tfrac12$"); also
  O-WEIL-REALIZATION_RECON_2026-07-15.md, route 3 (Nyman-Beurling /
  Baez-Duarte) and NOTE-RH-DECODER-CLASSIFICATION_2026-08-12.md, section 2
  ("a criterion restates the target"). This note adds the
  $\varepsilon$-shifted quotient $\zeta(s)/\zeta(s+\varepsilon)$ and the
  shadow phenomenon; it is a new reading of the one wall in
  Nyman-Beurling/Mellin-quotient clothing and is counted as such, not as a
  new theorem.
- **Duplicate-of-record attributions (added on referee review).** The
  following parts of this note are readings or proofs of material already in
  the record and are not new theorems:
  (i) the mechanism of Theorem 4.1 (weighted $L^2$ membership forces the
  Mellin quotient into $H^2$ of a half-plane, so zeros of the denominator
  produce uncancelled poles) is the note's own section-8 guard, (23)-(24);
  (ii) the $H^2(\operatorname{Re}s>\tfrac12)$ reading and "natural candidates
  converge exactly when $1/\zeta$ is controlled in $\operatorname{Re}s>\tfrac12$"
  are REVIEW-CZ.md sections 3.7 and 4;
  (iii) the distinction between formal Mellin boundary values and actual
  $L^2$ membership, on which Theorem 4.1(ii)-(iii) turns, is the content the
  note cites from its external input 3, J.-F. Burnol, arXiv:math/0202166
  (C-RH-MOBIUS-MEAN-CHANNEL-N.md section 15), which is prior record for the
  C2 mechanism;
  (iv) "RH implies finiteness of the $\varepsilon$-damped norm" is stated in
  the note's section 9 for the discrete form (26) (see the end of Section 7
  above);
  (v) the Parseval identity (36) and the Jacobi/Hankel form (39) are stated
  in the note's sections 11-12; Section 3 above supplies the missing proof
  and the identification of $g_\varepsilon$, which is new text, not a new
  theorem;
  (vi) the family equivalence of Corollary 7.2 is a Baez-Duarte-type
  equivalence in Mellin-quotient clothing (O-WEIL-REALIZATION_RECON_2026-07-15.md
  route 3; REVIEW-CZ.md section 4).
  What is not already in the record read here: the $\varepsilon$-shifted
  quotient $\zeta(s)/(s\zeta(s+\varepsilon))$ on the line
  $\operatorname{Re}s=\tfrac12-\delta$, the shadow-chain bookkeeping
  (Theorem 5.1, Corollary 5.2), and the written proof of Theorem 6.3.
- **The discrete norm (26).** The note's $\|a_1-q_\varepsilon\|_H^2$ uses the
  unshifted weight $1/(n(n+1))\asymp n^{-2}$. Running the same guard with the
  weight $x^{-2}$ puts the Mellin line at $\operatorname{Re}s=\tfrac12$ and
  yields shadows only for zeros with $\operatorname{Re}\rho\ge\tfrac12+\varepsilon$,
  a weaker reading (abscissa $\tfrac12+\varepsilon$ instead of
  $\tfrac12+\tfrac\varepsilon2$); the finite certificate condition (29),
  which concerns a finite rational $q\in E$ and not $q_\varepsilon$, is not
  touched by anything here.

### 8.4 What the note's program becomes

A zero-free half-plane ladder. Each rung "(41) at $\varepsilon$" is a
quasi-RH statement with abscissa $\tfrac12+\tfrac\varepsilon2$ (modulo
shadows); no rung is known; the ladder as a whole, or any sequence of rungs
$\varepsilon_j\to0$, is RH (Corollary 7.2), and RH gives every rung
(Theorem 6.3). The note's handoff instruction "continue from (41)" therefore
means: prove a zero-free half-plane by the joined Jacobi/Hankel form, or
find a breaker showing $\|F_\varepsilon\|_\varepsilon=\infty$ at the selected
$\varepsilon$; the latter would be, by Theorem 6.3, a proof that no zero-free
half-plane $\operatorname{Re}w\ge\tfrac12+\tfrac\varepsilon2-\eta$ exists,
i.e. a disproof of RH, and by the program declaration of 2026-09-08 a program
falsifier, so it must meet the falsifier standard of
RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md (exact enclosure or machine-checked
proof in an independent public record) before anything is folded.

## 9. DIAGNOSTIC (C6): the $L_N$ table to $N=64$

DIAGNOSTIC block, asserts nothing. The enclosures are computed with a port
of the note's rigorous interval machinery (the interval block of
C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py carried into verify_epsilon_guard.py
with the same interval class, root enclosure and Euler-Maclaurin routine:
outward 256-bit rational grid, 288-bit integer root enclosures, 128 direct
terms and 24 Bernoulli terms). It is not an independent re-implementation;
check G8a is a port self-consistency gate confirming that the port
reproduces all ten coarse enclosures printed in
C-RH-MOBIUS-MEAN-CHANNEL-N_EXPECTED.txt exactly (non-vacuous: shifting one
published bound by $10^{-12}$ makes it fail). Values are enclosure
midpoints; every printed width is below $10^{-27}$.

| $\varepsilon$ | $N$ | $L_N$ | increment over previous row |
|---|---|---|---|
| 1/4 | 0 | 0.442144934508 | |
| 1/4 | 4 | 0.574428336006 | +0.132283401498 |
| 1/4 | 8 | 0.593159495461 | +0.018731159455 |
| 1/4 | 16 | 0.602913453310 | +0.009753957849 |
| 1/4 | 24 | 0.606912182200 | +0.003998728890 |
| 1/4 | 32 | 0.608193475645 | +0.001281293445 |
| 1/4 | 40 | 0.609777102899 | +0.001583627254 |
| 1/4 | 48 | 0.610282749329 | +0.000505646430 |
| 1/4 | 56 | 0.610685032988 | +0.000402283659 |
| 1/4 | 64 | 0.611344330745 | +0.000659297757 |
| 1/16 | 0 | 0.649629624473 | |
| 1/16 | 4 | 0.846886792420 | +0.197257167947 |
| 1/16 | 8 | 0.865126082364 | +0.018239289944 |
| 1/16 | 16 | 0.872724018346 | +0.007597935983 |
| 1/16 | 24 | 0.874770076449 | +0.002046058102 |
| 1/16 | 32 | 0.875502085955 | +0.000732009506 |
| 1/16 | 40 | 0.875960134095 | +0.000458048140 |
| 1/16 | 48 | 0.876144112206 | +0.000183978110 |
| 1/16 | 56 | 0.876274211104 | +0.000130098899 |
| 1/16 | 64 | 0.876431563562 | +0.000157352458 |

One-step terms $(2n+3)|a_n|^2$ for $n=57,\dots,64$: at $\varepsilon=\tfrac14$
they are $1.8\cdot10^{-8}$, $8.1\cdot10^{-5}$, $1.4\cdot10^{-4}$,
$8.2\cdot10^{-5}$, $6.0\cdot10^{-5}$, $8.7\cdot10^{-5}$, $1.1\cdot10^{-4}$,
$9.9\cdot10^{-5}$; at $\varepsilon=\tfrac1{16}$ they are $4.1\cdot10^{-6}$,
$1.9\cdot10^{-5}$, $2.7\cdot10^{-5}$, $2.2\cdot10^{-5}$, $2.0\cdot10^{-5}$,
$2.2\cdot10^{-5}$, $2.3\cdot10^{-5}$, $1.9\cdot10^{-5}$.

Reading. The increments are not monotone (the $32\to40$ step exceeds the
$24\to32$ step at $\varepsilon=\tfrac14$) and show no visible decay between
$n=57$ and $n=64$. Finiteness of $\lim_NL_N$ is exactly the target (41), and
by Section 7 it is a zero-free half-plane statement; finite partial sums
decide nothing in either direction (ZETA-RH-STATUS-2026-09-08.md, section 5).
HEURISTIC, not asserted: under RH the poles of $Q_\varepsilon$ nearest to the
line $\operatorname{Re}s=\tfrac12-\delta$ lie on $\operatorname{Re}s=\tfrac12-\varepsilon$,
at distance $\delta$, so $g_\varepsilon$ would have endpoint behaviour of type
$t^{\alpha}$, $\alpha=-\tfrac12+\delta+i\gamma$, at $t=0$. For a single such
term the Jacobi coefficient has the closed form (Rodrigues form and $n$-fold
integration by parts, valid for $\operatorname{Re}\alpha>-1$)
$a_n=\prod_{j=1}^n(\alpha-j)\big/\prod_{j=0}^n(\alpha+2+j)$, so by Stirling
$|a_n|\asymp n^{-2-2\operatorname{Re}\alpha}$ and
$(2n+3)|a_n|^2\asymp n^{-3-4\operatorname{Re}\alpha}=n^{-1-4\delta}=n^{-1-2\varepsilon}$;
the tail of the sum is then of order $N^{-2\varepsilon}$, which at
$\varepsilon=\tfrac1{16}$ is $N^{-1/8}$ (and $N^{-1/2}$ at $\varepsilon=\tfrac14$).
The original draft of this note printed $n^{-1-\varepsilon}$ and
$N^{-\varepsilon}$ here; both referees corrected the exponent, and the
correction was confirmed in exact arithmetic (the closed form agrees with
$\sum_kb_{n,k}/(k+2+\alpha)$ for $n\le30$, and
$(2n+3)a_n^2\,n^{1+2\varepsilon}$ stabilises near $2$ for $n\le800$ at
$\varepsilon=\tfrac14$ and $\tfrac1{16}$, while $n^{1+\varepsilon}$-scaling
drifts). If this heuristic is right, the table cannot show convergence at any
feasible $N$ even when (41) is true, which is one more reason the table is a
diagnostic and not evidence.

## 10. Verifier map

verify_epsilon_guard.py, 31 checks, all PASS, stdout in
verify_epsilon_guard.stdout.txt (final line `CHECKS: 31 of 31 PASS`).

| Check | Certifies | Supports |
|---|---|---|
| G1a-d | formal Dirichlet identity $(1*\mu u)(k)=\prod_{p\mid k}(1-u_p)$, $k\le400$; Dirichlet inverse; specialisations $u_p\in\{0,1,\tfrac12\}$ | Lemma 3.1 (finite part) |
| G2a-d | exact step-function Mellin identity on truncated models: integer $s$, rational $s$ with $q$-th-power jumps, formal Abel identity, telescoping of the linear term | Lemma 3.2 (finite part) |
| G3a-e | Laurent bookkeeping: residue $c$ at $s=1$, cancellation of $(s-1)^{-2}$ and $(s-1)^{-1}$, constant term (G3a-c, real computations); G3d-e: given a simple pole of the denominator model at $1-\varepsilon$ (a model input), the truncated-Laurent quotient has a simple zero there and $M(1-\varepsilon)=-c/\varepsilon$; G3d-e cannot fail for any model coefficients and certify nothing about $\zeta$; Lemma 3.3(b) is carried by the $\eta$-function argument in the text | Lemma 3.3 |
| G4a-g | orthonormality of $\sqrt{2n+3}\,tR_n$ ($n,m\le24$); $a_n$ definitions agree; exact Parseval on 36 rational polynomials, no additive constant; vanishing and Bessel; Muentz deficit $1/(N+2)^2$; tail-energy bookkeeping (G4f, a Fraction identity that cannot fail); Rodrigues form ($n\le40$) | Lemma 3.5, Proposition 3.6, Remark 3.6 |
| G5a-d | (35) equals (34) at $s=k+2-\delta$ (G5a, a transcription check: a Fraction identity that cannot fail); exact substitution on monomial models (norm and moments); power-rule bracket | Lemma 3.4 |
| G6a-d | chain length and endpoint strip; mirror-pair arithmetic; distinct shadows on a bounded segment | Theorem 5.1, Remark 5.3, Corollary 7.2 |
| G7a-b | square-integrability exponent $-\tfrac32+\delta<-1$; Cauchy-Schwarz exponent; three-circle geometry, $a<1$ | Theorem 4.1(i), Lemma 6.2, Theorem 6.3 |
| G8a | port self-consistency gate: exact reproduction of the note's ten published $L_N$ enclosures by the port of its interval machinery | Section 9 |

Non-vacuity (from the code referee's mutation harness, recorded here, not
re-run by this note): a polynomial outside $V_N$ fails G4c-d; a perturbed
$R_3$ fails G4a, G4e, G4g; $\mu(6):=0$ fails G1a-d; a $10^{-12}$ shift of one
published bound fails G8a; $\theta>\sigma_1$ fails the G7b predicate.
Bookkeeping identities that cannot fail for any input: G3d, G3e, G4f and the
tuple comparison in G5a. So the substantive exact checks number 27, not 31;
the four are kept for the record and are not counted as evidence.

The verifier does not and cannot verify: holomorphy and $H^2$ membership,
the identity theorem step, the imports (I1)-(I7), the location or
multiplicity of any zero, or the finiteness of $\|F_\varepsilon\|_\varepsilon$.
Those are the content of the proofs above and of the cited theorems.

## 11. Review record

Two adversarial referee reports of 2026-09-15 (mathematics lens; evidence and
code lens) were applied to the first draft. Every accepted correction is
listed; no status label was raised; no claim was added.

Accepted corrections (mathematics and wording):

1. Section 9, HEURISTIC decay exponent: $n^{-1-\varepsilon}$ / $N^{-\varepsilon}$
   corrected to $n^{-1-2\varepsilon}$ / $N^{-2\varepsilon}$, with the closed-form
   Jacobi coefficient and its Stirling asymptotics now written out; confirmed
   in exact arithmetic by the repair owner as well as by both referees.
2. Corollary 5.2, direction ($\Leftarrow$): "all zeros lie in the open strip"
   restricted to nontrivial zeros; the trivial-zero case $w=-2k$ added; the
   statement now records that ($\Leftarrow$) does not use (41).
3. Remark 5.3(b): "does not imply RH" replaced by "is not known to imply RH"
   with the abstract-configuration reading, since the flat statement is
   unprovable as written.
4. Corollary 7.1 and the C5 row: "equivalent modulo the shadow caveat and an
   $\eta$ of margin" is now labelled an informal gloss; the content is the
   three displayed implications.
5. C5 claim text: "Theorem 6.3 with $\theta=\tfrac12$" corrected to
   $\eta=\delta/2$, i.e. $\theta=\tfrac12+\tfrac\delta2$, as in the proof.
6. Lemma 6.2: the three-circle constant is $\max(1,C_2)\,C_1^a$, not
   $\max(C_1,C_2)$; the enlargement of $t_0$ so that $C_1\log t\ge1$ is stated.
7. Theorem 6.3, Step 2: the absorption of $\log|t|$ and
   $\exp(C_3(\log|t|)^a)$ into $|t|^{\kappa}$ is now explicit.
8. Section 8.3: the nonvanishing of $\mathscr A_Q$ by (24) is stated with its
   hypothesis $Q\ge4|s+1|$.
9. Section 8.1: the stray reference to "the task's open form" (an
   orchestrator prompt invisible to the reader) deleted.
10. Duplicate-of-record attributions added in Section 8.3 (six items),
    including Burnol, arXiv:math/0202166, the note's external input 3, as
    prior record for the $L^2$-membership versus formal-Mellin distinction
    used in Theorem 4.1, and the note's section 9 for "RH implies finiteness"
    (end of Section 7).
11. Verdict table: G3a-e removed from the C1 check list (they support Lemma
    3.3, used by C2).

Accepted corrections (verifier and its description):

12. "independent re-implementation" (verifier docstring, G8a label, stdout
    line, Section 9, falsifier C6, verdict row C6) replaced by "port of the
    note's interval machinery; G8a is a port self-consistency gate".
13. G7b label "Lemma A" corrected to "Lemma 6.2".
14. G3d, G3e, G4f and G5a labels now say that they are bookkeeping identities
    that cannot fail for any input; the verifier map counts 27 substantive
    checks out of 31.
15. The four bare `assert` statements replaced by explicit `raise
    AssertionError(...)` guards so that `python3 -O` cannot strip them; a
    violation still aborts with exit 1 (protocol deviation acknowledged).
16. G4f is now printed before G4g.
17. The verifier was re-run twice from a clean shell after the changes; the
    frozen stdout equals the fresh run byte for byte; new pins in Section 12.
    All numerical DIAGNOSTIC lines are unchanged from the first draft.

18. Section 8.3, no-go item 7 bullet: "weaker than RH" replaced by "implied
    by RH and not known to imply RH", for consistency with item 3 (repair
    owner's own consistency fix in the referees' sense).

Referee objections considered and rejected: none. Every objection in both
reports was either accepted as listed above or was a confirmation.

## 12. Pins

```text
verifier   verify_epsilon_guard.py
           SHA-256 1fea7551db665cb603879b433a05d74523a3b48bcdef85a300ece64d8acf7cc6
stdout     verify_epsilon_guard.stdout.txt
           SHA-256 1d293119de0a530de6a6f61e09e920143b26d6fe5cbb418578e550d97be91014
command    env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_epsilon_guard.py
python     3.11.15; exit 0; CHECKS: 31 of 31 PASS; wall about 3.7 s;
           two consecutive clean-shell runs byte-identical
```

## 13. What this does not do

- It does not prove RH, does not give evidence for or against RH, and does
  not move any registry row; RH remains the open program-level obligation
  declared on 2026-09-08.
- It does not prove (41) at any $\varepsilon$, and does not prove
  $\|F_\varepsilon\|_\varepsilon=\infty$ at any $\varepsilon$; both remain
  open (row O of the verdict table). A breaker of the second kind would be a
  disproof of RH and must meet the program's falsifier standard.
- It does not establish any zero-free region, any zero-density statement, or
  any property of the zeros of $\zeta$; Theorem 4.1(iv), Theorem 5.1 and the
  corollaries are conditional on (41).
- It does not remove the shadow caveat at a single fixed $\varepsilon$; that
  needs either $\mathrm{H}_\varepsilon$ (Corollary 5.2) or the ladder
  (Corollary 7.2).
- It does not claim the exact converse of Theorem 4.1 without margin
  (Remark 6.4).
- It does not verify the imports (I1)-(I7) by machine; they are classical
  theorems cited with their statements. The verifier certifies finite
  algebraic pieces only.
- It does not touch the note's finite certificate target (29), its sharp
  family (sections 1-8), or the external Mertens input of its (38).
- It does not upgrade the DIAGNOSTIC of Section 9 to evidence of any kind;
  the HEURISTIC decay remark there (exponent $n^{-1-2\varepsilon}$, corrected
  on review) is labelled as such and asserts nothing.
- Its verifier is not an independent check of the note's interval machinery;
  G8a is a port self-consistency gate.
- It is one more reading of the one wall, counted under
  RH-ONE-WALL-CROSSREF_2026-08-17.md; it is not a second theorem and must not
  be booked as one.
