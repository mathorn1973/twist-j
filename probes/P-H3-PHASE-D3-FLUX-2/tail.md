# Infinite-lattice monopole and its first directional correction

Use the same registered scalar \(D_3\) stencil as [the finite tests](shell.md), now on the infinite even-sum lattice with a unit counting-measure point source and a potential vanishing at infinity. Let \(R=|x|,\ n=x/R\). The Fourier integral selects the decaying Green function
\[
G(x)=\frac{2}{(2\pi)^3}\int_{\mathbb R^3/\Gamma_{D_3}}e^{ik\cdot x}\,s(k)^{-1}\,d^3k .
\]
The factor 2 is the primitive cell volume. The symbol has one quadratic zero on this reciprocal torus; \(s^{-1}\) is locally integrable in dimension three, and multiplication by \(s\) verifies \(A G=\delta_0\) by character orthogonality. The integral vanishes at infinity by the Riemann-Lebesgue lemma. The maximum principle on the connected positive-weight graph gives uniqueness among decaying solutions.

**Candidate asymptotic.** Uniformly in lattice direction,
\[
G(x)=\frac{1}{2\pi R}\left(1+\frac{c(n)}{R^4}+O(R^{-6})\right),\quad
c(n)=-\frac1{648}\sum_v w_v [u^6]\sqrt{1+2(n\cdot v)u+|v|^2u^2}.
\]
This is an infinite-volume conclusion with a specified scalar carrier and source weight. It cannot be inferred by fitting the two finite cubes.

**Derivation.** Put \(K=|k|\), \(a=11/27\), \(P_6(k)=\sum_v w_v(v\cdot k)^6/(324\cdot720)\). The cosine expansion and the exact second and fourth moment tensors give
\(s=K^2-aK^4+P_6+O(K^8)\). Thus
\(s^{-1}=K^{-2}+a+a^2K^2-P_6/K^4+E(k)\).
On rescaled annuli \(k=h\xi,\ 1/2<|\xi|<2\), analytic Taylor expansion and a uniformly nonzero leading denominator give \(|\partial^\beta E|\le C_\beta K^{4-|\beta|}\) near zero. Split off a smooth cutoff in a Euclidean chart about zero. The complement on the torus has rapidly decaying Fourier coefficients. The localized polynomial terms also decay rapidly. On dyadic annuli the remaining amplitudes of order four have Fourier bounds \(C2^{-7j}(1+R2^{-j})^{-8}\) by volume scaling and eight integrations by parts; summing gives \(O(R^{-7})\).

In the inverse transform normalized by \((2\pi)^{-3}\) in Euclidean space, \(K^{-2}\) gives \(1/(4\pi R)\), by the unit flux of the Laplace fundamental solution. A biharmonic extension of \(K^{-4}\) gives \(-R/(8\pi)\) because \(\Delta R=2/R\) and \(-\Delta(1/(4\pi R))=\delta_0\). Taking six derivatives eliminates the low-order origin-extension ambiguity (choose the homogeneous extension); multiplying by \(P_6\) gives the locally integrable degree-two symbol \(P_6/K^4\). Differences from the smooth localization away from zero contribute rapid decay at large \(R\) by repeated integration by parts. The sixth-order Fourier sign and lattice covolume then give the absolute correction \(-P_6(\partial)|x|/(4\pi)\). Evaluating the directional derivatives of \(|x|\) gives the displayed formula for \(c(n)\). The proof uses the actual reciprocal quotient rather than double-counting equivalent zero characters in a cubic reciprocal cell.

The pointwise half-first-moment current is \(\mathcal E(x)=\tfrac12\sum_v v\,w_v[G(x)-G(x+v)]/324\). Its leading term is \(x/(2\pi R^3)\), with error \(O(R^{-6})\): signed displacement pairs cancel even Taylor orders, the second moment yields \(-\nabla G_0\) for \(G_0=1/(2\pi R)\), the fourth moment contracts to a multiple of \(\nabla\Delta G_0=0\), and the fifth derivatives of \(G_0\) and first differences of the displayed correction are of order \(R^{-6}\). Normalizing this current per Euclidean cell volume divides by two. Neither this local moment nor flux divided by \(4\pi R^2\) is the exact graph-cut sum. A point source remains at its location throughout this *static* problem.

Freeze the distinct unit directions \(e_1\) and \((2,2,1)/3\), with common allowed radii \(R=6m\), \(m\ge1\). Compute \(c(n)\) by the square-root recurrence and independently by the polynomial \(16[u^6]=b^3-15h^2b^2+35h^4 b-21h^6\) for \(b=|v|^2,\ h=n\cdot v\). Check each moment and that the directional coefficients differ. A mismatch of the asymptotic expression or equality of the specified directional coefficients would falsify the respective claim. This analysis concerns the unbounded \(D_3\) Green function; no charged H3 source, physical electric field or dynamic source law was assumed.
