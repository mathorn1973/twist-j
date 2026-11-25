# Round 7 scope, compact balanced spectrum

C-RH-ARITHMETIC-KERNEL-N, issue #2087 / draft #2089, team session. NON-CANONICAL. No authority. Preregistration. Intended status candidate-D or O. Paper work only.

- Use pinned candidate head 4e098f9742a72a128bfb61a10c429bced78fe17e and neighbor #2093 head eac05e3cde56d0fb3e429b91aa7129087e5da4db. Use the actual \(t=\mu*v\), its padded balance, and its signed cubic unit correction. Retain the round-6 window and finite-taper quantifiers.
- Investigate smooth localization of the raw denominators of the actual balanced sum. Any discarded affine part must be allocated to the same raw coefficients. Test whether an exact removal above the slab and a quantitative spectral reduction are compatible with this joint allocation.
- Investigate quantitative cancellation in the smooth slow frequency band via two prefix sums of the actual \(t\) and the signed unit on a complementary range of unit factors. Compare the result with the inherited unconditional exponent and with the requested \(X^{2+\epsilon}\) squared norm. Keep the affine contribution and cubic unit correction in the carrier unless a two-sided error estimate controls their deletion.
- The two carriers approximate the same time sequence. Any comparison with \(G_{\rm core}+C_z\) must be through a proved norm on the original taper. A frequency identity, term-by-term pairing, RH hypothesis, or new computational evidence is outside this scope.
- Check endpoints, convolution support, coefficient bounds after the raw mask, large unit factors, and cross terms under all original quantifiers. The proposed argument fails if a needed smooth cut changes a nonzero floor without a controlled signed error.
