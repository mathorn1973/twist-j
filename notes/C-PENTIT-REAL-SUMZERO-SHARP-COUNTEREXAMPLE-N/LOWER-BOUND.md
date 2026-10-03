# A stronger lower bound on real sum-zero pentit Wigner negativity

**Status:** NON-CANONICAL, candidate-T, action layer L1. This is an exposed
analytic derivation, obtained after reading the existing claims and their
targets. It claims neither blindness nor a program execution. It changes no
Canon row, occurrence contract, or physical interpretation.

## 1. Claim and conventions

Let the indices belong to `F_5`, with addition taken modulo five, and set
`zeta = exp(2 pi i / 5)`. Use the phase-point convention

\[
A_{q,r}|j\rangle=\zeta^{2r(q-j)}|2q-j\rangle,
\qquad
W_\psi(q,r)=\frac15\langle\psi,A_{q,r}\psi\rangle.
\]

Suppose that the state vector has real amplitudes and satisfies

\[
\psi\in\mathbb R^5,\qquad
\sum_{j=0}^4\psi_j=0,\qquad
\sum_{j=0}^4\psi_j^2=1.
\]

For the corresponding pure density operator, define total Wigner negativity
and the negativity confined to the row `r=0` by

\[
\mathcal N(\psi)
 =\sum_{q,r}\max\{0,-W_\psi(q,r)\},
\qquad
\mathcal N_0(\psi)
 =\sum_q\max\{0,-W_\psi(q,0)\}.
\]

Then

\[
\boxed{
\mathcal N(\psi)\ge\mathcal N_0(\psi)
\ge\frac12\tan\frac\pi{10}
=\frac1{2\sqrt{5+2\sqrt5}}.
}
\]

This exceeds the previously proved lower bound `sqrt(5)/20`: the difference
of squared bounds is `(19-8*sqrt(5))/80 > 0`, since `19^2 > 8^2*5`.
No assertion that this is the sharp lower bound on **total** negativity
is made.

## 2. The row as a real cyclic convolution

Define the cyclic convolution

\[
c_t=(\psi*\psi)_t
 =\sum_{j=0}^4\psi_j\psi_{t-j}.
\]

At `r=0`, the phase-point operator sends `|j>` to `|2q-j>`. Reality of
the amplitudes therefore gives

\[
W_\psi(q,0)
 =\frac15\sum_j\psi_j\psi_{2q-j}
 =\frac15c_{2q}.
\]

Multiplication by two permutes `F_5`. Moreover,

\[
\sum_t c_t
 =\sum_j\sum_t\psi_j\psi_{t-j}
 =\left(\sum_j\psi_j\right)^2=0.
\]

Thus the row is a permutation of `c/5`, and has zero sum.

## 3. A fixed Fourier one-norm

Use the unnormalized discrete Fourier transform

\[
\widehat f(k)=\sum_{j=0}^4 f_j\zeta^{-kj}.
\]

The convolution and Parseval identities in this normalization are

\[
\widehat c(k)=\widehat\psi(k)^2,
\qquad
\sum_{k=0}^4|\widehat\psi(k)|^2
 =5\sum_j|\psi_j|^2=5.
\]

Consequently

\[
\sum_{k=0}^4|\widehat c(k)|
 =\sum_{k=0}^4|\widehat\psi(k)^2|
 =\sum_{k=0}^4|\widehat\psi(k)|^2=5.
\]

The sum-zero assumption implies `hat(psi)(0)=hat(c)(0)=0`, so equivalently

\[
\boxed{\sum_{k=1}^4|\widehat c(k)|=5.}
\]

In particular, `c` is not zero. Since it is real and has zero sum, both
its positive and negative parts have the same strictly positive mass.

## 4. Transport decomposition of a real zero-sum vector

Write

\[
c_i^+=\max\{c_i,0\},\qquad
c_i^-=\max\{-c_i,0\},\qquad
p=\sum_i c_i^+=\sum_i c_i^->0.
\]

An explicit transport decomposition is obtained with

\[
t_{ij}=\frac{c_i^+c_j^-}{p}\ge0.
\]

Its row sums, column sums and total mass are

\[
\sum_jt_{ij}=c_i^+,\qquad
\sum_it_{ij}=c_j^-,\qquad
\sum_{i,j}t_{ij}=p.
\]

Therefore, with `e_i` denoting a coordinate basis vector,

\[
\boxed{c=\sum_{i,j}t_{ij}(e_i-e_j).}
\]

Whenever `t_ij>0`, the signs of `c_i` and `c_j` are opposite, so `i != j`.
This is merely a finite-vector decomposition. It is not a dynamics,
probability preparation, or additional physical assumption.

## 5. The pentit Fourier constant

For every nonzero difference `i-j` in `F_5`, multiplication by that
difference permutes `F_5` without zero. Hence

\[
\sum_{k=1}^4
\left|\widehat{(e_i-e_j)}(k)\right|
 =\sum_{k=1}^4|\zeta^{-ki}-\zeta^{-kj}|
 =\sum_{k=1}^4|1-\zeta^k|
 =D.
\]

The constant is independent of the distinct indices. As
`|1-exp(2 pi i k/5)|=2 sin(pi k/5)` for `k=1,...,4`, it equals

\[
D=2\sum_{k=1}^4\sin\frac{k\pi}{5}.
\]

The finite trigonometric sum gives

\[
\sum_{k=1}^4\sin(kx)
 =\frac{\sin(5x/2)\sin(2x)}{\sin(x/2)}.
\]

At `x=pi/5`, its numerator is
`sin(pi/2) sin(2 pi/5)=cos(pi/10)`. Therefore

\[
\boxed{D=2\cot\frac\pi{10}.}
\]

The primality of five is used explicitly in the permutation argument.
No unqualified extension of this identical constant to a composite cyclic
dimension is asserted.

## 6. Conclusion

Apply the triangle inequality to the Fourier transform of the transport
decomposition, then sum over the four nonzero frequencies. The nonnegative
transport coefficients allow the finite sums to be interchanged:

\[
\begin{aligned}
5
 &=\sum_{k=1}^4|\widehat c(k)|\\
 &\le\sum_{i,j}t_{ij}
       \sum_{k=1}^4|\zeta^{-ki}-\zeta^{-kj}|\\
 &=Dp.
\end{aligned}
\]

Thus `p>=5/D`. Because the map `q -> 2q` is a permutation, the negative
mass of the Wigner row is exactly

\[
\mathcal N_0(\psi)=\frac p5\ge\frac1D
 =\frac12\tan\frac\pi{10}.
\]

Total negativity includes that row and possibly additional negative
entries, so `N(psi)>=N_0(psi)`. This proves the claimed bound.

## 7. Assumptions, limits and author self-audit

- **Reality is essential here.** It identifies the row with the ordinary
  self-convolution of a real vector and makes its signed transport
  decomposition applicable. This argument does not apply unchanged to
  complex sum-zero vectors.
- **Normalization fixes the constant five.** Without normalization,
  the Fourier one-norm above is `5 ||psi||^2`; the density operator must
  be normalized before quoting the displayed negativity bound.
- **No division by zero is used.** The Fourier one-norm proves `c != 0`
  before `p>0` and the explicit transport coefficients are introduced.
- **The Fourier conventions are consistent.** Convolution has no
  prefactor, Parseval has a factor five, and Wigner row values have a
  factor `1/5`. Also `|z^2|=|z|^2` for a complex Fourier coefficient.
- **The bound concerns the row and therefore the total.** The inequalities
  do not identify a minimizer for total negativity, nor prove that total
  negativity can attain the displayed constant.
- **The proof has no occurrence premise.** Signed Wigner values are not
  asserted to be a physical distribution or a frequency law. There is no
  claim of an actual outcome selector, preparation mechanism, or native
  renewal.

The author checked these potential failure points analytically and found
no unmet mathematical assumption within the stated normalized real
sum-zero pentit scope. That self-audit is not an independent review.
