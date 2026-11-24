# Sharp numerator caps under a periodic zero mask

**NON-CANONICAL. No authority. Candidate-D paper deduction.** Round 8, C-RH-ARITHMETIC-KERNEL-N, issue #2087, draft #2089. Action layer NOT_APPLICABLE. This is a continuation under the same frozen lane scope. The full Q7 estimate remains **O**. The separate reviewed moving-residue note retains its original hash.

Use `X,R,D,w,G_7,C_z,Q_7,A_r,m_X,Phi_r,K_r` and the signed numerators from [MOVING-RESIDUE-ZEROS](MOVING-RESIDUE-ZEROS.md). In particular `R>=X^(2/3)` is an original shell left endpoint, the shell is `R<r<=min(2R,D)`, `D=4X`, and its actual modes have coefficient `A_r b(r,a)m_X(a/(5r))`. The numerical caps are

\[
 |a|\le\lceil R^3/X^2\rceil,\qquad |a|\le 10r/\sqrt X,
 \qquad X|a|/r<\sqrt X\exp(-\sqrt{\log X}).                    \tag{1}
\]

Here and below all conductor subsets are drawn from the fixed surviving conductors of `G_7`. Changing multiplier treatment only inside a difference leaves those original coefficients in the removal itself.

## 1. The omitted harmonics after periodic multiplication

Let `W_r` be a real `5r`-periodic mask, even under reflection `n` to `-1-n`, with Fourier coefficients `w_r(b)` at signed centered `b/(5r)` satisfying `|w_r(b)|<<1/(1+|b|)` uniformly in `r,X`. Both the robust plateau masks from the moving-residue note and the thinner mask below satisfy these properties. Fix any outer conductor subset `F` in the shell. For one dyadic magnitude `A`, let `L_(r,A)` be the part of `m_X Phi_r` omitted by (1) with `A<=|a|<2A`, taking both signs. The cutoff is even, so `L_(r,A)` has odd reflection. Therefore the product `W_r L_(r,A)` has zero mean on the full period. The only terms at zero in its mode product are `a+b=0`, since `|a|/(5r)<=2/sqrt(X)` and `|b|/(5r)<=1/2`. Delete these resonances after their exact per-conductor cancellation. Define the full box of omitted harmonics under the masks by

\[
       D_A(n)=\sum_{r\in F} A_r W_r(n)L_{r,A}(n).
\]

**Claim.** For the original taper,

\[
 \|D_A\|_w\ll_\epsilon X^\epsilon
       \left(\frac{(X+R^2)R}{A}\right)^{1/2}.                          \tag{2}
\]

To prove it, split by the fixed signed numerator `b` of `W_r`, then by `g=gcd(a+b,r)` and put `e=r/g`. The frequency is `(a+b)/(5r)`. Its reduced denominator is `5e` or `e`, according as `5` does not or does divide `a+b`. The squarefree split `r` is coprime to five, so the two possibilities cannot collide for unequal `e`. At fixed `g,e` there is just one `r`, and as `a` varies throughout the whole dyadic box on the Jackson support the distinct `a` differ by less than `5r`. Consequently no distinct retained coordinates coincide on the circle at this fixed `g`. All their reduced denominators are at most `10R/g`, so distinct frequencies are separated by at least a constant times `g^2/R^2`.

For fixed `b` let `lambda_g` count the two-signed integers `a` in the dyadic box with `a+b!=0` and `g|a+b`, allowing more than the actual cap conditions. There are `O(R/g)` possible `r` in the shell with `g|r` whenever the range is occupied, since `g<=2R`. Each product coefficient has magnitude `O_eps(X^eps/[A(1+|b|)])`, by the uniform bound on `A_r`, `|b(r,a)|<<1/|a|`, and `|m_X|<=1`. Therefore the translated additive large sieve bounds the `g,b` norm by

\[
 \ll_\epsilon \frac{X^\epsilon}{A(1+|b|)}
       \left[\sqrt{XR}\sqrt{\lambda_g/g}
               +R^{3/2}\sqrt{\lambda_g/g^3}\right].                 \tag{3}
\]

For `g<=A`, counting multiples gives `lambda_g<<A/g`. For `g>A`, sum the divisor counts of the nonzero integers `a+b` to obtain `sum_g lambda_g<<_eps A X^eps`. These integers have magnitude `O(X)`, including their endpoints. By Cauchy–Schwarz and harmonic summation,

\[
 \sum_{g>A}\sqrt{\lambda_g/g}\ll_\epsilon X^\epsilon\sqrt A,
 \qquad
 \sum_{g>A}\sqrt{\lambda_g/g^3}\ll_\epsilon X^\epsilon/\sqrt A.
\]

The corresponding sums over `g<=A` are `O(sqrt(A)log(2X))` and `O(sqrt(A))`. Sum (3) first over `g`, then over `|b|=O(X)`. Its harmonic weight costs only another logarithm. Shrinking the intermediate exponent proves (2). The proof bounds the signed product after its constant term cancellation. It allows an arbitrary fixed outer subset `F` and the original conductor-dependent caps.

The dyadic boxes occupied by omitted modes have `A` at least a constant times

\[
 N=\min\{R^3/X^2,\,(R/\sqrt X)\exp(-\sqrt{\log X})\},
\]

with `A>=1`. If `R<=X^(3/4)`, then `N>=(R^3/X^2)exp(-sqrt(log X))`. Summing the decreasing square-root bound (2) over the boxes gives a squared norm `O_eps(X^(2+eps))`, since `X+R^2<<R^2` in this range. For `R>=X^(3/4)` the pointwise sharp-cap discrepancy in the moving-residue note, §5, already gives the same squared bound for an arbitrary moving conductor set and applies when `W_r` is an indicator. Thus the original sharp-capped packet and the whole Jackson-smoothed primitive packet differ, after either specified indicator mask, by `O_eps(X^(2+eps))` in squared norm on every original shell.

Combined with the periodic proper-divisor estimate in the moving-residue note, §7, this removes the sharp-capped zero-state packet on every shell where the largest proper divisor is `O(X^(2/3))`. In particular for each fixed `l>=3` one can choose a fixed `rho>2/3` small enough that `rho(1-1/l)<=2/3`. At `R` of order `X^rho` the whole original sharp-capped packet is removable on the moving zero states for the specified balanced `l`-prime conductors. The same incidence proof applies on that shell, and the shell is polynomially above the ordinary cutoff `X^(2/3)`.

## 2. A common zero window for all actual conductors

Set `D_0=floor(X^(2/3))`. On any original shell and for any fixed outer conductor family `F`, let `W_r(n)` select exactly

\[
       n=5k r+u,\qquad k\in\mathbb Z,\qquad -D_0\le u<D_0.             \tag{4}
\]

There are at most two jumps per period, and reflection `n` to `-1-n` sends `u` to `-1-u`. This mask has all the properties in §1. For any divisor `d|r` with `d>=D_0`, at a selected time one has

\[
 \lfloor n/d\rfloor=5k(r/d)+\lfloor u/d\rfloor,
 \qquad \lfloor u/d\rfloor\in\{-1,0\}.
\]

Both residues make `K_d` zero. Thus the large raw divisors all vanish at once, even if the conductor has a fixed small prime divisor.

Expand the entire primitive kernel exactly as

\[
    \Phi_r=\sum_{d\mid r}\mu(r/d)(d/r)K_d.
\]

For each evaluation time freeze `F_n={r in F: W_r(n)=1}`. In the part with `d>=D_0`, the combined coefficient of each `K_d` is

\[
  c_d(n)=\sum_{\substack{r\in F_n\\d\mid r}}A_r\mu(r/d)(d/r),
     \qquad |c_d(n)|\ll_\epsilon X^\epsilon.
\]

The last assertion uses the crude `A_r` bound and the harmonic sum over `r/d`. The resulting raw polynomial vanishes at its evaluation time by (4). Its successive difference at positive `v` near the taper has magnitude `O_eps(X^eps)`, by `K_d(v)-K_d(v-1)=1_(d|v)chi_5(v/d)` and the divisor bound on `v`. The first absolute moment `O(sqrt(X))` of the original Jackson weights bounds the shifted contribution with `|j|<=X/2` by `O_eps(X^(1/2+eps))`. The full raw sup bound `O_eps(R X^eps)` and the cubic tail handle all farther shifts. After squaring and summing on the taper this costs `O_eps(X^(2+eps))`.

For `d<D_0` write `K_d=sum_(e|d) (e/d) Phi_e`. The new coefficient at each fixed `r,e` before multiplying by `W_r` and including the factor `A_r` is

\[
   \frac e r\sum_{\substack{e\mid d\mid r\\d<D_0}}\mu(r/d),
      \qquad \text{of magnitude } O_\epsilon(X^\epsilon e/r).
\]

The periodic moving-mask estimate in the moving-residue note, §7, applies with `E=D_0`. Its proof only uses a coefficient ceiling `O_eps(X^eps e/r)` at each `r,e` and the even reflection and coefficient decay of `W_r`. Both hold here. In particular the resonance at zero still cancels separately for each `r,e`, since `W_r (m_X Phi_e)` has odd reflection. The resulting squared bound for these small raw divisors is `O_eps(X^eps (XD_0+D_0^3))=O_eps(X^(2+eps))`.

The two parts before the sharp cap together cost `O_eps(X^(2+eps))`. Using §1 pays the original numerical restrictions at the same precision. The result is the unconditional removal bound

\[
 \left\|\sum_{r\in F}W_r(n)
     \sum_{\substack{a\text{ actually retained}\\(a,5r)=1}}
          A_r b(r,a)m_X(a/(5r))e(na/(5r))\right\|_w^2
         \ll_\epsilon X^{2+\epsilon}.                               \tag{5}
\]

This applies to the entire set of actual surviving conductors, shell by shell. There are only `O(log X)` shells, so the norm triangle inequality gives (5) for their combined packet with the same claimed exponent after shrinking the intermediate exponent. It is a statement about the designated short time windows of (4).

For actual examples beyond the largest-proper-divisor criterion, take the shell with largest left endpoint `R<=X/1000`. Choose `r=11p_1p_2p_3` with the three distinct split primes in `[(6R/55)^(1/3),(7R/55)^(1/3)]`. Their products give `R<r<2R`. These three primes are at most `z=D^(1/3)` and above `(log X)^2`. Thus the two round-seven small-prime products both equal 11 and are below the two deletion thresholds eventually. Numerator one is retained and nonzero by the parity argument of the moving-residue note. The largest proper divisor `r/11` has order `X`, beyond the previous proper-divisor ceiling. On this shell each conductor has at least a constant times `X D_0/R` selected times in `[X,2X)`, by the complete-period count. The fixed-modulus prime number theorem and unique factorization give at least a constant times `R/(log X)^3` such conductors, so there are at least a constant times `X^(5/3)/(log X)^3` actual numerator-one incidences, including those with the fixed small prime 11.

## 3. Complete successor and remaining estimate

Let `V` be the exact amplitude in (5), with whichever fixed outer families are selected. The successor quantity is

\[
 Q_{\rm new}=Q_7-2\Re\langle V,G_7+C_z\rangle_w+\|V\|_w^2.
\]

It equals `||G_7-V+C_z||_w^2+O_eps(X^(2+eps))` by the original round-seven comparison. The full prime profile and every cross-interaction in this identity are retained. The norm bound (5) transfers the all-epsilon criterion in both directions. It neither bounds the change of energy by the removal norm squared alone nor asserts the original finite determinant-strip identity for the new time-dependent mask. The original compact balanced expansion with its affine pieces and unit term is connected through the same comparison with `T`.

**O.** The complement of these periodic windows remains in the actual signed amplitude. This paper deduction does not prove the complete `Q_7` target. Read the preceding round-eight moving-residue proof and the inherited original mode and taper data cited there. The fixed-modulus prime-count input is only used to count the examples, with the inherited primary source from that note. No numerical experiments, scientific code, formal checks, or independent review were run for this extension at the time of writing.
