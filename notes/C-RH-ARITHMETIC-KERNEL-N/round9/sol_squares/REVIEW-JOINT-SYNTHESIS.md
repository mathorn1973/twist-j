# Opposition on the common use of the logarithmic cutoff and the two squares

C-RH-ARITHMETIC-KERNEL-N, issue #2087 and draft #2089, round 9. **NON-CANONICAL. No authority. Candidate-D paper review.** Action layer NOT_APPLICABLE. The complete \(Q_7\) and \(Q_8\) bounds remain **O**.

## Compatible use of the two transfers

Write \(h_y(1)=1\), and for \(d>1\) use the nonnegative coefficients of the Euler completion in ROUGH-COMPLETION-AND-CRITICAL-THRESHOLD. With \(y=\log X\), its remaining rough sum satisfies the exact identity
\[
 A_X(n)=\sum_{d\le n}h_y(d)T(\lfloor n/d\rfloor)-T_y(n).
\]
The \(h_y\) coefficients are distinct from the harmonic moment \(h(a)\) of the padded short factor. For each dyadic block \(Y\) take the padded cut \(A=\lfloor Y^{2/15}\rfloor\) from LONGER-FACTOR-CUT, with its same actual inverse \(f\). Define \(Z(u)\) for \(u\ge1\) by the signed profile at the integer \(\lfloor u\rfloor\) on its own central dyadic block \(Y\):
\[
 Z(u)=\mathcal L_{b_Y}(\lfloor u\rfloor)
   -\lfloor u\rfloor U(1)h(a_Y)^2-\mathcal S_{b_Y}(\lfloor u\rfloor).
\]
Set \(Z=T\) below any finite initial scale needed for the proved estimates. Then \(|T(u)-Z(u)|\ll\sqrt u\) uniformly for \(u\ge1\). This choice allows the factor cutoff to reset at each smaller argument and retains the complete oriented sum there.

For any fixed \(\sigma>1/2\), the exact Euler factors in ROUGH-COMPLETION-AND-CRITICAL-THRESHOLD give the uniform finite upper bound
\[
 \sum_{d\ge1}h_y(d)d^{-\sigma}=1+O_\sigma(y^{1-2\sigma}),
\]
since every nonconstant local coefficient starts at exponent two. Hence, on the full original taper,
\[
 A_X(n)=\sum_{d\le n}h_y(d)Z(n/d)-T_y(n)+O_\sigma(X^\sigma).
\]
Indeed \(n/d\ge1\) in the whole sum, so \(\sqrt{n/d}\le(n/d)^\sigma\). The squared taper error is \(O_\sigma(X^{1+2\sigma})\). Each weight is nonnegative and each dilation therefore keeps both negative squares in the expression. The unit is uniformly bounded at every fixed exponent \(\sigma>1/2\), with no strict critical-norm assertion for \(y=\log X\). Since \(T_y(n)\ll_\eta X^\eta\) for every fixed \(\eta>0\), it may also be paid at the required norm precision. This combines the two transfers by using the original inverse \(f\) and its proved mean throughout. Refactoring the inverse of the completed coefficient sequence and transferring that mean below \(\Re s=1/2\) would require a separate proof.

The composition yields no signed estimate for the displayed sum. The mixed terms include all \(d,d'\) and the actual linear and square terms on both lower blocks. The separate log-share obstruction also survives inspection. The modified cube-root single-prime sum cancels to every fixed inverse-log order, while the distinct pair term contributes \(+\kappa n/2\) before its division by \((\log n)^2\). With the unchanged true smooth prefix this leaves coefficient \(-\kappa\log 2\) at \(n/(\log n)^2\). This forbids that uncorrected prescription only, and supplies no bound for \(A_X\).

## Scope of the square-omission obstruction on complete windows

The signed-window lemma applied to \(T\) in SQUARE-RETENTION supplies an integer \(n_0\) with \(T(n_0)>0\) between \(\lfloor Y^{5/4}\rfloor\) and \(Y^{3/2}\) for every sufficiently large \(Y\). Use logarithmic ratio \(6/5\) in that lemma and floor its argument. The central dyadic block of \(n_0\) lies entirely inside \([Y,Y^2)\) at late \(Y\). The overlap-omission lower bound there is at least \(X^{3-6\alpha}\) with weight one. Multiplying by the complete-window weight \(1/[n(n+1)]\asymp X^{-2}\) therefore gives a lower bound \(\gg Y^{(5/4)(1-6\alpha)}\) for every sufficiently late original window, for \(0<\alpha<1/6\). The same conclusion applies to affine omission at the separately specified nearby strict cutoff. At the original strict cutoff the lower exponent is \(5/7\).

The overlap obstruction also applies to the padded cut. Since \(T(v)=o(v)\) by the inherited unconditional estimate, partial summation gives \(\sum_{m\le A}t(m)m^{-1/3}=o(A^{2/3})\). Therefore \(\lambda_X=o(1)\). For \(A<m\le2A\) with \(5\nmid m\), the actual increment of the padded long prefix has magnitude \(|t(m)-\lambda_X|\ge1/2\) eventually. At least one endpoint thus has prefix magnitude at least \(1/4\), and an endpoint counts at most twice. The floor bins in SQUARE-RETENTION then give \(\mathcal S_{b_X}(n)\gg X/A^2\), uniformly on the taper, also for \(A=\lfloor X^{2/15}\rfloor\). With the \(O(\sqrt X)\) reconstruction error the previous positive-time argument gives \(X^{11/5}\) unweighted, and \(\gg Y^{1/4}\) after the complete-window weights. These lower bounds apply to deleting the overlap square from the actual padded \(T\) profile. They do not assert the same positive-part lower bound after the additional signed rough convolution.

Read ROUGH-COMPLETION-AND-CRITICAL-THRESHOLD, LOG-SHARE-OBSTRUCTION, SQUARE-RETENTION, and LONGER-FACTOR-CUT at their frozen round-nine paper scope. The transfer and the complete-window obstruction checks use only those stated inputs. No numerical or symbolic scientific execution, formal check, or repository edit.
