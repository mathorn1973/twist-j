# RH attack addendum — 2026-09-16

```text
STATUS      NON-CANONICAL review addendum
DATE        2026-09-16
BASIS       PR #1020, head 39dd4a6a4a5bd973e98cc805aad98a00d3921c90 before this addendum
TARGETS     ATTACK-EPSILON-GUARD.md; ATTACK-NB-PROJECTION.md; PR #979 target (29)
AUTHORITY   none; no Canon, Registry, Frontier, gate, evidence or claim-status motion
ARCH        one local x86_64 run; nothing here is filed as C
```

This addendum records two corrections to the 2026-09-15 summary reading and one new exact finite obstruction. It does not replace the four attack lanes and it does not alter their frozen verifier outputs. Where the wording below differs from a summary sentence in `ATTACK-EPSILON-GUARD.md`, this addendum is the intended reading.

## 1. New exact result: target (29) cannot be met in the span through K=72

Let

\[
r_k(n)=n\bmod k,
\qquad
E_{72}=\operatorname{span}\{r_2,\ldots,r_{72}\},
\]

and define the finite part of the H-norm by

\[
E_{144}(q)=\sum_{n=1}^{144}\frac{|1-q(n)|^2}{n(n+1)}.
\]

The standard-library verifier solves the exact weighted least-squares problem over the full 71-dimensional span. Fraction-free Bareiss elimination gives the exact minimum and checks

\[
\boxed{
\frac{7601923}{10^9}
<
\min_{q\in E_{72}}E_{144}(q)
<
\frac{7601924}{10^9}.
}
\]

In particular,

\[
\min_{q\in E_{72}}E_{144}(q)
>
7000\frac9{2^{23}}.
\]

Since the omitted H-norm tail is nonnegative, every finite rational sum used by target (29) with support contained in `2,...,72` satisfies

\[
\delta_q^2=\|1-q\|_H^2>\frac9{2^{23}}.
\]

The computation is over real coefficients, so the conclusion also covers rational coefficients; complex coefficients cannot do better because real and imaginary parts separate and the target is real.

**Narrow verdict.** The support `2,...,72` is ruled out for target (29). This does not rule out a finite certificate using indices above 72, does not invalidate transfer (28), and has no direct consequence for RH.

This is stronger than reporting failure of one numerical approximation: it minimizes over the entire stated finite span.

## 2. Hardy-space correction: the holomorphic object is the pole-subtracted Mellin transform

For fixed `0 < eps <= 1/4`, put

\[
c_\varepsilon=\zeta(1+\varepsilon)^{-1},
\qquad
F_\varepsilon(x)=c_\varepsilon x-H_\varepsilon(\lfloor x\rfloor),
\]

and

\[
\alpha_\varepsilon=\frac12-\frac\varepsilon2.
\]

The correct Hardy-space object is

\[
\boxed{
M_\varepsilon(s)
=
\int_1^\infty F_\varepsilon(x)x^{-s-1}\,dx
=
\frac{c_\varepsilon}{s-1}
-
\frac{\zeta(s)}{s\zeta(s+\varepsilon)}.
}
\]

Thus

\[
\|F_\varepsilon\|_\varepsilon<\infty
\Longrightarrow
M_\varepsilon\in H^2(\Re s>\alpha_\varepsilon).
\]

It is not correct to state that the bare quotient

\[
\zeta(s)/(s\zeta(s+\varepsilon))
\]

itself belongs to that Hardy space: it has the simple pole at `s=1` with residue `c_eps`. The detailed theorem in `ATTACK-EPSILON-GUARD.md` already subtracts this pole correctly; the correction applies to the compressed summary wording.

Away from `s=1`, the pole exclusion still yields the multiplicity condition

\[
\zeta(\rho)=0,
\quad
\Re\rho\ge\frac12+\frac\varepsilon2
\Longrightarrow
\operatorname{ord}_{\rho-\varepsilon}\zeta
\ge
\operatorname{ord}_{\rho}\zeta.
\]

## 3. Fixed epsilon gives a shadow condition, not by itself a zero-free half-plane

For one fixed `eps`, the preceding implication forces shifted shadow zeros. Without a separate argument excluding such exact shifts, it does not by itself prove

\[
\zeta(s)\ne0
\quad
(\Re s>\tfrac12+\tfrac\varepsilon2).
\]

The following exact algebraic model shows why cancellation by a shadow chain is a genuine logical possibility of the quotient mechanism. It is not the Riemann zeta function and is not a counterexample to RH:

\[
P(s)=\prod_{\beta\in\{1/4,1/2,3/4\}}((s-\beta)^2+1),
\qquad
P(1-s)=P(s),
\]

while

\[
\frac{P(s)}{P(s+1/4)}
=
\frac{(s-3/4)^2+1}{s^2+1}.
\]

With

\[
Z(s)=\frac{P(s)}{P(1)(s-1)},
\qquad
c=\frac1{Z(5/4)}=\frac{17}{128},
\]

one obtains exactly

\[
\frac{c}{s-1}-\frac{Z(s)}{sZ(s+1/4)}
=
\frac{-111s^2+177s-150}{128s(s^2+1)}.
\]

The verifier checks these polynomial identities exactly.

Therefore the safe fixed-epsilon reading is:

\[
(41)_\varepsilon
\Longrightarrow
\text{shadow condition at shift }\varepsilon,
\]

not an unconditional zero-free half-plane unless the shadows are independently removed.

## 4. An accumulating family of epsilon values removes the shadows

The existing isolation argument remains valid and should be used as the exact ladder statement. If (41) holds for infinitely many distinct values

\[
\varepsilon_j\to\varepsilon_*,
\]

then there is no zero with

\[
\Re\rho>\frac12+\frac{\varepsilon_*}{2}.
\]

Indeed, such a zero would force the distinct zeros `rho-eps_j` for all sufficiently large `j`, producing a finite accumulation point of zeros of a nonzero meromorphic function.

Consequences:

- an accumulating family with `eps_* = 1/4` gives the genuine zero-free half-plane `Re s > 5/8`;
- an accumulating family with `eps_* = 0`, together with the usual functional-equation symmetry, gives RH;
- no uniform bound in `j` is required for this isolation step: finiteness for each member of the family suffices.

For example, a proof of (41) for every

\[
\varepsilon_j=\frac14-\frac1{8j}
\]

would imply `Re s > 5/8` is zero-free, while still falling short of RH.

## 5. Corrected interpretation of the finite diagnostics

The finite `K` data from lane A should not be described as proving convergence or nonconvergence of an infinite sequence. The supported statement is narrower:

- on the inspected sharp cuts, the errors do not show sustained decrease;
- the inspected Cesaro averages improve substantially over the same finite range;
- this finite observation does not settle the asymptotic question.

The new obstruction above is different: it is an exact universal statement for the complete finite span `r_2,...,r_72` because the full finite least-squares minimum is solved.

## 6. Consequence for PR #979 handoff

For `Q=8`, `U=64`, transfer (29) still reads

\[
\delta_q^2\le\frac9{2^{23}}
\Longrightarrow
\|A_8-\widetilde p_{8,64}[q]\|_B^2\le\frac{17}{16384}.
\]

The arithmetic of the implication is unchanged. The new result says only that its premise cannot be met with support contained in `2,...,72`.

The next finite-certificate attempt should therefore change the support or improve the transfer. For a proposed finite

\[
q=\sum_k c_kr_k,
\]

a complete upper certificate must also bound the infinite tail. The elementary bound

\[
\sum_{n>N}\frac{|1-q(n)|^2}{n(n+1)}
\le
\frac{(1+\sum_k|c_k|(k-1))^2}{N+1}
\]

is crude but exact; periodicity may provide a sharper tail certificate.

## 7. Reproduction

Run from this directory:

```bash
python verify_2026_09_16.py > ACTUAL.txt
cmp ACTUAL.txt EXPECTED.txt
sha256sum -c SHA256SUMS-2026-09-16
```

The verifier uses only the Python standard library: integers, `Fraction`, `lcm`, and fraction-free Bareiss elimination. It performs no network access and needs no external zero table or computer algebra package.

Expected runtime on the review host was about six seconds. Two clean runs were byte-identical before publication.

The checks cover only the new finite obstruction and the finite algebraic shadow model. They do not re-run the four 2026-09-15 lane verifiers and they do not certify external analytic imports.
