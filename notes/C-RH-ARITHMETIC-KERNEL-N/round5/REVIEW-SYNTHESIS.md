# Final paper review of the round-5 combined reduction

C-RH-ARITHMETIC-KERNEL-N, #2087 / #2089. NON-CANONICAL, no authority. Candidate-D same-session review of the integrated REPORT.md equations (4)–(6) and PREFIX-PANEL-SCOPE.md. No scientific computation or source edits.

**Disposition.** The combined cutoff, determinant criterion and uniform prefix implication follow at their stated scopes. No mathematical gap found in the reviewed steps.

## 1. Combined cut and same-window equivalence

For \(y_X=(\log X)^2\), the smooth-conductor packet has coefficient absolute mass
\[
 O\bigl((1+\log X)^2 W(4X,y_X)\bigr)=O_\eta(X^{1/2+\eta})
\]
for every fixed \(\eta>0\). The estimate applies to an arbitrary restriction of its numerators because it is already absolute. Rankin with any fixed exponent just above \(1/2\) suffices for this threshold. It does not rely on the sharper constant threshold for a strict \(O(\sqrt X)\) bound.

For \(Y_X=\sqrt X\exp(-\sqrt{\log X})\), the inequality \(640k\le Y_X\le10\sqrt X\) holds on all sufficiently large scales. The numerator amplitude bound for the single interval \([Y_X,10\sqrt X]\) is
\[
 O_\eta(X^{1+\eta}/Y_X)
   =O_\eta(X^{1/2+\eta+o(1)}).
\]
With \(\eta\) chosen below the final error exponent before the limit, this gives the claimed tapered square-norm bound. Remove that high-height packet first, then the smooth-conductor subpacket of the remaining low-height spectrum. The new errors and the inherited \(T-G_X\) error combine by the triangle inequality in the tapered square norm, yielding (4). This does not require estimating their mixed inner products against the retained packet. The masks on original support integers and on Fourier conductors are distinct.

On the smaller spectrum, expanding its tapered square norm is still exact. The far-pair and large-gcd omissions were bounded by sums of absolute values and pass to any subset of the original modes. The same-conductor energy bound also passes to a subset because its coefficient-square majorant is nonnegative. The remaining unequal-conductor sum is real by pair exchange. These facts prove (5) including its lower direction \(P_X^\star\ge-O_\epsilon(X^{2+\epsilon})\), which follows from the energy's nonnegativity.

For RH implies (6), the unconditional transfer of the coefficient unit on the half-plane \(\Re s>1/2\), together with the classical implication RH \(\Rightarrow\) the all-epsilon Mertens estimate, bounds \(T\) on the whole taper support. Equations (4) and (5) then bound \((P_X^\star)_+\). Conversely the positive-part bound controls the nonnegative tapered energy in (5). Equation (4) and \(w=1\) on the original dyadic block give \(\sum_{X\le n<2X}|T(n)|^2\ll_\epsilon X^{2+\epsilon}\). Cauchy–Schwarz and dyadic summation make the Mellin integral of \(T\) holomorphic in \(\Re s>1/2\), since a block's absolute sum is \(O_\epsilon(X^{3/2+\epsilon/2})\). The reciprocal \(1/(s\zeta(s)U(s))\) then supplies the zeta-only zero exclusion. This argument neither supplies a difference estimate for two pair sums nor needs one.

The numerator-one positive panel persists. On \(3X<r\le4X\) its heights are at most \(1/3\), far below \(Y_X\). The deleted conductor absolute mass is \(O_\eta(X^{1/2+\eta})=o(X)\) for fixed \(\eta<1/2\), so the retained panel still has absolute mass \(\asymp X\). The same-sign lower bound and the diagonal subtraction therefore continue to apply to that fixed panel.

## 2. Uniform initial intervals of the first harmonic

For \(2X<r\le4X\), the mode \(a=1\) satisfies both inherited cutoffs and \(A_r=s(r)\). The far-pair and high-gcd absolute estimates remain valid for every endpoint \(u\) of the prefix \(2X<r\le u\). The within-conductor part of this one-mode panel is diagonal. Thus the tapered squared norm of \(B_u\) differs from \(P(X,u)\) by \(O_\epsilon(X^{2+\epsilon})\), uniformly in \(u\).

For \(\sigma\ge1/2\) the error is within the requested scale \(X^{1+2\sigma+\epsilon}\). Averaging over the original block and applying Cauchy–Schwarz therefore gives the uniform weighted prefix bound with weight \(C_X(r)\). Its phase average has strictly positive real part uniformly because \(n/(5r)\in[1/20,1/5]\) on this block. The other factors in \(c_X(r)\) have modulus uniformly bounded below and total variation \(O(1)\), by the removable singularity at \(1/r=0\) and the Lipschitz multiplier profile. This proves the lower modulus and bounded variation for \(C_X\); the lower modulus gives the bounded variation of its reciprocal. Summation by parts applies to every prefix with the same fixed \(C_X\) and recovers \(S(u)-S(2X)\). Dyadic intervals \((2X,4X]\) are consecutive, so geometric summation yields the global all-epsilon bound for \(S\). In the reverse direction the global bound for \(S\) gives uniform partial sums on every prefix. Multiplication by \(c_X(r){\rm e}(n/(5r))\) costs bounded variation uniformly throughout the taper support. The tapered energy and the same absolute deletion bound prove the converse.

Finally the global estimate on \(S\) makes its step-function Mellin transform holomorphic in \(\Re s>\sigma\). The Euler identity equals \(1/[\zeta(s)L(s,\chi_5)U(s)]\) there by meromorphic continuation. The unit is nonzero in this region. At every possible zero of either factor other than \(s=1\), the other factor is holomorphic, so simultaneous zeros increase the pole order. At \(s=1\), \(L(1,\chi_5)>0\). Thus the uniform prefix requirement yields both zero exclusions. One fixed endpoint panel does not give the uniform prefixes needed for this argument. No independence between the two zero statements has been asserted.
