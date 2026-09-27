# RESULT - C-PHOTON-DENSE-ONE-HOLE-CURRENT-N

**Verdict:** PASS at the frozen NON-CANONICAL scope.
**Ceiling:** candidate-T written proof; candidate-C finite audit.
**Canon:** unchanged.

For every even \(L\ge4\), the frozen family gives one augmented component
\(K_L\) with

\[
\boxed{
A_{K_L}=\frac52L^4,
\qquad
M_{K_L}=L^4,
\qquad
A_{K_L}/M_{K_L}=5/2.
}
\]

Every \(e_0\)-edge is charged degree five. Every occupied spatial edge is
neutral degree two. Neutral matchings are unique, and the whole face-link graph
is connected.

The current is

\[
j_0(x)=(-1)^{x_1+x_2+x_3},
\qquad
j_1=j_2=j_3=0,
\]

with zero total homology.

For the axial \(01\) slice,

\[
\boxed{B_K(r)=0\quad\forall r,}
\]

hence

\[
\boxed{\ell_K=0.}
\]

Nevertheless the unsigned current-size term used by the \(R_3\) majorant is

\[
\boxed{
M_K^4/(4L^4)=L^{12}/4.
}
\]

Thus the exact bound \(\Xi_L\le R_3(L)/16\) can be arbitrarily loose on
individual exact components. No ensemble divergence statement follows,
because the fixed component also has very small activity

\[
z(K_L)=2^{1-(5/2)L^4}.
\]

The result additionally proves that no universal component support lower bound
\(A_K\ge cM_K\) can hold with \(c>5/2\).

## Route decision

The primary analytical target should retain signed projected-current
cancellation through \(B_K\), \(H_K\), or an equivalent Fourier object.
Current-component size \(M_K\) remains a valid auxiliary bound but is no longer
the preferred infrared variable.

P1 and the photon phase remain open.
