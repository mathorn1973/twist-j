# C-RH-JACOBI-GROWTH-LADDER-N

**Title:** Polynomial growth of the joined Jacobi energy and a weaker sufficient RH target
**Author:** A. M. Thorn
**Date:** 2026-09-16
**Status:** NON-CANONICAL; candidate-T analytical implication only.
**Object lock:** [#1030](https://github.com/mathorn1973/twist-j/issues/1030)
**Basis:** Public Canon v87, main `5c9a494de3f4b9856c292a77d35280fb086a0404`, normative content `41c8d4229b71437f09957d959975dc1772e95806`.
**Layer:** NOT_APPLICABLE, analytic number theory; no physical or L1-to-L6 reading.
**Authority:** none. No Canon, Registry, Frontier, evidence, gate, or release change.

## 1. Result and exact boundary

The joined Jacobi energy of #979 need not first be proved bounded in degree
in order to pursue ordinary RH. A proved family of polynomial energy bounds
whose exponents tend to zero would suffice.

More precisely, for the actual energy defined below, the implication is

\[
 A_N(\varepsilon)=O((N+2)^\kappa),\qquad \kappa\ge0
 \quad\Longrightarrow\quad
 M_\varepsilon\text{ is holomorphic on }
 \Re s>\frac12-\frac\varepsilon2+\frac\kappa4.
 \tag{1}
\]

The implied constant may depend on both fixed parameters. Consequently a
nontrivial zeta zero beyond

\[
 \Re\rho>\frac12+\frac\varepsilon2+\frac\kappa4
 \tag{2}
\]

must have the exact complex shadow `rho-epsilon`, with at least the same
multiplicity. A single epsilon still does not remove shadows. For distinct
`epsilon_j -> 0` and `kappa_j -> 0`, bounds of this form for every degree
exclude every zero to the right of the critical line by isolation of zeros.

**No new upper energy bound is proved here.** In particular, neither
`A_N=O(N^(2 epsilon))` nor fixed-epsilon full norm finiteness is established.
This note proves a quantitative implication and weakens the sufficient
estimate sought next. It does not prove RH, locate a zero, or move a
registered claim. The conclusion concerns ordinary RH for `zeta` only.

## 2. Source custody and what is new

The source objects are equations (34)-(41) of
[the mean-channel note at #979](https://github.com/mathorn1973/twist-j/blob/3fbb912d1af00d26c29d624f2182bbfba629bb92/notes/C-RH-MOBIUS-MEAN-CHANNEL-N.md).
Its
[2026-09-16 addendum](https://github.com/mathorn1973/twist-j/blob/3fbb912d1af00d26c29d624f2182bbfba629bb92/notes/C-RH-MOBIUS-MEAN-CHANNEL-N_ADDENDUM-2026-09-16.md)
controls the pole subtraction and the distinction between a single epsilon
and an accumulating family. The same corrections are recorded in
[#1020](https://github.com/mathorn1973/twist-j/pull/1020), source head
`1c2612dc22602f6263d671e7cbdbf1a93630f842`.

The source already has the Jacobi basis, exact power-model coefficient
identities, and the bounded-energy accumulating-epsilon argument. Those are
not claimed as new. The new step is the quantitative passage from a
polynomial bound on the **joined coefficient energy** to the shifted
holomorphy domain in (1), and its vanishing-exponent consequence.

Current issues, the registry, notes, probes and all remote heads were
scanned before the object lock. This note does not take over #978 or #965,
edit their sources, or reuse a probe. No scientific code was executed.

## 3. Actual arithmetic moments and normalization

Fix `0 < epsilon <= 1/4`, put `delta=epsilon/2`, and define for `x>0`

\[
 h_\varepsilon(n)=\sum_{d\mid n}\frac{\mu(d)}{d^\varepsilon}
   =\prod_{p\mid n}(1-p^{-\varepsilon}),\qquad
 H_\varepsilon(m)=\sum_{n\le m}h_\varepsilon(n),\qquad H_\varepsilon(0)=0,
\]
\[
 c_\varepsilon=\zeta(1+\varepsilon)^{-1},\qquad
 F_\varepsilon(x)=c_\varepsilon x-H_\varepsilon(\lfloor x\rfloor),\qquad
 g_\varepsilon(t)=t^{-\delta}F_\varepsilon(1/t).
 \tag{3}
\]

Since `0 <= h_epsilon(n) <= 1` and `0<c_epsilon<1`, the trivial bound
`|F_epsilon(x)| <= 2x` gives

\[
 \int_0^1t|g_\varepsilon(t)|\,dt
 \le 2\int_0^1t^{-\delta}\,dt<\infty.
 \tag{4}
\]

This ensures the individual moments exist without any full square norm
assumption. On `t>1`, `g_epsilon(t)=c_epsilon t^(-1-delta)` and hence its
separate squared norm there is exactly `c_epsilon^2/(1+epsilon)`.

On `(0,1)`, use the real orthonormal basis

\[
 R_n(t)=P_n^{(0,2)}(2t-1)
  =\sum_{k=0}^n(-1)^{n-k}\binom nk\binom{n+k+2}{k+2}t^k,
 \qquad e_n(t)=\sqrt{2n+3}\,tR_n(t).
 \tag{5}
\]

Orthogonality is
`integral_0^1 t^2 R_n(t)R_m(t) dt = 1_(n=m)/(2n+3)`.
Completeness follows because polynomials are dense in `L^2((0,1),t^2 dt)`
and multiplication by `t` maps that space isometrically onto `L^2(0,1)`.

Set

\[
 u_n(\varepsilon)=\int_0^1g_\varepsilon(t)e_n(t)\,dt,
 \qquad A_N(\varepsilon)=\sum_{n=0}^N|u_n(\varepsilon)|^2.
 \tag{6}
\]

In the source notation, `u_n=sqrt(2n+3) a_n` and
`A_N=L_N-c_epsilon^2/(1+epsilon)`. Indeed substitution `x=1/t` gives

\[
 \int_0^1g_\varepsilon(t)t^{k+1}\,dt
 =\frac{c_\varepsilon}{k+1-\delta}
 -\frac{\zeta(k+2-\delta)}{(k+2-\delta)\zeta(k+2+\delta)},
 \tag{7}
\]

the source's actual moment `m_k`. Thus the energy in this note is the
same energy, not a substitute sequence. All the zeta arguments in (7) are
real and greater than one.

For `Re s>1`, direct absolute convergence of the Dirichlet series yields

\[
 \begin{split}
 M_\varepsilon(s)
 &=\int_1^\infty F_\varepsilon(x)x^{-s-1}\,dx
   =\int_0^1g_\varepsilon(t)t^{s+\delta-1}\,dt\\
 &=\frac{c_\varepsilon}{s-1}
   -\frac{\zeta(s)}{s\zeta(s+\varepsilon)}.
 \end{split}
 \tag{8}
\]

The apparent singularity at `s=1` is removable: both displayed terms have
residue `c_epsilon`. The bare quotient without the first term is not the
holomorphic object under discussion.

## 4. Exact power-test coefficients

For a complex variable `alpha` with `Re alpha>-1`, let

\[
 d_n(\alpha)=\int_0^1t^{\alpha-1}e_n(t)\,dt.
\]

The exact formula is

\[
 \boxed{
 d_n(\alpha)=\sqrt{2n+3}\,
 \frac{\prod_{j=2}^{n+1}(\alpha-j)}
      {\prod_{j=1}^{n+1}(\alpha+j)}.
 }
 \tag{9}
\]

For `n=0` the numerator is an empty product. A proof uses Rodrigues' formula

\[
 R_n(t)=\frac1{n!t^2}\frac{d^n}{dt^n}
          \bigl[t^{n+2}(t-1)^n\bigr].
\]

Initially take `Re alpha` large and integrate by parts `n` times.
The resulting beta integral is

\[
 \int_0^1t^\alpha R_n(t)\,dt
 =\frac{\prod_{j=2}^{n+1}(\alpha-j)}{n!}
       \int_0^1t^\alpha(1-t)^n\,dt,
\]

which is (9). Holomorphy of the integral and the rational expression extends
the identity to `Re alpha>-1`.

For sufficiently large `n` on any fixed compact set of alpha values, it may
also be written

\[
 d_n(\alpha)=(-1)^n\sqrt{2n+3}
 \frac{\Gamma(\alpha+1)}{\Gamma(2-\alpha)}
 \frac{\Gamma(n+2-\alpha)}{\Gamma(n+2+\alpha)}.
 \tag{10}
\]

Use (9) at apparent singularities of this gamma expression. In particular,
the rational function is holomorphic throughout the needed region
`Re alpha>1/2`; no claim of global entire dependence is made.
The gamma-ratio estimate gives, locally uniformly there,

\[
 |d_n(\alpha)|\le C_K(n+1)^{1/2-2\Re\alpha}
 \qquad(\alpha\in K).
 \tag{11}
\]

The finitely many small indices can be absorbed into `C_K`. Positive
integral alpha values cause no problem: the relevant coefficients
eventually vanish.

## 5. Growth-to-holomorphy theorem

**candidate-T.** Suppose for fixed `epsilon` and `kappa>=0` that

\[
 A_N(\varepsilon)\le C(N+2)^\kappa\qquad(N\ge0).
 \tag{12}
\]

Then

\[
 \mathcal M_\varepsilon(s)
   =\sum_{n\ge0}u_n(\varepsilon)d_n(s+\delta)
 \tag{13}
\]

converges absolutely and locally uniformly on the half-plane in (1).

**Proof of convergence.** Put `alpha=s+delta`. On a compact set with
`Re alpha>=a>1/2+kappa/4`, apply Cauchy-Schwarz to each block
`B<=n<2B`, where `B=2^b>=1`:

\[
 \begin{split}
 \sum_{n=B}^{2B-1}|u_nd_n(\alpha)|
 &\le
 \left(\sum_{n=B}^{2B-1}|u_n|^2\right)^{1/2}
 \left(\sum_{n=B}^{2B-1}|d_n(\alpha)|^2\right)^{1/2}\\
 &\le C'_K B^{\kappa/2+1-2a}.
 \end{split}
 \tag{14}
\]

The exponent is negative, so summing over powers of two is a convergent
geometric series, uniformly on that compact set. Each summand is
holomorphic. This proves holomorphy of (13). The argument uses the joined
energy (12) before taking an absolute value of the power-test pairing;
it does not replace the underlying signed arithmetic by absolute Mobius
pairs or by a pointwise Mertens envelope.

**Identification with the arithmetic transform.** This step must not
presume `g_epsilon` is in `L^2`. For `Re alpha>2`, the standard Jacobi bound

\[
 \sup_{0\le t\le1}|R_n(t)|\le R_n(0)(-1)^n
   =\frac{(n+1)(n+2)}2
 \tag{15}
\]

and (11) show that
`sum_n d_n(alpha)e_n(t)/t` converges uniformly on `[0,1]`: its terms are
bounded by a constant times `(n+1)^(3-2 Re alpha)`. Orthogonal completeness
identifies the `L^2` expansion `sum_n d_n(alpha)e_n(t)` with
`t^(alpha-1)`; uniform convergence after division by `t` identifies the
same function pointwise on `(0,1]`. By (4), termwise integration against
`g_epsilon` is therefore legitimate and gives

\[
 \sum_{n\ge0}u_nd_n(\alpha)
   =\int_0^1g_\varepsilon(t)t^{\alpha-1}\,dt
   =M_\varepsilon(\alpha-\delta).
 \tag{16}
\]

Take `Re alpha>max(2,1/2+kappa/4)` to overlap the convergence domains.
The zeta expression in (8) is meromorphic, and (13) is holomorphic on
the connected half-plane in (1). The identity theorem gives equality
throughout that half-plane as meromorphic functions; hence any apparent
poles of the zeta expression there are removable. This proves (1).

The expansion is a bilinear analytic pairing, with `d_n` as written in
(9), not its complex conjugate. The basis functions are real. Inserting a
conjugate of the parameter-dependent coefficient would destroy the claimed
holomorphy and is not part of the proof.

**Sharpness check on an auxiliary model.** This is not the arithmetic
`g_epsilon`. Take `g_*(t)=t^(-3/4)` on `(0,1)`, which still satisfies
`integral_0^1 t|g_*|<infinity`. Its coefficients are `u_n^*=d_n(1/4)`.
Formula (10) gives

\[
 u_n^*=(-1)^n\sqrt2\,
       \frac{\Gamma(5/4)}{\Gamma(7/4)}(1+O(n^{-1})),\qquad
 A_N^*\sim 2\frac{\Gamma(5/4)^2}{\Gamma(7/4)^2}N.
\]

Its Mellin pairing is `1/(s+delta-3/4)`, with a pole exactly at
`s=3/4-delta=1/2-delta+1/4`. Thus `kappa=1` reaches exactly the boundary
in (1). The factor `1/4` cannot be decreased in a general inference using
only coefficient-energy growth and the integrability in (4). This
analytical model neither predicts an arithmetic pole nor bounds the actual
energies.

## 6. Exact shadow threshold and quantitative obstruction

Let `rho=beta+i gamma` be a nontrivial zero of multiplicity `m`, and assume
(2). Then `s_0=rho-epsilon` belongs to the holomorphy domain (1).
Nontrivial zeta zeros are nonreal, so `s_0` is neither `0` nor `1`.
The first term of (8) is analytic at `s_0`. The denominator
`zeta(s+epsilon)` has a zero of order `m` there. Therefore holomorphy forces

\[
 \boxed{\operatorname{ord}_{\rho-\varepsilon}\zeta
                  \ge\operatorname{ord}_\rho\zeta.}
 \tag{17}
\]

Order at a nonzero value is zero. No simple-zero assumption is used.
All half-plane inequalities in this note are strict; convergence on the
boundary is not inferred from (14).

Equivalently, one zero lacking a shadow of sufficient multiplicity gives
the growth obstruction

\[
 \boxed{
 \limsup_{N\to\infty}
 \frac{\log(1+A_N(\varepsilon))}{\log(N+2)}
 \ge 4\beta-2-2\varepsilon.
 }
 \tag{18}
\]

If the right side is nonpositive, this says only the trivial nonnegativity
of the limsup. Otherwise, if the limsup were smaller, choose a nonnegative
`kappa` strictly between it and the right side. Enlarging a constant to
cover finitely many initial indices gives (12), and (17) contradicts the
missing shadow. No assertion that an offending zero exists is made.

## 7. Accumulating epsilon with a vanishing growth exponent

**candidate-T, conditional implication.** Let the positive values
`epsilon_j<=1/4` be pairwise distinct, with `epsilon_j -> epsilon_*>=0`.
Suppose `kappa_j>=0`, `kappa_j -> kappa_*>=0`, and for each `j` there exists
a finite constant `C_j` such that

\[
 A_N(\varepsilon_j)\le C_j(N+2)^{\kappa_j}
 \quad\text{for every }N\ge0.
 \tag{19}
\]

Then no nontrivial zero satisfies

\[
 \Re\rho>\frac12+\frac{\varepsilon_*}2+\frac{\kappa_*}4.
 \tag{20}
\]

**Proof.** Such a zero would satisfy (2) for all sufficiently large `j`,
so (17) would force distinct zeros `rho-epsilon_j` converging to the finite
point `rho-epsilon_*`. Zeta is analytic near this nonreal point and is not
identically zero. Its zeros cannot accumulate there. No uniform bound on
the constants `C_j` is needed.

In particular, `epsilon_*=kappa_*=0`, followed by the zeta functional
equation, gives ordinary RH. Thus a concrete sufficient next target is

\[
 \boxed{
 A_N(2^{-j})\le C_j(N+2)^{2^{1-j}}
 \quad(j\ge2,\ N\ge0).
 }
 \tag{21}
\]

This is an **open estimate**, not a result of this note. It allows
polynomial growth in `N` at every fixed epsilon and is less demanding
than requiring uniformly bounded energy there. It does not assert that
the actual full norm diverges, or that (21) is equivalent to RH.

For this illustrative schedule, the individual shadow threshold is
`beta>1/2+epsilon`; only the accumulating family removes shadows.
Any other proved nonnegative exponents tending to zero would serve.

## 8. What the existing finite-degree bound actually reaches

Equation (38) of the source note gives the polynomial exponent

\[
 \kappa_{\rm current}=2-2\varepsilon.
\]

Substituting this exponent into (2) yields exactly

\[
 \frac12+\frac\varepsilon2
      +\frac{2-2\varepsilon}{4}=1.
 \tag{22}
\]

Thus its present power reaches only the already known boundary
`Re rho=1`; it supplies no nontrivial zero exclusion through this theorem.
The factor `exp(-c sqrt(log N))` in the source's stronger branch improves
the bound but does not lower its limiting polynomial exponent. It cannot
by itself be replaced by `N^(-eta)` for any fixed positive `eta`.

A fixed power saving `eta>0` from that exponent would shift the individual
shadow threshold to `beta>1-eta/4`. With an accumulating epsilon family
and that same saving, isolation would give a genuine zero-free region
to the right of this line. No such saving is established here.

The remaining analytic debt is therefore precise: obtain a bound on the
actual joined energies with exponents tending to zero, or a still stronger
bound, without importing a zero-location hypothesis or assuming the bound
one is trying to prove. Constants alone and finite-degree observations do
not fill this gap.

## 9. Imports, review and promotion boundary

Classical inputs, distinguished from the new implication:

- Jacobi orthogonality and normalization, Rodrigues' formula, and the
  standard maximum bound (15) for parameters `(0,2)`; see Szego,
  *Orthogonal Polynomials*, fourth edition, section 4.3 and Theorem 7.32.1, and
  [DLMF 18.3](https://dlmf.nist.gov/18.3),
  [DLMF 18.5(ii)](https://dlmf.nist.gov/18.5#ii),
  [DLMF 18.14.2](https://dlmf.nist.gov/18.14.E2).
- The locally uniform asymptotic for a ratio of gamma functions with fixed
  shifts; [DLMF 5.11(iii)](https://dlmf.nist.gov/5.11#iii).
- Meromorphic continuation of zeta, its sole pole at `1`, the location of
  nontrivial zeros in the critical strip, functional-equation symmetry,
  and isolation of analytic zeros; [DLMF 25.2](https://dlmf.nist.gov/25.2),
  [DLMF 25.4](https://dlmf.nist.gov/25.4),
  [DLMF 25.10](https://dlmf.nist.gov/25.10).

The source's finite computations and exact real-zeta enclosures are not
rerun and are not evidence for (12), (19), or (21). This proof needs no
zero data, decimal arithmetic, numerical experiment, or verifier. Static
mathematical review is not a blind preregistered two-agent confirmation or
a two-architecture computation gate.

Two separate static mathematical reviews checked normalization, the exact
power coefficient, the interchange without an `L^2` assumption, the strict
boundary, multiplicity, and the accumulating-family implication. Neither
identified a remaining mathematical defect. A separate power-model check
is written out in section 5. This review record confers no Canon status.

Promotion package: `PROMO-C-RH-JACOBI-GROWTH-LADDER-N`. Its only proposed
content is the conditional implication (1), shadow consequence (17),
growth obstruction (18), and accumulating-family consequence (20).
They remain candidate-T here. Any promotion requires a separate public
review and ordinary sealed fold; no existing RH row is closed by them.

The exact failure tests for this proof are a wrong normalization in (7)
or (9), an exponent error in (14), an unjustified interchange in (16),
an uncovered singularity in (17), or an invalid accumulation argument.
These are review obligations, not a retrospectively pinned probe.
